---
id: "42430228382487"
titulo: "Neppo Chat API — Chat Suggestion"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430228382487-Neppo-Chat-API-Chat-Suggestion"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:38Z"
rotulos: ["sync_hc", "neppo", "neppo_782991363", "sync_hash_4548af1a8c0e"]
---

# Neppo Chat API — Chat Suggestion

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430228382487-Neppo-Chat-API-Chat-Suggestion#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430228382487-Neppo-Chat-API-Chat-Suggestion#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430228382487-Neppo-Chat-API-Chat-Suggestion#Referencia-tecnica-completa)
- [V1 — chat-suggestion-controller (12 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430228382487-Neppo-Chat-API-Chat-Suggestion#V1--chat-suggestion-controller-12-endpoints)

**O que é este módulo?**

Gerencia sugestões inteligentes de resposta exibidas para o atendente durante a conversa, baseadas no contexto do chat.

| Quem usa | Atendentes, produto (IA assistiva). |
| --- | --- |
| Problema que resolve | Atendentes inexperientes demoram para formular respostas ou podem não conhecer todas as opções disponíveis para o cliente. |
| Impacto na experiência do cliente | O cliente recebe respostas mais assertivas e rápidas, pois o atendente é guiado pela IA para as melhores opções. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar sugestões** | Retorna sugestões configuradas para um contexto específico. |
| **Criar sugestão** | Adiciona uma nova sugestão baseada em palavras-chave ou intenção. |
| **Atualizar sugestão** | Modifica quando e como a sugestão é exibida. |
| **Remover sugestão** | Exclui uma sugestão do sistema. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/chat/suggestion/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-suggestion-controller` (12 endpoints)

### `/api/chat/suggestion`

**findAll** · `operationId: findAllUsingPOST_40`

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
| 200 | OK | [PageResponse«ChatSuggestion»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      },
      "suggestion": "string"
    }
  ]
}
```

---

### `/api/chat/suggestion/delete`

**delete** · `operationId: deleteUsingDELETE_27`

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

### `/api/chat/suggestion/save`

**insert** · `operationId: insertUsingPOST_27`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

---

### `/api/chat/suggestion/unique`

**findOne** · `operationId: findOneUsingPOST_36`

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
| 200 | OK | [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

---

### `/api/v1/chat/suggestion`

**findAll** · `operationId: findAllUsingPOST_41`

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
| 200 | OK | [PageResponse«ChatSuggestion»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      },
      "suggestion": "string"
    }
  ]
}
```

---

### `/api/v1/chat/suggestion/delete`

**delete** · `operationId: deleteUsingDELETE_28`

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

### `/api/v1/chat/suggestion/save`

**insert** · `operationId: insertUsingPOST_28`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

---

### `/api/v1/chat/suggestion/unique`

**findOne** · `operationId: findOneUsingPOST_37`

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
| 200 | OK | [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

---

### `/api/v2/chat/suggestion`

**findAll** · `operationId: findAllUsingPOST_42`

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
| 200 | OK | [PageResponse«ChatSuggestion»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      },
      "suggestion": "string"
    }
  ]
}
```

---

### `/api/v2/chat/suggestion/delete`

**delete** · `operationId: deleteUsingDELETE_29`

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

### `/api/v2/chat/suggestion/save`

**insert** · `operationId: insertUsingPOST_29`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

---

### `/api/v2/chat/suggestion/unique`

**findOne** · `operationId: findOneUsingPOST_38`

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
| 200 | OK | [ChatSuggestion](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
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
  },
  "suggestion": "string"
}
```

---
