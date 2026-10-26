---
id: "360045107133"
titulo: "Configurações para Impressão de Boletos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107133-Configura%C3%A7%C3%B5es-para-Impress%C3%A3o-de-Boletos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:54:12Z"
rotulos: ["Configuração", "Impressão", "Relatórios Formatados", "Configurações para Impressão de Boletos manual", "Boleto", "Financeiro", "Configurações para Impressão de Boletos"]
---

# Configurações para Impressão de Boletos

Abaixo serão descritas as configurações necessárias para realizar a impressão de boletos:

Primeiramente, o modelo de Relatório Formatado no iReport deve ser cadastrado na tela [Modelos de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134-Modelos-de-Boleto-s-).

![Imagem 1: O Sankhya-Om não suporta impressão de boletos em formato " txt ."](https://ajuda.sankhya.com.br/hc/article_attachments/16117154856727) O Sankhya-Om não suporta impressão de boletos em formato **"txt."**

![Imagem 2: O Sankhya-Om não suporta impressão de boletos em formato " txt ."](https://ajuda.sankhya.com.br/hc/article_attachments/1500008094421)

Depois, vincule o modelo cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-) por meio do campo **"Número do relatório modelo"**.

![Imagem 3: Depois, vincule o modelo cadastrado na tela Modelos de Nota Fiscal/Duplicatas/Boletos por meio do campo "Número do…](https://ajuda.sankhya.com.br/hc/article_attachments/1500008095161)

Em seguida, no [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), habilite a marcação **"Emite"** e preencha os campos **"Modelo"** e **"Impressora"**.

![Imagem 4: Em seguida, no Cadastro de Contas , aba Boleto(s)/Duplicatas , habilite a marcação "Emite" e preencha os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007907602)

Realizados os procedimentos acima, na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), configure o campo **"Imprimir Pix/Boleto/Duplicata?"**, de forma a permitir a impressão de boletos.

![Imagem 5: Realizados os procedimentos acima, na tela Tipos de Negociação , aba Características , configure o campo "Imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/6987984888727)

Por fim, no Cadastro de [Tipo de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), selecione no campo **"Imprimir Pix/Boleto/Duplicata"** a opção **"Manual"** ou **"Na confirmação"** da nota.

![Imagem 6: Por fim, no Cadastro de Tipo de Operação – TOP , aba Impressão , selecione no campo "Imprimir Pix/Boleto/Duplicata" a…](https://ajuda.sankhya.com.br/hc/article_attachments/6988028182039)

**Nota:** deve haver harmonia entre essas configurações, pois elas estão interligadas. Por exemplo, se um usuário tentar emitir um boleto com uma TOP que não foi configurada para a emissão de boletos, ele não obterá sucesso, ou se utilizar um Tipo de Negociação que não permita emissão de boletos, ele também não obterá sucesso.

![Imagem 7: Ao selecionar um Tipo de Título na Central de Notas , e este título estiver com a marcação "Proibir impressão boleto?"…](https://ajuda.sankhya.com.br/hc/article_attachments/17549864134295) Ao selecionar um Tipo de Título na Central de Notas, e este título estiver com a marcação **"Proibir impressão boleto?"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) realizada, não será impresso como boleto e também não possuirá taxa de boleto. Portanto, ao confirmar a nota na [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), poderá ser observado que no rodapé da nota em que o tipo de título selecionado está com essa marcação efetuada, as linhas [Cód. Barras Receb.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) e **"Linha Dig. Receb."** não estarão preenchidas.
