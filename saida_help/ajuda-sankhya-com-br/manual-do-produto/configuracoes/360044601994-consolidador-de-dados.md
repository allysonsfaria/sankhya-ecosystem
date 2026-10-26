---
id: "360044601994"
titulo: "Consolidador de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:52:10Z"
rotulos: ["manual", "SQL", "Configuração", "Relatórios", "Dashboards", "Agendamento", "br.com.sankhya.core.cfg.consolidador.dados", "Consolidador de Dados manual", "Consolidador de Dados: Configuração e Execução"]
---

# Consolidador de Dados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310802720151) Módulo: Configurações > Avançado
```

---

Esta tela permite a consolidação de informações que serão utilizadas como fonte de dados para a criação de dashboards, possibilitando assim um melhor desempenho na visualização dos mesmos.

Inicialmente, informe no campo **"Código"** a chave da consolidação no sistema; esta numeração será responsável por identificá-la em todas as rotinas em que ela estiver presente. Você pode preencher esse campo de forma manual ou automática.

Depois, através do campo **"Descrição"** escreva o nome da consolidação que está sendo cadastrada.

Quando a marcação **"Ativo"** estiver habilitada, indicará que a consolidação está em uso e poderá ser empregada no momento da execução.

**Observação:** para que esta tela seja disponibilizada para utilização no Sankhya-Om, deve-se possuir na licença de uso, o produto **"30616 - EDITOR DE DASHBOARD/W"**e para utilização no Jiva Evo é necessário possuir na licença de uso, o produto **"20495 - ANÁLISES PARA DASHBOARDS/W"**.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#abageral)                                                             [Aba Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#abaconsulta)       

[Aba Execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#abaexecuo)                                                     [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#botooutrasopes...)

## Aba Geral

Efetue nesta aba as configurações gerais a respeito da consolidação de dados.

![Imagem 2: Efetue nesta aba as configurações gerais a respeito da consolidação de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/4406034155927)

No campo **"Nome da Tabela no Banco de Dados"** informe a descrição que o sistema irá criar para a nova consolidação.

**Nota:** será acrescentado o prefixo **"CND\_"** ao nome da tabela informado.

Ao lado do campo Nome da Tabela no Banco de Dados, tem-se o botão **"Copiar para área de transferência"** que, ao clicar neste, o sistema permitirá que o texto inserido no referido campo possa ser replicado.

Utilize o campo **"Observação"** para descrever informações a respeito da consolidação.

O campo **"Início da Consolidação"** irá determinar a forma do período inicial da consolidação. São apresentadas as seguintes opções:

- **Fixa:** Ao selecionar esta opção, será exibido o campo **"Data Inicial"**, na qual você deverá informar uma data fixa para o início da consolidação
- **Variável:** Ao informar essa opção, será apresentado o campo **"Qtd. Meses a Consolidar"**, onde você indicará o período em meses que ocorrerá a consolidação.

**Nota:** este campo tem como padrão de preenchimento a opção Fixa.

A opção **"Qtd. Meses a Retroagir"** tem como funcionalidade informar ao sistema o período em meses que os dados serão mantidos atualizados. Isso significa que após a primeira execução o sistema sempre irá considerar esse período de tempo para atualização dos dados.

No campo **"Agrupamento"** selecione a forma de processamento da query criada na aba [Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#abaconsulta), conforme as seguintes opções:

- **Único:** o processamento será executado em uma única vez;
- **Diário:** o processamento será realizado em períodos diários;
- **Mensal:** o processamento será realizado em períodos mensais.

**Observação:** este campo tem como padrão de preenchimento a opção Único.

Através do campo **"Tipo de gatilho"**, defina a forma como será tratada a sequência de execução da consolidação. Temos duas opções:

- **Intervalo de tempo:** Pode-se definir um intervalo homogêneo de segundos, minutos ou horas para ser executada a consolidação;
- **Expressão CRON:** Permite um ajuste mais fino do intervalo de tempo, possibilitando a inserção manual no campo uma expressão do cron.

O campo **"Expressão de gatilho"** é preenchido na medida em que os intervalos dispostos em forma de lista de opções (segundos, minutos, horas, dias, meses, dias da semana) forem definidos.

Ainda sobre a Lista de Opções, temos as seguintes considerações:

1. Cada lista de opções equivale a um dos caracteres gerados no campo Expressão de gatilho, ao passo que qualquer modificação em uma das listas ou suas opções, irá refletir em uma atualização no referido campo;
2. O caractere **"\*"** (asterisco) significa "todos". No caso, uma lista vazia gera um asterisco e significa que a consolidação irá rodar em todos os valores para aquela determinada lista de opções;
3. Pode-se especificar um dia ou o dia da semana para a execução, mas não os dois simultaneamente, pois tal configuração poderia ser inconsistente;
4. O caractere "?" (interrogação) significa **"não importa"**. No caso, utilizado para dias ou dias da semana. Caso seja selecionado um ou mais dias para executar a consolidação, obrigatoriamente o dia da semana será preenchido com interrogação no campo Expressão do gatilho. Caso sejam selecionados dias da semana, os dias serão configurados com interrogação no campo Expressão do gatilho;

Além disso, será exibido nos campos **"Cód. Usuário"** e **"Dt. Alteração"** o usuário responsável pela inclusão da consolidação; bem como o usuário, a data e o horário da última alteração realizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#top)

## Aba Consulta

A consulta necessita ser uma expressão SQL que retorne os campos que serão consolidados. Sendo que, a query deverá conter o campo **"DTREF"** (Data de Referência). Os parâmetros disponíveis no link **"Inserir parâmetro..."** podem ser utilizados para compor a consulta SQL.

![Imagem 3: A consulta necessita ser uma expressão SQL que retorne os campos que serão consolidados. Sendo que, a query deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/4406027191447)

Através do botão ![Imagem 4: Através do botão "Fonte de Dados" execute a consulta utilizando outras fontes de dados, previamente configuradas.](https://ajuda.sankhya.com.br/hc/article_attachments/4406033658263) **"Fonte de Dados"** execute a consulta utilizando outras fontes de dados, previamente configuradas.

O botão  **"Executar"** é responsável pela realização da consulta SQL.

Localizado no lado superior direito da tela, o link **"Inserir parâmetro..."** será utilizado para inserir na query as varáveis de contexto. Temos os seguintes valores:

- **Período inicial:** Irá adicionar o trecho ":PERIODO.INI";
- **Período final:** Tem-se a inclusão do trecho ":PERIODO.FIN".

Sendo que, é necessário adicionar as variáveis onde o cursor estiver posicionado na query. Vejamos abaixo um exemplo de filtro utilizando uma constante:

SELECT XTPO

FROM XTPO

 WHERE DATAXTPO >= {:PERINI} AND

  DATAXTPO <= {:PERFIN}

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#top)

## Aba Execução

Nesta aba, você poderá visualizar as informações pertinentes a última execução da consolidação de dados.

![Imagem 5: Nesta aba, você poderá visualizar as informações pertinentes a última execução da consolidação de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/4406034228247)

O campo **"Dt. Últ. Execução"** apresentará a data e a hora da última execução da consolidação.

Por meio do campo **"Tempo de Processamento (seg.)"**, pode-se visualizar o prazo (em segundos) que o sistema levou para executar a última consolidação.

No campo **"Status"** temos o status da última execução da consolidação. Serão apresentados os seguintes status:

- Em execução;
- Erro.

**Nota:** quando a execução da consolidação ocorrer sem erros, o campo Dt. Últ. Execução será preenchido.

Será exibido no campo **"Log Erro"** o trecho do log que ocasionou o erro na execução da consolidação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#top)

## Botão Outras Opções...

No botão ![Imagem 6: No botão "Outras Opções..." , localizado na parte superior direita da tela, temos as seguintes opções:](https://ajuda.sankhya.com.br/hc/article_attachments/16190752672791) **"Outras Opções..."**, localizado na parte superior direita da tela, temos as seguintes opções:

**Executar consolidação agora**

Esta opção quando acionada, realiza a execução da consolidação naquele determinado momento.

**Observação:** para visualizar a data e hora da última execução na aba Execução, é necessário acionar o botão **"Atualizar"** visto que os campos não atualizam automaticamente.

---

**Consolidações em andamento**

Ao acionar esta opção, tem-se a exibição de um pop-up de mesma nomenclatura contendo as informações pertinentes as consolidações que estão sendo executadas.

![Imagem 7: Ao acionar esta opção, tem-se a exibição de um pop-up de mesma nomenclatura contendo as informações pertinentes as…](https://ajuda.sankhya.com.br/hc/article_attachments/4406034243863)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994-Consolidador-de-Dados#top)

![Imagem 8: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16190769381271) Acesse também:

[Construtor de Dashboards](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605574-Construtor-de-Dashboards)

[Ações Agendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas)
