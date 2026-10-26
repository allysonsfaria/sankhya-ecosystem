---
id: "42430199255575"
titulo: "Neppo Chat API — Event Producer"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199255575-Neppo-Chat-API-Event-Producer"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:29Z"
rotulos: ["sync_hc", "neppo", "neppo_783908889", "sync_hash_6e49b34a6bf8"]
---

# Neppo Chat API — Event Producer

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199255575-Neppo-Chat-API-Event-Producer#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199255575-Neppo-Chat-API-Event-Producer#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199255575-Neppo-Chat-API-Event-Producer#Referencia-tecnica-completa)
- [V1 — event-producer-controller (2 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430199255575-Neppo-Chat-API-Event-Producer#V1--event-producer-controller-2-endpoints)

**O que é este módulo?**

Publica eventos em filas/tópicos de mensageria (Kafka, RabbitMQ) para integração com sistemas externos via event-driven.

| Quem usa | Times de integração, arquitetura de sistemas. |
| --- | --- |
| Problema que resolve | Integrar sistemas via polling (consultas periódicas) é ineficiente e cria latência. Eventos permitem reação em tempo real. |
| Impacto na experiência do cliente | Sistemas parceiros (ERP, CRM, BI) recebem atualizações instantâneas sobre atendimentos, sem precisar consultar a API continuamente. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Publicar evento** | Publica um evento customizado no tópico configurado. |
| **Testar publicação** | Envia um evento de teste para validar a configuração. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/event/billing" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "component": "string",
  "content": "string",
  "resource": "string",
  "duration": 0,
  "startTime": 0,
  "endTime": 0,
  "timestamp": 0,
  "extra": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

---

## Referência técnica completa

## V1 — `event-producer-controller` (2 endpoints)

### `/api/event/billing`

**billing** · `operationId: billingUsingPOST`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [BillingEventDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "component": "string",
  "content": "string",
  "resource": "string",
  "duration": 0,
  "startTime": 0,
  "endTime": 0,
  "timestamp": 0,
  "extra": "string"
}
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

### `/api/event/log`

**log** · `operationId: logUsingPOST`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [LogEventDTO](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "content": "string",
  "logLevel": "INFO",
  "timestamp": 0,
  "error": "string",
  "extra": "string"
}
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
