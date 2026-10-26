---
id: "360043227893"
titulo: "cvc-type.3.1.3: The value '-XX' of element 'vICMS' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227893-cvc-type-3-1-3-The-value-XX-of-element-vICMS-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:20Z"
rotulos: ["ERRONF", "#PUBLIFER", "#revisadohugo", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "Valor ICMS negativo", "Ajustar configurações ICMS", "Verificar descontos", "Erro"]
---

# cvc-type.3.1.3: The value '-XX' of element 'vICMS' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16514746063767) MENSAGEM:**

cvc-pattern-valid: Value '-XX' is not facet-valid with respect to pattern '0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?' for type 'TDec\_1302'.
cvc-type.3.1.3: The value '-XX' of element 'vICMS' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16514746067607) SOLUÇÃO:**

![Imagem 3: Mensagem ocorre quando informado um " Vlr.ICMS" negativo para determinado produto. Certifique-se que essa situação está…](https://ajuda.sankhya.com.br/hc/article_attachments/16514736213783) Mensagem ocorre quando informado um "**Vlr.ICMS"** **negativo** para determinado produto. Certifique-se que essa situação está ocorrendo, selecionando os itens da nota >> "**Outras Opções"** >> "**Consultar/alterar dados dos impostos do item"**:

![Imagem 4: Localizado o item com o valor incorreto para o imposto ICMS, verifique se as configurações realizadas para o cálculo…](https://ajuda.sankhya.com.br/hc/article_attachments/16514736218263) Localizado o item com o valor incorreto para o imposto ICMS, verifique se as configurações realizadas para o cálculo desse imposto foram realizadas corretamente.  Caso tenha dúvida sobre como realizar essa análise, recomendamos as orientações do artigo "[Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050753)".

![Imagem 5: Caso a configuração esteja incorreta, realize os devidos ajustes, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16514736219671) Caso a configuração esteja incorreta, realize os devidos ajustes, redigite o cabeçalho da nota e gere um novo lote.

![Imagem 6: Caso não localize nenhuma divergência nos cadastros, avalie com cautela as informações de 'Desconto' inseridas nos…](https://ajuda.sankhya.com.br/hc/article_attachments/16514746074775) Caso não localize nenhuma divergência nos cadastros, avalie com cautela as informações de 'Desconto' inseridas nos itens e rodapé da nota. Essa situação pode ser causada por descontos inseridos acima de 100% do total da NF-e, gerando valores negativos indevidos.

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16514746076311) OBSERVAÇÕES:**

Se nenhuma das situações acima for diagnosticada, recomendamos inutilizar a numeração dessa NF-e e realizar um novo faturamento.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16514746079511) CAUSA:**

Mensagem ocorre quando informado um 'Vlr.ICMS' negativo para determinado produto da respectiva nota fiscal eletrônica.
