---
id: "360045106673"
titulo: "Análise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-09T19:03:15Z"
rotulos: ["Produtos", "Pedidos", "manual", "Configuração", "Relatórios", "análise de giro", "Estoque Mínimo", "Análise de Giro", "CONTACESSCONSOL", "DEDUZIRRESESTAN", "Estocagem", "Fornecedores", "Frequencia", "LIMCURVA_BPRO", "LIMCURVA_CPRO", "Matriz de Análise de Giro", "Períodos", "Sugestão de Compra", "Técnica ABC", "br.com.sankhya.com.rotinas.analisegiro", "Análise de Giro manual", "Agendamento", "TOP", "Vendas", "Estoque", "Gestão de Estoque", "Compras Estratégicas"]
---

# Análise de Giro

```
  Módulo: Comercial > Rotinas
```

---

**ATENÇÃO:** A Análise de Giro não está preparada para a movimentação do processo produtivo.

O Processo de Compra é uma peça fundamental na atividade de praticamente todas as empresas dos diversos seguimentos, sobretudo da indústria e do comércio (atacadista ou varejista). Determinar o que, quanto, quando e de quem comprar, negociando o melhor preço/prazo possível é uma tarefa complexa e exaustiva que normalmente é feita por profissionais experientes. Esses profissionais acabam desenvolvendo uma "intuição" para responder a todas essas perguntas, nem sempre de forma correta, o que pode conduzir a compras equivocadas provocando problemas como: excesso de estocagem, diminuição dos lucros, falta de produtos/insumos e até inviabilizando as atividades da empresa.

Com o intuito de diminuir a dependência dessa intuição dos profissionais de compra, a Análise de Giro extrai informações do ERP, possibilitando uma visão acurada e realista sobre o fluxo das mercadorias dentro da empresa, expondo situações antes desconhecidas pela gestão de compras. Além disso, essa ferramenta torna-se aliada ao processo de compra em si, compondo um esboço do pedido de compra que será finalizado na Central de Compras.

Assim, com uma maior assertividade no momento da compra, a empresa se torna mais eficaz e lucrativa de forma geral.

É importante destacar que Giro é um conceito diretamente associado à Vendas. Neste sentido, todas as operações que representam giro efetivo de estoque devem ser assinaladas com a opção **"Saídas"**, como as Vendas e as Bonificações. Já as Entradas são apenas as operações de **"estorno de saídas"** que devem ser abatidas das movimentações de vendas para se chegar ao giro final, como as Devoluções de Vendas, por exemplo. Portanto, nas Compras e em outras movimentações de entrada não deve ser escolhida a opção **"Entrada"**, sob a consequência de distorcer toda a análise de giro e subavaliar suas necessidades de reposição.

**Importante:** a premissa básica para que um produto seja apresentado na Matriz de Análise de Giro, é que o mesmo se encontre Ativo.

Acesse os links abaixo para facilitar sua navegação nas funcionalidades desta tela:

| Funcionalidades da tela |
| --- |
| [Considerações para Geração da Tabela de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#considera%C3%A7%C3%B5esparagera%C3%A7%C3%A3odatabeladegiro) |
| [Sincronização entre os Processos da Matriz e do Job de Consolidação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#sincroniza%C3%A7%C3%A3oentreosprocessosdamatrizedojobdeconsolida%C3%A7%C3%A3o) |
| [Técnica ABC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#t%C3%A9cnicaabc) |
| [Como funciona o estoque mínimo e máximo dos produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#Comofuncionaoestoquem%C3%ADnimoem%C3%A1ximodosprodutos) |
| [Parâmetros importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#par%C3%A2metrosimportantes) |
| [Campos para Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro) |
| [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554) |

---

![Imagem 1: Botões do topo da tela](https://ajuda.sankhya.com.br/hc/article_attachments/4404197241239)

### Considerações para Geração da Tabela de Giro

Para que a nota seja considerada na geração da tabela de giro, ela passará pelas seguintes validações:

![Imagem 2: O Status da Nota deve ser " Confirmada" e o Valor da Nota deve ser maior que 0 (zero).](https://ajuda.sankhya.com.br/hc/article_attachments/23562502280471) O Status da Nota deve ser **"Confirmada"** e o Valor da Nota deve ser maior que 0 (zero).

![Imagem 3: O Tipo de Operação - TOP utilizado na nota deve ter o campo " Análise de Giro" (localizado na aba Geral ) configurado…](https://ajuda.sankhya.com.br/hc/article_attachments/23562518954007) O [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado na nota deve ter o campo **"Análise de Giro"** (localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)) configurado com a opção como **"Devolução de Venda (Entrada)"** ou **"Venda (Saída)"**. Se for selecionada a opção **"Desconsiderar"**, as notas com essa TOP serão desconsideradas.

![Imagem 4: Quanto aos itens da nota, devem ter " Valor Unitário" e "Quantidade maior que 0" (zero), e o produto deve ter o campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/25993907170327) Quanto aos itens da nota, devem ter **"Valor Unitário"** e **"Quantidade maior que 0"** (zero), e o produto deve ter o campo **"Calcular giro pelo agendador"** (aba Medidas e Estoque, sub-aba Estoque) marcado.

**![Imagem 5: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/23562648691735) Informações adicionais**

- Para que as informações inseridas nas colunas **"Parceiro"** e **"Nome Parceiro"** sejam exibidas na Análise de Giro, os referidos campos deverão ser adicionados na grade **"Campos Significativos"**, aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abapropriedades) da tela [Configuração da Estrutura de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794).
- Os dados da empresa serão apresentados na matriz, se na tela [Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line), botão [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line), aba [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abamargemdecontribuio), seção **"Configurações por Empresa"**, for informada a empresa que será utilizada na Análise de Giro. Preencha também os dados nas seções **"% de custo variável a ser calculado sobre o faturamento"** e **"% de custo fixo"**.
- Para que o produto seja exibido na consolidação dos dados, é necessário que o mesmo contenha custos. Sendo assim, possuindo uma linha na TGFCUS, o produto será apresentado no resumo das informações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#top)

### Técnica ABC

Uma análise ABC consiste da separação dos itens de estoque em três grupos de acordo com o valor de demanda anual, se tratando de produtos acabados ou valor de consumo anual quando se tratar de produtos em processo ou matérias-primas e insumos.

O valor de consumo anual ou valor de demanda anual é determinado multiplicando-se o preço ou custo unitário de cada item pelo seu consumo ou sua demanda anual.

Assim, como resultado de uma típica classificação ABC, surgirão grupos divididos em três classes, como segue:

(1)** Classe A:** itens que possuem alto valor de demanda ou consumo anual.

(1)** Classe B:** itens que possuem um valor de demanda ou consumo anual intermediário.

(1)** Classe C:** itens que possuem um valor de demanda ou consumo anual baixo.

A construção da curva ABC prevê o trabalho com um conjunto determinado de produto ou qualquer conjunto de entidades tais como clientes, fornecedores, entre outras, sempre considerando quantidades e valores e seu produto dentro de um determinado período. Assim, observe o exemplo:

Pode-se efetuar uma classificação por participação em vendas considerando quantidades vendidas e preços de venda de todos os itens em janeiro de 2015. Para tanto, é necessário calcular os produtos de quantidade x preço para cada item individualmente, calculando também a somatória total deste produto.

Posteriormente, é necessário calcular a participação do total de cada item em relação ao total geral, em percentual, ordenando de forma decrescente. É necessário calcular os percentuais acumulados item a item, de tal forma a efetuar a separação dos produtos em classes conforme parâmetros pré-determinados.

Além dos parâmetros **"Limite em % para Curva B - LIMCURVA\_BPRO"** e **"Limite em % para Curva C - LIMCURVA\_CPRO"**, é possível obter os percentuais de outra forma, conforme o detalhamento definido para a curva. Para isso, acesse a ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15471507742103) [Configuração da Matriz de Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro), aba [Outras configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#outrasconfigura%C3%A7%C3%B5es), campo **"Detalhar de acordo com"**. Nele, são apresentadas quatro opções de escolha, sendo elas:

- Produto;
- Grupo de produto;
- Marca;
- Empresa.

Ao definir este campo com as opções **"Produto"**, **"Marca"** ou **"Empresa"**, serão respeitados para formação da curva ABC, os percentuais informados nos parâmetros. Se for selecionada a opção **"Grupo de produto"**, serão utilizados os percentuais informados na tela [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), aba [Curva ABC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abacurvaabc).

As Curvas ABC podem ser construídas com base em diferentes critérios, tais como **"quantidades vendidas"** dos produtos, **"peso bruto"** dos produtos, **"valor vendido"** dos produtos ou **"margem de contribuição"** dos itens. Todas essas possibilidades, dentro de um período pré-definido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#top)

### Sincronização entre os Processos da Matriz e do Job de Consolidação

Sendo:

#### Ao rodar uma matriz:

- Caso esteja sendo executado um Job sem filtros (não possuía linhas na TGFGIR1 antes de iniciar), é lançado um erro informando que o job está sendo executado e não será possível processar a matriz no momento.
- Se estiver sendo executado um Job com filtros, o processamento da matriz irá aguardar o término do job para então iniciar.
- Caso esteja sendo executada uma limpeza de consolidação, uma mensagem é lançada informando que não é possível processar a matriz pois a limpeza está em andamento e depois não haverá dados para o processamento dela.

#### Ao rodar uma limpeza de consolidação:

- Caso existam processamentos de matrizes rodando, será exibida uma mensagem informando que não é possível executar a limpeza no momento, pois a consolidação está sendo usada para gerar matrizes.
- Se o agendador de consolidação do giro, seja com filtro ou sem filtro, estiver sendo executado, será apresentada uma mensagem informando que não é possível executar a limpeza no momento, pois a consolidação está sendo gerada.

#### Ao iniciar o Job da consolidação do giro com ou sem filtros:

- Caso esteja sendo rodada uma limpeza, será exibida uma mensagem no log, informando que ele não será executado no momento.
- Se estiver sendo rodado algum processamento de matriz, será apresentada uma mensagem no log, informando que existem matrizes sendo executadas e a consolidação não será feita no momento.

**Nota:** nesta tela, não é possível desenvolver mais de um agendamento simultâneo. Caso isso ocorra, o primeiro agendamento será executado normalmente, enquanto o segundo receberá a seguinte mensagem:

**"Análise de Giro com código 44507 já está sendo executada por outro usuário, verifique."**

Se o Job 'AgendadorConsolidacaoGiroJob' não tiver sua consolidação finalizada, o sistema mostrará a seguinte mensagem:

**"Uma consolidação de giro está sendo executada neste momento, tente novamente mais tarde."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#top)

### Como funciona o estoque mínimo e máximo dos produtos

A Análise de Giro define uma prioridade para organizar o Estoque Mínimo e o Estoque Máximo que serão utilizados como base no processamento. Inicialmente, o Sankhya OM busca as informações de estoque mínimo e máximo lançadas na aba **"Impostos/Informações por empresa"** do [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Se não houver registros de estoque mínimo e máximo nesta aba específica, o sistema segue a lógica padrão.

O sistema irá buscar a informação do estoque mínimo e máximo da aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaestoque) sempre que, nas configurações da matriz de giro for selecionado no campo **"Apresentar resultado por:" Empresa, local e/ou Controle.**
Quando não for selecionada nenhuma dessas opções no campo citado, o sistema buscará a informação do estoque mínimo e máximo já preenchida na aba **Medidas e estoque.**

![9b9087f0-c329-4e14-b4cf-dd5f134049e0](https://ajuda.sankhya.com.br/hc/article_attachments/31898583211031)A  Análise de Giro calcula a Sugestão de Compra quando o Estoque Atual do produto está menor que o Estoque Mínimo (apurado conforme a regra de prioridade).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#top)

### Parâmetros importantes

Os parâmetros abaixo estão relacionados à geração do Custo de Reposição e Sugestão de Compra, além do Valor Unitário a ser considerado na validação do evento [68 - Variação do vlr. unit. orig./dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#68-variaodovlr.unit.orig.dest.).

**Cus. rep. matriz analise giro baseado tab. cotação - TABCOTFORMTZ:** a habilitação desse parâmetro define que o custo de reposição será alimentado através da tabela de cotação do fornecedor principal do produto. A utilização do parâmetro de chave TABCOTFORMTZ implica na realização das seguintes configurações:

- Deve-se criar uma [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os) que corresponda à tabela de cotação, onde deverá inserir o produto desejado;
- O produto tem que possuir um Parceiro Fornecedor preferencial; campo com esta nomenclatura, localizado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral);
- No [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) fornecedor, aba [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abainformaes), informe no campo **"Tabela p/ usar módulo cotação"** a Tabela de Preços inicialmente cadastrada.

**Sug. de compra estoque mínimo ao máximo? - SUGCOMPMIMAMTZ:** quando ativado, define que a sugestão de compra será feita para se alcançar o estoque máximo do produto, ou seja, a sugestão de compra será calculada com base na seguinte equação:

```
 Sug. Compra = Estoque Máx. – Estoque
```

Com o parâmetro desligado, o sistema calcula a sugestão de compra respeitando a seguinte fórmula:

```
 Sug. Compra = (Estoque Min. * % Acréscimo na Sugestão de Compras)
 – Estoque – Compra Pendente + Venda Pendente
```

**Observação:** na fórmula acima, o campo **"Estoque"** já considera as **"Entradas Pendentes"** somando e a **"Venda Pendente"** diminuindo.

**Importante:** o parâmetro SUGCOMPMIMAMTZ apenas será utilizado quando o Estoque for menor que o **"Estoque Mínimo"**.

**Tipo arred. mult. compra na Análise de giro - TIPARMULTCPGIRO:** esse parâmetro irá interferir diretamente nos resultados dos campos Sug. Compra Mult. Cpa e Multipl. Compra da matriz. Para isso, a matriz buscará pelo fator multiplicador informado no campo **"Multipl. Compra"** da aba [Produtos Equivalentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosequivalentes) no Cadastro de Produtos. Depois, irá aproximar a Sug.Compra Mult.Cpa do fator multiplicador de acordo com a configuração realizada neste parâmetro, que pode ser definido dentre as 4 (quatro) opções abaixo:

- **Sempre para mais:** a matriz sempre irá aproximar o arredondamento da sugestão para mais;
- **Meio acima:** por meio desta opção, a matriz irá analisar se o percentual faltante para alcançar o arredondamento é maior ou igual a 50%, dessa forma, o arredondamento será para cima.
- **Meio abaixo:** esta alternativa possui o mesmo comportamento da opção Meio acima, porém, caso o percentual esteja abaixo de 50%, o arredondamento será feito para baixo;
- **Sempre para menos:** através desta opção, o arredondamento será feito sempre para baixo, sem avaliação do percentual faltante.

**Observação:** para que o sistema utilize o valor definido no Cadastro de Produtos, aba Produtos Equivalentes, campo Multipl. Compra, é necessário preencher o campo o **"Fornec. Preferencial"** localizado na [Grade Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradeprodutos) da tela Análise de Giro. Caso este campo não seja preenchido será utilizado o valor definido no campo **"Qtd. multiplicador Compra"** presente na aba Geral do Cadastro de Produtos.

**Campo p/ validação valor unit. evento 68? - CAMVLRUNITEVT68:** insira nesse parâmetro o nome do campo criado no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) que será responsável pela validação do evento [68 - Variação do vlr. unit. orig./dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#68-variaodovlr.unit.orig.dest.), ou seja, caso seja informado no referido parâmetro algum campo (que pode ser também um Campo Adicional), o sistema irá tomar este por base para validar o evento 68; o sistema não irá validar o evento 68 utilizando o campo Vlr. Unitário (tabela TGFITE) do pedido.

**Qtd. meses p/ refazer consolidação compra/venda - QTDMESESRETCONS:** por meio desse parâmetro a quantidade de meses será definida para realizar a consolidação da última compra e venda. Sendo assim, apenas os últimos X meses (definidos no campo **"Inteiro"** do parâmetro) serão refeitos.

**Observação:** para desabilitar o parâmetro, configure-o com o valor 0; desta forma, o sistema irá refazer a tabela de consolidação, retroagindo 6 meses. 

**Ignora última compra/venda na matriz? - MATSEMMULTCPVD:** quando habilitado, a consolidação da tabela de última compra/venda deixa de ser executada durante o processamento da Matriz de Giro. Isso melhora a performance em bases grandes, já que essa consolidação percorre todo o histórico de notas para reconstruir a tabela. Em contrapartida, os campos Últ. Vnd e Dias Sem Venda deixam de refletir as movimentações reais do produto.

**Controla acesso para consolidador de giro? - CONTACESSCONSOL:** quando habilitado, irá liberar na tela [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) as configurações específicos da caixa de seleção **"Consolidação do Giro"**. Se este parâmetro estiver ativado, será possível acessar as funcionalidades do botão   **"Agendamento da geração da tabela de giro"** na tela Análise de Giro.

Caso seja feita a tentativa de utilização deste botão por uma pessoa que não possui esta liberação em seus acessos, será apresentada a mensagem descrita abaixo: 

**"Seu usuário não possui permissão de acesso a funcionalidade".**

**Nota:** se o parâmetro estiver desabilitado, o comportamento do sistema em relação ao botão mencionado não será alterado, ou seja, todas as pessoas terão acesso à função do botão mencionado.

**Validar custo repetido na consolidação de giro? - VALCUSREPCONGIR:** quando estiver desligado, a validação de custos duplicados na consolidação de giro não será realizada.

**Qtd. meses p/ refazer consolidação matriz giro - MESESRETCONSGIR:** por meio desse parâmetro pode-se informar o número de meses que o sistema irá retroagir para que seja iniciada a consolidação da matriz.

**Limite em % para Curva B - LIMCURVA\_BPRO"** e **"Limite em % para Curva C - LIMCURVA\_CPRO:** por meio desses parâmetros são informados os percentuais que irão representar o total no faturamento dos produtos em um determinado período, ou seja, o quanto os produtos contribuíram para o faturamento obedecendo o percentual estipulado. Por exemplo:

Se deseja identificar quais produtos atingiram os percentuais no faturamento total da empresa de 40%, 30% e 30%, sendo estes percentuais para A, B e C respectivamente, informa-se **"30"** em ambos os parâmetros, e o restante (40%) o sistema automaticamente irá atribuir para **"A"**.

**Usa Dt.EntSai. p/entradas na consolidação de Giro? - DTENTSAIGIRENT:** ao ligar este parâmetro, o sistema considerará o campo **"Dt. Entrada/Saída"** das movimentações de Compra e Devolução de Venda na consolidação de giro.

**Filtro adicional para a consolidação do giro - FILTROADCGIRO:** insira nesse parâmetro um filtro adicional em formato SQL e, no momento da execução da rotina de consolidação do giro, o sistema irá considerar o filtro definido. Observe o seguinte exemplo:

Utiliza-se a empresa 100 para realizações de notas de transferências e essas notas geradas com essa empresa não podem fazer parte do giro; sendo assim, deve-se fazer o seguinte filtro: TGFCAB.CODEMP <> 100. Com esse exemplo de filtro, não serão consolidadas as notas da empresa 100.

O filtro deve iniciar com a expressão do filtro direto, conforme demonstrado acima, ou iniciar com **'AND'**. Qualquer expressão diferente disso, por exemplo **'OR'**, fará com que a consolidação não possa ser realizada.

Apenas as tabelas abaixo podem participar do filtro adicional:

- TGFITE
- TGFPRO
- TGFCUS
- TGFCAB
- TGFEMP
- TGFCGM
- TGFTOP

Para utilizar um filtro da TGFCAB ou da TGFTOP, faça-o da seguinte forma: TGFCAB.[campo] ou TGFTOP.[campo]; para usar os demais, faça conforme escrevemos abaixo:

- ITE.[campo]
- PRO.[campo]
- CUS.[campo]
- EMP.[campo]
- CGM.[campo]

**Nota:** é possível usar EXISTS com um select em outras tabelas que não estão na lista porém, a ligação deverá ser feita com um campo dessas tabelas e usadas das formas que descrevemos acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro#top)

![Imagem 8: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/23614659879447) Acesse também:

[Análise de Giro - Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554)

[Campos para Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro)
