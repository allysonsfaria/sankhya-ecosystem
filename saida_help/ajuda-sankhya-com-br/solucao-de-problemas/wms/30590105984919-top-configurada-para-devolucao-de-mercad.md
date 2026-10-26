---
id: "30590105984919"
titulo: "TOP configurada para Devolução de Mercadorias no WMS com a diferença na quantidade dos produtos não foi encontrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30590105984919-TOP-configurada-para-Devolu%C3%A7%C3%A3o-de-Mercadorias-no-WMS-com-a-diferen%C3%A7a-na-quantidade-dos-produtos-n%C3%A3o-foi-encontrada"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:35:20Z"
rotulos: ["Configuração", "Devolução de Compra", "WMS", "TOP", "Estoque", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "com a diferença na quantidade dos produtos não foi encontrada", "WMS_E00695", "TOP configurada para Devolução de Mercadorias no WMS"]
---

# TOP configurada para Devolução de Mercadorias no WMS com a diferença na quantidade dos produtos não foi encontrada

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30590105969047) **MENSAGEM:**

[WMS\_E00695] TOP configurada para Devolução de Mercadorias no WMS com a diferença na quantidade dos produtos não foi encontrada. 

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30590061448727)SOLUÇÃO:**

Acesse a tela **Preferência da empresa**, na aba **"WMS"**, verifique se existe uma TOP no campo **"TOP p/ Devolução de Mercadorias cadastrada"**. Caso não tenha, inclua uma TOP com o tipo de movimento E- Devolução de Compra para a empresa.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30590061450519)CAUSA:**

Ocorre quando na tela Preferência da empresa não há uma TOP definida no campo TOP p/ Devolução de Mercadorias e o usuário tenta gerar uma devolução de compra durante o recebimento de mercadoria.
