---
id: "360044608174"
titulo: "TOP Contabilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilização"
atualizado_em: "2026-10-07T14:52:14Z"
rotulos: ["AJUDA DO SKW", "manual", "Campos", "Configuração", "Contas", "Centro de Resultado", "Adicionais", "Flexíveis", "USANATCTA", "USANATPROJ", "USANATXEMP", "br.com.sankhya.ctbz.mov.contabilizacaotop", "TOP Contabilização manual", "TOP", "Contabilização", "Financeiro", "Configuração da TOP Contabilização"]
---

# TOP Contabilização

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314943683351) Módulo: Contabilização > Arquivos
```

---

Essa configuração é necessária para contabilizar os registros lançados nas Centrais de [Vendas, Compras e Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), no financeiro, nas movimentações bancárias e no movimento de baixa. Na ausência dessa configuração, não será possível realizar a contabilização por processo de geração de lote na Contabilização.

Para que se tenha a TOP configurada para utilização desta rotina, deve-se:

- Marcar o campo **"Atualiza Contabilidade"** nos [Cadastros de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) em sua aba **"Geral"**;
- Acessar esta rotina **Contabilização > Arquivos > TOP Contabilização** e filtrar a TOP;
- Clique no botão de inclusão (+) e inserir as configurações para contabilização. Para configurar corretamente os registros dessa tela, deve-se solicitar apoio ao contador da empresa quanto aos lançamentos a serem reproduzidos de acordo com cada operação a ser contabilizada.

**Observação:** as opções para configuração dos **"Centros de Resultado (CR)"** somente estarão disponíveis nesta tela no Jiva-Om, se a empresa trabalhar com o opcional **"JIVA-CENTRO DE RESULTADOS/W"**.

| Funcionalidades da tela |
| --- |
| [Campos a serem configurados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#camposaseremconfigurados) |
| [Divergências no lançamento contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#Diverg%C3%AAnciasnolan%C3%A7amentocont%C3%A1bil) |
| [Contas Flexíveis na Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#contasflexveisnacontabilizao) |
| [Contextualizando sobre Fórmulas e Funções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#contextualizandosobrefrmulasefunes) |

![Imagem 2: Contextualizando sobre Fórmulas e Funções](https://ajuda.sankhya.com.br/hc/article_attachments/5166615244311)

### Campos a serem configurados

Na grade **"Configurações p/ Lançamentos Contábeis"** teremos os seguintes campos:

Na marcação **"Atualiza Contabilidade"** é definida se a TOP selecionada será utilizada para contabilizar movimentos ou não.

Em relação ao campo **"Consultas Auxiliares"** informe o nome das querys salvas no [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos). Dessa forma, informe no campo mencionado quais arquivos aquela TOP utilizará na contabilização, sendo necessário separá-los por uma vírgula. Assim, teremos o seguinte exemplo:

```
queryImposto.sql, queryImpostoPis.sql, queryImpostoCofins.sql.
```

Indique no campo **"Tipo de Lançamento"** se a TOP realizará a operação de **"Crédito"** ou de **"Débito"**.

O campo **"Cód. Histórico"** é destinado a determinar o Histórico padrão a ser utilizado. Os históricos aqui apresentados, serão aqueles cadastrados previamente na rotina [Histórico Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116113).

Defina o campo **"Tipo de Centro de Resultado"** como **"Constante"** ou **"Variável"**, sendo que para cada uma dessas opções, tem-se o seguinte comportamento:

**Constante:** sempre que esta TOP Contabilização for utilizada, o Centro de Resultado informado no campo **"Cód. Centro de Resultado"**, será utilizado.

**Variável:** ao selecionar essa opção, o campo **"Cód. Centro de Resultado"** irá apresentar as seguintes alternativas para a Contabilização referente ao Centro de Resultado:

- **2 - Empresa destino (CR 2):** irá levar para a Contabilização as informações de Centro de Resultado da empresa de destino da transferência. **"CR 2"** corresponde ao campo **"Centro de Resultado 2"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Contabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abacontabilidade).
- **R - Rateio**: será utilizado o CR do rateio para a contabilização.
- **O - Empresa Origem (CR 1)**: serão levadas para a Contabilização as informações de Centro de Resultado da empresa de origem da transferência. **"CR 1"** corresponde ao campo **"Centro de Resultado 1"** nas Preferências da Empresa, aba **"Contabilidade"**.
- **N - Rateio ou Financeiro**: por essa opção, tem-se o seguinte critério para a contabilização: Primeiro irá utilizar o Centro de Resultado do rateio, se este for zero, irá utilizar o Centro Resultado do financeiro, que se for zero, utilizará o Centro de Resultado da nota.
- **C - Cabeçalho da Nota:** será utilizado o CR do cabeçalho da Nota para a contabilização.
- **E - Empresa Origem (CR 2)**: serão levadas para a Contabilização as informações de "Centro de Resultado" da empresa de origem da transferência. **"CR 2"** corresponde ao campo **"Centro de Resultado 2"** nas Preferências da Empresa, aba **"Contabilidade"**.
- **F - Financeiro**: será utilizado para a contabilização o CR definido no título financeiro.
- **1 - Empresa destino (CR 1)**: serão levadas para a Contabilização as informações de **"Centro de Resultado"** da empresa de destino da transferência. **"CR 1"** corresponde ao campos **"Centro de Resultado 1"** nas Preferências da Empresa, aba **"Contabilidade"**.
- **P - Produto:** ao selecionar essa opção, as contabilizações irão considerar o Centro de Resultado do Produto configurado na aba [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-). Sendo que, se houver mais de um produto e para cada um deles um Centro de Resultado específico em uma nota, os Lançamentos Contábeis apresentarão valores de crédito e débito para cada produto com Centros de Resultados diferentes.

**Nota:** quando os campos Tipo de Centro de Resultado e Tipo de projeto forem configurados com a opção Variável, o campo **"Cód. Projeto"** deve ser informado com a mesma opção selecionada no campo **"Cód. Centro de Resultado"**.

No campo **"Cód. Centro de Resultado"** defina o Centro de Resultado em específico, ou o local para busca do mesmo, dependendo da escolha feita no campo anterior (Tipo de Centro de Resultado).

**Observação:** para que o sistema faça a busca da natureza de receitas e despesas ao realizar um [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento), o campo acima deve ser preenchido.

Pode-se definir o campo **"Tipo de Conta Contábil"** como **"Constante"** ou **"Variável"**, sendo que para cada uma destas opções, tem-se o seguinte comportamento:

- **Constante:** sempre que esta TOP Contabilização for utilizada, a Conta Contábil informada no campo **"Conta Contábil"**, será utilizada;
- **Variável:** ao selecionar essa opção, o campo **"Conta Contábil"** irá apresentar as seguintes alternativas para a Contabilização referente à Conta Contábil:

| - Conta 1 do parceiro; - Conta 2 do parceiro; - Conta 3 do parceiro; - Conta 4 do parceiro; - Conta 1 do tipo de negociação; - Conta 2 do tipo de negociação; - Conta 1 da empresa; - Conta 2 da empresa; - Conta 1 da natureza; - Conta 2 da natureza; - Conta do rateio; - Conta 1 do produto; - Conta 2 do produto; - Conta 3 do produto; - Conta 4 do produto; - Conta da conta bancária; - CFO dos itens; | - Conta 1 do Tip. Título; - Conta 2 do Tip. Título; - Conta 3 do Tip. Título; - Conta 1 do projeto; - Conta 2 do projeto; - Conta 1 da Transportadora; - Conta 2 da Transportadora; - Conta 3 da Transportadora; - Conta 4 da Transportadora; - Natureza por CR; - Conta Adicional 20 do Parceiro; - Conta Adicional 20 da Transportadora; - Conta Adicional 01 do Produto; - Conta Adicional 50 do Produto; - Conta Adicional 80 do Produto; - Conta Adicional 81 do Produto; |
| --- | --- |

Como exemplo dessa configuração, teremos na contabilização da TOP o tipo de conta **"Variável"** e em **"Conta Contábil"** selecione **"Conta 1 do produto"**, e no **"Cadastro do Produto"**, no campo **"Conta Contábil 1"** (Aba Geral), registre a **"Conta 10"**, ao contabilizar os lançamentos pelo módulo de Contabilização, o sistema buscará as informações da TOP, e como nessa foi feita a configuração para contabilizar pelo produto, serão contabilizadas na conta informada no campo **"Conta Contábil 1"** do produto, ou seja, na **"Conta 10"**.

**Observação**: o parâmetro **"Usar relação Natureza X Empresa - USANATXEMP"** influencia diretamente na apresentação da conta contábil. Caso este esteja ligado a opção **"Natureza por Empresa"** é apresentada na **"Conta Contábil"** da Top de Contabilização. Caso desligado, a opção **"Natureza por CR"** não é apresentada na Conta Contábil da TOP de Contabilização. Lembrando que o mesmo só é apresentado quando o tipo da conta for **"Variável"**.

No campo **"Conta contábil"** defina a Conta Contábil específica, ou o local para busca da mesma, dependendo da escolha feita no campo anterior (Tipo de Conta Contábil).

**Observação:** caso a TOP Contabilização esteja cadastrada com o campo Conta contábil definido com a opção Natureza por Projeto, o sistema irá verificar se existe Projeto cadastrado na tela [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774), se houver, a Conta Contábil do Projeto será utilizada para gravar o valor do lançamento, caso não exista, será utilizada a Conta Contábil 1 do cadastro de Naturezas. Para que a opção Natureza por Projeto seja apresentada, é necessário que o parâmetro **"Usar relação Natureza X Projeto? - USANATPROJ"** esteja ativado, e os parâmetros **"Usar relação Natureza X Cta Bancária? - USANATCTA"** e **"Usar relação Natureza X Empresa - USANATXEMP"**, estejam desativados.

Pode-se definir o campo **"Tipo de Projeto"** como **"Constante"** ou **"Variável"**, sendo que para cada uma dessas opções, tem-se o seguinte comportamento:

- **Constante:** sempre que esta **"TOP Contabilização"** for utilizada, o Projeto informado no campo **"Cód. Projeto"**, será utilizado.
- **Variável:** escolhendo-se esta opção, o campo **"Cód. Projeto"** irá apresentar as seguintes alternativas para a Contabilização referente ao Tipo de Projeto:

**C - Cabeçalho da Nota**: será utilizado o Projeto do cabeçalho da Nota para a contabilização.

**N - Rateio ou Financeiro**: por essa opção, a seguir o critério para a contabilização:

Primeiro irá utilizar o Centro de Resultado do rateio, se esse for zero, irá utilizar o Centro Resultado do financeiro, que se for zero, utilizará o Centro de Resultado da nota.

**F - Financeiro:** será utilizado para a contabilização o CR definido no título financeiro.

**R - Rateio**: será utilizado o CR do rateio para a contabilização.

**P - Produto:**  quando essa opção é selecionada, o sistema buscará a informação do projeto no campo **"Projeto"**, da aba [Venda,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abavenda) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) para realizar a contabilização.

**Nota:** quando os campos Tipo de Centro de Resultado e Tipo de projeto forem configurados com a opção Variável, o campo **"Cód. Projeto"** deve ser informado com a mesma opção selecionada no campo **"Cód. Centro de Resultado"**.

Por meio do campo **"Cód. Projeto"** defina o Projeto em específico, ou o local para busca do mesmo, dependendo da escolha feita no campo **"Tipo de Projeto"**.

Informe no campo **"Lançamento"**, a ordem do lançamento em número, exemplo: 0, 1, 2, 3, 4 etc.

Pode-se informar no campo **"Fórmula"**, uma fórmula para valor a ser utilizado no lançamento, onde pode-se utilizar do campo ![Imagem 3: Pode-se informar no campo "Fórmula" , uma fórmula para valor a ser utilizado no lançamento, onde pode-se utilizar do…](https://ajuda.sankhya.com.br/hc/article_attachments/5167411527319), localizado à frente do campo, que ao ser acionado, será aberta a seguinte tela para construção da fórmula:

![Imagem 4: Pode-se informar no campo "Fórmula" , uma fórmula para valor a ser utilizado no lançamento, onde pode-se utilizar do…](https://ajuda.sankhya.com.br/hc/article_attachments/5167389424791)

**Observação:** visando auxiliar na criação das fórmulas, o sistema conta com um recurso de busca ao banco de dados denominado PDES, que tem como objetivo agilizar as consultas e obtenções de informações, devido a objetividade acerca de sua formulação. Para uso desse recurso, aconselhamos a intervenção de um Consultor Sankhya.

Defina no campo **"Tipo de data"**, o tipo de data para a contabilização. Pode-se escolher dentre as seguintes opções:

- Vencimento;
- Ajusta Valor Presente;
- Negociação;
- Movimento;
- Juro/Multa Mês;
- Faturamento;
- Ent./Saída;
- Conciliação;
- Validade;
- Baixa.

**Nota:** para maiores informações sobre a Contabilização de Financeiros com Ajuste ao Valor Presente, consulte o link [Contabilização de Financeiros com Ajuste ao Valor Presente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734).

Informe no campo **"Empresa"**, o código da empresa para operação entre empresas, cujo reflexo destas será apenas na contabilidade. Caso contrário, deixe-o em branco.

Efetue a marcação **"Sintetiza"**, para operações com grande volume de lançamentos, aos quais estes são destinados a uma conta em que se queira agrupá-los por período, evitando assim várias linhas de contabilização a serem impressas no Diário ou Razão.

**Observação:** quando a TOP estiver marcada como Sintetiza, não será compatível com a contabilização multipartida, ou seja, para o caso de TOP que Sintetiza não será gerado múltiplas partidas, sendo gerado apenas sequência zero e incrementando o número dos lançamentos.

Informe no campo **"Desc. Histórico"**, um complemento do histórico ou o histórico da TOP, onde pode-se também utilizar algumas variáveis que serão apresentadas a seguir.

O sistema disponibiliza função de adicionar variáveis no campo Histórico, variáveis para descrição de **"Natureza"** e **"Projeto"** na Contabilização, por exemplo. Assim, quando houver a Contabilização de algum título que utiliza a TOP em questão, no qual os históricos foram selecionados, nesse exemplo, o nome da Natureza e/ou nome do Projeto serão adicionados no histórico do lançamento.

Segue abaixo a lista das variáveis, com suas respectivas finalidades:

| |NF| Nota Fiscal; | |NA| Descrição Natureza; |
| --- | --- |
| |DN| Data da negociação; | |PR| Identificação do Projeto; |
| |HH| Histórico (50 posições); | |CT| Nome do Contato; |
| |DV| Data de Vencimento; | |CP| Código Produto/Serviço; |
| |DM| Data de Movimento; | |CE| Código Empresa; |
| |DB| Data da Baixa; | |NE| Nome Empresa; |
| |ND| Número do Documento; | |DD| Desdobramento; |
| |NS| Nosso Número; | |ED| Espécie de Documento; |

| |NP| Nome/Razão Social do Parceiro; | |RSCE| Razão Social do Contato de Entrega; |
| --- | --- |
| |RP| Nome/Razão Social do Parceiro; | |RSPT| Razão Social do Parceiro Transportadora; |
| |RS| Razão Social do Parceiro; | |RSPD| Razão Social do Parceiro Destinatário; |
| |NO| Nome Parceiro; | |RSPR| Razão Social do Parceiro Remetente; |
| |NT| Número Transferência; | |NCF| Nro. Conhec. Frete; |
| |CC| Conta Corrente; | |NC| Número Contrato; |
| |CD| Descrição da Conta; | |BB| Código do Bem baixado pela NF |
| |CR| Descrição C. Resultado; | |NR| Número de NF referenciada |
| |OB| Observação da nota (50 posições); | |DC| Descrição da conta bancária de contrapartida |
| |DI| Descrição Produto/Serviço; | |NSD| Série do documento fiscal |

No campo **"Histórico"**, a variável **"|CR| Descrição C. Resultado"** só funcionará se o campo **"Centro de Resultado"** apresentar as seguintes opções:

**O** - Empresa origem (CR 1);

**E** - Empresa origem (CR 2).

As variáveis **"|CE| - Código Empresa"** e **"|NE| - Nome Empresa"**, facilitam a identificação de alguns lançamentos no "Razão", pelo campo Histórico.

A parametrização desta tela pode receber quantas linhas forem necessárias para a contabilização da operação; com o mapeamento essa tarefa fica mais fácil e rápida. Após a parametrização dessa tela, os registros realizados com a(s) TOP(s) parametrizada(s), estarão em condições de serem contabilizados com a geração de lotes.

O campo **"Contabilização entre Partes Relacionadas"** tem o objetivo de atender empresas que trabalham com contas transitórias. Nesse campo, teremos as seguintes opções:

- **Não há**;
- **Normal:** ao selecionar essa opção, a Contabilização será identificada e realizada como um lançamento normal.
- **Intra-Company:** nesta, será identificado e realizado a Contabilização como lançamento Intra Company.
- **Inter-Company:** identifica-se e efetua-se a Contabilização Inter-Company com esta opção selecionada.

**Nota:** para a opção **"Normal"**, o sistema resolverá o **"Vlr. do Lançamento"** de acordo com a fórmula inserida no campo **"Fórmula"** desta tela.

**Observação:** ao selecionar a opção **"Intra-Company"** ou **"Inter-Company"** e o lançamento seja válido, teremos que o sistema utilizará o valor de **"Vlr. Baixa"** para o filtro **"Baixas"** ou Vlr. do Lançamento para o filtro **"Mov. Bancários"**, ambos localizados na tela [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389053-Agendamento), aba [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento#abafiltros).

Ainda nesse contexto, caso seja selecionada no campo acima as opções Intra-Company ou Inter-Company, serão exibidos outros três campos na tela, conforme mencione abaixo:

O campo **"Representante Company"** será utilizado para verificar se a empresa da geração do lote trata-se de uma empresa válida para a linha de Contabilização, ou seja, para o filtro Baixas, tem-se que a empresa matriz é a mesma que baixou o título e a empresa filial será a empresa que gerou o título. Para o filtro Mov. Bancário, a matriz é a empresa que possui a despesa bancária e a filial a que possui a receita.

Em relação ao campo **"Conta Contábil Transitória"** tem-se que este será utilizado para informar a Conta Contábil do lançamento de Conta Transitória, possuindo as opções **"Constante"** e **"Variável"** disponíveis neste campo.

No botão **"Outras Opções..."** teremos a opção **"Validar Partidas"**; ao acionar essa e não apresentando erros, o sistema emitirá a seguinte mensagem:

**"Configuração p/ Lançamentos contábeis sem divergências".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#top)

### Divergências no Lançamento Contábil

Caso as configurações abaixo sejam realizadas em conjunto, pode ocorrer divergência no lançamento contábil:

![Imagem 5: Se for configurado os campos "Conta contábil" , "Cód. Centro de Resultado" ou "Cód. Projeto" nos lançamentos contábeis…](https://ajuda.sankhya.com.br/hc/article_attachments/24126231499671) Se for configurado os campos **"Conta contábil"**, **"Cód. Centro de Resultado"** ou **"Cód. Projeto"** nos lançamentos contábeis (crédito ou débito) com as opções:

- R - Rateio;
- N - Rateio ou Financeiro.

E, no Construtor de Fórmulas for utilizada uma das seguintes fórmulas de itens:

- Formula.VLRDESCITEM
- Formula.VLRICMSITEM
- Formula.VLRIPIITEM
- Formula.VLRITEM
- Formula.VLRREPREDITEM
- Formula.VLRTOTITEM

Ao tentar salvar essa configuração, o sistema exibirá uma mensagem de aviso, permitindo a escolha de prosseguir ou cancelar a alteração:

**"A configuração de rateio nos campos Conta contábil, Cód. Centro de Resultado e Cód. Projeto, em conjunto com a fórmula para buscar valores dos itens, causará divergência na contabilização do lançamento. Deseja prosseguir com o cadastro?"**

![Imagem 6: Se nos lançamentos contábeis (crédito ou débito), os campos Conta contábil , Cód. Centro de Resultado ou Cód. Projeto…](https://ajuda.sankhya.com.br/hc/article_attachments/24126234870295) Se nos lançamentos contábeis (crédito ou débito), os campos Conta contábil, Cód. Centro de Resultado ou Cód. Projeto forem configurados de forma divergente, ou seja:

- Um dos campos foi configurado para buscar o rateio (**"R - Rateio"** ou **"N - Rateio ou Financeiro"**);
- Os demais campos foram configurados para buscar o produto (**"P - Produto"** ou **"Conta 1, 2, 3, 4 do Produto"**).

Ao salvar essas configurações, o sistema exibirá uma mensagem de aviso, permitindo a escolha de prosseguir ou cancelar a alteração:

**"A configuração conjunta de rateio e produto nos campos Conta contábil, Cód. Centro de Resultado e Cód. Projeto causará divergência na contabilização do lançamento.** **Deseja prosseguir com o cadastro?"**

![Imagem 7: Caso as configurações mencionadas nos pontos 01 e 02 sejam realizadas simultaneamente, isto é, ocorra a combinação de…](https://ajuda.sankhya.com.br/hc/article_attachments/24126234873879) Caso as configurações mencionadas nos pontos 01 e 02 sejam realizadas simultaneamente, isto é, ocorra a combinação de configurações divergentes entre rateio e produto com o uso de fórmulas de itens, será exibida uma mensagem de alerta, na qual o usuário pode decidir se deseja continuar ou cancelar o cadastro:

**"A configuração conjunta de rateio e produto nos campos "Conta Contábil", "Cód. Centro de Resultado" e "Cód. Projeto", aliada ao uso de fórmula de itens, pode causar divergências na contabilização do lançamento. Deseja prosseguir com o cadastro?"**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#top)

### Contas Flexíveis na Contabilização

Hoje o sistema conta um recurso que possibilita no processo de contabilização, a utilização de campos adicionais para determinar as contas contábeis. Pode-se fazer uso desta funcionalidade, nas contas de Parceiros, Parceiros Transportadora e Produtos.

**Observação:** para realização do procedimento abaixo, aconselhamos o acompanhamento de um consultor Sankhya.

Inicialmente na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) realize a criação de campos adicionais nas tabelas TGFPRO e TGFPAR, com as seguintes descrições:

- **"CODCTACTB3"** onde o número não pode ser maior que 99 (noventa e nove), e não pode ser criado com número contendo apenas uma casa, por exemplo, **"CODCTACTB3"**. Caso o campo seja criado maior que 99, ou com apenas uma casa, este não será apresentado no campo **"Conta Contábil"** na tela TOP Contabilização. Dessa forma, teremos o exemplo na imagem abaixo:

![Imagem 8: "CODCTACTB3" onde o número não pode ser maior que 99 (noventa e nove), e não pode ser criado com número contendo apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/28948187835927)

Note o campo adicional criado com a estrutura mencionada, disponível para uso no campo **"Conta Contábil"** na tela TOP Contabilização.

Na realização da contabilização na rotina de [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento), serão consideradas as contas especificadas no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) ou no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#top)

### Contextualizando sobre Fórmulas e Funções

**Observação:** quando o parâmetro **"HARMOCTXFORMULA"** for ligado, as expressões do construtor de fórmulas se tornarão mais intuitivas, sendo assim, será possível ter mais autonomia ao montar as expressões das regras de contabilizações.

Para a contabilização dos valores dos impostos como PIS, COFINS e CSLL, são disponibilizadas funções para cálculo dos impostos PIS, COFINS e CSLL que estão disponíveis no construtor de expressões do Sankhya-Om. Segue abaixo a descrição destas funções:

#### Para a nota:

getVlrPisNota(NUNota)

getVlrCofinsNota(NUNota)

getVlrCSLLNota(NUNota)

**Nota:** o campo **"Number"** gerado na expressão das funções acima é apenas informativo; por isso, deve ser retirado da função antes de salvá-la.

####

#### Para o item:

getVlrPisItem(NUNota,Sequencia)

getVlrCofinsItem(NUNota,Sequencia)

getVlrCSLLItem(NUNota,Sequencia)

####

#### Funcionalidade:

Na contabilização, os valores serão obtidos por meio da soma do campo VALOR da TGFDIN da ‘Nota’ ou do ‘Item’ em questão, de acordo com os códigos de imposto "TGFDIN.CODIMP":

CODIMP 6 à VLRPIS

CODIMP 7 à VLRCOFINS

CODIMP 9 à VLRCSLL

![Imagem 9: O valor do imposto apresentado se refere a toda Nota, não sendo discriminado por Produto ou por CST.](https://ajuda.sankhya.com.br/hc/article_attachments/28944764550295) O valor do imposto apresentado se refere a toda Nota, não sendo discriminado por Produto ou por CST.

#### Contabilização de Outros Impostos:

Deve-se utilizar as seguintes funções/fórmulas para contabilizar Outros Impostos:

- VALORIMPOSTOFIN(Cód.Imp,NUFin,(Base|Valor|Aliq.));
- VALORIMPOSTOCAB(Cód.Imp,NUNota,(Base|Valor|Aliq.)).

Na construção da função/fórmula VALORIMPOSTOCAB, informe:

- 'B' para base;
- 'V' para valor;
- 'A' para alíquota.

Na construção da função/fórmula VALORIMPOSTOFIN, caso seja indicado 0(Zero) significará todos, contabilizar todos os impostos.

Exemplos:

VALORIMPOSTOFIN(0,NUFin,'V') retornará a soma do valor do imposto da TGFIMF para o financeiro indicado.

VALORIMPOSTOCAB(1,NUNOTA,'B') voltará a base do imposto 1 da TGFIMN para a nota indicada.

#### Contabilização de frete extra-nota para Parceiro Transportadora.

Quando o campo **"Tipo de Conta Contábil"** estiver com a opção **"Variável"** indicada, o campo **"Conta Contábil"** apresentará também as opções de conta da Transportadora. Desse modo, estas representarão as contas contábeis dos parceiros transportadoras usados na nota lançada com esta TOP.

Ao lançar uma nota com a TOP configurada com um dos tipos de Conta contábil da Transportadora e o frete for Extra-Nota FOB, a contabilização desta nota gerará crédito/débito na referida conta contábil.

#### Contabilização dos impostos do DIFAL/FCP

Vejamos abaixo as fórmulas e funções responsáveis pela contabilização dos impostos do DIFAL/FCP:

#### **(1)** Fórmulas:

- VLRICMSDIFALDEST e LIVVLRICMSDIFALDEST - Deverá buscar o valor total do ICMS pertinente ao DIFAL do destino da nota fiscal;
- VLRICMSDIFALREM e LIVVLRICMSDIFALREM - Buscará o valor total do ICMS pertinente ao DIFAL do da nota fiscal;
- VLRICMSFCP e LIVVLRICMSFCP - Irá pesquisar o valor total do ICMS do FCP da nota fiscal;
- VLRICMSFCPINT e LIVVLRICMSFCPINT - Tem-se a busca do valor total do ICMS do FCP da nota fiscal;
- VLRSTFCPINT e LIVVLRSTFCPINT - Executa a busca pelo valor total do ST do FCP da nota fiscal;
- LIVVLRICMSCOMPL - Realizará a procura pelo valor total de complemento do ICMS daquela nota fiscal.

**Nota:** as fórmulas que iniciam a sua descrição com o termo "LIV", são referentes a tabela TGFLIV que registra os valores do livro fiscal.

#### **(1)** Funções

- GETVLRICMSITEM(NUNota,Sequencia) - Deverá buscar o valor total do ICMS do item, para aquela sequência.
- GETVLRIPIITEM(NUNota,Sequencia) - Buscará o valor total do IPI do item, para aquela sequência;
- GETVLRICMSDIFALDESTITEM(NUNota,Sequencia) - Irá pesquisar o valor total do ICMS do DIFAL do destino do item, para aquela sequência;
- GETVLRICMSDIFALREMITEM(NUNota,Sequencia) - Tem-se a busca do valor total do ICMS do DIFAL do remente do item, para aquela sequência;
- GETVLRICMSFCPITEM(NUNota,Sequencia) - Executa a busca pelo valor total do ICMS do FCP do item, para aquela sequência;
- GETVLRICMSFCPINTITEM(NUNota,Sequencia) - Realizará a procura pelo valor total do ICMS do FCP Interno do item, para aquela sequência;
- GETVLRSTFCPINTITEM(NUNota,Sequencia) - Deverá buscar o valor total da ST do FCP Interno do item, para aquela sequência;
- GETVLRSTITEM(NUNota,Sequencia) - Buscará o valor total da ST do item, para aquele produto;
- VALORIMPOSTODIN(CODIMP,NUNota,CODINC) - Tem-se a busca do valor total da base, alíquota ou o valor pertinente ao total do imposto e incidência definida (TGFDIN).

Na construção da função/fórmula VALORIMPOSTODIN, informe:

- 'B' para base;
- 'V' para valor;

Na construção da função/fórmula VALORIMPOSTOFIN, caso seja indicado 0(Zero) significará todos, contabilizar todos os impostos.

- Exemplos:

VALORIMPOSTODIN(1,NUNota,0,'B') retornará a base do imposto 1 (ICMS) de incidência geral da TGFDIN para a nota indicada;

VALORIMPOSTODIN(2,NUNota,1,'V') voltará o valor do imposto 2 (ICMS) de incidência do produto da TGFDIN para a nota indicada.

---

#### Imagem 10: Informações adicionais importantes para a rotina: Informações adicionais importantes para a rotina:

![Imagem 11: As variáveis para contabilização: VLRIPI, VLRICMS, VLRSUBST, VLRDESC, buscam os valores na TGFCAB (tabela de Notas).…](https://ajuda.sankhya.com.br/hc/article_attachments/24126231499671) As variáveis para contabilização: VLRIPI, VLRICMS, VLRSUBST, VLRDESC, buscam os valores na TGFCAB (tabela de Notas). Para contabilizar usando os itens, é imprescindível utilizar alguma informação, de itens na configuração da contabilização, bem como, Conta Contábil da CFOP dos itens ou Contas Contábeis dos Produtos.

Para valores dos itens tem-se as variáveis que podem ser utilizadas nas fórmulas (campo Fórmula):

- VLRTOTITEM, que representa: VLRTOT + VLRIPI + VLRSUBST – VLRDESC;
- VLRITEM, que representa: ((QTDNEG \* VLRUNIT) + VLRIPI + VLRSUBST -  LRDESC);
- VLRIPIITEM, com o valor do IPI do item;
- VLRICMSITEM, com o valor do ICMS do item;
- VLRDESCITEM, com o valor do desconto do item.

É possível utilizar o Código de Grupo de Produtos nas Fórmulas de Contabilização. Para isso, basta utilizar a expressão **"queTGFITE.CODGRUPOPROD"**.

![Imagem 12: Na coluna "Histórico" , a variável "|CT| Nome do Contato" , será utilizada para que se possa formatar o histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/24126234870295) Na coluna **"Histórico"**, a variável **"|CT| Nome do Contato"**, será utilizada para que se possa formatar o histórico contábil com o nome do "Contato" do parceiro. Com isso, na contabilização do título que utiliza a TOP com esta opção selecionada, o nome do "Contato" será adicionado no histórico do lançamento.

![Imagem 13: As variáveis |NP| e |RP| no campo "Histórico" trazem o mesmo valor, que pode ser Nome ou a Razão Social do Parceiro ,…](https://ajuda.sankhya.com.br/hc/article_attachments/24126234873879) As variáveis |NP| e |RP| no campo **"Histórico"** trazem o mesmo valor, que pode ser Nome ou a Razão Social do Parceiro, de acordo com o que estiver informado no parâmetro **"Apresentar Nome ou Razão Social do Parceiro - NOMERAZAOPARC"**. Já as variáveis |NO| e |RS| sempre irão apresentar o **"Nome do Parceiro"** e a **"Razão Social do Parceiro"**, respectivamente.

![Imagem 14: A variável NURENEG , só possui utilidade para a contabilização de " Renegociações "; ela não funciona na contabilização…](https://ajuda.sankhya.com.br/hc/article_attachments/24126231508375) A variável NURENEG, só possui utilidade para a contabilização de "Renegociações"; ela não funciona na contabilização de baixas e/ou financeiro.

![Imagem 15: Fórmula para Contabilização de devoluções:](https://ajuda.sankhya.com.br/hc/article_attachments/24126234878103) Fórmula para Contabilização de devoluções:

A contabilização de devoluções visa reverter a operação que originou a devolução. Para isso, é necessário utilizar, além dos dados presentes no documento de devolução, os custos da data do documento de origem na contabilização do movimento de devolução.

**(1)** **Devolução de Venda:**

Para obter os custos da data em que o documento de origem foi emitido (neste caso, a Nota de Venda), utilize as seguintes fórmulas na definição das regras de contabilização da nota de [Devolução de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#oqueumadevoluodevenda):

- Custo médio sem ICMS: `CUSTODEV.CUSMEDSEMICM`;
- Custo médio com ICMS: `CUSTODEV.CUSMEDCOMICM;`
- Custo de entrada sem ICMS: `CUSTODEV.ENTRADASEMICM`;
- Custo de entrada com ICMS: `CUSTODEV.ENTRADACOMICM`.

**(1)** **Devolução de Compra:**

Para obter os custos da data em que o documento de origem foi emitido (neste caso, a Nota de Compra), utilize as seguintes fórmulas na definição das regras de contabilização da nota de Devolução de Compra:

- Custo médio sem ICMS: `CUSTOORIGEM.CUSMEDSEMICM`;
- Custo médio com ICMS: `CUSTOORIGEM.CUSMEDCOMICM`;
- Custo de entrada sem ICMS: `CUSTOORIGEM.ENTRADASEMICM`;
- Custo de entrada com ICMS: `CUSTOORIGEM.ENTRADACOMICM`.

**(1)** **Para o correto funcionamento:**

Cálculo dos Custos:

A nota de origem deve ter os custos de entrada e custos médios calculados.

1. Amarração dos Itens:

Os itens da nota de devolução devem estar obrigatoriamente conectados à nota de origem (via TGFVAR).

2. Valores retornados:

Os custos retornados pelas fórmulas referem-se ao custo unitário na unidade de comercialização. Sendo então necessário multiplicar pelo valor da quantidade atendida na nota de devolução em relação à nota de origem, utilizando-se a variável **'QTDATENDIDA'**, que receberá a quantidade devolvida de uma Nota de Devolução.

**(1)** **Exemplo de fórmula:**

Contabilização para/devolução de venda considerando a fórmula CUSTODEV.CUSMEDSEMICM mais a variável **QTDATENDIDA**:

```
Fórmula: CUSTODEV.CUSMEDSEMICM * CUSTODEV.QTDATENDIDA
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#top)
