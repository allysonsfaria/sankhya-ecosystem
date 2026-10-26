---
id: "360045115313"
titulo: "Impressão de Cheques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:26Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios", "Movimentação Financeira", "Financeiro", "Cheque", "Impressão de Cheques", "br.com.sankhya.fin.impressao.cheques.grafico", "Impressão de Cheques manual", "Baixe template formate com iReport crie e vincule modelo", "Selecione títulos ajuste filtros escolha parâmetros e imprima cheques", "Use variáveis e funções específicas configure impressora conforme manual"]
---

# Impressão de Cheques

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312483090455) Módulo: Financeiro > Relatórios
```

---

Para configurar a impressão de cheques você deve, primeiramente:

- Baixar o template do modelo de cheques, na tela [Modelos de cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074);
- Formatar o relatório, usando o iReport 4.0 ou superior, de acordo com os campos e dimensões da folha de cheque do banco usado;
- Criar um modelo de cheque e vinculá-lo à conta que será usada para efetuar os pagamentos.

Uma vez configurado o Modelo de Cheques, basta acessar a tela de Impressão de Cheques, selecionar os títulos e marcações e, usando a conta vinculada ao modelo, efetuar a impressão.

[Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#filtros)                                                                                 [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#botooutrasopes...)

[Aba Marcação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#abamarcao)                                                                  [Aba Parâmetros Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#abaparmetrosimpresso)

[Impressão de cheques em TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#impressodechequesemtxt)

![Imagem 2: Impressão de cheques em TXT](https://ajuda.sankhya.com.br/hc/article_attachments/360083846973)

**Observação:** na impressão de cheques, é possível realizar a configuração de algumas impressoras para modificar como os dados serão apresentados no cheque; para isto, fique atento ao manual e às funcionalidades de sua impressora. Por exemplo: para as impressoras PertoChek 501S e 502S, é possível imprimir os dados do cheque em negrito, habilitar a impressão do ano no cheque com 4 dígitos, habilitar o preenchimento dos espaços em branco do cheque com o caractere asterisco (\*), entre outras possibilidades. Os detalhes e configurações relacionados à estas funcionalidades, são encontrados no manual de cada impressora, disponível no site do fabricante da mesma.

**Nota:** de acordo com o tipo de banco de dados utilizado (Oracle, SQL Server, dentre outros) e suas respectivas versões, ao clicar no botão ![Imagem 3: Nota: de acordo com o tipo de banco de dados utilizado (Oracle, SQL Server, dentre outros) e suas respectivas versões,…](https://ajuda.sankhya.com.br/hc/article_attachments/16370484351383) **"Imprime os cheques marcados"**  o sistema poderá gerar a seguinte mensagem:

**"ORA-00600: código de erro interno, argumentos: [qctstc2o1], [1], [0], [0], [96], [0], [0], [ ]".**

Diante disto, é necessário que você realize as devidas configurações do parâmetro **"Campos p/ mod. cheque (TAB.CAMPO,TAB2.CAMPO2,...) - CAMPOSMODCHEQUE"**, conforme especificações contidas na tela Modelos de Cheques.

## Filtros

Informe o **"Número Financeiro"** caso queira somente filtrar um filtro para impressão do cheque.

Informe o **"Parceiro"** para filtrar os títulos lançados para este.

Preencha o campo **"Empresa"** para filtrar os títulos lançados para esta.

Informe no campo **"Vencimento"** o período de vencimento dos títulos

No campo **"Receita/Despesa"**, você pode selecionar uma das três opções: **"Receita"**, **"Despesa"** e **"Ambos"**. As receitas são representadas na grade pela cor azul, enquanto as despesas pela cor vermelha.

O campo **"Conta Bancária"** irá filtrar os títulos lançados para esta.

Preencha o **"Banco"** para filtrar os títulos lançados para este.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#top)

## Botão Outras Opções...

![Imagem 4: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/360083847033)

No botão Outras Opções..., existe a opção **"Reimprimir Cheques"** que serve para informar o número (ou intervalo de números) do cheque (nosso número) para reimprimir o cheque.

![Imagem 5: No botão Outras Opções... , existe a opção "Reimprimir Cheques" que serve para informar o número (ou intervalo de…](https://ajuda.sankhya.com.br/hc/article_attachments/360082676354)

Para facilitar o manuseio dos títulos na impressão do cheque referente à marcação do tipo de cheque como também o banco e a conta bancária, existe no sistema a opção de alterar todos os títulos da grade nestes quesitos. Para isto, é necessário efetuar o filtro com os títulos que serão emitidos os cheques e utilizar a opção **"Alteração Automática"**; ao acionar esta opção, será aberto o seguinte pop-up:

![Imagem 6: Para facilitar o manuseio dos títulos na impressão do cheque referente à marcação do tipo de cheque como também o banco…](https://ajuda.sankhya.com.br/hc/article_attachments/360083847113)

No campo **"Marcação do Cheque"** serão apresentadas as opções de Tipo de Marcação de Cheque para informar nas Despesas, sendo que você pode escolher dentre as seguintes marcações:

- Nominal ao histórico;
- Agrupar nominal ao banco de pagamento;
- Sem emitir cheque;
- Nominal ao banco de pagamento;
- Não nominal;
- Agrupar nominal ao fornecedor;
- Agrupar nominal ao histórico;
- Agrupar não nominal;
- Nominal ao fornecedor;
- Agrupar nominal à empresa;
- Nominal à empresa.

**Importante:** o ato de trazer títulos de receita na impressão de cheques é devido à necessidade de compensar o financeiro de forma que o cheque fique com o valor real a pagar ao fornecedor. Para isto, ao selecionar receitas, o sistema automaticamente trará para o campo Marcação do Cheque a opção de Agrupar nominal ao fornecedor e a emissão do cheque é feita somente para títulos de despesas.

**Observação:** caso seja selecionado somente um título de receita e solicite-se a emissão do cheque, o sistema avisa a não possibilidade da emissão.

Você deve informar o **"Banco"** que será alterado nos títulos selecionados. Trará na tela de pesquisa os bancos previamente cadastrados na tela [Bancos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894-Bancos).

Informe a **"Conta Bancária"** que será alterada nos títulos selecionados. Trará na tela de pesquisa as contas previamente cadastradas na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#top)

## Aba Marcação

![Imagem 7: Aba Marcação](https://ajuda.sankhya.com.br/hc/article_attachments/360083847653)

Um recurso interessante da tela de Impressão de Cheques é poder alterar a configuração da coluna **"Tipo Marcação Cheque"** na grade da aba Marcação para definir como agrupar os títulos em cheques. Os títulos que possuem a marcação **"Sem Cheque"** não serão agrupados. Quando ocorrer o erro **"Coleção de números de títulos financeiros não pode ser vazia!"**, verifique se os títulos que devem formar o cheque não estão com o campo Tipo Marcação Cheque preenchidos com a marcação Sem Cheque.

Seguem alguns detalhes sobre os tipos de opções existentes:

- **Nominal ao fornecedor:** Emitirá um cheque para cada título, o qual será nominal ao Fornecedor.
- **Agrupar nominal ao fornecedor:** Poderão ser reunidos vários cheques para o mesmo Parceiro; poderão ser cheques de receitas e de despesas (vale ressaltar que um Parceiro poderá ser cliente e fornecedor ao mesmo tempo. Por isto, pode haver receitas e despesas para o mesmo Parceiro). Este tipo de opção, reunirá todos os cheques do mesmo Parceiro com esta opção selecionada e calcular a diferença entre as receitas e despesas, sendo que as despesas devem ser maiores do que as receitas, emitindo um cheque com o resultado.
- **Nominal ao banco de pagamento:** Emitirá um cheque para cada despesa, o qual será nominal ao banco de pagamento.
- **Agrupar nominal ao banco de pagamento:** Agrupa como na opção Agrupar nominal ao fornecedor. Neste caso, será nominal ao banco e não podem ser utilizadas receitas. Exemplo: imprimir um cheque para o pagamento no banco de várias despesas (água, energia, aluguel)
- **Não nominal:** O campo Nominal ficará em branco.
- **Agrupar não nominal:** Esta opção é utilizada quando existem várias despesas a serem pagas que podem ser reunidas e pagas com um único cheque. Neste caso, todos os cheques deverão estar com a mesma opção selecionada. Por exemplo, um cheque para ser descontado no banco para pagar várias contas pequenas.
- **Nominal ao histórico:** Será emitido um cheque para cada despesa que será nominal ao histórico.
- **Agrupar nominal ao histórico:** Vários cheques com o mesmo histórico que serão reunidos e emitidos um cheque com o valor total.
- **Nominal à empresa:** Nominal à empresa, utilizada em transferências de valores.
- **Agrupar nominal à empresa:** Vários cheques nominais à empresa, utilizada no caso de transferência de valores entre contas da empresa.
- **Sem emitir cheque:** O cheque não será emitido.

**Observação:** a ordenação da impressão do cheque é definida pela opção selecionada no campo Tipo Marcação Cheque.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#top)

## Aba Parâmetros impressão

![Imagem 8: Aba Parâmetros impressão](https://ajuda.sankhya.com.br/hc/article_attachments/360082677194)

Informe no campo **"Conta bancária"** a conta bancária para a baixa dos títulos.

Se a marcação **"Gerar o Número do Cheque (nosso número)?"** for selecionada, o número do cheque a ser gerado será registrado no campo Nosso Número da tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874).

**Número do próximo cheque:** Ao selecionar a conta bancária, será apresentado o último número de cheque impresso para esta conta. Este número é configurado no cadastro da conta bancária e é incrementado automaticamente. Caso seja necessário alterar o número, basta subscrevê-lo ou alterá-lo no [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros), campo **"Último nro. cheque"**.

**Nota:** se o Último nro. cheque for alterado, ao solicitar a impressão dos cheques, o sistema emitirá o aviso: **"Você poderá provocar repetição de número de Cheque! Tem certeza que quer alterar para este número?"**. Clicando em **"Sim"**, o número informado é mantido. Clicando em **"Não"**, o sistema retorna a numeração automática antes da alteração;

Efetuando a marcação **"Valor líquido"**, será impresso no cheque o valor líquido do título, que pode ser configurado em [Componentes do Valor Líquido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607174). Exemplo: será considerado o seguinte cálculo: valor do desdobramento + juros – desconto;

No campo **"Data a ser impressa no cheque"**, selecione a data a ser gerada no cheque que será impresso, as opções são: a data da **"Baixa"** do título, a data do **"Vencimento"** do título, ou ainda a opção **"Fixa"**, sendo que, quando esta última for selecionada, será necessário informar a data;

Caso você deseje que o tipo de título gravado no financeiro seja alterado, basta realizar a marcação **"Alterar o tipo de título?"**. Normalmente, quando emitimos cheques, informamos, neste campo, o tipo de título cheque pagamento;

Quando a marcação **"Gerar cópia do cheque"** for realizada, será gerada uma cópia.

#### Seção Dados da baixa

Ao realizar a marcação **"Efetuar baixa** **automática?"**, o lançamento será automaticamente baixado após a impressão do cheque. Para isto, preencha os campos referentes à baixa: **"Lançamento bancário"**, **"Top despesa"** e **"TOP Receita"**.

O campo **"Dt. Mov. Bancário"** será habilitado para utilização se a marcação Efetuar baixa automática estiver realizada. Neste campo, é informada a data do movimento bancário que será registrada para o título, na realização da baixa automática. É possível realizar o preenchimento de uma data menor que a data corrente, para isto, deve-se habilitar o parâmetro **"Permite Dt.Mov.Bancário retroativa (Imp. Cheques) - BAIRETROIMPCHEQ"**. Além disto, a data informada no campo Data a ser impressa no cheque não poderá ser menor que a data informada neste campo (Dt. Mov. Bancário).

Veja como enviar cheques por e-mail clicando no link: [Conhecendo o Sankhya Om/Envio de Relatórios por Email](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934-Conhecendo-o-Sankhya-W#envioderelatriospore-mail).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#top)

## Impressão de Cheques em TXT

Para imprimir cheques utilizando modelos TXT, é necessário criar o modelo, colocá-lo no [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos), através do botão **"Propriedades"** e na tela que se abre, clicar no botão **"Copiar Caminho"**.

![Imagem 9: Para imprimir cheques utilizando modelos TXT, é necessário criar o modelo, colocá-lo no Repositório de Arquivos ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360083847733)

Em seguida, incluir este caminho na tela [Modelos de cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607074).

![Imagem 10: Em seguida, incluir este caminho na tela Modelos de cheques .](https://ajuda.sankhya.com.br/hc/article_attachments/360083847833)

Segue abaixo a lista de variáveis suportadas:

&VALOR\_TOTAL

&EXTENSOL1

&EXTENSOL2

&NOMINAL

&DATA\_EXTENSO

&DATA\_DIA

&DATA\_MES

&DATA\_ANO

&NUMERO\_CHEQUE

&MOV\_NUMTRANSF

&MOV\_HISTORICO

&MOV\_CODCTAORG

&MOV\_DESCRCTAORG

&MOV\_CODCTADEST

&MOV\_DESCRCTADEST

**Variáveis Adicionais (Primary Keys para PDES):**

&EMP\_COD\_EMPRESA

&END\_CODENDERECO

&PAR\_COD\_PARCEIRO

&CUS\_CENTRO\_DE\_RESULTADO

&VEN\_CODIGO

&TOP\_DATA\_E\_HORA\_ALTERACAO

&CTA\_CODIGO\_DA\_CONTA\_BANCARIA

&NAT\_NATUREZA

&TOP\_COD\_TIPO\_DE\_OPERACAO

&CTT\_PARCEIRO

&BCO\_COD\_BANCO

&CTT\_CONTATO

**Observação:** também é possível utilizar funções. Abaixo temos um exemplo:

**&pdes('NOMEBCO', 'TSIBCO', 'CODBCO = ' + &BCO\_COD\_BANCO) -** Retorna a descrição do banco.

**&formatNumeric("#,##0.00;(#,##0.00)", &VALOR\_TOTAL, 10) -** Formata o valor do cheque. O número "10" representa a largura em caracteres, que serão preenchidos à esquerda caso necessário. Desta maneira o número virá alinhado à direita.

**Variáveis que representam comandos para impressora:**

![Imagem 11: Caso você necessite de algum comando que não conste na lista acima, basta inserir os caracteres, diretamente no modelo,…](https://sankhyasd.zendesk.com/hc/article_attachments/360056826313/embim572.jpg)Caso você necessite de algum comando que não conste na lista acima, basta inserir os caracteres, diretamente no modelo, conforme lista disponível no manual da impressora.

![Imagem 12: No exemplo, basta inserir no modelo o caractere correspondente ao ESC e a letra M .](https://sankhyasd.zendesk.com/hc/article_attachments/360056826333/embim573.jpg)No exemplo, basta inserir no modelo o caractere correspondente ao ESC e a letra M.

![Imagem 13: No exemplo, basta inserir no modelo o caractere correspondente ao ESC e a letra M .](https://ajuda.sankhya.com.br/hc/article_attachments/360082677394)

O próprio Notepad++ possui um Painel (**Editar > Painel de Caracteres**) de caracteres onde você poderá escolher tais caracteres especiais, como o ESC utilizado neste exemplo.

![Imagem 14: O próprio Notepad++ possui um Painel ( Editar > Painel de Caracteres ) de caracteres onde você poderá escolher tais…](https://ajuda.sankhya.com.br/hc/article_attachments/360082677514)

**Nota:** para que as variáveis da impressora sejam processadas, o tipo da impressora que será utilizada será o tipo definido no [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) (aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), campo **"Tipo impressora"**). Caso não se tenha a informação do tipo da impressora na conta bancária, será utilizado o tipo configurado no parâmetro **"Tipo de Impressora - TIPOIMP"**.

Para maiores informações acesse [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

**Observação:** o parâmetro **"Charset para processamento de impressão de cheques - PROCCHEQCHARSET"** irá tratar os problemas de charset na impressão de cheque, por isso, observe em qual charset a impressora está tentando imprimir e indique o mesmo nesse parâmetro.

**Importante:** acione o parâmetro **"Imprimir cheques suprimindo caracteres especiais? - IMPCHEQUESEMCS"** para que os caracteres especiais sejam substituídos por letras comuns.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques#top)
