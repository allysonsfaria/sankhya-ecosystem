---
id: "37230639950359"
titulo: "E0680 Rejeição: O valor BC do Pis/Cofins informado deve ser maior que zero e menor que o valor do serviço informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37230639950359-E0680-Rejei%C3%A7%C3%A3o-O-valor-BC-do-Pis-Cofins-informado-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:40Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Maior que zero e menor que o valor do serviço informado na DPS", "documento fiscal de serviço (DPS)", "Base de Cálculo do PIS/COFINS", "BC do PIS/COFINS", "Código de situação tributária - CST", "tributação de PIS/COFINS", "Valor do serviço"]
---

# E0680 Rejeição: O valor BC do Pis/Cofins informado deve ser maior que zero e menor que o valor do serviço informado na DPS.

**MENSAGEM:**

E0680 Rejeição: O valor BC do Pis/Cofins informado deve ser maior que zero e menor que o valor do serviço informado na DPS.

**SITUAÇÃO:**

Ao emitir um **documento fiscal de serviço (DPS)**, o sistema calculou a **Base de Cálculo do PIS/COFINS** com valor zerado ou com valor igual ou superior ao valor total do serviço prestado, violando a regra de validação da SEFAZ que exige que este valor seja **maior que zero e menor que o valor do serviço** informado no documento.

**SOLUÇÃO:**

**(1)** Acesse as telas **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize a alíquota utilizada no documento fiscal rejeitado.

**(3)** Na aba **''Tributação''**, verifique se o campo **"Código de situação tributária - CST"** está configurado corretamente para permitir a **tributação de PIS/COFINS**.

**(4)** Certifique-se de que o **percentual de redução de base de cálculo** não está configurado com valor que resulte em base de cálculo zerada ou igual ao valor do serviço.

**(5)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize o TOP utilizado na operação.

**(6)** Na aba **"Impostos"**, verifique as configurações relacionadas à dedução de valores na base de cálculo do PIS/COFINS:

- Verifique se a opção **"Deduzir valor do ICMS na BC do PIS e COFINS?"** está configurada adequadamente.
- Verifique se a opção **"Deduzir valor do ICMS/ST na BC do PIS e COFINS?"** está configurada adequadamente.
- Certifique-se de que as deduções não estão **zerando ou igualando** a base de cálculo ao valor do serviço.

**(7)** Revise o **valor do serviço** informado no documento fiscal e certifique-se de que está correto e **maior que zero**.

**(8)** Após realizar os ajustes necessários, **reemita o documento fiscal** para que o cálculo da Base de Cálculo do PIS/COFINS seja processado corretamente.

**CAUSA**

A rejeição ocorre quando a **Base de Cálculo do PIS/COFINS** informada no documento fiscal de serviço está com **valor zerado**, **negativo** ou **igual ou superior ao valor total do serviço**. Isso pode acontecer devido a:

- **Configuração incorreta** do CST na alíquota, impedindo a tributação adequada.
- **Percentual de redução de base** configurado de forma inadequada, resultando em base de cálculo inválida.
- **Deduções excessivas** configuradas no TOP (ICMS, ICMS/ST, ISS) que eliminam ou excedem o valor da base de cálculo.
- **Valor do serviço** informado incorretamente no documento fiscal.
- **Erro no cálculo proporcional** de despesas acessórias que impactam a base de cálculo do PIS/COFINS.
