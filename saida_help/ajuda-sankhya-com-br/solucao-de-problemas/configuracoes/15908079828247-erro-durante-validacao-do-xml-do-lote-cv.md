---
id: "15908079828247"
titulo: "Erro durante validação do XML do lote: cvc-pattern-valid: Value  -x' is not facet-valid with respect to pattern '0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\\.[0-9]{2})?' for type 'TDec_1302'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15908079828247-Erro-durante-valida%C3%A7%C3%A3o-do-XML-do-lote-cvc-pattern-valid-Value-x-is-not-facet-valid-with-respect-to-pattern-0-0-0-9-2-1-9-1-0-9-0-12-0-9-2-for-type-TDec-1302"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:55:56Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Impostos", "Validação de XML e Desconto de Produto", "Erro"]
---

# Erro durante validação do XML do lote: cvc-pattern-valid: Value  -x' is not facet-valid with respect to pattern '0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec_1302'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15908094552855)  MENSAGEM:**

Erro durante validação do XML do lote: cvc-pattern-valid: Value '-0.68' is not facet-valid with respect to pattern '0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec\_1302'.

cvc-type.3.1.3: The value '-0.68' of element 'vBC' is not valid.

cvc-pattern-valid: Value '-0.12' is not facet-valid with respect to pattern '0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec\_1302'.

cvc-type.3.1.3: The value '-0.12' of element 'vICMS' is not valid.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15908054627479) CAUSA:**

Quando há desconto no item maior do que o valor do produto

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15908071195031) SOLUÇÃO:**

Abra a nota que está apresentando o erro e verifique entre os itens quais possuem valor de desconto e se são superiores ao valor do produto.

Caso seja, esse valor de desconto precisa ser reajustado, e posteriormente gerado o lote da nota novamente.
