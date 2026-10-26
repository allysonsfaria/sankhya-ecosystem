---
id: "30587098790167"
titulo: "Para compensação de títulos que possuem moedas todos os envolvidos deverão possuir a mesma moeda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30587098790167-Para-compensa%C3%A7%C3%A3o-de-t%C3%ADtulos-que-possuem-moedas-todos-os-envolvidos-dever%C3%A3o-possuir-a-mesma-moeda"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:35:33Z"
rotulos: ["Configuração", "Moeda", "Movimentação Financeira", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "todos os envolvidos deverão possuir a mesma moeda", "compensação de títulos que possuem moedas", "moeda do título de receita", "moeda do título de despesa", "Erro"]
---

# Para compensação de títulos que possuem moedas todos os envolvidos deverão possuir a mesma moeda

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30587098787351) **MENSAGEM:**

Para compensação de títulos que possuem moedas todos os envolvidos deverão possuir a mesma moeda

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30587078581399)SOLUÇÃO:**

Verifique a moeda do título de receita e a moeda do título de despesa. Caso sejam diferentes, a mensagem acima será exibida:

![Imagem 3: Verifique a moeda do título de receita e a moeda do título de despesa. Caso sejam diferentes, a mensagem acima será…](https://ajuda.sankhya.com.br/hc/article_attachments/30587078582167)

Não será possível compensar títulos com moedas diferentes quando essas forem do tipo **Valor**.

O sistema somente permite a compensação de moedas distintas quando o parâmetro "**Realizar compensação financeira com moedas do Tipo - COMPMOEDAINDICE"**está ativado e **uma das condições** abaixo é respeitada:

- Ambas as moedas são do tipo **Índice**; ou
- Um dos títulos está sem moeda definida e o outro com moeda do tipo **Índice**.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30587098788503)CAUSA:**

Ocorre ao tentar realizar uma Compensação Financeira entre títulos com moedas diferentes.
