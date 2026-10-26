---
id: "14865147663511"
titulo: "Os seguintes produtos já existem em alguma cotação para a empresa  com o situação igual a \"Aberta\", portanto não é possível incluí-los. Produtos: XXXXXX - Altere o produto ou volte para a rotina de cotação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14865147663511-Os-seguintes-produtos-j%C3%A1-existem-em-alguma-cota%C3%A7%C3%A3o-para-a-empresa-com-o-situa%C3%A7%C3%A3o-igual-a-Aberta-portanto-n%C3%A3o-%C3%A9-poss%C3%ADvel-inclu%C3%AD-los-Produtos-XXXXXX-Altere-o-produto-ou-volte-para-a-rotina-de-cota%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-05T15:23:20Z"
rotulos: ["Produtos", "Configuração", "Cotação", "CORE_E00275", "Parâmetro", "Produtos já existem em cotação aberta", "Ajuste o parâmetro para permitir repetição", "Produto repetido e parâmetro não permite", "Erro"]
---

# Os seguintes produtos já existem em alguma cotação para a empresa  com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos: XXXXXX - Altere o produto ou volte para a rotina de cotação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16620955475351) MENSAGEM:**

[CORE\_E00275]: Os seguintes produtos já existem em alguma cotação para a empresa com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos: XXXXXX - Altere o produto ou volte para a rotina de cotação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16620943747991)SOLUÇÃO:**

Caso o produto a ser inserido seja repetido na mesma cotação e o parâmetro esteja configurado para não permitir a inserção; tem-se a exibição da seguinte mensagem:

**"Os seguintes produtos já existem em alguma cotação para a empresa X com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos:**

**Y - "NOMEDOPRODUTO"**

Através do parâmetro **"Código p/ produto genérico na cotação - CODPRODGENCOT"**, o comprador permite ou não o lançamento de produtos repetidos na cotação. O parâmetro pode ser configurado com três valores:

(1)** -1 (menos um):** caso seja informado este valor, todo e qualquer produto poderá se repetir no lançamento da cotação;

(1)** 0 (zero):** informando este valor, nenhum produto poderá se repetir no lançamento da cotação;

(1)** Valor maior que 0:** neste caso, deve-se informar o código do produto que poderá se repetir, sendo permitida repetição somente para este produto no lançamento da cotação.

![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16620943750039) **OBSERVAÇÃO:**

Caso o produto esteja sendo inserido com o mesmo controle, codvol e codlocal iguais, a aplicação entende que se trata do mesmo produto. Então, este só pode ter um fornecedor aprovado associado ao mesmo produto. Caso o produto possua controle ou codlocal diferentes, o sistema não barra o processo.

![Imagem 4: Caso o produto esteja sendo inserido com o mesmo controle, codvol e codlocal iguais, a aplicação entende que se trata…](https://ajuda.sankhya.com.br/hc/article_attachments/14865242862231)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16620955484567)CAUSA:**

Ocorre quando o produto é repetido e o parâmetro CODPRODGENCOT  não permite produto repetido.
