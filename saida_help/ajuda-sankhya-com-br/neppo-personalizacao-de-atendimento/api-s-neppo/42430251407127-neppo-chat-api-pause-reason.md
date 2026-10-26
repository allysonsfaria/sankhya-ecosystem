---
id: "42430251407127"
titulo: "Neppo Chat API — Pause Reason"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251407127-Neppo-Chat-API-Pause-Reason"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:36Z"
rotulos: ["sync_hc", "neppo", "neppo_783155224", "sync_hash_dab854be5d88"]
---

# Neppo Chat API — Pause Reason

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251407127-Neppo-Chat-API-Pause-Reason#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251407127-Neppo-Chat-API-Pause-Reason#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251407127-Neppo-Chat-API-Pause-Reason#Referencia-tecnica-completa)
- [V1 — pause-reason-controller (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251407127-Neppo-Chat-API-Pause-Reason#V1--pause-reason-controller-4-endpoints)
- [V2 — pause-reason-controller-v-2 (2 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251407127-Neppo-Chat-API-Pause-Reason#V2--pause-reason-controller-v-2-2-endpoints)

**O que é este módulo?**

Gerencia os motivos de pausa dos atendentes — razões pré-definidas que o atendente seleciona ao sair da fila.

| Quem usa | Gestores de operação, RH, analytics. |
| --- | --- |
| Problema que resolve | Sem controle de motivos de pausa, não é possível distinguir pausas legítimas (almoço, reunião) de ausências não justificadas. |
| Impacto na experiência do cliente | Com atendentes melhor gerenciados, os clientes encontram mais atendentes disponíveis quando precisam. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar motivos** | Retorna todos os motivos de pausa configurados. |
| **Criar motivo** | Adiciona um novo motivo ao catálogo. |
| **Atualizar motivo** | Modifica a descrição ou ativa/desativa um motivo. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/pause-reasons/unique" \
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
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `pause-reason-controller` (4 endpoints)

### `/api/pause-reasons`

**findAll** · `operationId: findAllUsingPOST_85`

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
| 200 | OK | [PageResponse«PauseReason»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
    }
  ]
}
```

---

### `/api/pause-reasons/unique`

**findOne** · `operationId: findOneUsingPOST_81`

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
| 200 | OK | [PauseReason](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/v1/pause-reasons`

**findAll** · `operationId: findAllUsingPOST_86`

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
| 200 | OK | [PageResponse«PauseReason»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
    }
  ]
}
```

---

### `/api/v1/pause-reasons/unique`

**findOne** · `operationId: findOneUsingPOST_82`

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
| 200 | OK | [PauseReason](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

## V2 — `pause-reason-controller-v-2` (2 endpoints)

### `/api/v2/pause-reasons`

**findAll** · `operationId: findAllUsingPOST_87`

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
| 200 | OK | [PageResponse«PauseReason»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
    }
  ]
}
```

---

### `/api/v2/pause-reasons/unique`

**findOne** · `operationId: findOneUsingPOST_83`

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
| 200 | OK | [PauseReason](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---
