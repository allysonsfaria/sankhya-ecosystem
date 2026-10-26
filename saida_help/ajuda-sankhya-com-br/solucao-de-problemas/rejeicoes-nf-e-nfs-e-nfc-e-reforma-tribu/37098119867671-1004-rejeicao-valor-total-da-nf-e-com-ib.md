---
id: "37098119867671"
titulo: "1004 Rejeição: Valor total da NF-e com IBS / CBS / IS (vNFTot) não informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098119867671-1004-Rejei%C3%A7%C3%A3o-Valor-total-da-NF-e-com-IBS-CBS-IS-vNFTot-n%C3%A3o-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:20Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "CST (Código de Situação Tributária)", "Artigo atualizado KCS", "NF-e ou NFC-e", "Alíquotas de CBS", "Alíquotas de IBS", "Assistente de Configuração Integral da Reforma Tributária", "IBS CBS ou IS", "Valor total da nota fiscal (vNFTot)", "Ausencia do valor total da NF-e", "Tributos da Reforma Tributária (IBS CBS ou IS)", "Docs Eletrônicos - KCS"]
---

# 1004 Rejeição: Valor total da NF-e com IBS / CBS / IS (vNFTot) não informado

**MENSAGEM**

1004 Rejeição: Valor total da NF-e com IBS / CBS / IS (vNFTot) não informado

**SITUAÇÃO**

Ao emitir uma **NF-e ou NFC-e** com informações de **IBS, CBS ou IS**, o sistema retorna rejeição durante a transmissão do documento fiscal eletrônico, relacionada ao **valor total da nota fiscal (vNFTot)** informado no XML.

**SOLUÇÃO**

**(1)** Verifique se a TOP utilizada na nota fiscal está configurado corretamente para a Reforma Tributária.

**(2)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e selecione o TOP utilizado na nota fiscal rejeitada.

**(3)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado com a finalidade correta para a operação que está sendo realizada.

**(4)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

Certifique-se de que os produtos da nota fiscal possuem as seguintes alíquotas:

- **Alíquotas de IBS**
- **Alíquotas de CBS**

**(5)** Verifique se o **''Código de Situação Tributária''** (**CST)** do IBS/CBS está configurado corretamente para cada item da nota fiscal.

**(6)** Após realizar as configurações necessárias, tente emitir a nota fiscal novamente para que o sistema calcule e informe corretamente o valor total da NF-e com IBS/CBS/IS (vNFTot).

**CAUSA**

Esta rejeição ocorre devido à **ausência do valor total da NF-e** considerando os novos tributos da Reforma Tributária (IBS, CBS ou IS) no campo específico (vNFTot). Com a implementação da Reforma Tributária através da Lei Complementar nº 214 de 16 de janeiro de 2025, tornou-se **obrigatório informar o valor total da nota fiscal** incluindo estes novos impostos quando aplicáveis.

O sistema precisa calcular e informar este valor total no XML da nota fiscal para que a SEFAZ possa validar corretamente os valores dos novos tributos. Quando este campo não é informado, a nota é rejeitada com o código 1004.
