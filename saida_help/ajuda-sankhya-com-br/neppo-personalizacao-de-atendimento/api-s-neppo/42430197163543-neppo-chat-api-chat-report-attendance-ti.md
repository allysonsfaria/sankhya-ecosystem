---
id: "42430197163543"
titulo: "Neppo Chat API — Chat Report Attendance Time"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197163543-Neppo-Chat-API-Chat-Report-Attendance-Time"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:37Z"
rotulos: ["sync_hc", "neppo", "neppo_783122442", "sync_hash_778df48cf9f2"]
---

# Neppo Chat API — Chat Report Attendance Time

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197163543-Neppo-Chat-API-Chat-Report-Attendance-Time#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197163543-Neppo-Chat-API-Chat-Report-Attendance-Time#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197163543-Neppo-Chat-API-Chat-Report-Attendance-Time#Referencia-tecnica-completa)
- [V1 — chat-report-attendance-time-controller (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197163543-Neppo-Chat-API-Chat-Report-Attendance-Time#V1--chat-report-attendance-time-controller-4-endpoints)
- [V2 — chat-report-attendance-time-controller-v-2 (2 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430197163543-Neppo-Chat-API-Chat-Report-Attendance-Time#V2--chat-report-attendance-time-controller-v-2-2-endpoints)

**O que é este módulo?**

Gera relatórios de tempo de atendimento, incluindo tempo de resposta, TMA (Tempo Médio de Atendimento) e tempo de espera.

| Quem usa | Gestores de operação, analistas de qualidade, diretores de CX. |
| --- | --- |
| Problema que resolve | Sem métricas de tempo, não há como identificar gargalos operacionais, medir SLA ou justificar investimentos em equipe. |
| Impacto na experiência do cliente | Clientes esperam menos e são atendidos mais rapidamente, pois os gestores conseguem agir sobre os dados de tempo real. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Gerar relatório** | Retorna métricas de tempo de atendimento por período, canal e agente. |
| **Consultar relatório por agente** | Analisa o desempenho de um atendente específico. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/report-attendance-time/unique" \
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
  "agentName": "string",
  "attendanceTime": 0,
  "channelName": "string",
  "closedAtProtocol": "2024-01-01T00:00:00Z",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdAtProtocol": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupName": "string",
  "id": 0,
  "lastGroup": "string",
  "lastStatus": "string",
  "nextGroup": "string",
  "operationName": "string",
  "protocol": "string",
  "protocolDuration": 0,
  "step": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "waitingTime": 0
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-report-attendance-time-controller` (4 endpoints)

### `/api/report-attendance-time`

**findAll** · `operationId: findAllUsingPOST_37`

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
| 200 | OK | [PageResponse«ChatReportAttendanceTime»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentName": "string",
      "attendanceTime": 0,
      "channelName": "string",
      "closedAtProtocol": "2024-01-01T00:00:00Z",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdAtProtocol": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "groupName": "string",
      "id": 0,
      "lastGroup": "string",
      "lastStatus": "string",
      "nextGroup": "string",
      "operationName": "string",
      "protocol": "string",
      "protocolDuration": 0,
      "step": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "waitingTime": 0
    }
  ]
}
```

---

### `/api/report-attendance-time/unique`

**findOne** · `operationId: findOneUsingPOST_33`

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
| 200 | OK | [ChatReportAttendanceTime](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentName": "string",
  "attendanceTime": 0,
  "channelName": "string",
  "closedAtProtocol": "2024-01-01T00:00:00Z",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdAtProtocol": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupName": "string",
  "id": 0,
  "lastGroup": "string",
  "lastStatus": "string",
  "nextGroup": "string",
  "operationName": "string",
  "protocol": "string",
  "protocolDuration": 0,
  "step": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "waitingTime": 0
}
```

---

### `/api/v1/report-attendance-time`

**findAll** · `operationId: findAllUsingPOST_38`

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
| 200 | OK | [PageResponse«ChatReportAttendanceTime»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentName": "string",
      "attendanceTime": 0,
      "channelName": "string",
      "closedAtProtocol": "2024-01-01T00:00:00Z",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdAtProtocol": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "groupName": "string",
      "id": 0,
      "lastGroup": "string",
      "lastStatus": "string",
      "nextGroup": "string",
      "operationName": "string",
      "protocol": "string",
      "protocolDuration": 0,
      "step": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "waitingTime": 0
    }
  ]
}
```

---

### `/api/v1/report-attendance-time/unique`

**findOne** · `operationId: findOneUsingPOST_34`

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
| 200 | OK | [ChatReportAttendanceTime](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentName": "string",
  "attendanceTime": 0,
  "channelName": "string",
  "closedAtProtocol": "2024-01-01T00:00:00Z",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdAtProtocol": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupName": "string",
  "id": 0,
  "lastGroup": "string",
  "lastStatus": "string",
  "nextGroup": "string",
  "operationName": "string",
  "protocol": "string",
  "protocolDuration": 0,
  "step": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "waitingTime": 0
}
```

---

## V2 — `chat-report-attendance-time-controller-v-2` (2 endpoints)

### `/api/v2/report-attendance-time`

**findAll** · `operationId: findAllUsingPOST_39`

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
| 200 | OK | [PageResponse«ChatReportAttendanceTime»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentName": "string",
      "attendanceTime": 0,
      "channelName": "string",
      "closedAtProtocol": "2024-01-01T00:00:00Z",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdAtProtocol": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "groupName": "string",
      "id": 0,
      "lastGroup": "string",
      "lastStatus": "string",
      "nextGroup": "string",
      "operationName": "string",
      "protocol": "string",
      "protocolDuration": 0,
      "step": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "waitingTime": 0
    }
  ]
}
```

---

### `/api/v2/report-attendance-time/unique`

**findOne** · `operationId: findOneUsingPOST_35`

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
| 200 | OK | [ChatReportAttendanceTime](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentName": "string",
  "attendanceTime": 0,
  "channelName": "string",
  "closedAtProtocol": "2024-01-01T00:00:00Z",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdAtProtocol": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "groupName": "string",
  "id": 0,
  "lastGroup": "string",
  "lastStatus": "string",
  "nextGroup": "string",
  "operationName": "string",
  "protocol": "string",
  "protocolDuration": 0,
  "step": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "waitingTime": 0
}
```

---
