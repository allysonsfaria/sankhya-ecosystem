---
id: "42637911712407"
titulo: "Perguntas Frequentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42637911712407-Perguntas-Frequentes"
trilha: "NEPPO: Personalização de atendimento > Neppo Billing"
atualizado_em: "2026-08-11T16:13:03Z"
rotulos: ["sync_hc", "neppo", "sync_hash_84f45ec5e86b", "neppo_917536786"]
---

# Perguntas Frequentes

**O Neppo Billing calcula quanto o cliente deve pagar?**
Não. Ele só mede e envia quantidades de consumo (ex.: "342 mensagens enviadas em
julho"). O cálculo de preço acontece em um sistema downstream separado, fora deste
projeto.

**Onde ficam os valores/preços de cada Package?**
Em nenhum lugar deste sistema. Package é só um nome de catálogo — o preço é resolvido
por outro sistema a partir do código que o Package carrega.

**O sistema gera fatura?**
Não. Ele fornece os dados de consumo; a fatura é gerada por outro sistema, a partir
desses dados.

**Por que um registro de consumo "sumiu" ou está diferente do que eu vi ontem?**
Ele não sumiu — consumo é append-only. Se um valor foi corrigido, existe um novo
registro (revisão) e o antigo foi marcado como substituído, nunca apagado. Dá pra
consultar o histórico completo de revisões.

**Quem pode acessar a UI interna do Neppo Billing?**
Qualquer pessoa autenticada via Keycloak (login único da empresa) tem acesso de
leitura. Ações de escrita — criar/editar Operations, Licenses, disparar jobs, etc. —
exigem o papel de "operador" (`billing.operator`).

**Como um sistema externo consome os dados de consumo?**
Via API `/api/v1`, autenticado por chave de API com escopo específico (ex.:
`consumption:read`). As chaves são geridas na seção "Chaves de API" das
Configurações.

**Onde fica a lógica de precificação, então?**
Em um sistema separado, fora deste repositório. Se alguém encontrar, dentro deste
projeto, código calculando desconto, valor ou parcela — é sinal de que aquilo está no
lugar errado.

**Ver também:** [Visão Geral](https://sankhya.zendesk.com/hc/pt-br/articles/42637887921175) · [Segurança e Acesso](https://sankhya.zendesk.com/hc/pt-br/articles/42637888477591)
