---
id: "42430244664343"
titulo: "Neppo Chat API — Chat Answer"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244664343-Neppo-Chat-API-Chat-Answer"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:34Z"
rotulos: ["sync_hc", "neppo", "neppo_783417348", "sync_hash_05b716cdcb34"]
---

# Neppo Chat API — Chat Answer

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244664343-Neppo-Chat-API-Chat-Answer#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244664343-Neppo-Chat-API-Chat-Answer#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244664343-Neppo-Chat-API-Chat-Answer#Referencia-tecnica-completa)
- [V1 — chat-answer-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244664343-Neppo-Chat-API-Chat-Answer#V1--chat-answer-controller-8-endpoints)
- [V2 — chat-answer-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244664343-Neppo-Chat-API-Chat-Answer#V2--chat-answer-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia respostas rápidas pré-configuradas que os atendentes podem usar durante o chat.

| Quem usa | Atendentes, supervisores de qualidade, gestores de conteúdo. |
| --- | --- |
| Problema que resolve | Atendentes perdem tempo digitando as mesmas respostas repetidamente, com risco de inconsistências na comunicação da marca. |
| Impacto na experiência do cliente | O cliente recebe respostas rápidas, padronizadas e sem erros, melhorando a percepção de profissionalismo da empresa. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar respostas rápidas** | Retorna todas as respostas rápidas disponíveis para os atendentes. |
| **Criar resposta rápida** | Cadastra uma nova resposta com atalho e conteúdo. |
| **Atualizar resposta** | Modifica o conteúdo ou atalho de uma resposta existente. |
| **Remover resposta** | Exclui uma resposta rápida do catálogo. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/chat-answer/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-answer-controller` (8 endpoints)

### `/api/chat-answer`

**findAll** · `operationId: findAllUsingPOST_22`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CustomPageRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "conditions": [
    {
      "key": "status",
      "value": "OFFLINE",
      "operator": "EQ",
      "logic": "AND"
    }
  ],
  "page": 0,
  "size": 10
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [PageResponse«ChatAnswer»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "page": 0,
  "size": 10,
  "results": [
    {
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "optionAnswerId": 0,
      "questionId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "value": "string"
    }
  ]
}
```

---

### `/api/chat-answer/delete`

**delete** · `operationId: deleteUsingDELETE_15`

Auth: Application & Application User | Escopos: `delete`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): integer (int64)

Exemplo de corpo:

```
42
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | boolean |
| 204 | No Content | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |

Exemplo de resposta (`200 OK`):

```
true
```

---

### `/api/chat-answer/save`

**insert** · `operationId: insertUsingPOST_15`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

---

### `/api/chat-answer/unique`

**findOne** · `operationId: findOneUsingPOST_18`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CustomRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "conditions": [
    {
      "key": "id",
      "value": "42",
      "operator": "EQNUM"
    }
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

---

### `/api/v1/chat-answer`

**findAll** · `operationId: findAllUsingPOST_23`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CustomPageRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "conditions": [
    {
      "key": "status",
      "value": "OFFLINE",
      "operator": "EQ",
      "logic": "AND"
    }
  ],
  "page": 0,
  "size": 10
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [PageResponse«ChatAnswer»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "page": 0,
  "size": 10,
  "results": [
    {
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "optionAnswerId": 0,
      "questionId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "value": "string"
    }
  ]
}
```

---

### `/api/v1/chat-answer/delete`

**delete** · `operationId: deleteUsingDELETE_16`

Auth: Application & Application User | Escopos: `delete`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): integer (int64)

Exemplo de corpo:

```
42
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | boolean |
| 204 | No Content | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |

Exemplo de resposta (`200 OK`):

```
true
```

---

### `/api/v1/chat-answer/save`

**insert** · `operationId: insertUsingPOST_16`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

---

### `/api/v1/chat-answer/unique`

**findOne** · `operationId: findOneUsingPOST_19`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CustomRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "conditions": [
    {
      "key": "id",
      "value": "42",
      "operator": "EQNUM"
    }
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

---

## V2 — `chat-answer-controller-v-2` (4 endpoints)

### `/api/v2/chat-answer`

**findAll** · `operationId: findAllUsingPOST_24`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CustomPageRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "conditions": [
    {
      "key": "status",
      "value": "OFFLINE",
      "operator": "EQ",
      "logic": "AND"
    }
  ],
  "page": 0,
  "size": 10
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [PageResponse«ChatAnswer»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "page": 0,
  "size": 10,
  "results": [
    {
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "optionAnswerId": 0,
      "questionId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "value": "string"
    }
  ]
}
```

---

### `/api/v2/chat-answer/delete`

**delete** · `operationId: deleteUsingDELETE_17`

Auth: Application & Application User | Escopos: `delete`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): integer (int64)

Exemplo de corpo:

```
42
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | boolean |
| 204 | No Content | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |

Exemplo de resposta (`200 OK`):

```
true
```

---

### `/api/v2/chat-answer/save`

**insert** · `operationId: insertUsingPOST_17`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

---

### `/api/v2/chat-answer/unique`

**findOne** · `operationId: findOneUsingPOST_20`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CustomRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "conditions": [
    {
      "key": "id",
      "value": "42",
      "operator": "EQNUM"
    }
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "optionAnswerId": 0,
  "questionId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "value": "string"
}
```

---
