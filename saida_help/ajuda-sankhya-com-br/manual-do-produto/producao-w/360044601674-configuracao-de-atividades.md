---
id: "360044601674"
titulo: "Configuração de Atividades"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-22T15:43:06Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Operações de Estoque", "Apontamento", "Controle de Qualidade", "Atividades", "Configuração de Atividades", "Estoque", "Produtos (PA)", "Formulários", "Processo Produtivo", "Candidatos Executantes", "Inicialização de Repositório", "Lista de Materiais Alternativos", "Lista de MPs", "Lista de Subprodutos", "PERMITEDITLSTMP", "Recursos do Centro de Trabalho", "Tipo de Material", "Configuração de Atividades manual", "APOTARIFAMAT", "Produção", "br.com.sankhya.mgeprod.cad.composicao.produto", "Tipo de Tempo Unidade de Tempo Tipo de Reprocesso", "Processo Produtivo e Atividades", "Cálculo de Tempo por Quantidade Lote Fixo", "Qualidade"]
---

# Configuração de Atividades

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16646136232471) Módulo: Produção > Cadastros > Processo Produtivo - Botão Roteiro
```

---

Depois que você realizar o desenho do Processo Produtivo por meioda utilização do [Botão Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238714-Bot%C3%A3o-Roteiro), será necessário a configuração das atividades adicionadas ao fluxo. Para início desta configuração, efetue um duplo clique sobre a atividade, e a tela é direcionada para a interface de **"Configuração de Atividade"**.

Na nova tela que é aberta, na barra superior teremos o botão **"Voltar"** para que voltemos a interface para a folha de desenho do Processo caso necessário, e o **"Código/Descrição"** do processo em questão.

No lado esquerdo da tela, teremos uma grade denominada **"Itens do Roteiro"**, onde são exibidas todas as atividades do processo selecionado, facilitando a movimentação entre as atividades que se deseja configurar.

No centro da tela, o campo **"Código"**, juntamente com a descrição da atividade selecionada serão apresentados.

**Observação:** é possível visualizar no lado superior esquerdo da tela o botão **"Anexar"**, o seu acionamento possibilita a inserção de arquivos ou link's nas atividades do processo.

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abageral) |  | [A](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)[ba Produtos (](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)[PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa) |
| --- | --- | --- |
| [Aba Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaoperaesdeestoque) |  | [A](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento)[ba A](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento)[pontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento) |
| [Aba Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abacontroledequalidade) |  | [Aba Candidatos Executantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abacandidatosexecutantes) |
| [Aba Formulários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaformulrios) |  | [Aba Inicialização de Repositório](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abainicializaoderepositrio) |
| [Aba Recursos de Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abarecursosdecentrodetrabalho) |  |  |

##

## Aba Geral

Nesta aba são configurados os detalhes de cada atividade.

![Imagem 2: Nesta aba são configurados os detalhes de cada atividade.](https://ajuda.sankhya.com.br/hc/article_attachments/360097630313)

**Observação:** o Repositório de destino de uma atividade será resolvido a nível de execução, ou seja, o repositório de destino da atividade é encontrado pela aplicação durante a sua finalização e será o repositório de execução da próxima atividade. Desse modo, o mesmo é informado automaticamente pelo sistema, não sendo necessária a sua indicação manual.

O campo **"Repositório da operação"** deverá ser utilizado para definir o repositório de Produto Acabado ao qual o sistema irá utilizar na operação da atividade.

Referente ao campo **"Alocação de C. Trabalho"**, teremos que este especificará neste campo onde essa atividade deve ser executada (um Centro de Trabalho). A regra de alocação de Centro de Trabalho é vinculada anteriormente ao Processo Produtivo.

No campo **"Tipo de Tempo"** você indicará o tipo de tempo empregado no processamento da atividade. Tem-se as seguintes opções:

- **Por quantidade:** para quantidades diferentes do lote padrão é feita uma regra de três para encontrar o tempo da quantidade desejada;
- **Por lote:** nas quantidades diferentes do lote padrão, emprega-se o tempo da atividade a cada fração menor ou igual ao lote padrão;
- **Fixo:** O tempo de processamento será fixo.

Vejamos abaixo um exemplo:

Em um lote padrão = 1.000 UN

Tempo da atividade = 1,25 hora

Quantidade:

- Para uma OP com tam. lote igual à 2.750 UN o tempo da atividade será 3,43 hora;
- Para uma OP com tam. lote igual à 2.000 UN o tempo da atividade será 2,50 hora;
- Para uma OP com tam. lote igual à 1.500 UN o tempo da atividade será 1,8 hora;
- Para uma OP com tam. lote igual à 750 UN o tempo da atividade será 0,93 hora.

Lote:

- Para uma OP com tam. lote igual à 2.750 UN o tempo da atividade será 3,75 hora;
- Para uma OP com tam. lote igual à 2.000 UN o tempo da atividade será 2,50 hora;
- Para uma OP com tam. lote igual à 1.500 UN o tempo da atividade será 2,50 hora;
- Para uma OP com tam. lote igual à 750 UN o tempo da atividade será 1,25 hora.

Fixo:

- Para uma OP com tam. lote igual à 2.750 UN o tempo da atividade será 1,25 hora;
- Para uma OP com tam. lote igual à 2.000 UN o tempo da atividade será 1,25 hora;
- Para uma OP com tam. lote igual à 1.500 UN o tempo da atividade será 1,25 hora;
- Para uma OP com tam. lote igual à 750 UN o tempo da atividade será 1,25 hora.

Por meio do campo **"Unidade de tempo"**, determine a unidade de tempo utilizada para o tempo de atravessamento da atividade. As opções disponíveis são:

- Minutos;
- Horas;
- Dias.

Em **"Tempo da atividade"** está destinado a determinar o tempo padrão gasto para a execução da tarefa respeitando a Unidade de Tempo selecionada anteriormente. Esse campo será atualizado automaticamente caso você opte por alterar o  [Tamanho de Lote Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314?flash_digest=97b79c9c1458ea4e49542f1d68fbc925b632391d#pa-abageral).

Você utilizará o campo **"Tipo de reprocesso"** para determinar o tipo de reprocesso que a atividade pode iniciar. Pode-se definir dentre as seguintes opções:

- Não inicia reprocesso;
- Reprocesso c/ quantidade total;
- Reprocesso c/ quantidade parcial.

Em **"Status do processo"** defina qual o "status" do processo ao passar pela atividade. Teremos as seguintes opções de escolha:

- Mantém o status atual;
- Em andamento;
- Suspenso;
- Cancelado.

Utilizaremos o campo **"Usuário para logon"** para determinar um usuário para "logon" (entrada). Pode ser utilizado em atividades do sistema onde um "logon" seja necessário.

A marcação **"Lista de matéria-prima padrão"** determina, se a lista de matérias-primas desta atividade compõe o extrato de matérias-primas padrão para o produto.

Ao marcar o campo **"Libera centro de trabalho no final da atividade"**, será estabelecido que o Centro de Trabalho deverá ser liberado ao final da atividade.

A marcação do campo **"Libera centro de trabalho manualmente"** define se o Centro de Trabalho poderá ser liberado manualmente por você.

Quando você realizar a marcação do campo **"Inicializa repositório de produtos acabados"**, instaura-se que o repositório de Produtos Acabados será inicializado assim que a atividade for criada. Se ligado, o sistema irá iniciar o repositório de operação com todos os PA's a serem produzidos na ordem, de acordo com suas quantidades de lote. Se for necessário iniciar o repositório com componentes de manufatura, estes devem ser configurados na inicialização do repositório.

Defina no campo **"Execução Terceirizada"**, se a operação é executada em terceiros ou não. As possíveis opções de escolha são:

- **Nunca:** representa que essa operação nunca é executada em terceiros, mesmo que a Ordem de Produção esteja com alguma forma de terceirização.
- **Sempre:** ao contrário da opção anterior, esta representa que essa operação é sempre executada em terceiros. Esta opção só pode ser selecionada, caso o processo seja terceirizado.
- **Opcional:** esta marcação se refere ao fato de que você irá determinar, no momento da criação da Ordem de Produção, se a operação será terceirizada ou não.

**Observação:** esse campo ficará desabilitado se no [Cadastro do Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392213-Processo-Produtivo), o campo **"Produção para Terceiro"** presente na [aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392213-Processo-Produtivo#abageral), se encontre configurado com a opção **"Sempre"**.

A marcação **"Multi-turno"** quando acionada, permitirá que a execução da atividade seja realizada em múltiplos turnos por usuários diferentes, ou seja, o executante da atividade será capaz de parar o seu trabalho (fim do turno) e liberar esta atividade para outro usuário (novo turno).

O campo **"Motivo de parada (fim de turno)"** será preenchido com a justificativa pela qual está ocorrendo a parada do turno para troca de executantes. Sendo que, este campo só estará visível para configuração quando a marcação Multi-turno estiver habilitada. Além disso, os motivos de parada necessitam estar previamente configurados na tela [Motivos de Parada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232394-Motivos-de-Parada).

Por meio da marcação **"Considerar atividades de Setup no OEE"**, o sistema entenderá que a atividade de setup deverão ser consideradas nos cálculos do OEE, sendo estes realizados na tela [Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793#abaoee).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Produtos (PA)

Essa aba tem o objetivo permitir a realização da configuração da lista de matérias-primas, lista de subprodutos, lista de materiais alternativos, listas dos recursos e parceiros terceiros por atividade, relacionados ao processo produtivo.

Para a escolha do Produto Acabado que se deseja realizar tais operações, deve-se utilizar o campo **"Produto (PA)"** localizado no topo da aba. Ao clicar sobre a "lupa" localizada à frente do campo, é possível realizar uma pesquisa em todos produtos Produtos Acabados vinculados ao Processo Produtivo. Caso o produto em questão esteja configurado com controle adicional do tipo lista, o campo **"Controle (PA)"** será habilitado para seleção do mesmo.

**Observação:** é possível visualizar no lado superior esquerdo da aba o botão ![Imagem 3: Observação: é possível visualizar no lado superior esquerdo da aba o botão "Anexar" , o seu acionamento possibilita a…](https://ajuda.sankhya.com.br/guide-media/01H6748806TF4YTBWEJSKWJX68) **"Anexar"**, o seu acionamento possibilita a inserção de arquivos ou link's nos produtos (PA) do processo. Como por exemplo, um procedimento operacional padrão.

| [Sub-aba Lista de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistademps) |  | [Sub-aba Lista de Subprodutos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistadesubprodutos) |
| --- | --- | --- |
| [Sub-aba Recursos do Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abarecursosdocentrodetrabalho) |  | [Sub-aba Tempo de Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abatempodeprocessamento) |
| [Sub-aba Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abatarifascip) |  | [Sub-aba Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abaterceiros) |

#### Sub-aba Lista de MPs

Esta aba está destinada a construção da lista de materiais necessários para o processamento da atividade. Esses materiais, em geral são matérias-primas e insumos que depois de utilizados, agregam valor ao produto acabado.

![Imagem 4: Esta aba está destinada a construção da lista de materiais necessários para o processamento da atividade. Esses…](https://ajuda.sankhya.com.br/hc/article_attachments/16646136245783)

Quando a lista estiver ligada a um subprocesso (embarcado ou não), todos os materiais existentes na lista (considerando os Produtos Acabados em processamento) serão enviados ao subprocesso como lista de Produtos Intermediários a serem produzidos naquele processo. O subprocesso por sua vez, deve suportar todos os produtos que por ventura possam ser enviados para processamento nele.

O campo **"Matéria-prima"** deve ser utilizado para determinar o material que você deseja adicionar à lista de materiais do produto acabado selecionado.

![Imagem 5: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16646162247191) **Informações adicionais:**

1. O parâmetro **"Permitir definir produto como MP de si próprio. - PRODMPPROP"** quando habilitado, permitirá que o produto seja cadastrado como Matéria-prima de si mesmo.
2. Tratando-se de um processo de reprocessamento/reparo, é possível que um produto seja utilizado como matéria-prima de si mesmo.
3. Para que seja possível realizar a vinculação de um produto inativo como matéria-prima, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

**Importante:** no processo produtivo ao se inserir a mesma matéria-prima para o mesmo Produto (PA) em duas atividades diferentes, as seguintes configurações deverão estar idênticas:

- Unidade;
- Local de Origem;
- Local de Baixa;
- Tipo de Uso do Material;
- Fixar qtd. apontada para uma mesma MP ao editar qtd. apontada do PA.

Caso seja apresentada alguma diferença nas referidas configurações, não será concluído o processo de inclusão sendo exibida a  seguinte mensagem:

**"'Unidade', 'Local de Origem', 'Local de Baixa', 'Tipo de Uso do Material, 'Fixar qtd. apontada para uma mesma MP ao editar qtd. apontada do PA' devem ser iguais para uma mesma MP dentro do processo para um mesmo PA."**

O campo **"Tipo Controle (MP)"** deve ser utilizado para determinar qual o tipo do controle do produto. Pode-se definir dentre as seguintes opções:

- **Automático:** O módulo de produção irá utilizar as regras do ERP para determinar o controle deste material. Esta marcação é útil principalmente em casos de Matérias-Primas controladas por lote; desta forma o sistema pode executar o FEFO (First-Expire, First-Out), dependendo da configuração do material.

![Imagem 6: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16646162247191) **Informações adicionais:**

1. Caso exista alguma movimentação de estoque configurada para "Validar estoque p/ Reserva", será necessário que você aponte o lote que está de fato sendo consumido, pois a reserva em questão irá acontecer para um lote específico da matéria-prima.
2. **Sugestão de lote no apontamento:** quando a Ordem possui movimentações acessórias (nota de transferência, requisição que reserva estoque, etc) para MPs controladas por lote, as rotinas de apontamento (Operações de Produção e Apontamento de Produção) sugerem os lotes movimentados no momento do apontamento, evitando assim divergência entre a movimentação de estoque da Ordem e os Apontamentos.
3. **Explosão de lote automática:** quando a Ordem não possui nenhuma movimentação acessória para MPs controladas por lote, ao fazer apontamento não especificando um lote o sistema realizada a explosão de lote automática, ou seja, a nota de produção gerada recebe lote das MPs automaticamente conforme FEFO. Sendo que neste cenário as rotinas de Apontamento não sugerem lote.
4. Com o parâmetro **"Aponta Tarifa junto com Materiais. - APOTARIFAMAT"** ligado, a configuração das [Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074) poderão ser realizadas através da tela [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto), aba [Matérias-Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abamat%C3%A9rias-primas), e o apontamento de Tarifas CIP feito juntamente com o apontamento de materiais.

- **Literal:** caso a Matéria-Prima possua controle adicional de estoque, o valor deve ser definido literalmente.
- **Herdar do PA:** por meio desta opção, o controle da Matéria-Prima será o mesmo do Produto Acabado que está sendo processado.

Este campo só pode ser configurando quando o Produto e o Subproduto (Ou MPs) estão configurados com controle adicional de estoque do tipo Lista.

Teremos no campo **"Referência do Produto"** o conteúdo do campo **"Referência"** presente na aba Geral do [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-).

**Importante:** quando o parâmetro **"Permitir editar Lista de MPs de produtos em fabricação - PERMITEDITLSTMP"**estiver ativado, você poderá editar a Lista de MPs e os Materiais Alternativos de um produto acabado mesmo que já existam Ordens de Produção criadas para aquele produto/processo.

**Observação:** ao habilitar o parâmetro **"Visualizar total da quantidade de MP na grade - VISUTOTALQTDMP"**, será exibido no rodapé da grade (coluna **"Quantidade"**) o totalizador da quantidade das MPs utilizadas nesta atividade.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Material

Teremos nesta aba, os Materiais que irão compor a Lista de Materiais essenciais para o processamento da atividade.

No campo **"Tipo de Uso do Material"** você deverá especificar o tipo de uso do material nas Ordens de Produção lançadas para esse processo produtivo. Assim, o sistema terá as seguintes opções:

- **Reaproveitamento em Desmonte:** Esta opção poderá ser utilizada somente em processos de desmonte, e ela determina que esse material será reaproveitado (ou resgatado) quando a Ordem de Produção de desmonte for executada. Materiais reaproveitados são devolvidos ao estoque quando se efetua o lançamento de uma nota de produção de desmonte.
- **Usada na Operação normal:** Este tipo de material é utilizado na operação normal do Produto Acabado (independente de ser reprocesso ou não) e as Matérias Primas deste tipo, fazem parte do "bom" do produto.
- **Usada em Ajustes:** Esse tipo de material é utilizado em ajustes do Produto Acabado, ou seja, não fazem parte da formulação do produto, mas podem ser utilizados para realizar ajustes técnicos, como por exemplo, em indústrias químicas. Esse tipo de material não aparece no formulário normal de apontamento, mas sim em um formulário específico e com isso, deve fazer parte da nota de produção.

**Observação:** o mesmo material não pode ser utilizado na operação Normal e na operação em Ajustes para o mesmo Produto Produto Acabado.

No **"Tipo de Quantidade"**, determine como o sistema deve calcular a quantidade desse material para a produção do produto acabado. O valor calculado será inicializado no formulário de apontamento de Matérias-Primas, e depois tem-se a liberdade de modificá-lo conforme desejado. As opções disponíveis são:

- **Fixa:** Será utilizada sempre a quantidade determinada no campo "Quantidade".
- **Variável:** A quantidade será variável em função da quantidade produzida.

Determine no campo **"Quantidade"**, a quantidade da matéria-prima para a produção do Produto Acabado.

O campo **"Unidade"** é destinado para a definição da unidade de medida a ser utilizada pelo material.

A marcação **"Verifica Estoque"** determina se esta matéria-prima deve ter o estoque validado em transições condicionais vinculadas a essa atividade (seu uso mais comum é para verificação do estoque de Produtos Intermediários).

Quando você realizar a marcação do campo **"Gera Requisição"**, será determinado que o sistema irá incluir esse material nas operações de estoque comandadas para os materiais dessa atividade.

Ao efetuar a marcação do campo **"Fixar qtd. apontada da MP ao editar qtd. apontada do PA"**, fixa a quantidade apontada de Matéria-Prima quando se efetua uma edição da quantidade apontada de Produto Acabado. Quando for realizada uma alteração na quantidade apontada, o sistema verifica esta marcação para realizar a respectiva proporcionalização das Matérias-Primas para os registros nos quais, ela não esteja assinalada, será calculada a proporcionalização.

No campo **"Local de Origem"** seleciona-se o local de origem utilizado para a requisição da matéria-prima.

O campo **"Local de Baixa"** é empregado na seleção do local para baixa desse material em notas de produção.

Por meio da marcação **"Material consumido por refugo"** será determinado se o material da Lista de MP's em questão foi consumido por refugo. Lembrando que refugo é um Produto Acabado ou um Produto em Processamento que está fora das especificações técnicas aceitáveis pela fábrica. Um refugo pode ser gerado por qualquer atividade do processo produtivo de um Produto Acabado.

**Observação:** os materiais assinalados como consumidos por refugo, também serão incluídos na nota de produção do Produto Acabado, ou seja, a matéria prima apontada será distribuída entre a **"Qtd. apontada"** e a **"Qtd. Perda"** do PA. Portanto, ao realizar a marcação acima, a perda do PA nos apontamentos deve ser realizada manualmente, pois se a perda for gerada pelo sistema, o consumo da matéria prima nas notas de produção e refugo permanecerão incorretas, visto que, a grade de MP não é ajustada ao gerar a perda pela confirmação do apontamento.

Quando a opção **"Vínculo direto com série do PA"** for assinalada,  o sistema terá a obrigatoriedade de vincular as séries da matéria-prima apontada com uma série já apontada do Produto Acabado, isto se o PA também for controlado por número de série. Esta opção deve ser utilizada se o PA ao qual a Matéria-Prima está vinculada, também for controlado por número de série.

A matéria-prima que possuir a marcação **"Estoque de terceiro"**, encontra-se em poder da empresa, mas pertence a terceiros. Sendo que, a sua atualização irá respeitar a configuração contida no campo **"Estoque com/de Terceiros"**, localizado na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Estoque de terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Desvios

Em **"% Desvio Inferior"** é destinado a especificar o % de limite inferior de consumo desta Matéria-Prima em relação à quantidade padrão (definida anteriormente no campo **"Quantidade"**). O sistema não permitirá apontamentos que ultrapassarem este limite.

**% Desvio Superior:** De forma contrária ao campo anterior, especificar-se aqui o % de limite superior de consumo desta Matéria-Prima em relação à quantidade padrão (definida anteriormente no campo **"Quantidade"**). O sistema não permitirá apontamentos que ultrapassarem este limite.

**Nota:** no cálculo do % desvio de consumo de MPs, as MPs alternativas serão consideradas proporcionalmente. Deste modo, a quantidade consumida da MP será:

O consumo da MP + o consumo da MP alternativa (convertida na MP principal)

Ao selecionar a marcação **"Solicitar liberação ao exceder desvio"**, o sistema irá solicitar a liberação em todo caso em que a quantidade informada na coluna **"Qtd. apontada"** (Tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025393153-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o), Aba Apontamentos, sub-aba [Materiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025393153-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaapontamentos)) for superior ou inferior ao registrado nos campos descritos acima.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Liberação de desvios

Quando o valor da Qtd. apontada de MP for informado manualmente (em Operações de Produção e Apontamento de Produção), e você confirmar este apontamento por meio do botão **"Confirmar"**, caso o percentual de desvio seja diferente daquele informado na aba Desvios, o sistema abrirá o pop-up **"Liberações solicitadas"**, para que você possa verificar as informações e informar um usuário liberador no campo **"Liberador".**

Ao clicar em salvar, note a mensagem ao lado do botão confirmar:

**"Apontamento pendente, com solicitação de liberação"**

Ao solicitar a liberação, será executada na tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234914-Libera%C3%A7%C3%A3o-de-Limites) pelo usuário liberador de tal processo, sendo assim, ao clicar no botão **"Liberar"** o sistema permitirá que o apontamento possa ser confirmado posteriormente nas telas de Operações de Produção ou Apontamento de Produção.

Na tela Liberação de Limites, no Painel de Filtros, informe o usuário e a senha do liberador do evento em questão para que este seja filtrado.

Caso o referido usuário negar a solicitação de liberação de desvio, não será possível confirmar o apontamento. Assim, remova o apontamento e realizar um novo.

**Nota:** para apontamentos de desvios que possuam mais de uma divergência, os valores destes deverão ser informados um a um no campo Qtd. Apontada para que sejam salvos e, em seguida, estas serão aprovadas ou negadas individualmente na tela de Liberações de Limites.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Materiais Alternativos

A lista de materiais permitirá a produção de um determinado PA a partir de uma variação de materiais devido a uma falta de estoque, por exemplo. Porém, essa variação de materiais impacta na operação da produção, visto que podem existir operações de estoque que consideram essa lista de materiais.

Defina em **"Material Alternativo"**, o material a que deseja adicionar a lista de materiais alternativos da Matéria-Prima.

**Nota:** para que seja possível realizar a vinculação de um produto inativo como material alternativo, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

Teremos no campo **"Referência do Produto (Alternativo)"**, o conteúdo do campo **"Referência"** presente na aba Geral do [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-), neste caso, referente ao produto alternativo.

Informe em **"Quantidade"**, a Quantidade do Material Alternativo relativa a uma unidade do Material Principal a qual ele está ligado.

Informe a Unidade de medida a ser utilizada quando for considerado o material alternativo no campo **"Unidade"**.

Informe no campo **"Conjunto"**, os números do conjunto que deve ser utilizado em caos em que a matéria-prima é substituída por vários materiais alternativos ao mesmo tempo. Com isso, esses materiais alternativos devem fazer parte do mesmo conjunto.

No campo **"Local de Origem"**, você poderá informar o local de origem para todas as movimentações de estoque do material com exceção da nota de produção, ou seja, nas movimentação acessórias.

Você poderá inserir no campo **"Local de Baixa"**, o local que será utilizado para as movimentações de estoque do material exclusivamente em notas de produção.

**Importante:** o local informado nos campos Local de Origem e Local de Baixa é um nível de configuração acima do local inserido nos campos Local de Origem e Local de Baixa da operação de estoque, sendo assim, se preenchido será utilizado como local de movimentação do produto por uma operação de estoque do processo ao invés do local configurado nela. Portanto, deve ser preenchido somente em exceções em que o local do material seja diferente daquele informado na Operação de Estoque.

**Nota:** você poderá visualizar os locais cadastrados aqui na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o), aba **"Mov. Acessórias"** grade Itens.

**Importante:** os campos Local de Origem e Local de Baixa desta aba só estarão disponíveis a partir da versão 4.4.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Lista de Subprodutos

Configure nessa aba a lista de subprodutos (ou scrap's) criados com o processamento das matérias-primas na atividade. Uma operação pode gerar diversos subprodutos, cuja quantidade é geralmente uma função da quantidade de Produto Acabado processado.

O campo **"Subproduto"**, deve ser utilizado para determinar o material que você deseja adicionar a lista de materiais do produto acabado selecionado.

**Nota:** para que seja possível realizar a vinculação de um produto inativo como subproduto, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

Determine  em **"Tipo de Controle"**, qual o tipo do controle do produto. Tem-se as seguintes opções para escolha:

- **Literal:** caso o subproduto possua controle adicional de estoque, o valor deve ser definido literalmente.
- **Herdar do PA:** definindo-se por esta opção, o controle do subproduto será o mesmo do Produto Acabado que está sendo processado.

Este campo só pode ser configurando quando o Produto e o Subproduto (Ou MPs) estão configurados com Controle Adicional de estoque do tipo Lista.

O campo **"Controle"** será apresentado apenas quando o subproduto selecionado possuir controle adicional por lista. Aqui determine qual o controle da matéria-prima vinculada a produção do produto.

Por meio do campo **"Tipo de Quantidade"** determine como o sistema deve calcular a quantidade desse produto para a produção do produto acabado. O valor calculado será inicializado no formulário de apontamento de Subproduto e em seguida, teremos a liberdade de modificá-lo como desejado. Pode-se definir dentre as seguintes opções:

- **Fixa:** o sistema utiliza sempre a quantidade determinada no campo "Quantidade".
- **Variável:** a quantidade será variável, ou seja, em função da quantidade produzida.

O campo **"Quantidade"** deve ser utilizado para determinar a quantidade da matéria-prima pra a produção do Produto Acabado.

Utilize a **"Unidade"** para o preenchimento da unidade de medida a ser utilizada pelo material.

A marcação **"Exige Apontamento"** determinará a obrigatoriedade do apontamento para essa matéria-prima.

Defina no campo **"Local de Destino"**, o local de estoque do subproduto. Quando informado, este local será utilizado em notas de subprodutos. Se não informado, o sistema usa o local informado na própria operação de estoque (local de origem).

Por meio da marcação **"Subproduto por Perda/Refugo"** você definirá se o subproduto em questão se trata ou não de perda/refugo. Por padrão, esta marcação não será exibida marcada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Recursos do Centro de Trabalho

Esta aba tem a finalidade de permitir a determinação de uma lista de categorias de recursos Centro de Trabalho que são necessários para o processamento da atividade. Dessa forma, tem-se um resumo de recursos e suas respectivas quantidades necessárias para o processamento de determinado Produto Acabado, tornando possível a visualização dessa informação em relatórios ou demonstrativos de formulação.

No campo **"Categoria de Recurso"** determine uma categoria de recurso. Pode ser informada qualquer categoria, independentemente desta ser analítica ou sintética. Em listagens onde o sistema apresenta formulação juntamente com outros insumos, pode-se agrupar essas categorias pelo tipo da categoria (máquina, mão de obra, equipamento).

Defina em **"Quantidade de Utilização"** a quantidade (em minutos) da utilização deste recurso no processamento desta atividade.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Tempo de Processamento

Nesta aba será definido o tempo de processamento de um produto na atividade em questão. Este cadastro deverá ser utilizado nas situações onde o tempo da atividade é variável para cada um dos produtos processados no processo, assim como podem variar em função do Centro de Trabalho que será utilizado.

**Observação:** quando Centro de Trabalho não for informado, o sistema especificará automaticamente o valor zero. Isso significa que este é um tempo genérico de processamento do produto naquela atividade, ou seja, para qualquer Centro de Trabalho utilizado o tempo será o mesmo.

No campo **"Tipo de Tempo"** será indicado o tipo de tempo empregado no processamento da atividade. Tem-se as seguintes opções:

- **Por quantidade:** para quantidades diferentes do lote padrão é feita uma regra de três para encontrar o tempo da quantidade desejada;
- **Por lote:** nas quantidades diferentes do lote padrão, emprega-se o tempo da atividade a cada fração menor ou igual ao lote padrão;
- **Fixo:** o tempo de processamento será fixo.

Vejamos abaixo um exemplo:

Em um lote padrão = 1.000 UN

Tempo da atividade = 1,25 hora

Quantidade:

- Para uma OP com tam. lote igual à 2.750 UN o tempo da atividade será 3,4375 hora;
- Para uma OP com tam. lote igual à 2.000 UN o tempo da atividade será 2,50 hora;
- Para uma OP com tam. lote igual à 1.500 UN o tempo da atividade será 1,875 hora;
- Para uma OP com tam. lote igual à 750 UN o tempo da atividade será 0,9375 hora.

Lote:

- Para uma OP com tam. lote igual à 2.750 UN o tempo da atividade será 3,75 hora;
- Para uma OP com tam. lote igual à 2.000 UN o tempo da atividade será 2,50 hora;
- Para uma OP com tam. lote igual à 1.500 UN o tempo da atividade será 2,50 hora;
- Para uma OP com tam. lote igual à 750 UN o tempo da atividade será 1,25 hora.

Fixo:

- Para uma OP com tam. lote igual à 2.750 UN o tempo da atividade será 1,25 hora;
- Para uma OP com tam. lote igual à 2.000 UN o tempo da atividade será 1,25 hora;
- Para uma OP com tam. lote igual à 1.500 UN o tempo da atividade será 1,25 hora;
- Para uma OP com tam. lote igual à 750 UN o tempo da atividade será 1,25 hora.

Será determinado no campo **"Tempo da atividade"** o tempo padrão gasto para a execução da tarefa respeitando a Unidade de Tempo selecionada anteriormente. Esse campo será atualizado automaticamente caso você opte por alterar o  [Tamanho de Lote Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314?flash_digest=97b79c9c1458ea4e49542f1d68fbc925b632391d#pa-abageral).

Por meio do campo **"Unidade de Tempo"**, determine a unidade de tempo utilizada para o tempo de atravessamento da atividade. As opções disponíveis são:

- Minutos;
- Horas;
- Dias.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub -aba Tarifas CIP

Nesta aba são inseridas as Tarifas CIP (Custo Indireto de Produção), que para serem aqui apresentadas, devem ter sido previamente incluídas no [Cadastro de Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025397373-Tarifas-CIP).

Nas telas [Filtro para cálculo CIP (Financeiros)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025241694-Filtro-para-c%C3%A1lculo-CIP-Financeiros-) ou [Filtro para cálculo CIP (Requisições)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392773-Filtro-para-c%C3%A1lculo-CIP-Requisi%C3%A7%C3%B5es-), determine a regra a qual aquela tarifa sofrerá alteração em seu custo. Assim, considere o exemplo:

Financeiros gerados para a "Empresa 1", cuja natureza seja "Energia Elétrica" geram alterações no custo da Tarifa 1.

Em um dado momento o custo real da tarifa pode ser calculado e atualizado considerando-se "os filtros p/ cálculo de custo" (Cálculo de custo baseado no Financeiro/Requisição).

Nesta aba, realize o vínculo de uma ou várias tarifas na atividade selecionada.

Informe em **"Tarifa"** a tarifa que será configurada para a atividade.

Especifique em **"Índice"**, a quantidade da tarifa por unidade produzida.

O campo **"UN. Consumo"** será destinado a especificar a unidade de consumo para a tarifa nesta atividade.

Em **"Tipo de Índice"** você poderá determinar o tipo de índice da tarifa vinculada com a atividade. Tem-se as seguintes opções:

- **Fixo:** O índice da tarifa será fixo;
- **Variável (Execução de atividades):** O índice da tarifa será variável em função do tempo de execução das atividades da OP.

Utilize o campo **"Tipo de Execução"** para determinar o tipo de execução que será considerado. Este campo só ficará visível quando o campo Tipo de Índice estiver configurado com a opção Variável (Execução de atividades).

- Parada;
- Todos;
- Normal.

![Imagem 7: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16646162247191)**Informações adicionais:**

1. Tendo-se tarifas em comum no Processo e na Atividade, a tarifa da Atividade terá prioridade. Sendo que, se a tarifa estiver configurada no Processo como "Variável" e a mesma não existir nas Atividades, o índice gerado será em função da execução de cada uma das Atividades;
2. No primeiro apontamento será utilizada a data de início da atividade como data início do filtro de execuções.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa)

#### Sub-aba Terceiros

Esta aba será habilitada, caso no [Cadastro do Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392213-Processo-Produtivo), o campo Usa Terceiro presente na [aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392213-Processo-Produtivo#abageral) for definido com a opção **"Sempre"**. Além disso, na mesma aba, o campo Definição de Terceiro deve estar definido com a opção **"Por Operação"**.

Nela, determine o Parceiro Terceiro correspondente ao produto, bem como se este for o Parceiro Terceiro Preferencial do item em questão. Será possível configurar apenas um parceiro preferencial para cada produto.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Operações de Estoque

Nessa aba são configuradas as operações com estoque que irão ocorrer automaticamente no decorrer da atividade do Processo Produtivo.

Essas operações podem ser de qualquer tipo (pedidos, notas, requisições, transferências etc). Cada atividade pode possuir um número infinito de operações, que podem ocorrer em vários momentos diferentes do ciclo de vida da atividade. A coerência entre as diversas operações que ocorrem em uma atividade, é de responsabilidade do configurador do processo.

Você poderá selecionar diversos tipos diferentes de itens que irão compor estas operações com estoque, por exemplo, as Matérias-Primas necessárias na atividade, produtos acabados apontados na atividade, subprodutos gerados na atividade etc.

O campo **"Ordem"** deve ser utilizado para determinar a ordem em que as operações serão executadas dentro da atividade. Sendo que, não será possível inserir a mesma numeração de Ordem, para duas Operações de Estoque distintas em uma mesma atividade.

Informe no campo **"Descrição da Operação"** uma descrição para identificar a operação. Caso não seja inserida nenhuma informação nesse campo, o sistema buscará a descrição do Tipo de Operação inserido na seguinte ordenação:

- Caso exista descrição no campo Tipo de Operação, utilizará a descrição deste, senão;
- Existindo descrição no campo Tipo de Operação para Perda, será usada a descrição deste;
- Em último momento, utilizará a descrição da TOP do Modelo da Nota definido nesta operação.

O campo **"Tipo de Execução da Operação"** definirá a maneira que a operação de estoque será realizada, sendo elas:

- Automática;
- Manual;
- Ambas.

Ao selecionar a opção Manual, a marcação **"Obrigatória"** será exibida na tela e o campo **"Quando"** será desabilitado. Ao acionar a referida marcação, a operação de estoque deverá ser executada antes da finalização da Atividade/Ordem de Produção.

**Observação:** o campo Tipo de Execução da Operação só poderá ter a opção Manual selecionada quando o **"Tipo dos Itens"** for relacionado à matéria-prima, caso contrário, o sistema exibirá a seguinte mensagem:

**"Tipo de execução da operação igual a 'Manual' ou 'Ambas' é possível somente quando o Tipo dos Itens for referente a matéria-prima (Lista de materiais da atividade/OP)".**

Por meio do campo **"Tipo de Produção"**, defina quando a operação de estoque será executada. Tem-se as seguintes opções:

- Ambas;
- Para terceiros - Quando a OP for uma ordem de produção para terceiros;
- Para estoque próprio - Quando a OP for uma ordem de produção própria (produção para estoque próprio).

O campo **"Quando"** será utilizado para determinar o momento em que a operação de estoque deve ser gerada. Dessa forma, você poderá selecionar uma dentre as seguintes opções:

- **Saída:** define que a operação de estoque irá acontecer quando a atividade for encerrada.
- **Ao preencher um formulário:** determina que a operação de estoque deve acontecer quando for finalizado o preenchimento de um formulário. Não implementada.
- **Ao apontar PA:** esta opção representa que a operação de estoque irá acontecer quando o Produto Acabado for apontado.
- **Quando o usuário iniciar a atividade:** esta marcação estabelece que a operação deve acontecer quando a atividade for iniciada pelo usuário.
- **Entrada:** define que a operação de estoque irá acontecer quando a atividade for criada.
- **Aceite da atividade:** determina que a operação de estoque deve acontecer no aceite da atividade pelo usuário.
- **Ao apontar materiais de ajustes:** esta opção representa que a operação de estoque deve acontecer quando forem apontados os materiais de ajuste pelo usuário.

Os modelos apresentados aqui, deverão ser previamente cadastrado na tela **"Comercial > Consulta > Modelo de Notas e Pedidos"**.

Determine no campo **"Atividade Base"**, a atividade que será utilizada como base da operação. **Informe o código da atividade que estão configurados os itens que deverão ser movimentados.**

No campo **"Parceiro"** selecione um parceiro para ser utilizado na operação de estoque; caso o campo não seja preenchido, o sistema irá utilizar o parceiro da nota modelo.

Teremos em **"Centro de Resultado"** o Centro de Resultado que será utilizado na operação de estoque. Caso ele não seja preenchido, o sistema irá utilizar o Centro de Resultado da nota modelo.

Selecione no campo **"Projeto"**, um projeto a ser utilizado na operação de estoque; caso não seja preenchido, o sistema irá utilizar o projeto da nota modelo.

Em **"Natureza"** será definido uma natureza a ser utilizada na operação de estoque; caso esse campo não seja preenchido, o sistema irá utilizar a natureza da nota modelo.

O campo **"Tipo de Negociação"** deverá ser utilizado pelo usuário para selecionar um tipo de negociação para ser utilizado na operação de estoque, caso esse campo não seja preenchido o sistema utilizará o tipo de negociação da nota modelo.

Defina em **"Tipo de Operação"**, uma TOP a ser utilizada na operação de estoque; caso esta não seja informada, o sistema irá utilizar a TOP da nota modelo.

Determine no campo **"Tipo de Operação para Perda"** o Tipo de Operação a ser utilizado nas Perdas correspondentes às Operações de Estoque no Processo Produtivo. Este campo poderá ser utilizado caso o campo **"Tipo dos Itens"** esteja definido como Subproduto da Atividade. Poderão ser selecionados aqui, Tipos de Operação do Tipo de Movimento **"F - Produção"**.

O campo **"Local de Origem"** é destinado a determinar o local de origem para os itens da operação de estoque. Caso esse valor não seja informado, ele receberá **"0"** (zero) por padrão, e o material sendo controlado por local, o sistema irá utilizar como local o "Local de origem" do Processo Produtivo.

Em **"Local de Destino"** determine o local de destino para os itens para a operação de estoque. Caso esse valor não seja informado, ele receberá **"0"** (zero) por padrão, e o material sendo controlado por local, o sistema irá utilizar como local o Local de Destino do Processo Produtivo.

Informe no campo **"Local de Destino para Perda"**, o local de destino na ocorrência de perdas. Caso não seja especificado um valor neste campo, automaticamente o mesmo será alimentado com o valor "0" (Sem local). Este estará habilitado para uso, caso tenha-se especificado um Tipo de Operação para Perda.

Determine no campo **"Local para baixa de MPs"**, o local de baixa de Matérias-Primas sempre que a operação de estoque corresponder a uma nota de produção. Quando este campo não for informado (valor = "0"), o sistema irá buscar o local com a seguinte regra: **1º** - Local do Centro de Trabalho, **2º** - Local de Manufatura, definido no cabeçalho do processo.

Em **"Empresa Origem"** determine a empresa de origem que será utilizada para a operação de estoque.

Diferente do campo anterior, em **"Empresa Destino"** você informará aqui, a empresa de destino da operação de estoque. Seu preenchimento é necessário, apenas quando a operação de estoque seja uma transferência. Caso não seja informada, será utilizada a empresa de origem da operação de estoque.

O campo **"Tipo dos Itens"** será utilizado para determinar o que será utilizado como itens no movimento. Sendo assim, pode-se definir dentre as seguintes opções:

- **Subproduto da Atividade**: será utilizada a quantidade de subproduto apontada, menos à quantidade que já tenha sido movimentada.
- **Produto acabado apontado na atividade:** a lista de materiais será a soma de todos os apontamentos feitos até o momento, independente da atividade onde tenham sido apontados. Esta marcação é útil em situações onde se aponta Produtos Acabados em diversas atividades, mas deseja-se gerar a nota de produção apenas no final do processo.
- **Lista de materiais de todas as atividades:** quando utilizar-se esta opção, o sistema irá considerar apenas atividades do fluxo principal. Geralmente se utiliza essa opção em atividades no início do processo. Selecionando-se esta opção, todas as Matérias-Primas serão multiplicadas pela quantidade de Produto Acabado presentes na lista de Produtos Acabados a produzir na instância do processo, sempre subtraindo a quantidade já utilizada em um registro de operação com estoque do processo.
- **Materiais de ajuste:** o sistema irá utilizar materiais de ajuste presentes no apontamento de materiais deste tipo. Somente deve ser utilizado em conjunto com o campo **"Quando"** marcado como **"Ao apontar materiais de ajustes"**.
- **Lista de materiais da atividade base:** a quantidade de cada matéria-prima será multiplicada pela quantidade de Produto Acabado presente atualmente no repositório de entrada, subtraindo a quantidade utilizada em operações anteriores. Caso o repositório não possua Produto Acabado, será utilizada a quantidade a ser produzida.

**Importante:** nos casos em que o campo **"Tipo dos Itens"** estiver definido como **"Lista de materiais de todas as atividades"** ou **"Lista de materiais da atividade base"**, será apresentado logo abaixo deste, o campo **"Tipo de Material"** que tem como objetivo, fazer com que o sistema, de acordo com a opção selecionada, respeite este valor na geração de notas de produção, de modo que os itens que irão para a nota serão aqueles em conformidade com esta informação. Tem-se as seguintes opções:

- **Ambos:** as notas serão geradas tanto para os PI's, quanto para as MP's;
- **Somente MPs:** as notas geradas terão nos itens apenas as MP's;
- **Somente PIs:** as notas geradas terão nos itens apenas os PI's.

Determine no campo **"Selecionar Impressora"**, a impressora que será selecionada nas operações de estoque. As opções disponíveis são:

- Conforme a TOP;
- Específica;
- Usar impressora Padrão do Centro de Trabalho.

O campo **"Impressora"** é destinado a informar-se o nome ou apelido de uma impressora a qual deseja-se imprimir documentos da atividade.

Determine em **"Status da Execução"**, em qual "status" de execução a operação será concretizada. As opções disponíveis para escolha são:

- **Todos:** ao marcar esta opção, a operação será executada em todas as situações.
- **Normal:** essa opção faz com que a operação seja executada apenas quando a atividade estiver sendo efetivada em situações normais.
- **Reprocesso:** através desta opção, a operação será executada apenas quando a atividade estiver sendo efetuada em situações de reprocesso.

O campo **"Formulário"** será habilitado apenas quando o momento da operação de estoque for ao preencher formulário. O sistema irá utilizar o valor dos campos do formulário sempre que encontrados. Os campos que serão considerados serão:

- CODPARC
- CODCENCUS
- CODPROJ
- CODNAT
- CODTIPVENDA
- CODTIPOPER
- CODLOCALORIG
- CODLOCALDEST
- CODEMPORIG
- CODEMPDEST

Se um campo não for encontrado no formulário, então este será ignorado e o valor utilizado será o da operação, ou o obtido através da nota modelo.

Utilize o campo **"Confirmar Operação"** para determinar se a operação (nota, requisição etc) deverá ser confirmada no momento da geração. Essa marcação é predominante sobre qualquer outra configuração, inclusive a realizada nos Tipos de Operação.

A marcação **"Baixar reserva na nota de produção"** deve ser utilizada nas operações de pedidos que reservam estoque. Ao gerar operações de produção, o sistema irá baixar essas reservas, vinculando o item de Matéria-Prima à nota de produção com o item do pedido.

No campo **"Execução da Atividade"** você definirá quando a operação de estoque deverá ser executada, em relação ao Tipo de Execução da Atividade (Própria ou Terceiros). Pode-se definir dentre as seguintes opções:

- **Terceiros:** esta marcação representa que esta operação de estoque será executada se a atividade estiver sendo executada por terceiros.
- **Própria:** por esta definição, tem-se que esta operação de estoque será executada se a atividade estiver sendo executada internamente, ou seja, não terceirizada.
- **Todos:** através desta marcação, tem-se que esta operação de estoque será executada independente de a atividade ser terceirizada ou não.

#### Botão Operação Encadeada

Por Operação Encadeada entende-se que após finalizar uma produção, pode ser necessário executar a transferência dos produtos produzidos em uma OP para outro local/empresa, portanto esta operação consistirá na transferência destes.

Assim, por meio deste botão, você irá definir operações de estoque encadeadas após a nota de produção de produtos acabados. Sendo que, para que ele se encontre habilitado, são necessárias as seguintes configurações:

- O Campo Quando: desta aba, estiver com a opção Ao apontar PA selecionada.
- O campo Tipo dos Itens deverá estar selecionado com a opção Produto acabado apontado na atividade ou Subproduto da Atividade.
- Se o **"Tipo de Operação"** estiver vazio, ou a TOP do modelo igual a Produção.

Ao acioná-lo, você terá a exibição do seguinte pop-up:

![Imagem 8: Ao acioná-lo, você terá a exibição do seguinte pop-up:](https://ajuda.sankhya.com.br/hc/article_attachments/16646136281239)

O campo **"Tipo de Execução"** poderá ser **"Manual"** ou **"Automático"**.

Caso a opção Manual seja marcada, esta consistirá que a Operação Encadeada não será executada após a geração da Nota de Produção, caso a opção Automática for habilitada, a execução da Operação Encadeada ocorrerá logo após a geração da Nota.

Quando a opção Manual estiver selecionada, a marcação **"Obrigatória"** será habilitada para seleção.

Ao utilizar a opção Manual, o sistema irá habilitar o botão [+ Nova Movimentação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#bot%C3%A3onovamovimenta%C3%A7%C3%A3o) na aba **"Mov. Acessórias"** da atividade na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o) para que a movimentação seja realizada pelo usuário.

Caso a operação de estoque for Manual e Obrigatória e a operação de estoque encadeada não for realizada, ao finalizar a atividade o sistema apresentará o seguinte aviso:

**"Não é possível finalizar a atividade, pois existe operação encadeada pendente para a Ordem de Produção."**

Ao selecionar a marcação **"Confirmar Operação"**, a nota/pedido gerado será confirmado automaticamente a sua confirmação.

O campo **"Modelo de Nota"** será o modelo de nota que será utilizado para geração do cabeçalho da nota/pedido, sendo assim, a operação receberá Parceiro, Empresa, TOP, Centro de Resultado, Projeto e Natureza conforme o modelo selecionado.

Para esta operação, o **"Tipo de Operação"** deverá estar igual a **"Nota de venda"**, **"Pedido de venda"** ou **"Transferência"**.

No campo **"Parceiro"**, você deverá selecionar o parceiro.

Ao selecionar o Tipo de Operação como Nota de Venda, Pedido de Venda ou Transferência, o sistema habilitará dois campos, sendo eles:

A **"Empresa de Destino"** em que, deverá apresentar o tipo de movimento como T- Transferência.

E o campo **"Local de Destino"** terá de ser o tipo de movimento como T-Transferência. **Observação:** quando a combinação que gera a nota de produção for alterada, um pop-up de confirmação será exibido, pois a operação encadeada será removida.

Ao  configurar a Operação Encadeada como Nota de Transferência e o Tipo de Execução como Automática, a operação será executada após a geração da nota de produção automática. Caso definida como Manual, a Operação Encadeada não será executada após a geração da nota de produção.

**Nota:** ao gerar o apontamento e confirmá-lo, será gerado a nota de produção, e após esta, ocorrerá a operação encadeada com a quantidade conforme o apontamento.

Ao acionar a marcação **"Usar o Parceiro Terceiro da OP"**, o sistema utilizará o parceiro terceiro da Ordem de Produção/Operação no lugar do parceiro vinculado na operação. Esta marcação é indicada para o processo de produção Em Terceiros ([Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova)/Configuração da atividade, aba Geral).

#### Execução da Operação Encadeada

Na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025393153-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o), [aba Mov. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025393153-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abamov.acessrias), tem-se o botão ![CA02](https://ajuda.sankhya.com.br/hc/article_attachments/360060996794/ca02.png) que ao ser acionado exibe uma lista com as operações de estoque que poderão ser apresentadas de acordo com a engenharia do processo.

No Cabeçalho da Nota, tem-se o campo **"Empresa de Origem"**, que representa a empresa da nota de produção.

O campo **"Empresa de Destino"** receberá o valor da operação encadeada. Este campo será habilitado somente se a TOP for de Transferência.

Ao clicar no botão **"Próximo"**, o pop-up seguirá para a próxima página de configurações, em que tem-se os campos:

O **"saldo"** será o saldo do produto disponível para movimentação a partir da operação Encadeada. Sendo que, o valor deste campo é calculado como o total do produto em notas de produção subtraindo o valor movimentado por operação encadeada.

No campo **"Qtd. a Movimentar"** será informado a quantidade do produto que será movimentado na operação encadeada em questão. A quantidade a ser inserida neste campo não poderá ser superior ao Saldo, e não aceitará valores negativos.

O **"Local de Destino"** será o local de destino da Operação Encadeada. Este campo será habilitado para edição somente se a TOP for do tipo T-Transferência.

**Nota:** a finalização da atividade não será permitida caso a Operação Encadeada não for sido executada e estiver marcada como Obrigatória.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Apontamento

São configurados nesta aba os Apontamentos da atividade.

![Imagem 10: São configurados nesta aba os Apontamentos da atividade.](https://ajuda.sankhya.com.br/hc/article_attachments/16646162288663)

Por meio do campo **"Tipo de Apontamento"**, defina como serão realizados os apontamentos nas Operações de Produção. Pode-se escolher dentre duas opções:

- **Apontamento de PA / MP:** Esta opção, indica que o apontamento será com base nos Produtos Acabados e Matérias-Primas. Ele habilita os campos da seção **"Configuração Apontamento de PA / MP"**, logo abaixo. Além disso, na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025393153-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o) são apresentadas as abas **"Apontamentos" e "Produtos (PA)"**.
- **Conferência:** Por meio desta, o apontamento será feito com base na Conferência; serão habilitados os campos da seção **"Configuração da conferência"**, logo abaixo, além de na tela **"Produção > Rotinas > Operações de Produção"** ser apresentada a aba **"Conferência"**.

**Importante:** a definição realizada neste campo anula a outra, ou seja, na tela "Produção > Rotinas > Operações de Produção", serão apresentadas ou as abas **"Apontamentos"** e **"Produtos (PA)"**, ou a aba **"Conferência"**. Da mesma forma que, ou realiza-se as configurações do apontamento PA / MP ou as configurações da conferência, nas seções descritas abaixo.

Quando a marcação **"Exige apontamento de PA"** for realizada, determina a obrigatoriedade do apontamento de Produtos Acabados.

#### Configuração Apontamento de PA / MP

O campo **"Quantidade base para apontamento"** é destinado a determinar-se qual a quantidade a ser utilizada como base para os apontamentos de consumo. Essa quantidade será utilizada por exemplo, para multiplicar a quantidade de mistura da lista de Matérias-Primas, para se chegar a quantidade total das Matérias-Primas. Desta forma, teremos as seguintes opções de escolha:

- Qtd. Atual de PA no Repositório de Trabalho;
- Qtd. do Lote a Produzir;
- Qtd. Apontada de PA.

A marcação do campo **"Aponta matéria-prima"**, determina se a atividade permite apontamento do uso de matéria-prima. O fato de não ser permitido apontar matéria-prima em uma atividade, não implica em não poder solicitar-se as matérias-primas. Em atividades que consomem matéria-prima, mas não possuem apontamento, no caso de geração de nota de produção, o sistema deverá considerar a quantidade definida na formulação. Essa configuração não se aplica a materiais utilizados para ajuste (esse tipo de material sempre pode ser apontado). As opções disponíveis são:

- **Não aponta MP:** não será possível apontar matérias-primas nesta atividade. A aba de materiais não estará disponível no apontamento.
- **Aponta as MPs da atividade:** será possível apontar as matérias-primas consumidas na própria atividade. Conforme configuração, pode-se ou não adicionar outras matérias-primas.
- **Aponta as MPs da OP:** o usuário irá apontar todas as matérias-primas listadas em todas as atividades ditas do caminho padrão. O sistema irá iniciar o apontamento com todas as matérias-primas da Ordem de Produção, no entanto, conforme configuração, pode-se adicionar ou remover matérias-primas.

Ao efetuar a marcação do campo **"Aponta componente de manufatura"**, tem-se que a atividade permite apontamento de componentes de manufatura.

Quando a marcação **"Aponta subproduto"** for realizada, tem-se que a atividade permite apontamento de subprodutos. Pode-se escolher dentre as seguintes opções:

- **Não aponta Subproduto:** por meio desta, não será possível apontar Subprodutos nesta atividade. A aba de Subprodutos não estará disponível no apontamento.
- **Aponta os Subprodutos da atividade:** poderão ser apontados os subprodutos produzidos na própria atividade. Conforme configuração, pode-se ou não adicionar outros subprodutos.
- **Aponta os Subprodutos da OP:** por meio desta, você irá apontar todos os subprodutos listados em todas as atividades ditas do caminho padrão. O sistema irá iniciar o apontamento com todos os subprodutos da Ordem de Produção, no entanto conforme configuração, pode-se ou não adicionar ou remover subprodutos.

A marcação **"Apontar PA diferente em relação ao início do processo"**, determinará se a atividade permite que o operador realize apontamento de produtos acabados diferentes em relação ao início do processo. Desta forma, tem-se o exemplo:

A produção era para fabricar o Shampoo A 200 ml, porém devido a falta das embalagens de 250 ml, definiu-se por produzir o Shampoo 450 ml.

Ao acionar a marcação **"Proibir apontamento à maior"**, será definido que não é permitido apontar uma quantidade superior que o tamanho de lote da Ordem de Produção. Sendo que, essa funcionalidade não se aplica ao apontamento por conferência.

Em **"Aponta Recursos do Centro de Trabalho"**, será definido quentes da geração dos registros de apontamento dos Recursos dos Centros de Trabalho, é necessário identificar quais são os Centros de Trabalhos cujos recursos serão apontados, para isso, determina-se neste campo qual o tipo de apontamento de recursos a ser utilizado na atividade. Tem-se as seguintes opções:

- **Não aponta:** atividades com esta opção definida não suportam apontamento de Recurso;
- **Aponta os Recursos de CT da Atividade:** atividades com esta configuração apontam recursos apenas do Centro de Trabalho em uso pela mesma;
- **Aponta os Recursos de CT da OP:** atividades com esta opção definida apontam recursos de todos os Centros de Trabalhos utilizados por todas as atividades da Ordem.

Ao realizar a marcação do campo **"Permitir apontamento de 100% de perda"**, o sistema permitirá que você realize o apontamento de produções que por algum motivo tiveram uma perda de 100% da produção.

Sendo assim, depois de iniciar a atividade na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o) e iniciar o processo de apontamento na aba **"Apontamentos"**, insira no campo **"Qtd. Apontada"** o valor **"0"** e no campo **"Qtd. perda"** aponte o valor total do lote e confirme o apontamento.

Ao finalizar essa atividade, se não houver outras atividades abertas, nenhuma outra será criada e a Ordem de Produção também será finalizada. Caso existam atividades em aberto, somente a atividade atual será finalizada e nenhuma outra será criada. Neste caso, ao clicar no botão **"Finalizar"** e realizar o apontamento com perda total sem que outra atividade esteja aberta, a atividade é finalizada juntamente com a OP.

E caso tenha outra atividade aberta ao Finalizar a atual, teremos que ao realizar o apontamento com a perda total, a atividade será finalizada, mas a outra atividade aberta e a OP não serão encerradas. Por fim, se uma atividade não tiver mais saldo para transferir para uma próxima atividade a ser criada, a OP será concluída.

#### Configuração da conferência

Quando você realizar a marcação **"Contagem Cumulativa"**, a conferência será cumulativa, com isso, o campo **"Quantidade"** da aba **"Conferência"** (tela Produção > Rotinas > Operações de Produção) não será habilitado para digitação e cada inserção do produto será contada uma vez pelo sistema.

Determine por meio do campo **"Tipo de Conferência"**, qual será o tipo de conferência. Tem-se as seguintes opções:

- Exige Conferências Iguais;
- Exige Recontagem.

No campo **"Qtd. de conferências iguais"**, indique a quantidade de conferências similares. Será habilitado quando, o campo "Tipo de Conferência" estiver definido com a opção **"Exige Conferências Iguais"**.

Quando empregada a configuração de modo a **"exigir quantidade igual de conferências"**, significa que as últimas X conferências (onde X é o valor definido na configuração) devem possuir produtos e quantidades iguais (a configuração em execução no momento, é contada como sendo a última conferência). Caso isso ocorra, a conferência será finalizada e é inserido apontamento. Caso contrário, é apenas finalizada a conferência.

Informe no campo **"Qtd. de recontagens"**, a quantidade de recontagens que devem ser realizadas. Será habilitado quando, o campo **"Tipo de Conferência"** estiver definido com a opção **"Exige Recontagem"**.

Quando utilizada a configuração **"Exigir Recontagem"**, significa que tem-se a obrigatoriedade de realizar X recontagens, de forma a garantir a conferência (onde X é a quantidade de recontagens definidas na configuração). A configuração de recontagem, é adicional a configuração de "Conferências iguais". Caso o número de recontagens seja atingido, finaliza-se a conferência e é inserido um apontamento. Caso contrário, apenas finaliza-se a conferência.

**Importante:** para inserção de um apontamento (quantidade do PA), será sempre considerada a última conferência. Feita a inclusão deste apontamento, deve-se confirmá-lo, para que caso exista alguma operação de estoque definida para esse momento, a mesma seja executada.

A marcação **"Usar seq. lote no cód. barras"**, determina o uso da sequência de lote no código de barras. Ao ser assinalada, o campo **"Separador"** localizado logo à frente, é habilitado; neste, podem ser informados até **"5"** (cinco) letras e/ou números. A funcionalidade oriunda da marcação "Usar seq. lote no cód. barras", somente pode ser utilizada quando a conferência possuir **"Contagem Cumulativa"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Controle de Qualidade

Determine nesta aba, as configurações de uma atividade pertencente ao controle de qualidade.

![Imagem 11: Determine nesta aba, as configurações de uma atividade pertencente ao controle de qualidade.](https://ajuda.sankhya.com.br/hc/article_attachments/16646136295959)

Defina no campo **"Operação a ser realizada"**, qual operação de controle de qualidade essa atividade representa. Pode-se definir dentre as seguintes opções:

- **Nenhuma:** por esta opção, nenhuma operação de controle de qualidade será representada pela atividade.
- **Amostragem:** definindo-se esta opção, tem-se que a atividade realiza tarefas relacionadas a amostragem (coleta e aprovação/reprovação de amostras).
- **Laudo:** Essa atividade realiza tarefas relacionadas ao preenchimento de laudos.
- **Amostragem + Laudo:** através desta opção, a atividade realiza tarefas relacionadas a amostragem e preenchimento de laudos.

No campo **"Ciclo controle de qualidade"** deverá será utilizado, para determinar-se a qual ciclo de controle de qualidade a atividade está vinculada. O preenchimento desse campo é obrigatório caso a atividade realize alguma operação de qualidade.

Quando o campo "**Validar ciclo de controle de qualidade"** for marcado, esta atividade somente poderá seguir o processo caso o(s) Laudo(s) vinculado(s) ao ciclo de controle de qualidade estejam todos validados.

Por meio da marcação **"Conclui Ciclo de Controle de Qualidade"**, determine que a conclusão da atividade também conclui o ciclo de controle de qualidade ao qual está vinculada e correntemente pendente (o vínculo acontece na aba **"Controle de Qualidade"**).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Candidatos Executantes

O preenchimento desta aba está destinado a formulação da listagem de executantes ou grupos de executantes candidatos na execução da atividade.

![Imagem 12: O preenchimento desta aba está destinado a formulação da listagem de executantes ou grupos de executantes candidatos na…](https://ajuda.sankhya.com.br/hc/article_attachments/16646136300311)

Por meio do campo **"Tipo"** será determinado qual o tipo de usuário a ser vinculado. Assim, teremos as seguintes opções de escolha:

- Usuário;
- Fórmula;
- Grupo de Usuário.

Em **"Código"**, deverá ser utilizado para determinar-se qual o usuário ou grupo de usuários vinculado como candidato a executante.

Informe no campo **"Fórmula"**, a fórmula para definição do candidato que irá executar a atividade. Deverá ser utilizada uma fórmula no formato JavaScript, que retorne um número positivo para o usuário e um número negativo para grupo de usuário. Nesta fórmula, o retorno deve ser um número inteiro; além disso, teremos a possibilidade de se buscar a variável IDIATV. Vejamos os exemplos:

**var query = getQuery();**

**query.setParam("IDIATV", getParam("IDIATV"));**

**query.nativeSelect("SELECT CODEXEC FROM TPRIATV WHERE IDIATV = {IDIATV}");**

**if(query.next()){**

**return query.getInt("CODEXEC");**

}

ou

**return 1;** - representando um código de usuário

**return -2;** - representando um código de grupo de usuário

**Importante:** o usuário "dono" da atividade (seu candidato Executante), é aquele que realizou seu aceite ou a inicializou. Considerando um único usuário ou mesmo um grupo de usuários, uma atividade poderá ser visualizada apenas pelo usuário que fez sua aceitação ou inicialização. O usuário configurado como Gerente de Manufatura, poderá visualizar todas as atividades, tendo elas passado ou não pelo aceite ou inicialização. Além disso, a finalização das atividades poderá ser realizada apenas pelo usuário dono da atividade, ou ainda pelo seu Gerente de Manufatura.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Formulários

O objetivo dessa aba é a configuração de uma lista de formulários que serão disponibilizadas em cada atividade do processo. O mesmo formulário pode ser apresentado em diversas atividades, e os dados podem ser definidos por atividade ou de forma global no processo. Desta forma é possível acessar informações inseridas em atividades anteriores, criando assim um canal de comunicação entre as diversas atividades do processo.

![Imagem 13: O objetivo dessa aba é a configuração de uma lista de formulários que serão disponibilizadas em cada atividade do…](https://ajuda.sankhya.com.br/hc/article_attachments/16646136306071)

Selecione no campo **"Formulário"**, o formulário que deseja-se configurar para a atividade. Os formulários disponíveis devem estar vinculados anteriormente ao processo produtivo da atividade por meio da aba [Formulários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392213-Processo-Produtivo#abaformulrios).

No campo **"Ordem"** determine a ordem em que as operações serão executadas.

Por meio do campo **"Tipo de Acesso"**, é feita a determinação de qual o tipo de acesso aos dados ao formulário. Pode-se escolher dentre as seguintes opções:

- **Somente Leitura:** essa opção permite apenas a leitura do formulário. Esta marcação se justifica quando o escopo do formulário configurado é "Processo".
- **Leitura e Gravação:** essa opção permite que você executante da atividade realize leituras e gravações do formulário configurado.

A marcação **"Obrigatório"** desse campo definirá se o formulário deve ser informado obrigatoriamente nesta atividade, caso ainda não tenha sido preenchido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Inicialização de Repositório

O objetivo dessa aba é a manutenção dos registro dos detalhes da inicialização de um repositório de Produto Acabado, para os casos em que essa inicialização não seguir o padrão, que é iniciar juntamente aos Produtos Acabados a serem produzidos na Ordem de Produção.

O repositório pode ser iniciado com os Produtos Acabados ou com componentes de manufatura vinculados ao Produto Acabado produzível por esse processo.

![Imagem 14: O repositório pode ser iniciado com os Produtos Acabados ou com componentes de manufatura vinculados ao Produto Acabado…](https://ajuda.sankhya.com.br/hc/article_attachments/16646136311959)

No campo **"Produto (PA)"** selecione o produto acabado da inicialização. É um campo de preenchimento obrigatório.

**Nota:** para que seja possível realizar a vinculação de um produto inativo neste campo, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

O campo **"Controle"** será habilitado quando o produto selecionado possuir controle adicional por lista; nele selecione o controle do produto a ser inicializado no repositório.

Em **"Tipo do item inicializando"**, você poderá selecionar o tipo de item a ser inicializado no repositório. Pode-se definir dentre as seguintes opções:

- **Produto Acabado:** o repositório será inicializado com o produto acabado especificado no campo **"Produto (PA)"**.
- **Componente de Manufatura:** o repositório será inicializado com o componente de manufatura especificado no campo "Componente de manufatura", considerando a quantidade do lote de produção do Produto Acabado, multiplicando pela quantidade relativa do componente conforme o cadastro de componentes de manufatura.

Informe em **"Componente de Manufatura"**, o componente de manufatura que será enviado ao repositório.

**Importante:** esta funcionalidade ainda não foi implementada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)

## Aba Recursos de Centro de Trabalho

Esta aba tem a finalidade de permitir a determinação de uma lista de categorias de recursos Centro de Trabalho que são necessários para o processamento da atividade. Dessa forma, tem-se um resumo de recursos e suas respectivas quantidades necessárias para o processamento de todos os produtos do processo, tornando possível a visualização dessa informação em relatórios ou demonstrativos de formulação.

![Imagem 15: Esta aba tem a finalidade de permitir a determinação de uma lista de categorias de recursos Centro de Trabalho que são…](https://ajuda.sankhya.com.br/hc/article_attachments/16646136315415)

No campo **"Categoria de Recurso"** determine uma categoria de recurso. Pode ser informada qualquer categoria, independentemente desta ser analítica ou sintética. Em listagens onde o sistema apresenta formulação juntamente com outros insumos, você poderá agrupar essas categorias pelo tipo da categoria (máquina, mão de obra, equipamento).

Defina em **"Quantidade de Utilização"** aqui a quantidade (em minutos) da utilização deste recurso no processamento desta atividade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#top)
