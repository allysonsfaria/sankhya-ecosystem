---
id: "42430248093591"
titulo: "Neppo Chat API — User Group Conf"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430248093591-Neppo-Chat-API-User-Group-Conf"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:20Z"
rotulos: ["sync_hc", "neppo", "neppo_784597050", "sync_hash_94cd91c7b5b7"]
---

# Neppo Chat API — User Group Conf

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430248093591-Neppo-Chat-API-User-Group-Conf#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430248093591-Neppo-Chat-API-User-Group-Conf#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430248093591-Neppo-Chat-API-User-Group-Conf#Referencia-tecnica-completa)
- [V1 — user-group-conf-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430248093591-Neppo-Chat-API-User-Group-Conf#V1--user-group-conf-controller-8-endpoints)
- [V2 — user-group-conf-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430248093591-Neppo-Chat-API-User-Group-Conf#V2--user-group-conf-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia as configurações dos grupos de usuários — regras de roteamento, SLAs e comportamentos específicos por grupo.

| Quem usa | Administradores, gestores de operação. |
| --- | --- |
| Problema que resolve | Sem configurações por grupo, todos os segmentos de clientes recebem o mesmo tratamento, ignorando diferenças de SLA e prioridade. |
| Impacto na experiência do cliente | Clientes de segmentos prioritários têm SLAs garantidos e são atendidos primeiro, aumentando a satisfação e a retenção. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar configurações** | Retorna as configurações de todos os grupos. |
| **Criar/atualizar configuração** | Define SLA, prioridade e regras para um grupo. |
| **Remover configuração** | Remove as configurações especiais de um grupo. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/user-group/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "chatUserGroupConfId": {
    "agentId": 0,
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
  "chatUserGroupConfId": {
    "agentId": 0,
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

## V1 — `user-group-conf-controller` (8 endpoints)

### `/api/user-group`

**findAll** · `operationId: findAllUsingPOST_112`

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
| 200 | OK | [PageResponse«ChatUserGroupConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatUserGroupConfId": {
        "agentId": 0,
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

### `/api/user-group/delete`

**delete** · `operationId: deleteUsingDELETE_90`

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

### `/api/user-group/save`

**insert** · `operationId: insertUsingPOST_90`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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
| 200 | OK | [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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

### `/api/user-group/unique`

**findOne** · `operationId: findOneUsingPOST_105`

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
| 200 | OK | [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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

### `/api/v1/user-group`

**findAll** · `operationId: findAllUsingPOST_113`

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
| 200 | OK | [PageResponse«ChatUserGroupConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatUserGroupConfId": {
        "agentId": 0,
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

### `/api/v1/user-group/delete`

**delete** · `operationId: deleteUsingDELETE_91`

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

### `/api/v1/user-group/save`

**insert** · `operationId: insertUsingPOST_91`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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
| 200 | OK | [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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

### `/api/v1/user-group/unique`

**findOne** · `operationId: findOneUsingPOST_106`

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
| 200 | OK | [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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

## V2 — `user-group-conf-controller-v-2` (4 endpoints)

### `/api/v2/user-group`

**findAll** · `operationId: findAllUsingPOST_114`

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
| 200 | OK | [PageResponse«ChatUserGroupConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatUserGroupConfId": {
        "agentId": 0,
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

### `/api/v2/user-group/delete`

**delete** · `operationId: deleteUsingDELETE_92`

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

### `/api/v2/user-group/save`

**insert** · `operationId: insertUsingPOST_92`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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
| 200 | OK | [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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

### `/api/v2/user-group/unique`

**findOne** · `operationId: findOneUsingPOST_107`

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
| 200 | OK | [ChatUserGroupConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatUserGroupConfId": {
    "agentId": 0,
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
