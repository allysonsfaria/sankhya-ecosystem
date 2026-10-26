---
id: "42950938568983"
titulo: "Melhores práticas para aprovação e reprovação de orçamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950938568983-Melhores-pr%C3%A1ticas-para-aprova%C3%A7%C3%A3o-e-reprova%C3%A7%C3%A3o-de-or%C3%A7amentos"
trilha: "MITRA: Planejamento orçamentário  > Acompanhamento e aprovação"
atualizado_em: "2026-08-24T13:48:32Z"
rotulos: ["sync_hc", "mitra", "mitra_7", "sync_hash_ec3d53bc2395"]
---

# Melhores práticas para aprovação e reprovação de orçamentos

## Melhores práticas para aprovação e reprovação de orçamentos

A avaliação dos orçamentos submetidos é o ponto de controle do ciclo: uma aprovação apressada congela números errados, e uma reprovação sem explicação gera retrabalho e idas e vindas com o gestor. Este artigo orienta como conduzir as transições de status com rastreabilidade e comunicação clara.

### Quando aplicar

- Ao avaliar CRs ou pacotes no status **Submetido**.
- Ao devolver um orçamento para correção (**Reprovado**).
- Ao reabrir um item já avaliado para nova rodada. [VALIDAR: como a reabertura é acionada na interface]

### Pré-requisitos

- Perfil com permissão de aprovação.
- CR ou pacote no status adequado — as transições são validadas pelo sistema; não é possível aprovar o que não foi submetido.

### Procedimento recomendado

1. **Avalie pelo quadro de acompanhamento**, filtrando a versão vigente e, se necessário, o gestor.
2. **Confira o progresso do cartão** antes de abrir a avaliação: o CR submetido deve estar com todos os modelos confirmados.
3. **Analise os valores** nas visões de resultado (orçado × realizado) antes de decidir.
4. **Ao aprovar**, registre a decisão. O CR fica bloqueado para edição.
5. **Ao reprovar, escreva um comentário específico**: qual conta, qual mês, qual premissa deve ser revista. O comentário fica visível ao gestor no link de preenchimento e orienta a correção.
6. **Notifique o gestor** na transição — o sistema envia e-mail com o contexto da decisão.

### Cenários e recomendações

#### Cenário 1: reprovação com correção pelo gestor

**Condição:** o orçamento submetido tem inconsistências pontuais.

**Recomendação:** reprove com comentário objetivo em vez de corrigir por fora. O CR volta a aceitar edição, o gestor corrige exatamente o que foi apontado e ressubmete. Todo o vai-e-vem fica na trilha de auditoria.

#### Cenário 2: necessidade de alterar um CR já aprovado

**Condição:** surgiu um ajuste depois da aprovação.

**Recomendação:** não tente contornar o bloqueio. Use a reabertura para devolver o CR ao fluxo — o evento fica registrado na auditoria — e repita a avaliação após o ajuste.

### Pontos de atenção

> **Atenção:** a aprovação bloqueia a edição do CR. Reverter exige reabertura registrada em auditoria. Aprove somente após a conferência dos valores.

- Toda transição grava na trilha de auditoria: evento, status de origem e destino, autor, comentário, data e origem (aplicativo ou link).
- Reprovações sem comentário deixam o gestor sem direção; trate o comentário como parte obrigatória da decisão.
- A auditoria completa da versão pode ser consultada com filtros por evento — use-a na prestação de contas do ciclo.

### Checklist de conclusão

- [ ] Todos os cartões da versão avaliados (nenhum Submetido pendente de decisão).
- [ ] Reprovações com comentário específico e gestor notificado.
- [ ] Aprovações conferidas contra as visões de resultado.
- [ ] Trilha de auditoria da versão revisada ao final do ciclo.

### Resultado esperado

Ciclo encerrado com todos os CRs e pacotes em **Aprovado**, decisões documentadas com autor, data e comentário, e gestores informados de cada transição.

### Artigos relacionados

- Como submeter o orçamento de um centro de resultado para aprovação?
- Acompanhamento de status do orçamento: visão geral e utilização

---

### Pendências para validação

1. `[VALIDAR: como a reabertura é acionada na interface]` — o evento de reabertura existe na auditoria; confirmar o controle na tela.
2. `` com permissão de aprovação.
3. Confirmar se a notificação por e-mail é automática em toda transição ou opcional por decisão do aprovador.
