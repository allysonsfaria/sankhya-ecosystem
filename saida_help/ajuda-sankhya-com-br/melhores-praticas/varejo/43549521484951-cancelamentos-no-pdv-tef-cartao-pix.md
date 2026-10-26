---
id: "43549521484951"
titulo: "Cancelamentos no PDV (TEF/Cartão/Pix)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549521484951-Cancelamentos-no-PDV-TEF-Cart%C3%A3o-Pix"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-10-20T20:36:50Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Cancelamentos no PDV (TEF/Cartão/Pix)

**MENSAGEM**

Ao tentar cancelar uma nota fiscal no Portal de Caixa, o sistema pode apresentar a seguinte mensagem de erro: “**O** **documento** **de** **número** **único** **XXX** **não** **pode** **ser** **excluído.** **Existe** **parcela** **recebida** **com** **TEF**.”

Essa mensagem indica que há uma transação TEF associada ao recebimento da venda, impedindo o cancelamento da nota fiscal antes da regularização financeira.

**SITUAÇÃO**

Essa situação pode ocorrer quando a venda possui recebimento via PIX ou cartão, por meio da integração TEF/SiTef. Nesses casos, o sistema bloqueia o cancelamento da nota fiscal enquanto houver um recebimento vinculado que precise ser estornado, impedindo a continuidade do processo até que a regularização financeira seja realizada.

**SOLUÇÃO**

**(1)** Localizar a nota no Portal de Caixa ( Comercial » Consulta » Portal de Caixa), clicar pra abrir a nota no Layout de PDV.
**(2)** No botão Outras Opções > **"Ver Financeiros Nota".** Em seguida, clique no botão **[9] Excluir**. O sistema exibirá a seguinte mensagem de confirmação: Você deseja realmente apagar o registro selecionado? Confirme a operação para prosseguir

**(3)** No pop-up **“Estornar Recebimento PIX TEF”**, clique no botão **Estornar**. O sistema acionará o client SiTef. Nesse ambiente, será necessário selecionar carteira digital **PIX**, informar a data da transação e o número do documento. Conclua o procedimento conforme as instruções apresentadas pelo sistema.

![Imagem 1: (3) No pop-up “Estornar Recebimento PIX TEF” , clique no botão Estornar . O sistema acionará o client SiTef. Nesse…](https://ajuda.sankhya.com.br/hc/article_attachments/44394250155415)

**(4)** Caso o recebimento tenha sido realizado por cartão de crédito ou débito, será exibido o pop-up **“Cancelar Recebimento com Cartão”**, com os dados da venda e a opção **Cancelar**.

Clique em **Cancelar**. O sistema acionará o client SiTef para processar a operação. Após o processamento, deverá ser apresentada a mensagem:

![Imagem 2: Clique em Cancelar . O sistema acionará o client SiTef para processar a operação. Após o processamento, deverá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/44395978533399)

**(5)** Após concluir o estorno ou cancelamento do recebimento, prossiga com o cancelamento da nota fiscal pelo **Portal de Caixa/Venda** para regularizar a operação.

**(6)** Caso o prazo para cancelamento tenha sido excedido, o sistema exibirá a mensagem:  **“Estorno bloqueado por ultrapassar o tempo previsto. Já se passaram X horas da emissão da nota (limite de 24 horas).”**

Nessa situação, realize o processo de devolução da venda para efetuar o reembolso do valor ao cliente.

Confirme o resultado do estorno ou cancelamento antes de finalizar o processo, a fim de evitar inconsistências financeiras ou fiscais.

O recebimento via PIX Fintech não se enquadra neste procedimento e deve ser tratado separadamente.

**CAUSA**

A causa do erro está relacionada aos controles de segurança do sistema, que visam garantir a integridade das transações financeiras e exigem o estorno do recebimento antes do cancelamento da nota fiscal.
