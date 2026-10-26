---
id: "37141427071511"
titulo: "1047 Rejeição: Valor da Alíquota Efetiva do IBS do Município calculado incorretamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141427071511-1047-Rejei%C3%A7%C3%A3o-Valor-da-Al%C3%ADquota-Efetiva-do-IBS-do-Munic%C3%ADpio-calculado-incorretamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:22Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Erro", "Valor da Alíquota Efetiva (pAliqEfet)", "Alíquota Efetiva", "Alíquotas de IBS", "Valor da Alíquota Efetiva do IBS", "Alíquota Efetiva do IBS do Município calculado", "Redução de Alíquota do IBS Municipal (gIBSMun/gRed)", "% da Redução de Alíquota IBS Municipal"]
---

# 1047 Rejeição: Valor da Alíquota Efetiva do IBS do Município calculado incorretamente [nItem: 999]

**MENSAGEM**

1047 Rejeição: Valor da Alíquota Efetiva do IBS do Município calculado incorretamente [nItem: 999]

**SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e) com grupo de Redução de Alíquota do IBS Municipal (gIBSMun/gRed), o sistema calculou incorretamente o valor da Alíquota Efetiva (pAliqEfet), resultando na rejeição do documento pela SEFAZ.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique a configuração da alíquota utilizada no item rejeitado.

**(2)** Na aba **''Tributação'**' verifique o campo **''% da Redução de Alíquota IBS Municipal''** (pRedAliq) no grupo do IBS Municipal está configurado corretamente para o CST utilizado.

**(3)** Confira se a "**Alíquota Efetiva**" (pAliqEfet) está sendo calculada corretamente, seguindo a fórmula:

- Para operações **sem** compra governamental: pAliqEfet = pIBSMun × (1 - (pRedAliq ÷ 100))
- Para operações **com** compra governamental: pAliqEfet = 0

**(4)** Caso seja necessário, ajuste o **"% da Redução de Alíquota"** para que o cálculo da Alíquota Efetiva esteja de acordo com as regras estabelecidas na LC 214/2025.

**(5)** Verifique se o CST utilizado é compatível com a redução de alíquota aplicada, pois alguns CSTs não permitem redução de alíquota (ind\_gRed = 0).

**(6)** Após realizar os ajustes necessários, tente emitir o documento fiscal novamente.

**CAUSA**

A rejeição ocorre quando o valor da Alíquota Efetiva (pAliqEfet) do IBS Municipal não está sendo calculado corretamente conforme as regras estabelecidas na validação UB47-10 da SEFAZ.

O cálculo incorreto pode ocorrer por diversos motivos:

- Percentual de Redução de Alíquota (pRedAliq) configurado incorretamente;
- Utilização de CST incompatível com redução de alíquota;
- Erro no cálculo da Alíquota Efetiva, que deve considerar a fórmula específica para operações com ou sem compra governamental;
- Inconsistência entre os valores informados no documento fiscal e os valores calculados pelo sistema.

A validação UB47-10 exige que, quando informado o grupo de Redução de Alíquota (gIBSMun/gRed), a Alíquota Efetiva (pAliqEfet) seja calculada corretamente, seguindo as regras estabelecidas na legislação da Reforma Tributária (LC 214/2025).
