---
id: "42430230543895"
titulo: "Neppo Chat API — Campaign"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:31Z"
rotulos: ["sync_hc", "neppo", "neppo_783581186", "sync_hash_7d6d3112daa0"]
---

# Neppo Chat API — Campaign

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign#Referencia-tecnica-completa)
- [V1 — campaign-controller (6 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign#V1--campaign-controller-6-endpoints)
- [V2 — campaign-controller-v-2 (3 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign#V2--campaign-controller-v-2-3-endpoints)
- [V3 — campaign-controller-v-3 (3 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230543895-Neppo-Chat-API-Campaign#V3--campaign-controller-v-3-3-endpoints)

**O que é este módulo?**

Gerencia campanhas de comunicação ativa para grupos de contatos via WhatsApp, SMS ou outros canais.

| Quem usa | Marketing, vendas, times de CX (Customer Experience). |
| --- | --- |
| Problema que resolve | Sem campanhas, a empresa fica restrita a comunicação reativa — apenas responde, nunca inicia a conversa com o cliente de forma organizada. |
| Impacto na experiência do cliente | Clientes recebem comunicações relevantes no momento certo (promoções, lembretes de vencimento, pesquisas), aumentando o engajamento. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar campanhas** | Retorna todas as campanhas criadas, com status de execução. |
| **Criar campanha** | Configura uma nova campanha com público-alvo, canal e mensagem. |
| **Consultar campanha** | Verifica os dados e métricas de uma campanha específica. |
| **Remover campanha** | Cancela e remove uma campanha. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/campaign/execute" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "campaignId": 0,
  "data": [
    {}
  ]
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

## Referência técnica completa

## V1 — `campaign-controller` (6 endpoints)

### `/api/campaign`

**findAll** · `operationId: findAllUsingPOST_18`

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
| 200 | OK | [PageResponse«Campaign»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "defaultSendGroupId": 0,
      "description": "string",
      "expiration": "2024-01-01T00:00:00Z",
      "hasAttachment": true,
      "hsm": true,
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
      "hsmTemplateId": 0,
      "id": 0,
      "jolt": "string",
      "name": "string",
      "status": "string",
      "templateId": 0,
      "title": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/campaign/execute`

**execute** · `operationId: executeUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignExecuteRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "campaignId": 0,
  "data": [
    {}
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignExecuteResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string"
}
```

---

### `/api/campaign/execute/status`

**execute/status** · `operationId: executeStatusUsingPOST`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignStatusRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "executionId": 0,
  "campaignId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignStatusResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string",
  "statusMessages": [
    {
      "id": 0,
      "message": "string",
      "recipient": "string",
      "recipientId": "string",
      "status": "string"
    }
  ]
}
```

---

### `/api/v1/campaign`

**findAll** · `operationId: findAllUsingPOST_19`

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
| 200 | OK | [PageResponse«Campaign»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "defaultSendGroupId": 0,
      "description": "string",
      "expiration": "2024-01-01T00:00:00Z",
      "hasAttachment": true,
      "hsm": true,
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
      "hsmTemplateId": 0,
      "id": 0,
      "jolt": "string",
      "name": "string",
      "status": "string",
      "templateId": 0,
      "title": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v1/campaign/execute`

**execute** · `operationId: executeUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignExecuteRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "campaignId": 0,
  "data": [
    {}
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignExecuteResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string"
}
```

---

### `/api/v1/campaign/execute/status`

**execute/status** · `operationId: executeStatusUsingPOST_1`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignStatusRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "executionId": 0,
  "campaignId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignStatusResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string",
  "statusMessages": [
    {
      "id": 0,
      "message": "string",
      "recipient": "string",
      "recipientId": "string",
      "status": "string"
    }
  ]
}
```

---

## V2 — `campaign-controller-v-2` (3 endpoints)

### `/api/v2/campaign`

**findAll** · `operationId: findAllUsingPOST_20`

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
| 200 | OK | [PageResponse«Campaign»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "defaultSendGroupId": 0,
      "description": "string",
      "expiration": "2024-01-01T00:00:00Z",
      "hasAttachment": true,
      "hsm": true,
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
      "hsmTemplateId": 0,
      "id": 0,
      "jolt": "string",
      "name": "string",
      "status": "string",
      "templateId": 0,
      "title": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v2/campaign/execute`

**execute** · `operationId: executeUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignExecuteRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "campaignId": 0,
  "data": [
    {}
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignExecuteResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string"
}
```

---

### `/api/v2/campaign/execute/status`

**execute/status** · `operationId: executeStatusUsingPOST_2`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignStatusRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "executionId": 0,
  "campaignId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignStatusResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string",
  "statusMessages": [
    {
      "id": 0,
      "message": "string",
      "recipient": "string",
      "recipientId": "string",
      "status": "string"
    }
  ]
}
```

---

## V3 — `campaign-controller-v-3` (3 endpoints)

### `/api/v3/campaign`

**findAll** · `operationId: findAllUsingPOST_21`

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
| 200 | OK | [PageResponse«CampaignConfig»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "campaignTypeId": 0,
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "emailBody": "string",
      "emailSubject": "string",
      "executionType": "string",
      "expiresAt": "2024-01-01T00:00:00Z",
      "groupConfId": 0,
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
      "id": 0,
      "jolt": "string",
      "message": "string",
      "name": "string",
      "nextRun": "2024-01-01T00:00:00Z",
      "recurrenceFrequency": "string",
      "responsibleUserId": 0,
      "scheduledAt": "2024-01-01T00:00:00Z",
      "sourceReference": "string",
      "sourceType": "string",
      "status": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
      "updatedBy": "string"
    }
  ]
}
```

---

### `/api/v3/campaign/execute`

**execute** · `operationId: executeUsingPOST_3`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignExecuteRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "campaignId": 0,
  "data": [
    {}
  ]
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignExecuteResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string"
}
```

---

### `/api/v3/campaign/execute/status`

**execute/status** · `operationId: executeStatusUsingPOST_3`

Auth: Application & Application User | Escopos: `write`

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [CampaignStatusRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "executionId": 0,
  "campaignId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [CampaignStatusResponse](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "campaignId": 0,
  "executionId": 0,
  "message": "string",
  "status": "string",
  "statusMessages": [
    {
      "id": 0,
      "message": "string",
      "recipient": "string",
      "recipientId": "string",
      "status": "string"
    }
  ]
}
```

---
