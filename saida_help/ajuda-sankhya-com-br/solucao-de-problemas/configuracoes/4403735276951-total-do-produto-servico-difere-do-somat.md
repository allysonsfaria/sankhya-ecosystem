---
id: "4403735276951"
titulo: "Total do Produto / Serviço difere do somatório dos itens "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403735276951-Total-do-Produto-Servi%C3%A7o-difere-do-somat%C3%B3rio-dos-itens"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:23:41Z"
rotulos: ["Produtos", "NF-e", "XML", "SEFAZ", "Impostos", "NFC-e", "não apagar", "#publicadoHyago", "#validadoTiagoBarbosa", "564", "Total do Produto / Serviço e Somatório dos Itens: Divergência", "Identificação dos Itens no Somatório", "Correção dos Totais da NF-e"]
---

# Total do Produto / Serviço difere do somatório dos itens 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16345304126487) MENSAGEM:**

[Rejeição 564]: Total do Produto / Serviço difere do somatório dos itens

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345304130839) SOLUÇÃO:**

Utilizando o mesmo exemplo dado, realizamos o cálculo, considerando os itens que possuem o campo**indTot = '1'**:

vProd [Total] = vProd [item 1] + vProd [item 2]

vProd [Total] = 199.99 + 199.99

vProd [Total] = 399.98

O mesmo cálculo é válido para qualquer quantidade de itens que haja na NF-e / NFC-e. Feito o cálculo, corrija nos Totais da NF-e o campo correspondente ao somatório (vProd). Veja a informação corrigida no XML abaixo:

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | `<``total``>`  `<``ICMSTot``>`  `<``vBC``>000.00</``vBC``>`  `<``vICMS``>00.00</``vICMS``>`  `<``vICMSDeson``>0.00</``vICMSDeson``>`  `<``vBCST``>0.00</``vBCST``>`  `<``vST``>0.00</``vST``>`  `<``vProd``>000.00</``vProd``>`  `<``vFrete``>0.00</``vFrete``>`  `<``vSeg``>0.00</``vSeg``>`  `<``vDesc``>0.00</``vDesc``>`  `<``vII``>0.00</``vII``>`  `<``vIPI``>0.00</``vIPI``>`  `<``vPIS``>0.00</``vPIS``>`  `<``vCOFINS``>0.00</``vCOFINS``>`  `<``vOutro``>0.00</``vOutro``>`  `<``vNF``>000.00</``vNF``>`  `<``vTotTrib``>0.00</``vTotTrib``>`  `</``ICMSTot``>`  `</``total``>` |
| --- | --- |

Agora,  reenvie a NF-e / NFC-e para processamento.

Referência:

- Manual de Orientação ao Contribuinte: [http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc    (link de Download)](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16345304147479)CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o Total dos Produtos e Serviços (Campo: total / ICMSTot / vProd - ID: W07) informado no Grupo de Totais da NF-e, for diferente do somatório dos itens (Campo: det / prod / vProd - ID: I11) que fazem parte do cálculo, será retornado a rejeição "564 - Total do Produto / Serviço difere do somatório dos itens".

**Como saber se o item faz parte do somatório do Total dos Produtos e Serviços?**

O campo **indTot**(ID: I17b) indica se o produto compõe ou não o somatório do Total:

- **0** = Valor do item (vProd) não compõe o valor total da NF-e;
- **1** = Valor do item (vProd) compõe o valor total da NF-e (vProd).

**Exemplo:**

Foi emitida uma NF-e com dois itens informados, cada um com o Valor do Produto de R$ 199,99 reais, mas no Grupo de Totais da NF-e foi informado o valor de R$ 400,00 reais. Como o somatório correto é R$ 399,98 reais, pois os dois itens compõe o somatório Total dos Produtos e Serviços, a NF-e / NFC-e será rejeitada pelo motivo 564.

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60 | `<``det` `nItem``=``"1"``>`  `<``prod``>`  `<``cProd``>000000</``cProd``>`  `<``cEAN``/>`  `<``xProd``>-----</``xProd``>`  `<``NCM``>00000</``NCM``>`  `<``CFOP``>5101</``CFOP``>`  `<``uCom``>UN</``uCom``>`  `<``qCom``>1.0000</``qCom``>`  `<``vUnCom``>000.0000000000</``vUnCom``>`  `<``vProd``>000.00</``vProd``>`  `<``cEANTrib``/>`  `<``uTrib``>UN</``uTrib``>`  `<``qTrib``>1.0000</``qTrib``>`  `<``vUnTrib``>000.0000000000</``vUnTrib``>`  `<``indTot``>1</``indTot``>`  `</``prod``>`  `...`    `</``det``>`  `<``det` `nItem``=``"2"``>`  `<``prod``>`  `<``cProd``>000000</``cProd``>`  `<``cEAN``/>`  `<``xProd``>----</``xProd``>`  `<``NCM``>00000000</``NCM``>`  `<``CFOP``>0000</``CFOP``>`  `<``uCom``>UN</``uCom``>`  `<``qCom``>1.0000</``qCom``>`  `<``vUnCom``>000.0000000000</``vUnCom``>`  `<``vProd``>000.00</``vProd``>`  `<``cEANTrib``/>`  `<``uTrib``>UN</``uTrib``>`  `<``qTrib``>1.0000</``qTrib``>`  `<``vUnTrib``>000.0000000000</``vUnTrib``>`  `<``indTot``>1</``indTot``>`  `</``prod``>`  `...`    `</``det``>`  `<``total``>`  `<``ICMSTot``>`  `<``vBC``>399.98</``vBC``>`  `<``vICMS``>48.00</``vICMS``>`  `<``vICMSDeson``>0.00</``vICMSDeson``>`  `<``vBCST``>0.00</``vBCST``>`  `<``vST``>0.00</``vST``>`  `<``vProd``>400.00</``vProd``>`  `<``vFrete``>0.00</``vFrete``>`  `<``vSeg``>0.00</``vSeg``>`  `<``vDesc``>0.00</``vDesc``>`  `<``vII``>0.00</``vII``>`  `<``vIPI``>0.00</``vIPI``>`  `<``vPIS``>0.00</``vPIS``>`  `<``vCOFINS``>0.00</``vCOFINS``>`  `<``vOutro``>0.00</``vOutro``>`  `<``vNF``>399.98</``vNF``>`  `<``vTotTrib``>0.00</``vTotTrib``>`  `</``ICMSTot``>`  `</``total``>` |
| --- | --- |

Veja regra de validação da Sefaz:

![Imagem 4: Veja regra de validação da Sefaz:](http://www.oobj.com.br/bc/assets/Articles/277/Rej564.PNG)
