---
id: "42430411139479"
titulo: "Como identificar problemas na Importação de Base de Conhecimento pelo Airflow"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430411139479-Como-identificar-problemas-na-Importa%C3%A7%C3%A3o-de-Base-de-Conhecimento-pelo-Airflow"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:03:56Z"
rotulos: ["sync_hc", "neppo", "neppo_857999671", "sync_hash_7e0a3c0498d8"]
---

# Como identificar problemas na Importação de Base de Conhecimento pelo Airflow

## Visão Geral

Este documento tem como finalidade auxiliar na identificação de problemas ocasionados durante o processo de importação de base de conhecimento.

Para verificação é necessário ter acesso ao airflow do ambiente que a base foi importada:

Prod:

## Sobre o Apache Airflow

O Apache Airflow é uma plataforma de **orquestração de workflows** usada para criar, agendar e monitorar pipelines de dados ou processos automatizados. Nele podemos definir fluxos de trabalho como código, organizando tarefas em estruturas chamadas DAGs (Directed Acyclic Graphs). Ele gerencia a execução dessas tarefas com base em dependências, agendamento e regras configuráveis.

Na tela inicial é possivel ver todas as dags e suas execuções:

![Imagem 1: Na tela inicial é possivel ver todas as dags e suas execuções:](https://ajuda.sankhya.com.br/hc/article_attachments/42639679881879)

Em casos de manutenção e erro de execução é possível saber quais DAG’s tem dependencias: no menu Browse >> DAG Dependencies

![Imagem 2: Em casos de manutenção e erro de execução é possível saber quais DAG’s tem dependencias: no menu Browse >> DAG…](https://ajuda.sankhya.com.br/hc/article_attachments/42639694808215)

## Acessando Logs

Para verificar os logs nos durante o processo de importação de base de conhecimento clique sobre o nome da DAG etl\_knowledge\_customer.

Quando a tela da dag for exibida, selecione a ultima execução, como mostra na figura abaixo na primeira seta a esquerda.

![Imagem 3: Quando a tela da dag for exibida, selecione a ultima execução, como mostra na figura abaixo na primeira seta a esquerda.](https://ajuda.sankhya.com.br/hc/article_attachments/42639668716311)

Nesta tela você consegue ver o status da dag, horários de execuções e o que chegou da api (que recebe do importador de base de conhecimento)

Se você selecionar o menu Graph, uma tela com os operadores abrirá como mostra abaixo:

![Imagem 4: Se você selecionar o menu Graph, uma tela com os operadores abrirá como mostra abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639695367447)

Depois disto basta selecionar o operador desejado que pretende ver o log dele e clicar no menu Logs. (Neste caso veremos o log de sucesso para saber quantos contextos foram interpretados.

### Sucesso na importação da base de conhecimento

Quando o arquivo é importado corretamente, o nome do index onde está sendo salvo o contexto, a quantidade de contextos identificados e outros detalhes, são exibidos ao final da mensagem da mensagem de log pela dag etl\_knowledge\_customer, conforme mostra na figura abaixo:

![Imagem 5: Quando o arquivo é importado corretamente, o nome do index onde está sendo salvo o contexto, a quantidade de contextos…](https://ajuda.sankhya.com.br/hc/article_attachments/42639701419799)

E assim também você pode repetir o processo e entrar na dag ia\_rag\_embeddings\_elastic para saber a quantidade de vetores gerados e o nome do index da base de conhecimento que foi gerada:

![Imagem 6: E assim também você pode repetir o processo e entrar na dag ia_rag_embeddings_elastic para saber a quantidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/42639701764887)

### Casos de Erro:

Dica: Para saber se a dag executou com falhas **não confie apenas na cor exibida** (verde e vermelho), entre no log para saber se a execução apresenta falhas.

Para selecionar os últimos erros que aconteceram em uma dag existem filtros na parte superior que podem ajudar:

![Imagem 7: Para selecionar os últimos erros que aconteceram em uma dag existem filtros na parte superior que podem ajudar:](https://ajuda.sankhya.com.br/hc/article_attachments/42639715125399)

Estes são exemplos de erros recorrentes mais comuns de acontecerem:

- Arquivo sem permissão:

![Imagem 8: Arquivo sem permissão:](https://ajuda.sankhya.com.br/hc/article_attachments/42639696565783)

- Arquivo sem extensão:

![Imagem 9: Arquivo sem extensão:](https://ajuda.sankhya.com.br/hc/article_attachments/42639715876375)![Imagem 10: Arquivo sem extensão:](https://ajuda.sankhya.com.br/hc/article_attachments/42639670554007)

E outros erros comuns são: Erro para ler os dados do arquivos e/ou não foi possível identificar as quebras e/ou o contexto do arquivo e quando o arquivo excede número de linhas que é de 10.000 para contextos embeddings.
