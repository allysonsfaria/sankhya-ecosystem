---
id: "42430243972503"
titulo: "Neppo Chat API — Chat Embedded Integration"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243972503-Neppo-Chat-API-Chat-Embedded-Integration"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:37Z"
rotulos: ["sync_hc", "neppo", "neppo_783089666", "sync_hash_cdbf932f155f"]
---

# Neppo Chat API — Chat Embedded Integration

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243972503-Neppo-Chat-API-Chat-Embedded-Integration#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243972503-Neppo-Chat-API-Chat-Embedded-Integration#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243972503-Neppo-Chat-API-Chat-Embedded-Integration#Referencia-tecnica-completa)
- [V1 — chat-embedded-integration-controller (3 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430243972503-Neppo-Chat-API-Chat-Embedded-Integration#V1--chat-embedded-integration-controller-3-endpoints)

**O que é este módulo?**

Gerencia a integração do chat embarcado (widget) em sites e aplicações web dos clientes.

| Quem usa | Times de desenvolvimento, produto, marketing digital. |
| --- | --- |
| Problema que resolve | Sem chat embarcado, o cliente precisa sair do site para entrar em contato, aumentando a fricção e a taxa de abandono. |
| Impacto na experiência do cliente | O cliente inicia uma conversa diretamente no site da empresa, sem interrupção da jornada de compra ou suporte. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar integrações** | Retorna os widgets de chat configurados. |
| **Criar integração** | Gera um novo widget com configurações de cor, posição e canal. |
| **Consultar integração** | Obtém o código de embed e configurações de um widget. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v2/chat-embedded-integration" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "accountKey": "string",
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "url": "string"
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "accountKey": "string",
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "url": "string"
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

---

## Referência técnica completa

## V1 — `chat-embedded-integration-controller` (3 endpoints)

### `/api/v2/chat-embedded-integration`

**save** · `operationId: saveUsingPOST`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatEmbeddedIntegration](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "accountKey": "string",
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "url": "string"
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatEmbeddedIntegration](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accountKey": "string",
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "url": "string"
}
```

---

### `/api/v2/chat-embedded-integration/{name}`

**findByName** · `operationId: findByNameUsingGET`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| name | path | string | Sim | name |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatEmbeddedIntegration](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "accountKey": "string",
  "active": true,
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "id": 0,
  "name": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
  "updatedBy": "string",
  "url": "string"
}
```

---

### `/api/v2/chat-embedded-integration/{name}/status`

**updateStatus** · `operationId: updateStatusUsingPUT`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |
| name | path | string | Sim | name |

**Request body** (obrigatório): [UpdateStatusRequest](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "active": true
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | — |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

---
