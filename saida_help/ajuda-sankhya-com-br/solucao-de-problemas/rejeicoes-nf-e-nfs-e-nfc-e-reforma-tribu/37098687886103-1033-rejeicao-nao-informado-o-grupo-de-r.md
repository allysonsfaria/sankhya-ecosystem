---
id: "37098687886103"
titulo: "1033 Rejeição: Não informado o grupo de redução de alíquota Estadual [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098687886103-1033-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-08T18:43:12Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Rejeição", "Artigo atualizado KCS", "Nota Fiscal Eletrônica (NF-e)", "IBS (Imposto sobre Bens e Serviços)", "Alíquotas de IBS", "Cód. de Benefício Fiscal na UF", "Redução de alíquota estadual do IBS", "Alíquota Estadual", "Alíquota IBS", "Alíquota CBS", "Docs Eletrônicos - KCS"]
---

# 1033 Rejeição: Não informado o grupo de redução de alíquota Estadual [nItem: 999]

1033 Rejeição: Não informado o grupo de redução de alíquota estadual [nItem: 999]

### SITUAÇÃO

A rejeição ocorre na emissão de **NF-e** quando o **CST do IBS/CBS** exige redução de alíquota (`ind_gRed = 1`), mas o grupo de **redução de alíquota estadual** não foi informado ou não está corretamente configurado.

Também pode ocorrer quando o grupo de **Compras Governamentais** foi informado, mas não existe uma configuração correspondente de redução de alíquota estadual.

Para corrigir, verifique o **CST do IBS/CBS** e as configurações de **redução de alíquota estadual** e, quando aplicável, de **Compras Governamentais**.

A validação segue as regras da **Lei Complementar nº 214/2025** e da **Nota Técnica 2025.002-RTC**.

### SOLUÇÃO

**(1)** Acesse as telas **"Alíquotas de IBS"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS) e **"Alíquotas de CBS"** (Livros Fiscais >> Cadastros >> Alíquotas de CBS).

**(2)**  Verifique se o **CST** configurado está correto e se é compatível com a operação que envolve redução de alíquota estadual.

**(3)** Certifique-se de que os campos estejam preenchidos com o percentual correto de redução:

- CBS: **"% da Redução de Alíquota CBS"**
- IBS: **"% da Redução de Alíquota IBS Estadual"**

**(4)** Verifique se a vigência da alíquota está correta (a vigência do IBS/CBS iniciou em 01/01/2026).

**(5)** Acesse a tela **"Produtos"** (Configurações >> Cadastros >> Produtos >> Produtos). Na aba **Imposto**, verifique se o campo **"Cód. de Benefício Fiscal na UF"** está preenchido com o código correto conforme legislação da UF.

**(6)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) e, na aba **"Impostos"**, verifique se a configuração está correta para a operação que envolve redução de alíquota estadual.

**(7)** Após realizar as correções, retorne à Central de Vendas, localize a nota fiscal rejeitada, selecione-a e clique em **"Gerar Lote"** (ou duplique a nota) para reprocessar o documento.

### CAUSA

Esta rejeição ocorre devido à implementação da Reforma Tributária (Lei Complementar 214 de 16 de janeiro de 2025), que estabelece a obrigatoriedade de informar o grupo de redução de alíquota estadual do IBS quando aplicável.

Conforme as regras de validação da SEFAZ, quando um produto possui redução de alíquota estadual do IBS, é necessário informar corretamente o grupo de redução no documento fiscal, incluindo o percentual de redução e o código de benefício fiscal correspondente. A ausência dessas informações resulta na rejeição da nota fiscal.
