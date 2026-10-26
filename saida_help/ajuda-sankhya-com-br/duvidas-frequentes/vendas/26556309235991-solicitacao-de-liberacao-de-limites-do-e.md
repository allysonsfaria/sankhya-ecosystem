---
id: "26556309235991"
titulo: "Solicitação de liberação de limites do evento 25 - Desconto por Item da Nota para produto mesmo o vendedor tendo saldo flex disponível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26556309235991-Solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-de-limites-do-evento-25-Desconto-por-Item-da-Nota-para-produto-mesmo-o-vendedor-tendo-saldo-flex-dispon%C3%ADvel"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:41:27Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Liberação de Limites", "Passos para resolver", "Razão do erro", "Detalhe do erro", "liberação de limites saldo flex", "VALDESCMAX - Valida desconto máximo", "Venda Mais"]
---

# Solicitação de liberação de limites do evento 25 - Desconto por Item da Nota para produto mesmo o vendedor tendo saldo flex disponível

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26670334223895) **SITUAÇÃO:**

Solicitação de liberação de limites do evento 25 - Desconto por Item da Nota para produto mesmo o vendedor tendo saldo flex disponível.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26556325267223)SOLUÇÃO:**

Espera-se que empresas que utilizam a configuração do Saldo flex, use esta rotina como regra de descontos proporcionando flexibilidade para sua equipe de vendas negociar melhor o produto. Nesse sentido, seria contraditório flexibilizar o desconto de alguns produtos, enquanto se define um limite máximo para outros.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26556325264919)CAUSA:**

O uso do Saldo flex com a validação de desconto máximo (Parâmetro **VALDESCMAX - Valida desconto máximo**) não está previsto em conjunto. Caso o parâmetro esteja configurado com alguma opção diferente de **"Não valida"**, a validação ocorrerá independente do saldo flex do vendedor.
