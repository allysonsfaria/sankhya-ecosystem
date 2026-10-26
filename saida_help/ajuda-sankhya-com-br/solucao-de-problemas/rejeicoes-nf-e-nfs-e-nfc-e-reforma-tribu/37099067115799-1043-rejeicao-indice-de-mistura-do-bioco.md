---
id: "37099067115799"
titulo: "1043 Rejeição: Índice de mistura do Biocombustível inferior ao obrigatório para esta Classificação Tributária do IBS e CBS [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099067115799-1043-Rejei%C3%A7%C3%A3o-%C3%8Dndice-de-mistura-do-Biocombust%C3%ADvel-inferior-ao-obrigat%C3%B3rio-para-esta-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-CBS-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:01Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "índice de mistura do Etanol Anidro na Gasolina C", "Alíquotas de CBS", "Classificação Tributária do IBS e CBS 620004", "Percentual do Índice de Mistura", "Alíquotas de IBS"]
---

# 1043 Rejeição: Índice de mistura do Biocombustível inferior ao obrigatório para esta Classificação Tributária do IBS e CBS [nItem: 999]

**MENSAGEM**

1043 Rejeição: Índice de mistura do Biocombustível inferior ao obrigatório para esta Classificação Tributária do IBS e CBS [nItem: 999]

**SITUAÇÃO**

Ao emitir uma nota fiscal, o sistema retorna uma rejeição relacionada ao **índice de mistura do Etanol Anidro na Gasolina C** informado no documento. A rejeição está associada a itens que utilizam a **Classificação Tributária do IBS e CBS 620004**, quando o percentual informado não é aceito para esse enquadramento.

**SOLUÇÃO**

**(1)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e localize o produto de combustível que está gerando a rejeição.

**(2)** Na aba **"Combustível"**, verifique o campo **"Percentual do Índice de Mistura"** e ajuste-o para um valor superior ao mínimo obrigatório, conforme orientação da sua contabilidade e legislação vigente.

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(4)** Verifique se o campo **''Código de Classificação Tributária''** está configurado como 620004, que exige percentual de mistura superior ao obrigatório.

**(5)** Após realizar os ajustes, gere novamente o lote da nota fiscal para que a TAG correspondente ao índice de mistura seja alimentada com a informação correta.

**CAUSA**

A rejeição é apresentada quando o documento fiscal possui um produto com **Classificação Tributária do IBS e CBS (cClassTrib) igual a 620004**, que exige que o percentual do índice de mistura do Etanol Anidro na Gasolina C seja **superior ao obrigatório**, conforme estabelecido no artigo 179, inciso IIa da Lei Complementar 214/2025. Quando o percentual informado é inferior ao mínimo exigido pela legislação, a nota fiscal é rejeitada pela SEFAZ.
