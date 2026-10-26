---
id: "42430232396823"
titulo: "Neppo Chat API — Agent Hist"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232396823-Neppo-Chat-API-Agent-Hist"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:24Z"
rotulos: ["sync_hc", "neppo", "neppo_784302083", "sync_hash_1c55156e2cdc"]
---

# Neppo Chat API — Agent Hist

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232396823-Neppo-Chat-API-Agent-Hist#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232396823-Neppo-Chat-API-Agent-Hist#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232396823-Neppo-Chat-API-Agent-Hist#Referencia-tecnica-completa)
- [V1 — agent-hist-controller (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232396823-Neppo-Chat-API-Agent-Hist#V1--agent-hist-controller-4-endpoints)
- [V2 — agent-hist-controller-v-2 (2 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430232396823-Neppo-Chat-API-Agent-Hist#V2--agent-hist-controller-v-2-2-endpoints)

**O que é este módulo?**

Registra o histórico de alterações dos atendentes ao longo do tempo.

| Quem usa | Auditores, gestores de RH, analistas de operações. |
| --- | --- |
| Problema que resolve | Sem histórico, mudanças em atendentes (desativações, trocas de equipe) são invisíveis, dificultando auditorias e análise de performance. |
| Impacto na experiência do cliente | Garante rastreabilidade e conformidade, possibilitando revisões de atendimento passado com dados corretos do agente na época. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar histórico** | Retorna todas as versões históricas de um agente. |
| **Buscar registro histórico** | Consulta um estado específico do agente em determinado momento. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/agent-hist/unique" \
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
  "createdAt": "2024-01-01T00:00:00Z",
  "descriptionOfChange": "string",
  "id": 0,
  "maxChatChannels": 0,
  "pauseReasonsId": {
    "active": true,
    "controlPauseTime": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "notifySupervisor": true,
    "pauseChat": true,
    "pauseChatByVoice": true,
    "pauseTime": 0,
    "pauseVoice": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "status": "string",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `agent-hist-controller` (4 endpoints)

### `/api/agent-hist`

**findAll** · `operationId: findAllUsingPOST_3`

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
| 200 | OK | [PageResponse«AgentHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "descriptionOfChange": "string",
      "id": 0,
      "maxChatChannels": 0,
      "pauseReasonsId": {
        "active": true,
        "controlPauseTime": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "notifySupervisor": true,
        "pauseChat": true,
        "pauseChatByVoice": true,
        "pauseTime": 0,
        "pauseVoice": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "status": "string",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/agent-hist/unique`

**findOne** · `operationId: findOneUsingPOST_3`

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
| 200 | OK | [AgentHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "createdAt": "2024-01-01T00:00:00Z",
  "descriptionOfChange": "string",
  "id": 0,
  "maxChatChannels": 0,
  "pauseReasonsId": {
    "active": true,
    "controlPauseTime": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "notifySupervisor": true,
    "pauseChat": true,
    "pauseChatByVoice": true,
    "pauseTime": 0,
    "pauseVoice": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "status": "string",
  "updatedBy": "string"
}
```

---

### `/api/v1/agent-hist`

**findAll** · `operationId: findAllUsingPOST_4`

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
| 200 | OK | [PageResponse«AgentHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "descriptionOfChange": "string",
      "id": 0,
      "maxChatChannels": 0,
      "pauseReasonsId": {
        "active": true,
        "controlPauseTime": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "notifySupervisor": true,
        "pauseChat": true,
        "pauseChatByVoice": true,
        "pauseTime": 0,
        "pauseVoice": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "status": "string",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/agent-hist/unique`

**findOne** · `operationId: findOneUsingPOST_4`

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
| 200 | OK | [AgentHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "createdAt": "2024-01-01T00:00:00Z",
  "descriptionOfChange": "string",
  "id": 0,
  "maxChatChannels": 0,
  "pauseReasonsId": {
    "active": true,
    "controlPauseTime": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "notifySupervisor": true,
    "pauseChat": true,
    "pauseChatByVoice": true,
    "pauseTime": 0,
    "pauseVoice": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "status": "string",
  "updatedBy": "string"
}
```

---

## V2 — `agent-hist-controller-v-2` (2 endpoints)

### `/api/v2/agent-hist`

**findAll** · `operationId: findAllUsingPOST_5`

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
| 200 | OK | [PageResponse«AgentHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "descriptionOfChange": "string",
      "id": 0,
      "maxChatChannels": 0,
      "pauseReasonsId": {
        "active": true,
        "controlPauseTime": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "notifySupervisor": true,
        "pauseChat": true,
        "pauseChatByVoice": true,
        "pauseTime": 0,
        "pauseVoice": true,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "status": "string",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/agent-hist/unique`

**findOne** · `operationId: findOneUsingPOST_5`

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
| 200 | OK | [AgentHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "createdAt": "2024-01-01T00:00:00Z",
  "descriptionOfChange": "string",
  "id": 0,
  "maxChatChannels": 0,
  "pauseReasonsId": {
    "active": true,
    "controlPauseTime": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "notifySupervisor": true,
    "pauseChat": true,
    "pauseChatByVoice": true,
    "pauseTime": 0,
    "pauseVoice": true,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "status": "string",
  "updatedBy": "string"
}
```

---
