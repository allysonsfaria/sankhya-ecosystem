---
id: "42427312229271"
titulo: "R21 - Como gerar a Planilha para Controle de Banco de Horas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427312229271-R21-Como-gerar-a-Planilha-para-Controle-de-Banco-de-Horas"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T13:29:35Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_148f27442a17", "pontotel_6a3329f584c5ab2970dcd801"]
---

# R21 - Como gerar a Planilha para Controle de Banco de Horas

O relatório **R21 - Planilha para controle de banco de horas** é a ferramenta mais completa para a **gestão** e auditoria detalhada do banco de horas dos seus colaboradores.
Diferente de outros relatórios que mostram apenas o saldo final, o R21 funciona como um **extrato bancário**, detalhando dia a dia todos os eventos (créditos e débitos) que movimentaram o saldo do banco, além de informações sobre as janelas de compensação.

---

## Como gerar o Relatório

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de Relatórios (à direita), selecione a opção **R21 - Planilha para controle de banco de horas**.
3. Defina os filtros para a sua consulta:

   - **Filtro principal:** Você pode filtrar por **locais de trabalho**, **empregadores**, **empregados** ou **grupos**.
   - **Período:** Selecione o intervalo de datas (início e fim) que deseja consultar.
4. Configure as opções extras de acordo com sua necessidade:

   - **incluir também período com baixa de horas:** Marque esta opção se você precisar auditar dados de períodos de banco que já foram fechados (que tiveram "[baixa](https://sankhya.zendesk.com/hc/pt-br/articles/42427349304855)").
   - **incluir aba de janelas de BH...:** Essencial se sua empresa utiliza a regra de **Compensação por Janela**. Isso adiciona uma aba na planilha mostrando os saldos que estão vencendo ou já venceram**.**
   - **incluir histórico de compensações...:** Também usado para a regra de **Compensação por Janela**, detalha como as horas foram compensadas.
5. Clique em **gerar excel**.

![Imagem 1: Clique em gerar excel .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_6d0h3j.png)

---

## Como baixar o Relatório

Após clicar em "gerar excel", a plataforma processará o relatório em segundo plano:

1. No menu de navegação, clique no **ícone de sino** (Notificações), para acompanhar o arquivo ser gerado.
2. Quando chegar a "100%", o relatório será baixado automaticamente.
3. O R21 é baixado como um arquivo compactado (ZIP). Ao extrair o arquivo, você verá três planilhas:

   - **r21-sucesso:** O relatório principal com todos os dados.
   - **r21-status:** Um arquivo técnico sobre o status da geração.
   - **r21-erro:** Lista eventuais erros na geração.
4. Abra o arquivo **r21-sucesso** para iniciar sua análise.

---

## Como fazer a leitura do relatório

![Imagem 2: Como fazer a leitura do relatório](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_vpnep.png)

O arquivo `r21-sucesso` é o seu extrato detalhado. Cada linha representa um dia de um colaborador, mostrando exatamente o que aconteceu.

| Coluna(s) | O que a informação representa | Dicas de Auditoria (Sua Gestão) |
| --- | --- | --- |
| **Funcionário, Data, Local...** | Identificação do colaborador e o dia exato da movimentação. | Permite filtrar a análise por um dia ou colaborador específico. |
| **Vencimento** | Mostra a data de validade (vencimento) daquele saldo específico, conforme a regra de banco. | Use esta data para garantir que as compensações sejam feitas antes do vencimento. |
| **H. Extra, Atraso, H. Falta, etc.** | Detalha todos os apontamentos (eventos) que ocorreram no dia e que, segundo a sua regra, devem alimentar o banco de horas. | **Auditoria:** Se o colaborador teve "H. Atraso" de 10:48, esta é a causa do débito no banco. |
| **Saldo** | Este é o valor final (crédito ou débito) que foi efetivamente lançado no banco de horas naquele dia. É o resultado dos eventos. | **Transparência:** É o valor da transação diária. Se o colaborador teve 10:48 de atraso, o "Saldo" lançado no banco foi "-10:48". |
| **Aprovado?** | Confirma se o lançamento do "Saldo" foi validado e contabilizado no banco. | "Aprovado" significa que o saldo foi computado. "Sem saldo/evento no dia" indica que não houve movimentação de banco naquele dia. "Reprovado" significa que foi retirado do banco e consta na folha. |

---

O R21 é a principal ferramenta para a **evolução** da sua auditoria de banco de horas. Com ele, você tem total **transparência** sobre cada evento que compõe o saldo final dos seus colaboradores, facilitando a conferência e a **gestão** da folha de pagamento.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao site [Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
