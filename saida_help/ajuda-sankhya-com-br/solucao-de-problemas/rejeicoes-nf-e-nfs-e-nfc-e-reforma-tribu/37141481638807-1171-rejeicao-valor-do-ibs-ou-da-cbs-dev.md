---
id: "37141481638807"
titulo: "1171 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no ajuste de competência [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141481638807-1171-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-no-ajuste-de-compet%C3%AAncia-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:14Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "Rejeição", "Alíquotas de CBS", "Alíquotas de IBS", "grupo de ajuste de competência", "valores do IBS", "Valores do IBS ou da CBS foram informados com zero ou não foram preenchidos"]
---

# 1171 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no ajuste de competência [nItem: 999]

**MENSAGEM**

1171 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no ajuste de competência [nItem: 999]

**SITUAÇÃO**

Ao emitir um documento fiscal com o grupo de ajuste de competência (gAjusteCompet), os valores do IBS (Imposto sobre Bens e Serviços) ou da CBS (Contribuição sobre Bens e Serviços) foram informados com valor zero ou não foram preenchidos, gerando a rejeição pela SEFAZ.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela de "**Notas Fiscais**" (Gestão Fiscal » Movimentação » Notas Fiscais) e localize o documento fiscal que apresentou a rejeição.

**(2)** Verifique se o CST utilizado possui indicador que obriga o preenchimento do grupo de ajuste de competência (**ind\_gAjusteCompet = 1**).

**(3)** Acesse a aba "**Itens**" da nota fiscal e selecione o item que apresentou a rejeição.

**(4)** Na seção "**IBS/CBS**", localize o grupo "**Ajuste de Competência**" e verifique os valores informados.

**(5)** Certifique-se de que pelo menos um dos campos a seguir esteja preenchido com valor **maior que zero**: Campo "**Valor do IBS**" (gAjusteCompet/vIBS) Campo "**Valor da CBS**" (gAjusteCompet/vCBS).

**(6)** Após realizar as correções necessárias, salve as alterações e tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o documento fiscal possui o grupo de ajuste de competência (gAjusteCompet) informado, mas os valores do IBS (Imposto sobre Bens e Serviços) ou da CBS (Contribuição sobre Bens e Serviços) estão zerados ou não foram preenchidos. De acordo com a regra de validação UB112-30 da SEFAZ, quando o grupo de ajuste de competência é informado, pelo menos um dos valores (IBS ou CBS) deve ser maior que zero.

Esta validação faz parte das regras implementadas pela Lei Complementar 214/2025 no contexto da Reforma Tributária, que estabelece a necessidade de informar corretamente os valores dos novos tributos (IBS e CBS) nos documentos fiscais, inclusive nos casos de ajuste de competência.
