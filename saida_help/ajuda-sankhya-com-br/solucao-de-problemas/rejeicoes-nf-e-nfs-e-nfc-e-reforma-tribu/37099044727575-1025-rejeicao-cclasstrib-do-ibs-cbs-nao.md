---
id: "37099044727575"
titulo: "1025 Rejeição: cClassTrib do IBS/CBS não permitido neste modelo de DFe [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099044727575-1025-Rejei%C3%A7%C3%A3o-cClassTrib-do-IBS-CBS-n%C3%A3o-permitido-neste-modelo-de-DFe-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-03T12:54:37Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "NFC-e", "Alíquota de IBS", "NFC-e (modelo 65)", "NF-e (modelo 55)", "Alíquota de CBS", "Classificação Tributária do IBS/CBS", "NF-e ou NFC-e com a Classificação Tributária do IBS/CBS"]
---

# 1025 Rejeição: cClassTrib do IBS/CBS não permitido neste modelo de DFe [nItem: 999]

**MENSAGEM**

1025 Rejeição: cClassTrib do IBS/CBS não permitido neste modelo de DFe [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e com a Classificação Tributária do IBS/CBS (cClassTrib) que não é permitida para o modelo de documento fiscal eletrônico utilizado, a SEFAZ rejeita o documento e apresenta esta mensagem de erro.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Verifique a classificação tributária configurada para o produto que esteja gerando a rejeição.

**(3)** Verifique se a **Classificação Tributária** selecionada possui o indicador correto para o modelo de documento que está tentando emitir:

- **Para NF-e (modelo 55)**: a Classificação Tributária deve ter o indicador **"indNFe = 1"**
- **Para NFC-e (modelo 65)**: a Classificação Tributária deve ter o indicador **"indNFCe = 1"**

**(4)** Caso a Classificação Tributária esteja incorreta, selecione uma classificação compatível com o modelo de documento fiscal que está emitindo.

**(5)** Alternativamente, acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está com a **Classificação Tributária do IBS/CBS** correta para o modelo de documento que está sendo emitido.

**(6)** Após realizar as correções, tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre porque a **Classificação Tributária do IBS/CBS** (cClassTrib) informada no documento fiscal possui um indicador que **não permite sua utilização** no modelo de documento que está sendo emitido.

Conforme a regra de validação UB14-25, cada Classificação Tributária possui indicadores específicos que determinam em quais modelos de documentos fiscais ela pode ser utilizada:

- Para NF-e (modelo 55): o indicador **indNFe** deve ser igual a 1
- Para NFC-e (modelo 65): o indicador **indNFCe** deve ser igual a 1

Se o indicador correspondente ao modelo do documento for igual a 0, a Classificação Tributária não pode ser utilizada naquele modelo específico, resultando nesta rejeição.
