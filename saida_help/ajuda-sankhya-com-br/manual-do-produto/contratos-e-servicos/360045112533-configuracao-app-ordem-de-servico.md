---
id: "360045112533"
titulo: "Configuração App Ordem de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112533-Configura%C3%A7%C3%A3o-App-Ordem-de-Servi%C3%A7o"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:04:59Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Layout", "Contratos e Serviços", "Ordem de Serviço", "br.com.sankhya.os.conf.configappos", "Configuração App Ordem de Serviço manual", "Sankhya Tasks", "Configuração do App Ordem de Serviço"]
---

# Configuração App Ordem de Serviço

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311229370263) Módulo: Contratos e Serviços > Avançado
```

---

Essa tela possibilita que você faça as configurações necessárias para o lançamento/apontamento de OS no Sankhya Tasks. Aqui temos recursos para configurar a apresentação dos campos da OS no aplicativo de forma a otimizar as tarefas realizadas, configurando os campos que ficarão visíveis, salvar último valor, valor padrão, etc.

![Imagem 2: Essa tela possibilita que você faça as configurações necessárias para o lançamento/apontamento de OS no Sankhya Tasks .…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007251901)

Nessa tela, temos duas abas onde se configuram os campos que serão apresentados no Sankhya Tasks e uma aba para definir o intervalo entre as tarefas.

Na **"Layout Cabeçalho"** são configurados os campos do cabeçalho da OS. Já na aba **"Layout Itens"** são configurados os campos da Sub-OS. Em ambas as abas, você deve configurar os seguintes campos:

No campo **"Ordem"** defina a ordem em que o campo deverá aparecer no app (sempre respeitando a lógica de, primeiro os campos do cabeçalho e, em seguida, os referentes aos itens).

No **"Campo"** teremos o nome do campo no banco de dados. Utilize o botão **"Selecionar"** para escolher o campo desejado.

Informe no campo **"Descrição"** o nome do campo que deverá aparecer no aplicativo.

Insira no campo **"Valor padrão"** o valor padrão que será utilizado ao criar uma OS ou Sub-OS.

Efetuando a marcação **"Salvar último valor"** será armazenado o último valor do campo e ele será reutilizado ao criar uma nova OS ou Sub-OS.

**Observação:** a marcação acima sobrescreve a informação do campo Valor padrão.

A marcação **"Apresenta no lançamento de nova OS"** quando realizada, apresentará o campo ao criar uma nova OS ou Sub-OS.

Selecionando a marcação **"Apresenta na edição de** **OS"**, fará com que o campo seja apresentado ao editar uma OS ou Sub-OS.

**Nota:** as duas marcações acima deverão ser configuradas por um consultor Sankhya, de acordo com a regra de negócio de quem utiliza o app.

Quando a marcação **"Somente leitura"** estiver habilitada, não será permitida a alteração do campo, apenas sua visualização.

O campo **"Ligação com cadastro"** será preenchido pelo sistema quando for selecionado um campo que possui ligação com um cadastro; ele é utilizado internamente para saber qual tabela será sincronizada com o aplicativo. Durante a sincronização, é feita a análise se existe um dos campos, **"SYNCAPPOS"** ou **"AD\_SYNCAPPOS"**; caso exista um, serão sincronizados todos os registros dessa ligação cujo campo esteja com o valor **"S"**.

Caso você não queira criar um dos campos citados no item anterior, poderá configurar uma expressão através do botão **"Alterar"**, apresentada no campo **"Filtro para importação do cadastro"**. Essa expressão só será utilizada quando não existirem um dos campos SYNCAPPOS ou AD\_SYNCAPPOS na ligação com o cadastro. Caso a expressão seja vazia, nada será sincronizado.

**Observação:** nessa tela, temos a possibilidade de configurar tanto o cabeçalho quanto o item da OS, podendo contar tanto com campos nativos do sistema quanto com os campos adicionais (TCSOSE e TCSITE).

Na **"Configurações"**, temos a marcação **"Apresentar o intervalo da tarefa"** que, ao ser selecionada, define que será utilizado o intervalo das tarefas:

![Imagem 3: Na "Configurações" , temos a marcação "Apresentar o intervalo da tarefa" que, ao ser selecionada, define que será…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007252701)

**Nota:** quando essa marcação estiver habilitada, no aplicativo será liberado o campo **"Intervalo"** no apontamento das tarefas.

Para que as pausas não sejam perdidas durante a sincronização das tarefas, foi criado o campo TCSITE.DHPAUSEAPP, que guarda a data e hora que foi realizada a pausa da tarefa. O aplicativo utilizará esse campo quando a tarefa for finalizada para calcular o intervalo. Como os campos de intervalo **"Hora Inicial"** e **"Final"** não armazenam os segundos, o aplicativo utiliza os segundos somente para indicar o andamento das tarefas.
