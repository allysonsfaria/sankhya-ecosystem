---
id: "9650459273879"
titulo: "O tipo de título para a forma de pagamento informada não foi configurado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9650459273879-O-tipo-de-t%C3%ADtulo-para-a-forma-de-pagamento-informada-n%C3%A3o-foi-configurado"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:07:01Z"
rotulos: ["Configuração", "Financeiro", "Pagamento", "Sankhya Checkout", "CHK_E00024", "Tipo de título não configurado", "Verifique e cadastre tipo de título", "Analise JSON e configure tipo de pagamento"]
---

# O tipo de título para a forma de pagamento informada não foi configurado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16759498157847) MENSAGEM:**

[CHK\_E00024]  O tipo de título para a forma de pagamento informada não foi configurado!

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16759533418135) SITUAÇÃO:**

Ao tentar receber a venda a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16759533418903) SOLUÇÃO:**

![Imagem 4: Verifique se o tipo de título informado no recebimento existe. Por exemplo, se as vendas foram feitas com a forma de…](https://ajuda.sankhya.com.br/hc/article_attachments/16759498168855) Verifique se o tipo de título informado no recebimento existe. Por exemplo, se as vendas foram feitas com a forma de pagamento Voucher, cadastre um tipo de título voucher.

![Imagem 5: Normalmente essa mensagem irá ocorrer em recebimentos POS.](https://ajuda.sankhya.com.br/hc/article_attachments/16759498171543) Normalmente essa mensagem irá ocorrer em recebimentos POS.

Analise o JSON - TGFFIN campos CODFORMAPGTO e TIPOPAGAMENTONFCe para identificar qual a forma de pagamento. Para isso, acesse a tela **"Administração de Checkout"** (Caminho de acesso: Configurações » Sankhya Checkout » Administração de Checkout), Importação de movimentações, selecione a venda que está presa e, por fim, inspecione JSON.

Subtipo - Pagamento

1 - À vista
2 - À prazo
4 - Cheque
7 - Cartão de crédito
8 - Cartão de débito
99 - Cartão POS
9 - Voucher
10 - PIX
97 - Recarga Celular
98 - Troca

![Imagem 6: 1 - À vista 2 - À prazo 4 - Cheque 7 - Cartão de crédito 8 - Cartão de débito 99 - Cartão POS 9 - Voucher 10 - PIX 97 -…](https://ajuda.sankhya.com.br/hc/article_attachments/16759533425559)

![Imagem 7: Identificado o tipo de pagamento, cadastre o tipo de título de código 99, para isso acesse a tela "Tipos de título"…](https://ajuda.sankhya.com.br/hc/article_attachments/16759533426583) Identificado o tipo de pagamento, cadastre o tipo de título de código 99, para isso acesse a tela **"Tipos de título"** (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Título) outras opções, numeração.

![Imagem 8: Identificado o tipo de pagamento, cadastre o tipo de título de código 99, para isso acesse a tela "Tipos de título"…](https://ajuda.sankhya.com.br/hc/article_attachments/16759498178327)

![Imagem 9: Em "Configurar numeração" informe o código 99 e, em seguida, desmarque a numeração automática para que seja possível…](https://ajuda.sankhya.com.br/hc/article_attachments/16759533432343) Em **"Configurar numeração"** informe o código 99 e, em seguida, desmarque a numeração automática para que seja possível digitar manualmente o código para o tipo de título.

![Imagem 10: Em "Configurar numeração" informe o código 99 e, em seguida, desmarque a numeração automática para que seja possível…](https://ajuda.sankhya.com.br/hc/article_attachments/9652634816151)

![Imagem 11: Feito isso, cadastre o tipo de título 99 com descrição voucher e no campo "Tipo de pgto para NFC-e / NF-e / CF-e"…](https://ajuda.sankhya.com.br/hc/article_attachments/16759533433111) Feito isso, cadastre o tipo de título 99 com descrição **voucher** e no campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** coloque de acordo com a forma de pagamento correta.

![Imagem 12: Feito isso, cadastre o tipo de título 99 com descrição voucher e no campo "Tipo de pgto para NFC-e / NF-e / CF-e"…](https://ajuda.sankhya.com.br/hc/article_attachments/16759498182551)

Isso deixará a venda presa, não sendo possível finalizar a integração da venda. Cadastre o tipo de título e tente reprocessar o recebimento. Caso não resolva, entre em contato com o Suporte para análise.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16759498184087)CAUSA:**

Ocorre quando o tipo de título não existe para o recebimento da venda.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9650459273879-O-tipo-de-t%C3%ADtulo-para-a-forma-de-pagamento-informada-n%C3%A3o-foi-configurado#top)
