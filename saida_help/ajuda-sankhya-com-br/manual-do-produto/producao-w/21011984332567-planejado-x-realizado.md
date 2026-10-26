---
id: "21011984332567"
titulo: "Planejado x Realizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:50:36Z"
rotulos: ["Planejamento", "Relatórios", "Realizado", "TOP", "Ordens de Produção", "Produção", "APREALMPS", "Planejado", "Performance", "MPS"]
---

# Planejado x Realizado

Por meio desta tela, o gestor de produção pode monitorar de forma clara e simples o planejado com o que de fato foi realizado no Plano Mestre de Produção (MPS) conforme a execução das Ordens de Produção (OP's) lançadas pela [Programação Plano Mestre de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS). Isso oferece uma visão antecipada sobre quando as Ordens de Produção serão concluídas, o que ajuda a prever a execução do planejamento de produção.

Esse acompanhamento pode possibilitar ajustes nos processos para garantir que a produção sempre esteja alinhada ao plano estabelecido, além de que, destaca também eventuais atrasos. 

Em resumo, os painéis irão auxiliar o gestor a identificar possíveis atrasos antes que ocorram, o que possibilita a implementação de ações corretivas e garantia do desempenho e otimização da produção.

![Imagem 1: Lembre-se que, para acessar essa tela, é preciso possuir a licença do produto "30426 - PROGRAMAÇÃO DE O.P/W" e…](https://ajuda.sankhya.com.br/hc/article_attachments/21051088819735) Lembre-se que, para acessar essa tela, é preciso possuir a licença do produto **"30426 - PROGRAMAÇÃO DE O.P/W"** e habilitar o parâmetro **"Apresenta planejado x realizado MPS - APREALMPS"** que, por sua vez, é ligado ou desligado para exibir ou não essa rotina.

![Imagem 2: Lembre-se que, para acessar essa tela, é preciso possuir a licença do produto "30426 - PROGRAMAÇÃO DE O.P/W" e…](https://ajuda.sankhya.com.br/hc/article_attachments/21012005500951)

| Funcionalidades disponíveis | |
| --- | --- |
| [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#PaineldeFiltros) | [Planejado x Realizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#abaPlanejadoxRealizado) |
| [TOP Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#TOPCentrosdeTrabalho) | [TOP Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#TOPOrdensdeProdu%C3%A7%C3%A3o) |

---

### Painel de Filtros

Nesse painel tem-se os seguintes campos:

O campo **"Nro. Plano"**, onde se deve inserir o **"Código"** do [Planejamento de Produção (MRP I)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174) que deseja analisar.

As **"Categorias de Centro de Trabalho"** cadastradas na tela [Categorias de Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119033) do sistema.

Além dos **"Centros de Trabalho"** que também serão exibidos conforme o cadastro na tela [Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793).

Já, por meio da marcação **"Considerar atividades em execução no cálculo do tempo realizado/previsto"** pode-se definir se as atividades em andamento serão ou não, consideradas no cálculo do tempo realizado e previsto. Observe abaixo, um exemplo de como essa marcação funciona:

Com o filtro realizado, caso o tempo planejado para uma atividade for 5 horas e a atividade foi iniciada há 6, mas ainda não foi finalizada, o sistema irá considerar essas 6 horas como tempo **"Realizado"** e irá considerar 0 horas como **"Tempo Previsto"**. 

De modo que, sem a realização desse filtro, essa atividade será considerada como não executada, e o sistema irá considerar 0 horas como tempo Realizado e 5 horas como Tempo Previsto.

Além desse, considere também o exemplo abaixo:

![Imagem 3: Além desse, considere também o exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/21012005505559)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#top)

### Aba Planejado x Realizado

Nessa aba têm-se diferentes painéis para análise. Observe:

#### Gráfico Planejado x Realizado x Previsto:

![Imagem 4: Gráfico Planejado x Realizado x Previsto:](https://ajuda.sankhya.com.br/hc/article_attachments/21011984325527)

Esse gráfico representa as Ordens de Produção **"Disponível"**, **"Planejado"**, **"Realizado"** e o **"Previsto"** programadas no MPS selecionado conforme a capacidade dos Centros de Trabalho. Observe:

**Disponível:** este apresenta o tempo disponível no Centro de Trabalho, sendo que o mesmo considera a carga diária configurada nesse centro, multiplicada pelos dias disponíveis do período do MPS o que irá diminuir as indisponibilidades e as horas já consumidas nos Centros de Trabalho do período, podendo as horas consumidas serem OP's programadas para serem executadas nos Centros de Trabalho em outros planejamentos e no mesmo período do MPS, ou OPs já executadas no Centro de Trabalho dentro do mesmo período do MPS.

Assim, considere o exemplo abaixo:

**(1)** Suponha que a carga horária do Centro de Trabalho é de segunda à sexta de 08:00 as 18:00.

**(2)** Ao gerar um planejamento de produção do dia 01/01/2024 ao dia 31/01/2024 o centro de trabalho terá 230 horas disponíveis, considerando que a empresa irá trabalhar todos os dias do mês, sendo assim 230 horas será 100% da capacidade.

**(2)** Essa capacidade já pode ter sido comprometida por uma indisponibilidade de Centro de Trabalho. Caso houvesse uma indisponibilidade de CT gerada do dia 01/01/2024 as 08:00 ao dia 05/01/2024 as 18:00, o CT teria 180 horas disponíveis, o que corresponde a 78,26% de disponibilidade. Ou seja, o valor que seria apresentado como disponível para esse CT, seria 78,26%.

**(2)** Supondo que exista outro planejamento de produção com Período MPS do dia 01/01/2024 ao dia 31/01/2024, nesse planejamento existe uma OP programada no CT para ser executada do dia 08/01/202 as 08:00 ao dia 12/01/2023 às 18:00, nesse caso o CT teria 130 horas disponíveis, o que corresponde a 56,52% de disponibilidade.

**Planejado:** apresenta o tempo planejado para execução das atividades das Ordens de Produção do MPS programadas para serem executadas nos Centros de Trabalhos. Observe o exemplo:

De forma a considerar o exemplo dado para o disponível, imaginemos que foram programadas duas atividades para serem executadas no centro de trabalho, por exemplo, a primeira atividade foi planejada para ser executada do dia 22/01/2023 as 08:00 ao dia 24/01/2023 14:00, a segunda atividade foi planejada para ser executada do dia 25/01/2023 às 08:00 ao dia 29/01/2023 18:00. A primeira atividade terá 26 horas de duração e a segunda atividade terá 30 horas de duração, totalizando 56 horas para serem executadas no CT dentro do período.

Se o tempo disponível é de 230 horas que equivalem a 100%, o tempo planejado de 56 horas equivale a 24,34% do tempo disponível. Assim, no gráfico, o disponível será de 56,52% e o planejado será de 24,34%.

**Realizado:** exibe o tempo realizado das atividades das OP's que já tiveram sua execução iniciada ou finalizada no Centro de Trabalho desconsiderando as paradas e indisponibilidades destes, que ocorreram durante a execução das atividades. Com base nisso, considere o exemplo:

Considerando o exemplo dado para o planejado, imaginemos que a primeira atividade programada no CT foi iniciada no dia 22/01/2023 as 08:00, parada no dia 23/01/2023 as 09:00, reiniciada no dia 23/01/2023 as 12:00 e finalizada no dia 24/01/2023 as 15:00. A atividade em questão teve 24 horas de duração.

Se o tempo disponível é de 230 horas que equivalem a 100%, o tempo executado de 24 horas equivale a 10,43% do tempo disponível.

No gráfico o disponível será de 56,52% visto o que já foi comprometido para o CT, o planejado será de 24,34% e o executado será de 10,43%.

**Observação:** o cálculo do Realizado pode ser impactado pela marcação Considerar atividades em execução do Painel de Filtros conforme tabela exemplo exibida no filtro. Caso a última atividade da OP tenha sido executada em atraso, a cor do Realizado no gráfico será diferente de quando a atividade foi executada dentro, ou antes do programado. Um Realizado em atraso representa um ponto de atenção, pois pode comprometer a execução das atividades posteriores que poderão ocorrer em atraso.

**Previsto:** apresenta as atividades das OP's que ainda deverão ser executadas no Centro de Trabalho. Desse modo, observe o exemplo abaixo:

Considerando o exemplo dado para o Realizado, como a primeira atividade da OP já foi executada e falta somente a segunda atividade para ser executada, e a segunda atividade foi programada com um tempo de 30 horas de duração: se o tempo disponível é de 230 horas que equivalem a 100%, o tempo previsto de 30 horas equivale a 13,04 do tempo disponível.

No gráfico o disponível será de 56,52% visto o que já foi comprometido para o CT, o planejado será de 24,34%, o executado será de 10,43% e o previsto será 13,04%.

**Observação:** o cálculo do Previsto pode ser impactado pela marcação Considerar atividades em execução do Painel de Filtros. Caso as próximas atividades das OPs estejam previstas para ocorrerem em atraso (o sistema identifica o atraso conforme o momento da consulta e a data e hora programada para início da atividade). A cor do Previsto no gráfico terá uma cor diferente de quando a atividade estiver prevista para ocorrer de acordo com o início programado, de forma que um Previsto em atraso representa um ponto de atenção, pois esse atraso poderá comprometer a finalização da produção dentro do prazo esperado.

Além da visualização por meio do gráfico de barras, a rotina também permite uma visão do Programado, Realizado e Previsto das OP's em forma de tabela para que essa mesma informação também seja exibida no formato data/hora:

[GIF animado: Imagem 5: Além da visualização por meio do gráfico de barras, a rotina também permite uma visão do Programado , Realizado e…](https://ajuda.sankhya.com.br/hc/article_attachments/21051055576087)

Nesse formato, as atividades que ocorreram em atraso ou estiverem previstas para serem executadas em atraso serão apresentadas na cor **vermelha** e as atividades que ocorreram conforme a data e hora prevista, serão apresentadas na cor **azul**.

A **"Dh. Início Prevista"** e **"Dh. Final Prevista"** será de acordo com a **"Dh. Início Planejada"** e **"Dh. Final Planejada"**, exceto nos casos em que a atividade estiver prevista para ocorrer em atraso, pois alguma outra atividade anterior a ela foi executada em atraso, gerando impactos nas atividades que ocorrerão posteriormente a ela.

#### Gráfico % Realização do MPS

No referido gráfico é possível visualizar o Realizado e as atividades a serem realizadas por Ordem de Produção conforme a execução das OP's:

[GIF animado: Imagem 6: No referido gráfico é possível visualizar o Realizado e as atividades a serem realizadas por Ordem de Produção conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/21051055589143)

Por exemplo:

**(1)** Na Programação Plano Mestre de Produção, ao programar duas execuções de Ordens de Produção:

**(2)** **OP1**

- **Atividade1:** 2 horas de duração;
- **Atividade 2:** 3 horas de duração;
- **Atividade 3:** 5 horas de duração.

**(2)OP2**

- **Atividade 1:** 3 horas de duração;
- **Atividade 2:** 6 horas de duração;
- **Atividade 3:** 7 horas de duração.

Para executar todas as atividades da OP1 serão gastas um total de 10 horas e para executar a OP2 serão gastas 16 horas, ou seja, para realizar todas as OP's programadas a partir do MPS, serão utilizadas 26 horas.

**(2)** Desse modo, se a primeira atividade de cada OP tenha sido executada, o Realizado da OP1 será de 2 horas, independente se a atividade foi efetuada em 2 horas, mais, ou menos tempo, e o Realizado da OP2 será de 3 horas, totalizando 5 horas de realizado;

**(2)** Caso as 26 horas equivalem a 100%, 5 horas são equivalente à 19,23%. Assim, o Realizado do MPS será de 19,23% e o A Realizar do MPS será de 80,77%;

**(2)** Quando 10 horas forem equivalentes a 100% da OP1, 2 horas irão representar 20%. Então, o Realizado da OP1 será 20% e o A Realizar da OP1 será 80%;

**(2)** Por fim, se 16 horas equivalem a 100% da OP2, 3 horas correspondem a 18,75%. Dessa forma, o Realizado da OP2 será de 18,75% e o A Realizar da OP2 será de 81,25%.

#### Gráfico Volume Previsto x Volume Realizado

No referido gráfico, pode-se visualizar o **"Volume Previsto"** e **"Volume Realizado"** de cada Ordem de Produção de acordo com o **"Saldo a Produzir"** das OP's e a quantidade de produtos em notas de produção:

[GIF animado: Imagem 7: No referido gráfico, pode-se visualizar o "Volume Previsto" e "Volume Realizado" de cada Ordem de Produção de acordo…](https://ajuda.sankhya.com.br/hc/article_attachments/21051055598359)

**Contador Tempo restante para execução**

Esse contador exibe o tempo que falta para início previsto de execução das Ordens de Produção de forma a considerar o Tempo restante para a execução de acordo a **"Dh. Início Planejado"** da primeira atividade programada para ser executada no planejamento selecionado, a carga horário da planta de manufatura e o momento que a consulta está sendo realizada.

Caso as atividades das OP's programadas não tiverem sido iniciadas e estiverem em atraso, ou iniciados em atraso, o contador irá apresentar a cor **vermelha**. Além disso, ao iniciar qualquer atividades das OP's programadas no planejamento selecionado, o contador será travado para que, em futuras consultas possa ser verificado se o planejamento foi iniciado em atraso ou não.

![Imagem 8: Caso as atividades das OP's programadas não tiverem sido iniciadas e estiverem em atraso, ou iniciados em atraso, o…](https://ajuda.sankhya.com.br/hc/article_attachments/21051088892183)

**(1)** Baseado nisso, considere o exemplo abaixo:

**(2)** Suponha que a carga horária da planta de manufatura é de segunda a sexta de 08:00 às 18:00. Após gerar mestre de produção, ao gerar a programação de produção que está configurada para realizar a primeira atividade das OP's no dia 02/01/2024 as 10:00;

**(2)** Caso seja realizada uma consulta do Planejado x Realizado desse Plano de Mestre de Produção no dia 02/01/2024 as 12:00, o contador irá apresentar um valor igual a 2 horas, e o horário exibirá a cor **vermelha**, pois a execução das atividades da OP está 2 horas atrasado;

**(2)** Se a atividade da OP for iniciada 02/01/2024 09:00, sempre que uma consulta do MPS for realizada, o contador apresentará um valor igual a 1:00, pois as atividades programadas no MPS se iniciaram 1 hora adiantada;

**(2)** Caso a atividade da OP seja iniciada 02/01/2024 as 12:00, ao consultar o MPS o contador irá exibir um valor igual a 2:00 na cor vermelha, pois as atividades programadas no MPS se iniciaram 2 horas em atraso.

#### Indicador de Folga

Esse indicador indica se existe folga ou não na execução das atividades das Ordens de Produção conforme a configuração do indicador de folga, a **"Dh. Planejada"** para execução e conclusão das OPs e a **"Dh. Prevista"** para execução e conclusão das OP's calculadas de acordo com a execução das atividades.

[GIF animado: Imagem 9: Esse indicador indica se existe folga ou não na execução das atividades das Ordens de Produção conforme a configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/21051055632663)

**(1)** Desse modo, observe o exemplo abaixo:

**(2)** No Indicador de Folga, os campos foram preenchido da seguinte maneira:

- ![Imagem 10: <: 500 min.;](https://ajuda.sankhya.com.br/hc/article_attachments/21051088915735) **<:** 500 min.;
- ![Imagem 11: <: 1000 min;](https://ajuda.sankhya.com.br/hc/article_attachments/21051055672087) **<:**1000 min;
- ![Imagem 12: >: 1500 min;](https://ajuda.sankhya.com.br/hc/article_attachments/21051088956055) **>:** 1500 min;
- ![Imagem 13: >=: 2000 min.](https://ajuda.sankhya.com.br/hc/article_attachments/21051088976791) **>=:** 2000 min.

Foi gerada uma Programação Plano Mestre de Produção para as atividades das OPs  serem iniciadas dia 09/01/2024 as 9:00h e finalizadas dia 01/01/2024 as 18:00 do mesmo dia.

Ao consultar o Programado x Realizado no dia 08/01/2024 as 8:00, o Indicador de Folga deverá apresentar a cor **laranja**, pois faltam 660 minutos úteis para início da execução das OPs da programação.

Quando as Ordens de Produção forem iniciadas, o sistema irá comparar a **"Dh. Final Planejada"** e **"Dh. Final Prevista"** para execução da última atividade que será executada dentro da programação para calcular o indicador, pois a folga pode sofrer alterações conforme o andamento da produção, considerando que uma produção pode iniciar em atraso e ainda assim terminar dentro do esperado.

Assim, ao finalizar todas as atividades das OP's programadas para serem executadas, o Indicador de Folga será travado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#top)

### Aba TOP Centros de Trabalho

Na aba TOP Centros de Trabalho pode-se consultar os Centros de Trabalho que possuem a melhor e/ou pior performance na execução das Ordens de Produção. Essa informação é importante para que seja possível identificar os Centros de Trabalho que não estão atendendo as expectativas do planejamento e agir de forma corretiva para moderar os problemas e evitar atrasos na produção.

Desse modo, têm-se 4 painéis, sendo eles:

- TOP 5 Centros de Trabalho com melhor performance;
- Detalhes dos CTs com melhor performance;
- TOP 5 Centros de Trabalho com pior performance;
- Detalhes dos CTs com pior performance.

O sistema irá apresentar o detalhamento das atividades executadas no centro de trabalho, de acordo com o Centro de Trabalho selecionado na painel TOP 5 Centros de Trabalho com melhor performance ou TOP 5 Centros de Trabalho com pior performance.

![Imagem 14: O sistema irá apresentar o detalhamento das atividades executadas no centro de trabalho, de acordo com o Centro de…](https://ajuda.sankhya.com.br/hc/article_attachments/21051055713175)

Os painéis TOP 5 Centros de Trabalho com melhor performance e Detalhes dos CTs com melhor performance possuem as mesmas colunas; assim como os painéis TOP 5 Centros de Trabalho com pior performance e Detalhes dos CTs com pior performance.

É relevante mencionar, que a performance do CT é calculada conforme o tempo planejado e o executado das atividades nos Centros de Trabalho, de forma que, se as atividades gastaram menos tempo do que o planejado, a performance foi boa, porém, se estas utilizaram mais do que o planejado para a execução, o desempenho do CT será classificado como ruim.

Sabendo disso, considere o exemplo:

(1)** Se CT possuir uma performance de 120%:** esta iria executar 10 atividades da OP em 10 horas, mas as atividades foram realizadas em 8 horas;

(1)** Caso a CT tenha uma performance de 90%:** para a execução de 10 atividades da OP levariam 10 horas, no entanto, as atividades foram executadas em 11 horas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#top)

### Aba TOP Ordens de Produção

Nessa aba, o usuário pode consultar as Ordens de Produção que possuem a melhor e/ou pior performance na execução. Essa informação é importante para que o usuário possa identificar as Ordens de Produção que podem ser concluídas em atraso e agir de forma corretiva para moderar os problemas e evitar atrasos na produção.

Assim como a aba acima, essa aba possui 4 painéis, sendo eles:

- TOP 5 Ordens de Produção com melhor performance;
- Detalhes das OPs com melhor performance;
- TOP 5 Ordens de Produção com pior performance;
- Detalhes das OPs com pior performance.

O sistema irá apresentar o detalhamento das atividades executadas na Ordem de Produção, de acordo com a OP selecionada na grade TOP 5 Ordens de Produção com melhor performance ou TOP 5 Ordens de Produção com pior performance.

![Imagem 15: O sistema irá apresentar o detalhamento das atividades executadas na Ordem de Produção, de acordo com a OP selecionada…](https://ajuda.sankhya.com.br/hc/article_attachments/21051055719447)

Aqui, serão exibidos os dados de desempenho OP, sendo esta calculada com base no tempo de planejamento e no tempo executado das atividades de OP's nos Centros de Trabalho, de modo que, se as atividades gastarem menos tempo do que o planejado para serem executadas, a performance da OP foi boa, enquanto se as atividades utilizarem mais tempo do que o planejado para suas execuções, então o desempenho foi ruim.

Dessa forma, considere o exemplo abaixo:

(1)** Se OP possuir uma performance de 120%:** esta iria executar 10 atividades da OP em 10 horas, mas as atividades foram executadas em 8 horas;

(1)** Caso a OP tenha uma performance de 90%:** para a execução de 10 atividades da OP levariam 10 horas, no entanto, as atividades foram executadas em 11 horas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21011984332567-Planejado-x-Realizado#top)
