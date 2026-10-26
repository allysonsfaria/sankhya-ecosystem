---
id: "21512545337751"
titulo: "Quantidade vendida não é levada para Análise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21512545337751-Quantidade-vendida-n%C3%A3o-%C3%A9-levada-para-An%C3%A1lise-de-Giro"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:50:08Z"
rotulos: ["Produtos", "Configuração", "Portal de Vendas", "Análise de Giro", "TOP", "Estoque"]
---

# Quantidade vendida não é levada para Análise de Giro

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21891439286423) **SITUAÇÃO:**

Quando a quantidade de venda dos produtos na análise de giro é 0 (zero) ou apresenta divergências em relação ao portal de vendas/gerência de produtos. É necessário verificar alguns pontos para garantir que a quantidade correta seja levada após o processo da matriz.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21512545329047)CAUSA:**

Ocorre quando a nota de venda não atende aos requisitos acima, onde ela é desconsiderada ou pode ocasionar no travamento do Job consolidador responsável por coletar as informações de quantidades vendidas (giro) e levar para Análise de Giro.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21512545303831) **SOLUÇÃO:**

**(1)** Os requisitos informados abaixo, devem ser seguidos, pois caso contrário, a quantidade vendida não será levada para análise de giro, o que pode resultar em divergências nos cálculos da sugestão de compra giro.

**(1)** Para realizar os testes, utilize uma nota de venda como exemplo, que tenha sido negociada dentro do período informado na Análise de giro.

![Imagem 4: A nota deverá estar confirmada;](https://ajuda.sankhya.com.br/hc/article_attachments/21891454158999) A nota deverá estar confirmada;

![Imagem 5: O valor total da nota (cabeçalho) e o valor unitário do item vendido, precisam ser maior que zero;](https://ajuda.sankhya.com.br/hc/article_attachments/21891439335063) O valor total da nota (cabeçalho) e o valor unitário do item vendido, precisam ser maior que zero;

![Imagem 6: A TOP de venda deverá ter a configuração de Análise de Giro;](https://ajuda.sankhya.com.br/hc/article_attachments/21891454188439) A TOP de venda deverá ter a configuração de Análise de Giro;

![Imagem 7: A TOP de venda deverá ter a configuração de Análise de Giro;](https://ajuda.sankhya.com.br/hc/article_attachments/21891439360023)

![Imagem 8: No cadastro do produto deverá ter a marcação 'Calcula Giro pelo Agendador' ( Produto » aba Medidas e Estoque );](https://ajuda.sankhya.com.br/hc/article_attachments/21891454204951) No cadastro do produto deverá ter a marcação 'Calcula Giro pelo Agendador' (Produto » aba Medidas e Estoque);

![Imagem 9: No cadastro do produto deverá ter a marcação 'Calcula Giro pelo Agendador' ( Produto » aba Medidas e Estoque );](https://ajuda.sankhya.com.br/hc/article_attachments/21891439389847)

![Imagem 10: Obrigatoriamente o produto vendido precisar ter CUSTO com data igual ou anterior a nota de venda realizada;](https://ajuda.sankhya.com.br/hc/article_attachments/21891454244503) Obrigatoriamente o produto vendido precisar ter **CUSTO** com data igual ou anterior a nota de venda realizada;

![Imagem 11: O tipo e o tamanho dos campos entre as tabelas TGFPRO e TGFGIR devem ser idênticas ao banco de dados. Segue abaixo…](https://ajuda.sankhya.com.br/hc/article_attachments/21891454269207) O **tipo** e o **tamanho** dos campos entre as tabelas TGFPRO e TGFGIR devem ser idênticas ao banco de dados. Segue abaixo consulta que auxiliará na comparação:

**(1)** SQL:

```
SELECT PRO.NAME AS COLUNA,

TYPE_NAME(PRO.XTYPE) AS TIPO_PRO,

PRO.LENGTH AS TAMANHO_PRO,

TYPE_NAME(GIR.XTYPE) AS TIPO_GIR,

GIR.LENGTH AS TAMANHO_GIR

FROM SYSCOLUMNS PRO, SYSCOLUMNS GIR WHERE PRO.ID = OBJECT_ID('TGFPRO') AND GIR.ID = OBJECT_ID('TGFGIR')

AND PRO.NAME = GIR.NAME

AND (TYPE_NAME(PRO.XTYPE) <> TYPE_NAME(GIR.XTYPE) OR PRO.LENGTH <> GIR.LENGTH)
```

**(1)** ORACLE:

```
SELECT * FROM (SELECT PRO.COLUMN_NAME AS COLUNA,

PRO.DATA_TYPE AS TIPO_PRO,

CAST(PRO.DATA_LENGTH AS NUMBER) AS TAMANHO_PRO,

GIR.DATA_TYPE AS TIPO_GIR,

CAST(GIR.DATA_LENGTH AS NUMBER) AS TAMANHO_GIR

FROM USER_TAB_COLUMNS PRO, USER_TAB_COLUMNS GIR WHERE PRO.TABLE_NAME = 'TGFPRO'

AND GIR.TABLE_NAME = 'TGFGIR' AND PRO.COLUMN_NAME = GIR.COLUMN_NAME) X

WHERE X.TAMANHO_PRO <> X.TAMANHO_GIR
```

![Imagem 12: O produto não poderá ter o custo duplicado, ou seja, custo com a mesma data para o mesmo produto. Segue abaixo consulta…](https://ajuda.sankhya.com.br/hc/article_attachments/21891454284311) O produto não poderá ter o custo duplicado, ou seja, custo com a mesma data para o mesmo produto. Segue abaixo consulta que auxiliará na identificação do custo duplicado, que pode ocasionar o travamento do Job consolidador:

**(1)** Execute a consulta abaixo referente ao parâmetro CUSTOPORCONT (Custo por controle):

**(2)**Se estiver desligado:

```
SELECT CODPROD , CODEMP , DTATUAL, COUNT(1) FROM TGFCUS GROUP BY CODPROD , CODEMP , DTATUAL HAVING COUNT(1) > 1 ORDER BY DTATUAL DESC, CODPROD
```

**(2)**Se estiver ligado:

```
SELECT CODPROD,DTATUAL,CONTROLE,COUNT(1) FROM TGFCUS GROUP BY CODPROD,DTATUAL,CONTROLE HAVING COUNT(1) > 1
```

![Imagem 13: É necessário existir uma referência de Custo Variável para cada empresa analisada. Na tela Gerente On-Line - GOL (…](https://ajuda.sankhya.com.br/hc/article_attachments/21891439475991) É necessário existir uma referência de Custo Variável para cada empresa analisada. Na tela Gerente On-Line - GOL (Comercial » Gerente), abra as configurações e acesse a aba Margem de contribuição.

**(1)** O ano de referência deve ser anterior ao período de negociação da nota utilizada.

![Imagem 14: (1) O ano de referência deve ser anterior ao período de negociação da nota utilizada.](https://ajuda.sankhya.com.br/hc/article_attachments/21891454327831)

![Imagem 15: Verifique se a Matriz analisada possui algum filtro que impeça o item de levar sua quantidade vendida. Na tela Análise…](https://ajuda.sankhya.com.br/hc/article_attachments/21891439502359) Verifique se a Matriz analisada possui algum filtro que impeça o item de levar sua quantidade vendida. Na tela Análise de Giro (Comercial » Rotinas), abra as configurações e acesse a aba Outras Configurações.

![Imagem 16: Verifique se a Matriz analisada possui algum filtro que impeça o item de levar sua quantidade vendida. Na tela Análise…](https://ajuda.sankhya.com.br/hc/article_attachments/21891439516951)

![Imagem 17: Após verificar os itens acima, certifique-se de que o Job de consolidação da Análise de giro esteja rodando.](https://ajuda.sankhya.com.br/hc/article_attachments/21891454390551) Após verificar os itens acima, certifique-se de que o Job de consolidação da Análise de giro esteja rodando.

![Imagem 18: Após verificar os itens acima, certifique-se de que o Job de consolidação da Análise de giro esteja rodando.](https://ajuda.sankhya.com.br/hc/article_attachments/21891454407831)

![Imagem 19: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/21891439567511)**IMPORTANTE:**

Se após seguir as orientações e aguardar o horário agendado o problema persistir, acione o time de Service Desk.

**Observação:** Existem operações que, apesar de ser uma saída (baixa no estoque) não devem ser consideradas no processo de ANALISE DE  GIRO  (Ex:  Doações,  registros de Perdas, Ajustes etc.)
