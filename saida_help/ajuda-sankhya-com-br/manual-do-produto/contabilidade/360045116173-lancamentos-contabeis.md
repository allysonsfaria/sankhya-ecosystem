---
id: "360045116173"
titulo: "Lançamentos Contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-09-04T16:12:35Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Projeto", "Centro de Resultado", "Crédito", "Lote", "Contabilidade", "Financeiro", "Débito", "Lançamentos Contábeis", "Múltiplas Partidas", "Partida Dobrada", "REPCAMPOADPART", "USALANCPARTDOB", "br.com.sankhya.mgecontab.mov.lancamentos.contabeis", "Lançamentos Contábeis manual", "Filtros e Edição de Lançamentos Contábeis: Gerenciando Dados com Eficiência", "Lançamento Contábil"]
---

# Lançamentos Contábeis

```
 Módulo: Contabilidade > Arquivos
```

---

Lançamento Contábil é um termo utilizado em escrituração contábil, que define a maneira que um Contador irá registrar as transações financeiras de uma entidade; é o registro dos fatos contábeis, ou seja, aqueles que provocam mudanças na composição do patrimônio da entidade.

Através desta tela, você realiza a consulta e análise dos referidos lançamentos contábeis, bem como alterações, adição, exclusão e duplicação de lançamentos.

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#filtros) | [Totalizadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#totalizadores) |
| --- | --- |
| [Cadastro de Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#cadastrodelanamentoscontbeis) | [Edição, Duplicação e Exclusão de Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#edioduplicaoeexclusodelanamentoscontbeis) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#botooutrasopes...) | [Detalhes do lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#detalhesdolanamento) |
| [Parâmetros que influenciam na rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#par%C3%A2metrosqueinfluenciamnarotina) | [Estorno de Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#EstornodeLan%C3%A7amentosCont%C3%A1beis) |

![Imagem 1: Estorno de Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/article_attachments/13074930868887)

Na Grade Principal, o resultado das contas serão apresentados na cor **azul** para os saldos positivos e em **vermelho** quando o saldo estiver negativo. Essa verificação é feita com base nos seguintes resultados:

- Receita/Credora = Azul
- Despesa/Devedora = Vermelho
- Receita/Devedora = Vermelho
- Despesa/Credora = Azul

Ao acionar o botão **"Conciliar todos"**, todos os lançamentos contidos na tela serão apresentados como Conciliados, da mesma forma, quando o botão **"Desconciliar todos"** for pressionado, todos os lançamentos exibidos na tela serão Desconciliados. 

## Filtros

Ao lado esquerdo da tela temos alguns campos que, quando preenchidos servirão de filtros para a busca e identificação dos lançamentos contábeis.

![Imagem 2: Ao lado esquerdo da tela temos alguns campos que, quando preenchidos servirão de filtros para a busca e identificação…](https://ajuda.sankhya.com.br/hc/article_attachments/13074782830743)

Inicialmente, temos no alto do Painel de Filtros, o assistente para configuração de filtros personalizados, onde você pode montar o filtro desejado, que atenda alguma necessidade de busca em específico.

Logo abaixo, temos o campo **"Referência"**, que diz respeito ao período de referência dos lançamentos contábeis e é de preenchimento obrigatório para busca dos dados.

Por meio do campo **"Conciliado"** é possível visualizar os lançamentos contábeis que estão conciliados, não conciliados ou ambos. 

Informe no campo **"Núm. Lote"** o número do lote de algum lançamento, ou ainda um intervalo deles.

O campo **"Período de Movimento"** é destinado ao preenchimento do período em que foram realizados os movimentos contábeis.

De forma semelhante ao Número do Lote, você pode informar no campo **"Núm. Lançamento"**um número de lançamento em específico, ou mesmo um intervalo destes.

No campo **"Conta Inicial"**, informe uma conta contábil que possua lançamentos dentro daquele período de referência.

De maneira similar ao campo anterior, informe no campo **"Conta Final"** uma conta contábil que contenha lançamentos dentro daquele período de referência.

Você pode buscar os lançamentos por meio de seu Centro de Resultados, ou seja, serão exibidos apenas os lançamentos que possuírem o Centro de Resultado informado no campo **"Centro de Resultados"**.

**Observação:** Esta opção de preenchimento estará habilitada apenas se, nas Preferências da Empresa de Contabilidade, aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos), a marcação **"Utiliza Centro de Resultado"** estiver efetuada.

O campo **"Número único"** será apresentado se o parâmetro **"Exibir coluna com Número Único e Código Parceiro - EXIBECOLANCONT"** estiver ligado, ao selecioná-lo serão filtrados os lançamentos contábeis originados nas movimentações de estoque, baixa, financeira e bancária.

Você ainda pode buscar os lançamentos através de seu **"Projeto"**. Esta opção de preenchimento estará habilitada apenas se, nas Preferências da Empresa de Contabilidade, aba Lançamentos, a marcação **"Utiliza Projeto"** estiver realizada.

Inserindo algum código de histórico no campo **"Histórico"**, será filtrado os lançamentos contábeis que possuírem o código escolhido.

Informe no campo **"Intervalo de Documentos"**, o número de documento referente a algum lançamento, ou ainda um intervalo deles.

É possível filtrar os lançamentos, informando seus "Valores", seja este em específico ou um intervalo entre eles.

Por fim, você pode buscar os lançamentos contábeis por meio de algum trecho do histórico que ele possua, através do campo **"Complemento do Histórico Contendo"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Totalizadores

![Imagem 3: Totalizadores](https://ajuda.sankhya.com.br/hc/article_attachments/13074962089495)

Os totalizadores encontram-se no rodapé da tela e deverá somar todos os lançamentos de Receita, Despesas e o valor da Diferença entre estas, referente aos lançamentos que estão disponibilizados na tela.

**Observação:** Independente se no valor da Diferença constar débito maior ou crédito maior, o totalizador ficará com a cor vermelha e este valor será negativo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Cadastro de Lançamentos Contábeis

Assim como todo cadastro no sistema, este inicia-se através do acionamento do botão ![Botão](https://ajuda.sankhya.com.br/guide-media/01H3CA0KM288HV7BA1ABKZKVS0) **"Novo Lançamento"**. Ao fazê-lo, será aberto o pop-up Lançamento contábil:

![Imagem 5: Assim como todo cadastro no sistema, este inicia-se através do acionamento do botão "Novo Lançamento" . Ao fazê-lo,…](https://ajuda.sankhya.com.br/hc/article_attachments/13075018478999)

Primeiramente, preencha alguns campos obrigatórios:

- **Referência:** Determine o período da referência do lançamento contábil que está sendo inserido.
- **Núm. Lote:** Aqui, temos a possibilidade de digitação ou busca (ícone representado pela lupa) do número do lote contábil ao qual o lançamento contábil irá fazer parte.

**Nota:** Já deverá existir o lote contábil de acordo com a empresa do lançamento e a data de Referência informada.

- **Data Movimento:** Informe aqui a data do movimento do determinado lançamento contábil.
- **Núm. Documento:** Este espaço é destinado ao preenchimento do número de documento do lançamento contábil em questão.

O campo **"Conciliado"** demonstrará o status da conciliação do lançamento contábil através das opções **"Sim"** ou **"Não"**. Para Múltiplas Partidas, deve ser setado em cada lançamento individual, já, na Partilha Dobrada, ao ser conciliado responderá ao lançamento e sua contra partida. 

Neste primeiro momento, o campo **"Núm. Lançamento"** é de preenchimento automático pelo sistema; nele não são permitidas alterações.

Os campos **"Nro. Único"** e **"Cód. Parceiro"** são originados nas movimentações de estoque, baixa, financeira e bancária, por isso, são alimentados automaticamente e serão apresentados nesta grade apenas se o parâmetro **"Exibir coluna com Número Único e Código Parceiro - EXIBECOLANCONT"** estiver ligado.

Ao habilitar a marcação **"Extemporâneo?"** o campo **"Dt. Ocorrência Extem."** será habilitado para edição.

**Observação:** Em relação ao Registro I200, ao validar o arquivo ECD gerado com o Lançamento Extemporâneo, o campo **"Tipo de lançamento"** deste registro será igual a **"X - Lançamento extemporâneo"**.

**Importante:** Caso não seja possível informar a data precisa referente aos fatos do lançamento extemporâneo, você deverá inserir a data de encerramento do exercício em que ocorreram estes fatos.

O botão **"Excluir"** ficará habilitado se o pop-up **"Lançamento contábil"** estiver em modo de edição, e ficará desabilitado caso o pop-up esteja em modo de inserção.

O campo **"Forma de Lançamento Contábil"**será apresentado caso o parâmetro **"Usa lançamento contábil como partida dobrada? - USALANCPARTDOB"** estiver habilitado. Com o referido parâmetro ativado, serão disponibilizadas no campo duas alternativas de escolha, **"Múltiplas Partidas"** e **"Partida Dobrada"**; de acordo com a definição realizada, será habilitada a respectiva aba para continuidade na inclusão das partidas, ou seja, aba Múltiplas Partidas ou aba Partida Dobrada, as quais serão detalhadas abaixo.

![Imagem 6: O campo "Forma de Lançamento Contábil" será apresentado caso o parâmetro "Usa lançamento contábil como partida dobrada?…](https://ajuda.sankhya.com.br/hc/article_attachments/13075118129687)

#### Aba Múltiplas Partidas

**Nota:** A aba Múltiplas Partidas possui a mesma confirmação, independente da definição realizada no parâmetro Usa lançamento contábil como partida dobrada? -USALANCPARTDOB.

Você deve informar, obrigatoriamente, no campo **"Conta Contábil (Red.)"** (digitando ou buscando pelo ícone em forma de lupa), o código da conta reduzida a qual irá compor o lançamento contábil.

**Observação:** é possível realizar o preenchimento dos campos pelo modo grade e pelo modo formulário.

No campo **"Centro de Resultado"**informe o código do Centro de Resultado da determinada conta contábil.

**Observação:** Este campo será apresentado na tela, se nas Preferências da Empresa de Contabilidade, aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos), a marcação **"Utiliza Centro de Resultado"** estiver efetuada.

Caso esteja configurado no Cadastro de Plano de Contas, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393-Plano-de-Contas#abageral), o campo **"Centro de Resultado Obrigatório"**, será obrigatória a digitação do Centro de Resultado.

No campo **"Projeto"**, informe o código do Projeto da conta contábil.

**Nota:** Este campo será apresentado na tela, apenas se nas Preferências da Empresa de Contabilidade, aba Lançamentos, a marcação **"Utiliza Projeto"** estiver realizada.

Caso esteja configurado no Cadastro de Plano de Contas, aba Geral, o campo **"Projeto obrigatório"**, a digitação do Projeto será obrigatória.

Informe no campo **"Valor Débito"**, o valor a débito, se for o caso, para a conta contábil informada.

No campo **"Valor Crédito"**, informe o valor a crédito, se for o caso, para a respectiva conta contábil.

O campo **"Cód. Histórico"** é destinado a digitar ou buscar (pelo ícone representado pela lupa) o código do histórico que irá compor o lançamento contábil.

O campo **"Parte A do e-LALUR (Lançamentos)"**, indicará se o lançamento participa ou não da Parte A do e-LALUR, afetando a geração do registro M310 da ECF (Escrituração Contábil Fiscal). Por padrão, este campo é apresentado desmarcado. Além disso, ele só estará visível se a conta selecionada no Plano de Contas, aba Geral estiver com o campo Tipo de Saldo e-LALUR definido com a opção **"0 - Buscar Lançamentos (Parcial)"**.

Digite no campo **"Complemento"**, informações relevantes relacionadas ao lançamento contábil em questão.

No rodapé da aba Múltiplas Partidas, temos:

- **Total Débito:** Será exibido aqui, o valor total a débito referente ao lançamento contábil.
- Total Crédito: Ao contrário do campo anterior, temos aqui o valor total a crédito referente ao lançamento contábil.
- **Diferença:** Teremos aqui, o valor da diferença entre o total a crédito e o total a débito referentes ao lançamento contábil.

**Observação:** Caso exista alguma divergência entre a soma do total de débitos e o total de créditos o sistema irá apresentar a seguinte mensagem:

**"O valor da soma dos créditos deve ser igual ao valor da soma dos débitos"**

**Observação:** Quando o pop-up **"Opções para salvar os lançamentos"** for exibido na tela e um registro na aba Múltiplas Partidas for salvo, ao definir a opção **"Unificando Nro Lançamentos e incrementando sequência"** do campo **"Salvar os lançamentos"** do pop-up **"Opções para os lançamentos"** o sistema tornará os lançamentos realizados na tela em apenas um único lançamento com o mesmo número, mesmo que estes não tenham sofrido modificações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

#### Aba Partida Dobrada

Esta aba será disponibilizada para uso caso o parâmetro **"Usa lançamento contábil como partida dobrada? - USALANCPARTDOB"** esteja habilitado.

![Imagem 7: Esta aba será disponibilizada para uso caso o parâmetro "Usa lançamento contábil como partida dobrada? -…](https://ajuda.sankhya.com.br/hc/article_attachments/13075106798615)

Temos nesta aba, nas seções **"Débito"** e **"Crédito"**, os campos que irão compor o lançamento contábil, sendo a Conta Contábil (Red.) de preenchimento obrigatório; o Centro de Resultado, Projeto e Código do Histórico, podem ser informados manualmente, ou seguir a definição realizada no [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#botooutrasopes...), Configuração dos Lançamentos Contábeis.

Na seção Dados Gerais, determine, obrigatoriamente, o **"Valor do Lançamento"**, sendo que esta informação também poderá sofrer influência do Botão Outras Opções..., Configuração dos Lançamentos Contábeis.

O campo **"Parte A do e-LALUR (Lançamentos)"**, indicará se o lançamento participa ou não da Parte A do e-LALUR, afetando a geração do registro M310 da ECF (Escrituração Contábil Fiscal). Por padrão, este campo é apresentado desmarcado. Além disso, ele só estará visível se a conta selecionada no Plano de Contas, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393-Plano-de-Contas#abageral) estiver com o campo Tipo de Saldo e-LALUR definido com a opção **"0 - Buscar Lançamentos (Parcial)"**.

É possível ainda, inserir algum **"Complemento"** necessário e pertinente ao lançamento.

Observe no rodapé do pop-up os botões:

- **Limpar:** Quando acionado, serão limpos todos os campos informados até então.
- **Salvar:** Este botão realiza o salvamento dos lançamentos contábeis realizados.
- **Salvar e Novo:** Clicando neste botão, o sistema irá salvar os lançamentos contábeis efetuados e manter a tela aberta para que se possa realizar outros lançamentos contábeis, conforme a necessidade.
- **Fechar:** Este botão realiza o fechamento da tela; este procedimento não salva automaticamente os dados, portanto, na conclusão de um cadastro, faça seu salvamento por meio dos botões citados anteriormente (**"Salvar"** ou **"Salvar e Novo"**) antes de fechar a referida tela.

**Importante:** Para lançamentos contábeis manuais, é necessário que você configure nas Preferências da Empresa de Contabilidade, aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos), Seção Intervalo de Lotes para Lançamento Manual, os campos:

- Início do número do lote manual;
- Fim do do número do lote manual.

Ao realizar lançamentos contábeis manuais, caso um destes campos esteja vazio o sistema irá apresentar a seguinte mensagem de erro:

**"Para Lançamentos Contábeis manuais é necessário configurar o Intervalo de Lotes para lançamentos Manuais nas preferências da empresa."**

Caso tenha sido feita a configuração mencionada, porém o lote manual informado esteja fora da faixa configurada, será exibida a mensagem:

**"O número de lote deve estar entre a faixa: 001 (loteMínimo) e 100 (loteMáximo)."**

**Nota:** Quando criado um campo adicional e o mesmo for vinculado à tela Lançamentos Contábeis (tabela TCBLAN), ao realizar a inclusão de lançamentos contábeis de forma manual, caso o parâmetro **"Replica campo adicional para todas as partidas do lançamento contábil? - REPCAMPOADPART"** esteja ativado (comportamento padrão), a informação pertinente ao campo adicional será reproduzida para todas as partidas correspondentes ao lançamento contábil. Se o referido parâmetro estiver desativado, os dados do campo adicional criado não serão duplicados nas demais partidas do lançamento contábil, tal informação será considerada apenas para o lançamento em que foi inserido.

O campo **"Empresa de Origem"** quando preenchido, possibilitará para os lançamentos manuais, a opção de registro da empresa de origem do lançamento e, desta forma, sendo possível realizar a rastreabilidade destes lançamentos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Edição, Duplicação e Exclusão de Lançamentos Contábeis

Caso seja necessário, é possível realizar a edição dos lançamentos contábeis. Para isso, acione o botão ![editar](https://ajuda.sankhya.com.br/hc/article_attachments/15438074697623) **"Editar Lançamento"** presente na parte superior da tela. Feito isso, será aberto novamente o pop-up Lançamento contábil apresentando o registro a ser editado, onde nos casos de edição dos valores de crédito e débito, deve-se manter a mesma regra de seu cadastro, ou seja, a inexistência de divergência na soma destas quantias.

**Nota:** Ao editar um lançamento, você deve lançar um crédito para cada débito efetuado.

Para que a edição de um lançamento seja executada com a sequência correta, é necessário realizar as etapas a seguir:

Após selecionar o lançamento a ser editado, você deverá lançar um crédito e um débito; feito isso, no pop-up Lançamento Contábil irá constar dois lançamentos.

Em seguida, o sistema abrirá outro pop-up com **"Opções para salvar os lançamentos"**, em que você deve utilizar a opção **"Incrementando Nro de Lançamento"**.

Realizando estas configurações, os lançamentos seguirão uma sequência correta.

Você também poderá **"Duplicar"** um lançamento contábil por meio do ícone ![Imagem 9: Você também poderá "Duplicar" um lançamento contábil por meio do ícone . Ao acioná-lo, será exibido um pop-up de…](https://ajuda.sankhya.com.br/hc/article_attachments/15438074701463). Ao acioná-lo, será exibido um pop-up de Confirmação do procedimento.

Clicando em **"Sim"**, será aberto um novo pop-up de nome **"Duplicar Lançamento Contábil"**, onde determina-se, obrigatoriamente, os dados do cabeçalho; ao término do preenchimento, clique no botão **"Duplicar"**, onde será aberto o pop-up Lançamento contábil em modo de edição, com o registro duplicado posicionado:

![Imagem 10: Clicando em "Sim" , será aberto um novo pop-up de nome "Duplicar Lançamento Contábil" , onde determina-se,…](https://ajuda.sankhya.com.br/hc/article_attachments/5278353283479)

Clicando em **"Não"**, todo o lançamento será duplicado, gerando um novo número de lançamento, sem editar nenhuma informação do lançamento original.

Ainda no pop-up Lançamento contábil, observe em seu lado superior direito, o botão ![remover](https://ajuda.sankhya.com.br/hc/article_attachments/15438074702359)**"Remover Lançamento"** que, quando acionado, fará com que o sistema exclua todo o lançamento contábil, incluindo as partidas do lançamento.

**Nota:** Este botão será apresentado para utilização, apenas depois que o cadastro o lançamento contábil foi devidamente realizado e salvo no sistema; por esse motivo, ele não é exibido no momento da realização do cadastro. Além disso, para excluir um lançamento, é preciso inicialmente acionar o botão Editar Lançamento, descrito acima.

**Observação:** Não é possível realizar um lançamento contábil manual em um lote fechado; caso ocorra, a seguinte mensagem é apresentada:

**"O lote "XX" já está fechado e nessa situação não pode ser utilizado. Deseja reabri-lo?"**

Na mensagem, **"XX"** se refere ao número do lote. Clicando-se em **"OK"**, o lote é reaberto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Botão Outras Opções...

O botão ![Outras](https://ajuda.sankhya.com.br/hc/article_attachments/15438346864663) Outras Opções..., apresenta a funcionalidade **"Configurar lançamentos contábeis"** que, ao ser acionada, apresenta o pop-up **"Configuração de Lançamentos Contábeis"**:

![Imagem 13: O botão Outras Opções... , apresenta a funcionalidade "Configurar lançamentos contábeis" que, ao ser acionada,…](https://ajuda.sankhya.com.br/hc/article_attachments/38473121563799)

Neste pop-up temos as seguintes configurações:

**Seção Múltiplas Partidas**

Trabalhando-se com Múltiplas Partidas, caso a marcação **"Propagar Núm. Documento"** esteja realizada, o Número de Documento, será reproduzido para todas as partidas do lançamento.

**Seção Partida Dobrada**

Nesta seção, você pode determinar a Configuração para fixar campos, estabelecendo dentro das operações de Débito e Crédito, quais campos terão seus valores fixados, quando na inclusão de um novo lançamento contábil.

**Seção Dados Gerais**

Nesta seção, você pode optar por **"Duplicar Histórico"**, marcação esta que, se realizada, fará com que o campo Cód. Histórico, presente no espaço Configuração para fixar campos fique desabilitado (tanto para Débito, quanto para Crédito), ou seja, se você optar por duplicar o histórico, ao salvar o registro, existindo Cód. Histórico do Débito salvo no histórico, este será replicado para o Crédito e vice-versa.

A marcação **"Valor Lançamento"** quando realizada, fará com que, ao inserir um novo lançamento, o Valor do Lançamento seja apresentado já preenchido; logicamente o inverso ocorre, caso a marcação em questão não esteja realizada.

##### Seção Lotes para Estorno

Nesta seção, você define o comportamento do sistema para a seleção do lote ao realizar estornos, evitando inconsistências em fechamentos contábeis. As opções disponíveis são:

- **Mesmo lote do lançamento:** o sistema tentará realizar o estorno no mesmo lote onde o lançamento original foi contabilizado. Caso este lote não esteja disponível (por exemplo, se estiver fechado), o sistema exibirá um pop-up solicitando que você informe outro número de lote.
- **Maior lote disponível:** o sistema direcionará o estorno para o lote de numeração mais alta que estiver aberto no momento.
- **Lote fixo:** ao selecionar esta opção, o campo ao lado será habilitado para que você informe um número de lote específico. Todos os estornos serão direcionados para este lote; caso ele esteja indisponível, o sistema solicitará um novo número.
- **Sempre perguntar:** o sistema abrirá um pop-up a cada operação de estorno, exigindo que você informe manualmente o lote de destino.

**Nota:** ao selecionar múltiplos lançamentos para estorno simultâneo, se a configuração exigir a informação do lote (seja pela opção **"Sempre perguntar"** ou por indisponibilidade do lote padrão), a pergunta será feita **apenas uma vez** e aplicada a todos os lançamentos selecionados. Se não houver nenhum lote aberto no sistema, será exigida a criação de um novo lote.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Detalhes do lançamento

Através de um duplo clique sobre alguma linha, ou por meio do botão ![detalhes](https://ajuda.sankhya.com.br/hc/article_attachments/15438402890135) **"Detalhes do Lançamento"** localizado na parte superior direita da tela, é aberto o pop-up Detalhes do Lançamento, onde visualiza-se as informações do referido lançamento.

Além disso, uma vez selecionado o detalhe desejado, clicando em "OK", é aberta a tela correspondente à seleção realizada, ou seja, serão abertas as telas de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653) ou [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973).

**Importante:** Para que seja possível analisar o detalhe desejado em sua respectiva tela, é necessário que você possua a permissão de acesso à visualização mesma.

Durante a [Consolidação de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas) será gerada uma chave de rastreabilidade na tela Lançamentos Contábeis para que os movimentos de origem da contabilização das empresas anteriores sejam identificados com facilidade.

![Imagem 15: Durante a Consolidação de Empresas será gerada uma chave de rastreabilidade na tela Lançamentos Contábeis para que os…](https://ajuda.sankhya.com.br/hc/article_attachments/13077394189847)

Esta chave será composta com os seguintes dados:

- CODEMP: 1
- REFERENCIA: 01122022
- NUMLANC: 4
- TIPLANC: R
- ORIGEM: E
- NUNICO: 2371
- NUMLOTE: 16
- VLRLANC: 287,90
- SEQNOTA: 0
- SEQUENCIA: 0

**Nota:** as informações serão separadas por dois pontos (:), conforme apresentado na imagem acima.

Os lançamentos manuais não têm rastreabilidade, sendo assim, as chaves não serão apresentadas na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Estorno de Lançamentos Contábeis

O estorno de lançamentos foi criado para atender às normas contábeis e garantir que o histórico dos documentos seja mantido, mesmo quando for necessário realizar ajustes após a contabilização. Com essa funcionalidade, é possível desfazer um lançamento sem apagar o original, preservando a rastreabilidade das informações contábeis.

#### Quando usar o estorno?

Use o estorno quando for necessário ajustar um lançamento já contabilizado, sem perder o registro do documento original. Exemplos comuns:

- Correções de lançamentos com dados incorretos.
- Cancelamentos de documentos contabilizados por engano.
- Ajustes em documentos que precisam ser reprocessados.

#### Como estornar um lançamento?

1. Acesse a tela **Lançamentos contábeis**.
2. Identifique o lançamento que precisa ser ajustado.
3. Clique no botão **Estornar**.

Ao executar essa ação, o sistema gera automaticamente um lançamento inverso ao original, que neutraliza o impacto no resultado contábil.

**Importante:** o estorno não apaga o lançamento original, apenas o neutraliza com um lançamento inverso.

#### Como identificar um lançamento estornado?

Após o estorno, as colunas da tela são atualizadas para indicar o status dos lançamentos:

- **Foi estornado** – exibido no lançamento original.
- **É um estorno** – exibido no lançamento criado pelo estorno.
- **Não é um estorno** – para os lançamentos que não passaram pelo processo de estorno.

Além disso, a coluna **Cód. Rastreamento Estorno** mostra o vínculo entre os lançamentos: no lançamento de estorno, está registrado o número do lançamento original para facilitar consultas.

#### Como o estorno afeta o documento de origem?

- Quando um documento de origem (nota fiscal, baixa, título financeiro etc.) é contabilizado, ele é automaticamente **travado para edição**.
- Ao realizar o estorno, esse documento original é **desbloqueado**, permitindo novos ajustes.

**Importante:** o desbloqueio pelo estorno não ignora as regras próprias do documento. Por exemplo, uma nota fiscal aprovada pela SEFAZ continua sujeita às regras fiscais e não poderá ser editada, mesmo após o estorno.

Dessa forma, o sistema respeita todas as validações e restrições previstas para cada tipo de documento.

- Se o documento original gerou vários lançamentos, o estorno será aplicado a todos eles de forma conjunta.

#### Conta contábil do estorno

Por padrão, o estorno é lançado na **mesma conta contábil** do lançamento original. Porém, o sistema permite configurar contas específicas para receber os estornos.

#### Como configurar contas de estorno?

1. Acesse o cadastro da conta contábil na tela [**Plano de Contas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas).
2. Ative a marcação **Conta de estorno**.
3. Na aba, [**Parâmetros de estorno**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas#Par%C3%A2metrosEstorno), informe os códigos das contas de origem que devem ser estornadas nesta conta.

**Importante:**

- Uma mesma conta de estorno pode ser vinculada a várias contas de origem.
- Uma conta marcada como conta de estorno pode receber outros tipos de lançamentos além de estornos.
- Se nenhuma conta de estorno for configurada, o estorno será registrado na conta original.

**Entenda com base no seguinte exemplo:**

A conta **“Vendas Canceladas”** foi configurada como conta de estorno para lançamentos da conta **“Vendas Realizadas”**. Assim, ao estornar lançamentos dessa conta, os valores são lançados na conta de estorno configurada, facilitando a identificação e controle contábil.

#### Relatório de Histórico de Lançamentos Contábeis

Para facilitar o acompanhamento e auditoria dos lançamentos, foi criada uma opção de relatório exportável em Excel diretamente na tela **Lançamentos contábeis**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

## Parâmetros que influenciam na rotina

Você pode definir no parâmetro **"Tamanho da página p/ consulta ao banco de dados -PAGCONSLANC"**, a quantidade de registros que serão exibidos na grade dessa tela. Assim, a depender do valor informado, novas páginas serão geradas na tela e os botões de navegação, habilitados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#top)

Acesse também:

[Consulta Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607374)
