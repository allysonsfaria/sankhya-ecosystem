---
id: "9531453241623"
titulo: "Bandeira do cartão informada no TEF não é levada para movimentação financeira - Checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9531453241623-Bandeira-do-cart%C3%A3o-informada-no-TEF-n%C3%A3o-%C3%A9-levada-para-movimenta%C3%A7%C3%A3o-financeira-Checkout"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:07:32Z"
rotulos: ["Configuração", "TEF - Transação Eletrônica de Fundos manual", "Movimentação Financeira", "TEF", "Financeiro", "Tipo de Título", "Checkout", "BANDEIRA", "Cartão TEF sem bandeira", "Ajustar forma de pagamento", "Adicionar variação de bandeira"]
---

# Bandeira do cartão informada no TEF não é levada para movimentação financeira - Checkout

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16748505490455) MENSAGEM:**

Bandeira do cartão informada no TEF não é levada para movimentação financeira - CHECKOUT.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16748505496471) SITUAÇÃO:**

Abaixo temos três tipos de títulos cadastrados, para cartão de crédito. Com bandeiras GETNET (82), CIELO (105) e VISA (109);

![Imagem 3: Abaixo temos três tipos de títulos cadastrados, para cartão de crédito. Com bandeiras GETNET (82), CIELO (105) e VISA…](https://ajuda.sankhya.com.br/hc/article_attachments/16748505500951)

O tipo de título '82' é o padrão para recebimento em crédito no cadastro do Checkout;

![Imagem 4: O tipo de título '82' é o padrão para recebimento em crédito no cadastro do Checkout;](https://ajuda.sankhya.com.br/hc/article_attachments/9530558380951)

Após o recebimento via TEF, verificamos que a bandeira da transação foi 'DEMOCARD' (TGFTEF);

![Imagem 5: Após o recebimento via TEF, verificamos que a bandeira da transação foi 'DEMOCARD' (TGFTEF);](https://ajuda.sankhya.com.br/hc/article_attachments/9530695394327)

Mas o sistema puxou o tipo de titulo '82' para o recebimento no Sankhya/W (bandeira GETNET);

![Imagem 6: Mas o sistema puxou o tipo de titulo '82' para o recebimento no Sankhya/W (bandeira GETNET);](https://ajuda.sankhya.com.br/hc/article_attachments/16748505504023)

**![Imagem 7: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16748505509399) SOLUÇÃO:**

![Imagem 8: Informe a forma de pagamento TEF correta no Tipo de Título. É possível adicionar uma nova forma de pagamento TEF, caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16748520619287) Informe a forma de pagamento TEF correta no Tipo de Título. É possível adicionar uma nova forma de pagamento TEF, caso ainda não esteja registrada;

[GIF animado: Imagem 9: Informe a forma de pagamento TEF correta no Tipo de Título. É possível adicionar uma nova forma de pagamento TEF, caso…](https://ajuda.sankhya.com.br/hc/article_attachments/9530896161687)

![Imagem 10: Informe a variação de bandeira, na tela "Administração de Checkout" ;](https://ajuda.sankhya.com.br/hc/article_attachments/16748505518359)  Informe a variação de bandeira, na tela **"Administração de Checkout"**;

**Exemplo:**

Se informar uma variação para bandeira 'VISA', sempre que a variação entrar, o sistema irá buscar o Tipo de Título com a forma de pagamento 'VISA'.

[GIF animado: Imagem 11: Se informar uma variação para bandeira 'VISA', sempre que a variação entrar, o sistema irá buscar o Tipo de Título com…](https://ajuda.sankhya.com.br/hc/article_attachments/9531188120983)

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16748505524375) CAUSA:**

Sistema não encontra um Tipo de Titulo com a forma de pagamento TEF recebida pela TGFTEF, assim busca o Tipo de Titulo padrão.
