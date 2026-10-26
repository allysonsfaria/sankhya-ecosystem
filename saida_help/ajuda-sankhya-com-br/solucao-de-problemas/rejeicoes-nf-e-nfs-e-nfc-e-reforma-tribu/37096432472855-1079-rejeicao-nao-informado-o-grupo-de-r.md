---
id: "37096432472855"
titulo: "1079 Rejeição: Não informado o grupo de redução de alíquota da CBS [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096432472855-1079-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:20Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Lei Complementar 214/2025", "NF-e ou NFC-e", "Alíquotas de CBS", "Redução de Alíquota", "% de Redução de Alíquota", "Inconsistência na configuração tributária", "Redução de alíquota"]
---

# 1079 Rejeição: Não informado o grupo de redução de alíquota da CBS [nItem: 999]

**MENSAGEM**

1079 Rejeição: Não informado o grupo de redução de alíquota da CBS [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e ou NFC-e quando é utilizado um CST da **CBS** que requer a informação do grupo de **redução de alíquota**, porém esse grupo não foi informado no documento fiscal, inclusive em situações em que há indicação de uso de redução de alíquota ou informação do grupo de compras governamentais.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST da CBS que está sendo utilizado na operação.

**(2)** Confirme se o CST selecionado possui indicador que exige o uso de Redução de Alíquota (ind\_gRed = 1). Se sim, será necessário informar o grupo de redução de alíquota da CBS.

**(3)** Na aba **''Tributação''** preencha os campos do grupo de redução de alíquota:

- Informe o **"% de Redução de Alíquota (pRedAliq)"** com um valor válido para o CST utilizado;
- Verifique se a **"Alíquota Efetiva (pAliqEfet)"** está sendo calculada corretamente.

**(4)** Caso esteja utilizando operação de compra governamental, certifique-se de que o grupo de redução de alíquota da CBS também esteja devidamente preenchido.

**(5)** Salve as alterações e tente emitir o documento fiscal novamente.

**CAUSA**

A rejeição ocorre devido a uma **inconsistência na configuração tributária** relacionada à CBS (Contribuição sobre Bens e Serviços). Quando um CST da CBS com indicador que exige o uso de Redução de Alíquota (ind\_gRed = 1) é utilizado, o sistema deve obrigatoriamente informar o grupo de redução de alíquota da CBS no documento fiscal.

Da mesma forma, quando é informado o grupo de compras governamentais, também é obrigatório informar o grupo de redução de alíquota da CBS. Esta validação faz parte das regras estabelecidas pela Lei Complementar 214/2025, que implementa a Reforma Tributária, exigindo que as informações sobre redução de alíquota da CBS sejam devidamente informadas quando o CST utilizado assim o exigir, garantindo a correta tributação e cálculo dos impostos.
