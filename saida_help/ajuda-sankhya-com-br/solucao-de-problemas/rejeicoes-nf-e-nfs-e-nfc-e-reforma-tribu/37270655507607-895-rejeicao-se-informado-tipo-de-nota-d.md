---
id: "37270655507607"
titulo: "895 Rejeição: Se informado tipo de nota de crédito (tag: tpNFCredito) Finalidade <> 5 - Nota de Crédito (tag: finNFe)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37270655507607-895-Rejei%C3%A7%C3%A3o-Se-informado-tipo-de-nota-de-cr%C3%A9dito-tag-tpNFCredito-Finalidade-5-Nota-de-Cr%C3%A9dito-tag-finNFe"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:33Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "TOP", "Nota de Crédito (tag: finNFe)", "Configuração com finalidade finNFe = 5", "Tipo de Nota Fiscal de Crédito", "tag: tpNFCredito"]
---

# 895 Rejeição: Se informado tipo de nota de crédito (tag: tpNFCredito) Finalidade <> 5 - Nota de Crédito (tag: finNFe)

**MENSAGEM:**

895 Rejeição: Se informado tipo de nota de crédito (tag: tpNFCredito) Finalidade <> 5 - Nota de Crédito (tag: finNFe)

**SITUAÇÃO:**

A NF-e é rejeitada quando a tag `<tpNFCredito>` está presente no XML e a finalidade da nota (`finNFe`) **não está configurada como 5 – Nota de Crédito**.

**SOLUÇÃO:**

Siga o passo a passo para corrigir a rejeição:

**(1)** Acesse a tela [**''Tipos de Operação''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Selecione a TOP utilizada para emitir a NF-e rejeitada.

**(3)** Na aba ''**NF-e/NFC-e/CF-e''** verifique o campo **''NF-e''**:

- Se a operação for uma **Nota de Crédito**, selecione a opção ''**Nota de Crédito''**.
- Esse ajuste habilita o preenchimento do **Tipo de Nota Fiscal de Crédito**.

**(4)** Caso a operação corresponda a uma Nota de Crédito, localize o campo ''**Tipo de Nota Fiscal de Crédito''** e selecione uma das opções disponíveis no sistema:

- Multa e Juros
- Apropriação de crédito presumido
- Retorno

Essas opções definem o valor enviado na tag **<tpNFCredito>** do XML.

**(5)** Salve as alterações na TOP e transmita novamente a NF-e.

**(6)** Aguarde o retorno da SEFAZ e confirme a autorização da nota.

**CAUSA:**

A rejeição ocorre porque a tag `<tpNFCredito>` é gerada indevidamente no XML quando a nota **não está configurada com finalidade**`finNFe = 5`**(Nota de Crédito)**.

Isso acontece devido à **configuração incorreta na TOP**, especialmente na aba ''NF-e/NFC-e/CF-e''.
