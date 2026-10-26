---
id: "42430301747735"
titulo: "Neppo Chat API — Work Schedule"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301747735-Neppo-Chat-API-Work-Schedule"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:17Z"
rotulos: ["sync_hc", "neppo", "neppo_784728065", "sync_hash_40f86aad0624"]
---

# Neppo Chat API — Work Schedule

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301747735-Neppo-Chat-API-Work-Schedule#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301747735-Neppo-Chat-API-Work-Schedule#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301747735-Neppo-Chat-API-Work-Schedule#Referencia-tecnica-completa)
- [V1 — work-schedule-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301747735-Neppo-Chat-API-Work-Schedule#V1--work-schedule-controller-8-endpoints)
- [V2 — work-schedule-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301747735-Neppo-Chat-API-Work-Schedule#V2--work-schedule-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia os horários de funcionamento do atendimento — quando cada canal, grupo ou agente está disponível para receber clientes.

| Quem usa | Administradores, gestores de operação. |
| --- | --- |
| Problema que resolve | Sem controle de horários, atendimentos chegam fora do horário operacional sem resposta automática, frustrando clientes. |
| Impacto na experiência do cliente | Fora do horário, o cliente recebe uma mensagem automática informando quando será atendido, gerenciando a expectativa corretamente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar horários** | Retorna todos os horários de funcionamento configurados. |
| **Criar horário** | Define os dias e horários de operação. |
| **Atualizar horário** | Modifica o calendário de um canal ou grupo. |
| **Remover horário** | Exclui uma configuração de horário. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/work-schedule/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `work-schedule-controller` (8 endpoints)

### `/api/v1/work-schedule`

**findAll** · `operationId: findAllUsingPOST_118`

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
| 200 | OK | [PageResponse«WorkSchedule»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "closeTime": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "dayCode": 0,
      "id": 0,
      "name": "string",
      "openTime": "string",
      "scheduleName": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/work-schedule/delete`

**delete** · `operationId: deleteUsingDELETE_96`

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

### `/api/v1/work-schedule/save`

**insert** · `operationId: insertUsingPOST_96`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/work-schedule/unique`

**findOne** · `operationId: findOneUsingPOST_111`

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
| 200 | OK | [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/work-schedule`

**findAll** · `operationId: findAllUsingPOST_119`

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
| 200 | OK | [PageResponse«WorkSchedule»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "closeTime": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "dayCode": 0,
      "id": 0,
      "name": "string",
      "openTime": "string",
      "scheduleName": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/work-schedule/delete`

**delete** · `operationId: deleteUsingDELETE_97`

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

### `/api/work-schedule/save`

**insert** · `operationId: insertUsingPOST_97`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/work-schedule/unique`

**findOne** · `operationId: findOneUsingPOST_112`

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
| 200 | OK | [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `work-schedule-controller-v-2` (4 endpoints)

### `/api/v2/work-schedule`

**findAll** · `operationId: findAllUsingPOST_120`

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
| 200 | OK | [PageResponse«WorkSchedule»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "closeTime": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "dayCode": 0,
      "id": 0,
      "name": "string",
      "openTime": "string",
      "scheduleName": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/work-schedule/delete`

**delete** · `operationId: deleteUsingDELETE_98`

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

### `/api/v2/work-schedule/save`

**insert** · `operationId: insertUsingPOST_98`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/work-schedule/unique`

**findOne** · `operationId: findOneUsingPOST_113`

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
| 200 | OK | [WorkSchedule](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "closeTime": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dayCode": 0,
  "id": 0,
  "name": "string",
  "openTime": "string",
  "scheduleName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
