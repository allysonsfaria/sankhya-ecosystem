---
id: "37228242317335"
titulo: "E0707 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228242317335-E0707-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:12Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquotas de ICMS", "Rejeição", "Alíquota tributária", "Valor menor que 0% ou maior que 100%", "Alíquota informada está fora do intervalo permitido", "Redução de base de cálculo"]
---

# E0707 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

**MENSAGEM**

E0707 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o documento fiscal foi **rejeitado pela SEFAZ** com a mensagem acima, indicando que uma **alíquota informada está fora do intervalo permitido**.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** **Identifique o imposto com alíquota inválida**

- Analise a mensagem de rejeição detalhada e verifique qual tributo está com a alíquota fora do intervalo permitido, como **ICMS, IBS, CBS, PIS, COFINS** ou outro imposto informado no documento.

**(2)** Acesse o cadastro da alíquota correspondente:

- Para **ICMS**, acesse a tela ''**Alíquotas de ICMS''** (Comercial » Relatórios » Cadastros » Alíquotas de ICMS).
- Para **IBS**, **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS).
- Para **CBS ''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(3)** Localize a **regra de alíquota** que foi aplicada ao produto ou serviço da nota fiscal rejeitada.

Utilize os filtros disponíveis para facilitar a busca, como:

- "Tipo de Operação"
- "UF de Origem"
- "UF de Destino"
- "Código de Situação Tributária - CST"

**(4)** Verifique o campo **"Alíquota"** ou **"Percentual (%)"** da regra identificada e certifique-se de que o valor está **entre 0 e 100**. Caso o valor esteja fora desse intervalo, corrija-o imediatamente.

**(5)** Caso o erro esteja relacionado a **campos de redução de base de cálculo** ou **alíquotas de crédito**, verifique também esses campos e ajuste os valores para que estejam dentro do intervalo permitido

**(6)** Salve as alterações realizadas no cadastro de alíquotas.

**(7)** Retorne à nota fiscal rejeitada, **inutilize a numeração** caso necessário e realize um **novo faturamento**.

**(8)** Confira se as **alíquotas aplicadas** estão corretas e dentro do intervalo permitido antes de confirmar a nota.

**(9)** Proceda com a **autorização da NF-e ou NFC-e** junto à SEFAZ.

**CAUSA**

A rejeição E0707 ocorre quando o sistema identifica que **alguma alíquota tributária informada no documento fiscal está fora do intervalo válido**, ou seja, possui valor **menor que 0% ou maior que 100%**. Essa validação é realizada pela SEFAZ para garantir a **consistência dos dados tributários** transmitidos.

As principais causas incluem:

- Cadastro incorreto de **alíquotas de ICMS, IBS, CBS, PIS ou COFINS** com valores negativos ou superiores a 100%.
- Erro de digitação ao informar o **percentual da alíquota** no cadastro de regras tributárias.
- Configuração inadequada de **campos de redução de base de cálculo** ou **alíquotas de crédito**.
- Utilização de **regras tributárias desatualizadas** ou incompatíveis com a legislação vigente.

**Importante:** Esse ajuste deve ser realizado por um **usuário com conhecimento fiscal e tributário**, preferencialmente com orientação do contador responsável, para evitar impactos indevidos na apuração de impostos.
