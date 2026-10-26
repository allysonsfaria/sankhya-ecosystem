---
id: "360044601854"
titulo: "Relação Produto/Parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601854-Rela%C3%A7%C3%A3o-Produto-Parceiro"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:24:02Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Consulta", "Parceiro", "Giro Mensal", "Produtos Comercializados com a Empresa", "Relação Produto/Parceiro", "UTILIZACONTROLE", "UTILIZALOCAL", "br.com.sankhya.mgecom.cons.relacaoprodutoparceiro", "Relação Produto/Parceiro manual", "TOP", "Estoque", "Movimentações de Produtos", "Parceiros comerciais", "Análise de Vendas e Compras"]
---

# Relação Produto/Parceiro

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311815513239) Módulo: Comercial > Consulta
```

---

Nesta tela, você visualiza os produtos que foram comercializados com os parceiros da empresa, em um período de tempo determinado, disponibilizando informações completas sobre estes, conforme o Tipo de Movimento selecionado.

[Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601854-Rela%C3%A7%C3%A3o-Produto-Parceiro#configura%C3%A7%C3%B5esiniciais)                                          [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601854-Rela%C3%A7%C3%A3o-Produto-Parceiro#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 2: Configurações Iniciais Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360086870494)

## Configurações Iniciais

Em relação à aba**"Grupos"** encontrada no Painel de Filtros, são disponibilizados os grupos das TOP's que estão disponíveis para consulta.

No Painel de Filtros, a aba **"Tipo Movimento"** contém os tipos de movimentos cadastrados na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), sendo que estes poderão ser selecionados para consulta.

**Observação:** É necessário selecionar pelo menos um Tipo de Movimento para aplicação do filtro. Caso você escolha apenas o Grupo, a consulta não será realizada.

1. Primeiramente, selecione nas abas Tipo de Movimento e Grupos as opções pretendidas para que sejam visualizadas na consulta.

2. Após este procedimento, preencha os campos **"Produto"**, **"Parceiro"**, **"Controle"** e **"Local"** caso existam estas informações para o produto selecionado, e o período a ser analisado, conforme o campo **"Data de Negociação"** das notas.

3. Selecionando a marcação **"Exibir Variação"**, fará com que seja visualizada a variação de preços negociados.

**Nota:** A variação buscará o preço médio realizado do último dia de negociação para este Produto, Tipo de Movimento e/ou Parceiro e calculará a diferença em percentual, em relação ao preço da linha em exame, tendo a seguinte fórmula:

((Valor Atual / Valor Anterior) - 1)\* 100.

Trouxemos um exemplo de variação:

Um produto foi vendido a R$100,00. Na data anterior, foi vendido a R$90,00. Desta forma, resultará em 11% de variação.

Foi efetuada a compra de um produto a R$120,00. Na data anterior foi comprado a R$100,00. Assim, a variação exibida será de 20%.

4. Na marcação **"Agrupar Lançamentos"**, você define a visualização dos lançamentos agrupados por Parceiro e Tipo de Movimento. Quando esta marcação estiver desabilitada, o sistema exibirá nas colunas **"Unidade"**, **"Quantidade"** e **"Vlr. Unit. Nota"** os valores iguais aos visualizados no lançamento da nota. Apresentará também, na coluna **"Valor Unit. Líq."**, o valor unitário considerando a unidade principal do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-). Por outro lado, quando esta marcação estiver habilitada, será exibida a unidade principal do Cadastro de Produtos.

**Importante:** Se a marcação Exibir Variação estiver selecionada e a marcação Agrupar Lançamentos desabilitada, na grade principal, você pode visualizar a coluna **"Variação"**. Caso contrário, esta coluna não estará visível.

Quando a marcação **"Exibir Referência do fornecedor"** estiver habilitada, fará com que a referência do fornecedor seja exibida logo abaixo deste campo.

5. Clicando no botão **"Aplicar"**, os dados configurados nos filtros serão apresentados na parte superior da tela.

A coluna **"Vlr. Total Itens"** apresenta o valor do item, somando o valor do desconto do item, o valor do IPI e o valor da ST, não considerando estes valores no pé da nota.

Será apresentado na coluna **"Apelido Vendedor"** o nome do vendedor sempre que você selecionar o produto, desta forma, facilitando a análise de compra e venda do produto por vendedor.

Os dados exibidos nas grades inferiores são detalhes do registro selecionado na grade principal. Estes detalhes podem ser ocultados ou exibidos através dos botões ![Imagem 3: Os dados exibidos nas grades inferiores são detalhes do registro selecionado na grade principal. Estes detalhes podem…](https://ajuda.sankhya.com.br/hc/article_attachments/16637587087255)**"Giro Mensal"** e ![Imagem 4: Os dados exibidos nas grades inferiores são detalhes do registro selecionado na grade principal. Estes detalhes podem…](https://ajuda.sankhya.com.br/hc/article_attachments/16637593150487) **"Estoque"**, na parte superior desta tela.

[GIF animado: Imagem 5: Os dados exibidos nas grades inferiores são detalhes do registro selecionado na grade principal. Estes detalhes podem…](https://ajuda.sankhya.com.br/hc/article_attachments/360088003913)

Ao clicar no botão Giro Mensal, será exibida uma grade no canto inferior esquerdo da tela, que informará o total de entradas e saídas de produtos conforme a quantidade de meses escolhida no campo **"Meses"** localizado ao lado deste botão.

Referente ao botão Estoque, clicando neste, será apresentada uma grade com detalhes do estoque do produto na parte inferior direita da tela. Nesta grade, serão exibidos os campos **"Tipo"** e **"Poder"**, que terão como conteúdo as informações Próprio ou Terceiros. Desta forma, você pode restringir a consulta de estoque, por exemplo, para que seja visualizado apenas o estoque daquele produto com tipo Próprio e que esteja em Poder de uma empresa específica.

No botão **![Imagem 6: No botão "Exibir Estoque" , existem 3 opções disponíveis para marcação, sendo estas "Exibir estoque da Empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/16637577189143) "Exibir Estoque"**, existem 3 opções disponíveis para marcação, sendo estas **"Exibir estoque da Empresa (Próprio) em poder da Empresa (Próprio)"**, **"Exibir estoque da Empresa (Próprio) em poder de Terceiros"** e **"Exibir estoque de Terceiros em poder da Empresa (Próprio)"**. Estas opções têm o objetivo de definir o que será visualizado ou não nesta consulta referente ao Estoque de Terceiros e ao Estoque Próprio. Estando as três opções desmarcadas, nenhuma informação será apresentada na grade **"Estoque"**.

[GIF animado: Imagem 7: No botão "Exibir Estoque" , existem 3 opções disponíveis para marcação, sendo estas "Exibir estoque da Empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/360088004433)

Independente se a grade Estoque está visível ou não, teremos no rodapé desta tela os totalizadores **"Estoque"**, **"Reservado"** e **"Disponível"**, sendo estes responsáveis por exibirem o total do estoque do produto selecionado na grade principal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601854-Rela%C3%A7%C3%A3o-Produto-Parceiro#top)

## Parâmetros que influenciam esta rotina

O parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"** exibirá ou ocultará o filtro por Controle.

Em relação ao parâmetro **"Utiliza a coluna Local para controlar o estoque -** **UTILIZALOCAL"**, este habilitará ou desabilitará o filtro por Local.

**Observação:** Caso a chave de parâmetro UTILIZACONTROLE esteja habilitada, ao alterar o produto no filtro, o campo **"Controle"** sofrerá modificação em sua aparência conforme o tipo de controle do produto em questão. O campo Controle poderá ser do tipo **"Texto"**, **"Data"**, **"Lista de Seleção"** ou ficar desabilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601854-Rela%C3%A7%C3%A3o-Produto-Parceiro#top)
