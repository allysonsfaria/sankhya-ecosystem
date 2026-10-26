---
id: "42430253037207"
titulo: "Neppo Chat API — Direct Message"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430253037207-Neppo-Chat-API-Direct-Message"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:29Z"
rotulos: ["sync_hc", "neppo", "neppo_783843353", "sync_hash_57453a93cc4b"]
---

# Neppo Chat API — Direct Message

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430253037207-Neppo-Chat-API-Direct-Message#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430253037207-Neppo-Chat-API-Direct-Message#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430253037207-Neppo-Chat-API-Direct-Message#Referencia-tecnica-completa)
- [V1 — direct-message-controller (6 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430253037207-Neppo-Chat-API-Direct-Message#V1--direct-message-controller-6-endpoints)
- [V2 — direct-message-controller-v-2 (3 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430253037207-Neppo-Chat-API-Direct-Message#V2--direct-message-controller-v-2-3-endpoints)

**O que é este módulo?**

Gerencia mensagens diretas entre usuários internos da plataforma (atendentes, supervisores) sem envolver o cliente.

| Quem usa | Atendentes, supervisores, equipes de suporte interno. |
| --- | --- |
| Problema que resolve | Sem comunicação interna, os atendentes precisam usar ferramentas externas (WhatsApp pessoal, Slack) para se consultar, perdendo contexto. |
| Impacto na experiência do cliente | O atendente resolve dúvidas internamente com mais agilidade, resultando em um atendimento mais rápido ao cliente final. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Listar conversas** | Retorna as conversas de mensagem direta do usuário logado. |
| **Enviar mensagem** | Envia uma mensagem direta para outro usuário da plataforma. |
| **Marcar como lida** | Atualiza o status de leitura das mensagens. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/direct-message/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}'
```

**Exemplo de resposta** (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

Endpoints de listagem (`findAll`) e busca (`findOne`) deste módulo recebem um corpo com **filtros (conditions)** e **paginação**. Veja como montar o corpo de busca no guia: [Neppo Chat API — Guia de Busca, Filtros e Paginação](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711).

---

**Envio ativo / Disparos** — como montar a requisição

O envio ativo (disparo proativo de mensagem para um contato, fora de uma sessão já existente) é feito via `POST /api/v1/direct-message/save` usando o modelo **ChatDirectMessage** no corpo da requisição. Para envios no WhatsApp fora da janela de 24h, é obrigatório usar um **template HSM aprovado** (campo `hsmTemplate`).

**Campos mais usados no disparo** (todos os campos do modelo `ChatDirectMessage` são opcionais no schema; abaixo os relevantes para um disparo típico):

| Campo | Tipo | Para que serve no disparo |
| --- | --- | --- |
| `phoneNumber` | string | Número do destinatário (formato E.164, ex. +5511...). |
| `channel` | string | Canal do envio (ex. `WHATSAPP`). |
| `hsmTemplate` | integer | ID do template HSM aprovado (obrigatório p/ WhatsApp ativo fora da janela de 24h). |
| `message` | string | Texto da mensagem (quando aplicável ao canal/sessão aberta). |
| `campaignName` | string | Identificador da campanha para rastreio/relatórios. |
| `groupConfId` | integer | Configuração de grupo que receberá/atenderá o retorno. |
| `senderUserId` | integer | Usuário/atendente responsável pelo disparo. |
| `recipientId` | string | Identificador do contato destinatário na plataforma. |
| `additionalInfo` | string | Dados extras (ex. variáveis do template) em JSON serializado. |

[VERIFICAR: confirmar quais campos o backend exige como obrigatórios para o disparo — o schema marca todos como opcionais, mas na prática um disparo válido normalmente exige destinatário (phoneNumber/recipientId), channel e, no WhatsApp ativo, hsmTemplate.]

**Exemplo de corpo (request body) — ChatDirectMessage**:

```
{
  "phoneNumber": "+5511999998888",
  "channel": "WHATSAPP",
  "hsmTemplate": 10,
  "message": "Olá João! Sua fatura de março vence em 10/04. Acesse: https://app.empresa.com/fatura",
  "campaignName": "cobranca_marco_2024",
  "groupConfId": 3,
  "senderUserId": 42,
  "recipientId": "1001",
  "additionalInfo": "{\"variaveis\":{\"nome\":\"João\",\"vencimento\":\"10/04\"}}"
}
```

**Exemplo de chamada**:

```
curl -X POST "https://hml-chat-api.neppo.com.br/api/v1/direct-message/save" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d @body.json
```

**Exemplo de resposta** (`200 OK`):

```
{
  "id": 98765,
  "dispatchId": 55012,
  "status": "QUEUED",
  "phoneNumber": "+5511999998888",
  "channel": "WHATSAPP",
  "campaignName": "cobranca_marco_2024",
  "sentAt": null,
  "createdAt": "2024-03-25T14:30:00Z"
}
```

---

## Referência técnica completa

## V1 — `direct-message-controller` (6 endpoints)

### `/api/direct-message`

**findAll** · `operationId: findAllUsingPOST_58`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«ChatDirectMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "additionalInfo": "string",
      "agentId": 0,
      "broadcastListId": 0,
      "callback": "string",
      "campaignName": "string",
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "dispatchId": 0,
      "email": "string",
      "executionId": 0,
      "generatedSession": true,
      "groupConfId": 0,
      "groupName": "string",
      "hsmTemplate": 0,
      "id": 0,
      "message": "string",
      "phoneNumber": "string",
      "recipientId": "string",
      "resend": true,
      "sendGroupConfId": 0,
      "sendTimestamp": "string",
      "senderUserId": 0,
      "sentAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "status": "string",
      "subject": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
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
      "userId": 0
    }
  ]
}
```

---

### `/api/direct-message/save`

**insert** · `operationId: insertUsingPOST_45`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

---

### `/api/direct-message/unique`

**findOne** · `operationId: findOneUsingPOST_54`

Auth: Application & Application User

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
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

---

### `/api/v1/direct-message`

**findAll** · `operationId: findAllUsingPOST_59`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«ChatDirectMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "additionalInfo": "string",
      "agentId": 0,
      "broadcastListId": 0,
      "callback": "string",
      "campaignName": "string",
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "dispatchId": 0,
      "email": "string",
      "executionId": 0,
      "generatedSession": true,
      "groupConfId": 0,
      "groupName": "string",
      "hsmTemplate": 0,
      "id": 0,
      "message": "string",
      "phoneNumber": "string",
      "recipientId": "string",
      "resend": true,
      "sendGroupConfId": 0,
      "sendTimestamp": "string",
      "senderUserId": 0,
      "sentAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "status": "string",
      "subject": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
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
      "userId": 0
    }
  ]
}
```

---

### `/api/v1/direct-message/save`

**insert** · `operationId: insertUsingPOST_46`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

---

### `/api/v1/direct-message/unique`

**findOne** · `operationId: findOneUsingPOST_55`

Auth: Application & Application User

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
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

---

## V2 — `direct-message-controller-v-2` (3 endpoints)

### `/api/v2/direct-message`

**findAll** · `operationId: findAllUsingPOST_60`

Auth: Application & Application User

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
| 200 | OK | [PageResponse«ChatDirectMessage»](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
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
      "additionalInfo": "string",
      "agentId": 0,
      "broadcastListId": 0,
      "callback": "string",
      "campaignName": "string",
      "channel": "string",
      "createdAt": "2024-01-01T00:00:00Z",
      "createdBy": "string",
      "description": "string",
      "dispatchId": 0,
      "email": "string",
      "executionId": 0,
      "generatedSession": true,
      "groupConfId": 0,
      "groupName": "string",
      "hsmTemplate": 0,
      "id": 0,
      "message": "string",
      "phoneNumber": "string",
      "recipientId": "string",
      "resend": true,
      "sendGroupConfId": 0,
      "sendTimestamp": "string",
      "senderUserId": 0,
      "sentAt": "2024-01-01T00:00:00Z",
      "sessionId": 0,
      "status": "string",
      "subject": "string",
      "updatedAt": "2024-01-01T00:00:00Z",
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
      "userId": 0
    }
  ]
}
```

---

### `/api/v2/direct-message/save`

**insert** · `operationId: insertUsingPOST_47`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Request body** (obrigatório): [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

Exemplo de corpo:

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

---

### `/api/v2/direct-message/unique`

**findOne** · `operationId: findOneUsingPOST_56`

Auth: Application & Application User

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
| 200 | OK | [ChatDirectMessage](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x) |
| 201 | Created | — |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{
  "additionalInfo": "string",
  "agentId": 0,
  "broadcastListId": 0,
  "callback": "string",
  "campaignName": "string",
  "channel": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "createdBy": "string",
  "description": "string",
  "dispatchId": 0,
  "email": "string",
  "executionId": 0,
  "generatedSession": true,
  "groupConfId": 0,
  "groupName": "string",
  "hsmTemplate": 0,
  "id": 0,
  "message": "string",
  "phoneNumber": "string",
  "recipientId": "string",
  "resend": true,
  "sendGroupConfId": 0,
  "sendTimestamp": "string",
  "senderUserId": 0,
  "sentAt": "2024-01-01T00:00:00Z",
  "sessionId": 0,
  "status": "string",
  "subject": "string",
  "updatedAt": "2024-01-01T00:00:00Z",
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
  "userId": 0
}
```

---
