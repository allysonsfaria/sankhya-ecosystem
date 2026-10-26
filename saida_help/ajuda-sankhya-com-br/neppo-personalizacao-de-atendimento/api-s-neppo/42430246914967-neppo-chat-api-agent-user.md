---
id: "42430246914967"
titulo: "Neppo Chat API — Agent User"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246914967-Neppo-Chat-API-Agent-User"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:24Z"
rotulos: ["sync_hc", "neppo", "neppo_784236546", "sync_hash_78ac98a44461"]
---

# Neppo Chat API — Agent User

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246914967-Neppo-Chat-API-Agent-User#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246914967-Neppo-Chat-API-Agent-User#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246914967-Neppo-Chat-API-Agent-User#Referencia-tecnica-completa)
- [V1 — agent-user-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246914967-Neppo-Chat-API-Agent-User#V1--agent-user-controller-8-endpoints)
- [V2 — agent-user-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246914967-Neppo-Chat-API-Agent-User#V2--agent-user-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia a relação entre atendentes e os usuários/contatos que eles atendem.

| Quem usa | Sistema de distribuição de atendimentos, supervisores de operação. |
| --- | --- |
| Problema que resolve | Sem este vínculo, não é possível saber qual agente atende qual cliente, impedindo roteamento inteligente e continuidade no atendimento. |
| Impacto na experiência do cliente | O cliente é sempre direcionado ao atendente que já conhece seu histórico, criando uma experiência personalizada e eficiente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar vínculos** | Retorna todos os pares agente-usuário ativos. |
| **Criar vínculo** | Associa um atendente a um usuário/contato específico. |
| **Remover vínculo** | Desvincula o atendente do usuário. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/agent-user/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
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
  "virtualAgent": true
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `agent-user-controller` (8 endpoints)

### `/api/agent-user`

**findAll** · `operationId: findAllUsingPOST_6`

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
| 200 | OK | [PageResponse«Agent»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "virtualAgent": true
    }
  ]
}
```

---

### `/api/agent-user/delete`

**delete** · `operationId: deleteUsingDELETE_3`

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

### `/api/agent-user/save`

**insert** · `operationId: insertUsingPOST_3`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
  "virtualAgent": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

---

### `/api/agent-user/unique`

**findOne** · `operationId: findOneUsingPOST_6`

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
| 200 | OK | [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

---

### `/api/v1/agent-user`

**findAll** · `operationId: findAllUsingPOST_7`

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
| 200 | OK | [PageResponse«Agent»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "virtualAgent": true
    }
  ]
}
```

---

### `/api/v1/agent-user/delete`

**delete** · `operationId: deleteUsingDELETE_4`

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

### `/api/v1/agent-user/save`

**insert** · `operationId: insertUsingPOST_4`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
  "virtualAgent": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

---

### `/api/v1/agent-user/unique`

**findOne** · `operationId: findOneUsingPOST_7`

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
| 200 | OK | [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

---

## V2 — `agent-user-controller-v-2` (4 endpoints)

### `/api/v2/agent-user`

**findAll** · `operationId: findAllUsingPOST_8`

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
| 200 | OK | [PageResponse«Agent»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "virtualAgent": true
    }
  ]
}
```

---

### `/api/v2/agent-user/delete`

**delete** · `operationId: deleteUsingDELETE_5`

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

### `/api/v2/agent-user/save`

**insert** · `operationId: insertUsingPOST_5`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
  "virtualAgent": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

---

### `/api/v2/agent-user/unique`

**findOne** · `operationId: findOneUsingPOST_8`

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
| 200 | OK | [Agent](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
  "virtualAgent": true
}
```

---
