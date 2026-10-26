---
id: "360044599514"
titulo: "Layout de Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599514-Layout-de-Pedidos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Pedido Web"
atualizado_em: "2026-07-29T14:11:48Z"
rotulos: ["manual", "Configuração", "Layout", "Pedido Web", "Nota Fiscal", "TOP", "Layout de Pedidos", "br.com.sankhya.web.layout.pedidos", "Layout de Pedidos manual", "Personalização do Layout de Pedidos"]
---

# Layout de Pedidos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311463004695) Módulo: Pedido Web > Configurações
```

O sistema permite que seja definido o layout do Pedido Web, adicionando e removendo os campos necessários, inclusive campos adicionais, através da rotina Layout de Pedidos.

![Imagem 2: O sistema permite que seja definido o layout do Pedido Web , adicionando e removendo os campos necessários, inclusive…](https://ajuda.sankhya.com.br/hc/article_attachments/17788974573207)

Na criação de um novo registro, será selecionado automaticamente o tipo de movimento **"Pedido de Venda"**.

![Imagem 3: Na criação de um novo registro, será selecionado automaticamente o tipo de movimento "Pedido de Venda" .](https://ajuda.sankhya.com.br/hc/article_attachments/17788973953559)

O comportamento da tela Layout de Pedidos é idêntico ao da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), mas inclui apenas Pedidos de Vendas. Um layout configurado em uma dessas duas telas não pode ser visualizado na outra, mesmo que se trate do tipo de movimento Pedido de Venda.

A seleção do Layout de Pedidos, na exibição, respeitará as seguintes regras:

1. Se o [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado na Nota está configurado com um layout específico, este layout será utilizado para apresentação;
2. Se não for possível definir o Layout no item 1, será realizada a busca do layout marcado como padrão **"Sim"** na grade de layout da tela de configuração (layout personalizado marcado como padrão);
3. Se não for possível definir o Layout no item 2, o sistema buscará pelo layout que vem de origem no sistema, ou seja, layout padrão do sistema.

**Nota:** com o parâmetro **"Utiliza layout configuracao Cenral? - USALAYCONFCENT"** desligado, as configurações de Grade das Centrais serão compartilhadas, independente do layout do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114). Por exemplo:

Se houver um layout A para vendas e um layout B para pedidos, ao configurar o grid ou o formulário em uma nota de venda, essa configuração será aplicada nas notas de venda e pedidos para os layouts A e B.

**Importante:** caso o layout B tenha colunas configuradas que não estejam no layout A, essas colunas podem ficar ocultas se forem utilizadas em uma nota do layout A.

**Observações:**

Por definição arquitetural, uma TOP só poderá ser vinculada à um layout, ou seja, se utilizada no layout do Módulo Pedido Web, a TOP não poderá ser vinculada à um layout no Módulo Comercial. A justificativa de se manter assim é que, quem geralmente acessa o Módulo Pedido Web utilizará uma TOP específica, e não as utilizadas pelo comercial.

As telas [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas) | [Central - Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas) e [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601934-Ficha-de-Parceiros) respeitarão as configurações de layout efetuadas na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).
