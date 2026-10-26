---
id: "360044596614"
titulo: "Botão Desenhos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:20:53Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Botão Desenhos", "Botão Desenhos manual", "Impressão", "USACHAVERGA", "Recurso de Desenhos", "Edição de Desenhos Bidimensionais", "Desenhos em Pedidos de Venda", "Comercial", "Pedidos de Venda"]
---

# Botão Desenhos

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311763740311)  Módulo: Comercial
```

---

![Imagem 2: Este botão está disponível apenas no Layout Anterior (Flex).](https://ajuda.sankhya.com.br/hc/article_attachments/17281013825559) Este botão está disponível apenas no Layout Anterior (Flex). 

O Sankhya Om possui um recurso para, a partir do lançamento de Pedidos de Venda, no painel de itens, fazer a edição de desenhos bi-dimensionais de: chapadas dobradas, chapas cortadas, vergalhões, discos e anéis.

A partir da indicação das faces do desenho e dos ângulos de dobras, o sistema mostrará um desenho bi-dimensional conforme os dados inseridos e, em seguida, incluirá o item no Pedido de Venda com a quantidade conforme o peso calculado a partir das medidas das áreas dos desenhos gerados.

Os dados do desenho são salvos e atrelados ao campo **"NUNOTA"** da tabela TGFCAB, isso é feito apenas no momento de salvar os dados no pop-up do desenho pela Central de Notas. Portanto, ao faturar, os dados do desenho não serão transferidos para os dados das tabelas TGFDDC e TGFFAC. Neste caso, para consultar as informações do desenho, basta acessar os documentos relacionados.

**Importante:** para que o sistema apresente o botão **"Desenhos..."**na tela de Pedidos de Venda, é necessário que você habilite o parâmetro **"Usa rotina de desenho de chapas e vergalhões - USACHAVERGA"**. Abaixo, trataremos sobre as opções disponíveis neste botão:

[Editar desenho atual](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#editardesenhoatual)                                                      [Desenho por template](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#desenhoportemplate)

[Desenho de chapas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#desenhodechapas)                                                        [Desenho de anéis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#desenhodean%C3%A9is)

[Desenho de discos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#desenhodediscos)                                                          [Desenho de vergalhões dobrados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#desenhodevergalh%C3%B5esdobrados)

[Desenho de vergalhões em cinta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#desenhodevergalh%C3%B5esemcinta)                                [Impressão dos Desenhos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#impress%C3%A3odosdesenhos)

![Imagem 3: Desenho de vergalhões em cinta Impressão dos Desenhos](https://ajuda.sankhya.com.br/hc/article_attachments/360086567934)

## Editar desenho atual

Quando a barra de seleção estiver posicionada em um produto vendido, utilizando o recurso do botão Desenhos..., será habilitado no seu menu, a opção **"Editar desenho atual..."** que, ao ser selecionada, abrirá a janela **"Editando desenho atual"**. Esta opção é utilizada para todos os modelos de desenho.

[GIF animado: Imagem 4: Quando a barra de seleção estiver posicionada em um produto vendido, utilizando o recurso do botão Desenhos... , será…](https://ajuda.sankhya.com.br/hc/article_attachments/360086568114)

Quando você selecionar um produto vendido que não possua desenho, o sistema mostra a mensagem:

**"Editando desenho atual". Este item não está associado a um desenho, não é possível editar.".**

Caso contrário, será aberta uma janela de edição, com o desenho vinculado àquele produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Desenho por template

Quando você selecionar a opção **"Desenho por template"**, o sistema abrirá uma janela para que você possa inserir item de desenho, através de templates pré-cadastrados na tela [Registro de Peças](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112493).

Ao escolher o produto, serão buscados os templates que tiveram este produto vinculado e mostrará na grade de Templates. Você deverá preencher as informações de cabeçalho do desenho e, após escolher o template, o sistema exibirá o desenho e os campos que você pode ou não editar. Para os templates que usam faces, não é possível alterar o Ângulo, somente a Largura da face.

![Imagem 5: Ao escolher o produto, serão buscados os templates que tiveram este produto vinculado e mostrará na grade de Templates.…](https://ajuda.sankhya.com.br/hc/article_attachments/360086690834)

Você poderá escolher a **"Unidade de Medida"**, possibilitando a criação de um template para qualquer tipo de desenho, usando qualquer uma das duas medidas: centímetro ou milímetro.

Na tela aberta pela Central - Compras | Vendas, não é possível alterar a unidade de medida. Uma vez utilizado um template, a unidade utilizada será a definida no template.

A unidade será sempre milímetros para as telas de desenho de Anéis, Discos e Chapa.

**Nota:** Para os desenhos de vergalhão dobrado e vergalhão em cinta, será sempre em centímetros, pois os vergalhões comumente são medidos em centímetros.

Com a unidade de medida liberada no template, caso o cliente deseje, será possível criar templates com unidade de medida à sua escolha.

Depois de incluídos os desenhos, o sistema segue o fluxo padrão de um Pedido de Venda para finalizar o pedido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Desenho de chapas

Selecionando a opção **"Desenho de chapas..."**, o sistema abre uma janela para informar o **"Nome do projeto"**, o **"Produto"**, a **"Quantidade"** de peças e o **"Comprimento"** da chapa. Você também informa as faces da chapa e, conforme a inclusão da face, o sistema vai mostrando o desenho ao lado da grade de faces:

[GIF animado: Imagem 6: Selecionando a opção "Desenho de chapas..." , o sistema abre uma janela para informar o "Nome do projeto" , o "Produto"…](https://ajuda.sankhya.com.br/hc/article_attachments/360086690014)

O sistema utilizará a soma da largura das faces, juntamente com o comprimento da chapa, a quantidade de chapas e o valor informado no campo adicional **"Peso da dobra"** (considerando o peso por metro quadrado) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) para calcular o Peso Total das chapas e incluirá um item na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) com o Produto e a quantidade calculada.

![Imagem 7: O campo adicional Peso da dobra deve ser criado com a denominação AD_PESOPORMQ para funcionar corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/20035054282903) O campo adicional Peso da dobra deve ser criado com a denominação AD\_PESOPORMQ para funcionar corretamente.

**Nota:** o preço do Produto será calculado conforme a [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os).

Observe que, no desenho da grade, o sistema mostra na cor vermelha a face selecionada na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Desenho de anéis

Quando você selecionar a opção **"Desenho de anéis..."**, o sistema abrirá uma janela para informar o Nome do projeto, o Produto, a Quantidade, o Diâmetro externo e Diâmetro interno do disco; ao final, o sistema calcula o peso da peça e inclui um item na grade, semelhante ao desenho de chapa.

[GIF animado: Imagem 8: Quando você selecionar a opção "Desenho de anéis..." , o sistema abrirá uma janela para informar o Nome do projeto , o…](https://ajuda.sankhya.com.br/hc/article_attachments/360087848073)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Desenho de discos

Ao acionar a opção **"Desenho de disco..."**, o sistema abre uma janela para informar o Nome do projeto, o Produto, a Quantidade e o Diâmetro externo; ao final, o sistema calcula o peso da peça e inclui um item na grade de itens, semelhante ao desenho de chapa. Observe que, diferente do desenho de anéis, o desenho de disco não tem o diâmetro interno.

[GIF animado: Imagem 9: Ao acionar a opção " Desenho de disco..." , o sistema abre uma janela para informar o Nome do projeto , o Produto , a…](https://ajuda.sankhya.com.br/hc/article_attachments/360086690114)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Desenho de vergalhões dobrados

Quando você selecionar a opção **"Desenho de vergalhões dobrados..."**, será aberta uma janela para informar o Nome do projeto, o Produto e a Quantidade de peças. Você também informa as Faces da chapa e, conforme a inclusão da face, o sistema vai mostrando o desenho ao lado da grade de faces. Após concluir o desenho, clique em Salvar e fechar e o sistema utiliza a soma da largura das faces, a quantidade de chapas e o valor informado no campo **"Peso líquido"** (considerando o peso por metro linear) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), para calcular o peso total das chapas e incluir um item na grade de itens com o produto e a quantidade calculada; o preço do produto é calculado conforme a Tabela de Preços.

[GIF animado: Imagem 10: Quando você selecionar a opção " Desenho de vergalhões dobrados..." , será aberta uma janela para informar o Nome do…](https://ajuda.sankhya.com.br/hc/article_attachments/360087848193)

Esse desenho é bem semelhante ao desenho de chapas, exceto por não ter o campo de comprimento e, nesse caso, o cálculo do peso da peça é através de metro linear, ou seja, o valor informado no campo Peso líquido do Cadastro de Produto deve ser por metro linear.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Desenho de vergalhões em cinta

Quando você selecionar a opção **"Desenho de vergalhões em cinta..."** o sistema abre uma janela para informar o Nome do projeto, o Produto e a Quantidade de peças. Você também informa o Diâmetro da cinta, o Comprimento da orelha 1 e o Comprimento da orelha 2 e, assim, o sistema calcula o comprimento total.

Neste caso, o peso também é calculado em metro linear; nessa tela, é apresentado o campo Comprimento total da peça, considerando o comprimento da circunferência e das orelhas.

[GIF animado: Imagem 11: Neste caso, o peso também é calculado em metro linear; nessa tela, é apresentado o campo Comprimento total da peça,…](https://ajuda.sankhya.com.br/hc/article_attachments/360087848313)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)

## Impressão dos Desenhos

Para impressão personalizada dos desenhos utiliza-se o iReport, que é a ferramenta usada para geração de PDF e para impressão dos relatórios.

Estes relatórios poderão ser personalizados incluindo os dados desejados por você.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596614-Bot%C3%A3o-Desenhos#top)
