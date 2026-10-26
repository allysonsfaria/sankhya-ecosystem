---
id: "360043133154"
titulo: "Frete FOB exige que a transportadora seja informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133154-Frete-FOB-exige-que-a-transportadora-seja-informada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-11T19:55:28Z"
rotulos: ["#PUBLIFER", "#RevisadoClaudio", "CORE_E02065", "Configuração", "Parceiro", "Transporte", "Verificar marcação \"Exige Transportadora\"", "Frete FOB exige transportadora", "Preencher \"Parceiro Transportadora\"", "FOB", "Documentos Eletrônicos"]
---

# Frete FOB exige que a transportadora seja informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16137126521495) MENSAGEM:**

[CORE\_E02065] Frete FOB exige que a transportadora seja informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16137106442519) SOLUÇÃO:**

![Imagem 3: Quando definido na aba "Transporte" do respectivo lançamento o frete: FOB (Campo " CIF/FOB" ) e informar "Vlr do Frete"…](https://ajuda.sankhya.com.br/hc/article_attachments/16137126524311) Quando definido na aba **"Transporte"** do respectivo lançamento o frete: **FOB** [Campo "**CIF/FOB"**] e informar **"Vlr do Frete"** é necessário que o campo **"Parceiro Transportadora"** seja devidamente preenchido.

![Imagem 4: Quando definido na aba "Transporte" do respectivo lançamento o frete: FOB (Campo " CIF/FOB" ) e informar "Vlr do Frete"…](https://ajuda.sankhya.com.br/hc/article_attachments/14663590357655)

Caso não localize esse campo no lançamento, será necessário inseri-lo através do 'Configurador de layout da nota', para mais detalhes: [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16137106446103) IMPORTANTE:**

Se informar frete **"FOB"**, **"Vlr do Frete"** e **"Parceiro Transportadora"** é necessário informar também data de vencimento para o frete, caso não informe o sistema irá apresentar a mensagem:

Vencimento do frete deve ser maior que a data da negociação menos 30 dias (DD/MM/AAAA).

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16137106447895) CAUSA:**

Quando definido na aba **"Transporte"** do respectivo lançamento o frete: **FOB** [Campo 'CIF/FOB'], o **"Vlr do Frete"** for diferente de zero e o parceiro transportador não for informado, será apresentada a mensagem.
