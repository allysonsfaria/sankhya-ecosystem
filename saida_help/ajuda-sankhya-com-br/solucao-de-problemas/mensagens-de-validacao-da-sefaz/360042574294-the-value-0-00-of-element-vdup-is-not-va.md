---
id: "360042574294"
titulo: "The value '0.00' of element 'vDup' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574294-The-value-0-00-of-element-vDup-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:30Z"
rotulos: ["ERRONF", "NF-e", "Movimentação Financeira", "XML", "Financeiro", "Valor '0.00' de 'vDup' Inválido", "Erro"]
---

# The value '0.00' of element 'vDup' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16474615922327) MENSAGEM:**

Erro durante validação do XML do lote: cvc-pattern-valid: Value '0.00' is not facet-valid with respect to pattern '0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec\_1302Opc'.
cvc-type.3.1.3: The value '**0.00**' of element **'vDup**' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474571714327) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a Nota Fiscal, aba: " FINANCEIRO" .](https://ajuda.sankhya.com.br/hc/article_attachments/16474571717015) Acesse a Nota Fiscal, aba: "**FINANCEIRO"**.

Verifique os valores de desdobramento de cada título se estão corretos e caso algum valor seja 0(zero), tente refazer o Financeiro- Através do botão "**Outras Opções" »** "**Refazer Financeiro".**

![Imagem 4: Se mesmo assim o título ficar com valor 0 (zero), procure analisar o Tipo de Negociação utilizado na nota para…](https://ajuda.sankhya.com.br/hc/article_attachments/16474615926935) Se mesmo assim o título ficar com valor 0 (zero), procure analisar o Tipo de Negociação utilizado na nota para verificar se existe alguma fórmula que esteja resultando essa parcela em 0(zero). Procure orientações de sua Equipe de Financeiro.

![Imagem 5: Após ajustes da nota, gere lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16474571719447) Após ajustes da nota, gere lote novamente.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474571720471) CAUSA:**

Ocorre quando alguma parcela do título financeiro da nota, está com valor 0 (zero).
