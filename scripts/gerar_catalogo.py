#!/usr/bin/env python3
"""
Gera catálogo indexado de telas e APIs de todas as fontes do acervo Sankhya Help.
Totalmente dinâmico: varre qualquer subpasta em saida_help sem nomes fixos.
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
            conteudo = f.read(2048)
    except Exception:
        return None

    if not conteudo.startswith("---"):
        return None

    partes = conteudo.split("---", 2)
    if len(partes) < 3:
        return None

    yaml_texto = partes[1]
    meta = {}
    
    for linha in yaml_texto.splitlines():
        linha = linha.strip()
        if ":" in linha:
            chave, _, valor = linha.partition(":")
            chave = chave.strip()
            valor = valor.strip().strip('"').strip("'")
            if chave in ("id", "titulo", "url", "trilha", "atualizado_em"):
                meta[chave] = valor
            elif chave == "rotulos" and valor.startswith("["):
                tags = [t.strip().strip('"').strip("'") for t in valor.strip("[]").split(",") if t.strip()]
                meta["rotulos"] = tags[:15]

    return meta

def indexar_acervo(help_dir, output_dir):
    help_path = Path(help_dir).resolve()
    out_path = Path(output_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    telas = []
    apis = []

    if not help_path.exists():
        print(f"[AVISO] Pasta de acervo {help_path} não encontrada.")
        return

    subpastas = [p for p in help_path.iterdir() if p.is_dir() and not p.name.startswith(".")]
    print(f"Indexando {len(subpastas)} fontes encontradas em {help_path}...")

    for subpasta in subpastas:
        nome_pasta = subpasta.name.lower()
        eh_portal_dev = any(k in nome_pasta for k in ("developer", "dev", "api", "doc", "recipe"))

        print(f" -> Processando acervo: {subpasta.name}...")
        for root, _, files in os.walk(subpasta):
            for file in files:
                if file.endswith(".md") and not file.startswith("_"):
                    full_p = Path(root) / file
                    meta = extrair_metadados_md(full_p)
                    rel_path = str(full_p.relative_to(help_path)).replace("\\", "/")
                    
                    titulo = (meta.get("titulo") if meta else "") or file.replace(".md", "")
                    
                    # Se tiver trilha ou for manual de produto -> catálogo de telas
                    if meta and meta.get("trilha"):
                        telas.append({
                            "id": meta.get("id", ""),
                            "titulo": titulo,
                            "trilha": meta.get("trilha", ""),
                            "rotulos": meta.get("rotulos", []),
                            "arquivo": rel_path
                        })
                    elif eh_portal_dev or any(k in rel_path.lower() for k in ("reference", "recipe", "api", "docs")):
                        apis.append({
                            "id": meta.get("id", "") if meta else "",
                            "titulo": titulo,
                            "url": meta.get("url", "") if meta else "",
                            "arquivo": rel_path
                        })
                    else:
                        # Conteúdo geral
                        telas.append({
                            "id": meta.get("id", "") if meta else "",
                            "titulo": titulo,
                            "trilha": subpasta.name,
                            "rotulos": meta.get("rotulos", []) if meta else [],
                            "arquivo": rel_path
                        })

    # Grava catálogos
    telas_json = out_path / "catalogo_telas.json"
    with open(telas_json, "w", encoding="utf-8") as f:
        json.dump(telas, f, ensure_ascii=False, separators=(',', ':'))

    apis_json = out_path / "catalogo_apis.json"
    with open(apis_json, "w", encoding="utf-8") as f:
        json.dump(apis, f, ensure_ascii=False, separators=(',', ':'))

    print(f"\n[OK] Sucesso: {len(telas)} telas/manuais indexados em {telas_json}")
    print(f"[OK] Sucesso: {len(apis)} itens de API/Docs indexados em {apis_json}")

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    default_help = skill_dir / "saida_help"
    if not default_help.exists():
        default_help = skill_dir.parent / "GIT" / "saida_help"
    
    help_base = sys.argv[1] if len(sys.argv) > 1 else str(default_help)
    saida = sys.argv[2] if len(sys.argv) > 2 else str(script_dir)
    indexar_acervo(help_base, saida)
