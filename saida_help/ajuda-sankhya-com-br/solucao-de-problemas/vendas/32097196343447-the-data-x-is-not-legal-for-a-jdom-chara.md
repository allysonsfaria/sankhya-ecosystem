---
id: "32097196343447"
titulo: "The data \"X\" is not legal for a JDOM character content"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32097196343447-The-data-X-is-not-legal-for-a-JDOM-character-content"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-24T12:42:52Z"
rotulos: ["Produtos", "Cache", "XML", "COM_E00717", "Cadastro", "Detalhe do erro", "The data", "is not legal for a JDOM character content", "0x1f is not a legal XML character", "Erro"]
---

# The data "X" is not legal for a JDOM character content

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32405083171863) MENSAGEM:**

[COM\_E00717] The data "X" is not legal for a JDOM character content: 0x1f is not a legal XML character

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/32405117321495) SITUAÇÃO**

Ao realizar qualquer consulta na tela **"Consulta de produtos"**, apresenta a mensagem de erro acima.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32097213451927)SOLUÇÃO:**

![Imagem 4: Acesse o cadastro do Produto citado na mensagem de erro e remova qualquer cactere especial que estiver na descrição.](https://ajuda.sankhya.com.br/hc/article_attachments/32097213453463) Acesse o cadastro do **Produto** citado na mensagem de erro e remova qualquer cactere especial que estiver na descrição.

![Imagem 5: Feche a consulta de produtos, acesse a "Administração do Servidor" e limpe o cache do sistema. Após isso, realize um…](https://ajuda.sankhya.com.br/hc/article_attachments/32097213453847) Feche a consulta de produtos, acesse a **"Administração do Servidor"** e limpe o cache do sistema. Após isso, realize um novo teste.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32405083182103) CAUSA:**

O erro acontece porque o produto citado na mensagem possui algum caractere especial na sua descrição, no entanto, esse tipo de caractere não é válido para o sistema.
