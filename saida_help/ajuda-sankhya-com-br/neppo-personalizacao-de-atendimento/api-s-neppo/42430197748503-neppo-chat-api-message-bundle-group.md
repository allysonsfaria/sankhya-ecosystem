---
id: "42430197748503"
titulo: "Neppo Chat API — Message Bundle Group"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197748503-Neppo-Chat-API-Message-Bundle-Group"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:35Z"
rotulos: ["sync_hc", "neppo", "neppo_783351836", "sync_hash_71d6ec89caa7"]
---

# Neppo Chat API — Message Bundle Group

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197748503-Neppo-Chat-API-Message-Bundle-Group#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197748503-Neppo-Chat-API-Message-Bundle-Group#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197748503-Neppo-Chat-API-Message-Bundle-Group#Referencia-tecnica-completa)
- [V1 — message-bundle-group-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197748503-Neppo-Chat-API-Message-Bundle-Group#V1--message-bundle-group-controller-8-endpoints)
- [V2 — message-bundle-group-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197748503-Neppo-Chat-API-Message-Bundle-Group#V2--message-bundle-group-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia grupos de pacotes de mensagens — conjuntos de mensagens pré-configuradas para envio sequencial ou condicional.

| Quem usa | Times de produto, automação, marketing. |
| --- | --- |
| Problema que resolve | Fluxos complexos de comunicação (ex: onboarding em etapas) são difíceis de gerenciar sem agrupamento de mensagens. |
| Impacto na experiência do cliente | O cliente recebe uma sequência lógica e bem-estruturada de mensagens, melhorando a jornada de onboarding ou de resolução. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar grupos** | Retorna todos os grupos de pacotes de mensagens. |
| **Criar grupo** | Agrupa mensagens em um fluxo sequencial. |
| **Atualizar grupo** | Modifica a ordem ou conteúdo das mensagens do grupo. |
| **Remover grupo** | Exclui o grupo de mensagens. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/message-bundle-group/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `message-bundle-group-controller` (8 endpoints)

### `/api/message-bundle-group`

**findAll** · `operationId: findAllUsingPOST_79`

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
| 200 | OK | [PageResponse«MessageBundle»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "code": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
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
      "id": 0,
      "locale": "string",
      "text": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "use": true
    }
  ]
}
```

---

### `/api/message-bundle-group/delete`

**delete** · `operationId: deleteUsingDELETE_60`

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

### `/api/message-bundle-group/save`

**insert** · `operationId: insertUsingPOST_63`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

---

### `/api/message-bundle-group/unique`

**findOne** · `operationId: findOneUsingPOST_75`

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
| 200 | OK | [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

---

### `/api/v1/message-bundle-group`

**findAll** · `operationId: findAllUsingPOST_80`

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
| 200 | OK | [PageResponse«MessageBundle»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "code": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
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
      "id": 0,
      "locale": "string",
      "text": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "use": true
    }
  ]
}
```

---

### `/api/v1/message-bundle-group/delete`

**delete** · `operationId: deleteUsingDELETE_61`

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

### `/api/v1/message-bundle-group/save`

**insert** · `operationId: insertUsingPOST_64`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

---

### `/api/v1/message-bundle-group/unique`

**findOne** · `operationId: findOneUsingPOST_76`

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
| 200 | OK | [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

---

## V2 — `message-bundle-group-controller-v-2` (4 endpoints)

### `/api/v2/message-bundle-group`

**findAll** · `operationId: findAllUsingPOST_81`

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
| 200 | OK | [PageResponse«MessageBundle»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "code": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
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
      "id": 0,
      "locale": "string",
      "text": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "use": true
    }
  ]
}
```

---

### `/api/v2/message-bundle-group/delete`

**delete** · `operationId: deleteUsingDELETE_62`

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

### `/api/v2/message-bundle-group/save`

**insert** · `operationId: insertUsingPOST_65`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

---

### `/api/v2/message-bundle-group/unique`

**findOne** · `operationId: findOneUsingPOST_77`

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
| 200 | OK | [MessageBundle](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
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
  "id": 0,
  "locale": "string",
  "text": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "use": true
}
```

---
