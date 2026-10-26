---
id: "36294145879447"
titulo: "Erro: \"ORA-01795: o número máximo de expressões em uma lista é de 1000\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36294145879447-Erro-ORA-01795-o-n%C3%BAmero-m%C3%A1ximo-de-express%C3%B5es-em-uma-lista-%C3%A9-de-1000"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:23:12Z"
rotulos: ["Produtos", "Oracle", "Requisição", "API", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "ORA-1795", "Cláusula IN", "1000 valores"]
---

# Erro: "ORA-01795: o número máximo de expressões em uma lista é de 1000"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36294145849239) **MENSAGEM:**

**ORA-01795: o número máximo de expressões em uma lista é de 1000**

![Imagem 2: ORA-01795: o número máximo de expressões em uma lista é de 1000](https://ajuda.sankhya.com.br/hc/article_attachments/36493822655511)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36294155897879)SOLUÇÃO:**

**(1)** **Revise a requisição** para garantir que a cláusula **IN** não ultrapasse o limite máximo de **1000 valores,** imposto pelo Oracle.

**(2)** Se for necessário tratar um volume maior de registros, utilize alternativas como **paginação**, **filtros de faixa** ou **divisão da consulta** em blocos menores.

Essas abordagens evitam que o limite do Oracle seja excedido e asseguram que a consulta seja executada corretamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36294155898135)CAUSA:**

O erro ocorre pois o banco Oracle possui uma limitação de até 1000 valores na clausula **IN**.

Neste cenário, a consulta enviada pela requisição via API continha mais de 1000 códigos de produto, ultrapassando o limite e gerando a falha.
