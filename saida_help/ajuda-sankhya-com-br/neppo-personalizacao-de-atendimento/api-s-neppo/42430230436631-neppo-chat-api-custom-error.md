---
id: "42430230436631"
titulo: "Neppo Chat API — Custom Error"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230436631-Neppo-Chat-API-Custom-Error"
trilha: "NEPPO: Personalização de atendimento > API's Neppo"
atualizado_em: "2026-08-11T16:13:31Z"
rotulos: ["sync_hc", "neppo", "neppo_783515689", "sync_hash_5518e3b0cac6"]
---

# Neppo Chat API — Custom Error

**📘 Documentação Neppo Chat API**  |  [🏠 Visão Geral (índice)](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/783253512/x)  ·  [🔎 Guia de Busca](https://sankhya.zendesk.com/hc/pt-br/articles/42430243874711)  ·  [📦 Modelos de Dados](https://neppo-team.atlassian.net/wiki/spaces/neppo/pages/784367627/x)

- [O que você pode fazer com este módulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230436631-Neppo-Chat-API-Custom-Error#O-que-voce-pode-fazer-com-este-modulo)
- [Exemplo de chamada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230436631-Neppo-Chat-API-Custom-Error#Exemplo-de-chamada)
- [Referência técnica completa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230436631-Neppo-Chat-API-Custom-Error#Referencia-tecnica-completa)
- [V1 — custom-error-controller (1 endpoints)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430230436631-Neppo-Chat-API-Custom-Error#V1--custom-error-controller-1-endpoints)

**O que é este módulo?**

Retorna detalhes de erros customizados da plataforma para facilitar diagnóstico de integrações.

| Quem usa | Desenvolvedores, times de integração. |
| --- | --- |
| Problema que resolve | Erros HTTP genéricos (400, 500) não explicam o que realmente deu errado. Erros customizados trazem o contexto exato. |
| Impacto na experiência do cliente | Integrações são corrigidas mais rapidamente, reduzindo indisponibilidade de serviços que dependem da Neppo API. |

## O que você pode fazer com este módulo

| Operação | O que faz (em linguagem simples) |
| --- | --- |
| **Consultar erro** | Retorna a descrição detalhada de um código de erro específico da plataforma. |

## Exemplo de chamada

Substitua `SEU_TOKEN_AQUI` pelo Bearer token obtido via OAuth2.

```
curl -X GET "https://hml-chat-api.neppo.com.br/error" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

**Exemplo de resposta** (`200 OK`):

```
{}
```

Valores ilustrativos (esqueleto do schema). Os campos retornados seguem o modelo de dados do recurso.

---

## Referência técnica completa

## V1 — `custom-error-controller` (1 endpoints)

### `/error`

**handleError** · `operationId: handleErrorUsingGET`

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
