---
id: "39373801767063"
titulo: "Erro no Cálculo do Adiantamento - Valor Incorreto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39373801767063-Erro-no-C%C3%A1lculo-do-Adiantamento-Valor-Incorreto"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-19T13:00:50Z"
rotulos: ["Configuração", "Fórmulas", "Folha de Pagamento", "Pessoal+", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no Cálculo do Adiantamento - Valor Incorreto

**Situação**

Ao processar a folha de adiantamento, o sistema apresenta um valor diferente do esperado. Isso ocorre principalmente em meses com quantidade de dias diferente de 30, quando a fórmula personalizada utiliza uma divisão fixa por 30 e multiplica pela variável **"&DIASTRA"**, resultando em cálculos proporcionais incorretos.

**Solução**

**(1)** Acesse a tela **"Regras de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo) e localize a regra de cálculo utilizada pelos funcionários com divergência no adiantamento.

**(2)** Na aba **"Tipo de Mês"**, verifique se a opção **"Calcula resíduo de afastamento em meses que não possuem 30 dias"** está marcada corretamente para a referência atual.

**(3)** Verifique a fórmula personalizada do evento de adiantamento. Se a fórmula utiliza divisão fixa por 30, ajuste-a para utilizar variáveis que se adaptem automaticamente ao tipo de mês configurado na regra de cálculo.

**(4)** Após os ajustes, recalcule a folha de adiantamento para os funcionários afetados e valide se o valor está correto (40% do salário base).

 

**Causa**

O erro ocorre quando a fórmula personalizada do adiantamento utiliza uma divisão fixa por 30 dias e multiplica pela variável **"&DIASTRA"**, que é sensível às configurações do tipo de mês definidas na regra de cálculo. Em meses com 31 dias, por exemplo, a conta realiza uma divisão por 30 e uma multiplicação por 31, fazendo com que o valor final não seja compatível com os 40% esperados.

Além disso, a marcação incorreta da opção **"Calcula resíduo de afastamento em meses que não possuem 30 dias"** no histórico da regra de cálculo pode gerar divergências no cálculo proporcional.

A solução definitiva envolve ajustar a fórmula personalizada para que utilize variáveis dinâmicas, garantindo que mesmo com mudanças nas regras de cálculo ou no tipo de mês, a proporcionalidade seja calculada corretamente.
