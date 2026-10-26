---
id: "35318966201111"
titulo: "Realizado lançamento de venda com mais de um vendedor na aba"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35318966201111-Realizado-lan%C3%A7amento-de-venda-com-mais-de-um-vendedor-na-aba"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:25:21Z"
rotulos: ["Configuração", "Parceiro", "Atualização do Realizado", "Impostos", "Venda Mais", "Realizado lançamento de venda", "com mais de um vendedor na aba", "tabela TGFCAB"]
---

# Realizado lançamento de venda com mais de um vendedor na aba

**SITUAÇÃO:**

Configurada a meta simplificada para os vendedores. Foram realizadas vendas cujo resultado deve ser considerado para mais de um vendedor, por exemplo:

![Imagem 1: Configurada a meta simplificada para os vendedores. Foram realizadas vendas cujo resultado deve ser considerado para…](https://ajuda.sankhya.com.br/hc/article_attachments/35318987733399)

**(1)** Ao atualizar o realizado, pela tela '**'Atualização do Realizado''** (Comercial» Avançado) o sistema não registra a venda para os vendedores informado no lançamento.

![Imagem 2: (1) Ao atualizar o realizado, pela tela ' 'Atualização do Realizado'' (Comercial» Avançado) o sistema não registra a…](https://ajuda.sankhya.com.br/hc/article_attachments/35318966199959)

**CAUSA:**

Metas simplificadas na atualização do realizado busca o vendedor do cabeçalho da nota (tabela TGFCAB), as informações da aba ''Comissão'' (utilizada para o cálculo de 'Comissão Múltipla', tabela TGFCCM) não são consideradas, ou seja, somente irá gerar realizado para o vendedor do cabeçalho da nota.
