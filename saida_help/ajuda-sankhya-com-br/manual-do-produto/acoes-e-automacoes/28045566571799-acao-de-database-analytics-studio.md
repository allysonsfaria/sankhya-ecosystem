---
id: "28045566571799"
titulo: "Ação de Database - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28045566571799-A%C3%A7%C3%A3o-de-Database-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Ações e automações"
atualizado_em: "2026-09-23T17:35:14Z"
rotulos: ["SQL", "Configuração", "Analytics Studio", "DML", "Ação de Database"]
---

# Ação de Database - Analytics Studio

No [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio), as Ações de Database permitem executar diretamente operações como INSERT, UPDATE e DELETE nos registros do banco de dados, usando componentes como labels, tabelas e listas. 

![Imagem 1: No Analytics Studio , as Ações de Database permitem executar diretamente operações como INSERT, UPDATE e DELETE nos…](https://ajuda.sankhya.com.br/hc/article_attachments/28045566568855)

### Como Adicionar uma Ação de Database

![Imagem 2: No componente desejado, acesse a área de "Interações" .](https://ajuda.sankhya.com.br/hc/article_attachments/28046984171415) No componente desejado, acesse a área de **"Interações"**.

![Imagem 3: Selecione a opção "Ação de Database" . Escolha entre c riar uma nova ação ou s elecionar uma ação de database já…](https://ajuda.sankhya.com.br/hc/article_attachments/28046984178455) Selecione a opção **"Ação de Database"**. Escolha entre criar uma nova ação ou selecionar uma ação de database já existente.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=3KLc-fhLFEg)

### Configuração da Ação de Database

Ao configurar uma ação de database, a interface exibirá os seguintes elementos:

- **Dicionário de Dados:** no lado direito, será exibido o dicionário com todas as tabelas e colunas disponíveis para manipulação via INSERTS, UPDATES e DELETES.
- **Variáveis de Filtro e Input:** todas as variáveis do contexto da tela e variáveis de input configuradas estarão disponíveis. Isso permite o uso de informações dinâmicas, como filtros aplicados ou dados inseridos pelo usuário, diretamente nas suas ações de database. Para mais detalhes sobre as variáveis, acesse o artigo [VIEW de SQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/28074561568023-VIEW-de-SQL).

### Teste de Script

Depois de configurar sua ação de database, é possível testar os scripts para garantir que estão funcionando conforme o esperado. Isso envolve testar o DML (Data Manipulation Language) e verificar se os comandos INSERT, UPDATE ou DELETE estão sendo executados corretamente. Após o teste, confirme a configuração da ação e o script será ativado nas interações do componente.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=gSTYUQ46u3M)

### Exemplos

**Deletando Vendedores**

Neste exemplo, será configurada uma ação de database para deletar vendedores diretamente de uma lista.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=qITuFPUdL5Q)

- **Componente:** lista de vendedores.
- **Interação:** ao clicar em um botão **"Excluir"**, a ação de database executa o seguinte script:

```
DELETE FROM CAD_1026 WHERE ID = :ID_VENDEDOR
```

No script acima, :ID\_VENDEDOR é uma variável que captura o ID do vendedor selecionado na lista. O sistema de variáveis do Analytics Studio garantirá que o delete seja aplicado corretamente.

#### Criando Vendedores a partir de Inputs

Neste caso, serão adicionados os inputs na tela (por exemplo, para nome, cidade, e salário do vendedor). Ao clicar no botão **"Salvar"**, a ação de database executará um INSERT com base nos valores desses inputs.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=05Irz4jpX-k)

- **Componente:** Inputs de nome, cidade e salário.
- **Interação:** ao clicar no botão **"Salvar"**, a ação de database executa o script:

```
INSERT INTO CAD_1026 (ID, DESCR, FOTO)

SELECT (MAX(ID)+1) AS ID, :INPUT__310, :INPUT__311

FROM CAD_1026
```

As variáveis :INPUT\_310 e :INPUT\_311 são preenchidas pelos valores dos inputs na tela.

#### Atualização de Tarefa

Neste exemplo, tem-se uma lista de tarefas, e cada tarefa possui um botão de **"Concluir"**. Ao clicar nesse botão, um UPDATE será feito para marcar a tarefa como concluída.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=4n3Q2nibFHo)

- **Componente:** Lista de tarefas com um botão Concluir.
- **Interação:** Ao clicar no botão Concluir, a ação de database executa o seguinte script:

```
UPDATE CAD_1024 SET ID_STATUS = 2 WHERE ID = :ID_TAREFAS
```

A variável :ID\_TAREFA é obtida a partir da linha selecionada na lista.

#### Sequência de DML

Em uma ação de database, é possível múltiplos comandos DML. Por exemplo, ao trabalhar com uma lista de tarefas, pode-se criar uma ação de database para marcar uma tarefa como concluída e, ao mesmo tempo, registrar essa tarefa na lista de tarefas concluídas.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=bEaR7p4pjD0)

- **Componente:** uma lista com as tarefas e outra lista com as tarefas concluídas.
- **Interação:** ao clicar no botão **"Concluir"**, a ação de database executa os seguintes scripts:

#### UPDATE

Primeiro, o status da tarefa é atualizado para **"Concluída"** na lista original de tarefas.

```
UPDATE CAD_1024 SET ID_STATUS = 2 WHERE ID = :ID_TAREFAS
```

Aqui, :ID\_TAREFA captura o ID da tarefa que está sendo concluída. A coluna STATUS da tarefa é alterada para Concluída.

#### INSERT

Em seguida, a tarefa é registrada na lista de tarefas concluídas.

```
INSERT INTO CAD_1050 (ID, DESCR)

SELECT ID, DESCR, FROM CAD_1024 WHERE ID = :ID_TAREFAS
```

As informações da tarefa são copiadas da lista original de tarefas. A variável :ID\_TAREFAS garante que a tarefa correta seja copiada para a lista de tarefas concluídas.

Assim, pode-se configurar a sequência de scripts em uma única ação de database, que serão executados na ordem definida.

---

![Imagem 4: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28156489363223) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
