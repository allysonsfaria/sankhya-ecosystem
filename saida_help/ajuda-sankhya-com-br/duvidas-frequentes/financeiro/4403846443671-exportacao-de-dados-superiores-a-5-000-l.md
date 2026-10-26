---
id: "4403846443671"
titulo: "Exportação de dados superiores a 5.000 linhas na tela de Movimentação Financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403846443671-Exporta%C3%A7%C3%A3o-de-dados-superiores-a-5-000-linhas-na-tela-de-Movimenta%C3%A7%C3%A3o-Financeira"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:23:35Z"
rotulos: ["Configuração", "Relatórios", "Movimentação Financeira", "Financeiro", "não apagar", "Parâmetro ajuste: QTDMAXREGEXPORT", "Relatório personalizado: Dados grandes", "Limite exportação: 5000 registros", "Exportacao"]
---

# Exportação de dados superiores a 5.000 linhas na tela de Movimentação Financeira

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16345588117271) MENSAGEM:**

Atenção: Apenas os 5000 primeiros registros a partir da primeira página serão exportados. Deseja continuar?
Dica: Para exportar uma quantidade muito grande de registros, utilize um extratos de dados através de um relatório personalizado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345601475351) SOLUÇÃO:**

Para permitir que o sistema realize a exportação de dados superiores a 5.000 linhas na tela de **"Movimentação Financeira"**, acesse o parâmetro: **"QTDMAXREGEXPORT - Qtd. máx. de reg. para export. de PDF, XLS e Cubo",** e nele informe a quantidade máxima de linhas permitidas no momento da exportação.

Para exportar uma quantidade muito grande de registros, utilize um extrator de dados através de um relatório personalizado.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16345588131607) CAUSA:**

Existe uma trava interna e nativa para que a quantidade de resultados não exceda 5000 linhas e, assim, comprometer a performance do banco de dados em casos de má utilização.
