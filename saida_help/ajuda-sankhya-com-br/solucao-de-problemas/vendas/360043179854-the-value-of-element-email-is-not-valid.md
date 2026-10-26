---
id: "360043179854"
titulo: "The value '' of element 'Email' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179854-The-value-of-element-Email-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:34Z"
rotulos: ["Configuração", "Parceiro", "NFS-e", "Valor '' do elemento 'Email' é inválido", "Preencha o e-mail no cadastro de Parceiros e gere o lote novamente", "E-mail do parceiro não informado ou incorreto no cadastro", "Erro", "Documentos Eletrônicos"]
---

# The value '' of element 'Email' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16454055222807) MENSAGEM:**

The value '' of element 'Email' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454055224471) SITUAÇÃO:**

Ao gerar lote de uma NFS-e é apresentada a mensagem de rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454052730647) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 4: Acesse: " Parceiros " (Caminho de acesso: Configurações » Cadastros » Parceiros )](https://ajuda.sankhya.com.br/hc/article_attachments/16454055229207) Acesse: "[**Parceiros**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)" (Caminho de acesso: Configurações » Cadastros » Parceiros)

- Aba "**NF-e/NFS-e/CT-e"**,
- Campo "**E-mail p/ envio NF-e/NFS-e/CT-e"**: informe os e-mail's do parceiro

![Imagem 5: Após o ajustes, gere o lote da nota novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16454052736407) Após o ajustes, gere o lote da nota novamente.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16454055233431) CAUSA:**

Ocorre quando o e-mail do parceiro não está devidamente informado/cadastrado. Podem ocorrer rejeições como:

- EL35: O campo e-mail não foi preenchido para um novo tomador 
  Conforme o manual: O preenchimento do e-mail é obrigatório para um novo tomador.
- EL40: Campo E-mail do tomador informado incorretamente. 
  Conforme o manual: O campo E-mail do tomador deverá ter tamanho máximo de 80 caracteres.
