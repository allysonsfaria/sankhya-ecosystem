---
id: "42430246459415"
titulo: "Neppo Chat API — Batch"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246459415-Neppo-Chat-API-Batch"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:27Z"
rotulos: ["sync_hc", "neppo", "neppo_784072710", "sync_hash_393c3c2b3e2d"]
---

# Neppo Chat API — Batch

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246459415-Neppo-Chat-API-Batch#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246459415-Neppo-Chat-API-Batch#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246459415-Neppo-Chat-API-Batch#Referencia-tecnica-completa)
- [V1 — batch-controller (2 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246459415-Neppo-Chat-API-Batch#V1--batch-controller-2-endpoints)
- [V2 — batch-controller-v-2 (1 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430246459415-Neppo-Chat-API-Batch#V2--batch-controller-v-2-1-endpoints)

**O que é este módulo?**

Permite executar operações em massa, como envio de mensagens para múltiplos contatos simultaneamente.

| Quem usa | Marketing, equipes de CRM, operações de engajamento proativo. |
| --- | --- |
| Problema que resolve | Enviar mensagens individualmente para milhares de contatos é inviável manualmente e caro em termos de tempo operacional. |
| Impacto na experiência do cliente | Permite que a empresa alcance clientes em momentos estratégicos (renovações, alertas, promoções) de forma eficiente e escalável. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Criar lote** | Inicia um processamento em lote com lista de contatos e mensagem. |
| **Consultar status** | Verifica o andamento e resultados do processamento em lote. |
| **Cancelar lote** | Interrompe um processamento em lote em execução. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/batch/client" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "requestId": "string",
    "client": {
      "displayName": "string",
      "channels": [],
      "phones": [],
      "emails": [],
      "cpfCnpj": "string",
      "birthDate": "string",
      "active": true,
      "externalCode": "string",
      "attributes": [],
      "agentIds": [],
      "channelsIdentifiers": {}
    }
  }
]'
```

**Exemplo de resposta** (`200 OK`):

```
{}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

---

## Referência técnica completa

## V1 — `batch-controller` (2 endpoints)

### `/api/batch/client`

**batchClient** · `operationId: batchClientUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): array<[RequestClientDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)>

Exemplo de corpo:

```
[
  {
    "requestId": "string",
    "client": {
      "displayName": "string",
      "channels": [],
      "phones": [],
      "emails": [],
      "cpfCnpj": "string",
      "birthDate": "string",
      "active": true,
      "externalCode": "string",
      "attributes": [],
      "agentIds": [],
      "channelsIdentifiers": {}
    }
  }
]
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---

### `/api/v1/batch/client`

**batchClient** · `operationId: batchClientUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): array<[RequestClientDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)>

Exemplo de corpo:

```
[
  {
    "requestId": "string",
    "client": {
      "displayName": "string",
      "channels": [],
      "phones": [],
      "emails": [],
      "cpfCnpj": "string",
      "birthDate": "string",
      "active": true,
      "externalCode": "string",
      "attributes": [],
      "agentIds": [],
      "channelsIdentifiers": {}
    }
  }
]
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---

## V2 — `batch-controller-v-2` (1 endpoints)

### `/api/v2/batch/client`

**batchClient** · `operationId: batchClientUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): array<[RequestClientDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)>

Exemplo de corpo:

```
[
  {
    "requestId": "string",
    "client": {
      "displayName": "string",
      "channels": [],
      "phones": [],
      "emails": [],
      "cpfCnpj": "string",
      "birthDate": "string",
      "active": true,
      "externalCode": "string",
      "attributes": [],
      "agentIds": [],
      "channelsIdentifiers": {}
    }
  }
]
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---
