---
id: "360045115673"
titulo: "Conciliação Bancária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-09-18T12:25:17Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "Movimentação Financeira", "Preferências", "Financeiro", "EMAILGESFIN", "Conciliação Bancária", "DIASNTFCONCBANC", "FREQUSOCONCBANC", "Saldo bancário", "Saldo real", "br.com.sankhya.fin.cad.conciliacaobancaria", "Conciliação Bancária manual", "ESTRECOMPOPC", "PERMTROCOCARTAO", "USAPRDTDTLANC", "TRANSFMBEXC", "INCMBCTRANSDESP", "USADTCONEMPCTBZ", "DIASBLQDESCONBC", "Objetivo: Controlar saldo final", "Importância: Executar diariamente", "Filtros: Conciliados Pendentes", "Controlar saldo bancário", "Filtros e botões", "Conciliar lançamentos diários"]
---

# Conciliação Bancária

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312486834327) Módulo: Financeiro > Rotinas
```

---

A Conciliação Bancária tem por objetivo controlar o saldo final do Extrato Bancário evitando erros, tanto por lançamentos estranhos que por ventura apareçam no extrato bancário, quanto por lançamentos não efetuados (especialmente de CPMF, IOF e tarifas bancárias), aumentando assim a segurança e integridade das informações.

**Nota:** esta rotina é de fundamental importância e deve ser executada de preferência diariamente, pois é ela que dará a segurança de que todo o movimento do dia foi realmente lançado e que o saldo disponível pode ser considerado pela gerência.

[Filtros Rápidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#filtrosrpidos)                                                      [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#Bot%C3%B5esdotopodatela)           

[Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#painelprincipal)                                                     [Grade Detalhes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#gradedetalhes)

[Estorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#estorno)                                                                   [Como realizar a Conciliação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#comorealizaraconciliaobancria)

[Outras Informações sobre esta Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#outrasinformaessobreestarotina)            [Parâmetros que influenciam esta Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#parmetrosqueinfluenciamestarotina)

## Filtros Rápidos

![Imagem 2: Filtros Rápidos](https://ajuda.sankhya.com.br/hc/article_attachments/4409381877655)

No canto esquerdo da tela, temos os seguintes campos e marcações nos Filtros Rápidos:

A marcação **"Conciliados"**, quando habilitada, apresentará os lançamentos já conciliados; da mesma forma, quando a marcação **"Pendentes"** estiver selecionada, apresentará os lançamentos pendentes de conciliação. Você também pode filtrar por conciliações do tipo **"Receitas"** e **"Despesas"**.

No campo **"Conta"** insira o código da Conta Bancária que você deseja conciliar.

Defina no campo **"Data de Lançamento"** o período de lançamento para exibição do saldo da conta.

O campo **"Data da Conciliação"** ficará habilitado apenas se a marcação Conciliados estiver assinalada.

Pode-se filtrar ainda por **"Núm. Documento"**, **"Núm. Único Bancário"** e **"Vlr. Lançamento"**.

O campo **"Histórico"** é utilizado para registrar uma descrição da operação realizada, com o propósito de facilitar futuras consultas. Por exemplo: "Transferência de fundos para cobertura da conta garantida no Banco A".

Marque o **"Tipo de Movimento"** que deseja filtrar, de acordo com as opções abaixo:

- Aplicação;
- Depósito;
- Financeiro;
- Resgate;
- Saque;
- Transferência.

Além da opção de Filtros Rápidos, temos também a possibilidade de criar um **"Filtro personalizado"** através do ícone ![Imagem 3: Além da opção de Filtros Rápidos , temos também a possibilidade de criar um "Filtro personalizado" através do ícone…](https://ajuda.sankhya.com.br/hc/article_attachments/16117144569623)**"Cadastrar Filtro"**.

**Observação:** para adicionar um Filtro personalizado com instrução SQL, pressione o botão ![Imagem 4: Observação: para adicionar um Filtro personalizado com instrução SQL, pressione o botão "Modo Avançado" e realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/22757754451223) **"Modo Avançado"** e realize a inserção da expressão desejada, feito isso utilize o botão **"Visualizar expressão"** para verificar o filtro.

Depois de definidos os filtros desejados e adequados à rotina, clique no botão ![Imagem 5: Depois de definidos os filtros desejados e adequados à rotina, clique no botão "Aplicar" para apresentação dos títulos…](https://ajuda.sankhya.com.br/hc/article_attachments/16117128736791) **"Aplicar"** para apresentação dos títulos Conciliados e/ou Pendentes.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Botões do topo da tela

**Botão Preferências**

Ao acionar o botão **"Preferências"**, será aberto um pop-up de mesma nomenclatura, onde você pode configurar a cor dos títulos de Receita e Despesa para quando forem visualizados no modo grade, sendo que, por padrão elas possuem a cor **azul** e **vermelha**, respectivamente.

[GIF animado: Imagem 6: Ao acionar o botão "Preferências" , será aberto um pop-up de mesma nomenclatura, onde você pode configurar a cor dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4409382596887)

Ainda nesse pop-up, você pode configurar o padrão de comportamento do campo de filtro **"Data de Lançamento"**, de acordo com a marcação efetuada no **"Intervalo de Vencimento"**, sendo elas:

- **Última data utilizada:** A data de lançamento será preenchida, automaticamente, pela última data utilizada no filtro dos títulos vencidos.
- **Hoje:** A data de lançamento será preenchida, automaticamente, pela data do dia e trará apenas os títulos que estão vencendo naquele dia.
- **Semana Corrente:** A data de lançamento será preenchida, automaticamente, com data inicial referente ao primeiro dia da semana e data final referente ao último dia da semana, e trará apenas os títulos com vencimento naquela semana.
- **Mês Corrente:** A data de lançamento será preenchida, automaticamente, com data inicial referente ao primeiro dia do mês e data final referente ao último dia do mês, e trará apenas os títulos com vencimento naquele mês.
- **Limpar data:** O intervalo da data de lançamento virá sempre em branco, e ao aplicar o filtro o sistema trará todos os títulos lançados no sistema, de acordo com os demais campos de filtro, independente da data de lançamento dos títulos.
- **Personalizado:** Esta marcação habilitará os campos **"Últimos Dias"** e **"Próximos dias"**, para que você componha um filtro por vencimento que apresente os títulos dentro destes parâmetros, como por exemplo:

Considerando que no campo **"Último(s)"** foi informado um valor de 3 dias e no campo **"Próximo(s)"** um valor de 2 dias. Então, o sistema trará todos os títulos que vencerão no intervalo de 3 dias antes da data atual e 2 dias depois da data atual. Se a data atual é, por exemplo, 10/03/2018, logo serão apresentados os títulos com vencimento a partir do dia 07/03/2018 até o dia 12/03/2018.

**Botão Configurar grade superior**

Você pode criar campos adicionais para essa rotina, na tela [Dicionários de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294), tabela TGFMBC. Após a criação dos campos, por meio do botão **"Configurar grade superior"**, você poderá incluí-los para que eles sejam apresentados na grade superior da tela.

![Imagem 7: Você pode criar campos adicionais para essa rotina, na tela Dicionários de Dados , tabela TGFMBC. Após a criação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4409382150039)

**Botão Ações**

Serão apresentadas no botão ![Imagem 8: Serão apresentadas no botão "Ações" , ações que permitem a execução de tarefas específicas de forma rápida e…](https://ajuda.sankhya.com.br/hc/article_attachments/16117175475223) **"Ações"**, ações que permitem a execução de tarefas específicas de forma rápida e descomplicada. No [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) e no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) por meio da aba**"Ações"** é possível definir a execução de uma Rotina no Banco de dados (Stored Procedure), execução de uma Rotina Java, execução de um Script (JavaScript) ou o Lançamento de uma tela do sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Painel Principal

![Imagem 9: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/4409382259223)

No campo **"Saldo fim do dia"** defina a data de referência para o cálculo dos campos **"Real"** e **"Banco"**.

Em relação ao campo Real, você pode observar o saldo de todos os lançamentos, incluindo os que já encontram-se presentes no extrato do banco e os que ainda estão pendentes, mas como os cheques já foram emitidos, a qualquer momento poderão entrar no saldo.

Informe no campo Banco o saldo do banco, ou seja, apenas os lançamentos que já afetaram a conta no banco.

No campo **"Data para conciliação"** indique a data para conciliar o título.

**Observação:** caso não seja indicada nenhuma data, o sistema utilizará a data de lançamento como Data para conciliação. Esta opção deverá ser utilizada ao efetuar uma conciliação de lançamentos retroativos pois, é importante alterar a data para que o lançamento atualize o saldo na data correta, conforme o extrato bancário (emitido pelo banco).

**Nota:** a data deverá ser maior ou igual à data de lançamento do título.

Por meio dos botões ![Imagem 10: Por meio dos botões " Remove todas as linhas selecionadas" e "Remove todas as linhas não selecionadas" você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/16117153836951)**"Remove todas as linhas selecionadas"** e ![Imagem 11: Por meio dos botões " Remove todas as linhas selecionadas" e "Remove todas as linhas não selecionadas" você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/16117177926935) **"Remove todas as linhas não selecionadas"** você pode remover os itens que não deseja visualizar na grade.

Quando o botão ![Imagem 12: Quando o botão "Conciliar todos" estiver selecionado, todos os lançamentos apresentados na tela serão conciliados.](https://ajuda.sankhya.com.br/hc/article_attachments/16201542152983) **"Conciliar todos"** estiver selecionado, todos os lançamentos apresentados na tela serão conciliados.

Selecionando o botão ![Imagem 13: Selecionando o botão "Desconciliar todos" , todos os lançamentos disponíveis na tela serão desconciliados.](https://ajuda.sankhya.com.br/hc/article_attachments/16201551878551) **"Desconciliar todos"**, todos os lançamentos disponíveis na tela serão desconciliados.

A coluna **"Conciliado"** é editável no modo grade e formulário; as colunas **"Dt. Conciliação"**, **"Histórico"** e **"Pré-Data"** são editáveis apenas no modo formulário.

Na coluna **"Histórico"** será possível inserir até 150 caracteres; esta poderá ser editada mesmo que o título esteja **"Conciliado"** ou **"Pendente"**. 

**Observação:** quando uma sangria ou suprimento for realizado no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119653-Central-de-Vendas-PDV-Web), caso você não preencha o campo **"Histórico"**, ao verificar a conta em que essas ações foram realizadas, na Conciliação Bancária o campo Histórico estará preenchido com o texto **"Histórico Sangria"** ou **"Histórico Suprimento"** conforme a ação realizada. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Grade Detalhes

Através do botão ![Imagem 14: Através do botão "Mostrar detalhes" localizado no painel principal , será aberta uma nova grade na parte inferior da…](https://ajuda.sankhya.com.br/hc/article_attachments/16201783127191) **"Mostrar detalhes"** localizado no painel principal, será aberta uma nova grade na parte inferior da tela, exibindo os detalhes do item selecionado. Caso o título selecionado tenha o **"Tipo de Movimento"** como Financeiro, a grade exibirá informações do financeiro; sendo um Título Bancário, serão exibidas informações relativas ao Movimento Bancário.

Ao clicar duas vezes sobre o item disponível na grade exibida após acionar o botão acima, abre-se a tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) com o título correspondente, caso seja um Título Financeiro. Para os demais tipos de títulos, será aberta a tela [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653).

![Imagem 15: Ao clicar duas vezes sobre o item disponível na grade exibida após acionar o botão acima, abre-se a tela Movimentação…](https://ajuda.sankhya.com.br/hc/article_attachments/4409389049879)

**Observação:** quando os detalhes estão sendo exibidos, o botão Mostrar detalhes torna-se ![Imagem 16: Observação: quando os detalhes estão sendo exibidos, o botão Mostrar detalhes torna-se "Esconder detalhes" .](https://ajuda.sankhya.com.br/hc/article_attachments/16202153101719) **"Esconder detalhes"**.

No rodapé da tela o sistema exibirá o **"Total"** de **"Crédito"**, **"Débito"**, **"Líquido"**, **"Conciliado"** e o **"Selecionado"** dos títulos da grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Estorno

O botão ![Imagem 17: O botão "Estorno" será exibido na grade de Detalhes quando o título selecionado na grade superior for do Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/16202143197847) **"Estorno"** será exibido na grade de [Detalhes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#gradedetalhes) quando o título selecionado na grade superior for do Tipo Financeiro e você tiver permissão de acesso à rotina, conforme demonstrado abaixo na tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos):

![Imagem 18: O botão "Estorno" será exibido na grade de Detalhes quando o título selecionado na grade superior for do Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/4409046579479)

#### Estorno de Receitas

Para que você tenha permissão apenas para estornar Receitas através da tela Conciliação Bancária, será necessário que na tela Controle de Acessos a marcação "Estorno de Receitas" da rotina Conciliação Bancária esteja marcada como **"Permitido"**.

Neste contexto, ao configurar da forma mencionada acima, com esta permissão você poderá realizar o estorno das Receitas.

**Nota:** o botão Estorno estará disponível apenas quando o título selecionado tratar-se de Receita; quando uma Despesa for selecionada, este botão será desabilitado.

Quando o estorno a ser efetuado for do Tipo de Título igual a PIX, o sistema irá questionar a efetivação do estorno por meio da seguinte mensagem:

**"Há título(s) recebido(s) com PIX na sua seleção. O estorno da baixa não devolve os valores recebidos. Deseja prosseguir?"**

Caso você clique na opção **"Sim"**, o sistema o direcionará para o pop-up de **"Estorno de títulos"**. Porém, se a opção **"Não"** for selecionada, a operação será cancelada.

#### Estorno de Despesas

Da mesma forma, para que você possa realizar o estorno apenas das Despesas, será necessário que a marcação **"Estorno de Despesas"** esteja selecionada como Permitido.

**Observação:** o botão Estorno estará disponível apenas quando o título selecionado tratar-se de Despesa; quando uma Receita for selecionada, este botão será desabilitado.

#### Estorno (Todos)

Esta marcação quando selecionada como Permitido, possibilitará que você realize o estorno tanto de Receitas quanto de Despesas através da rotina de Conciliação Bancária.

**Nota:** o botão Estorno estará habilitado tanto para Despesas quanto para Receitas selecionadas.

**Importante:** para que o botão Estorno seja apresentado, além do título ser do Tipo Financeiro e você possuir permissão de Acesso, será necessário que na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana), a marcação **"Inibe acesso a estorno"** não encontre-se selecionada.

**Observação:** através deste botão, você poderá realizar o estorno do título selecionado sem que seja necessário acessar a tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874).

**Nota:** ao tentar realizar o estorno de um título já conciliado, o sistema emitirá a seguinte mensagem:

**"Título já conciliado! Deseja estornar mesmo assim?".**

Caso você deseje continuar o estorno do título, basta clicar em **"Sim"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Como realizar a Conciliação Bancária

Primeiramente, verifique a **"Data para conciliação"** localizada no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#painelprincipal).

Após, é necessário conferir quais os lançamentos exibidos na tela que já constam no Extrato Bancário.

**Importante:** Somente estarão visíveis para a Conciliação Bancária os lançamentos que já foram baixados.

Para realizar a conciliação do lançamento, se você estiver visualizando a tela no modo **"Grade"**, bastará selecionar a marcação **"Conciliado"** e acionar o botão ![Imagem 19: Para realizar a conciliação do lançamento, se você estiver visualizando a tela no modo "Grade" , bastará selecionar a…](https://ajuda.sankhya.com.br/hc/article_attachments/16202224583959) **"Salvar"**.

Em seguida, verifique se o saldo **"Banco"** apresentado no Painel Principal da tela encontra-se igual ao saldo do Extrato Bancário impresso pelo banco que está sendo conferido.

Por fim, ao concluir a conferência entre o Extrato Bancário e o saldo da tela de Conciliação Bancária, bastará clicar no botão **"Aplicar"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Outras Informações sobre esta Rotina

Antes de realizar a Conciliação Bancária, aconselhamos que você, tendo o Extrato Bancário em mãos, efetue a baixa das Despesas e Receitas no Financeiro.

**Observação:** Este procedimento não é obrigatório mas, caso não seja feito, você terá que alternar entre telas do sistema para lançar e baixar os títulos durante a Conciliação Bancária, causando interrupções e desvios de atenção, podendo acarretar em diferenças nos valores.

**Nota:** Se todos os lançamentos forem conciliados, o saldo **"Real"** deverá, necessariamente, ser igual ao saldo **"Banco"**.

**Observação:** Caso os lançamentos não estejam todos conciliados, haverá diferença entre os saldos Real e Bancário; você deverá realizar a conferência para perceber se com a subtração ou adição dos saldos os valores ficarão equiparados.

Em relação aos campos **"Vlr. Cheque"** e **"Vlr. Troco"** desta tela, temos que, nos casos em que o valor do cheque é superior ao valor do desdobramento e é necessário retornar troco, o valor deste será registrado na Conciliação. Trouxemos um exemplo:

A empresa recebeu um título cujo valor do desdobramento era de R$1.000,00 com um cheque no valor de R$1.500,00; na Conciliação Bancária, o campo Vlr. Cheque apresentará o valor de R$1.500,00 e o campo Vlr. Troco o valor de R$500,00, registrando, portanto, a saída deste troco para que não haja diferença no Saldo Bancário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)

## Parâmetros que influenciam esta Rotina

**Utilizar Pré-Data para Dt. Lançamento? - USAPRDTDTLANC:** deverá encontrar-se desabilitado para que você consiga visualizar um Título Financeiro com cheque pré-datado e com a baixa realizada. Caso este parâmetro não esteja desligado, apenas será possível a visualização da baixa do título caso seja realizada a filtragem pela data de vencimento.

**Inclui Mov. bancário p/ transferência de despesa? - INCMBCTRANSDESP**: quando estiver habilitado, será apresentado na tela Conciliação Bancária o Título de Despesa realizada na transferência de títulos. No entanto, quando o parâmetro estiver desligado, a rotina de transferência não irá misturar Receita com Despesa na mesma transferência, ou seja não haverá compensação.

**E-mail(s) do(s) gestor(es) financeiro(s) - EMAILGESFIN**: neste parâmetro deverá ser inserido(s) o(s) e-mail(s) do(s) gestor(es) que serão comunicados sobre o não acesso às telas [Agenda Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115533), Fluxo de Caixa e Conciliação Bancária. Somente os e-mails cadastrados receberão a notificação sobre o não acesso dos usuários nas telas.

**Nota:** Havendo a necessidade de incluir ou alterar os dados, você poderá efetuar as modificações dentro do próprio parâmetro.

**Frequência de uso esperada Conciliação bancária - FREQUSOCONCBANC**: informe neste parâmetro a frequência aguardada de uso da tela Conciliação Bancária; por exemplo, de 05 em 05 dias.

**Dias notificação de não uso Conciliação bancária - DIASNTFCONCBANC:** defina neste parâmetro os dias de notificação em que o gerente receberá um e-mail caso a tela Conciliação Bancária não seja acessada conforme definição do parâmetro FREQUSOCONCBANC. Por exemplo, caso a tela de Conciliação Bancária não seja acessada em 10 dias, será enviado um e-mail ao gestor sobre o não acesso dos usuários à tela.

**Observação:** os parâmetros de chaves EMAILGESFIN, FREQUSOCONCBANC e DIASNTFCONCBANC trabalham em conjunto e afetam o sistema da seguinte maneira:

- Quando algum funcionário, que possua acesso à tela Conciliação Bancária, efetuar o login no sistema, será exibido um pop-up de alerta sobre o período que a referida tela não está sendo acessada, de acordo com os parâmetros FREQUSOCONCBANC e DIASNTFCONCBANC; caso os dias definidos em ambos os parâmetros sejam ultrapassados, será encaminhado um e-mail ao(s) endereço(s) de e-mail(s) inserido(s) no parâmetro EMAILGESFIN.
- Uma vez posicionado no pop-up citado, clicando-se em **"Próximo"** na mensagem apresentada, tem-se a marcação **"Não quero receber mais este alerta"**; sendo esta efetuada, o pop-up não será mais apresentado. Com esta medida, nas **"Opções de contexto"** (localizado no lado superior direito da tela) será apresentada a opção **"Receber notificações Gaps gestão"** para que o(s) usuário(s) volte(m) a receber o alerta.
- Quando você ler o aviso, somente será notificado quando atingir o prazo estipulado no parâmetro FREQUSOCONCBANC com base no último envio, mesmo que ele ainda não tenha acessado a rotina;
- Ao deixar os parâmetros FREQUSOCONCBANC e DIASNTFCONCBANC indicados com "0" (zero), as mensagens não serão exibidas aos usuários. O preenchimento padrão deste parâmetro é "0" (zero);
- As mensagens são exibidas tendo em vista o grupo de funcionários que possuam acesso à tela mencionada. Por exemplo, se existem os funcionários A, B e C que possuem acesso à tela, a mensagem será exibida a todos eles. Quando qualquer um desses usuários acessar a tela, a mensagem não será mais emitida para os demais.

**Validar Empresa Exclusiva das Contas? - TRANSFMBEXC:** quando estiver habilitado, será permitido realizar a transferência e a conciliação entre contas exclusivas por meio de duas hipóteses:

- Se as empresas das contas de origem/destino forem iguais;
- Quando somente uma das contas for exclusiva.

**Nota:** não ocorrendo os pontos elencados acima, desabilite o referido parâmetro para executar a transferência e a conciliação entre contas exclusivas.

**Permite troco p/ cartão (Créd/Déb/Voucher)? - PERMTROCOCARTAO:** ao desabilitar este parâmetro, não será permitido o troco em títulos de cartão de débito, crédito ou voucher. Caso esteja habilitado, será autorizado o troco em títulos de cartão.

**Observação:** Utilizando o pagamento com vários títulos, o sistema buscará um título que permite o troco antes de lançar uma exceção.

**Estorno com Recomposição Opcional? - ESTRECOMPOPC:** quando habilitado e o título corresponder à recomposição, no momento de finalizar o estorno, o sistema apresentará um pop-up questionando se o usuário deseja recompor o título original. Por outro lado, quando estiver desabilitado, será apresentada uma mensagem informando que, ao concluir, será recomposto o título original, ou seja, você não poderá realizar o estorno.

**Usar Dt. Conciliação da empresa em contabilização - USADTCONEMPCTBZ:** ao hablitar este parâmetro o sistema irá utilizar como data da conciliação dos lançamentos somente a data da empresa em contabilização.

**Dias bloquear desconciliação de movim. bancário - DIASBLQDESCONBC**: este parâmetro define o número máximo de dias para realizar a desconciliação de um lançamento bancário conciliado. Ao tentar desconciliar um lançamento, o sistema verificará se a data de conciliação é anterior à data atual menos o número de dias informado no parâmetro DIASBLQDESCONBC. Caso esse prazo tenha sido ultrapassado, a desconciliação será bloqueada. Por exemplo:

Se a data de conciliação foi 23/09/2024 e o parâmetro DIASBLQDESCONBC está configurado com o valor de 2 dias, uma tentativa de desconciliação realizada em 26/09/2024 será impedida, pois excede o prazo permitido.

Logo, a seguinte mensagem surge na tela:

**"ORA-20101: A desconciliação só pode ser feita em lançamentos conciliados a partir de xx/xx/xxxx. Na tela "Preferências", atráves do parâmetro "DIASBLQDESCONBC" é possível ajustar esse prazo."**

Portanto, ajuste o prazo conforme a sua necessidade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria#top)
