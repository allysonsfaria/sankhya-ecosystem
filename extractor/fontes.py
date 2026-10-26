"""De onde vêm as páginas: API do Zendesk (rápida e exata) ou qualquer site (sitemap ou varredura de links)."""
import gzip
import hashlib
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ElementTree
from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Iterator

from bs4 import BeautifulSoup

from conversao import MIN_CARACTERES_CONTEUDO, extrair_conteudo_principal, texto_visivel

USER_AGENT = "extrator-help/1.0"
TAMANHO_PAGINA_ZENDESK = 100  # máximo aceito pela API do Zendesk
TENTATIVAS_HTTP = 6
TIMEOUT_HTTP_S = 60
ESPERA_BASE_S = 2
CODIGOS_RETENTAVEIS = {429, 500, 502, 503, 504}
CODIGOS_DE_BLOQUEIO = {403, 503}  # Cloudflare e afins: vale tentar com navegador
TAMANHO_MAX_SEGMENTO = 40  # mantém o caminho bem abaixo do MAX_PATH (260) do Windows
TAMANHO_HASH_NOME = 8
TIMEOUT_NAVEGADOR_MS = 60_000
ESPERA_REDE_OCIOSA_MS = 15_000
ESPERA_MAX_DESAFIO_S = 20
CANAIS_NAVEGADOR = ("chrome", "msedge")  # usa o navegador instalado; dispensa baixar Chromium
# Só marcas da página de desafio; "challenge-platform" fica de fora porque o Cloudflare injeta em páginas normais.
SINAIS_DE_DESAFIO = ("cf_chl_opt", "<title>just a moment", "<title>um momento")
EXTENSOES_NAO_HTML = re.compile(r"\.(pdf|zip|rar|7z|gz|exe|msi|dmg|png|jpe?g|gif|svg|webp|mp4|mp3|avi|docx?|xlsx?|"
                                r"pptx?|csv|xml|json|js|css|ico|woff2?|ttf)$", re.IGNORECASE)
CAMINHOS_SITEMAP_PADRAO = ("/sitemap.xml", "/sitemap_index.xml")
CARACTERES_SEGUROS_URL = ":/?#[]@!$&'()*+,;=%~"  # inclui '%' para não codificar de novo o que já vem codificado
LINK_MARKDOWN = re.compile(r"\]\((https?://[^)\s]+)\)")
CABECALHO_YAML = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
DATA_NO_CABECALHO = re.compile(r"^updatedAt:\s*(\S+)", re.MULTILINE)


@dataclass
class Pagina:
    chave: str
    url: str
    pasta: str = ""                 # relativa à pasta de saída
    nome: str = ""                  # nome do arquivo, sem .md
    titulo: str = ""
    trilha: list = field(default_factory=list)
    rotulos: list = field(default_factory=list)
    versao: str | None = None       # updated_at (Zendesk) ou lastmod (sitemap); None = desconhecida
    html: str | None = None         # None = não baixada porque a versão não mudou
    markdown: str | None = None     # Markdown oficial do site (.md do llms.txt); dispensa conversão
    erro: str | None = None
    ignorada: str | None = None     # motivo, quando não é página de conteúdo (ex.: PDF)


# ---------- utilitários ----------

def criar_slug(texto: str) -> str:
    ascii_puro = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_puro).strip("-").lower()
    return slug[:TAMANHO_MAX_SEGMENTO].rstrip("-") or "sem-nome"


def registrar(mensagem: str):
    print(f"[{time.strftime('%H:%M:%S')}] {mensagem}", flush=True)


def obter(url: str, aceitar: str = "*/*") -> tuple[bytes, str]:
    """GET com retentativa para falhas de rede, 429 (respeitando Retry-After) e 5xx. Devolve (corpo, content-type)."""
    url = urllib.parse.quote(url, safe=CARACTERES_SEGUROS_URL)  # acentos na URL ('serviço') viram %C3%A7
    requisicao = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": aceitar})
    for tentativa in range(1, TENTATIVAS_HTTP + 1):
        try:
            with urllib.request.urlopen(requisicao, timeout=TIMEOUT_HTTP_S) as resposta:
                return resposta.read(), resposta.headers.get("Content-Type", "")
        except urllib.error.HTTPError as erro:
            if erro.code not in CODIGOS_RETENTAVEIS or tentativa == TENTATIVAS_HTTP:
                raise
            espera = int(erro.headers.get("Retry-After") or ESPERA_BASE_S ** tentativa)
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if tentativa == TENTATIVAS_HTTP:
                raise
            espera = ESPERA_BASE_S ** tentativa
        registrar(f"  falha temporária em {url}; nova tentativa em {espera}s ({tentativa}/{TENTATIVAS_HTTP})")
        time.sleep(espera)
    raise RuntimeError("inalcançável")


def obter_json(url: str) -> dict:
    return json.loads(obter(url, "application/json")[0])


def raiz_do_site(url: str) -> str:
    partes = urllib.parse.urlparse(url)
    return f"{partes.scheme}://{partes.netloc}"


# ---------- Zendesk ----------

def eh_zendesk(base: str, locale: str) -> bool:
    try:
        return "articles" in obter_json(f"{raiz_do_site(base)}/api/v2/help_center/{locale}/articles.json?per_page=1")
    except (urllib.error.URLError, ValueError):
        return False


def iterar_paginas_api(url: str, chave: str):
    """Paginação por cursor da API, que não pula itens se o help mudar durante a leitura."""
    proxima = f"{url}{'&' if '?' in url else '?'}page%5Bsize%5D={TAMANHO_PAGINA_ZENDESK}"
    while proxima:
        pagina = obter_json(proxima)
        yield pagina[chave]
        proxima = pagina["links"]["next"] if pagina["meta"]["has_more"] else None


def listar_tudo(url: str, chave: str) -> list:
    return [item for pagina in iterar_paginas_api(url, chave) for item in pagina]


class FonteZendesk:
    def __init__(self, base: str, locale: str):
        self.base_api = f"{raiz_do_site(base)}/api/v2/help_center/{locale}"

    def total(self) -> int:
        return obter_json(f"{self.base_api}/articles.json?per_page=1")["count"]

    def paginas(self, ja_atualizada: Callable[[str, str | None], bool]) -> Iterator[Pagina]:
        secoes = {s["id"]: s for s in listar_tudo(f"{self.base_api}/sections.json", "sections")}
        categorias = {c["id"]: c for c in listar_tudo(f"{self.base_api}/categories.json", "categories")}
        for lote in iterar_paginas_api(f"{self.base_api}/articles.json", "articles"):
            for artigo in lote:
                yield self.montar_pagina(artigo, secoes, categorias)

    @staticmethod
    def montar_pagina(artigo: dict, secoes: dict, categorias: dict) -> Pagina:
        """Trilha completa (categoria > seções) para o cabeçalho; pasta curta categoria/seção para o disco."""
        trilha, pasta, secao = ["Sem seção"], "sem-secao", secoes.get(artigo["section_id"])
        if secao:
            trilha, atual = [], secao
            while atual:
                trilha.insert(0, atual["name"])
                atual = secoes.get(atual.get("parent_section_id"))
            categoria = categorias.get(secao["category_id"], {}).get("name", "Sem categoria")
            trilha, pasta = [categoria, *trilha], f"{criar_slug(categoria)}/{criar_slug(secao['name'])}"
        return Pagina(chave=str(artigo["id"]), url=artigo["html_url"], pasta=pasta,
                      nome=f"{artigo['id']}-{criar_slug(artigo['title'])}", titulo=artigo["title"], trilha=trilha,
                      rotulos=artigo.get("label_names") or [], versao=artigo["updated_at"], html=artigo.get("body") or "")


# ---------- busca de páginas (HTTP, com navegador como reserva) ----------

def parece_bloqueada_ou_vazia(html: bytes | str) -> bool:
    """Desafio anti-robô ou página montada por JavaScript (quase sem texto no HTML bruto)."""
    soup = BeautifulSoup(html, "html.parser")
    return len(texto_visivel(soup)) < MIN_CARACTERES_CONTEUDO or parece_desafio(str(soup))


class Buscador:
    """HTTP simples primeiro; Chrome/Edge instalado (via Playwright) só quando a página é bloqueada ou depende de JS."""

    def __init__(self, intervalo_s: float):
        self.intervalo_s = intervalo_s
        self._playwright = self._navegador = self._aba = None
        self._visivel = False

    def obter_html(self, url: str) -> tuple[bytes | str | None, str, bool]:
        """Devolve (html, motivo_para_ignorar, veio_do_navegador). html None quando o recurso não é página HTML."""
        time.sleep(self.intervalo_s)
        try:
            corpo, tipo = obter(url, "text/html,application/xhtml+xml")
            if "html" not in tipo.lower():
                return None, f"não é HTML ({tipo or 'tipo desconhecido'})", False
            if not parece_bloqueada_ou_vazia(corpo):
                return corpo, "", False
        except urllib.error.HTTPError as erro:
            if erro.code not in CODIGOS_DE_BLOQUEIO:
                raise
        return self.obter_com_navegador(url), "", True

    def obter_com_navegador(self, url: str) -> str:
        html = self._carregar(url)
        if parece_desafio(html) and not self._visivel:
            registrar("  desafio anti-robô persistiu no modo oculto; reabrindo o navegador visível")
            self.fechar()
            self._visivel = True
            html = self._carregar(url)
        if parece_desafio(html):
            raise RuntimeError("bloqueada por desafio anti-robô mesmo com navegador")
        return html

    def _carregar(self, url: str) -> str:
        aba = self._abrir()
        aba.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT_NAVEGADOR_MS)
        limite = time.monotonic() + ESPERA_MAX_DESAFIO_S
        while parece_desafio(aba.content()) and time.monotonic() < limite:
            aba.wait_for_timeout(1000)
        try:
            aba.wait_for_load_state("networkidle", timeout=ESPERA_REDE_OCIOSA_MS)
        except Exception:  # site com conexão sempre aberta (chat, analytics) nunca fica ocioso; segue com o que tem
            pass
        return aba.content()

    def _abrir(self):
        if self._aba is not None:
            return self._aba
        from playwright.sync_api import Error as ErroPlaywright, sync_playwright
        self._playwright = sync_playwright().start()
        argumentos = ["--disable-blink-features=AutomationControlled"]
        for canal in CANAIS_NAVEGADOR:
            try:
                self._navegador = self._playwright.chromium.launch(channel=canal, headless=not self._visivel,
                                                                   args=argumentos)
                break
            except ErroPlaywright:
                continue
        else:
            self.fechar()
            raise RuntimeError("Chrome ou Edge não encontrado; instale um deles para páginas que exigem navegador")
        agente = self._navegador.new_page().evaluate("navigator.userAgent").replace("HeadlessChrome", "Chrome")
        self._aba = self._navegador.new_context(user_agent=agente).new_page()
        return self._aba

    def fechar(self):
        if self._navegador is not None:
            self._navegador.close()
        if self._playwright is not None:
            self._playwright.stop()
        self._playwright = self._navegador = self._aba = None


def tamanho_texto(fragmento: str) -> int:
    return len(texto_visivel(BeautifulSoup(fragmento, "html.parser")))


def conteudo_curto(fragmento: str) -> bool:
    return tamanho_texto(fragmento) < MIN_CARACTERES_CONTEUDO


def parece_desafio(html: str) -> bool:
    inicio = html[:20_000].lower()
    return any(sinal in inicio for sinal in SINAIS_DE_DESAFIO)


# ---------- descoberta de páginas (sites genéricos) ----------

def normalizar_url(url: str) -> str:
    """Sem fragmento (#...) e com '/' no caminho vazio: 'site.com' e 'site.com/' são a mesma página."""
    partes = urllib.parse.urlparse(urllib.parse.urldefrag(url)[0])
    return partes._replace(path=partes.path or "/").geturl()


class Escopo:
    """Só segue URLs do mesmo host e abaixo do caminho da URL base (ex.: base /docs -> só /docs/...)."""

    def __init__(self, base: str):
        partes = urllib.parse.urlparse(base)
        caminho = partes.path
        if "." in caminho.rsplit("/", 1)[-1]:  # base é um arquivo (ex.: /docs.html): o escopo é a pasta dele
            caminho = caminho.rsplit("/", 1)[0]
        self.host, self.prefixo = partes.netloc.lower(), caminho.rstrip("/")

    def contem(self, url: str) -> bool:
        partes = urllib.parse.urlparse(url)
        caminho = partes.path or "/"
        return (partes.scheme in ("http", "https") and partes.netloc.lower() == self.host
                and (caminho == self.prefixo or caminho.startswith(self.prefixo + "/") or not self.prefixo)
                and not EXTENSOES_NAO_HTML.search(caminho))


def ler_robots(base: str) -> urllib.robotparser.RobotFileParser:
    robots = urllib.robotparser.RobotFileParser()
    try:
        robots.parse(obter(f"{raiz_do_site(base)}/robots.txt")[0].decode("utf-8", "replace").splitlines())
    except (urllib.error.URLError, ValueError):
        robots.parse([])  # sem robots.txt: tudo permitido
    return robots


def ler_sitemap(url: str, visitados: set) -> list[tuple[str, str | None]]:
    """(url, lastmod) de um sitemap, seguindo índices de sitemap e .gz. Sitemap ausente ou inválido -> []."""
    if url in visitados:
        return []
    visitados.add(url)
    try:
        conteudo = obter(url, "application/xml,text/xml")[0]
        if conteudo[:2] == b"\x1f\x8b":
            conteudo = gzip.decompress(conteudo)
        raiz = ElementTree.fromstring(conteudo)
    except (urllib.error.URLError, ElementTree.ParseError, OSError, ValueError):
        return []
    entradas = []
    for item in raiz:
        filhos = {filho.tag.rsplit("}", 1)[-1]: (filho.text or "").strip() for filho in item}
        if not filhos.get("loc"):
            continue
        if raiz.tag.endswith("sitemapindex"):
            entradas += ler_sitemap(filhos["loc"], visitados)
        else:
            entradas.append((filhos["loc"], filhos.get("lastmod") or None))
    return entradas


def ler_llms_txt(base: str) -> list[str]:
    """Links do llms.txt (índice para IAs publicado por ReadMe, Mintlify, GitBook etc.), da pasta base ou da raiz."""
    pasta_base = Escopo(base).prefixo
    candidatos = dict.fromkeys([f"{raiz_do_site(base)}{pasta_base}/llms.txt", f"{raiz_do_site(base)}/llms.txt"])
    for candidato in candidatos:
        try:
            corpo, tipo = obter(candidato, "text/plain,text/markdown")
        except (urllib.error.URLError, ValueError):
            continue
        if "html" not in tipo.lower():
            return list(dict.fromkeys(LINK_MARKDOWN.findall(corpo.decode("utf-8", "replace"))))
    return []


def url_canonica(url: str) -> str:
    """'.../docs/pagina.md' -> '.../docs/pagina': a chave e o nome do arquivo não dependem do formato baixado."""
    return normalizar_url(url[:-3] if url.lower().endswith(".md") else url)


def separar_markdown(texto: str) -> tuple[str, str | None, str]:
    """(corpo sem o cabeçalho YAML do site, updatedAt, título do primeiro '# ')."""
    cabecalho = CABECALHO_YAML.match(texto)
    corpo = texto[cabecalho.end():] if cabecalho else texto
    data = DATA_NO_CABECALHO.search(cabecalho.group(1)) if cabecalho else None
    titulo = re.search(r"^# (.+)$", corpo, re.MULTILINE)
    return corpo.strip() + "\n", data.group(1) if data else None, titulo.group(1).strip() if titulo else ""


def links_da_pagina(html: bytes | str, url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    return [normalizar_url(urllib.parse.urljoin(url, a["href"].strip())) for a in soup.find_all("a", href=True)]


class FonteGenerica:
    def __init__(self, base: str, buscador: Buscador, seletor: str | None, max_paginas: int):
        self.base, self.buscador, self.seletor, self.max_paginas = base, buscador, seletor, max_paginas
        self.escopo, self.robots = Escopo(base), ler_robots(base)
        self.llms = self.descobrir_llms()
        self.sitemap = [] if self.llms else self.descobrir_sitemap()

    def descobrir_llms(self) -> list[str]:
        """Links do llms.txt dentro do escopo, sem repetir a mesma página (com e sem .md)."""
        links = {}
        for link in ler_llms_txt(self.base):
            canonica = url_canonica(link)
            if canonica not in links and self.escopo.contem(canonica) and self.permitida(canonica):
                links[canonica] = link
        return list(links.values())[:self.max_paginas]

    def descobrir_sitemap(self) -> list[tuple[str, str | None]]:
        candidatos = self.robots.site_maps() or [raiz_do_site(self.base) + c for c in CAMINHOS_SITEMAP_PADRAO]
        visitados, vistos, entradas = set(), set(), []
        for candidato in candidatos:
            for url, lastmod in ler_sitemap(candidato, visitados):
                url = normalizar_url(url)
                if url not in vistos and self.escopo.contem(url) and self.permitida(url):
                    vistos.add(url)
                    entradas.append((url, lastmod))
        return entradas[:self.max_paginas]

    def permitida(self, url: str) -> bool:
        return self.robots.can_fetch(USER_AGENT, url)

    def total(self) -> int | None:
        return len(self.llms) or len(self.sitemap) or None  # varredura por links não sabe o total antes

    def paginas(self, ja_atualizada: Callable[[str, str | None], bool]) -> Iterator[Pagina]:
        if self.llms:
            for link in self.llms:
                yield self.baixar_markdown(link)
            return
        if self.sitemap:
            for url, lastmod in self.sitemap:
                yield self.baixar(url, lastmod, ja_atualizada)
            return
        yield from self.varrer_links()

    def varrer_links(self) -> Iterator[Pagina]:
        """Sem sitemap: varredura em largura a partir da URL base, dentro do escopo."""
        fila, vistos = deque([normalizar_url(self.base)]), {normalizar_url(self.base)}
        while fila and len(vistos) - len(fila) < self.max_paginas:
            url = fila.popleft()
            pagina, html = self.baixar_com_html(url, None)
            yield pagina
            for link in links_da_pagina(html, url) if html is not None else []:
                if link not in vistos and self.escopo.contem(link) and self.permitida(link):
                    vistos.add(link)
                    fila.append(link)

    def baixar_markdown(self, link: str) -> Pagina:
        """Markdown oficial do site quando o link é .md; se vier HTML, segue o caminho normal de conversão."""
        if not link.lower().endswith(".md"):
            return self.baixar_com_html(url_canonica(link), None)[0]
        pagina = self.pagina_vazia(url_canonica(link), None)
        try:
            time.sleep(self.buscador.intervalo_s)
            corpo, tipo = obter(link, "text/markdown,text/plain")
            texto = corpo.decode("utf-8", "replace")
            if "html" in tipo.lower() or texto.lstrip().startswith("<"):
                return self.baixar_com_html(pagina.url, None)[0]
            pagina.markdown, pagina.versao, pagina.titulo = separar_markdown(texto)
        except Exception as erro:  # uma página com problema não pode derrubar as outras
            pagina.erro = repr(erro)
        return pagina

    def baixar(self, url: str, lastmod: str | None, ja_atualizada) -> Pagina:
        if lastmod and ja_atualizada(url, lastmod):
            return self.pagina_vazia(url, lastmod)
        return self.baixar_com_html(url, lastmod)[0]

    def baixar_com_html(self, url: str, lastmod: str | None) -> tuple[Pagina, bytes | str | None]:
        pagina = self.pagina_vazia(url, lastmod)
        try:
            html, motivo, do_navegador = self.buscador.obter_html(url)
            if html is None:
                pagina.ignorada = motivo
                return pagina, None
            pagina.html, pagina.titulo, achou_conteiner = extrair_conteudo_principal(html, url, self.seletor)
            if not do_navegador and (not achou_conteiner or conteudo_curto(pagina.html)):
                # o menu engana a checagem do HTML bruto; sem contêiner de conteúdo, pode ser página montada por JS
                html_renderizado = self.buscador.obter_com_navegador(url)
                renderizado = extrair_conteudo_principal(html_renderizado, url, self.seletor)
                if tamanho_texto(renderizado[0]) > tamanho_texto(pagina.html):
                    html, (pagina.html, pagina.titulo, _) = html_renderizado, renderizado
            return pagina, html
        except Exception as erro:  # uma página com problema não pode derrubar as outras
            pagina.erro = repr(erro)
            return pagina, None

    def pagina_vazia(self, url: str, lastmod: str | None) -> Pagina:
        segmentos = [s for s in urllib.parse.unquote(urllib.parse.urlparse(url).path).split("/") if s]
        pasta = criar_slug(segmentos[0]) if len(segmentos) > 1 else "inicio"
        resumo = hashlib.sha1(url.encode()).hexdigest()[:TAMANHO_HASH_NOME]  # evita colisão de nomes iguais
        nome = f"{criar_slug(segmentos[-1]) if segmentos else 'index'}-{resumo}"
        return Pagina(chave=url, url=url, pasta=pasta, nome=nome, versao=lastmod)
