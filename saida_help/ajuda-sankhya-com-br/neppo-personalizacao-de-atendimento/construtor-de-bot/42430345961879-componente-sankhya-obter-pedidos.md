---
id: "42430345961879"
titulo: "Componente Sankhya - Obter Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:30Z"
rotulos: ["sync_hc", "neppo", "neppo_857998584", "sync_hash_8e5605add463"]
---

# Componente Sankhya - Obter Pedidos

O componente **Obter Pedidos** permite recuperar os pedidos de venda cadastrados no ERP Sankhya para um determinado parceiro (cliente ou fornecedor). Ele suporta consulta por código do parceiro, número específico de pedido ou paginação de resultados em blocos de até 150 registros.

bot-server: **versão 1.4.0**

bot-component-service: **versão 1.0.0**

Doc Sankhya: <https://developer.sankhya.com.br/reference/get_loadrecords>

![Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/reference/get_loadrecords](https://ajuda.sankhya.com.br/hc/article_attachments/42639648012823)

Esse recurso é ideal para:

- Exibir histórico de pedidos via bot
- Consultar status de pedidos pendentes
- Validar pedidos em tempo real para tomada de decisão
- Automatizar ações a partir de pedidos (como reenvio de nota, status de entrega, etc.)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Objetivo-do-componente)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Integracao-tecnica)
- [Configuração no construtor de bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Configuracao-no-construtor-de-bot)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Descricao-dos-campos-retornados)
- [Exemplos de uso no Bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Exemplos-de-uso-no-Bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Boas-praticas)
- [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Seguranca)
- [Alerta técnico sobre paginação e hasMore](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Alerta-tecnico-sobre-paginacao-e-hasMore)
- [Retorno de erro](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430345961879-Componente-Sankhya-Obter-Pedidos#Retorno-de-erro)

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

Capacitar fluxos conversacionais com acesso direto e atualizado às movimentações comerciais do cliente na base Sankhya, otimizando processos de suporte, cobrança, vendas e logística.

---

## Integração técnica

A integração se conecta ao endpoint que consulta a tabela `TGFCAB`, responsável pelo controle de cabeçalhos de movimentações comerciais no Sankhya.

---

## Configuração no construtor de bot

### Parâmetros de entrada

#### Código do parceiro (Obrigatório)

Código do cliente ou fornecedor no sistema Sankhya.

Exemplo:

```
{{codigoParceiro}}
```

---

#### Número do pedido (Opcional)

Caso queira consultar um pedido específico.

Exemplo:

```
{{numPedido}}
```

---

#### Continuar listagem (Opcional)

Permite paginação da consulta em blocos de até 150 pedidos.
Use:

- `0` para a primeira página
- `1` para a próxima página
- E assim por diante.

---

### Armazenamento

#### Variável de armazenamento

Nome da variável onde o resultado será salvo.

Exemplo:

```
detalhesPedido
```

---

#### Variável de escopo global

Permite reutilizar os dados em qualquer parte do fluxo.

---

## Estrutura do retorno

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 1,
  "content": [
    {
      "code": 3720081,
      "companyCode": 1,
      "invoicedAt": null,
      "postedAt": "DD/MM/AAAA",
      "operationAt": "DD/MM/AAAA",
      "partnerCode": 654,
      "operationTypeCode": 1,
      "operationTypeUpdatedAt": "DD/MM/AAAA HH:MM:SS",
      "movementType": "P",
      "status": "A",
      "pending": true,
      "confirmed": false,
      "salesTypeCode": 30,
      "salesTypeUpdatedAt": "DD/MM/AAAA HH:MM:SS",
      "sellerCode": 0,
      "observation": null,
      "totalDiscountValue": 0,
      "itemsDiscountValue": 0,
      "freightValue": 0,
      "freightType": "S",
      "value": 699.9,
      "loadOrder": null,
      "transporterPartnerCode": 0,
      "icmsBase": 0,
      "icmsValue": 0,
      "ipiBase": 0,
      "ipiValue": 0,
      "discountPercent": 0,
      "natureCode": 2010000,
      "projectCode": 1010000,
      "costCenterCode": 50300,
      "nfeKey": null,
      "nfeStatus": null,
      "movementAt": "DD/MM/AAAA"
    }
  ],
  "error": null
}
```

---

## Descrição dos campos retornados

| Campo JSON | Descrição | Campo Sankhya |
| --- | --- | --- |
| code | Nº Único do pedido | TGFCAB.NUNOTA |
| companyCode | Código da empresa | TGFCAB.CODEMP |
| value | Valor total do pedido | TGFCAB.VLRNOTA |
| partnerCode | Código do parceiro | TGFCAB.CODPARC |
| pending | Pedido pendente | TGFCAB.PENDENTE |
| confirmed | Pedido confirmado | TGFCAB.CONFIRMADA |
| operationTypeCode | Tipo de operação | TGFCAB.CODTIPOPER |
| operationAt | Data de negociação | TGFCAB.DTNEG |
| postedAt | Data entrada/saída | TGFCAB.DTENTSAI |
| movementAt | Data do movimento | TGFCAB.DTMOV |
| natureCode | Código natureza operação | TGFCAB.CODNAT |
| projectCode | Código do projeto | TGFCAB.CODPROJ |
| costCenterCode | Código centro de resultado | TGFCAB.CODCENCUS |
| sellerCode | Código do vendedor | TGFCAB.CODVEND |
| salesTypeCode | Tipo de negociação | TGFCAB.CODTIPVENDA |
| loadOrder | Ordem de carga | TGFCAB.ORDEMCARGA |
| transporterPartnerCode | Transportadora | TGFCAB.CODPARCTRANSP |
| freightType | Tipo de frete | TGFCAB.TIPFRETE |
| freightValue | Valor do frete | TGFCAB.VLRFRETE |
| icmsBase | Base ICMS | TGFCAB.BASEICMS |
| icmsValue | Valor ICMS | TGFCAB.VLRICMS |
| ipiBase | Base IPI | TGFCAB.BASEIPI |
| ipiValue | Valor IPI | TGFCAB.VLRIPI |
| totalDiscountValue | Desconto total | TGFCAB.VLRDESCTOT |
| itemsDiscountValue | Desconto por item | TGFCAB.VLRDESCTOTITEM |
| discountPercent | % de desconto | TGFCAB.PERCDESC |
| observation | Observação | TGFCAB.OBSERVACAO |
| nfeKey | Chave da NFe | TGFCAB.CHAVENFE |
| nfeStatus | Status da NFe | TGFCAB.STATUSNFE |
| movementType | Tipo de movimento | TGFCAB.TIPMOV |
| operationTypeUpdatedAt | Última alteração tipo de operação | TGFCAB.DHTIPOPER |
| salesTypeUpdatedAt | Última alteração tipo de venda | TGFCAB.DHTIPVENDA |
| invoicedAt | Data de faturamento | TGFCAB.DTFATUR |
| status | Status da nota | TGFCAB.STATUSNOTA |

---

## Exemplos de uso no Bot

### ✔ Exibir resumo de último pedido

```
Seu último pedido foi em {{detalhesPedido.content[0].operationAt}} no valor de R$ {{detalhesPedido.content[0].value}}.
```

---

### ✔ Listar múltiplos pedidos

Use um componente de lista para exibir pedidos recentes, iterando sobre `detalhesPedido.content`.

---

### ✔ Regras baseadas em status

```
Se {{detalhesPedido.content[0].pending}} = true
→ Exibir: Seu pedido ainda está pendente de faturamento.
```

---

## Tratamento de erros

| Cenário | Comportamento |
| --- | --- |
| Nenhum pedido encontrado | `size = 0` |
| Consulta malformada | `error` preenchido |
| Parceiro inexistente | `content = []` e `error = null` |

---

## Boas práticas

- Validar o código do parceiro antes da chamada
- Utilizar paginação para grandes volumes
- Salvar os pedidos para reuso em escopos globais
- Sempre tratar pedidos pendentes x confirmados

---

## Segurança

- A integração respeita permissões de visualização
- Requer autenticação via token de serviço interno
- Alto volume deve ser tratado com cache ou limites

---

Claro! Aqui está o **alerta técnico** que você pode incluir na documentação do componente **Obter Pedidos**, destacando o comportamento da API da Sankhya com relação à paginação e o campo `hasMore`:

---

## Alerta técnico sobre paginação e `hasMore`

### Atenção ao uso do parâmetro “Continuar Listagem (offsetPage)”

A API da Sankhya apresenta um comportamento específico no endpoint `CRUDServiceProvider.loadRecords` (com `outputType=json`), que **pode impactar diretamente a consulta de múltiplos pedidos**:

- Quando uma **página diferente de 0** é informada **sem que haja mais resultados disponíveis** (`hasMore = false`),
  a **API retorna novamente os mesmos registros da página 0**.
- Ou seja, **você pode acabar em um loop de repetição de dados**, acreditando estar acessando novos pedidos, quando na verdade está apenas repetindo o primeiro bloco de registros.

### Boas práticas recomendadas pela Sankhya:

- Só envie o valor de `offsetPage` diferente de 0 **se o campo** `hasMore` **retornado anteriormente for** `true`.
- Caso contrário, **mantenha o offsetPage = 0**, para evitar resultados duplicados ou comportamento inconsistente.

### Impacto no componente Neppo:

Ao preencher o campo **“Continuar Listagem (opcional)”** com um valor maior que `0`, **sem verificar antes se** `hasMore` **é** `true`, a plataforma da Sankhya **retornará os mesmos registros da página 0** — mesmo que você já tenha exibido esses pedidos.

**Requisições paginadas devem sempre seguir esta lógica:**

```
Se retorno anterior → hasMore = true
→ incrementar offsetPage
Senão
→ manter offsetPage = 0 ou encerrar paginação
```

---

## Retorno de erro

1. **Obter Pedidos com código não cadastrado na base**
   Quando o código do parceiro é válido no formato (numérico), mas não existe na base, a API retorna lista vazia (`content=[]`), `size=0` e sem erro.

```
{
  "scenario": "Obter Pedidos com código não cadastrado na base",
  "input": {
    "partnerCode": 123123
  },
  "response": {
    "hasMore": false,
    "size": 0,
    "content": [],
    "error": null
  }
}
```

2. **Obter Pedidos com código inválido**
   Quando o código do parceiro vem em formato inválido (não numérico), ocorre falha de integração/conversão e a API retorna `error` preenchido.

```
{
  "scenario": "Obter Pedidos com código inválido",
  "input": {
    "partnerCode": "aaaa"
  },
  "response": {
    "hasMore": false,
    "size": null,
    "content": null,
    "error": {
      "code": "SANKHYA_INTEGRATION_FAILED",
      "message": "Erro de conversão para número: aaaa"
    }
  }
}
```

3. **Obter Pedidos com Código Parceiro válido e Número do Pedido inexistente**

Quando o parceiro é válido, mas o filtro de número do pedido não encontra resultados, a API retorna lista vazia (`content=[]`), `size=0` e sem erro.

```
{
  "scenario": "Obter Pedidos com Código Parceiro Válido e Número do Pedido inexistente",
  "input": {
    "partnerCode": 654,
    "orderNumber": 123123123
  },
  "response": {
    "hasMore": false,
    "size": 0,
    "content": [],
    "error": null
  }
}
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
