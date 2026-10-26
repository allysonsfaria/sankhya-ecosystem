---
id: "42430300900759"
titulo: "Neppo Chat API — Company"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300900759-Neppo-Chat-API-Company"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:19Z"
rotulos: ["sync_hc", "neppo", "neppo_784629761", "sync_hash_1a3fd630e576"]
---

# Neppo Chat API — Company

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300900759-Neppo-Chat-API-Company#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300900759-Neppo-Chat-API-Company#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300900759-Neppo-Chat-API-Company#Referencia-tecnica-completa)
- [V1 — company-controller (8 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300900759-Neppo-Chat-API-Company#V1--company-controller-8-endpoints)
- [V2 — company-controller-v-2 (4 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430300900759-Neppo-Chat-API-Company#V2--company-controller-v-2-4-endpoints)

**O que é este módulo?**

Gerencia as empresas (tenants) cadastradas na plataforma — o nível mais alto da hierarquia multi-tenant.

| Quem usa | Administradores Neppo, times de onboarding. |
| --- | --- |
| Problema que resolve | Em uma plataforma multi-tenant, sem gerenciar empresas não é possível isolar dados, configurar limites ou criar novos clientes. |
| Impacto na experiência do cliente | Cada empresa cliente da Neppo tem seu ambiente completamente isolado e configurado conforme suas necessidades. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar empresas** | Retorna todas as empresas cadastradas na plataforma. |
| **Criar empresa** | Onboarda um novo cliente/tenant. |
| **Atualizar empresa** | Modifica dados cadastrais ou limites de uma empresa. |
| **Remover empresa** | Desativa ou remove um tenant da plataforma. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/company/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `company-controller` (8 endpoints)

### `/api/company`

**findAll** · `operationId: findAllUsingPOST_55`

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
| 200 | OK | [PageResponse«Company»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "address": "string",
      "cep": "string",
      "city": "string",
      "cnpj": "string",
      "companyName": "string",
      "complement": "string",
      "contractSignature": 0,
      "country": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "dateEndPilot": "2024-01-01T00:00:00Z",
      "defaultLocale": "string",
      "email": "string",
      "groupCompany": {
        "active": true,
        "companyName": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "id": 0,
      "nameContact": "string",
      "neighborhood": "string",
      "number": "string",
      "phoneContact": "string",
      "sgemnet": "string",
      "site": "string",
      "sku": "string",
      "state": "string",
      "stateRegistration": "string",
      "timeHistory": 0,
      "tradeName": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/company/delete`

**delete** · `operationId: deleteUsingDELETE_42`

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

### `/api/company/save`

**insert** · `operationId: insertUsingPOST_42`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/company/unique`

**findOne** · `operationId: findOneUsingPOST_51`

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
| 200 | OK | [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/company`

**findAll** · `operationId: findAllUsingPOST_56`

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
| 200 | OK | [PageResponse«Company»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "address": "string",
      "cep": "string",
      "city": "string",
      "cnpj": "string",
      "companyName": "string",
      "complement": "string",
      "contractSignature": 0,
      "country": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "dateEndPilot": "2024-01-01T00:00:00Z",
      "defaultLocale": "string",
      "email": "string",
      "groupCompany": {
        "active": true,
        "companyName": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "id": 0,
      "nameContact": "string",
      "neighborhood": "string",
      "number": "string",
      "phoneContact": "string",
      "sgemnet": "string",
      "site": "string",
      "sku": "string",
      "state": "string",
      "stateRegistration": "string",
      "timeHistory": 0,
      "tradeName": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/company/delete`

**delete** · `operationId: deleteUsingDELETE_43`

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

### `/api/v1/company/save`

**insert** · `operationId: insertUsingPOST_43`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v1/company/unique`

**findOne** · `operationId: findOneUsingPOST_52`

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
| 200 | OK | [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

## V2 — `company-controller-v-2` (4 endpoints)

### `/api/v2/company`

**findAll** · `operationId: findAllUsingPOST_57`

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
| 200 | OK | [PageResponse«Company»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "address": "string",
      "cep": "string",
      "city": "string",
      "cnpj": "string",
      "companyName": "string",
      "complement": "string",
      "contractSignature": 0,
      "country": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "dateEndPilot": "2024-01-01T00:00:00Z",
      "defaultLocale": "string",
      "email": "string",
      "groupCompany": {
        "active": true,
        "companyName": "string",
        "createdAt": "2024-01-01T00:00:00Z",
        "createdBy": "string",
        "id": 0,
        "updatedAt": "2024-01-01T00:00:00Z",
        "updatedBy": "string"
      },
      "id": 0,
      "nameContact": "string",
      "neighborhood": "string",
      "number": "string",
      "phoneContact": "string",
      "sgemnet": "string",
      "site": "string",
      "sku": "string",
      "state": "string",
      "stateRegistration": "string",
      "timeHistory": 0,
      "tradeName": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/company/delete`

**delete** · `operationId: deleteUsingDELETE_44`

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

### `/api/v2/company/save`

**insert** · `operationId: insertUsingPOST_44`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---

### `/api/v2/company/unique`

**findOne** · `operationId: findOneUsingPOST_53`

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
| 200 | OK | [Company](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "active": true,
  "address": "string",
  "cep": "string",
  "city": "string",
  "cnpj": "string",
  "companyName": "string",
  "complement": "string",
  "contractSignature": 0,
  "country": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "dateEndPilot": "2024-01-01T00:00:00Z",
  "defaultLocale": "string",
  "email": "string",
  "groupCompany": {
    "active": true,
    "companyName": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "createdBy": "string",
    "id": 0,
    "updatedAt": "2024-01-01T00:00:00Z",
    "updatedBy": "string"
  },
  "id": 0,
  "nameContact": "string",
  "neighborhood": "string",
  "number": "string",
  "phoneContact": "string",
  "sgemnet": "string",
  "site": "string",
  "sku": "string",
  "state": "string",
  "stateRegistration": "string",
  "timeHistory": 0,
  "tradeName": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string"
}
```

---
