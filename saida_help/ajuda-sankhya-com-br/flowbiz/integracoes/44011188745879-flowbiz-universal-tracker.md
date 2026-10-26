---
id: "44011188745879"
titulo: "Flowbiz Universal Tracker"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011188745879-Flowbiz-Universal-Tracker"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:58:03Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_388", "sync_hash_5b38a07fc2d9"]
---

# Flowbiz Universal Tracker

## 1. Introdução

O Universal Tracker Flowbiz conecta qualquer plataforma de e-commerce ao ecossistema Flowbiz, capturando em tempo real o comportamento dos clientes no site. Ele permite visibilidade da jornada de compra, consistência de dados entre loja e CRM, e potencialização de campanhas de retenção.

## 2. Quickstart em 3 Passos

## Passo 1: Adição do Script de Eventos (mb\_track)

Adicione o script abaixo em todas as páginas do e-commerce (Home, Produto, Carrinho, Checkout e Pedido Finalizado).

JavaScript:

(function (m, a) {

```
if (!m[a]) {

  m[a] = function () { ;(m[a].q = m[a].q || []).push(arguments) }

  m[a].q = m[a].q || []

}
```

})(window, 'mb\_track');

## Passo 2: Envio de Eventos

Utilize a API de eventos para enviar as seguintes ações:

- accountSync: Identificação do usuário (Login, criação de conta ou input de e-mail no checkout).
- cartSync: Sempre que houver alteração no carrinho (Adição, remoção, atualização de frete ou endereço).
- productView: Disparado no carregamento das páginas de produto.
- checkoutStep: Disparado em cada etapa do processo de finalização de compra.
- orderComplete: Disparado na página de confirmação de pedido finalizado.

## Passo 3: Recuperação de Carrinho (mb\_recover\_cart)

Adicione o script na página de carrinho ou home para processar a recuperação de itens via API.

JavaScript:

(function (m, a) {

```
if (m[a]) { return; }

m[a] = function (arg) {

    var cartId = arg.cart_id;

    var userId = arg.user_id;

    var products = arg.products;

    // Exemplo: processar produtos e adicionar ao carrinho local

    products.forEach(function (product) {

        example.addToCart(product.product_id, product.sku, product.quantity);

    });

};
```

})(window, 'mb\_recover\_cart');

## 3. Lista de Eventos Suportados

- pageView
- accountSync
- productView
- cartSync
- addToCart
- cartItemUpdate
- cartSetPostalCode
- cartSetCoupon
- checkoutStep
- orderComplete
