---
id: "26507969297815"
titulo: "A subconsulta de uma única linha retorna mais de uma linha - Análise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26507969297815-A-subconsulta-de-uma-%C3%BAnica-linha-retorna-mais-de-uma-linha-An%C3%A1lise-de-Giro"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:41:50Z"
rotulos: ["Custos", "Configuração", "Análise de Giro", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "ORA-01427", "A subconsulta de uma única linha retorna mais de uma linha", "Erro"]
---

# A subconsulta de uma única linha retorna mais de uma linha - Análise de Giro

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26507969277207) **MENSAGEM:**

[ORA-01427] A subconsulta de uma única linha retorna mais de uma linha

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26507969278103)SOLUÇÃO:**

O erro ocorre pois existem custos duplicados, nos quais um mesmo produto possui mais de uma linha de custo para a mesma data.

![Imagem 3: Para identificar os custos duplicados realize uma consulta, por meio do banco de dados, que mostra todos os custos…](https://ajuda.sankhya.com.br/hc/article_attachments/26507931577751) Para identificar os custos duplicados realize uma consulta, por meio do banco de dados, que mostra todos os custos duplicados.

**(2)**Se o parâmetro **"CUSTOPORCONT - Custo por controle"** estiver desligado:

```
SELECT CODPROD , CODEMP , DTATUAL, COUNT(1) FROM TGFCUS GROUP BY CODPROD , CODEMP , DTATUAL HAVING COUNT(1) > 1 ORDER BY DTATUAL DESC, CODPROD;
```

**(2)**Se o parâmetro CUSTOPORCONT - Custo por controle estiver ligado:

```
SELECT CODPROD,DTATUAL,CONTROLE,COUNT(1) FROM TGFCUS GROUP BY CODPROD,DTATUAL,CONTROLE HAVING COUNT(1) > 1
```

**(1)**Se a consulta acima resultar em alguma linha, mostra que existem custos duplicados.

**(1)**A causa mais provável é a alteração dos parâmetros: **"CUSTOPOREMP", "CUSTOPORLOC"** e CUSTOPORCONT. Uma vez que configurados e gerado linhas de custo, não e recomendado alteração, pois pode ocasionar na geração de mais de uma linha de custo para a mesma data.

![Imagem 4: Para solução, revise os três parâmetros citados acima e configure de acordo com a necessidade da empresa. Para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/26507931582487) Para solução, revise os três parâmetros citados acima e configure de acordo com a necessidade da empresa. Para que o custo duplicado seja excluído, recalcule o custo na data em questão (por meio da tela **"Recálculo de Custos"**, de preferência filtrando o produto).

**Importante:**  o recálculo do custo pode ocasionar divergência fiscal/contábil, então antes de realizar o processo é necessário o acompanhamento de um responsável da área ou da unidade responsável.

![Imagem 5: Após corrigir os custos, acesse o agendamento da análise de giro e limpe a TGFGIR. Isso fará com que a consolidação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/26507969287703) Após corrigir os custos, acesse o agendamento da análise de giro e limpe a TGFGIR. Isso fará com que a consolidação dos dados seja refeita de imediato, levando os custos de forma correta.  

![Imagem 6: Após corrigir os custos, acesse o agendamento da análise de giro e limpe a TGFGIR. Isso fará com que a consolidação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/26641316386839)

![Imagem 7: Após corrigir os custos, acesse o agendamento da análise de giro e limpe a TGFGIR. Isso fará com que a consolidação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/26641316389271)

![Imagem 8: Após refazer a consolidação, clique em Processar Matriz.](https://ajuda.sankhya.com.br/hc/article_attachments/26507931591703) Após refazer a consolidação, clique em Processar Matriz.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26507931592087)CAUSA:**

Alterações incorretas dos parâmetros de custo quando já existe custo causam sua duplicidade. Isso trava não só a análise de giro, mas também demais rotinas que lê o custo do produto.
