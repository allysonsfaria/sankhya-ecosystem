---
id: "37098950256535"
titulo: "748 Rejeição: NF-e sem grupo da COFINS [nItem: nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098950256535-748-Rejei%C3%A7%C3%A3o-NF-e-sem-grupo-da-COFINS-nItem-nnn"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:04Z"
rotulos: ["Configuração", "NF-e", "COFINS", "SEFAZ", "Impostos", "TOP", "Passos para resolver", "Erro", "Como Resolver", "Código de Situação Tributária (CST)", "Dados de tributação da COFINS", "NF-e sem grupo da COFINS"]
---

# 748 Rejeição: NF-e sem grupo da COFINS [nItem: nnn]

**MENSAGEM**

748 Rejeição: NF-e sem grupo da COFINS [nItem: nnn]

**SITUAÇÃO**

A NF-e foi emitida sem o preenchimento das informações de tributação da COFINS em um ou mais itens do documento fiscal, resultando em inconsistência nos dados fiscais da nota.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o TOP utilizado na nota fiscal está configurado corretamente para a tributação da COFINS.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se os campos relacionados à tributação estão devidamente preenchidos.

**(3)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se os produtos da nota fiscal possuem as informações de tributação da COFINS configuradas corretamente.

**(4)** Acesse a tela **''Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS) e verifique se existe uma alíquota configurada para a COFINS com o Código de Situação Tributária (CST) adequado para a operação.

**(5)** Caso não exista, crie uma nova alíquota com as informações necessárias para a tributação da COFINS:

- Selecione o tipo de imposto **"COFINS"**;
- Informe o **"Código de situação tributária - CST"** adequado para a operação (mesmo que seja isento ou não tributado);
- Preencha a alíquota correspondente (ou zero, caso seja isento).

**(6)** Após configurar corretamente as alíquotas, vincule-as aos produtos e ao TOP utilizado na nota fiscal.

**(7)** Cancele a nota rejeitada e emita uma nova com as configurações corretas de tributação da COFINS.

**CAUSA**

A rejeição ocorre porque a SEFAZ exige que todas as NF-e contenham as informações de tributação da COFINS para cada item, mesmo que o produto seja isento ou não tributado. Quando o sistema tenta emitir uma nota fiscal sem essas informações, a validação da SEFAZ identifica a ausência do grupo da COFINS e rejeita o documento.

Esta exigência está relacionada às obrigações fiscais e à necessidade de controle tributário por parte do fisco. Mesmo que um produto não seja tributado pela COFINS, é necessário informar o CST correspondente (como 07 - Operação Isenta, por exemplo) para que a nota fiscal seja aceita pela SEFAZ.
