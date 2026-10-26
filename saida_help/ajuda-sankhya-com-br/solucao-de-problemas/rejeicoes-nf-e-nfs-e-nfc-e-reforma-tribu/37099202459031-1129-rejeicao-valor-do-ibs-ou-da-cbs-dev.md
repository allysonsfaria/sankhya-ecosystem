---
id: "37099202459031"
titulo: "1129 Rejeição: Valor do IBS ou da CBS deve ser maior que zero na transferência de crédito. [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099202459031-1129-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-na-transfer%C3%AAncia-de-cr%C3%A9dito-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:56Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Crédito", "Impostos", "TOP", "Financeiro", "Código de Situação Tributária", "Tipo de Nota Fiscal de Débito", "NF-e com finalidade de transferência de crédito", "IBS e/ou CBS foram informados como zero ou não foram preenchidos", "Valor do IBS ou da CBS deve ser maior que zero"]
---

# 1129 Rejeição: Valor do IBS ou da CBS deve ser maior que zero na transferência de crédito. [nItem: 999]

**MENSAGEM**

1129 Rejeição: Valor do IBS ou da CBS deve ser maior que zero na transferência de crédito. [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal de Débito (NF-e) com finalidade de transferência de crédito, o documento foi rejeitado pela SEFAZ porque os valores do IBS (Imposto sobre Bens e Serviços) e/ou da CBS (Contribuição sobre Bens e Serviços) foram informados como zero ou não foram preenchidos no grupo de transferência de crédito.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Na aba **''NF-e/NFC-e/CF-e''**, verifique se o campo **''NF-e''** está configurado como **''Nota de Débito''**.

**(3)** Verifique se o campo **''Tipo de Nota Fiscal de Débito''** está configurado como **''05 - Transferência de crédito de sucessão"** ou **"01 - Transferência de créditos para Cooperativas"**.

**(4)** Acesse a tela [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

**(5)** Abra a nota fiscal, clique em **''Outras Opções'' (ícone com três pontos)** e selecione **''Consultar/Alterar Dados do Imposto do Item''.**

**(6)** Nas seções **''IBS/CBS''** verifique o campo **''Código de Situação Tributária''** informado permite a transferência de crédito.

**(7)** No grupo **"Transferência de Crédito"**, preencha os campos:

- **"Valor do IBS"** com um valor maior que zero, ou
- **"Valor da CBS"** com um valor maior que zero.

**(8)** Certifique-se de que pelo menos um dos valores (IBS ou CBS) seja maior que zero para que a transferência de crédito seja válida.

**CAUSA**

Esta rejeição ocorre devido à regra de validação UB106-40 da SEFAZ, que determina que quando informado o grupo IBSCBS\gTransfCred, o valor do IBS (tag: gTransfCred\vIBS) ou da CBS (tag: gTransfCred\vCBS) deve ser maior que 0.

A transferência de crédito só é permitida em notas fiscais com finalidade específica (Nota de Débito) e para tipos específicos de operação (transferência de crédito de sucessão ou transferência de créditos para Cooperativas).

Além disso, para que a transferência seja válida, é necessário que pelo menos um dos valores (IBS ou CBS) seja maior que zero, caso contrário, a nota será rejeitada pela SEFAZ.
