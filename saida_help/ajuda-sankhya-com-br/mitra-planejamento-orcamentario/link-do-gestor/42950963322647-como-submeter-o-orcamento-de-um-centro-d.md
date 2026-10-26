---
id: "42950963322647"
titulo: "Como submeter o orçamento de um centro de resultado para aprovação?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950963322647-Como-submeter-o-or%C3%A7amento-de-um-centro-de-resultado-para-aprova%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Link do gestor"
atualizado_em: "2026-08-24T13:48:25Z"
rotulos: ["sync_hc", "mitra", "mitra_1", "sync_hash_bd81fbd16c5e"]
---

# Como submeter o orçamento de um centro de resultado para aprovação?

## Como submeter o orçamento de um centro de resultado para aprovação?

Para submeter o orçamento de um centro de resultado (CR), você precisa primeiro **confirmar todos os modelos de preenchimento** do CR (por exemplo, Base Zero, Base Histórico, Receita e Pessoal). Somente depois que todos os modelos estiverem confirmados a submissão é liberada. Ao submeter, o CR muda para o status **SUBMETIDO**, o preenchimento é bloqueado e o orçamento segue para avaliação do aprovador, que pode **aprovar** ou **reprovar** com comentário.

### Contexto

O preenchimento é organizado por **ciclo orçamentário** (por exemplo, `Orçamento 2026: 0+12` ou `Forecast 2026 (5+7)`). Dentro do ciclo, cada CR sob sua responsabilidade tem um conjunto de modelos (abas de preenchimento), e cada modelo possui um controle de confirmação individual.

O CR percorre os seguintes status no fluxo de aprovação:

| Status | O que significa | Pode editar valores? |
| --- | --- | --- |
| PENDENTE | Preenchimento em andamento | Sim |
| SUBMETIDO | Enviado para aprovação, aguardando avaliação | Não |
| APROVADO | Orçamento aceito pelo aprovador | Não |
| REPROVADO | Devolvido com comentário para correção | Sim |

Cada mudança de status gera um registro na trilha de auditoria do workflow (evento, status de origem, status de destino, autor, comentário, data e origem da ação — aplicativo ou link do gestor).

> **Nota:** o acesso do gestor ocorre por um link exclusivo com token, gerado por ciclo e por gestor. A página inicial do link mostra os cartões dos seus CRs e pacotes com status e progresso de preenchimento.

### Como fazer

1. Acesse o link de preenchimento recebido por e-mail.
2. Abra o CR desejado na página inicial.
3. Preencha os valores de cada modelo (aba) do CR.
4. Confirme cada modelo usando o controle de confirmação da aba. [VALIDAR: rótulo exato do botão de confirmação]
5. Depois que todos os modelos estiverem confirmados, acione a submissão do CR. [VALIDAR: rótulo exato do botão de submissão]
6. Aguarde a avaliação do aprovador. Você será notificado por e-mail sobre o resultado. [VALIDAR: se o gestor recebe e-mail em toda transição ou apenas em algumas]

### Resultado esperado

- O cartão do CR passa a exibir o status **SUBMETIDO**.
- Os campos de valores ficam bloqueados para edição.
- A submissão aparece registrada na trilha de auditoria do workflow.

### Limitações ou alternativas

- **Ciclo fechado bloqueia tudo:** se o ciclo estiver com status `FECHADO`, não é possível salvar valores nem submeter, mesmo com os modelos confirmados.
- **Submissão parcial não existe:** a submissão é do CR inteiro; não é possível submeter apenas um modelo.
- **Após reprovação:** o CR volta a aceitar edição. Corrija os valores conforme o comentário do aprovador e submeta novamente — a ressubmissão é permitida a partir dos status PENDENTE e REPROVADO.
- **Confirmação pode ser desfeita:** enquanto o CR não foi submetido, é possível desfazer a confirmação de um modelo para ajustá-lo (evento `CONFIRMACAO_DESFEITA` na auditoria).
- **Pacotes têm fluxo próprio:** modelos com escopo de pacote (por exemplo, Custos de Software) são submetidos separadamente do CR, com seu próprio status.

### Artigos relacionados

- [VALIDAR: artigo sobre o preenchimento das abas de modelo (Base Zero e Base Histórico)]
- [VALIDAR: artigo sobre aprovação e reprovação pelo administrador]

---

### Pendências para validação

1. `[VALIDAR: rótulo exato do botão de confirmação]` — confirmar o texto do controle de confirmação da aba na interface.
2. `[VALIDAR: rótulo exato do botão de submissão]` — confirmar o texto do botão que submete o CR no link do gestor.
3. `[VALIDAR: se o gestor recebe e-mail em toda transição ou apenas em algumas]` — a função de workflow envia e-mail com parâmetro `notificar`; confirmar em quais eventos ele é usado.
