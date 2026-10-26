---
id: "42430254627863"
titulo: "Neppo Chat API — User Attributes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254627863-Neppo-Chat-API-User-Attributes"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:22Z"
rotulos: ["sync_hc", "neppo", "neppo_784465922", "sync_hash_ff2cfd7b6079"]
---

# Neppo Chat API — User Attributes

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254627863-Neppo-Chat-API-User-Attributes#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254627863-Neppo-Chat-API-User-Attributes#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254627863-Neppo-Chat-API-User-Attributes#Referencia-tecnica-completa)
- [V1 — user-attributes-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254627863-Neppo-Chat-API-User-Attributes#V1--user-attributes-controller-8-endpoints)
- [V2 — user-attributes-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430254627863-Neppo-Chat-API-User-Attributes#V2--user-attributes-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia os valores dos atributos customizados para cada usuário/contato.

| Quem usa | CRM, atendentes, integrações. |
| --- | --- |
| Problema que resolve | Atributos customizados sem valores associados a usuários são apenas campos vazios. Este controller preenche os campos com os dados reais de cada cliente. |
| Impacto na experiência do cliente | O atendente vê instantaneamente o CPF, contrato e segmento do cliente sem precisar consultar sistemas externos. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar atributos do usuário** | Retorna todos os valores de atributos de um contato. |
| **Salvar atributo** | Define ou atualiza o valor de um atributo para um usuário. |
| **Buscar atributo** | Consulta um atributo específico de um usuário. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/user-attributes/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `user-attributes-controller` (8 endpoints)

### `/api/user-attributes`

**findAll** · `operationId: findAllUsingPOST_103`

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
| 200 | OK | [PageResponse«UserAttributes»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "attribute": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "description": "string",
        "id": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "user": {
        "accessKey": "string",
        "active": true,
        "agent": {},
        "birthDate": "2024-01-01T00:00:00Z",
        "company": {},
        "country": "string",
        "cpf": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "createdFromSurvey": true,
        "defaultLocale": "string",
        "displayName": "string",
        "email": "string",
        "externalCode": "string",
        "firstAccess": true,
        "firstLogin": "2024-01-01T00:00:00Z",
        "formal": true,
        "id": 0,
        "lastLogin": "2024-01-01T00:00:00Z",
        "name": "string",
        "operation": "string",
        "originUser": "string",
        "phone": "string",
        "priority": 0,
        "profile": {},
        "ticketUserId": 0,
        "tm2": true,
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "userName": "string",
        "usingMFA": true,
        "visible": true,
        "password": "string"
      },
      "value": "string"
    }
  ]
}
```

---

### `/api/user-attributes/delete`

**delete** · `operationId: deleteUsingDELETE_81`

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

### `/api/user-attributes/save`

**insert** · `operationId: insertUsingPOST_81`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

---

### `/api/user-attributes/unique`

**findOne** · `operationId: findOneUsingPOST_96`

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
| 200 | OK | [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

---

### `/api/v1/user-attributes`

**findAll** · `operationId: findAllUsingPOST_104`

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
| 200 | OK | [PageResponse«UserAttributes»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "attribute": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "description": "string",
        "id": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "user": {
        "accessKey": "string",
        "active": true,
        "agent": {},
        "birthDate": "2024-01-01T00:00:00Z",
        "company": {},
        "country": "string",
        "cpf": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "createdFromSurvey": true,
        "defaultLocale": "string",
        "displayName": "string",
        "email": "string",
        "externalCode": "string",
        "firstAccess": true,
        "firstLogin": "2024-01-01T00:00:00Z",
        "formal": true,
        "id": 0,
        "lastLogin": "2024-01-01T00:00:00Z",
        "name": "string",
        "operation": "string",
        "originUser": "string",
        "phone": "string",
        "priority": 0,
        "profile": {},
        "ticketUserId": 0,
        "tm2": true,
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "userName": "string",
        "usingMFA": true,
        "visible": true,
        "password": "string"
      },
      "value": "string"
    }
  ]
}
```

---

### `/api/v1/user-attributes/delete`

**delete** · `operationId: deleteUsingDELETE_82`

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

### `/api/v1/user-attributes/save`

**insert** · `operationId: insertUsingPOST_82`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

---

### `/api/v1/user-attributes/unique`

**findOne** · `operationId: findOneUsingPOST_97`

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
| 200 | OK | [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

---

## V2 — `user-attributes-controller-v-2` (4 endpoints)

### `/api/v2/user-attributes`

**findAll** · `operationId: findAllUsingPOST_105`

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
| 200 | OK | [PageResponse«UserAttributes»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "attribute": {
        "active": true,
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "description": "string",
        "id": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "id": 0,
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string",
      "user": {
        "accessKey": "string",
        "active": true,
        "agent": {},
        "birthDate": "2024-01-01T00:00:00Z",
        "company": {},
        "country": "string",
        "cpf": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "createdFromSurvey": true,
        "defaultLocale": "string",
        "displayName": "string",
        "email": "string",
        "externalCode": "string",
        "firstAccess": true,
        "firstLogin": "2024-01-01T00:00:00Z",
        "formal": true,
        "id": 0,
        "lastLogin": "2024-01-01T00:00:00Z",
        "name": "string",
        "operation": "string",
        "originUser": "string",
        "phone": "string",
        "priority": 0,
        "profile": {},
        "ticketUserId": 0,
        "tm2": true,
        "typeUser": "string",
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string",
        "userName": "string",
        "usingMFA": true,
        "visible": true,
        "password": "string"
      },
      "value": "string"
    }
  ]
}
```

---

### `/api/v2/user-attributes/delete`

**delete** · `operationId: deleteUsingDELETE_83`

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

### `/api/v2/user-attributes/save`

**insert** · `operationId: insertUsingPOST_83`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

---

### `/api/v2/user-attributes/unique`

**findOne** · `operationId: findOneUsingPOST_98`

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
| 200 | OK | [UserAttributes](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "attribute": {
    "active": true,
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "description": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "user": {
    "accessKey": "string",
    "active": true,
    "agent": {},
    "birthDate": "2024-01-01T00:00:00Z",
    "company": {},
    "country": "string",
    "cpf": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "createdFromSurvey": true,
    "defaultLocale": "string",
    "displayName": "string",
    "email": "string",
    "externalCode": "string",
    "firstAccess": true,
    "firstLogin": "2024-01-01T00:00:00Z",
    "formal": true,
    "id": 0,
    "lastLogin": "2024-01-01T00:00:00Z",
    "name": "string",
    "operation": "string",
    "originUser": "string",
    "phone": "string",
    "priority": 0,
    "profile": {},
    "ticketUserId": 0,
    "tm2": true,
    "typeUser": "string",
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string",
    "userName": "string",
    "usingMFA": true,
    "visible": true,
    "password": "string"
  },
  "value": "string"
}
```

---
