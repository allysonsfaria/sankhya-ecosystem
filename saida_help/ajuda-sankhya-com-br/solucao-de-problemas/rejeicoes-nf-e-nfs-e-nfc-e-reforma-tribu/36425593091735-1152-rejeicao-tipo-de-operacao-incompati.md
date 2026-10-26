---
id: "36425593091735"
titulo: "1152 Rejeição: Tipo de Operação incompatível com NF-e de Crédito do tipo Retorno"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36425593091735-1152-Rejei%C3%A7%C3%A3o-Tipo-de-Opera%C3%A7%C3%A3o-incompat%C3%ADvel-com-NF-e-de-Cr%C3%A9dito-do-tipo-Retorno"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:22:59Z"
rotulos: ["Configuração", "NF-e", "Retorno", "SEFAZ", "TOP", "CFOP", "Passos para resolver", "Erro", "Como Resolver", "Rejeição 1152", "Tipo de Operação incompatível com NF-e de Crédito do tipo Retorno", "1152 Rejeição", "NF-e de Crédito"]
---

# 1152 Rejeição: Tipo de Operação incompatível com NF-e de Crédito do tipo Retorno

**MENSAGEM**

1152 Rejeição: Tipo de Operação incompatível com NF-e de Crédito do tipo Retorno

**SITUAÇÃO**

Esta rejeição ocorre quando uma **NF-e de Crédito** está configurada como **"Retorno"**, mas o **Tipo de Operação** não está marcado como **"Entrada"**. A Sefaz exige que notas de crédito de retorno sejam sempre operações de entrada.

**SOLUÇÃO**

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Localize e selecione a nota fiscal que apresentou a rejeição.

**(3)** Na grade **''Cabeçalho''**, verifique o campo **''Tipo Operação''** e selecione uma outra TOP que tenha as seguintes características:

- Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).
- Verifique se o campo **"Tipo de movimento"** está preenchido com um tipo de movimento que represente **entrada, a depender do portal em que está emitindo nota**
- Na aba **“NF-e/NFC-e/CF-e”**, verifique se no campo **“NF-e”** está selecionada a opção **“Nota de crédito”**. Em seguida, confirme se no campo **“Tipo de nota fiscal de crédito”** está selecionada a opção **“Retorno”**.
- Na aba **"Livro Fiscal",** as seções **"CFOP's para DENTRO do estado"** e **"CFOP's para FORA do estado"** devem estar configuradas de modo compatível com uma operação de entrada/devolução. A CFOPs de entrada geralmente começam com o dígito "1" (Dentro do Estado) ou "2" (Fora do Estado)
- Além disso, para TOP de devolução de venda/compra/requisição, a opção de entrada deve estar configurada no campo **"Atualização do estoque"**

**(4)** Depois de selecionar uma nova Top, clique em **"Salvar".** Em seguida, transmita novamente a NF-e para a SEFAZ.

**CAUSA**

A causa da rejeição é a **incompatibilidade** entre o tipo de NF-e configurado como **"Crédito do tipo Retorno"** e o **Tipo de Operação** que não está configurado como **"Entrada"**. A Sefaz exige que todas as notas de crédito de retorno sejam obrigatoriamente operações de entrada.
