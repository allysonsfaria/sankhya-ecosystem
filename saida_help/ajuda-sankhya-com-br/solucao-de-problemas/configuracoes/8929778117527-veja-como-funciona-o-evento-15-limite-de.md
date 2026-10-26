---
id: "8929778117527"
titulo: "Veja como funciona o Evento 15 - Limite de Credito Mensal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8929778117527-Veja-como-funciona-o-Evento-15-Limite-de-Credito-Mensal"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:11:37Z"
rotulos: ["Configuração", "Eventos", "Parceiro", "Crédito", "Financeiro", "VALLIMCRED", "não apagar", "Limite de Crédito Mensal", "Evento 15"]
---

# Veja como funciona o Evento 15 - Limite de Credito Mensal

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16362521087383) MENSAGEM:**

Caso de uso do evento 15 - Limite de Credito Mensal.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16362514407063) SOLUÇÃO:**

Utilizando o parâmetro **"VALLIMCRED = 'Valida TUDO p/TOP c/Financeiro com provisão"** o sistema para o evento 15 sempre irá validar a primeira parcela, somente esta considerando:

[FINANCEIRO REAL C/VENC NO MÊS DA PRIMEIRA PARCELA DO LANÇAMENTO] +
[FINANCEIRO PROVISAO EXISTENTE C/VENC NO MÊS DA PRIMEIRA PARCELA DO LANÇAMENTO] +
[FINAN.REAL C/VENC NO MÊS DA PRIMEIRA PARCELA DO LANÇAMENTO BAIXADO COM DATA FUTURA] +
[FINANCEIRO PROVISAO DO LANÇAMENTO EM CURSO - SOMENTE PRIMEIRA PARCELA]

Para exemplificar geramos um pedido (que provisiona), neste foi solicitado a liberação:

Limite Crédito Mensal: 140.000,00
Mes/Ano: 10.0/2022.0
Financeiro pendente: 286.867,17 Há liberação pendente

![Evento](https://ajuda.sankhya.com.br/hc/article_attachments/15790291572247)

O Limite de Credito Mensal é definido no **"Parceiro"**, aba **"Crédito"**, campo **"Limite de Crédito Mensal"**. No exemplo utilizamos R$ 140.000,00:

![Evento](https://ajuda.sankhya.com.br/hc/article_attachments/15790291574039)

Onde havia 86.866,77 de receita real e 200.000,40 de provisão = 286.867,17 (valor solicitado)

Para ficar mais visual, criamos o seguinte filtro na Movimentação Financeira:

Financeiro.DTVENC >= ?:{desc=Data inicial mês;tipo=D} AND
Financeiro.DTVENC <= ?:{desc=Data final mês;tipo=D} AND
(Financeiro.DHBAIXA IS NULL  OR
Financeiro.DHBAIXA > ?:{entidade=Financeiro;campo=DHBAIXA})  AND
Financeiro.RECDESP = 1

![Evento](https://ajuda.sankhya.com.br/hc/article_attachments/15790281948951)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16362514410775) CAUSA:**

Como é feito o cálculo do valor solicitado na liberação do evento 15 quando utilizado o parâmetro VALLIMCRED = 'Valida TUDO p/TOP c/Financeiro com provisão.
