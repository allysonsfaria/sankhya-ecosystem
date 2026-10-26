---
id: "360045110253"
titulo: "Ordem de Despacho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:29:56Z"
rotulos: ["AJUDA DO SKW", "manual", "Relatórios Formatados", "Parceiro", "NF-e", "Transportadora", "Pedidos de Frete", "br.com.sankhya.mgecom.menu.ordemdedespacho", "Ordem de Despacho manual", "Transporte", "MODELOPEDFRETE", "Ordem de Despacho", "Documento Mercadorias Transportadora", "Gerenciamento de Ordens de Despacho", "Documentos Eletrônicos", "Comercial"]
---

# Ordem de Despacho

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312028850967) Módulo: comercial > rotinas
```

---

O objetivo da tela Ordem de Despacho é gerar um documento que agrupe as notas fiscais correspondentes às mercadorias que serão conduzidas pelos parceiros Transportadora. Através dela é possível Incluir, Excluir, Editar e Concluir uma Ordem de Despacho, bem como Vincular e Desvincular notas fiscais a ela, Imprimir e Reimprimir a Minuta de Despacho e Visualizar os Pedidos de frete gerados pela Ordem de Despacho.

Vejamos sobre o comportamento da tela:

| [Filtrando Ordens de Despacho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho#filtrandoordensdedespacho) |  | [Grade Ordem de Despacho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho#gradeordemdedespacho) |
| --- | --- | --- |
| [Grade Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho#gradenotas) |  |  |

![clip6903](https://ajuda.sankhya.com.br/hc/article_attachments/360061918153)

## Filtrando Ordens de Despacho

O lado esquerdo da tela, além da possibilidade de criação de um Filtro personalizado, possui um agrupamento de filtros dividido em três quadrantes, que irão auxiliar na busca das Ordens de Despacho. Vejamos abaixo os tipos de filtros disponíveis:

![Imagem 3: O lado esquerdo da tela, além da possibilidade de criação de um Filtro personalizado, possui um agrupamento de filtros…](https://ajuda.sankhya.com.br/hc/article_attachments/360061918173)

#### Filtro

Tem-se neste quadrante os campos Ordem de Despacho, Empresa e Transportadora, ou seja, pode-se informar a própria numeração da Ordem de Despacho, a Empresa que realizou sua geração, bem como a Transportadora pela qual a mercadoria negociada foi conduzida.

#### Dados da nota

Uma Ordem de Despacho também pode ser localizada através das informações das Notas Fiscais que foram vinculadas à Ordem de Despacho. Pode-se fazê-lo por meio dos campos Data de negociação, Data de movimento, Número do documento, Número único ou ainda, a Chave NF-e.

#### Parceiros

Pode-se ainda, filtrar as Ordens de Despacho com base nos Parceiros para os quais as Notas Fiscais foram geradas. Pode-se Adicionar ou Remover os Parceiros a serem utilizados como filtro, sempre que necessário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho#top)

## Grade Ordem de Despacho

Na grade Ordem de Despacho, realiza-se a Inclusão, Exclusão e Edição de uma Ordem de Despacho. Ao iniciar sua inclusão, os campos Transportadora e Empresa serão de preenchimento obrigatório; os campos Nro. único, Dt. inclusão e Status serão alimentados automaticamente, sendo que este último, recebe o status de **"Aberta"** no ato da inserção da Ordem de Despacho.

![clip6904](https://ajuda.sankhya.com.br/hc/article_attachments/360061918193)

Por meio do botão ![clip6911](https://ajuda.sankhya.com.br/hc/article_attachments/360061918213), finaliza-se a Ordem de Despacho; na sua conclusão, serão gerados os pedidos de frete e impressão a Minuta de Despacho. Para geração dos pedidos de frete, através da tela **"Comercial > Consulta > Modelo de Notas e Pedidos"** deve-se configurar um modelo de nota e informar seu Número Único no parâmetro **"Modelo p/ pedidos de frete na Ordem de Despacho - MODELOPEDFRETE"**.

**Importante:** o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado no cadastro do modelo de nota na tela Comercial > Consulta > Modelo de Notas e Pedidos deve ser do tipo de movimento **"Pedido de Compra"**.

Além disso, os [Eventos para Cálculo de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603334-Eventos-para-C%C3%A1lculo-de-Frete) inseridos na [Tabelas para cálculo de frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599534-Tabelas-para-c%C3%A1lculo-de-frete), aba Rotas, campo Evento, devem possuir serviços vinculados a eles, pois estes serão utilizados para gerar os itens dos pedidos. As Tabelas para cálculo de frete devem estar com o campo Rateio frete adequadamente configurado, dentre as opções Metro Cúbico, Valor da nota ou Peso.

Para realizar a Impressão e Reimpressão da Minuta de Despacho por meio do botão **"Imprimir"** ![clip6912](https://ajuda.sankhya.com.br/hc/article_attachments/360061918233), deve-se nas [Preferência da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba Geral, preencher o campo **"Minuta de Despacho"**; efetua-se a prévia configuração deste modelo através da tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

O botão ![clip6914](https://ajuda.sankhya.com.br/hc/article_attachments/360060992934) pode ser utilizado para casos em que precisa-se incluir ou mesmo retirar algum documento da Ordem de Despacho.

O acionamento do botão ![clip6915](https://ajuda.sankhya.com.br/hc/article_attachments/360060992954) permite a visualização dos pedidos de frete gerados pela Ordem de Despacho.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho#top)

## Grade Notas

A grade Notas, é destinada à ![clip6910](https://ajuda.sankhya.com.br/hc/article_attachments/360061918253) e ![clip6909](https://ajuda.sankhya.com.br/hc/article_attachments/360060992974) da Ordem de Despacho por meio dos respectivos botões. É importante mencionar que uma Ordem de Despacho lida com notas relacionadas aos processos de saída, ou seja, notas de venda ou devoluções de compra; notas pertencentes a estes tipos de movimento, poderão ser vinculadas às Ordens de Despacho.

Ao acionar o botão Vincular notas, é aberto o pop-up **"Seleção de notas"** designado para a localização das notas fiscais que irão compor a Ordem de Despacho.

Além disso, ao lado dos botões mencionados, tem-se o campo **"Chave NF-e"** que pode ser preenchido com a chave da Nota Fiscal que deseja-se vincular à Ordem de Despacho. Feito este preenchimento, pressiona-se o botão **"Buscar"** para que o sistema localize o documento em questão e o apresente diretamente na grade de notas.

![clip6905](https://ajuda.sankhya.com.br/hc/article_attachments/360060992994)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253-Ordem-de-Despacho#top)

Veja também:

[Pedido de Frete na conclusão da Ordem de Despacho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599154-Pedido-de-Frete-na-conclus%C3%A3o-da-Ordem-de-Despacho)
