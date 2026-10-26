---
id: "360044597014"
titulo: "Porporcionalização de PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597014-Porporcionaliza%C3%A7%C3%A3o-de-PIS-COFINS"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:45:44Z"
rotulos: ["Configuração", "Porporcionalização de PIS/COFINS", "Porporcionalização de PIS/COFINS manual", "COFINS", "PIS", "Impostos", "Financeiro", "Proporcionalização de PIS/COFINS: Roteiro Simplificado", "EFD Contribuições"]
---

# Porporcionalização de PIS/COFINS

#### Cálculo da Proporcionalização dos campos de Pé de Nota

É muito parecido em relação às marcações na aba **"Despesas Acessórias"** do cadastro de TOPs.

Para todos os impostos a regra segue a mesma, só possui algumas diferenciações como alguns impostos haver redução de base de cálculo, porém, a lógica é a mesma para todos:

Consideremos um exemplo:

Item 1 - Total (qtd x vlrunit): 8,00 - 8/16 = 0,50 = 50%

Item 2 - Total (qtd x vlrunit): 4,00 - 4/16 = 0,25 = 25%  

Item 3 - Total (qtd x vlrunit): 4,00 - 4/16 = 0,25 = 25%

Total dos Itens: 16,00

Vlr do Frete Total: 10,00

Vlr do Frete Proporcional:

Item 1 - Total:5,00

Item 2 - Total:2,50

Item 3 - Total:2,50

No caso de PIS e COFINS, o cálculo segue o seguinte roteiro a cada nota:

- O que for escrito abaixo para PIS, vale também para o COFINS.

- Buscamos na TGFDIN todas as linhas que possuem o imposto PIS e com incidência igual à Geral ou Produto ou Serviço, ou seja, o valor do PIS normal que cada item da nota calculou (PIS normal está sempre na incidência igual à Geral).
- Para que haja a proporcionalização do PIS/COFINS, é necessário que os itens possuam o cálculo de PIS/COFINS.
