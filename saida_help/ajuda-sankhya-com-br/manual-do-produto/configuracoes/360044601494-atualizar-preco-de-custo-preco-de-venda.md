---
id: "360044601494"
titulo: "Atualizar Preço de Custo, Preço de Venda/Tabela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:33Z"
rotulos: ["Produtos", "Configuração", "Como Atualizar Preço de Custo", "Preço de Venda/Tabela", "Preço de Venda/Tabela manual", "Atualização", "Estoque", "Preferências", "Atualizando Preço de Custo e Preço de Venda/Tabela", "Tabela de Preços"]
---

# Atualizar Preço de Custo, Preço de Venda/Tabela

Nesse artigo trataremos dos seguintes pontos:

- [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#Configura%C3%A7%C3%B5esiniciais)
- [Atualização de tabelas de preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#Atualiza%C3%A7%C3%A3odetabeladepre%C3%A7os)
- [Utilizando a fórmula interna do sistema para atualização de custo e preço de venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#Utilizandof%C3%B3rmulainternadosistemaparaatualiza%C3%A7%C3%A3odecustoepre%C3%A7odevenda)
- [Atualização de preço de tabela quando produto utiliza unidade alternativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#Atualiza%C3%A7%C3%A3odepre%C3%A7odetabelaquandoprodutoutilizaunidadealternativa)

## Configurações Iniciais

Abaixo trataremos das configurações necessárias para que os custos sejam atualizados de forma correta:

Primeiramente, nas [TOPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) de Compra, no campo **"Precifica"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), seção **"Preço/Custo"**) verifique se a opção **"Atualizar custo e preço de venda"** ou **"Atualizar somente custo"** esta selecionada.

**Observações:**

- A opção **"Atualizar custo pelo agendador"** será utilizada para fazer o cálculo de custos do produto apenas no [Agendador para Recálculo de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594294).
- Usando outras opções, o botão [Recalcular custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#recalcularcustos) na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), não estará habilitado para uso.
- Como é utilizado com o tarefas, no **"Cadastro de Produtos"**, aba **"Medidas e Estoque"**, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque) o campo **"% Aviso Var.Custo"** não deve ser preenchido.

Realizados os procedimentos acima, na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) configure os seguintes parâmetros:

- Percentual de custo fixo- PERCCUSFIXO
- Controla custo por local?- CUSTOPORLOC
- Percentual PIS/COFINS- PERCPISCOFINS
- Decimais para custo- CUSTODEC
- Custo por empresa?- CUSTOPOREMP
- Controla custo por controle?- CUSTOPORCONT

O parâmetro **"Atualiza custo independente da data?- ATUALCUSINDEP"**, impede que ocorra atualizações de custo quando a data da nota é inferior a data da última atualização de custo ou a data do servidor. Ou seja, se ele estiver = **'N'** o sistema só calculará o custo se a data informada for maior ou igual a maior data na tabela de custos, se estiver=**'S'** ele sempre calculará.

Em relação ao parâmetro **"Data para atualização de custos- DTPATUCUST"**, ao abrir a tela de [Recálculo de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214) e ao confirmar uma nota que gere cálculo de custo (apresentada no painel de avisos) são apresentadas as seguintes mensagens:

- Se o parâmetro DTPATUCUST estiver configurado como **"Negociação"**:

**"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos "Dt. Negociação". Foi identificado que você está usando configuração diferente do que é atualmente permitido, entre em contato com a Sankhya para se informar sobre as consequências de usar esta configuração."**

- E quando o parâmetro DTPATUCUST estiver configurado como **"Movimentação"** ou **"Faturamento"**:

**"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos "Dt. Negociação". Foi identificado que você possui configuração diferente de "Dt. Entrada/Saída", para não ver esta mensagem novamente, basta ajustar o parâmetro "Data para atualização de custo" (DTPATUCUST) colocando a opção "Entrada/Saída", quando o parâmetro "DTPATUCUST" está igual a "Negociação".**

Para que as mensagens acima não sejam apresentadas, basta configurar o parâmetro DTPATUCUST para **"Entrada/Saída"**.

Ao habilitar o parâmetro **"Apresentar variação de preço na NF de compra?- APRVARPNFCOMPRA"** e ao confirmar uma Nota de Compra que a TOP esteja configurada para precificar, o sistema apresentará a variação de preço de venda e a seguinte mensagem: 

**"Houve variação no preço de venda. Deseja visualizar os produtos com variação?"**

Ao clicar em **"Sim"**, é apresentada a variação do preço em relação à última data de vigor da tabela de preço ignorando o dia da confirmação da Nota de Compra.

Com os parâmetros configurados, na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) verifique se o campo **"Fórmula de Custo/Preço"** e **"% Margem de Lucro"** estão devidamente preenchidos.

Certifique-se também se a expressão matemática está correta no cadastro de **"Formulas de Precificação"**. Quando o produto não possui fórmulas de precificação ([Fórmulas de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874)), o sistema utiliza a fórmula interna para calcular os custos e preço do produto.

**Importante:** quando for utilizada tabela de preço por parceiro, o Produto não deverá ter preço cadastrado na tabela zero, pois não havendo o Cadastro do Produto na tabela do parceiro, o sistema buscará o preço do produto na tabela zero.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#top)

## Atualização de tabelas de preços

O sistema possui várias formas de atualizar as tabelas de preço, assim trataremos abaixo  das telas em que isso ocorre:

- Tela [Tabela de preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854).

Nesta opção, ao incluir uma tabela de preços, informa-se o produto com seus respectivos preços. Lembrando que estes produtos que são informados são exceções.

- Tela [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), botão [Recalcular custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#recalcularcustos).

Quando você realiza a entrada de um produto no sistema, se o cadastro do sistema atender às especificações abaixo o sistema calcula o preço do produto, após confirmar a nota, clicando-se neste botão.

Nesta tela, temos as seguintes especificações para o recálculo:

Na [TOPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) de Compra, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), na seção **"Precificação"** selecione a opção **"Atualizar custo e preço de venda"**.

Depois, no [Cadastro de produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo), é necessário que tenha uma fórmula de precificação cadastrada. Quando o produto não possui fórmulas de precificação ([Fórmulas de custo/preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874)), o sistema utiliza a fórmula interna para calcular os custos e preço do produto.

- Tela [Atualização de Preço de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612094).

Você pode utilizar a rotina de Atualização de Preço de Venda para gerenciamento de tabelas de preços. Nesta tela é possível atualizar todas as tabelas, ou apenas a que for selecionada por meio do campo **"Tabela"**.

No Painel de Filtros desta tela temos a opção de personalizar os filtros, na qual pode-se atualizar somente um **"Grupo de produtos"**, uma **"Marca"**, **"Matéria- prima"**, **"Produto de revenda"**, entre outras.

Na seção**"Opções"**, campo **"Data de atualização"**, você pode informar a data em que esta tela foi utilizada para reajustar o preço de determinada tabela. Considerando que esta tela foi utilizada para reajustar alguma tabela, o campo **"Data de vigor"** mostra a data em que a tabela alterada entrará em vigor.

Clicando no botão **"Outras opções"** temos as seguintes alternativas:

- **Reajustar por índice:** esta opção atualiza o preço dos produtos filtrados na tela, através de um percentual de reajuste informado.
- **Trazer todos os produtos:** sistema mostra todos os produtos do filtro especificado.
- **Incluir valor para todos:** esta opção abre uma tela para o cliente informar o preço dos produtos filtrados, escolhidos na tela.

Abaixo da Grade de Produtos é apresentado um Painel com os seguintes campos:

**Custo:** Gerencial, Reposição e Variável do item selecionado na grade.

**Margem s/ preço de tabela:** a margem Gerencial, Reposição e Variável sobre o preço de tabela do item selecionado na grade.

- Tela [Recálculo de custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214).

Esta tela permite que você realize o recálculo de custos de produtos, a partir de Movimentações de Entrada, Notas de Compra, Produção etc. Tal funcionalidade é útil em casos de alterações em fórmulas de precificação ([Fórmulas de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874)) necessárias devido a redefinições em políticas de custeio e precificação.

Nesta opção, você também tem acesso ao cálculo de custos médios.

- Tela [Recálculo do Preço de Tabela pela fórmula de Precificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612634).

**Observação:** no parâmetro **"Tabela preços por-TIPTABPRECOS"**, ao indicar uma das opções abaixo é necessário realizar as seguintes configurações: 

Se for selecionado a opção **"Única"**, você deverá utilizar a tabela 0.

Quando indicada a opção **"Região do vendedor"** informe a tabela na tela [Regiões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074), no campo **"Tab. Básica p/ Calc. de Acréscimo"**. Além disso, defina a região do vendedor no campo **"Região"**, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral) do Cadastro de [V](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133)[endedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133).

Com a opção **"Região do Parceiro"** indicada, informe a tabela na tela Regiões no campo Tab. Básica p/ Calc. de Acréscimo. Defina também a região do parceiro no campo **"Região"** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo).

Se for selecionada a opção **"Perfil do Parceiro"**, informe a tabela de preços na tela [Perfil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110753), no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110753-Perfil#painelprincipal), campo **"Tabela de Preço"**.

Quando informado a opção **"Parceiro"** indique a tabela de preços no Cadastro de parceiros, aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) no campo **"Tabela de Preço"**.

Ao indicar a opção **"Tipo de Negociação"** informe a tabela de preço no cadastro de **"Tipo de Negociação"**, aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), no campo **"Tabela Preço"**.

Com a opção **"Local"** selecionada, no cadastro de [Locais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602894) informe a tabela de preço, no campo **"Tabela de Preço"**.

Quando for indicado a opção **"Tipo de Negociação/Vendedor"** o sistema habilitará a aba **"Vendedor/Tabela"** no cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), na qual você poderá vincular os vendedores a diferentes Tabelas de Preços.

### ✅ Como configurar a TOP para usar o custo como preço

Se você deseja que o sistema utilize o **"Último Custo de Entrada Sem ICMS"** como base de preço ao incluir produtos em pedidos de venda, siga esta orientação:

1. Acesse o cadastro da **TOP** desejada.
2. No campo **"Usar como Preço"**, selecione a opção **"Último Custo de Entrada Sem ICMS"**.
3. **Importante:** Certifique-se de que o campo

   > **"Usar tabela de preço alternativa da empresa?"**
   > esteja **desmarcado**.

🔎 Essa configuração é necessária porque, quando o parâmetro **USATABALTEMP** está ativado, e esse campo está marcado, o sistema utiliza o preço da tabela configurada na empresa — ignorando o custo definido na TOP.

💡 Com a configuração correta, o sistema irá:

- Utilizar o valor do **último custo de entrada sem ICMS**, se houver.
- Preencher o preço como **zerado**, caso não exista um custo registrado para o produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#top)

## Utilizando a fórmula interna do sistema para atualização de custo e preço de venda

Primeiramente, na TOP marque a opção **"Atualiza custo e preço de venda"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), seção **"Preço/Custo"**, campo **"Precifica"**).

![Imagem 1: Primeiramente, na TOP marque a opção "Atualiza custo e preço de venda" ( aba Geral , seção "Preço/Custo" , campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006945781)

Depois conforme apresentado no gif abaixo, acesse a tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Formação de Custo/ Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo), campo **"% Margem de Lucro"** e informe o valor percentual de lucro pretendido; o campo **"Fórmula de precificação"** não deve ser preenchido, pois será calculado através da fórmula interna do sistema. Na aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda), campo **"Digitação na nota"**, selecione a opção **"Quantidade"**, isto fará com que na hora de fazer o lançamento de um pedido nota de venda o usuário digite apenas a quantidade.

[GIF animado: Imagem 2: Depois conforme apresentado no gif abaixo, acesse a tela Cadastro de Produtos , aba Formação de Custo/ Preço , campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006945861)

Realizada as configurações acima, efetue a compra do Produto e confirme a nota. Logo após, clique no botão **"Recalcular Custos"**.

![Imagem 3: Realizada as configurações acima, efetue a compra do Produto e confirme a nota. Logo após, clique no botão " Recalcular…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006765622)

Feito isso, acesse a tela [Atualização de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594174) e verifique se o registro referente ao produto que foi efetuada a compra existe nesta tela.

![Imagem 4: Feito isso, a cesse a tela Atualização de Custos e verifique se o registro referente ao produto que foi efetuada a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006765742)

Acesse também a tela [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854) e localize a tabela com a data de vigor igual a data da compra.

![Imagem 5: Acesse também a tela Tabela de Preços e localize a tabela com a data de vigor igual a data da compra.](https://ajuda.sankhya.com.br/hc/article_attachments/1500006765762)

Por fim, você pode verificar de duas maneiras as configurações efetuadas: 

1. Realizando a venda deste mesmo produto e verificando se o valor dele está recalculado.
2. Acessando a tela [Atualização de Preço de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612094).

**Observação:** os passos são os mesmos para as outras opções do parâmetro TIPTABPRECOS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#top)

## Atualização de preço de tabela quando produto utiliza unidade alternativa

Quando o parâmetro **"Armazenar preço tabela em unidade alternativa- MULTVLRPRC"** estiver ligado, nos lançamentos utilizando unidade alternativa com multiplicador para valor, o valor de tabela armazenado para o item será convertido conforme a configuração do multiplicador da unidade alternativa utilizada no [Cadastro do produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113).

Considere o seguinte exemplo:

**Produto:** A

**Preço de tabela na unidade principal (VLRCUS):** 10,00

**Unidade alternativa:** CX

**Multiplicador para valor:** 0,80

Com o parâmetro desligado, o sistema armazena valores diferentes para o VLRUNIT e o VLRCUS, na tabela de itens da nota:

**VLRCUS:** 10,00

**VLRUNIT:** 8,00

Com o novo parâmetro igual a **"Sim"**, o sistema armazenará também no VLRCUS o valor convertido na unidade alternativa.

**VLRCUS:** 8,00

**VLRUNIT:** 8,00

Neste caso, o programa não barra o desconto máximo do produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601494-Atualizar-Pre%C3%A7o-de-Custo-Pre%C3%A7o-de-Venda-Tabela#top)
