---
id: "42430229203223"
titulo: "Neppo Chat API — Tag Bot"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229203223-Neppo-Chat-API-Tag-Bot"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:36Z"
rotulos: ["sync_hc", "neppo", "neppo_783187983", "sync_hash_5c8ab003d48e"]
---

# Neppo Chat API — Tag Bot

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229203223-Neppo-Chat-API-Tag-Bot#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229203223-Neppo-Chat-API-Tag-Bot#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229203223-Neppo-Chat-API-Tag-Bot#Referencia-tecnica-completa)
- [V1 — tag-bot-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229203223-Neppo-Chat-API-Tag-Bot#V1--tag-bot-controller-8-endpoints)
- [V2 — tag-bot-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229203223-Neppo-Chat-API-Tag-Bot#V2--tag-bot-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia tags aplicadas pelos bots durante conversas para categorização automática e roteamento.

| Quem usa | Times de automação, produto, operação. |
| --- | --- |
| Problema que resolve | Sem tags automáticas, o bot não consegue categorizar conversas em tempo real, exigindo classificação manual posterior. |
| Impacto na experiência do cliente | O atendimento é roteado automaticamente para o grupo certo com base nas tags detectadas pelo bot, sem demora. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar tags** | Retorna todas as tags configuradas para uso por bots. |
| **Criar tag** | Adiciona uma nova tag ao catálogo do bot. |
| **Atualizar tag** | Modifica o nome ou comportamento de uma tag. |
| **Remover tag** | Exclui uma tag do catálogo. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/tag-bot/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `tag-bot-controller` (8 endpoints)

### `/api/tag-bot`

**findAll** · `operationId: findAllUsingPOST_97`

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
| 200 | OK | [PageResponse«ChatTagBot»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "bot": {
        "active": true,
        "agent": {},
        "botTree": {},
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "external": true,
        "id": 0,
        "survey": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "message": "string",
      "session": {
        "agent": {},
        "agentConnectedInstance": "string",
        "agentConnectedResource": "string",
        "attendedAt": "2024-01-01T00:00:00Z",
        "availableAt": "2024-01-01T00:00:00Z",
        "closedAt": "2024-01-01T00:00:00Z",
        "closedBy": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "customProtocol": "string",
        "directMessageId": 0,
        "externalOrderId": 0,
        "externalProtocol": "string",
        "groupConf": {},
        "groupList": "string",
        "hasReservedWord": true,
        "id": 0,
        "inactivity": "string",
        "lastAgent": "string",
        "onlyBot": true,
        "pending": true,
        "priority": true,
        "properties": "string",
        "protocol": "string",
        "status": "string",
        "ticketId": 0,
        "tma": 0,
        "tmaTicket": 0,
        "tme": 0,
        "tmi": 0,
        "tmia": 0,
        "tmic": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "user": {},
        "userConnectedInstance": "string",
        "userConnectedResource": "string"
      },
      "tag": "string"
    }
  ]
}
```

---

### `/api/tag-bot/delete`

**delete** · `operationId: deleteUsingDELETE_75`

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

### `/api/tag-bot/save`

**insert** · `operationId: insertUsingPOST_75`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

---

### `/api/tag-bot/unique`

**findOne** · `operationId: findOneUsingPOST_90`

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
| 200 | OK | [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

---

### `/api/v1/tag-bot`

**findAll** · `operationId: findAllUsingPOST_98`

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
| 200 | OK | [PageResponse«ChatTagBot»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "bot": {
        "active": true,
        "agent": {},
        "botTree": {},
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "external": true,
        "id": 0,
        "survey": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "message": "string",
      "session": {
        "agent": {},
        "agentConnectedInstance": "string",
        "agentConnectedResource": "string",
        "attendedAt": "2024-01-01T00:00:00Z",
        "availableAt": "2024-01-01T00:00:00Z",
        "closedAt": "2024-01-01T00:00:00Z",
        "closedBy": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "customProtocol": "string",
        "directMessageId": 0,
        "externalOrderId": 0,
        "externalProtocol": "string",
        "groupConf": {},
        "groupList": "string",
        "hasReservedWord": true,
        "id": 0,
        "inactivity": "string",
        "lastAgent": "string",
        "onlyBot": true,
        "pending": true,
        "priority": true,
        "properties": "string",
        "protocol": "string",
        "status": "string",
        "ticketId": 0,
        "tma": 0,
        "tmaTicket": 0,
        "tme": 0,
        "tmi": 0,
        "tmia": 0,
        "tmic": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "user": {},
        "userConnectedInstance": "string",
        "userConnectedResource": "string"
      },
      "tag": "string"
    }
  ]
}
```

---

### `/api/v1/tag-bot/delete`

**delete** · `operationId: deleteUsingDELETE_76`

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

### `/api/v1/tag-bot/save`

**insert** · `operationId: insertUsingPOST_76`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

---

### `/api/v1/tag-bot/unique`

**findOne** · `operationId: findOneUsingPOST_91`

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
| 200 | OK | [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

---

## V2 — `tag-bot-controller-v-2` (4 endpoints)

### `/api/v2/tag-bot`

**findAll** · `operationId: findAllUsingPOST_99`

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
| 200 | OK | [PageResponse«ChatTagBot»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "bot": {
        "active": true,
        "agent": {},
        "botTree": {},
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "external": true,
        "id": 0,
        "survey": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "message": "string",
      "session": {
        "agent": {},
        "agentConnectedInstance": "string",
        "agentConnectedResource": "string",
        "attendedAt": "2024-01-01T00:00:00Z",
        "availableAt": "2024-01-01T00:00:00Z",
        "closedAt": "2024-01-01T00:00:00Z",
        "closedBy": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "customProtocol": "string",
        "directMessageId": 0,
        "externalOrderId": 0,
        "externalProtocol": "string",
        "groupConf": {},
        "groupList": "string",
        "hasReservedWord": true,
        "id": 0,
        "inactivity": "string",
        "lastAgent": "string",
        "onlyBot": true,
        "pending": true,
        "priority": true,
        "properties": "string",
        "protocol": "string",
        "status": "string",
        "ticketId": 0,
        "tma": 0,
        "tmaTicket": 0,
        "tme": 0,
        "tmi": 0,
        "tmia": 0,
        "tmic": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "user": {},
        "userConnectedInstance": "string",
        "userConnectedResource": "string"
      },
      "tag": "string"
    }
  ]
}
```

---

### `/api/v2/tag-bot/delete`

**delete** · `operationId: deleteUsingDELETE_77`

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

### `/api/v2/tag-bot/save`

**insert** · `operationId: insertUsingPOST_77`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

---

### `/api/v2/tag-bot/unique`

**findOne** · `operationId: findOneUsingPOST_92`

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
| 200 | OK | [ChatTagBot](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "bot": {
    "active": true,
    "agent": {},
    "botTree": {},
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "external": true,
    "id": 0,
    "survey": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "message": "string",
  "session": {
    "agent": {},
    "agentConnectedInstance": "string",
    "agentConnectedResource": "string",
    "attendedAt": "2024-01-01T00:00:00Z",
    "availableAt": "2024-01-01T00:00:00Z",
    "closedAt": "2024-01-01T00:00:00Z",
    "closedBy": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "customProtocol": "string",
    "directMessageId": 0,
    "externalOrderId": 0,
    "externalProtocol": "string",
    "groupConf": {},
    "groupList": "string",
    "hasReservedWord": true,
    "id": 0,
    "inactivity": "string",
    "lastAgent": "string",
    "onlyBot": true,
    "pending": true,
    "priority": true,
    "properties": "string",
    "protocol": "string",
    "status": "string",
    "ticketId": 0,
    "tma": 0,
    "tmaTicket": 0,
    "tme": 0,
    "tmi": 0,
    "tmia": 0,
    "tmic": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "userConnectedInstance": "string",
    "userConnectedResource": "string"
  },
  "tag": "string"
}
```

---
