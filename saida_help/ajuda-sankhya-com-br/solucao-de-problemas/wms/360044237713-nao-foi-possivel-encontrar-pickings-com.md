---
id: "360044237713"
titulo: "Não foi possível encontrar pickings com quantidade suficiente para o produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044237713-N%C3%A3o-foi-poss%C3%ADvel-encontrar-pickings-com-quantidade-suficiente-para-o-produto"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:13Z"
rotulos: ["WMS_E00770", "Produtos", "Configuração", "WMS", "Estoque", "Quantidade insuficiente no picking", "Verifique configuração dos endereços de armazenamento", "Informe produtos no cadastro; envie novamente", "Erro"]
---

# Não foi possível encontrar pickings com quantidade suficiente para o produto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17291223835799) MENSAGEM:**

[WMS\_E00770]  Não foi possível encontrar pickings com quantidade suficiente para o produto: XXX
Verifique a configuração do endereços.

Pickings disponíveis:
-------------------:
Pulmões Disponíveis:
-------------------:
Pegas registradas:

**![Imagem 2: SITUAÇÃO: Ao acessar a Formação de Carga e selecionar a opção "Enviar para Expedição por OC" do botão "Outras Opções",…](https://ajuda.sankhya.com.br/hc/article_attachments/17291223839255) SITUAÇÃO:**
Ao acessar a Formação de Carga e selecionar a opção **"Enviar para Expedição por OC"** do botão **"Outras Opções",** apresenta o erro:

![Imagem 3: SOLUÇÃO: Para correção deste erro, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17291262949911) **SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo:

![Imagem 4: Acesse: WMS » Cadastros » Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/article_attachments/17291262956439) Acesse: WMS » Cadastros » Endereço de Armazenamento

Acesse o endereço em que o produto está armazenado fisicamente e na aba: **"Produto" / "Produtos Relacionados"**: permitir

- Informe o produto e os detalhes de configuração de armazenamento.

Após isso, volte na tela de **"Formação de carga"** e envie novamente para Expedição;

![Imagem 5: Acesse: Comercial » Rotinas » Ordem de Carga » Formação de Carga](https://ajuda.sankhya.com.br/hc/article_attachments/17291223869847) Acesse: Comercial » Rotinas » Ordem de Carga » Formação de Carga

Botão: Outras Opções>>Enviar Para Expedição por OC

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17291262973207) CAUSA:**

No cadastro de endereço de armazenamento não foi informado o(s) produtos(s) permitido(s).
