---
id: "360045110073"
titulo: "Atualização do Realizado - Gestão Estratégica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110073-Atualiza%C3%A7%C3%A3o-do-Realizado-Gest%C3%A3o-Estrat%C3%A9gica"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:16Z"
rotulos: ["Configuração", "Realizado", "Atualização do Realizado - Gestão Estratégica manual", "Relatórios Gerenciais", "Atualização", "Log", "Repositório", "Financeiro", "EXEJOBINDICADOR", "Atualização do Realizado na Gestão Estratégica", "Metas Gerenciais"]
---

# Atualização do Realizado - Gestão Estratégica

A atualização dos valores realizados é efetuada automaticamente pelo sistema quando o parâmetro **"Executa Job de Atualização de Indicadores - EXEJOBINDICADOR"** estiver ativado. Esta atualização é feita conforme a **"Periodicidade de Atualização"** e o **"Horário"** configurado em cada meta na tela [Metas Gerenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608534), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608534-Metas-Gerenciais#abageral).

![Imagem 1: A atualização dos valores realizados é efetuada automaticamente pelo sistema quando o parâmetro "Executa Job de…](https://ajuda.sankhya.com.br/hc/article_attachments/360101671374)

O job de atualização roda a cada 1 (um) minuto, buscando por metas que precisam ser atualizadas e realizando as atualizações. Para o controle de quais metas devem ser atualizadas, o sistema busca pela **"data da próxima atualização"** registrada na meta (TMIMET.DHPROXATUAL) de forma que, se esta data estiver vazia ou menor que a data atual, significa que a meta precisa ser atualizada e com isso o job faz a atualização da mesma. Se a meta for atualizada com sucesso, a data da próxima atualização é ajustada conforme a configuração da meta. Considere o exemplo: 

Se a configuração estiver feita de modo que a atualização da meta é efetuada diariamente às 19 horas, quando a meta for atualizada, será registrada a próxima atualização com a data do dia seguinte às 19 horas.

Caso ocorra algum erro na atualização da meta, a data da próxima atualização não é atualizada, fazendo com que o job tente atualizar aquela meta em todas as suas próximas execuções, registrando seu erro no log, até que seja providenciada a correção para que a meta possa ser atualizada com sucesso.

Para validação do correto funcionamento da atualização automática ou de algum recálculo das metas, pode-se visualizar na tela Metas Gerenciais, aba [Exercícios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608534-Metas-Gerenciais#abaexerccios) através do botão **"Visualizar Resultados"**, que exibe as linhas de resultado para a meta e exercício em questão.

![Imagem 2: Para validação do correto funcionamento da atualização automática ou de algum recálculo das metas, pode-se visualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/360101683854)

Na atualização automática, seguindo as configurações feitas, o sistema irá atualizar os valores que são "calculados" em cada meta, podendo se tratar tanto do realizado quanto do previsto e seus acumulados, assim como cada farol correspondente a estes resultados.

A atualização dos valores previstos é feita para todo o exercício. Ou seja, em cada atualização, o sistema recalcula os valores previstos para o exercício inteiro, incluindo os períodos futuros.

A atualização dos valores realizados é feita para todo o exercício até o período atual, ou seja, os valores anteriores sempre serão recalculados a não ser que seja feito o **"fechamento do período"**, mas os períodos futuros não serão calculados. Considere o exemplo a seguir:

Em um meta mensal no exercício de 2020, a atualização do realizado feita no dia 23/03/2020 fará a atualização dos períodos de Janeiro, Fevereiro e Março, mesmo que março ainda esteja parcial. A atualização de 03/04/2020 fará a atualização dos mesmos períodos citados e também de Abril, mesmo que este ainda esteja parcial.

## Log da atualização do realizado

A cada atualização de metas, o sistema grava um log com informações referentes à atualização realizada. Assim, pode-se visualizar mais detalhes no log da atualização de resultado das metas, através da tela [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594).

![Imagem 3: A cada atualização de metas, o sistema grava um log com informações referentes à atualização realizada. Assim, pode-se…](https://ajuda.sankhya.com.br/hc/article_attachments/360101684034)

Através de um duplo clique em uma linha desejada, será feito o download do arquivo de extensão **"txt"** contendo os detalhes da atualização de cada meta. O arquivo mostra o status de cada atualização e o tempo gasto com cada uma, permitindo inclusive uma análise de performance de cada query ou expressão das metas.

No caso da ocorrência de algum erro, o log demonstra que houve erro na execução da consulta ou da expressão e exibe a consulta ou expressão executada, podendo ser inclusive no cálculo do farol.

![Imagem 4: No caso da ocorrência de algum erro, o log demonstra que houve erro na execução da consulta ou da expressão e exibe a…](https://ajuda.sankhya.com.br/hc/article_attachments/360103832613)
