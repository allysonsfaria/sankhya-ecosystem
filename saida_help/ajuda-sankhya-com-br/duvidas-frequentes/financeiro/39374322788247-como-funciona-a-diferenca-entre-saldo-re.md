---
id: "39374322788247"
titulo: "Como funciona a diferença entre Saldo Real e Saldo do Banco?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39374322788247-Como-funciona-a-diferen%C3%A7a-entre-Saldo-Real-e-Saldo-do-Banco"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-08-17T20:29:08Z"
rotulos: ["Configuração", "Financeiro", "Conciliação Bancária", "Artigo criado KCS", "Financeiro - KCS", "Saldo Real", "Saldo do Banco"]
---

# Como funciona a diferença entre Saldo Real e Saldo do Banco?

Na tela **"Conciliação Bancária"** (Financeiro » Rotinas » Conciliação Bancária), é comum observar divergências entre o **"Saldo Real"** e o **"Saldo do Banco"**. Essa diferença não representa um erro do sistema, mas sim o reflexo de como cada saldo é calculado e atualizado.

Compreenda a distinção entre esses dois tipos de saldo para realizar uma conciliação bancária precisa e evitar interpretações equivocadas sobre a situação financeira da empresa.

### Diferença entre Saldo Real e Saldo do Banco

O **"Saldo Real"** representa todas as baixas realizadas no sistema para a conta bancária em questão, independentemente de terem sido conciliadas ou não. Ele é atualizado automaticamente na **"Data da Baixa"** do título.

Já o **"Saldo do Banco"** corresponde ao que foi baixado e conciliado na tela **"Conciliação Bancária"**. Ele é atualizado apenas na **"Data da Conciliação"** do título.

### Exemplo prático da divergência

Considere a seguinte situação: um título de **"R$ 100,00"** possui data de lançamento ou baixa em **"01/10/2025"**, porém foi conciliado somente em **"02/10/2025"**, trabalhando assim com conciliação D+1.

Neste cenário:

- O **"Saldo Real"** será atualizado em **"01/10/2025"**.
- O **"Saldo do Banco"** será atualizado apenas em **"02/10/2025"**.

Dessa forma, ao consultar a tela **"Conciliação Bancária"** na data de **"01/10/2025"**, haverá uma divergência de **"R$ 100,00"** entre os saldos devido à diferença entre as datas de baixa e conciliação.

### Campos de Saldo na tela Contas

Na tela **"Contas"** (Configurações » Cadastros » Bancários » Contas), os campos **"Saldo Banco Referência"** e **"Saldo Real Referência"** estão relacionados ao saldo implantado inicialmente na conta bancária.

Esses valores representam o ponto de partida para o cálculo dos saldos e não devem ser confundidos com os saldos atuais apresentados na conciliação bancária.

### Principais causas de divergência

As divergências entre **"Saldo Real"** e **"Saldo do Banco"** podem ocorrer devido a:

- Diferença entre data de baixa e data de conciliação: títulos baixados mas ainda não conciliados.
- Títulos não conciliados: movimentações como transferências entre contas que não foram conciliadas.
- Títulos baixados em conta ou data incorreta: quando um título é baixado em uma conta bancária diferente da original, gerando saldo negativo na conta correta.

### Como verificar e corrigir divergências

Para identificar e corrigir divergências entre os saldos, siga os passos abaixo:

Acesse a tela **"Conciliação Bancária"** (Financeiro Movimentação Conciliação Bancária).
 Selecione a conta bancária e a data de referência desejada.
 Verifique os títulos que aparecem como não conciliados na listagem.
 Realize a conciliação dos títulos pendentes, marcando-os e confirmando a operação.
 Caso identifique títulos baixados em conta ou data incorreta, estorne a baixa e refaça na conta/data correta.
 Após as correções, verifique se o **"Saldo do Banco"** está de acordo com o extrato bancário.

Caso a divergência persista, será possível forçar a correção dos saldos. Para isso, acesse a tela **Contas**, vá até a aba **Saldos** e utilize as opções **“Corrigir Saldo Banco”** e **“Corrigir Saldo Real”**.

![Imagem 1: Acesse a tela "Conciliação Bancária" (Financeiro Movimentação Conciliação Bancária). Selecione a conta bancária e a…](https://ajuda.sankhya.com.br/hc/article_attachments/42083841171223)

Siga esses procedimentos para que os saldos sejam atualizados corretamente e a conciliação bancária reflita a situação real da conta.
