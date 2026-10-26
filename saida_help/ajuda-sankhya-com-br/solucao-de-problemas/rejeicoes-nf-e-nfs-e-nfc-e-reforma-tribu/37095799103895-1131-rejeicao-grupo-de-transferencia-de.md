---
id: "37095799103895"
titulo: "1131 Rejeição: Grupo de transferência de crédito informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095799103895-1131-Rejei%C3%A7%C3%A3o-Grupo-de-transfer%C3%AAncia-de-cr%C3%A9dito-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:32Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "incompatibilidade entre o CST do IBS/CBS", "Tipo de Nota Fiscal de Débito", "Alíquotas de CBS", "Alíquotas de IBS", "Grupo de transferência de crédito", "Transferência de Crédito do IBS/CBS"]
---

# 1131 Rejeição: Grupo de transferência de crédito informado indevidamente [nItem: 999]

**MENSAGEM**

1131 Rejeição: Grupo de transferência de crédito informado indevidamente [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada na emissão de uma nota fiscal eletrônica (NF-e) quando é informado o grupo de **Transferência de Crédito do IBS/CBS** em conjunto com um CST que não permite a utilização desse grupo no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o CST do IBS/CBS utilizado na operação.

**(2)** Acesse a aba **"NF-e/NFC-e/CF-e"** e verifique se o campo **"NF-e"** está configurado com a finalidade **"Nota de Débito"**.

**(3)** Caso esteja configurado como Nota de Débito, verifique se o campo **"Tipo de Nota Fiscal de Débito"** está configurado com um valor **diferente** de **"05-Transferência de crédito de sucessão"** ou **"01-Transferência de créditos para Cooperativas"**.

**(4)** Se o problema persistir, acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o CST do IBS/CBS utilizado possui indicador que **não permite** a informação de transferência de crédito.

**(5)** Altere o CST do IBS/CBS para um código que seja compatível com a operação desejada, ou remova o grupo de transferência de crédito caso não seja necessário para a operação.

**CAUSA**

A rejeição ocorre devido a uma **incompatibilidade entre o CST do IBS/CBS** informado e o **grupo de transferência de crédito**. Conforme a regra de validação UB13-44 da Sefaz, quando o CST do IBS/CBS possui um indicador que não permite a informação do grupo de transferência de crédito (ind\_gTransfCred = 0), o grupo gTransfCred não deve ser informado no documento fiscal.

Além disso, a regra UB106-30 estabelece que o grupo de transferência de crédito só pode ser informado quando a finalidade da NF-e for "Nota de Débito" e o tipo de nota de débito for "05-Transferência de crédito de sucessão" ou "01-Transferência de créditos para Cooperativas".

Esta validação faz parte das novas regras implementadas pela Reforma Tributária, conforme a Lei Complementar 214 de 16 de janeiro de 2025, que estabelece os critérios para transferência de créditos do IBS e da CBS.
