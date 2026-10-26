---
id: "39334984419735"
titulo: "Como definir qual local de estoque o carrinho de compras usa na digitação de pedidos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39334984419735-Como-definir-qual-local-de-estoque-o-carrinho-de-compras-usa-na-digita%C3%A7%C3%A3o-de-pedidos"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-10-02T21:19:57Z"
rotulos: ["Produtos", "Pedidos", "Configuração", "Estoque", "Artigo criado KCS", "CVE - KCS", "Comercial"]
---

# Como definir qual local de estoque o carrinho de compras usa na digitação de pedidos?

Ao digitar pedidos no sistema pelo carrinho de compras, alguns itens podem puxar locais de estoque diferentes do padrão cadastrado no produto. Este comportamento ocorre porque o sistema seleciona automaticamente a primeira linha da grade **"Detalhes de estoque"**.

Para garantir que o **"Local de Estoque"** correto seja selecionado automaticamente durante a digitação de pedidos, é necessário configurar a ordenação dos dados na consulta de produtos.

### Configurando a ordenação do estoque

Para ajustar a ordenação e garantir que o sistema selecione o local de estoque desejado, siga os passos abaixo:

**(1)** Abra a **"Consulta de Produtos"** no mesmo lugar em que o carrinho é usado: pela própria digitação do pedido (por exemplo, no Portal de Vendas) ou pela tela **"Consulta de Produtos"** (Comercial » Consulta).
**(2)** Pesquise qualquer produto e abra os **"Detalhes de estoque"**. A configuração vale para todos os produtos.
**(3)** Clique no botão **"Configuração da Grade"**.
**(4)** Na opção **"Ordenação dos Dados"**, selecione **"Local"**.
**(5)** Confirme a configuração para que o sistema ordene os locais de estoque, posicionando o local correto na primeira linha.

### Importante: ordenação por número de local

A ordenação configurada é baseada no número do local de estoque. Isso significa que o sistema sempre selecionará o local com o menor número como primeira opção.

Caso exista outro local com número menor que o desejado, ele assumirá a primeira linha automaticamente. Nessa situação, será necessário selecionar manualmente a linha do estoque correto durante a digitação do pedido.

### Comportamento do sistema

O sistema foi projetado para selecionar sempre a primeira linha da grade de estoque ao adicionar produtos no pedido. Por isso, a configuração da ordenação é fundamental para que o local desejado fique na primeira linha.

Essa configuração não é feita por produto: ela vale para todos os produtos e fica salva por usuário. Usuários sem configuração própria dessa grade seguem a configuração feita pelo usuário SUP. Para padronizar para todos, faça a configuração com o usuário SUP. Se algum usuário já tiver configuração própria dessa grade, faça a ordenação também com o login dele.
