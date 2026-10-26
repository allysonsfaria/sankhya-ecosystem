#!/usr/bin/env python3
"""
atualizar_acervo.py - Sincronização e Atualização do Acervo Sankhya.
Executa extração incremental (apenas o que mudou) e reconstrói os catálogos de busca.
"""
import sys
import os
import subprocess
from pathlib import Path

def atualizar():
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    extractor_dir = skill_dir / "extractor"
    extrator_py = extractor_dir / "extrator_help.py"
    saida_help = skill_dir / "saida_help"
    catalogo_py = script_dir / "gerar_catalogo.py"

    if not extrator_py.exists():
        print(f"[ERRO] Extrator não encontrado em: {extrator_py}")
        sys.exit(1)

    print("=== [1/3] Atualizando artigos do Ajuda Sankhya (ajuda.sankhya.com.br) ===")
    cmd_ajuda = [
        sys.executable,
        str(extrator_py),
        "--base", "https://ajuda.sankhya.com.br",
        "--saida", str(saida_help / "ajuda-sankhya-com-br")
    ]
    res1 = subprocess.run(cmd_ajuda)
    if res1.returncode != 0:
        print("[AVISO] Extração do Ajuda retornou código diferente de zero.")

    print("\n=== [2/3] Atualizando Portal do Desenvolvedor (developer.sankhya.com.br) ===")
    cmd_dev = [
        sys.executable,
        str(extrator_py),
        "--base", "https://developer.sankhya.com.br",
        "--saida", str(saida_help / "developer-sankhya-com-br")
    ]
    res2 = subprocess.run(cmd_dev)
    if res2.returncode != 0:
        print("[AVISO] Extração do Developer retornou código diferente de zero.")

    print("\n=== [3/3] Reconstruindo catálogos indexados de busca ===")
    cmd_cat = [
        sys.executable,
        str(catalogo_py),
        str(saida_help),
        str(script_dir)
    ]
    res3 = subprocess.run(cmd_cat)

    # Propagar para as outras IAs locais caso existam e não sejam a pasta atual
    print("\n=== [4/4] Sincronizando com as IAs instaladas (Claude, Codex, AGY) ===")
    user_home = Path.home()
    destinos = [
        user_home / ".claude" / "skills" / "sankhya-ecosystem",
        user_home / ".codex" / "skills" / "sankhya-ecosystem",
        user_home / ".gemini" / "config" / "skills" / "sankhya-ecosystem",
    ]

    for dest in destinos:
        if dest.exists() and dest.resolve() != skill_dir.resolve():
            try:
                # Usa robocopy no Windows ou shutil
                if os.name == "nt":
                    subprocess.run(["robocopy", str(skill_dir), str(dest), "/E", "/NFL", "/NDL", "/NJH", "/NJS"], capture_output=True)
                print(f"✔ Sincronizado com: {dest}")
            except Exception as e:
                print(f"[AVISO] Falha ao sincronizar com {dest}: {e}")

    if res3.returncode == 0:
        print("\n✔ Atualização, reindexação e sincronização concluídas com sucesso!")
    else:
        print("\n❌ Falha ao reconstruir catálogo de busca.")

if __name__ == "__main__":
    atualizar()
