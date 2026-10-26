---
id: "37636668821399"
titulo: "Como emitir relatório para identificar a necessidade de compras de acordo com os pedidos de vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37636668821399-Como-emitir-relat%C3%B3rio-para-identificar-a-necessidade-de-compras-de-acordo-com-os-pedidos-de-vendas"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:18Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "Portal de Vendas", "Estoque"]
---

# Como emitir relatório para identificar a necessidade de compras de acordo com os pedidos de vendas

| Categoria |
| --- |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37636668821399-Como-emitir-relat%C3%B3rio-para-identificar-a-necessidade-de-compras-de-acordo-com-os-pedidos-de-vendas#h_01KFBGG9E1DE9TSK2HRME4820Z) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37636668821399-Como-emitir-relat%C3%B3rio-para-identificar-a-necessidade-de-compras-de-acordo-com-os-pedidos-de-vendas#h_01KEVJGVZ8KV42EF694F4RPWJC) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37636668821399-Como-emitir-relat%C3%B3rio-para-identificar-a-necessidade-de-compras-de-acordo-com-os-pedidos-de-vendas#h_01KEVJHNZ1027PCCFNAZ7MN8M0) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37636668821399-Como-emitir-relat%C3%B3rio-para-identificar-a-necessidade-de-compras-de-acordo-com-os-pedidos-de-vendas#h_01KEVJKWJHMMPDBENCXV2KMDDD) |

## Compra com base em pedidos de venda (Encomenda) relatório

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1060469646)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na **Axis**, os vendedores registraram um novo Pedido de Venda por Encomenda, que não faz parte do estoque regular. A solicitação foi encaminhada à equipe de compras para dar andamento à aquisição.

Como o comprador já estava lidando com várias requisições simultâneas, ele optou por utilizar a emissão de relatório, uma alternativa mais prática para consolidar os pedidos feitos sob encomenda em um único lugar. Com base nesse levantamento, ele conseguiu identificar rapidamente quais produtos precisam ser comprados, em que quantidade e com qual prioridade, garantindo que o pedido seja atendido dentro do prazo e sem risco de excesso no estoque.

**Tarefa:** Acesse a tela Entradas e Saídas e gere o **Relatório 113 – Sugestão de Compra para Pedidos de Venda**. Use o relatório para identificar a necessidade de compra dos produtos com base nos pedidos de venda registrados na sua base de testes.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Acesse a tela de Entradas e Saídas**
   Menu: Comercial » Relatórios » Entradas e Saídas

- Clique na seta para abrir a pasta “**Indicadores**”.
- Clique na seta para abrir a subpasta “**Compras**”.
- Clique na seta para abrir “**Análise da Necessidade de Compra**”**.**
- Dê um duplo clique no relatório “**113 - Sugestão de Compra p/ Requisições**”.

2. **Configure os parâmetros do relatório**

- Insira o **Cód. Empresa** relacionada.
- Clique em **OK**.

3. **Pré-Requisitos para a emissão do relatório**
   **Antes de emitir o relatório, certifique-se de que:**

- **Existe um Pedido de Venda pendente registrado no Portal de Vendas.**
- O **Estoque Mínimo e Máximo** está configurado corretamente na tela de **Produtos**, na aba **Medidas e Estoque**, sub-aba **Estoque**.

4. **Verifique as Informações do Relatório**
   **Revise os seguintes campos essenciais no relatório:**

- **Cód.:** Código do produto
- **Desc. Produtos:** Descrição do Produto
- **Controle:** Quando o produto tiver alguma característica específica, como cor, tamanho ou outro tipo de variação.
- **Soma Estoque**: Quantidade total de itens disponíveis no estoque.
- **Reservado**: Quantidade reservada.
- **Qtd Total**: Quantidade total considerando o pedido de venda.
- **Custo Reposição**: Valor estimado para reposição de cada item.
- **Estoque Mínimo**: Nível mínimo configurado para evitar indisponibilidade no estoque.
- **Sugestão de Compra**: Quantidade recomendada para reposição.

#### Correção e Repetição

- **Confira se todos os campos obrigatórios foram preenchidos corretamente** na tela de **Produtos**.
- **Verifique se o Estoque Mínimo e Máximo foi definido para o item.**
- **Se algo não tiver funcionado como esperado, refaça o processo ajustando as informações necessárias.**
- **Para treinar novamente**, crie um novo cenário com outro **pedido de Requisição Interna** e produtos diferentes.
