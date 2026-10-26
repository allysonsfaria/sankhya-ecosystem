---
id: "43567756441239"
titulo: "Guia de Investigação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43567756441239-Guia-de-Investiga%C3%A7%C3%A3o"
trilha: "Sankhya Official Pack - SOP > SOP Integração Conciliadora"
atualizado_em: "2026-09-22T14:08:17Z"
---

# Guia de Investigação

**SOP · INTEGRAÇÃO CONCILIADORA**

### Guia de Investigação

Um título de cartão não fechou: a árvore de decisão, o que consultar em cada tela e as consultas que confirmam cada etapa.

| **Público** | Suporte e operação |
| --- | --- |
| **Produto** | SOP Integração Conciliadora — Sankhya ERP |
| **Tipo de artigo** | Solução de problema |
| **Atualizado em** | 10/09/2026 |

### Sumário

**01**Venda não apareceu na Conciliadora?

**02**Pagamento não baixou?

**03**Renegociação travada?

A ordem das perguntas abaixo é a ordem do processo — cada resposta descarta uma etapa antes de olhar a seguinte.

![Imagem 1: A ordem das perguntas abaixo é a ordem do processo — cada resposta descarta uma etapa antes de olhar a seguinte.](https://ajuda.sankhya.com.br/hc/article_attachments/43567742281751)

A árvore de decisão: cada resposta descarta uma etapa antes da seguinte.

As consultas SQL desta página são executadas no **DBExplorer**, em **Configurações › Avançado**.

### Venda não apareceu na Conciliadora?

#### Na tela

|  | Abra o estabelecimento e consulte a aba **Vendas**: existe lote naquele dia? |
| --- | --- |
|  | Consulte a aba **Auditoria (Conciliadora)**: linha com **Stack** preenchido é erro real; **Mensagem** sem **Stack** é informativo — dia sem movimento, lote adiado. |
|  | Verifique a **Data Última Venda Enviada**, na aba **Geral**. |

Lendo o ponteiro do envio:

- **Anterior ao dia procurado** — a rotina está atrasada e ainda alcançará esse dia, a um dia por execução.
- **Posterior** — o dia já foi processado. Sem registro na aba **Vendas**, foi dia sem movimento ou houve erro. O automático não volta atrás: utilize o envio manual.
- **Em branco** — nunca houve envio automático concluído; a próxima execução enviará ontem.
- Se o título não estava apto a ser enviado, o motivo está na **Guia de Implantação › Conferindo o que está apto para envio**.

#### No banco

| -- 1. o lote foi gravado?  SELECT DATA, NULOTE, RETORNO, DHMOV    FROM TDCTCCESTVEN   WHERE CODEMP = :codemp     AND CODPARCADMIN = :codparcadmin     AND ESTABELECIMENTO = :est     AND DATA = :data   ORDER BY NULOTE;     -- 2. o título entrou no lote?  SELECT NULOTE, NUFIN    FROM TDCTCCVENENV   WHERE ESTABELECIMENTO = :est     AND NUFIN = :nufin;     -- 3. onde o ponteiro do envio está?  SELECT CODEMP, CODPARCADMIN, ESTABELECIMENTO, DTULTENV, DTULTPAG, NULOTEIDX    FROM TDCTCCEST   WHERE ESTABELECIMENTO = :est;     -- 4. erro ou informativo? STACK preenchido = erro real  SELECT DHMOV, MENSAGEM, CASE WHEN STACK IS NULL THEN 'informativo' ELSE 'erro' END AS TIPO    FROM TDCTCCLOG   WHERE ESTABELECIMENTO = :est   ORDER BY DHMOV DESC; |
| --- |

### Pagamento não baixou?

#### Na tela

A resposta está na grade **Pagamentos**, dentro de **Registros de Pagamentos**. Cada transação processada tem uma linha:

| Coluna | Indicação |
| --- | --- |
| **Localizado** | Achou o título correspondente? |
| **Baixado** | Conseguiu baixar? |
| **Conciliado** | Conciliou na Mov. Bancária? |
| **Sucesso** | Situação geral do processamento da linha |
| **Retorno** | Mensagem legível — é aqui que está o motivo |
| **Stack** | Erro técnico, quando houve exceção |
| **Nro. Único Financeiro** | O título com que a transação casou |

Depois, abra esse título na **Mov. Financeira** e confira, na aba **Conciliadora**, a data de pagamento, a divergência e a situação.

Se não houver linha nenhuma na grade, verifique a **Data Última Busca Pagamento**: pagamento recente pode ainda estar dentro da defasagem configurada.

#### No banco

| -- a linha da transação. RETORNO tem a mensagem legível; STACK, o erro técnico  SELECT SEQUENCIA, DATA, NSU, TID, PARCELA, NUFIN,         SUCESSO, LOCALIZADO, BAIXADO, CONCILIACAO,         RETORNO, STACK    FROM TDCTCCESTPAG   WHERE ESTABELECIMENTO = :est     AND (NSU = :nsu OR TID = :tid)   ORDER BY DHMOV DESC;     -- o financeiro foi baixado? DHBAIXA é o que o SOP consulta  SELECT NUFIN, DHBAIXA, CARTAODESC, TDCCONSTATUSMENSAGEM, TDCCONDIVERGENCIA, TDCCONDTPAG    FROM TGFFIN   WHERE NUFIN = :nufin; |
| --- |

### Renegociação travada?

#### Na tela

Os informativos da sincronização ficam na aba **Auditoria (Conciliadora)** e vivem apenas o número de dias configurado em TDCDIASLIMLOGE — três, no default. Em base com o default, quem só olha o log semanalmente perde o aviso.

Se não houver informativo e o título continuar sem chegar à Conciliadora, o mais provável é que a data dele caia fora da janela de TDCCONDRREN. Nesse caso o aviso saiu apenas no log do servidor, e o conserto é o envio manual daquela data.

Como a rotina funciona e o que cada informativo pede está no **Guia de Operação**.

#### No banco

| -- informativos da sincronização, que só vivem TDCDIASLIMLOGE dias  SELECT DHMOV, MENSAGEM    FROM TDCTCCLOG   WHERE ESTABELECIMENTO = :est     AND STACK IS NULL     AND MENSAGEM LIKE '%renegocia%'   ORDER BY DHMOV DESC; |
| --- |
