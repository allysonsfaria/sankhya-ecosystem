---
id: "360056785493"
titulo: "Pedido já liberado, solicitando nova liberação no faturamento para o Evento 3 - Limite de Crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056785493-Pedido-j%C3%A1-liberado-solicitando-nova-libera%C3%A7%C3%A3o-no-faturamento-para-o-Evento-3-Limite-de-Cr%C3%A9dito"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-21T17:51:38Z"
rotulos: ["Configuração", "Liberação de Limites", "Crédito", "TOP", "Preferências", "Financeiro", "não apagar", "Evitar Repetição de Solicitação de Liberação de Crédito e Atraso"]
---

# Pedido já liberado, solicitando nova liberação no faturamento para o Evento 3 - Limite de Crédito

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16939529865367)SOLUÇÃO:**

![Imagem 2: Verifique as marcações abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16939519059863) Verifique as marcações abaixo:

- Tipos de Operação - TOP » Pedido de Venda,  na aba **"Geral", "Copiar liberações quando faturando individualmente":** marcado
- Tipos de Operação - TOP » Venda, na aba **"Geral",** **"Copiar liberações quando faturando individualmente":** marcado;

![Imagem 3: Acesse a rotina: Comercial » Consulta » Liberação de Limites:](https://ajuda.sankhya.com.br/hc/article_attachments/16939519061143) Acesse a rotina: **Comercial » Consulta » Liberação de Limites:**

- Aplique o filtro utilizando o **Nro único Nota**para o Pedido e para a Nota de Faturamento, atente-se ao campo **"Data liberação";**
- Caso o faturamento ocorra com uma data superior a data do pedido que já havia sido liberado, uma nova solicitação de liberação ocorrerá.

![Imagem 4: Para que não ocorra a solicitação para liberação 2 vezes, tanto no pedido quanto no faturamento, verifique a…](https://ajuda.sankhya.com.br/hc/article_attachments/16939519062167) Para que não ocorra a solicitação para liberação 2 vezes, tanto no pedido quanto no faturamento, verifique a configuração do Parâmetro **"Duração de liberação de Atraso/Limite crédito? - DIASTOLCREATR".**

- Tela **"Preferências -** Configurações » Avançado » Preferências.
- O sistema considera a informação do parâmetro **"Duração de liberação de Atraso/Limite crédito? - DIASTOLCREATR"**, para validar ou não a Nota novamente, para liberações feitas no 'Pedido' em relação ao limite de crédito e atraso. Quando estiver configurado, na confirmação de uma nota originada de um Pedido já liberado, o sistema não solicitará liberação novamente.
- Alinhe com o Setor de Faturamento qual o prazo que um pedido após liberado pode ser faturado para ajustar o Parâmetro.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16939529877783) IMPORTANTE:**

Ao confirmar a Nota de Venda o sistema verifica os débitos do parceiro em questão e, caso haja uma ou mais nota após o pedido de liberação feito, ele soma o valor desta, solicitando assim a liberação do do novo valor.

**Exemplo:**

Nota com valor liberado de 12.741.092,81 no pedido XX, porém após esse pedido houve uma nota de venda YYYYY  no valor de 98,02 tendo três financeiros (2 de 32,01 + 1 de 32,00) todos em aberto. Com isso, o valor de débito do cliente subiu para 12.741.188,83. Nesse cenário o sistema solicita novamente a liberação para aprovar essa diferença de 98,02.
Então, mesmo tendo sido liberado o pedido ao confirmar a Nota de Venda desse pedido, o sistema verifica novamente os financeiros do parceiro.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16939519064727) CAUSA:**

Quando liberado um pedido com a validação do Evento 3 - limite de crédito e o mesmo por algum motivo não foi faturado no mesmo dia, ao faturar no dia seguinte ou após 2, 3 dias, será solicitado uma nova liberação de limite para o evento.
