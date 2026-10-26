---
id: "26585839620375"
titulo: "LINE 679 - PL/SQL: erro: precisão de número grande demais numérico ou de valor ORA-06512: em \"SANKHYA.SNK_MATGIRCALCSUG\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26585839620375-LINE-679-PL-SQL-erro-precis%C3%A3o-de-n%C3%BAmero-grande-demais-num%C3%A9rico-ou-de-valor-ORA-06512-em-SANKHYA-SNK-MATGIRCALCSUG"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:41:08Z"
rotulos: ["Produtos", "Estoque", "ORA-06502", "ORA-06512", "Cadastro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PL/SQL: erro: precisão de número grande demais numérico ou de valor", "Erro"]
---

# LINE 679 - PL/SQL: erro: precisão de número grande demais numérico ou de valor ORA-06512: em "SANKHYA.SNK_MATGIRCALCSUG"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26585839604375) **MENSAGEM:**

[ORA-06502] PL/SQL: erro: precisão de número grande demais numérico ou de valor ORA-06512: em "SANKHYA.SNK\_MATGIRCALCSUG", line 679 ORA-06512: em line 1

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26585839605271)SOLUÇÃO:**

![Imagem 3: O erro ocorre quando algum Estoque Mínimo foi cadastrado com uma quantidade errada no cadastro do Produto, aba "Medidas…](https://ajuda.sankhya.com.br/hc/article_attachments/26585839607063) O erro ocorre quando algum Estoque Mínimo foi cadastrado com uma quantidade errada no cadastro do Produto, aba **"Medidas e Estoque".**

**(1)** Para facilitar a busca, a consulta abaixo pode ser realizada por meio da tela DBexplorer, usando a query abaixo.

```
SELECT CODPROD, ESTMIN FROM TGFEST WHERE ESTMIN IS NOT NULL ORDER BY ESTMIN DESC
```

![Imagem 4: Caso algum valor no campo ESTMIN (estoque mínimo) esteja extremamente alto, isso pode ocasionar em problemas nos…](https://ajuda.sankhya.com.br/hc/article_attachments/26585800059799) Caso algum valor no campo ESTMIN (estoque mínimo) esteja extremamente alto, isso pode ocasionar em problemas nos cálculos quando é realizado o processo da matriz, resultando no erro. Neste caso, realize a correção no cadastro do produto e faça novamente o processamento da matriz.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26585839613719)CAUSA:**

Ocorre quando um valor de estoque mínimo/máximo é informado de forma errada.
