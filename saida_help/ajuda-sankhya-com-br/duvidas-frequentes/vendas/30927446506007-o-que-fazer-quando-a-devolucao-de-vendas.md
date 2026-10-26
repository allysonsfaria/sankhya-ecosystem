---
id: "30927446506007"
titulo: "O que fazer quando a devolução de Vendas via recusa não calcula saldo flex?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30927446506007-O-que-fazer-quando-a-devolu%C3%A7%C3%A3o-de-Vendas-via-recusa-n%C3%A3o-calcula-saldo-flex"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:34:18Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Crédito", "Vendas", "Devolução", "Devolução de Vendas via recusa não calcula saldo flex", "NF-e de Devolução via Recusa", "Usar Créd.Flex"]
---

# O que fazer quando a devolução de Vendas via recusa não calcula saldo flex?

![Imagem 1: SITUAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/30927446504343) **SITUAÇÃO:**

NFe de venda tem desconto e consome saldo flex do vendedor, ao realizar a devolução marcando a opção **"NF-e de Devolução via Recusa?"** não devolve o saldo flex consumido na venda.

![Imagem 2: NFe de venda tem desconto e consome saldo flex do vendedor, ao realizar a devolução marcando a opção "NF-e de Devolução…](https://ajuda.sankhya.com.br/hc/article_attachments/30996710813335)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30927480708503)SOLUÇÃO:**

Como a devolução via recusa utiliza o parceiro vinculado ao cadastro da empresa (Configurações » Cadastros » Empresas), se precisar que o saldo flex seja calculado neste lançamento, marque no cadastro deste parceiro, aba **"Crédito"**, o campo **"Usar Créd.Flex?"**.

![Imagem 4: Como a devolução via recusa utiliza o parceiro vinculado ao cadastro da empresa (Configurações » Cadastros » Empresas),…](https://ajuda.sankhya.com.br/hc/article_attachments/30996748208023)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30927480708247)CAUSA:**

A devolução via recusa é necessária quando a mercadoria retorna ao estabelecimento de origem sem ter sido recebida pelo destinatário, ou seja, não houve a entrada da mercadoria no estabelecimento e nem a emissão do documento fiscal referente à sua saída em devolução. Nessa situação, é emitida uma nota fiscal de entrada (devolução de venda), com a empresa sendo tanto a emitente quanto o destinatário. Dessa forma, o sistema altera o parceiro do lançamento para o parceiro configurado no cadastro da empresa, no caso desse parceiro não estar configurado para calcular saldo flex o "estorno" do saldo flex do vendedor não ocorrerá.
