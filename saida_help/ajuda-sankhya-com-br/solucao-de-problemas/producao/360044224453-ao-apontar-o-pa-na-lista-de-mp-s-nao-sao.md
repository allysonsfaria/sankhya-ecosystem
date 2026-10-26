---
id: "360044224453"
titulo: "Ao apontar o PA na lista de MP's, não são apresentados os lotes das MP's utilizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044224453-Ao-apontar-o-PA-na-lista-de-MP-s-n%C3%A3o-s%C3%A3o-apresentados-os-lotes-das-MP-s-utilizada"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:16Z"
rotulos: ["Configuração", "Movimentação Financeira", "Estoque", "Produção", "Lotes", "Falha Explosão Lotes", "Movimentação Anterior", "Atividade Única de Apontamento"]
---

# Ao apontar o PA na lista de MP's, não são apresentados os lotes das MP's utilizada

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199087804311) SITUAÇÃO:**

Ao iniciar a atividade de Apontamento na Produção, não explode os lotes das MP's.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199075348887) SOLUÇÃO:**

Geralmente na produção pode existir apenas uma única atividade, que consiste no Apontamento do PA.

Então consideramos utilizar um processo anterior ao apontamento, que faça a movimentação de estoque, pois o processo de explosão de lotes ocorre quando é gerado uma movimentação de estoque, seja via Pedido de Venda, Requisição, Transferência, etc.

Desta forma, será apresentada a Movimentação Acessória dos MP's, ou seja a nota/pedido gerado, com os lotes dos produtos.

![Imagem 3: Exemplo da Mov. Acessória.](https://ajuda.sankhya.com.br/hc/article_attachments/16199087809431) Exemplo da Mov. Acessória.

![Imagem 4: Exemplo da Mov. Acessória.](https://ajuda.sankhya.com.br/hc/article_attachments/14499528694551)

![Imagem 5: Apontamento do PA com Explosão de Lote das MP's](https://ajuda.sankhya.com.br/hc/article_attachments/16199087815575) Apontamento do PA com Explosão de Lote das MP's

![Imagem 6: Apontamento do PA com Explosão de Lote das MP's](https://ajuda.sankhya.com.br/hc/article_attachments/14499567964695)

![Imagem 7: Caso a opção seja por trabalhar com apenas 1 (uma) atividade, ao apontar o PA, a explosão de Lote ocorrerá somente…](https://ajuda.sankhya.com.br/hc/article_attachments/16199075368727) Caso a opção seja por trabalhar com apenas 1 (uma) atividade, ao apontar o PA, a explosão de Lote ocorrerá somente depois que for gerada a nota de Produção.

**(1)** Fica a critério de cada empresa buscar a melhor prática para atender ao seu processo produtivo.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199087828247) CAUSA:**

Isto ocorre quando existe apenas 1 (uma) atividade que consiste basicamente no Apontamento e a explosão do lote ocorrerá somente na confirmação da produção, com a geração da nota de produção.
