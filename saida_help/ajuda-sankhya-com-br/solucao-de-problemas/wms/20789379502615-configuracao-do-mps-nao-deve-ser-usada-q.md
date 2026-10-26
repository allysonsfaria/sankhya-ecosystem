---
id: "20789379502615"
titulo: "Configuração do MPS não deve ser usada quando o PI estiver configurado para PA herdando o lote do PI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20789379502615-Configura%C3%A7%C3%A3o-do-MPS-n%C3%A3o-deve-ser-usada-quando-o-PI-estiver-configurado-para-PA-herdando-o-lote-do-PI"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-24T12:41:45Z"
rotulos: ["Produtos", "Configuração", "Produção", "Parâmetro", "Erro"]
---

# Configuração do MPS não deve ser usada quando o PI estiver configurado para PA herdando o lote do PI

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20789379499671)SOLUÇÃO:**

Quando temos a "Tamanho de Lote da OP igual ao Lote Padrão" localizada na tela Planejamento de Produção MRP I em Configuração MPS, combinada com a parametrização feita na tela Composição do Produto aba matérias primas, opção configuração do PI "PA herdando o lote do PI", teremos essa mensagem de erro.

Isso porque o tamanho do lote no lançamento da Ordem de Produção gera mais de uma dependência ao PA.
 Quando o PA verifica o PI para buscar o lote,  ele encontra dois registros de PI, gerando o erro que surge na tela.

Reforço que, desta forma, a configuração "Tamanho de Lote da OP igual ao Lote Padrão" feita na  Configuração do MPS,  não deve ser combinada com o "PA herdando o lote do PI"  feita na composição do produto (configuração do PI), pois teremos a possibilidade da criação de mais de uma OP com o mesmo PI, gerando o erro na busca do Lote pelo PA.

![Imagem 2: Reforço que, desta forma, a configuração "Tamanho de Lote da OP igual ao Lote Padrão" feita na Configuração do MPS, não…](https://ajuda.sankhya.com.br/hc/article_attachments/20880743960599)
