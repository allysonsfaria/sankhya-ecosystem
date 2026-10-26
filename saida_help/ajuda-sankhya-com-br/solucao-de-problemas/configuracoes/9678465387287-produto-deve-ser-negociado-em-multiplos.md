---
id: "9678465387287"
titulo: "Produto deve ser negociado em múltiplos de XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9678465387287-Produto-deve-ser-negociado-em-m%C3%BAltiplos-de-XX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:06:35Z"
rotulos: ["DUVIDANF", "Produtos", "Configuração", "Estoque", "CORE_E01987", "Negociação em Múltiplos", "Erro"]
---

# Produto deve ser negociado em múltiplos de XX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19572724990359) MENSAGEM:**

[CORE\_E01987] Produto deve ser negociado em múltiplos de XX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19572787002263) SITUAÇÃO:**

Ao confirmar o produto de unidade alternativa no portal a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19572725012119) CAUSA:**

Quando o produto possui agrupamento mínimo e é informada uma quantidade diferente das múltiplas permitidas.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19572787007255) SOLUÇÃO:**

Esse aviso acontece porque na tela Cadastro de **Produtos** (Caminho de acesso à tela: Configurações » Cadastros » Produtos) está cadastrado o agrupamento mínimo exemplo de 5,40. Desta forma, ele somente permitirá colocar na quantidade da nota múltiplos de 5,40 e não deixará colocar a quantidade 2/4/9, por exemplo. Assim, colocando um valor diferente será gerado esse aviso de erro.

![Imagem 5: O campo " Agrupamento mínimo " comporta os dados pertinentes ao agrupamento mínimo para a venda ou compra do produto,…](https://ajuda.sankhya.com.br/hc/article_attachments/19572725018263)

O campo "Agrupamento mínimo" comporta os dados pertinentes ao agrupamento mínimo para a venda ou compra do produto, ou seja, a negociação desse produto só poderá ser feita com quantidades múltiplas do valor (4 casas decimais) informado nesse campo.

**Exemplo:** Temos o produto "Ovo" com sua Unidade padrão: unidade e para ele é definido um agrupamento mínimo de 12. Na inserção do item na nota, o campo "Quantidade" deverá ser preenchido com um múltiplo de 12.

**[GIF animado: Imagem 6: Exemplo: Temos o produto "Ovo" com sua Unidade padrão: unidade e para ele é definido um agrupamento mínimo de 12. Na…](https://ajuda.sankhya.com.br/hc/article_attachments/9678442058775)

 Informando no campo Agrupamento mínimo o valor 0 (zero), será aceita qualquer quantidade na compra.**

Desta forma, caso queira que seja digitado o valor diferente de múltiplos de 5,40, por exemplo, é necessário deixar o campo em branco ou inserir o número 0. Assim, será possível digitar a quantidade desejada.
