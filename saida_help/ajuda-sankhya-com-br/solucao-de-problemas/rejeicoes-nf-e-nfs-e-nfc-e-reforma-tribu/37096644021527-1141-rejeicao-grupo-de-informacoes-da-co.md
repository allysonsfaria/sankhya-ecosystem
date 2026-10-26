---
id: "37096644021527"
titulo: "1141 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais não informado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096644021527-1141-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-da-composi%C3%A7%C3%A3o-do-valor-do-IBS-e-da-CBS-em-compras-governamentais-n%C3%A3o-informado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:14Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "IBS", "CBS", "Tipo de operação com o ente governamental", "Grupo de informações da composição do valor do IBS e da CBS", "valor do IBS e da CBS em compras governamentais não informado", "composição do valor do IBS e da CBS", "Inconsistência na configuração fiscal", "Compras Governamentais"]
---

# 1141 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais não informado [nItem: 999]

**MENSAGEM**

1141 Rejeição: Grupo de informações da composição do valor do IBS e da CBS em compras governamentais não informado [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e (modelo 55) quando é informado o grupo de **compras governamentais**, sem que o grupo de **composição do valor do IBS e da CBS** específico para esse tipo de operação esteja preenchido no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação utilizada está configurada corretamente para compras governamentais.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Tipo de operação com o ente governamental"** está marcado como:

- **''1 – Fornecimento''** ou,
- **''2 – Recebimento do pagamento''.**

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(4)** Verifique se o **CST** selecionado é compatível com operações de compras governamentais.

**(5)** Na seção de **"Composição do Valor do IBS e CBS em Compras Governamentais"**, preencha os campos obrigatórios:

- Valor do IBS UF
- Valor do IBS Municipal Valor da CBS.

**(6)** Certifique-se de que a soma dos valores informados na composição (vTribIBSUF + vTribIBSMun + vTribCBS) seja igual ao resultado da soma dos valores de IBS UF, IBS Municipal e CBS calculados para o item.

**CAUSA**

A rejeição 1141 ocorre devido à **inconsistência na configuração fiscal** para operações de compras governamentais. Conforme a regra de validação UB82a-10, quando o grupo de Compra Governamental (grupo: gCompraGov) é informado na NF-e, é **obrigatório** informar também o grupo de informações da composição do valor do IBS e da CBS específico para compras governamentais (grupo: gTribCompraGov).

Esta obrigatoriedade está relacionada às exigências da Lei Complementar 214/2025, que estabelece regras específicas para a tributação de operações com órgãos públicos no contexto da Reforma Tributária, determinando que a composição dos valores de IBS e CBS deve ser detalhada de forma específica nestas operações.
