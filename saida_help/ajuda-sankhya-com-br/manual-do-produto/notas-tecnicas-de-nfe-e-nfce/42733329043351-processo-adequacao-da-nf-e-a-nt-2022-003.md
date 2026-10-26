---
id: "42733329043351"
titulo: "Processo Adequação da NF-e à NT 2022.003 v.1.00"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42733329043351-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2022-003-v-1-00"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2022.003 v.1.00

Caminhos de Acesso: Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e

---

## O que é e para que serve

A Nota Técnica (NT) 2022.003 v.1.0 divulga novos campos e Regras de Validação da NF-e versão 4.0. Nela, foi incluído um campo específico no grupo de Documento Fiscal Referenciado (NFref) para permitir ao contribuinte referenciar uma Nota Fiscal Eletrônica de modelo 55, informando a Chave da NF-e com o código numérico zerado. Essa alteração visa garantir a manutenção do Sigilo Fiscal da NF-e referenciada.

## O que foi alterado e Configurações necessárias

Para gerar as notas fiscais eletrônicas de acordo com as regras da NT 2022.003 v.1.0, é necessário realizar as seguintes configurações:

- Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e), aba Nota Técnica NF-e, ative a "Nota Técnica 2022.003 - v.1.00".
- Na aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e), acione a marcação "Gerar chave referenciada sigilosa?".

Feito isso, ao emitir uma nota fiscal configurada com o [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) diferente de Complementar e o CFOP diferente de Devolução, a nota fiscal será gerada com a tag <refNFeSig>.
