---
id: "37141551929495"
titulo: "1050 Rejeição: Crédito Presumido para a CBS informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141551929495-1050-Rejei%C3%A7%C3%A3o-Cr%C3%A9dito-Presumido-para-a-CBS-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:09Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Crédito", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS", "crédito presumido para a CBS", "código de crédito presumido (cCredPres)"]
---

# 1050 Rejeição: Crédito Presumido para a CBS informado indevidamente [nItem: 999]

**MENSAGEM**

1050 Rejeição: Crédito Presumido para a CBS informado indevidamente [nItem: 999]

**SITUAÇÃO**

O documento fiscal foi emitido com a informação de crédito presumido da CBS associada a um Código de Situação Tributária que não contempla a aplicação desse crédito no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Na aba **''Tributação''** confirme se o campo **''Código de Class. do Crédito Presumido''** permite a utilização de crédito presumido para a CBS.

**(3)** Caso o CST não permita o uso de crédito presumido, você tem duas opções:

- Remova as informações de crédito presumido para a CBS do documento fiscal, ou
- Altere o CST para um que permita a utilização de crédito presumido para a CBS, desde que adequado à operação.

**(4)** Para remover as informações de crédito presumido, acesse a tela de **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas), localize o documento rejeitado e:

- Selecione o item que apresenta o erro [nItem: 999]
- Remova as informações do grupo "Crédito Presumido para a CBS" (grupo: IBSCBS/gCredPresOper/gCBSCredPres).

**(5)** Se optar por alterar o CST, certifique-se de que o novo CST selecionado seja compatível com a operação e permita a utilização de crédito presumido para a CBS.

**CAUSA**

Esta rejeição ocorre devido a uma incompatibilidade entre o CST (Código de Situação Tributária) utilizado e a informação de crédito presumido para a CBS. De acordo com as regras de validação da Sefaz (UB127-10), quando o código de crédito presumido (cCredPres) possui um indicador que não permite o uso de crédito presumido para a CBS (ind\_gCBSCredPres = 0), o sistema rejeita a nota fiscal caso o grupo de crédito presumido para a CBS seja informado indevidamente.

Cada CST possui regras específicas sobre quais benefícios fiscais podem ser aplicados. Quando um crédito presumido é informado para um CST que não permite este tipo de benefício, o sistema de validação da Sefaz rejeita o documento fiscal para garantir a conformidade com a legislação tributária estabelecida pela Lei Complementar 214/2025.
