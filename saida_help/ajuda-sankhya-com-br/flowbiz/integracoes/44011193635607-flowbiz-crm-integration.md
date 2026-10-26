---
id: "44011193635607"
titulo: "Flowbiz CRM Integration"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011193635607-Flowbiz-CRM-Integration"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:57:19Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_387", "sync_hash_c43116aa155c"]
---

# Flowbiz CRM Integration

## 1.Visão Geral

A Integração CRM permite que ERPs e sistemas de pedidos conectem dados de Clientes, Pedidos e Produtos ao ecossistema Flowbiz de forma padronizada via API REST.

## 2. Requisitos Técnicos

- Autenticação: Header 'X-Impulse-Key' obrigatório em todas as requisições.
- Formato: JSON (UTF-8).
- Protocolo: HTTPS obrigatório.
- Paginação: Obrigatória via parâmetros 'offset' e 'limit' (máx 100).
- A resposta deve conter: total, offset, limit, count, hasNext e nextOffset.

## 3. Endpoints Obrigatórios (Sua API deve expor)

- GET /healthz: Check de disponibilidade.
- GET /categories: Listagem de categorias.
- GET /brands: Listagem de marcas.
- GET /products: Listagem de produtos e variantes.
- GET /orders: Listagem de pedidos (Suporta start\_date e end\_date no formato YYYY-MM-DD).

## 4. Modelos de Dados (Esquema JSON)

## Objeto Order (Pedido)

Campos Obrigatórios:

- orderId, date (ISO 8601), total (numérico), currency (ISO 4217), rawPaymentStatus, customerId, customerEmail, items (mínimo 1).

## Objeto Product (Produto)

Campos Obrigatórios:

- productId, url, variants.
- Cada variante deve conter: sku, name, price, stock, available.

## Objeto Category / Brand

- id, name (Obrigatórios).

## 5. Exemplo de Requisição (Listar Pedidos)

GET /api/v2/orders?offset=0&limit=10&start\_date=2023-01-01&end\_date=2023-01-31

Header: X-Impulse-Key: [SUA\_CHAVE]

## 6. FAQ

- Por que não há endpoint de Customer? Os dados do cliente são enviados dentro do objeto Order para simplificar a sincronização.
- Como tratar variantes? Um único productId pode conter múltiplas variantes (cores, tamanhos), cada uma com seu SKU e estoque próprio.
- Filtro de data: O intervalo de datas em /orders é inclusivo e deve ignorar o fuso horário (usar UTC).

## 7. Suporte

E-mail: [suporte@flowbiz.com.br](mailto:suporte@flowbiz.com.br) | Telefone: (51) 9790-9718
