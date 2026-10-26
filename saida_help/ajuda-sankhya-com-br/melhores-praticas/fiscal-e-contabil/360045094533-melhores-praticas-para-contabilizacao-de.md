---
id: "360045094533"
titulo: "Melhores Práticas para Contabilização de transferência bancária entre empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094533-Melhores-Pr%C3%A1ticas-para-Contabiliza%C3%A7%C3%A3o-de-transfer%C3%AAncia-banc%C3%A1ria-entre-empresas"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-09-03T18:20:38Z"
rotulos: ["Configuração", "Movimentação Financeira", "criadoRoger", "TOP", "Contabilização", "Financeiro", "Entre empresas gera dúvidas e erros comuns", "Dois lançamentos por empresa filtro específico necessário", "Fórmulas variam conforme empresas envolvidas"]
---

# Melhores Práticas para Contabilização de transferência bancária entre empresas

**Contabilização de transferência bancária entre empresas**

A contabilização das transferências bancárias entre empresas diferentes é um processo que gera bastante dúvidas tanto para analistas quanto para consultores, elaboramos esta documentação a fim de mostrar um exemplo pratico da configuraçao e contabilização para melhor entendimento.

Vamos tomar como exemplo a transferência bancária a seguir:

![Imagem 1: Financeiro » Rotinas » Movimentação Bancária](https://ajuda.sankhya.com.br/hc/article_attachments/19197075668887) **Financeiro » Rotinas » Movimentação Bancária**

O sistema identifica que a transferência é de uma empresa para outra, através das empresas das contas bancárias, no caso dessa transferência bancária que estamos analisando, seguem as contas bancárias de origem e destino e empresas as quais elas pertencem respectivamente:

- Conta 30==> Empresa 1
- Conta 31==> Empresa 2

**Então essa transferência será da empresa 1 para a empresa 2.**

A primeira coisa a se configurar deverá ser a fórmula de contabilização da TOP de transferência bancária, que no nosso exemplo é a 16, essa fórmula deverá levar em conta se a transferência é feita entre contas bancárias da mesma empresa ou de empresas diferentes, seguem as fórmulas utilizadas:

- Se Conta de Origem e Conta de Destino pertencem a mesma empresa:

C(Credito)- Conta da conta bancária

Formula: IF(Formula.CTACODEMP = Formula.EMPCTABCOCONTRAPART,Formula.VLRLANC,0)

D(Debito)- Conta da conta bancária

Formula: IF(Formula.CTACODEMP = Formula.EMPCTABCOCONTRAPART,Formula.VLRLANCCONTRAPART,0)

- Se Conta de Origem e Conta de Destino pertencem a empresas diferentes:

Contabilização conta origem/conta da empresa:

C- Conta Variável - Conta da conta bancária

Formula: IF((Formula.CTACODEMP<>Formula.EMPCTABCOCONTRAPART) AND (Formula.CTACODEMP = queLOTE.CODEMP),Formula.VLRLANC,0)

D- Conta fixa - Transferência numerários

Formula: IF((Formula.CTACODEMP<>Formula.EMPCTABCOCONTRAPART) AND (Formula.EMPCTABCOCONTRAPART = queLOTE.CODEMP),Formula.VLRLANC,0)

Contabilização conta destino/conta de contra partida da empresa:

D- Conta Variável - Conta da conta bancária

Formula: IF((Formula.CTACODEMP<>Formula.EMPCTABCOCONTRAPART) AND (Formula.CTACODEMP = queLOTE.CODEMP),Formula.VLRLANCCONTRAPART,0)

C- Conta fixa - Transferência numerários

Formula: IF((Formula.CTACODEMP<>Formula.EMPCTABCOCONTRAPART) AND (Formula.EMPCTABCOCONTRAPART= queLOTE.CODEMP),Formula.VLRLANCCONTRAPART,0)

![Imagem 2: Contabilização » Arquivos » TOP Contabilização](https://ajuda.sankhya.com.br/hc/article_attachments/19197075675543) **Contabilização » Arquivos » TOP Contabilização**

**CONTABILIZAÇÃO:**

Estando a TOP devidamente configurada, podemos partir para a contabilização, a qual deve ser feita em duas etapas:

1º- Para a empresa de origem, a qual deverá ter dois lançamentos sendo:

C- Para a movimentação de saída do dinheiro da conta bancárias
D- Em uma conta transitória

2º- Para a empresa de destino, a qual deverá ter dois lançamentos sendo:

D-Para a movimentação de entrada do dinheiro na conta bancária vindo da empresa 1
C- Em uma conta transitória (a mesma utilizada no lançamento da empresa 1 pra poder anular o lançamento)

**FILTRO:**

O filtro a ser utilizado deve considerar todas as movimentações descritas anteriormente para as duas empresas envolvidas, segue o exemplo do filtro que foi usado para contabilizar a transferência:

MovimentoBancario.DTLANC >= ?:{entidade=MovimentoBancario;campo=DTLANC} AND
MovimentoBancario.DTLANC <= ?:{entidade=MovimentoBancario;campo=DTLANC} AND
(ContaBancaria->CODEMP >= ?:{entidade=ContaBancaria;campo=CODEMP} OR
( (SELECT CTA.CODEMP \* 1.0 FROM TGFMBC MBD, TSICTA CTA WHERE MBD.NUMTRANSF = TGFMBC.NUMTRANSF AND MBD.ORIGMOV = TGFMBC.ORIGMOV AND MBD.RECDESP = (TGFMBC.RECDESP \* -1) AND MBD.DTLANC = TGFMBC.DTLANC AND MBD.CODCTABCOINT = CTA.CODCTABCOINT) >= ?:{entidade=ContaBancaria;campo=CODEMP})) AND
(ContaBancaria->CODEMP <= ?:{entidade=ContaBancaria;campo=CODEMP} OR
( (SELECT CTA.CODEMP \* 1.0 FROM TGFMBC MBD, TSICTA CTA WHERE MBD.NUMTRANSF = TGFMBC.NUMTRANSF AND MBD.ORIGMOV = TGFMBC.ORIGMOV AND MBD.RECDESP = (TGFMBC.RECDESP \* -1) AND MBD.DTLANC = TGFMBC.DTLANC AND MBD.CODCTABCOINT = CTA.CODCTABCOINT) <= ?:{entidade=ContaBancaria;campo=CODEMP}))

Estando o filtro criado, agora é só contabilizar conforme exemplo:

![Imagem 3: Primeiro contabiliza para empresa de origem, ou seja: empresa 1](https://ajuda.sankhya.com.br/hc/article_attachments/19197075668887) **Primeiro contabiliza para empresa de origem, ou seja: empresa 1**

![Imagem 4: Depois contabiliza para a empresa de destino, ou seja: Empresa 2](https://ajuda.sankhya.com.br/hc/article_attachments/19197075675543) **Depois contabiliza para a empresa de destino, ou seja: Empresa 2**

Conforme já mencionado, devem ser gerados dois lançamentos pra empresa de origem e dois para a empresa.

**EMPRESA 1:**

**EMPRESA 2:**

**Transferência entre empresas e o uso da conta transitória**

A transferência envolve dois fatos contábeis distintos: a saída de uma conta financeira e a entrada em outra. Nesse processo, a **conta transitória funciona como uma ponte contábil entre os dois movimentos**.

Como, no sistema, a contabilização é realizada considerando apenas uma empresa por vez, o sistema não consegue identificar, durante a contabilização, a outra empresa envolvida na transferência como contrapartida. Dessa forma, é necessária a utilização de uma **conta transitória** para que o sistema consiga realizar corretamente o fechamento entre débito e crédito.

Por esse motivo, ao realizar a contabilização, o sistema efetiva o lançamento, mas também retorna a mensagem de que o **resultado foi igual a zero**.

Isso ocorre porque a fórmula possui uma validação que verifica se a empresa do lote é a mesma empresa da contrapartida. Quando as empresas são diferentes, a própria fórmula retorna **ZERO**, conforme a lógica:

```
A empresa do lote é igual à empresa da contrapartida? Se não for, retorna ZERO.
```

Dessa forma, a mensagem está relacionada à validação da fórmula e ao fato de a transferência envolver **empresas distintas**.

Assim, a **conta transitória permite que a movimentação seja contabilizada de forma adequada**, servindo como a contrapartida necessária entre as empresas envolvidas na transferência.
