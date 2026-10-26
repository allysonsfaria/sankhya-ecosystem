---
id: "42950953896343"
titulo: "Acompanhamento de status do orçamento: visão geral e utilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950953896343-Acompanhamento-de-status-do-or%C3%A7amento-vis%C3%A3o-geral-e-utiliza%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Acompanhamento e aprovação"
atualizado_em: "2026-08-24T13:48:30Z"
rotulos: ["sync_hc", "mitra", "mitra_5", "sync_hash_328ca324feb2"]
---

# Acompanhamento de status do orçamento: visão geral e utilização

## Acompanhamento de status do orçamento: visão geral e utilização

**Módulo:** Acompanhamento do orçamento

### O que é e para que serve

A tela de acompanhamento mostra, para uma versão do orçamento, o andamento do preenchimento de todos os centros de resultado (CRs) e pacotes em um quadro de cartões organizado por status. É a visão do administrador e do aprovador para saber quem já preencheu, quem submeteu e o que falta avaliar.

### Pré-requisitos

- Perfil com acesso à administração ou aprovação do orçamento.
- Uma versão do orçamento criada, com gestores e CRs configurados.

### Visão geral

- **Cartões por CR e por pacote:** cada cartão mostra o responsável e o progresso de preenchimento — a quantidade de modelos confirmados em relação ao total de modelos do CR.
- **Organização por status:** os cartões se distribuem entre **Pendente**, **Submetido**, **Aprovado** e **Reprovado**. Pacotes possuem seu próprio ciclo de status.
- **Contadores agregados:** a tela apresenta a contagem consolidada de CRs e pacotes por status na versão selecionada.

### Filtros

| Filtro | O que faz | Obrigatório |
| --- | --- | --- |
| Versão (ciclo) | Define qual versão do orçamento é exibida | Sim |
| Gestor | Restringe os cartões aos CRs e pacotes de um gestor | Não |

### Ações e controles

| Ação | O que faz |
| --- | --- |
| Aprovar | Move o CR ou pacote submetido para **Aprovado** e bloqueia a edição |
| Reprovar | Devolve o CR ou pacote ao gestor com comentário, para correção e ressubmissão |
| Notificação | O sistema pode enviar e-mail ao gestor na transição de status |

[VALIDAR: rótulos exatos dos botões de aprovação e reprovação na interface]

### Comportamentos e pontos de atenção

- Toda transição de status é registrada na **trilha de auditoria** do workflow, com evento, status de origem e destino, autor, comentário, data e origem da ação (aplicativo ou link do gestor). A trilha pode ser consultada com filtros por versão e por tipo de evento.
- Após o fechamento da versão, o total de modelos de cada cartão fica **congelado como fotografia** do momento do fechamento — alterações posteriores na configuração de modelos não mudam o histórico.
- O comentário informado na reprovação fica visível para o gestor no link de preenchimento.

### Resultado esperado

O quadro reflete em tempo real o andamento do ciclo: ao final do processo, todos os cartões devem estar em **Aprovado**, e a trilha de auditoria conta a história completa de cada CR e pacote.

### Artigos relacionados

- Como submeter o orçamento de um centro de resultado para aprovação?
- Melhores práticas para aprovação e reprovação de orçamentos

---

### Pendências para validação

1. `` com acesso à tela.
2. `[VALIDAR: rótulos exatos dos botões de aprovação e reprovação na interface]`.
3. Confirmar se o comentário é obrigatório na reprovação.
