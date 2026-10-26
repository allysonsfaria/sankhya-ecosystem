---
id: "42430254388759"
titulo: "Neppo Chat API — Bot Answer"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254388759-Neppo-Chat-API-Bot-Answer"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:23Z"
rotulos: ["sync_hc", "neppo", "neppo_784334858", "sync_hash_0d7ee2481763"]
---

# Neppo Chat API — Bot Answer

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254388759-Neppo-Chat-API-Bot-Answer#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254388759-Neppo-Chat-API-Bot-Answer#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254388759-Neppo-Chat-API-Bot-Answer#Referencia-tecnica-completa)
- [V1 — bot-answer-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254388759-Neppo-Chat-API-Bot-Answer#V1--bot-answer-controller-8-endpoints)
- [V2 — bot-answer-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254388759-Neppo-Chat-API-Bot-Answer#V2--bot-answer-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia as respostas configuradas nos fluxos dos chatbots.

| Quem usa | Analistas de automação, criadores de conteúdo de bot. |
| --- | --- |
| Problema que resolve | Sem gerenciar as respostas do bot, não é possível atualizar o conteúdo sem acessar o sistema de configuração diretamente. |
| Impacto na experiência do cliente | As respostas do bot ficam sempre atualizadas e relevantes, melhorando a assertividade no atendimento automático. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar respostas** | Retorna todas as respostas configuradas para um bot. |
| **Criar resposta** | Adiciona uma nova resposta a um nó do fluxo do bot. |
| **Atualizar resposta** | Modifica o conteúdo ou condições de uma resposta existente. |
| **Remover resposta** | Exclui uma resposta do fluxo do bot. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/bot-answer/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `bot-answer-controller` (8 endpoints)

### `/api/bot-answer`

**findAll** · `operationId: findAllUsingPOST_12`

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
| 200 | OK | [PageResponse«BotAnswer»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "answer": "string",
      "botQuestions": {
        "active": true,
        "id": 0,
        "question": "string",
        "seq": 0
      },
      "id": 0,
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
      }
    }
  ]
}
```

---

### `/api/bot-answer/delete`

**delete** · `operationId: deleteUsingDELETE_9`

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

### `/api/bot-answer/save`

**insert** · `operationId: insertUsingPOST_9`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

---

### `/api/bot-answer/unique`

**findOne** · `operationId: findOneUsingPOST_12`

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
| 200 | OK | [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

---

### `/api/v1/bot-answer`

**findAll** · `operationId: findAllUsingPOST_13`

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
| 200 | OK | [PageResponse«BotAnswer»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "answer": "string",
      "botQuestions": {
        "active": true,
        "id": 0,
        "question": "string",
        "seq": 0
      },
      "id": 0,
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
      }
    }
  ]
}
```

---

### `/api/v1/bot-answer/delete`

**delete** · `operationId: deleteUsingDELETE_10`

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

### `/api/v1/bot-answer/save`

**insert** · `operationId: insertUsingPOST_10`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

---

### `/api/v1/bot-answer/unique`

**findOne** · `operationId: findOneUsingPOST_13`

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
| 200 | OK | [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

---

## V2 — `bot-answer-controller-v-2` (4 endpoints)

### `/api/v2/bot-answer`

**findAll** · `operationId: findAllUsingPOST_14`

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
| 200 | OK | [PageResponse«BotAnswer»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "answer": "string",
      "botQuestions": {
        "active": true,
        "id": 0,
        "question": "string",
        "seq": 0
      },
      "id": 0,
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
      }
    }
  ]
}
```

---

### `/api/v2/bot-answer/delete`

**delete** · `operationId: deleteUsingDELETE_11`

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

### `/api/v2/bot-answer/save`

**insert** · `operationId: insertUsingPOST_11`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

---

### `/api/v2/bot-answer/unique`

**findOne** · `operationId: findOneUsingPOST_14`

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
| 200 | OK | [BotAnswer](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "answer": "string",
  "botQuestions": {
    "active": true,
    "id": 0,
    "question": "string",
    "seq": 0
  },
  "id": 0,
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
  }
}
```

---
