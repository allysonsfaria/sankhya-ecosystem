---
id: "360044609874"
titulo: "Planejamento Orçamentário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:25:49Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Despesa", "Realizado", "Previsto", "Metas", "TOP", "Preferências", "Financeiro", "Natureza", "Receita", "Base de Planejamento", "Cálculo relativo", "Diferença", "Grupo de Natureza", "Hieráquica", "Pivot", "Planejamento Orçamentário", "br.com.sankhya.com.avancado.planejamentoorcamentario", "Planejamento Orçamentário manual", "Configuração e Utilização do Planejamento Orçamentário", "Configuração Metas Planejamento."]
---

# Planejamento Orçamentário

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311922491415) Módulo: Comercial > Avançado
```

---

**Importante:** Esta tela foi substituída pela tela [Planejamento de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814). Deste modo, é recomendável o uso da nova tela.

[Configurações para utilização da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configura%C3%A7%C3%B5esparautiliza%C3%A7%C3%A3odatela)                              [Planejamento Orçamentário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#planejamentoor%C3%A7ament%C3%A1rio)

Teremos neste artigo, um passo a passo para utilização do Planejamento Orçamentário por Grupo de Naturezas.

## Configurações para utilização da tela

Abaixo, daremos as especificações para utilizações da tela Planejamento Orçamentário, sendo que algumas delas serão realizadas na tela [Configuração da Estrutura de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794):

[Configurações para Natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configura%C3%A7%C3%B5esparanatureza)                                               [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#abageral)

[Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#abapropriedades)                                                                    [Aba TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#abatop)

**Importante:** Antes de iniciar o planejamento, certifique-se de que a estrutura da sua meta esteja configurada corretamente na tela "**Configuração da Estrutura de Metas/Orçamentos"**. Para metas por Gerente, é fundamental que o campo `Vendedor` também esteja selecionado nos `Campos Significativos`. Acesse o artigo [Configuração da Estrutura de Metas/Orçamentos](https://www.google.com/search?q=link_do_artigo) para mais detalhes.

## Configurações para Natureza

**1.** Configuração do parâmetro para definição da máscara para o Grupo de Naturezas

Para que seja possível a configuração do(s) grupo(s) de naturezas, inicialmente é necessário realizar as devidas configurações do parâmetro **"Máscara para grupo de naturezas - MASCGRUPONAT"** utilizando a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

**2.** Após a configuração deste parâmetro é possível efetuar a configuração do Grupo de Naturezas

![Imagem 2: 2. Após a configuração deste parâmetro é possível efetuar a configuração do Grupo de Naturezas](https://ajuda.sankhya.com.br/hc/article_attachments/1500003983541)

A tela [Grupo de Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598514) possui configurações hierárquicas onde são cadastrados os Grupos de Naturezas sendo possível vincular as naturezas já existentes no sistema por meio da aba Naturezas.

Diante disto, considere que:

- As naturezas que serão relacionadas ao Grupo de Naturezas obrigatoriamente deverão ser marcadas como analíticas;
- Apenas os Grupos de Naturezas analíticos poderão ter naturezas vinculadas a si;
- Uma natureza só pode ser vinculada a um único grupo de naturezas; por exemplo, se for vinculada a natureza 10 ao grupo 15, não será possível vincular essa mesma natureza 10 para o grupo 22.

O campo **"Tipo de natureza"** localizado na tela Grupo de Naturezas deve ser preenchido considerando as opções **"Receita"** e **"Despesa"**, além disso, essas opções devem ser consideradas também na tela Natureza de Receitas e Despesas ([Financeiro> Relatórios> Cadastros> Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)). Ainda nesse contexto, você irá configurar o Grupo de Naturezas conforme o tipo que o corresponde, pois influenciará na visualização da tela de Planejamento Orçamentário.

**Observação:** o vínculo do tipo de natureza do Grupo de Naturezas deve ser realizado antes de se relacionar as naturezas que farão parte deste. Pode-se também buscar somente as naturezas condizentes com o tipo de natureza vinculado ao grupo, pois quando a natureza e o tipo de natureza configurado estiverem diferentes, será emitida a seguinte mensagem:

**"Não é possível vincular a um grupo, uma natureza que não tenha tipo de natureza definido."**

**3.** Configuração das Naturezas com relação ao campo **"Tipo de natureza"**

O campo **"Grupo da Natureza"** será exibido somente para as naturezas analíticas. Posto isto, mesmo solicitando para apresentar hierarquia na pesquisa deste campo, serão visualizados somente os Grupos de Naturezas analíticos.

**Nota:** caso a natureza não possua Grupo de Naturezas informado, ou seja, Grupo de Natureza zero, o sistema não efetuará validação com relação ao Tipo de Natureza.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configura%C3%A7%C3%B5esparautiliza%C3%A7%C3%A3odatela)

## Aba Geral

Ao utilizar esta aba, você poderá realizar a Configuração de Metas/Orçamentos. Para isto, inicialmente acesse a tela [Configuração da Estrutura de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794).

![Imagem 3: Ao utilizar esta aba, você poderá realizar a Configuração de Metas/Orçamentos . Para isto, inicialmente acesse a tela…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003918482)

Ainda neste contexto, será necessário configurar o campo **"Tipo de Meta"** selecionando a opção **"Financeira"** e mantendo a marcação como **"Ativo"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configura%C3%A7%C3%B5esparautiliza%C3%A7%C3%A3odatela)

## Aba Propriedades

Em relação a esta aba, considere as seguintes informações:

![Imagem 4: Em relação a esta aba, considere as seguintes informações:](https://ajuda.sankhya.com.br/hc/article_attachments/1500003918562)

No campo **"Periodicidade"** marque a opção **"Mensal"**, após este procedimento, configure no campo **"Campos Significativos"** a opção **"Grupo Natureza"** uma vez que esta será utilizada no Planejamento Orçamentário. Você também poderá selecionar uma opção adicional, como por exemplo, **"Períodos"**.

O campo **"Quando exceder a Despesa Prevista"** deve ser selecionado em conformidade ao que o sistema deverá executar. Se a opção de solicitação de liberação for marcada ao efetuar os lançamentos que condizem com a meta/orçamento, será solicitada a liberação de limites, evento 16 – Metas para Despesas. Dessa forma, tem-se o exemplo:

**"Avisar e Não aceitar o lançamento"** ou **"Exigir Liberação SEMPRE, mesmo que não exceda o orçamento"**.

**Observação:** ao efetuar a Configuração de Metas/Orçamentos selecionando simultaneamente no campo **"Campos Significativos"** as opções **"Natureza"** e Grupo Natureza o sistema não permitirá esta ação, emitindo a seguinte mensagem:

**"Não pode ter numa mesma Meta/Orçamento, Natureza e Grupo Natureza."**

**Nota:** para proceder com as devidas configurações de Metas/Orçamentos considerando que tenha sido selecionada a opção Grupo Natureza, faz-se necessário habilitar o parâmetro **"Utiliza Grupo de Naturezas? - UTILIZAGRUPONAT"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configura%C3%A7%C3%B5esparautiliza%C3%A7%C3%A3odatela)

## Aba TOP

Por meio dessa aba, configure as TOP's que serão consideradas nos lançamentos.

![Imagem 5: Por meio dessa aba, c onfigure as TOP's que serão consideradas nos lançamentos.](https://ajuda.sankhya.com.br/hc/article_attachments/360102769454)

Ao realizar a vinculação das TOP's considerando a Configuração da Meta, tem-se como finalidade realizar a atualização do realizado e previsão do planejamento das Metas/Orçamentos.

**Observação:** para maiores detalhes sobre a configuração das TOP's mencionadas anteriormente, acesse a tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configura%C3%A7%C3%B5esparautiliza%C3%A7%C3%A3odatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#top)

## Planejamento Orçamentário

Após as Configurações da meta serem realizadas, você poderá realizar o Planejamento Orçamentário. Desta forma, na referida teremos:

[Seleção da Base de Planejamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#sele%C3%A7%C3%A3odabasedeplanejamento)                        [Barra de Filtros não hierárquica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#barradefiltrosn%C3%A3ohier%C3%A1rquica)

[Barra de Filtros hierárquica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#barradefiltroshier%C3%A1quica)                                     [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#outrasop%C3%A7%C3%B5es)

## Seleção da Base de Planejamento

Por meio da tela Planejamento Orçamentário, serão apresentadas todas as Metas/Orçamentos que foram configuradas como o Tipo de Meta Financeira, Ativo e cuja marcação de periodicidade tenha sido classificada como Mensal.

Primeiramente, selecione a Meta que você deseja configurar o planejamento orçamentário e clicar no botão **"Avançar"**. Após a seleção da Meta, selecione a Base de Planejamento conforme as especificações configuradas na tela Configuração da Estrutura de Metas/Orçamentos:

![Imagem 6: Primeiramente, selecione a Meta que você deseja configurar o planejamento orçamentário e clicar no botão "Avançar" .…](https://ajuda.sankhya.com.br/hc/article_attachments/360102769574)

Posteriormente, selecione a Base de Planejamento. Nesta etapa, serão apresentados todos os campos significativos, exceto o período, para selecionar a Base de Planejamento.

**Nota:** a Base de Planejamento é o campo configurado na Meta\Orçamento sendo utilizado para definir a Estrutura da grade.

Ao clicar em Avançar o sistema irá para a tela de Planejamento Orçamentário e trará a tela de Filtros constando a grade orçamentária.

[GIF animado: Imagem 7: Ao clicar em Avançar o sistema irá para a tela de Planejamento Orçamentário e trará a tela de Filtros constando a grade…](https://ajuda.sankhya.com.br/hc/article_attachments/360102770034)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#planejamentoor%C3%A7ament%C3%A1rio)

## Barra de Filtros não hierárquica

![Imagem 8: Barra de Filtros não hierárquica](https://ajuda.sankhya.com.br/hc/article_attachments/1500003919342)

No campo **"Filtro"**, informe o texto que você deseja pesquisar e o sistema fará a busca **"Começando por"**. Considere o exemplo:

Ao informar o texto **"Des"** o sistema buscará todos os Grupos de Natureza que inicie com este nome.

Em **"Ano"**, indique o ano do planejamento.

O **"Tipo de meta"** poderá ser classificada como **"Despesa"** ou **"Receita"**. Se marcado Despesa trará todos os orçamentos\metas configurados para Despesa, senão para Receita.

**Observação:** caso seja selecionada a opção Receita e seja necessário visualizar a opção Despesa, o sistema não trará as informações. Se na Base de Planejamento for definida a **"Natureza"** ou o **"Grupo de Natureza"** o sistema não trará para visualização as opções mencionadas anteriormente. Posto isto, para esse caso, serão visualizadas todas as previsões de Receitas e Despesas ao mesmo tempo.

Ao utilizar o botão **"Aplicar"**, os filtros informados serão aplicados na grade.

Quando você pressionar o botão **"Salvar"**, o sistema irá salvar todas as informações alteradas e/ou incluídas. 

Por meio do botão **"Outras Opções"** teremos as seguintes opções:

- Adicionar item da Grade;
- Configurar Grade;
- Importar Arquivo de Planejamento;
- Log de Importação;
- Editar Filtros.

**Nota:** estas opções serão detalhadas nesta documentação posteriormente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#planejamentoor%C3%A7ament%C3%A1rio)

## Barra de Filtros Hierárquica

![Imagem 9: Barra de Filtros Hierárquica](https://ajuda.sankhya.com.br/hc/article_attachments/360102770394)

No **"Filtro"** informe o texto que você deseja pesquisa e o sistema fará a busca **"Começando por"**. Considere o exemplo:

Ao informar o texto **"Des"** o sistema buscará todos os Grupos de Natureza que inicia com este nome.

Por meio do botão  **"Expandir"**, irá expandir todos os níveis da árvore.

O Botão  **"Retrair"** irá retrair todos os níveis contidos na árvore.

Em **"Ano"**, informe o ano do planejamento.

Ao utilizar o botão **"Aplicar"**, os filtros informados serão aplicados na grade.

Quando você pressionar o botão **"Salvar"**, o sistema irá salvar todas as informações alteradas e/ou incluídas. 

Por meio do botão **"Outras Opções"** teremos as seguintes opções:

- Configurar Cálculo Relativo;
- Configurador da grade e;
- Editar Filtros.

**Observação:** se o campo selecionado como Base de Planejamento não for hierárquico, o sistema não gerará a grade, só se já houver algum Planejamento Orçamentário configurado. Se for hierárquico, teremos por exemplo: Grupo de Naturezas, o sistema efetuará a construção da Grade.

Tem-se abaixo um exemplo de Campo Base de Planejamento não configurado como hierárquico. Dessa forma, suponhamos que tenha sido definida como Base de Planejamento o campo **"Empresa"** e ao efetuar o filtro o sistema trouxe um orçamento já configurado:

![Imagem 10: Tem-se abaixo um exemplo de Campo Base de Planejamento não configurado como hierárquico. Dessa forma, s uponhamos que…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000246761)

Orçamento configurado para um campo não hierárquico

Caso não tenha nenhum orçamento configurado, virá em branco a tela. Para inserir um novo planejamento orçamentário deve-se utilizar o botão **"Outras Opções"** selecionando a opção **"Adicionar item de meta"**:

![Imagem 11: Caso não tenha nenhum orçamento configurado, virá em branco a tela. Para inserir um novo planejamento orçamentário…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000236022)

Abrirá uma tela de pesquisa para seleção da empresa:

Uma vez selecionada a empresa, configure a previsão do orçamento para os meses do Ano de Planejamento.

![Imagem 12: Uma vez selecionada a empresa, configure a previsão do orçamento para os meses do Ano de Planejamento.](https://ajuda.sankhya.com.br/hc/article_attachments/1500000246841)

Inicialmente selecione a empresa e depois para realizar a configuração do campo **"Previsto"** basta dar duplo clique no campo e teclar enter ou tab. Após este procedimento, será solicitado para Salvar as Alterações e Aplicar de acordo com as alterações efetuadas.

As Bases de Planejamento, Natureza ou Grupo de Naturezas, são apresentadas na grade Receita e Despesa simultaneamente nas cores azul para receita e vermelha para despesa, conforme configurado no cadastro de Grupo de Natureza e Natureza, campo **"Tipo de Natureza"**.

Logo, se estiver configurado para o Tipo de Natureza ser igual à receita será inserido a previsão de receita e o contrário de despesa. O cálculo da coluna Realizado para Receitas é Realizado de Receita (REALREC) – Realizado de Despesa (REALDESP) e o inverso para despesas.

Na Seleção da Base de Planejamento considere o **"Grupo de Naturezas"** sendo informados os filtros:

![Imagem 13: Na Seleção da Base de Planejamento considere o "Grupo de Naturezas" sendo informados os filtros:](https://ajuda.sankhya.com.br/hc/article_attachments/360099116014)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#planejamentoor%C3%A7ament%C3%A1rio) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#top)

## Outras Opções

Por meio deste botão teremos algumas opções que influenciarão na tela, sendo estas:

[Configurar Cálculo Relativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configurarc%C3%A1lculorelativo)                                     [Editar Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#editarfiltros)

[Configurar Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#configurargrade)                                                        [Importar Arquivos de Planejamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#importararquivosdeplanejamento)

[Log de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#logdeimporta%C3%A7%C3%A3o)

## Configurar Cálculo Relativo

Para as Metas/Orçamentos gerados mediante uma Base de Planejamento hierárquico, o sistema disponibilizará no botão **"Outras Opções"** selecionando a opção **"Configurar cálculo relativo"** as seguintes funcionalidades:

![Imagem 14: Para as Metas/Orçamentos gerados mediante uma Base de Planejamento hierárquico, o sistema disponibilizará no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/360099116054)

Ao clicar nesta opção o sistema abrirá a seguinte tela:

![Imagem 15: Ao clicar nesta opção o sistema abrirá a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/360101347953)

Selecione o Grupo de Naturezas a ser considerado e clicar no botão **"Finalizar"**:

**Observação:** o sistema trará nesta tela o cálculo relativo ao anteriormente configurado para que você possa saber qual foi à última configuração. O sistema efetuará o cálculo do percentual da Base de Planejamento levando em consideração a base de cálculo selecionada. Por exemplo:

![Imagem 16: Observação: o sistema trará nesta tela o cálculo relativo ao anteriormente configurado para que você possa saber qual…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000236342)

Esta figura traz os percentuais mediante a configuração da base de cálculo, em que a **"% Meta"** trará os percentuais referentes a todos os meses da Meta.

Na coluna de Janeiro, o Grupo de Natureza configurado para a Base de Calculo são as **"Despesas administrativas"**, portanto, esta será 100% para todos os meses inseridos a Previsão. No Mês de Janeiro o valor de R$100 equivale aos 100%.

Analisando no Grupo de Naturezas **"Comissões"** verifica-se que o valor R$100,00 referente aos R$200,00 que são os 100% equivale a 150% do total da Meta.

Se no Mês de Janeiro houvesse uma previsão zerada ou sem valor, o sistema zeraria o percentual:

- Total Anual:

![Imagem 17: Total Anual:](https://ajuda.sankhya.com.br/hc/article_attachments/360099116514)

Como já explicitado acima, a coluna % Meta é referente aos percentuais referentes a todos os meses da meta.

O **"Previsto"** equivale ao somatório do total de todas as previsões do total de meses do ano de planejamento.

Em **"Realizado"** teremos o somatório do total de todos os realizados do total de meses do ano de planejamento.

A **"Diferença"** refere-se à diferença entre o Realizado menos o Previsto do total de meses do ano de planejamento.

O **"% Pivot"** é a somatória de todos os itens de meta para o mês que a coluna representa, ou seja, se a coluna é janeiro, e a somatória de todos os itens do mês para janeiro sendo 100, se eu tenho 1 item de meta em janeiro que é 10, então esse item de meta representa 10% do pivot.

- Totalizadores:

![Imagem 18: Totalizadores:](https://ajuda.sankhya.com.br/hc/article_attachments/360099116974)

O **"Saldo Anterior"** é o saldo final do mês anterior. O único mês que fica com o valor zerado é o mês de Janeiro.

A coluna **"Total Mensal"** refere-se ao valor total previsto e realizado para cada mês. O campo virá preenchido somente se houver valor de previsão e/ou realizado preenchido.

Em **"Saldo Atual"** teremos o somatório do mês analisado com o mês anterior. Exemplo: Mês de Março será o somatório do mês de Janeiro + Fevereiro+ Março.

**Nota:** é relevante mencionar que:

1. Os totalizadores estão disponíveis para todos os tipos de estruturas;

2. Só irão atualizar os valores dos Totalizadores mediante as opções **"Salvar"** e **"Aplicar"**, caso contrário, serão considerados os valores antigos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#outrasop%C3%A7%C3%B5es)

## Editar Filtros

Ao clicar nesta opção o sistema trará a tela de filtros para que se possa selecionar novos campos para gerar novos planejamentos.

**Observação:** para o navegador Internet Explorer existem algumas incompatibilidades que ainda serão resolvidas e por isso solicita-se que utilize os navegadores Firefox e o Chrome para utilização desta tela.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#outrasop%C3%A7%C3%B5es)

## Configurar Grade

Esta opção serve para indicar quais são os meses e campos que deverão ser visualizados no planejamento orçamentário.

Esta configuração é gravada por usuário e é determinada por dois tipos de configurações, sendo:

1. Bases de planejamentos hierárquicas, como por exemplo: **"Natureza"**, **"Centro de Resultado"** e **"Grupo de Naturezas"**;

2. Bases de planejamentos não hierárquicas, como por exemplo: **"Estado (UF)"**, **"Cidade"**, **"País"**, **"Parceiro"** e **"Empresa"**.

**Nota:** é relevante mencionar que ao salvar configurações para a Base de Planejamento hierárquico, essa configuração valerá para o restante das entidades hierárquicas de todas as metas configuradas e vice-versa, ou seja, o mesmo valerá para Base de Planejamento não hierárquica.

#### Base de Planejamento Não hierárquica:

![Imagem 19: Base de Planejamento Não hierárquica:](https://ajuda.sankhya.com.br/hc/article_attachments/1500000248441)

Trará todos os meses na grade, assim como, as marcações a serem selecionadas, sendo **"Total Anual"**, **"Previsto"**, **"Realizado"** e **"Diferença"**.

#### Base de Planejamento Hierárquico:

![Imagem 20: Base de Planejamento Hierárquico:](https://ajuda.sankhya.com.br/hc/article_attachments/360101348853)

Trará todos os meses na grade e as marcações a serem selecionadas, tais como **"Total Anual"**, **"Previsto"**, **"Realizado"**, **"Diferença"**, **"% Pivot"**, **"% Meta"** e **"% Diferença"**.

**Observação:** caso você não realize nenhuma configuração, prevalecerá a que for configurada para o usuário SUP.

A opção **"Marcar/Desmarcar Todos"** irá marcar ou desmarcar todos os meses e o Total Anual.

Quando nenhum mês ou Total Anual for selecionado, o sistema não permitirá salvar e exibirá a mensagem:

**"Não é possível salvar as configurações, sem selecionar no mínimo uma coluna de mês/campo de meta para apresentação na grade."**

**Nota:** esse procedimento servirá tanto para não hierárquicos como também hierárquicos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#outrasop%C3%A7%C3%B5es)

## Importar Arquivos de Planejamento

O arquivo deverá conter as informações em conformidade com o filtro da meta, estas informações deverão estar no Header (primeira linha do arquivo) além do Ano de Planejamento e Data/Hora da Geração do Arquivo. Os campos no arquivo devem estar delimitados pelo caractere "Pipe" (|).

Como o filtro é variável, de acordo com o Pivot escolhido, cada informação do Header deve estar precedida de uma chave de referência para se obter a que aquela informação se refere. Sendo as chaves:

- **Meta:** MET
- **Empresa:** EMP
- **Projeto:** PROJ
- **Natureza:** NAT
- **Centro de Resultado:** CR
- **UF:** UF
- **Cidade:** CID
- **País:** PAIS
- **Perfil:** PERFIL
- **Ano de Planejamento:** ANO
- **Data/Hora da Geração do Arquivo:** DHGER

Devido à utilização destas chaves a ordem das informações no Header não importa com exceção do campo **"DHGER"**, que deve sempre ser o último. A validação será feita com base nos filtros informados na tela de Planejamento, ou seja, todos os valores informados no filtro devem possuir seu correspondente no header do arquivo de importação. Sendo obrigatório no mínimo as informações **"Cód. Meta"**, **"Ano de Planejamento"**, **"Data/Hora da Geração do Arquivo"** e **"Natureza"** (caso esta não seja o pivot).

Teremos ainda que para o detalhamento (2ª linha em diante) serão informados o **"Mês da Referência"**, o **"Código do Pivot"** e **"Valor"**. Sendo necessariamente nesta ordem e não contendo as chaves precedendo os valores. As linhas de detalhamento são validadas em relação ao mês de referência e a existência do pivot selecionado com aquele código do arquivo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#outrasop%C3%A7%C3%B5es)

## Log de Importação

Na tela Configuração da Estrutura de Metas/Orçamentos foi inserido o caminho do arquivo de importação.

![Plaorç31](https://ajuda.sankhya.com.br/hc/article_attachments/360061938553)

Na tela em referência Planejamento Orçamentário foi selecionada a meta 20.

![Plaorç32](https://ajuda.sankhya.com.br/hc/article_attachments/360061938573)

Em seguida selecionada a base: Empresa.

![Plaorç33](https://ajuda.sankhya.com.br/hc/article_attachments/360061938593)

Informados os dados no filtro em conformidade com os dados inseridos no arquivo.

![Plaorç34](https://ajuda.sankhya.com.br/hc/article_attachments/360061019254)

No botão **"Outras Opções"** acione a opção **"Importar Arquivo de Planejamento"**.

![Plaorç35](https://ajuda.sankhya.com.br/hc/article_attachments/360061019274)

**Observação:** a segunda mensagem só será exibida caso o arquivo já tenha sido importado anteriormente.

Após confirmar as mensagens, o planejamento "Empresa Teste Boleto" foi importado em conformidade com os dados do arquivo.

![Plaorç36](https://ajuda.sankhya.com.br/hc/article_attachments/360061019294)

Após a importação do arquivo, no botão **"Outras Opções"**, opção **"Log de Importação"** são verificados todos os registros de importação.

![Plaorç37](https://ajuda.sankhya.com.br/hc/article_attachments/360061019334)

Para visualizar melhor o erro basta dar um duplo clique no registro desejado.

![Plaorç38](https://ajuda.sankhya.com.br/hc/article_attachments/360061938633)

**Nota:** destacamos que a rotina de importação desta tela encontra-se indisponível.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#outrasop%C3%A7%C3%B5es) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio#top)
