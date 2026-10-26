---
id: "35298608017431"
titulo: "304 Rejeição: CIOT deve ser informado para TAC e equiparado a TAC - MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35298608017431-304-Rejei%C3%A7%C3%A3o-CIOT-deve-ser-informado-para-TAC-e-equiparado-a-TAC-MDF-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:36Z"
rotulos: ["ERROMDFE", "MDF-e", "CIOT", "Transporte", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Viagens de Transporte (MDF-e)", "304 Rejeição", "Rejeição 304", "CIOT deve ser informado para TAC e equiparado a TAC - MDF-e", "TAGs <infCIOT>", "dados do CIOT", "RNTRC", "Documentos Eletrônicos"]
---

# 304 Rejeição: CIOT deve ser informado para TAC e equiparado a TAC - MDF-e

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35298636945047) **MENSAGEM:**

304 Rejeição: CIOT deve ser informado para TAC e equiparado a TAC

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35298608011031)SOLUÇÃO:**

**(1)** Acesse a tela de **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), em seguida, abra a viagem que está sendo apresentada a rejeição.

**(2)** Depois, na viagem em questão, vá até a aba **"MDF-e",** sub aba **"CIOT"** e preencha as informações referente ao dados do CIOT.

![Imagem 3: (2) Depois, na viagem em questão, vá até a aba "MDF-e", sub aba "CIOT" e preencha as informações referente ao dados do…](https://ajuda.sankhya.com.br/hc/article_attachments/35298608011287)

**Após o preencimento dos dados do CIOT, o sistema vai gerar o grupo de TAGs <infCIOT> no arquivo XML do MDF-e.**

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35298608011927)CAUSA:**

A rejeição acontece se **não for informado o grupo infCIOT nos casos em que:**

- O modal for rodoviário, e for informado o RNTRC (do emitente ou do proprietário do veículo) e esse RNTRC for de um TAC ou Equiparado a TAC (segundo o cadastro da ANTT).

**(1)** Para **mais informações sobre os ajustes necessários para adequação à Nota Técnica 2025.001 v1.02** acesse o artigo: [**Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência.**](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503)
