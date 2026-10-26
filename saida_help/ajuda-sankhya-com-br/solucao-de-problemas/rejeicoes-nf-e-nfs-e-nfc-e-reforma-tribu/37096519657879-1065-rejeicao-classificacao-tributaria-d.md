---
id: "37096519657879"
titulo: "1065 Rejeição: Classificação Tributária do IBS e da CBS informada obriga informação da tributação regular [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096519657879-1065-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-informada-obriga-informa%C3%A7%C3%A3o-da-tributa%C3%A7%C3%A3o-regular-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-06T19:25:51Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Classificação Tributária do IBS e da CBS", "Classificação Tributária", "Código de Situação Tributária Regular", "Tributação regular", "Código de Classificação Tributária Regular"]
---

# 1065 Rejeição: Classificação Tributária do IBS e da CBS informada obriga informação da tributação regular [nItem: 999]

**MENSAGEM**

1065 Rejeição: Classificação Tributária do IBS e da CBS informada obriga informação da tributação regular [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e com a nova tributação do IBS e CBS, o documento foi rejeitado pela SEFAZ porque a **Classificação Tributária** selecionada exige que seja informado o grupo de **Tributação Regular**, porém este grupo não foi informado no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(2)** Verifique a **Classificação Tributária** que está sendo utilizada na operação e confirme se ela exige a informação do grupo de Tributação Regular.

**(3)** Acesse as telas **''Alíquotas de IBS'**' (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e selecione a alíquota utilizada na operação.

**(4)** Na aba **"Tributação"**, preencha os campos obrigatórios:

- Selecione o **"Código de Situação Tributária Regular"** adequado para a operação;
- Informe a **"Código de Classificação Tributária Regular"** compatível com o CST Regular.

**(5)** Salve as alterações e tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre porque a **Classificação Tributária do IBS e da CBS** informada no documento fiscal possui um indicador que **exige** a informação do grupo de Tributação Regular (ind\_gTribRegular = 1), conforme estabelecido nas regras de validação da SEFAZ.

De acordo com a regra de validação UB68-10, quando a Classificação Tributária (cClassTrib) informada possui indicador que exige a informação do grupo de Tributação Regular, este grupo deve ser obrigatoriamente preenchido no documento fiscal.

A Tributação Regular é um componente essencial para determinadas classificações tributárias no contexto da Reforma Tributária, pois complementa as informações necessárias para o correto cálculo e aplicação do IBS e da CBS.
