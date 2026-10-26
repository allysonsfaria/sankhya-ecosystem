---
id: "360042624514"
titulo: "The value '0.00' of element 'pMVAST' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624514-The-value-0-00-of-element-pMVAST-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:42Z"
rotulos: ["ERRONF", "Configuração", "Fiscal", "NF-e", "ICMS", "Impostos", "Valor '0.00' de 'pMVAST' Inválido", "Erro"]
---

# The value '0.00' of element 'pMVAST' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16085674662039) MENSAGEM:**

Erros encontrados:cvc-pattern-valid: Value '0.00' is not facet-valid with respect to pattern '0.[0-9]{1}[1-9]{1}|0.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(.[0-9]{2})?' for type 'TDec\_0302Opc'.cvc-type.3.1.3: The value '0.00' of element 'pMVAST' is not valid.cvc-pattern-valid: Value '0.00' is not facet-valid with respect to pattern '0.[0-9]{1}[1-9]{1}|0.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(.[0-9]{2})?' for type 'TDec\_0302Opc'.cvc-type.3.1.3: The value '0.00' of element 'pMVAST' is not valid.erro.handshake=true

**![Imagem 2: SOLUÇAO: Para correção desta mensagem, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16085674667287) SOLUÇAO:**
Para correção desta mensagem, siga os passos abaixo:

![Imagem 3: Acesse a tela " Alíquotas de ICMS" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas)](https://ajuda.sankhya.com.br/hc/article_attachments/16085674673431) Acesse a tela "**Alíquotas de ICMS"**(Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas)

- Localize a Regra de ICMS que incidiu na nota.
- Acesse a aba: **"Substituição Tributária"**
- Campo **"Margem Lucro (MVA)":** Ajuste o valor nesse campo

Obs: O valor mínimo para MVA é 0,01. Verifique junto à área Fiscal e insira o valor no respectivo campo acima.

![Imagem 4: Após os ajustes, redigite a Empresa/Parceiro da nota e gere lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16085693864087) Após os ajustes, redigite a Empresa/Parceiro da nota e gere lote novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16085693867799) CAUSA:**

Esta mensagem ocorre por não ter informado um MVA (Margem Valor Agregado) válido para o cálculo do ICMS ST na nota.
