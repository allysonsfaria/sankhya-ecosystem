---
id: "18160411874327"
titulo: "Qual configuração é necessária para preencher o local campo (CODLOCAL) na tabela de endereço \"TGWEND\" e a de estoque \"TGWEST\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18160411874327-Qual-configura%C3%A7%C3%A3o-%C3%A9-necess%C3%A1ria-para-preencher-o-local-campo-CODLOCAL-na-tabela-de-endere%C3%A7o-TGWEND-e-a-de-estoque-TGWEST"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:52:46Z"
rotulos: ["Configuração", "WMS", "Estoque", "Configuração do Campo CODLOCAL nas Tabelas TGWEND e TGWEST", "TGWEST", "CODLOCAL", "TGWEND"]
---

# Qual configuração é necessária para preencher o local campo (CODLOCAL) na tabela de endereço "TGWEND" e a de estoque "TGWEST"

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18198110496663) **SITUAÇÃO:**

Duvida sobre qual momento ou qual configuração é necessária para que o local campo (CODLOCAL) na tabela de endereço "TGWEND" e a de estoque "TGWEST" seja informado e como o sistema do WMS se comporta com esses campos preenchidos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18160414420119)SOLUÇÃO:**

O Local é representado pelo campo CODLOCAL nas tabelas TGWEND (endereço de armazenamento) e TGWEST (Estoque WMS), o sistema nativamente não preenche o referido campo, ficando ele com o valor '0',  visto que, o WMS não valida local e sim o endereço de armazenamento do produto.
