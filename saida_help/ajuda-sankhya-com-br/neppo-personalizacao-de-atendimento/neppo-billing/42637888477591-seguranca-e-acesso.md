---
id: "42637888477591"
titulo: "Segurança e Acesso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42637888477591-Seguran%C3%A7a-e-Acesso"
trilha: "NEPPO: Personalização de atendimento > Neppo Billing"
atualizado_em: "2026-08-11T17:13:20Z"
rotulos: ["sync_hc", "neppo", "neppo_918192129", "sync_hash_58ba235ff594"]
---

# Segurança e Acesso

O Neppo Billing tem **dois mecanismos de autenticação** completamente separados, um
para cada tipo de consumidor.

## Acesso interno (UI Angular) — rotas `/api/**`

- Login via **Keycloak** (SSO da empresa), sessão autenticada.
- Dois papéis:

  - `billing.viewer` — somente leitura
  - `billing.operator` — leitura **+** escrita (criar/editar Operations, Licenses,
    disparar jobs, etc.)
- Sem sessão válida, chamadas à API retornam **401** (navegação de página é
  redirecionada para o login).
- Endpoints que expõem segredos/credenciais (ex.: Chaves de API, configuração de
  integrações) exigem `operator` mesmo para leitura.

## Acesso externo (integradores/sistemas) — rotas `/api/v1/**`

- Autenticação por **chave de API**, enviada no header `Authorization: Bearer <chave>`.
- Cada chave carrega **escopos** específicos, que limitam o que ela pode fazer:

  - `operations:write` — criar/editar Operations
  - `dialog360:write` — gerenciar vínculos do 360dialog (WhatsApp)
  - `consumption:read` — ler dados de consumo
- Chaves são geridas na seção "Chaves de API" das Configurações, na UI interna.

## Por que dois mecanismos?

A API interna serve **pessoas** (via VPN, com login humano). A API externa
(`/api/v1`) serve **máquina-a-máquina** — sistemas parceiros consumindo dados de
consumo ou registrando operações, sem depender de sessão de navegador. São contratos
com ciclos de vida diferentes: a API externa é **versionada** (`/api/v1`, `/api/v2`…)
e muda com muito mais cuidado do que a UI interna, que pode evoluir livremente.

**Ver também:** [Perguntas Frequentes](https://sankhya.zendesk.com/hc/pt-br/articles/42637911712407) · [Glossário de Domínio](https://sankhya.zendesk.com/hc/pt-br/articles/42637882473879)
