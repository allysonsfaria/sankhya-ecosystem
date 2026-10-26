---
id: "43549269146775"
titulo: "Produtos não apresentados na importação de pedido no PDV Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549269146775-Produtos-n%C3%A3o-apresentados-na-importa%C3%A7%C3%A3o-de-pedido-no-PDV-Web"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-09-29T18:32:22Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Produtos não apresentados na importação de pedido no PDV Web

Ao importar um pedido no **PDV Web**, acessando o **Portal de Caixa (Comercial > Consulta)**, pode ocorrer de alguns produtos não serem apresentados na grade de itens.

Esse comportamento ocorre quando o produto está configurado no cadastro com o campo **“Usado Como”**, localizado na tela **Produtos (Configurações >> Cadastros >> Produtos)**, na sub-aba **“Geral”**, com uma opção diferente das aceitas pelo PDV Web.

### Solução:

**(1)**Acesse o **Cadastro de Produtos** (**Configurações > Cadastros > Produtos**) e localize o produto que não está sendo apresentado.

Na aba **Geral**, localize o campo **“Usado Como”** e verifique a configuração realizada.

Para que o produto seja apresentado no **PDV Web**, configure o campo como **“Revenda”** ou **“Venda (Fabricação Própria)”**.

![Imagem 1: Para que o produto seja apresentado no PDV Web , configure o campo como “Revenda” ou “Venda (Fabricação Própria)” .](https://ajuda.sankhya.com.br/hc/article_attachments/43825777709335)

#### Importante:

no layout HTML5 do PDV Web, somente serão apresentados na grade os itens configurados como **“Revenda”** ou **“Venda (Fabricação Própria)”** no campo **“Usado Como”**. Caso contrário, a grade poderá ser apresentada sem o respectivo item.

### Causa

Atualmente, o **PDV Web** considera para a importação de pedidos apenas produtos cujo campo **“Usado Como”** esteja configurado como:

- **Revenda**
- **Venda (Fabricação Própria)**

Quando o produto está configurado por exemplo como **“Consumo”**, ele não é apresentado na grade de itens do pedido importado.
