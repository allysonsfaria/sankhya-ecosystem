---
id: "37099228549015"
titulo: "1137 Rejeição: Valor do crédito presumido calculado sobre o saldo devedor apurado não informado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099228549015-1137-Rejei%C3%A7%C3%A3o-Valor-do-cr%C3%A9dito-presumido-calculado-sobre-o-saldo-devedor-apurado-n%C3%A3o-informado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:54Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Crédito", "Impostos", "TOP", "Passos para resolver", "Erro", "Como Resolver", "Nota Fiscal Eletrônica (NF-e)", "Tipo de Nota de Crédito", "Valor do crédito presumido", "Saldo devedor apurado"]
---

# 1137 Rejeição: Valor do crédito presumido calculado sobre o saldo devedor apurado não informado [nItem: 999]

**MENSAGEM**

1137 Rejeição: Valor do crédito presumido calculado sobre o saldo devedor apurado não informado [nItem: 999]

**SITUAÇÃO**

Esta rejeição ocorre quando o usuário tenta emitir uma Nota Fiscal Eletrônica (NF-e) com **Tipo de Nota de Crédito** configurado como "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM", mas não informa o **valor do crédito presumido** calculado sobre o saldo devedor apurado.

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na emissão da nota fiscal rejeitada.

**(2)** Selecione a aba **"NF-e/NFC-e/CF-e"** e verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

**(3)** Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal rejeitada.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas)**.**

**(4)** Na grade **''Itens''**, clique em **''Outras Opções'' (ícone com três pontos)** e selecione **''Consultar/Alterar Dados do Imposto Item''**.

**(5)** Localize as abas CBS e IBS e confira o grupo de **Crédito Presumido IBS ZFM.**

**(6)** Preencha o **valor do crédito presumido calculado sobre o saldo devedor apurado** (vCredPresIBSZFM) com o valor correspondente ao crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus.

**(7)** Salve as alterações e tente emitir a nota fiscal novamente.

**CAUSA**

A rejeição 1137 ocorre devido a uma validação da Sefaz que verifica se o **valor do crédito presumido calculado sobre o saldo devedor apurado** (campo vCredPresIBSZFM) foi informado quando o **Tipo de Nota de Crédito** (campo tpNFCredito) está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

Esta validação está relacionada às regras estabelecidas pela Lei Complementar 214/2025, que implementa a Reforma Tributária e estabelece benefícios fiscais específicos para operações na Zona Franca de Manaus. Quando uma nota fiscal é emitida com o propósito de apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM, é obrigatório informar o valor desse crédito presumido.
