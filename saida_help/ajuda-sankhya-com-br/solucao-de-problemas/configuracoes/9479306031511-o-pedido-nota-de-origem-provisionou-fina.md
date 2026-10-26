---
id: "9479306031511"
titulo: "O Pedido/Nota de origem provisionou financeiro, a TOP de destino não pode provisionar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9479306031511-O-Pedido-Nota-de-origem-provisionou-financeiro-a-TOP-de-destino-n%C3%A3o-pode-provisionar"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:41Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "CORE_E04609", "Erro de Provisionamento Financeiro na TOP", "Erro"]
---

# O Pedido/Nota de origem provisionou financeiro, a TOP de destino não pode provisionar

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18613926784279) MENSAGEM:**

[CORE\_E04609] O Pedido/Nota de origem provisionou financeiro, a TOP de destino não pode provisionar.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613926790295) SITUAÇÃO:**

Ao faturar um pedido com provisionamento para uma Top que não atualiza financeiro a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18613926794263) CAUSA:**

Ocorre quando a TOP de origem e destino possuem a mesma configuração de atualização de financeiro.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613926795159) SOLUÇÃO:**

Verifique no cadastro do **Tipo de Operação TOP** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) de destino o campo "Atualiza Financeira na TOP de origem" se está selecionado.

![Imagem 5: Verifique no cadastro do Tipo de Operação TOP (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) de destino…](https://ajuda.sankhya.com.br/hc/article_attachments/18613926804631)

Se a marcação **"Atualiza Financeiro na TOP de Origem"** for efetuada, possibilitará que, em um lançamento na Central, a TOP de Destino atualize o financeiro, mesmo que a TOP de Origem já o tenha atualizado.
