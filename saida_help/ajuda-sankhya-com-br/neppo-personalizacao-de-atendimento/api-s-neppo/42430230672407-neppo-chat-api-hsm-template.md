---
id: "42430230672407"
titulo: "Neppo Chat API — Hsm Template"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230672407-Neppo-Chat-API-Hsm-Template"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:30Z"
rotulos: ["sync_hc", "neppo", "neppo_783613954", "sync_hash_16f883a8ba6d"]
---

# Neppo Chat API — Hsm Template

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230672407-Neppo-Chat-API-Hsm-Template#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230672407-Neppo-Chat-API-Hsm-Template#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230672407-Neppo-Chat-API-Hsm-Template#Referencia-tecnica-completa)
- [V1 — hsm-template-controller (12 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230672407-Neppo-Chat-API-Hsm-Template#V1--hsm-template-controller-12-endpoints)
- [V2 — hsm-template-controller-v-2 (6 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230672407-Neppo-Chat-API-Hsm-Template#V2--hsm-template-controller-v-2-6-endpoints)

**O que é este módulo?**

Gerencia os templates HSM (Highly Structured Messages) — mensagens pré-aprovadas pela Meta para envio ativo no WhatsApp Business.

| Quem usa | Marketing, produto, times de CX, compliance. |
| --- | --- |
| Problema que resolve | O WhatsApp só permite envio de mensagens ativas (fora da janela de 24h) com templates aprovados pela Meta. Sem gestão desses templates, a empresa não consegue fazer comunicação proativa. |
| Impacto na experiência do cliente | A empresa consegue entrar em contato com o cliente de forma estruturada e aprovada, sem risco de bloqueio do número. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar templates HSM** | Retorna todos os templates e seus status de aprovação. |
| **Criar template** | Submete um novo template para aprovação da Meta. |
| **Consultar template** | Verifica o status de aprovação e o conteúdo de um template. |
| **Remover template** | Exclui um template HSM da plataforma. |
| **Sincronizar templates** | Atualiza o status de aprovação consultando a Meta. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/hsm-template/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
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
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `hsm-template-controller` (12 endpoints)

### `/api/hsm-template`

**findAll** · `operationId: findAllUsingPOST_73`

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
| 200 | OK | [PageResponse«HsmTemplate»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "elementName": "string",
      "id": 0,
      "language": "string",
      "mediaParameterCount": 0,
      "nameSpace": "string",
      "parameterCount": 0,
      "template": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/hsm-template/delete`

**delete** · `operationId: deleteUsingDELETE_54`

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

### `/api/hsm-template/languages`

**getLanguages** · `operationId: getLanguagesUsingGET`

Returns list of available languages for HSM Template. Available in v1 and v2.

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[LanguageDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "description": "string"
}
```

---

### `/api/hsm-template/save`

**insert** · `operationId: insertUsingPOST_57`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "elementName": "string",
  "id": 0,
  "language": "string",
  "mediaParameterCount": 0,
  "nameSpace": "string",
  "parameterCount": 0,
  "template": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/hsm-template/unique`

**findOne** · `operationId: findOneUsingPOST_69`

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
| 200 | OK | [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "elementName": "string",
  "id": 0,
  "language": "string",
  "mediaParameterCount": 0,
  "nameSpace": "string",
  "parameterCount": 0,
  "template": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/hsm-template/{id}/parameters`

**findParametersById** · `operationId: findParametersByIdUsingPOST`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[HsmTemplateParam](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmId": 0,
  "id": 0,
  "paramType": "TEXT",
  "type": "HEADER"
}
```

---

### `/api/v1/hsm-template`

**findAll** · `operationId: findAllUsingPOST_74`

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
| 200 | OK | [PageResponse«HsmTemplate»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "elementName": "string",
      "id": 0,
      "language": "string",
      "mediaParameterCount": 0,
      "nameSpace": "string",
      "parameterCount": 0,
      "template": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/hsm-template/delete`

**delete** · `operationId: deleteUsingDELETE_55`

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

### `/api/v1/hsm-template/languages`

**getLanguages** · `operationId: getLanguagesUsingGET_1`

Returns list of available languages for HSM Template. Available in v1 and v2.

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[LanguageDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "description": "string"
}
```

---

### `/api/v1/hsm-template/save`

**insert** · `operationId: insertUsingPOST_58`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "elementName": "string",
  "id": 0,
  "language": "string",
  "mediaParameterCount": 0,
  "nameSpace": "string",
  "parameterCount": 0,
  "template": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/hsm-template/unique`

**findOne** · `operationId: findOneUsingPOST_70`

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
| 200 | OK | [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "elementName": "string",
  "id": 0,
  "language": "string",
  "mediaParameterCount": 0,
  "nameSpace": "string",
  "parameterCount": 0,
  "template": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/hsm-template/{id}/parameters`

**findParametersById** · `operationId: findParametersByIdUsingPOST_1`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[HsmTemplateParam](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmId": 0,
  "id": 0,
  "paramType": "TEXT",
  "type": "HEADER"
}
```

---

## V2 — `hsm-template-controller-v-2` (6 endpoints)

### `/api/v2/hsm-template`

**findAll** · `operationId: findAllUsingPOST_75`

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
| 200 | OK | [PageResponse«HsmTemplate»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "elementName": "string",
      "id": 0,
      "language": "string",
      "mediaParameterCount": 0,
      "nameSpace": "string",
      "parameterCount": 0,
      "template": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/hsm-template/delete`

**delete** · `operationId: deleteUsingDELETE_56`

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

### `/api/v2/hsm-template/languages`

**getLanguages** · `operationId: getLanguagesUsingGET_2`

Returns list of available languages for HSM Template. Available in v1 and v2.

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[LanguageDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "code": "string",
  "description": "string"
}
```

---

### `/api/v2/hsm-template/save`

**insert** · `operationId: insertUsingPOST_59`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
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
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "elementName": "string",
  "id": 0,
  "language": "string",
  "mediaParameterCount": 0,
  "nameSpace": "string",
  "parameterCount": 0,
  "template": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/hsm-template/unique`

**findOne** · `operationId: findOneUsingPOST_71`

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
| 200 | OK | [HsmTemplate](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
  "elementName": "string",
  "id": 0,
  "language": "string",
  "mediaParameterCount": 0,
  "nameSpace": "string",
  "parameterCount": 0,
  "template": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/hsm-template/{id}/parameters`

**findParametersById** · `operationId: findParametersByIdUsingPOST_2`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| id | path | integer | Sim | id |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[HsmTemplateParam](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "hsmId": 0,
  "id": 0,
  "paramType": "TEXT",
  "type": "HEADER"
}
```

---
