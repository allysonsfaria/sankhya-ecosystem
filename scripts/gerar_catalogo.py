#!/usr/bin/env python3
"""
Gera catálogo indexado de telas e APIs do acervo extraído do Sankhya Help.
Produz arquivos JSON compactos para busca instantânea sem varredura em 10k arquivos.
"""
import os
import sys
import json
import re
from pathlib import Path

def extrair_metadados_md(caminho_arquivo):
    """Lê o frontmatter YAML de um arquivo Markdown extraído."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
            conteudo = f.read(2048) # Lê apenas o início para pegar o frontmatter
    except Exception:
        return None

    if not conteudo.startswith("---"):
        return None

    partes = conteudo.split("---", 2)
    if len(partes) < 3:
        return None

    yaml_texto = partes[1]
    meta = {}
    
    # Extração simples de campos comuns sem precisar de PyYAML externo
    for linha in yaml_texto.splitlines():
        linha = linha.strip()
        if ":" in linha:
            chave, _, valor = linha.partition(":")
            chave = chave.strip()
            valor = valor.strip().strip('"').strip("'")
            if chave in ("id", "titulo", "url", "trilha", "atualizado_em"):
                meta[chave] = valor
            elif chave == "rotulos" and valor.startswith("["):
                # Captura tags
                tags = [t.strip().strip('"').strip("'") for t in valor.strip("[]").split(",") if t.strip()]
                meta["rotulos"] = tags[:15] # Limita a 15 tags principais

    return meta

def indexar_acervo(help_dir, output_dir):
    help_path = Path(help_dir).resolve()
    out_path = Path(output_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    telas = []
    apis = []

    ajuda_dir = help_path / "ajuda-sankhya-com-br"
    dev_dir = help_path / "developer-sankhya-com-br"

    print(f"Indexando ajuda em {ajuda_dir}...")
    if ajuda_dir.exists():
        for root, _, files in os.walk(ajuda_dir):
            for file in files:
                if file.endswith(".md") and not file.startswith("_"):
                    full_p = Path(root) / file
                    meta = extrair_metadados_md(full_p)
                    if meta and meta.get("titulo"):
                        rel_path = str(full_p.relative_to(help_path)).replace("\\", "/")
                        telas.append({
                            "id": meta.get("id", ""),
                            "titulo": meta.get("titulo", ""),
                            "trilha": meta.get("trilha", ""),
                            "rotulos": meta.get("rotulos", []),
                            "arquivo": rel_path
                        })

    print(f"Indexando developer em {dev_dir}...")
    if dev_dir.exists():
        for root, _, files in os.walk(dev_dir):
            for file in files:
                if file.endswith(".md") and not file.startswith("_"):
                    full_p = Path(root) / file
                    meta = extrair_metadados_md(full_p)
                    rel_path = str(full_p.relative_to(help_path)).replace("\\", "/")
                    titulo = meta.get("titulo", file.replace(".md", "")) if meta else file.replace(".md", "")
                    apis.append({
                        "id": meta.get("id", "") if meta else "",
                        "titulo": titulo,
                        "url": meta.get("url", "") if meta else "",
                        "arquivo": rel_path
                    })

    # Grava catálogos
    telas_json = out_path / "catalogo_telas.json"
    with open(telas_json, "w", encoding="utf-8") as f:
        json.dump(telas, f, ensure_ascii=False, separators=(',', ':'))

    apis_json = out_path / "catalogo_apis.json"
    with open(apis_json, "w", encoding="utf-8") as f:
        json.dump(apis, f, ensure_ascii=False, separators=(',', ':'))

    print(f"Sucesso: {len(telas)} telas indexadas em {telas_json}")
    print(f"Sucesso: {len(apis)} itens de API/Doc indexados em {apis_json}")

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    default_help = skill_dir / "saida_help"
    if not default_help.exists():
        default_help = skill_dir.parent / "GIT" / "saida_help"
    
    help_base = sys.argv[1] if len(sys.argv) > 1 else str(default_help)
    saida = sys.argv[2] if len(sys.argv) > 2 else str(script_dir)
    indexar_acervo(help_base, saida)
