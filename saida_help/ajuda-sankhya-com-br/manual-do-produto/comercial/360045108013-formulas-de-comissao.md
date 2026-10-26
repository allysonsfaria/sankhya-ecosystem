---
id: "360045108013"
titulo: "Fórmulas de Comissão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:28:06Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Fórmulas", "Vendedor", "Fórmulas de Comissão", "br.com.sankhya.formulas.comissao", "Fórmulas de Comissão manual", "CORE_E00433", "Comissão", "USAPROCCALCCOM", "Cálculo Fórmulas Comissões", "Fórmulas de Comissão: Configuração e Funcionalidades", "Comercial"]
---

# Fórmulas de Comissão

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311936932759) Módulo: Comercial > Avançado > Fórmulas
```

---

O Sankhya Om possui formas de cálculo de comissão por Produtos, Tipos de Negociação, Vendedor, Gerente, Executor, Perfil etc, que são campos disponíveis nos cadastros e o cálculo é realizado através da combinação destes valores. Esta junção de informações é realizada por meio desta tela.

Este cadastro conta, inicialmente, com o preenchimento manual e obrigatório do **"Código"** destinado à identificação da fórmula no sistema.

Em seguida, igualmente importante como a informação anterior, temos a **"Descrição da Fórmula"**, em que você informa uma nomenclatura que melhor identificará a fórmula cadastrada perante os demais cadastros.

| [Aba Região Própria Vendedor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#abaregioprpriavendedor) |  | [Aba Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#abaintegrao) |
| --- | --- | --- |
| [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#construtordeexpresses) |  | [Comissões por Meta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#comissespormeta) |
| [Considerações Importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#consideraesimportantes) |  |  |

## Aba Região Própria Vendedor

![Imagem 2: Aba Região Própria Vendedor](https://ajuda.sankhya.com.br/hc/article_attachments/360094138694)

Caso seja necessário, informe no campo **"Histórico"**, um histórico de comissões para a fórmula.

O campo **"Fórmula"** é destinado à criação da fórmula que irá calcular a comissão. Você pode utilizar do componente de [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213-Construtor-de-Express%C3%B5es).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#top)

## Aba Integração

Esta aba é habilitada através da ativação do parâmetro **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"**. Ela trata as funcionalidades para o cálculo das comissões por premiação; nesta rotina, configure as fórmulas que serão utilizadas no cálculo das premiações.

**Observação:** Ainda referente ao parâmetro acima, considere:

- Se ambos os parâmetros TRATAPREMIACAO e **"Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"** forem desligados, o tipo de integração no fechamento de comissão a ser utilizado será conforme o campo **"Gerar comissão para"** da tela [Fechamento de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o);
- Porém, quando apenas o parâmetro TRATAPREMIACAO for habilitado, o tipo de integração a ser utilizado será o do campo **"Tipo de Integração"** desta aba;
- Por fim, com o parâmetro FECHCOMVEN acionado, o sistema utilizará a informação do campo **"Tipo de fechamento de comissão"** da tela [Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral).

![Imagem 3: Por fim, com o parâmetro FECHCOMVEN acionado, o sistema utilizará a informação do campo "Tipo de fechamento de…](https://ajuda.sankhya.com.br/hc/article_attachments/360096410013)

Certas empresas promovem campanhas comerciais para incentivar as vendas, gerando para seus vendedores uma premiação especial, fora a comissão de venda. Além do cálculo das comissões, o sistema fará o cálculo destas premiações especiais. Tendo assim, comissões e premiações sendo calculadas sobre o mesmo fator gerador.

Realize o preenchimento dos seguintes campos:

Informe no campo **"Evento"**, um evento pessoal que será utilizado pela fórmula.

Defina no campo Tipo de Integração, o tipo de integração relacionado à fórmula e ao evento anteriormente selecionado dentre as seguintes opções:

- **Financeiro:** Através desta opção, será calculada para pagamento pelo financeiro;
- **Folha:** Por esta marcação, o pagamento se dará na folha de pagamento do vendedor;
- **Nenhuma:** Na utilização de outra forma de pagamento, defina o campo Tipo de Integração com esta opção, onde o sistema não gerará nem o Financeiro e nem a Folha.

**Nota:** Quando o Tipo de Integração for pela Folha, será possível indicar o Evento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#top)

## Construtor de Expressões

Por meio do botão ![Imagem 4: Por meio do botão "F(x) Construtor" , teremos o componente Construtor de Expressões . Para detalhes do funcionamento…](https://ajuda.sankhya.com.br/hc/article_attachments/16270334975127) **"F(x) Construtor"**, teremos o componente Construtor de Expressões. Para detalhes do funcionamento deste componente, acesse o link [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025394553-Construtor-de-Express%C3%B5es).

**Observação:** Ocorrerão casos onde será necessário utilizar as funções **"SEMENOR"** ou **"SEMAIOR"**. Estas funções tem o objetivo de calcular comissões por faixas de valores e possuem a seguinte estruturação:

SEMAIOR (referência, limite, valor) e SEMENOR (referência, limite, valor) em que,

**Referência -** É o resultado de uma expressão a partir de variáveis a serem criadas para busca de dados de uma meta específica (previsto e realizado);

**Limite -** É o valor limite de cada faixa; quando você utilizar a função SEMAIOR, será o limite mínimo (ou seja, fará o cálculo se o valor de referência for maior que o limite); quando você utilizar a função SEMENOR, será o limite máximo (ou seja, fará o cálculo se o valor de referência for menor que o limite)

**Valor -** É o resultado obtido entre o limite e o cálculo.

Abaixo temos um exemplo da função SEMENOR:

Supondo que as faixas de comissionamento sejam

- Cobertura de 80%: comissão de 1%;
- Cobertura de 85%: comissão de 2%;
- Cobertura de 90%: comissão de 3%;
- Cobertura de 95%: comissão de 4%;
- Cobertura de 100% ou mais: comissão de 5%.

Nesta situação, portanto, a fórmula seria assim:

SEMENOR(resultmeta / prevmeta \* 100 (codvendedor, codgrupoprod), 80,0, 85,1, 90,2, 95,3, 100,4, 5)

**Nota:** As funções SEMENOR e SEMAIOR não poderão ser utilizadas na criação de fórmulas no Sankhya Om.

**Observação:** No sistema, é possível que você utilize a função PREÇO. Abaixo, temos um exemplo da fórmula:

IF((queItens.VLRUNIT-queItens.VLRDESC)>=Preco(1,queItens.CODPROD,queCab.DTNEG),(queItens.VLRTOT-queItens.VLRDESC)\*(0.025),IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))<=0.01,(queItens.VLRTOT-queItens.VLRDESC)\*(0.025),IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))>=0.0101,IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))<=0.019,(queItens.VLRTOT-queItens.VLRDESC)\*(0.022),IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))>=0.0191,IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))<=0.038,(queItens.VLRTOT-queItens.VLRDESC)\*(0.019),IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))>=0.0381,IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))<=0.057,(queItens.VLRTOT-queItens.VLRDESC)\*(0.016),IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))>=0.0571,IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))<=0.076,(queItens.VLRTOT-queItens.VLRDESC)\*(0.013),IF(((Preco(1,queItens.CODPROD,queCab.DTNEG)-(queItens.VLRUNIT-queItens.VLRDESC)) / Preco(1,queItens.CODPROD,queCab.DTNEG))>=0.0761,(queItens.VLRTOT-queItens.VLRDESC)\*(0.01),0)),0)),0)),0)),0))) \* IF(queCab.TIPMOV='D',-1,1)

**Variáveis disponíveis no Construtor de Expressões:**

**CTIP:** % Comissão do Tipo de Negociação

**CPROV:** % Comissão do Vendedor no Cadastro de Produtos

**CPROG:** % Comissão do comissão do Gerente

**CVGP:** % Comissão por grupo de perfil do Cadastro de  Produtos

**CUGP:** % Comissão por grupo/perfil do Cadastro de Vendedores

**MIN:** Preço mínimo pela tabela de preço mínimo da região do Parceiro

**TAB:** Preço de tabela

**PILUCRO:** Aqui o sistema irá considerar o valor dessa variável igual ao % lucro do item, obtido na Análise de Rentabilidade. No mesmo local é calculado o % da variável PIMARGCONTRIB, utilizando o resultado da mesma query.

**PNLUCRO:** O sistema irá considerar o valor dessa variável igual ao % lucro da nota, obtido na Análise de Rentabilidade. No mesmo local é calculado o % da variável PNMARGCONTRIB, utilizando o resultado da mesma query.

**CHAMADOR:**

**N** para vendedor da Nota;

**V** para vendedor do Parceiro;

**A** para assessor do Parceiro;

**I** para vendedor dos Itens da Nota;

**E** para executante dos Itens da Nota.

**QUETOTALVENDAS.VALOR:** Através desta, temos o acesso ao somatório do VLRNOTA das linhas que foram selecionadas na tela de cálculo de comissão para o vendedor.

**QUEMIX.QTD:** Por meio desta variável, temos acesso à contagem de diferentes Códigos de Produto (CODPROD) das notas selecionadas na tela de cálculo. Não serão contados produtos da nota com USOPROD = 'D' (campo Usado como), ou seja, Matéria Prima.

**quePESONOTA.QTDITENSNOTA:** Para contar apenas produtos com USOPROD <> 'D', se na nota for utilizado o mesmo CODPROD duas vezes, será contado duas vezes; diferente da contagem do MIX. SUM(CASE WHEN ITE.USOPROD = 'D' THEN 0 ELSE 1 END) AS.

**Importante:** Os campos não devem ser utilizados no Pé da Nota na Fórmula. A comissão é o somatório das comissões dos itens.

**Observação:** Quando o parâmetro **"Usar procedure no Calculo de Comissão por Fórmula - USAPROCCALCCOM"** for ligado, o sistema irá utilizar as fórmulas cadastradas na procedure **"STP\_AVALIA\_FORM\_COMISSA"**, e não aquelas cadastradas nessa tela. Porém, quando o parâmetro for desativado, as fórmulas cadastradas aqui serão utilizadas normalmente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#top)

## Comissões por Meta

As variáveis **"queMeta.PREVISTA"** e **"queMeta.REALIZADA"** são alimentadas pelas metas prevista e realizada pertencentes ao módulo de Metas para o cálculo de comissão.

As funções **"queTotalVendasItem"** e **"queTotalVendasGerItem"**, buscam o valor das vendas realizadas pelo Gerente e pelos Vendedores ligados a ele, que estejam informados nos itens dos Pedidos/Notas, para realização do cálculo de comissão. Deste modo, a comissão de vendas será calculada não somente para o vendedor da Nota, mas também para o Vendedor do item da nota, assim como para o seu respectivo Gerente.

O parâmetro **"Código Meta para Gerente On line? - GOL-CODMETA"** influencia diretamente este comportamento, pois habilitará a query **"queMeta"** com os campos CODMETA, PREVDESP, PREVISTA, QTDPREV, QTDREAL, REALDESP e REALIZADA. Estes campos possibilitarão a construção de uma fórmula de comissão por meta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#top)

## Considerações Importantes

A interpretação de fórmulas do Sankhya Om funciona de maneira diferente do MGE, apesar da maioria das fórmulas serem compatíveis com os dois sistemas, existem casos em que são necessárias algumas adequações. Exemplos:

#### Caso 1)

Quando utilizamos a função 'TO\_CHAR' dentro de um PDES, por exemplo:

Pdes('SUM(MET.PREVREC)','TGFMET MET','TO\_CHAR(MET.DTREF,'MM')='+MES(queCab.DTNEG)+'AND TO\_CHAR(MET.DTREF,'YYYY')='+ANO(queCab.DTNEG))

Observe que dentro do TO\_CHAR temos que utilizar aspas simples ('') para o segundo argumento, que no caso é 'MM' e 'YYYY', esse TO\_CHAR é um argumento do PDES que já demanda aspas, dessa forma o sistema só conseguirá resolver a fórmula caso esteja explicito na fórmula que existe aspas dentro de aspas, o sistema reconhece que as aspas simples em 'MM' são delimitadoras da string e interpreta como se fosse 'TO\_CHAR(MET.DTREF,' + MM + ')=' e então, ocorrerá erro por MM não ser um valor ou variável válida. Para explicitar na fórmula que existem aspas dentro de aspas deve-se alterar as aspas internas para \', o PDES ficará assim:

Pdes('SUM(MET.PREVREC)','TGFMET MET','TO\_CHAR(MET.DTREF,\'MM\')='+MES(queCab.DTNEG)+'AND TO\_CHAR(MET.DTREF,\'YYYY\')='+ANO(queCab.DTNEG))

#### Caso 2)

Quando utilizar divisão nas fórmulas, é necessário o cuidado com o tipo dos dados que serão utilizados; existem casos em que para representar porcentagem, alguns preferem escrever (9/100) ao invés de (0.09); neste caso estaríamos cometendo um erro, pois o sistema interpreta o trecho 9/100 como sendo a divisão de dois inteiros, sendo assim ele retornará um inteiro, só que como a divisão resulta em 0.09 quando arredondado para inteiro o sistema retorna 0.

A solução é alterar todos os pontos que realizam este tipo de cálculo para (9.0/100), assim, será interpretado como a divisão de decimais e então retornará um decimal, que neste exemplo seria 0.09.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#top)
