---
id: "360044607894"
titulo: "Registro da Produção e do Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-09-15T14:42:13Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Livros Fiscais", "LISTOPEXCREGPRO", "TOPBRINDE", "TOPBRINDENF", "br.com.sankhya.mgeliv.rel.registroproducaoestoque", "Registro da Produção e do Estoque manual", "Estoque", "Produção", "Registro", "Entrada e Saída notas confirmadas", "Filtragem por produto e uso", "Configuração de livro e impressão"]
---

# Registro da Produção e do Estoque

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313031989399) Módulo: Livros Fiscais > Relatórios
```

---

Por meio deste relatório, empresas industriais poderão emitir as movimentações de Entrada e Saída do estoque, compondo o que foi produzido e seu consumo de acordo com os lançamentos efetuados no sistema.

Neste relatório são apresentadas somente as notas confirmadas e cuja TOP utilizada em seu lançamento esteja com a marcação **"Atualização de Livro ICMS"** presente na aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal) realizada.

![Imagem 2: Neste relatório são apresentadas somente as notas confirmadas e cuja TOP utilizada em seu lançamento esteja com a…](https://ajuda.sankhya.com.br/hc/article_attachments/6302636146583)

Inicialmente para geração do relatório, informe a **"Empresa"** da qual deseja gerar as informações.

Em seguida, insira as **"Data Inicial"** e **"Data Final"** que correspondem ao período de geração dos dados de movimentações de Entrada e Saída do estoque.

**Nota:** as marcações da tela irão buscar os registros datados em ordem decrescente junto às informações do produto conforme datas de emissão da nota.

Na aba **"Parâmetros"** disponível nessa tela, teremos as seguintes seções:

| [Seção Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#se%C3%A7%C3%A3oproduto) |  | [Seção Usado como](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#se%C3%A7%C3%A3ousadocomo) |
| --- | --- | --- |
| [Seção Livros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#se%C3%A7%C3%A3olivros) |  | [Seção Páginas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#se%C3%A7%C3%A3op%C3%A1ginas) |
| [Seção Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#se%C3%A7%C3%A3ofiltros) |  | [Geração do relatório](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#geracaoderelatorio) |

## Seção Produto

Nessa seção, você poderá buscar um **"Produto"** ou **"Grupo de Produtos"** específicos para geração do relatório. Essa opção evita a geração de dados referentes a todos os produtos e/ou grupos de modo a facilitar alguma conferência específica.

Quando você acionar a marcação **"Usar descrição do produto conforme NFe"**, a descrição do produto será exibida no relatório conforme os dados contidos no campo **"Descrição para NFE"**(aba Geral do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)). Ao deixá-la desabilitada, o produto será apresentado com a descrição informada em seu cadastro. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#na)

## Seção Usado como

É possível também filtrar produtos através da utilização dada à eles. As marcações aqui apresentadas são as mesmas disponibilizadas no Cadastro dos Produtos (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abageral), campo **"Usado como"**). São elas:

- Matéria Prima;
- Consumo;
- Revenda;
- Terceiros;
- Venda (Fabricação Própria);
- Revenda (por Fórmula);
- Imobilizado;
- Embalagem;
- Em Processo;
- Sub Produto;
- Prod. Intermediário;
- Outros Insumos;
- Brinde (NF);
- Brinde.

As duas últimas marcações (Brinde (NF) e Brinde) são habilitadas para uso, caso os parâmetros **"Top para Brindes (NF SUFRAMA) - TOPBRINDENF"** e **"Top para Brindes - TOPBRINDE"** possuam alguma informação diferente de "0" (zero), respectivamente.

**Importante:** os Tipos de Operação informados no parâmetro **"Lista de TOPs excluídas do registro de produção - LISTOPEXCREGPRO"** não terão as notas com elas lançadas consideradas para geração do relatório.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#na)

## Seção Livros

Por meio dessa seção, é possível realizar a impressão do relatório Registro da Produção e do Estoque com quebra de páginas. Temos os seguintes campos e marcações nesta seção:

Ao acionar a marcação **"Informar o número do livro"**, o número do livro será impresso antes do número da folha.

Através do campo **"Livro inicial"**, informe a numeração inicial do livro.

Quando você habilitar a opção **"Gravar número do livro no final?"**, o número do último livro será gravado e ao realizar a impressão do próximo livro, esta informação será recuperada através do campo Livro inicial.

A marcação **"Gerar termo de abertura apenas para primeiro livro"** permite que o termo de abertura seja impresso apenas para o primeiro livro.

Informe no campo **"Quantidade de páginas por livro"**, a quantidade máxima de páginas permitidas pela UF em cada livro, já incluindo a página de abertura e a página de encerramento, se for o caso.

Quando você efetuar a marcação **"Reservar número de pág. para termo de abertura"**, fará com que a página a ser impressa tenha o número da primeira página do livro. Portanto, uma página vazia será impressa, ocupando o lugar do termo de abertura do livro. Nesse caso, você deverá trocá-la pela página oficial de termo de abertura.

**Observação:** é importante que você atente para o fato de que a primeira página gerada pelo relatório, pode não ser a primeira página do livro.

Se você realizar a marcação **"Reservar número de pág. para termo de encerramento"**, fará com que a página a ser impressa tenha o número da última página do livro; então, uma página vazia será impressa, ocupando o lugar do termo de encerramento do livro. Nesse caso, você deverá trocá-la pela página oficial de termo de encerramento.

**Nota:** atente-se ao fato de que a última página gerada pelo relatório, pode não ser a última página do livro.

**Observação:**não será possível gerar o relatório nas seguintes situações:

- Se realizada as marcações Reservar número de pág. para termo de abertura, Reservar número de pág. para termo de encerramento e Reiniciar número da página por livro gerado, você deve preencher o campo Quantidade de páginas por livro.
- Se realizada as marcações Reservar número de pág. para termo de abertura, Reservar número de pág. para termo de encerramento e Reiniciar número da página por livro gerado, e você preencher o campo Quantidade de páginas por livro com número menor que 4.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#na)

## Seção Páginas

No campo **"Página Inicial"** é inserida a informação referente a primeira página do relatório que será gerado.

A marcação **"Grava página no final?"** quando realizada, o valor do campo **"Página inicial"** é atualizado com a numeração da **"Página final"** para que na próxima geração do relatório a numeração fique em sequência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#na)

## Seção Filtros

Nessa seção, com a marcação **"Carregar produtos sem giro"** realizada, serão considerados todos o produtos sem movimentações mas que possuam saldo de estoque.

É possível criar filtros específicos e personalizados para obtenção dos dados no relatório para Produtos com Giro e Produtos sem Giro através do botão ![Imagem 3: É possível criar filtros específicos e personalizados para obtenção dos dados no relatório para Produtos com Giro e…](https://ajuda.sankhya.com.br/hc/article_attachments/6302192736663).

**Observação:** os Filtros p/ Produtos sem Giro só serão habilitados para edição se a marcação Carregar produtos sem giro estiver efetuada. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#na)

## Geração do relatório

Na parte superior da tela temos a marcação **"Apresentar notas que não atualizam o Livro Fiscal"**; esta marcação quando realizada, mesmo as notas lançadas com TOP's que não atualizam Livros Fiscais, serão exibidas no relatório.

O botão ![Imagem 4: O botão "Visualizar" quando acionado, carrega na tela as informações resultantes dos filtros configurados.](https://ajuda.sankhya.com.br/hc/article_attachments/4416988047255) **"Visualizar"** quando acionado, carrega na tela as informações resultantes dos filtros configurados.

Assim, teremos o seguinte exemplo de um relatório gerado:

![Imagem 5: Assim, teremos o seguinte exemplo de um relatório gerado:](https://ajuda.sankhya.com.br/hc/article_attachments/4416983340823)

No final do relatório do Registro da Produção e do Estoque de cada produto, será apresentado o **"Saldo a Transportar"**, sendo que esse saldo será igual ao valor do Estoque do Total do Período.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque#na)
