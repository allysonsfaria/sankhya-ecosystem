---
id: "42430243874711"
titulo: "Neppo Chat API — Guia de Busca, Filtros e Paginação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:01:17Z"
rotulos: ["sync_hc", "neppo", "neppo_783056918", "sync_hash_a7a6cc20f1fc"]
---

# Neppo Chat API — Guia de Busca, Filtros e Paginação

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  **🔎 Guia de Busca**  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Este guia explica como montar o **corpo (body) das requisições de busca e listagem**
usadas em toda a Neppo Chat API. Os endpoints de listagem (`findAll`) e de busca
individual (`findOne`) recebem um objeto com **filtros (conditions)**,
**ordenação** e **paginação**. As regras abaixo valem para todos os
controllers que usam `CustomRequest` e `CustomPageRequest`.

- [1. Autenticação — como usar o token](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#1-Autenticacao--como-usar-o-token)
- [2. Estrutura geral do corpo de busca](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#2-Estrutura-geral-do-corpo-de-busca)
- [3. Anatomia de uma condition](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#3-Anatomia-de-uma-condition)
- [4. Operadores válidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#4-Operadores-validos)
- [5. Lógica de combinação (AND / OR)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#5-Logica-de-combinacao-AND--OR)
- [6. Paginação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#6-Paginacao)
- [7. Exemplo completo e funcional](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#7-Exemplo-completo-e-funcional)
- [8. Erros e códigos de status](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243874711-Neppo-Chat-API-Guia-de-Busca-Filtros-e-Pagina%C3%A7%C3%A3o#8-Erros-e-codigos-de-status)

## 1. Autenticação — como usar o token

A API utiliza **OAuth2** (no gateway WSO2, combinada com basic auth e API key),
conforme descrito na página de Visão Geral. Todas as chamadas autenticadas devem enviar o token
no cabeçalho:

```
Authorization: Bearer <SEU_TOKEN>
```

Os endpoints declaram escopos `read` / `write` / `delete` conforme a operação.

[VERIFICAR: o endpoint de emissão do token, os parâmetros da requisição e o
formato da resposta dependem da configuração do gateway WSO2 e **não constam na especificação
Swagger desta API**. Confirmar com a equipe de plataforma antes de documentar o fluxo de
obtenção do token — esta seção descreve apenas o uso do token já emitido, que é o que está documentado.]

## 2. Estrutura geral do corpo de busca

O corpo de uma busca paginada (`CustomPageRequest`) tem o seguinte formato:

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `conditions` | array<Condition> | Não\* | Lista de filtros. Vazio/ausente retorna todos os registros (respeitando a paginação). \*Funcionalmente necessário para filtrar. |
| `page` | integer | **Sim** | Número da página (começa em `0`). Sem valor-padrão no `CustomPageRequest`. |
| `size` | integer | **Sim** | Quantidade de itens por página. Limite máximo padrão: **50** (configurável via `chat.api.max-page-size`). |
| `sort` | boolean | Não | Habilita ordenação dos resultados. Padrão: `false`. |
| `sortColumn` | string | Não | Nome do campo usado para ordenar (quando `sort=true`). |
| `direction` | string (enum) | Não | Direção da ordenação: `ASC` ou `DESC`. |

[VERIFICAR: confirmar se o backend exige `conditions` não-vazio
e se há validação que torne `page`/`size` obrigatórios na desserialização.]

## 3. Anatomia de uma condition

Cada item de `conditions` é um objeto **Condition** com os campos:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `key` | string | Nome do campo da entidade a ser filtrado (ex. `status`, `name`). |
| `value` | string | Valor de comparação. **Sempre enviado como string** (campo do tipo `String`), inclusive para comparações numéricas — use os operadores `*NUM` com o número entre aspas (ex.: `"5"`). Não é exigido por operadores como `NOT_NULL`, `IS_NULL`, `IS_TRUE`, `IS_FALSE`. |
| `operator` | string (enum) | Operador de comparação. Veja a tabela na seção 4. |
| `logic` | string (enum) | `AND` ou `OR` — define como esta condition se combina com a anterior (e como seus filhos aninhados se combinam). Veja a seção 5. |
| `and` | array<Condition> | Lista de conditions aninhadas (subgrupo). |
| `or` | array<Condition> | Lista de conditions aninhadas (subgrupo). |
| `conditions` | array<Condition> | Lista de conditions aninhadas (subgrupo). |

**Importante (comportamento real do motor de busca):** os três campos de
aninhamento — `and`, `or` e `conditions` — são
**equivalentes**: todos servem para agrupar subfiltros. O que define se o
subgrupo é combinado por E ou por OU com o restante é sempre o campo
`logic` da condition que os contém — **não** o nome do campo
(`and` vs `or`). Use o nome que tornar o JSON mais legível e controle a
combinação pelo `logic`.

## 4. Operadores válidos

Valores aceitos no campo `operator` (enum `Operator`):

| Operador | Significado | Descrição | Exemplo |
| --- | --- | --- | --- |
| `EQ` | Igualdade de texto | Campo é igual ao `value` (comparação como string). | `{"key": "status", "value": "OFFLINE", "operator": "EQ"}` |
| `EQNUM` | Igualdade numérica | Campo é igual ao `value` tratado como número. | `{"key": "maxChatChannels", "value": "5", "operator": "EQNUM"}` |
| `NEQ` | Diferente (texto) | Campo é diferente do `value` (comparação como string). | `{"key": "status", "value": "ONLINE", "operator": "NEQ"}` |
| `NEQNUM` | Diferente (numérico) | Campo é diferente do `value` tratado como número. | `{"key": "maxChatChannels", "value": "0", "operator": "NEQNUM"}` |
| `IS_TRUE` | Booleano verdadeiro | Campo booleano é `true`. Não exige `value`. | `{"key": "active", "operator": "IS_TRUE"}` |
| `IS_FALSE` | Booleano falso | Campo booleano é `false`. Não exige `value`. | `{"key": "active", "operator": "IS_FALSE"}` |
| `LIKE` | Contém / padrão | Campo de texto corresponde a um padrão (busca parcial). [VERIFICAR: confirmar uso de curingas, ex. `%`] | `{"key": "name", "value": "maria", "operator": "LIKE"}` |
| `NOT_LIKE` | Não contém | Campo de texto NÃO corresponde ao padrão. [VERIFICAR: confirmar uso de curingas] | `{"key": "name", "value": "teste", "operator": "NOT_LIKE"}` |
| `IN` | Está na lista | Campo está contido em uma lista de valores. [VERIFICAR: confirmar formato do `value` p/ lista — ex. separado por vírgula] | `{"key": "status", "value": "ONLINE,OFFLINE", "operator": "IN"}` |
| `NOT_IN` | Não está na lista | Campo NÃO está contido na lista de valores. [VERIFICAR: confirmar formato do `value`] | `{"key": "status", "value": "PAUSED", "operator": "NOT_IN"}` |
| `IS_NULL` | É nulo | Campo não possui valor (é `null`). Não exige `value`. | `{"key": "agentId", "operator": "IS_NULL"}` |
| `NOT_NULL` | Não é nulo | Campo possui algum valor (não é `null`). Não exige `value`. | `{"key": "status", "operator": "NOT_NULL"}` |
| `BEFORE` | Data anterior a | Campo de data/hora é anterior ao `value`. [VERIFICAR: confirmar formato de data esperado — ex. ISO-8601] | `{"key": "createdAt", "value": "2024-01-01T00:00:00Z", "operator": "BEFORE"}` |
| `AFTER` | Data posterior a | Campo de data/hora é posterior ao `value`. [VERIFICAR: confirmar formato de data esperado — ex. ISO-8601] | `{"key": "createdAt", "value": "2024-01-01T00:00:00Z", "operator": "AFTER"}` |

## 5. Lógica de combinação (AND / OR)

O campo `logic` aceita dois valores (enum `LogicEnum`):

| Valor | Efeito |
| --- | --- |
| `AND` | A condition (e seus subgrupos) precisa ser satisfeita **em conjunto** com as demais (E lógico). |
| `OR` | A condition (e seus subgrupos) é uma **alternativa** às demais (OU lógico). |

As conditions são avaliadas **na ordem em que aparecem**. A primeira inicia o
filtro; cada condition seguinte é combinada com o resultado acumulado de acordo com o seu próprio
`logic`. Quando uma condition possui subgrupo (`and`/`or`/`conditions`),
esse subgrupo é resolvido recursivamente e combinado pelo mesmo `logic`.

## 6. Paginação

| Campo | Descrição |
| --- | --- |
| `page` | Índice da página desejada, iniciando em `0`. Ex.: `page: 0` = primeira página. |
| `size` | Itens por página. Máximo padrão de **50** (parâmetro `chat.api.max-page-size`). Valores acima podem ser limitados pelo servidor. |

A resposta de listagem segue o modelo **PageResponse**:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `page` | integer | Página retornada. |
| `size` | integer | Tamanho da página. |
| `results` | array | Lista de registros encontrados. |

## 7. Exemplo completo e funcional

Busca que retorna registros cujo `status` não é nulo **E** que,
em um subgrupo, têm `maxChatChannels = 5` **OU** `status = OFFLINE`,
trazendo a primeira página com 10 itens:

```
{
  "conditions": [
    {
      "key": "status",
      "operator": "NOT_NULL",
      "logic": "AND",
      "and": [
        { "key": "maxChatChannels", "value": "5", "operator": "EQNUM" },
        { "key": "status", "value": "OFFLINE", "operator": "EQ", "logic": "OR" }
      ]
    }
  ],
  "page": 0,
  "size": 10
}
```

**Chamada** (salve o JSON acima como `busca.json`):

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/agent" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d @busca.json
```

**Exemplo de resposta** (`200 OK` — PageResponse):

```
{
  "page": 0,
  "size": 10,
  "results": [
    {
      "id": 42,
      "name": "Maria Silva",
      "status": "OFFLINE",
      "maxChatChannels": 5
    }
  ]
}
```

### Exemplo simples (um único filtro)

Buscar contatos cujo nome contenha "maria":

```
{
  "conditions": [
    { "key": "name", "value": "maria", "operator": "LIKE" }
  ],
  "page": 0,
  "size": 20
}
```

## 8. Erros e códigos de status

| Código | Significado | O que costuma indicar |
| --- | --- | --- |
| `200` | OK | Requisição bem-sucedida. |
| `201` | Created | Recurso criado com sucesso. |
| `204` | No Content | Operação concluída sem corpo de resposta (ex. exclusão). |
| `400` | Bad Request | Corpo malformado, operador inválido ou tipo de `value` incompatível. |
| `401` | Unauthorized | Token ausente, expirado ou inválido. |
| `403` | Forbidden | Token válido, mas sem o escopo necessário (`read`/`write`/`delete`). |
| `404` | Not Found | Recurso ou rota inexistente. |
| `422` | Unprocessable Entity | Regra de negócio violada (ver módulo Custom Error). |
| `500` | Internal Server Error | Falha inesperada no servidor. |

[VERIFICAR: confirmar o catálogo de códigos de erro de negócio específicos
da plataforma (módulo Custom Error) e suas mensagens.]
