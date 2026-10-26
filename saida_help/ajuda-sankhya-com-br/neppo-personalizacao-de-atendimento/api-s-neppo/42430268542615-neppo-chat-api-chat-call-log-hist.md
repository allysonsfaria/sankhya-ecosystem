---
id: "42430268542615"
titulo: "Neppo Chat API — Chat Call Log Hist"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430268542615-Neppo-Chat-API-Chat-Call-Log-Hist"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:21Z"
rotulos: ["sync_hc", "neppo", "neppo_784597012", "sync_hash_8aa11c784eda"]
---

# Neppo Chat API — Chat Call Log Hist

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430268542615-Neppo-Chat-API-Chat-Call-Log-Hist#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430268542615-Neppo-Chat-API-Chat-Call-Log-Hist#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430268542615-Neppo-Chat-API-Chat-Call-Log-Hist#Referencia-tecnica-completa)
- [V1 — chat-call-log-hist-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430268542615-Neppo-Chat-API-Chat-Call-Log-Hist#V1--chat-call-log-hist-controller-8-endpoints)
- [V2 — chat-call-log-hist-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430268542615-Neppo-Chat-API-Chat-Call-Log-Hist#V2--chat-call-log-hist-controller-v-2-4-endpoints)

**O que é este módulo?**

Mantém o histórico persistente de atendimentos fechados para consulta retroativa e compliance.

| Quem usa | Auditores, jurídico, analytics. |
| --- | --- |
| Problema que resolve | Logs ativos são rotacionados por performance. Sem histórico, atendimentos antigos ficam inacessíveis, prejudicando disputas e análises longas. |
| Impacto na experiência do cliente | Garante que qualquer atendimento passado possa ser consultado, o que é essencial para resolver disputas e proteger o cliente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar histórico** | Consulta atendimentos históricos com filtros avançados de data. |
| **Consultar atendimento histórico** | Obtém o detalhamento completo de um atendimento arquivado. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/call-log-hist/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-call-log-hist-controller` (8 endpoints)

### `/api/call-log-hist`

**findAll** · `operationId: findAllUsingPOST_28`

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
| 200 | OK | [PageResponse«ChatCallLogHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "callId": "string",
      "callerId": "string",
      "callerType": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "eventDate": "2024-01-01T00:00:00Z",
      "eventType": "string",
      "groupConfId": 0,
      "id": 0,
      "origCallId": "string",
      "origin": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/call-log-hist/delete`

**delete** · `operationId: deleteUsingDELETE_21`

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

### `/api/call-log-hist/save`

**insert** · `operationId: insertUsingPOST_21`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/call-log-hist/unique`

**findOne** · `operationId: findOneUsingPOST_24`

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
| 200 | OK | [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/call-log-hist`

**findAll** · `operationId: findAllUsingPOST_29`

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
| 200 | OK | [PageResponse«ChatCallLogHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "callId": "string",
      "callerId": "string",
      "callerType": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "eventDate": "2024-01-01T00:00:00Z",
      "eventType": "string",
      "groupConfId": 0,
      "id": 0,
      "origCallId": "string",
      "origin": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/call-log-hist/delete`

**delete** · `operationId: deleteUsingDELETE_22`

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

### `/api/v1/call-log-hist/save`

**insert** · `operationId: insertUsingPOST_22`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/call-log-hist/unique`

**findOne** · `operationId: findOneUsingPOST_25`

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
| 200 | OK | [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `chat-call-log-hist-controller-v-2` (4 endpoints)

### `/api/v2/call-log-hist`

**findAll** · `operationId: findAllUsingPOST_30`

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
| 200 | OK | [PageResponse«ChatCallLogHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "callId": "string",
      "callerId": "string",
      "callerType": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "eventDate": "2024-01-01T00:00:00Z",
      "eventType": "string",
      "groupConfId": 0,
      "id": 0,
      "origCallId": "string",
      "origin": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/call-log-hist/delete`

**delete** · `operationId: deleteUsingDELETE_23`

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

### `/api/v2/call-log-hist/save`

**insert** · `operationId: insertUsingPOST_23`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/call-log-hist/unique`

**findOne** · `operationId: findOneUsingPOST_26`

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
| 200 | OK | [ChatCallLogHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "callId": "string",
  "callerId": "string",
  "callerType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "eventDate": "2024-01-01T00:00:00Z",
  "eventType": "string",
  "groupConfId": 0,
  "id": 0,
  "origCallId": "string",
  "origin": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
