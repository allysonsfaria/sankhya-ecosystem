---
id: "42430231461783"
titulo: "Neppo Chat API — Main"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231461783-Neppo-Chat-API-Main"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:27Z"
rotulos: ["sync_hc", "neppo", "neppo_784039938", "sync_hash_5ba18413f328"]
---

# Neppo Chat API — Main

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231461783-Neppo-Chat-API-Main#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231461783-Neppo-Chat-API-Main#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231461783-Neppo-Chat-API-Main#Referencia-tecnica-completa)
- [V1 — main-controller (1 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430231461783-Neppo-Chat-API-Main#V1--main-controller-1-endpoints)

**O que é este módulo?**

Endpoint principal de health check da API — verifica se a plataforma está operacional.

| Quem usa | Times de DevOps, monitoramento, load balancers. |
| --- | --- |
| Problema que resolve | Sem health check, não é possível monitorar automaticamente se a API está disponível ou configurar alertas de indisponibilidade. |
| Impacto na experiência do cliente | A empresa detecta problemas de disponibilidade antes que os clientes percebam, minimizando o impacto. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Health check** | Retorna o status de saúde da aplicação e suas dependências. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X GET "https://hml-chat-api.neppo.com.br/" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

**Exemplo de resposta** (`200 OK`):

```
{}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

---

## Referência técnica completa

## V1 — `main-controller` (1 endpoints)

### `/`

**main** · `operationId: mainUsingGET`

Auth: Application & Application User

**Parâmetros**

| Nome | Em | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| Authorization | header | string | Não | Bearer token |

**Respostas**

| Código | Descrição | Schema |
| --- | --- | --- |
| 200 | OK | object |
| 401 | Unauthorized | — |
| 403 | Forbidden | — |
| 404 | Not Found | — |

Exemplo de resposta (`200 OK`):

```
{}
```

---
