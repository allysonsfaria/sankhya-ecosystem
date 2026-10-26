---
id: "9222045960087"
titulo: "Controle de Qualidade dos PA’s"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:56:42Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Produção", "Ciclo de Controle de Qualidade", "Controle de Qualidade dos PA’s", "Configuração Inicial", "Controle de Qualidade Integrado", "Execução do Ciclo de Qualidade", "Qualidade"]
---

# Controle de Qualidade dos PA’s

Este processo representa a execução do Controle de Qualidade dos Produtos Acabados (PA's) numa [Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o). Ele também é denominado por Controle de Qualidade Embarcado ao Processo Produtivo, pois a execução do controle de qualidade é representada por atividades no roteiro de produção do Produto Acabado.

Neste artigo trataremos dos seguintes tópicos:

- [Configurações gerais](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#Configura%C3%A7%C3%B5esgerais)
- [Cadastro do processo de controle de qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#Cadastrodoprocessodecontroledequalidade)
- [Vinculando o produto com o Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#VinculandooprodutocomoProcessoprodutivo)
- [Publicação do Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#Publica%C3%A7%C3%A3odoProcessoProdutivo)
- [Iniciando o Ciclo de controle de qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#IniciandooCiclodecontroledequalidade)

---

### Configurações gerais

Para o funcionamento do processo de Controle de Qualidade dos PA’s, é necessário realizar as configurações a seguir:

Primeiramente, defina o **"Tipo de amostra"** que será utilizado pelo Produto Acabado e que você deseja executar o controle de qualidade. Esse cadastro é realizado na tela [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013).

![Imagem 1: Primeiramente, defina o "Tipo de amostra" que será utilizado pelo Produto Acabado e que você deseja executar o controle…](https://ajuda.sankhya.com.br/hc/article_attachments/9222091688471)

Depois, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) você deve realizar os procedimentos abaixo:

**1)** Inicialmente, na aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), selecione no campo **"Controlar por"**, a opção **"Número de lote"**. Em seguida, na sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abaestoque), acione a marcação **"Usa Status de Lote"**.

![Imagem 2: 1) Inicialmente, na aba Medidas e estoque , sub-aba Controle Adicional , selecione no campo "Controlar por" , a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/9222153874583)

**Observação:** para realizar esta configuração, é necessário ligar o parâmetro **"Utiliza Status do Lote? - UTILSTATUSLOTE"**

**2)** Informe o **"Tipo Amostra"** que será utilizado para o produto em questão, na aba [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abatiposdeamostra):

![Imagem 3: 2) Informe o "Tipo Amostra" que será utilizado para o produto em questão, na aba Tipos de Amostra :](https://ajuda.sankhya.com.br/hc/article_attachments/9222216261015)

Agora, na tela [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593), cadastre o padrão de classificação que será a representação sistêmica do ensaio (análise) ao qual o produto deve ser submetido durante o processo de Controle de Qualidade. Ao Padrão de Classificação, são relacionadas as [Características Analisáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595014-Caracter%C3%ADsticas-Analis%C3%A1veis) que devem ser consideradas no ensaio, bem como o intervalo de aceitação de cada uma delas para o produto.

[GIF animado: Imagem 4: Agora, na tela Padrões de Classificação , cadastre o padrão de classificação que será a representação sistêmica do…](https://ajuda.sankhya.com.br/hc/article_attachments/9238728406807)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#top)

### Cadastro do processo de controle de qualidade

Na tela [Processo Produtivo-Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), cadastre primeiramente um processo de controle de qualidade. Para isso, acione o botão ![Imagem 5: Na tela Processo Produtivo-Nova , cadastre primeiramente um processo de controle de qualidade. Para isso, acione o…](https://ajuda.sankhya.com.br/hc/article_attachments/16647300942743) **"Cadastrar Processo Produtivo [F8]"** e preencha os campos obrigatórios:

![Imagem 6: Na tela Processo Produtivo-Nova , cadastre primeiramente um processo de controle de qualidade. Para isso, acione o…](https://ajuda.sankhya.com.br/hc/article_attachments/9238845608855)

Em seguida, por meio do botão ![Imagem 7: Em seguida, por meio do botão "Outras Opções..." , opção "Ciclos de Controle de Qualidade" , cadastre os ciclos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16647339389207) **"Outras Opções..."**, opção **"Ciclos de Controle de Qualidade"**, cadastre os ciclos de controle de qualidade que serão executados durante a Ordem de Produção do processo em questão.

![Imagem 8: Em seguida, por meio do botão "Outras Opções..." , opção "Ciclos de Controle de Qualidade" , cadastre os ciclos de…](https://ajuda.sankhya.com.br/hc/article_attachments/9238733893911)

No pop-up acima, realize as seguintes configurações:

No campo **"Descrição"**, especifique uma descrição para identificar o ciclo em questão.

Acionando a marcação **"Permite aprovar laudos com ressalvas"**, a aplicação permitirá que o executante do laudo o conclua aprovando-o, mesmo se uma das características estiver fora do intervalo de aceitação, ficando, deste modo, com o resultado igual a **"Aprovado com Ressalva"**. A consequência de um laudo com ressalva é a instância de ciclo de controle de qualidade com o mesmo resultado. 

Configurado os campos, clique em **"Salvar"**.

Agora, acione o botão **"Roteiro"** e crie um fluxo do roteiro.

![Imagem 9: Agora, acione o botão "Roteiro" e crie um fluxo do roteiro.](https://ajuda.sankhya.com.br/hc/article_attachments/9238945217175)

Depois, você deve vincular um evento de início de Controle de Qualidade na atividade que de fato irá inicializar o fluxo secundário referente ao controle de qualidade. Na atividade em questão, você deverá especificar qual o ciclo de controle que ela deve iniciar, por meio do campo **"Ciclo controle de qualidade"** localizado na aba [Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova#abacontroledequalidade).

![Imagem 10: Depois, você deve vincular um evento de início de Controle de Qualidade na atividade que de fato irá inicializar o…](https://ajuda.sankhya.com.br/hc/article_attachments/9222515657623)

Ainda nesta aba, acione a marcação **"Validar ciclo de controle de qualidade"** para que esta atividade siga o processo, apenas se o(s) Laudo(s) vinculado(s) ao ciclo de controle de qualidade estejam todos validados.

Para a atividade **"Amostragem/Laudo"**, você também deve vincular o Ciclo de controle de qualidade, e ainda, selecionar qual operação de controle de qualidade essa atividade representa por meio do campo **"Operação a ser realizada"**. No nosso exemplo, iremos utilizar a opção **"Amostragem + Laudo"**, pois esta atividade irá realizar as tarefas relacionadas à amostragem e preenchimento de laudos em uma mesma tarefa.

[GIF animado: Imagem 11: Para a atividade "Amostragem/Laudo" , você também deve vincular o Ciclo de controle de qualidade , e ainda, selecionar…](https://ajuda.sankhya.com.br/hc/article_attachments/9222574442263)

Você também pode realizar as seguintes configurações:

Através da marcação **"Conclui Ciclo de Controle de Qualidade"**, você determina que a conclusão da atividade também conclui o ciclo de controle de qualidade ao qual está vinculada e correntemente pendente (o vínculo acontece na aba Controle de Qualidade).

Com a marcação acima acionada, será disponibilizada a marcação **"Aprova 'Status do Lote' no final do Ciclo"**, que deverá ser utilizada somente nas atividades de Controle de Qualidade que ocorrem após a produção do produto acabado, pois só é possível aprovar o status de produtos que estão no estoque com Status = Quarentena. 

Acionando a marcação Aprova 'Status do Lote' no final do Ciclo será apresentada a marcação **"Gerar registro de Amostra e Laudo"**. Ao acioná-la, as Amostras e Laudos gerados na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o) poderão ser visualizados nas telas [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334-Registro-de-Amostras) e [Controle de Laudos e Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114-Controle-de-Laudo-de-Amostras). 

**Nota:** no exemplo de configuração acima, foi demonstrado uma configuração de controle de qualidade por evento, a mesma configuração pode ser realizada mesmo sem utilizar um evento, para os casos em que o controle de qualidade é realizado no próprio fluxo do processo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#top)

### Vinculando o produto com o Processo Produtivo

Na tela [Composição do produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto), informe no Painel Principal o **"Produto"** e o **"Processo Produtivo"** configurado nas etapas anteriores.

![Imagem 12: Na tela Composição do produto , informe no Painel Principal o "Produto" e o "Processo Produtivo" configurado nas etapas…](https://ajuda.sankhya.com.br/hc/article_attachments/9222871968791)

Ainda na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abageral), especifique no campo **"Tamanho de Lote Padrão"**, o tamanho do lote padrão do produto em questão para o processo produtivo. Esse valor é um tamanho de lote que quase sempre é utilizado, sendo sugerido de forma automática no lançamento de OP.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#top)

### Publicação do Processo Produtivo

Acesse novamente a tela [Processo Produtivo- Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314) e realize a publicação do processo produtivo, por meio do botão **"Publicar"**.

![Imagem 13: Acesse novamente a tela Processo Produtivo- Nova e realize a publicação do processo produtivo, por meio do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/9222915326359)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#top)

### Iniciando o Ciclo de controle de qualidade

Por meio da tela [Ordens de Produção-Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova) realize o lançamento de uma Ordem de Produção para o produto configurado no processo produtivo com controle de qualidade. Para isso, acione o botão **"Nova OP" ![Imagem 14: Por meio da tela Ordens de Produção-Nova realize o lançamento de uma Ordem de Produção para o produto configurado no…](https://ajuda.sankhya.com.br/hc/article_attachments/16647300942743)** Cadastrar Processo Produtivo [F8] e  preencha os campos obrigatórios presentes no pop-up **"Incluir OP"**.

[GIF animado: Imagem 15: Por meio da tela Ordens de Produção-Nova realize o lançamento de uma Ordem de Produção para o produto configurado no…](https://ajuda.sankhya.com.br/hc/article_attachments/9222979701015)

Preenchidos os campos, clique em **"Incluir OP"** e, em seguida, clique em **"Concluir"**. Assim, será exibida a ficha técnica da operação.

![Imagem 16: Preenchidos os campos, clique em "Incluir OP" e, em seguida, clique em "Concluir" . Assim, será exibida a ficha técnica…](https://ajuda.sankhya.com.br/hc/article_attachments/9223274818327)

Agora, acesse a tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o) e informe no Painel de Filtros, campo **"Nra OP"**, o número da Ordem de produção lançada anteriormente e clique em **"Aplicar"**.

Após selecionar a OP, clique em **"Iniciar"** para que a atividade da Ordem de Produção seja iniciada (Para esse passo é necessário que a Ordem de Produção tenha sido inicializada na tela [Ordens de Produção - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova)).

Feito isso, na aba [Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaapontamentos), acione o botão para incluir o produto acabado. Ao acionar este botão, o produto será carregado automaticamente. Assim, clique em **"Confirmar"**.

Como no nosso exemplo o processo produtivo possui somente uma atividade, que é a atividade responsável por gerar a nota de produção, ao confirmar o apontamento, a nota de produção do PA será gerada, dando entrada no estoque do mesmo, sendo que o estoque do PA até esse momento terá seu ‘Status’ = ‘Quarentena’.

![Imagem 17: Como no nosso exemplo o processo produtivo possui somente uma atividade, que é a atividade responsável por gerar a nota…](https://ajuda.sankhya.com.br/hc/article_attachments/9223384203799)

Iremos agora iniciar o ciclo de controle de qualidade do produto acabado. Para isso, acione o botão **"Iniciar ciclo"** localizado na aba [Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abacontroledequalidade).

**Importante:** para iniciar um novo ciclo de controle de qualidade é necessário que exista uma nota de produção do PA. Do contrário, será apresentada a mensagem:

**"Não é possível iniciar o ciclo de controle de qualidade de produtos acabados antes da geração da nota de produção"**

Após iniciar o ciclo de controle de qualidade, o evento será iniciado e a atividade de Amostragem/Laudo será disponibilizada para ser executada pelo usuário.

![Imagem 18: Após iniciar o ciclo de controle de qualidade, o evento será iniciado e a atividade de Amostragem/Laudo será…](https://ajuda.sankhya.com.br/hc/article_attachments/9223542769303)

Em seguida, para realizar o processo de amostragem é necessário abrir a atividade **"Amostragem/Laudo"** e clicar no botão **"Iniciar"** para iniciar a tarefa.

[GIF animado: Imagem 19: Em seguida, para realizar o processo de amostragem é necessário abrir a atividade "Amostragem/Laudo" e clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/9223587669399)

Para registrar a amostra nessa atividade, na grade **"Amostras"** clique no botão ![Imagem 20: Para registrar a amostra nessa atividade, na grade "Amostras" clique no botão "Cadastrar (F8)" . Informe a "Dh.…](https://ajuda.sankhya.com.br/hc/article_attachments/16647300942743) **"Cadastrar [F8]"**. Informe a **"Dh. Amostragem"** e **"Dh Verificação"** e salve o registro. Depois, clique em  ![Imagem 21: Para registrar a amostra nessa atividade, na grade "Amostras" clique no botão "Cadastrar (F8)" . Informe a "Dh.…](https://ajuda.sankhya.com.br/hc/article_attachments/9223644120599)**"Aprovar"**.

[GIF animado: Imagem 22: Para registrar a amostra nessa atividade, na grade "Amostras" clique no botão "Cadastrar (F8)" . Informe a "Dh.…](https://ajuda.sankhya.com.br/hc/article_attachments/9223833064087)

Realizada a aprovação da amostra, informe o campo **"Dh. Análise"** e salve o registro para que a amostra seja protocolada.

![Imagem 23: Realizada a aprovação da amostra, informe o campo "Dh. Análise" e salve o registro para que a amostra seja protocolada.](https://ajuda.sankhya.com.br/hc/article_attachments/9223892590743)

**Observação:** defina um modelo de requisição no parâmetro **"Nro Requisição Modelo p/ Baixa Est.MP.Amostragem - MODREQAMOSTRAS"**. Assim, sempre que uma amostra for aprovada ou reprovada, uma requisição de estoque representando o consumo do produto/lote para se formar a amostra será gerada.

Agora, na grade **"Laudos"** clique no botão ![Imagem 24: Agora, na grade "Laudos" clique no botão Cadastrar (F8) , depois na aba "Item de laudo" efetue o apontamento do…](https://ajuda.sankhya.com.br/hc/article_attachments/16647300942743) Cadastrar [F8], depois na aba **"Item de laudo"** efetue o apontamento do resultado de cada uma das características analisáveis, além de especificar uma observação no caso de rejeição da mesma para uma possível correção. 

Os registros dessa aba têm sua coloração modificada de acordo com seu resultado, sendo elas, **azul** caso esteja dentro dos valores aceitáveis e **vermelho** caso esteja fora dos valores aceitáveis.

Ao acionar o botão **"Concluir Laudo"**, será realizada a finalização do ensaio (análise) a qual o laudo representa.

Além disso, será considerado o resultado apontado em cada um dos itens de laudo para se chegar ao resultado do laudo e o último laudo de cada amostra do lote de produto para se chegar ao resultado da instância do Ciclo de Controle de Qualidade. 

**Importante:** pode-se efetuar o lançamento de diversos laudos para uma mesma amostra, porém apenas o último laudo será considerado válido para a conclusão do ciclo de controle de qualidade, ou seja, o último laudo da amostra torna os laudos anteriores inválidos.

Quando o ciclo de controle de qualidade estiver configurado para **"Gerar registro de Amostra e Laudo"** (localizado na aba [Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova#abacontroledequalidade), tela [Processo Produtivo-Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314)), as amostras e os laudos gerados na Operação de Produção, serão apresentados nas telas [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334) e [Controle de Laudos e Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114).

Para encerrar o ciclo do controle de qualidade, acione o botão ![Imagem 25: Para encerrar o ciclo do controle de qualidade, acione o botão "Finalizar" .](https://ajuda.sankhya.com.br/hc/article_attachments/9224421751063) **"Finalizar"**.

**Importante:** se houver mais de uma amostra protocolada e apenas uma delas possuir laudo, ao Finalizar a atividade, o sistema exibirá a seguinte mensagem:

**"Não foram gerados laudos para amostra Nro. Único XX. Deseja continuar?"**

Clique em **"Sim"** para gerar o laudo. Se desejar cancelar a operação, clique na opção **"Não"**.

Ao finalizar o ciclo de controle de qualidade, o sistema valida se todos os tipos de amostras possuem laudos com resultado igual à **"Aprovado"** ou **"Aprovado com ressalvas"**.

Se pelo menos um tipo de amostra, o resultado do laudo for igual a **"Reprovado"**, será apresentado o pop-up **"Laudos Reprovados"**, com as seguintes opções:

![Laudos](https://ajuda.sankhya.com.br/hc/article_attachments/15908846922007)

Selecionando a opção **"Reprovando ‘Status Lote’ do Produto no estoque"**, o Status Lote do PA que foi produzido na OP e está no estoque, deverá mudar de quarentena para reprovado e a atividade deverá ser finalizada.

No entanto, caso seja selecionada a opção **"Reprovando o Ciclo e gerando um novo Ciclo de Controle de Qualidade"**, ocorrerá o seguinte:

- O Status Lote do PA no estoque não deverá sofrer alteração;
- O resultado do ciclo de controle de qualidade deverá ser Reprovado;
- A atividade onde o ciclo de controle de qualidade está sendo realizado deverá ser finalizada;
- Um novo ciclo de controle de qualidade deverá ser iniciado automaticamente, dando início a uma nova atividade.

Diante disso, caso o novo ciclo de controle de qualidade seja finalizado sem que amostras e laudos sejam gerados para o mesmo, o sistema irá apresentar a seguinte mensagem, com a opção de responder **"Sim"** ou **"Não"**:

**“O ciclo de controle de qualidade Nro. único XPTO não foi finalizado, e o ultimo ciclo de controle de qualidade 'Concluído' foi 'Reprovado'. Deseja continuar reprovando o status lote do produto no estoque?”**

**Observação:**quando o ciclo de controle de qualidade for o primeiro a ser realizado na OP, a finalização da atividade só será realizada após a conclusão do laudo.

Há casos em que mais de um ciclo de controle de qualidade é realizado no mesmo processo (de produto em processamento e produto acabado), neste caso, o sistema só permitirá a finalização das atividades que **"Concluam o ciclo de controle de qualidade"** sem amostras ou laudos, quando o ciclo possuir a configuração **"Aprova/Reprova status lote no final do ciclo".**

Assim, ao concluir o ciclo de controle de qualidade, o status do produto acabado que foi produzido na Ordem de Produção será alterado de **"Quarentena"** para **"Aprovado"** ou **"Reprovado"**, de acordo com o resultado do laudo.

> **⚠️ Importante:** O sistema não permite a existência de múltiplos status para um mesmo lote do produto. Para produtos que passam por controle de qualidade, o status do lote é sempre definido com base no laudo mais recente emitido (ou seja, o laudo da última nota fiscal). Isso ocorre porque o sistema não controla o estoque por nota fiscal; em vez disso, o estoque é tratado de forma agrupada, considerando o lote como um todo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9222045960087-Controle-de-Qualidade-dos-PA-s#top)
