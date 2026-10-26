---
id: "360044600294"
titulo: "Botão Atualizar Itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600294-Bot%C3%A3o-Atualizar-Itens"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:49:56Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Central de Vendas", "Movimentação Financeira", "Atualização", "TOP", "Botão Atualizar Itens", "Botão Atualizar Itens manual", "Estoque", "br.com.sankhya.com.mov.CentralNotas", "Botão ‘Atualizar Itens’: Gerenciamento de Estoque Eficiente"]
---

# Botão Atualizar Itens

Na [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973), o botão **![botão](https://ajuda.sankhya.com.br/hc/article_attachments/16027994008599) "Atualizar Itens"** está presente para a verificação do estoque dos itens lançados apenas quando o Tipo de Movimento informado for:

- Nota de Venda;
- Devolução de compra;
- Pedido de Requisição;
- Requisição;
- Transferência.

Utilizaremos o usuário "Júlio Lima", para ilustrar o funcionamento do botão Atualizar Itens em um lançamento de uma Nota de Venda.

Primeiramente é necessário configurar o acesso especial, pois uma vez que os itens são excluídos não será possível desfazer esta operação. Assim, as configurações a seguir serão realizadas na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), na qual o nome do acesso é **"Atualizar itens"**.

Escolha o Portal e o Tipo de Movimento  onde o usuário terá permissão para realizar este novo processo. No nosso exemplo, o usuário "Júlio Lima" terá acesso para Atualizar itens de Notas de vendas. Se a mesma permissão se estender para outros Portais ou Tipos de Movimentos (Pedidos, Devoluções, entre outros), eles deverão ser selecionados e a mesma liberação deverá ser realizada.

![Imagem 2: Escolha o Portal e o Tipo de Movimento onde o usuário terá permissão para realizar este novo processo. No nosso…](https://ajuda.sankhya.com.br/hc/article_attachments/360102519414)

Efetuado os procedimentos acima, é necessário configurar a TOP utilizada no lançamento, pois mesmo que o usuário possua o acesso e o botão esteja presente na tela, ele ficará habilitado apenas se no [Tipo de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) informado no cabeçalho da nota estiver:

- Com a opção **"Atualizar Estoque a partir da Confirmação"** da aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), marcada;
- Nesta mesma aba, os campos **"Atualização do Estoque"** ou **"Atualiza estoque MP"** estiverem indicados com a opção **"Baixar"**;
- A Nota possuir itens.

Realizadas as configurações descritas acima, ao utilizar o botão Atualizar itens podem ocorrer as seguintes situações:

- Se os produtos (itens) estiverem com o estoque zerado ou negativo, eles serão excluídos;
- Caso o estoque de algum produto seja inferior à quantidade negociada no item, a quantidade negociada será atualizada para a quantidade em estoque.

Considere o exemplo abaixo, onde os itens informados possuem variações nas quantidades em estoque e lançadas:

| **Produto** | **700001** | **700056** | **80053** | **700059** |
| --- | --- | --- | --- | --- |
| **Quantidade em estoque** | 875 | -100 | 0 | 100994 |
| **Quantidade lançada** | 900 | 50 | 30 | 5 |

Ao clicar no botão Atualizar itens surgirá a seguinte mensagem:

**"O sistema irá atualizar todos os itens com base no estoque, excluindo os que estejam em falta e atualizando a quantidade negociada para a quantidade em estoque".**

Se você optar por **"Sim"**o resultado será:

- Os produtos **700056** e **80053** serão excluídos, pois estão com os seus respectivos estoques negativo e zerado;
- A quantidade negociada do produto **700001** será alterada para a sua quantidade em estoque;
- O produto **700059** continuará da mesma forma.

Se optar por **"Não"** a operação será cancelada.
