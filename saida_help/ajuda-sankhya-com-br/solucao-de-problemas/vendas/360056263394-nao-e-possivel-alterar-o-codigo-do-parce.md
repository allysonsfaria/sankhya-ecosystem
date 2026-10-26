---
id: "360056263394"
titulo: "Não é possível alterar o código do parceiro quando o lançamento atualiza estoque de terceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056263394-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-c%C3%B3digo-do-parceiro-quando-o-lan%C3%A7amento-atualiza-estoque-de-terceiros"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:27:18Z"
rotulos: ["Configuração", "Parceiro", "TOP", "Estoque", "Financeiro", "não apagar", "CORE_E05148", "Alteração de parceiro não permitida em estoque de terceiros", "Bloqueio para manter integridade fiscal", "Faça ajuste manual; não altere parceiro em lançamentos"]
---

# Não é possível alterar o código do parceiro quando o lançamento atualiza estoque de terceiros

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17270469133463) MENSAGEM:**

Não é possível alterar o código do parceiro quando o lançamento atualiza estoque de terceiros

[CORE\_E05148] Parceiro não pode ser alterado em TOP que atualizam estoque de Terceiros

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17270492979223) SOLUÇÃO:**

- Lançamentos em que a TOP atualiza estoque **de** ou **com** terceiros não permitirá alterações do campo **"Parceiro"**;
- Esse bloqueio ocorre para manter a integridade dos processos de geração das obrigações fiscais, relacionadas a estoque de terceiros.

![Imagem 3: Com isso, não é possível duplicar um lançamento com Tipos de Operação nessas condições (atualiza estoque de terceiros)…](https://ajuda.sankhya.com.br/hc/article_attachments/17270492983575) Com isso, não é possível duplicar um lançamento com Tipos de Operação nessas condições (atualiza estoque de terceiros) e, em seguida, tentar alterar o parceiro.

- Recomenda-se que um lançamento manual seja realizado, com as informações desejadas.

![Imagem 4: Também não será permitido alterar o parceiro para uma nota de remessa durante o processo de faturamento, considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/17270469141143) Também não será permitido alterar o parceiro para uma nota de remessa durante o processo de faturamento, considerando que o parceiro da nota origem é o parceiro esperado/válido para esse processo.

- Se o lançamento origem foi feito incorretamente, com o parceiro errado, proceda com as respectivas exclusões e/ou cancelamentos corrigindo todos os documentos relacionados. E após isso refaça os lançamentos.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17270492991255) CAUSA:**

TOP configurada para atualizar estoque **de** ou **com** terceiros ao informar parceiro no lançamento e salvar o sistema grava esta informação para este lançamento e não permitirá mais alterar o parceiro.
