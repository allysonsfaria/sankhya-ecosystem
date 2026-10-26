---
id: "42430229750039"
titulo: "Neppo Chat API — Message"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229750039-Neppo-Chat-API-Message"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:34Z"
rotulos: ["sync_hc", "neppo", "neppo_783417367", "sync_hash_bc4f2741263d"]
---

# Neppo Chat API — Message

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229750039-Neppo-Chat-API-Message#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229750039-Neppo-Chat-API-Message#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229750039-Neppo-Chat-API-Message#Referencia-tecnica-completa)
- [V1 — message-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229750039-Neppo-Chat-API-Message#V1--message-controller-8-endpoints)
- [V2 — message-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430229750039-Neppo-Chat-API-Message#V2--message-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia as mensagens trocadas nas conversas de atendimento — o núcleo da plataforma.

| Quem usa | Interface do atendente, bots, integrações. |
| --- | --- |
| Problema que resolve | Sem controle de mensagens, não há como armazenar o histórico das conversas nem garantir entrega e ordenação correta. |
| Impacto na experiência do cliente | Toda conversa fica registrada e acessível, permitindo continuidade no atendimento mesmo com troca de atendente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar mensagens** | Retorna as mensagens de uma sessão de atendimento. |
| **Enviar mensagem** | Envia uma mensagem de texto, imagem, documento ou áudio. |
| **Buscar mensagem** | Consulta uma mensagem específica pelo ID. |
| **Marcar como lida** | Atualiza o status de leitura de uma mensagem. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/messages/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `message-controller` (8 endpoints)

### `/api/messages`

**findAll** · `operationId: findAllUsingPOST_82`

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
| 200 | OK | [PageResponse«ChatMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "caption": "string",
      "cognition": {
        "appId": "string",
        "appKey": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "endPoint": "string",
        "id": 0,
        "name": "string",
        "password": "string",
        "type": "string",
        "userName": "string",
        "version": "string"
      },
      "contentType": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "errorConversation": true,
      "fromUser": "string",
      "id": 0,
      "message": "string",
      "repliedMessage": "string",
      "sendBy": "string",
      "sentBySuperAgent": true,
      "sentiment": "string",
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
      "toUser": "string"
    }
  ]
}
```

---

### `/api/messages/delete`

**delete** · `operationId: deleteUsingDELETE_63`

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

### `/api/messages/save`

**insert** · `operationId: insertUsingPOST_66`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

---

### `/api/messages/unique`

**findOne** · `operationId: findOneUsingPOST_78`

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
| 200 | OK | [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

---

### `/api/v1/messages`

**findAll** · `operationId: findAllUsingPOST_83`

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
| 200 | OK | [PageResponse«ChatMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "caption": "string",
      "cognition": {
        "appId": "string",
        "appKey": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "endPoint": "string",
        "id": 0,
        "name": "string",
        "password": "string",
        "type": "string",
        "userName": "string",
        "version": "string"
      },
      "contentType": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "errorConversation": true,
      "fromUser": "string",
      "id": 0,
      "message": "string",
      "repliedMessage": "string",
      "sendBy": "string",
      "sentBySuperAgent": true,
      "sentiment": "string",
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
      "toUser": "string"
    }
  ]
}
```

---

### `/api/v1/messages/delete`

**delete** · `operationId: deleteUsingDELETE_64`

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

### `/api/v1/messages/save`

**insert** · `operationId: insertUsingPOST_67`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

---

### `/api/v1/messages/unique`

**findOne** · `operationId: findOneUsingPOST_79`

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
| 200 | OK | [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

---

## V2 — `message-controller-v-2` (4 endpoints)

### `/api/v2/messages`

**findAll** · `operationId: findAllUsingPOST_84`

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
| 200 | OK | [PageResponse«ChatMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "caption": "string",
      "cognition": {
        "appId": "string",
        "appKey": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "endPoint": "string",
        "id": 0,
        "name": "string",
        "password": "string",
        "type": "string",
        "userName": "string",
        "version": "string"
      },
      "contentType": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "errorConversation": true,
      "fromUser": "string",
      "id": 0,
      "message": "string",
      "repliedMessage": "string",
      "sendBy": "string",
      "sentBySuperAgent": true,
      "sentiment": "string",
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
      "toUser": "string"
    }
  ]
}
```

---

### `/api/v2/messages/delete`

**delete** · `operationId: deleteUsingDELETE_65`

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

### `/api/v2/messages/save`

**insert** · `operationId: insertUsingPOST_68`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

---

### `/api/v2/messages/unique`

**findOne** · `operationId: findOneUsingPOST_80`

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
| 200 | OK | [ChatMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "caption": "string",
  "cognition": {
    "appId": "string",
    "appKey": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "endPoint": "string",
    "id": 0,
    "name": "string",
    "password": "string",
    "type": "string",
    "userName": "string",
    "version": "string"
  },
  "contentType": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "errorConversation": true,
  "fromUser": "string",
  "id": 0,
  "message": "string",
  "repliedMessage": "string",
  "sendBy": "string",
  "sentBySuperAgent": true,
  "sentiment": "string",
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
  "toUser": "string"
}
```

---
