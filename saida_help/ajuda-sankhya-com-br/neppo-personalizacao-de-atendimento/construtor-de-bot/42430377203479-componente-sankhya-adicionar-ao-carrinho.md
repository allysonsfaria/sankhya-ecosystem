---
id: "42430377203479"
titulo: "Componente Sankhya - Adicionar ao Carrinho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:23Z"
rotulos: ["sync_hc", "neppo", "neppo_857999330", "sync_hash_d85caa313879"]
---

# Componente Sankhya - Adicionar ao Carrinho

O componente **Adicionar ao Carrinho** é responsável por **incluir um produto no carrinho de compras da jornada de venda digital** dentro do bot.

Esse carrinho representa uma **estrutura temporária de itens da venda**, que posteriormente será utilizada pelo componente **Criar Pedido** para registrar o pedido no ERP Sankhya.

bot-server: **versão 1.7.0**

Cada item adicionado ao carrinho contém informações essenciais da venda, como:

- produto
- quantidade
- preço unitário
- local de estoque
- unidade de venda
- controle do produto (quando aplicável)

![Imagem 1: controle do produto (quando aplicável)](https://ajuda.sankhya.com.br/hc/article_attachments/42639678352535)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Objetivo-do-componente)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Interface-do-componente-leitura-da-tela)
- [Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Armazenamento)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Descricao-dos-campos-retornados)
- [Comportamento do carrinho](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Comportamento-do-carrinho)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Boas-praticas)
- [Consistência com o ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430377203479-Componente-Sankhya-Adicionar-ao-Carrinho#Consistencia-com-o-ERP)

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

Permitir que o fluxo do bot **monte dinamicamente um carrinho de compras**, acumulando os itens selecionados pelo usuário antes da criação do pedido no Sankhya.

---

## Interface do componente (leitura da tela)

## Parâmetros

**Configuração do item que será adicionado ao carrinho**

| Campo | Descrição |
| --- | --- |
| **Código do produto**\* | Código único do produto no Sankhya |
| **Quantidade**\* | Quantidade do produto que será adicionada |
| **Preço Unitário**\* | Valor unitário do produto |
| **Código do Local de Estoque**\* | Local de onde o produto será retirado |
| **Código do Volume (Unidade)** | Unidade de venda (ex.: UN, CX, KG) |
| **Controle** | Identificação da variação do produto (ex.: sabor, tamanho, cor) |

---

### Código do produto

Exemplo:

```
12345
```

ou

```
{{codigoProduto}}
```

---

### Quantidade

Quantidade do item que será adicionada ao carrinho.

Exemplo:

```
5
```

ou

```
{{quantidadeSelecionada}}
```

---

### Preço unitário

Valor unitário do produto.

Exemplo:

```
19.99
```

ou

```
{{precoUnitario}}
```

Esse valor normalmente é obtido pelo componente **Preço do Produto**.

---

### Código do local de estoque

Código do local de estoque de onde o produto será retirado.

Exemplo:

```
101
```

ou

```
{{codigoLocalEstoque}}
```

Esse valor normalmente é obtido pelo componente **Locais de Estoque**.

---

### Código do volume (Unidade)

Define a unidade utilizada na venda.

Exemplos:

```
UN
CX
KG
```

Caso não informado, será utilizada a **unidade padrão do produto**.

---

### Controle do produto

Utilizado quando o produto possui **variações cadastradas**, como:

- sabor
- tamanho
- cor
- lote

Exemplo:

```
MACA VERDE
```

---

### Se o produto já existir no carrinho

Define o comportamento quando o produto já está presente no carrinho.

Opções disponíveis:

| Opção | Comportamento |
| --- | --- |
| **Somar quantidade** | Soma a nova quantidade ao item existente |
| **Substituir quantidade** | Atualiza o item com a nova quantidade |

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Variável que receberá o estado atualizado do carrinho |
| **Variável de escopo global** | Permite acessar o carrinho em qualquer ponto do fluxo |

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
    }
  ],
  "error": null,
  "total": 21.5
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| **items** | Lista de itens presentes no carrinho |
| **items[].product.code** | Código do produto |
| **items[].product.referenceCode** | Código de referência do produto |
| **items[].product.description** | Descrição do produto |
| **items[].product.brand** | Marca do produto |
| **items[].quantity** | Quantidade do item no carrinho |
| **items[].locationCode** | Código do local de estoque |
| **items[].unitCode** | Unidade de venda |
| **items[].controlCode** | Controle do produto (variação) |
| **items[].price** | Preço unitário |
| **total** | Valor total acumulado do carrinho |
| **error** | Informações de erro (quando houver) |

---

## Comportamento do carrinho

O carrinho funciona como uma **estrutura acumulativa de itens**, permitindo que o usuário adicione vários produtos antes de finalizar a compra.

Exemplo:

| Produto | Quantidade | Preço | Subtotal |
| --- | --- | --- | --- |
| BALAS SORTIDAS | 5 | 4.3 | 21.5 |
| GUARANÁ SANTANA | 2 | 8.0 | 16.0 |

Total:

```
37.5
```

---

## Exemplos de uso no bot

### Confirmar adição ao carrinho

```
Produto adicionado ao carrinho!

{{carrinho.items[0].product.description}}
Quantidade: {{carrinho.items[0].quantity}}
```

---

### Mostrar total do carrinho

```
Total do carrinho:

R$ {{carrinho.total}}
```

---

### Listar itens do carrinho

```
Itens no carrinho:

{{carrinho.items[0].product.description}}
{{carrinho.items[1].product.description}}
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Produto inválido | erro retornado no campo `error` |
| Quantidade inválida | item não adicionado |
| Preço inválido | erro de validação |

---

## Boas práticas

- Sempre consultar **Preço do Produto** antes de adicionar ao carrinho
- Validar **estoque disponível** antes da inclusão
- Utilizar **controle do produto** quando existir
- Garantir que **local de estoque esteja correto**

---

## Consistência com o ERP

O carrinho é uma **estrutura intermediária da jornada de venda digital**.

Os itens armazenados serão posteriormente enviados ao Sankhya através do componente:

```
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
