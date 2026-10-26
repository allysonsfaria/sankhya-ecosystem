---
id: "37141331241239"
titulo: "1016 Rejeição: CST do Imposto Seletivo obriga informação de alíquota de Imposto Seletivo [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141331241239-1016-Rejei%C3%A7%C3%A3o-CST-do-Imposto-Seletivo-obriga-informa%C3%A7%C3%A3o-de-al%C3%ADquota-de-Imposto-Seletivo-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:32Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquotas de IBS", "CST do Imposto Seletivo", "Imposto Seletivo (IS)", "Alíquota do Imposto Seletivo", "Quantidade Tributável", "alíquota (pIS) foi preenchido com valor zero ou não foi preenchido", "Unidade Tributável"]
---

# 1016 Rejeição: CST do Imposto Seletivo obriga informação de alíquota de Imposto Seletivo [nItem: 999]

**MENSAGEM**

1016 Rejeição: CST do Imposto Seletivo obriga informação de alíquota de Imposto Seletivo [nItem: 999]

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) contendo produtos sujeitos ao Imposto Seletivo (IS), foi informado um Código de Situação Tributária (CST) do Imposto Seletivo que exige a informação da alíquota, porém o campo de alíquota (pIS) foi preenchido com valor zero ou não foi preenchido.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS), **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e **''Alíquotas de IS''** (Livros Fiscais » Cadastros » Aliquotas de IS).

**(2)** Verifique se o CST do Imposto Seletivo configurado para o produto exige a informação de alíquota.

**(3)** Verifique se o produto está corretamente classificado na NCM (Nomenclatura Comum do Mercosul) que corresponde a produtos sujeitos ao Imposto Seletivo:

- **Tabaco**: (NCM 2401, 2402, 2403, 2404).
- **Bebidas alcoólica**s: (NCM 2203, 2204, 2205, 2206, 2208).

**(4)** Retorne ao passo 1 e localize o registro correspondente ao produto.

**(5)** Na aba **''Tributação''**, na seção **''Alíquota''**, no campo **''Alíquota IS''** (campo "pIS") informe a alíquota do Imposto Seletivo com valor maior que zero, conforme a legislação vigente para o produto.

**(6)** Caso seja necessário, também preencha os campos "**Unidade Tributável**" (uTrib) e "**Quantidade Tributável**" (qTrib) do Imposto Seletivo, que são obrigatórios quando o IS é aplicável.

**(7)** Após realizar as alterações necessárias, tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre devido à inconsistência entre o CST (Código de Situação Tributária) do Imposto Seletivo informado e a alíquota correspondente. De acordo com a regra de validação UB06-10 da Sefaz, quando o CST do Imposto Seletivo informado exige a aplicação de uma alíquota (tag: pIS), esta deve ser preenchida com valor diferente de zero.

O Imposto Seletivo, instituído pela Lei Complementar nº 214/2025 como parte da Reforma Tributária, incide sobre produtos específicos como tabaco e bebidas alcoólicas. Quando o produto se enquadra nas NCMs sujeitas ao IS (2401, 2402, 2403, 2404, 2203, 2204, 2205, 2206, 2208) e o CST utilizado exige tributação, a alíquota correspondente deve ser obrigatoriamente informada com valor maior que zero.
