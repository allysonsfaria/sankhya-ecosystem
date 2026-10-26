---
id: "42430198515735"
titulo: "Neppo Chat API — Chat Web Conf"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430198515735-Neppo-Chat-API-Chat-Web-Conf"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:32Z"
rotulos: ["sync_hc", "neppo", "neppo_783515670", "sync_hash_789a1ffaac18"]
---

# Neppo Chat API — Chat Web Conf

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430198515735-Neppo-Chat-API-Chat-Web-Conf#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430198515735-Neppo-Chat-API-Chat-Web-Conf#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430198515735-Neppo-Chat-API-Chat-Web-Conf#Referencia-tecnica-completa)
- [V1 — chat-web-conf-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430198515735-Neppo-Chat-API-Chat-Web-Conf#V1--chat-web-conf-controller-8-endpoints)
- [V2 — chat-web-conf-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430198515735-Neppo-Chat-API-Chat-Web-Conf#V2--chat-web-conf-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia as configurações globais do módulo de chat web, como comportamento de sessão, mensagens padrão e limites.

| Quem usa | Administradores de plataforma, times de TI. |
| --- | --- |
| Problema que resolve | Sem configurações centralizadas, cada instância do chat pode ter comportamentos inconsistentes, afetando a experiência do usuário. |
| Impacto na experiência do cliente | O chat se comporta de forma previsível e configurada pelo negócio, sem surpresas para o cliente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar configurações** | Retorna as configurações atuais do chat web. |
| **Salvar configuração** | Atualiza parâmetros globais do chat. |
| **Buscar configuração específica** | Consulta uma configuração específica por ID. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/chat-web-conf/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-web-conf-controller` (8 endpoints)

### `/api/chat-web-conf`

**findAll** · `operationId: findAllUsingPOST_43`

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
| 200 | OK | [PageResponse«ChatWebConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatGroupConf": {
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
      "configuration": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "cssScript": "string",
      "htmlScript": "string",
      "id": 0,
      "initialMessage": "string",
      "jsScript": "string",
      "token": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/chat-web-conf/delete`

**delete** · `operationId: deleteUsingDELETE_30`

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

### `/api/chat-web-conf/save`

**insert** · `operationId: insertUsingPOST_30`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/chat-web-conf/unique`

**findOne** · `operationId: findOneUsingPOST_39`

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
| 200 | OK | [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/chat-web-conf`

**findAll** · `operationId: findAllUsingPOST_44`

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
| 200 | OK | [PageResponse«ChatWebConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatGroupConf": {
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
      "configuration": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "cssScript": "string",
      "htmlScript": "string",
      "id": 0,
      "initialMessage": "string",
      "jsScript": "string",
      "token": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/chat-web-conf/delete`

**delete** · `operationId: deleteUsingDELETE_31`

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

### `/api/v1/chat-web-conf/save`

**insert** · `operationId: insertUsingPOST_31`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/chat-web-conf/unique`

**findOne** · `operationId: findOneUsingPOST_40`

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
| 200 | OK | [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `chat-web-conf-controller-v-2` (4 endpoints)

### `/api/v2/chat-web-conf`

**findAll** · `operationId: findAllUsingPOST_45`

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
| 200 | OK | [PageResponse«ChatWebConf»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "chatGroupConf": {
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
      "configuration": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "cssScript": "string",
      "htmlScript": "string",
      "id": 0,
      "initialMessage": "string",
      "jsScript": "string",
      "token": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/chat-web-conf/delete`

**delete** · `operationId: deleteUsingDELETE_32`

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

### `/api/v2/chat-web-conf/save`

**insert** · `operationId: insertUsingPOST_32`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/chat-web-conf/unique`

**findOne** · `operationId: findOneUsingPOST_41`

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
| 200 | OK | [ChatWebConf](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "chatGroupConf": {
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
  "configuration": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "cssScript": "string",
  "htmlScript": "string",
  "id": 0,
  "initialMessage": "string",
  "jsScript": "string",
  "token": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
