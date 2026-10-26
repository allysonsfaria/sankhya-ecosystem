---
id: "42430231834135"
titulo: "Neppo Chat API — Survey"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231834135-Neppo-Chat-API-Survey"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:26Z"
rotulos: ["sync_hc", "neppo", "neppo_784138262", "sync_hash_352d0c33e3d3"]
---

# Neppo Chat API — Survey

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231834135-Neppo-Chat-API-Survey#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231834135-Neppo-Chat-API-Survey#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231834135-Neppo-Chat-API-Survey#Referencia-tecnica-completa)
- [V1 — survey-controller (15 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231834135-Neppo-Chat-API-Survey#V1--survey-controller-15-endpoints)

**O que é este módulo?**

Gerencia pesquisas de satisfação (CSAT, NPS) enviadas aos clientes ao finalizar um atendimento.

| Quem usa | CX, produto, diretores de operação. |
| --- | --- |
| Problema que resolve | Sem pesquisas de satisfação, a empresa não sabe se os clientes estão satisfeitos, reagindo apenas quando já perdeu o cliente. |
| Impacto na experiência do cliente | O cliente tem voz — seu feedback é coletado e usado para melhorar o serviço continuamente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar pesquisas** | Retorna todas as pesquisas configuradas. |
| **Criar pesquisa** | Configura uma nova pesquisa com perguntas e escala de avaliação. |
| **Consultar resultados** | Agrega as respostas recebidas para análise. |
| **Remover pesquisa** | Exclui uma pesquisa e seus resultados. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/survey/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "allowedSenderTypes": [],
  "active": true,
  "questions": {},
  "id": 0
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `survey-controller` (15 endpoints)

### `/api/survey`

**findAll** · `operationId: findAllUsingPOST_94`

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
| 200 | OK | [PageResponse«SurveyDTO»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "allowedSenderTypes": [],
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "name": "string",
      "type": {
        "id": 0,
        "name": "string"
      },
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/survey/save`

**insert** · `operationId: saveUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [PutSurveyDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "name": "string",
  "allowedSenderTypes": [],
  "active": true,
  "questions": {},
  "id": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [SurveyDetailDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/survey/types`

**findAllTypes** · `operationId: findAllTypesUsingPOST`

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
| 200 | OK | [PageResponse«SurveyType»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "id": 0,
      "name": "string"
    }
  ]
}
```

---

### `/api/survey/{id}`

**findOne** · `operationId: findByIdUsingGET`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [SurveyDetailDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/survey/{id}`

**delete** · `operationId: deleteUsingDELETE_72`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | — |
| 204 | No Content | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |

---

### `/api/v1/survey`

**findAll** · `operationId: findAllUsingPOST_95`

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
| 200 | OK | [PageResponse«SurveyDTO»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "allowedSenderTypes": [],
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "name": "string",
      "type": {
        "id": 0,
        "name": "string"
      },
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/survey/save`

**insert** · `operationId: saveUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [PutSurveyDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "name": "string",
  "allowedSenderTypes": [],
  "active": true,
  "questions": {},
  "id": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [SurveyDetailDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/survey/types`

**findAllTypes** · `operationId: findAllTypesUsingPOST_1`

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
| 200 | OK | [PageResponse«SurveyType»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "id": 0,
      "name": "string"
    }
  ]
}
```

---

### `/api/v1/survey/{id}`

**findOne** · `operationId: findByIdUsingGET_1`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [SurveyDetailDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/survey/{id}`

**delete** · `operationId: deleteUsingDELETE_73`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | — |
| 204 | No Content | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |

---

### `/api/v2/survey`

**findAll** · `operationId: findAllUsingPOST_96`

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
| 200 | OK | [PageResponse«SurveyDTO»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "allowedSenderTypes": [],
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "name": "string",
      "type": {
        "id": 0,
        "name": "string"
      },
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/survey/save`

**insert** · `operationId: saveUsingPOST_3`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [PutSurveyDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "name": "string",
  "allowedSenderTypes": [],
  "active": true,
  "questions": {},
  "id": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [SurveyDetailDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/survey/types`

**findAllTypes** · `operationId: findAllTypesUsingPOST_2`

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
| 200 | OK | [PageResponse«SurveyType»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "id": 0,
      "name": "string"
    }
  ]
}
```

---

### `/api/v2/survey/{id}`

**findOne** · `operationId: findByIdUsingGET_2`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [SurveyDetailDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "allowedSenderTypes": [],
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "questions": [
    {
      "active": true,
      "answers": [],
      "id": 0,
      "seq": 0,
      "type": {},
      "value": "string"
    }
  ],
  "type": {
    "id": 0,
    "name": "string"
  },
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/survey/{id}`

**delete** · `operationId: deleteUsingDELETE_74`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | — |
| 204 | No Content | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |

---
