---
id: "4415478433047"
titulo: "Telemetria de Processos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4415478433047-Telemetria-de-Processos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:02:13Z"
rotulos: ["Configuração", "Eventos", "Relatórios", "NF-e", "Analítico", "Preferências", "br.com.sankhya.mge.TelemetriaProcesso", "Telemetria de processos", "Consolidado", "Telemetria de Processos: Monitoramento e Análise"]
---

# Telemetria de Processos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311143615383) Módulo: Configurações > Consulta
```

---

A Telemetria de Processos é uma ferramenta que fornece dados para medição e monitoramento de determinadas rotinas envolvidas na emissão de NF-e. No Sankhya Om, temos exemplos clássicos que demandam monitoramento, sendo eles: Lançamento de Pedidos/Nota, Faturamento, Geração de XML (NF-e, NFS-e), Contabilização, entre outros.

O objetivo desta ferramenta é gerar dados suficientes para encontrar problemas de desempenho em diferentes rotinas. Os principais dados que serão apurados são:

- A aplicação que solicitou o serviço.
- O nome do serviço executado.
- Tempo total de execução do serviço.
- Tempo médio de execução do serviço.
- Menor tempo de execução do serviço.
- Maior tempo de execução do serviço.
- O detalhamento de micro chamadas dentro do serviço (quantidade de chamadas, tempo total, médio, menor e maior).
- Permitir um comparativo de dados anteriores com dados apurados recentemente.

As informações coletadas e processadas da telemetria estão divididas em duas categorias:

(1)** Analítico:** Trata-se de registros individuais coletados pela telemetria de processos que se mantêm por uma quantidade parametrizada de dias disponíveis até serem consolidados e excluídos;

(1)** Consolidado:** São registros analíticos agrupados por dia. Esse tipo de registro possui mais informações que o analítico, por exemplo, quantidade chamadas, tempo médio, maior tempo, menor tempo e se mantêm por uma quantidade parametrizada de meses até serem excluídos.

---

![Imagem 2: Para acessar esta tela, primeiramente é necessário habilitar o parâmetro "HABILITATELPRO - Habilitar tela da Telemetria…](https://ajuda.sankhya.com.br/hc/article_attachments/16807952501143) Para acessar esta tela, primeiramente é necessário habilitar o parâmetro **"HABILITATELPRO - Habilitar tela da Telemetria de Processo?"** na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834).

O próximo passo é consultar os processos desejados, para isso você poderá utilizar o Painel de Filtros preenchendo alguns dos campos abaixo:

![Imagem 3: O próximo passo é consultar os processos desejados, para isso você poderá utilizar o Painel de Filtros preenchendo…](https://ajuda.sankhya.com.br/hc/article_attachments/4415552124951)

Informe um **"Período de Coleta de dados"** para consultar o processo desejado. Por default a tela já apresenta um período predefinido para a consulta.

No campo **"Nome do Serviço/Processo"**, informe o nome dado ao serviço, que na coleta é identificado como ServiceName. 

O **"ResourceID"** representa o identificador único de tela. Este dado é utilizado quando desejar uma consulta mais precisa de um processo, porém por não ser obrigatório, se não for informado durante a coleta, essa informação não existirá nos dados coletados.

Preencha na **"Descrição da Tela"** o nome da funcionalidade coletada.

O campo **"Tipo"** é utilizado para realizar uma pesquisa por apenas um tipo de coleta, sendo Analítico ou Consolidado. 

Por meio da **"Pesquisa Evento"**, você poderá inserir descrições de eventos ao clicar no botão **"Adicionar"**, assim será exibido um pop-up onde pode pesquisar por eventos e o resultado da consulta será listado por uma estrutura em árvore, baseado na estrutura da criação do Evento (Modulo@Processo@Rotina). Ao selecionar um item da estrutura com um duplo clique, este será criado na estrutura da busca, podendo incorporar as informações do evento com as informações dos Filtros rápidos para refinar a pesquisa. Você poderá escolher vários eventos.

---

Após o retorno da busca, a tela irá apresentar uma grade com os dados das coletas realizadas e você poderá analisar uma coleta específica ou realizar comparações entre elas das seguintes maneiras:

### Detalhar coleta da Telemetria

Para detalhar uma coleta específica, você poderá clicar no botão **"Detalhar"** ou clicar duas vezes na linha da coleta desejada, assim será apresentada a tela de Detalhamento por Evento ou Processo.

- **Detalhe na coleta de Visão por Evento:** A tela Detalhamento Evento mostra as informações do item selecionado na Visão por Evento, sendo que só é possível detalhar apenas uma coleta de telemetria por vez.![Imagem 4: Detalhe na coleta de Visão por Evento: A tela Detalhamento Evento mostra as informações do item selecionado na Visão…](https://ajuda.sankhya.com.br/hc/article_attachments/4415534461975)
- **Detalhe na coleta de Visão por Processo:** A tela de Detalhamento Processo exibe a coleta selecionada com todas as informações, dependendo do seu tipo, por exemplo, coletas do tipo analíticas trazem apenas a informação do tempo total do processo. Já as coletas do tipo consolidadas, retornam as informações da quantidade de chamadas, tempo total, tempo médio, maior tempo e menor tempo. A montagem da grade é feita pelo Evento pai e abaixo seus eventos filhos, há uma opção para minimizar os eventos clicando na seta ao lado do nome do evento inicial.![Imagem 5: Detalhe na coleta de Visão por Processo: A tela de Detalhamento Processo exibe a coleta selecionada com todas as…](https://ajuda.sankhya.com.br/hc/article_attachments/4415534656279)

### Comparar Itens da Telemetria

Esta opção permite comparar duas coletas distintas, que poderão ser ambas analíticas, ambas consolidadas ou uma consolidada e uma analítica.

A seleção das coletas que desejar comparar pode ser realizada de duas formas; selecionando uma coleta na grade e clicando no botão **"Comparar"**, será apresentado dois novos botões com os numerais um e dois, assim você poderá selecionar outra coleta que desejar, clicando na linha e no botão Comparar novamente. Outra opção é selecionar as linhas da grade utilizando o botão **"Ctrl"** do seu teclado, para isso, basta segurar e clicar nas coletas desejadas e depois no botão Comparar.

Esta comparação pode ser feita das seguintes formas:

- **Comparar Itens da Telemetria na Visão por Evento:** A comparação pela Visão por Evento irá utilizar as mesmas informações da tela de Detalhamento, porém irá apresentar uma coluna com a diferença entre os itens comparados.

![Imagem 6: Comparar Itens da Telemetria na Visão por Evento: A comparação pela Visão por Evento irá utilizar as mesmas informações…](https://ajuda.sankhya.com.br/hc/article_attachments/4415542385559)

- **Comparar Itens da Telemetria na Visão por Processo:** A comparação é utilizada para analisar duas coletas na mesma tela, onde serão exibidas as mesmas informações da tela de Detalhamento, seguindo as mesmas regras conforme o seu tipo de coleta.

![Imagem 7: Comparar Itens da Telemetria na Visão por Processo: A comparação é utilizada para analisar duas coletas na mesma tela,…](https://ajuda.sankhya.com.br/hc/article_attachments/4415542399511)

### Botões da tela

O botão ![Imagem 8: O botão "Mostrar/esconder painel de filtros " , permite ocultar o Painel dos F iltros, que após a consulta pode ser…](https://ajuda.sankhya.com.br/hc/article_attachments/16808010742167) **"Mostrar/esconder painel de filtros"**, permite ocultar o Painel dos Filtros, que após a consulta pode ser interessante para caso queira visualizar melhor todos os campos da tela. Para exibir novamente basta clicar nele e o Painel de Filtros voltará à tela.

Por meio do botão**![Imagem 9: Por meio do botão "Configurar grade" , você poderá c onfigurar os campos que deseja que apareça na grade.](https://ajuda.sankhya.com.br/hc/article_attachments/16808010747159) "Configurar grade"**, você poderá configurar os campos que deseja que apareça na grade.

No botão**"Visão por Evento"** é apresentado o resultado da pesquisa com a grade baseada nas tabelas de Eventos.

O botão **"Visão por Processo"** mostra o resultado da pesquisa com a grade baseada nas tabelas de Processo.

As informações **"Analítico"** e **"Consolidado"** servem para especificar o significado de cada tipo de coleta. Basta clicar em cima de cada uma para saber mais sobre esse tipo. 

![Imagem 10: A legenda Analítico e Consolidado são exibidas dinamicamente nas telas Detalhamento por Evento ou Comparação. No caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16808015835159) A legenda Analítico e Consolidado são exibidas dinamicamente nas telas Detalhamento por Evento ou Comparação. No caso da Comparação, se selecionada uma coleta analítica e outra consolidada, exibirá os dois campos, se o tipo for o mesmo para ambos registros, exibirá somente o campo de acordo com o tipo da(s) coleta(s).

### Parâmetros que influenciam esta rotina

A Telemetria de Processos possui alguns parâmetros que são necessários para o seu funcionamento. São eles:

- **HABCOLTELPRO - Habilitar coleta da Telemetria de Processos?** Habilita a coleta de eventos parametrizados no código fonte. Por default esse parâmetro é definido como verdadeiro;
- **TELPROQTDDIAS - Manter dados analíticos durante quantos dias?** Define a quantidade de dias limite, em que os dados coletados analíticos devem permanecer até sua consolidação e o processo de limpeza de dados ser executado. Por padrão, está definido em 7 dias.
- **TELPROQTDMESES - Manter dados consolidados durante quantos meses?** Define a quantidade de meses limite, em que os dados consolidados devem permanecer até o processo de limpeza de dados ser executado. Por padrão, está definido em 6 meses.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4415478433047-Telemetria-de-Processos#top)
