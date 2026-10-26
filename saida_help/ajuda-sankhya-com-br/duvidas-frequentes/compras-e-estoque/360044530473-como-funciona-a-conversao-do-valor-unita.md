---
id: "360044530473"
titulo: "Como funciona a conversão do Valor Unitário, no lançamento de itens em Notas de Compras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044530473-Como-funciona-a-convers%C3%A3o-do-Valor-Unit%C3%A1rio-no-lan%C3%A7amento-de-itens-em-Notas-de-Compras"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:55:31Z"
rotulos: ["Produtos", "Custos", "Configuração", "#camilanobre", "TOP", "Conversão de Valor Unitário em Notas de Compras", "Notas de compras", "custo de reposição"]
---

# Como funciona a conversão do Valor Unitário, no lançamento de itens em Notas de Compras

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18860322867351) SOLUÇÃO:**

A conversão do valor unitário ocorrerá caso possua custo na tabela de custo do(s) respectivo(s) produto(s).

Temos alguns exemplos:

**Exemplo prático 1:**

Produto: 9016,possui como Unidade Padrão= UN e possui 2 Unidades Alternativas cadastrada CX e PC e um valor de R$ 1,50 de Custo de Reposição(Lançado Manual).

Considerando que o produto possui CUSTO DE REPOSIÇÃO no valor de **R$ 1,50** e a TOP de Compra está configurada para Usar como preço = **Ultimo custo reposição**

1.1- Se houver o lançamento do Produto na grade de Itens, com a Unidade CX, o valor unitário será multiplicado pela quantidade da **Caixa**, que neste caso é 12.

Calculo: R$ 1,50 \* 12 = Vlr Unitário R$ 18,00

1.2- Se houver o lançamento do produto na grade de Itens, com a Unidade PC, o valor unitário será dividido pela quantidade da **Peça,**que neste caso é 10.

Calculo: R$ 1,50 / 10 = Vlr Unitario R$ 0,15

Para que a conversão chegue ao valor correto, de acordo com a fator de multiplicação/divisão da Unidade Alternativa, considere ajustar o parâmetro **DECVLRVOLALT**com uma quantidade aceitável de casas decimais, para que não haja arrendamento ou ate 'zeramento' do valor unitário, quando houver divisão.

**Exemplo prático 2:**

2.1- Caso o parâmetro **DECVLRVOLALT = 1** e o lançamento do produto na grade de itens, com a Unidade PC, o valor unitário será dividido pela quantidade da peça que neste caso é 10, e não chegando ao valor correto, será arredondado para cima, ficando R$ 0,20.

2.2- Lembrando que o parâmetro '**CUSTODEC-Decimais para custo'**, é usado para determinar a quantidade de casas decimais no Processo de Compra, então se no caso ressaltado logo acima, o parâmetro estivesse  **CUSTODEC= 0**, e o lançamento ocorresse com a Unidade **PC**, o valor unitário do produto seria R$ 0,00, pois não seria possível apresentar o calculo matemático feito pelo fator de divisão em PC.

**Observação:**

Vale ressaltar que na primeira compra não temos o custo destacado, pois ainda não ocorreu a compra do produto. Então os cálculos feito acima não acontecerão.
