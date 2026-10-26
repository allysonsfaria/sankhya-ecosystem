---
id: "43655511068311"
titulo: "SOP Ficha de Cheques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43655511068311-SOP-Ficha-de-Cheques"
trilha: "Sankhya Official Pack - SOP > SOP Ficha de Cheque"
atualizado_em: "2026-09-22T14:17:01Z"
---

# SOP Ficha de Cheques

### Configuração de Cheques: prepare a empresa para operar a Ficha de Cheque

**O que será feito:** definir, **por empresa**, com quais naturezas, tipos de operação, tipo de título, conta bancária e relatórios a rotina Ficha de Cheque vai trabalhar. Nada na Ficha de Cheque acontece sem essa configuração: a cada operação o sistema busca a configuração da empresa e recusa a operação quando falta um dos campos essenciais.

![Imagem 1: O que será feito: definir, por empresa , com quais naturezas, tipos de operação, tipo de título, conta bancária e…](https://ajuda.sankhya.com.br/hc/article_attachments/43655511048599)

| **Essencial:**  Uma configuração por empresa que opera cheques. Empresa sem configuração faz a Ficha de Cheque parar com **"Necessário cadastrar a configuração da Empresa <n>."** |
| --- |

| **Definições**  **TOP** — Tipo de Operação; diz ao **Sankhya Om** que efeito o lançamento tem sobre o financeiro e o banco. **Natureza** — classificação de receita ou despesa do título gerado. **Conta do cheque** — a conta bancária onde os cheques da empresa ficam registrados; é a origem ou o destino das transferências que a rotina gera. |
| --- |

#### 1.1 Como acessar

Acesse **Sankhya Om** → SOP Ficha de Cheques → Cadastros → **"Configuração de Cheques"**.

A tela é um formulário dinâmico sobre a instância `ConfiguracaoCheque`. A listagem exibe **apenas a configuração vigente de cada empresa** — as versões anteriores continuam gravadas, mas não aparecem na tela.

| **OBSERVAÇÃO:** Para consultar o histórico completo de configurações de uma empresa, recorra a uma consulta sobre a tabela `CTCCON`, ordenada pelo campo "Data". |
| --- |

#### 1.2 Etapa 1 — Cadastrar a configuração da empresa

**(1)** Clique no botão de inclusão da barra de ferramentas.

**(2)** Informe **"Empresa"**.

**(3)** Preencha os campos do bloco principal, na tabela abaixo.

**(4)** Percorra as abas Troco, Credito, Devolução e Relatórios.

**(5)** Salve. Na inclusão, o sistema grava o campo **"Data"** com a data e hora do momento — o campo não é editável, nem na inclusão nem depois.

| Campo | O que informar |
| --- | --- |
| **"Conta Cheque"** | A conta bancária em que os cheques da empresa ficam registrados |
| **"Tipo Titulo Cheque"** | O tipo de título que os títulos gerados pela rotina recebem |
| **"TOP Recebimento"** | Tipo de operação usado na baixa dos títulos a receber e nas transferências de entrada |
| **"TOP Pagamento"** | Tipo de operação usado na baixa dos títulos a pagar e nas transferências de saída |
| **"TOP Lanc. Banc."** | Tipo de operação dos lançamentos bancários de transferência — sangria, depósito e complemento de valor |
| **"Natureza"** | Natureza padrão dos títulos gerados |
| **"Centro Resultado"** | Centro de resultado dos títulos gerados |

| **Mensagem**  Quatro campos são verificados a cada operação da Ficha de Cheque, e a ausência de qualquer um interrompe a operação: **"Conta Cheque"** → **"Necessário informar a conta na configuração."** · **"TOP Pagamento"** → **"Necessário informar o Tipo de Operação para Pagamento, no cadastro de configuração da empresa selecionada."** · **"TOP Recebimento"** → **"Necessário informar o Tipo de Operação para Recebimento, no cadastro de configuração da empresa selecionada."** · **"Tipo Titulo Cheque"** → **"Necessário informar a conta na Tipo De Titulo Cheque, no cadastro de configuração da empresa selecionada."** |
| --- |

#### 1.3 Etapa 2 — Aba Troco

Preenche o que a rotina usa quando o cheque cobre **mais** que os títulos e a operação decide devolver a diferença como **troco**.

| Campo | Uso |
| --- | --- |
| **"Natureza Troco Receita"** | Natureza do título de receita do troco |
| **"Natureza Troco Despesa"** | Natureza do título de despesa do troco |
| **"TOP Troco Receita"** | Tipo de operação do título de receita do troco |
| **"TOP Troco Despesa"** | Tipo de operação do título de despesa do troco |

Os quatro campos são obrigatórios. Sem eles, a decisão **"Troco"** do Complemento Financeiro não conclui.

#### 1.4 Etapa 3 — Aba Credito

Preenche o que a rotina usa quando a diferença a maior é registrada como **crédito** do parceiro, em vez de troco.

| Campo | Uso |
| --- | --- |
| **"Natureza Credito Receita"** | Natureza do título de receita do crédito |
| **"Natureza Credito Despesa"** | Natureza do título de despesa do crédito |
| **"TOP Credito Receita"** | Tipo de operação do título de receita do crédito |
| **"TOP Credito Despesa"** | Tipo de operação do título de despesa do crédito |

Os quatro campos são obrigatórios.

#### 1.5 Etapa 4 — Aba Devolução

Preenche os padrões da devolução de cheque.

| Campo | Uso |
| --- | --- |
| **"Natureza Receita Devolução"** | Natureza assumida quando a devolução não informa natureza |
| **"Natureza Despesa Devolução"** | Natureza de despesa da devolução |
| **"TOP Devolução Receita"** | Tipo de operação do título de receita da devolução |
| **"TOP Devolução Despesa"** | Tipo de operação do título de despesa da devolução |

| **OBSERVAÇÃO:** Na tela de devolução da rotina Ficha de Cheque o operador informa tipo de operação, natureza, centro de resultado, tipo de título, alínea, conta e data. O valor desta aba entra como padrão de retaguarda: quando a natureza não é informada, o sistema usa "Natureza Receita Devolução". |
| --- |

#### 1.6 Etapa 5 — Aba Relatórios

Define qual relatório a rotina imprime e em que momento.

| Campo | Uso |
| --- | --- |
| **"Relatório Rastreamento"** | Relatório aberto pelo botão "Relatório Rastreamento" da Ficha de Cheque; recebe o número único do cheque |
| **"Relatório Recibo"** | Relatório do recibo da operação; recebe o número do lote |
| **"Imprime Recibo no Recebimento?"** | Marcado, o recibo é impresso ao concluir um recebimento |
| **"Imprime Recibo no Pagamento?"** | Marcado, o recibo é impresso ao concluir um pagamento |

Os dois relatórios são obrigatórios. As duas marcações são opcionais — desmarcadas, a operação conclui sem impressão.

#### 1.7 Aba Adiantamento

A aba Adiantamento existe na estrutura da tabela, com naturezas e tipos de operação de receita e despesa, mas os campos estão **ocultos na tela** e nenhum fluxo da rotina os consome hoje.

| **OBSERVAÇÃO:** Não é necessário preencher esses campos. Eles ficam reservados para o fluxo de adiantamento, ainda não habilitado. |
| --- |

#### 1.8 Campos da configuração

| Campo | Nome na tela | Aba | Obrigatório? | Editável? |
| --- | --- | --- | --- | --- |
| `CODEMP` | "Empresa" | Principal | Sim | Sim, na inclusão |
| `DHINC` | "Data" | Principal | — | Não, gravado pelo sistema |
| `CODCTABCOINT` | "Conta Cheque" | Principal | Sim | Sim |
| `CODTIPTIT` | "Tipo Titulo Cheque" | Principal | Sim | Sim |
| `CODTIPOPER` | "TOP Lanc. Banc." | Principal | Sim | Sim |
| `CODTIPOPERREC` | "TOP Recebimento" | Principal | Sim | Sim |
| `CODTIPOPERPAG` | "TOP Pagamento" | Principal | Sim | Sim |
| `CODNAT` | "Natureza" | Principal | Sim | Sim |
| `CODCENCUS` | "Centro Resultado" | Principal | Sim | Sim |
| `CODNATTROCOREC` | "Natureza Troco Receita" | Troco | Sim | Sim |
| `CODNATTROCODESP` | "Natureza Troco Despesa" | Troco | Sim | Sim |
| `CODTIPOPERTROCOREC` | "TOP Troco Receita" | Troco | Sim | Sim |
| `CODTIPOPERTROCODESP` | "TOP Troco Despesa" | Troco | Sim | Sim |
| `CODNATCREDREC` | "Natureza Credito Receita" | Credito | Sim | Sim |
| `CODNATCREDDESP` | "Natureza Credito Despesa" | Credito | Sim | Sim |
| `CODTIPOPERCREDREC` | "TOP Credito Receita" | Credito | Sim | Sim |
| `CODTIPOPERCREDDESP` | "TOP Credito Despesa" | Credito | Sim | Sim |
| `CODNATDEVREC` | "Natureza Receita Devolução" | Devolução | Não | Sim |
| `CODNATDEVDESP` | "Natureza Despesa Devolução" | Devolução | Não | Sim |
| `CODTIPOPERRECDEV` | "TOP Devolução Receita" | Devolução | Sim | Sim |
| `CODTIPOPERDESPDEV` | "TOP Devolução Despesa" | Devolução | Sim | Sim |
| `CODRELRAST` | "Relatório Rastreamento" | Relatórios | Sim | Sim |
| `CODRELRECI` | "Relatório Recibo" | Relatórios | Sim | Sim |
| `IMPREC` | "Imprime Recibo no Recebimento?" | Relatórios | Não | Sim |
| `IMPDESP` | "Imprime Recibo no Pagamento?" | Relatórios | Não | Sim |
| `CODNATADT*` / `CODTIPOPERADT*` | Naturezas e TOPs de adiantamento | Adiantamento | Não | Ocultos na tela |
| `DHTIPOPER` | Data do tipo de operação | — | Não | Oculto na tela |

#### 1.9 Como a rotina escolhe a configuração vigente

A chave da configuração é o par **empresa + data**. Em cada operação, a Ficha de Cheque busca a configuração de **maior data** daquela empresa.

- **Incluir** uma configuração cria uma nova versão, que passa a valer para as operações seguintes. A anterior permanece gravada.
- **Editar** a configuração vigente altera aquela versão no lugar: a data não muda e o valor anterior é perdido.
- A listagem da tela exibe apenas a versão vigente de cada empresa.

| **ATENÇÃO:** Para preservar o histórico ao mudar uma regra — trocar a conta do cheque ou uma TOP, por exemplo — **inclua uma nova configuração** em lugar de editar a vigente. A edição sobrescreve a versão que explicava as operações já registradas. |
| --- |

| **Dica:** Use o botão de cópia da barra de ferramentas para partir da configuração vigente e ajustar apenas o que mudou. |
| --- |

#### 1.10 Parâmetros do módulo

Além desta configuração por empresa, o módulo tem parâmetros de sistema que valem para todo o ambiente. Eles são mantidos na rotina de parâmetros do **Sankhya Om**, e não nesta tela.

| Parâmetro | Descrição | Padrão |
| --- | --- | --- |
| **PREPARACUSTODIA** | FICHACHEQUE Prepara cheque para custódia? | Ativo |
| **PERAJUSTEPREDT** | FICHACHEQUE Permite ajuste pré data? | Inativo |
| **PERCODBARDUPLO** | FICHACHEQUE Permite 2 Chq mesmo Cód. Barras? | Inativo |
| **BLOQPARCFCH** | FICHACHEQUE Bloquear parceiro dev? | Inativo |
| **VALCHQHJ** | FICHACHEQUE Valida Utilizar Chq Com data De Hoje? | Inativo |
| **DEPOSITOSANGRIA** | FICHACHEQUE Possibilita Deposito após sangria | Inativo |
| **SALDORESIDUAL** | FICHACHEQUE Retém cheque com saldo residual? | Inativo |
| **TRANSFCTACX** | Transfere da conta caixa para conta cheque? | Inativo |

| **Essencial:** Com **TRANSFCTACX** ativo, a operação exige usuário configurado como caixa **com conta bancária vinculada**, e essa conta precisa ser **diferente** da "Conta Cheque" da configuração. Do contrário a rotina para antes de qualquer baixa. |
| --- |

#### 1.11 Situações comuns e como resolver

| O que aconteceu | Por que | O que fazer |
| --- | --- | --- |
| A Ficha de Cheque reclama de configuração inexistente | A empresa da operação não tem registro em Configuração de Cheques | Cadastre a configuração daquela empresa |
| A Ficha de Cheque reclama de conta, tipo de título ou TOP | O campo está vazio na configuração vigente | Complete o campo e salve |
| A decisão "Troco" ou "Credito" falha na operação | As naturezas ou TOPs da aba correspondente estão vazias | Complete as abas Troco e Credito |
| O recibo não é impresso ao concluir a baixa | A marcação de impressão está desmarcada, ou o relatório não está informado | Marque a opção de impressão e informe "Relatório Recibo" |
| O botão "Relatório Rastreamento" não abre nada | O campo "Relatório Rastreamento" está vazio | Informe o relatório na configuração |
| A operação para citando a conta do caixa igual à do cheque | O usuário caixa está vinculado à mesma conta configurada para cheques | Vincule ao usuário uma conta caixa distinta |
| Uma alteração da configuração não parece ter efeito | A alteração foi feita em uma versão que não é a vigente | Confira o campo "Data": a rotina usa sempre a configuração de maior data da empresa |

#### 1.12 FAQ — Perguntas e erros mais frequentes

##### Cadastro e vigência

- **Preciso de uma configuração por empresa?**

Sim. A rotina busca a configuração pela empresa da operação. Empresa sem configuração não opera cheques.

- **Por que o campo "Data" não é editável?**

A data é a parte da chave que versiona a configuração. O sistema a grava com a data e hora da inclusão, para que a rotina saiba qual versão é a vigente. Por ser chave, ela não muda depois.

- **Alterei a configuração. A alteração vale para operações antigas?**

Depende de como a alteração foi feita. Incluir uma configuração cria uma nova versão e preserva a anterior, que continua explicando as operações já registradas. Editar a configuração vigente altera aquela mesma versão — e aí as operações antigas passam a apontar para os valores novos. Para mudanças de regra, prefira incluir.

- **A tela não mostra as configurações antigas. Elas foram apagadas?**

Não. A listagem exibe apenas a versão vigente de cada empresa; as anteriores permanecem gravadas na tabela `CTCCON`.

- **Posso excluir uma configuração?**

A barra de ferramentas permite a exclusão, mas remover a versão vigente deixa a empresa sem configuração e interrompe a Ficha de Cheque. Prefira incluir uma nova versão corrigida.

##### Mensagens que aparecem na Ficha de Cheque

- **"Necessário cadastrar a configuração da Empresa <n>." — o que fazer?**

Cadastrar a configuração daquela empresa nesta rotina.

- **"Necessário informar a conta na configuração." — qual campo?**

O campo "Conta Cheque".

- **"Necessário informar o Tipo de Operação para Pagamento, no cadastro de configuração da empresa selecionada." — qual campo?**

O campo "TOP Pagamento".

- **"Necessário informar o Tipo de Operação para Recebimento, no cadastro de configuração da empresa selecionada." — qual campo?**

O campo "TOP Recebimento".

- **"Necessário informar a conta na Tipo De Titulo Cheque, no cadastro de configuração da empresa selecionada." — qual campo?**

Apesar da redação, o campo é "Tipo Titulo Cheque".

- **"Algum erro no retorno da do banco da conta informada." — o que verificar?**

A conta bancária informada em "Conta Cheque" — ou a conta vinculada ao usuário caixa — está sem banco no cadastro. Informe o banco no cadastro da conta bancária.

- **"Usuário configurado para caixa, mas nao possui conta vinculada" — onde resolvo?**

No cadastro de contas bancárias, vinculando a conta ao operador de caixa.

- **"A conta caixa vinculada ao usuário é a mesma conta de cheques da configuração (<n>)." — por quê?**

A transferência gerada na baixa vai da conta do caixa para a conta do cheque. Contas iguais tornariam origem e destino idênticos, e o lançamento seria rejeitado.

- **"O parâmetro de transferência (TRANSFCTACX) para a conta do caixa está ativo…" — o que escolher?**

Vincule a conta ao usuário caixa, ou desative o parâmetro se a transferência entre contas não for desejada no ambiente.

#### Campos e abas

- **Preciso preencher a aba Adiantamento?**

Não. Os campos estão ocultos na tela e nenhum fluxo atual os consome.

- **Qual a diferença entre "TOP Lanc. Banc.", "TOP Recebimento" e "TOP Pagamento"?**

"TOP Lanc. Banc." vale para os lançamentos bancários de transferência — sangria, depósito e complemento de valor. "TOP Recebimento" e "TOP Pagamento" valem para a baixa dos títulos a receber e a pagar, respectivamente, e para as transferências de entrada e saída da conta do caixa.

- **Quando as naturezas de troco e de crédito são usadas?**

No Complemento Financeiro da Ficha de Cheque, quando o cheque cobre mais que os títulos e a operação decide registrar a diferença como troco ou como crédito do parceiro.

- **Onde vejo o efeito de "Imprime Recibo no Recebimento?"**

Ao concluir um recebimento na Ficha de Cheque: com a marcação ativa, o recibo é gerado com o relatório de "Relatório Recibo" e o número do lote.

| Acesse também  - Guia do usuário da rotina Ficha de Cheque (`docs/fichaCheque/GUIA_USUARIO_FICHA_CHEQUE.md`) e a documentação técnica da Configuração de Cheques (`docs/configuracaoCheque/CONFIGURACAO_CHEQUE_Documentacao_Tecnica.md`).   Este guia descreve o comportamento da rotina conforme implementado no addon. Em caso de divergência entre o guia e o sistema, prevalece o comportamento do sistema — reporte a diferença à equipe responsável pelo módulo. |
| --- |

### Ficha de Cheque: controle de cheques de terceiros, do recebimento à baixa

#####

**O que será feito:** cada cheque de terceiro entra uma vez na ficha, recebe um número único e, a partir daí, tudo o que acontece com ele vira um movimento registrado. Enquanto o cheque circula, a rotina cria e baixa títulos financeiros e lançamentos bancários no **Sankhya Om**, sempre amarrados ao cheque por um **lote** — é esse lote que permite estornar a operação inteira depois.

![Imagem 2: O que será feito: cada cheque de terceiro entra uma vez na ficha, recebe um número único e, a partir daí, tudo o que…](https://ajuda.sankhya.com.br/hc/article_attachments/43655511057815)

| **Definições: Lote** — o pacote de uma operação: reúne, sob um mesmo número, o cheque, os títulos financeiros e os lançamentos bancários gerados. **Movimento** — o registro do que aconteceu com o cheque; é o último movimento vivo que define o `Status Cheque`. **Cheque do acerto** — quando a operação usa vários cheques, um deles responde pelos títulos de acerto (troco, crédito, pendência, complemento). **Saldo do Cheque** — o valor do cheque menos o que já foi consumido em pagamentos não estornados. |
| --- |

| **Essencial:** Antes do primeiro uso, a empresa precisa estar cadastrada na rotina Configuração de Cheques. Sem conta do cheque, tipo de título e tipos de operação de recebimento e pagamento configurados, nenhuma operação conclui. |
| --- |

#### 2.1 Como acessar e localizar cheques

Acesse **Sankhya Om** → SOP Ficha de Cheques → Rotinas → **"Ficha de Cheque"**. A tela abre em duas partes: o painel de filtros à esquerda e a grade de cheques à direita. Dê duplo clique em uma linha para alternar entre grade e formulário.

No painel **"Filtros Rápidos"**, acione as chaves conforme o conjunto desejado:

| Filtro | O que traz |
| --- | --- |
| **"A Receber"** | cheques ainda não recebidos (status `NVO`) |
| **"A Pagar"** | cheques Em Caixa, disponíveis para pagar despesa (status `REC`) |
| **"Em Caixa"** | mesmo conjunto de "A Pagar" (status `REC`) |
| **"Baixado"** | cheques com movimento de depósito |
| **"Devolvido"** | cheques devolvidos (status `DEV`) |

Complete com **"Empresa"**, **"Parceiro"**, **"Pré-data"**, **"Nro. Único Cheque"** e **"Nro. Cheque"**, e clique em **"Aplicar"** para recarregar a grade.

| **OBSERVAÇÕES:** As chaves **"A Pagar"** e **"Em Caixa"** selecionam o mesmo conjunto de cheques. O rótulo "A Pagar" existe para o fluxo de pagamento a fornecedor: o cheque só tem lastro para pagar despesa depois que o recebimento o vinculou aos títulos de receita. |
| --- |

#### 2.2 Etapa 1 — Cadastrar o cheque

O cadastro parte da leitura do **CMC7**, a tarja do cheque. Nada é digitado à mão.

**(1)** Clique em **"Adicionar Novo"**.

**(2)** Na janela de leitura do CMC7, passe o cheque na leitora ou informe a tarja.

**(3)** Confirme. O sistema preenche sozinho **"Nro. do cheque"**, **"Cód. Barras"**, **"Banco Cheque"**, **"Agencia Cheque"**, **"Conta Cheque"**, **"CPF/CGC do Cheque"**, **"Nome Emitente"**, **"Valor"** e **"Bom para"**, e grava o registro.

**(4)** Se **"Dt. Entrada"** estiver vazia, o sistema assume a data corrente.

**(5)** O sistema também grava Dt. Cadastro e Usuario Alteração na inclusão, e a conta do cliente é salva junto pela própria janela de CMC7.

| **ATENÇÃO:** O código de barras é único por cheque. Ao tentar cadastrar um segundo cheque com o mesmo código de barras, o sistema recusa com **"Já Existe um Cheque com este Código de Barras, não é possível criar outro cheque com o mesmo Código de Barras."** Para permitir a repetição, ative o parâmetro **PERCODBARDUPLO**. Cheques marcados como troco não passam por essa validação. |
| --- |

| **Dica:** Com o parâmetro **VALCHQHJ** ativo, o sistema recusa cheque com "Bom para" anterior à data de hoje, na inclusão e no recebimento, com a mensagem **"Rotina Configurada para não receber Cheques com data menor que HOJE"**. |
| --- |

#### 2.3 Etapa 2 — Receber do cliente

O recebimento é o que dá lastro ao cheque: ele vincula o cheque aos títulos a receber que está quitando. Só depois disso o cheque pode pagar despesa, sofrer sangria ou ser depositado.

**(1)** Na grade, marque os cheques a receber. O botão **"Receber"** fica disponível apenas para cheque com status **Novo**.

**(2)** Clique em **"Receber"**. Abre a janela Recebimento Cliente.

**(3)** Informe **"Parceiro"** e **"Empresa"** e clique em **"Aplicar"**. A grade Titulos do Parceiro carrega os títulos a receber em aberto do parceiro e da empresa informados.

**(4)** Ajuste a seleção com **"Remove Selecionado(s)"** e **"Remove NÃO Selecionado(s)"**.

**(5)** Na grade Cheques Selecionados, confira os cheques e escolha o **"Cheque do acerto"**. Com um único cheque, o campo já vem preenchido.

**(6)** Acompanhe o rodapé: **"Total Financeiro"**, **"Total Cheque"** e **"Saldo"**.

**(7)** Clique em **"Efetivar Recebimento"**. Abre a janela Complemento Financeiro — ver a etapa seguinte.

| **OBSERVAÇÃO:** O título de **menor valor** da seleção fica de fora da baixa automática e recebe a baixa individual, que é onde a pendência, o desconto ou os juros da diferença são aplicados. A comparação é pelo valor líquido do título, não pelo número. |
| --- |

| **Atenção:** Sem o **"Cheque do acerto"** a operação não prossegue: o sistema exibe **"Informe o cheque do acerto antes de efetivar o recebimento."** |
| --- |

#### 2.4 Etapa 3 — Decidir a diferença no Complemento Financeiro

A janela Complemento Financeiro existe para resolver a diferença entre o que os títulos somam e o que os cheques cobrem. O que ela oferece muda conforme o fluxo e o parâmetro **SALDORESIDUAL**.

Informe a **"Dt. Baixa"** — campo obrigatório — e escolha uma decisão quando houver diferença:

| Situação | No recebimento | No pagamento |
| --- | --- | --- |
| Cheque cobre exatamente o financeiro | nada a decidir; a baixa é automática | nada a decidir |
| Cheque cobre **menos** que o financeiro | **"Pendencia"** ou **"Desconto"** | somente **"Pendencia"** |
| Cheque cobre **mais** que o financeiro | **"Juros"**, **"Troco"** ou **"Credito"** | **"Troco"** ou **"Credito"** — nenhuma decisão quando o cheque é retido com saldo |

| **Calculadora**  `Saldo = Total Financeiro − Total Cheque`. Saldo **positivo** significa cheque insuficiente; saldo **negativo**, cheque com sobra. |
| --- |

Duas faixas de aviso aparecem quando o caso pede:

- **Baixa parcial** (pagamento com cheque insuficiente): a faixa mostra **"Será baixado"** e **"Permanece em aberto"**. O título é desdobrado — parte é baixada, o restante segue em aberto como pendência.
- **Sobra retida no cheque** (pagamento com **SALDORESIDUAL** ativo): a faixa informa que a sobra fica como saldo do cheque, que continua Em Caixa para o próximo pagamento. Nesse caso as cinco chaves ficam desabilitadas de propósito.

Ao final, clique em **"Finalizar Operação"**. No recebimento a tela dispara a baixa dos títulos e depois registra a movimentação do cheque; no pagamento a tela apenas registra a movimentação, e a baixa da despesa acontece no servidor, pela rotina nativa de baixa de títulos de despesa com cheque.

| **ATENÇÃO:** Havendo diferença e nenhuma chave acionada, o sistema exibe **"Favor preencha a decisão."** e não prossegue. Sem data de baixa, exibe **"É necessário informar uma data para baixa."** |
| --- |

#### 2.5 Etapa 4 — Pagar um fornecedor com o cheque

O cheque recebido de um cliente pode quitar títulos a pagar de um fornecedor, sem passar pelo banco.

**(1)** Na grade, marque os cheques. O botão **"Pagar"** fica disponível apenas para cheque **Em Caixa**.

**(2)** Clique em **"Pagar"**. Abre a janela Pagamento a Fornecedor, com o mesmo desenho da tela de recebimento.

**(3)** Informe **"Parceiro"** e **"Empresa"** e clique em **"Aplicar"**. A grade traz os títulos **a pagar** em aberto.

**(4)** Escolha o **"Cheque do acerto"** e clique em **"Efetivar Pagamento"**.

**(5)** Resolva a diferença na janela Complemento Financeiro e clique em **"Finalizar Operação"**.

| **ATENÇÃO:** Somente cheque Em Caixa paga despesa. Ao marcar cheques em outros status, a tela recusa a abertura com **"Somente cheque Em Caixa paga despesa. Fora desse status: <números>."** O servidor repete a validação, e é ele que barra chamadas feitas fora da tela. |
| --- |

| **OBSERVAÇÃO**: O pagamento com cheque **não concede desconto** sobre a diferença. A rotina só sabe deixar o saldo restante em aberto — por isso a decisão disponível é "Pendencia". |
| --- |

| **Versão:** Com o parâmetro **SALDORESIDUAL** ativo, o mesmo cheque paga mais de uma despesa: a cada pagamento ele consome parte do valor e segue Em Caixa enquanto sobrar saldo. Com o parâmetro desativado, o cheque sai da carteira inteiro e a sobra vira troco ou crédito. |
| --- |

#### 2.6 Etapa 5 — Sangria e depósito

As duas ações transferem o valor do cheque entre contas bancárias e registram a saída do cheque da carteira. A diferença é o destino.

**Sangria** — disponível para cheque Em Caixa. É a passagem do cheque do operador de caixa para a conta de cheques da empresa. **Depósito** — disponível para cheque Em Caixa ou em custódia. É a entrega do cheque ao banco.

**(1)** Marque os cheques na grade e clique em **"Sangria"** ou **"Deposito"**.

**(2)** Informe **"Conta para Sangria"** / **"Conta para Deposito"** e **"Data do Depósito"**, e confirme.

**(3)** Confirme a pergunta **"Deseja realizar a Sangria/Depósito do(s) cheque(s) selecionado(s)?"**

O sistema gera um lançamento bancário de transferência, registra o movimento do cheque (`CUS` na sangria, `DEP` no depósito) e preenche os dados de saída do cheque.

| **ATENÇÃO:** Usuário configurado como caixa não transfere para o banco: **"Usuario caixa não pode transferir para o Banco"**. O destino da sangria de um usuário caixa deve ser a conta de cheques da configuração: **"O destino da Sangria deve ser a conta cadastrada de cheque"**. Cheque já depositado e não estornado é recusado: **"Este Cheque ja foi depositado, não é possivel depositar novamente"**. O depósito exige parceiro cadastrado na empresa ou na conta bancária: **"Para realizar um deposito é necessário o cadastro do Parceiro na Empresa ou na Conta Bancária."** |
| --- |

| **Dica:** Com o parâmetro **DEPOSITOSANGRIA** ativo, o cheque que passou por sangria pode ser depositado depois, e o depósito parte da conta de destino da sangria. |
| --- |

#### 2.7 Etapa 6 — Devolver o cheque

A devolução registra o cheque que voltou do banco e gera a contrapartida financeira. O botão **"Devolver"** fica disponível para cheque em custódia, depositado ou que pagou despesa.

| **OBSERVAÇÃO**: "Que pagou despesa" é o cheque **consumido por inteiro** no pagamento, que aparece com status Pago. Cheque consumido só em parte continua Em Caixa enquanto sobrar saldo — nesse status a rotina oferece Receber, Pagar, Sangria e Depósito, não Devolver. |
| --- |

**(1)** Marque os cheques e clique em **"Devolver"**.

**(2)** Na janela Informe os Dados para Devolução, informe todos os campos: **"Tipo de Operação Receita"**, **"Tipo de Operação Despesa"**, **"Natureza"**, **"Centro de Resultado"**, **"Tipo de Titulo"**, **"Alíneas de Devolução de Cheques"**, **"Conta Cheque"** e **"Data da Devolução"**.

**(3)** Confirme a pergunta **"Deseja realmente devolver o(s) cheque(s) selecionado(s)?"**

O sistema cria o título financeiro da devolução, o lançamento bancário correspondente, registra o movimento `DEV` com a alínea informada e limpa o lote de entrada do cheque — o que retira o cheque do conjunto disponível para nova devolução.

| **Versão:** Quando o cheque devolvido havia pagado uma despesa, o **título de despesa reabre em aberto**: o sistema estorna a baixa pela mesma rotina do estorno de pagamento, devolve a conta bancária original ao título e restaura o histórico anterior à baixa. Antes, o sistema criava um par de títulos novos de receita e despesa para o parceiro de saída, sem vínculo com o título pago. |
| --- |

| **ATENÇÃO:** Duas regras convivem na devolução, e a diferença é proposital. O título de **receita** que originou o cheque **não reabre**: a devolução gera títulos novos e marca o original com o número da devolução, padrão da plataforma. O título de **despesa** pago com o cheque **reabre**, por estorno da baixa — mecanismo diferente, e legítimo: a obrigação com o fornecedor volta a existir porque o pagamento não se sustentou. |
| --- |

| **OBSERVAÇÃO:** O cheque devolvido fica **sem saldo disponível**, mesmo que tenha sido consumido só em parte — ele não volta a pagar despesa. |
| --- |

| **ATENÇÃO**: A alínea da devolução anterior decide se o cheque pode ser reapresentado. Alínea que não permite reapresentação faz o sistema recusar com **"Devolução anterior não permite reapresentação"**. |
| --- |

| **OBSERVAÇÃO:** Com o parâmetro **BLOQPARCFCH** ativo, o parceiro do cheque devolvido é bloqueado automaticamente, com motivo "Devolução Cheque". |
| --- |

#### 2.8 Etapa 7 — Estornar uma operação

O estorno desfaz o **último lote** relacionado ao cheque: reabre os títulos, remove os lançamentos bancários e os títulos de acerto, devolve os dados de entrada ou de saída ao cheque e marca o movimento como estornado.

**(1)** Marque os cheques e clique em **"Estornar"**. O botão fica disponível para qualquer cheque que já tenha movimento.

**(2)** Confirme a pergunta **"Deseja realizar o estorno do último lote relacionado ao cheque?"**

**(3)** Ao concluir, o sistema informa **"Estorno Concluido!"**

O estorno é sempre do lote inteiro. Se a operação original usou vários cheques, **todos** precisam estar marcados.

| **MENSAGEM:** Cheque devolvido não é estornado: **"Não é possivel estornar Cheque Devolvido."** Cheques de lotes diferentes não são estornados juntos: **"Não é possivel prosseguir, cheque selecionados não são do mesmo lote de Baixa!"** Cheque que ainda não faz parte de um movimento não é estornado, e sim excluído: **"Lançamento ainda não faz parte de um movimento, não é possivel estornar! Só é possivel Excluir!"** |
| --- |

| **ATENÇÃO:** Faltando cheques do lote, o sistema lista os que faltam: **"Lançamento faz parte de um Recebimento Agrupado! Selecione todos os cheques para prosseguir com o estorno <números>"**, e no pagamento **"O pagamento do lote <n> foi feito com mais de um cheque, e o estorno desfaz o lote inteiro. Selecione tambem o(s) cheque(s): <números>."** Cheque do lote com movimento posterior impede o estorno do pagamento. Título do lote não baixado também impede: **"não é possivel realizar o Estorno, pois um dos financeiro nufin <n> do Lote <n> não está baixado."** |
| --- |

| **OBSERVAÇÃO:** No estorno de um **pagamento**, o financeiro volta pela rotina nativa: a transferência do cheque é removida, a conta bancária original volta ao título, o desdobramento da baixa parcial é recomposto e o histórico anterior à baixa é devolvido ao título. O saldo do cheque volta por consequência de o movimento ser marcado como estornado. |
| --- |

#### 2.9 Excluir um cheque

O botão **"Excluir"** apaga o cadastro do cheque. Só cheque **sem nenhum movimento** pode ser excluído.

Cheque com lote de entrada ou de saída preenchido é recusado com **"Não possivel apagar um cheque já movimentado."** Nesse caso, estorne o movimento antes.

#### 2.10 Relatório de rastreamento e recibo

**"Relatório Rastreamento"** — clique no botão, confirme **"Deseja imprimir o cheque selecionado?"** e o sistema abre, em nova aba, o relatório configurado no campo **"Relatório Rastreamento"** da rotina Configuração de Cheques, com o número único do cheque como parâmetro.

**Recibo** — a impressão do recibo é automática ao final da baixa, e depende das marcações da configuração: **"Imprime Recibo no Recebimento?"** para o recebimento e **"Imprime Recibo no Pagamento?"** para o pagamento. O recibo usa o relatório do campo **"Relatório Recibo"** e recebe o número do lote como parâmetro.

| **ATENÇÃO:** Para imprimir o recibo é obrigatório informar a empresa: **"Para Imprimir um recibo, é necessário informar uma Empresa"**. |
| --- |

#### 2.11 Campos da ficha

| Campo | Nome na tela | O que é | Editável? |
| --- | --- | --- | --- |
| `NUCHEQUE` | "Nro. único do cheque" | Identificador do cheque na ficha, gerado pelo sistema | Não |
| `NOSSONUM` | "Nro. do cheque" | Número impresso no cheque, lido do CMC7 | Não |
| `CODBARRA` | "Cód. Barras" | Tarja CMC7 completa | Não |
| `CODBCO_CMC7` | "Banco Cheque" | Banco do emitente | Não |
| `AGENCIA_CMC7` | "Agencia Cheque" | Agência do emitente | Não |
| `CONTA_CMC7` | "Conta Cheque" | Conta do emitente | Não |
| `CGC_CPF_CMC7` | "CPF/CGC do Cheque" | Documento do emitente | Não |
| `NOMEEMITENTE_CMC7` | "Nome Emitente" | Nome do emitente | Não |
| `VALOR` | "Valor" | Valor de face do cheque | Sim, até o cheque ter movimento |
| `DHBOM` | "Bom para" | Pré-data do cheque | Sim, conforme PERAJUSTEPREDT |
| `SALDO` | "Saldo do Cheque" | Valor menos o já consumido em pagamentos não estornados | Não |
| `STATUS` | "Status Cheque" | Situação atual, derivada do último movimento vivo | Não |
| `CODPARCINC` | "Parceiro Entrada" | Parceiro do recebimento | Sim, até o cheque ter movimento |
| `CODPARCSAI` | "Parceiro Saida" | Parceiro da saída (pagamento, sangria, depósito) | Não |
| `CODPARCORIG` | "Parceiro Origem" | Parceiro de origem, no cheque de troco | Não |
| `DHINC` / `DHSAI` | "Dt. Entrada" / "Dt. Saida" | Datas de entrada e de saída do cheque | Não |
| `LOTEINC` / `LOTESAI` | "Lote Entrada" / "Lote Saida" | Lotes das operações de entrada e de saída | Não |
| `ENTSAI` | "Entrada Saida" | Sentido do cheque | Não |
| `TROCO` | "Troco" | Indica cheque gerado como troco | Não |
| `NUCHEQUEORIG` / `LOTEORIG` | "Cheque Original" / "Lote Original" | Rastro do cheque que originou o troco | Não |
| `CODALINEADEV` | "Alinea Devolução" | Alínea da última devolução | Não |
| `CODEMP` | "Empresa" | Empresa da operação | Não |
| `ARQUIVO` | "Digilitalização" | Imagem do cheque, anexada na devolução | Sim |
| `DTCAD` | "Dt. Cadastro" | Data e hora do cadastro | Não |
| `CODUSUINC` / `CODUSUALT` | "Usuário da Inclusão" / "Usuario Alteração" | Usuários de inclusão e da última alteração | Não |

#### 2.12 Status do cheque

O **"Status Cheque"** não é digitado: o sistema o deriva do último movimento do cheque que ainda vale, desconsiderando estornos.

| Status | Significa | Botões disponíveis |
| --- | --- | --- |
| `NVO` | Novo — cadastrado, ainda não recebido | Receber, Excluir |
| `REC` | **Em Caixa** — recebido e em carteira | Pagar, Sangria, Deposito, Estornar |
| `CUS` | Em custódia — passou por sangria | Deposito, Devolver, Estornar |
| `DEP` | Depositado | Devolver, Estornar |
| `PGT` | Consumido em pagamento de despesa | Estornar |
| `DEV` | Devolvido | Estornar não se aplica |

| **OBSERVAÇÃO**: No pagamento parcial com o parâmetro **SALDORESIDUAL** ativo, o cheque que ainda tem saldo continua aparecendo como Em Caixa, e não como pago — é o saldo, e não o último movimento, que decide. |
| --- |

#### 2.13 Parâmetros que mudam o comportamento

| Parâmetro | Descrição | Padrão | Efeito |
| --- | --- | --- | --- |
| **PREPARACUSTODIA** | Prepara cheque para custódia? | Ativo | Habilita o registro de custódia na sangria |
| **PERAJUSTEPREDT** | Permite ajuste pré data? | Inativo | Inativo, bloqueia a alteração de "Bom para" de cheque movimentado |
| **PERCODBARDUPLO** | Permite 2 Chq mesmo Cód. Barras? | Inativo | Ativo, aceita cheques com o mesmo código de barras |
| **BLOQPARCFCH** | Bloquear parceiro dev? | Inativo | Ativo, bloqueia o parceiro do cheque devolvido |
| **VALCHQHJ** | Valida Utilizar Chq Com data De Hoje? | Inativo | Ativo, recusa cheque com pré-data anterior a hoje |
| **DEPOSITOSANGRIA** | Possibilita Deposito após sangria | Inativo | Ativo, permite depositar cheque que passou por sangria |
| **SALDORESIDUAL** | Retém cheque com saldo residual? | Inativo | Ativo, o cheque é retido e consome saldo a cada pagamento |
| **TRANSFCTACX** | Transfere da conta caixa para conta cheque? | Inativo | Ativo, exige usuário caixa com conta vinculada e gera a transferência entre contas |

#### 2.14 Situações comuns e como resolver

| O que aconteceu | Por que | O que fazer |
| --- | --- | --- |
| O botão "Pagar" está desabilitado | O cheque não está Em Caixa | Receba o cheque antes de usá-lo para pagar despesa |
| A tela recusa o pagamento citando cheques fora do status | A seleção tem cheque que não está Em Caixa | Desmarque os cheques citados na mensagem |
| No Complemento Financeiro todas as chaves estão desabilitadas e há sobra | O cheque é retido e a sobra fica como saldo dele | Nada a decidir; confirme a operação |
| A opção "Desconto" não aparece no pagamento | O pagamento com cheque não concede desconto | Escolha "Pendencia" |
| O estorno reclama de cheques não selecionados | A operação foi feita com vários cheques e o estorno desfaz o lote inteiro | Marque todos os cheques citados e repita |
| O estorno reclama de movimento posterior | Outro cheque do lote já foi depositado ou custodiado | Estorne primeiro o movimento mais recente daquele cheque |
| A exclusão é recusada | O cheque já tem lote de entrada ou de saída | Estorne o movimento e depois exclua |
| A baixa do título pela Movimentação Financeira é recusada | O título está vinculado a um cheque | Faça a baixa pela rotina Ficha de Cheque |
| A operação para por falta de configuração | A empresa não tem configuração completa | Complete a rotina Configuração de Cheques |

#### 1.15 FAQ — Perguntas e erros mais frequentes

##### Cadastro do cheque

- **"Já Existe um Cheque com este Código de Barras, não é possível criar outro cheque com o mesmo Código de Barras." — como resolver?**

O código de barras lido já pertence a outro cheque da ficha. Confira se o cheque não foi cadastrado antes. Para permitir a repetição de propósito, ative o parâmetro PERCODBARDUPLO.

- **"Rotina Configurada para não receber Cheques com data menor que HOJE" — por que aparece?**

O parâmetro VALCHQHJ está ativo e o campo "Bom para" tem data anterior à data corrente. Corrija a pré-data ou desative o parâmetro.

- **"Não é possivel alterar a pré data de um cheque movimentado. Verifique o parâmetro PERAJUSTEPREDT" — o que fazer?**

A alteração de "Bom para" está bloqueada. Ative o parâmetro PERAJUSTEPREDT para liberar o ajuste.

- **"Não é possivel alterar valor de um cheque que já tenha movimentos." — posso contornar?**

Não pela edição. Estorne o movimento e refaça a operação, ou trate a diferença por título de acerto. A mesma trava vale para o valor e o parceiro de origem de um cheque de troco.

- **"Não possivel apagar um cheque já movimentado." — como excluir?**

Estorne o movimento do cheque. Sem lote de entrada e sem lote de saída, a exclusão é liberada.

##### Recebimento e pagamento

- **"Informe o cheque do acerto antes de efetivar o recebimento." — o que é o cheque do acerto?**

É o cheque que responde pela operação nos títulos de acerto — troco, crédito, pendência e complemento. Escolha um dos cheques no campo "Cheque do acerto".

- **"Somente cheque Em Caixa paga despesa. Fora desse status: <números>." — por quê?**

Cheque só tem lastro para pagar despesa depois que o recebimento o vinculou aos títulos de receita. Receba os cheques citados ou desmarque-os.

- **"O cheque <n> nao esta Em Caixa e por isso nao pode pagar despesa." — qual a diferença da mensagem anterior?**

Essa vem do servidor e aparece também quando o serviço é chamado fora da tela. A causa é a mesma.

- **"O cheque <n> nao tem saldo disponivel e por isso nao pode pagar despesa. Ele ja foi usado por inteiro em outros pagamentos." — o que fazer?**

O cheque foi consumido por completo em pagamentos anteriores. Use outro cheque ou estorne um dos pagamentos anteriores.

- **"O cheque <n> nao tem titulo de receita no lote de entrada, exigido para pagar despesa." — como resolver?**

O cheque não tem vínculo com títulos de receita, o que acontece quando ele não foi recebido pela rotina. Faça o recebimento antes do pagamento.

- **"O pagamento com cheque nao concede desconto sobre a diferenca. Escolha Pendencia para deixar o saldo restante em aberto." — por quê?**

No pagamento, a rotina só sabe desdobrar o título e deixar o saldo em aberto. Escolha "Pendencia".

- **"Os cheques nao cobrem o total das despesas, e o pagamento com cheque so sabe deixar o saldo restante em aberto." — o que muda no título?**

O título é desdobrado: a parte coberta pelos cheques é baixada e o restante permanece em aberto, com histórico indicando a origem no cheque.

- **"Favor preencha a decisão." — qual decisão?**

Existe diferença entre o total dos títulos e o total dos cheques, e nenhuma chave foi acionada no Complemento Financeiro. Escolha a decisão adequada ao caso.

- **"Não é possível prosseguir, selecione o título para gerar a pendência!" — o que verificar?**

O valor calculado para a pendência ficou negativo, o que indica seleção de títulos incompatível com o valor dos cheques. Revise os títulos selecionados.

- **"É necessário informar uma data para baixa." — onde informo?**

No campo "Dt. Baixa" da janela Complemento Financeiro.

- **"Titulo só pode ser baixado pela tela controle de cheque, pois está vinculado a um cheque." — por que aparece na Movimentação Financeira?**

O título faz parte de um lote de cheque vivo. A baixa e o estorno desse título têm de acontecer pela rotina Ficha de Cheque, para que o cheque acompanhe a operação.

##### Sangria, depósito e devolução

- **"Usuario caixa não pode transferir para o Banco" — o que o caixa pode fazer?**

Sangria para a conta de cheques da empresa. O depósito bancário é feito por usuário que não seja caixa.

- **"O destino da Sangria deve ser a conta cadastrada de cheque" — qual conta informar?**

A conta do campo "Conta Cheque" da rotina Configuração de Cheques da empresa.

- **"Este Cheque ja foi depositado, não é possivel depositar novamente" — e se o depósito foi errado?**

Estorne o depósito e refaça a operação.

- **"Para realizar um deposito é necessário o cadastro do Parceiro na Empresa ou na Conta Bancária." — onde cadastro?**

No cadastro da empresa ou no cadastro da conta bancária de destino, informando o parceiro correspondente.

- **"Devolução anterior não permite reapresentação" — o que significa?**

A alínea da devolução anterior não admite reapresentação do cheque. Confira a alínea no cadastro de alíneas de devolução.

##### Estorno

- **"Não é possivel estornar Cheque Devolvido." — como corrigir uma devolução errada?**

A devolução não é desfeita pelo estorno da ficha. Trate a correção pelos títulos financeiros gerados, com apoio da equipe do módulo.

- **"Não é possivel prosseguir, cheque selecionados não são do mesmo lote de Baixa!" — como estornar então?**

Um lote por vez. Marque somente os cheques de um mesmo lote e repita a operação para os demais. No fluxo de pagamento, a mensagem equivalente é "Os cheques selecionados nao sao do mesmo lote de pagamento".

- **"Lançamento ainda não faz parte de um movimento, não é possivel estornar! Só é possivel Excluir!" — qual o caminho?**

O cheque nunca foi movimentado. Use "Excluir".

- **"O titulo de despesa <n> nao tem movimento bancario de baixa, entao o pagamento com cheque nao pode ser estornado." — o que investigar?**

O título foi baixado por outra rotina, sem o lançamento bancário que o estorno usa como ponto de partida. Trate o estorno pela rotina que fez a baixa.

- **Depois do estorno, o título ficou com valor menor que o original. Por quê?**

A recomposição do desdobramento da baixa parcial não aconteceu. O sistema registra um alerta no log do servidor nesse caso. Acione a equipe responsável pelo módulo.

##### Configuração e ambiente

- **"Necessário cadastrar a configuração da Empresa <n>." — onde cadastro?**

Na rotina Configuração de Cheques, uma configuração por empresa.

- **"Necessário informar a conta na configuração." e as demais mensagens de configuração — quais campos?**

Respectivamente, "Conta Cheque", "TOP Pagamento", "TOP Recebimento" e "Tipo Titulo Cheque" da configuração da empresa.

- **"A conta caixa vinculada ao usuário é a mesma conta de cheques da configuração (<n>)." — por que isso importa?**

A transferência gerada na baixa sai da conta do caixa para a conta do cheque. Contas iguais tornariam origem e destino idênticos, e o lançamento seria rejeitado.

- **"O parâmetro de transferência (TRANSFCTACX) para a conta do caixa está ativo…" — o que escolher?**

Vincule uma conta bancária ao usuário caixa ou desative o parâmetro TRANSFCTACX se a transferência não for desejada.

- **"Nenhuma digitalização encontrada" — onde anexo a imagem do cheque?**

O arquivo é anexado ao cheque no fluxo de devolução e fica no campo "Digilitalização".

| Acesse também  - Guia do usuário da rotina Configuração de Cheques (`docs/configuracaoCheque/GUIA_USUARIO_CONFIGURACAO_CHEQUE.md`) e a documentação técnica da Ficha de Cheque (`docs/fichaCheque/FICHA_CHEQUE_Documentacao_Tecnica.md`).  Este guia descreve o comportamento da rotina conforme implementado no addon. Em caso de divergência entre o guia e o sistema, prevalece o comportamento do sistema — reporte a diferença à equipe responsável pelo módulo. |
| --- |

### Talão de Cheque (Próprio): do talão recebido do banco à folha virar cheque

**O que será feito:** o talão que chega da agência é cadastrado, as folhas são geradas em bloco e cada uma é acompanhada até virar cheque. A rotina **não paga nada** — quando a folha está assinada e pronta, ela é enviada para a **Ficha de Cheque**, e é lá que o pagamento ao fornecedor, o estorno e a devolução acontecem.

![Imagem 3: O que será feito: o talão que chega da agência é cadastrado, as folhas são geradas em bloco e cada uma é acompanhada…](https://ajuda.sankhya.com.br/hc/article_attachments/43655560358423)

#### 3.1 Como acessar e localizar talões

Acesse **Sankhya Om** → SOP Ficha de Cheques → Cadastros → **Talão de Cheque (Próprio)**.

A tela abre em duas partes: em cima o **talão**, embaixo a grade de **folhas** do talão selecionado. Cada folha, por sua vez, tem a grade de **histórico**.

Para localizar, use a pesquisa do cabeçalho por **"Número do Talão"**, **"Empresa"**, **"Conta Bancária Interna"** ou **"Situação"**. Na grade de folhas, a pesquisa alcança **"Número da Folha"**, **"Status da Folha"** e **"Valor"**.

| **Definições:**  **Talão** — o bloco recebido do banco, identificado pela conta bancária e pela faixa de numeração. **Folha** — cada cheque em branco do talão. É criada pela rotina, nunca à mão, e não pode ser excluída depois. **Envio para a Ficha** — o momento em que a folha vira um cheque próprio na rotina Ficha de Cheque. **Histórico da folha** — o registro de cada mudança de status, com data, usuário e justificativa. |
| --- |

| **Essencial:** A conta bancária do talão precisa existir em Contas Bancárias e a empresa em Empresas. Para o cheque próprio conseguir pagar despesa depois, a empresa também precisa estar configurada na rotina Configuração de Cheques — sem isso o envio funciona, mas o pagamento na Ficha não conclui. |
| --- |

#### 3.2 Etapa 1 — Cadastrar o talão

**(1)** Clique em **"Adicionar Novo"** no cabeçalho.

**(2)** Informe **"Número do Talão"** (o identificador impresso pelo banco), **"Empresa"** e **"Conta Bancária Interna"**.

**(3)** Informe a faixa: **"Folha Inicial"** e **"Folha Final"** — exatamente a numeração impressa nas folhas.

**(4)** Deixe **"Situação"** como **Ativo**.

**(5)** Use **"Observação"** para o que precisar registrar (agência de origem, data de retirada, quem retirou).

**(6)** Salve.

O sistema grava sozinho Dt./Hr. da Inclusão e Usuário da Inclusão. **"Quantidade de Folhas"** é calculado e mostra quantas folhas já existem para o talão — depois da geração.

| **ATENÇÃO:** Confira a faixa antes de gerar as folhas. Depois de geradas, a numeração não muda: o sistema recusa uma segunda geração no mesmo talão, e folha criada não se exclui. Faixa errada custa um talão novo. |
| --- |

#### 3.3 Etapa 2 — Gerar as folhas

**(1)** Com o talão selecionado, clique em **"Gerar Folhas"**.

**(2)** Confira a confirmação: ela mostra a faixa, a quantidade que será criada e avisa que a operação não tem volta.

**(3)** Confirme.

Todas as folhas nascem com **valor zerado**, **não assinadas** e com status **Disponível**. O sistema informa quantas foram criadas e atualiza a grade.

| **Dica:** A geração é feita em bloco e aguenta talões grandes — o limite por talão é de **2000 folhas**. Talões do dia a dia (300 a 500 folhas) levam poucos segundos. |
| --- |

| **ATENÇÃO:** Um talão só gera folhas uma vez. Tentar de novo devolve **"O talão X já teve as folhas geradas. Para mudar a faixa, cadastre um novo talão."** |
| --- |

#### 3.4 Etapa 3 — Marcar as folhas assinadas

Folha não assinada não vira cheque. Como a assinatura costuma acontecer em bloco — o diretor assina o talão inteiro de uma vez —, a marcação também é em bloco.

**(1)** Na grade de folhas, marque as folhas assinadas (use a seleção múltipla da grade).

**(2)** Clique em **"Marcar Assinatura"**.

**(3)** Em **"Assinatura"**, escolha **Assinada** (ou **Não assinada**, para desfazer um engano).

**(4)** Clique em **"Confirmar"**.

**OBSERVAÇÃO:** A marcação vale só enquanto a folha está no talão, com status **Disponível**. Depois de enviada para a Ficha, a assinatura já valeu e não muda mais — o sistema responde **"A folha X está Em utilização e a assinatura dela não muda mais."**

#### 3.5 Etapa 4 — Enviar a folha para a Ficha de Cheque

É aqui que a folha vira cheque. O envio cria o cheque próprio na rotina **Ficha de Cheque** e muda o status da folha para **Em utilização**.

**Enviar folhas específicas:**

**(1)** Marque as folhas na grade.

**(2)** Clique em **"Enviar para a Ficha"**.

**(3)** Confirme.

**Enviar tudo o que está pronto:**

**(1)** Com o talão selecionado, clique em **"Enviar Todas para a Ficha"**.

**(2)** Confirme.

O envio em massa segue a numeração e **para na primeira folha que ainda não está assinada** — o sistema informa em qual folha parou. Assine as que faltam e repita.

| **ESSENCIAL:** As folhas devem ser usadas **em ordem**. Se você selecionar uma folha e existir outra ainda **Disponível** com número menor, a tela abre a janela **"Envio fora de ordem"** e exige uma **justificativa**, indicando qual folha ficou para trás. A justificativa fica gravada no histórico da folha — é o que permite auditar o pulo depois. |
| --- |

| **ATENÇÃO:** O envio é tudo ou nada: se qualquer folha da seleção for recusada, nenhuma é enviada. Assim não sobra meio-envio para reconciliar. |
| --- |

| **OBSERVAÇÃO:** O cheque criado na Ficha nasce com o **valor da folha** (zero, se ela ainda não tem valor). O valor pode ser definido no pagamento, lá na Ficha. |
| --- |

#### 3.6 Etapa 5 — O que acontece na Ficha de Cheque

A partir do envio, o cheque é gerenciado na rotina **Ficha de Cheque**, e o talão apenas reflete o que acontece lá. Consulte o guia daquela rotina para o passo a passo; o resumo do efeito na folha é este:

| O que você faz na Ficha | O que acontece com a folha |
| --- | --- |
| Paga uma despesa com o cheque próprio | Passa para **Utilizada** e recebe o valor pago |
| Estorna o pagamento | Volta para **Em utilização** — o papel continua na rua, só a baixa do título foi desfeita |
| Devolve o cheque (sem fundos, sustado) | Continua **Utilizada** — o cheque foi emitido de verdade; os títulos de despesa reabrem |
| Exclui o cheque ainda não movimentado | Volta para **Disponível** e pode ser enviada de novo |

| **OBSERVAÇÃO:** Cheque já movimentado não pode ser excluído na Ficha: o sistema responde **"CONTROLE DE CHEQUES: Não possivel apagar um cheque já movimentado."** Para desfazer, estorne. |
| --- |

#### 3.7 Folha perdida: Inutilizada, Destruída ou Extraviada

Folha rasgada, perdida ou cancelada não some do sistema — ela muda de status e sai da fila, sem travar as seguintes.

**(1)** Marque as folhas na grade.

**(2)** Clique em **"Alterar Status"**.

**(3)** Escolha o **"Novo status"**: **Inutilizada**, **Extraviada** ou **Destruída**.

**(4)** Preencha a **"Justificativa"**.

**(5)** Clique em **"Confirmar"**.

Os três status são **definitivos**: não há volta para Disponível.

| Status | Quando usar | Justificativa |
| --- | --- | --- |
| **Inutilizada** | Erro de preenchimento, folha rasgada na emissão | Opcional |
| **Destruída** | Folha eliminada de propósito, com controle | **Obrigatória** |
| **Extraviada** | Folha sumiu, paradeiro desconhecido | **Obrigatória** |

| **ATENÇÃO:** Só esses três status podem ser marcados à mão. Disponível, Em utilização e Utilizada são consequência do fluxo — deixar a tela escrevê-los faria o status mentir sobre o que aconteceu de fato. |
| --- |

| **OBSERVAÇÃO:** Folha nunca é excluída. Ao tentar, o sistema responde **"A folha X não pode ser excluída. Marque-a como Inutilizada, Destruída ou Extraviada."** |
| --- |

#### 3.8 Histórico da folha

Cada folha tem a própria grade de **histórico**, abaixo dela. Uma linha é gravada a cada mudança de status, com:

- **"Status Anterior"** e **"Status Novo"**
- **"Data do Evento"** e **"Usuário"**
- **"Justificativa"** — inclusive a do uso fora de ordem
- **"Cheque (Ficha de Cheque)"** — preenchido na linha do envio, ligando a folha ao cheque criado

| **OBSERVAÇÃO:** A criação das folhas não gera linha de histórico: o nascimento delas está datado no próprio talão, em "Dt./Hr. da Inclusão" e "Usuário da Inclusão". O histórico começa no primeiro evento que acontece com a folha. |
| --- |

Esse histórico é **complementar** ao da Ficha de Cheque: aqui fica o ciclo de vida do papel; lá, o dos movimentos financeiros do cheque.

#### 3.9 Campos do talão e da folha

**Talão**

| Campo | Descrição |
| --- | --- |
| **Nro Único do Talão** | Numeração automática do sistema |
| **Número do Talão** | Identificação impressa pelo banco |
| **Empresa** | Empresa dona da conta |
| **Conta Bancária Interna** | Conta do talão |
| **Folha Inicial** / **Folha Final** | Faixa de numeração das folhas |
| **Situação** | Ativo, Encerrado ou Cancelado |
| **Observação** | Texto livre |
| **Quantidade de Folhas** | Calculado: folhas já geradas |
| **Dt./Hr. da Inclusão** / **Usuário da Inclusão** | Preenchidos pelo sistema |

**Folha**

| Campo | Descrição |
| --- | --- |
| **Número do Talão** / **Número da Folha** | Identificam a folha |
| **Status da Folha** | Ver a seção seguinte |
| **Assinada?** | Marcada pela ação "Marcar Assinatura" |
| **Justificativa** | Motivo da baixa manual ou do uso fora de ordem |
| **Valor** | Zero até o cheque receber valor na Ficha |
| **Nro Único Cheque (Ficha de Cheque)** | Cheque gerado no envio; em branco enquanto a folha não foi enviada |
| **Data do Status** / **Usuário do Status** | Preenchidos pelo sistema a cada mudança |

| **ATENÇÃO: "Situação"** do talão é informada por você. **Encerrado** e **Cancelado** bloqueiam o envio de folhas: **"O talão X está encerrado e não libera mais folhas."** Use ao devolver ou dar baixa no talão. |
| --- |

#### 3.10 Status da folha e transições

| Status | Significado |
| --- | --- |
| **Disponível** | Folha no talão, ainda não usada |
| **Em utilização** | Enviada para a Ficha; virou cheque, ainda não pagou nada |
| **Utilizada** | O cheque pagou uma despesa |
| **Inutilizada** | Baixa manual — erro de preenchimento |
| **Destruída** | Baixa manual — eliminada de propósito |
| **Extraviada** | Baixa manual — sumiu |

Transições aceitas:

| De | Para | O que provocou |
| --- | --- | --- |
| Disponível | Em utilização | Envio para a Ficha |
| Disponível | Inutilizada / Destruída / Extraviada | Ação "Alterar Status" |
| Em utilização | Utilizada | Pagamento na Ficha |
| Em utilização | Disponível | Exclusão do cheque na Ficha |
| Em utilização | Inutilizada | Ação "Alterar Status" |
| Utilizada | Em utilização | Estorno do pagamento na Ficha |

Qualquer outro caminho é recusado com **"A folha X está <status> e não pode passar para <status>."** Inutilizada, Destruída e Extraviada são terminais.

#### 3.11 Situações comuns e como resolver

| Situação | O que fazer |
| --- | --- |
| Cadastrei a faixa errada e já gerei as folhas | O talão não gera de novo. Marque as folhas erradas como **Inutilizada**, coloque a **Situação** do talão em **Cancelado** e cadastre o talão correto |
| Preciso pular uma folha (já usada fora do sistema) | Envie a folha desejada normalmente: a tela pede a justificativa do uso fora de ordem. Ou marque a folha pulada como **Inutilizada**, que a tira da fila |
| Marquei assinatura na folha errada | Selecione a folha e use **"Marcar Assinatura" → "Não assinada"**, enquanto ela ainda estiver **Disponível** |
| Enviei a folha por engano e o cheque ainda não pagou nada | Exclua o cheque na Ficha de Cheque: a folha volta para **Disponível** e pode ser reenviada |
| O cheque pagou a despesa errada | Estorne na Ficha de Cheque. A folha volta para **Em utilização** — o papel já saiu, então não volta a Disponível |
| O talão acabou | Coloque a **Situação** em **Encerrado**. Isso impede novos envios sem apagar o histórico |

#### 3.12 FAQ — Perguntas e erros mais frequentes

##### Cadastro e geração

**"Informe a folha inicial e a folha final do talão."**
A faixa é obrigatória para gerar. Preencha os dois campos e salve antes de clicar em "Gerar Folhas".

**"A folha inicial (x) não pode ser maior que a folha final (y)."**
A faixa está invertida. Corrija a numeração no talão.

**"A faixa informada geraria N folhas, acima do limite de 2000."**
Quase sempre é dígito trocado na numeração. Confira a faixa; se o talão for realmente maior, divida em mais de um cadastro.

**"O talão X já teve as folhas geradas."**
A geração acontece uma vez por talão. Para outra faixa, cadastre um novo talão.

**Posso excluir uma folha gerada a mais?**
Não. Marque como **Inutilizada** — a folha sai da fila e o registro permanece

##### Assinatura e envio

**"A folha X não está assinada e não pode ser usada como cheque."**
Marque a assinatura antes de enviar. É a trava que evita folha assinada em branco circulando.

**"A folha X já foi enviada para a Ficha de Cheque e virou o cheque N."**
A folha já está em uso. Consulte o cheque N na Ficha de Cheque.

**"As folhas do talão devem ser usadas em ordem: a folha Y ainda está disponível e vem antes da folha X."**
Use a janela "Envio fora de ordem" que a tela apresenta e informe a justificativa, ou envie a folha Y antes, ou tire-a da fila marcando-a como Inutilizada.

**"O talão X está encerrado e não libera mais folhas."**
Mude a "Situação" do talão para **Ativo** se o encerramento foi engano.

**Enviei "Todas para a Ficha" e parou antes do fim.**
O envio em massa respeita a ordem e para na primeira folha não assinada. Marque a assinatura das seguintes e repita.

##### Status e histórico

**"Informe a justificativa para marcar a folha X como Destruída."**
Destruída e Extraviada exigem justificativa; Inutilizada não.

**"A folha X está Utilizada e não pode passar para Destruída."**
Folha que já virou pagamento não aceita baixa manual. O que existe para desfazer o pagamento é o estorno, na Ficha de Cheque.

**Por que a folha continua Utilizada depois da devolução do cheque?**
Porque o cheque foi emitido de verdade e voltou sem fundos — o papel foi gasto. O que a devolução desfaz é o efeito financeiro: os títulos de despesa reabrem.

**Onde vejo quem inutilizou a folha e por quê?**
Na grade de **histórico** da folha: "Status Anterior", "Status Novo", "Usuário", "Data do Evento" e "Justificativa".
