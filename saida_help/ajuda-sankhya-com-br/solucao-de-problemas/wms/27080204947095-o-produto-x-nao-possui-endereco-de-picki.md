---
id: "27080204947095"
titulo: "O Produto: X não possui endereço de Picking configurado. Verifique com o Gerente do WMS Pedido: XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27080204947095-O-Produto-X-n%C3%A3o-possui-endere%C3%A7o-de-Picking-configurado-Verifique-com-o-Gerente-do-WMS-Pedido-XXXX"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:40:11Z"
rotulos: ["WMS_E00770", "Produtos", "Configuração", "WMS", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "O Produto: X não possui endereço de Picking configurado", "O produto deve estar vinculado em um endereço do Tipo", "Picking e que 'Permite Expedição'", "Esse cadastro é feito na Rotina", "WMS >> Cadastros >> Endereço de Armazenamento", "Verifique com o Gerente do WMS Pedido", "Erro"]
---

# O Produto: X não possui endereço de Picking configurado. Verifique com o Gerente do WMS Pedido: XXXX

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27080204918423) **MENSAGEM:**

[WMS\_E00770] O Produto: X não possui endereço de Picking configurado. Verifique com o Gerente do WMS Pedido: XXXX

O produto deve estar vinculado em um endereço do Tipo: Picking e que 'Permite Expedição'. Esse cadastro é feito na Rotina: WMS >> Cadastros >> Endereço de Armazenamento

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27080204922135)SOLUÇÃO:**

Verifique com o gerente do WMS qual o endereço de picking que o produto pertence e valide se o mesmo se encontra disponível. Caso não exista endereço vinculado, acesse a tela **"Endereço de Armazenamento"** na aba **"Produto"**, defina a relação permitir e faça o vínculo do produto no endereço de picking.

[GIF animado: Imagem 3: Verifique com o gerente do WMS qual o endereço de picking que o produto pertence e valide se o mesmo se encontra…](https://ajuda.sankhya.com.br/hc/article_attachments/27080224897303)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27080224898967)CAUSA:**

Ocorre ao tentar enviar um pedido para expedição no qual um ou mais produtos estão sem endereço de pincking vinculado ou em endereço de picking bloqueado na tela de endereço de armazenamento.
