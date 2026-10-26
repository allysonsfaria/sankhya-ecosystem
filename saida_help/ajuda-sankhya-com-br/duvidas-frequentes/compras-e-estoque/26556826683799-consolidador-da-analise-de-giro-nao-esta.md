---
id: "26556826683799"
titulo: "Consolidador da Análise de Giro não está executando depois de alterar o parâmetro CUSTOPOREMP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26556826683799-Consolidador-da-An%C3%A1lise-de-Giro-n%C3%A3o-est%C3%A1-executando-depois-de-alterar-o-par%C3%A2metro-CUSTOPOREMP"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:41:25Z"
rotulos: ["Custos", "CUSTOPORCONT", "CUSTOPOREMP", "CUSTOPORLOC", "Configuração", "Análise de Giro", "Estoque", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Consolidador da Análise de Giro não está executando"]
---

# Consolidador da Análise de Giro não está executando depois de alterar o parâmetro CUSTOPOREMP

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26565818758167) **SITUAÇÃO:**

Consolidador da Análise de Giro não está executando, conforme imagem abaixo:

![Imagem 2: Consolidador da Análise de Giro não está executando, conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/26556826671127)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26556780172439)SOLUÇÃO:**

Execute no dbexplore o comando  SELECT CODPROD , CODEMP , DTATUAL, COUNT(1) FROM TGFCUS GROUP BY CODPROD , CODEMP , DTATUAL HAVING COUNT(1) > 1 ORDER BY DTATUAL DESC, CODPROD

![Imagem 4: Execute no dbexplore o comando SELECT CODPROD , CODEMP , DTATUAL, COUNT(1) FROM TGFCUS GROUP BY CODPROD , CODEMP ,…](https://ajuda.sankhya.com.br/hc/article_attachments/26556780175255)

Serão apresentados os produtos que tenham custos duplicados. Nesse caso, será preciso recalcular os custos. Vale destacar que **essa operação deve ser feita por pessoas que entendam bem do processo.**

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26556780176535)CAUSA:**

Essa questão de custos duplicados normalmente ocorre quando os parâmetros **CUSTOPORCONT, CUSTOPORLOC ou CUSTOPOREMP** são ligados ou desligados e os custos não são recalculados.
