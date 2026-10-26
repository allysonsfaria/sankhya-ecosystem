---
id: "360043724414"
titulo: "Plano Mestre de Produção (MPS) gerando necessidade de produção duplicada do PA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043724414-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS-gerando-necessidade-de-produ%C3%A7%C3%A3o-duplicada-do-PA"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T15:59:59Z"
rotulos: ["Configuração", "TOP", "Estoque", "Produção", "Produção duplicada no MPS", "Ajuste configurações em TIPOS DE OPERAÇÃO e MRP I", "TOP reserva estoque causando duplicidade"]
---

# Plano Mestre de Produção (MPS) gerando necessidade de produção duplicada do PA

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290802413975) SITUAÇÃO:**

Plano Mestre de Produção (MPS) gerando necessidade de produção duplicada do PA.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290814425367) SOLUÇÃO:**

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/17290802431895) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

- Efetue conferência nas TOP's de 'Pedido de Venda' se estão configuradas para 'Reservar' estoque.
  Se SIM, considere se a necessidade de Produção irá suprir o estoque além do que a necessidade à produzir.

![Imagem 4: Efetue a configuração conforme a necessidade do processo, acessando: Produção » Rotinas » Planejamento de Produção (MRP…](https://ajuda.sankhya.com.br/hc/article_attachments/17290802438295) Efetue a configuração conforme a necessidade do processo, acessando: Produção » Rotinas » Planejamento de Produção (MRP I):

- Botão: **"Configuração"**
- Selecione a Configuração desejada

Aba: **"Filtros de Estoque"**
Sub-Aba: **"Produtos Acabados (PA)"**
Campo: **"Estoque Atual"**

Opção **"Não Considera":** usado quando as TOPs de Pedido de Venda precisam reservar o estoque. Desta forma, a Necessidade de Produção será gerada apenas para atender os Pedidos e não o estoque faltante.

**![Imagem 5: CAUSA: Quando a TOP para geração de Pedido está configurado para 'Reservar Estoque' e as Configurações do MPS(Produção…](https://ajuda.sankhya.com.br/hc/article_attachments/17290802441111) CAUSA:**
Quando a TOP para geração de Pedido está configurado para 'Reservar Estoque' e as Configurações do MPS(Produção » Rotinas » Planejamento de Produção (MRP I)) está considerando o estoque das Matérias Primas (MP's), gerando duplicidade de informação.

(1)** Caso de Uso:**
Quando um pedido para um determinado Produto (PA-Produto Acabado), que é de 20 unidades e ao gerar a Necessidade de compra pelo MRP I calcula-se que é preciso produzir 40 unidades, mas o correto é apenas 20.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290814469015) OBSERVAÇÃO:**

Mais detalhes sobre configuração de Plano Mestre de Produção, acesse o HELP do Sistema.
