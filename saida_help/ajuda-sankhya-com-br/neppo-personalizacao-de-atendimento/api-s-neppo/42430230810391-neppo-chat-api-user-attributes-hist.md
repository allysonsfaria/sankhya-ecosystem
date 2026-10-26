---
id: "42430230810391"
titulo: "Neppo Chat API — User Attributes Hist"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230810391-Neppo-Chat-API-User-Attributes-Hist"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:30Z"
rotulos: ["sync_hc", "neppo", "neppo_783646725", "sync_hash_df42114e2457"]
---

# Neppo Chat API — User Attributes Hist

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230810391-Neppo-Chat-API-User-Attributes-Hist#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230810391-Neppo-Chat-API-User-Attributes-Hist#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230810391-Neppo-Chat-API-User-Attributes-Hist#Referencia-tecnica-completa)
- [V1 — user-attributes-hist-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230810391-Neppo-Chat-API-User-Attributes-Hist#V1--user-attributes-hist-controller-8-endpoints)
- [V2 — user-attributes-hist-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230810391-Neppo-Chat-API-User-Attributes-Hist#V2--user-attributes-hist-controller-v-2-4-endpoints)

**O que é este módulo?**

Mantém o histórico de alterações dos atributos dos usuários — rastreia quem mudou o que e quando.

| Quem usa | Auditores, compliance, analytics. |
| --- | --- |
| Problema que resolve | Sem histórico de mudanças de atributos, não é possível rastrear alterações de dados do cliente (ex: troca de plano, mudança de segmento). |
| Impacto na experiência do cliente | Garante que dados do cliente sejam rastreáveis e auditáveis, protegendo a empresa em disputas e garantindo conformidade com LGPD. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar histórico** | Retorna todas as mudanças de atributos de um usuário. |
| **Consultar mudança** | Obtém os detalhes de uma alteração específica. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/user-attributes-hist/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `user-attributes-hist-controller` (8 endpoints)

### `/api/user-attributes-hist`

**findAll** · `operationId: findAllUsingPOST_106`

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
| 200 | OK | [PageResponse«UserAttributesHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "userAttributesHistId": {
        "sessionId": 0,
        "userAttributesId": 0
      }
    }
  ]
}
```

---

### `/api/user-attributes-hist/delete`

**delete** · `operationId: deleteUsingDELETE_84`

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

### `/api/user-attributes-hist/save`

**insert** · `operationId: insertUsingPOST_84`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

---

### `/api/user-attributes-hist/unique`

**findOne** · `operationId: findOneUsingPOST_99`

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
| 200 | OK | [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

---

### `/api/v1/user-attributes-hist`

**findAll** · `operationId: findAllUsingPOST_107`

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
| 200 | OK | [PageResponse«UserAttributesHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "userAttributesHistId": {
        "sessionId": 0,
        "userAttributesId": 0
      }
    }
  ]
}
```

---

### `/api/v1/user-attributes-hist/delete`

**delete** · `operationId: deleteUsingDELETE_85`

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

### `/api/v1/user-attributes-hist/save`

**insert** · `operationId: insertUsingPOST_85`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

---

### `/api/v1/user-attributes-hist/unique`

**findOne** · `operationId: findOneUsingPOST_100`

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
| 200 | OK | [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

---

## V2 — `user-attributes-hist-controller-v-2` (4 endpoints)

### `/api/v2/user-attributes-hist`

**findAll** · `operationId: findAllUsingPOST_108`

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
| 200 | OK | [PageResponse«UserAttributesHist»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "userAttributesHistId": {
        "sessionId": 0,
        "userAttributesId": 0
      }
    }
  ]
}
```

---

### `/api/v2/user-attributes-hist/delete`

**delete** · `operationId: deleteUsingDELETE_86`

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

### `/api/v2/user-attributes-hist/save`

**insert** · `operationId: insertUsingPOST_86`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

---

### `/api/v2/user-attributes-hist/unique`

**findOne** · `operationId: findOneUsingPOST_101`

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
| 200 | OK | [UserAttributesHist](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "userAttributesHistId": {
    "sessionId": 0,
    "userAttributesId": 0
  }
}
```

---
