"""Conversão do HTML de páginas de help em Markdown limpo para RAG, com as regras de mídia."""
import re
import urllib.parse

import trafilatura
from bs4 import BeautifulSoup
from markdownify import markdownify

LADO_MAX_ICONE_PX = 42
TAMANHO_MAX_LEGENDA = 120
MIN_CARACTERES_CONTEUDO = 200
EXTENSOES_IMAGEM = re.compile(r"\.(png|jpe?g|gif|bmp|webp|svg)$", re.IGNORECASE)
NUMERO_MARCADOR = re.compile(r"^(?:marcador\s*)?(\d{1,2})\b", re.IGNORECASE)
TAGS_COM_IMAGEM = ["td", "th", "span", "a", "strong", "b", "em", "i", "li", "p", "div", "figure"]
LARGURA_ZERO = "​"
TITULOS = ["h1", "h2", "h3", "h4", "h5", "h6"]
BLOCOS_DE_TEXTO = ["p", "li", "td", "th", "summary", *TITULOS]
NEGRITOS = ["b", "strong"]
# Ordem importa: o mais específico primeiro. "main" costuma trazer breadcrumb e paginação junto.
SELETORES_CONTEUDO = ["article", "[role=main]", "main", ".article-body", ".markdown-body", ".md-content",
                      ".theme-doc-markdown", "#content", ".content"]
RUIDO_DENTRO_DO_CONTEUDO = ["nav", "footer", "aside", "form", "button", "script", "style", "noscript", "svg",
                            "template"]
MAX_CARACTERES_PERMALINK = 2


# ---------- extração do conteúdo principal (sites genéricos) ----------

def texto_visivel(soup) -> str:
    copia = BeautifulSoup(str(soup), "html.parser")
    for invisivel in copia.find_all(["script", "style", "noscript", "template"]):
        invisivel.decompose()
    return copia.get_text(" ", strip=True)


def localizar_conteudo(soup, seletor: str | None):
    if seletor:
        elemento = soup.select_one(seletor)
        if elemento is None:
            raise ValueError(f"seletor {seletor!r} não encontrado na página")
        return elemento
    for candidato in SELETORES_CONTEUDO:
        elemento = soup.select_one(candidato)
        if elemento is not None and len(elemento.get_text(" ", strip=True)) >= MIN_CARACTERES_CONTEUDO:
            return elemento
    return None


def remover_ruido(conteudo):
    for ruido in conteudo.select(", ".join(RUIDO_DENTRO_DO_CONTEUDO)):
        ruido.decompose()


def remover_permalinks(soup):
    """Âncoras '¶', '#' ou ícone de fonte ao lado de títulos. Precisa rodar antes de tornar as URLs absolutas."""
    for ancora in soup.find_all("a", href=re.compile(r"^#")):
        texto = ancora.get_text(strip=True)
        if len(texto) <= MAX_CARACTERES_PERMALINK and not any(caractere.isalnum() for caractere in texto):
            ancora.decompose()


def titulo_da_pagina(soup, conteudo) -> str:
    for origem in (conteudo.find("h1") if conteudo else None, soup.find("h1"), soup.title):
        if origem is not None and origem.get_text(strip=True):
            return re.sub(r"\s+", " ", origem.get_text(" ", strip=True))
    return ""


def extrair_conteudo_principal(html: str | bytes, url: str, seletor: str | None = None) -> tuple[str, str, bool]:
    """Devolve (HTML só do conteúdo principal, título, achou_conteiner). achou_conteiner=False indica extração
    por heurística (trafilatura), menos confiável. Vídeos viram links antes, para sobreviver à extração."""
    soup = BeautifulSoup(html, "html.parser")
    remover_permalinks(soup)
    tornar_urls_absolutas(soup, url)
    tratar_videos(soup)
    conteudo = localizar_conteudo(soup, seletor)
    titulo = titulo_da_pagina(soup, conteudo)
    if conteudo is not None:
        remover_ruido(conteudo)
        return str(conteudo), titulo, True
    extraido = trafilatura.extract(str(soup), url=url, output_format="html", include_images=True,
                                   include_links=True, include_tables=True, include_formatting=True,
                                   favor_recall=True)
    if not extraido:
        raise ValueError("conteúdo principal não encontrado")
    return extraido, titulo, False


# ---------- regras de mídia ----------

def ler_dimensao(valor) -> int:
    """'25', '25px' -> 25; '100%', vazio ou inválido -> 0 (desconhecido)."""
    texto = str(valor or "").strip()
    if texto.endswith("%"):
        return 0
    numero = re.match(r"\d+", texto)
    return int(numero.group()) if numero else 0


def parece_nome_arquivo(texto: str) -> bool:
    return bool(EXTENSOES_IMAGEM.search(texto)) or texto.isdigit() or (" " not in texto and "_" in texto)


def limpar_legenda(texto: str) -> str:
    texto = re.sub(r"\s+", " ", texto.replace(LARGURA_ZERO, "")).strip().replace("[", "(").replace("]", ")")
    if len(texto) <= TAMANHO_MAX_LEGENDA:
        return texto
    return texto[:TAMANHO_MAX_LEGENDA].rsplit(" ", 1)[0] + "…"


def texto_anterior(elemento) -> str:
    """Texto do bloco mais próximo antes do elemento (o próprio parágrafo/item, se tiver texto)."""
    for bloco in elemento.find_all_previous(BLOCOS_DE_TEXTO):
        texto = bloco.get_text(" ", strip=True).replace(LARGURA_ZERO, "").strip()
        if texto:
            return texto
    return ""


def legenda_imagem(img, indice: int) -> str:
    alt = (img.get("alt") or "").strip()
    if alt and not parece_nome_arquivo(alt):
        return limpar_legenda(alt)
    contexto = limpar_legenda(texto_anterior(img))
    return f"Imagem {indice}: {contexto}" if contexto else f"Imagem {indice}"


def eh_icone(img) -> bool:
    largura, altura = ler_dimensao(img.get("width")), ler_dimensao(img.get("height"))
    pequena = 0 < largura <= LADO_MAX_ICONE_PX and 0 < altura <= LADO_MAX_ICONE_PX
    return pequena or "marcador" in (img.get("alt") or "").lower()


def eh_gif(img) -> bool:
    caminho = urllib.parse.urlparse(img.get("src") or "").path
    return any(valor.lower().endswith(".gif") for valor in (caminho, (img.get("alt") or "").strip()))


def substituir_por_link(soup, elemento, rotulo: str, url: str):
    paragrafo = soup.new_tag("p")
    link = soup.new_tag("a", href=url)
    link.string = rotulo
    paragrafo.append(link)
    elemento.replace_with(paragrafo)


def tratar_imagens(soup):
    """Ícones viram o número do passo (marcadores numerados) ou somem; GIFs viram link; prints ganham legenda."""
    indice = 0
    for img in soup.find_all("img"):
        if not (img.get("src") or "").strip():
            img.decompose()
            continue
        if eh_icone(img):
            numero = NUMERO_MARCADOR.match((img.get("alt") or "").strip())
            if not numero:
                img.decompose()
                continue
            negrito = soup.new_tag("strong")
            negrito.string = f"({numero.group(1)})"
            img.replace_with(negrito)
            continue
        indice += 1
        legenda = legenda_imagem(img, indice)
        if eh_gif(img):
            substituir_por_link(soup, img, f"GIF animado: {legenda}", img.get("src", ""))
        else:
            img["alt"] = legenda


def url_video(src: str) -> str:
    """Converte embed do YouTube em link assistível; demais URLs ficam como estão."""
    embed = re.search(r"youtube(?:-nocookie)?\.com/embed/([\w-]+)", src)
    return f"https://www.youtube.com/watch?v={embed.group(1)}" if embed else src


def tratar_videos(soup):
    for video in soup.find_all(["iframe", "video"]):
        fonte = video.get("src") or (video.find("source") or {}).get("src") or ""
        if not fonte:
            video.decompose()
            continue
        rotulo = f"Vídeo: {limpar_legenda(video.get('title') or '') or 'tutorial do artigo'}"
        substituir_por_link(soup, video, rotulo, url_video(fonte))


def tornar_urls_absolutas(soup, url_pagina: str):
    for tag, atributo in (("a", "href"), ("img", "src"), ("iframe", "src"), ("source", "src")):
        for elemento in soup.find_all(tag, attrs={atributo: True}):
            elemento[atributo] = urllib.parse.urljoin(url_pagina, elemento[atributo].strip())


def tratar_acordeoes(soup):
    """<summary> vira título em negrito; sem isso o markdownify cola o título no conteúdo."""
    for resumo in soup.find_all("summary"):
        paragrafo = soup.new_tag("p")
        negrito = soup.new_tag("strong")
        negrito.string = resumo.get_text(" ", strip=True)
        paragrafo.append(negrito)
        resumo.replace_with(paragrafo)


def simplificar_formatacao(soup):
    """Itálico/sublinhado não ajudam no RAG e, aninhados no HTML do help, geram '***x****' no Markdown."""
    for tag in soup.find_all(["i", "em", "u"]):
        tag.unwrap()
    for negrito in soup.find_all(NEGRITOS):
        if not negrito.get_text(strip=True) or negrito.find_parent([*NEGRITOS, *TITULOS, "th"]):
            negrito.unwrap()
    for negrito in soup.find_all(NEGRITOS):
        vizinho = negrito.next_sibling
        while vizinho is not None and getattr(vizinho, "name", None) in NEGRITOS:
            negrito.extend(list(vizinho.contents))
            vizinho.decompose()
            vizinho = negrito.next_sibling


def converter_corpo(html: str, url_pagina: str) -> str:
    soup = BeautifulSoup((html or "").replace(LARGURA_ZERO, ""), "html.parser")
    for lixo in soup.find_all(["script", "style"]):
        lixo.decompose()
    simplificar_formatacao(soup)
    tornar_urls_absolutas(soup, url_pagina)
    tratar_imagens(soup)
    tratar_videos(soup)
    tratar_acordeoes(soup)
    markdown = markdownify(str(soup), heading_style="ATX", bullets="-",
                           keep_inline_images_in=TAGS_COM_IMAGEM, table_infer_header=True)
    markdown = markdown.replace("****", "")  # negritos colados que o HTML separa em tags vizinhas: **a****b** -> **ab**
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    return re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
