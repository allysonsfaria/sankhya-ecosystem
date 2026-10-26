---
id: "37097077436567"
titulo: "1053 Rejeição: Crédito Presumido para o IBS informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097077436567-1053-Rejei%C3%A7%C3%A3o-Cr%C3%A9dito-Presumido-para-o-IBS-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:55Z"
rotulos: ["NF-e", "SEFAZ", "Crédito", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Reforma Tributária", "Nota Fiscal Eletrônica (NF-e)", "Crédito Presumido para o IBS", "Código de Crédito Presumido", "IBS informado indevidamente"]
---

# 1053 Rejeição: Crédito Presumido para o IBS informado indevidamente [nItem: 999]

**MENSAGEM**

1053 Rejeição: Crédito Presumido para o IBS informado indevidamente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma **Nota Fiscal Eletrônica (NF-e)**, **foi informado Crédito Presumido de IBS na NF-e**, porém a classificação tributária utilizada no item **não permite a utilização desse tipo de crédito**.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o Código de Situação Tributária - (CST) utilizado na operação.

**(2)** Confirme se o CST utilizado permite o uso de crédito presumido para o IBS. Caso não permita, será necessário **remover o grupo de crédito presumido** da nota fiscal ou **alterar o CST** para um que permita esse tipo de crédito.

**(3)** Se estiver utilizando o **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), verifique se o **código de crédito presumido (cCredPres)** está configurado corretamente para o CST utilizado.

**(4)** Caso seja necessário emitir a nota com crédito presumido, selecione um CST que possua o indicador que permite o uso de crédito presumido para o IBS (ind\_gIBSCredPres = 1). 

**CAUSA**

A rejeição 1053 ocorre devido a uma incompatibilidade entre o CST utilizado e a informação de crédito presumido para o IBS. De acordo com a regra de validação UB123-10, quando o código de crédito presumido (cCredPres) possui indicador que não permite o uso de crédito presumido para o IBS (ind\_gIBSCredPres = 0), o sistema da SEFAZ rejeita a nota fiscal caso o grupo de crédito presumido para o IBS seja informado indevidamente.

Esta validação faz parte das regras implementadas pela Lei Complementar 214/2025 no contexto da Reforma Tributária, que estabelece critérios específicos para a utilização de créditos presumidos do IBS de acordo com a classificação tributária da operação.
