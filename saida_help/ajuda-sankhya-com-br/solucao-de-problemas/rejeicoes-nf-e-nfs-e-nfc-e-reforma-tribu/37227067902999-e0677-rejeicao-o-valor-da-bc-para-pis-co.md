---
id: "37227067902999"
titulo: "E0677 Rejeição: O valor da BC para Pis/Cofins deve ser menor ou igual ao valor do serviço informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227067902999-E0677-Rejei%C3%A7%C3%A3o-O-valor-da-BC-para-Pis-Cofins-deve-ser-menor-ou-igual-ao-valor-do-servi%C3%A7o-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:33Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Alíquotas de COFINS", "Impostos", "Alíquotas de PIS", "Regra de validação", "BC para Pis/Cofins", "Valor de base de cálculo superior ao valor total do serviço", "Deduções na base de cálculo do PIS e COFINS", "Deduzir valor do ICMS/ST na BC do PIS e COFINS"]
---

# E0677 Rejeição: O valor da BC para Pis/Cofins deve ser menor ou igual ao valor do serviço informado na DPS.

**MENSAGEM**

E0677 Rejeição: O valor da BC para Pis/Cofins deve ser menor ou igual ao valor do serviço informado na DPS.

**SITUAÇÃO**

Ao emitir um documento fiscal de prestação de serviços (DPS), o usuário configurou deduções na base de cálculo do PIS e COFINS que resultaram em um **valor de base de cálculo superior ao valor total do serviço** informado no documento. Esta inconsistência ocorre quando há configurações inadequadas de dedução de impostos, fazendo com que a SEFAZ rejeite o documento por violação da regra de validação que estabelece que a base de cálculo do PIS/COFINS não pode exceder o valor do serviço prestado.

**SOLUÇÃO**

Para resolver esta rejeição, **revise as configurações de dedução** na base de cálculo do PIS e COFINS, seguindo os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

**(2)** Na aba **"Propriedades"**, verifique a configuração do campo **"Deduzir valor do ICMS/ST na BC do PIS e COFINS"**:

- Se estiver configurado como **"Deduz para NF-e"** ou **"Configurado pela TOP"**, certifique-se de que as deduções estão sendo aplicadas corretamente.
- Caso a dedução não seja aplicável ao tipo de serviço, altere para **"Não Deduz"**.

**(3)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba **"Impostos"**, e verifique as seguintes marcações:

- Desmarque a opção **"Deduzir valor do ICMS na BC do PIS e COFINS"** se ela estiver habilitada indevidamente para operações de serviço.
- Verifique se a marcação **"Deduzir valor do ISS na BC do PIS e COFINS"** está configurada adequadamente para o tipo de serviço.
- Certifique-se de que não há múltiplas deduções sendo aplicadas simultaneamente que possam inflar a base de cálculo.

**(4)** Acesse as telas **''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e verifique se há percentual de redução de base configurado que possa estar impactando incorretamente o cálculo da base de PIS/COFINS para serviços.

**(5)** Revise o documento fiscal e **recalcule os impostos**, garantindo que o valor da base de cálculo do PIS/COFINS seja igual ou inferior ao valor total do serviço informado.

**(6)** Após realizar os ajustes necessários, **retransmita o documento fiscal** para a SEFAZ.

**CAUSA**

A rejeição ocorre porque o sistema está configurado para **deduzir valores da base de cálculo do PIS e COFINS** (como ICMS, ISS ou outros impostos) de forma inadequada para operações de prestação de serviços. Quando essas deduções são aplicadas incorretamente ou em conjunto, podem fazer com que a **base de cálculo resultante seja maior que o valor do serviço**, violando a regra de validação da SEFAZ que estabelece que a base de cálculo do PIS/COFINS deve ser sempre menor ou igual ao valor do serviço informado na DPS.
