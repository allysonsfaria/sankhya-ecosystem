---
id: "30653008420119"
titulo: "Importador de Dados - Erro: Registro já existente na Tabela de Preços para esta Data de Vigor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30653008420119-Importador-de-Dados-Erro-Registro-j%C3%A1-existente-na-Tabela-de-Pre%C3%A7os-para-esta-Data-de-Vigor"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-01T02:38:22Z"
rotulos: ["Produtos", "Configuração", "Importação", "Importador de dados", "Erro: Registro já existente na Tabela de Preços", "para esta Data de Vigor", "Erro", "Artigo atualizado KCS", "CVE - KCS", "Tabela de Preços"]
---

# Importador de Dados - Erro: Registro já existente na Tabela de Preços para esta Data de Vigor

**MENSAGEM:**

Registro já existente na Tabela de Preços para esta Data de Vigor. Cód.Produto: X Cód.Local: Y Controle: Z

**SITUAÇÃO:**

**(1)** Ao realizar uma importação de dados usando como modelo a "**Tabela de preço por produto**", ocorre o erro abaixo. A mesma lógico pode ser aplicada para o mesmo erro na importação de outros modelos.

![Imagem 1: (1) Ao realizar uma importação de dados usando como modelo a " Tabela de preço por produto ", ocorre o erro abaixo. A…](https://ajuda.sankhya.com.br/hc/article_attachments/30698255524631)

**(1)** Este artigo tem como objetivo apresentar a solução para o erro acima, partindo do pressuposto de que o usuário já possui conhecimento sobre a criação, preenchimento e importação de arquivos **CSV** no sistema. Por isso, não serão abordadas as etapas de importação nem as regras necessárias para esse processo.

**(1)**Antes de ir para solução, é necessário entender se a importação está **inserindo** novos produtos na tabela em questão ou está **alterando** o preço dos produtos já existentes na tabela de preços, pois o preenchimento do arquivo CSV muda dependendo da ação realizada.

**SOLUÇÃO:**

**(1)** Se os dados inseridos no arquivo CSV tem o objetivo de inserir novos produtos, a lógica abaixo deve ser seguida.

**(2)**Identifique o número único da tabela de preço onde o produto deve ser incluído.

![Imagem 2: (2) Identifique o número único da tabela de preço onde o produto deve ser incluído.](https://ajuda.sankhya.com.br/hc/article_attachments/30698255527319)

**(2)**No arquivo CSV informamos o código do produto, o número da tabela e o valor de venda.

![Imagem 3: (2) No arquivo CSV informamos o código do produto, o número da tabela e o valor de venda.](https://ajuda.sankhya.com.br/hc/article_attachments/30653015201943)

**Observação:** O campo **AD\_IDEXTERNO** pode ficar em branco, por se tratar de uma inserção de dados. Mas lembrando que esse campo deve existir na tabela **TGFEXC**. Já, o campo **CODLOCAL,** só deve ser preenchido se o parâmetro **PRECOPORLOC** estiver ligado.

**(2)** Se o objetivo é apenas alterar valores de produtos já existentes na tabela de preço, seguimos essa lógica.

**(2)** Siga a mesma lógica do passo 1, porém a diferença é que será necessário informar não só no arquivo CSV mas também na tela tabela de preços o campo **AD\_IDEXTERNO**, caso contrário resultará no erro.

![Imagem 4: (2) Siga a mesma lógica do passo 1, porém a diferença é que será necessário informar não só no arquivo CSV mas também…](https://ajuda.sankhya.com.br/hc/article_attachments/30698255528727)

![Imagem 5: (2) Siga a mesma lógica do passo 1, porém a diferença é que será necessário informar não só no arquivo CSV mas também…](https://ajuda.sankhya.com.br/hc/article_attachments/30653008409239)

**Observação:** o código informado na tela deverá ser o mesmo código informado no arquivo.
