---
id: "36923787422359"
titulo: "Como fazer o faturamento de pedido de venda parcial quando se utiliza desconto promocional por quantidade?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36923787422359-Como-fazer-o-faturamento-de-pedido-de-venda-parcial-quando-se-utiliza-desconto-promocional-por-quantidade"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:22:09Z"
rotulos: ["Produtos", "Configuração", "Faturamento", "Vendas", "faturamento de pedido de venda parcial", "qtd.parcial dos itens", "utiliza desconto promocional por quantidade", "Selecionar itens", "QTD.FATURADA", "Desconto Promocional"]
---

# Como fazer o faturamento de pedido de venda parcial quando se utiliza desconto promocional por quantidade?

Eventualmente acontece o uso do recurso de **Desconto promocional por quantidade,** porém o faturamento dos itens pode ser realizado de forma fracionada (parcial). Assim, para evitar que o cálculo do desconto registrado na nota fique diferente do desconto informado no pedido, o seguinte procedimento devera ser realizado :

**(1)** No **faturamento do pedido**,  utilize o botão  **'Selecionar itens'** para informar no campo: "**QTD.FATURADA"**a **qtd.parcial** dos itens. Desta forma,  o sistema irá manter o  %Desconto promocional informando no pedido.

**Observação:** caso o usuário não utilize o botão Selecionar itens ,  ao  abrir  a nota e modificar o campo QTDNEG, o sistema irá revalidar o Desconto promocional, podendo gerar divergências dos valores iniciais 

**Exemplo:**
Pedido de venda  
Produto: 10     
Preço de venda normal   = 100,00 
Desconto promocional por qtd. 
 0  a 10    Un  -   Valor de venda  = 90,00 
 11 a 20    Un -   Valor de venda  = 85,00 
 21 a 1000  Un-  Valor de venda  = 80,00 
 
 Ao incluir um pedido de venda  com o produto: 10   informando a  QTD  = 50 unidade,  sistema ira considerar o VALOR DE VENDA  = 80,00  
 
Ao faturar este pedido parcialmente com 10  unidades,  utilizando o botão  SELECIONAR ITENS,  sistema manterá o VALOR DE VENA  = 80,00 
 
Caso cliente não utilize o botão **Selecionar itens**,  ao abrir a **nota de venda**  e modificar o campo **Quantidade  = 10**,  o sistema **irá  considerar o valor de venda  = 90,00** (revalidando o Des. Promocional) , causando divergências entre o **Pedido** e a **Nota de venda**.
