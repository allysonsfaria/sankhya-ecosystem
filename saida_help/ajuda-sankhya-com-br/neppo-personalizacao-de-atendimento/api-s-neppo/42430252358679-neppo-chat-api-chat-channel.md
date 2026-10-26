---
id: "42430252358679"
titulo: "Neppo Chat API — Chat Channel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430252358679-Neppo-Chat-API-Chat-Channel"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:32Z"
rotulos: ["sync_hc", "neppo", "neppo_783515651", "sync_hash_9eea73f744f8"]
---

# Neppo Chat API — Chat Channel

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430252358679-Neppo-Chat-API-Chat-Channel#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430252358679-Neppo-Chat-API-Chat-Channel#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430252358679-Neppo-Chat-API-Chat-Channel#Referencia-tecnica-completa)
- [V1 — chat-channel-controller (6 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430252358679-Neppo-Chat-API-Chat-Channel#V1--chat-channel-controller-6-endpoints)
- [V2 — chat-channel-controller-v-2 (3 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430252358679-Neppo-Chat-API-Chat-Channel#V2--chat-channel-controller-v-2-3-endpoints)

**O que é este módulo?**

Gerencia os canais de atendimento (WhatsApp, Instagram, chat web, SMS, e-mail) conectados à plataforma.

| Quem usa | Administradores de TI, times de produto, integrações. |
| --- | --- |
| Problema que resolve | Sem gerenciar canais, não é possível adicionar novos pontos de contato com clientes nem monitorar o status das integrações. |
| Impacto na experiência do cliente | Clientes podem ser atendidos no canal de sua preferência, sem precisar mudar de plataforma. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar canais** | Retorna todos os canais configurados e seus status de conexão. |
| **Criar canal** | Integra um novo canal (número de WhatsApp, página do Instagram etc.). |
| **Consultar canal** | Verifica configurações e status de um canal específico. |
| **Remover canal** | Desconecta e remove um canal da plataforma. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/channel/unique" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "conditions": [
    {
      "key": "id",
      "value": "42",
      "operator": "EQNUM"
    }
  ]
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `chat-channel-controller` (6 endpoints)

### `/api/channel`

**findAll** · `operationId: findAllUsingPOST_31`

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
| 200 | OK | [PageResponse«ChatChannel»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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

### `/api/channel/active`

**findAllActive** · `operationId: findAllActiveUsingGET`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[ChatChannel](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

---

### `/api/channel/unique`

**findOne** · `operationId: findOneUsingPOST_27`

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
| 200 | OK | [ChatChannel](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

---

### `/api/v1/channel`

**findAll** · `operationId: findAllUsingPOST_32`

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
| 200 | OK | [PageResponse«ChatChannel»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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

### `/api/v1/channel/active`

**findAllActive** · `operationId: findAllActiveUsingGET_1`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[ChatChannel](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

---

### `/api/v1/channel/unique`

**findOne** · `operationId: findOneUsingPOST_28`

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
| 200 | OK | [ChatChannel](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

---

## V2 — `chat-channel-controller-v-2` (3 endpoints)

### `/api/v2/channel`

**findAll** · `operationId: findAllUsingPOST_33`

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
| 200 | OK | [PageResponse«ChatChannel»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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

### `/api/v2/channel/active`

**findAllActive** · `operationId: findAllActiveUsingGET_2`

Auth: Application & Application User | Escopos: `read`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | array<[ChatChannel](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)> |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

---

### `/api/v2/channel/unique`

**findOne** · `operationId: findOneUsingPOST_29`

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
| 200 | OK | [ChatChannel](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "id": 0,
  "name": "string"
}
```

---
