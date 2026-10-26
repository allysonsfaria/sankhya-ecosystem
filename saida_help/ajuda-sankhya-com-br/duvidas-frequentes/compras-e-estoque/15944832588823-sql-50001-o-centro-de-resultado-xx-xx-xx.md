---
id: "15944832588823"
titulo: "SQL-50001 O Centro de Resultado xx.xx.xx  não está cadastrado, não está ativo, ou não é analítico nos portais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15944832588823-SQL-50001-O-Centro-de-Resultado-xx-xx-xx-n%C3%A3o-est%C3%A1-cadastrado-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico-nos-portais"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:55:50Z"
rotulos: ["Configuração", "Rateio", "Centro de Resultado", "Financeiro", "SQL-50001", "Solução para erro SQL-50001 no Portal de Compras ao faturar um pedido", "Erro"]
---

# SQL-50001 O Centro de Resultado xx.xx.xx  não está cadastrado, não está ativo, ou não é analítico nos portais

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16831067331479) MENSAGEM:**

SQL-50001 O Centro de Resultado xx.xx.xx  não está cadastrado, não está ativo, ou não é analítico.
 
**Cenário:** No "Portal de Compras", ao  tentar faturar um pedido,  sistema apresenta a mensagem de erro de que o centro de resultado do pedido está inativo e não é analítico, porém no cabeçalho da nota o centro de resultado informado é um centro de resultado ativo e analítico e não é a mesma numeração da mensagem de erro.
 
![Imagem 2: SQL-50001 O Centro de Resultado xx.xx.xx não está cadastrado, não está ativo, ou não é analítico. Cenário: No "Portal…](https://ajuda.sankhya.com.br/attachments/token/Ybyazfgyurr6gQswgQrrFLvb0/?name=image.png)
 
![Imagem 3: SQL-50001 O Centro de Resultado xx.xx.xx não está cadastrado, não está ativo, ou não é analítico. Cenário: No "Portal…](https://ajuda.sankhya.com.br/attachments/token/ZujWhk9Tlc6ZuUumNUn4T2YiT/?name=image.png)
 
**![Imagem 4: SQL-50001 O Centro de Resultado xx.xx.xx não está cadastrado, não está ativo, ou não é analítico. Cenário: No "Portal…](https://ajuda.sankhya.com.br/hc/article_attachments/16831076682135) SOLUÇÃO:**

Identifique se o pedido de compra possui Rateio e verifique qual centro de resultado  consta no rateio. Observe que o código do centro de resultado que está no rateio é o mesmo código que aparece na mensagem de erro.
 
![Imagem 5: Identifique se o pedido de compra possui Rateio e verifique qual centro de resultado consta no rateio. Observe que o…](https://ajuda.sankhya.com.br/attachments/token/GIbn7nopydITEM2KcVwtf9Fqr/?name=image.png)
 
![Imagem 6: Identifique se o pedido de compra possui Rateio e verifique qual centro de resultado consta no rateio. Observe que o…](https://ajuda.sankhya.com.br/attachments/token/10PG4t8GgXaVcnFPvNc2sfI5v/?name=image.png)
 
 **![Imagem 7: Identifique se o pedido de compra possui Rateio e verifique qual centro de resultado consta no rateio. Observe que o…](https://ajuda.sankhya.com.br/hc/article_attachments/16831076684183) CAUSA:**

As informações utilizadas no RATEIO do PEDIDO DE COMPRA (Centro Resultado, Natureza, projeto etc) precisam estar nas condições de : Ativo e Analítico no momento de seu  Faturamento.
