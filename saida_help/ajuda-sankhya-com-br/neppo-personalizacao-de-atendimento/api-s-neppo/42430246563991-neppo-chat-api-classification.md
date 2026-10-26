---
id: "42430246563991"
titulo: "Neppo Chat API — Classification"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246563991-Neppo-Chat-API-Classification"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:26Z"
rotulos: ["sync_hc", "neppo", "neppo_784138243", "sync_hash_ca8b9ccee165"]
---

# Neppo Chat API — Classification

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246563991-Neppo-Chat-API-Classification#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246563991-Neppo-Chat-API-Classification#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246563991-Neppo-Chat-API-Classification#Referencia-tecnica-completa)
- [V1 — classification-controller (10 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246563991-Neppo-Chat-API-Classification#V1--classification-controller-10-endpoints)
- [V2 — classification-controller-v-2 (5 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246563991-Neppo-Chat-API-Classification#V2--classification-controller-v-2-5-endpoints)

**O que é este módulo?**

Gerencia as classificações (tags/categorias) que os atendentes aplicam ao finalizar um atendimento.

| Quem usa | Gestores de operação, analytics, produto. |
| --- | --- |
| Problema que resolve | Sem classificação, os motivos de contato ficam desconhecidos, impossibilitando análise de causa raiz e priorização de melhorias. |
| Impacto na experiência do cliente | A empresa entende o que os clientes precisam e pode agir proativamente para resolver os problemas mais comuns. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar classificações** | Retorna todas as categorias disponíveis para classificação. |
| **Criar classificação** | Adiciona uma nova categoria ao catálogo. |
| **Atualizar classificação** | Modifica nome ou hierarquia de uma categoria. |
| **Remover classificação** | Exclui uma categoria não mais utilizada. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/classification-service/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `classification-controller` (10 endpoints)

### `/api/classification-service`

**findAll** · `operationId: findAllUsingPOST_46`

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
| 200 | OK | [PageResponse«Classification»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "classificationTreeSession": 0,
      "commentClassification": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "displayName": "string",
      "groupConfId": 0,
      "id": 0,
      "rootId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/classification-service/complete`

**recursiveClassification** · `operationId: recursiveClassificationUsingPOST`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«Classification»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "classificationTreeSession": 0,
      "commentClassification": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "displayName": "string",
      "groupConfId": 0,
      "id": 0,
      "rootId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/classification-service/delete`

**delete** · `operationId: deleteUsingDELETE_33`

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

### `/api/classification-service/save`

**insert** · `operationId: insertUsingPOST_33`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/classification-service/unique`

**findOne** · `operationId: findOneUsingPOST_42`

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
| 200 | OK | [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/classification-service`

**findAll** · `operationId: findAllUsingPOST_47`

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
| 200 | OK | [PageResponse«Classification»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "classificationTreeSession": 0,
      "commentClassification": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "displayName": "string",
      "groupConfId": 0,
      "id": 0,
      "rootId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/classification-service/complete`

**recursiveClassification** · `operationId: recursiveClassificationUsingPOST_1`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«Classification»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "classificationTreeSession": 0,
      "commentClassification": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "displayName": "string",
      "groupConfId": 0,
      "id": 0,
      "rootId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/classification-service/delete`

**delete** · `operationId: deleteUsingDELETE_34`

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

### `/api/v1/classification-service/save`

**insert** · `operationId: insertUsingPOST_34`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/classification-service/unique`

**findOne** · `operationId: findOneUsingPOST_43`

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
| 200 | OK | [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `classification-controller-v-2` (5 endpoints)

### `/api/v2/classification-service`

**findAll** · `operationId: findAllUsingPOST_48`

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
| 200 | OK | [PageResponse«Classification»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "classificationTreeSession": 0,
      "commentClassification": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "displayName": "string",
      "groupConfId": 0,
      "id": 0,
      "rootId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/classification-service/complete`

**recursiveClassification** · `operationId: recursiveClassificationUsingPOST_2`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«Classification»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "agentId": 0,
      "classificationTree": {
        "active": true,
        "children": [],
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "nodeId": 0,
        "parent": {},
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "value": "string"
      },
      "classificationTreeSession": 0,
      "commentClassification": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "displayName": "string",
      "groupConfId": 0,
      "id": 0,
      "rootId": 0,
      "sessionId": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/classification-service/delete`

**delete** · `operationId: deleteUsingDELETE_35`

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

### `/api/v2/classification-service/save`

**insert** · `operationId: insertUsingPOST_35`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/classification-service/unique`

**findOne** · `operationId: findOneUsingPOST_44`

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
| 200 | OK | [Classification](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "agentId": 0,
  "classificationTree": {
    "active": true,
    "children": [],
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "nodeId": 0,
    "parent": {},
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "value": "string"
  },
  "classificationTreeSession": 0,
  "commentClassification": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "displayName": "string",
  "groupConfId": 0,
  "id": 0,
  "rootId": 0,
  "sessionId": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
