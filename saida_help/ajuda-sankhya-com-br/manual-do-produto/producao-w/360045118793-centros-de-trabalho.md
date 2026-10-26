---
id: "360045118793"
titulo: "Centros de Trabalho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:52Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Recurso", "Centro de Resultado", "Atributo", "Centros", "Indisponibilidade", "Modificação", "br.com.sankhya.mgeprod.cad.centro.trabalho", "Centros de Trabalho manual", "Setup", "Capacidade", "Cleanup", "Trabalho", "Produção", "Cadastro", "Eficiência operacional", "Integração e otimização", "Controle e ajustes precisos", "OEE"]
---

# Centros de Trabalho

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312786962967) Módulo: Produção > Cadastros
```

---

São realizados aqui os cadastros dos Centros de Trabalho envolvidos em uma planta de manufatura.

Centro de Trabalho é entendido neste contexto como a estrutura organizacional onde as operações de manufatura acontecem, ou seja, onde as matérias-primas, com a influência de máquinas, equipamentos e mão-de-obra, são transformados em produto acabado (PA).

Pode ser considerado um Centro de Trabalho, uma máquina, uma equipe ou uma junção de ambos. Além disso, ele apresenta capacidade produtiva e participa ativamente de uma planta de manufatura.

Para início do cadastro de um novo Centro de Trabalho, teremos o preenchimento do campo **"Código"**, que pode ser realizado de forma automática pelo sistema, ou de forma manual, dependendo da configuração realizada na opção **"Numeração"**, botão ![Imagem 2: Para início do cadastro de um novo Centro de Trabalho , teremos o preenchimento do campo "Código" , que pode ser…](https://ajuda.sankhya.com.br/hc/article_attachments/16644674080919) **"Configuração da Tela"**.

No campo **"Descrição"**, informe o nome do Centro de Trabalho; este é um campo de preenchimento obrigatório, essencial para continuidade no cadastro.

Para complemento do cadastro, são disponibilizadas cinco abas na qual são preenchidas as especificidades de cada Centro de Resultado. São elas:

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abageral) |  | [Aba Atributos de Setup](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abaatributosdesetup) |
| --- | --- | --- |
| [Aba Capacidade por Recurso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abacapacidadeporrecurso) |  | [Aba Histórico de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abahistricodeuso) |
| [Aba Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abarecursos) |  | [Aba Produto Acabado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abaprodutoacabado) |
| [Aba OEE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abaoee) |  | [Botão Indisponibilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#botoindisponibilidade) |
| [Botão Liberar C.T](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#botaoliberarct) |  |  |

## Aba Geral

São realizadas aqui as especificações gerais, de capacidade e de setup/cleanup do Centro de Trabalho.

![Imagem 3: São realizadas aqui as especificações gerais, de capacidade e de setup/cleanup do Centro de Trabalho .](https://ajuda.sankhya.com.br/hc/article_attachments/360061021614)

Informe no campo **"Quantidade de Alocações"**, a quantidade de OP's ([Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313)) nas quais o Centro de Trabalho está alocado, lembrando que, OP's no estado cancelado e finalizada não são consideradas.

#### Seção Informações Gerais

O campo **"Categoria"** é preenchido com a categoria que o Centro de Trabalho se encaixa. Estas são cadastradas previamente na tela [Categorias de Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119033).

Informe no campo **"Planta"** a planta que corresponde ao Centro de Trabalho. As plantas são cadastradas previamente na tela [Plantas de Manufatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119293).

O campo **"Usuário Responsável"** está destinado ao preenchimento do usuário responsável pelo Centro de Trabalho. Os usuários aqui apresentados, são aqueles inseridos previamente no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874). Assim como os dois últimos campos apresentados, este é de preenchimento obrigatório.

Determine no campo **"Centro de Resultado"** o Centro de Resultado relacionado ao Centro de Trabalho. Os Centros de Resultado são cadastrados antecipadamente na tela [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793), e serão úteis na realização da apropriação de custos.

Utilize o campo **"Carga Horária"** para preenchimento da carga horária do Centro de Trabalho. As Cargas Horárias aqui apresentadas são as cadastradas previamente na tela [Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118133). Caso este campo não seja preenchido, o sistema irá utilizar a carga horária padrão da planta na qual o Centro de Trabalho pertence.

**"OEE"** é utilizado para especificar o índice OEE (Overall Equipment Effectiveness - Eficácia Global do Equipamento) do Centro de Trabalho.  Esse índice pode ser utilizado para ajustar o cálculo de capacidade do Centro de Trabalho no momento da geração do planejamento de produção e também para os cálculos de projeção de término do processamento.

Preencha o campo **"Nome da Impressora"** com o nome da impressora utilizada no Centro de Trabalho; caso necessário esta pode sofrer roteamento.

No campo **"Máquina Principal"** realize o vínculo de uma máquina ao Centro de Trabalho, definindo a mesma como máquina principal. A informação aqui vinculada ganha melhor entendimento, quando o Centro de Trabalho é de fato uma máquina ou possui uma forte relação com uma máquina principal. As máquinas aqui apresentadas são as foram cadastradas previamente na tela [Máquinas de Manufatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611374).

Informe no **"Local de Estoque"**, o local de estoque do Centro de Trabalho, local que deve ser cadastrado anteriormente na tela [Cadastro de Locais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602894). Este local deve ser utilizado em operações que não possuam área de destino definido, e detêm prioridade sobre o local de manufatura do processo produtivo.

Determine no campo **"Operação"** a forma de operação do Centro de Trabalho em relação a seu compartilhamento. São apresentadas duas opções de escolha:

- **Exclusivo:** O Centro de Trabalho irá participar de uma operação por vez, utilizando o controle por fila destas operações;
- **Compartilhado:** O Centro de Trabalho poderá realizar diversas operações ao mesmo tempo, de ordens diferentes.

####

#### Seção Capacidade

Insira no campo **"Capacidade"** a especificação da capacidade do Centro de Trabalho. A capacidade é previamente cadastrada na tela [Capacidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611014). Seu preenchimento é obrigatório.

Preencha o campo **"Capacidade Mínima"** com a capacidade mínima de operação do Centro de Trabalho, ou seja, o volume mínimo de trabalho suportado pela operação do centro. Caso seja preenchido com "0" (zero), representa que não existe limite inferior; quando vazio, o campo irá receber o valor "0" (zero).

Informe no campo **"Capacidade Padrão"** a capacidade padrão de operação do Centro de Trabalho, ou seja, a condição padrão de operação do centro. Este valor deve ser considerado padrão independente do produto acabado.

O campo **"Capacidade Máxima"** é alimentado com a capacidade máxima de operação do Centro de Trabalho; mesmo que sejam adicionados mais recursos, sua capacidade não aumenta. Em muitos casos, esta capacidade possui ligação com o limite de máquina ou de processamento da mão-de-obra.

**Nota:** a capacidade mínima deve ser menor ou igual a capacidade padrão, que por sua vez deve ser menor ou igual a capacidade máxima.

O campo **"Capacidade por Hora"** não é editável e apresentará os resultados em unidades/horas.

**Observação:** no cálculo da capacidade será descontado o tempo de paradas e feriados apontados no sistema.

#### Seção Capacidade de Carga

Capacidade de Carga pode ser entendido como a limitação que os equipamentos possuem em seu compartimento de armazenamento de produtos durante o processamento.

Por meio do campo **"Carga Mínima"**, defina a capacidade mínima de carga do Centro de Trabalho.

O campo **"Carga Máxima"** comportará a capacidade máxima de carga do Centro de Trabalho.

**Nota:** caso os campos Carga Mínima e Carga Máxima não estejam preenchidos, não haverá uma limitação de carga máxima ou mínima para o Centro de Trabalho.

Informe no campo **"Unidade"** a unidade pertinente a carga do Centro de Trabalho.

Quando a marcação **"Restringir uso pela Capacidade de Carga"** for selecionada, definirá que o Centro de Trabalho tem seu uso restrito à OPs cujo tamanho de lote esteja compatível com a sua Capacidade de Carga. Deste modo, os Centros de Trabalho cujo Capacidade de Carga seja diferente do tamanho de lote da OP não devem estar disponíveis para uso/seleção.

#### Seção Setup/Cleanup

Determine no campo **"Tipo de Setup"** a necessidade de setup do Centro de Trabalho dentre as seguintes opções:

- **Sempre:** O Centro de Trabalho deverá passar pelo setup incondicionalmente;
- **Condicional:** O setup do Centro de Trabalho será necessário caso o estado atual não atenda ao produto acabado a ser processado;
- **Nunca:** O Centro de Trabalho não exige setup (opção comum em Centros de Trabalho apenas ne mão-de-obra).

Ao efetuar a marcação **"Exige Cleanup"**, significa que o Centro de Trabalho exige cleanup (limpeza ou desmonte) após o uso. Para os casos em que o mesmo Centro de Trabalho é utilizado em diversas atividades no mesmo processo, utilizando-se o mesmo setup, esta marcação deve manter-se desabilitada.

Preencha o campo **"Tempo Padrão de Setup"** com o tempo em minutos, referente a realização do setup do Centro de Trabalho. Este tempo será genérico para todos os produtos acabados processados neste Centro de Trabalho.

Informe no campo **"Tempo Padrão de Cleanup"** o tempo padrão em minutos para realização do cleanup do Centro de Trabalho. Este campo será habilitado apenas quando a marcação Exige Cleanup estiver efetuada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Aba Atributos de Setup

Nesta aba são inseridos os atributos que devem ser considerados no setup de um Centro de Trabalho.

Estes atributos, juntamente com a lista de equipamentos apontáveis, formam o estado atual do Centro de Trabalho. Esse estado pode ser utilizado para determinar a necessidade ou não de setup no Centro de Trabalho, de acordo com o produto acabado que está agendado para ser processado em seguida.

![Imagem 4: Estes atributos, juntamente com a lista de equipamentos apontáveis, formam o estado atual do Centro de Trabalho . Esse…](https://ajuda.sankhya.com.br/hc/article_attachments/360061940453)

O campo **"Código"** será automaticamente alimentado a cada inserção de um novo registro. Representa o código da alocação cadastrada, de modo a identificá-la.

Defina no campo **"Tipo"** qual o tipo de atributo que está sendo vinculado ao Centro de Trabalho. Você poderá escolher dentre as seguintes opções:

- Inteiro;
- Decimal;
- Texto curto;
- Texto longo;
- Lista;
- Referência.

Ao efetuar a marcação **"Considerar como Estado do CT"**, o sistema irá considerar o atributo no estado do Centro de Trabalho. Atributos que não fazem parte do Centro de Trabalho não serão considerados no teste de estado, no entanto vão estar disponíveis para serem informados no formulário de setup.

Informe no campo **"Peso Relativo"** o peso desse atributo ao setup do Centro de Trabalho, ou seja, o quanto este atributo representa no esforço necessário de setup do Centro de Trabalho. Este valor será utilizado quando existir mais de um Centro de Trabalho disponível para execução daquela operação produtiva, onde então será comparado pelo sistema qual Centro de Trabalho está mais próximo em termos de setup para assim determinar qual utilizar.

**Observação:** quanto maior este valor, mais importante é o atributo para o setup do Centro de Trabalho. Quanto maior a soma de todos os atributos com valores ao necessário, mais próximo estará o setup daquele centro de trabalho, do estado necessário.

Utilize o campo **"Instância de Referência"** para selecionar qual instância de dados este atributo representa. Este campo estará habilitado apenas quando o tipo do atributo for **"Referência"**.

No campo **"Lista"** são listados os valores que este atributo pode assumir. Ele estará habilitado apenas quando o tipo do atributo for **"Lista"**. A lista deverá ser separada por enter. Cada linha será uma opção e a ordem determinará o valor (1,2,3,...) que será gravado na tabela de valores na coluna de valor inteiro. Caso seja necessário arbitrar valores, basta colocar **<NRO>=<LABEL>**, por exemplo:

10 = Inativo

20 = Ativo

O campo **"Expressão"** será utilizado para especificar uma expressão em linguagem Java Scritp que será avaliada no formulário de setup do Centro de Trabalho.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Aba Capacidade por Recurso

Nesta aba são determinadas as capacidades específicas através de uma relação Categoria de Recurso X Produto Acabado X Centro de Trabalho.

Com isto, você poderá determinar capacidades específicas para qualquer tipo de recurso em qualquer configuração, seja esta específica por produto acabado ou por Centro de Trabalho.

![Imagem 5: Com isto, você poderá determinar capacidades específicas para qualquer tipo de recurso em qualquer configuração, seja…](https://ajuda.sankhya.com.br/hc/article_attachments/360061021634)

O campo **"Núm. da Regra"** será automaticamente alimentado a cada inserção de um novo registro. Representa o código da regra de capacidade cadastrada, de modo a identificá-la.

Determine no campo **"Categoria de Recurso"** uma categoria de recurso para a regra de capacidade que está sendo configurada. As categorias aqui apresentadas para escolha, são as previamente cadastradas na tela [Categorias de Recurso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119273).

Informe no campo **"Capacidade"** o domínio das capacidades do Centro de Trabalho para aquela regra de capacidade. As capacidades aqui disponibilizadas, são as cadastradas antecipadamente na tela [Capacidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611014).

Preencha o campo **"Produto"** com o produto acabado que faz parte da regra de capacidade do Centro de Trabalho. Não sendo informado nenhum produto, significa que a regra valerá para qualquer produto.

No campo **"Capacidade Mínima"** determine a capacidade mínima de operação do Centro de Trabalho para a regra de capacidade configurada. Caso seja preenchido com "0" (zero), representa que não existe limite inferior.

Informe no campo **"Capacidade Padrão"** a capacidade padrão de operação do Centro de Trabalho para a regra de capacidade configurada.

O campo **"Capacidade Máxima"** é alimentado com a capacidade máxima de operação do centro de trabalho para a regra de capacidade configurada. Em muitos casos, esta capacidade possui ligação com o limite de máquina ou de processamento da mão-de-obra. Se for preenchido com "0" (zero), o sistema irá utilizar a capacidade máxima do Centro de Trabalho.

**Nota:** a Capacidade Mínima deve ser menor ou igual a capacidade padrão, que por sua vez deve ser menor ou igual a capacidade máxima.

Defina no campo **"Tipo de Capacidade"** qual o tipo da regra de capacidade configurada. São apresentadas as seguintes opções de escolha:

- **Adicionar/Subtrair:** Ao escolher esta opção, será feita a soma ou subtração dessa capacidade (mínima, padrão e máxima) a capacidade do Centro de Trabalho.
- **Total:** Esta opção determina que a capacidade configurada será a capacidade do Centro de Trabalho para aquele produto e para aquela categoria de recurso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Aba Histórico de Uso

Esta aba está destinada à verificação do histórico de utilização do Centro de Trabalho. Teremos aqui informações a respeito do Número da Ordem de Produção, Atividade, as Datas e Horários de Alocação e Liberação do Centro, bem como os Usuários encarregados destas últimas funções, que poderão ser apenas consultadas.

![Imagem 6: Esta aba está destinada à verificação do histórico de utilização do Centro de Trabalho . Teremos aqui informações a…](https://ajuda.sankhya.com.br/hc/article_attachments/360061940473)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Aba Recursos

Nesta aba são listados os recursos necessários para a operação do Centro de Trabalho selecionado. Alguns recursos podem modificar a capacidade produtiva do Centro de Trabalho quando é adicionado uma quantidade diferente do recurso, ou mesmo quando este recurso é uma ferramenta com capacidade própria.

![Imagem 7: Nesta aba são listados os recursos necessários para a operação do Centro de Trabalho selecionado. Alguns recursos podem…](https://ajuda.sankhya.com.br/hc/article_attachments/360061021674)

No campo **"Cat. de Recurso"** é feita a seleção da categoria do recurso. Caso a categoria definida seja uma categoria "sintética" e apontável, o formulário de apontamento de recursos de Centro de Trabalho irá exigir uma categoria "analítica" desta.

Informe no campo **"Quantidade"** a quantidade necessária do recurso para a operação padrão do Centro de Trabalho.

Utilize o campo **"Modificação de Capacidade"** para determinar "se" e "como" o recurso modifica a capacidade do Centro de Trabalho. São disponibilizadas as seguintes opções para escolha:

- **Neutra:** Não modifica a capacidade padrão, caso seja adicionada uma quantidade diferente deste recurso;
- **Proporcional:** Modifica a capacidade, proporcionalmente, em relação à quantidade alocada, até o teto da capacidade máxima do Centro de Trabalho. Por exemplo, se a capacidade padrão é 1000UN/Dia utilizando 5 recursos deste tipo, então a cada unidade alocada deste recurso aumentamos a capacidade em 20%;
- **Fator de capacidade:** A capacidade é modificada de acordo com um fator da quantidade alocada, informada no campo seguinte **"Fator capacidade"**.

O campo Fator Capacidade deve ser utilizado para determinar um fator de modificação da capacidade. Se a capacidade padrão é definida utilizando quatro recursos deste tipo, logo, será concluído que cada recurso é responsável por 25% da capacidade, portanto se o valor neste campo for 0,5 o sistema irá aumentar a capacidade em 12,5% para cada nova unidade adicionada deste recurso.

Quando o vínculo do recurso do Centro de Trabalho tiver que considerar um produto específico, o cadastro deverá ser realizado através do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), [Aba Manufatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamanufatura), sub-aba **"Recursos"**. A configuração de capacidade para esses recursos deve ser configurada através da aba [Capacidades por Recurso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abacapacidadeporrecurso) desta mesma tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Aba Produto Acabado

Nesta aba será realizado o vínculo de Produtos Acabados ao Centro de Trabalho, sendo possível determinar informações específicas dessa relação, como por exemplo, capacidade, tempo de setup e atributos de setup.

| [Sub-aba Capacidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#sub-abacapacidade) |  | [Sub-aba Setup/Cleanup](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#sub-abasetup/cleanup) |
| --- | --- | --- |
| [Sub-aba Atributos de Setup](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#sub-abaatributosdesetup) |  |  |

Na utilização desta aba, inicialmente informe o campo **"Produto"**, onde é selecionado qual o produto que será configurado no Centro de Trabalho. O preenchimento deste campo é obrigatório.

**Observação:** para que seja possível realizar a vinculação de um produto inativo neste campo, é necessário habilitar o parâmetro **"Permitir vincular produtos inativos a Processo Produtivo - PRODINATPROC"**.

Além disto, quando o produto acabado selecionado possuir controle adicional por lista, esta deverá ser especificada no campo **"Controle"**.

**Importante:** para que o produto esteja disponível no filtro do campo Produto, é necessário que este produto tenha antes um processo produtivo que o produza. Ele deve estar cadastrado como Produto Acabado (PA) para algum processo na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

**Sub-aba Capacidade**

Nesta sub-aba, você poderá configurar as capacidades do Centro de Trabalho para a produção do produto acabado selecionado.

![Imagem 8: Nesta sub-aba, você poderá configurar as capacidades do Centro de Trabalho para a produção do produto acabado…](https://ajuda.sankhya.com.br/hc/article_attachments/360061940493)

No campo **"Capacidade"** determine o domínio das capacidades do Centro de Trabalho para a produção do produto. As capacidades aqui disponíveis, são as cadastradas anteriormente na tela [Capacidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611014).

Defina no campo **"Capacidade Mínima"** a capacidade mínima de operação do Centro de Trabalho para a produção do produto, ou seja, o volume mínimo de trabalho em que a operação do centro é viável na produção do produto. Caso seja preenchido com "0" (zero), representa que não existe limite inferior.

Informe no campo **"Capacidade Padrão"** a capacidade padrão de operação do Centro de Trabalho para a produção do produto.

O campo **"Capacidade Máxima"** é alimentado com a capacidade máxima de operação do Centro de Trabalho para a produção do produto, ou seja, mesmo que sejam adicionados mais recursos, sua capacidade não aumenta. Em muitos casos, esta capacidade possui ligação com o limite de máquina ou de processamento da mão-de-obra. Se for preenchido com "0" (zero), o sistema irá utilizar a capacidade máxima do Centro de Trabalho.

**Nota:** a capacidade mínima deve ser menor ou igual a capacidade padrão, que por sua vez deve ser menor ou igual a capacidade máxima.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abaprodutoacabado)

**Sub-aba Setup/Cleanup**

Esta sub-aba, permite configurar os tempos de setup e cleanup para a produção do produto selecionado no Centro de Trabalho.

![Imagem 9: Esta sub-aba, permite configurar os tempos de setup e cleanup para a produção do produto selecionado no Centro de…](https://ajuda.sankhya.com.br/hc/article_attachments/360061021694)

Informe no campo **"Tempo de Setup"** o tempo em minutos necessário para o setup do Centro de Trabalho para o produto. Caso este tempo seja "0" (zero), o sistema irá considerar o tempo de setup padrão do Centro de Trabalho.

Registre no campo **"Tempo de Cleanup"** o tempo em minutos necessário para o cleanup do Centro de Trabalho para o produto. Caso este tempo seja "0" (zero), o sistema irá considerar o tempo de cleanup padrão do Centro de Trabalho.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abaprodutoacabado)

**Sub-aba Atributos de Setup**

Nesta sub-aba, você definirá o valor de um atributo já cadastrado no Centro de Trabalho, para o produto selecionado.

![Imagem 10: Nesta sub-aba, você definirá o valor de um atributo já cadastrado no Centro de Trabalho, para o produto selecionado.](https://ajuda.sankhya.com.br/hc/article_attachments/360061021714)

Especifique no campo **"Atributo"** qual atributo de setup deseja-se configurar para o produto. Os atributos apresentados neste campo, são resultantes de uma pesquisa nos atributos já cadastrados no Centro de Trabalho.

Seguindo o tipo do atributo selecionado no campo anterior, preencha o campo **"Valor"** com o valor do atributo para o produto selecionado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#abaprodutoacabado) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Aba OEE

Nessa aba, teremos os indicadores OEE. Teremos que por meio destes você poderá acompanhar e analisar todas as causas das paradas no(s) Centro(s) de Trabalho além de perdas no desempenho de produção e à qualidade dos produtos, sendo que, desta forma pode-se verificar a eficácia e eficiência de recursos como maquinário, matéria-prima e mão de obra.

No botão **"Histórico"** você poderá visualizar um histórico de **"OEE"**, **"Disponibilidade"**, **"Performance"** e/ou **"Qualidade"**.

No campo **"Tipo de Agrupamento"**, temos as opções abaixo disponíveis:

- Dia;
- Semana;
- Mês;
- Ano;
- Turno;

**Observação:** quando a opção **"Turno"** for escolhida, será disponibilizado ao lado, o campo Turno. Esse campo terá as opções de turnos cadastrados na Carga Horária vinculada ao CT e a opção de filtrar **"Todos"** os turnos.

**Nota:** para a opção Turno do Tipo de Agrupamento, nosso sistema irá considerar no campo **"Período"**, a data e hora inicial e final do turno, quando você selecionar um turno específico e, para a opção Todos, considera a data e hora inicial do primeiro turno e a data e hora final do último turno.

No botão **"Outras Opções..."**, você poderá efetuar o **"Recálculo"** para casos em que houver ajuste/alteração durante determinado período, como uma exclusão de apontamento, assim, um pop-up será aberto para que o período do Recálculo seja selecionado:

[GIF animado: Imagem 11: No botão "Outras Opções..." , você poderá efetuar o "Recálculo" para casos em que houver ajuste/alteração durante…](https://ajuda.sankhya.com.br/hc/article_attachments/360095328274)

Para que os cálculos das paradas sejam corretamente efetuados, realize a marcação **"Considerar paradas planejadas no cálculo do OEE"** da tela [Motivos de Parada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611614-Motivos-de-Parada).

**Importante:** para realizar as configurações de quando serão executadas as rotinas para o cálculo dos indicadores, você deverá ligar o parâmetro **"Agendamento do Job OEE Diário - JOBOEEDIARIO"**.

Através do botão **"Alterar Faixas do gráfico de velocímetro dos indicadores OEE"**, representado pelo ícone ![Imagem 12: Através do botão "Alterar Faixas do gráfico de velocímetro dos indicadores OEE" , representado pelo ícone , você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002702642), você pode configurar os intervalos que deseja para cada uma das quatro faixas de cores que temos. Clicando nesse botão, o pop-up **"Preferências"** será aberto:

[GIF animado: Imagem 13: Através do botão "Alterar Faixas do gráfico de velocímetro dos indicadores OEE" , representado pelo ícone , você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/360103739493)

**Observação:** você não pode cadastrar faixas onde houver intersecção.

**Nota:** a faixa padrão de visualização do velocímetro do OEE é a seguinte:

- Resultado entre 0,00 % a 40.99% é apresentado na cor **vermelha**;
- Resultado entre 41,00 % a 84.99% é apresentado na cor **amarela**;
- Resultado entre 85,00 % a 100,00% é apresentado na cor **verde**;
- Resultado entre 100,01 % a 120,00% é apresentado na cor **azul**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Botão Indisponibilidade

Na parte superior da tela, podemos observar o botão "**Indisponibilidade"**.

![Imagem 14: Na parte superior da tela, podemos observar o botão " Indisponibilidade" .](https://ajuda.sankhya.com.br/hc/article_attachments/360061940513)

Na edição das configurações de um Centro de Trabalho, podemos ter a necessidade de consultar Centros de Trabalho que se encontram ou estiveram indisponíveis por algum motivo. O botão Indisponibilidade visa agilizar esta verificação.

Quando acionado, é aberta diretamente a tela [Indisponibilidade de Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611514):

![Imagem 15: Quando acionado, é aberta diretamente a tela Indisponibilidade de Centro de Trabalho :](https://ajuda.sankhya.com.br/hc/article_attachments/360061940553)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)

## Botão Liberar C.T

O botão **"Liberar C.T"** será habilitado caso o Centro de Trabalho da OP esteja em uso, desta forma, caso seja necessário, pode-se liberar um Centro de Trabalho por meio deste botão para que outra OP/Atividade seja executada.

[Realocar Centro de Trabalho ao continuar atividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#realocarcentrodetrabalhoaocontinuaratividade)

[Continuar atividade com o Centro de Trabalho alocado em outra atividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#continuaratividadecomocentrodetrabalhoalocadoemoutraatividade)

[Parar atividades ao suspender uma Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#pararatividadesaosuspenderumaordemdeprodu%C3%A7%C3%A3o)

![Imagem 16: Parar atividades ao suspender uma Ordem de Produção](https://ajuda.sankhya.com.br/hc/article_attachments/360061021734)

Por meio deste botão, você poderá liberar um Centro de Trabalho que esteja em uso para que outra OP/Atividade seja executada em casos de necessidade de produção.

**Realocar Centro de Trabalho ao continuar atividade**

Na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), no campo **"Tipo Alocação"**, você pode selecionar a opção **"Específico"** e no campo **"Centro de Trabalho"** indicar o Centro de Trabalho da alocação.

Referente ao campo Tipo Alocação, o sistema dispõe das opções:

- **Na inclusão da ordem:** Esta opção faz com que o sistema procure um Centro de Trabalho disponível quando a ordem foi criada;
- **Específico:** Escolhendo esta opção, será utilizado um Centro de Trabalho específico. Para esta opção, o campo Centro de Trabalho, deve ser informado;
- **Antecipado (No Planejamento):** Esta opção fará com que o sistema procure um Centro de Trabalho disponível no momento da geração do planejamento das operações;
- **Usar o padrão:** Por meio desta opção, o sistema irá utilizar o Centro de Trabalho padrão para a categoria definida, atendendo aqueles campos simples onde existem apenas um Centro de Trabalho.

Sendo assim, é necessário a verificação se o C.T da atividade está como exclusivo e liberado para a alocação. Caso o C.T alocado esteja em outra atividade, o sistema exibirá a mensagem:

**"Não é possível continuar a atividade, pois o Centro de Trabalho é exclusivo e está sendo utilizado por  outra atividade."**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#botaoliberarct)

**Continuar atividade com o Centro de Trabalho alocado em outra atividade**

Caso tente-se continuar uma atividade com um Centro de Trabalho que não foi alocado em outra Atividade, não será possível efetuar a realocação desta.

Na tela [Apontamento de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973), campo **"Tipo Alocação"** você poderá marcar a opção **"Específica"** e no campo Centro de trabalho deverá selecionar um CT exclusivo.

Caso o CT esteja em outra atividade, o sistema exibirá a mensagem:

**"Não é possível continuar a atividade, pois o Centro de Trabalho é exclusivo e está sendo utilizado por outra atividade."**

Para alocar CT, na tela Operações de Produção, no campo Tipo Alocação, selecione a opção **"Por categoria"**, o Tipo Alocação deverá ser Específica e, em seguida, executar a realocação do CT para a atividade; caso o CT estiver em outra atividade, o sistema exibirá um pop-up para selecionar-se outro Centro de Trabalho da mesma categoria.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#botaoliberarct)

**Parar atividades ao suspender uma Ordem de Produção**

Ao suspender OP, o sistema apresentará um pop-up referente à esta suspensão, caso existam Centros de Trabalho em um uso para serem liberados:

**"Existem Centros de Trabalho em uso nessa ordem. Deseja realmente suspender e executar a liberação dos Centros de Trabalho?"**

Caso seja confirmado, o **"Tipo"** a ser apresentado será **"Suspenso"**.

**Observação:** nas telas Operações de Produção e Apontamento de Produção, uma atividade suspensa ficará invisível para todos os usuários até que esta seja continuada novamente pelo responsável.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#botaoliberarct) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793-Centros-de-Trabalho#top)
