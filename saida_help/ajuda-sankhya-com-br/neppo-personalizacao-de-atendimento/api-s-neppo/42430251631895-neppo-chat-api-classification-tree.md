---
id: "42430251631895"
titulo: "Neppo Chat API — Classification Tree"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251631895-Neppo-Chat-API-Classification-Tree"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:35Z"
rotulos: ["sync_hc", "neppo", "neppo_783351817", "sync_hash_d123d01fcf06"]
---

# Neppo Chat API — Classification Tree

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251631895-Neppo-Chat-API-Classification-Tree#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251631895-Neppo-Chat-API-Classification-Tree#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251631895-Neppo-Chat-API-Classification-Tree#Referencia-tecnica-completa)
- [V1 — classification-tree-controller (10 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251631895-Neppo-Chat-API-Classification-Tree#V1--classification-tree-controller-10-endpoints)
- [V2 — classification-tree-controller-v-2 (5 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430251631895-Neppo-Chat-API-Classification-Tree#V2--classification-tree-controller-v-2-5-endpoints)

**O que é este módulo?**

Gerencia as árvores de classificação — estruturas hierárquicas que organizam categorias em forma de árvore (pai/filho).

| Quem usa | Gestores de operação, analistas de produto. |
| --- | --- |
| Problema que resolve | Categorias planas não representam a complexidade real dos motivos de contato. A árvore permite drill-down em relatórios. |
| Impacto na experiência do cliente | A empresa tem uma visão granular dos motivos de contato, podendo agir no nível certo (ex: 'Financeiro > Boleto > Segunda Via'). |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar árvores** | Retorna todas as estruturas de classificação configuradas. |
| **Criar árvore** | Cria uma nova hierarquia de classificação. |
| **Atualizar árvore** | Modifica a estrutura ou nome de uma árvore. |
| **Remover árvore** | Exclui uma árvore e suas classificações associadas. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/classification/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
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
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `classification-tree-controller` (10 endpoints)

### `/api/classification`

**findAll** · `operationId: findAllUsingPOST_49`

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
| 200 | OK | [PageResponse«ClassificationTree»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "children": [],
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "nodeId": 0,
      "parent": {},
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "value": "string"
    }
  ]
}
```

---

### `/api/classification/complete/{id}`

**getCompleteClassification** · `operationId: getCompleteClassificationUsingPOST`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/classification/delete`

**delete** · `operationId: deleteUsingDELETE_36`

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

### `/api/classification/save`

**insert** · `operationId: insertUsingPOST_36`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/classification/unique`

**findOne** · `operationId: findOneUsingPOST_45`

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
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/v1/classification`

**findAll** · `operationId: findAllUsingPOST_50`

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
| 200 | OK | [PageResponse«ClassificationTree»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "children": [],
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "nodeId": 0,
      "parent": {},
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "value": "string"
    }
  ]
}
```

---

### `/api/v1/classification/complete/{id}`

**getCompleteClassification** · `operationId: getCompleteClassificationUsingPOST_1`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/v1/classification/delete`

**delete** · `operationId: deleteUsingDELETE_37`

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

### `/api/v1/classification/save`

**insert** · `operationId: insertUsingPOST_37`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/v1/classification/unique`

**findOne** · `operationId: findOneUsingPOST_46`

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
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

## V2 — `classification-tree-controller-v-2` (5 endpoints)

### `/api/v2/classification`

**findAll** · `operationId: findAllUsingPOST_51`

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
| 200 | OK | [PageResponse«ClassificationTree»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "children": [],
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "nodeId": 0,
      "parent": {},
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "value": "string"
    }
  ]
}
```

---

### `/api/v2/classification/complete/{id}`

**getCompleteClassification** · `operationId: getCompleteClassificationUsingPOST_2`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/v2/classification/delete`

**delete** · `operationId: deleteUsingDELETE_38`

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

### `/api/v2/classification/save`

**insert** · `operationId: insertUsingPOST_38`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---

### `/api/v2/classification/unique`

**findOne** · `operationId: findOneUsingPOST_47`

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
| 200 | OK | [ClassificationTree](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
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
}
```

---
