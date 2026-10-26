---
id: "360050836154"
titulo: "Composição do Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-08-20T19:06:15Z"
rotulos: ["Configuração", "Fórmulas", "Estoque", "Produção", "br.com.sankhya.mgeprod.cad.composicao.produto", "Cadastro", "Configuração de composição de produtos", "Parâmetros e opções de controle", "Organização e detalhes específicos", "VISUTOTALQTDMP", "USATEMPOPROCESS", "PERMITEDITMP"]
---

# Composição do Produto

```
 Módulo: Produção > Cadastros         Versão disponível: a partir da 4.1
```

---

Esta tela permite que os usuários responsáveis pela engenharia dos produtos sejam capazes de cadastrar e manter as fórmulas de composições dos produtos fabricados no [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050884074).

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#filtros) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abageral) |
| --- | --- | --- |
| [Aba Matérias-Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abamat%C3%A9rias-primas) |  | [Aba Sub-Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abasub-produtos) |
| [Aba Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abatarifascip) |  | [Aba Terceiros (Parceiros)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abaterceiros(parceiros)) |
| [Aba Recursos do Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abarecursosdocentrodetrabalho) |  | [Aba Tempo de Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abatempodeprocessamento) |
| [Aba Formulários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abaformularios) |  | [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#bot%C3%B5esnotopodatela) |
| [Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#par%C3%A2metrosqueinfluenciamarotina) |  |  |

 ![Imagem 1: Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/article_attachments/1500000577702)

## Filtros

Na lateral esquerda da tela, além da alternativa de criar-se um filtro personalizado, pode-se através de alguns campos, configurar filtros a fim de se selecionar mais facilmente a Composição do Produto desejada. São eles:

**Produto:** através deste campo, pode-se filtrar a composição com base no produto utilizado.

**Processo Produtivo:** tem-se aqui a possibilidade de busca, por meio do código que identifica o processo produtivo cadastrado.

**Última versão:** ao acionar esta opção, serão carregados na tela os últimos versionamentos dos Processos Produtivos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Geral

Através desta aba realiza-se as configurações de detalhes relacionadas ao vínculo entre o processo produtivo e o produto.

![Imagem 2: Através desta aba realiza-se as configurações de detalhes relacionadas ao vínculo entre o processo produtivo e o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000575782)

**Seção Lote**

**Tamanho de Lote Padrão:** Nesse campo especifica-se o tamanho do lote padrão do produto em questão para o processo produtivo. Esse valor é um tamanho de lote que quase sempre é utilizado; esse valor é sugerido de forma automática no lançamento de OP.

**Observação:** caso o campo Tamanho de Lote Padrão não esteja preenchido, ou esteja com o valor 0 (zero), quando você tentar salvar/editar a Composição do Produto, será exibida a mensagem de alerta abaixo:

**"Tamanho de Lote Padrão deve ser maior que zero para o PRODUTO X."**

Na publicação do Processo Produtivo, nosso sistema validará, primeiramente, se existe Produto (PA) vinculado ao processo que foi criado e depois validará o campo Tamanho de Lote Padrão, observando se ele não está preenchido ou está com o valor 0, conforme mencionamos acima.

**Múltiplo Ideal:** Esse campo deve ser utilizado para especificar o múltiplo ideal para a quantidade a se produzir por ordem. Por exemplo: Se o valor neste campo for 250, será possível produzir 250, 500, 750, 1000, e não será possível produzir 1200, ou seja, pode-se produzir múltiplos do valor informado.

**Qtd. Mínima:** Informa-se neste campo a quantidade mínima a ser produzida em uma Ordem de Produção.

**Nota:** os campos descritos acima, respeitam a configuração de **"Decimais para quantidade''** do produto ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abamedidas)).

**Seção Tempo**

**Tipo de Tempo:** Através deste campo, pode-se especificar qual será o tipo do tempo de atravessamento do produto caso o tamanho de lote da OP seja diferente do tamanho de lote padrão. Tem-se duas opções:

- **Por Quantidade:** Para se chegar ao tempo de produção de uma determina quantidade, utiliza-se o Tempo de atravessamento dividido pelo Tamanho de lote Padrão multiplicado pela quantidade em questão;
- **Por Lote:** O tempo da atravessamento é um número múltiplo baseado no tamanho de lote padrão, ou seja, para se produzir até o tamanho de lote será gasto uma vez o tempo de atravessamento, a partir dessa quantidade será gasto duas vezes o tempo de atravessamento até o tamanho de duas vezes o lote padrão, e assim sucessivamente.

**Tempo de Atravessamento:** Esse campo deve ser utilizado para determinar qual o tempo de atravessamento padrão do processo produtivo. Esse tempo pode variar conforme a capacidade e os recursos dos Centros de Trabalho. Em casos onde a gestão de capacidades não é realizada, a única restrição será o tempo de atravessamento do processo.

**Importante:** quando o parâmetro **"Calcular tempo de atravessamento ao publicar processo? - CALCTEMPOATRAV"** estiver habilitado, ao publicar o processo (botão **"Publicar"**) tem-se a somatória do tempo de atravessamento de todas as atividades do processo e atualização dos campos Tipo de Tempo, Tempo de Atravessamento e Un. Tempo do Produto Acabado.

**Tempo de Atravessamento (parte fixa):** Corresponde a uma parcela fixa do tempo necessário para se fabricar o produto, de modo que uma mudança no tamanho de lote da OP não irá influenciar em mudanças neste valor.

**Un. Tempo:** Especifica-se neste campo a unidade de tempo utilizada para o Tempo de Atravessamento (Tempo de Atravessamento se refere ao tempo decorrido a partir do momento em que uma matéria-prima chega na empresa e o momento em que esta matéria-prima chega no armazém incorporada em um produto acabado). Pode-se definir dentre três unidades:

- Horas;
- Dias;
- Minutos.

**Seção Outros**

**Tipo de geração do Nro. de Série:** determina-se neste campo como será a geração dos números de série do produto quando este é controlado por série e é vinculado à lista de Produtos Acabados de um Processo Produtivo. Tem-se as seguintes opções:

- **Manual (Apontamento):** as séries dos produtos deverão ser informadas manualmente na realização do apontamento de Produtos Acabados;
- **Manual (Lançamento):** por esta opção, as séries deverão ser informadas manualmente ao efetuar-se o lançamento da OP considerando o tamanho de lote da mesma;
- **Automática:** através desta opção, as séries serão geradas no lançamento da Ordem de Produção com base no último valor sequencial gerado para o produto e no tamanho de lote da OP. De modo que, será permitido ter números de séries repetidos para produtos diferentes. Definindo-se por esta opção, deve-se determinar a Máscara do Número de Série.
- **Automático (Série Global):** com essa opção selecionada, no lançamento da OP serão criados, automaticamente, números de séries únicos de modo aleatório com o formato **"AAA#A##MMYY"**, sendo que: **"A"** é letra, **"#"** é número, **"MM"** é o mês atual e **"YY"** é o ano atual com dois dígitos. Lembre-se que nesta opção não se tem, em hipótese alguma, números de séries repetidos.

**Máscara do Nro. Série:** esta informação deve ser inserida se o Tipo de geração do Número de Série for definido como Automática. A máscara padrão do número de série é **"LLLLLLLLLLLLL#####"**, onde:

**L** = Número Lote da OP
**#** = Sequencial

**Importante:** ao optar pelo controle por série, não há necessidade de utilizar o controle por lote no mesmo produto. Pois, a tratativa do número de série permite rastrear o produto individualmente, tornando-se dispensável a rastreabilidade também por número de lote. 

**Base para cálculo da Dt.Validade:** Aqui define-se como o sistema proceder para realização do cálculo da data de validade do produto acabado a ser produzido. Pode-se escolher dentre as seguintes opções:

- **Não calcula:** Não será calculada a data de validade do PA.
- **Data da primeira nota de produção do lote:** Será considerada a data da primeira nota de produção do lote para se calcular a data de validade do produto. O cálculo sempre considera a quantidade de dias definidos no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque), campo **"Prazo validade/tolerância"**.
- **Menor Dt.Validade das MPs:** A data de validade do produto PA será a menor data de validade entre as Matérias-Primas que compuseram o produto PA.
- **Data de Inicialização da OP:** A data de validade do PA será calculada com base na data de inicialização da OP. O cálculo sempre considera a quantidade de dias definidos no Cadastro do Produto, aba Medidas e Estoque, sub-aba Estoque, campo Prazo validade/tolerância).

**Seção Estoque**

Através do campo **"Local de Destino"** você poderá definir um local específico para o destino do PA na geração da nota de produção, sendo que o sistema irá priorizar essa configuração em vez do Local de destino do PA informado na Operação de Estoque que gera a nota de produção. Porém, caso não haja um Local de Destino aqui na Composição do Produto, o sistema dará a entrada do PA no local configurado na Operação de Estoque.

**Seção Segurança {disponível na versão ≥ 4.17}**

Para gerenciar as alterações realizadas no registro, você pode conferir nessa seção o usuário responsável pelo cadastro e a data e hora da inclusão do registro. Pode-se verificar também o usuário da última alteração, bem como a data e hora da última alteração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Matérias-Primas

Esta aba está destinada a construção da lista de materiais necessários para o processamento da atividade. Estes materiais, em geral são matérias-primas e insumos que depois de utilizados, agregam valor ao produto acabado.

![Imagem 3: Esta aba está destinada a construção da lista de materiais necessários para o processamento da atividade. Estes…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000587681)

**Matéria-prima:** este campo deve ser utilizado para determinar-se o material que deseja-se adicionar à lista de materiais do produto acabado selecionado.

**Importante:** o parâmetro **"Permitir definir produto como MP de si próprio. - PRODMPPROP"** quando habilitado, permitirá que o produto seja cadastrado como Matéria-prima de si mesmo.

**Observação:** tratando-se de um processo de reprocessamento/reparo, é possível que um produto seja utilizado como matéria-prima de si mesmo.

**Nota:** para que seja possível realizar a vinculação de um produto inativo como matéria-prima, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

**Tipo Controle (MP):** Este campo deve ser utilizado para determinar se qual o tipo do controle do produto. Pode-se definir dentre as seguintes opções:

- **Automático:** O módulo de produção irá utilizar as regras do ERP para determinar o controle deste material. Esta marcação é útil principalmente em casos de Matérias-Primas controladas por lote; desta forma o sistema pode executar o FEFO (First-Expire, First- Out), dependendo da configuração do material.

![Imagem 4: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16645227887767)**Informações adicionais:**

1. Caso exista alguma movimentação de estoque configurada para **"Validar estoque p/ Reserva"**, será necessário que o usuário aponte o lote que está de fato sendo consumido, pois a reserva em questão irá acontecer para um lote específico da matéria-prima.
2. Sugestão de lote no apontamento: Quando a Ordem possui movimentações acessórias (nota de transferência, requisição que reserva estoque, etc) para MPs controladas por lote, as rotinas de apontamento (Operações de Produção e Apontamento de Produção) sugerem os lotes movimentados no momento do apontamento, evitando assim divergência entre a movimentação de estoque da Ordem e os Apontamentos.
3. Explosão de lote automática**:** Quando a Ordem não possui nenhuma movimentação acessória para MPs controladas por lote, ao fazer apontamento não especificando um lote o sistema realizada a explosão de lote automática, ou seja, a nota de produção gerada recebe lote das MPs automaticamente conforme FEFO. Sendo que neste cenário as rotinas de Apontamento não sugerem lote.

- **Literal:** caso a Matéria-Prima possua controle adicional de estoque, o valor deve ser definido literalmente.
- **Herdar do PA:** através desta opção, o controle da Matéria-Prima será o mesmo do Produto Acabado que está sendo processado. Este campo só pode ser configurando quando o Produto e o Subproduto (Ou MPs) estão configurados com controle adicional de estoque do tipo Lista.

**Referência do Produto:** tem-se neste campo o conteúdo do campo **"Referência"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) do [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos).

**Seção Quantidade**

**Tipo de Quantidade:** determina-se neste campo, como o sistema deve calcular a quantidade desse material para a produção do produto acabado. O valor calculado será inicializado no formulário de apontamento de Matérias-Primas, e depois tem-se a liberdade de modificá-lo conforme desejado. As opções disponíveis são:

- **Fixa:** será utilizada sempre a quantidade determinada no campo "Quantidade".
- **Variável:** a quantidade será variável em função da quantidade produzida.

Através da marcação **"Proporcionalizar matéria-prima do tipo Fixa"**, você define se a matéria-prima do tipo fixa será proporcionalizada de acordo com o apontamento realizado.

**Observação:** a marcação acima funciona para todas as rotinas de apontamento de produção que existem no Sankhya Om, sendo elas: [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o), [Apontamento de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o), [Pesagem de Produção (OP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594914-Pesagem-de-Produ%C3%A7%C3%A3o-OP-) e [Pesagem de Produção ID Volume](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594774-Pesagem-de-Produ%C3%A7%C3%A3o-ID-Volume-).

**Quantidade:** determina-se neste campo a quantidade da matéria-prima para a produção do Produto Acabado.

**Observação:** quando o produto acabado da composição faz parte de um grupo de co-produtos, ou seja, é um produto resultante de uma produção conjunta, o campo Quantidade não representará a quantidade consumida por uma unidade do produto acabado fabricado, pois, na rotina de Produção Conjunta, essa Quantidade é usada para compor um índice de consumo da matéria-prima compartilhada.

**Unidade:** este campo é destinado a definir-se a unidade de medida a ser utilizada pelo material.

**Gera Requisição:** marcando-se este campo, determina-se que o sistema irá incluir esse material nas operações de estoque comandadas para os materiais dessa atividade.

**Vínculo direto com série do PA:** esta opção quando assinalada, tem-se a obrigatoriedade de vincular as séries da matéria-prima apontada com uma série já apontada do Produto Acabado, isto se o PA também for controlado por número de série. Esta opção deve ser utilizada se o PA ao qual a Matéria-Prima está vinculada, também for controlado por número de série.

**Seção Estoque**

**Local de Origem:** nesse campo seleciona-se o local de origem utilizado para a requisição da matéria-prima.

**Local de Baixa:** este campo é empregado na seleção do local para baixa desse material em notas de produção.

**Verifica Estoque:** esta marcação deve ser acionada quando houver configuração de filtro de transição no processo produtivo e o campo **"Tipo"** da aba [Filtro de Transição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abafiltrosdetransies) estiver definido como **"Estoque Disponível de MP"**.

**Gera Requisição:** marcando-se este campo, determina-se que o sistema irá incluir esse material nas operações de estoque comandadas para os materiais dessa atividade.

**Vínculo direto com série do PA:** esta opção quando assinalada, tem-se a obrigatoriedade de vincular as séries da matéria-prima apontada com uma série já apontada do Produto Acabado, isto se o PA também for controlado por número de série. Esta opção deve ser utilizada se o PA ao qual a Matéria-Prima está vinculada, também for controlado por número de série.

**Material consumido por refugo:** esta marcação determina se o material da Lista de MP's em questão foi consumido por refugo. Lembrando que refugo é um Produto Acabado ou um Produto em Processamento que está fora das especificações técnicas aceitáveis pela fábrica. Um refugo pode ser gerado por qualquer atividade do processo produtivo de um Produto Acabado.

**Observação:** os materiais indicados como consumidos por refugo também serão incluídos na nota de produção do Produto Acabado; o consumo desses materiais será proporcional à quantidade de Produtos Acabados apontados (bons e refugo). Por exemplo:

Ao fabricar um Produto Acabado (PA), se 8 unidades do PA forem apontadas como boas e 2 unidades como refugo, consumindo 10 unidades da matéria-prima (MP), a nota de produção do PA irá consumir 8 MP's e a nota de refugo irá consumir 2 MP's.

Ou seja, quando existe uma MP consumida por perda ou refugo, deve ser configurada uma nota de refugo para que a MP seja consumida pelo mesmo. Caso a MP não seja uma MP consumida por refugo, a mesma não deve ter essa marcação. Se não existe nota de produção para o refugo, nenhuma das MP's deve ter essa configuração, pois todas as MP's apontadas devem ser consumidas na geração da nota de produção para evitar inconsistências no processo.

**Nota:** no processo produtivo ao se inserir a mesma matéria-prima para o mesmo Produto (PA) em duas atividades diferentes, as configurações abaixo deverão estar preenchidas da mesma forma:

- Unidade;
- Local de Origem;
- Local de Baixa;
- Tipo de Uso do Material;
- Fixar qtd. apontada para uma mesma MP ao editar qtd. apontada do PA.

Caso seja apresentada alguma diferença nas referidas configurações, não será concluído o processo de inclusão sendo exibida a seguinte mensagem:

**"'Unidade', 'Local de Origem', 'Local de Baixa', 'Tipo de Uso do Material, 'Fixar qtd. apontada para uma mesma MP ao editar qtd. apontada do PA' devem ser iguais para uma mesma MP dentro do processo para um mesmo PA."**

Ao efetuar a marcação **"Estoque de Terceiro"**, o saldo de estoque pertinente ao parceiro terceiro será apresentado na Ordem de Produção.

**Seção Desvios**

**% Desvio Superior:** De forma contrária ao campo anterior, especificar-se aqui o % de limite superior de consumo desta Matéria-Prima em relação à quantidade padrão (definida anteriormente no campo **"Quantidade"**). O sistema não permitirá apontamentos que ultrapassarem este limite.

**% Desvio Inferior:** Este espaço é destinado a especificar-se o % de limite inferior de consumo desta Matéria-Prima em relação à quantidade padrão (definida anteriormente no campo **"Quantidade"**). O sistema não permitirá apontamentos que ultrapassarem este limite.

**Nota:** no cálculo do % desvio de consumo de MPs, as MPs alternativas serão consideradas proporcionalmente. Deste modo, a quantidade consumida da MP será:

"O consumo da MP + o consumo da MP alternativa (convertida na MP principal)".

**Solicitar liberação ao exceder desvio:** quando esta marcação estiver acionada, ao ultrapassar o percentual de desvio permitido para o apontamento da matéria-prima, o evento 80 - Desvio no consumo de material será lançado. Sendo este liberado, será possível confirmar o apontamento mesmo existindo desvio no apontamento do material.

**Seção Segurança {disponível na versão ≥ 4.17}**

Para gerenciar as alterações realizadas no registro, você pode conferir nessa seção o usuário responsável pelo cadastro e a data e hora da inclusão do registro. Pode-se verificar também o usuário da última alteração, bem como a data e hora da última alteração.

No botão ![Imagem 5: No botão "Outras Opções..." desta aba, temos a opção "Configurações do PI" que, quando acionada, abrirá o seguinte…](https://ajuda.sankhya.com.br/hc/article_attachments/16645239864471) **"Outras Opções..."** desta aba, temos a opção **"Configurações do PI"** que, quando acionada, abrirá o seguinte pop-up:

![Imagem 6: No botão "Outras Opções..." desta aba, temos a opção "Configurações do PI" que, quando acionada, abrirá o seguinte…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001132761)

**Importante:** os produtos fabricados em Processos Produtivos configurados como **"Produção para Terceiro"** (configuração realizada na [Seções do Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova#se%C3%A7%C3%B5esdoprocessoprodutivo) da tela [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova#top)), não poderão ser utilizados como produtos intermediários, pois a produção para terceiros não foi desenvolvida para esse tipo de produção.

O pop-up Configurações do PI permite a configuração do vínculo do PI com o PA; esta associação é feita através dos seguintes campos:

**Tipo do PI:** nesse campo defina qual a relação entre o produto PI e o produto PA, ou seja, para fabricar o Produto Acabado, deve-se utilizar o PI buscando do **"Estoque"**, ou lançando **"Sub-ordem"** de produção para ele; sendo estas opções em destaque, as opções de escolha para este campo.

**Importante:** na utilização da opção **"Estoque"** em nenhuma circunstância será lançada uma sub-ordem para o PI, mesmo que seja no lançamento de OP manual ou no cálculo de demanda indireta do Planejamento de Produção /MRP I para um PI. Fato este, por entender que o mesmo deve ser tratado como as demais MPs, ou seja, sempre existirá estoque do produto disponível para a produção.

**Tipo de sub-ordem:** este campo definirá o comportamento do sistema na geração/utilização de Ordens de Produção do PI. O uso deste campo é relevante quando o campo **"Tipo do PI"** estiver configurado com a opção **"Sub-ordem"**. Desta forma, você pode selecionar as seguintes opções:

- **Sempre iniciar uma nova:** sempre que o sistema iniciar uma ordem principal, será feito um lançamento de uma sub-ordem para os PI's.

#### Iniciar quando não existir em aberto:

- **No rascunho do lançamento da OP:** será verificado pelo sistema se existem sub-ordens para o PI no rascunho. Caso exista, será aproveitado a sub-ordem do PI exibido de modo que a demanda dos PA's que utilizam este PI sejam atendidas.
- **Ao lançar a OP:** antes de criar a sub-ordem para o PI, será verificado se existe uma ordem principal em aberto para aquele PI. Caso não exista, será lançada uma nova.

#### Sempre usar uma em aberto:

- **No rascunho do lançamento da OP:** o sistema verificará se já existem sub-ordens para o PI neste rascunho. Caso haja, a sub-ordem do PI existente será aproveitada de modo que atenda a demanda dos PA's que utilizam este PI.
- **Ao lançar a OP:** ao efetuar o lançamento de uma ordem principal, será gerada uma dependência entre esta e uma ordem anteriormente aberta do PI, desde que a OP do PI possua quantidade suficiente para que seja atendida a demanda dos PA's a serem produzidos na ordem principal. De forma contrária, não poderão ser feitos lançamentos das OP's.

**Aguardar a sub-ordem:** quando se realiza a produção de um produto intermediário, e este servirá de "ponto de partida" para a produção de um PA, a marcação deste campo, fará com que a produção do PA, só tenha início após a finalização da produção deste PI.

**Observação:** caso esta marcação esteja selecionada e o PI esteja inserido no evento **"Aguardar PI"**, o PA e PI serão iniciados ao mesmo tempo e ao movimentar as atividades na tela Programação de **"Plano Mestre de Produção"**, ocorrerá conflito entre elas.

Se estiver selecionada, e nenhum PI se encontrar configurado em **"Configuração de evento"**, a programação do PA será executada após o término do PI.

Quando a marcação Aguardar a sub-ordem estiver acionada e um PI configurado na Configuração de Evento, o sistema exibirá uma mensagem de erro ao carregar a programação informando que existe conflito de configuração e que esta configuração do PI em relação ao PA é inválida.

Se a marcação **"Bloquear Inicialização do (PA) manual"** estiver selecionada, você não conseguirá inicializar a ordem do produto (PA) em paralelo com a produção do PI, ou seja, a inicialização do PA deverá aguardar a subordem do PI ser totalmente finalizada, para ter seu início.

**Observação:** caso a marcação acima esteja realizada, você não conseguirá iniciar uma OP de produto (PA) na tela de [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) e a seguinte mensagem será exibida:

**"Não é possível iniciar um OP com status criado com a opção "Bloquear Inicialização do (PA) manual" marcada no processo produtivo, verificar configurações antes de inicializar a ordem de produção."**

**Tipo de numeração de lote:** Neste campo defina qual será o critério de numeração dos lotes dos PI's e PA's. São disponíveis três opções de escolha:

- **PA usa o mesmo lote do PI:** no lançamento de um PI, a numeração do lote do PA que virá em seguida, seguirá a numeração do PI.
- **PI usa o mesmo lote do PA:** seguindo o mesmo critério da opção anterior, esta marcação irá realizar o processo inverso, ou seja, o PI lançado irá receber a mesma numeração de lote do PA.
- **Nro. de lote independente:** através desta marcação, temos a possibilidade de informar as numerações de PIs e PAs de forma independente.

Quando a marcação **"Considerar o lote da sub-ordem nas mov.acessórias"** estiver desabilitada, na explosão de lote da movimentação acessória de PI, não será considerado o lote da sub-ordem; por padrão, esta marcação já vem habilitada, ou seja, será considerado o o lote da sub-ordem nas movimentações acessórias de PI.

**Importante:** esta funcionalidade se aplica apenas à sugestão de lote para PIs que possuam controle adicional do tipo **"Nro de lote"**, cuja fabricação se dá por meio de uma sub-ordem vinculada à OP.

**Nota:** com a marcação Considerar o lote da sub-ordem nas mov. acessórias habilitada, o lote da sub-ordem também será sugerido nas operações de estoque manuais.

**Observação:** ao criar um apontamento, quando existir movimentação acessória, será considerado o lote desta movimentação, mesmo com a marcação Considerar o lote da sub-ordem nas mov. acessórias habilitada; se não existir uma movimentação acessória, o lote da sub-ordem será sugerido.

**Considerar quantidade em estoque:** dentre as definições realizadas nesta sub-aba para o Produto Intermediário (PI), esta marcação ao ser realizada, determina que o sistema irá considerar o estoque do produto antes do lançamento da sub-ordem, ou seja, o tamanho do lote da Ordem do Produto Intermediário será a quantidade necessária do PI subtraída da quantidade em estoque arredondando-a à configuração do lote (lote mínimo e múltiplo ideal).

**Nota:** a marcação Considerar quantidade em estoque será habilitada para utilização, apenas se o campo Tipo do PI for definido com a opção Sub-ordem.

**Redimensionar PA:** determine neste campo como irá ocorrer o redimensionamento do Produto Acabado; sendo a ordem do PI redimensionada, será feita a tentativa de redimensionamento proporcional à ordem do PA dependente. Temos as seguintes opções:

- Nunca;
- Sempre;
- Opcional.

**Redimensionar PA na Perda:** de acordo com este campo, na finalização de uma ordem do PI com apontamento de perda, o sistema tentará redimensionar a ordem do PA dependente, subtraindo a quantidade proporcional à perda. O campo é composto das seguintes opções:

- Nunca;
- Sempre;
- Opcional.

**Observação:** é relevante mencionar que nos casos em que uma MP é configurada para um PA no Processo Produtivo do mesmo, e posteriormente, criado um processo produtivo para a MP de forma que a mesma se torne um PI, essa MP não será apresentada na aba Produtos (PI) do cadastro do PA no Processo Produtivo.

Ainda no botão ![Imagem 7: Ainda no botão "Outras Opções..." desta aba, existe a opção "Materiais Alternativos" que, quando acionada, abrirá o…](https://ajuda.sankhya.com.br/hc/article_attachments/16645239864471) **"Outras Opções..."** desta aba, existe a opção **"Materiais Alternativos"** que, quando acionada, abrirá o seguinte pop-up:

![Imagem 8: Ainda no botão "Outras Opções..." desta aba, existe a opção "Materiais Alternativos" que, quando acionada, abrirá o…](https://ajuda.sankhya.com.br/hc/article_attachments/360102179753)

**Material Alternativo:** define-se aqui, o material que será adicionado na lista de materiais alternativos da matéria-prima.

**Referência do Produto (Alternativo):** tem-se neste campo o conteúdo do campo **"Referência"** presente na aba Geral do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral); neste caso, referente ao produto alternativo.

**Quantidade:** neste campo será indicada a quantidade do material alternativo relativa a uma unidade do material principal a qual ele está ligado.

**Unidade:** indica-se aqui a unidade de medida a ser utilizada quando for considerado o material alternativo.

**Conjunto:** um conjunto deve ser utilizado nos casos em que a matéria-prima é substituída por vários materiais alternativos ao mesmo tempo. Com isso, esses materiais alternativos devem fazer parte do mesmo conjunto. Informa-se aqui apenas números.

**Observações:** 

• Você poderá cadastrar uma mesma matéria-prima alternativa em dois ou mais conjuntos.

• O sistema não permite que uma mesma matéria-prima alternativa seja configurada como matéria-prima principal quando utilizada em mais de uma atividade.

• O sistema identifica um item como Produto Intermediário (PI) quando ele está cadastrado como matéria-prima de um produto acabado e existe um processo produtivo associado para sua fabricação.

• Quando o usuário cadastra uma matéria-prima principal que não é um PI, não é possível configurar esse item como Produto Intermediário. Nesse caso, o material é consumido diretamente do estoque.

As matérias-primas alternativas herdam as configurações da matéria-prima principal. Portanto, se não existe subordem de produção para a matéria-prima principal, também não haverá subordem para a matéria-prima alternativa. Nesse caso, o material alternativo será consumido diretamente do estoque, da mesma forma que uma matéria-prima comum.

Assim, o PI deverá ser produzido por meio de uma ordem de produção independente, sendo tratado como produto acabado, e não como produto intermediário dentro da estrutura do produto principal.

Para esse cenário, a operação de estoque da atividade pode ser gerada inicialmente como não confirmada. Dessa forma, o sistema somente atualizará o estoque após a confirmação da operação. Antes da confirmação da nota, o usuário também poderá excluir o item que não deve ser movimentado, evitando movimentações indevidas no estoque.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Sub-Produtos

Configura-se nesta aba a lista de subprodutos (ou scrap's) criados com o processamento das matérias primas na atividade. Uma operação pode gerar diversos subprodutos, cuja quantidade é geralmente uma função da quantidade de Produto Acabado processado.

![Imagem 9: Configura-se nesta aba a lista de subprodutos (ou scrap's) criados com o processamento das matérias primas na…](https://ajuda.sankhya.com.br/hc/article_attachments/360101673313)

**Subproduto:** esse campo deve ser utilizado para determinar-se o material que deseja-se adicionar a lista de materiais do produto acabado selecionado.

**Nota:** para que seja possível realizar a vinculação de um produto inativo como subproduto, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

**Tipo de Controle:** determina-se aqui, qual o tipo do controle do produto. Tem-se as seguintes opções para escolha:

- **Literal:** caso o subproduto possua controle adicional de estoque, o valor deve ser definido literalmente.
- **Herdar do PA:** definindo-se por esta opção, o controle do subproduto será o mesmo do Produto Acabado que está sendo processado.

Este campo só pode ser configurando quando o Produto e o Subproduto (Ou MPs) estão configurados com Controle Adicional de estoque do tipo Lista.

**Base para cálculo da Dt. Validade:**você poderá utilizar este campo para o preenchimento da data de validade e data de fabricação dos subprodutos gerados na OP, sendo que, contém as seguintes opções para seleção:

- Data da primeira nota de produção do lote;
- Data de inicialização da OP;
- Menor Dt.Validade das MPs;
- Não calcula.

**Observação:** ao selecionar a opção **"Data Inicialização da OP"** do subproduto, após o lançamento da OP verifique que as colunas de **"Dt. de Validade"** e **"Dt. de Fabricação"** foram automaticamente atualizadas.

**Nota:** se a opção Data da Primeira nota de produção do lote for selecionada, após a realização do apontamento de produção na tela **"Operações de Produção - Nova"**, é possível verificar no botão Visualizar subprodutos (tela **"Operações de Produção"**, botão **"Outras Opções"**, opção **"Resumo PA/ MP / MP Alternativa"**), que a Data de Validade e Data de Fabricação foram atualizadas e foram geradas notas de movimentações acessórias dos subprodutos apontados que poderão ser visualizados na tela **"Ordens de Produção - Nova"**.

**Referência do Produto:** neste campo será apresentada a referência informada no [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), campo **"Referência"**.

**Seção Quantidade**

**Quantidade:** campo que deve ser utilizado para determinar-se a quantidade da matéria-prima pra a produção do Produto Acabado.

**Unidade:** este espaço é destinado ao preenchimento da unidade de medida a ser utilizada pelo material.

**Tipo de Quantidade:** através deste campo determina-se como o sistema deve calcular a quantidade desse produto para a produção do produto acabado. O valor calculado será inicializado no formulário de apontamento de Subproduto e em seguida, tem-se a liberdade de modificá-lo como desejado. Pode-se definir dentre as seguintes opções:

- **Fixa:** o sistema utiliza sempre a quantidade determinada no campo "Quantidade";
- **Variável:** a quantidade será variável, ou seja, em função da quantidade produzida.

**Seção Apontamento**

**Exige Apontamento:** a marcação desse campo determina a obrigatoriedade do apontamento para essa matéria-prima.

**Subproduto por Perda/Refugo:** esta marcação define se o subproduto em questão se trata ou não de perda/refugo. Por padrão, esta marcação é apresentada desligada e é conflitante com a marcação Exige Apontamento, ou seja, elas não poderão ser realizadas simultaneamente.

**Seção Estoque**

**Local de Destino:** define-se neste campo, o local de estoque do subproduto. Quando informado, este local será utilizado em notas de subprodutos. Se não informado, o sistema usa o local informado na própria operação de estoque (local de origem).

**Seção Segurança**

Para gerenciar as alterações realizadas no registro, você pode conferir nessa seção o usuário responsável pelo cadastro e a data e hora da inclusão do registro. Pode-se verificar também o usuário da última alteração, bem como a data e hora da última alteração.

**Observação:** O sistema não está preparado para a configuração do mesmo código de produto como **matéria-prima e subproduto na mesma operação de produção**. Essa configuração pode gerar erros em processos que não foram previstos. Por exemplo, se uma matéria-prima **MP001** é consumida no processo e, ao mesmo tempo, o próprio **MP001** é gerado como subproduto, o sistema pode não identificar corretamente a origem do lote/controle, ocasionando inconsistências no apontamento. Dessa forma, mesmo que o subproduto gerado seja fisicamente igual à matéria-prima consumida, recomenda-se que seja cadastrado com **um código diferente**. O mesmo código deve ser utilizado em ambos os papéis apenas em cenários específicos, como reprocessos. Caso essa configuração já esteja realizada, o lote/controle poderá ser ajustado manualmente antes da confirmação do apontamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Tarifas CIP

Nesta aba são inseridas as Tarifas CIP (Custo Indireto de Produção), que para serem aqui apresentadas, devem ter sido previamente incluídas no [Cadastro de Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074-Tarifas-CIP).

Nas telas [Filtro para cálculo CIP (Financeiros)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118873) ou [Filtro para cálculo CIP (Requisições)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119153), determina-se a regra a qual aquela tarifa sofrerá alteração em seu custo. Por exemplo: Financeiros gerados para a "Empresa 1", cuja natureza seja "Energia Elétrica" geram alterações no custo da Tarifa 1.

Em um dado momento o custo real da tarifa pode ser calculado e atualizado considerando-se **"os filtros p/ cálculo de custo"** (Cálculo de custo baseado no Financeiro/Requisição).

Através desta aba, realiza-se o vínculo de uma tarifa ao produto acabado produzido pelo processo produtivo.

![Imagem 10: Através desta aba, realiza-se o vínculo de uma tarifa ao produto acabado produzido pelo processo produtivo.](https://ajuda.sankhya.com.br/hc/article_attachments/360099460114)

**Tarifa:** neste campo informa-se a tarifa que será configurada para o Processo Produtivo.

**Tipo de Índice:** através deste campo, pode-se determinar o tipo de índice da tarifa vinculada com o Produto Acabado/Processo Produtivo. Tem-se as seguintes opções:

- **Fixo:** o índice da tarifa será fixo. Para cada unidade do produto acabado sempre será consumida a mesma quantidade de tarifa CIP. Com isso, considere o exemplo:

Se o Tipo de Índice for Fixo e o **"Índice"** for 3, para cada unidade produzida do Produto Acabado serão consumidas 3 tarifas.

- **Variável (Execução de atividades):** o índice da tarifa será variável em função do tempo de execução das atividades da OP. A quantidade consumida de tarifa CIP dependerá do tempo de execução da atividade, ou seja, quanto maior a duração de uma atividade, maior será o consumo de tarifa CIP, sendo que esse tempo é contabilizado em minutos. Entenda melhor, com o seguinte exemplo:

Se o Tipo de Índice for Variável e o Índice for 3, para cada minuto de atividade serão consumidas 3 tarifas, independente da quantidade de produto acabado produzida nesse tempo. Logo, no exemplo apresentado, se o tempo de atividade for 10 minutos, serão consumidas 30 tarifas.

**Observação:** o sistema considera o tempo em que a atividade foi iniciada até o momento da inclusão do apontamento no cálculo do tempo que será utilizado.

**Tipo de Execução:** utiliza-se este campo para determinar o tipo de execução que será considerado. Este campo só ficará visível quando o campo Tipo de Índice estiver configurado com a opção Variável (Execução de atividades).

- Parada: considera **além** das execuções Paradas ("P"), as execuções de Finais de Turno ("T") e Suspensas ("S").
- Todos: considera **todas** as execuções, Normais ("N"), Paradas ("P"), Finais de Turno ("T") e Suspensas ("S").
- Normal: considera **somente** as execuções Normais ("N").

![Imagem 11: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16645227887767) **Informações adicionais:**

1. Tendo-se tarifas em comum no Processo e na Atividade, a tarifa da Atividade terá prioridade. Sendo que, se a tarifa estiver configurada no Processo como **"Variável"** e a mesma não existir nas Atividades, o índice gerado será em função da execução de cada uma das Atividades.
2. No primeiro apontamento será utilizada a data de início da atividade como data início do filtro de execuções.

**Índice:** especifica-se neste campo a quantidade da tarifa por unidade produzida deste produto, neste caso o Produto Acabado.

**UN. Consumo:** este campo é destinado a especificar-se a unidade de consumo para a tarifa neste produto, neste caso o Produto Acabado.

Para gerenciar as alterações realizadas no registro, você pode conferir nessa aba o usuário responsável pelo cadastro e a data e hora da inclusão do registro. Pode-se verificar também o usuário da última alteração, bem como a data e hora da última alteração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Terceiros (Parceiros)

Esta aba será habilitada, se no [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050884074), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050884074-Processo-Produtivo#h_01ED46ETZHVXW236BVVQ7JZWZ5), a marcação **"Produção terceirizada"** estiver habilitada.

![Imagem 12: Esta aba será habilitada, se no Processo Produtivo , aba Geral , a marcação "Produção terceirizada" estiver habilitada.](https://ajuda.sankhya.com.br/hc/article_attachments/1500000587761)

Nela determina-se o Parceiro Terceiro correspondente ao produto, bem como, se este é o Parceiro Terceiro Preferencial do item em questão. É possível configurar-se apenas um parceiro preferencial para cada produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Recursos do Centro de Trabalho

Nesta aba, cadastre a **"Atividade"** do Processo Produtivo que será realizada nos Centros de Trabalho **"Categoria de Recurso"** e **"Quantidade de Utilização"** do recurso.

![Imagem 13: Nesta aba, cadastre a "Atividade" do Processo Produtivo que será realizada nos Centros de Trabalho "Categoria de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000587921)

**Sub-aba Segurança**

Para gerenciar as alterações realizadas no registro, você pode conferir nessa seção o usuário responsável pelo cadastro e a data e hora da inclusão do registro. Pode-se verificar também o usuário da última alteração, bem como a data e hora da última alteração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Tempo de Processamento

Nesta aba, você poderá cadastrar Tempo de Processamento para cada atividade criada no Processo Produtivo, em que tem-se disponível os campos **"Centro de Trabalho"**, **"Tipo de tempo"**, **"Tempo da atividade"** e **"Unidade de tempo"**.

![Imagem 14: Nesta aba, você poderá cadastrar Tempo de Processamento para cada atividade criada no Processo Produtivo , em que…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000576042)

Por meio da marcação **"Padrão"**, o referido registro configurado será considerado como padrão, quando o campo **"Tipo Alocação"** do pop-up **"Alocações de Centro de Trabalho"**, localizado no ![Imagem 15: Por meio da marcação "Padrão" , o referido registro configurado será considerado como padrão, quando o campo "Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/16645239864471) [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) do [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533) for configurado com a opção **"Sugere CT Padrão (+OP no MPS)"**. Sabendo disso, a hierarquia abaixo será respeitada para a alocação de Centro de Trabalho:

![Imagem 16: Composição do produto: caso houver um Centro de Trabalho preenchido na tela de Composição do Produto e configurado como…](https://ajuda.sankhya.com.br/hc/article_attachments/21078546639127) **Composição do produto:** caso houver um Centro de Trabalho preenchido na tela de Composição do Produto e configurado como Padrão, esse Centro de Trabalho será considerado o padrão;

![Imagem 17: Categoria de centro de trabalho: se não houver um Centro de Trabalho configurado como Padrão na tela de Composição do…](https://ajuda.sankhya.com.br/hc/article_attachments/21078576396823) **Categoria de centro de trabalho:** se não houver um Centro de Trabalho configurado como Padrão na tela de Composição do Produto, o sistema irá buscar o Centro de Trabalho padrão no campo **"Centro de Trabalho Padrão"** da tela [Categoria de Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119033).

**Sub-aba Segurança**

Para gerenciar as alterações realizadas no registro, você pode conferir nessa seção o usuário responsável pelo cadastro e a data e hora da inclusão do registro. Pode-se verificar também o usuário da última alteração, bem como a data e hora da última alteração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Formulários

```
                Esta aba estará disponível a partir da versão 4.17 do sistema.
```

Esta aba será apresentada somente quando o Processo Produtivo informado na Composição do Produto possuir algum [Formulário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) do tipo **"Formulário de Atividade"** cadastrado.

![Imagem 18: Esta aba será apresentada somente quando o Processo Produtivo informado na Composição do Produto possuir algum…](https://ajuda.sankhya.com.br/hc/article_attachments/10976863502999)

Nesta aba você pode vincular os formulários do tipo Formulário de Atividade para os Produtos Acabados configurados no Processo Produtivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Botões no topo da tela

Os botões localizados na parte superior da tela possuem diferentes funcionalidades, vejamos sobre cada uma delas:

**Botão Versionar**

Existem determinados momentos nas indústrias em que modificações simples no Processo Produtivo precisam ser realizadas, como por exemplo, a existência de novas atividades de produção, novas operações de estoque, novas listas de materiais etc. Porém, como já existem Ordens de Produção em andamento para o processo, essas alterações devem surtir efeito apenas para as ordens criadas posteriormente às alterações.

Esta é a função do botão **"Versionar"**; ele irá criar uma nova versão para o processo produtivo selecionado, de modo que as Ordens de Produção que se encontram em andamento terão suas características e configurações mantidas, e a nova versão estará apta a receber as modificações necessárias.

Caso seja feita a tentativa de alteração em um Processo Produtivo que possua Ordens de Produção para ele lançadas, será exibida a seguinte mensagem:

**"Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição."**

**Botão Resumo MPs**

O Botão ![Imagem 19: O Botão ao ser acionado, será apresentado um resumo de todas as matérias primas referentes ao produto acabado e seus…](https://ajuda.sankhya.com.br/hc/article_attachments/360078892154) ao ser acionado, será apresentado um resumo de todas as matérias primas referentes ao produto acabado e seus níveis hierárquicos.

![Imagem 20: O Botão ao ser acionado, será apresentado um resumo de todas as matérias primas referentes ao produto acabado e seus…](https://ajuda.sankhya.com.br/hc/article_attachments/360101673833)

Para que o total da quantidade de matéria-prima seja exibido ao acionar o botão Resumo MPs, é necessário ativar o parâmetro **"Visualizar total da quantidade de MP na grade - VISUTOTALQTDMP"**.

**Botão Ver Custos**

Ao selecionar o botão ![ver](https://ajuda.sankhya.com.br/hc/article_attachments/15525250573847), o sistema exibirá o pop-up **"Visualizar Custos de Produção"** que trará informações referente ao custo do processo selecionado.

[GIF animado: Imagem 22: Ao selecionar o botão , o sistema exibirá o pop-up "Visualizar Custos de Produção" que trará informações referente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/360099460734)

Desta forma, ao clicar duas vezes em um item exibido na grade ou no botão , serão exibidos os detalhes de cada item disponível. Além de que, por meio do campo **"Tipo de Custo"**, você poderá alterar o tipo de custo a ser exibido no pop-up.

**Observação:** Em determinadas situações, ao tentar visualizar os custos pela tela de "Composição de Produtos" (Produção > Cadastros), o sistema pode solicitar permissão de acesso à tela Curva ABC, impedindo a abertura da consulta mesmo para usuários que atuam exclusivamente no módulo SUP.

**Botão Outras Opções...**

No botão Outras Opções é possível calcular de forma manual o tempo de atravessamento (padrão e parte fixa) para os PA's, esse processo é realizado por meio da opção **"Calcular Tempo de Atravessamento"**. Ao acionar a referida opção, o sistema irá questionar por meio de um pop-up se o cálculo será executado para **"Todos os produtos"** ou **"Apenas os produtos selecionados"**.

Ainda nesse botão, temos a opção **"Copiar Composição do Produto"** que, ao ser acionado, abre um pop-up de mesmo nome:

![Imagem 23: Ainda nesse botão, temos a opção "Copiar Composição do Produto" que, ao ser acionado, abre um pop-up de mesmo nome:](https://ajuda.sankhya.com.br/hc/article_attachments/1500014089961)

Nesse pop-up você deve informar o **"Produto Origem"**, ou seja, o produto que terá sua fórmula copiada.

**Observação:** o Produto deve ser um que já esteja cadastrado como PA do mesmo Processo Produtivo e versão que o PA em edição.

Você ainda deve definir nesse pop-up se deseja que a composição de todas as atividades sejam copiadas, através da marcação **"Copiar de todas as atividades"** ou se deseja selecionar determinadas atividades, por meio da marcação **"Copiar das atividades selecionadas"**; essa última marcação apenas ficará disponível quando a marcação Copiar de todas as atividades estiver desabilitada.

Fazendo a escolha das opções, ao clicar em **"OK"**, o sistema apresentará a mensagem abaixo:

**"Atenção! Esta operação substituirá os dados deste PA de acordo com as opções selecionadas. Deseja prosseguir?"**

Se você clicar em **"Sim"**, será feita a cópia da composição do produto selecionado de acordo com as opções escolhidas.

Por meio da opção **"Histórico Cadastro"**, você pode verificar o histórico de alteração, inclusão e exclusão realizada em cada aba. Observe no gif abaixo, um exemplo de quando o registro é excluído na aba.

[GIF animado: Imagem 24: Por meio da opção "Histórico Cadastro" , você pode verificar o histórico de alteração, inclusão e exclusão realizada em…](https://ajuda.sankhya.com.br/hc/article_attachments/10785774768535)

**Botão Anexar**

O botão **"Anexar"** ao ser acionado exibe um pop-up que permite adicionar documentos ou link's no [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050884074).

[GIF animado: Imagem 25: O botão "Anexar" ao ser acionado exibe um pop-up que permite adicionar documentos ou link's no Processo Produtivo .](https://ajuda.sankhya.com.br/hc/article_attachments/1500000576662)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

## Parâmetros que influenciam a rotina

**Usar o Tempo de Processamento das atividades no cálculo do carga máquina - USATEMPOPROCESS:** quando ligado, serão considerados os valores dos campos Tempo da atividade, Tipo de tempo e Unidade de tempo da aba [Tempo de processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abatempodeprocessamento), para o cálculo da ocupação em horas.
Por outro lado, caso o parâmetro esteja desligado, será considerada a capacidade da máquina x a disponibilidade instalada dos turnos (horas) x quantidade dia MPS.

Além disso, estando desligado, ao gerar a carga máquina na tela de [Planejamento de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I-), o cálculo da carga máquina irá desconsiderar o tempo de processamento dos produtos por atividade e considerar a capacidade do CT.

**Importante:**

- Se o cadastro da capacidade for em dia, semana ou mês, o sistema irá utilizar para o cálculo o campo **"Capacidade (UN/hr)"**.
- O % de carga será o resultado da ocupação em horas/disponibilidade em horas.
- O campo Tempo da atividade deve estar preenchido com o valor diferente de zero para que seja feito o cálculo.
- Para o cálculo, deve ser usado o valor do campo Tempo por hora da tela [Capacidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611014-Capacidades) (com o parâmetro desligado). Por exemplo, uma empresa produz um rolo de bobina de papel para jornal por dia, ou seja 1 dia = 24 horas ou 0,04 rolos por hora (=1/24).
- O dia produtivo é a soma dos turnos de trabalho cadastrados. Se não houver cadastro de turno, será considerado o dia com 24 horas.
- A semana produtiva considera a semana com os turnos cadastrados menos o descanso semanal (sem cadastro de turno e/ou horas de produção).
- Será considerado como indisponibilidade de produção os cadastros das paradas programadas (pausas, refeição, etc...) da tela [Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118133-Carga-Hor%C3%A1ria) e as horas cadastradas na tela [Indisponibilidade de CT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611514-Indisponibilidade-de-Centro-de-Trabalho), se esse cadastro coincidir dentro do período do MPS.
- Primeiramente, o sistema fará a busca do tempo de processamento na tela Composição do Produto e, caso não tenha cadastro, buscará na atividade dentro do [roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058453293-Bot%C3%A3o-Roteiro) do [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova).
- Nos casos em que o centro de trabalho possuir diferentes capacidades, será considerada a menor como padrão.

As informações acima referente ao parâmetro USATEMPOPROCESS estão disponíveis a partir da versão **4.16** do sistema.

**prod.permit.edit.mps.producao.composicao - PERMITEDITMP:** ao habilitar esse parâmetro, o sistema não permitirá que a edição de uma matéria-prima seja salva sem realizar um novo versionamento do [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo).

**Visualizar total da quantidade de MP na grade - VISUTOTALQTDMP:** com este parâmetro ativado, será possível visualizar o total da quantidade de matéria-prima diretamente no pop-up exibido ao acionar o botão ![Imagem 26: Visualizar total da quantidade de MP na grade - VISUTOTALQTDMP: com este parâmetro ativado, será possível visualizar o…](https://ajuda.sankhya.com.br/hc/article_attachments/360078892154) **"Resumo MPs"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top)

![Imagem 27: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16645227897879) Acesse também:

[Importador Fórmula de Composição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050833594)
