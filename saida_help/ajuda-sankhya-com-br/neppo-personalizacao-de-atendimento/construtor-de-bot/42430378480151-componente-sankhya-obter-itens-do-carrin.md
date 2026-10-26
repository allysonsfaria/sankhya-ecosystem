---
id: "42430378480151"
titulo: "Componente Sankhya - Obter Itens do Carrinho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:22Z"
rotulos: ["sync_hc", "neppo", "neppo_857999438", "sync_hash_c7e71cc17ef1"]
---

# Componente Sankhya - Obter Itens do Carrinho

O componente **Obter Itens do Carrinho** permite recuperar o **estado atual do carrinho de compras** durante a execução do fluxo do bot.

Esse componente é **somente leitura** e não altera os dados do carrinho. Ele serve para que o fluxo tenha acesso aos itens já adicionados anteriormente, permitindo:

- exibir o carrinho ao usuário
- validar itens antes de criar o pedido
- calcular totais
- revisar produtos antes da finalização da compra

bot-server: **versão 1.7.0**

![Imagem 1: bot-server: versão 1.7.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639711554327)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Objetivo-do-componente)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Interface-do-componente-leitura-da-tela)
- [Consulta de estado](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Consulta-de-estado)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Descricao-dos-campos-retornados)
- [Comportamento do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Comportamento-do-componente)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Boas-praticas)
- [Consistência com o ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Consistencia-com-o-ERP)
- [Posição do componente no fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430378480151-Componente-Sankhya-Obter-Itens-do-Carrinho#Posicao-do-componente-no-fluxo)

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)

---

## Objetivo do componente

Permitir que o fluxo do bot consulte os **dados mais recentes do carrinho de compras**, sem realizar alterações ou transações.

---

## Interface do componente (leitura da tela)

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá os dados do carrinho |
| **Variável de escopo global** | Permite acessar os dados do carrinho em qualquer fluxo |

Exemplo:

```
carrinho
```

Quando executado, o componente retorna o **estado completo do carrinho**, contendo todos os itens adicionados anteriormente.

---

## Consulta de estado

Este componente é classificado como uma **consulta de estado**.

> Este componente é apenas de leitura. Ele garante que o fluxo tenha acesso aos dados mais recentes do carrinho sem realizar alterações ou transações.

---

## Estrutura do retorno

### Exemplo de resposta

```
{
  "items": [
    {
      "product": {
        "code": 1185,
        "referenceCode": 91185,
        "defaultUnit": {
          "code": "UN",
          "description": "Unidade"
        },
        "description": "BALAS SORTIDAS",
        "complementaryDescription": null,
        "characteristics": null,
        "brand": "ERLAN"
      },
      "quantity": 5,
      "locationCode": 0,
      "unitCode": "UN",
      "controlCode": "MACA VERDE",
      "price": 4.3
    },
    {
      "product": {
        "code": 1185,
        "referenceCode": 91185,
        "defaultUnit": {
          "code": "UN",
          "description": "Unidade"
        },
        "description": "BALAS SORTIDAS",
        "complementaryDescription": null,
        "characteristics": null,
        "brand": "ERLAN"
      },
      "quantity": 10,
      "locationCode": 0,
      "unitCode": "UN",
      "controlCode": "UVA",
      "price": 4.6
    },
    {
      "product": {
        "code": 1236,
        "referenceCode": 91236,
        "defaultUnit": {
          "code": "UN",
          "description": "Unidade"
        },
        "description": "GUARANÁ SANTANA",
        "complementaryDescription": null,
        "characteristics": "Teste Caracteristicas",
        "brand": "MINEIRO"
      },
      "quantity": 10,
      "locationCode": 0,
      "unitCode": "CX",
      "controlCode": "1L",
      "price": 192
    }
  ],
  "error": null,
  "total": 1987.5
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| **items** | Lista de itens presentes no carrinho |
| **items[].product.code** | Código do produto |
| **items[].product.referenceCode** | Código de referência do produto |
| **items[].product.description** | Nome ou descrição do produto |
| **items[].product.brand** | Marca do produto |
| **items[].quantity** | Quantidade do item no carrinho |
| **items[].locationCode** | Código do local de estoque |
| **items[].unitCode** | Unidade de venda |
| **items[].controlCode** | Controle do produto (variação) |
| **items[].price** | Preço unitário |
| **total** | Valor total acumulado do carrinho |
| **error** | Informações de erro |

---

## Comportamento do componente

O componente sempre retorna o **estado atual do carrinho**, incluindo todos os itens adicionados ou alterados anteriormente no fluxo.

Exemplo de carrinho:

| Produto | Quantidade | Preço | Subtotal |
| --- | --- | --- | --- |
| BALAS SORTIDAS (MACA VERDE) | 5 | 4.3 | 21.5 |
| BALAS SORTIDAS (UVA) | 10 | 4.6 | 46.0 |
| GUARANÁ SANTANA (1L) | 10 | 192 | 1920 |

Total:

```
1987.5
```

---

## Exemplos de uso no bot

### Mostrar resumo do carrinho

```
Seu carrinho possui:

{{carrinho.items[0].product.description}} - {{carrinho.items[0].quantity}}
{{carrinho.items[1].product.description}} - {{carrinho.items[1].quantity}}
```

---

### Mostrar total da compra

```
Total do pedido:

R$ {{carrinho.total}}
```

---

### Validar se o carrinho possui itens

```
Se {{carrinho.items}} existir
→ continuar para criação do pedido
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Carrinho vazio | `items = []` |
| Falha interna | `error` preenchido |
| Dados inexistentes | `total = 0` |

---

## Boas práticas

- Utilizar esse componente antes de **Criar Pedido**
- Exibir resumo do carrinho para confirmação do usuário
- Validar se existem itens antes de finalizar a compra
- Permitir revisão ou alteração de quantidades

---

## Consistência com o ERP

O carrinho representa uma **estrutura temporária da venda**, mantida no contexto do bot.

Os dados somente serão enviados ao Sankhya quando o componente:

```
Criar Pedido
```

for executado.

---

## Posição do componente no fluxo

Fluxo típico da jornada de venda digital:

```
Busca de Produto
↓
Detalhe do Produto
↓
Locais de Estoque
↓
Estoque do Produto
↓
Preço do Produto
↓
Adicionar ao Carrinho
↓
Alterar Quantidade no Carrinho
↓
Obter Itens do Carrinho
↓
Criar Pedido
```

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)
