---
id: "43471435077015"
titulo: "Erro de metadados ao abrir o Portal de Vendas 'TGFPAR-->ASYCONSULTAID'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43471435077015-Erro-de-metadados-ao-abrir-o-Portal-de-Vendas-TGFPAR-ASYCONSULTAID"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-01T11:57:36Z"
---

# Erro de metadados ao abrir o Portal de Vendas 'TGFPAR-->ASYCONSULTAID'

**MENSAGEM**

Erro interno Não foi possível resolver os metadados da entidade 'CabecalhoNota-pt\_BR'. Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno: Metadados do campo 'TGFPAR-->ASYCONSULTAID' não inicializados.

**SITUAÇÃO**

Este erro ocorre ao tentar acessar telas criticas do sistema tais como: **"Portal de Vendas"**e **"Portal de Compras"**após atualização para as versões recentes do Sankhya.

**SOLUÇÃO**

Deve ser realizada a reinicialização das Unidades de Dados das seguintes tabelas e respectivas instâncias:

Esse processo deve ser feito usando a tela **''Dicionário de Dados''** (Configurações » Avançado).

**TGFCAB**

- CabecalhoNota

**TGFVEI**

- Veiculo

**TGFPAR**

- Parceiro

**Feito os processos, realize a limpeza de cache acessando a 'Administração de servidor >> Descartar Cache'.**
