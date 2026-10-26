---
id: "23088726259607"
titulo: "Cálculo de PIS e COFINS em Vendas de (KITS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23088726259607-C%C3%A1lculo-de-PIS-e-COFINS-em-Vendas-de-KITS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:48:37Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "Impostos"]
---

# Cálculo de PIS e COFINS em Vendas de (KITS)

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23135956629911) SITUAÇÃO:**

Realizando análise do gasto variável de uma nota, onde temos produtos do tipo KIT, percebi que os valores dos impostos PIS/COFINS estão com base de cálculo mais que dobrada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23135956637847) SOLUÇÃO:**

Referente a duvida apresentada, temos primeiramente a seguinte premissa para o devido funcionamento deste processo:

![Imagem 3: O correto no caso da venda de (Kits) é que os impostos sejam calculados apenas para os componentes do kit, e não para…](https://ajuda.sankhya.com.br/hc/article_attachments/23135984476439)  O correto no caso da venda de (Kits) **é que os impostos sejam calculados apenas para os componentes do kit, e não para eles em si, pois se forem calculados para ambos, teremos o problema citado.**
 

![Imagem 4: Entretanto, caso a necessidade de sua empresa, seja diferente desta o time de Unidade poderá atuar nesta demanda…](https://ajuda.sankhya.com.br/hc/article_attachments/23135984482839)  Entretanto, caso a necessidade de sua empresa, seja diferente desta o time de Unidade poderá atuar nesta demanda trazendo o comportamento conforme esperado desde que, com respaldo de sua Contabilidade. 

![Imagem 5: Sobre o campo "Resumo de Impostos" o valor da base dos impostos realmente ficará duplicada conforme comportamento do…](https://ajuda.sankhya.com.br/hc/article_attachments/23135984492567) Sobre o campo "Resumo de Impostos" o valor da base dos impostos**realmente ficará duplicada conforme comportamento do sistema**, visto que lá estará sendo realizada a "Soma de todas as sequências da tabela". Entretanto, ao verificar os de impostos na TGFDIN ''**Consultar alterar dados dos impostos**" será trago a base corretamente do itens, de forma separadas, e também será levado ao XML corretamente. 

![Imagem 6: Sobre o campo "Resumo de Impostos" o valor da base dos impostos realmente ficará duplicada conforme comportamento do…](https://ajuda.sankhya.com.br/hc/article_attachments/23135984509463) 
Para mais informações desta rotina acesse o artigo [Configuração de Kit.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjoxMDIwOTI5MDMyNTE0MywidGlja2V0X2lkIjozMzIzMjIsImNoYW5uZWxfaWQiOjYzLCJ0eXBlIjoiU0VBUkNIIiwiZXhwIjoxNzAzNzY0MzU1fQ.B-2oIBErtgCFl6BUgOUkJdX2Swl4ahE-eC1TpJXg2eE)
