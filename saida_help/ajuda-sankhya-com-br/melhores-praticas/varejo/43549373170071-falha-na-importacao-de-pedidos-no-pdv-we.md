---
id: "43549373170071"
titulo: "Falha na importação de pedidos no PDV Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549373170071-Falha-na-importa%C3%A7%C3%A3o-de-pedidos-no-PDV-Web"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-09-25T18:33:51Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Falha na importação de pedidos no PDV Web

A importação de pedidos no **PDV Web** considera alguns critérios para que o pedido seja apresentado para seleção. Quando esses critérios não são atendidos, o pedido pode não ser localizado ou disponibilizado para importação.

#### **(1)**Critérios para importação de pedidos

O sistema considera para importação os pedidos que estejam com o status **Confirmado** ou **Pendente**.

Para verificar o status do pedido, acesse o **Portal de Vendas** em **Comercial > Consulta**.

Pedidos com outros status, como **Cancelado** ou **Faturado**, ou pedidos que ainda não tenham sido confirmados, não serão apresentados para importação.

#### **(1)**Utilização dos filtros de busca

Na funcionalidade **Importar Pedidos** do **PDV Web**, é possível localizar os pedidos utilizando os seguintes critérios:

- **Nome** do parceiro;
- **CPF/CNPJ** do parceiro;
- **Nome do vendedor**;
- **Número Único** do pedido.

Caso o pedido não seja localizado, verifique se os filtros utilizados correspondem às informações cadastradas no pedido e se o status está como **Confirmado** ou **Pendente**.

#### **(1)**Parâmetro BUSCPEDPDV

A funcionalidade **Importar Pedidos** utiliza o parâmetro **BUSCPEDPDV** para definir como a busca dos pedidos será realizada.

Caso o cliente utilize exclusivamente o **Número Único** como critério de busca, configure o parâmetro **BUSCPEDPDV** com a seguinte expressão:

`CAB.NUNOTA = :BUSCA`
