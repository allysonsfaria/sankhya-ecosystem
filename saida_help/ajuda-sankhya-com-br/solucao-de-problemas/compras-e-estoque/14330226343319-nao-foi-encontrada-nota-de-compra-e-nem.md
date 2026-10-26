---
id: "14330226343319"
titulo: "Não foi encontrada nota de compra e nem custo de reposição para este produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14330226343319-N%C3%A3o-foi-encontrada-nota-de-compra-e-nem-custo-de-reposi%C3%A7%C3%A3o-para-este-produto"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:58:55Z"
rotulos: ["Produtos", "Configuração", "Movimentação Financeira", "Custo", "Estoque", "COM_E00581", "Erro"]
---

# Não foi encontrada nota de compra e nem custo de reposição para este produto

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16911574850967) **MENSAGEM:**

[COM\_E00581]: Não foi encontrada nota de compra e nem custo de reposição para este produto!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16911574861335)SOLUÇÃO:**

A tela **"Negociação e Simulação de Preços"** (Caminho de acesso: Comercial » Avançado » Negociação e Simulação de Preços) irá considerar apenas o último custo de reposição para nota de compra e com base nessa valor realizará uma simulação de cálculo para definir o melhor preço de mercado a ser praticado. O sistema não considera custos em movimentos de nota do tipo transferência e também não será inserido dados em tabelas com a finalidade de atualizar o custo do produto.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16911592062743)CAUSA:**

Não temos configurações para considerar notas de transferência, o sistema olha o tipmov 'C'.
