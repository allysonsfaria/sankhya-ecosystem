---
id: "360045118993"
titulo: "Acompanhamento da Produção "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:55:23Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Planejamento", "Acompanhamento da Produção", "br.com.sankhya.mgeprod.acompanhamentoproducao", "Acompanhamento da Produção  manual", "Estoque", "Produção", "Grades Planejamentos Etapas"]
---

# Acompanhamento da Produção 

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312789433879) Módulo: Produção > Rotinas
```

---

Esta tela possui duas grades, sendo a primeira com os planejamentos relacionados aos produtos selecionados, na qual são classificados inicialmente pelo código do produto e data da geração do planejamento; dessa forma, será apresentado as informações da etapa em que o planejamento se encontra. A segunda grade, detalha todas as etapas do planejamento selecionado na primeira grade.

Nesta tela o sistema mostrará as opções:

- [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#filtros);
- [Grade com os planejamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#gradecomosplanejamentos);
- [Grade com as etapas do planejamento selecionado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#gradecomasetapasdoplanejamentoselecionado);
- [Painel de Botões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es).

![Imagem 2: Painel de Botões .](https://ajuda.sankhya.com.br/hc/article_attachments/8821412181399)

## Filtros

**Empresa:** Informe neste campo a empresa para acompanhamento da produção. Este campo é obrigatório.

**Grupo ou Produto:** É obrigatório digitar Grupo de Produtos ou Produto. Caso informe os dois campos, o sistema irá filtrar por Grupo de Produtos.

**Grupo de Produto:** Indique neste campo o Grupo de produtos para seleção dos produtos que aparecerão na tela. No caso de um grupo sintético todos os produtos pertencentes a grupos abaixo na hierarquia deverão ser selecionados.

**Produto:** um grupo sintético todos os produtos pertencentes a grupos abaixo na hierarquia.

**Mostrar Planejamentos Concluídos:** Se essa marcação estiver desmarcado será apresentado apenas planejamentos não concluídos. Mas se estiver assinalada, exibirá todos os planejamentos independente de sua conclusão. Nos planejamentos concluídos o sistema mostra conteúdo nas colunas:

- Cód. Produto;
- Referência;
- Descr. Produto;
- Lote;
- Quantidade;
- Unidade.

As outras colunas aparecem em branco para diferenciar planejamentos finalizados de planejamentos não finalizados.

**Filtro Genérico:** Dados do cadastro de Produtos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#top)

## Grade com os planejamentos

Nas grade superior você poderá visualizar as seguintes colunas, com suas respectivas informações:

**Cód. Produto:** Será apresentado o Código do Produto.

**Referência:** Referência do Produto.

**Descr. Produto:** Descrição do Produto.

**Lote:** Lote do Planejamento.

**Quantidade:** Quantidade a ser produzida.

**Unidade:** Unidade padrão do Produto.

**Etapa Atual:** A Etapa Atual é indicada na tabela do planejamento. Os dados abaixo são obtidos da tabela filha de acordo com o código da etapa atual.  No caso do planejamento concluído os campos deste grupo deverão ficar vazios.

**Abrev. Etapa:** Abreviação da Etapa cadastrado no campo **"Abreviação"** no cadastro de [Estrutura de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611034). Caso seja uma etapa de **"CQL"** (CQL = 1) é acrescentado antes da abreviatura o texto CQL-, por exemplo: CQL-FBR.

**Data de Início:** Data de início da etapa.

**Número da OP:** Número único da Ordem de Produção quando esta etapa gerar produção.

**Prazo Planejado:** Prazo previsto (dias) para término da etapa de acordo com o início do planejamento. Deverá ser calculada a data prevista através da data de início do planejamento acrescida do Lead Time Total. O Prazo é a diferença entre a data prevista calculada e a data do servidor. Se estiver negativa será apresentada em **vermelho**, pois representa um atraso.  

**Previsão:** Prazo previsto (dias) para término da etapa de acordo com o seu início. A data prevista para término da etapa é calculada partindo da data de início da etapa adicionando o Lead Time da mesma. A Previsão é a diferença entre a data prevista calculada e a data do servidor. Se estiver negativa será apresentada em **vermelho**, pois representa um atraso.  

**Previsão Término:** Data prevista para a entrega calculada no item anterior.  Apresenta em branco se a Previsão for negativa.

**Erro Planejamento:** Diferença entre Previsão e Prazo Planejado. Quando negativo significa que a produção está antecipada em relação ao planejado. Ela estará em **vermelho** quando positiva.

**Insumos:** Esta coluna só será preenchida se a Etapa Atual for anterior à primeira que gera produção. Ela se refere ao número de insumos que faltam em estoque para o início da fabricação. Da mesma forma que a **"Geração da requisição de compra"**  levantará as quantidades necessárias das matérias-primas que serão utilizadas para a produção e comparadas com seu estoque (necessidade - estoque). Dessa forma, será obtido uma lista de matérias-primas faltantes (**"Código único"**).  As matérias-primas cujo estoque é suficiente são desprezadas.

**Observação:** deverá ser considerado apenas os produtos não pertencentes ao grupo de produtos configurado no parâmetro **"Grupo de Produtos das embalagens-PCPGREMBAL"** ou algum grupo de produto filho configurado no parâmetro. Será exibido em branco se for zerado; se for maior que zero, será apresentado na cor **vermelha**.

**Embalagens:** Da mesma que a coluna Insumos, será considerado apenas produtos pertencentes ao grupo de produtos configurado no parâmetro PCPGREMBAL ou algum grupo de produto filho configurado no parâmetro. É mostrado em branco se zerado e a na cor **amarelo** se for maior que zero.

**Insumos CQL:** Do mesmo modo que a coluna Insumos, esta coluna atuará. Porém, será considerado para o **"Estoque"** apenas quando estiver com **"status lote aprovado"**. Esta coluna representa quantos insumos faltam, se for levado em consideração o controle de qualidade das matérias-primas. É mostrado em branco se zerado e a na cor **vermelho** se maior que zero.

**Observações:** Com um duplo clique na linha abre-se pop-up para edição desta informação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#top)

## Grade com as etapas do planejamento selecionado

A grade de baixo se refere a todas as etapas existentes para o planejamento selecionado na grade acima. Ela possui as seguintes informações:

**Etapa:** Abreviação da Etapa cadastrado no campo Abreviação no cadastro de [Estrutura de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611034). Caso seja uma etapa de **"CQL"** (CQL = 1) é acrescentado antes da abreviatura o texto CQL-, exemplo: CQL-FBR.

**Data de Início:** Data de início da etapa.

**Data de finalização:** Data de finalização da etapa.

**Número da OP:** Número único da Ordem de Produção quando esta etapa gerar produção.

**Prazo Planejado:** Prazo previsto (dias) para término da etapa de acordo com o início do planejamento. É calculada a data prevista considerando a data de início do planejamento acrescida do Lead Time Total.  O Prazo é a diferença entre a data prevista calculada e a data do servidor.  Se for negativa será apresentada em **vermelho**, pois indica um atraso.

**Previsão:** Prazo previsto em dias para término da etapa baseado na data da análise.

**Previsão Término:** Data prevista para a entrega calculada no item anterior.  Não será apresentado nenhum dado se a Previsão for negativa.

**Erro Planejamento:** Diferença entre Previsão e Prazo. Quando negativa significa que a produção está antecipada em relação ao planejado. Apresentará em **vermelho** quando positiva.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#top)

## Painel de Botões

Na parte superior da tela você poderá acionar os seguintes botões:

[Avançar Etapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#avan%C3%A7aretapa)                         [Retroceder Etapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#retrocederetapa)                 [Gerar Produções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#gerarprodu%C3%A7%C3%B5es)     

[Insumos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#insumos)                                    [Cancelar Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#cancelarprodu%C3%A7%C3%A3o)              [Cancelar Planejamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#cancelarplanejamento)

**Avançar Etapa**

Só é possível utilizar este botão se a Etapa Atual, se for uma etapa que não gere produção e se ela for anterior à primeira que gera produção. Ao selecionar este botão será aberta um pop-up para informar a data de término da etapa; sendo que esta, deverá ser sempre inferior à data do servidor, inicializando com a data do servidor.

Esta data será gravada como data final da etapa. Caso não seja a última etapa do planejamento ela será gravada como data inicial da etapa seguinte; dessa forma, será alterado a etapa atual do planejamento.

Caso seja a última etapa, o sistema perguntará se tem certeza que deseja finalizar o planejamento, se a resposta for positiva atualizar o campo **"Concluído"** do planejamento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Retroceder Etapa**

Só é possível Retroceder Etapa se a etapa anterior à etapa atual for uma etapa que não gere produção e a etapa atual não seja a primeira do planejamento que gere produção.

Caso a etapa atual gere produção e não estiver na sua **"Etapa inicial"** (Módulo de Produção), isto é, processo produtivo já se iniciou, a rotina não poderá ser executada e o sistema irá apresentar a seguinte mensagem:

**"Etapa atual não pode ser a primeira a gerar produção"**

Caso a etapa atual seja com CQL = 1, isto é, processo produtivo já se iniciou, a rotina não poderá ser executada e será apresentado a mensagem:

**"Etapa anterior não pode gerar produção"**.

Ao confirmar a execução, a data de início da etapa e a data de final da etapa anterior serão limpas e a etapa atual do planejamento passara para a anterior.

Caso o planejamento seja um planejamento concluído o campo **"Concluído"** do planejamento retornará para **"N"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Gerar Produções**

O botão **"Gerar Produções"** executa rotina que irá gerar as Ordens de Produção no ERP.

A rotina será executada somente para planejamentos que estiverem na etapa anterior à primeira etapa que gere produção. Se o planejamento não estiver nesta etapa, o sistema exibirá a mensagem:

**"A próxima etapa deve ser o início da produção"**.

Serão geradas n Ordens de Produção relativas às Etapas existentes no planejamento (Apenas etapas de CQL = 0) que gerem produção, e seus números únicos serão guardados nos campos previstos para tal, na tabela de etapas do planejamento (O mesmo número se repete na etapa com CQL = 1).

A fórmula a ser utilizada na Geração das Produções será a mesma utilizada na geração dos pedidos de matéria-prima. O número do Lote (NUMNOTA) será o do planejamento. As produções não são geradas confirmadas.

A TOP de produção será a configurada na tela [Estrutura de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611034).

Ao final da geração, a Etapa do planejamento é atualizada com o código da primeira etapa existente que gera produção, e é gravada a data do servidor como a data de início desta primeira etapa. A etapa atual antes da geração, deverá ser finalizada gravando nesta a data de finalização igual a data do servidor.

A geração se inicia na última etapa do planejamento e terá como PA o próprio produto do planejamento. A geração continua com a etapa anterior até a primeira etapa, e os PA's de etapa serão as MP's da etapa seguinte que possuem fórmula principal.

As quantidades do PA da última etapa, são as próprias quantidades a serem produzidas, enquanto que das demais etapas é a quantidade a ser consumida de acordo com as fórmulas.

A estrutura da geração é uma estrutura em árvore tendo como raiz o Produto do planejamento. Os PA's dos níveis inferiores da árvore, pertencerão todos a uma única ordem de produção. Consulte o diagrama abaixo, para cada etapa será gerada um ordem de produção.

Etapa 4                Etapa 3                Etapa 2        

MP 1.1.1

MP 1.1                MP 1.1.2

MP 1.1.3

MP 1.2.1

PA                MP 1.2                MP 1.2.2

MP 1.3.1

MP 1.3                MP 1.3.2

MP 1.3.3

OP Etapa 4: PA = PA

OP Etapa 3: PA = MP 1.1, MP 1.2 e MP 1.3

OP Etapa 2: PA = MP 1.1.1, MP 1.1.2, MP 1.1.3, MP 1.2.1, MP 1.2.2, MP 1.3.1, MP 1.3.2, MP 1.3.3

Caso o número de níveis da fórmula seja maior que o número de etapas com geração de produção, o sistema não processa mostrando a mensagem:

**"Quantidade de etapas não pode ser maior que a estrutura de insumos da fórmula do produto"**

**Importante:** na geração da primeira produção que é a do produto do planejamento (o Produto Acabado), se o Produto Acabado desta produção possuir controle adicional de estoque por lote, seu controle será alimentado com o mesmo número do lote da produção.

Se alguma matéria-prima desta produção que terá explosão de fórmula, também possuir controle adicional de estoque por lote, esta terá seu controle alimentado pelo controle do Produto Acabado.

Para as produções seguintes, originadas da explosão de fórmulas de matérias-primas, a regra é praticamente a mesma, com a diferença que o Produto Acabado que possuir controle adicional de estoque por lote, terá seu controle alimentado pelo controle que recebeu na produção anterior em que era uma matéria-prima.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Insumos**

Ao clicar no botão Insumos, o sistema abre uma janela com 2 grades relacionadas com as matérias-primas faltantes para o início da produção da mesma forma que no cálculo da coluna CQL e Embalagens (será a junção das duas sem filtro do grupo de embalagens), de forma que só será aberta se a coluna CQL ou Embalagens possuir valor, caso contrário exibirá uma mensagem informando que não existem insumos faltantes para início da produção.

Caso o planejamento esteja em etapa diferente da primeira etapa que gera produção o sistema mostra a mensagem:

**"Etapa atual deve ser antes da primeira a gerar produção"**.

#### Grade com as Matérias-Primas faltantes

- **Código do produto.**
- **Descrição do produto.**
- **Unidade.**
- **Quantidade:** Quantidade necessária para a produção conforme cálculo.
- **Estoque:** Estoque Atual (considerando pesquisa de estoque personalizada e **"status lote aprovado"**).
- **Falta:** Quantidade – Estoque

#### Grade com Pedidos Pendentes da Matéria-Prima selecionada na grade superior

- Número do Pedido
- Código do Parceiro
- Nome do Parceiro
- Quantidade Negociada
- Quantidade Entregue
- Saldo
- Preço Unitário
- Desconto

Ao clicar duas vezes (duplo clique) em algum registro o sistema abre a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) posicionando no pedido selecionado.

**Nota:** no processo a fabricação poderá já ter sido iniciada sem que todos os insumos estejam em estoque, porém a partir do início da produção a análise de falta poderá ser distorcida em função do consumo das matérias-primas e sua baixa do estoque, além do fato que o início da produção sem estoque de todas as matérias-primas é uma decisão manual do gerente de produção estando este fato sobre controle.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Cancelar Produção**

Ao clicar no botão **"Cancelar Produção"** o sistema exclui as produções geradas no botão **"Gerar Produção"** de acordo com os números únicos registrados nas etapas. Esta opção só poderá ser executada se o planejamento estiver na primeira etapa do planejamento que gere produção e CQL = 0 e a Produção relativa a esta etapa estiver ainda na sua "**Etapa Inicial"** (Módulo de Produção), isto é, nada aconteceu no processo produtivo.

Caso o planejamento esteja na etapa inicial, o sistema mostra a mensagem:

**"Etapa atual deve ser a primeira a gerar produção"**

Caso o planejamento já tenha iniciado a produção e esteja fora da etapa inicial, o sistema também mostrará a mensagem acima.

Caso contrário, o sistema exclui a produção. Após a exclusão as informações de número único de todas as etapas acima são apagadas bem como a data de início da etapa atual voltando o planejamento à etapa anterior apagando a data de término desta.

Dependendo de for feito o bloqueio de exclusão no banco de dados previsto no módulo de produção os número únicos acima terão de ser memorizados e zerados para desfazer o vínculo que impedirá a exclusão.

Como por regra a primeira etapa do planejamento nunca poderá atualizar produção sempre existirá uma etapa anterior.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Cancelar Planejamento**

O cancelamento só poderá ser efetuado se o planejamento estiver na primeira etapa e nenhuma das requisições de compra geradas junto ao planejamento (tabela de ligação entre planejamento e requisições) estiverem faturadas, ou seja, estarem em condições de serem excluídas. No processo as requisições são excluídas e o planejamento também.

**Observação:** você deverá ter permissão de exclusão na tela.

Na realização do Cancelamento de Planejamento, a numeração do lote, poderá se comportar das seguintes maneiras:

Caso o produto do planejamento cancelado não pertença a um grupo de produção:

- Existindo outro planejamento para o produto com número de lote maior que o que está sendo cancelado, não será possível realizar o cancelamento, e uma mensagem de alerta será apresentada ao usuário.

**"Não foi possível excluir o planejamento, pois existem outros planejamentos para o produto do mesmo grupo de produção com número de lote maior ao do planejamento selecionado."**

Caso o produto do planejamento cancelado, pertença a um grupo de produção:

- Existindo outro planejamento de qualquer produto pertencente ao grupo de produção do produto, cujo número de lote seja maior que o que está sendo cancelado, não será permitido o cancelamento, e uma mensagem de alerta será exibida ao usuário.

**"Não foi possível excluir o planejamento, pois existem outros planejamentos para o produto do mesmo grupo de produção com número de lote maior ao do planejamento selecionado."**

- Existindo outro planejamento de qualquer produto pertencente ao grupo de produção do produto, onde o número de lote é igual ao que está sendo cancelado, o cancelamento será permitido.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Botão de Ação**

Ao lado do botão **"Cancelar Planejamento"**, é apresentado o botão de Ações, que é exibido apenas se uma ação for cadastrada na tela [Dicionário de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es)

**Observação/Quantidade**

Ao selecionar na grade superior um planejamento, que não tenha iniciado a produção, e dar um duplo clique com o mouse, o sistema abrirá uma janela para digitação da Quantidade e Observação do planejamento.

Após a digitação, clique no botão salvar, assim, o sistema altera a quantidade planejada (coluna Quantidade). O sistema modificará também a quantidade das Matérias Primas no botão Insumos e incluir o texto abaixo no campo Observação:

**"Qtde. Alterada - Qtde. Anterior: 400.0 | Usuário: 0 – SUP"**

**Nota:** caso exista alguma observação o sistema irá adicionar o texto acima na observação mantendo o texto atual.

Caso você selecione um planejamento que já tenha iniciado a produção, será apresentado a mensagem:

**"Produção já iniciada não pode ter quantidade alterada!"**

**Produção MGE:** Após gerar produção de um planejamento no Sankhya Om o processo de produção continua no MGE. O processo de produção no MGE já existe e não será testado por esta implementação. Foi utilizado os passos de confirmação no MGE para dar andamento no processo no Sankhya Om, mas não foi gerado o processo de Laudo e Finalização no MGE.

**Controle de Acesso:** Deverá existir controle de acesso que de forma a existir o acesso apenas para consulta, porém sem todas as ações da tela.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#paineldebot%C3%B5es) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993-Acompanhamento-da-Produ%C3%A7%C3%A3o#top)
