---
id: "42637858969239"
titulo: "Decisões de Arquitetura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42637858969239-Decis%C3%B5es-de-Arquitetura"
trilha: "NEPPO: Personalização de atendimento > Neppo Billing"
atualizado_em: "2026-08-11T16:13:02Z"
rotulos: ["sync_hc", "neppo", "neppo_918323201", "sync_hash_df92645b0cd8"]
---

# Decisões de Arquitetura

O time documenta decisões estruturais importantes como **ADRs** (Architecture
Decision Records) no repositório. Esta página é um resumo em linguagem simples — o
texto técnico completo, com o contexto e as alternativas consideradas, fica em
`docs/adr/` no repositório.

| # | Decisão | Em uma frase |
| --- | --- | --- |
| 0001 | Camada raw canônica | Os dados coletados dos clientes são normalizados num formato único (`raw_event` + `raw_seat_snapshot`) antes de qualquer cálculo de métrica. |
| 0002 | Autenticação da API externa | Integradores externos usam chave de API + escopos — não login de usuário. |
| 0003 | Cobertura de ingestão | Define o formato dos dados brutos necessário para conseguir faturar 100% das métricas (Licenses) configuradas. |
| 0004 | DuckDB via Quack (modo remoto) | Avaliado como alternativa de banco analítico; **bloqueado/parado** — não está em uso hoje. |
| 0005 | MySQL como banco analítico | Decisão vigente: o banco analítico usa a mesma instância MySQL do banco de configuração, com um pool de conexões dedicado. Substituiu o DuckDB embarcado. |

> A 0005 é a decisão que vale hoje para "qual banco guarda os dados de consumo" — a
> 0004 ficou historicamente registrada, mas não reflete o estado atual.

**Ver também:** [Como Funciona](https://sankhya.zendesk.com/hc/pt-br/articles/42637911579543) · [pasta docs/adr no repositório](https://bitbucket.org/neppo/neppo-billing/src/master/docs/adr/)
