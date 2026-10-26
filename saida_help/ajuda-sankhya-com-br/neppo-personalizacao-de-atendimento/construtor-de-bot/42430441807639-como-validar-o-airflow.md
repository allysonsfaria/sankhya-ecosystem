---
id: "42430441807639"
titulo: "Como validar o Airflow"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430441807639-Como-validar-o-Airflow"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:08:25Z"
rotulos: ["sync_hc", "neppo", "neppo_857999985", "sync_hash_c31055659fef"]
---

# Como validar o Airflow

## Visão Geral

Este documento tem como finalidade orientar como fazer a validação das principais dags do Airflow em casos onde os serviços do Airflow são reiniciados.

Para validar o airflow é necessário ter acesso ao ambiente:

Prod:

PreProd:

Para validar o ambiente do airflow verifique se o ambiente do airflow está acessivel:

![Imagem 1: Para validar o ambiente do airflow verifique se o ambiente do airflow está acessivel:](https://ajuda.sankhya.com.br/hc/article_attachments/42639877075351)

## Alerta ERRO que deve ser ignorado:

Obs: Atualmente estamos com um erro sendo exibido na tela, **que não impacta no funcionamento** e podem ignorar. Este erro já está sendo resolvido, e este é referente a importação de uma lib no repositorio de dags:

![Imagem 2: Obs: Atualmente estamos com um erro sendo exibido na tela, que não impacta no funcionamento e podem ignorar. Este erro…](https://ajuda.sankhya.com.br/hc/article_attachments/42639907260055)

## Executar a Importação da base de conhecimento para validação dos serviços consumidos pelas dags

O processo de importação de base de conhecimento faz a conexão com todos os serviços usados também por outras dags, portanto basta validar por este processo para saber se os demais também irão funcionar.

Para executar a importação entre no ambiente desejado de: atendimento (Prod) ou Botian (PreProd)

Entre no “Studio (Construtor de Bot)”:

![Imagem 3: Entre no “Studio (Construtor de Bot)”:](https://ajuda.sankhya.com.br/hc/article_attachments/42639846469911)

Clique no menu: “Configurações” e logo em seguida no card: “Importar Base de Conhecimento” clique em: “Acessar”

![Imagem 4: Clique no menu: “Configurações” e logo em seguida no card: “Importar Base de Conhecimento” clique em: “Acessar”](https://ajuda.sankhya.com.br/hc/article_attachments/42639893111319)

E execute a importação de uma das bases de conhecimento já cadastradas (pode usar do: “suporte\_eureciclo” exibida abaixo). Para executar só clicar uma vez no play.

![Imagem 5: E execute a importação de uma das bases de conhecimento já cadastradas (pode usar do: “suporte_eureciclo” exibida…](https://ajuda.sankhya.com.br/hc/article_attachments/42639866064023)

Você verá que o status irá modificar para “Em Progresso”:

![Imagem 6: Você verá que o status irá modificar para “Em Progresso”:](https://ajuda.sankhya.com.br/hc/article_attachments/42639847133719)

A validação das dags pode ser feita de duas formas: pelo bot verificando se o status da ultima importação está como finalizado e depois executando o bot que usa esta base de conhecimento para saber se está respondendo:

![Imagem 7: A validação das dags pode ser feita de duas formas: pelo bot verificando se o status da ultima importação está como…](https://ajuda.sankhya.com.br/hc/article_attachments/42639893859863)

**Ou** pela validação das dags no ambiente do airflow, como mostra no passo a passo abaixo.

## Passo a passo para validar execução de dags pelo ambiente do Airflow

Entre no airflow para ver a execução das dags e verificar os logs, para isto, clique sobre o nome da dag: “etl\_auto\_chunk\_rag\_provisioning”

![Imagem 8: Entre no airflow para ver a execução das dags e verificar os logs, para isto, clique sobre o nome da dag:…](https://ajuda.sankhya.com.br/hc/article_attachments/42639879427095)

Clique na execução, no menu “Graph” e depois verifique se os operadores finalizaram com sucesso:

![Imagem 9: Clique na execução, no menu “Graph” e depois verifique se os operadores finalizaram com sucesso:](https://ajuda.sankhya.com.br/hc/article_attachments/42639864201239)

Ou se quiser acompanhar o operador em especifico basta clicar no operador e o menu “Logs” que será habilitado:

![Imagem 10: Ou se quiser acompanhar o operador em especifico basta clicar no operador e o menu “Logs” que será habilitado:](https://ajuda.sankhya.com.br/hc/article_attachments/42639867665943)

E clicando em “Logs” é possível ver o log da execução:

![Imagem 11: E clicando em “Logs” é possível ver o log da execução:](https://ajuda.sankhya.com.br/hc/article_attachments/42639909379863)

E a mesma coisa na dag “ia\_rag\_embeddings\_elastic”, repita o mesmo processo para conferir os operadores desta dag que é executada sequencialmente automaticamente depois:

![Imagem 12: E a mesma coisa na dag “ia_rag_embeddings_elastic”, repita o mesmo processo para conferir os operadores desta dag que é…](https://ajuda.sankhya.com.br/hc/article_attachments/42639882117015)

E verifique no Logs se terminou com sucesso:

![Imagem 13: E verifique no Logs se terminou com sucesso:](https://ajuda.sankhya.com.br/hc/article_attachments/42639909839127)
