---
id: "17612409083415"
titulo: "Rejeição 567 - NF-e de devolução com valor do ICMS da UF Destino superior a NF-e devolvida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17612409083415-Rejei%C3%A7%C3%A3o-567-NF-e-de-devolu%C3%A7%C3%A3o-com-valor-do-ICMS-da-UF-Destino-superior-a-NF-e-devolvida"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:53:11Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "Alíquota interna da devolução difere da nota original", "[Rejeição - 567]: Valor ICMS UF Destino superior", "Verifique e ajuste o valor no campo vICMSUFDest", "Erro"]
---

# Rejeição 567 - NF-e de devolução com valor do ICMS da UF Destino superior a NF-e devolvida

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17612417808023) **MENSAGEM:**

[Rejeição - 567]: NF-e de devolução com valor do ICMS da UF Destino superior a NF-e devolvida

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17612425670423)SOLUÇÃO:**

![Imagem 3: Verifique o valor informado no campo vICMSUFDest , esse valor deve estar condizente com o informado na nota que…](https://ajuda.sankhya.com.br/hc/article_attachments/17614709239319) Verifique o valor informado no campo **vICMSUFDest**, esse valor deve estar condizente com o informado na nota que originou a devolução.

![Imagem 4: Acesse: Alíquotas de ICMS ( Comercial » Arquivo » Cadastros » Alíquotas) - aba: geral, campo: Alíq. Interna Destino](https://ajuda.sankhya.com.br/hc/article_attachments/17614771131287) Acesse:  Alíquotas de ICMS (Comercial » Arquivo » Cadastros » Alíquotas) - aba: geral, campo: Alíq. Interna Destino

![Imagem 5: Caso a alíquota interna de destino da nota de devolução estiver informada de maneira diferente da nota de origem, é…](https://ajuda.sankhya.com.br/hc/article_attachments/17614771138711) Caso a alíquota interna de destino da nota de devolução estiver informada de maneira diferente da nota de origem, é necessário igualar os campos e redigitar o item na nota ou gerar uma nova devolução. Assim, os valores da tag **vICMSUFDest** ficarão iguais.

![Imagem 6: Caso a alíquota interna de destino da nota de devolução estiver informada de maneira diferente da nota de origem, é…](https://ajuda.sankhya.com.br/hc/article_attachments/17612377413143)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17612431293207)CAUSA:**

Ocorre quando a alíquota interna preenchida na nota de devolução difere da nota fiscal referenciada/origem.

Exemplo:

Foi informado o grupo de ICMS para a UF de destino, onde o valor preenchido no campo **vICMSUFDest**, foi de **20.03** enquanto que na nota de venda, esse mesmo campo foi informado com o valor **10.03**, portanto devido a essa diferença a rejeição ocorre.
