---
id: "30589799797911"
titulo: "O Modelo Estorno WMS - Dev. Compra não está configurado no cadastro da empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30589799797911-O-Modelo-Estorno-WMS-Dev-Compra-n%C3%A3o-est%C3%A1-configurado-no-cadastro-da-empresa"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:35:28Z"
rotulos: ["Configuração", "WMS", "TOP", "Estoque", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "COM_E00913", "O Modelo Estorno WMS - Dev. Compra não está configurado no cadastro da empresa"]
---

# O Modelo Estorno WMS - Dev. Compra não está configurado no cadastro da empresa

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30589799789975) **MENSAGEM:**

[COM\_E00913] O Modelo Estorno WMS - Dev. Compra não está configurado no cadastro da empresa

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30589772182935)SOLUÇÃO:**

![Imagem 3: Acesse a tela Preferência da empresa, na aba "WMS" , em Movimentações e Armazenagem , no campo "Modelo Estorno WMS -…](https://ajuda.sankhya.com.br/hc/article_attachments/30617285067159) Acesse a tela Preferência da empresa, na aba **"WMS"**, em **Movimentações e Armazenagem**, no campo **"Modelo Estorno WMS - Dev. Compra"** verifique se existe um modelo cadastrado.

![Imagem 4: Caso não tenha, acesse a tela Modelo de Notas e Pedidos (Comercial » Consulta » Modelo de Notas e Pedidos) e inclua um…](https://ajuda.sankhya.com.br/hc/article_attachments/30617285070871) Caso não tenha, acesse a tela **Modelo de Notas e Pedidos**(Comercial » Consulta » Modelo de Notas e Pedidos) e inclua um modelo com uma TOP configurada para o processo de estorno de mercadorias.
**Observação:** para mais informações, veja o artigo: **["Como fazer o estorno de uma devolução total de nota gerada apartir de um recebimento?"](https://ajuda.sankhya.com.br/hc/pt-br/articles/30589110751127).**

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30589799792023)CAUSA:**

Ao deletar uma nota de devolução gerada indevidamente através do recebimento no portal de compras, a mensagem é apresentada.
