---
id: "360043141154"
titulo: "Não é possível liberar a nota XXXXX para conferência, pois a TOP XX não utiliza conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043141154-N%C3%A3o-%C3%A9-poss%C3%ADvel-liberar-a-nota-XXXXX-para-confer%C3%AAncia-pois-a-TOP-XX-n%C3%A3o-utiliza-confer%C3%AAncia"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:22Z"
rotulos: ["COM_E00002", "Conferência", "Configuração", "NF-e", "TOP", "Estoque", "Nota não liberada; TOP sem conferência", "Conferência configurada após lançamento", "Ajuste configuração e crie novo pedido"]
---

# Não é possível liberar a nota XXXXX para conferência, pois a TOP XX não utiliza conferência

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16135570426903) MENSAGEM:**

[COM\_E00002] Não é possível liberar a nota XXXXX para conferência, pois a TOP XX não utiliza conferência.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135606934935) SITUAÇÃO:**

Ao clicar em Liberar Conferência, pela opção **"Outras Opções..."**  » Conferência  » Liberar para conferência, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135570430999) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16135570431639) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

**(2)** Aba **"Estoque"**

**(2)** Campo **"Configuração p/ conferência"**, informe o código da configuração de conferência

![Imagem 5: (2) Campo "Configuração p/ conferência" , informe o código da configuração de conferência](https://ajuda.sankhya.com.br/hc/article_attachments/14653386969367)

![Imagem 6: Após o ajuste, gere um novo Pedido/Nota e use a opção de liberar para conferência.](https://ajuda.sankhya.com.br/hc/article_attachments/16135606942487) Após o ajuste, gere um novo Pedido/Nota e use a opção de liberar para conferência.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135570435735) OBSERVAÇÃO:**

Caso já esteja informado um código, efetue um novo lançamento de pedido/nota, pois a informação deste campo é histórica.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16135606949143) CAUSA:**

Ocorre quando a configuração para trabalhar com conferência é feita depois do lançamento do Pedido/Nota e como a  TOP é um registro histórico deve-se lançar um novo Pedido/Nota.
