---
id: "26515516533655"
titulo: "Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26515516533655-Apenas-a-TOP-configurada-para-Venda-Balc%C3%A3o-permite-envio-para-o-WMS-sem-OC"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:41:40Z"
rotulos: ["Ordem de Carga", "Configuração", "WMS", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC", "Nota/Pedido nro único: X não é venda Balcão e não possui OC informada", "WMS_E00652", "Venda Balcão"]
---

# Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26515500510487) **MENSAGEM:**

[WMS\_E00652] Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC. Nota/Pedido nro único: X não é venda Balcão e não possui OC informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26515516522647)SOLUÇÃO:**

Acesse a tela **"Ordens de Carga"** e crie uma ordem de carga, antes de vincular na tela **"Formação de Carga"**.

Expedição convencional que não utiliza separação balcão necessita que uma Ordem de Carga esteja vinculado ao pedido para que seja enviado para expedição.

[GIF animado: Imagem 3: Expedição convencional que não utiliza separação balcão necessita que uma Ordem de Carga esteja vinculado ao pedido…](https://ajuda.sankhya.com.br/hc/article_attachments/26560103446295)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26515500521367)CAUSA:**

Ocorre quando se tenta enviar um pedido para expedição, diferente de separação balcão, sem vincular uma OC no pedido.
