---
id: "42430301596311"
titulo: "Neppo Chat API — Holiday Operation"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301596311-Neppo-Chat-API-Holiday-Operation"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:17Z"
rotulos: ["sync_hc", "neppo", "neppo_784695297", "sync_hash_6c5cb1c2af47"]
---

# Neppo Chat API — Holiday Operation

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301596311-Neppo-Chat-API-Holiday-Operation#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301596311-Neppo-Chat-API-Holiday-Operation#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301596311-Neppo-Chat-API-Holiday-Operation#Referencia-tecnica-completa)
- [V1 — holiday-operation-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301596311-Neppo-Chat-API-Holiday-Operation#V1--holiday-operation-controller-8-endpoints)
- [V2 — holiday-operation-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301596311-Neppo-Chat-API-Holiday-Operation#V2--holiday-operation-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia feriados e exceções no calendário operacional — dias e horários em que o atendimento funciona diferente.

| Quem usa | Administradores, gestores de operação. |
| --- | --- |
| Problema que resolve | Sem controle de feriados, o sistema pode rotear atendimentos em dias não operacionais, frustrando clientes e sobrecarregando atendentes de plantão. |
| Impacto na experiência do cliente | O cliente recebe mensagem adequada quando entra em contato em um feriado, informando quando será atendido. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar feriados** | Retorna o calendário de exceções operacionais. |
| **Criar feriado** | Adiciona um dia/período de exceção com mensagem customizada. |
| **Atualizar feriado** | Modifica datas ou comportamento de um feriado. |
| **Remover feriado** | Remove uma exceção do calendário. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/holiday-operation/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `holiday-operation-controller` (8 endpoints)

### `/api/holiday-operation`

**findAll** · `operationId: findAllUsingPOST_70`

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
| 200 | OK | [PageResponse«HolidayOperation»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "holiday": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "dateHoliday": "string",
        "id": 0,
        "name": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "holidayOperationId": {
        "holidayId": 0,
        "operationId": 0
      },
      "operations": {
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
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/holiday-operation/delete`

**delete** · `operationId: deleteUsingDELETE_51`

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

### `/api/holiday-operation/save`

**insert** · `operationId: insertUsingPOST_54`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/holiday-operation/unique`

**findOne** · `operationId: findOneUsingPOST_66`

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
| 200 | OK | [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/holiday-operation`

**findAll** · `operationId: findAllUsingPOST_71`

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
| 200 | OK | [PageResponse«HolidayOperation»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "holiday": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "dateHoliday": "string",
        "id": 0,
        "name": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "holidayOperationId": {
        "holidayId": 0,
        "operationId": 0
      },
      "operations": {
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
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/holiday-operation/delete`

**delete** · `operationId: deleteUsingDELETE_52`

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

### `/api/v1/holiday-operation/save`

**insert** · `operationId: insertUsingPOST_55`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/holiday-operation/unique`

**findOne** · `operationId: findOneUsingPOST_67`

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
| 200 | OK | [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `holiday-operation-controller-v-2` (4 endpoints)

### `/api/v2/holiday-operation`

**findAll** · `operationId: findAllUsingPOST_72`

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
| 200 | OK | [PageResponse«HolidayOperation»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "holiday": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "dateHoliday": "string",
        "id": 0,
        "name": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "holidayOperationId": {
        "holidayId": 0,
        "operationId": 0
      },
      "operations": {
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
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/holiday-operation/delete`

**delete** · `operationId: deleteUsingDELETE_53`

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

### `/api/v2/holiday-operation/save`

**insert** · `operationId: insertUsingPOST_56`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/holiday-operation/unique`

**findOne** · `operationId: findOneUsingPOST_68`

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
| 200 | OK | [HolidayOperation](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "holiday": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "dateHoliday": "string",
    "id": 0,
    "name": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "holidayOperationId": {
    "holidayId": 0,
    "operationId": 0
  },
  "operations": {
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
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
