---
id: "360044041254"
titulo: "Definições de custo de produção e conceito de cálculo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044041254-Defini%C3%A7%C3%B5es-de-custo-de-produ%C3%A7%C3%A3o-e-conceito-de-c%C3%A1lculo"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-07-22T15:55:42Z"
rotulos: ["Produtos", "Custos", "Configuração", "Estoque", "Financeiro", "Componentes e Valores: Somatório de produtos", "Custo de Produção: Processo produtivo", "Cálculo Detalhado: Definições específicas"]
---

# Definições de custo de produção e conceito de cálculo

(1)** CUSTO DE PRODUÇÃO (CÁLCULO)**

Os **custos de produção** são aqueles ligados ao processo produtivo, podendo ser divididos em **custos** indiretos, material direto e mão-de-obra direta, ou seja, todos os itens que são obrigatórios no processo produtivo.

![Imagem 1: Veja as definições e como é o conceito do cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/16815679594647)Veja as definições e como é o conceito do cálculo:

(1)** CUSREP**: o valor desse campo vem da TGFCUSITE da nota de produção em questão. O cálculo da TGFCUSITE é simplesmente o somatório do produto entre QTD e TGFCUS.CUSREP das MPs (última data).

(1)** ENTRADASEMICMS**: o valor desse campo vem da TGFCUSITE da nota de produção em questão. O cálculo da TGFCUSITE é simplesmente o somatório do produto entre QTD e TGFCUS.CUSSEMICM das MPs (última data).

(1)** ENTRADACOMICMS**: o valor desse campo vem da TGFCUSITE da nota de produção em questão. O cálculo da TGFCUSITE é simplesmente o somatório do produto entre QTD e TGFCUS.CUSMEDICM das MPs (última data).

**(1)** **CUSVARIAVEL**: o valor desse campo vem da TGFCUSITE da nota de produção em questão. O cálculo da TGFCUSITE é simplesmente o somatório do produto entre QTD e TGFCUS.CUSVARIAVEL das MPs (última data).

(1)** CUSMED**: o valor desse campo vem de todas TGFCUSITE de notas de produção do produto em questão. ((ACusComCal \* EA) + (NCusComCal\* QC)) / (EA + QC)

Onde:
•AcusComCal: Custo Médio com ICMS Anterior
•EA: Estoque Anterior
•NCusComCal: Novo Custo Médio com ICMS
•QC: Quantidade Comprada (Entrada)
