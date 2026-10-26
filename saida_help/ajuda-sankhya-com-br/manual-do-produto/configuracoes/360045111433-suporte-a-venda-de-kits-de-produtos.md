---
id: "360045111433"
titulo: "Suporte a Venda de Kits de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:48Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Componentes", "Estoque", "EDITMPEXPLOD", "EDITMPSOMAIPI", "EXPLODEKITVAR", "Matérias-primas", "Suporte a Venda de Kits de Produtos", "Suporte a Venda de Kits de Produtos manual", "Configuração e Venda de Kits de Produtos", "MGE-Produção"]
---

# Suporte a Venda de Kits de Produtos

Para habilitar o suporte a kit na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) no **Sankhya Om**, é necessário primeiramente ativar o parâmetro **"Habilitar o suporte a kit no SankhyaW? - HABSUPORTEKITSW"**.

Existem duas formas principais de montar kits para vendê-los posteriormente na Central de Vendas:

1. Pela própria tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) ou então pelo módulo de produção, ainda inexistente no Sankhya Om;
2. Ou podemos criar os KIT's utilizando o modulo de produção do MGE, ou seja, o MGE Produção em integração com o Sankhya Om.

![Imagem 1: Atualmente, o sistema não realiza transferências de produtos Kit, pois esta se trata de uma operação que executa a…](https://ajuda.sankhya.com.br/hc/article_attachments/16749542374295) Atualmente, o sistema não realiza transferências de produtos Kit, pois esta se trata de uma operação que executa a explosão do Kit.

Além disso, não existe nos fontes relacionados à rotina de kit (Kit Convencional e Kit Independente) alguma rotina que atualize a coluna **"ATUALESTTERC"**. Durante o processo de explosão dos componentes, a aplicação não está preparada para atualizar as colunas relativas à atualização de estoque de terceiros, sendo assim, essa é uma situação não prevista pela aplicação (Kit cujos componentes atualizam estoque de terceiros).

| Tópicos deste artigo |
| --- |
| [Kits Montados pelo Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#Kitsmontadospelocadastrodeprodutos) |
| [Kits Produzidos pelo Módulo MGE-Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#Kitsproduzidospelom%C3%B3dulomgeprodu%C3%A7%C3%A3o) |
| [Venda de componentes fora do Kit](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#Vendadecomponentesforadokit) |
| [Venda de Kit's com componentes sem estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#Vendadekit'scomcomponentessemestoque) |
| [Parâmetros utilizados nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#Par%C3%A2metrosutilizadosnestarotina) |

---

## Kits Montados pelo Cadastro de Produtos

Inicialmente, configure os parâmetros abaixo da seguinte maneira:

- **Tem mat. prima na central? - TEMMPVENDA** = Ativado
- **Editar MP ligadas - EDITMP =** Produto
- **Explode Componentes na aba de MP? - EDITMPEXPLOD** = Ativado
- **Apresentar apenas MP da aba Componentes? - EDITMPVALCOMP** = Ativado

Para o tipo de KIT montado, na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) você deverá selecionar ou criar o produto que representará o KIT. Além disso, na aba [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abacomponentes) serão adicionados os outros produtos que compõem esse KIT.

![Imagem 2: Para o tipo de KIT montado, na tela Cadastro de Produtos você deverá selecionar ou criar o produto que representará o…](https://ajuda.sankhya.com.br/hc/article_attachments/4409115526679)

Ao abrir o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), por exemplo, e realizar o lançamento de uma nota de venda, nota-se que com o parâmetro TEMMPVENDA ligado será apresentada a grade de **"Matéria- prima"**. É nessa grade que serão mostrados os produtos que compõe o KIT, caso o parâmetro EDITMPEXPLOD esteja ligado.

**Observação:** lembre-se que ao informar um produto tipo kit (configuração realizada na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacomponentes)), ao preencher o campo Quantidade na grade de itens da Central de Vendas, o sistema registrará até no máximo 9 casas decimais.

**Nota:** não é possível utilizar o KIT sem habilitar o parâmetro TEMMPVENDA. Quando o referido parâmetro se encontrar desligado a grade de Matéria-prima não será exibida, qualquer recálculo de preço fará com que o sistema transforme as matérias-primas em componentes. Além disso, o recálculo de ICMS do KIT não será efetuado.

![Imagem 3: Nota: não é possível utilizar o KIT sem habilitar o parâmetro TEMMPVENDA . Quando o referido parâmetro se encontrar…](https://ajuda.sankhya.com.br/hc/article_attachments/4409100017303)

Ao adicionar um produto acabado na grade de itens superior e acionar o botão **"Outras Opções..."**, opção **"Revenda (por Fórmula)..."**, eles serão apresentados no pop-up  **"Venda por Fórmula de Composição"**:

![Imagem 4: Ao adicionar um produto acabado na grade de itens superior e acionar o botão "Outras Opções..." , opção "Revenda (por…](https://ajuda.sankhya.com.br/hc/article_attachments/4409099996311)

Para que esta opção seja apresentada, é necessário que a marcação da opção **"Atualização On-Line"** esteja efetuada, em **"Outras opções"** na parte dos itens. Essa tela permite a alteração das quantidades das matérias-primas, desde que essas alterações respeitem a fórmula de composição do KIT. Considere o seguinte exemplo:

Suponhamos que o produto "KIT Motor de arranque" seja composto por:

- 1 Bobina de Ignição;
- 1 Correia Alternada;
- Impulsor M. Partida.

O total desta fórmula de composição são 3 unidades, logo, no pop-up Venda por Fórmula de Composição, a quantidade dos itens poderá ser alterada desde que a soma dos itens não ultrapasse as 3 unidades da fórmula, podendo ser menor que 3.

Na formação de KIT, o campo **"Usado como"** deve estar igual a **"Revenda (por fórmula)"** apenas para o produto kit. Para os componentes do kit, este campo deve ser diferente de Revenda (por fórmula).

![Imagem 5: Na formação de KIT, o campo "Usado como" deve estar igual a "Revenda (por fórmula)" apenas para o produto kit. Para os…](https://ajuda.sankhya.com.br/hc/article_attachments/4409115655831)

**Observações:**

- O pop-up Venda por Fórmula de Composição só aparecerá para produtos com o tipo de uso igual a Revenda (por fórmula) (campo Usado Como, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-)).
- Caso o parâmetro **"Soma preço das MPs ao produto principal? - EDITMPSOMPRECO"** esteja ligado, o pop-up mencionado anteriormente não será exibido.

Caso os parâmetros **"Soma dos custo das MPs no produto principal? - EDITMPSOMCUSTO"**, **"Soma preço das MPs Extras ao produto principal? - EDITMPSOMAEXT"** e **"Soma preço das MPs ao produto principal? - EDITMPSOMPRECO"**, estejam desligados e a edição das matérias-primas for permitida, ao alterar a quantidade de uma matéria-prima, o produto principal não será atualizado. Isso não é erro, é comportamento. Para que as alterações nas matérias primas sejam refletidas no produto principal, um dos parâmetros citados acima deve estar ligado.

**Nota:**quando o parâmetro EDITMPEXPLOD estiver desligado, o valor do Kit será distribuído entre os componentes, sendo assim é feita uma regra de 3 para tal distribuição. Por exemplo, se eu tenho um produto que possui componentes. Se eu não somar o preço dos componentes, então irei distribuir o preço do produto entre os componentes. No Kit o conceito é sempre o valor do produto acabado igual a somatória das MPs.

**Importante:** no lançamento de uma nota de venda, quando habilitado o parâmetro **"Buscar local padrão para componente de Kit? - 'BUSLOCPADCOPKIT"**, o sistema considerará o Local Padrão para constituir os componentes do kit. Diante disto, caso o produto principal (pai) usar Local, o sistema seguirá a seguinte ordem:

1. Primeiramente, se no campo **"Inteiro"** configurado no parâmetro **"Local de destino de MP para transf. de Kit - LOCDESTMPKIT"** for registrado um valor diferente de -1 e o campo "Tipo de movimento" não constar a opção **"T-Transferência"** ([Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)) o sistema utilizará o local mencionado na chave de parâmetro LOCDESTMPKIT.

**Nota:** quando utilizado o valor -1 mencionado anteriormente, não será utilizado o local.

2. Caso não utilize o local informado no parâmetro acima, será considerada a informação inserida no campo **"Local"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abacomponentes).

3. Ainda não sendo encontrado, o sistema buscará o menor local com estoque se o parâmetro **"Informa menor local de armazenagem com estoque - INFMINLOC"** estiver ligado.

4. Caso contrário, o sistema observará o valor informado no campo **"Inteiro"** das configurações do parâmetro **"Local Padrão para Pedidos e Notas - LOCALPADRAO"** desde que este seja diferente de 0.

5. Por fim, se o parâmetro **"Buscar local padrão para componente de Kit? -BUSLOCPADCOPKIT"** estiver habilitado, o sistema considerará o local padrão da empresa ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa)).

**Nota:** quando o produto principal (pai) não usar Local, as matérias-primas (MP's) se inicializarão com Local Zero.

**Importante:**com os parâmetros EDITMPEXPLOD ligado e EDITMPSOMPRECO desligado, o sistema permitirá fazer a digitação do valor no produto principal. Quando ambos os parâmetros estiverem ligados, fazem com que o preço de venda do kit seja igual à soma dos preços de vendas dos componentes.

O parâmetro **"Soma ICMS das MPs (Art. 42 do RICMS/2002-MG) - EDITMPSOMAICMS"** realiza a subtração do ICMS da MP do ICMS total.

**Observação:** diferentemente do MGE este parâmetro vem padronizado como desligado, e no Sankhya Om como ligado.

Para fazer com que o preço do kit seja diferente da soma dos componentes, é preciso criar uma tabela de preços à parte e vinculá-la ao kit. Considere o seguinte exemplo:

- **Tabela de preços 01 ->** Componente 1, componente 2 e componente 3
- **Tabela de preços 02** **->** Kit

Neste caso, os parâmetros devem ser configurados como:

- HABSUPORTEKITSW e EDITMPEXPLOD: ligados
- EDITMPSOMCUSTO, EDITMPSOMPRECO e EDITMPSOMAEXT: desligados

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#top)

## Kits Produzidos pelo Módulo MGE-Produção

Configure primeiramente os parâmetros:

- **"Tem mat. prima na central? - TEMMPVENDA"** = Ativado
- **"Editar MP ligadas - EDITMP" =**Produto
- **"Explode Componentes na aba de MP? - EDITMPEXPLOD"**= Ativado
- **"Apresentar apenas MP da aba Componentes? - EDITMPVALCOMP"**= Ativado

Para o tipo de venda KIT produzido, será necessário a produção do KIT na tela [Fórmula de Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto) do módulo de Produção do MGE.

Assim, selecione ou crie o produto que será produzido:

![Imagem 6: Assim, selecione ou crie o produto que será produzido:](https://ajuda.sankhya.com.br/hc/article_attachments/9532053799447)

No painel de **"Etapas..."**, defina as etapas, pré-cadastradas no menu **"Arquivo/Etapas de Produção"**.

![Imagem 7: No painel de "Etapas..." , defina as etapas, pré-cadastradas no menu " Arquivo/Etapas de Produção" .](https://ajuda.sankhya.com.br/hc/article_attachments/9532038546583)

No painel de **"Matérias Primas/Insumos..."**, defina as matérias-primas que compõe esse produto produzido.

![Imagem 8: No painel de "Matérias Primas/Insumos..." , defina as matérias-primas que compõe esse produto produzido.](https://ajuda.sankhya.com.br/hc/article_attachments/9532042338455)

Com a fórmula de composição do produto cadastrada, você deverá acessar a tela **"Rotinas/Produção"** e cadastrar uma nova produção, informando **"Empresa"**, **"Lote"**, **"TOP"** e outros campos obrigatórios:

![Imagem 9: Com a fórmula de composição do produto cadastrada, você deverá acessar a tela " Rotinas/Produção" e cadastrar uma nova…](https://ajuda.sankhya.com.br/hc/article_attachments/9532080283415)

Na grade **"Produto"**, selecione o produto utilizado para se cadastrar a fórmula de composição do produto (realizado no passo anterior) e defina a quantidade e outros campos que desejar:

![Imagem 10: Na grade " Produto" , selecione o produto utilizado para se cadastrar a fórmula de composição do produto (realizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/9532134803351)

Na grade **"Matéria-prima"**, após a seleção do produto, será automaticamente apresentada as matérias-primas cadastradas na fórmula de composição do produto:

![Imagem 11: Na grade " Matéria-prima" , após a seleção do produto, será automaticamente apresentada as matérias-primas cadastradas…](https://ajuda.sankhya.com.br/hc/article_attachments/9532176852119)

Em seguida, clique no botão **"Confirmar"**, para que assim o MGE realize a produção.

Agora, já pelo Sankhya Om, ao abrir o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), por exemplo, e realizar o lançamento de uma nota de venda, nota-se que com o parâmetro TEMMPVENDA ligado será apresentada a grade de **"Matéria-prima"**. É nessa grade que serão mostrados os produtos que compõe o KIT, caso o parâmetro EDITMPEXPLOD esteja ligado.

Ao adicionar um produto acabado na grade de itens superior, se o produto for produzido, o sistema não irá mostrar o pop-up **"Venda por Fórmula de Composição"**.

O interessante ao se trabalhar com produto KIT produzido é que se o KIT tiver controle por lote e confirmamos uma nota/pedido, se o parâmetro **"Subst. Tributária embutida no preço? - STEMBUT"** estiver ligado, será feito um novo recálculo das quantidades e valores das matérias primas considerando a nota/pedido de produção daquele KIT, ou seja, o sistema irá ignorar as modificações feitas na grade de Matéria-prima da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), e considerará somente o que foi definido na fórmula de composição do produto, no MGE Produção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#top)

## Venda de componentes fora do Kit

Caso você queira configurar o sistema de forma que consiga vender um componente separado do kit, assinale a marcação **"Aceitar venda fora do Kit"**, da aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abavenda) localizada na tela de [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113).

![Imagem 12: Caso você queira configurar o sistema de forma que consiga vender um componente separado do kit, assinale a marcação…](https://ajuda.sankhya.com.br/hc/article_attachments/4409112998039)

Se o campo estiver marcado, ao lançar um pedido ou uma nota de venda com um produto que seja componente de outro e ele esteja sendo vendido separadamente o sistema irá permitir.

Caso o campo esteja desmarcado e você tente realizar um procedimento conforme descrito anteriormente, o sistema irá verificar se no parâmetro **"Tops para venda individual de componentes - TOPVENCOMPINDIV"** a TOP deste tipo de movimento está relacionada. Se sim, ele também conseguirá vender separadamente um produto que seja componente de outro. Se não estiver nem marcado e nem relacionado na TOP, esta venda não será permitida e a seguinte mensagem será apresentada:

**"Componente não pode ser vendido separadamente."**

Nesse processo também poderá ser vendida uma série avariada, e o sistema irá preencher o campo **"% Desconto"** (conforme configuração do mesmo na tela de [Registro de avarias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120333)). Se o produto utilizar Local, o sistema irá carregar o local correto e irá bloquear o campo **"Local origem"**.

Produtos avariados não respeitam a marcação do Cadastro de Produtos e podem ser vendidos separadamente independentemente da configuração do produto ou do parâmetro.

Para maiores informações sobre [Controle de Produtos com Número de Série Global](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597254-Controle-de-Produtos-com-N%C3%BAmero-de-S%C3%A9rie-Global), clique no link.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#top)

## Venda de Kit's com componentes sem estoque

Quando se trabalha com controle de estoque em componentes de um Kit, podem acontecer casos em que no momento da venda, algum componente deste Kit não tenha estoque suficiente para ser negociado. Visando solucionar este tipo de situação, o Sankhya Om conta com a possibilidade de selecionar os componentes de outros locais ou controles, para um componente da fórmula que não possua estoque no local ou controle que estão sendo negociados.

No momento da venda de um Kit, caso exista um componente com estoque insuficiente, mas exista estoque para este componente em outro local ou controle, que seja suficiente para suprir a quantidade que está sendo negociada, será aberto o pop-up **"Estoques disponíveis para o KIT":**

![Imagem 13: No momento da venda de um Kit, caso exista um componente com estoque insuficiente, mas exista estoque para este…](https://ajuda.sankhya.com.br/hc/article_attachments/4409102277911)

Na grade superior, são apresentados os componentes da fórmula que compõem o Kit que não possuem estoque suficiente. Nesta grade, os campos **"Qtd. Necessária"** e **"Qtd. Pendente"** inicialmente são apresentados com o mesmo valor, porém a medida que as quantidades são informadas na grade inferior, o campo Qtd. Pendente será subtraído até alcançar o valor zero. No campo **"Status"** tem-se a indicação de quando existem componentes que não tiveram suas quantidades necessárias informadas na cor **vermelha**, e quando foram totalmente informadas serão apresentadas na cor **verde**.

Na grade inferior, são exibidos os componentes de outros locais ou controles que possuem estoque suficiente (parcial ou não) para substituir o componente sem estoque.

Para o componente na grade inferior que possuir o mesmo controle do item sem estoque, o pop-up será exibido pois, apesar de não possuir a quantidade de estoque necessária, apresenta um estoque parcial que pode ser utilizado para compor o Kit. Este pop-up apenas não será exibido, se a soma de todos os estoques dos itens alternativos não forem maiores ou iguais a quantidade necessária.

Na tela [Fórmula de Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto), aba [Etapas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#abaetapas), na grade inferior é necessário que a marcação **"Permite variação de controle"** esteja assinalada para que sejam apresentados no pop-up Estoques disponíveis para o KIT, grade **"Estoque disponível"**  os itens com controles diferentes do componente da fórmula; caso esteja desmarcada, será realizada apenas a consulta no estoque por itens de mesmo estoque.

![Imagem 14: Na tela Fórmula de Composição do Produto , aba Etapas , na grade inferior é necessário que a marcação "Permite variação…](https://ajuda.sankhya.com.br/hc/article_attachments/4409112882711)

Não é permitido incluir os itens na nota, sem que todas as quantidades necessárias tenham sido informadas de todos os itens. Além disso, não é permitido utilizar um valor maior que o estoque disponível, assim como não é possível informar uma quantidade acima da quantidade necessária pelo componente.

**Observação:** é necessário que o parâmetro **"Explode Componentes na aba de MP? - EDITMPEXPLOD"** esteja habilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#top)

## Parâmetros utilizados nesta rotina

**Tem mat.prima na central atendimento ao Cliente? - TEMMPVENDA:** quando ligado, e o produto principal tiver componentes, ao gravar o item principal os itens do componente vão para a TGFITE e para a aba **"Matéria-Prima"**. Se desligado não será possível utilizar o kit, além disso, a grade de matéria-prima não será exibida; qualquer recálculo de preço fará com que o sistema transforme as matérias primas em componentes e o recálculo de ICMS do KIT não será efetuado.

**Editar MP ligadas - EDITMP:** quando for configurado para **"Não editar"**, não será permitido inserções na parte de Matéria-prima. Caso seja configurado para **"Produto"** ou **"Serviço"**, será permitido inserções na parte de Matéria-prima.

A respeito dos parâmetros **"Registra a Soma dos custos das MPs no produto principal - EDITMPSOMCUSTO"**, **"Soma preço das MPs Extras ao produto principal - EDITMPSOMAEXT"**, **"Soma preço das MPs ao produto principal - EDITMPSOMPRECO"**, **"Explode Componentes na aba de MP - EDITMPEXPLOD"**, se for um produto que tem fórmula no módulo de produção ou componentes no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), ao inserir o produto principal os itens componentes do produto principal irão para a grade Matéria-prima.

**Explodir componentes somente para KIT - EXPLODEKITVAR:** quando estiver ativado, serão explodidos na central, apenas os componentes que não forem matéria-prima. Na inclusão de um produto que possua matéria prima, essas MP's não serão exibidas, apenas os componentes de kit. Para que este procedimento funcione, é necessário que o parâmetro **"Explode Componentes na aba de MP - EDITMPEXPLOD"** também esteja ativado.

**Soma IPI das MPs ao valor total da nota. - EDITMPSOMAIPI:** quando habilitado, calcula o valor total do IPI dos componentes do Kit, e os soma diretamente ao valor total da nota.

Para que o sistema imprima o Kit nas Notas Fiscais (considerando também geração do XML e DANFE), no Cadastro de [Tipos de Operação- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114#abaimpresso), o campo **"Kit/Componentes - Impressão e Livro Fiscal"** deve estar devidamente configurado.

**Inibir exibição de MP nos movimentos de vendas? - INIBESELECUSOPD:** ao habilitar este parâmetro, não serão exibidos os produtos componentes (matérias-primas de um produto KIT) no lançamento de um pedido/nota, ou seja, não serão exibidas as MPs explodidas se o campo **"Usado como"**, estiver configurado com a opção **"Revenda (por Fórmula)"** no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-). Por exemplo:

- Produto A = Produto KIT
- Produtos B e C = Matérias-primas do produto A.

Quando o pedido/nota for lançado com o Produto A, os Produtos B e C não serão exibidos se o parâmetro estiver habilitado. Logo, se o pedido de venda for faturado as matérias-primas (produtos componentes) deste pedido não serão levadas para a nota de venda.

**Soma preço das MPs Extras ao produto principal? - EDITMPSOMAEXT:** quando estiver habilitado, ao faturar o pedido de venda os componentes do Kit serão incluídos juntamente aos produtos na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), grade **"Matéria-prima"**. Além disso, é importante destacar que, com este parâmetro ativado, o sistema não calculará o desconto automático dos componentes ao explodi-los.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos#top)
