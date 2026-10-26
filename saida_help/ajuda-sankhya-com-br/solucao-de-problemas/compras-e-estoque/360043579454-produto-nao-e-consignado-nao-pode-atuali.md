---
id: "360043579454"
titulo: "Produto não é consignado, não pode atualizar estoque de terceiros e próprio simultaneamente "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579454-Produto-n%C3%A3o-%C3%A9-consignado-n%C3%A3o-pode-atualizar-estoque-de-terceiros-e-pr%C3%B3prio-simultaneamente"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:30Z"
rotulos: ["#RevisadoCarmen", "Produtos", "Configuração", "Parceiro", "TOP", "Estoque", "ORA-20101", "Atualização de Estoque", "Erro ORA-20101", "Parceiro consignante"]
---

# Produto não é consignado, não pode atualizar estoque de terceiros e próprio simultaneamente 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108331898391) MENSAGEM:**

ORA-20101: Produto não é consignado, não pode atualizar estoque de terceiros e próprio simultaneamente.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108331900695) SITUAÇÃO:**

Ao tentar confirmar uma nota de Compra, pelo **"Portal de Compras"** é retornada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108331901975) SOLUÇÃO:**

Para correção, siga os passos abaixo:

(1)** Cenário 1:** Caso a atualização de estoque tenha que ser **"Atualizar Estoque Próprio e Estoque de Terceiro"**.

**(2)** Insira no campo **"Parceiro Consignante"** um valor correspondente ao Parceiro da Nota. O campo fica disponível na aba **"Geral"** no Cadastro de **"[Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos).

(1)** Cenário 2:** Caso a atualização de estoque não deve atualizar estoque próprio e de terceiro.

**(2)** Ajuste no cadastro da TOP (Caminho para acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) as atualizações:

**(3)** Aba **"[Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)",**Campo "**Atualização do Estoque".** Para atualização de estoque próprio.

**(3)** Aba **"[Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros)",** Campo **"Estoque com/de Terceiros".** Para atualização de estoque de Terceiro.

**(2)** Ajustar para atualizar somente uma das condições, de acordo com a movimentação da Nota.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16108364577559) CAUSA:**

Ocorre para movimentações de comodato, consignação ou produtos para produção externa, quando é necessário atualizar ambos os estoque e não possui parceiro consignante no(s) cadastro(s) do(s) produto(s).
