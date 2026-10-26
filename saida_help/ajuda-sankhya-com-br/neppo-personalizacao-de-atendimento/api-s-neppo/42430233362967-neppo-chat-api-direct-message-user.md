---
id: "42430233362967"
titulo: "Neppo Chat API — Direct Message User"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430233362967-Neppo-Chat-API-Direct-Message-User"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:20Z"
rotulos: ["sync_hc", "neppo", "neppo_784597031", "sync_hash_51bf1a05cbfd"]
---

# Neppo Chat API — Direct Message User

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430233362967-Neppo-Chat-API-Direct-Message-User#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430233362967-Neppo-Chat-API-Direct-Message-User#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430233362967-Neppo-Chat-API-Direct-Message-User#Referencia-tecnica-completa)
- [V1 — direct-message-user-controller (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430233362967-Neppo-Chat-API-Direct-Message-User#V1--direct-message-user-controller-4-endpoints)
- [V2 — direct-message-user-controller-v-2 (2 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430233362967-Neppo-Chat-API-Direct-Message-User#V2--direct-message-user-controller-v-2-2-endpoints)

**O que é este módulo?**

Gerencia os usuários participantes de conversas de mensagem direta.

| Quem usa | Sistema de mensageria interno. |
| --- | --- |
| Problema que resolve | Sem controle de participantes, não é possível criar conversas em grupo ou gerenciar quem tem acesso a qual conversa. |
| Impacto na experiência do cliente | Permite que equipes colaborem em grupos contextuais (por cliente, por campanha), acelerando a resolução. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar usuários da conversa** | Retorna os participantes de uma conversa específica. |
| **Adicionar usuário** | Inclui um novo participante em uma conversa de grupo. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/direct-message-user/unique" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "conditions": [
    {
      "key": "id",
      "value": "42",
      "operator": "EQNUM"
    }
  ]
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "userId": 0
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `direct-message-user-controller` (4 endpoints)

### `/api/direct-message-user`

**findAll** · `operationId: findAllUsingPOST_61`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«ChatDirectMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "additionalInfo": "string",
      "agentId": 0,
      "broadcastListId": 0,
      "callback": "string",
      "campaignName": "string",
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "dispatchId": 0,
      "email": "string",
      "executionId": 0,
      "generatedSession": true,
      "groupConfId": 0,
      "groupName": "string",
      "hsmTemplate": 0,
      "id": 0,
      "message": "string",
      "phoneNumber": "string",
      "recipientId": "string",
      "resend": true,
      "sendGroupConfId": 0,
      "sendTimestamp": "string",
      "senderUserId": 0,
      "sentAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "status": "string",
      "subject": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "user": {
        "accessKey": "string",
        "active": true,
        "agent": {},
        "birthDate": "2024-01-01T00:00:00Z",
        "company": {},
        "country": "string",
        "cpf": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "createdFromSurvey": true,
        "defaultLocale": "string",
        "displayName": "string",
        "email": "string",
        "externalCode": "string",
        "firstAccess": true,
        "firstLogin": "2024-01-01T00:00:00Z",
        "formal": true,
        "id": 0,
        "lastLogin": "2024-01-01T00:00:00Z",
        "name": "string",
        "operation": "string",
        "originUser": "string",
        "phone": "string",
        "priority": 0,
        "profile": {},
        "ticketUserId": 0,
        "tm2": true,
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "userName": "string",
        "usingMFA": true,
        "visible": true,
        "password": "string"
      },
      "userId": 0
    }
  ]
}
```

---

### `/api/direct-message-user/unique`

**findOne** · `operationId: findOneUsingPOST_57`

Auth: Application & Application User

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
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "userId": 0
}
```

---

### `/api/v1/direct-message-user`

**findAll** · `operationId: findAllUsingPOST_62`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«ChatDirectMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "additionalInfo": "string",
      "agentId": 0,
      "broadcastListId": 0,
      "callback": "string",
      "campaignName": "string",
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "dispatchId": 0,
      "email": "string",
      "executionId": 0,
      "generatedSession": true,
      "groupConfId": 0,
      "groupName": "string",
      "hsmTemplate": 0,
      "id": 0,
      "message": "string",
      "phoneNumber": "string",
      "recipientId": "string",
      "resend": true,
      "sendGroupConfId": 0,
      "sendTimestamp": "string",
      "senderUserId": 0,
      "sentAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "status": "string",
      "subject": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "user": {
        "accessKey": "string",
        "active": true,
        "agent": {},
        "birthDate": "2024-01-01T00:00:00Z",
        "company": {},
        "country": "string",
        "cpf": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "createdFromSurvey": true,
        "defaultLocale": "string",
        "displayName": "string",
        "email": "string",
        "externalCode": "string",
        "firstAccess": true,
        "firstLogin": "2024-01-01T00:00:00Z",
        "formal": true,
        "id": 0,
        "lastLogin": "2024-01-01T00:00:00Z",
        "name": "string",
        "operation": "string",
        "originUser": "string",
        "phone": "string",
        "priority": 0,
        "profile": {},
        "ticketUserId": 0,
        "tm2": true,
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "userName": "string",
        "usingMFA": true,
        "visible": true,
        "password": "string"
      },
      "userId": 0
    }
  ]
}
```

---

### `/api/v1/direct-message-user/unique`

**findOne** · `operationId: findOneUsingPOST_58`

Auth: Application & Application User

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
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "userId": 0
}
```

---

## V2 — `direct-message-user-controller-v-2` (2 endpoints)

### `/api/v2/direct-message-user`

**findAll** · `operationId: findAllUsingPOST_63`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«ChatDirectMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "additionalInfo": "string",
      "agentId": 0,
      "broadcastListId": 0,
      "callback": "string",
      "campaignName": "string",
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "dispatchId": 0,
      "email": "string",
      "executionId": 0,
      "generatedSession": true,
      "groupConfId": 0,
      "groupName": "string",
      "hsmTemplate": 0,
      "id": 0,
      "message": "string",
      "phoneNumber": "string",
      "recipientId": "string",
      "resend": true,
      "sendGroupConfId": 0,
      "sendTimestamp": "string",
      "senderUserId": 0,
      "sentAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "status": "string",
      "subject": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "user": {
        "accessKey": "string",
        "active": true,
        "agent": {},
        "birthDate": "2024-01-01T00:00:00Z",
        "company": {},
        "country": "string",
        "cpf": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "createdFromSurvey": true,
        "defaultLocale": "string",
        "displayName": "string",
        "email": "string",
        "externalCode": "string",
        "firstAccess": true,
        "firstLogin": "2024-01-01T00:00:00Z",
        "formal": true,
        "id": 0,
        "lastLogin": "2024-01-01T00:00:00Z",
        "name": "string",
        "operation": "string",
        "originUser": "string",
        "phone": "string",
        "priority": 0,
        "profile": {},
        "ticketUserId": 0,
        "tm2": true,
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "userName": "string",
        "usingMFA": true,
        "visible": true,
        "password": "string"
      },
      "userId": 0
    }
  ]
}
```

---

### `/api/v2/direct-message-user/unique`

**findOne** · `operationId: findOneUsingPOST_59`

Auth: Application & Application User

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
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "userId": 0
}
```

---
