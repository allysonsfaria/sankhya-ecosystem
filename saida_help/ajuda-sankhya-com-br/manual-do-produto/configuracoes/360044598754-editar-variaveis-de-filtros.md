---
id: "360044598754"
titulo: "Editar variáveis de filtros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598754-Editar-vari%C3%A1veis-de-filtros"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:07Z"
rotulos: ["Configuração", "Inteiro", "Parceiro", "Variáveis", "entity", "Letras", "req", "Editar variáveis de filtros manual", "Cidades", "Filtros", "Interface", "Configuração Avançada de variáveis de filtro"]
---

# Editar variáveis de filtros

Esta interface de criação da Expressão de Filtros permite a configuração de duas novas opções, sendo elas,  o campo **"Requerido"** e uma Tabela que pode ser utilizada para mostrar na tela uma pesquisa de registros.

Caso o campo seja configurado como **"Não Requerido"**, seu preenchimento se torna opcional na visualização do cubo; em outras palavras, um campo Requerido é de preenchimento obrigatório antes da execução do cubo. Se for escolhida uma Tabela do sistema para o campo, ele é exibido na tela como uma busca de registros, permitindo ao usuário selecionar o valor desejado de acordo com algum dos campos da Tabela, no caso de parceiro, nome, cidade, e-mail, por exemplo.

Ao clicar no botão**"Editar variáveis de filtros"** é aberto o pop-up de edição de variáveis (caso a área de expressões esteja vazia ou o filtro não seja variável, este botão estará desabilitado). Além disso, é possível editar o status de obrigatoriedade (todo campo é criado por padrão como obrigatório), ou ainda selecionar outra tabela do sistema para o filtro.

![Imagem 1: Ao clicar no botão "Editar variáveis de filtros" é aberto o pop-up de edição de variáveis (caso a área de expressões…](https://ajuda.sankhya.com.br/hc/article_attachments/4418009319959)

A pesquisa por entidades/tabelas, estará habilitada para uso, apenas para as opções **"Letras"** e **"Inteiro"** do campo **"Tipo"**.

![Imagem 2: A pesquisa por entidades/tabelas, estará habilitada para uso, apenas para as opções "Letras" e "Inteiro" do campo…](https://ajuda.sankhya.com.br/hc/article_attachments/4418021683223)

Os filtros criados com base nestas configurações, possuem a seguinte sintaxe:

```
/*{entity=<Nome do cadastro>;req=<s ou n>}*/
```

Onde:

**'entity' = < nome da entidade>**; quer dizer que o campo de filtro que possui essa variável configurada, irá ser agregado no Painel de Filtros como um componente de pesquisa (somente quando utilizado o Aplicativo [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection)).

**'req' = <s ou n>**, sendo **"s"** é para Requerido e **"n"** para Não Requerido.

**Observação:** a marcação Requerido também é apresentada na inserção/edição de um novo filtro por meio do botão ![Imagem 3: Observação: a marcação Requerido também é apresentada na inserção/edição de um novo filtro por meio do botão "Editar…](https://ajuda.sankhya.com.br/hc/article_attachments/4418022517655) **"Editar filtro"**.

![Imagem 4: Observação: a marcação Requerido também é apresentada na inserção/edição de um novo filtro por meio do botão "Editar…](https://ajuda.sankhya.com.br/hc/article_attachments/4418022538263)
