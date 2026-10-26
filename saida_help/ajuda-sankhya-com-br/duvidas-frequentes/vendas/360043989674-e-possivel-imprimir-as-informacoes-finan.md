---
id: "360043989674"
titulo: "É possível imprimir as informações financeiras do DANFE no campo Fatura/Duplicata?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043989674-%C3%89-poss%C3%ADvel-imprimir-as-informa%C3%A7%C3%B5es-financeiras-do-DANFE-no-campo-Fatura-Duplicata"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:57:07Z"
rotulos: ["DUVIDANF", "Configuração", "Impressão", "NF-e", "XML", "DANFE", "Financeiro", "Desative \"ESCDETDUPLNFE\"", "Mostra detalhes financeiros", "Configurações » Avançado » Preferências"]
---

# É possível imprimir as informações financeiras do DANFE no campo Fatura/Duplicata?

**(1)** Sim, para isso é preciso desligar o parâmetro "**ESCDETDUPLNFE- Esconder detalhes do campo Fatura/Duplicata na NFE".**

Quando desligado, o sistema emite o DANFE e XML, apresentando as informações financeiras no campo **"Fatura/Duplicata"**.

![Imagem 1: Acesse: Configurações » Avançado » Preferências, pesquise pelo parâmetro ESCDETDUPLNFE e o desligue.](https://ajuda.sankhya.com.br/hc/article_attachments/16832370049047) Acesse: Configurações » Avançado » Preferências, pesquise pelo parâmetro ESCDETDUPLNFE e o desligue.

Parâmetro: **desligado**

![Imagem 2: Parâmetro: desligado](https://ajuda.sankhya.com.br/hc/article_attachments/14659791488407)

**![Imagem 3: Significado de cada informação disposta no Danfe em 'Fatura/Duplicata'](https://ajuda.sankhya.com.br/hc/article_attachments/16832370050711) Significado de cada informação disposta no Danfe em 'Fatura/Duplicata'**

VENDA A VISTA | DUP=000000008-1 Venc=27-12-2010 Valor=25.70

**(1)** **1º campo - VENDA A VISTA:** se refere a nomenclatura do **Tipo de negociação** utilizada.

**(1)** **2º campo -** **DUP:** se refere ao tipo de pagamento, seja ele boleto, cheque, cartão de crédito. Então aparecerá as iniciais, de acordo com o escolhido no tipo de título, campo: **"Tipo de pgto para NFC-e / NF-e / CF-e"**; caso o campo esteja vazio irá aparecer OUT, de 'OUTROS';

**(1)** **3º campo -** **000000008-1:** apresentará a numeração de acordo com as parcelas, exemplo: 02 parcelas  DUP: 00001 .... DUP: 00002;

**(1)** **4º campo - Venc=27-12-2010:** data de vencimento, se for mais de uma parcela, aparecerá vencimento de cada parcela;

**(1)** **5º campo -** **Valor=25.70:** o valor da parcela. Se for mais de uma, aparecerá o valor de cada parcela.
