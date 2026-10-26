---
id: "35298216515863"
titulo: "303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35298216515863-303-Rejei%C3%A7%C3%A3o-Dados-banc%C3%A1rios-e-de-pagamento-devem-ser-informados-para-TAC-e-equiparado-a-TAC"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:38Z"
rotulos: ["ERROMDFE", "MDF-e", "Transporte", "Passos para resolver", "Razão do erro", "Detalhe do erro", "303 Rejeição", "Rejeição 303", "Dados bancários e de pagamento", "TAC e equiparado a TAC", "modal for rodoviário", "Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC", "Viagens de Transporte (MDF-e)", "informado o RNTRC", "RNTRC", "Documentos Eletrônicos", "Pagamento de Frete"]
---

# 303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35298170772247) **MENSAGEM:**

303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35298216502679)SOLUÇÃO:**

**(1)** Acesse a tela de **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), em seguida, abra a viagem que está sendo apresentada a rejeição.

**(2)** Depois, na viagem em questão, vá até a aba **"MDF-e"**, sub aba **"Pagamento de Frete",** em seguida, sub aba **"Geral" e** preencha as informações referente ao pagamento do frete, conforme exemplo abaixo:

![Imagem 3: (2) Depois, na viagem em questão, vá até a aba "MDF-e" , sub aba "Pagamento de Frete", em seguida, sub aba "Geral" e…](https://ajuda.sankhya.com.br/hc/article_attachments/35298216505623)

**Importante**: caso seja **informado a forma de pagamento "A prazo", preencha os dados da aba "Informações do Pagamento a Prazo".**

![Imagem 4: Importante : caso seja informado a forma de pagamento "A prazo", preencha os dados da aba "Informações do Pagamento a…](https://ajuda.sankhya.com.br/hc/article_attachments/35298170777239)

![Imagem 5: Importante : caso seja informado a forma de pagamento "A prazo", preencha os dados da aba "Informações do Pagamento a…](https://ajuda.sankhya.com.br/hc/article_attachments/35298170778391)

**Após o preencimento dessas informações, no arquivo XML do MDF-e  será gerado o grupo de Tags <infPag> e <infBanc>.**

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35298216508439)CAUSA:**

A rejeição acontece se o grupo de **informações de pagamento (infPag) e informações bancárias (infBanc) não tiverem sido informados** nos casos em que:

- O **modal for rodoviário**;
- E for **informado** o RNTRC (registro da ANTT), do **emitente** ou do **proprietário** do **veículo**;
- E essa pessoa for um **TAC ou Equiparado a TAC** (segundo o cadastro na ANTT),

**(1)** Para **mais informações sobre os ajustes necessários para adequação à Nota Técnica 2025.001 v1.02** acesse o artigo: [**Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.**](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)
