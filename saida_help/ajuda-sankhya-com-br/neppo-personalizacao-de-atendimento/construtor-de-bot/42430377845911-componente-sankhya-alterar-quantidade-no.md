---
id: "42430377845911"
titulo: "Componente Sankhya - Alterar Quantidade no Carrinho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:22Z"
rotulos: ["sync_hc", "neppo", "neppo_857999384", "sync_hash_8a3934b3ed14"]
---

# Componente Sankhya - Alterar Quantidade no Carrinho

O componente **Alterar Quantidade no Carrinho** permite **atualizar a quantidade de um item já existente no carrinho de compras** durante a jornada de venda digital.

Esse componente é utilizado quando o usuário deseja:

- alterar a quantidade de um produto selecionado
- aumentar ou reduzir itens no carrinho
- substituir a quantidade atual por uma nova quantidade

A alteração ocorre **sobre um item que já esteja presente no carrinho**, identificado pelo **produto, unidade e controle**.

bot-server: **versão 1.7.0**

![Imagem 1: bot-server: versão 1.7.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639683349655)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Objetivo-do-componente)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Interface-do-componente-leitura-da-tela)
- [Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Armazenamento)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Descricao-dos-campos-retornados)
- [Comportamento do carrinho](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Comportamento-do-carrinho)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Boas-praticas)
- [Consistência com o ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Consistencia-com-o-ERP)
- [Posição do componente no fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377845911-Componente-Sankhya-Alterar-Quantidade-no-Carrinho#Posicao-do-componente-no-fluxo)

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

Permitir que o fluxo do bot **modifique a quantidade de um item previamente adicionado ao carrinho**, mantendo a consistência dos dados antes da criação do pedido no Sankhya.

---

## Interface do componente (leitura da tela)

## Parâmetros

**Configuração do item que será alterado no carrinho**

| Campo | Descrição |
| --- | --- |
| **Código do Produto**\* | Código do produto que será alterado |
| **Código do Volume (Unidade)** | Unidade utilizada no item do carrinho |
| **Controle** | Variação do produto (sabor, cor, tamanho, etc.) |
| **Estratégia de Alteração** | Define como a nova quantidade será aplicada |
| **Nova Quantidade Final**\* | Nova quantidade que será aplicada ao item |

---

### Código do produto

Identifica o item do carrinho que será alterado.

Exemplo:

```
12345
```

ou

```
{{codigoProduto}}
```

⚠️ O produto **precisa existir no carrinho** para que a alteração seja aplicada.

---

### Código do volume (unidade)

Define qual unidade do produto está sendo alterada.

Exemplo:

```
UN
KG
CX
```

Caso o produto possua múltiplas unidades, a alteração ocorrerá **na unidade correspondente**.

---

### Controle do produto

Identificação da variação do produto.

Exemplos:

```
MACA VERDE
UVA
1L
500ML
```

Esse campo é necessário quando o produto possui **controle ativo**.

---

### Estratégia de alteração

Define como a nova quantidade será aplicada ao item.

| Opção | Comportamento |
| --- | --- |
| **Substituir pela nova quantidade** | A quantidade atual será substituída pela nova |

Exemplo:

Se o item possui quantidade **5** e a nova quantidade é **10**, o resultado será:

```
Quantidade final: 10
```

---

### Nova quantidade final

Quantidade que será aplicada ao item no carrinho.

Exemplo:

```
1
```

ou

```
{{quantidade}}
```

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Variável que receberá o estado atualizado do carrinho |
| **Variável de escopo global** | Permite acessar o carrinho em qualquer fluxo |

Exemplo:

```
carrinho
```

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
| **items** | Lista atualizada de itens do carrinho |
| **items[].product.code** | Código do produto |
| **items[].product.referenceCode** | Código de referência |
| **items[].product.description** | Nome do produto |
| **items[].quantity** | Quantidade atualizada |
| **items[].locationCode** | Código do local de estoque |
| **items[].unitCode** | Unidade de venda |
| **items[].controlCode** | Controle do produto |
| **items[].price** | Preço unitário |
| **total** | Valor total do carrinho |
| **error** | Informações de erro |

---

## Comportamento do carrinho

O carrinho sempre mantém o **estado atualizado dos itens** após a alteração.

Exemplo antes da alteração:

| Produto | Quantidade |
| --- | --- |
| BALAS SORTIDAS (MACA VERDE) | 5 |
| BALAS SORTIDAS (UVA) | 10 |

Após alterar:

| Produto | Quantidade |
| --- | --- |
| BALAS SORTIDAS (MACA VERDE) | **8** |
| BALAS SORTIDAS (UVA) | 10 |

---

## Exemplos de uso no bot

### Confirmar alteração da quantidade

```
Quantidade atualizada com sucesso!

{{carrinho.items[0].product.description}}
Nova quantidade: {{carrinho.items[0].quantity}}
```

---

### Mostrar total atualizado

```
Total atualizado do carrinho:

R$ {{carrinho.total}}
```

---

### Mostrar resumo do carrinho

```
Itens no carrinho:

{{carrinho.items[0].product.description}} - {{carrinho.items[0].quantity}}
{{carrinho.items[1].product.description}} - {{carrinho.items[1].quantity}}
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Produto não encontrado no carrinho | erro retornado |
| Quantidade inválida | alteração rejeitada |
| Controle incorreto | item não localizado |

---

## Boas práticas

- Sempre validar se o produto **existe no carrinho** antes de alterar
- Garantir que **controle e unidade estejam corretos**
- Atualizar a interface do usuário após a alteração
- Permitir revisão do carrinho antes de finalizar a compra

---

## Consistência com o ERP

A alteração da quantidade ocorre **apenas no carrinho do bot**, e não diretamente no Sankhya.

Os dados atualizados serão enviados ao ERP apenas quando o componente:

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
Estoque do Produto
↓
Preço do Produto
↓
Adicionar ao Carrinho
↓
Alterar Quantidade no Carrinho
↓
Itens do Pedido
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
