---
id: "360044606774"
titulo: "Devolução de Cheques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:40:45Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Aceita Devolução Individual?", "Compensação da Devolução", "Devolução de cheques", "Devolução individual de cheque", "Processar devolução de cheques", "br.com.sankhya.fin.cad.devolucaocheques", "Devolução de Cheques manual", "Financeiro", "Cheque", "Devolução", "Devolução de Cheques Automatizada", "Gerencia a devolução de cheques", "Seleção e devolução de cheques"]
---

# Devolução de Cheques

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312375193367) Módulo: Financeiro > Rotinas
```

---

Esta opção automatiza o processo de Devolução de Cheques. Esta tela pode ser utilizada, nos casos em que a empresa recebe um cheque como pagamento de uma dívida, baixa o lançamento, atualiza a movimentação bancária e o banco devolve o cheque por algum motivo.

Acesse os links abaixo para navegar de forma mais fácil nas funcionalidades desta tela:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#paineldefiltros)                                                                      [Movimentações bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#movimenta%C3%A7%C3%B5esbanc%C3%A1rias)

[Títulos financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#t%C3%ADtulosfinanceiros)                                                                  [Processar Devolução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#processardevolu%C3%A7%C3%A3o)

![Imagem 2: Títulos financeiros Processar Devolução](https://ajuda.sankhya.com.br/hc/article_attachments/360087614754)

## Painel de Filtros

Inicialmente, para utilização desta tela, você pode criar filtros personalizados, através do **"Assistente de filtro"**, de modo que sejam apresentados cheques específicos.

Abaixo do Assistente de filtro, são disponibilizados alguns campos que também são utilizados como filtro e que possibilitam a apresentação rápida dos cheques desejados.

No campo **"Tipo de Lançamento"** você pode definir se serão apresentados na tela os títulos de **"Receita"**, **"Despesa"** ou **"Ambos"**.

A definição realizada no campo Tipo de Lançamento, implica no seguinte comportamento:

- Quando definido como Despesa, ao processar a devolução, no pop-up **"Devolução de cheques"** que é aberto, no campo **"TOP Baixa"**, será possível pesquisar por Tipos de Operação de **"Recebimento"**;
- Sendo definido como Receita, no campo **"TOP Baixa"**, será possível pesquisar por Tipos de Operação de **"Pagamento"**;
- Caso o campo seja definido como Despesa ou Ambos, no campo TOP Baixa, será possível pesquisar por Tipos de Operação de Recebimento.

Informe no campo **"Data da baixa"** o intervalo em que os cheques foram baixados.

Preencha o campo **"Conta Bancária"**com a conta bancária relacionada aos cheques que você deseja visualizar.

Você pode determinar quais cheques serão apresentados, através do **"Parceiro"** relacionado aos mesmos.

Ao lado dos campos para filtragem dos cheques, são apresentadas duas grades disponibilizando os seguintes dados:

- Na [primeira grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#movimenta%C3%A7%C3%B5esbanc%C3%A1rias), são apresentados os títulos que já foram baixados e que fazem parte da tabela de **"Movimento Bancário"**.
- Na [segunda grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#t%C3%ADtulosfinanceiros) são apresentados os títulos correspondentes aos lançamentos selecionados na grade superior, mas com informações da tabela de **"Movimentação Financeira"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#top)

## Movimentações bancárias

Ao ser selecionado um título de Receita na grade **"Movimentações bancárias"**, na grade [Títulos financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#t%C3%ADtulosfinanceiros) serão apresentados também os títulos de Despesa vinculados à esta movimentação.

Temos os seguintes botões na grade Movimentações bancárias:

O botão ![Imagem 3: O botão "Processar Devolução" , p rocessa a devolução do valor total do título baixado, ou seja, se a baixa foi feita…](https://ajuda.sankhya.com.br/hc/article_attachments/16244274081175)**"Processar Devolução"**, processa a devolução do valor total do título baixado, ou seja, se a baixa foi feita com mais de um cheque, para todos eles são processados a devolução.

**Observação:** na utilização do botão Processar Devolução de movimentações de receita, se existirem movimentações de despesa baixadas relacionadas à movimentação de receita, não será possível realizar o procedimento, onde será apresentada a seguinte mensagem:

**"Quando existe pagamento de despesas com cheques, somente a opção 'Devolução Individual' é permitida".**

Através do botão ![Imagem 4: Através do botão "Preferências" , você realiza as definições de apresentação dos cheques de acordo com seu intervalo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16244070194455) **"Preferências"**, você realiza as definições de apresentação dos cheques de acordo com seu intervalo de vencimento, bem como as cores que irão caracterizar os títulos de Receita e Despesa. Ao acioná-lo, será aberta a seguinte tela:

[GIF animado: Imagem 5: Através do botão "Preferências" , você realiza as definições de apresentação dos cheques de acordo com seu intervalo de…](https://ajuda.sankhya.com.br/hc/article_attachments/360087618914)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#top)

## Títulos financeiros

Na grade inferior **"Títulos financeiros"**, temos o botão ![Imagem 6: Na grade inferior "Títulos financeiros" , temos o botão "Devolução Individual" , que é utilizada quando se deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/16244269274391)**"Devolução Individual"**, que é utilizada quando se deseja devolver um cheque que foi baixado em conjunto com outros pela baixa automática.

**Nota:** na utilização do botão **"Devolução Individual"** para movimentações bancárias de receita, para o título de receita a ser devolvido, será gerado um novo financeiro de receita com o mesmo valor do cheque; a fim de ser cobrado do cliente, será gerado um novo financeiro de despesa para que haja um reembolso ao fornecedor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#top)

## Processar Devolução

Ao clicar no botão ![Imagem 7: Ao clicar no botão Processar Devolução , ou em Devolução Individual , o sistema abrirá o assistente de Devolução de…](https://ajuda.sankhya.com.br/hc/article_attachments/16244274081175) Processar Devolução, ou em ![Imagem 8: Ao clicar no botão Processar Devolução , ou em Devolução Individual , o sistema abrirá o assistente de Devolução de…](https://ajuda.sankhya.com.br/hc/article_attachments/16244269274391) Devolução Individual, o sistema abrirá o assistente de Devolução de Cheques, que apresentaremos mais adiante nesta documentação.

Para processar a Devolução Individual, é necessária a seguinte configuração:

- Na tela [Históricos Lançamentos Bancários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606694-Hist%C3%B3ricos-Lan%C3%A7amentos-Banc%C3%A1rios), a marcação **"Aceita Devolução Individual?"** deve estar realiza, assim como na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), a opção **"Devolução Individual de Cheques"** somente será habilitada, se esta marcação estiver efetuada, além disso, o título deve estar baixado e não devolvido.
- Na realização da Devolução Individual, clicando no botão Devolução Individual**,** no assistente de Devolução de Cheques, o sistema apresenta o campo **"Valor"**, onde você informa o valor da devolução do cheque. O valor informado neste campo deve ser maior ou igual ao valor do cheque. Se não for informado nenhum valor, o sistema realizará a devolução utilizando o valor total do cheque.

Para realização de uma Devolução de Cheques, através dos botões Processar Devolução ou  Devolução Individual, pressionando um desses dois, teremos a seguinte tela:

[GIF animado: Imagem 9: Para realização de uma Devolução de Cheques , através dos botões Processar Devolução ou Devolução Individual ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360087617714)

Informe no campo **"Alínea"**, o tipo de alínea de Devolução do Cheque, ou seja, o motivo pelo qual o cheque foi devolvido. As alíneas são previamente cadastradas na tela [Alíneas de Devolução de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114713-Al%C3%ADneas-de-Devolu%C3%A7%C3%A3o-de-Cheques).

Preencha a **"Data"** em que o cheque foi devolvido.

**Nota:** caso o parâmetro **"Usar Dt.Dev.como Dt.Negociação na Dev.de Cheques? - DTNEGIGUALDTDEV"** esteja habilitado, o sistema substituirá a data de devolução pela data de negociação dos títulos gerados.

Informe no campo **"Valor"** o valor do cheque somado ao valor da taxa cobrada pelo banco (neste caso, na Devolução Individual).

Após o preenchimento destes campos, clique em **"Próximo"**, para acessar os passos relacionados à **"Compensação da Devolução"**:

[GIF animado: Imagem 10: Após o preenchimento destes campos, clique em "Próximo" , para acessar os passos relacionados à "Compensação da…](https://ajuda.sankhya.com.br/hc/article_attachments/360087617834)

Defina no campo **"TOP Baixa"**, a TOP que será utilizada na baixa do título de despesa gerado no financeiro.

**Observação:** os Tipos de Operação apresentados para pesquisa no campo TOP Baixa, seguem a definição realizada inicialmente no campo de filtro Tipo de Lançamento, ou seja:

- Se definido como Despesa, no campo TOP Baixa será possível pesquisar por Tipos de Operação de **"Recebimento"**;
- Sendo determinado como Receita, será possível pesquisar por Tipos de Operação de **"Pagamento"**;
- Caso o filtro seja definido como Ambos ou Despesa, a pesquisa poderá ser feita por Tipos de Operação de **"Recebimento"**.

Informe no campo **"Tipo de Título"**, o tipo de título de cheque devolvido que será utilizado na despesa.

No campo **"Natureza"** é feita a definição da Natureza da Devolução do Cheque.

O campo **"Conta"**deve ser preenchido com a conta bancária referente ao cheque.

Insira no campo **"Lançamento Bancário"** o tipo de lançamento bancário que será realizado; pode ser débito, crédito etc.

No campo **"Empresa Baixa"**, informe a empresa na qual será realizada a baixa do cheque.

O campo **"Histórico"** é destinado a vinculação de qualquer informação adicional a respeito da devolução do cheque.

Após o preenchimento dos campos obrigatórios, clicando em **"Próximo"**, será feito o direcionamento para a etapa **"Pendência"**:

[GIF animado: Imagem 11: Após o preenchimento dos campos obrigatórios, clicando em "Próximo" , será feito o direcionamento para a etapa…](https://ajuda.sankhya.com.br/hc/article_attachments/360087617954)

A TOP informada no campo **"Tipo Operação"** irá para o novo título de receita gerado no Financeiro. Para que o sistema não gere duplicidade de notas no livro fiscal, a TOP não deve atualizar Livros Fiscais e deve ser do tipo **"Financeiro"**.

Quando informada a **"Data do Vencimento"**, será colocada nos campos **"Data Vencimento"** e **"Data Vencimento Inicial"** da Movimentação Financeira para os novos títulos de receita gerados na devolução. Este campo será habilitado para quem possuir acesso à tela de [Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos). Somente pode ser usada se for Devolução Individual e a data informada deve ser maior ou igual (>=) a data da Devolução.

Efetuando a marcação **"Alterar Tipo de Título no original?"**, fará com que o sistema altere o tipo de título no registro que deu origem à devolução, além de alterar o tipo de título na **"Despesa"** gerada pela devolução de cheques, para o tipo de título informado na tela de devolução, campo **"Tipo de título"**.

Quando você efetuar a marcação **"Alterar Tipo de Título do(s) título(s) em aberto?"**, fará com que o sistema utilize o tipo de título informado na tela de devolução, no campo Tipo de título, lançando-o nos títulos de despesa e receita gerada pela devolução de cheques. Isso pode ser utilizado quando o parceiro trabalha com outro tipo de título para efetuar pagamento.

Se a marcação **"Passar o Nro Cheque p/o Nro Nota?"** estiver realizada, ao fazer a devolução do cheque, o número do cheque será inserido no campo **"Número Nota"** do título.

Quando a marcação **"Permitir devolução para títulos de receitas com comissão a ser paga?"** for efetuada, faz com que o sistema não critique a existência de comissão ainda não paga, e permite a devolução dos cheques. Se estiver desmarcada, o sistema barra a devolução de cheques quando houver comissão ainda não paga.

A marcação **"Bloquear Crédito do Parceiro?"** quando selecionada, realiza a marcação **"Bloquear venda a prazo"** da tela [Cadastros de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito), e registra no campo **"Motivo de Bloqueio"** o texto **"Devolução de cheques"**. Esta marcação está condicionada à opção **"Acessos Especiais"** referente à tela Cadastros de Parceiros.

Após o preenchimento dos dados, o botão **"Concluir"** caracteriza o fim do procedimento de Devolução do Cheque.

No momento em que for confirmada uma devolução, o sistema gera uma **"Receita"** pendente no Financeiro, e uma **"Despesa"** já baixada para compensar a devolução.

**Nota:** na **"Baixa"** de um título gerado pela devolução de cheques, ao clicar no botão de **"Pagamento com Vários Títulos"** presente na tela de baixa na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), o sistema apresentará a seguinte mensagem:

**"Título gerado pela devolução de cheque. Não pode ser baixado com vários títulos".**

Não é possível baixar um título originado da devolução de cheques através da opção **"Pagamento com Vários Títulos"**, pois esta opção modifica o título original e o histórico deste se perde.

Exemplo de devolução de título de despesa: A empresa emitiu um documento, para pagar uma despesa, mas este documento retornou do banco, digamos que por um erro de digitação, isso leva a empresa à emissão de uma devolução e à criação de um novo título de despesa.

**![Imagem 12: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/19834158865559) Informações adicionais:**

- Se o parâmetro **"Utiliza Sankhya Civil? - USASNKCIVIL"** estiver ligado, os títulos de Compensação e Pendência gerados, terão a **"Variação Cambial"** igual a do financeiro de origem.
- Quando o usuário trabalhar com Metas/Orçamentos, o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) e outros parâmetros utilizados para a devolução de cheques não devem ser iguais aos relacionados na tela [Configuração da Estrutura de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques#top)
