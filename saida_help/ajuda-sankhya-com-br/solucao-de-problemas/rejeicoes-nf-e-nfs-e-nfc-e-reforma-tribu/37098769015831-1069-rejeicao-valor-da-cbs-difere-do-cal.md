---
id: "37098769015831"
titulo: "1069 Rejeição: Valor da CBS difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098769015831-1069-Rejei%C3%A7%C3%A3o-Valor-da-CBS-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:09Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Alíquota de IBS", "Alíquota Efetiva", "Alíquotas de CBS", "Alíquota de CBS", "Diferimento", "CBS difere do calculado", "grupo de Redução de Alíquota", "Devolução tributária"]
---

# 1069 Rejeição: Valor da CBS difere do calculado [nItem: 999]

**MENSAGEM**

1069 Rejeição: Valor da CBS difere do calculado [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com a tributação da CBS (Contribuição sobre Bens e Serviços), o documento foi rejeitado pela SEFAZ porque o valor calculado para a CBS não corresponde ao valor esperado conforme a fórmula de cálculo estabelecida pela legislação.

**SOLUÇÃO**

**(1)** Inicialmente, verifique se o sistema está atualizado para uma versão que contemple melhorias relacionadas ao cálculo da CBS.

Versões recomendadas:

- **Sankhya Om:** 4.35 b459
- **Sankhya Livros:** 4.26.1

Caso o sistema esteja em versão inferior, recomendamos realizar a atualização antes de prosseguir com as demais verificações.

**IMPORTANTE:** Mesmo em versões atualizadas, a rejeição **1069 – Valor da CBS difere do calculado** ainda pode ocorrer devido a **diferenças de arredondamento no cálculo do imposto**, principalmente quando são utilizadas múltiplas casas decimais na quantidade ou no valor unitário dos itens. Nesses casos, mesmo com a parametrização correta, poderá ser necessário **forçar o recálculo do item no documento fiscal** ou realizar **um ajuste manual no valor da CBS do item**, garantindo que o valor enviado no XML seja igual ao valor recalculado pela SEFAZ.

Para verificar e corrigir possíveis inconsistências na configuração do sistema, **siga os passos descritos abaixo:**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a configuração da tributação está correta para a operação que está sendo realizada.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique:

- Se a alíquota de CBS está configurada corretamente para o produto/serviço.
- Se o **CST** (Código de Situação Tributária) está adequado para a operação.
- Se o campo **''% do Diferimento''** ou a **devolução tributária** estão preenchidos corretamente, caso aplicáveis.

**(3)** Verifique se o valor da CBS está sendo calculado conforme a fórmula:

```
vCBS = (vBC x (pCBS / 100)) - vDif - vDevTrib
```

Onde:

• **vCBS:** Valor da CBS

• **vBC:** Base de cálculo

• **pCBS:** Alíquota da CBS (em percentual)

• **vDif:** Valor do diferimento (se houver)

• **vDevTrib:** Valor da devolução tributária (se houver)

**(4)** Se estiver emitindo documentos em 2025 ou 2026, verifique se a alíquota da CBS está configurada em **0,9%**, conforme determinado pelo Art. 346 da LC 214/2025.

**(5)** Caso esteja utilizando **grupo de Redução de Alíquota** (gCBS/gRed), certifique-se de que a **Alíquota Efetiva** (pAliqEfet) está calculada corretamente.

**(6)** Após realizar as correções, tente emitir o documento novamente.

**CAUSA**

Esta rejeição ocorre quando o valor da CBS informado no documento fiscal não corresponde ao valor calculado pela SEFAZ de acordo com a fórmula estabelecida na legislação. Conforme a regra de validação UB67-10, o valor da CBS (vCBS) deve ser resultante da fórmula: vCBS = (gIBSCBS/vBC x (pCBS / 100)) - vDif - vDevTrib.

As causas mais comuns para esta divergência são:

- Configuração incorreta da alíquota da CBS no cadastro de alíquotas.
- Erro no cálculo do valor do diferimento ou da devolução tributária, quando aplicáveis.
- Utilização de alíquota incorreta para o período de emissão do documento (em 2025 e 2026, a alíquota da CBS deve ser de 0,9%).
- Inconsistência na base de cálculo utilizada para o cálculo da CBS.
- Configuração incorreta do CST que afeta o cálculo da CBS.
