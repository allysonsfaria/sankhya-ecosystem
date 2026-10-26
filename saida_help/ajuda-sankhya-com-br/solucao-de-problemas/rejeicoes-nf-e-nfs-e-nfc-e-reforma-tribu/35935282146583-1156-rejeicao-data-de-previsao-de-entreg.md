---
id: "35935282146583"
titulo: "1156 Rejeição: Data de Previsão de Entrega informada e Finalidade de Emissão diferente de \"1 - NF-e normal\" ou \"4 - Devolução de mercadoria\"."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35935282146583-1156-Rejei%C3%A7%C3%A3o-Data-de-Previs%C3%A3o-de-Entrega-informada-e-Finalidade-de-Emiss%C3%A3o-diferente-de-1-NF-e-normal-ou-4-Devolu%C3%A7%C3%A3o-de-mercadoria"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:24:19Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Erro", "1156 Rejeição", "Data de Previsão de Entrega informada", "Finalidade de Emissão diferente de \"1 - NF-e normal\"", "Rejeição 1156", "\"4 - Devolução de mercadoria\""]
---

# 1156 Rejeição: Data de Previsão de Entrega informada e Finalidade de Emissão diferente de "1 - NF-e normal" ou "4 - Devolução de mercadoria".

**MENSAGEM**

1156 Rejeição: Data de Previsão de Entrega informada e Finalidade de Emissão diferente de "1 - NF-e normal" ou "4 - Devolução de mercadoria".

**SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma nota fiscal eletrônica (NF-e) que possui o campo **"Data de Previsão de Entrega"** preenchido, porém a **"Finalidade de Emissão"** está configurada com valor diferente de **"1 - NF-e normal"** ou **"4 - Devolução de mercadoria"**.

**SOLUÇÃO**

Siga o passo a passo abaixo para corrigir a rejeição:

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Selecione a nota fiscal que apresentou a rejeição.

**(3)** Na grade **''Cabeçalho''**, verifique o campo **''Tipo de Operação''** e identifique o TOP usado na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(5)** Busque e selecione o TOP identificado no passo 3.

**(6)** Na aba **“NF-e/NFC-e/CF-e”**, verifique a configuração do campo **“NF-e”**, confirmando qual opção está selecionada e se ela está de acordo com o tipo de operação que está sendo realizada.

![Imagem 1: (6) Na aba “NF-e/NFC-e/CF-e” , verifique a configuração do campo “NF-e” , confirmando qual opção está selecionada e se…](https://ajuda.sankhya.com.br/hc/article_attachments/35935282134935)

**(7)** Retorne ao passo 1, na grade ''Cabeçalho'', verifique o campo **"Previsão de Entrega"**.

**(8)** Corrija a inconsistência conforme o cenário identificado:

- Se a nota fiscal deveria ser **Normal** ou de **Devolução**, altere a **TOP** utilizada, selecionando uma TOP correspondente ao tipo correto de operação.
- Se a finalidade da nota fiscal for **Complementar** ou **Ajuste**, remova o valor informado no campo “Previsão de Entrega” e salve a alteração.

**(9)** Após realizar a correção, transmita novamente a nota fiscal para a **Sefaz**.

**CAUSA**

A rejeição ocorre porque a legislação permite informar a **"Data de Previsão de Entrega"** apenas quando a **"Finalidade de Emissão"** da nota fiscal for **"1 - NF-e normal"** ou **"4 - Devolução de mercadoria"**. Se a finalidade for diferente, o preenchimento desse campo não é permitido.
