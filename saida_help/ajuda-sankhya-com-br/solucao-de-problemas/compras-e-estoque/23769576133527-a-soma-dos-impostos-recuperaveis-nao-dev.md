---
id: "23769576133527"
titulo: "A soma dos impostos recuperáveis, não deve ser maior ou igual ao 'Valor total dos bens'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23769576133527-A-soma-dos-impostos-recuper%C3%A1veis-n%C3%A3o-deve-ser-maior-ou-igual-ao-Valor-total-dos-bens"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:48:04Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Impostos", "CORE_E06906", "A soma dos impostos recuperáveis não deve ser maior ou igual ao 'Valor total dos bens'.", "Erro"]
---

# A soma dos impostos recuperáveis, não deve ser maior ou igual ao 'Valor total dos bens'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/23769548244119) MENSAGEM:**

[CORE\_E06906] A soma dos impostos recuperáveis, não deve ser maior ou igual ao 'Valor total dos bens'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23769576131223) SOLUÇÃO:**

Quando estamos lançando uma nota de compra de imobilizado, ou alterando alguma informação de um bem já lançado, o sistema analisa se o valor que o bem está calculando de CIAP (que pode ter somado ao seu valor, o FCP se nas preferências da empresa na aba BENS, o campo "Somar FCP na Base de Crédito do CIAP?" estiver marcado) está maior que o próprio valor do bem, que nesse momento estaria calculado com a seguinte fórmula:

(Quantidade negociada \* valor unitário) + (substituição tributária (ST) + Valor de IPI) - (Descontos do item)

Nesse sentido, analise o motivo do valor do CIAP (e FCP se for o caso) estar maior que o valor do imobilizado, pois não é algo correto em um processo comum de lançamento.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/23769548245015) CAUSA:**

Ao tentar incluir os bens no lançamento de uma nota de compra a mensagem é apresentada.
