---
id: "37096926725911"
titulo: "1169 Rejeição: Grupo de Ajuste de Competência informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096926725911-1169-Rejei%C3%A7%C3%A3o-Grupo-de-Ajuste-de-Compet%C3%AAncia-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:03Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "TOP", "Erro", "Nota Fiscal Eletrônica (NF-e)", "Código de Situação Tributária (CST)", "Grupo de Ajuste de Competência", "Ajuste de Competência", "Incompatibilidade entre o CST utilizado"]
---

# 1169 Rejeição: Grupo de Ajuste de Competência informado indevidamente [nItem: 999]

**MENSAGEM**

1169 Rejeição: Grupo de Ajuste de Competência informado indevidamente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e), o sistema está rejeitando a operação porque foi informado o grupo de Ajuste de Competência para um item que possui um **Código de Situação Tributária (CST)** que não permite a utilização deste grupo.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Verifique o CST utilizado na operação que está gerando a rejeição.

**(3)** Confira se o **CST** selecionado possui o indicador que **veda o preenchimento do grupo de ajuste de competência** (ind\_gAjusteCompet = 0).

**(4)** Caso o CST realmente não permita o uso do grupo de ajuste de competência, você tem duas opções:

- Remova o grupo de Ajuste de Competência da nota fiscal.
- Altere o CST para um que permita a utilização do grupo de Ajuste de Competência (ind\_gAjusteCompet = 1).

**(5)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(6)** Selecione o TOP utilizado e remova o grupo de Ajuste de Competência.

**(7)** Na aba **''Impostos''**, verifique as configurações relacioandas ao **Ajuste de Competência** e desabilite esta opção para o TOP em questão.

**(8)** Após realizar as alterações necessárias, tente emitir a nota fiscal novamente.

**CAUSA**

A rejeição ocorre devido a uma **incompatibilidade entre o CST utilizado** e a presença do grupo de Ajuste de Competência na nota fiscal. Conforme a regra de validação UB112-10, quando o CST possui um indicador que veda o preenchimento do grupo de ajuste de competência (ind\_gAjusteCompet = 0), este grupo não deve ser informado na nota fiscal. Cada CST possui indicadores específicos que determinam quais grupos de informações podem ou não ser utilizados na nota fiscal. No caso do grupo de Ajuste de Competência, alguns CSTs não permitem sua utilização, e quando este grupo é informado indevidamente, a validação da Sefaz rejeita a nota fiscal com o código 1169.
