---
id: "360044606014"
titulo: "Associar autenticação do DAE e GNRE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:12Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Arrecadação", "Associar notas", "DAE", "Excluir associação", "TIPTITDAE", "TIPTITGNREST", "br.com.sankhya.associarautenticacaododaeegnre", "Associar autenticação do DAE e GNRE manual", "Impostos", "GNRE", "Financeiro", "Filtros e grade", "Tela: Autenticação de Títulos", "Associação de notas", "Documentos Eletrônicos"]
---

# Associar autenticação do DAE e GNRE

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312272672279) Módulo: Financeiro > Rotinas             
```

---

Através desta tela, você realiza a autenticação dos títulos gerados pelo financeiro, que foram gerados utilizando os tipos de títulos informados nos parâmetros **"Tipo de título p/ Documento de Arrecadação - TIPTITDAE"** e **"Tipo de título p/indicar GNRE p/S.T. - TIPTITGNREST"** e associa-os às notas fiscais, conforme necessário.

**Observação:** Esta tela será apresentada para utilização apenas se os parâmetros mencionados acima estiverem com valores diferentes de **"0"** (zero).

**Importante:** Para que os títulos sejam apresentados nesta tela, preencha o campo **"Cód. Parceiro Secretaria da Receita Estadual"**, localizado no [Cadastro de Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294).

**Nota:** As buscas realizadas nesta tela serão realizadas, primeiramente, considerando a **"Observação"** informada nos Itens e, em segundo momento, a inserida no Cabeçalho da Nota. Assim, é indispensável que seja vinculada uma observação nos mesmos. A Observação será buscada primeiramente TGFITE e, caso não seja encontrada, o sistema buscará na TGFCAB.

Acesse os links abaixo para facilitar sua navegação nas funcionalidades desta tela:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE#abaparcelasorigem)                                               [Grade Superior - Títulos do Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE#gradesuperior-t%C3%ADtulosdofinanceiro)

[Grade Inferior - Notas Vinculadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE#gradeinferior-notasvinculadas)

![Imagem 2: Grade Inferior - Notas Vinculadas](https://ajuda.sankhya.com.br/hc/article_attachments/360095906294)

## Painel de Filtros

A tela é composta, primeiramente, por filtros que irão te auxiliar na apresentação dos títulos do financeiro. Através do **"Assistente de Filtro"**, localizado no topo da tela, você pode realizar a criação de um filtro personalizado, de modo que sejam exibidos títulos em específico. Além disso, você pode utilizar de alguns campos que te auxiliarão na filtragem dos documentos, são eles:

**Empresa:** Informe a Empresa na qual os títulos foram gerados no financeiro.

**Parceiro:** Caso seja necessária a apresentação de títulos gerados para um Parceiro em particular, preencha o Parceiro desejado neste campo.

**Data da baixa:** Temos também, a possibilidade de filtrar os títulos buscando-os por um intervalo de tempo em que estes foram baixados.

**Autenticação:** Você pode restringir a exibição dos títulos de acordo com a autenticação que estes sofreram ou não, dentre as seguintes alternativas para escolha:

- **Não autenticados:** Títulos que não possuem o número da autenticação bancária informado no campo Histórico;
- **Autenticados:** Títulos que possuem o número da autenticação bancária informado no campo Histórico;
- **Ambos.**

**Documento de Arrecadação:** É possível filtrar os títulos de acordo com o documento de arrecadação de cada um deles, de acordo com as seguintes opções:

- **GNRE:** Serão apresentados somente os documentos vinculados ao parâmetro TIPTITGNREST;
- **DAE:** Serão exibidos somente os documentos relacionados ao parâmetro TIPTITDAE;
- **Ambos**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE#top)

## Grade Superior - Títulos do Financeiro

Finalizada a formulação dos filtros, quando você clicar em **"Aplicar"**, os títulos gerados diretamente no financeiro como **"Despesa"**, que tenham seus tipos de títulos informados nos parâmetros inicialmente mencionados, serão apresentados na grade superior da tela.

![Imagem 3: Finalizada a formulação dos filtros, quando você clicar em "Aplicar" , os títulos gerados diretamente no financeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/360098198433)

A autenticação nos títulos gerados pelo financeiro é feita informando-se o número da autenticação no campo **"Histórico"**, uma vez que este campo é editável nesta tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE#top)

## Grade Inferior - Notas Vinculadas

Nesta grade, você vincula as notas à cada título financeiro da grade superior. Com um título selecionado na grade superior, associe-o às notas que forem desejadas.

Para realização do vínculo, é necessário que as notas escolhidas tenham a **"Observação Padrão"** informada na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474-Observa%C3%A7%C3%B5es-para-Notas); além disso, na configuração desta Observação Padrão, é necessário que a marcação **"Vincular DAE/GNRE"** esteja efetuada.

Note, juntamente à grade inferior, a existência de dois botões, **"Associar nota(s)"** e **"Excluir associação"**; o primeiro é responsável pela realização do vínculo entre o título do financeiro e a nota que, ao ser acionado, abrirá a seguinte tela:

![Imagem 4: Note, juntamente à grade inferior, a existência de dois botões, "Associar nota(s)" e "Excluir associação" ; o primeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/360095906474)

Na tela para escolha das notas a serem associadas ao título, podemos filtrá-las através do **"Assistente de Filtros"**, ou ainda, utilizarmos dos campos **"Empresa"**, **"Parceiro"**, **"Nro da nota"**, **"Data de negociação"** e **"Data de movimentação"** para apresentação dos documentos.

Definidos os filtros e clicando em **"Aplicar"**, você realiza a escolha das notas e, através dos botões **"Remover selec."** ou **"Remover NÃO selec."**, poderá retirar da tela as notas que não farão parte do procedimento no momento.

Escolhidas as notas, clique em **"OK"** para que a associação seja feita e a nota seja apresentada na grade inferior da tela, como podemos notar na imagem abaixo:

![Imagem 5: O botão "Excluir associação" , desfaz a associação realizada entre os títulos do financeiro e as notas. Ao acioná-lo,…](https://ajuda.sankhya.com.br/hc/article_attachments/360098198753) O botão **"Excluir associação"**, desfaz a associação realizada entre os títulos do financeiro e as notas. Ao acioná-lo, será apresentada uma mensagem de confirmação do procedimento e, escolhendo a opção **"Sim"**, o vínculo estará desfeito.

[GIF animado: Imagem 6: O botão "Excluir associação" , desfaz a associação realizada entre os títulos do financeiro e as notas. Ao acioná-lo,…](https://ajuda.sankhya.com.br/hc/article_attachments/360095906714)

Abaixo, temos um exemplo de utilização desta tela:

Pode ocorrer a situação em que determinados produtos na(s) nota(s) de entrada, a UF de origem não possua convênio com a UF de destino, de forma que o fornecedor possa destacar a substituição tributária na nota e recolher na UF de destino. Neste caso, é emitida a **"Guia de Recolhimento"** (GNRE) ou o DAE deste imposto (popularmente conhecido como ST de barreira); no sistema, você realiza o registro das notas de compras e a GNRE no financeiro. Logo, quando temos a autenticação do pagamento desta guia, na tela Associar autenticação do DAE/GNRE, informamos o número dessa autenticação do título e podemos associá-lo à(s) nota(s) que geraram o referido recolhimento.

**Observação 1:**O vínculo com as notas é realizado, independentemente, de ter sido feita a autenticação do titulo, ou seja, se filtrar o título do financeiro na grade superior, ao clicar no botão **"Associar nota(s)"** da grade inferior, será permitido selecionar e associar conforme necessário.

**Observação 2:** A associação do título pode ser feita a mais de uma nota, porém, este procedimento deverá ser feito individualmente, ou seja, é possível selecionar apenas um título por vez na grade superior para realizar sua associação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE#top)
