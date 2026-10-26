---
id: "6319143448215"
titulo: "Produto não pode ser excluído porque existe dependência de 'Componentes'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6319143448215-Produto-n%C3%A3o-pode-ser-exclu%C3%ADdo-porque-existe-depend%C3%AAncia-de-Componentes"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:16:50Z"
rotulos: ["Produtos", "Configuração", "Fórmulas", "#publifercausaraiz", "CORE_E03834", "Dependência de Componentes ao Excluir Produto", "Erro"]
---

# Produto não pode ser excluído porque existe dependência de 'Componentes'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16449028504727) MENSAGEM:**

[CORE\_E03834] Produto não pode ser excluído porque existe dependência de 'Componentes'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16449002896535) SOLUÇÃO:**

![Imagem 3: A mensagem é apresentada pois existem 'Componentes' vinculados a esse produto, que estão cadastrados na rotina "Fórmula…](https://ajuda.sankhya.com.br/hc/article_attachments/16449002902423) A mensagem é apresentada pois existem 'Componentes' vinculados a esse produto, que estão cadastrados na rotina **"Fórmula de Composição do Produto".**

- Acesse a **aba "Componentes"** do respectivo produto (Tela: **"Produtos"**) e verifique os componentes cadastrados
- Acesse a tela **"Fórmula de Composição do Produto"** e encontre a fórmula vinculada a tais componentes.

A exclusão do produto só será permitida se esse vínculo/cadastro for desfeito.

**Importante:**

**(1)** Ao duplicar um produto que tenha fórmula de composição vinculada, o produto duplicado traz a mesma fórmula.

**(1)** Caso seja necessário duplicar o produto sem que seja copiado o componente, desligue o parâmetro **"COPITEMCOMPPRO"**.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16449002914071) CAUSA:**

A mensagem é apresentada pois existem 'Componentes' vinculados a esse produto, que estão cadastrados na rotina Fórmula de Composição do Produto.
