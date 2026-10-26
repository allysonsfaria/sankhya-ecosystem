---
id: "37099211102487"
titulo: "1136 Rejeição: Não é possível repetir o Tipo de Classificação para o cálculo do crédito presumido na ZFM neste DFe"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099211102487-1136-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-repetir-o-Tipo-de-Classifica%C3%A7%C3%A3o-para-o-c%C3%A1lculo-do-cr%C3%A9dito-presumido-na-ZFM-neste-DFe"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:55Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Crédito", "Impostos", "TOP", "Passos para resolver", "Erro", "Como Resolver", "Tipo de Nota de Crédito", "Tipo de Classificação para o cálculo do crédito presumido", "Cálculo do crédito presumido", "Cálculo do crédito presumido na ZFM", "ZFM"]
---

# 1136 Rejeição: Não é possível repetir o Tipo de Classificação para o cálculo do crédito presumido na ZFM neste DFe

**MENSAGEM**

1136 Rejeição: Não é possível repetir o Tipo de Classificação para o cálculo do crédito presumido na ZFM neste DFe

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) com apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus (ZFM), o documento foi rejeitado porque foram informados dois ou mais itens com o mesmo **Tipo de Classificação para o cálculo do crédito presumido na ZFM** (mesmo valor na tag tpCredPresIBSZFM).

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Na aba **''NF-e/NFC-e/CF-e''**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

**(3)** Acesse a nota fiscal que está sendo rejeitada e verifique os itens que possuem o grupo de crédito presumido da ZFM.

**(4)** Para cada item da nota, certifique-se de que o **tipo de classificação para o cálculo do crédito presumido na ZFM** seja único, não podendo haver repetição do mesmo tipo em diferentes itens da nota.

**(5)** Altere os tipos de classificação repetidos, atribuindo um tipo diferente para cada item, conforme a natureza da operação e as regras específicas da Zona Franca de Manaus.

**CAUSA**

Esta rejeição ocorre porque, de acordo com as regras de validação da Sefaz, quando o **Tipo de Nota de Crédito** é igual a **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**, não é permitido que haja dois ou mais itens com o mesmo **Tipo de Classificação para o cálculo do crédito presumido na ZFM** (mesmo valor na tag tpCredPresIBSZFM).

A validação UB110-10 especifica que, para notas fiscais com finalidade de apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM, cada tipo de classificação deve ser único dentro do documento fiscal, garantindo assim a correta aplicação dos benefícios fiscais previstos para a Zona Franca de Manaus, conforme estabelecido na Lei Complementar 214/2025.
