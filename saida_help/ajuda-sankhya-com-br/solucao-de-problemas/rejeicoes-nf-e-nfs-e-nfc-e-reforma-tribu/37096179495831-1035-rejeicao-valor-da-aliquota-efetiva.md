---
id: "37096179495831"
titulo: "1035 Rejeição: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096179495831-1035-Rejei%C3%A7%C3%A3o-Valor-da-Al%C3%ADquota-Efetiva-do-IBS-da-UF-calculado-incorretamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:25Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquota de IBS", "Alíquotas de IBS", "Alíquota de CBS", "Alíquota Efetiva do IBS", "Grupo de Redução de Alíquota do IBS da Unidade Federada", "Valor da Alíquota Efetiva", "Alíquota Efetiva do IBS da UF"]
---

# 1035 Rejeição: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente [nItem: 999]

**MENSAGEM**

1035 Rejeição: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente [nItem: 999]

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com o grupo de Redução de Alíquota do IBS da Unidade Federada (gIBSUF/gRed), o sistema identificou que o valor da Alíquota Efetiva (pAliqEfet) foi calculado incorretamente, resultando na rejeição do documento fiscal pela SEFAZ.

**SOLUÇÃO**

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação utilizada está configurada corretamente para a tributação do IBS da UF.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se as alíquotas do IBS da UF estão configuradas corretamente para o produto e operação em questão.

**(3)** Verifique se o **CST** utilizado permite a aplicação de redução de alíquota. Caso o CST não permita, remova a informação de redução de alíquota.

**(4)** Se o CST permitir redução de alíquota, verifique se o **percentual de redução** está configurado corretamente e se é válido para a classificação tributária utilizada.

**(5)** Verifique se a **Alíquota Efetiva** está sendo calculada corretamente conforme a fórmula:

- Para operações **sem compra governamental**:

```
pAliqEfet = pIBSUF × (1 - (pRedAliq / 100))
```

- Para operações com compra governamental:

```
pAliqEfet = pIBSUF × (1 - (pRedAliq / 100)) × (1 - (pRedAliqGov / 100)).
```

**(6)** Após realizar as correções necessárias, tente emitir o documento fiscal novamente.

**CAUSA**

A rejeição ocorre quando o valor da Alíquota Efetiva (pAliqEfet) do IBS da UF informado no documento fiscal não corresponde ao resultado do cálculo esperado pela SEFAZ. Conforme a regra de validação UB28-10, quando informado o grupo de Redução de Alíquota (gIBSUF/gRed), a Alíquota Efetiva deve ser calculada considerando o percentual de redução aplicado à alíquota original do IBS da UF.

Esta validação está em conformidade com as regras estabelecidas pela Lei Complementar 214/2025, que regulamenta a implementação do Imposto sobre Bens e Serviços (IBS) no âmbito da Reforma Tributária. O cálculo incorreto pode ocorrer devido a erros na configuração das alíquotas, percentuais de redução incompatíveis com o CST utilizado, ou falhas no processamento do cálculo pelo sistema.
