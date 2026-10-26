---
id: "37096950124951"
titulo: "1170 Rejeição: Grupo de Ajuste de Competência não informado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096950124951-1170-Rejei%C3%A7%C3%A3o-Grupo-de-Ajuste-de-Compet%C3%AAncia-n%C3%A3o-informado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:02Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Nota Fiscal Eletrônica (NF-e)", "Alíquotas de CBS", "Alíquotas de IBS", "Código de Situação Tributária (CST)", "Grupo de Ajuste de Competência", "CST exige o preenchimento do grupo de ajuste de competência"]
---

# 1170 Rejeição: Grupo de Ajuste de Competência não informado [nItem: 999]

**MENSAGEM**

1170 Rejeição: Grupo de Ajuste de Competência não informado [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) com um CST que exige o preenchimento do grupo de ajuste de competência, o documento foi rejeitado pela SEFAZ porque este grupo obrigatório não foi informado.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a operação utilizada na nota fiscal rejeitada.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se os campos **"Tipo de Nota Fiscal de Crédito"** e/ou **"Tipo de Nota Fiscal de Débito"** estão configurados corretamente para a operação.

**(3)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(4)** Verifique se o **Código de Situação Tributária (CST)** do item realmente exige o Ajuste de Competência.

- O sistema só permite esse grupo se o indicador do código for igual a 1 (`ind_gAjusteCompet = 1`)

**(5)** Na seção **''Impostos''**, inclua as informações do grupo de ajuste de competência, preenchendo os valores de IBS e/ou CBS conforme necessário.

**(6)** Certifique-se de que pelo menos um dos valores (IBS ou CBS) seja maior que zero, conforme exigido pela regra de validação UB112-30.

**(7)** Após realizar as correções, emita a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando um **CST do IBS/CBS** que possui indicador que obriga o preenchimento do grupo de ajuste de competência (ind\_gAjusteCompet = 1) é utilizado na nota fiscal, mas o grupo **"gAjusteCompet"** não foi informado. De acordo com a regra de validação UB112-20, quando o CST possui este indicador, é obrigatório informar o grupo de ajuste de competência. Além disso, conforme a regra UB112-30, quando este grupo é informado, pelo menos um dos valores (IBS ou CBS) deve ser maior que zero. Esta validação faz parte das novas regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025), que introduziu os novos tributos IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços).
