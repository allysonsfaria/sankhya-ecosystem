---
id: "42430254803991"
titulo: "Neppo Chat API — Chat Call Log"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254803991-Neppo-Chat-API-Chat-Call-Log"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:21Z"
rotulos: ["sync_hc", "neppo", "neppo_784596993", "sync_hash_67b5de2fc9d6"]
---

# Neppo Chat API — Chat Call Log

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254803991-Neppo-Chat-API-Chat-Call-Log#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254803991-Neppo-Chat-API-Chat-Call-Log#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254803991-Neppo-Chat-API-Chat-Call-Log#Referencia-tecnica-completa)
- [V1 — chat-call-log-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254803991-Neppo-Chat-API-Chat-Call-Log#V1--chat-call-log-controller-8-endpoints)
- [V2 — chat-call-log-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254803991-Neppo-Chat-API-Chat-Call-Log#V2--chat-call-log-controller-v-2-4-endpoints)

**O que é este módulo?**

Registra e consulta o log completo de atendimentos (sessões de chat) em tempo real.

| Quem usa | Supervisores, analistas de qualidade, sistemas de BI. |
| --- | --- |
| Problema que resolve | Sem log de atendimentos, não há visibilidade sobre o que acontece nas conversas, impossibilitando análise de qualidade e auditoria. |
| Impacto na experiência do cliente | Permite que a empresa monitore a qualidade de cada interação e identifique pontos de melhoria antes que impactem a satisfação do cliente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar logs** | Retorna todos os logs de atendimento com filtros por período, agente e canal. |
| **Consultar log específico** | Obtém os detalhes completos de um atendimento. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/call/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-call-log-controller` (8 endpoints)

### `/api/call`

**findAll** · `operationId: findAllUsingPOST_25`

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
| 200 | OK | [PageResponse«ChatCallLog»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "attendanceTime": 0,
      "callId": "string",
      "callMode": "string",
      "city": "string",
      "classified": true,
      "comment": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "externalId": "string",
      "finishedAt": "2024-01-01T00:00:00Z",
      "finishedByAgent": true,
      "groupConfId": 0,
      "id": 0,
      "ivrTime": 0,
      "kind": "string",
      "liked": true,
      "plataformCode": "string",
      "provider": "string",
      "ringingAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "startedAt": "2024-01-01T00:00:00Z",
      "startedByAgent": true,
      "state": "string",
      "status": "string",
      "tme": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "userId": 0
    }
  ]
}
```

---

### `/api/call/delete`

**delete** · `operationId: deleteUsingDELETE_18`

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

### `/api/call/save`

**insert** · `operationId: insertUsingPOST_18`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

---

### `/api/call/unique`

**findOne** · `operationId: findOneUsingPOST_21`

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
| 200 | OK | [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

---

### `/api/v1/call`

**findAll** · `operationId: findAllUsingPOST_26`

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
| 200 | OK | [PageResponse«ChatCallLog»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "attendanceTime": 0,
      "callId": "string",
      "callMode": "string",
      "city": "string",
      "classified": true,
      "comment": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "externalId": "string",
      "finishedAt": "2024-01-01T00:00:00Z",
      "finishedByAgent": true,
      "groupConfId": 0,
      "id": 0,
      "ivrTime": 0,
      "kind": "string",
      "liked": true,
      "plataformCode": "string",
      "provider": "string",
      "ringingAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "startedAt": "2024-01-01T00:00:00Z",
      "startedByAgent": true,
      "state": "string",
      "status": "string",
      "tme": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "userId": 0
    }
  ]
}
```

---

### `/api/v1/call/delete`

**delete** · `operationId: deleteUsingDELETE_19`

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

### `/api/v1/call/save`

**insert** · `operationId: insertUsingPOST_19`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

---

### `/api/v1/call/unique`

**findOne** · `operationId: findOneUsingPOST_22`

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
| 200 | OK | [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

---

## V2 — `chat-call-log-controller-v-2` (4 endpoints)

### `/api/v2/call`

**findAll** · `operationId: findAllUsingPOST_27`

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
| 200 | OK | [PageResponse«ChatCallLog»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "attendanceTime": 0,
      "callId": "string",
      "callMode": "string",
      "city": "string",
      "classified": true,
      "comment": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "externalId": "string",
      "finishedAt": "2024-01-01T00:00:00Z",
      "finishedByAgent": true,
      "groupConfId": 0,
      "id": 0,
      "ivrTime": 0,
      "kind": "string",
      "liked": true,
      "plataformCode": "string",
      "provider": "string",
      "ringingAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "startedAt": "2024-01-01T00:00:00Z",
      "startedByAgent": true,
      "state": "string",
      "status": "string",
      "tme": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "userId": 0
    }
  ]
}
```

---

### `/api/v2/call/delete`

**delete** · `operationId: deleteUsingDELETE_20`

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

### `/api/v2/call/save`

**insert** · `operationId: insertUsingPOST_20`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

---

### `/api/v2/call/unique`

**findOne** · `operationId: findOneUsingPOST_23`

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
| 200 | OK | [ChatCallLog](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "attendanceTime": 0,
  "callId": "string",
  "callMode": "string",
  "city": "string",
  "classified": true,
  "comment": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "externalId": "string",
  "finishedAt": "2024-01-01T00:00:00Z",
  "finishedByAgent": true,
  "groupConfId": 0,
  "id": 0,
  "ivrTime": 0,
  "kind": "string",
  "liked": true,
  "plataformCode": "string",
  "provider": "string",
  "ringingAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "startedAt": "2024-01-01T00:00:00Z",
  "startedByAgent": true,
  "state": "string",
  "status": "string",
  "tme": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userId": 0
}
```

---
