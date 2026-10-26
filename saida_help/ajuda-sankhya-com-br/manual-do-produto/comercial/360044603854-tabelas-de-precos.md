---
id: "360044603854"
titulo: "Tabelas de Preços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:24:58Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Fast Service", "PRECOPORCONT", "Destino", "Origem", "Moeda", "Preço", "Conta Corrente Flex", "Dt. vigor", "Flex", "PRECOPORLOC", "Tabela de Origem", "Tabelas de Preços", "USATABALTEMP", "Variação", "br.com.sankhya.com.cad.tabeladepreco", "Tabelas de Preços manual", "Funcionalidades", "Comercial", "Tabelas de Preço"]
---

# Tabelas de Preços

```
 Módulo: Comercial > Arquivo
```

---

Nesta tela, você pode realizar o cadastro de tabelas de preço que serão utilizadas em diversas rotinas do sistema. Assim, confira por meio dos links abaixo sobre as particularidades dessa tela:

[Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#painelprincipal)                                                   [Aba Histórico de Atualizações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#hist%C3%B3ricodeatualiza%C3%A7%C3%B5es)

[Aba Regras/Exceções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#abaregrasexcees)                                          [Botão Copiar Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#botocopiartabela)

[Campos Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#camposadicionais)                                              [Tabelas de Preços Alternativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#tabelasdepreosalternativos)

[Como vincular a Tabela de Preço a um cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#ComovincularTabelasdePre%C3%A7oaumcadastro)

## Painel Principal

![Imagem 1: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/1500019681981)

Primeiramente, realize as configurações dos campos abaixo:

No campo **"Código Tabela"** você deverá informar o número da nova tabela de preço manualmente. Considera-se que o preenchimento deste campo é obrigatório.

A marcação **"Ativo"** determinará se a Tabela de Preço encontra-se ativa ou inativa.

**Importante:** atente-se para o ato de **"Desativar"** uma tabela de preços, pois não será possível inativar apenas uma versão da tabela. Quando uma tabela de preços é inativada, a empresa que utilizava da mesma, ficará sem tabela.

**Nota:** caso você deseje inativar uma Tabela de Preço que não é mais válida e está sendo utilizada como origem para uma outra tabela, basta desabilitar a marcação Ativo. Assim, o sistema questionará:

**"A tabela de preço: X está sendo referenciada pela tabela Y, Deseja realmente inativá-la?"**. Caso você escolha **"Sim"**, a tabela atual será inativada; optando por **"Não"**, nenhuma ação será realizada.

Informe no campo **"Nome Tabela de Preço"** a descrição da tabela.

Quando se trabalha com operações envolvendo moedas estrangeiras, informa-se no campo **"Moeda (Tabela de Preço)"** a moeda estrangeira da tabela em questão. As moedas apresentadas para escolha neste campo, deverão ser previamente cadastradas na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas) e serão as do tipo **"Valor"**.

Quando a marcação **"Integrar com EConect:"** for realizada, implica que a tabela de preços em questão realizará integração com o EConect.

**Nota:** ao realizar a marcação anterior, o campo **"Observação"** poderá ser preenchido com um máximo de 20 caracteres.

Além disto, a marcação Integrar com EConect não poderá ser realizada quando a tabela em questão for a **"Tabela 0"**.

Na Configuração dos Produtos da Tabela de Preços (aba **"Exceções"**), o único registro aceito pela integração no campo **"Tipo"** será a opção **"Valor"**.

**Observação:** este campo está destinado à digitação de informações adicionais pertinentes a tabela de preços em questão.

O campo **"Casas decimais"**, será habilitado através do parâmetro **"Utiliza Decimais na tabela de Preço? - USADECPREC"**. Neste campo, você deverá indicar a quantidade de casas decimais, utilizadas pela tabela de preço, sendo que, os valores aceitáveis são 0, 1, 2, 3 ou 4.

**Nota:** na grade de produtos desta tela o preço será arredondado conforme a quantidade de casas decimais informada neste campo.

**Observação:** o Fast Service validará o preço, utilizando o menor número de casas decimais que encontrar, seja no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), ou nas Tabelas de Preços, como exemplo:

- O produto tem 4 casas decimais e na tabela está informado para usar 3 casas; assim,o Fast Service apresentará o preço com 3 casas;
- O produto possui 2 casas decimais e na tabela está informado para usar 2 casas; desta forma, o Fast Service apresentará o preço do produto com 2 casas;

**Importante:** para trabalhar com Fast Service, a Tabela de Preço utilizada deverá ter no máximo 3 casas decimais.

**Nota:** a Central validará a Tabela de Preço usada na negociação e a quantidade de casas decimais da tabela não será afetada.

O campo **"Região"**poderá ser utilizado para indicar uma região para a tabela de preço.

Informe no campo **"Perfil"** um perfil, se esta tabela for utilizada por um perfil em específico.

Referente ao campo **"Tabela p/ Flex"**, deverá conter o código da tabela a ser utilizada como tabela do **"Preço Base do Flex"**. Se não houver tabela informada neste campo, o sistema utilizará a **"Tabela da Negociação"**, conforme o parâmetro **"Tabela de Preços por** **-** **TIPTABPRECOS"**; caso não haja a informação no parâmetro, o processo [Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388733-Saldo-Flex) não funcionará.

**Importante:** para criar filtros por tabela no layout HTML5 é necessário buscar a partir da instância NomeTabelasPreco ao invés de TabelaPreco.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

## Aba Histórico de Atualizações

![Imagem 2: Aba Histórico de Atualizações](https://ajuda.sankhya.com.br/hc/article_attachments/1500020025821)

No campo obrigatório **"Dt. Vigor"** dessa aba, informe a data de início da operação da tabela.

Referente ao campo **"Dt. alteração"**, insira a data da última alteração da tabela de preços. Uma vez que, ao adicionar um novo registro nessa aba, o sistema preencherá esse campo automaticamente com a data em que o registro for inserido, porém você pode mudá-lo, caso assim desejar.

O percentual informado no campo **"Percentual %"** será aplicado no preço dos produtos, caso seja criada uma tabela derivada da tabela selecionada. Este percentual poderá ser negativo, caso você deseje diminuir o valor dos produtos na nova tabela em relação à tabela principal. Abaixo, temos o seguinte exemplo:

Uma determinada tabela X, cuja tabela de origem é a zero, e sobre esta incide o percentual de -6%, e outra tabela Y, cuja tabela de origem é a 1,  e sobre esta incide o percentual de 4, o sistema SOMA todos os percentuais e aplica no primeiro preço, para calcular o preço da tabela 2.  No exemplo dado, o percentual seria (-6) + 4, resultando -2 %.

Em **"Tabela de Origem"**, indique a tabela que originará a tabela atual.

A marcação **"Utiliza decimais do custo para preço:"** quando realizada, fará com que o arredondamento seja obtido através do parâmetro **"Decimais para custo - CUSTODEC"**, ou seja, caso exista um valor diferente de "0" (zero) no parâmetro de chave CUSTODEC, o arredondamento das casas decimais tanto no Cadastro de Exceção da Tabela de Preços, quanto na obtenção de preço da tabela será arredondado de acordo com o que foi configurado no referido parâmetro. Caso o valor seja "0", o arredondamento será feito para "2" (duas) casas decimais por padrão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

## Aba Regras/Exceções

Abaixo dos campos acima tratados, temos a aba **"Regras"** (no caso de tabelas 0 (zero)) ou a aba **"Exceções"** (no caso de outras tabelas).

![Imagem 3: Abaixo dos campos acima tratados, temos a aba "Regras" (no caso de tabelas 0 (zero)) ou a aba "Exceções" (no caso de…](https://ajuda.sankhya.com.br/hc/article_attachments/40886846200599)

Nesta parte, além do campo **"Digite o produto e tecle ENTER"**, por onde você poderá pesquisar produtos da grade, temos os seguintes campos:

Em **"Produto"** deverá ser informado o produto que fará parte da Regra ou Exceção.

O campo **"Tipo"** é uma lista em que você define se será utilizado **Percentual** ou **Fixo**. No campo **"Valor"**, informe o preço do produto para a Regra ou Exceção — seu preenchimento é obrigatório quando o "Tipo" estiver definido como **"Fixo"**. Vale lembrar que qualquer alteração de preço terá efeito apenas sobre as novas movimentações de vendas, não impactando documentos já lançados.

Informe no campo **"Local"** o local padrão nessa Regra ou Exceção para esse produto. Esse campo aparecerá na tela caso o parâmetro **"Controla Preços por Local? - PRECOPORLOC"** esteja habilitado.

O campo **"Controle"** estará visível quando o parâmetro **"Controla Preços por Controle? - PRECOPORCONT"** estiver ligado. Caso o produto possua controle adicional de estoque, será exibido neste campo.

O campo **"Referência do Fornecedor"** será preenchido automaticamente pelo sistema com a informação do Cadastro do Produto, assim como o campo **"Cód. de Barra"**.

No carregamento das regras/exceções, os registros são exibidos de forma **paginada** — ou seja, carregados aos poucos para que você possa utilizar a tela enquanto as informações são processadas. É possível editar um registro no modo formulário durante esse carregamento; ao concluir, o sistema emitirá uma mensagem para confirmação da edição.

> **Observação:** o parâmetro **"Desconto acima do Flex vai para pé da nota? - DESCFLEXPENOTA"** é utilizado apenas no momento do faturamento e, quando ativo, distribui o desconto dos itens que ficaram abaixo do flex do pedido.

Caso o produto incluído possua Controle Adicional por **"Grade"**, o sistema exibirá o botão **"Grade"** ao selecioná-lo. Para habilitar esse comportamento, ative o parâmetro **"PRECOPORCONT - Controla Preços por Controle?"**. Ao abrir o pop-up, informe o preço no campo **"Valor"** e selecione no campo **"Tipo"** se será **"Fixo"** ou **"Percentual"**. O botão **"Replicar"** aplica o valor informado a todos os itens disponíveis na grade.

[GIF animado: Imagem 4: Caso o produto incluído possua Controle Adicional por "Grade" , o sistema exibirá o botão "Grade" ao selecioná-lo. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019681081)

> **Nota:** caso já exista uma tabela de preço cadastrada para o produto em questão, o sistema exibirá uma mensagem informando sobre isso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

## Botão Copiar Tabela

Através do botão ![Imagem 5: Através do botão "Copiar tabela" , localizado no alto da tela, será possível copiar os dados de uma tabela para outra.](https://ajuda.sankhya.com.br/hc/article_attachments/16677891120151) **"Copiar tabela"**, localizado no alto da tela, será possível copiar os dados de uma tabela para outra.

Ao clicar neste botão, será exibido o pop-up **"Copiando tabela de preços"**.

![Imagem 6: Ao clicar neste botão, será exibido o pop-up "Copiando tabela de preços" .](https://ajuda.sankhya.com.br/hc/article_attachments/1500019682381)

Assim, é solicitada a cópia dos dados de uma tabela 0 (zero) de origem para uma tabela 0 de destino, o sistema somente realizará a cópia do cabeçalho da mesma.

####

#### Seção Origem

Nesta seção, será possível visualizar os dados da tabela que terá os registros copiados.

**Nota:** o sistema copiará os dados da tabela de origem com a data de vigor mais recente.

Se você desejar copiar apenas produtos de um local específico,  realize o preenchimento do campo **"Local"**. Por outro lado, caso este campo não estiver preenchido, serão copiados todos os produtos, independentemente do local.

####

#### Seção Destino

No campo **"Tabela"**, informe qual tabela receberá a atualização.

Em **"Dt. vigor"** insira a data de vigor da nova tabela.

O campo **"% aplicar nos produtos"** deverá ser preenchido com o valor em porcentagem a ser aplicado sobre os preços dos produtos da tabela de destino em relação à tabela de origem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

## Campos Adicionais

A tela Tabelas de Preços possui suporte para campos adicionais e os mesmos poderão ser criados na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados):

![tp4](https://ajuda.sankhya.com.br/hc/article_attachments/360061007474)

Abaixo temos um exemplo:

Para a tabela TGFTAB - Tabela de Preço, cria-se um campo adicional na tela Dicionário de Dados:

Para incluir o campo adicional,  clique no botão ![Imagem 8: Para incluir o campo adicional, clique no botão "Novo" e realize o cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/16677891124631) **"Novo"** e realize o cadastro.

Os campos adicionais que não receberem nome de aba no botão **"Atributos"** serão adicionados na aba **"Campos Adicionais"** (que será exibida na tela Tabela de Preços); caso o campo adicional receber o nome de aba no botão atributos, será criada uma aba com o nome informado.

**Observação:** esta aba somente será apresentada se houver campo adicional cadastrado e a mesma sempre será exibida ao final do controle de abas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

## Tabelas de Preços Alternativos

Através das configurações listadas abaixo, realize o lançamento de um Pedido ou Nota de Compra, utilizando Tabelas de Preços específicas para a própria empresa.

**Nota:** a utilização desta configuração é propicia para empresas de uma mesma rede de franquias.

Inicialmente, realize a configuração do parâmetro **"Usar tabela de preço alternativa por empresa? - USATABALTEMP"** que, quando ativado, serão apresentados alguns campos nas telas que seguem:

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025239374-Empresa#abaestoquepreo), teremos o campo **"Tabela de preço alternativa"** e neste, informe a tabela de preço referente à empresa que será utilizada.

Nos [Cadastros de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes) temos a marcação **"Usar tabela de preço alternativa da empresa?"** que, para utilização desta funcionalidade, deverá ser selecionada.

Realizadas estas configurações, ao efetuar o lançamento de um Pedido ou Nota de Compra, informe um produto cadastrado na Tabela de Preços, seu respectivo valor será considerado, para cada empresa diferente, onde cada uma poderá utilizar uma tabela de preços diferente, se assim desejado e necessário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

## Como vincular a Tabela de Preço a um cadastro

Por meio do parâmetro **"Tabela de Preços por-TIPTABPRECOS"**, você pode vincular de forma mais rápida a Tabela de Preço aos seguintes cadastros:

| - Única; - Região do Vendedor; - Região do Parceiro; - Perfil; - Parceiro; | - Tipo de Negociação; - Local; - Tipo de Negociação/Vendedor; - Parceiro/Tipo Negociação/Vendedor; - Parceiro/Empresa. |
| --- | --- |

Desse modo, de acordo com a opção selecionada no parâmetro acima, será exibida na tela Tabela de Preços, uma aba onde você deve efetuar a configuração da tabela com o respectivo cadastro.

![Imagem 9: Ao configurar o parâmetro TIPTABPRECOS com a opção " Parceiro ", o sistema busca a tabela de preços diretamente no…](https://ajuda.sankhya.com.br/hc/article_attachments/16950610985751)Ao configurar o parâmetro TIPTABPRECOS com a opção "**Parceiro**", o sistema busca a tabela de preços diretamente no cadastro do parceiro. Caso não exista uma tabela configurada, a busca é redirecionada para os preços da Tabela Zero.

Para melhor compreensão, considere o exemplo a seguir:

Suponhamos que você deseja vincular a Tabela de Preço ao cadastro de Parceiros. Para isso, acesse primeiramente a tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834) e configure o parâmetro **"Tabela de Preços por - TIPTABPRECOS"**, campo **"Valor"**, com a opção **"Parceiro"**. 

[GIF animado: Imagem 10: Suponhamos que você deseja vincular a Tabela de Preço ao cadastro de Parceiros . Para isso, acesse primeiramente a tela…](https://ajuda.sankhya.com.br/hc/article_attachments/7245064781719)

Em seguida, acesse novamente a tela Tabela de Preços. Desse modo, será apresentada a aba **"Parceiros"**, nela informe o **"Cód. Parceiro"** e **"Salve"** o registro. 

[GIF animado: Imagem 11: Em seguida, acesse novamente a tela Tabela de Preços . Desse modo, será apresentada a aba "Parceiros" , nela informe o…](https://ajuda.sankhya.com.br/hc/article_attachments/7245091225879)

Realizadas as configurações acima, a Tabela de Preço estará vinculada ao cadastro do Parceiro.

| ```          Dica: Para remover o registro, basta acionar o botão  "Excluir". ``` |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os#top)

![Imagem 12: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16675739597463)Acesse também:

[Como Atualizar Preço de Custo, Preço de Venda/Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Como-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela).
