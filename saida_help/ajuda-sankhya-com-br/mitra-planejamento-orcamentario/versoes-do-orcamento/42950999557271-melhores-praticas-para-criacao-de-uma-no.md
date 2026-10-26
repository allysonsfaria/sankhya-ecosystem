---
id: "42950999557271"
titulo: "Melhores práticas para criação de uma nova versão do orçamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950999557271-Melhores-pr%C3%A1ticas-para-cria%C3%A7%C3%A3o-de-uma-nova-vers%C3%A3o-do-or%C3%A7amento"
trilha: "MITRA: Planejamento orçamentário  > Versões do orçamento"
atualizado_em: "2026-08-24T13:48:28Z"
rotulos: ["sync_hc", "mitra", "sync_hash_885093c65acf", "mitra_3"]
---

# Melhores práticas para criação de uma nova versão do orçamento

## Melhores práticas para criação de uma nova versão do orçamento

A criação de uma nova versão (ciclo orçamentário) afeta todos os gestores ao mesmo tempo: **a versão aberta anterior é fechada automaticamente**, os links de preenchimento passam a valer para o novo ciclo e o progresso de preenchimento recomeça. Este artigo orienta como preparar, executar e conferir essa operação para evitar perda de acesso dos gestores e retrabalho.

### Quando aplicar

- **Orçamento anual completo (0+12):** novo exercício, preenchimento de janeiro a dezembro.
- **Forecast ou revisão (por exemplo, 5+7):** parte do ano já realizada; os meses realizados ficam travados e o preenchimento cobre os meses restantes.
- **Simulação ou cenário alternativo:** duplicação de uma versão existente para ajustar premissas e valores sem perder a original.

### Pré-requisitos

- Perfil com permissão de administração do orçamento.
- Definição prévia de: nome da versão, ano, último mês realizado e se a versão servirá de referência de comparação (versão de controle).
- Realizado contábil carregado até o mês que será considerado como último mês realizado, quando se tratar de forecast ou revisão.

### Procedimento recomendado

1. **Prepare a nomenclatura.** Use um padrão que identifique exercício e cenário, como `Orçamento 2026: 0+12`, `Forecast 2026 (5+7)` ou `Revisão Orçamento`. O nome é o principal identificador da versão para gestores e relatórios.
2. **Escolha o modo de criação:**
   - **Criar do zero:** gera a nova versão com o mapa de status dos CRs e pacotes zerado e **copia as premissas** da versão anterior. Os valores de orçamento começam vazios.
   - **Duplicar uma versão existente:** copia também os **dados já preenchidos** da versão de origem, preservando os desligamentos projetados.
3. **Informe o último mês realizado.** Ele define quantos meses ficam travados como realizado no preenchimento (0 para orçamento cheio; 5 para um forecast 5+7, por exemplo).
4. **Execute a criação.** A operação fecha as versões abertas, cria o novo ciclo e o mapa de status em uma única ação, com proteção contra duplo acionamento.
5. **Confira a nova versão** antes de comunicar os gestores (ver checklist abaixo).
6. **Comunique os gestores.** Os links de preenchimento são gerados por versão e por gestor — dispare os novos links para que cada gestor acesse o ciclo correto.

### Cenários e recomendações

#### Cenário 1: forecast com meses realizados

**Condição:** parte do exercício já possui realizado contábil (por exemplo, cinco meses).

**Recomendação:** informe o último mês realizado corretamente na criação. Se ficar errado, os gestores conseguirão editar meses que já têm realizado — ou ficarão travados em meses que ainda deveriam orçar — e a correção exigirá revisão dos lançamentos.

#### Cenário 2: simulação a partir de uma versão preenchida

**Condição:** é preciso testar premissas diferentes sem descartar o trabalho já feito.

**Recomendação:** use a duplicação, que copia os dados preenchidos e preserva os desligamentos projetados. Marque claramente no nome que se trata de simulação, para não ser confundida com a versão oficial.

### Pontos de atenção

> **Atenção:** criar uma nova versão **fecha automaticamente as versões abertas**. No fechamento, o total de modelos de cada CR é congelado como fotografia da versão e **os links de preenchimento dos gestores da versão anterior são desativados**. Com o ciclo fechado, não é mais possível salvar valores nem submeter CRs nele.

- Faça a criação em um momento comunicado aos gestores, preferencialmente fora do horário de preenchimento ativo.
- A versão marcada como **versão de controle** serve de referência de comparação no preenchimento; confirme qual versão deve ter essa marcação após a criação.
- O fluxo de aprovação recomeça na nova versão: todos os CRs voltam ao status pendente, e as confirmações de modelos precisam ser refeitas.

### Checklist de conclusão

- [ ] Nova versão aparece como versão atual, com nome, ano e último mês realizado corretos.
- [ ] Versões anteriores constam como fechadas.
- [ ] Premissas copiadas conferidas (e dados copiados, no caso de duplicação).
- [ ] Status dos CRs e pacotes zerados (pendentes) na nova versão.
- [ ] Novos links de preenchimento gerados e comunicados aos gestores.
- [ ] Versão de controle definida, quando aplicável.

### Resultado esperado

A nova versão fica aberta como versão atual, com o mapa de status zerado e as premissas herdadas; as versões anteriores ficam fechadas e preservadas para consulta e comparação; cada gestor acessa o novo ciclo pelo seu link atualizado.

---

### Pendências para validação

1. Confirmar os rótulos da interface na tela de versões (botões de criar, duplicar e fechar).
2. Confirmar se o disparo dos links aos gestores é feito por ação manual na tela ou automaticamente após a criação.
