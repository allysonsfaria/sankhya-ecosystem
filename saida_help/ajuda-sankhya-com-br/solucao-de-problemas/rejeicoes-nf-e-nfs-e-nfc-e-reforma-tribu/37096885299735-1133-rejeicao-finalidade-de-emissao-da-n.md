---
id: "37096885299735"
titulo: "1133 Rejeição: Finalidade de Emissão da Nota Fiscal incompatível com o CST [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096885299735-1133-Rejei%C3%A7%C3%A3o-Finalidade-de-Emiss%C3%A3o-da-Nota-Fiscal-incompat%C3%ADvel-com-o-CST-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:05Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Nota de Débito", "Nota Fiscal Eletrônica (NF-e)", "Alíquotas de CBS", "Alíquotas de IBS", "Transferência de crédito do IBS ou CBS", "Assistente de Configuração Integral da Reforma Tributária", "Código de Situação Tributária (CST)", "CST (Código de Situação Tributária) do IBS/CBS"]
---

# 1133 Rejeição: Finalidade de Emissão da Nota Fiscal incompatível com o CST [nItem: 999]

**MENSAGEM**

1133 Rejeição: Finalidade de Emissão da Nota Fiscal incompatível com o CST [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma nota fiscal eletrônica (NF-e) com transferência de crédito do IBS ou CBS, o sistema está rejeitando a operação porque a finalidade de emissão da nota fiscal não está configurada corretamente para o Código de Situação Tributária (CST) utilizado.

**SOLUÇÃO**

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize o tipo de operação que está sendo utilizado na nota fiscal rejeitada.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique o campo **"NF-e"** e selecione a opção **"Nota de Débito"**.

**(3)** No campo **"Tipo de Nota Fiscal de Débito"**, selecione uma das seguintes opções:

- **"01 - Transferência de créditos para Cooperativas"**
- **"05 - Transferência de crédito de sucessão"**.

**(4)** Salve as alterações.

**(5)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(6)** Verifique se o CST do IBS/CBS utilizado na nota fiscal é compatível com operações de transferência de crédito.

**(7)** Certifique-se de que o grupo **"gTransfCred"** esteja sendo informado corretamente na nota fiscal para o CST utilizado.

**(8)** Emita a nota fiscal novamente com as configurações corretas.

**CAUSA**

Esta rejeição ocorre quando há uma incompatibilidade entre o CST (Código de Situação Tributária) do IBS/CBS informado na nota fiscal e a finalidade de emissão configurada. De acordo com as regras de validação da SEFAZ, quando um CST que exige informação do grupo de Transferência de Crédito (gTransfCred) é utilizado, a finalidade da nota fiscal **deve ser obrigatoriamente** "Nota de Débito" e o tipo de nota de débito deve ser "01 - Transferência de créditos para Cooperativas" ou "05 - Transferência de crédito de sucessão".

A validação UB106-30 da SEFAZ verifica especificamente se, quando informado o grupo IBSCBS\gTransfCred, a finalidade de emissão da nota fiscal (finNFe) é igual a 6 (Nota de Débito). Caso contrário, a nota é rejeitada com o código 1133.
