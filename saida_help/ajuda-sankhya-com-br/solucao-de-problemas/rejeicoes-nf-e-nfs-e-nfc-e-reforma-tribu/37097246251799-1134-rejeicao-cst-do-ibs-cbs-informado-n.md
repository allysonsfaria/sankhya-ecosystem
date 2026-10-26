---
id: "37097246251799"
titulo: "1134 Rejeição: CST do IBS/CBS informado não permite informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097246251799-1134-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-n%C3%A3o-permite-informa%C3%A7%C3%A3o-do-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:50Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "CST do IBS/CBS", "Saldo devedor na ZFM", "Grupo para apropriação de crédito presumido", "Crédito presumido de IBS"]
---

# 1134 Rejeição: CST do IBS/CBS informado não permite informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

**MENSAGEM**

1134 Rejeição: CST do IBS/CBS informado não permite informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma **Nota Fiscal eletrônica (NF-e)** com informações do **grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus (ZFM)**, o sistema rejeita a operação porque o Código de Situação Tributária (CST) do IBS/CBS utilizado não permite a inclusão desse grupo específico.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS'**' (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se o **CST do IBS/CBS** utilizado na operação.

**(2)** Confirme se o **Código de Situação Tributária (CST)** selecionado possui o indicador que permite o uso de crédito presumido para a ZFM (ind\_gCredPresIBSZFM = 1).

**(3)** Caso o CST atual não permita o uso do crédito presumido para a ZFM, selecione um CST compatível com essa operação.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o tipo de operação utilizado na emissão da nota fiscal.

**(5)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

**(6)** Certifique-se de que a empresa emitente está localizada no Amazonas (UF = AM) e possui inscrição de indústria incentivada, pois apenas emitentes com essas características podem utilizar o grupo de crédito presumido da ZFM.

**CAUSA**

A rejeição ocorre porque cada CST do IBS/CBS possui indicadores específicos que determinam quais grupos de informações podem ser utilizados na nota fiscal. Neste caso, o CST informado possui o indicador **ind\_gCredPresIBSZFM = 0**, o que significa que ele **não permite** a inclusão do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus.

Conforme a regra de validação UB131-20, quando um CST possui indicador que não permite o uso de crédito presumido para a ZFM (ind\_gCredPresIBSZFM = 0) e mesmo assim é informado o grupo gCredPresIBSZFM, o sistema rejeita a operação com o código 1134. Além disso, é importante ressaltar que apenas empresas localizadas no Amazonas (UF = AM) e com inscrição de indústria incentivada podem utilizar esse grupo específico, conforme estabelecido na Lei Complementar 214/2025.
