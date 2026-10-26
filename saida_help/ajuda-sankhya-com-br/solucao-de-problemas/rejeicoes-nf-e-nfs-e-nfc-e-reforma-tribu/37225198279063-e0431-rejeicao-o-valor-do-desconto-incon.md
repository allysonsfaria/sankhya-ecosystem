---
id: "37225198279063"
titulo: "E0431 Rejeição: O valor do desconto incondicionado informado na DPS deve ser menor que o valor do serviço e maior que zero."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225198279063-E0431-Rejei%C3%A7%C3%A3o-O-valor-do-desconto-incondicionado-informado-na-DPS-deve-ser-menor-que-o-valor-do-servi%C3%A7o-e-maior-que-zero"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:09Z"
rotulos: ["Configuração", "SEFAZ", "NFS-e", "Erro", "DPS (Declaração de Prestação de Serviços)", "Valor do desconto incondicionado", "DPS deve ser menor que o valor do serviço e maior que zero", "Valor do serviço e maior que zero", "Valor de desconto incondicionado inconsistente"]
---

# E0431 Rejeição: O valor do desconto incondicionado informado na DPS deve ser menor que o valor do serviço e maior que zero.

**MENSAGEM**

E0431 Rejeição: O valor do desconto incondicionado informado na DPS deve ser menor que o valor do serviço e maior que zero.

**SITUAÇÃO**

O Documento de Prestação de Serviços (DPS) foi transmitido com a informação de um valor de desconto incondicionado inconsistente em relação ao valor total do serviço informado no documento.

**SOLUÇÃO**

Para resolver esta rejeição, ajuste o **valor do desconto incondicionado** no documento fiscal, seguindo os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que foi rejeitado.

**(2)** Na grade **''Itens''**, localize o campo **''Vlr. desconto''** do documento.

**(3)** Verifique o **valor total do serviço** informado no documento.

**(4)** Ajuste o valor do desconto incondicionado considerando as seguintes regras:

- O valor do desconto deve ser **maior que zero**;
- O valor do desconto deve ser **menor que o valor total do serviço**.

**(5)** Salve as alterações.

**(6)** Transmita novamente o **Documento de Prestação de Serviços (DPS)** para a Sefaz.

**CAUSA**

A rejeição ocorre quando o **valor do desconto incondicionado** informado no Documento de Prestação de Serviços não atende às regras de validação da Sefaz. Especificamente, o sistema rejeita o documento quando:

- O valor do desconto é **igual ou menor que zero**;
- O valor do desconto é **igual ou maior que o valor total do serviço**, o que resultaria em um valor líquido negativo ou zero para o serviço prestado.

Essa validação garante a **consistência fiscal** do documento e impede que sejam transmitidos valores incompatíveis com a prestação de serviços.
