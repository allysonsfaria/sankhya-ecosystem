---
id: "360044597074"
titulo: "Desconto por quantidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597074-Desconto-por-quantidade"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:45:50Z"
rotulos: ["Produtos", "Configurações", "Configuração", "Desconto por quantidade manual", "TOP", "Desconto", "quantidade", "grupo", "Venda Mais"]
---

# Desconto por quantidade

As configurações descritas abaixo, orientam quanto à utilização de descontos promocionais com base na quantidade total de itens de um mesmo grupo de desconto.

![Imagem 1: Configure os parâmetros abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/31715222385943) Configure os parâmetros abaixo:

- ative o parâmetro **"Tabela de preço c/base no desconto por quantidade - CONSTABDESCQTD"**;
- Configure o parâmetro **"Regra p/ excesso em desc. por quantidade - REGRAEXCDESCQTD"** conforme as seguintes opções:

  - **Aplicar Último Desconto**: ao inserir uma quantidade maior que a informada na última faixa de desconto, o sistema considera o valor ou percentual de desconto da última faixa;

    **Exemplo**: para o um produto onde a última faixa de desconto configurada é quantidade até 5 - 10% de desconto, ao vender quantidades maiores que 5, o desconto de 10% continuará sendo aplicado.
  - **Aplicar Tabela Preço**: se preenchida uma quantidade maior que a informada na última faixa desconto, não é aplicado desconto e é considerado o valor de tabela do produto.

    **Exemplo**: para o um produto onde a última faixa de desconto configurada é quantidade até 5 - 10% de desconto, ao vender quantidades maiores que 5, o desconto não vai ser aplicado e será considerado o preço de tabela do produto.

![Imagem 2: No Cadastro de Tipos de Operação - TOP , aba Validações , a marcação "Aplica Desc. Promocional por Qtd/Grupo de Desc.…](https://ajuda.sankhya.com.br/hc/article_attachments/31715222388759) No [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes), a marcação **"Aplica Desc. Promocional por Qtd/Grupo de Desc. Prod?"** deve ser realizada:

![Imagem 3: No Cadastro de Tipos de Operação - TOP , aba Validações , a marcação "Aplica Desc. Promocional por Qtd/Grupo de Desc.…](https://ajuda.sankhya.com.br/hc/article_attachments/17086450644247)

**Observação:** com a marcação efetuada, caso o parâmetro **"Valida tipo negociação p/ desconto por quantidade? - VALDESCQTDTPV"** esteja habilitado e o campo **"Desconto Promocional"** da aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) (tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)) for igual a **"Não considerar"**, ao realizar a confirmação da nota o desconto promocional será desconsiderado. 

![Imagem 4: No Cadastro de Descontos Promocionais , define-se o campo "Tipo Desconto Produto" com a opção Grupo de Produto ; com…](https://ajuda.sankhya.com.br/hc/article_attachments/31715210717335) No [Cadastro de Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034), define-se o campo **"Tipo Desconto Produto"** com a opção Grupo de Produto; com isso, o campo **"Grupo Desconto Produto/Serviço"** será habilitado para preenchimento do Grupo de Produtos desejado. Feito isso, ainda nesta mesma tela, define-se o campo **"Usa desconto por quantidade"** com a opção por Grupo. Além disso, a aba Descontos por quantidade deve ser devidamente definida com as respectivas quantidades e percentuais/valores de desconto. 

![Imagem 5: A regra de desconto promocional não é aplicada ao faturar múltiplos documentos em uma única nota. Isso ocorre porque,…](https://ajuda.sankhya.com.br/hc/article_attachments/26077197599511) A regra de desconto promocional não é aplicada ao faturar múltiplos documentos em uma única nota. Isso ocorre porque, nesse caso, o valor unitário do item informado não reflete o desconto promocional, uma vez que o cálculo é feito com base no valor total dividido pela quantidade.

**Nota:** a descrição do Grupo de Descontos da tela Descontos Promocionais necessita ser a mesma que a do Grupo de Descontos do Cadastro de Produtos.

O sistema apenas realizará o cálculo do desconto se na tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), a opção **"Calcular VLR de tabela considerando Desc. por Qtd. e grupo de Desc de produto"** encontrar-se selecionada.

![Imagem 6: O sistema apenas realizará o cálculo do desconto se na tela Central de Vendas , grade Itens , botão Outras Opções... ,…](https://ajuda.sankhya.com.br/hc/article_attachments/17086441995927)

Caso o parâmetro de chave CONSTABDESCQTD esteja desabilitado, o campo **"Usa desconto por quantidade"** será exibido apenas para ser ou não assinalado (checkbox), ou seja, será possível somente definir se ocorrerá ou não o uso de desconto por quantidade.

![Imagem 7: Quando o desconto por quantidade for utilizado, não será possível aplicar acréscimos (descontos negativos).](https://ajuda.sankhya.com.br/hc/article_attachments/26077197599511) Quando o desconto por quantidade for utilizado, não será possível aplicar acréscimos (descontos negativos).

![Imagem 8: No Cadastro de Produtos , aba Venda , determina-se nos itens desejados qual Grupo Desconto os mesmos farão parte:](https://ajuda.sankhya.com.br/hc/article_attachments/31715210718871) No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Venda, determina-se nos itens desejados qual Grupo Desconto os mesmos farão parte:

![Imagem 9: No Cadastro de Produtos , aba Venda , determina-se nos itens desejados qual Grupo Desconto os mesmos farão parte:](https://ajuda.sankhya.com.br/hc/article_attachments/17086604649495)

Para que o desconto seja aplicado e o valor unitário recalculado, é necessário executar o tópico 5:

![Imagem 10: Feitas as configurações relatadas acima, na Central de Vendas ao proceder com o lançamento de um Pedido ou Nota de…](https://ajuda.sankhya.com.br/hc/article_attachments/31715222392087) Feitas as configurações relatadas acima, na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ao proceder com o lançamento de um Pedido ou Nota de Venda, no botão Outras Opções presente na grade de Itens, tem-se a opção **"Calcular Vlr de tabela considerando Desc. por Qtd e Grupo de Desc. de Produto"**, que ao ser acionada, tem-se o recálculo dos valores unitários dos itens correspondentes ao grupo de desconto anteriormente definido:

![Imagem 11: Feitas as configurações relatadas acima, na Central de Vendas ao proceder com o lançamento de um Pedido ou Nota de…](https://ajuda.sankhya.com.br/hc/article_attachments/17086441995927)

A opção Calcular Vlr de tabela considerando Desc. por Qtd e Grupo de Desc. de Produto realiza a busca em todas as tabelas de descontos pelo **"Grupo Desconto Produto/Serviço"** comparando com o "**Grupo Desconto"** da aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda) da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#top). Desta forma o desconto é identificado independente da tabela de preço.

**Observação:** caso a opção não seja utilizada, o recálculo também será feito após confirmação da nota.

Vale salientar que a opção mencionada (Calcular Vlr de tabela considerando Desc. por Qtd e Grupo de Desc. de Produto) será disponibilizada para uso, apenas se o parâmetro de chave CONSTABDESCQTD estiver habilitado e os documentos trabalhados na Central de Vendas sejam Pedidos ou Notas de Venda.

![Imagem 12: Caso uma tabela de preço esteja informada nos Descontos Promocionais , ela será levada em consideração durante a…](https://ajuda.sankhya.com.br/hc/article_attachments/26077197599511) Caso uma tabela de preço esteja informada nos [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais), ela será levada em consideração durante a aplicação do desconto, independente da tabela à qual o vendedor esteja vinculado.

Além disso, quando houver mais de uma promoção dentro do mesmo período e com a mesma data inicial, o sistema organizará as promoções considerando primeiro a data e, em seguida, o número da promoção. Assim, será sempre aplicada a promoção mais recente dentro daquele período.
