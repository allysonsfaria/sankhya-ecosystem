---
id: "360042525354"
titulo: "The value 'INFORMAÇOES DA OBSERVAÇÃO DA NOTA' of element 'infCpl' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042525354-The-value-INFORMA%C3%87OES-DA-OBSERVA%C3%87%C3%83O-DA-NOTA-of-element-infCpl-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:07Z"
rotulos: ["ERRONF", "NF-e", "Central de Vendas", "XML", "SEFAZ", "Valor Inválido em Observação", "Erro"]
---

# The value 'INFORMAÇOES DA OBSERVAÇÃO DA NOTA' of element 'infCpl' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457156490775) MENSAGEM:**

cvc-type.3.1.3: The value 'INFORMAÇOES DA OBSERVAÇÃO DA NOTA' of element 'infCpl' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457156498199) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela " Central de Vendas ": (Caminho de acesso: Comercial » Rotinas » Central de Vendas )](https://ajuda.sankhya.com.br/hc/article_attachments/16457172098327) Acesse a tela "[**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)": (Caminho de acesso: Comercial » Rotinas » Central de Vendas)

Vá até a nota que está com o erro e identifique as informações no campo "**Observação".** Caso haja espaçamento, carácter especial, a SEFAZ não irá aceitar a nota, então retire os caracteres.

![Imagem 4: Após os ajustes, gere lote novamente da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16457172102551) Após os ajustes, gere lote novamente da nota.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457156505239) CAUSA:**

Ocorre quando a observação da nota possui caractere especial ou espaçamento indevido, sendo necessário ajustar diretamente no campo Observação da Nota.

![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17856036775319) **OBSERVAÇÃO:**

Dúvidas de como identificar carácter especial, acesse o artigo:

[**"Como identificar caracteres inválidos em um XML?"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473)
