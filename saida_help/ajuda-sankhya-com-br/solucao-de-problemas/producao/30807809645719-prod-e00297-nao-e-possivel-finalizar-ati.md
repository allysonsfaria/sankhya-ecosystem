---
id: "30807809645719"
titulo: "[PROD_E00297] Não é possível finalizar atividade, pois existe operação de estoque manual pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30807809645719--PROD-E00297-N%C3%A3o-%C3%A9-poss%C3%ADvel-finalizar-atividade-pois-existe-opera%C3%A7%C3%A3o-de-estoque-manual-pendente"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:34:39Z"
rotulos: ["Configuração", "Operações de Estoque", "Estoque", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Código: PROD_E00297", "Processo Produtivo - NOVA", "Mov. Acessórias", "Não é possível finalizar atividade", "existe operação de estoque manual pendente", "+ Nova Movimentação", "Squad WMS", "Operação Manual"]
---

# [PROD_E00297] Não é possível finalizar atividade, pois existe operação de estoque manual pendente

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30807764929303) **MENSAGEM:**

[PROD\_E00297] Não é possível finalizar atividade, pois existe operação de estoque manual pendente

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30807809634583)SOLUÇÃO:**

**(1)** Acesse a tela [**''Processo Produtivo - NOVA''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova) (Produção » Cadastros » Processo Produtivo).

**(2)** No campo **''Operações de Estoque''** verifique se o campo **''Obrigatória''** encontra se marcado.

![Imagem 3: (2) No campo ''Operações de Estoque'' verifique se o campo ''Obrigatória'' encontra se marcado.](https://ajuda.sankhya.com.br/hc/article_attachments/36808640065815)

**(3)** Caso esteja marcado sera necessário realizar a operação de estoque manualmente, acesse a aba **''Mov. Acessórias''** e clique em **"+ Nova Movimentação"**.

[GIF animado: Imagem 4: (3) Caso esteja marcado sera necessário realizar a operação de estoque manualmente, acesse a aba ''Mov. Acessórias'' e…](https://ajuda.sankhya.com.br/hc/article_attachments/30807764931863)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30807809637271)CAUSA:**

A operação de estoque manual está configurada como obrigatória na atividade que se deseja finalizar.

Como essa operação não foi realizada, ao tentar concluir a atividade, o sistema exibirá a mensagem de aviso.
