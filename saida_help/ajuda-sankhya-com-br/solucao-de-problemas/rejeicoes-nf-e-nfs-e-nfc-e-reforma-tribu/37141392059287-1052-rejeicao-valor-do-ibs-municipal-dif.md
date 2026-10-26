---
id: "37141392059287"
titulo: "1052 Rejeição: Valor do IBS Municipal difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141392059287-1052-Rejei%C3%A7%C3%A3o-Valor-do-IBS-Municipal-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:21Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Regra de validação", "Alíquotas de CBS", "Alíquotas de IBS", "Valor calculado para o IBS Municipal", "NF-e ou NFC-e com tributação de IBS Municipal", "alíquota de IBS Municipal"]
---

# 1052 Rejeição: Valor do IBS Municipal difere do calculado [nItem: 999]

**MENSAGEM**

1052 Rejeição: Valor do IBS Municipal difere do calculado [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir um documento fiscal (NF-e ou NFC-e) com tributação de IBS Municipal, o sistema da Sefaz está rejeitando a nota fiscal porque o valor calculado para o IBS Municipal está diferente do valor que deveria ser calculado conforme a regra de validação estabelecida pela legislação.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se o valor do IBS Municipal (vIBSMun) está sendo calculado corretamente conforme a fórmula:

```
vIBSMun = (gIBSCBS/vBC x (pIBSMun / 100)) - vDif - vDevTrib.
```

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(3)** Verifique se a alíquota de IBS Municipal (pIBSMun) está configurada corretamente para o ano de emissão do documento:

- Para documentos emitidos em 2026: a alíquota deve ser igual a 0% (Art. 343 da LC 214/2025)
- Para documentos emitidos em 2027 e 2028: a alíquota deve ser igual a 0,05% (Art. 344 da LC 214/2025)

**(4)** Verifique se o CST utilizado está correto e se é compatível com a operação realizada. Se o CST possuir indicador de Tributação Regular, o pIBSMun deve ser igual a zero.

**(5)** Confira se os valores de diferimento (vDif) e devolução tributária (vDevTrib), quando aplicáveis, estão sendo calculados e informados corretamente:

- Se houver diferimento, verifique se o valor está sendo calculado conforme a fórmula:

```
vDif = vBC x (pIBSMun / 100) x (pDif / 100)
```

- Se houver devolução tributária, confirme se o valor está correto.

**(6)** Verifique se a base de cálculo (vBC) está correta e se corresponde ao valor utilizado para o cálculo do IBS Municipal.

**(7)** Após realizar as correções necessárias, tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o valor do IBS Municipal (vIBSMun) informado no documento fiscal não corresponde ao valor calculado pela Sefaz conforme a regra de validação UB54-10. O cálculo correto deve seguir a fórmula: vIBSMun = (gIBSCBS/vBC x (pIBSMun / 100)) - vDif - vDevTrib.

As causas mais comuns para esta rejeição são:

- Alíquota do IBS Municipal (pIBSMun) configurada incorretamente para o ano de emissão do documento
- Base de cálculo (vBC) informada incorretamente
- Valores de diferimento (vDif) ou devolução tributária (vDevTrib) calculados ou informados incorretamente
- CST incompatível com a operação realizada
- Erro no cálculo do valor do IBS Municipal pelo sistema emissor
