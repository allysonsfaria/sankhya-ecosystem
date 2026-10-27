"""Extrai as páginas de um site de help/documentação para Markdown, prontas para RAG, sem passar conteúdo por IA.

Help Center Zendesk (ex.: ajuda.sankhya.com.br) é detectado e lido pela API pública: rápido e exato.
Qualquer outro site: páginas do sitemap.xml (ou varredura de links), HTTP simples e, quando a página é
bloqueada ou montada por JavaScript, o Chrome/Edge instalado.
Execuções seguintes só regravam o que mudou.

Uso:
    python extrator_help.py                                   # Help Sankhya
    python extrator_help.py --base https://site.com/docs      # qualquer site
    python extrator_help.py --base https://site.com/docs --limite 20
"""
import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from conversao import converter_corpo
from fontes import Buscador, FonteGenerica, FonteZendesk, Pagina, criar_slug, eh_zendesk, raiz_do_site, registrar

BASE_PADRAO = "https://ajuda.sankhya.com.br"
LOCALE_PADRAO = "pt-br"
PASTA_SAIDAS = Path(__file__).resolve().parent.parent / "saida_help"
ARQUIVO_ESTADO = "_estado.json"
ARQUIVO_RELATORIO = "_relatorio.json"
ARQUIVO_TRAVA = ".trava"
MAX_PAGINAS_PADRAO = 10_000  # teto da varredura genérica: protege contra sites com páginas infinitas
INTERVALO_PADRAO_S = 0.5     # pausa entre páginas de sites genéricos, para não sobrecarregar o servidor
PAGINAS_POR_PROGRESSO = 100


# ---------- arquivos ----------

def pasta_saida_do_site(base: str) -> Path:
    # Se a URL estiver configurada em fontes.json com pasta específica, usa ela
    for cand in (Path(__file__).resolve().parent.parent / "fontes.json", Path(__file__).resolve().parent / "fontes.json"):
        if cand.exists():
            try:
                fontes = json.loads(cand.read_text(encoding="utf-8"))
                base_norm = base.rstrip("/").lower()
                for f in fontes:
                    if f.get("url", "").rstrip("/").lower() == base_norm and f.get("pasta"):
                        return PASTA_SAIDAS / f["pasta"]
            except Exception:
                pass
    return PASTA_SAIDAS / criar_slug(raiz_do_site(base).split("://", 1)[1])


def gravar_atomico(caminho: Path, conteudo: str):
    """Grava em arquivo temporário e renomeia: interrupção nunca deixa arquivo pela metade."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = caminho.with_name(caminho.name + ".tmp")
    temporario.write_text(conteudo, encoding="utf-8", newline="\n")
    os.replace(temporario, caminho)


def ler_json(caminho: Path, padrao: dict) -> dict:
    return json.loads(caminho.read_text(encoding="utf-8")) if caminho.exists() else padrao


def gravar_json(caminho: Path, dados: dict):
    gravar_atomico(caminho, json.dumps(dados, ensure_ascii=False, indent=1))


def adquirir_trava(pasta: Path):
    """Trava do sistema operacional: liberada sozinha se o processo morrer. Retorna None se já houver outra execução."""
    pasta.mkdir(parents=True, exist_ok=True)
    arquivo = open(pasta / ARQUIVO_TRAVA, "a+")
    try:
        if os.name == "nt":
            import msvcrt
            arquivo.seek(0)
            msvcrt.locking(arquivo.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(arquivo, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        arquivo.close()
        return None
    return arquivo


def montar_markdown(pagina: Pagina, corpo: str) -> str:
    cabecalho = {"id": pagina.chave, "titulo": pagina.titulo, "url": pagina.url, "trilha": " > ".join(pagina.trilha),
                 "atualizado_em": pagina.versao, "rotulos": pagina.rotulos}
    linhas = [f"{chave}: {json.dumps(valor, ensure_ascii=False)}" for chave, valor in cabecalho.items() if valor]
    tem_titulo_proprio = re.search(r"^# ", corpo, re.MULTILINE)
    titulo = "" if tem_titulo_proprio or not pagina.titulo else f"# {pagina.titulo}\n\n"
    return "---\n" + "\n".join(linhas) + f"\n---\n\n{titulo}{corpo}"


# ---------- execução ----------

class Extracao:
    def __init__(self, fonte, pasta: Path, forcar: bool, limite: int | None):
        self.fonte, self.pasta, self.forcar, self.limite = fonte, pasta, forcar, limite
        self.estado = ler_json(pasta / ARQUIVO_ESTADO, {"paginas": {}})
        self.vistos: set[str] = set()
        self.relatorio = {
            "status": "executando", "inicio": agora(), "fim": None, "total_previsto": None,
            "contadores": {"novos": 0, "atualizados": 0, "inalterados": 0, "removidos": 0, "ignorados": 0, "erros": 0},
            "erros": [], "ignorados": [],
        }

    def obter_estado_anterior(self, chave: str) -> dict | None:
        return self.estado["paginas"].get(chave)

    def executar(self) -> int:
        self.salvar_progresso()
        self.relatorio["total_previsto"] = self.fonte.total()
        for pagina in self.fonte.paginas(self.ja_atualizada, self.obter_estado_anterior):
            if self.limite is not None and len(self.vistos) >= self.limite:
                return self.finalizar(completa=False)
            self.processar(pagina)
            if len(self.vistos) % PAGINAS_POR_PROGRESSO == 0:
                self.salvar_progresso()
                registrar(f"{len(self.vistos)}/{self.relatorio['total_previsto'] or '?'} | {self.relatorio['contadores']}")
        return self.finalizar(completa=True)

    def ja_atualizada(self, chave: str, versao: str | None) -> bool:
        anterior = self.estado["paginas"].get(chave)
        return (not self.forcar and versao is not None and anterior is not None and anterior.get("versao") == versao
                and (self.pasta / anterior["arquivo"]).exists())

    def processar(self, pagina: Pagina):
        self.vistos.add(pagina.chave)
        if pagina.erro or pagina.ignorada:
            self.registrar_problema(pagina)
            return

        anterior = self.estado["paginas"].get(pagina.chave)
        arquivo_existe = anterior and (self.pasta / anterior.get("arquivo", "")).exists()

        if pagina.nao_modificado and arquivo_existe:
            self.relatorio["contadores"]["inalterados"] += 1
            return

        nada_baixado = pagina.html is None and pagina.markdown is None
        if (nada_baixado or self.ja_atualizada(pagina.chave, pagina.versao)) and arquivo_existe:
            self.relatorio["contadores"]["inalterados"] += 1
            return

        try:
            self.gravar(pagina)
        except Exception as erro:  # uma página com problema não pode derrubar as outras milhares
            pagina.erro = repr(erro)
            self.registrar_problema(pagina)

    def gravar(self, pagina: Pagina):
        corpo = pagina.markdown if pagina.markdown is not None else converter_corpo(pagina.html, pagina.url)
        resumo = hashlib.sha1(corpo.encode()).hexdigest()
        relativo = f"{pagina.pasta}/{pagina.nome}.md"
        anterior = self.estado["paginas"].get(pagina.chave)

        dados_estado = {
            "versao": pagina.versao,
            "hash": resumo,
            "arquivo": relativo,
            "etag": pagina.etag or (anterior.get("etag") if anterior else None),
            "last_modified": pagina.ultimo_modificado or (anterior.get("last_modified") if anterior else None),
        }

        if (not self.forcar and anterior and anterior.get("hash") == resumo and anterior.get("arquivo") == relativo
                and (self.pasta / relativo).exists()):
            self.estado["paginas"][pagina.chave] = dados_estado
            self.relatorio["contadores"]["inalterados"] += 1
            return

        gravar_atomico(self.pasta / relativo, montar_markdown(pagina, corpo))
        if anterior and anterior.get("arquivo") != relativo:
            (self.pasta / anterior["arquivo"]).unlink(missing_ok=True)
        self.estado["paginas"][pagina.chave] = dados_estado
        self.relatorio["contadores"]["atualizados" if anterior else "novos"] += 1

    def registrar_problema(self, pagina: Pagina):
        tipo = "erros" if pagina.erro else "ignorados"
        self.relatorio["contadores"][tipo] += 1
        self.relatorio[tipo].append({"id": pagina.chave, "url": pagina.url, "motivo": pagina.erro or pagina.ignorada})

    def remover_obsoletos(self):
        """Só após leitura completa: página que sumiu da origem sai também do disco."""
        for chave in set(self.estado["paginas"]) - self.vistos:
            (self.pasta / self.estado["paginas"].pop(chave)["arquivo"]).unlink(missing_ok=True)
            self.relatorio["contadores"]["removidos"] += 1

    def finalizar(self, completa: bool) -> int:
        if completa:
            self.remover_obsoletos()
        self.relatorio.update(status="concluido" if completa else "concluido_parcial", fim=agora())
        self.salvar_progresso()
        registrar(f"Fim: {self.relatorio['contadores']}")
        return 1 if self.relatorio["contadores"]["erros"] else 0

    def salvar_progresso(self):
        gravar_json(self.pasta / ARQUIVO_ESTADO, self.estado)
        gravar_json(self.pasta / ARQUIVO_RELATORIO, self.relatorio)


def agora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def ler_argumentos():
    parser = argparse.ArgumentParser(description="Extrai páginas de um site de help/documentação para Markdown.")
    parser.add_argument("--base", default=BASE_PADRAO, help=f"URL inicial; só páginas abaixo dela (padrão: {BASE_PADRAO})")
    parser.add_argument("--modo", choices=["auto", "zendesk", "generico"], default="auto",
                        help="auto detecta Help Center Zendesk; generico força a leitura das páginas HTML")
    parser.add_argument("--locale", default=LOCALE_PADRAO, help=f"idioma no Zendesk (padrão: {LOCALE_PADRAO})")
    parser.add_argument("--seletor", help="seletor CSS do conteúdo principal (genérico), ex.: 'div.article-body'")
    parser.add_argument("--max-paginas", type=int, default=MAX_PAGINAS_PADRAO, help="teto de páginas (genérico)")
    parser.add_argument("--intervalo", type=float, default=INTERVALO_PADRAO_S, help="segundos entre páginas (genérico)")
    parser.add_argument("--saida", type=Path, help="pasta de saída (padrão: saida_help/<site>)")
    parser.add_argument("--forcar", action="store_true", help="regrava tudo, mesmo o que não mudou")
    parser.add_argument("--limite", type=int, help="processa só N páginas (teste); não remove obsoletos")
    return parser.parse_args()


def criar_fonte(argumentos, buscador: Buscador):
    zendesk = argumentos.modo == "zendesk" or (argumentos.modo == "auto" and eh_zendesk(argumentos.base, argumentos.locale))
    registrar(f"Modo: {'Zendesk (API)' if zendesk else 'genérico'} | {argumentos.base}")
    if zendesk:
        return FonteZendesk(argumentos.base, argumentos.locale)
    return FonteGenerica(argumentos.base, buscador, argumentos.seletor, argumentos.max_paginas)


def executar(argumentos, pasta: Path) -> int:
    buscador = Buscador(argumentos.intervalo)
    extracao = None
    try:
        extracao = Extracao(criar_fonte(argumentos, buscador), pasta, argumentos.forcar, argumentos.limite)
        return extracao.executar()
    except BaseException as erro:
        relatorio = extracao.relatorio if extracao else {"status": None, "inicio": agora(), "contadores": {}}
        relatorio.update(status="falhou", fim=agora(), erro_fatal=repr(erro))
        gravar_json(pasta / ARQUIVO_RELATORIO, relatorio)
        if extracao:
            gravar_json(pasta / ARQUIVO_ESTADO, extracao.estado)
        raise
    finally:
        buscador.fechar()


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # console Windows (cp1252) quebra com emoji
    argumentos = ler_argumentos()
    pasta = argumentos.saida or pasta_saida_do_site(argumentos.base)
    trava = adquirir_trava(pasta)
    if trava is None:
        registrar(f"Já existe uma extração em execução em {pasta}. Nada feito.")
        return 2
    try:
        return executar(argumentos, pasta)
    finally:
        trava.close()


if __name__ == "__main__":
    sys.exit(main())
