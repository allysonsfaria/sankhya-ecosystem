---
id: "37141458979223"
titulo: "1144 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141458979223-1144-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-da-composi%C3%A7%C3%A3o-do-valor-do-IBS-e-da-CBS-em-compras-governamentais-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:15Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Financeiro", "valor do IBS e da CBS em compras governamentais", "Compra governamental", "grupo gCompraGov", "composição do valor do IBS e da CBS em compras governamentais", "Tipo de operação com o ente governamental"]
---

# 1144 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais informado indevidamente [nItem: 999]

**MENSAGEM**

1144 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais informado indevidamente [nItem: 999]

**SITUAÇÃO**

Esta rejeição ocorre quando o contribuinte informa o grupo de informações da composição do valor do IBS e da CBS em compras governamentais (grupo: gTribCompraGov) em uma nota fiscal, porém o grupo de compra governamental (grupo: gCompraGov) não foi informado na mesma nota.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se a operação realmente se trata de uma **compra governamental**. Caso não seja, remova o grupo de informações da composição do valor do IBS e da CBS em compras governamentais.

**(2)** Se a operação for uma compra governamental, acesse a tela **''Tipos de Operação - TOP''** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(3)** Na aba **''NF-e/NFC-e/CF-e''**, verifique se o campo **''Tipo de operação com o ente governamental''** está preenchido com uma das opções:

- **''1 - Fornecimento''**
- **''2 - Recebimento do pagamento, conforme fato gerador do IBS/CBS definido no Art. 10 2º''**

**(4)** Caso não esteja, marque a opção conforme a operação para que o sistema preencha corretamente o grupo gCompraGov na nota fiscal.

**(5)** Após realizar as alterações necessárias, emita novamente a nota fiscal para que o sistema preencha corretamente tanto o grupo de compra governamental (gCompraGov) quanto o grupo de informações da composição do valor do IBS e da CBS em compras governamentais (gTribCompraGov).

**CAUSA**

A rejeição ocorre devido a uma inconsistência na estrutura da nota fiscal, onde o grupo de informações da composição do valor do IBS e da CBS em compras governamentais (gTribCompraGov) foi informado, mas o grupo principal de compra governamental (gCompraGov) não foi incluído.

De acordo com a regra de validação UB82a-30, quando o grupo de compra governamental não é informado, o grupo de informações da composição do valor do IBS e da CBS em compras governamentais não deve ser preenchido.

Esta validação está alinhada com a Lei Complementar 214/2025, que estabelece regras específicas para a tributação de IBS e CBS em operações de compras governamentais, exigindo que ambos os grupos sejam informados de forma consistente para garantir a correta apuração dos tributos.
