---
id: "360044599554"
titulo: "Lançamento de uma Ordem de Produção (OP)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-22T15:45:21Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Lançamento", "Configuração", "Dependências", "Ordem de Produção", "Centros de Trabalho", "Ordens de Produção", "Descartar", "Incluir OP", "Lançar Ordens", "LANCOPVERSANT", "Nova OP", "OPDESMONTESNOTA", "Produtos Acabados (PA)", "Reutilizar", "Terceiros", "Lançamento de uma Ordem de Produção (OP) manual", "Estoque", "Produção", "br.com.sankhya.producao.rotina.OrdemProducao", "Preencher campos obrigatórios", "Configurar estoque e concluir OP", "Criar nova Ordem de Produção"]
---

# Lançamento de uma Ordem de Produção (OP)

O lançamento manual de uma Ordem de Produção, se dá a partir do acionamento do botão ![Imagem 1: O lançamento manual de uma Ordem de Produção , se dá a partir do acionamento do botão "Nova OP" , localizado no alto da…](https://ajuda.sankhya.com.br/hc/article_attachments/16676175426327)**"Nova OP"**, localizado no alto da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o), quando esta é visualizada em **"Modo Grade"**.

Assim, além do lançamento de uma OP, trataremos neste artigo sobre os seguintes tópicos:

| [Lançamento de OP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#lan%C3%A7amentodeop) |  | [Grade Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#gradeordensdeprodu%C3%A7%C3%A3o) |
| --- | --- | --- |
| [Configurações de estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#configura%C3%A7%C3%B5esdeestoque) |  | [Facilitador do lançamento de OPs...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#facilitadordolan%C3%A7amentodeops...) |

![Imagem 2: Facilitador do lançamento de OPs...](https://ajuda.sankhya.com.br/hc/article_attachments/4416531121687)

**Observação:** este lançamento será possível se o usuário logado possuir em suas permissões de acesso, a marcação **"Incluir"** efetuada. Para isto, na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos), escolha o módulo **"Produção > Rotinas > Ordens de Produção"**, defina o usuário desejado e marque para o mesmo a opção Incluir. Deste modo, você poderá indicar quais usuários poderão realizar o lançamento manual de uma Ordem de Produção.

## Lançamento de OP

Ao acionar o botão ![Imagem 3: Ao acionar o botão Nova OP , será aberta a tela denominada "Lançamento de OP" , que nesta situação representa um…](https://ajuda.sankhya.com.br/hc/article_attachments/16676175426327) Nova OP, será aberta a tela denominada **"Lançamento de OP"**, que nesta situação representa um rascunho de lançamento que pode ou não ser salvo, visando uma possível utilização futura.

![Imagem 4: Ao acionar o botão Nova OP , será aberta a tela denominada "Lançamento de OP" , que nesta situação representa um…](https://ajuda.sankhya.com.br/hc/article_attachments/4416531569687)

Em seguida, será aberto o pop-up **"Incluir OP"**, no qual você deverá preencher os campos apresentados.

![Imagem 5: Em seguida, será aberto o pop-up "Incluir OP" , no qual você deverá preencher os campos apresentados .](https://ajuda.sankhya.com.br/hc/article_attachments/4416531666199)

Selecione o **"Tipo de Ordem"** a ser lançada de acordo com as opções:

- Produção;
- Desmonte;
- Reprocessamento/Reparo;
- Produção Conjunta.

**Observação:** ao selecionar a opção Produção Conjunta, o campo Produto será alterado para **"Grupo Co-produto"**. Este campo atua também como filtro para produtos e processos produtivos que poderão ser utilizados no lançamento.

A marcação **"Produção para Terceiro"** indica que esta Ordem de Produção será realizada para terceiros. Além disso, ao efetuar esta marcação será apresentado o campo **"Parceiro"**, para você indicar qual será o parceiro/terceiro destinatário desta produção.

O campo **"Planta de Produção"** tem o objetivo de definir de qual planta de produção as ordens a serem lançadas fazem parte. Ele também atua como filtro sobre os produtos e processos que poderão ser utilizados no lançamento.

Por meio do campo **"Produto"**, indique para qual Produto Acabado deseja lançar uma Ordem de Produção. Como mencionado anteriormente, seu filtro é influenciado pelos campos, Tipo de Ordem e Planta de Produção.

Nos campos referente ao **"Nro. Pedido/Sequencia"**, selecione o número do pedido ou nota de produção para o produto informado.

**Importante:** caso o sistema não encontre notas de produção para o produto e lote informados na ordem, temos o parâmetro **"OP de Desmonte s/ nota de Produção - OPDESMONTESNOTA"** (por padrão é apresentado desligado), que ao ser ativado, o sistema irá validar a existência de estoque para o Produto, Lote e Empresa da planta de manufatura.

Através do campo **"Processo"**, você poderá escolher o Processo Produtivo que deseja inserir nesta Ordem.

Informe o **"Tamanho de Lote"** e **"Nro de Lote"** respectivamente, do produto selecionado.

Após o preenchimento dos campos acima, basta clicar no botão ![Imagem 6: Após o preenchimento dos campos acima, basta clicar no botão "Incluir OP" . Uma vez efetuado o cadastro de uma nova OP…](https://ajuda.sankhya.com.br/hc/article_attachments/16676140130327) **"Incluir OP"**. Uma vez efetuado o cadastro de uma nova OP, é possível visualizá-la na grade **"Ordens de Produção (OP)"** da tela Lançamento de OP.

**Nota:** ao realizar o Lançamento de uma nova Ordem de Produção, caso o parâmetro **"Lançar OPs utilizando versões anteriores à última - LANCOPVERSANT"** esteja ativado, as versões antecedentes à última também serão apresentadas para escolha ao pesquisar por um Processo Produtivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#top)

## Grade Ordens de Produção

Na grade Ordens de Produção (OP) são apresentas as informações gerais da ordem: Sequência, Cód. Planta, Tipo de Ordem, Cód. Proc. Produtivo, Descr. Proc. Produtivo, Cód. Produto, Produto Acabado, Tam. Lote e Qtd. Produtos. 

![Imagem 7: Na grade Ordens de Produção (OP) são apresentas as informações gerais da ordem: Sequência, Cód. Planta, Tipo de Ordem,…](https://ajuda.sankhya.com.br/hc/article_attachments/4416579953047)

Ao acionar o botão ![Imagem 8: Ao acionar o botão "Próximo" , será apresentado o "Extrato de MPs" que tem o objetivo de disponibilizar um extrato de…](https://ajuda.sankhya.com.br/hc/article_attachments/16676140138263) **"Próximo"**, será apresentado o **"Extrato de MPs"** que tem o objetivo de disponibilizar um extrato de materiais que serão utilizados nas atividades padrão de uma Ordem de Produção no momento de seu lançamento. Assim, é possível identificar possíveis produtos com falta de estoque antes do lançamento da OP e você poderá visualizar as Matérias-Primas conforme o Produto Acabado a ser produzido, e seus correspondentes Materiais Alternativos.

![Imagem 9: Para saber mais sobre a tela Extrato de Materiais , acesse o referido artigo.](https://ajuda.sankhya.com.br/hc/article_attachments/16676175435799) Para saber mais sobre a tela [Extrato de Materiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais), acesse o referido artigo.

![Imagem 10: Para saber mais sobre a tela Extrato de Materiais , acesse o referido artigo.](https://ajuda.sankhya.com.br/hc/article_attachments/4416571337111)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#top)

## Configurações de estoque

Esta configuração será realizada através do botão ![Imagem 11: Esta configuração será realizada através do botão "Configurações de estoque" localizado ao lado superior direito da…](https://ajuda.sankhya.com.br/hc/article_attachments/16676175437975)**"Configurações de estoque"** localizado ao lado superior direito da tela. Ao acioná-lo, será aberto o pop-up:

![Imagem 12: Esta configuração será realizada através do botão "Configurações de estoque" localizado ao lado superior direito da…](https://ajuda.sankhya.com.br/hc/article_attachments/4416746416279)

No campo **"Empresa"**, informe os códigos das empresas que deseja agrupar estoques de produtos ligados a planta de manufatura.

Você pode criar um **"Filtro personalizado"** sobre o registro de estoque. Caso necessário, utilize o botão ![Imagem 13: Você pode criar um "Filtro personalizado" sobre o registro de estoque. Caso necessário, utilize o botão "Abrir…](https://ajuda.sankhya.com.br/hc/article_attachments/16676175441047) **"Abrir assistente"** para obter auxílio na construção do filtro.

Na definição de **"Locais"**, temos as seguintes opções:

- **Todos os locais:** Não será considerado local no filtro de estoque;
- **Todos, exceto com controle específico:** Serão considerados todos os locais no filtro, exceto aqueles com controle específico (locais com a marcação **"Val.Est. Independente"**);
- **Lista:** Será considerada a lista de locais especificada no campo **"Lista"** (abaixo deste campo, onde os locais deverão ser informados, separados por vírgula).

Acionando a marcação **"Desconsiderar estoque vencido"**, será desconsiderado no lançamento da Ordem de Produção, o estoque de MP's que possuem a data de validade menor que a data atual do sistema.

Esta configuração poderá ser utilizada para os produtos que foram configurados na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), seção [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), campo **"Controlar Por"** com a opção **"Número do lote"** selecionada e que possuem a **"Data de Validade"** preenchida na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaestoque).

Por fim, você efetiva o lançamento das OP's, ao clicar no botão ![Imagem 14: Por fim, você efetiva o lançamento das OP's , ao clicar no botão "Concluir" ou faz seu cancelamento a partir do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16950907024919)**"Concluir"** ou faz seu cancelamento a partir do botão ![Imagem 15: Por fim, você efetiva o lançamento das OP's , ao clicar no botão "Concluir" ou faz seu cancelamento a partir do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16676140149655) **"Cancelar"**, localizados no canto inferior direito da tela.

**Nota:** para o caso de cancelamento, se o lançamento foi configurado para ser reutilizável, este ficará salvo para uma próxima utilização.

**Observação:** ao realizar o lançamento de uma Ordem de Produção, caso você esteja efetuando tal processo em uma versão anterior à última, será exibida a seguinte mensagem:

**"Processo: X está desatualizado, a versão mais atual é: Y. Atualize antes de lançar ordens."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#top)

## Facilitador do lançamento de OPs de uma Operação Conjunta

Nesta tela, a operação conjunta poderá ser desencadeada após a opção Produção conjunta, ser selecionada (campo Tipo de Ordem), que por sua vez irá alterar o campo Produto para Grupo Co-produto.

Quando o botão ![Imagem 16: Quando o botão Incluir OP for clicado, será apresentado o pop-up com a mesma nomenclatura :](https://ajuda.sankhya.com.br/hc/article_attachments/16676140130327) Incluir OP for clicado, será apresentado o pop-up com a mesma nomenclatura:            

![Imagem 17: Quando o botão Incluir OP for clicado, será apresentado o pop-up com a mesma nomenclatura :](https://ajuda.sankhya.com.br/hc/article_attachments/4416755268631)

Logo, os campos **"Grupo Co-produto"**, **"MP Compartilhada"**, **"Qtd. de processamento"**, **"Unidade"**, **"Qtd de processamento (padrão)"**  e **"Un. Padrão"**, serão apresentados.

**Nota:** a quantidade que será proporcionado para os PAs do co-produto será a Qtd. de processamento (Un. padrão).

Ao clicar no botão Incluir OP e o rendimento total previsto dos itens do grupo de co-produto selecionado for diferente de 100%, será apresentado a mensagem de alerta:

**"O rendimento total previsto dos itens do grupo de co-produto selecionado é diferente de 100%."**

Caso na MP Compartilhada exista unidade alternativa, e o campo Unidade for alterado, a quantidade que será apresentada no campo Qtd. de processamento (Un. padrão) também será mudada.

Quando você confirmar a inclusão das OPs conforme o campo Qtd. de processamento (Un. padrão), serão incluídos OPs para os itens do [Grupo de Co-produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107313), sendo assim, será realizado a quantidade equivalente conforme será exibido na tabela **"Rendimento Previsto (%)"**.

![Imagem 18: Quando você confirmar a inclusão das OPs conforme o campo Qtd. de processamento (Un. padrão) , serão incluídos OPs para…](https://ajuda.sankhya.com.br/hc/article_attachments/4416755332887)

Quando o Co-produto for salvo, você poderá alterar a quantidade de processamento Co-produto por meio do botão ![Imagem 19: Quando o Co-produto for salvo, você poderá alterar a quantidade de processamento Co-produto por meio do botão "Alterar…](https://ajuda.sankhya.com.br/hc/article_attachments/16676175450775) **"Alterar Qtd. Processamento Co-produto"** , no entanto, este só aparecerá quando o item da OP for Produção Conjunta, ao clicar neste, o pop-up surgirá novamente para edição.

Porém, na edição deste irá constar a marcação **"Reproporcionar qtd. entre Co-produções"**, quando ligado, as OPs de lançamento serão ajustadas de acordo com a Qtd. de processamento (Un. padrão). Quando não habilitada, somente a Qtd. processamento (Un. padrão) será alterada, sendo que, irá como sugestão para a Qtd. da MP na tela [Apontamento de Produções Conjuntas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118753-Apontamento-de-Produ%C3%A7%C3%B5es-Conjuntas) e não será ajustado para as OPs do lançamento.

Se você clicar no botão ![Imagem 20: Se você clicar no botão "Remover" , o sistema mostrará a mensagem de confirmação:](https://ajuda.sankhya.com.br/guide-media/01H7GBG8NP6RQ9SC3PR3PR185B) **"Remover"**, o sistema mostrará a mensagem de confirmação:

**"Deseja remover todas as OPs que fazem parte desta produção conjunta?"**

Ao confirmar, o sistema irá remover todas as OPs com a sequência de produção conjunta;

Caso seja selecione o **"Não"**, o sistema excluirá somente a que foi selecionada;

E o botão Cancelar não irá remover nenhuma OP.

Se houver lançamento de OP específico que você queira filtrar, você poderá buscar pelo seu número único no campo **"Nro. OP Conjunta"**.

Na tela Apontamento de Produções Conjuntas você pode incluir OPs de Produção Conjunta por meio do botão ![Imagem 21: Na tela Apontamento de Produções Conjuntas você pode incluir OPs de Produção Conjunta por meio do botão "Incluir OP" .…](https://ajuda.sankhya.com.br/hc/article_attachments/16676175463063) **"Incluir OP"**. Assim, abrirá o pop up:

![Imagem 22: Na tela Apontamento de Produções Conjuntas você pode incluir OPs de Produção Conjunta por meio do botão "Incluir OP" .…](https://ajuda.sankhya.com.br/hc/article_attachments/4416742805271)

No campo **"Tipo"** terá as opções **"Produção Conjunta"** ou **"Ordem Produção"**, de acordo com o que for selecionado o nome do campo abaixo deste irá variar entre **"Nro. Produção Conjunta"** e **"Ordem de Produção (OP)"**.

Após a inclusão, as OPs lançadas serão apresentadas da seguinte maneira:

![Imagem 23: Após a inclusão, as OPs lançadas serão apresentadas da seguinte maneira:](https://ajuda.sankhya.com.br/hc/article_attachments/4416757386647)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP#top)
