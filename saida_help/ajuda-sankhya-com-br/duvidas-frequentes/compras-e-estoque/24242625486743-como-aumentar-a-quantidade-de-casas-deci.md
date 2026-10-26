---
id: "24242625486743"
titulo: "Como aumentar a quantidade de casas decimais no campo 'Estoque' da tela Contagem de Estoque?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24242625486743-Como-aumentar-a-quantidade-de-casas-decimais-no-campo-Estoque-da-tela-Contagem-de-Estoque"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:47:20Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Preferências", "Configurar em \"Preferências\" o parâmetro _MQTD", "Define casas decimais em \"Contagem de Estoque\"", "Máscaras: 0.00 (2) 0.0000 (4) 0.000000 (6)"]
---

# Como aumentar a quantidade de casas decimais no campo 'Estoque' da tela Contagem de Estoque?

O parametro **"\_MQTD - Máscara para quantidade de produtos"** é quem define a quantidade de casas decimais, da tela de **"Contagem de Estoque".**  Esse parâmetro recebe uma máscara e através desta extrai a quantidade de casas decimais que serão usadas para o campo **"Estoque"** da tela Contagem de Estoque, por exemplo:
 
###,###,##0.00 = 2 casas decimais
###,###,##0.0000 = 4 casas decimais
###,###,##0.000000 = 6 casas decimais

Assim, para aumentar o número de casas decimais no campo Estoque, da tela Contagem de estoque, acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"**, busque pelo parâmetro \_MQTD - Máscara para quantidade de produtos e configure-o do para a quantidade desejada, de acordo com as orientações acima.
