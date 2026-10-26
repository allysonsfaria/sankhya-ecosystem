---
id: "35305930972823"
titulo: "724 Rejeição: Grupo de informações do pagamento a prazo deve ser informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35305930972823-724-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-do-pagamento-a-prazo-deve-ser-informado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:33Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Transporte", "724 Rejeição", "Rejeição 724", "Grupo de informações do pagamento a prazo deve ser informado", "724 Rejeição: Grupo de informações do pagamento a prazo deve ser informado", "Documentos Eletrônicos", "Pagamento a Prazo"]
---

# 724 Rejeição: Grupo de informações do pagamento a prazo deve ser informado

**MENSAGEM**

724 Rejeição: Grupo de informações do pagamento a prazo deve ser informado

**SITUAÇÃO**

Ao emitir o MDF-e (modelo 58) com **"Modal"** igual a **"1 – Rodoviário"**, **"Tipo do Emitente"** igual a **"1 – Prestador de serviço de transporte"** ou **"3 – Prestador de serviço de transporte que emitirá CT-e Globalizado"**, e **"Indicador da Forma de Pagamento"** igual a **"1 – Pagamento a Prazo"**, sem informar o **"Grupo de Informações do Pagamento a Prazo"**, o sistema apresenta a rejeição.

**SOLUÇÃO**

**(1)**  Acesse tela **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), vá até a aba **"MDF-e",** sub aba **"Pagamento de frete",** por fim sub aba **"Geral"**.

![Imagem 1: (1) Acesse tela "Viagens de Transporte (MDF-e)" (Comercial » Rotinas » Viagens de Transporte (MDF-e)), vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/35674847509911)

**(2)**  Selecione a opção **"Pagamento a Prazo"** no campo **"Forma de Pagamento"**.

**(3)**  Na aba **"Informações do pagamento a prazo"** (ainda na tela Viagens de Transporte (MDF-e)), informe a **"parcela"** e a **"data de vencimento"**.

![Imagem 2: (2) Selecione a opção "Pagamento a Prazo" no campo "Forma de Pagamento" . (3) Na aba "Informações do pagamento a prazo"…](https://ajuda.sankhya.com.br/hc/article_attachments/35305930966039)

**CAUSA**

O erro ocorre quando é selecionada a forma de pagamento a prazo, mas não são informados os dados de **"parcelas"**, **"vencimento"** e **"valor"** no grupo de informações do pagamento a prazo.
