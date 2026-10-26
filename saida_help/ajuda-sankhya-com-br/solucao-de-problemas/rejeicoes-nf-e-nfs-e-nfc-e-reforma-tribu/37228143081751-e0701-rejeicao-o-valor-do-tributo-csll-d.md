---
id: "37228143081751"
titulo: "E0701 Rejeição: O valor do tributo CSLL deve ser maior que zero e menor que o valor do serviço informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228143081751-E0701-Rejei%C3%A7%C3%A3o-O-valor-do-tributo-CSLL-deve-ser-maior-que-zero-e-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:18Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "NFS-e", "Erro", "DPS (Declaração de Prestação de Serviços)", "valor do tributo CSLL", "Igual a zero ou superior ao valor total do serviço", "Contribuição Social sobre o Lucro Líquido"]
---

# E0701 Rejeição: O valor do tributo CSLL deve ser maior que zero e menor que o valor do serviço informado na DPS.

**MENSAGEM**

E0701 Rejeição: O valor do tributo CSLL deve ser maior que zero e menor que o valor do serviço informado na DPS.

**SITUAÇÃO**

Ao emitir um documento fiscal de prestação de serviços (DPS), o usuário informou um **valor de CSLL** (Contribuição Social sobre o Lucro Líquido) que está **igual a zero ou superior ao valor total do serviço** declarado no documento. Com isso, a Sefaz rejeitou o documento, pois o valor do tributo CSLL deve obrigatoriamente ser **maior que zero e menor que o valor do serviço** informado na DPS.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento fiscal que foi rejeitado.

**(2)** Verifique na aba **"Impostos"** ou **"Outros Impostos"** o **valor da CSLL** que foi calculado e informado no documento.

**(3)** Certifique-se de que o **valor da CSLL é maior que zero** e **menor que o valor total do serviço** informado no documento fiscal. Caso o valor esteja incorreto, realize os ajustes necessários:

- Se o valor da CSLL estiver **zerado**, verifique a configuração da **alíquota de CSLL** aplicada ao serviço nas telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) ou nas configurações fiscais da empresa.
- Se o valor da CSLL estiver **igual ou superior ao valor do serviço**, revise o cálculo e a base de cálculo do tributo, ajustando a alíquota ou o valor manualmente, se necessário.

**(4)** Após realizar os ajustes, **recalcule os impostos** do documento fiscal clicando no botão **"Recalcular Impostos"** ou similar, disponível na tela de edição da nota.

**(5)** Salve as alterações e **transmita novamente o documento fiscal** para a Sefaz.

**CAUSA**

A rejeição ocorre quando o **valor do tributo CSLL** informado no documento fiscal de prestação de serviços está **igual a zero ou é maior ou igual ao valor total do serviço** declarado. A Sefaz exige que o valor da CSLL seja **maior que zero e menor que o valor do serviço**, garantindo a consistência e a validade das informações tributárias transmitidas.
