---
id: "42430232688023"
titulo: "Neppo Chat API — User"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232688023-Neppo-Chat-API-User"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:23Z"
rotulos: ["sync_hc", "neppo", "neppo_784334877", "sync_hash_85f5d8f5d5d6"]
---

# Neppo Chat API — User

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232688023-Neppo-Chat-API-User#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232688023-Neppo-Chat-API-User#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232688023-Neppo-Chat-API-User#Referencia-tecnica-completa)
- [V1 — user-controller (28 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232688023-Neppo-Chat-API-User#V1--user-controller-28-endpoints)
- [V2 — user-controller-v-2 (14 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232688023-Neppo-Chat-API-User#V2--user-controller-v-2-14-endpoints)

**O que é este módulo?**

Gerencia os usuários/contatos — as pessoas que entram em contato com a empresa através dos canais atendidos pela Neppo.

| Quem usa | CRM, atendentes, bots, integrações externas. |
| --- | --- |
| Problema que resolve | Sem gerenciamento de usuários, não é possível manter histórico de contatos, segmentar clientes ou personalizar o atendimento. |
| Impacto na experiência do cliente | A empresa conhece o cliente pelo nome, histórico e preferências, oferecendo uma experiência personalizada desde o primeiro contato. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar usuários** | Retorna todos os contatos com filtros avançados. |
| **Criar usuário** | Cadastra um novo contato com nome, telefone e atributos. |
| **Atualizar usuário** | Modifica dados de um contato existente. |
| **Buscar usuário** | Consulta os dados completos de um contato pelo ID ou telefone. |
| **Remover usuário** | Remove ou desativa um contato. |
| **Bloquear usuário** | Impede que um contato inicie novos atendimentos. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/users/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "ticketUserId": 0,
  "tm2": true,
  "typeUser": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userName": "string",
  "usingMFA": true,
  "visible": true,
  "password": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `user-controller` (28 endpoints)

### `/api/users`

**findAll** · `operationId: findAllUsingPOST_109`

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
| 200 | OK | [PageResponse«User»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "accessKey": "string",
      "active": true,
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
      "birthDate": "2024-01-01T00:00:00Z",
      "company": {
        "active": true,
        "address": "string",
        "cep": "string",
        "city": "string",
        "cnpj": "string",
        "companyName": "string",
        "complement": "string",
        "contractSignature": 0,
        "country": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "dateEndPilot": "2024-01-01T00:00:00Z",
        "defaultLocale": "string",
        "email": "string",
        "groupCompany": {},
        "id": 0,
        "nameContact": "string",
        "neighborhood": "string",
        "number": "string",
        "phoneContact": "string",
        "sgemnet": "string",
        "site": "string",
        "sku": "string",
        "state": "string",
        "stateRegistration": "string",
        "timeHistory": 0,
        "tradeName": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
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
      "profile": {
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "name": "string",
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "visible": true
      },
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
  ]
}
```

---

### `/api/users/channels`

**listChannels** · `operationId: listChannelsUsingPOST`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<string> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
[]
```

---

### `/api/users/delete`

**delete** · `operationId: deleteUsingDELETE_87`

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

### `/api/users/rules`

**rules** · `operationId: listRulesUsingPOST`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserRuleRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": "string",
  "query": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<string> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
[]
```

---

### `/api/users/save`

**insert** · `operationId: insertUsingPOST_87`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

---

### `/api/users/save/administrator`

**insertAdministrator** · `operationId: insertAdministratorUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AdministratorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "birthDate": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "id": 0,
  "password": "string",
  "phone": "string",
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "userName": "string",
  "usingMFA": true,
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  }
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

### `/api/users/save/agent`

**insertAgent** · `operationId: insertAgentUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AgentDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
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

### `/api/users/save/agent-supervisor`

**insertAgentSupervisor** · `operationId: insertAgentSupervisorUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AgentSupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "operationsId": [],
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
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

### `/api/users/save/bot`

**insertBot** · `operationId: insertBotUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BotDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "id": 0,
  "userName": "string",
  "displayName": "string",
  "botTree": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "name": "string",
    "description": "string",
    "active": true,
    "version": 0
  },
  "botSurvey": true,
  "active": true
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

### `/api/users/save/client`

**insertClient** · `operationId: insertClientUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "id": 0,
  "userName": "string",
  "phone": "string",
  "displayName": "string",
  "email": "string",
  "birthDate": "string",
  "active": true,
  "cpf": "string",
  "formal": true,
  "priority": 0,
  "externalCode": "string",
  "attributes": [
    {
      "description": "string",
      "value": "string"
    }
  ]
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

### `/api/users/save/supervisor`

**insertSupervisor** · `operationId: insertSupervisorUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [SupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "birthDate": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "id": 0,
  "password": "string",
  "phone": "string",
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "userName": "string",
  "usingMFA": true,
  "operationsId": []
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

### `/api/users/unique`

**findOne** · `operationId: findOneUsingPOST_102`

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
| 200 | OK | [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

---

### `/api/users/{id}/agent`

**findAgent** · `operationId: findAgentUsingGET`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [AgentDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
}
```

---

### `/api/users/{id}/agent-supervisor`

**findAgentSupervisor** · `operationId: findAgentSupervisorUsingGET`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [AgentSupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "operationsId": [],
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
}
```

---

### `/api/v1/users`

**findAll** · `operationId: findAllUsingPOST_110`

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
| 200 | OK | [PageResponse«User»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "accessKey": "string",
      "active": true,
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
      "birthDate": "2024-01-01T00:00:00Z",
      "company": {
        "active": true,
        "address": "string",
        "cep": "string",
        "city": "string",
        "cnpj": "string",
        "companyName": "string",
        "complement": "string",
        "contractSignature": 0,
        "country": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "dateEndPilot": "2024-01-01T00:00:00Z",
        "defaultLocale": "string",
        "email": "string",
        "groupCompany": {},
        "id": 0,
        "nameContact": "string",
        "neighborhood": "string",
        "number": "string",
        "phoneContact": "string",
        "sgemnet": "string",
        "site": "string",
        "sku": "string",
        "state": "string",
        "stateRegistration": "string",
        "timeHistory": 0,
        "tradeName": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
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
      "profile": {
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "name": "string",
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "visible": true
      },
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
  ]
}
```

---

### `/api/v1/users/channels`

**listChannels** · `operationId: listChannelsUsingPOST_1`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<string> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
[]
```

---

### `/api/v1/users/delete`

**delete** · `operationId: deleteUsingDELETE_88`

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

### `/api/v1/users/rules`

**rules** · `operationId: listRulesUsingPOST_1`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserRuleRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": "string",
  "query": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<string> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
[]
```

---

### `/api/v1/users/save`

**insert** · `operationId: insertUsingPOST_88`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

---

### `/api/v1/users/save/administrator`

**insertAdministrator** · `operationId: insertAdministratorUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AdministratorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "birthDate": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "id": 0,
  "password": "string",
  "phone": "string",
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "userName": "string",
  "usingMFA": true,
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  }
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

### `/api/v1/users/save/agent`

**insertAgent** · `operationId: insertAgentUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AgentDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
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

### `/api/v1/users/save/agent-supervisor`

**insertAgentSupervisor** · `operationId: insertAgentSupervisorUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AgentSupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "operationsId": [],
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
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

### `/api/v1/users/save/bot`

**insertBot** · `operationId: insertBotUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BotDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "id": 0,
  "userName": "string",
  "displayName": "string",
  "botTree": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "name": "string",
    "description": "string",
    "active": true,
    "version": 0
  },
  "botSurvey": true,
  "active": true
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

### `/api/v1/users/save/client`

**insertClient** · `operationId: insertClientUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "id": 0,
  "userName": "string",
  "phone": "string",
  "displayName": "string",
  "email": "string",
  "birthDate": "string",
  "active": true,
  "cpf": "string",
  "formal": true,
  "priority": 0,
  "externalCode": "string",
  "attributes": [
    {
      "description": "string",
      "value": "string"
    }
  ]
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

### `/api/v1/users/save/supervisor`

**insertSupervisor** · `operationId: insertSupervisorUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [SupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "birthDate": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "id": 0,
  "password": "string",
  "phone": "string",
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "userName": "string",
  "usingMFA": true,
  "operationsId": []
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

### `/api/v1/users/unique`

**findOne** · `operationId: findOneUsingPOST_103`

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
| 200 | OK | [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

---

### `/api/v1/users/{id}/agent`

**findAgent** · `operationId: findAgentUsingGET_1`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [AgentDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
}
```

---

### `/api/v1/users/{id}/agent-supervisor`

**findAgentSupervisor** · `operationId: findAgentSupervisorUsingGET_1`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [AgentSupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "operationsId": [],
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
}
```

---

## V2 — `user-controller-v-2` (14 endpoints)

### `/api/v2/users`

**findAll** · `operationId: findAllUsingPOST_111`

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
| 200 | OK | [PageResponse«User»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "accessKey": "string",
      "active": true,
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
      "birthDate": "2024-01-01T00:00:00Z",
      "company": {
        "active": true,
        "address": "string",
        "cep": "string",
        "city": "string",
        "cnpj": "string",
        "companyName": "string",
        "complement": "string",
        "contractSignature": 0,
        "country": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "dateEndPilot": "2024-01-01T00:00:00Z",
        "defaultLocale": "string",
        "email": "string",
        "groupCompany": {},
        "id": 0,
        "nameContact": "string",
        "neighborhood": "string",
        "number": "string",
        "phoneContact": "string",
        "sgemnet": "string",
        "site": "string",
        "sku": "string",
        "state": "string",
        "stateRegistration": "string",
        "timeHistory": 0,
        "tradeName": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
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
      "profile": {
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "name": "string",
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "visible": true
      },
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
  ]
}
```

---

### `/api/v2/users/channels`

**listChannels** · `operationId: listChannelsUsingPOST_2`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<string> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
[]
```

---

### `/api/v2/users/delete`

**delete** · `operationId: deleteUsingDELETE_89`

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

### `/api/v2/users/rules`

**rules** · `operationId: listRulesUsingPOST_2`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserRuleRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": "string",
  "query": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<string> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
[]
```

---

### `/api/v2/users/save`

**insert** · `operationId: insertUsingPOST_89`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

---

### `/api/v2/users/save/administrator`

**insertAdministrator** · `operationId: insertAdministratorUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AdministratorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "birthDate": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "id": 0,
  "password": "string",
  "phone": "string",
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "userName": "string",
  "usingMFA": true,
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  }
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

### `/api/v2/users/save/agent`

**insertAgent** · `operationId: insertAgentUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AgentDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
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

### `/api/v2/users/save/agent-supervisor`

**insertAgentSupervisor** · `operationId: insertAgentSupervisorUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [AgentSupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "operationsId": [],
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
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

### `/api/v2/users/save/bot`

**insertBot** · `operationId: insertBotUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BotDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "id": 0,
  "userName": "string",
  "displayName": "string",
  "botTree": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "name": "string",
    "description": "string",
    "active": true,
    "version": 0
  },
  "botSurvey": true,
  "active": true
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

### `/api/v2/users/save/client`

**insertClient** · `operationId: insertClientUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "id": 0,
  "userName": "string",
  "phone": "string",
  "displayName": "string",
  "email": "string",
  "birthDate": "string",
  "active": true,
  "cpf": "string",
  "formal": true,
  "priority": 0,
  "externalCode": "string",
  "attributes": [
    {
      "description": "string",
      "value": "string"
    }
  ]
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

### `/api/v2/users/save/supervisor`

**insertSupervisor** · `operationId: insertSupervisorUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [SupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "birthDate": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "id": 0,
  "password": "string",
  "phone": "string",
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "userName": "string",
  "usingMFA": true,
  "operationsId": []
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

### `/api/v2/users/unique`

**findOne** · `operationId: findOneUsingPOST_104`

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
| 200 | OK | [User](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accessKey": "string",
  "active": true,
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
  "birthDate": "2024-01-01T00:00:00Z",
  "company": {
    "active": true,
    "address": "string",
    "cep": "string",
    "city": "string",
    "cnpj": "string",
    "companyName": "string",
    "complement": "string",
    "contractSignature": 0,
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateEndPilot": "2024-01-01T00:00:00Z",
    "defaultLocale": "string",
    "email": "string",
    "groupCompany": {},
    "id": 0,
    "nameContact": "string",
    "neighborhood": "string",
    "number": "string",
    "phoneContact": "string",
    "sgemnet": "string",
    "site": "string",
    "sku": "string",
    "state": "string",
    "stateRegistration": "string",
    "timeHistory": 0,
    "tradeName": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
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
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
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
```

---

### `/api/v2/users/{id}/agent`

**findAgent** · `operationId: findAgentUsingGET_2`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [AgentDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
}
```

---

### `/api/v2/users/{id}/agent-supervisor`

**findAgentSupervisor** · `operationId: findAgentSupervisorUsingGET_2`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [AgentSupervisorDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "agentAllHistory": true,
  "agentAllHistoryOperation": true,
  "agentAttendSimple": true,
  "agentToken": "string",
  "agentViewPhone": true,
  "birthDate": "string",
  "chatAgent": true,
  "department": "string",
  "displayName": "string",
  "email": "string",
  "firstAccess": true,
  "groupsId": [],
  "id": 0,
  "maxChatChannels": 0,
  "operationsId": [],
  "password": "string",
  "pauseOnReceiveCall": true,
  "phone": "string",
  "priority": 0,
  "profile": {
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "name": "string",
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "visible": true
  },
  "socialToken": "string",
  "superAgent": true,
  "userName": "string",
  "usingMFA": true,
  "virtualAgent": true,
  "voice": {
    "agentBusyDelayTime": 0,
    "agentCallTimeout": 0,
    "agentContact": "string",
    "agentId": "string",
    "agentMaxNoAnswer": 0,
    "agentName": "string",
    "agentNoAnswerDelayTime": 0,
    "agentRejectDelayTime": 0,
    "agentType": "string",
    "agentWrapUpTime": 0,
    "extension": {}
  }
}
```

---
