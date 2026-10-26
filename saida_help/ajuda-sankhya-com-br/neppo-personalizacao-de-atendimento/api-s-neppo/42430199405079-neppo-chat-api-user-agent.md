---
id: "42430199405079"
titulo: "Neppo Chat API — User Agent"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199405079-Neppo-Chat-API-User-Agent"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:28Z"
rotulos: ["sync_hc", "neppo", "neppo_783908908", "sync_hash_198070c00ee4"]
---

# Neppo Chat API — User Agent

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199405079-Neppo-Chat-API-User-Agent#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199405079-Neppo-Chat-API-User-Agent#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199405079-Neppo-Chat-API-User-Agent#Referencia-tecnica-completa)
- [V1 — user-agent-controller (12 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199405079-Neppo-Chat-API-User-Agent#V1--user-agent-controller-12-endpoints)
- [V2 — user-agent-controller-v-2 (6 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199405079-Neppo-Chat-API-User-Agent#V2--user-agent-controller-v-2-6-endpoints)

**O que é este módulo?**

Gerencia as configurações específicas de cada atendente — preferências, limites de atendimento e capacidades individuais.

| Quem usa | Administradores, supervisores. |
| --- | --- |
| Problema que resolve | Configurações iguais para todos os atendentes não refletem a realidade operacional (trainee vs senior, parcial vs integral). |
| Impacto na experiência do cliente | Cada atendente opera dentro de suas capacidades reais, garantindo qualidade no atendimento. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar configurações** | Retorna as configurações de todos os agentes. |
| **Criar/atualizar configuração** | Define limites e preferências individuais do agente. |
| **Buscar configuração** | Consulta as configurações de um agente específico. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/user-agent/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `user-agent-controller` (12 endpoints)

### `/api/user-agent`

**findAll** · `operationId: findAllUsingPOST_100`

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
| 200 | OK | [PageResponse«UserAgent»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agent": {
        "agentAllHistory": true,
        "agentAllHistoryOperation": true,
        "agentAttendSimple": true,
        "agentToken": "string",
        "agentViewPhone": true,
        "attendanceServiceChannel": "string",
        "audioOn": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "department": "string",
        "extensionAttendance": "string",
        "id": 0,
        "loginAttendance": "string",
        "maxChatChannels": 0,
        "passwordAttendance": "string",
        "pauseOnReceiveCall": true,
        "socialToken": "string",
        "status": "string",
        "superAgent": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "user": {},
        "virtualAgent": true
      },
      "associationId": {
        "userId": 0,
        "agentId": 0
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
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
      }
    }
  ]
}
```

---

### `/api/user-agent/client-agents-association`

**saveClientAgentsAssociation** · `operationId: saveClientAgentsAssociationUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientAgentsDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "agentsIds": []
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---

### `/api/user-agent/delete`

**delete** · `operationId: deleteUsingDELETE_78`

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

### `/api/user-agent/deleteAssociation`

**deleteAssociation** · `operationId: deleteAssociationUsingDELETE`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AssociationId](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "agentId": 0
}
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

### `/api/user-agent/save`

**insert** · `operationId: insertUsingPOST_78`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

---

### `/api/user-agent/unique`

**findOne** · `operationId: findOneUsingPOST_93`

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
| 200 | OK | [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

---

### `/api/v1/user-agent`

**findAll** · `operationId: findAllUsingPOST_101`

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
| 200 | OK | [PageResponse«UserAgent»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agent": {
        "agentAllHistory": true,
        "agentAllHistoryOperation": true,
        "agentAttendSimple": true,
        "agentToken": "string",
        "agentViewPhone": true,
        "attendanceServiceChannel": "string",
        "audioOn": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "department": "string",
        "extensionAttendance": "string",
        "id": 0,
        "loginAttendance": "string",
        "maxChatChannels": 0,
        "passwordAttendance": "string",
        "pauseOnReceiveCall": true,
        "socialToken": "string",
        "status": "string",
        "superAgent": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "user": {},
        "virtualAgent": true
      },
      "associationId": {
        "userId": 0,
        "agentId": 0
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
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
      }
    }
  ]
}
```

---

### `/api/v1/user-agent/client-agents-association`

**saveClientAgentsAssociation** · `operationId: saveClientAgentsAssociationUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientAgentsDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "agentsIds": []
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---

### `/api/v1/user-agent/delete`

**delete** · `operationId: deleteUsingDELETE_79`

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

### `/api/v1/user-agent/deleteAssociation`

**deleteAssociation** · `operationId: deleteAssociationUsingDELETE_1`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AssociationId](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "agentId": 0
}
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

### `/api/v1/user-agent/save`

**insert** · `operationId: insertUsingPOST_79`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

---

### `/api/v1/user-agent/unique`

**findOne** · `operationId: findOneUsingPOST_94`

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
| 200 | OK | [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

---

## V2 — `user-agent-controller-v-2` (6 endpoints)

### `/api/v2/user-agent`

**findAll** · `operationId: findAllUsingPOST_102`

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
| 200 | OK | [PageResponse«UserAgent»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agent": {
        "agentAllHistory": true,
        "agentAllHistoryOperation": true,
        "agentAttendSimple": true,
        "agentToken": "string",
        "agentViewPhone": true,
        "attendanceServiceChannel": "string",
        "audioOn": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "department": "string",
        "extensionAttendance": "string",
        "id": 0,
        "loginAttendance": "string",
        "maxChatChannels": 0,
        "passwordAttendance": "string",
        "pauseOnReceiveCall": true,
        "socialToken": "string",
        "status": "string",
        "superAgent": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "user": {},
        "virtualAgent": true
      },
      "associationId": {
        "userId": 0,
        "agentId": 0
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
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
      }
    }
  ]
}
```

---

### `/api/v2/user-agent/client-agents-association`

**saveClientAgentsAssociation** · `operationId: saveClientAgentsAssociationUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientAgentsDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "agentsIds": []
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---

### `/api/v2/user-agent/delete`

**delete** · `operationId: deleteUsingDELETE_80`

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

### `/api/v2/user-agent/deleteAssociation`

**deleteAssociation** · `operationId: deleteAssociationUsingDELETE_2`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AssociationId](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "agentId": 0
}
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

### `/api/v2/user-agent/save`

**insert** · `operationId: insertUsingPOST_80`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

---

### `/api/v2/user-agent/unique`

**findOne** · `operationId: findOneUsingPOST_95`

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
| 200 | OK | [UserAgent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agent": {
    "agentAllHistory": true,
    "agentAllHistoryOperation": true,
    "agentAttendSimple": true,
    "agentToken": "string",
    "agentViewPhone": true,
    "attendanceServiceChannel": "string",
    "audioOn": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "department": "string",
    "extensionAttendance": "string",
    "id": 0,
    "loginAttendance": "string",
    "maxChatChannels": 0,
    "passwordAttendance": "string",
    "pauseOnReceiveCall": true,
    "socialToken": "string",
    "status": "string",
    "superAgent": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "user": {},
    "virtualAgent": true
  },
  "associationId": {
    "userId": 0,
    "agentId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
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
  }
}
```

---
