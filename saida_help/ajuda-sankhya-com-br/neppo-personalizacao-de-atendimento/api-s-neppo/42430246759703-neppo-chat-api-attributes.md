---
id: "42430246759703"
titulo: "Neppo Chat API — Attributes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246759703-Neppo-Chat-API-Attributes"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:25Z"
rotulos: ["sync_hc", "neppo", "neppo_784203786", "sync_hash_71692c1f76f2"]
---

# Neppo Chat API — Attributes

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246759703-Neppo-Chat-API-Attributes#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246759703-Neppo-Chat-API-Attributes#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246759703-Neppo-Chat-API-Attributes#Referencia-tecnica-completa)
- [V1 — attributes-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246759703-Neppo-Chat-API-Attributes#V1--attributes-controller-8-endpoints)
- [V2 — attributes-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246759703-Neppo-Chat-API-Attributes#V2--attributes-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia atributos customizados que podem ser criados para enriquecer informações de contatos e atendimentos.

| Quem usa | Administradores, equipes de CRM, integrações com sistemas externos. |
| --- | --- |
| Problema que resolve | Cada empresa tem campos específicos de negócio (CPF, código de contrato, segmento). Sem atributos customizados, essas informações ficam perdidas fora da plataforma. |
| Impacto na experiência do cliente | Atendentes têm acesso imediato a informações relevantes do cliente durante o atendimento, sem precisar consultar outros sistemas. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar atributos** | Retorna todos os atributos customizados configurados. |
| **Criar atributo** | Cria um novo campo personalizado (texto, número, data, lista). |
| **Atualizar atributo** | Modifica nome, tipo ou opções de um atributo existente. |
| **Remover atributo** | Exclui um atributo e seus dados associados. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/attributes/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `attributes-controller` (8 endpoints)

### `/api/attributes`

**findAll** · `operationId: findAllUsingPOST_9`

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
| 200 | OK | [PageResponse«Attributes»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "id": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/attributes/delete`

**delete** · `operationId: deleteUsingDELETE_6`

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

### `/api/attributes/save`

**insert** · `operationId: insertUsingPOST_6`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/attributes/unique`

**findOne** · `operationId: findOneUsingPOST_9`

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
| 200 | OK | [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/attributes`

**findAll** · `operationId: findAllUsingPOST_10`

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
| 200 | OK | [PageResponse«Attributes»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "id": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/attributes/delete`

**delete** · `operationId: deleteUsingDELETE_7`

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

### `/api/v1/attributes/save`

**insert** · `operationId: insertUsingPOST_7`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/attributes/unique`

**findOne** · `operationId: findOneUsingPOST_10`

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
| 200 | OK | [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `attributes-controller-v-2` (4 endpoints)

### `/api/v2/attributes`

**findAll** · `operationId: findAllUsingPOST_11`

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
| 200 | OK | [PageResponse«Attributes»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "id": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/attributes/delete`

**delete** · `operationId: deleteUsingDELETE_8`

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

### `/api/v2/attributes/save`

**insert** · `operationId: insertUsingPOST_8`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/attributes/unique`

**findOne** · `operationId: findOneUsingPOST_11`

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
| 200 | OK | [Attributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
