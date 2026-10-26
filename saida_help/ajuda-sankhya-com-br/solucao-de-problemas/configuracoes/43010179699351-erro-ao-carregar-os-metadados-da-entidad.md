---
id: "43010179699351"
titulo: "Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno. Metadados do campo 'TGFORD->HORAENTRADA' não inicializados."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43010179699351-Erro-ao-carregar-os-metadados-da-entidade-CabecalhoNota-Erro-interno-Metadados-do-campo-TGFORD-HORAENTRADA-n%C3%A3o-inicializados"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-02T12:34:18Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "metadados", "Plataforma - KCS", "Documentos Eletrônicos", "CabecalhoNota", "TGFORD->HORAENTRADA", "HORAENTRADA"]
---

# Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno. Metadados do campo 'TGFORD->HORAENTRADA' não inicializados.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/43010231688215) **MENSAGEM:**

Erro interno
Não foi possível resolver os metadados da entidade
'CabecalhoNota-pt\_BR'.
Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno. Metadados do campo 'TGFORD->HORAENTRADA' não
inicializados.

**SITUAÇÃO**

Este erro ocorre ao tentar acessar telas criticas do sistema tais como: **"Portal de Vendas"**e **"Portal de Compras"**após atualização para as versões recentes do Sankhya.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/43010231689879)SOLUÇÃO:**

Deve ser realizada a reinicialização da Unidade de Dado da seguinte tabela:

**TGFORD**

- OrdemCarga

**TGFFIN**

- Financeiro

Esse processo deve ser feito usando a tela Dicionário de Dados (Configurações >> Avançado) conforme vídeo abaixo.

[GIF animado: Imagem 3: Esse processo deve ser feito usando a tela Dicionário de Dados (Configurações >> Avançado) conforme vídeo abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/43010750439447)
