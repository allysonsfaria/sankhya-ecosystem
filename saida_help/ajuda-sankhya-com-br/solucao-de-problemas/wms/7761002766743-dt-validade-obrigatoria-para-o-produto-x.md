---
id: "7761002766743"
titulo: "Dt.validade obrigatória para o produto 'xxxx' no endereço 'xxxx'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7761002766743-Dt-validade-obrigat%C3%B3ria-para-o-produto-xxxx-no-endere%C3%A7o-xxxx"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:13:10Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Validade", "não apagar", "#validadojhonatan", "Data validade obrigatória", "Verificar campo shelflife data validade", "Alteração shelflife data não solicitada", "Erro"]
---

# Dt.validade obrigatória para o produto 'xxxx' no endereço 'xxxx'

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16538296489367) MENSAGEM**:

No coletor aparece a mensagem: Dt.validade obrigatória para o produto 'xxxx' no endereço 'xxxx'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16538283442583) SOLUÇÃO:**

Acesse a tela cadastro do produto, aba **"WMS"** e verifique se o campo shelflife está preenchido para o produto.

Acesse a tela Estoque/Endereçamento WMS, e na a doca onde está o produto para ser armazenado, veja se o campo data de validade apresenta data informada. Caso não apresente, cancele o recebimento e confira novamente informando a data de validade do produto.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16538296492567)CAUSA:**

A mensagem é apresentada quando ao armazenar um produto que trabalha com data de validade acontece alguma alteração no campo (shelflife) do produto durante o processo de recebimento, e na conferência a data de validade não é solicitada.
