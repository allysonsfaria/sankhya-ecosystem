---
id: "42430301377431"
titulo: "Neppo Chat API — Hsm Template Group"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301377431-Neppo-Chat-API-Hsm-Template-Group"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:17Z"
rotulos: ["sync_hc", "neppo", "neppo_784662548", "sync_hash_8a59c58e2c5f"]
---

# Neppo Chat API — Hsm Template Group

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301377431-Neppo-Chat-API-Hsm-Template-Group#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301377431-Neppo-Chat-API-Hsm-Template-Group#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301377431-Neppo-Chat-API-Hsm-Template-Group#Referencia-tecnica-completa)
- [V1 — hsm-template-group-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301377431-Neppo-Chat-API-Hsm-Template-Group#V1--hsm-template-group-controller-8-endpoints)
- [V2 — hsm-template-group-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301377431-Neppo-Chat-API-Hsm-Template-Group#V2--hsm-template-group-controller-v-2-4-endpoints)

**O que é este módulo?**

Organiza templates HSM em grupos para facilitar o acesso e a permissão por equipe ou canal.

| Quem usa | Administradores, gestores de campanha. |
| --- | --- |
| Problema que resolve | Com muitos templates, sem organização os atendentes não encontram o template correto rapidamente, atrasando o envio. |
| Impacto na experiência do cliente | Atendentes acessam templates relevantes para seu contexto de forma rápida, agilizando a comunicação. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar grupos de templates** | Retorna todos os grupos de templates HSM. |
| **Criar grupo** | Agrupa templates relacionados com nome e descrição. |
| **Atualizar grupo** | Modifica os templates ou nome de um grupo. |
| **Remover grupo** | Exclui o agrupamento. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/hsm-template-group/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `hsm-template-group-controller` (8 endpoints)

### `/api/hsm-template-group`

**findAll** · `operationId: findAllUsingPOST_76`

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
| 200 | OK | [PageResponse«HsmTemplateGroup»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "hsmTemplate": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "description": "string",
        "elementName": "string",
        "id": 0,
        "language": "string",
        "mediaParameterCount": 0,
        "nameSpace": "string",
        "parameterCount": 0,
        "template": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "hsmTemplateGroupId": {
        "groupConfId": 0,
        "hsmTemplateId": 0
      }
    }
  ]
}
```

---

### `/api/hsm-template-group/delete`

**delete** · `operationId: deleteUsingDELETE_57`

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

### `/api/hsm-template-group/save`

**insert** · `operationId: insertUsingPOST_60`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

---

### `/api/hsm-template-group/unique`

**findOne** · `operationId: findOneUsingPOST_72`

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
| 200 | OK | [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

---

### `/api/v1/hsm-template-group`

**findAll** · `operationId: findAllUsingPOST_77`

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
| 200 | OK | [PageResponse«HsmTemplateGroup»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "hsmTemplate": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "description": "string",
        "elementName": "string",
        "id": 0,
        "language": "string",
        "mediaParameterCount": 0,
        "nameSpace": "string",
        "parameterCount": 0,
        "template": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "hsmTemplateGroupId": {
        "groupConfId": 0,
        "hsmTemplateId": 0
      }
    }
  ]
}
```

---

### `/api/v1/hsm-template-group/delete`

**delete** · `operationId: deleteUsingDELETE_58`

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

### `/api/v1/hsm-template-group/save`

**insert** · `operationId: insertUsingPOST_61`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

---

### `/api/v1/hsm-template-group/unique`

**findOne** · `operationId: findOneUsingPOST_73`

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
| 200 | OK | [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

---

## V2 — `hsm-template-group-controller-v-2` (4 endpoints)

### `/api/v2/hsm-template-group`

**findAll** · `operationId: findAllUsingPOST_78`

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
| 200 | OK | [PageResponse«HsmTemplateGroup»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "hsmTemplate": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "description": "string",
        "elementName": "string",
        "id": 0,
        "language": "string",
        "mediaParameterCount": 0,
        "nameSpace": "string",
        "parameterCount": 0,
        "template": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "hsmTemplateGroupId": {
        "groupConfId": 0,
        "hsmTemplateId": 0
      }
    }
  ]
}
```

---

### `/api/v2/hsm-template-group/delete`

**delete** · `operationId: deleteUsingDELETE_59`

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

### `/api/v2/hsm-template-group/save`

**insert** · `operationId: insertUsingPOST_62`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

---

### `/api/v2/hsm-template-group/unique`

**findOne** · `operationId: findOneUsingPOST_74`

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
| 200 | OK | [HsmTemplateGroup](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmTemplate": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "elementName": "string",
    "id": 0,
    "language": "string",
    "mediaParameterCount": 0,
    "nameSpace": "string",
    "parameterCount": 0,
    "template": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "hsmTemplateGroupId": {
    "groupConfId": 0,
    "hsmTemplateId": 0
  }
}
```

---
