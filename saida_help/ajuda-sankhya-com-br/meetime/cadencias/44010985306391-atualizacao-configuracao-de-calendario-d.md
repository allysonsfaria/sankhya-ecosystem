---
id: "44010985306391"
titulo: "Atualização - Configuração de Calendário de Trabalho e Feriados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010985306391-Atualiza%C3%A7%C3%A3o-Configura%C3%A7%C3%A3o-de-Calend%C3%A1rio-de-Trabalho-e-Feriados"
trilha: "Meetime > Cadências"
atualizado_em: "2026-10-05T18:51:53Z"
rotulos: ["sync_hc", "meetime", "meetime_464", "sync_hash_0a6981bf0df9"]
---

# Atualização - Configuração de Calendário de Trabalho e Feriados

A página de **Calendário de Trabalho** permite que **Gestores e Admins** definam:

- quais dias da semana são considerados **dias úteis**
- e quais datas devem ser tratadas como **feriados e recessos**

Essas configurações impactam **exclusivamente as atividades programadas automaticamente pela cadência padrão** (ligações, follow-ups, e-mails manuais, WhatsApp, etc.).

O objetivo é evitar que essas atividades caiam em dias não trabalhados, reduzir falsos atrasos nos relatórios e eliminar a necessidade de pausar cadências manualmente em feriados.

As alterações do calendário são **salvas automaticamente**.

⚠️ As configurações são aplicadas **para toda a conta**, impactando todos os usuários.

## Como acessar?

Para acessar, basta clicar em Prospecção > Ajustes > Calendário de trabalho

### Imagem 1: 1. Dias úteis da semana1. Dias úteis da semana

Define em quais dias as **atividades programadas automaticamente pela cadência padrão** podem ser agendadas.

- Os dias da semana são exibidos como botões (**Segunda a Domingo**)
- **Ativo** = dia útil; **Inativo** = dia não útil
- Por padrão, a conta inicia com **segunda a sexta** como dias úteis

#### Regras importantes

- Deve existir **pelo menos um dia útil ativo**
- Alterações **não afetam atividades já programadas** — valem apenas para agendamentos futuros
- Contas com configurações antigas (ex.: sábado útil) terão essas regras refletidas automaticamente ao abrir a tela pela primeira vez

---

### 2. Feriados e recessos

Permite cadastrar datas que devem ser tratadas como **não úteis**.

Cada feriado pode ser:

- **Data única**, ou
- **Intervalo de datas** (ex.: recesso coletivo)

Atividades que seriam programadas automaticamente pela cadência para essas datas são **reagendadas para o próximo dia útil disponível**.

#### Regras e limitações

- Apenas **datas futuras** podem ser cadastradas
- **Nome** e **data** são obrigatórios
- Intervalos devem ter data final ≥ data inicial
- Não é permitido cadastrar feriados que **se sobreponham** a outros já existentes

> Exemplo:
>
> Se “Natal – 25/12” já está cadastrado, não é possível criar “Recesso – 20/12 a 01/01”.

Quando há sobreposição, o sistema impede o cadastro e exibe uma mensagem de erro.

#### Listagem de feriados

- Exibe apenas **feriados do ano atual e futuros**
- Feriados antigos não aparecem
- Cada item mostra nome + período, além das ações **Editar** e **Excluir**

---

### 3. Edição de feriados

Ao editar um feriado:

- Os dados atuais são carregados no modal
- Após salvar, o período é atualizado
- O calendário passa a considerar o novo intervalo para agendamentos futuros

---

### 4. Exclusão de feriados

Ao excluir um feriado:

- Um modal solicita confirmação
- Após confirmar, o item é removido da lista
- A data deixa de ser considerada não útil para futuras programações da cadência

---

### 5. Impacto na rotina do Flow

O calendário afeta **somente**:

#### ➤ Atividades programadas automaticamente pela cadência padrão

Ou seja, qualquer passo configurado no fluxo da cadência que gera tarefa automaticamente:

- Ligações
- Follow-ups
- E-mails manuais
- WhatsApp
- Qualquer outra atividade padrão da cadência

---

#### ❌ O calendário não interfere em:

- Cadências automáticas de e-mail
- Atividades criadas manualmente na tela de execução
- Reagendamentos feitos manualmente
- Entrada de leads (API, RD, importação, inbound etc.)
- Nova prospecção após perdido

---

#### ✔ O que muda

- Se uma atividade automática cair em um feriado ou dia não útil, ela é **reagendada para o próximo dia útil**
- Essas atividades **não aparecem como atrasadas** nos relatórios
- Se houver sequência de dias inválidos (ex.: feriado + fim de semana), o sistema avança até o próximo dia útil disponível

---

#### ✔ O que não muda

- Atividades já programadas antes de alterar o calendário **não são editadas**
- A nova regra vale apenas para programações futuras

---

### Valores padrão

**Novas contas:**

- Segunda a sexta vêm marcadas como dias úteis
- Nenhum feriado cadastrado

**Contas existentes:**

- Regras legadas (como sábado útil) aparecem refletidas ao abrir a tela pela primeira vez
- Após a primeira edição, o calendário passa a ser a **fonte de verdade** da conta

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
