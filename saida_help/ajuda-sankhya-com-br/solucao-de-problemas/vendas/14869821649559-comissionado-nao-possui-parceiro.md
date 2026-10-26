---
id: "14869821649559"
titulo: "Comissionado não possui parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14869821649559-Comissionado-n%C3%A3o-possui-parceiro"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:57:46Z"
rotulos: ["Configuração", "Parceiro", "Financeiro", "Vendedores", "Vincule parceiro ao vendedor", "Comissionado sem parceiro", "Vendedor sem cliente vinculado", "Erro"]
---

# Comissionado não possui parceiro

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16620791967895) MENSAGEM:**

Fechamento de comissão: Comissionado não possui parceiro!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16620765885463) SOLUÇÃO:**

Acesse o cadastro do vendedor, na tela: Configurações » Cadastros » Vendedores/Compradores, campo **"Parceiro"** e vincule o código do parceiro ao cadastro do vendedor ou preencha com 0 (zero).

![Imagem 3: Acesse o cadastro do vendedor, na tela: Configurações » Cadastros » Vendedores/Compradores , campo "Parceiro" e vincule…](https://ajuda.sankhya.com.br/hc/article_attachments/14871597891223)

Feito isso, realize o fechamento da comissão novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16620791973271) CAUSA:**

Na rotina "Fechamento de comissão",  ao  informar um **comissionado**  (filtros rápidos) ,  caso este **vendedor** não possua um cliente vinculado em seu cadastro a mensagem será apresentada.
