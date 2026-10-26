---
id: "44010630244247"
titulo: "Calendário de Trabalho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010630244247-Calend%C3%A1rio-de-Trabalho"
trilha: "Meetime > Configurações"
atualizado_em: "2026-10-05T18:43:05Z"
rotulos: ["sync_hc", "meetime", "meetime_628", "sync_hash_be07072d3e0f"]
---

# Calendário de Trabalho

A página de **Calendário de Trabalho** permite que **Gestores e Administradores** definam quais dias são considerados úteis na conta, incluindo dias da semana trabalhados e datas de **feriados ou recessos**.

Essas configurações impactam **exclusivamente as atividades geradas automaticamente pela cadência padrão** (ligações, follow-ups, e-mails manuais, WhatsApp, entre outros), evitando que sejam agendadas em dias não trabalhados. Com isso, também é possível reduzir atrasos incorretos nos relatórios e eliminar a necessidade de pausar cadências manualmente em feriados.

![Imagem 1: Essas configurações impactam exclusivamente as atividades geradas automaticamente pela cadência padrão (ligações,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010664134039)

As alterações realizadas no calendário são salvas automaticamente.

⚠️ Importante: as configurações são aplicadas para toda a conta, impactando todos os usuários.

---

## Dias úteis da semana

Define em quais dias as atividades programadas automaticamente pela cadência padrão podem ser agendadas.

Os dias da semana são exibidos como botões (segunda a domingo):

- Ativo = dia útil
- Inativo = dia não útil

Por padrão, a conta inicia com segunda a sexta como dias úteis.

Regras importantes:

- Deve existir pelo menos um dia útil ativo
- Alterações não afetam atividades já programadas, valem apenas para agendamentos futuros

---

### Feriados e recessos

Permite cadastrar datas que devem ser tratadas como não úteis. Cada feriado pode ser uma data única ou um intervalo de datas (ex: recesso coletivo).

Quando uma atividade automática cair em um feriado, ela é reagendada para o próximo dia útil disponível.

Regras e limitações:

- Apenas datas futuras podem ser cadastradas
- Nome e data são obrigatórios
- Intervalos devem ter data final ≥ data inicial
- Não é permitido cadastrar feriados que se sobreponham

Exemplo: se “Natal – 25/12” já existe, não é possível cadastrar “Recesso – 20/12 a 01/01”.

![Imagem 2: Exemplo: se “Natal – 25/12” já existe, não é possível cadastrar “Recesso – 20/12 a 01/01”.](https://ajuda.sankhya.com.br/hc/article_attachments/44010637454999)

![Imagem 3: Exemplo: se “Natal – 25/12” já existe, não é possível cadastrar “Recesso – 20/12 a 01/01”.](https://ajuda.sankhya.com.br/hc/article_attachments/44010706231831)

A listagem exibe apenas feriados do ano atual e futuros, mostrando nome, período e as ações de Editar e Excluir.

Ao editar, o novo período passa a valer para agendamentos futuros.

Ao excluir, a data deixa de ser considerada não útil.

---

## Impacto na rotina

O calendário afeta somente atividades programadas automaticamente pela cadência padrão, como ligações, follow-ups, e-mails manuais e WhatsApp.

Ele não interfere em:

- cadências automáticas de e-mail
- atividades criadas manualmente
- reagendamentos manuais
- entrada de leads (API, RD, importação, inbound etc.)
- nova prospecção após perdido

Na prática:

- atividades que caem em dias inválidos são reagendadas
- elas não aparecem como atrasadas nos relatórios
- o sistema avança automaticamente até o próximo dia útil disponível
- atividades já existentes não são alteradas

---

## Valores padrão

Novas contas iniciam com segunda a sexta como dias úteis e sem feriados cadastrados.

Contas existentes mantêm regras antigas refletidas ao abrir a tela pela primeira vez. Após a primeira edição, o calendário passa a ser a fonte oficial de configuração da conta.

Atividades já existentes não são alteradas

---

Ainda tem dúvidas? Entre em contato com a gente através do e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
