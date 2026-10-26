#!/usr/bin/env python3
"""
search_help.py - Localizador de Telas, Manuais e APIs Sankhya.
Permite à IA consultar instantaneamente documentação de telas, parâmetros e endpoints
sem poluir o contexto e com resposta em milissegundos.
"""
import sys
import os
import json
import re
import argparse
from pathlib import Path

def get_base_dirs():
    """Identifica diretório dos catálogos e acervo markdown de forma 100% dinâmica."""
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    
    # 1. Caminho autocontido na própria skill (padrão preferencial)
    candidatos = [
        os.environ.get("SANKHYA_HELP_DIR"),
        skill_dir / "saida_help",
        skill_dir / "acervo",
        script_dir / "saida_help",
        skill_dir.parent / "saida_help",
        skill_dir.parent / "GIT" / "saida_help",
    ]

    help_dir = None
    for cand in candidatos:
        if cand:
            p = Path(cand).resolve()
            if p.exists() and (p / "ajuda-sankhya-com-br").exists():
                help_dir = p
                break

    # Se ainda não encontrou, busca subindo a árvore de diretórios
    if not help_dir:
        curr = skill_dir
        for _ in range(5):
            tentativa = curr / "saida_help"
            if tentativa.exists() and (tentativa / "ajuda-sankhya-com-br").exists():
                help_dir = tentativa.resolve()
                break
            if curr.parent == curr:
                break
            curr = curr.parent

    return script_dir, help_dir

def carregar_catalogo(script_dir, nome):
    cat_file = script_dir / nome
    if cat_file.exists():
        try:
            with open(cat_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def extrair_resumo_arquivo(caminho_completo, max_linhas=40):
    """Extrai cabeçalho e primeiros tópicos de um artigo de help."""
    if not caminho_completo.exists():
        return "Arquivo não encontrado no disco."
    
    linhas = []
    try:
        with open(caminho_completo, "r", encoding="utf-8", errors="ignore") as f:
            for _ in range(max_linhas):
                l = f.readline()
                if not l:
                    break
                linhas.append(l)
    except Exception as e:
        return f"Erro ao ler arquivo: {e}"
        
    return "".join(linhas).strip()

def buscar(query, tipo="all", limite=5, detalhe=False):
    script_dir, help_dir = get_base_dirs()
    if not help_dir:
        print("[ERRO] Diretório 'saida_help' não localizado. Configure a variável SANKHYA_HELP_DIR.")
        sys.exit(1)

    termos = [t.lower().strip() for t in query.split() if t.strip()]
    if not termos:
        print("Informe um termo de busca.")
        return

    resultados = []

    # 1. Buscar em Telas
    if tipo in ("all", "tela", "manual"):
        telas = carregar_catalogo(script_dir, "catalogo_telas.json")
        for item in telas:
            titulo = item.get("titulo", "").lower()
            trilha = item.get("trilha", "").lower()
            rotulos = " ".join(item.get("rotulos", [])).lower()
            texto_busca = f"{titulo} {trilha} {rotulos}"

            score = 0
            if all(t in texto_busca for t in termos):
                # Pontuação de relevância
                if all(t in titulo for t in termos):
                    score += 10
                if query.lower() in titulo:
                    score += 20
                score += sum(2 for t in termos if t in rotulos)
                
                item_copia = dict(item)
                item_copia["score"] = score
                item_copia["categoria"] = "Tela/Manual"
                resultados.append(item_copia)

    # 2. Buscar em APIs e Docs de Desenvolvedor
    if tipo in ("all", "api", "dev"):
        apis = carregar_catalogo(script_dir, "catalogo_apis.json")
        for item in apis:
            titulo = item.get("titulo", "").lower()
            arquivo = item.get("arquivo", "").lower()
            texto_busca = f"{titulo} {arquivo}"

            score = 0
            if all(t in texto_busca for t in termos):
                if all(t in titulo for t in termos):
                    score += 10
                if query.lower() in titulo:
                    score += 20
                item_copia = dict(item)
                item_copia["score"] = score
                item_copia["categoria"] = "API/Dev"
                resultados.append(item_copia)

    # Ordenar por score decrescente
    resultados.sort(key=lambda x: x.get("score", 0), reverse=True)
    top = resultados[:limite]

    if not top:
        print(f"Nenhum resultado encontrado para: '{query}'")
        return

    print(f"\n=== {len(top)} Resultados para '{query}' ===")
    for idx, res in enumerate(top, 1):
        rel_path = res.get("arquivo")
        full_path = help_dir / rel_path
        titulo = res.get("titulo")
        cat = res.get("categoria")
        trilha = res.get("trilha", "")
        
        print(f"\n[{idx}] {cat}: {titulo}")
        if trilha:
            print(f"    Trilha: {trilha}")
        print(f"    Arquivo: {full_path}")
        
        if detalhe:
            print("    --- Início do Conteúdo ---")
            trecho = extrair_resumo_arquivo(full_path, max_linhas=30)
            for linha in trecho.splitlines()[:25]:
                print(f"    | {linha}")
            print("    --------------------------")

def main():
    parser = argparse.ArgumentParser(description="Consulta documentação do ecossistema Sankhya")
    parser.add_argument("query", nargs="*", help="Termo de pesquisa (ex: parceiro, loadRecords, tgfcab)")
    parser.add_argument("-t", "--tipo", choices=["all", "tela", "manual", "api", "dev"], default="all", help="Tipo de recurso")
    parser.add_argument("-l", "--limite", type=int, default=5, help="Quantidade de resultados (padrão: 5)")
    parser.add_argument("-d", "--detalhe", action="store_true", help="Exibe resumo do conteúdo do arquivo")

    args = parser.parse_args()
    query_str = " ".join(args.query).strip()
    if not query_str:
        parser.print_help()
        sys.exit(0)

    buscar(query_str, tipo=args.tipo, limite=args.limite, detalhe=args.detalhe)

if __name__ == "__main__":
    main()
