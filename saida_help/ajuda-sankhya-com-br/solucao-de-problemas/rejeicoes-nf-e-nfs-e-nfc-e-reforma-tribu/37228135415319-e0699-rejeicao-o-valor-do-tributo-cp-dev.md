---
id: "37228135415319"
titulo: "E0699 Rejeição: O valor do tributo CP deve ser maior que zero e menor que o valor do serviço informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228135415319-E0699-Rejei%C3%A7%C3%A3o-O-valor-do-tributo-CP-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:20Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Valor da Contribuição Previdenciária (CP)", "Valor de tributo CP inválido", "O valor do tributo CP deve ser menor que o valor do serviço informado na DPS", "Valor da CP estava igual a zero ou superior ao valor total", "O valor do tributo CP deve ser maior que zero"]
---

# E0699 Rejeição: O valor do tributo CP deve ser maior que zero e menor que o valor do serviço informado na DPS.

**MENSAGEM**

E0699 Rejeição: O valor do tributo CP deve ser maior que zero e menor que o valor do serviço informado na DPS.

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e ou NFC-e) contendo serviços sujeitos à **Contribuição Previdenciária (CP)**, o usuário informou um **valor de tributo CP inválido**. O sistema rejeitou o documento porque o valor da CP estava **igual a zero ou superior ao valor total do serviço** declarado na DPS (Declaração de Prestação de Serviços), violando a regra de validação da Sefaz.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse uma das telas [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e/ou [**''Central de Compras''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) (Comercial » Rotinas » Central de Compras).

**(2)** Localize o documento fiscal rejeitado.

**(3)** Clique no botão **“Outras Opções”** e selecione **“Consultar/Alterar dados impostos do item”** para visualizar os **impostos calculados**.

**(4)** Verifique o valor da Contribuição Previdenciária (CP). Confirme que:

- O **valor da CP seja maior que zero**.
- O **valor da CP seja inferior ao valor total do serviço** informado na DPS.

**(5)** Caso o valor da CP esteja incorreto, acesse a tela **“Serviço”** (Configurações » Cadastros » Produtos » Serviço) e revise as **configurações tributárias** na aba **“Impostos”**, verificando:

- Se a **alíquota da CP** está configurada corretamente.
- Se a **base de cálculo** está adequada ao **tipo de serviço prestado**.

**(6)** Se necessário, ajuste o Tipo de Natureza de Operação (TOP), acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e confirme se as **regras tributárias da CP** estão corretamente parametrizadas para a operação.

**(7)** Após realizar os ajustes necessários**.** Recalcule os **impostos do documento fiscal** e verifique se o **valor da CP** está dentro dos **limites permitidos**.

**(8)** Transmita novamente o documento fiscal eletrônico para a Sefaz.

**CAUSA**

A rejeição ocorre quando o **valor da Contribuição Previdenciária (CP)** informado no documento fiscal está **igual a zero ou é maior ou igual ao valor total do serviço** declarado na DPS. A Sefaz exige que o valor da CP seja **maior que zero e menor que o valor do serviço**, garantindo a consistência fiscal da operação. Essa validação assegura que a tributação previdenciária esteja corretamente aplicada sobre a prestação de serviços.
