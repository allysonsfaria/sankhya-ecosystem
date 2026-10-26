---
id: "360044470633"
titulo: "Qual é a configuração para desoneração de PIS/COFINS referente a vendas na zona franca de Manaus (SUFRAMA)? "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044470633-Qual-%C3%A9-a-configura%C3%A7%C3%A3o-para-desonera%C3%A7%C3%A3o-de-PIS-COFINS-referente-a-vendas-na-zona-franca-de-Manaus-SUFRAMA"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:57:08Z"
rotulos: ["Configuração", "Parceiro", "XML", "SUFRAMA", "Impostos", "Alíquota Zero desonera PIS/COFINS", "Suframa para PIS/COFINS isenta valores", "Valores desonerados incluídos no XML", "PIS/COFINS", "Zona Franca"]
---

# Qual é a configuração para desoneração de PIS/COFINS referente a vendas na zona franca de Manaus (SUFRAMA)? 

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17124868407575) SOLUÇÃO:**

Foi criado no  tela de cadastro de parceiros  a marcação **"Possui Suframa para PIS/COFINS",** que tem o objetivo de atender a regra de vendas para a Zona Franca de Manaus e a Área de Livre Comércio. Ou seja, com ela habilitada, os valores que seriam devidos à título de PIS/COFINS serão dados como desconto no total da nota, sem influenciar o valor do produto.

![Imagem 2: Foi criado no tela de cadastro de parceiros a marcação "Possui Suframa para PIS/COFINS", que tem o objetivo de atender…](https://ajuda.sankhya.com.br/hc/article_attachments/4415911332887)

**![Imagem 3: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17124894784535) IMPORTANTE:**

Com a marcação acima habilitada e o campo **"Alíquota Suframa",** do Cadastro de [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS) e [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS), preenchido, a nota sendo de venda e o CST do PIS e COFINS igual à **"06 - Alíquota Zero"**, o cálculo desses dois impostos será feito preenchendo os campos de **"Alíquota"** e **"Valor de PIS/COFINS"** desonerados, sendo que, isso vale tanto para incidência no produto quanto para despesas acessórias.

No cadastro de alíquotas de PIS/COFINS não marque a opção **"Produto sem tributação".**

![Imagem 4: No cadastro de alíquotas de PIS/COFINS não marque a opção "Produto sem tributação".](https://ajuda.sankhya.com.br/hc/article_attachments/13782627906327)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17124868413207) OBSERVAÇÃO:**

A soma dos valores de PIS/COFINS, desonerados dos impostos do item, será incluída no campo **"Valor PIS/COFINS Desonerados"** do [Rodapé da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) e, no XML tem-se os valores desonerados adicionados à tag **<vDesc>**.

**(1)** Artigos relevantes:

- [Cadastro de parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)
- [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS)
- [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS)
