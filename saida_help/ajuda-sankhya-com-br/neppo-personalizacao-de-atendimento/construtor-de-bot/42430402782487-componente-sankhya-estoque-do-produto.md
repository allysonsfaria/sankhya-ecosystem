---
id: "42430402782487"
titulo: "Componente Sankhya - Estoque do Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:27Z"
rotulos: ["sync_hc", "neppo", "neppo_857998818", "sync_hash_7111bbfcf42a"]
---

# Componente Sankhya - Estoque do Produto

O componente **Estoque do Produto** permite consultar no ERP **Sankhya** a **quantidade disponível em estoque de um produto**, retornando os registros de estoque por **local de armazenamento** e, quando aplicável, também por **controle do produto** (ex.: sabor, tamanho, lote ou variação).

Esse componente é utilizado principalmente em jornadas de **venda digital**, permitindo que o bot:

- valide disponibilidade antes de adicionar itens ao carrinho
- mostre ao usuário as opções disponíveis de variação
- identifique em qual local o produto está disponível

bot-server: **versão 1.7.0**

bot-component-service: **versão 1.3.0**

![Imagem 1: bot-component-service: versão 1.3.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639621251607)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Objetivo-do-componente)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Interface-do-componente-leitura-da-tela)
- [Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Armazenamento)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Integracao-tecnica)
- [Exemplo de requisição](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Exemplo-de-requisicao)
- [Estrutura do retorno (componente)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Estrutura-do-retorno-componente)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Descricao-dos-campos-retornados)
- [Mapeamento técnico dos campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Mapeamento-tecnico-dos-campos)
- [Comportamento importante](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Comportamento-importante)
- [Estrutura \_rmd](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Estrutura-_rmd)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430402782487-Componente-Sankhya-Estoque-do-Produto#Boas-praticas)

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

Disponibilizar no fluxo do bot as **informações de estoque atual do produto no Sankhya**, permitindo validações de disponibilidade antes da criação do pedido.

---

## Interface do componente (leitura da tela)

## Parâmetros

**Configuração da consulta de estoque**

| Campo | Descrição | Origem Sankhya |
| --- | --- | --- |
| **Código do Produto**\* | Código único do produto no Sankhya | `TGFPRO.CODPROD` |
| **Empresa (opcional)** | Empresa responsável pelo estoque | `TGFFIL.CODEMP` |
| **Local de Estoque (opcional)** | Local específico de armazenamento | `TGFLOC.CODLOCAL` |
| **Continuar Listagem (opcional)** | Página da consulta para paginação | `offsetPage` |

Exemplo de uso:

```
{{codigoProduto}}
```

ou

```
1236
```

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Variável que receberá o resultado da consulta |
| **Variável de escopo Global** | Permite acessar os dados em qualquer fluxo |

Exemplo:

```
estoqueProduto
```

---

## Integração técnica

A consulta utiliza o serviço Sankhya:

```
CRUDServiceProvider.loadRecords
```

Entidade consultada:

**Estoque**

Essa entidade armazena a quantidade de produtos disponíveis por **empresa, local e controle**.

---

## Exemplo de requisição

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'appkey: <APPKEY>' \
--header 'Content-Type: application/json' \
--data '{
"serviceName": "CRUDServiceProvider.loadRecords",
"requestBody": {
"dataSet": {
"rootEntity": "Estoque",
"includePresentationFields": "S",
"offsetPage": "0",
"criteria": {
"expression": {
"$": "this.CODPROD = ? AND this.CODEMP = ? AND this.CODLOCAL = ?"
},
"parameter": [
{ "$": "1236", "type": "I" },
{ "$": "1", "type": "I" },
{ "$": "8000", "type": "I" }
]
},
"entity": {
"fieldset": {
"list": "CODPROD,CODLOCAL,ESTOQUE,CODEMP,CONTROLE"
}
}
}
}
}'
```

---

## Estrutura do retorno (componente)

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 4,
  "content": [
    {
      "quantity": 500,
      "control": "AMORA",
      "location": {
        "code": 6100,
        "description": "Galpão A"
      }
    }
  ],
  "error": null
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| **hasMore** | Indica se existem mais registros disponíveis para paginação |
| **size** | Quantidade de registros retornados |
| **content[]** | Lista de registros de estoque |
| **content[].quantity** | Quantidade disponível em estoque |
| **content[].control** | Controle do produto (variação) |
| **content[].location.code** | Código do local de estoque |
| **content[].location.description** | Descrição do local |
| **error** | Informações de erro quando a consulta falha |

---

## Mapeamento técnico dos campos

| Campo | Origem Sankhya | Tabela |
| --- | --- | --- |
| quantity | ESTOQUE | Estoque |
| control | CONTROLE | Estoque |
| location.code | CODLOCAL | Estoque |
| location.description | LocalFinanceiro\_DESCRLOCAL | TGFLOC |

---

## Comportamento importante

Um produto pode possuir **controle ativo**, como:

- sabor
- tamanho
- cor
- lote

Quando isso acontece, o retorno da API contém **um registro por controle**, mesmo que o local seja o mesmo.

Exemplo:

| Controle | Estoque |
| --- | --- |
| AMORA | 500 |
| MORANGO | 500 |
| UVA | 500 |
| MAÇÃ VERDE | 500 |

---

## Estrutura `_rmd`

Quando presente, o campo `_rmd` retornado pelo Sankhya contém metadados sobre o controle de estoque, como:

- nome do controle
- lista de opções
- tipo de controle

Exemplo:

```
"controle": {
  "tipoContEst": "S",
  "labelContEst": "Tamanho",
  "listaContEst": ["500ML", "1L", "2L"]
}
```

Essas informações podem ser utilizadas pelo bot para montar interfaces de seleção de variação.

---

## Exemplos de uso no bot

### Validar se há estoque disponível

```
Se {{estoqueProduto.size}} > 0
→ Produto disponível
```

---

### Mostrar estoque disponível por variação

```
Temos estoque disponível para:

{{estoqueProduto.content[0].control}}
{{estoqueProduto.content[1].control}}
```

---

### Exibir local do estoque

```
Local do estoque: {{estoqueProduto.content[0].location.description}}
```

---

## Tratamento de erros

### Exemplo

```
{
  "hasMore": false,
  "size": 0,
  "content": [],
  "error": {
    "code": "PRODUCT_CODE_IS_INVALID",
    "message": "..."
  }
}
```

---

| Situação | Comportamento |
| --- | --- |
| Código de produto inválido | erro `PRODUCT_CODE_IS_INVALID` |
| Produto sem estoque | `size = 0` |
| Falha de integração | objeto `error` preenchido |

---

## Boas práticas

- Validar `size` antes de permitir adicionar ao carrinho
- Se existir `control`, solicitar escolha da variação ao usuário
- Usar paginação quando houver muitos registros
- Filtrar por **empresa** quando o ambiente for multiempresa

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
