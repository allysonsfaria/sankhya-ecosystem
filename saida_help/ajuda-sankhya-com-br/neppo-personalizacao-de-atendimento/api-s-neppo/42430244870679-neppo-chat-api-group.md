---
id: "42430244870679"
titulo: "Neppo Chat API — Group"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244870679-Neppo-Chat-API-Group"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:33Z"
rotulos: ["sync_hc", "neppo", "neppo_783450116", "sync_hash_d1f27436936d"]
---

# Neppo Chat API — Group

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244870679-Neppo-Chat-API-Group#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244870679-Neppo-Chat-API-Group#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244870679-Neppo-Chat-API-Group#Referencia-tecnica-completa)
- [V1 — group-controller (10 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244870679-Neppo-Chat-API-Group#V1--group-controller-10-endpoints)
- [V2 — group-controller-v-2 (5 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430244870679-Neppo-Chat-API-Group#V2--group-controller-v-2-5-endpoints)

**O que é este módulo?**

Gerencia grupos de atendimento — conjuntos de atendentes organizados por especialidade, produto ou regional.

| Quem usa | Gestores de operação, administradores. |
| --- | --- |
| Problema que resolve | Sem grupos, todos os atendentes recebem todos os tipos de atendimento, mesmo sem especialidade, resultando em baixa qualidade. |
| Impacto na experiência do cliente | O cliente é direcionado automaticamente para o grupo especializado no seu tipo de problema, resolvendo mais rápido na primeira interação. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar grupos** | Retorna todos os grupos de atendimento configurados. |
| **Criar grupo** | Cria um novo grupo com nome e atendentes associados. |
| **Atualizar grupo** | Modifica os membros ou configurações de um grupo. |
| **Remover grupo** | Exclui um grupo de atendimento. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/groups/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `group-controller` (10 endpoints)

### `/api/groups`

**findAll** · `operationId: findAllUsingPOST_67`

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
| 200 | OK | [PageResponse«GroupConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "acceptedMedias": "string",
      "active": true,
      "agentExpireSession": true,
      "agentReplyMaxDelay": 0,
      "broker": "string",
      "businessUnit": "string",
      "channels": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "configInactivity": true,
      "configInactivityTime": 0,
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "defaultAgent": {
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
      "emailActiveShipping": true,
      "finalAgent": {
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
      "gatewayQueue": "string",
      "id": 0,
      "inactivityAction": "string",
      "inactivityAgent": {
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
      "inactivityGroup": 0,
      "inngageShipping": true,
      "interactQueueDelay": 0,
      "limitTimeWaitingForInteract": 0,
      "mandatoryClassificationTree": true,
      "mandatoryFinalAgent": true,
      "name": "string",
      "offlineAttendance": true,
      "onlyBot": true,
      "onlyReceptive": true,
      "operation": {
        "company": {},
        "country": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "customerPortfolio": true,
        "defaultLocale": "string",
        "id": 0,
        "operationName": "string",
        "operationStatus": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "verifyHoliday": "string"
      },
      "pausedTransfer": true,
      "pending": true,
      "queueControl": "string",
      "queueScheduleStrategy": true,
      "redirectAttendanceAgentDisconnect": true,
      "scheduleActiveSendTime": 0,
      "scheduleName": "string",
      "skipQueue": true,
      "sla": 0,
      "smsActiveShipping": true,
      "survey": 0,
      "telegramActiveShipping": true,
      "timeMaxAttendance": 0,
      "timePending": 0,
      "timeUnit": "NANOSECONDS",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "uraActiveShipping": true,
      "visible": true,
      "voiceActiveShipping": true,
      "warningRatio": 0,
      "wavy": true,
      "whatsappActiveShipping": true,
      "whatsappPartner": true,
      "whatsappPartnerInactivity": 0
    }
  ]
}
```

---

### `/api/groups/delete`

**delete** · `operationId: deleteUsingDELETE_48`

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

### `/api/groups/save`

**insert** · `operationId: insertUsingPOST_51`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

---

### `/api/groups/save-group`

**saveGroup** · `operationId: saveGroupUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [GroupDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "group": {
    "acceptedMedias": "string",
    "active": true,
    "agentExpireSession": true,
    "agentReplyMaxDelay": 0,
    "broker": "string",
    "businessUnit": "string",
    "channels": [],
    "classificationTree": {},
    "configInactivity": true,
    "configInactivityTime": 0,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "defaultAgent": {},
    "emailActiveShipping": true,
    "finalAgent": {},
    "gatewayQueue": "string",
    "id": 0,
    "inactivityAction": "string",
    "inactivityAgent": {},
    "inactivityGroup": 0,
    "inngageShipping": true,
    "interactQueueDelay": 0,
    "limitTimeWaitingForInteract": 0,
    "mandatoryClassificationTree": true,
    "mandatoryFinalAgent": true,
    "name": "string",
    "offlineAttendance": true,
    "onlyBot": true,
    "onlyReceptive": true,
    "operation": {},
    "pausedTransfer": true,
    "pending": true,
    "queueControl": "string",
    "queueScheduleStrategy": true,
    "redirectAttendanceAgentDisconnect": true,
    "scheduleActiveSendTime": 0,
    "scheduleName": "string",
    "skipQueue": true,
    "sla": 0,
    "smsActiveShipping": true,
    "survey": 0,
    "telegramActiveShipping": true,
    "timeMaxAttendance": 0,
    "timePending": 0,
    "timeUnit": "NANOSECONDS",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "uraActiveShipping": true,
    "visible": true,
    "voiceActiveShipping": true,
    "warningRatio": 0,
    "wavy": true,
    "whatsappActiveShipping": true,
    "whatsappPartner": true,
    "whatsappPartnerInactivity": 0
  },
  "agentsId": [],
  "groupsId": [],
  "callCenterQueue": {
    "queueName": "string",
    "queueExtension": "string",
    "queueGreeting": "string",
    "queueStrategy": "string",
    "queueMOHSound": "string",
    "queueRecordEnable": true,
    "queueTimeBaseScore": "string",
    "queueTimeBaseScoreSec": 0,
    "queueMaxWaitTime": 0,
    "queueMaxWaitTimeWithNoAgent": 0,
    "queueMaxWaitTimeWithNoAgentTimeReached": 0,
    "queueTierRulesApply": "string",
    "queueTierRuleWaitSecond": 0,
    "queueTierRuleNoAgentNoWait": "string",
    "queueTimeoutAction": "string",
    "queueDiscardAbandonedAfter": 0,
    "queueAbandonedResumeAllowed": "string",
    "queueTierRuleWaitMultiplyLevel": "string",
    "queueCidPrefix": "string",
    "queueAnnounceSound": "string",
    "queueAnnounceFrequency": 0,
    "queueCCExitKeys": "string",
    "queueEmailAddress": "string",
    "queueDescription": "string",
    "queueAnnouncePositionEnabled": true,
    "queueAnnouncePositionFrequency": 0
  },
  "callCenterTiers": [
    {
      "extension": "string",
      "tierLevel": 0,
      "tierPosition": 0
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

### `/api/groups/unique`

**findOne** · `operationId: findOneUsingPOST_63`

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
| 200 | OK | [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

---

### `/api/v1/groups`

**findAll** · `operationId: findAllUsingPOST_68`

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
| 200 | OK | [PageResponse«GroupConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "acceptedMedias": "string",
      "active": true,
      "agentExpireSession": true,
      "agentReplyMaxDelay": 0,
      "broker": "string",
      "businessUnit": "string",
      "channels": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "configInactivity": true,
      "configInactivityTime": 0,
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "defaultAgent": {
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
      "emailActiveShipping": true,
      "finalAgent": {
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
      "gatewayQueue": "string",
      "id": 0,
      "inactivityAction": "string",
      "inactivityAgent": {
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
      "inactivityGroup": 0,
      "inngageShipping": true,
      "interactQueueDelay": 0,
      "limitTimeWaitingForInteract": 0,
      "mandatoryClassificationTree": true,
      "mandatoryFinalAgent": true,
      "name": "string",
      "offlineAttendance": true,
      "onlyBot": true,
      "onlyReceptive": true,
      "operation": {
        "company": {},
        "country": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "customerPortfolio": true,
        "defaultLocale": "string",
        "id": 0,
        "operationName": "string",
        "operationStatus": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "verifyHoliday": "string"
      },
      "pausedTransfer": true,
      "pending": true,
      "queueControl": "string",
      "queueScheduleStrategy": true,
      "redirectAttendanceAgentDisconnect": true,
      "scheduleActiveSendTime": 0,
      "scheduleName": "string",
      "skipQueue": true,
      "sla": 0,
      "smsActiveShipping": true,
      "survey": 0,
      "telegramActiveShipping": true,
      "timeMaxAttendance": 0,
      "timePending": 0,
      "timeUnit": "NANOSECONDS",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "uraActiveShipping": true,
      "visible": true,
      "voiceActiveShipping": true,
      "warningRatio": 0,
      "wavy": true,
      "whatsappActiveShipping": true,
      "whatsappPartner": true,
      "whatsappPartnerInactivity": 0
    }
  ]
}
```

---

### `/api/v1/groups/delete`

**delete** · `operationId: deleteUsingDELETE_49`

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

### `/api/v1/groups/save`

**insert** · `operationId: insertUsingPOST_52`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

---

### `/api/v1/groups/save-group`

**saveGroup** · `operationId: saveGroupUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [GroupDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "group": {
    "acceptedMedias": "string",
    "active": true,
    "agentExpireSession": true,
    "agentReplyMaxDelay": 0,
    "broker": "string",
    "businessUnit": "string",
    "channels": [],
    "classificationTree": {},
    "configInactivity": true,
    "configInactivityTime": 0,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "defaultAgent": {},
    "emailActiveShipping": true,
    "finalAgent": {},
    "gatewayQueue": "string",
    "id": 0,
    "inactivityAction": "string",
    "inactivityAgent": {},
    "inactivityGroup": 0,
    "inngageShipping": true,
    "interactQueueDelay": 0,
    "limitTimeWaitingForInteract": 0,
    "mandatoryClassificationTree": true,
    "mandatoryFinalAgent": true,
    "name": "string",
    "offlineAttendance": true,
    "onlyBot": true,
    "onlyReceptive": true,
    "operation": {},
    "pausedTransfer": true,
    "pending": true,
    "queueControl": "string",
    "queueScheduleStrategy": true,
    "redirectAttendanceAgentDisconnect": true,
    "scheduleActiveSendTime": 0,
    "scheduleName": "string",
    "skipQueue": true,
    "sla": 0,
    "smsActiveShipping": true,
    "survey": 0,
    "telegramActiveShipping": true,
    "timeMaxAttendance": 0,
    "timePending": 0,
    "timeUnit": "NANOSECONDS",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "uraActiveShipping": true,
    "visible": true,
    "voiceActiveShipping": true,
    "warningRatio": 0,
    "wavy": true,
    "whatsappActiveShipping": true,
    "whatsappPartner": true,
    "whatsappPartnerInactivity": 0
  },
  "agentsId": [],
  "groupsId": [],
  "callCenterQueue": {
    "queueName": "string",
    "queueExtension": "string",
    "queueGreeting": "string",
    "queueStrategy": "string",
    "queueMOHSound": "string",
    "queueRecordEnable": true,
    "queueTimeBaseScore": "string",
    "queueTimeBaseScoreSec": 0,
    "queueMaxWaitTime": 0,
    "queueMaxWaitTimeWithNoAgent": 0,
    "queueMaxWaitTimeWithNoAgentTimeReached": 0,
    "queueTierRulesApply": "string",
    "queueTierRuleWaitSecond": 0,
    "queueTierRuleNoAgentNoWait": "string",
    "queueTimeoutAction": "string",
    "queueDiscardAbandonedAfter": 0,
    "queueAbandonedResumeAllowed": "string",
    "queueTierRuleWaitMultiplyLevel": "string",
    "queueCidPrefix": "string",
    "queueAnnounceSound": "string",
    "queueAnnounceFrequency": 0,
    "queueCCExitKeys": "string",
    "queueEmailAddress": "string",
    "queueDescription": "string",
    "queueAnnouncePositionEnabled": true,
    "queueAnnouncePositionFrequency": 0
  },
  "callCenterTiers": [
    {
      "extension": "string",
      "tierLevel": 0,
      "tierPosition": 0
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

### `/api/v1/groups/unique`

**findOne** · `operationId: findOneUsingPOST_64`

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
| 200 | OK | [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

---

## V2 — `group-controller-v-2` (5 endpoints)

### `/api/v2/groups`

**findAll** · `operationId: findAllUsingPOST_69`

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
| 200 | OK | [PageResponse«GroupConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "acceptedMedias": "string",
      "active": true,
      "agentExpireSession": true,
      "agentReplyMaxDelay": 0,
      "broker": "string",
      "businessUnit": "string",
      "channels": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "configInactivity": true,
      "configInactivityTime": 0,
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "defaultAgent": {
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
      "emailActiveShipping": true,
      "finalAgent": {
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
      "gatewayQueue": "string",
      "id": 0,
      "inactivityAction": "string",
      "inactivityAgent": {
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
      "inactivityGroup": 0,
      "inngageShipping": true,
      "interactQueueDelay": 0,
      "limitTimeWaitingForInteract": 0,
      "mandatoryClassificationTree": true,
      "mandatoryFinalAgent": true,
      "name": "string",
      "offlineAttendance": true,
      "onlyBot": true,
      "onlyReceptive": true,
      "operation": {
        "company": {},
        "country": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "customerPortfolio": true,
        "defaultLocale": "string",
        "id": 0,
        "operationName": "string",
        "operationStatus": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "verifyHoliday": "string"
      },
      "pausedTransfer": true,
      "pending": true,
      "queueControl": "string",
      "queueScheduleStrategy": true,
      "redirectAttendanceAgentDisconnect": true,
      "scheduleActiveSendTime": 0,
      "scheduleName": "string",
      "skipQueue": true,
      "sla": 0,
      "smsActiveShipping": true,
      "survey": 0,
      "telegramActiveShipping": true,
      "timeMaxAttendance": 0,
      "timePending": 0,
      "timeUnit": "NANOSECONDS",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "uraActiveShipping": true,
      "visible": true,
      "voiceActiveShipping": true,
      "warningRatio": 0,
      "wavy": true,
      "whatsappActiveShipping": true,
      "whatsappPartner": true,
      "whatsappPartnerInactivity": 0
    }
  ]
}
```

---

### `/api/v2/groups/delete`

**delete** · `operationId: deleteUsingDELETE_50`

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

### `/api/v2/groups/save`

**insert** · `operationId: insertUsingPOST_53`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

---

### `/api/v2/groups/save-group`

**saveGroup** · `operationId: saveGroupUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [GroupDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "group": {
    "acceptedMedias": "string",
    "active": true,
    "agentExpireSession": true,
    "agentReplyMaxDelay": 0,
    "broker": "string",
    "businessUnit": "string",
    "channels": [],
    "classificationTree": {},
    "configInactivity": true,
    "configInactivityTime": 0,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "defaultAgent": {},
    "emailActiveShipping": true,
    "finalAgent": {},
    "gatewayQueue": "string",
    "id": 0,
    "inactivityAction": "string",
    "inactivityAgent": {},
    "inactivityGroup": 0,
    "inngageShipping": true,
    "interactQueueDelay": 0,
    "limitTimeWaitingForInteract": 0,
    "mandatoryClassificationTree": true,
    "mandatoryFinalAgent": true,
    "name": "string",
    "offlineAttendance": true,
    "onlyBot": true,
    "onlyReceptive": true,
    "operation": {},
    "pausedTransfer": true,
    "pending": true,
    "queueControl": "string",
    "queueScheduleStrategy": true,
    "redirectAttendanceAgentDisconnect": true,
    "scheduleActiveSendTime": 0,
    "scheduleName": "string",
    "skipQueue": true,
    "sla": 0,
    "smsActiveShipping": true,
    "survey": 0,
    "telegramActiveShipping": true,
    "timeMaxAttendance": 0,
    "timePending": 0,
    "timeUnit": "NANOSECONDS",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "uraActiveShipping": true,
    "visible": true,
    "voiceActiveShipping": true,
    "warningRatio": 0,
    "wavy": true,
    "whatsappActiveShipping": true,
    "whatsappPartner": true,
    "whatsappPartnerInactivity": 0
  },
  "agentsId": [],
  "groupsId": [],
  "callCenterQueue": {
    "queueName": "string",
    "queueExtension": "string",
    "queueGreeting": "string",
    "queueStrategy": "string",
    "queueMOHSound": "string",
    "queueRecordEnable": true,
    "queueTimeBaseScore": "string",
    "queueTimeBaseScoreSec": 0,
    "queueMaxWaitTime": 0,
    "queueMaxWaitTimeWithNoAgent": 0,
    "queueMaxWaitTimeWithNoAgentTimeReached": 0,
    "queueTierRulesApply": "string",
    "queueTierRuleWaitSecond": 0,
    "queueTierRuleNoAgentNoWait": "string",
    "queueTimeoutAction": "string",
    "queueDiscardAbandonedAfter": 0,
    "queueAbandonedResumeAllowed": "string",
    "queueTierRuleWaitMultiplyLevel": "string",
    "queueCidPrefix": "string",
    "queueAnnounceSound": "string",
    "queueAnnounceFrequency": 0,
    "queueCCExitKeys": "string",
    "queueEmailAddress": "string",
    "queueDescription": "string",
    "queueAnnouncePositionEnabled": true,
    "queueAnnouncePositionFrequency": 0
  },
  "callCenterTiers": [
    {
      "extension": "string",
      "tierLevel": 0,
      "tierPosition": 0
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

### `/api/v2/groups/unique`

**findOne** · `operationId: findOneUsingPOST_65`

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
| 200 | OK | [GroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "acceptedMedias": "string",
  "active": true,
  "agentExpireSession": true,
  "agentReplyMaxDelay": 0,
  "broker": "string",
  "businessUnit": "string",
  "channels": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "configInactivity": true,
  "configInactivityTime": 0,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "defaultAgent": {
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
  "emailActiveShipping": true,
  "finalAgent": {
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
  "gatewayQueue": "string",
  "id": 0,
  "inactivityAction": "string",
  "inactivityAgent": {
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
  "inactivityGroup": 0,
  "inngageShipping": true,
  "interactQueueDelay": 0,
  "limitTimeWaitingForInteract": 0,
  "mandatoryClassificationTree": true,
  "mandatoryFinalAgent": true,
  "name": "string",
  "offlineAttendance": true,
  "onlyBot": true,
  "onlyReceptive": true,
  "operation": {
    "company": {},
    "country": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "customerPortfolio": true,
    "defaultLocale": "string",
    "id": 0,
    "operationName": "string",
    "operationStatus": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "verifyHoliday": "string"
  },
  "pausedTransfer": true,
  "pending": true,
  "queueControl": "string",
  "queueScheduleStrategy": true,
  "redirectAttendanceAgentDisconnect": true,
  "scheduleActiveSendTime": 0,
  "scheduleName": "string",
  "skipQueue": true,
  "sla": 0,
  "smsActiveShipping": true,
  "survey": 0,
  "telegramActiveShipping": true,
  "timeMaxAttendance": 0,
  "timePending": 0,
  "timeUnit": "NANOSECONDS",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "uraActiveShipping": true,
  "visible": true,
  "voiceActiveShipping": true,
  "warningRatio": 0,
  "wavy": true,
  "whatsappActiveShipping": true,
  "whatsappPartner": true,
  "whatsappPartnerInactivity": 0
}
```

---
