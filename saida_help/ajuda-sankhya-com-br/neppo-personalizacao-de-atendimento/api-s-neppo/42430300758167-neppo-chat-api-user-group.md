---
id: "42430300758167"
titulo: "Neppo Chat API — User Group"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300758167-Neppo-Chat-API-User-Group"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:20Z"
rotulos: ["sync_hc", "neppo", "neppo_784597069", "sync_hash_c637b6d4a5d3"]
---

# Neppo Chat API — User Group

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300758167-Neppo-Chat-API-User-Group#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300758167-Neppo-Chat-API-User-Group#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300758167-Neppo-Chat-API-User-Group#Referencia-tecnica-completa)
- [V1 — user-group-controller (12 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300758167-Neppo-Chat-API-User-Group#V1--user-group-controller-12-endpoints)
- [V2 — user-group-controller-v-2 (6 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300758167-Neppo-Chat-API-User-Group#V2--user-group-controller-v-2-6-endpoints)

**O que é este módulo?**

Gerencia a associação de usuários/contatos a grupos — organiza clientes em segmentos para atendimento personalizado.

| Quem usa |  |
| --- | --- |
| Problema que resolve | Sem segmentação de usuários, não é possível direcionar campanhas ou criar regras de roteamento baseadas no perfil do cliente. |
| Impacto na experiência do cliente | Clientes premium são atendidos por equipes especializadas e recebem comunicações relevantes ao seu perfil. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar grupos do usuário** | Retorna os grupos aos quais um usuário pertence. |
| **Adicionar usuário ao grupo** | Associa um contato a um segmento. |
| **Remover do grupo** | Remove a associação de um contato com um grupo. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/chat-user-group/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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

## V1 — `user-group-controller` (12 endpoints)

### `/api/chat-user-group`

**findAll** · `operationId: findAllUsingPOST_115`

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
| 200 | OK | [PageResponse«ChatUserGroup»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatUserGroupId": {
        "userId": 0,
        "groupConfId": 0
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "groupConf": {
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

### `/api/chat-user-group/client-groups-association`

**saveClientGroupsAssociation** · `operationId: saveClientGroupsAssociationUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientGroupsDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "groupIds": []
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

### `/api/chat-user-group/delete`

**delete** · `operationId: deleteUsingDELETE_93`

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

### `/api/chat-user-group/deleteAssociation`

**deleteAssociation** · `operationId: deleteAssociationUsingDELETE_3`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroupId](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "groupConfId": 0
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

### `/api/chat-user-group/save`

**insert** · `operationId: insertUsingPOST_93`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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
| 200 | OK | [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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

### `/api/chat-user-group/unique`

**findOne** · `operationId: findOneUsingPOST_108`

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
| 200 | OK | [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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

### `/api/v1/chat-user-group`

**findAll** · `operationId: findAllUsingPOST_116`

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
| 200 | OK | [PageResponse«ChatUserGroup»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatUserGroupId": {
        "userId": 0,
        "groupConfId": 0
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "groupConf": {
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

### `/api/v1/chat-user-group/client-groups-association`

**saveClientGroupsAssociation** · `operationId: saveClientGroupsAssociationUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientGroupsDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "groupIds": []
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

### `/api/v1/chat-user-group/delete`

**delete** · `operationId: deleteUsingDELETE_94`

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

### `/api/v1/chat-user-group/deleteAssociation`

**deleteAssociation** · `operationId: deleteAssociationUsingDELETE_4`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroupId](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "groupConfId": 0
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

### `/api/v1/chat-user-group/save`

**insert** · `operationId: insertUsingPOST_94`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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
| 200 | OK | [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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

### `/api/v1/chat-user-group/unique`

**findOne** · `operationId: findOneUsingPOST_109`

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
| 200 | OK | [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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

## V2 — `user-group-controller-v-2` (6 endpoints)

### `/api/v2/chat-user-group`

**findAll** · `operationId: findAllUsingPOST_117`

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
| 200 | OK | [PageResponse«ChatUserGroup»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatUserGroupId": {
        "userId": 0,
        "groupConfId": 0
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "groupConf": {
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

### `/api/v2/chat-user-group/client-groups-association`

**saveClientGroupsAssociation** · `operationId: saveClientGroupsAssociationUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClientGroupsDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "groupIds": []
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

### `/api/v2/chat-user-group/delete`

**delete** · `operationId: deleteUsingDELETE_95`

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

### `/api/v2/chat-user-group/deleteAssociation`

**deleteAssociation** · `operationId: deleteAssociationUsingDELETE_5`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroupId](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "userId": 0,
  "groupConfId": 0
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

### `/api/v2/chat-user-group/save`

**insert** · `operationId: insertUsingPOST_95`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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
| 200 | OK | [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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

### `/api/v2/chat-user-group/unique`

**findOne** · `operationId: findOneUsingPOST_110`

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
| 200 | OK | [ChatUserGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupId": {
    "userId": 0,
    "groupConfId": 0
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupConf": {
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
