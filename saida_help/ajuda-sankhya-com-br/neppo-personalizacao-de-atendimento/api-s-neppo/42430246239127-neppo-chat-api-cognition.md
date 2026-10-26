---
id: "42430246239127"
titulo: "Neppo Chat API — Cognition"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246239127-Neppo-Chat-API-Cognition"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:28Z"
rotulos: ["sync_hc", "neppo", "neppo_783941644", "sync_hash_d8c5c7e5893d"]
---

# Neppo Chat API — Cognition

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246239127-Neppo-Chat-API-Cognition#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246239127-Neppo-Chat-API-Cognition#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246239127-Neppo-Chat-API-Cognition#Referencia-tecnica-completa)
- [V1 — cognition-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246239127-Neppo-Chat-API-Cognition#V1--cognition-controller-8-endpoints)
- [V2 — cognition-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246239127-Neppo-Chat-API-Cognition#V2--cognition-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia as configurações de IA cognitiva da plataforma — modelos de NLP, intenções e entidades para compreensão de linguagem natural.

| Quem usa | Times de IA, produto, analistas de automação. |
| --- | --- |
| Problema que resolve | Sem cognição configurada, os bots só entendem comandos exatos, falhando quando o cliente usa linguagem natural ou variações. |
| Impacto na experiência do cliente | O bot entende o que o cliente quis dizer, mesmo com erros de digitação ou linguagem informal, criando uma experiência muito mais natural. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar configurações de cognição** | Retorna os modelos de NLP configurados. |
| **Criar/atualizar cognição** | Configura um novo modelo com intenções e exemplos de frases. |
| **Buscar cognição** | Consulta as configurações de um modelo específico. |
| **Remover cognição** | Exclui uma configuração de NLP. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/cognition/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `cognition-controller` (8 endpoints)

### `/api/cognition`

**findAll** · `operationId: findAllUsingPOST_52`

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
| 200 | OK | [PageResponse«Cognition»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "appId": "string",
      "appKey": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "endPoint": "string",
      "id": 0,
      "name": "string",
      "password": "string",
      "type": "string",
      "userName": "string",
      "version": "string"
    }
  ]
}
```

---

### `/api/cognition/delete`

**delete** · `operationId: deleteUsingDELETE_39`

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

### `/api/cognition/save`

**insert** · `operationId: insertUsingPOST_39`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

---

### `/api/cognition/unique`

**findOne** · `operationId: findOneUsingPOST_48`

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
| 200 | OK | [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

---

### `/api/v1/cognition`

**findAll** · `operationId: findAllUsingPOST_53`

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
| 200 | OK | [PageResponse«Cognition»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "appId": "string",
      "appKey": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "endPoint": "string",
      "id": 0,
      "name": "string",
      "password": "string",
      "type": "string",
      "userName": "string",
      "version": "string"
    }
  ]
}
```

---

### `/api/v1/cognition/delete`

**delete** · `operationId: deleteUsingDELETE_40`

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

### `/api/v1/cognition/save`

**insert** · `operationId: insertUsingPOST_40`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

---

### `/api/v1/cognition/unique`

**findOne** · `operationId: findOneUsingPOST_49`

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
| 200 | OK | [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

---

## V2 — `cognition-controller-v-2` (4 endpoints)

### `/api/v2/cognition`

**findAll** · `operationId: findAllUsingPOST_54`

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
| 200 | OK | [PageResponse«Cognition»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "appId": "string",
      "appKey": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "endPoint": "string",
      "id": 0,
      "name": "string",
      "password": "string",
      "type": "string",
      "userName": "string",
      "version": "string"
    }
  ]
}
```

---

### `/api/v2/cognition/delete`

**delete** · `operationId: deleteUsingDELETE_41`

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

### `/api/v2/cognition/save`

**insert** · `operationId: insertUsingPOST_41`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

---

### `/api/v2/cognition/unique`

**findOne** · `operationId: findOneUsingPOST_50`

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
| 200 | OK | [Cognition](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "appId": "string",
  "appKey": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "endPoint": "string",
  "id": 0,
  "name": "string",
  "password": "string",
  "type": "string",
  "userName": "string",
  "version": "string"
}
```

---
