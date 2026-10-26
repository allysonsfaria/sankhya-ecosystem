---
id: "360044604654"
titulo: "Faturamento de Contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-10-15T12:01:13Z"
rotulos: ["AJUDA DO SKW", "manual", "Faturamento", "Contrato", "CONTGRUPBASEFAT", "Data de Reajuste", "EXIBPARCFATCON", "FATCONTRMESFUT", "Faturamento de Contrato de Fornecedor", "Faturamento de Contratos", "Histórico do Faturamento de Contrato", "Observação Padrão", "Provisões", "QTDMESPROVFATC", "TAXBOLNOT", "TAXBOLNOTTJ", "br.com.sankhya.mgeos.faturamento.contratos", "Faturamento de Contratos manual", "Conta Bancária", "Tipo de Negociação", "CONTSOFT", "Histórico", "Serviços", "GERIMPOSTO", "Perfil de Consumo", "Contrato de Manutenção", "Financeiro", "SOMIMPRETVLRFIN", "Automático e periódico com tela específica para \"Livre\"", "Agrupamento notas únicas e dados de perfil", "Configura parâmetros e lista contratos", "IMPOSTCONT"]
---

# Faturamento de Contratos

```
 Módulo: Contratos e Serviços > Rotinas
```

---

Fatura-se a partir de **"Contratos"** toda negociação com parceiros que contenham as seguintes características:

- Renovação automática;
- Controle de reajuste segundo uma moeda e data base;
- Faturamento conforme periodicidade pré-definida: mensal, semestral e anual.

**Observação:** vale ressaltar que, os Contratos em que o campo **"Periodicidade do Faturamento"** estiver selecionado com a opção **"Livre"**, só podem ser faturados por meio da tela [Faturamento por Período Livre](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113193).

A rotina de Faturamento de Contratos é responsável pela emissão das Notas Fiscais de Serviço. A tela é constituída por duas partes principais, à esquerda existem os painéis para configuração dos parâmetros obrigatórios e os filtros personalizados, à direita estão as grades onde serão listados os contratos a serem faturados e os serviços complementares de ordens de serviços de contrato.

![Imagem 1: No processo de faturamento de serviços , o sistema sempre trará o USOPROD (Usado como) do produto como ‘S’ = Serviço na…](https://ajuda.sankhya.com.br/hc/article_attachments/25938799470359) No processo de **faturamento de serviços**, o sistema sempre trará o **USOPROD (Usado como)** do produto como **‘S’ = Serviço** na nota de venda gerada pelo contrato, independentemente se no contrato existir um produto com **USOPROD** diferente de serviço. Embora seja permitido incluir um produto, ele será interpretado como serviço, pois este é um faturamento de serviço.

**Nota:** a **rotina de Faturamento de Contratos não está preparada para trabalhar com multi-moedas, pois a precificação das notas faturadas é feita pelo contrato e não por tabela de preços.**

O sistema segue uma configuração padrão, para que os registros sejam devidamente apresentados nesta tela, trazendo apenas os contratos que respeitam a seguinte condição:

**"Data base de Reajuste + Frequência de Reajuste (em meses) <= último dia do mês da 'Referencia do Faturamento"** (informada na tela, caso não seja preenchida será considerada a referência corrente).

Ou seja, só será possível faturar contratos onde a Referência considerada se encontre dentro do período de reajuste.

| [Painel de Filtros Personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#paineldefiltrospersonalizados) |  | [Painel de Parâmetros Obrigatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#paineldeparmetrosobrigatrios) |
| --- | --- | --- |
| [Removendo Contratos da Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#removendocontratosdagrade) |  | [Botão Faturar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#botofaturar) |
| [Configurações para o Faturamento...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#configuraesparaofaturamentodecontratos) |  | [Faturamento de Contratos...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#faturamentodecontratoscompagamentodecomisses) |
| [Histórico do Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#histricodofaturamentodecontratos) |  | [Renegociação de Títulos...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#renegociaodettuloseenviodee-mailsautomticos) |
| [Geração do Boleto e envio por E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#h_7815ed9a-9cff-4f62-b9bb-86f2d94ff357) |  | [Renegociação com Agrupamento...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#renegociaocomagrupamentodecontratos) |
| [Faturamento por Perfil de Consumo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#faturamentoporperfildeconsumo) |  | [Rateio de Parcelas Financeiras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#rateiodeparcelasfinanceiras) |
| [Permitir o Faturamento de Contratos...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#permitirofaturamentodecontratosdofornecedor) |  | [Cálculo de IRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#clculodeirf) |
| [Dedução dos custos VA e VT na BC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#dedu%C3%A7%C3%A3odoscustosvaevtnabcdeinss)... |  | [Alerta de contratos a reajustar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#alertadecontratosareajustar) |

## Painel de Filtros Personalizados

![Imagem 2: Painel de Filtros Personalizados](https://ajuda.sankhya.com.br/hc/article_attachments/1500014114902)

Os filtros poderão ser feitos por **"Empresa"**, **"Parceiro"** e **"Data de Reajuste"** do contrato.

A opção **"Considerar Contatos/Perfil/Serviço"** funciona da seguinte maneira:

- Caso o parceiro possua um perfil vinculado e este possua um perfil de consumo, na nota gerada no faturamento do contrato com essa opção marcada serão gerados também itens para cada produto desse perfil de consumo do parceiro;
- Se esta opção estiver desmarcada e o parâmetro **"Contrato para software? - CONTSOFT"** estiver ligado, o sistema validará se existe ISS cadastrado para a relação Natureza x Serviço e incluirá um item na nota com valor zero para o serviço encontrado na relação com a natureza.
- Ao utilizar o parametro CONTSOFT, o parâmetro IMPOSTCONT deverá ser habilitado caso não deseje realizar o recalculo de impostos por meio do item inserido **automaticamente** na nota com valor zerado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Painel de Parâmetros Obrigatórios

![Imagem 3: Painel de Parâmetros Obrigatórios](https://ajuda.sankhya.com.br/hc/article_attachments/1500014114982)

Os campos deste painel são preenchidos com os valores presentes nos seguintes parâmetros:

**TOP Padrão para Faturamento de Contratos - FATSERVTOP:** Campo **"Tipo de Operação"**;

**Tipo de Título para Faturamento de Contratos - FATSERVTIT:** Campo **"Tipo de Título"**;

**Tipo de Negociação para Faturamento de Contratos - FATSERVTPV:** Campo **"Tipo de Negociação"**.

**Observação:** ao acessar essa rotina, caso não haja qualquer informação no campo **"TOP para faturamento em contratos"** no [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) ou de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), ao realizar o faturamento de um contrato, a TOP da nota faturada será a mesma informada no campo **"Tipo de Operação"** dessa tela.

Os **"Parâmetros Obrigatórios"** somente serão utilizados para o faturamento, ou seja, serão utilizados na nota gerada após o faturamento do contrato ou serviço complementar, então não é necessário informá-los para realizar o filtro.

Na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474 "br.com.sankhya.com.cad.observacoesNotas") pode-se cadastrar a observação padrão que será impressa nas Notas Fiscais. Para melhores informações sobre esta tela, verificar a documentação de apoio referente a mesma clicando no link acima.

No faturamento de um Contrato o sistema utiliza a conta informada no campo **"Conta bancária** **empresa"**, da aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), diferentemente dos outros faturamentos que utilizam a conta do Tipo de Negociação.

Se o parâmetro **"Contrato para software - CONTSOFT"** estiver habilitado, será exibido o campo **"Conta Bancária"**. Caso seja necessário utilizar uma conta diferente da conta do cadastro de Parceiros, informe-a neste campo.

No campo **"Data para Faturamento"** informe a data em que o contrato está sendo faturado.

**Observação:** o campo **"Dia do pagamento"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades) do [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), equivale ao dia de vencimento original do título que ainda pode ser alterado no faturamento conforme as configurações do **"Tipo de Negociação"** a ser utilizado. Assim como a marcação **"Considera dia do pagamento como dia útil"** da mesma tela, ou ainda de acordo com o parâmetro **"Transfere vencimento quando fim de semana/feriado - TRANSFVENC"**.

O campo **"Mês para Referência"** corresponderá ao mês de vencimento do contrato. É com base na data informada neste campo que o sistema validará o Tipo de Pagamento definido no Cadastro do Contrato. Este campo virá preenchido com a data para o próximo faturamento, ou seja, o primeiro dia do próximo mês.

A marcação **"Gerar 1 única fatura"**, quando selecionado, irá fazer com que o sistema gere uma única nota agrupando Fatura de Serviços Complementares com Faturamento Mensal do Contrato.  Essa opção estará habilitada somente se o parâmetro de chave CONTSOFT  estiver ligado.

A opção **"Agrupar Contratos"** agrupará o faturamento de vários contratos em uma única nota. O Agrupamento do contrato seguirá a ordem: Parceiro, Dia de Pagamento, Dia útil e Critério de Rateio.

**Observação:** quando você utilizar a marcação acima e faturar, caso possua contratos pro-rata e "não pro-ratas" na seleção, eles não serão agrupados entre si.

**Importante:** ao faturar um contrato que gere comissão, se a opção **"Agrupar Contratos"** se encontrar habilitada, a comissão do contrato não será gerada na nota.

**Nota:** para utilizar esta opção, deve-se ligar os parâmetros **"Utiliza grupos de faturamento de contratos? - GRUPFATCONT?"** e **"Utiliza faturamento de contratos pro rata? - FATCONTPRORATA"**, assim como o campo **"Grupo de Faturamento"** (tela [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774), aba **"Geral"**) que deverá ser preenchido com o faturamento a qual o grupo pertence.

**Observações:**

- O agrupamento de contratos que não são pro-rata respeitará a ordem Parceiro, Dia de Pagamento, Dia útil, Critério de Rateio, TOP e Série.
- Se nos contratos convencionais (não pro-rata) tiver produtos com TOP's diferentes, o sistema respeitará essa configuração e irá faturar esses produtos separadamente, assim como ocorre nos contratos pro-rata.
- Caso algum dos contratos selecionados (não pro-rata) tenham produtos com TOP's distintas, o sistema irá faturar separadamente os produtos que possuem TOP's diferentes, ou seja, não agrupando esses produtos.

Referente ao parâmetro **"Valida confirmação nota contrato pro-rata pela TOP - VALCONPRORATOP"**, teremos os seguintes comportamentos:

- Se estiver ligado, será verificada a configuração da TOP para confirmar ou não as notas geradas a partir de contratos pró-rata, desde que o parâmetro GRUPFATCONT também esteja ligado.
- Caso esteja desligado, nunca serão confirmadas as notas geradas a partir de contratos pró-rata, desde que o parâmetro GRUPFATCONT esteja ligado, independente da configuração da TOP.
- Se o parâmetro GRUPFATCONT estiver desligado ou o contrato não for pró-rata, o parâmetro VALCONPRORATOP não terá influência sobre a aprovação das notas, apenas a configuração da TOP.
- Se o parâmetro **"Faturar contratos pro rata sem grupo isoladamente - FATCONPRSGISOL"** estiver ligado e o contrato não tiver grupo de faturamento associado, o parâmetro VALCONPRORATOP também não terá influência sobre a aprovação das notas, apenas a configuração da TOP.

No campo **"Série"**, informa-se a série da nota a ser gerada. Se houver uma série que irá enviar uma Nota Fiscal de Serviço, ao ser informada neste campo, o sistema irá gerar a nota fiscal de serviço automaticamente no final do processo.

**Observações:**

- Se não houver nenhuma informação no campo **"Série para faturamento em contratos"** no [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) ou de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), ao faturar um contrato, a série da nota faturada será àquela informada no campo **"Série"** dessa tela.
- Não havendo informação nos campos TOP para faturamento em contratos e/ou Série para faturamento em contratos nas telas mencionadas acima, ao efetuar o faturamento de um contrato, a TOP e Série da nota faturada serão as mesmas informadas nesses campos, respeitando a hierarquia abaixo:

1. Cadastro de Produtos / Serviço;
2. Cadastro de Contratos, aba Produtos/Serviços, sub-aba Geral;
3. Cadastro de Contatos, aba Geral.

Os dados inseridos nos campos **"Mês para Referência do V.T. e dos Insumos"** e **"Mês para Referência do V.A"** serão utilizados para preencher os campos de referência da nota que será gerada. Sendo que, estes campos só estarão visíveis na tela quando a TOP informada no campo **"Tipo de Operação"** possuir em sua aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) a marcação **"Tem VA e/ou VT no contrato"** acionada.

**Nota:** as informações destes campos não serão utilizadas na busca dos contratos.

Após informar os Filtros Personalizados e os Parâmetros Obrigatórios, clica-se em **"Aplicar"**.

O sistema apresentará na grade todos os Contratos disponíveis para faturamento que atendam as configurações dos filtros.

**Observação:** ao realizar o procedimento de faturamento, tem-se que os dados bancários correspondentes ao tipo de negociação constarão na nota fiscal. Portanto, diante disto, deve-se considerar as informações abaixo:

Neste cenário, o sistema analisará os seguintes itens:

- Preenchimento do campo **"Tipo de negociação"** (tela [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades));
- Marcação no faturamento de contratos utilizando o tipo de negociação deste;
- Informações inseridas no campo **"Tipo de Negociação"**;
- Configurações do parâmetro **"Tipo de Negociação para Faturamento de Contratos - FATSERVTPV"**.

Ainda neste contexto, em relação aos dados bancários, tem-se que o sistema levará em consideração esta sequência para sua respectiva validação:

a) Se os campos **"Banco"** e **"Conta Bancária"** (tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)) estiverem preenchidos serão utilizados estes dados; ou

b) As configurações registradas no parâmetro **"Conta padrão para financeiro - CONTAPADRAOFIN"**; ou

c) As informações inseridas no campo **"Conta bancária empresa"** ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao)); ou

d) Ainda considerando o tipo de negociação e que a marcação **"Conta padrão para emissão"** esteja acionada (tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas)), tem-se que nos casos em que houverem mais de uma conta bancária, o sistema considerará a conta de menor código, sendo que preferencialmente será utilizada a conta que seja exclusiva da empresa, porém, permitirá também contas não exclusivas.

**Nota:** posto isto, o sistema utilizará estas regras para gerar os dados bancários no faturamento do contrato.

O parâmetro **Determinação do Indicador de Operação - CODINDOPER** determina automaticamente o **Código Indicador da Operação de Fornecimento** seguindo esta ordem de prioridade:

1. [**Cadastro do Serviço (Configurações por Empresa)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa)**:** valor mais específico.
2. [**Cadastro do Serviço (Aba Impostos)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos)**:** valor global do serviço.
3. [**Valor da TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF)**:** utilizado apenas se o cadastro do serviço estiver vazio.

**Nota:** diferente de outros faturamentos, nos contratos o sistema prioriza o cadastro do serviço para garantir que cada item da nota reflita sua natureza real perante a NFS-e Nacional.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Removendo Contratos da Grade

Você poderá faturar todos os contratos de uma só vez ou poderá selecionar os que deseja faturar, excluindo da grade os contratos que não deseja faturar utilizando os botões **"Remove selecionados"** e **"Remove NÃO selecionados"**.

![Imagem 4: Você poderá faturar todos os contratos de uma só vez ou poderá selecionar os que deseja faturar, excluindo da grade os…](https://ajuda.sankhya.com.br/hc/article_attachments/1500014392281)

O contador de registros localizado no canto superior direito da tela exibirá quantos registros existem na grade da aba **"Contratos"**.  Ou seja, esse contador não se refere ao número de registros da grade **"Serviços Complementares"**.

A aba **"Serviços Complementares"** irá conter serviços lançados através de ordens de serviço para o contrato. Como os serviços complementares são cobrados, também será feito o seu faturamento.

**Observação:** esta aba é habilitada nesta tela pelo parâmetro **"Contrato para software? - CONTSOFT"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Botão Faturar

Ao clicar no botão **“Faturar”**, o sistema processará o faturamento de todos os contratos filtrados e mantidos na grade, agrupando aqueles que possuírem as mesmas características de **tipo de serviço, tributação, natureza da operação, cliente e empresa**.

Para cada agrupamento, será gerado um único documento fiscal. Caso seja identificada alguma diferença entre essas características, os contratos serão separados em agrupamentos distintos, gerando um documento fiscal para cada agrupamento.

Para que o processo de faturamento seja simples e dinâmico, o sistema exibirá o pop-up "Resumo do Faturamento" ao finalizar o processamento.

Os contratos com impedimentos no faturamento serão exibidos na aba **"Não faturados"**, apresentando o motivo que impediu o faturamento para que os ajustes sejam realizados. Ao dar um duplo clique em um registro, você será direcionado à tela [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) para agilizar a conferência e correção dos impedimentos apontados.

Os documentos gerados com sucesso a partir do faturamento dos contratos, serão exibidos na aba **"Faturas geradas"**. Ao clicar duas vezes em um registro dessa aba, o sistema irá lançar o documento aberto na tela da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414).

Caso todos os contratos sejam faturados com sucesso, apenas a aba Faturas Geradas será apresentada. Se a situação for contrária e, todos os contratos selecionados na tela possuírem impedimentos, apenas a aba Não faturados será exibida, assim como seus respectivos motivos de impedimento.

**Impedimento por Indicadores Distintos:** se você tentar realizar um faturamento manual que resulte em múltiplos serviços com indicadores de operação diferentes em uma mesma nota, o sistema impedirá o processo. Para evitar esse erro, utilize as regras de agrupamento ou verifique se os serviços do contrato possuem o mesmo "**Código indicador da operação de fornecimento"** no cadastro.

[GIF animado: Imagem 5: Impedimento por Indicadores Distintos: se você tentar realizar um faturamento manual que resulte em múltiplos serviços…](https://ajuda.sankhya.com.br/hc/article_attachments/1500014489881)

O botão **"Mostrar no Portal"** disponível na aba Faturas Geradas, irá direcioná-lo ao [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) com as notas contidas nessa aba para que consultas detalhadas ou ajustes necessários possam ser realizados.

Para que o sistema permita a confirmação automática  do lançamento sem exigir a informação sobre o local ao clicar no botão faturar, o parâmetro **"Valida local serviço no faturamento de contratos? - VALLOCFATCONT"** deverá estar desabilitado. Desta mesma forma, o campo **"Atualização do Estoque"** deverá estar com a opção **"Nenhuma"** selecionada (tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)).

**Nota:** para este caso, tem-se o faturamento de contratos considerando a prestação de serviços. Desta forma, não haverá o controle de estoque e, portanto, não será necessário considerar a marcação **"Usa Local"** no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abaestoque).

**Observação:** o parâmetro **"Habilitar preço por faixa** **-** **BILFAIXA"** se habilitado, o sistema usará o preço configurado no [Cadastro do Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774). Na falta de configurações do contrato, o sistema emitirá a mensagem: **"Valor da nota não pode ser zero para gerar financeiro."**. Se o parâmetro estiver desabilitado será possível faturar o contrato.

![Imagem 6: Observação: o parâmetro "Habilitar preço por faixa - BILFAIXA" se habilitado, o sistema usará o preço configurado no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500014115282)

Ao clicar na seta localizada ao lado do botão **"Faturar"**, o sistema exibirá as opções para refazer provisões.

A opção **"Refazer Futuras Provisões sem Faturar"**, quando utilizada excluirá as provisões futuras e irá gerá-las novamente. Esta opção não considera a data de referência do faturamento, ou seja, se estiver, por exemplo, refazendo os financeiros do mês 12/2010 até 05/2011 o mês 12/2010 não será considerado.

Através da opção **"Refazer Futuras Provisões sem Faturar (Considerando Mês de Referência)"**, exclui-se e gera-se as provisões de todos os meses, inclusive do mês de referência. Esse mês de referência é definido no campo de filtro da tela chamado "Mês para referência".

**Observação:** as provisões originadas a partir do Faturamento de Contratos são registradas com a mesma TOP indicada no campo **"Tipo de Operação"** dos [Parâmetros Obrigatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#paineldeparmetrosobrigatrios) da tela. Portanto, ao contrário do que ocorre na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), não existe uma restrição que limite os registros apenas ao tipo de movimento **"I-Financeiro"**, seja nas opções de geração automática disponíveis nesta tela quanto na aba de [Provisões Financeiras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprovisesfinanceiras) da tela de [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774).

**Nota:** caso o parâmetro **"Vincular provisões de contrato às ocorrências - VINPROCONOCO"** esteja ligado, a composição dos valores provisionados por referência levará em consideração as ocorrências de cancelamento, bonificação, suspensão e expiração do contrato.

Para maiores detalhes sobre o lançamento de provisões, consulte [Gerando Provisões de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/32724709688983-Gerando-Provis%C3%B5es-de-Contratos).

**Observação:** para geração das opções apresentadas acima, o sistema levará em consideração uma conta Exclusiva da empresa, a referida marcação é realizada na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros). Tendo mais de uma conta configurada, o sistema não segue um padrão para seleção, não havendo uma conta configurada o sistema informará 0 (zero) no código do banco.

**Nota:** ao faturar um contrato não ocorrerá a atualização do Compromisso, mesmo que este esteja com a TOP configurada para gerá-lo (aba [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abatop), tela [Configuração da Estrutura de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos)). Pois tal atualização ocorre somente quando a origem é do financeiro, e o faturamento de contrato possui origem do estoque.

**Importante:** para evitar que a empresa tenha que cadastrar contratos separados ou lançar pedidos para cada configuração de CNAE encontrada nos serviços, o sistema trata o faturamento de contratos e o faturamento de pedidos com serviços para a geração de NFSe, na situação em que existir serviços com configurações de CNAE, tipo de serviço e código de tributação diferentes, gerando notas diferentes com seus respectivos itens, baseadas em cada configuração encontrada. Desta forma, acompanhe o exemplo:

Ao realizar o faturamento de dois contratos de prestação de serviço, onde um contém três serviços e outro dois serviços. Dentre estes serviços dois possuem os dados semelhantes entre si e os outros não, consequentemente o sistema gerará 4 notas.

**Nota:** ao realizar o faturamento de contratos que tenham periodicidade não mensal, através do parâmetro **"Faturar contratos não mensais com meses futuros? - FATCONTRMESFUT"** pode-se optar por considerar os meses futuros para compor o período ou não, logicamente, ativando ou desativando o referido parâmetro.

**Observação:** para realizar o faturamento de contratos que contenham apenas a provisão do mês vigente do faturamento configurada no [Cadastro do Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) em sua aba **"Provisões Financeiras"**, o parâmetro **"Informar Qtd Provisão qdo no último mês? - CONTPROV"** necessita estar desabilitado. Caso o referido parâmetro esteja ligado o faturamento não será finalizado e será exibida a seguinte mensagem:

**"Para o contrato X deverá ser informada a quantidade de provisões a serem geradas."**

**Importante:** no Faturamento de Contratos, a cidade a ser utilizada no cálculo do ISS, bem como a cidade do contrato, podem ser definidas com base no parâmetro **"Utiliza CNAE para definir cidade do contrato? - UTILCNAECIDCONT"** que ao ser ativado, o sistema considera as configurações realizadas nas [Preferências de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [CNAE Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abacnaeempresa), campos Local tributação (ISS Retido) e Local tributação (ISS normal) para busca de tais cidades, ou seja, uma vez o parâmetro habilitado e de acordo com as definições realizadas nos campos citados, tem-se as seguintes possibilidades:

- **Cidade de Prestação** - será utilizada a cidade inserida na tela Contratos, aba Impostos;
- **Cidade do Prestador** - nesta situação, será empregada a cidade vinculada ao [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas), aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas#abaendereo);
- **Cidade do Tomador** - por esta opção, será utilizada a cidade incluída no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaendereo).

Para este comportamento, é essencial que o [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o) que está sendo utilizado no contrato possua em seu cadastro o CNAE informado (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos)).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Configurações para o Faturamento de Contratos

As Configurações para o Faturamento de Contratos são definidas através do botão **"Configurações"** localizado no lado superior direito da tela. Ao clicar neste botão tem-se a exibição da seguinte tela:

![Imagem 7: As Configurações para o Faturamento de Contratos são definidas através do botão "Configurações" localizado no lado…](https://ajuda.sankhya.com.br/hc/article_attachments/4404191510167)

Com as seguintes opções:

**Exibir 'Parcela Faturamento':** Se marcada esta opção, o sistema irá informar automaticamente no campo **"Nro Nota"** na aba **"Provisões Financeiras"** do Cadastro de Contratos, o número da fatura referente à nota gerada pelo faturamento do contrato.

**Observação:** para isso, o parâmetro **"Exibir parcelas no faturamento de contratos?** **-** **EXIBPARCFATCON"** deve estar ligado.

**Usar Tipo de Negociação do Contrato:** Esta marcação necessita estar desmarcada caso se deseje usar o tipo de negociação desta tela.

**Calcular ISS/IRF pelo Contrato:** Ao acionar esta marcação, o sistema calculará os impostos ISS e IRF de acordo com as configurações presentes no cadastro do contrato na aba **"Impostos"**, ao invés de utilizar as configurações da TOP.

**Nota:**o parâmetro **"Buscar retenção de ISS pelo contrato? - ISSRETCONTRATO"** quando ativado, faz a retenção de ISS sempre de acordo com a definição indicada no campo **"Retém ISS"** do contrato e nunca de acordo com a configuração indicada no Cadastro do Parceiro.

**Na Central:** Quando o parâmetro de chave ISSRETCONTRATO estiver ligado e o parceiro de um documento for alterado, caso a nota possua um contrato vinculado, o ISS será retido ou não de acordo com o campo RETEM ISS do cadastro do contrato. Caso esteja desligado, funciona verificando o campo RETEM ISS do cadastro do parceiro.

**Calcular Impostos Mensais:** Se marcada, esta opção irá ativar o cálculo dos impostos mensais na notas geradas pelo processo de faturamento.

**Importante:** o cálculo ocorrerá somente se o valor do faturamento for maior ou igual ao valor mínimo da base mensal dos outros impostos.

**Gerar taxa conforme Conta Bancária:** Se acionada esta opção, você não utilizará a taxa da conta informada no cadastro do parceiro.

- Caso esteja marcada, o parâmetro **"Taxa de boleta no total da nota -** **TAXBOLNOT"** estiver ligado e o valor da nota for inferior ao valor mínimo da conta, o campo VLRJURO do FINANCEIRO da nota resultante do faturamento ficará com o valor da taxa informada no cadastro da conta bancária.
- Se estiver marcada, o parâmetro de chave TAXBOLNOT estiver desligado e o valor da nota for inferior ao valor mínimo da conta, o campo VLRJURO do FINANCEIRO da nota resultante do faturamento ficará com o valor da taxa informada no cadastro da conta bancária.

**Observação:** o Tipo de Juro depende do parâmetro **"Taxa de boleta com tipo INCLUSO -** **TAXBOLNOTTJ"**. Fato este, se estiver ligado, o valor do juro será somado ao valor do Desdobramento.

**Gerar Financeiro pelo tipo de negociação usando Vencto da tela + (mais) Prazo das parcelas:** Se habilitada, o sistema usará as informações do tipo de negociação, mas se não estiver, o parâmetro **"Contrato para software? -** **CONTSOFT"** estiver ligado e no contrato tiver tipo de negociação informado, então usará as informações do tipo de negociação.

![Imagem 8: Para saber mais detalhes sobre como estas parametrizações influenciam no vencimento das notas geradas a partir da…](https://ajuda.sankhya.com.br/hc/article_attachments/25938799470359) Para saber mais detalhes sobre como estas parametrizações influenciam no vencimento das notas geradas a partir da rotina de faturamento, consulte o artigo: [Cálculo do Vencimento das Notas geradas a partir do Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos).

**Gerar Rateio por Critério para a Nota:** Quando habilitada, o critério de rateio informado no cadastro de contrato é copiado para a nota destino que será gerada pelo processo de faturamento.

**Faturamento baseado em Instalação (Pró-Rata por Veículo):** Tem a função de faturar o serviço de acordo com a instalação do dispositivo no carro, esta informação deverá estar que está informada na aba Veículos do cadastro de contratos. Assim, teremos o exemplo:

Foi configurado como padrão que todo mês teria 30 dias, então se um carro teve o dispositivo instalado no dia 15 ao faturar este serviço no mês referente a instalação o valor será proporcional aos dias utilizados.

**Nota:** esta opção só será exibida quando o parâmetro **"Importar Serviços de Pedidos do Parceiro? -** **IMPSERVPED"** estiver ligado e o parâmetro **"Usar Bilhetagem p/ qtd prevista igual a zero -** **BILPREVZERO"** desligado.

Quando essa opção estiver marcada, o contrato só ficará disponível na grade quando o cálculo do valor do pró rata para esse item for maior que zero.

**Usar Série maiúscula:** Marcando-se esta opção, o sistema alterará a série que foi informada no faturamento com letra minúscula, para letra maiúscula, possibilitando assim a geração da fatura em casos de conflito entre a configuração da TOP e o faturamento. Vejamos um exemplo:

Na Central de Faturamento de Contratos são validadas as configurações do Controle de Numeração da TOP, utilizada no Faturamento.

Se na Central a série for informada com letra minúscula e na configuração do Controle de Numeração da TOP tiver sido informada com letra maiúscula, o sistema não permitirá a geração da Fatura.

Marcando esta opção, o sistema altera a série informada de minúscula para maiúscula, possibilitando assim a geração da fatura.

**Copiar observação dos itens do contrato:** Quando marcada esta opção, tem-se a cópia da observação digitada no campo **"Local de instalação"** do Cadastro de Contratos, para o campo **"Observação"** nos itens de Produto/Serviço da nota gerada através do faturamento.

Se no [Cadastro do Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos) houver alguma informação de **"Observação Padrão"**, ao acessar a tela de Faturamento de Contratos e utilizar a opção **"Usar observação padrão do contrato"** disponível nesse botão, ao faturar, a nota será gerada com a Observação do Contrato.

Caso haja a informação do Tipo de Título no Cadastro do Contrato e na tela Faturamento de Contratos utilize a opção **"Usar tipo de título do contrato"**, ao faturar, a nota será gerada com o Tipo de Título do Contrato independente das demais configurações que impactem no tipo de negociação utilizado.

Através da marcação **"Gerar provisões a partir do vencimento da nota faturada"** você define se será calculado o vencimento das provisões a partir do vencimento real da nota faturada ou não.

**Observação:** caso a marcação acima esteja selecionada e a marcação **"Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das Parcelas"** também esteja realizada, o sistema fará a conta dos vencimentos das provisões considerando a data para vencimento da primeira provisão.

Sendo assim, ao faturar o contrato, quando a marcação Gerar provisões a partir do vencimento da nota faturada estiver realizada, será utilizada a data fixa também para as provisões subsequentes ao faturamento do contrato, independente da data do faturamento deste e do tipo de negociação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Faturamento de Contratos com Pagamento de Comissões

No faturamento do contrato, caso ele não seja um contrato de locação e possua comissões, estas serão incluídas na nota gerada. Nesse caso, a TOP utilizada para faturamento deve estar configurada para calcular comissões. Serão geradas comissões, se o vendedor ainda não tiver atingido o número máximo de parcelas de comissão que tem direito e ainda estiver dentro do prazo definido.

Será validado o percentual máximo de comissão, caso ultrapasse o valor definido no parâmetro **"% Máximo de Comissão em CM** **-** **COMMAXCM"**, ele será barrado.

#### Marcação Nunca Incluir Confirmada

Na aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes) do cadastro do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), a marcação **"Nunca incluir confirmada"** influencia no faturamento de contratos da seguinte maneira:

- Quando acionada, os faturamentos não irão gerar notas confirmadas.
- Se desmarcada, serão geradas notas confirmadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Histórico do Faturamento de Contratos

Ao faturar um contrato, a informação de referência que é aplicada ao campo **"Observação** **da Nota"** também será aplicada ao campo **"Histórico"** das Movimentações Financeiras, evitando assim, que você tenha que localizar a Nota para visualizar a Observação, ou seja, a Refe**rência** do Contrato.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Renegociação de Títulos e envio de E-mail's Automáticos

Ainda na tela de Faturamento de Contratos, é possível realizar a configuração para que a partir do faturamento de contratos, sejam geradas as NFS-e's com possibilidade de gerar uma nota para cada serviço com CNAE's diferentes, aprovar estas notas, gerar a renegociação e encaminhar o boleto por e-mail.

Para que isso ocorra, são necessárias algumas configurações, são elas:

- O parâmetro **"Reneg. de títulos automática no fat. de contrato? - RENEGNOTAAUTO"** deve estar ativado;
- As configurações para emissão de NFS-e devem estar previamente efetuadas;
- A TOP utilizada para o faturamento dos contratos, deve ser do Tipo de Movimento "Venda" e atualizar o financeiro (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral));
- As configurações para geração de Boleto também devem estar realizadas, conta bancária, modelos de impressão tanto de notas, quantidade de boletos (tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas));
- O [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) deverá ter um e-mail configurado (aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaendereo)), como também os contatos devem estar com as marcações de poder receber o boleto e nota por e-mail (aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontatos)).

Depois de realizadas as devidas configurações, ao realizar o faturamento de um contratos, caso as notas não tenham sido aprovadas, na tela de aviso, será exibida a seguinte mensagem:

**"Não foi possível renegociar os financeiros pois existem NFS-e não aprovadas. Favor verificar as notas com status diferente 'Aprovada'."**

Caso as notas sejam aprovadas, será apresentado o aviso que a renegociação foi gerada, os RPS's que foram aprovados, uma linha informando que a renegociação foi gerada e a quantidade de e-mail's enviados. Além disso, no Portal de Vendas, poderão ser visualizadas as notas geradas.

Na tela de [Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393), pode-se visualizar que o vencimento dos títulos, será o que for definido conforme seus títulos de origem (Vencimento Original) e a Data de Negociação será a Data de Faturamento informada no Faturamento de Contratos; a taxa de juros e multas seguirão em conformidade com os títulos de origem; o sistema não transfere o rateio do título de origem para o título gerado na renegociação e não valida se os títulos possuem contatos diferentes.

Se o contrato for do tipo de Pagamento Vencido, a data de negociação será a mesma da data de vencimento dos Títulos. Isso não vale se marcar-se a opção **"Agrupar Contratos"** nos parâmetros obrigatórios na tela de Faturamento de Contratos.

Quando o parâmetro **"Usa contrato do grupo como base faturamento? - CONTGRUPBASEFAT"**, estiver ligado a realização do faturamento será baseada no agrupamento de contratos, portanto, será respeitada a data de vencimento de cada contrato, assim como ocorre com o campo Parceiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Geração do Boleto e envio por E-mail

Para que o e-mail seja enviado corretamente, é necessário que as seguintes configurações sejam realizadas no [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros):

- Na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaendereo), configura-se o e-mail do parceiro;
- Tem-se na [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abainformaes), o campo **"Tipo geração boleto"** que deverá estar configurado com a opção **"Enviar e-mail"**,
- Se o envio for realizado para os contatos, é necessário que os mesmos tenham informado um e-mail e as opções **"Receber boletos por e-mail"** **e** **"Receber nota por e-mail"** localizadas na aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontatos), estejam marcadas.

Além destas marcações, a conta bancária e o Banco que serão utilizados para efetuar a geração do boleto serão:

- No Cadastro do Parceiro, aba [Identificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), utiliza-se as informações contidas no campo **"Conta Bancária Empresa"**;
- Caso a opção anterior não tenha sido satisfeita, será realizada uma busca das contas da empresa do contrato e que são exclusivas desta empresa.

**Observação:** em todas as situações na conta bancária, o campo **"Emite boleto"** localizado na aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), deve estar marcado.

O financeiro renegociado que é gerado, busca a conta padrão configurada no parâmetro **"Conta padrão para financeiro - CONTAPADRAOFIN"**, caso não seja configurada uma conta padrão será utilizada à mesma conta do financeiro original que é gerado pelo faturamento.

Se as condições acima não foram sanadas, não será efetuada a geração do boleto e nem o envio deste por e-mail; com isso, o Banco e a Conta Bancária serão inseridos com o valor zero e vazio, respectivamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Renegociação com Agrupamento de Contratos

Para este processo é necessário selecionar vários contratos do mesmo parceiro e marcar a opção **"Agrupar Contratos"**. Feito isso, clicando-se no botão **"Faturar"**, será apresentada a seguinte mensagem:

"Foram geradas X faturas."

#### Importante:

- A prefeitura de Goiânia não possui ambiente de homologação e por isso foram feitos os testes de aprovação de NFS'e para a prefeitura de Belo Horizonte, que possui o ambiente de homologação;
- No faturamento dos contratos, não são gerados pedidos, apenas notas;
- Caso as configurações de boleto, não estejam corretas, ou a nota não tenha sido aprovada, o sistema não irá renegociar e nem enviar boleto. Neste caso, as configurações, terão que ser revistas manualmente.
- No Faturamento de Contratos, na tela destinada aos avisos, será apresentado um parecer do ambiente e caso não apareça nenhum erro referente à geração de boleto, e este não foi enviado, significa que as configurações de envio de boleto, deverão ser revistas;
- Se ao realizar o faturamento de contratos e gerar-se somente uma nota, não havendo a geração de uma nota para cada serviço com CNAE's diferentes, o sistema não irá efetuar a renegociação e enviará o boleto, apenas se este estiver configurado corretamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Faturamento por Perfil de Consumo

Empresas prestadoras de serviço de Planos de Saúde ou Seguradoras, por exemplo, possuem um contrato fixo mensal com o Parceiro e vários outros com os Associados deste parceiro. Desta forma, tem-se o seguinte exemplo:

Mensalidade: 100,00

Funcionários: José Plano A = 20,00 e João Plano B = 15,00

Dependentes do João:

Maria – Plano B 15,00 e Joaquim – Plano C 10,00

Possíveis análises:

1.Quais os serviços faturados e recebidos por Parceiro?

2.Quanto foi recebido por Plano de Saúde para a análise de rentabilidade?

Para esta análise o sistema reúne de forma automática os seguintes cadastros, bastando para isso fazer as prévias configurações:

1) Tabelas de Preço, onde são descriminados os Preços dos Planos de Saúde;

2) Cadastro de Perfil de Parceiro que deverá conter todos os Planos de Saúde como forma de agrupar parceiros por Perfil;

3) Cadastro de Parceiros e Contatos do Parceiro (funcionários e dependentes) classificados por Perfil de Consumo;

4) Cadastro do Contrato do Parceiro informando o serviço de mensalidade;

5) Relacionamento entre os Serviços X Naturezas.

O Faturamento é muito simples, bastando marcar a opção **"Considerar Contatos/Perfil/Serviços"** ([Painel de Filtros Personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#paineldefiltrospersonalizados)), o sistema gera todo o faturamento e análises necessárias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Rateio de Parcelas Financeiras

No faturamento de um contrato é possível efetuar o rateio das parcelas financeiras, geradas para diversas naturezas automaticamente. De acordo com a configuração da opção **"Gerar Rateio por Critério para a Nota", do botão** **"Configurações"** da tela de Faturamento de Contratos como explicado em tópico anterior deste help.

São duas as formas de rateio que podem ser utilizadas:

1.Caso seja associado um Critério de Rateio ao contrato, é gerado um rateio, origem Financeiro, baseado no percentual definido neste critério de rateio.

2.Se não houver nenhum Critério de Rateio associado ao contrato, ao faturar, será gerado rateio pela nota, para as naturezas cadastradas em Natureza x Serviço, com percentuais calculados pela proporção entre total de cada item em relação ao total da nota.

**Observação:** quando não há Critério de Rateio associado ao Contrato e todos os serviços deste contrato estão associados à mesma natureza, não será gerado rateio.

No Cadastro de Contrato, aba **"Propriedades"**, tem-se a marcação **"Considera dia do pagamento como dia útil"** que ao ser acionada faz com que o sistema considere apenas dias úteis para calcular o vencimento do faturamento do contrato. Vejamos um exemplo:

A data de faturamento é 01/03/2005, são 5 dias para pagamento incluindo o dia de faturamento. Com a opção desmarcada, o dia para pagamento é 05/03/2005. Se estiver marcada, o sistema altera o vencimento para 08/03/2005, desconsiderando sábado e domingo.

A provisão de recebimento de acordo com o contrato de manutenção, é efetuada através da configuração do parâmetro **"Qtd de meses p/provisionamento no faturamento do contrato -** **QTDMESPROVFATC"**. Informa-se no campo **"Inteiro"** deste parâmetro, a quantidade de meses para gerar provisões.

No faturamento de contratos, ao gerar as notas, o sistema apaga as provisões dos vários meses seguintes e gera cópia dos financeiros para os vários meses seguintes, conforme parâmetro acima. Baixa as provisões com data de vencimento menor ou igual ao último dia do mês de vencimento do financeiro gerado para o contrato.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Permitir o Faturamento de Contratos do Fornecedor

O parâmetro **"Tipo de faturamento de contratos - TIPFATCON"** permite faturar contratos de fornecedores gerando pedidos de compras ou notas de compras a confirmar ou já confirmadas (de acordo com a configuração da TOP) baseado em contratos de despesa.

Como padrão ele será apresentado sem valor, que faz com que não haja alterações na estrutura de como é realizado o faturamento atualmente.

Se o parâmetro estiver configurado como Despesa, fará com que apenas TOP’s de compras ou de pedidos de compra sejam apresentadas na pesquisa do Tipo de Operação da tela de Faturamento de Contratos.

Caso o parâmetro esteja configurado como Receita, fará com que apenas TOP’s de vendas ou de pedidos de venda sejam apresentadas na pesquisa.

Além disso, o parâmetro poderá ser configurado como Ambos, o que fará com que sejam apresentadas na pesquisa do Tipo de operação da tela de Faturamento de contratos Top’s de compras, pedidos de compras, vendas e pedidos de vendas.

Sendo assim, se o parâmetro estiver habilitado, o sistema filtrará os contratos que o tipo do financeiro for igual ao tipo do financeiro da TOP.

O financeiro do pedido ou da nota gerado a partir deste faturamento deverá ter a Receita/Despesa definida de acordo com a TOP.

Deste modo, o sistema baixará as provisões criadas para os contratos de despesas assim como já são realizados para as receitas. Caso seja consultado, será possível constatar que o financeiro foi baixado e que foi gerada uma provisão real.

**Nota:** quando a TOP é informada, o sistema não mostrará os contratos que estão vinculados a notas (essa nota usa a TOP informada que é do mesmo parceiro do contrato e é da empresa informada) que têm 'Dt. da Validade' = 'Mês para referencia', informado na tela Faturamento de Contratos ou a Dt. da Validade nula bem como a Dt. negociação da nota está dentro do mês informado no campo 'Data para faturamento' da tela Faturamento de Contratos.

**Importante:** em relação a rotina de Faturamento de Contratos, considerando uma TOP que não atualiza o financeiro (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), campo **"Financeiro"**, configurado com a opção **"Não atualizar"**), o parâmetro **"Ignorar marcação financeiro da top para faturar contrato - IGFINTOPFAT"** deverá estar desligado para que não seja gerado o financeiro dos contratos. Quando habilitado, mantém-se o comportamento padrão do sistema, ou seja, tem-se a geração do financeiro no rodapé da nota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Cálculo de IRF

No faturamento de um contrato, para que seja efetuado o cálculo do IRF, são necessários os seguintes cadastros:

1) No cadastro de contratos, aba Propriedades: no campo Natureza informar a natureza financeira do contrato;

2) Em Arquivos/ Cadastros/ Naturezas/ Natureza X Serviço: cadastrar o serviço relacionado com a natureza do contrato;

3) O parceiro, obrigatoriamente, deve ser pessoa jurídica;

4) No cadastro do parceiro, aba Fiscal, o campo **"Calcula IRF"** tem que estar marcado;

5) No cadastro do serviço, registrado no item 2, na aba Impostos, configurar para calcular IRRF e informar a alíquota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Dedução dos custos VA e VT na BC de INSS

De acordo com o artigo 124 da Instrução Normativa RFB n° 971 de 13 de novembro de 2009, poderá ser deduzido da Base de Cálculo do INSS os valores correspondentes às despesas de vale transporte e alimentação quando se tratar de prestação de serviço por contrato. Essa funcionalidade serve para quem emite notas fiscais a partir do Faturamento de Contratos.

Para que seja possível deduzir os custos de vale transporte e alimentação na Base de Cálculo do INSS, é necessário realizar as configurações abaixo:

Vincule um projeto às notas de despesas e ao contrato, sendo que esse projeto deve ser o mesmo tanto para as notas quanto para o contrato;

Preencha os parâmetros **"Natureza para reduzir Vale Alimentação no Vlr no INSS do contrato - NATVA"**, **"Natureza para reduzir Vale Transporte no Vlr no INSS do contrato - NATVT"** e **"TOPs para requisição de insumos de contratos - TOPSREQCON"**.

**Observações:**

- As notas de compras referentes ao vale alimentação e vale transporte devem ser lançadas utilizando as naturezas configuradas nos parâmetros NATVA e NATVT, respectivamente.
- A nota de compra referente aos insumos devem ser lançadas usando a TOP configurada no parâmetro TOPSREQCON;
- As notas de despesas/requisição que tiverem rateio, só serão consideradas caso o rateio seja feito por natureza ou projeto. Se for utilizado rateio por natureza, somente serão abatidos na Base de Cálculo do INSS o percentual que corresponde às naturezas configuradas nos parâmetros NATVA e NATVT; caso seja usado rateio por projeto dentro de uma NF lançada com as naturezas configuradas nos parâmetros mencionados, a proporcionalização será feita para cada contrato, de acordo com o percentual definido no rateio.

No lançamento do contrato deve ser vinculado o projeto criado para que ele seja ligado às despesas lançadas com o mesmo projeto.

Na TOP utilizada para o faturamento (pedido de venda) a marcação **"Tem VA e/ou VT no contrato"** (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)) deve estar realizada para que seja liberado no painel de filtros da tela Faturamento de Contratos os campos **"Mês p/ Referência do VT e dos Insumos"** e **"Mês p/ Referência do VA"** e os mesmos devem ser preenchidos com as datas das notas.

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16033493563287)**Importante:**

- Esses campos não serão utilizados no filtro para buscar os contratos. Se a marcação da TOP estiver realizada, esses valores serão utilizados para preencher os campos de referência da nota que será gerada.
- Se a marcação estiver feita e os filtros não forem informados, os campos do cabeçalho da nota receberão o valor do campo **"Mês para Referência"**.

Para calcular o INSS, no [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos), configure os campos abaixo:

**Calcular FUNRURAL:** Efetue essa marcação se incidir INSS sobre o serviço quando este for de terceiros.

**% Funrural:** Informe o percentual de incidência de INSS sobre o serviço.

**% Red. Base Funrural:** Preencha o percentual de redução na base do INSS se houver redução.

---

**![informações](https://ajuda.sankhya.com.br/hc/article_attachments/16033493560983) Informações adicionais**

- Na rotina de Faturamento de Contratos, após a nota ser faturada na Central de Vendas, o campo **"Base de INSS"** da aba Impostos será calculado considerando o valor da nota deduzido dos valores totais de vale alimentação, vale transporte e insumos que tenham sido lançadas na mesma referência do faturamento do contrato e que atendam as configurações dos parâmetros TOPSREQCON, NATVA e NATVT e que tenham ligação com o contrato.
- O sistema não diferencia os títulos por empresa, portanto, os títulos de despesas de vale alimentação e vale transporte não necessariamente serão da mesma empresa do contrato faturado. Serão buscados os títulos pela data de negociação a partir da data de referência informada Mês p/ Referência do VT e dos Insumos e Mês p/ Referência do VA da tela Faturamento de Contratos, mesmo que os mesmos não tenham sido baixados.
- Para que os custos de VA, VT e Insumos sejam deduzidos da Base de Cálculo do INSS, todos os cadastros que estiverem envolvidos no processo de faturamento de contratos devem estar devidamente configurados para Calcular INSS (TOP, Empresa, Parceiro, Serviço, etc).

---

Os parâmetros abaixo impactam o cálculo do INSS com base deduzida dos custos de vale alimentação e vale transporte:

- **Valor Líquido p/Retenção de INSS - VLRCALCINSS:** Nesse parâmetro deve ser configurado o valor mínimo para que seja feita a retenção do INSS.
- **TOP's p/ requisição de insumos para reter INSS - TOPSREQCON:** Configure aqui a TOP utilizada para o lançamento das requisições de insumos de contratos para que o custo seja deduzido da Base de Cálculo do INSS.
- **Natureza da desp. p/reduzir VT no valor do INSS do contrato - NATVT:** Informe nesse parâmetro a natureza utilizada para o lançamento da nota fiscal de despesa de vale transporte que será deduzido da Base de Cálculo do INSS no Faturamento de Contratos.
- **Natureza da desp. p/reduzir VA no valor do INSS do contrato - NATVA:** Nesse parâmetro, preencha a natureza usada para o lançamento da nota fiscal de despesa de vale alimentação que será deduzido da Base de Cálculo do INSS no Faturamento de Contratos.
- **Considerar impostos retidos no valor da nota? - CONSIMPRETNOTA:** Quando esse parâmetro estiver ligado, será feita a retenção dos impostos ISS, IRRF e INSS/Funrural na Central de Atendimento.
- **Gerar impostos (ISS,INSS,IRF) no financeiro? - GERIMPOSTO:** Com este parâmetro ligado, o financeiro gerado receberá os valores de IRF, INSS e ISS da nota conforme as configurações envolvidas acima.
- **Soma ISS,INSS,IRF ao financeiro do faturamento de contrato -** **SOMIMPRETVLRFIN:** Quando esse parâmetro estiver ligado os valores serão somados ao Desdobramento**.**

**Importante:** o parâmetro CONSIMPRETNOTA não pode ser utilizado em conjunto com o parâmetro GERIMPOSTO, e a nota de venda proveniente do faturamento de contratos não deverá possuir configuração de outros impostos que subtraiam a partir do total da nota, caso contrário, ocorrerá a retenção dos impostos em duplicidade. Se os impostos estiverem configurados para não reterem na nota, mesmo que o parâmetro esteja ligado, a retenção não irá ocorrer.

---

Quando o parâmetro **"Proporcionalizar Custos VA, VT e Insumos - PROPCUSTVAVTIN"** estiver ligado, ao ser faturado um pedido de forma proporcional (valor menor que o total), além do valor da nota ser gerado de acordo com a quantidade faturada, os custos de vale transporte, vale alimentação e insumos deduzidos da BC de INSS também irão obedecer a quantidade faturada e deduzir de forma proporcional por nota.

O cálculo do índice é:

```
 Índice = VlrTotalItensNota / VlrTotalItensPedido
```

E o cálculo da proporcionalização dos custos de VA, VT e Insumos:

```
 NovoVlrDeducao = (totalInsumos + totalValeTransporte + totalValeAlimentacao) x Índice
```

Por exemplo:

**Pedido de Venda:** R$1.000,00
**Total Custo VA, VT e Insumos:** R$100,00
**Nota 1:** R$333,33 (33,33% do total de R$1.000,00)
**Proporção VA, VT e Insumos para a Nota 1:** 33,33% de R$100,00 = R$33,33 (esse valor será reparticionado para todos os itens da nota).
**Base de Cálculo do INSS da Nota 1:** R$333,33 - 33,33 = R$300,00

**Nota:** a proporcionalização será feita pelo índice, desprezando o arredondamento.

**Observação:** além do parâmetro acima, os parâmetros NATVA, NATVT, **"Usar quantidade do contrato na nota? - USAQTDECONNF"** e **"Tipo de faturamento de contratos - TIPFATCON"** também devem estar configurados para ser realizada a proporcionalização na dedução dos valores de VA, VT e Insumos na BC do INSS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

## Alerta de contratos a reajustar

O botão ![Imagem 11: O botão será apresentado somente quando o parâmetro de chave "Notificar pendências de reajuste de contratos -…](https://ajuda.sankhya.com.br/hc/article_attachments/15450714079895) será apresentado somente quando o parâmetro de chave **"Notificar pendências de reajuste de contratos - NOTPENREACON"** estiver habilitado e, será exibido sempre que, ao abrir a tela em HTML5, for identificado que existem contratos ativos pendentes de reajuste.

Clicando nesse botão, será aberto o pop-up **"Contratos Pendentes de Reajuste"**:

[GIF animado: Imagem 12: Clicando nesse botão, será aberto o pop-up "Contratos Pendentes de Reajuste" :](https://ajuda.sankhya.com.br/hc/article_attachments/8029137901079)

Clicando no botão **"Ir para Reajuste"**, você será redirecionado para a tela [Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos) contextualizando apenas os contratos exibidos no pop-up.

[GIF animado: Imagem 13: Clicando no botão "Ir para Reajuste" , você será redirecionado para a tela Reajuste de Contratos Ativos…](https://ajuda.sankhya.com.br/hc/article_attachments/15450714088727)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/25938841742359) Acesse também:

[Cálculo do vencimento das notas geradas a partir do Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos)

[Gerando Provisões de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/32724709688983-Gerando-Provis%C3%B5es-de-Contratos)
