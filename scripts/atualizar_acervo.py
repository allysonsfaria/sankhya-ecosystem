#!/usr/bin/env python3
"""
atualizar_acervo.py - Sincronização e Atualização do Acervo Sankhya.
Configurável via fontes.json e aceita URLs avulsas pela linha de comando.
Executa extração incremental (apenas o que mudou) e reconstrói os catálogos de busca.
"""
import sys
import os
import json
import argparse
import subprocess
from pathlib import Path
from urllib.parse import urlparse

def slug_url(url: str) -> str:
    """Gera nome de pasta padronizado para uma URL."""
    dominio = urlparse(url).netloc or urlparse(url).path
    return dominio.replace(".", "-").replace(":", "-").lower()

def obter_executavel_python() -> str:
    """Detecta o interpretador Python com as dependências instaladas (bs4, playwright)."""
    try:
        import bs4  # noqa: F401
        return sys.executable
    except ImportError:
        pass
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    candidatos = [
        skill_dir.parent / "GIT" / ".venv" / "Scripts" / "python.exe",
        skill_dir / ".venv" / "Scripts" / "python.exe",
        Path.home() / ".venv" / "Scripts" / "python.exe",
    ]
    for c in candidatos:
        if c.exists():
            return str(c)
    return sys.executable

def carregar_fontes(caminho_json: Path) -> list:
    if caminho_json.exists():
        try:
            with open(caminho_json, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[AVISO] Erro ao ler fontes.json: {e}")
    # Fontes padrão fallback
    return [
        {
            "nome": "Ajuda Sankhya",
            "url": "https://ajuda.sankhya.com.br",
            "pasta": "ajuda-sankhya-com-br",
            "ativo": True
        },
        {
            "nome": "Portal do Desenvolvedor",
            "url": "https://developer.sankhya.com.br",
            "pasta": "developer-sankhya-com-br",
            "ativo": True
        },
        {
            "nome": "Sankhya Design System",
            "url": "https://gilded-nasturtium-6b64dd.netlify.app",
            "pasta": "sankhya-design-system",
            "ativo": True
        }
    ]

def salvar_fontes(caminho_json: Path, fontes: list):
    try:
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(fontes, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[AVISO] Falha ao salvar fontes.json: {e}")

def atualizar(url_especifica=None, nome_especifico=None, pasta_especifica=None, forcar=False, adicionar=False):
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    extractor_dir = skill_dir / "extractor"
    extrator_py = extractor_dir / "extrator_help.py"
    saida_help = skill_dir / "saida_help"
    catalogo_py = script_dir / "gerar_catalogo.py"
    fontes_json = skill_dir / "fontes.json"

    if not extrator_py.exists():
        print(f"[ERRO] Extrator não encontrado em: {extrator_py}")
        sys.exit(1)

    lista_fontes = carregar_fontes(fontes_json)

    # Se o usuário passou uma URL avulsa no comando
    if url_especifica:
        pasta = pasta_especifica or slug_url(url_especifica)
        nome = nome_especifico or url_especifica
        fontes_a_processar = [{
            "nome": nome,
            "url": url_especifica,
            "pasta": pasta,
            "ativo": True
        }]
        
        if adicionar:
            # Verifica se já existe na lista
            existente = next((f for f in lista_fontes if f["url"].rstrip("/") == url_especifica.rstrip("/")), None)
            if not existente:
                lista_fontes.append(fontes_a_processar[0])
                salvar_fontes(fontes_json, lista_fontes)
                print(f"[OK] Nova fonte adicionada permanentemente a fontes.json: {url_especifica}")
    else:
        fontes_a_processar = [f for f in lista_fontes if f.get("ativo", True)]

    print(f"=== Iniciando atualização de {len(fontes_a_processar)} fonte(s) ===")

    py_bin = obter_executavel_python()
    for idx, fonte in enumerate(fontes_a_processar, 1):
        nome = fonte.get("nome", fonte["url"])
        url = fonte["url"]
        pasta = fonte.get("pasta") or slug_url(url)
        destino = saida_help / pasta

        print(f"\n[{idx}/{len(fontes_a_processar)}] Atualizando: {nome} ({url})")
        cmd = [
            py_bin,
            str(extrator_py),
            "--base", url,
            "--saida", str(destino)
        ]
        if forcar:
            cmd.append("--forcar")

        res = subprocess.run(cmd)
        if res.returncode != 0:
            print(f"[AVISO] Extração de '{nome}' finalizou com código {res.returncode}")

    print("\n=== Reconstruindo catálogos indexados de busca ===")
    cmd_cat = [
        py_bin,
        str(catalogo_py),
        str(saida_help),
        str(script_dir)
    ]
    res_cat = subprocess.run(cmd_cat)

    print("\n=== Sincronizando com as IAs instaladas (Claude, Codex, AGY) ===")
    user_home = Path.home()
    destinos = [
        user_home / ".claude" / "skills" / "sankhya-ecosystem",
        user_home / ".codex" / "skills" / "sankhya-ecosystem",
        user_home / ".gemini" / "config" / "skills" / "sankhya-ecosystem",
    ]

    for dest in destinos:
        if dest.exists() and dest.resolve() != skill_dir.resolve():
            try:
                if os.name == "nt":
                    subprocess.run(["robocopy", str(skill_dir), str(dest), "/E", "/NFL", "/NDL", "/NJH", "/NJS"], capture_output=True)
                print(f"[OK] Sincronizado com: {dest}")
            except Exception as e:
                print(f"[AVISO] Falha ao sincronizar com {dest}: {e}")

    if res_cat.returncode == 0:
        print("\n[OK] Atualizacao, reindexacao e sincronizacao concluidas com sucesso!")
    else:
        print("\n[ERRO] Falha ao reconstruir catalogo de busca.")

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Atualiza acervo do Sankhya Ecosystem de forma incremental")
    parser.add_argument("--url", help="URL base de um site ou portal específico para extrair")
    parser.add_argument("--nome", help="Nome identificador da fonte")
    parser.add_argument("--pasta", help="Nome da subpasta de destino em saida_help/")
    parser.add_argument("--forcar", action="store_true", help="Regrava tudo, mesmo artigos não alterados")
    parser.add_argument("--adicionar", action="store_true", help="Salva a nova --url permanentemente no fontes.json")

    args = parser.parse_args()
    atualizar(
        url_especifica=args.url,
        nome_especifico=args.nome,
        pasta_especifica=args.pasta,
        forcar=args.forcar,
        adicionar=args.adicionar
    )

if __name__ == "__main__":
    main()
