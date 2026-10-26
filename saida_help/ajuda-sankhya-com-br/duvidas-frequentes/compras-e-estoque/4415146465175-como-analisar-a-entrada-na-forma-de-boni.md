---
id: "4415146465175"
titulo: "Como analisar a entrada na forma de bonificação no KARDEX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4415146465175-Como-analisar-a-entrada-na-forma-de-bonifica%C3%A7%C3%A3o-no-KARDEX"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:20:20Z"
rotulos: ["Produtos", "Custos", "Configuração", "Fórmulas", "Movimentação Financeira", "Estoque", "#validadoSilvio", "#kardex", "Bonificação de mercadoria", "Redução de custos", "Fórmula de Custo/Preço"]
---

# Como analisar a entrada na forma de bonificação no KARDEX

A Entrada de uma mercadoria/produto na forma "**Bonificada"** tem como principal efeito a redução dos custos da mercadoria (médio). Visto que está operação não atualiza o movimento financeiro, ou seja, não há desembolso monetário.

Para que esta situação seja efetiva, esta 'consideração' deve ser descrita na expressão da **Fórmula de Custo/Preço**, vinculada ao **Produto**. Exemplo simples da condição na formula:

| if(queTOP.BONIFICACAO='S',val(0), (queItens.VLRICMS / queItens.QTDNEG)) |
| --- |

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16250696804119) OBSERVAÇÃO:**

A fórmula de precificação interna (**sem fórmula)** não contempla a marcação **Bonificação** de forma nativa.
