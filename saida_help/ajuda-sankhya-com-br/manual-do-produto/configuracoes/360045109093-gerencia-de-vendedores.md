---
id: "360045109093"
titulo: "Gerência de Vendedores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:27Z"
rotulos: ["Produtos", "manual", "Configuração", "Parceiro", "Central de Vendas", "Relatórios Gerenciais", "Parceiros", "Cubo", "Bairro", "Estatísticas", "Movimentos", "Negociações Mensais", "QTDMAXREGEXPORT", "UF", "Grupo de Produtos", "ADDFILTVENDEDOR", "Cidade", "Gerência de Vendedores", "Maiores Parceiros", "Parceiro em Potencial", "br.com.sankhya.mgecom.cons.gerenciavendedores", "Gerência de Vendedores manual", "Vendedores", "Gerência de Vendedores: Análise Detalhada"]
---

# Gerência de Vendedores

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310918113559) Módulo: Comercial > Gerente
```

---

A Gerência de Vendedores é semelhante as demais telas de gerência e permite que seja realizada análise em um **"Objeto Principal"**, que é a análise de resultado por vendedores, cruzando as informações com diversos outros critérios que possam ser relevantes.

Considere o seguinte exemplo:

Pode-se selecionar um **"Vendedor"** indicado na grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) para análise e visualizar os resultados de desempenho desse vendedor por produtos, parceiros, grupos de produtos, entre outros. Importante observar que a tela não inclui os vendedores informados na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens).

Na tela, temos disponíveis as seguintes abas:

| [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#paineldefiltros) | [Aba Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abaparceiros) |
| --- | --- |
| [Aba Estatísticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abaestat%C3%ADsticas) | [Aba Movimentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abamovimentos) |
| [Aba Maiores Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abamaioresparceiros) | [Aba Negociações Mensais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abanegocia%C3%A7%C3%B5esmensais) |
| [Aba UF/Cidade/Bairro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abauf/cidade/bairro) | [Aba Perfil de Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abaperfildeparceiro) |
| [Aba Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abaprodutos) | [Aba Grupo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abagrupodeprodutos) |
| [Aba Parceiros em Potencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#abaparceirosempotencial) |  |

A visualização dos dados por usuário na Gerência de Vendedores, se dará com base na configuração realizada no campo **"Ver Pedidos/Notas (WEB)"** presente na aba Segurança do [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios). Além disso, o parâmetro **"Adicionar verificação do vendedor associado à nota? - ADDFILTVENDEDOR"** deve estar ativado. Vejamos através de um exemplo, como o sistema irá se comportar:

Suponhamos que o Diretor da Empresa queira visualizar as vendas de todos os vendedores subordinados a ele; então no cadastro do seu usuário, configure o Vendedor (aba Identificação) e defina o campo Ver Pedidos/Notas (WEB) com a opção Desse vendedor e subordinados. O vendedor vinculado ao Diretor é gerente de todos os demais gerentes da empresa e estes por sua vez possuem outros vendedores vinculados a eles. Quando o Diretor acessar a Gerência de Vendedores informando o seu Vendedor, serão exibidas as informações pertinentes à todos os vendedores vinculados hierarquicamente a ele, ou seja Diretor > Todos os Gerentes > Todos os Vendedores.

Para a utilização da **"Gerência de Vendedores"**, é necessário que os [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) sejam agrupados segundo suas funções, por exemplo: Vendas, Compras, Devoluções, etc, pois será a partir destes grupos que serão filtrados os dados para a análise.

## Painel de Filtros

Por meio do botão ![Imagem 2: Por meio do botão , no lado esquerdo da tela, você poderá exibir o painel de filtros para facilitar a análise,…](https://ajuda.sankhya.com.br/hc/article_attachments/360095655094), no lado esquerdo da tela, você poderá exibir o painel de filtros para facilitar a análise, escolhendo: um Vendedor específico e um Período de Negociação. Os critérios definidos nos filtros serão aplicados para todas as abas da tela. Além dos filtros estáticos pode-se montar um filtro personalizado através do componente **"Assistente de filtros"**.

**Grupos TOP:**

Os grupos de TOP são definidos no cadastro de **"Tipo de Operação"**, ao selecionar um grupo o sistema trará para análise todas as negociações feitas com as TOP's que pertençam àquele agrupamento. O campo **"Marcar"** seleciona todas as TOP's da lista para filtrar os lançamentos; já o **"Desmarcar"** desmarca todas as TOP's da lista.

É possível selecionar grupos de TOPs individualmente marcando a caixa de seleção correspondente na lista de **"Grupos de TOP"**.

**Opções:**

A marcação **"Visualizar perfis"** habilitará na aba **"Parceiros"**, os painéis de **"Perfil do Parceiro"** e **"Perfil de Contato"**.

Se a opção **"Considerar Qtd. Negativa"** for marcada, fará com que as quantidades referentes às negociações de vendas sejam consideradas negativas pelo sistema, pois representam uma saída de produto do estoque. Marcando esta opção o sistema apresentará a coluna **"Qtd. Negociada"** com sinal **"negativo"** para as vendas e com sinal **"positivo"** para as compras, em todas as abas.

Caso a opção **"Considerar Qtd. Positiva"** estiver selecionada, o sistema apresentará a coluna **"Qtd. Negociada"** com sinal **"positivo"** para as vendas, e **"negativo"** para as compras, em todas as abas.

**Nota:** as duas opções anteriores são excludentes, ou seja, se você marcar uma a outra será automaticamente desmarcada.

**Observação:** as opções Considerar Qtd. Negativa e Considerar Qtd. Positiva só se comportará conforme descrito, se a opção **"Apoio a Decisão"** na aba **"Geral"** no **"Cadastro de TOP's"** estiver corretamente configurada de acordo com o **"Tipo de Movimento"**, ou seja, marcando **"Venda"** para **"TOP de venda"**, **"Compra"** para **"TOP de Compra"**, tanto para o produto quanto para Matéria-Prima (Tipo MP).

Se a opção **"Exibir componentes das fórmulas"** for marcada, faz com que sejam exibidos os produtos que são componentes de fórmulas, considerando as "Matérias-Primas" nos resultados. Se desmarcado as composições do produto não serão apresentadas para análise gerencial.

Com a marcação **"Somar S.T ao total da nota de compra?"** efetuada, esta somará ao total da nota o valor da Substituição Tributária.

Marcando-se a opção **"Não considerar o Vlr. Outros nas Compras"**, não serão considerados os acréscimos/descontos dos itens no pé das notas de compra; além disso, o VLROUTROS da nota não será considerado.

Uma vez definidos os filtros, clique no botão **"Aplicar"** pra que todas as informações referentes aos filtros estabelecidos sejam visualizadas nas abas à direita que seguem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Parceiros

Nesta aba é possível visualizar os parceiros com os quais o vendedor negociou no período especificado. A grade superior esquerda apresenta os dados do parceiro, como: código, nome etc. A grade superior direita apresenta os dados do contato. Quando a opção **"Visualizar perfis"** estiver marcada, nesta aba serão apresentados também os perfis do parceiro e do contato, em duas grades na parte inferior da tela.

![Imagem 3: Nesta aba é possível visualizar os parceiros com os quais o vendedor negociou no período especificado. A grade superior…](https://ajuda.sankhya.com.br/hc/article_attachments/360097954673)

Dando dois cliques sobre qualquer parceiro selecionado nesta aba, será aberta a tela **"Gerência de Parceiros"**, posicionada no parceiro selecionado, permitindo a análise gerencial do mesmo.

O componente de **"Impressão"** permitirá que os dados na grade sejam impressos em formato PDF, XLS (planilha), ou sejam visualizados em cubo.

![Imagem 4: O componente de "Impressão" permitirá que os dados na grade sejam impressos em formato PDF, XLS (planilha), ou sejam…](https://ajuda.sankhya.com.br/hc/article_attachments/360095657854)

**Nota:** por meio da configuração do parâmetro **"Qtd. máx. de reg. para export. de PDF, XLS e Cubo - QTDMAXREGEXPORT"**, tem-se a possibilidade de limitar a quantidade máxima de registros que serão exportados na utilização das funcionalidades **"Exportar como PDF"**, **"Exportar como planilha"** e **"Visualizar em cubo"**. Informe um número inteiro, que representa o limite de registro que serão exportados, por exemplo 50 registros, 100 registros; dependendo da necessidade da empresa/usuário.

O componente para **"Configuração da Grade"** permitirá a alteração do layout da grade, disponibilizando as colunas na ordem que você desejar.

Nesta aba, você não visualizará informações quando este possui em seu cadastro um vendedor configurado. Visto que a regra consiste em:

**1 -** Usuários que não são vendedores, quando têm acesso a esta tela podem ver as informações de TODOS os vendedores.

**2 -** Usuários que são vendedores, se enquadram em dois subgrupos:

**2.1 - Vendedores** - Só visualizam as informações a respeito da sua própria movimentação. Isso existe pois o Gerente de vendas pode permitir que cada vendedor acompanhe seu próprio desempenho.

  **2.2 - Vendedor gerente** - Visualizam as informações de todos os vendedores que o apontam como gerente. Esse tipo de usuário existe em um ambiente onde há mais de um gerente de vendas, assim cada gerente pode visualizar as informações de sua equipe. (A relação aqui deve ser direta, ou seja, vendedor A é gerente do vendedor B. Mesmo que o vendedor B seja gerente do vendedor C o vendedor A NÃO conseguirá ver a movimentação do vendedor C).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Estatísticas

Esta aba apresenta um resumo por parceiro, das negociações de compra, venda etc, de acordo com a seleção dos **"Grupos da TOP"**.

![Imagem 5: Esta aba apresenta um resumo por parceiro, das negociações de compra, venda etc, de acordo com a seleção dos "Grupos da…](https://ajuda.sankhya.com.br/hc/article_attachments/360095658274)

Nesta aba serão apresentadas algumas informações como, a quantidade total negociada, valor total negociado, quantidade de notas etc, todas por parceiro. No rodapé da aba será apresentado um totalizador das principais colunas.

Assim como na aba **"Parceiros"**, você poderá **"Imprimir"** os dados da grade, e também priorizar as colunas que deseja visualizar pelo componente **"Configuração da Grade"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Movimentos

Nesta aba são apresentadas nota a nota, todas as movimentações realizadas no período solicitado. Como uma forma analítica dos dados da aba Estatísticas.

![Imagem 6: Nesta aba são apresentadas nota a nota, todas as movimentações realizadas no período solicitado. Como uma forma…](https://ajuda.sankhya.com.br/hc/article_attachments/360095658674)

Nesta aba pode-se analisar todas as negociações feitas pelo vendedor, por data de negociação, quantidade negociada, número das notas etc.

Ao selecionar um título na grade será habilitado o botão **"Rentabilidade"**, onde ao acioná-lo, pode-se visualizar a contribuição desta negociação, pela análise de rentabilidade da nota.

![Imagem 7: Ao selecionar um título na grade será habilitado o botão "Rentabilidade" , onde ao acioná-lo, pode-se visualizar a…](https://ajuda.sankhya.com.br/hc/article_attachments/360095659094)

Para ver os detalhes das notas/pedidos, bastará dar um duplo clique sobre a negociação na grade ou selecionar a nota e clicar no botão **"Ver Nota/Pedido"**. O sistema exibirá a nota/pedido selecionada na tela **"Central de Vendas"**.

![Imagem 8: Para ver os detalhes das notas/pedidos, bastará dar um duplo clique sobre a negociação na grade ou selecionar a nota e…](https://ajuda.sankhya.com.br/hc/article_attachments/360095659434)

No rodapé da aba, pode-se visualizar os totalizadores das principais colunas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Maiores Parceiros

Nesta aba serão exibidos os parceiros que negociaram com o vendedor, e dentre eles quais são os que deram maior lucratividade, os que geraram  maior faturamento e margem de contribuição etc.

![Imagem 9: Nesta aba serão exibidos os parceiros que negociaram com o vendedor, e dentre eles quais são os que deram maior…](https://ajuda.sankhya.com.br/hc/article_attachments/360097958193)

As movimentações de entrada e saída serão apresentadas de forma distinta, marcando de amarelo as Entradas, e de branco as Saídas.

É possível gerar um gráfico para melhor análise das informações, bastando para isso pressionar o botão de gráfico ![Imagem 10: É possível gerar um gráfico para melhor análise das informações, bastando para isso pressionar o botão de gráfico .](https://ajuda.sankhya.com.br/hc/article_attachments/360095661594).

![Imagem 11: É possível gerar um gráfico para melhor análise das informações, bastando para isso pressionar o botão de gráfico .](https://ajuda.sankhya.com.br/hc/article_attachments/360095661874)

Cada barra do gráfico representa um parceiro que está sendo analisado. Pode-se limitar a visualização dos parceiros, através da configuração das **"Linhas no gráfico"**. As barras serão exibidas de acordo com a ordem dos parceiros na grade, ou seja, serão exibidos no gráfico os primeiros parceiros visualizados na grade, até o limite definido pelas linhas. Isto quando não houver múltipla seleção na grade, ou seja, não houver mais de um parceiro selecionado.

Pode-se selecionar na grade, parceiros específicos para visualização de seus resultados no gráfico. Esta seleção é feita segurando a tecla **"Ctrl"** do teclado e clicando-se sobre as linhas desejadas. Neste caso, o sistema irá desprezar a quantidade informada em **"Linhas no gráfico"** e analisará os parceiros selecionados na grade.

Em **"Analisar no gráfico"** pode-se definir o item a ser analisado, o qual poderá ser:

- Custo Reposição;
- Custo Fixo;
- Custo Variável;
- Lucro;
- Margem de Contribuição;
- Valor Médio;
- Valor Total.

No rodapé da aba, pode-se visualizar os totalizadores das principais colunas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Negociações Mensais

A aba Negociações Mensais agrupa todos os lançamentos mês a mês, apresentando os valores totais de cada um dos meses na grade.

A marcação **"Valor/Qtd. sem sinal"** faz com que os dados referentes aos campos **"Qtd.Neg."** e **"Vlr.Total"** de todas as negociações sejam apresentadas em valor absoluto, isto é, sem sinal de discriminação entre positivo e negativo. Esta marcação terá prevalência sobre as opções, **"Considerar Qtd. Negativa"** e **"Considerar Qtd. Positiva"** do painel opções.

![Imagem 12: A marcação "Valor/Qtd. sem sinal" faz com que os dados referentes aos campos "Qtd.Neg." e "Vlr.Total" de todas as…](https://ajuda.sankhya.com.br/hc/article_attachments/360095664054)

Os resultados também poderão ser visualizados de forma gráfica.

![Imagem 13: Os resultados também poderão ser visualizados de forma gráfica.](https://ajuda.sankhya.com.br/hc/article_attachments/360097962533)

O sistema exibirá o gráfico seguindo a ordem dos dados na grade. A quantidade de meses no gráfico será limitada pelo campo **"Qtd. de meses no gráfico"**, ou seja, se neste campo for informado o número **"3"**, serão exibidos no gráfico apenas os dois primeiros registros da grade.

Caso sejam selecionados mais de uma linha na grade (seleção esta realizada segurando o botão **"Ctrl"** do teclado, e clicando sobre as linhas desejadas), o campo **"Qtd. de meses no gráfico"** será ignorado e serã exibidos no gráfico os itens selecionados na grade.

As marcações **"Qtd."** e **"Valor"** alteram no gráfico a visualização dos dados, por valor ou quantidade negociada em cada mês.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba UF/Cidade/Bairro

Nesta aba tem-se a apresentação dos valores totais das negociações, por UF's, cidades e bairros em forma de "Cubo".

Este "Cubo" é uma ferramenta flexível, que permitirá a escolha dos campos ou critérios para efetuação das análises desejadas, além de prover um grande número de recursos para permitir que se visualize os resultados por diferentes aspectos, acrescentando ainda diversos indicadores sobre os dados selecionados, comparando-os em suas **"Linhas"** ou **"Colunas"**.

Para que você selecione os campos que irão compor o cubo, selecione-os na lista Campos Disponíveis e transporte-os para a área de preferência no cubo por meio da opção **"Adicionar à área de"** ou arrastando-os com o mouse.

![Imagem 14: Para que você selecione os campos que irão compor o cubo, selecione-os na lista Campos Disponíveis e transporte-os para…](https://ajuda.sankhya.com.br/hc/article_attachments/360095668014)

Os dados serão analisados de acordo com os campos filtrados e os resultados poderão ser visualizados por diferentes aspectos. Tudo dependerá da forma como forem combinados os campos de filtros.

Em cada uma das colunas é possível filtrar os dados que deverão ser apresentados no "Cubo", assim pode-se personalizar o filtro da forma que irá facilitar ao máximo a análise.

Pode-se também visualizar todos os dados em forma de grade, para isso pressiona-se o ícone **"Grade"** no lado superior esquerdo da tela.

[GIF animado: Imagem 15: Pode-se também visualizar todos os dados em forma de grade, para isso pressiona-se o ícone "Grade" no lado superior…](https://ajuda.sankhya.com.br/hc/article_attachments/360097966813)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Perfil de Parceiro

Nesta aba tem-se as negociações do vendedor de acordo com o perfil do parceiro, bem como a lucratividade, margem de contribuição etc.

![Imagem 16: Nesta aba tem-se as negociações do vendedor de acordo com o perfil do parceiro, bem como a lucratividade, margem de…](https://ajuda.sankhya.com.br/hc/article_attachments/360097966873)

Assim como na aba **"Negociações Mensais"**, esta aba permite que os resultados também sejam apresentados de forma gráfica.

Cada barra do gráfico representa um perfil que esta sendo analisado na grade. Pode-se limitar a visualização dos perfis, através da configuração das **"Linhas no gráfico"**. As barras serão mostradas de acordo com a ordem na grade, ou seja, serão exibidos no gráfico os primeiros perfis visualizados na grade, até o limite definido pelas linhas.

Pode-se também selecionar na grade perfis específicos para visualização de seus resultados. Neste caso, o sistema irá desprezar a quantidade informada em Linhas no gráfico e exibirá os dados de acordo com a quantidade de perfis selecionados na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Produtos

Nesta aba tem-se os produtos negociados pelo vendedor no período selecionado, permitindo-se analisar quais dentre eles, deram maior lucratividade, os que geraram maior faturamento e margem de contribuição etc. Nesta aba pode-se analisar produto a produto, por data de negociação, quantidade negociada, quantidade de notas, entre outros aspectos.

![Imagem 17: Nesta aba tem-se os produtos negociados pelo vendedor no período selecionado, permitindo-se analisar quais dentre eles,…](https://ajuda.sankhya.com.br/hc/article_attachments/360097966993)

No rodapé da aba tem-se os totalizadores das principais colunas.

Você também poderá **"Imprimir"** os dados da grade, assim como priorizar as colunas que se deseja visualizar pelo componente **"Configuração da Grade"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Grupo de Produtos

Essa aba totaliza os valores das negociações realizadas pelo vendedor por grupo de produtos, apresentando todos os dados da aba **"Produtos"** de forma sintetizada.

![Imagem 18: Essa aba totaliza os valores das negociações realizadas pelo vendedor por grupo de produtos, apresentando todos os…](https://ajuda.sankhya.com.br/hc/article_attachments/360095669574)

No rodapé da aba tem-se os totalizadores das principais colunas.

Pode-se também **"Imprimir"** os dados da grade, assim como priorizar as colunas que se deseja visualizar pelo componente **"Configuração da Grade"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)

## Aba Parceiros em Potencial

Esta aba apresenta os parceiros com potencial de venda, ou seja, os parceiros para os quais esse vendedor não vendeu, no período definido no filtro **"Período de negociação"**; independente do grupo de TOP selecionado.

![Imagem 19: Esta aba apresenta os parceiros com potencial de venda, ou seja, os parceiros para os quais esse vendedor não vendeu ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360095669614)

**Observação:** as abas **"Produtos"**, **"Grupo de Produtos"** e **"Parceiros em Potencial"**, não apresentam modo de exibição gráfico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109093-Ger%C3%AAncia-de-Vendedores#top)
