---
id: "6977603937687"
titulo: "Nenhuma nota válida encontrada para a expedição do WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6977603937687-Nenhuma-nota-v%C3%A1lida-encontrada-para-a-expedi%C3%A7%C3%A3o-do-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:15:35Z"
rotulos: ["Configuração", "WMS", "TOP", "Estoque", "WMS_E00621", "Use TOP com tipos P E J ou T", "TIPOs diferentes causam erro na expedição", "Nenhuma nota válida para expedição WMS", "Erro"]
---

# Nenhuma nota válida encontrada para a expedição do WMS

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16478417912215) MENSAGEM:**

[WMS\_E00621] Nenhuma nota valida encontrada para a expedição do WMS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16478417921303) SOLUÇÃO:**

Para realizar o envio de nota ao WMS, o sistema Sankhya aceita apenas a TOP configurada com o Tipo de movimento: 
 
**P - Pedido de venda**
**E - Devolução de compra**
**J - Pedido de requisição**
**T - Transferência**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16478389453975)CAUSA:**

Essa mensagem ocorre pois atualmente a  EXPEDIÇÃO do WMS no Sankhya somente ocorre quando é utilizado uma top que esteja configurada com os tipos de movimentos citados acima.

Qualquer outra TOP que tenha um tipo de movimento diferente destes, ao tentar enviar para a **expedição** no WMS, irá ocorrer o erro.
