---
id: "360045113573"
titulo: "Reajuste de Contratos Ativos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:05:43Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Contrato", "Moeda", "Bonificados", "Cancelados", "REAJAPARTDTBASE", "Reajuste de Contrato Proporcional à Inclusão do Módulo", "Reajuste de Contratos", "Reajuste de Contratos Ativos", "Suspensos", "br.com.sankhya.mgeos.reajuste.contrato", "Reajuste de Contratos Ativos manual", "Reajuste", "Financeiro", "Reajuste de Contratos Ativos: Procedimentos e Configurações"]
---

# Reajuste de Contratos Ativos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311300493463) Módulo: Contratos e Serviços > Rotinas
```

---

Esta tela reajustará os contratos, gerando um lançamento com o novo valor para cada produto ativo em conjunto com uma ocorrência, que indicará em sua descrição, o índice calculado, o período de pesquisa do índice e atualizará a Data Base para Reajuste do contrato.

[Informações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#informa%C3%A7%C3%B5esiniciais)                                                              [Regra de Arredondamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#regradearredondamento)

[Detalhes sobre o cálculo do Reajuste](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#detalhessobreoc%C3%A1lculodoreajuste)                              [Definição da Moeda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#defini%C3%A7%C3%A3odamoeda)

[Reajuste de Contrato Proporcional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#reajustedecontratoproporcional)                                   [Cálculo do Índice de Reajuste](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#c%C3%A1lculodo%C3%ADndicedereajuste)

[Reajuste de Contrato com a Data Base](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#reajustedecontratocomadatabase)                            [Reajuste para Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#reajusteparaprodutos)

[Contratos Inativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#contratosinativos)

![Imagem 2: Contratos Inativos](https://ajuda.sankhya.com.br/hc/article_attachments/1500019517621)

## Informações Iniciais

Esta rotina também permite a visualização do índice, valor atual e contratos a serem reajustados, antes que o processo seja executado, dando uma maior segurança na execução da rotina.

Através do Painel de Filtros, ao lado esquerdo da tela, você define alguns parâmetros para que, ao aplicar, a tela apresente apenas os contratos que atendem os critérios definidos, sendo eles:

- Empresa;
- Parceiro;
- Moeda;
- Produto;
- Receita / Despesa.

Se você acionar o botão ![PRÉ](https://ajuda.sankhya.com.br/hc/article_attachments/15468731981975), localizado no topo da tela, será aberto o pop-up **"Pre visualização de reajuste"** com a simulação do reajuste para os contratos apresentados na tela e exibirá os novos valores dos contratos a serem reajustados. Nesse pop-up, temos os seguintes campos:

- Contrato;
- Parceiro;
- Cod.Produto;
- Descrição;
- Valor Reajuste;
- Indice de Reajuste.

Ainda no topo da tela, temos os botões ![Imagem 4: Ainda no topo da tela, temos os botões "Remover selecionados" e "Remover não selecionados" que têm a funcionalidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019270362) **"Remover selecionados"**e **![Imagem 5: Ainda no topo da tela, temos os botões "Remover selecionados" e "Remover não selecionados" que têm a funcionalidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019517761) "Remover não selecionados"** que têm a funcionalidade de remover os itens que não se deseja visualizar na grade.

**Observação:** O Reajuste é mensal.

**Notas:**

- Não serão considerados contratos com moeda = 0 ou sem moeda;
- Não serão considerados produtos bonificados, suspensos, cancelados ou sem valor;
- O sistema verificará se a quantidade de índices lançados corresponde à frequência de reajuste, o que implica que deverá existir um lançamento na tabela de cotação para todos os meses, mesmo para aqueles em que o índice não possui valor.

**Observação:** Será possível realizar o Reajuste de Contratos com índice negativo quando, na tela [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades), a marcação **"Aceita reajuste com índice negativo"** estiver habilitada.

Como a preparação do faturamento, normalmente, é realizada no mês anterior à referência, você deve realizar o reajuste no mês desta preparação.

Usualmente, não haverá o índice para o mês, por serem divulgados no último dia. Isto obriga a pegar como período para índices da data base do reajuste, - 1 mês até a data base do reajuste + frequência - 1.

Vejamos alguns exemplos:

Data Base para Reajuste 04/2002 e Frequência de Reajuste 3:

O início será 01/03/2002 e o fim será 31/05/2002; a próxima Data Base para Reajuste será 01/07/2002 e, assim que for reajustar novamente, pegará de 01/06/2002 a 30/09/2002.

Data Base para Reajuste 04/2002 e Frequência de Reajuste 12:

O início será 01/03/2002 e o fim será 28/02/2003; a próxima Data Base para Reajuste será 01/04/2003 e, assim que for reajustar novamente, pegará de 03/2003 a 02/2004.

No faturamento de 02/2003, que é referente ao mês 3, este contrato não sofrerá reajuste.

No faturamento de 03/2003, que é referente ao mês 4, ele será reajustado.

O tratamento dos meses será assim: nunca considerar o dia, nem para índice e nem para valor.

Ao faturar, o sistema passará os contratos selecionados em revista para saber se algum precisa ser corrigido e, caso isto ocorra, impedirá o faturamento, avisando o número do contrato. Neste momento, será possível checar se seus índices estão cadastrados e usar a sua nova opção.

**Importante:** Para que os registros sejam apresentados, o sistema segue uma configuração padrão para esta tela, que trará apenas os contratos que respeitam a seguinte condição:

- Com o parâmetro **"Permite novo reajuste de contrato? - NOVOREAJCONT"** ligado:

Data base reajuste + (Frequência reajuste -1) <= "Último dia do Mês atual".

Frequência: 3 meses

Contrato "X"

Data Base Reajuste: 01/01/2015

Data do Servidor: 11/02/2015 (Data do computador)

Como a frequência desse contrato é de 3 meses, a **"Data para Reajuste"** deverá ser 01/03/2015.

A data para reajuste no caso do parâmetro ligado é sempre um mês antes do mês ao qual o contrato será faturado. Portanto:

01/01/2015 + (3 - 1) = 01/03/2015

A data limite será sempre o último dia do mês atual; nesse caso estando-se no mês 02, a data limite será 28/02/2015.

- Com o parâmetro de chave NOVOREAJCONT desligado:

Data base reajuste + (Frequência reajuste -2) <= "Último dia do Mês atual".

Frequência: 3 meses

Contrato "Y"

Data Base Reajuste: 01/03/2015

Data do Servidor: 16/04/2015 (Data do computador)

Data limite: 30/04/2015 (último dia do mês atual)

Como a frequência desse contrato é de 3 meses, a **"Data para Reajuste"** deverá ser 01/04/2015.

A data para reajuste no caso do parâmetro desligado é sempre um mês antes do mês ao qual o contrato será faturado. Portanto:

01/03/2015 + (3 - 2) = 01/04/2015

A data limite será sempre o último dia do mês atual; nesse caso estando-se no mês 04, a data limite será 30/04/2015.

**Nota:** A validação acima mencionada é realizada de maneira igual na tela de Reajuste de Contratos Ativos e na tela de [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654).

**Observação:** Mesmo em casos onde o produto possua um preço futuro, o sistema buscará o último preço em vigor para realizar o reajuste do contrato.

**Observação:** Por meio da tela [Agendador de Reajuste de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403554832023), você pode configurar o sistema para que os contratos sejam reajustados automaticamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Regra de Arredondamento no Reajuste Automático de Contratos

O campo **"Ajuste de Valor"** apresenta as opções de **"Arredondar"** e **"Truncar"**, que atuarão da seguinte forma:

- **Arredondar:** Quando marcada, se o algarismo decimal seguinte ao indicado no campo Casas decimais, for menor que 5, o anterior não se modificará. Exemplo: 100,49 = 100,00. Se o campo de casas decimais for maior que 5, o anterior será incrementado em uma unidade. Exemplo: 100,51 = 101,00.
- **Truncar:** Quando marcada, o sistema irá ignorar os decimais após a quantidade de casas decimais. Exemplo: 100,49 = 100,40.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Detalhes sobre o cálculo do reajuste

1. No cálculo do reajuste, o valor atual do contrato é multiplicado por um fator calculado, de acordo com a moeda de reajuste.
2. Quando a moeda é índice, o fator é calculado tomando-se como base todos os índices dentro do período de reajuste.
3. Quando a moeda é valor, o fator é calculado dividindo-se o último valor pelo primeiro valor do período de reajuste.
4. De acordo com a nova regra implementada, calcula-se o fator de reajuste considerando-se a moeda principal; caso o fator seja menor que 1, calcula-se o fator pela moeda alternativa, caso ela exista. Se o resultado final do fator for menor que 1, ele será considerado como igual a 1, ou seja, o valor do contrato não sofrerá alteração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Definição da Moeda

O parâmetro **"Uso de moeda em reajuste de contrato - MOEREAJCON"** serve para definir qual moeda (Moeda ou Moeda Alternativa) será utilizada para reajuste dos produtos/serviços do contrato. O parâmetro contém 3 opções:

- **Usar alternativa quando moeda principal negativa:** Este é o padrão do parâmetro. Esta opção fará com que o reajuste utilize a moeda alternativa apenas quando a moeda principal for negativa.
- **Usar a de maior índice:** A moeda que tiver maior índice será utilizada.
- **Usar a de menor índice:** A moeda que tiver menor índice será utilizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Reajuste de Contrato Proporcional à Inclusão do Módulo

No sistema, é possível que você efetue o reajuste de contratos para produtos, através da última data de ocorrência deste no contrato.

Para utilizar esta funcionalidade, é necessário habilitar o parâmetro **"Reajuste de contrato proporcional à inclusão do módulo-  REAJCONTPORPROD"**. Se habilitado, efetuará o reajuste conforme data de inclusão do produto, se não, levará em conta a data base reajuste do contrato.

No caso do Contrato, devemos cadastrar apenas os produtos com as suas respectivas ocorrências e valores.

![Imagem 6: No caso do Contrato , devemos cadastrar apenas os produtos com as suas respectivas ocorrências e valores.](https://ajuda.sankhya.com.br/hc/article_attachments/9906619662871)

**Nota:** Na rotina de Reajuste de Contratos Ativos, caso haja no contrato algum produto que não possua ocorrência, será exibida a seguinte mensagem:

**"O produto/serviço X do contrato X não possui ocorrência. Para que seja possível realizar o reajuste é necessário que seja incluída uma ocorrência para o produto/serviço informado".**

Com todas as configurações feitas, o sistema fará o reajuste, no caso do contrato exemplo, segue:

Contrato: 42

Data Base de Reajuste: 01/12/2013

Frequência: 2

Produtos:

NUMCONTRATO|CODPROD|SITPROD

42         |8159   |Ativo

Preço:

NUMCONTRATO |CODPROD  |REFERENCIA |VALOR

42                    |8159          |01/12/2013 |100

Ocorrência:

NUMCONTRATO |CODPROD   |DTOCOR                |OCORRENCIA

42                    |8159          |01/12/2013            |Ativo

Depois de feito o reajuste, no contrato fica:

SELECT

 cotacao

FROM TSICOT WHERE CODMOEDA=10 AND DTMOV>='01/01/2014' AND DTMOV<'01/03/2014'

Índice = 1

Índice = 1 \* (1 + 2/100)=1,02

Índice = 1,02\* (1 + 4/100)=1,0608

2.01 -> 1,0608 - 1 \* 100 = 0,0201 \* 100 = 2,01

NO cadastro DO contrato trouxe:

Índice: 6.08 Referente à: 2 meses  Período: 01/2014 - 03/2014

Com o índice é 6,08/100+1 \* 102 = 108,20

NUMCONTRATO|CODPROD|REFERENCIA |VALOR

42         |8159   |01/12/2013 |102

42         |8159   |01/02/2014 |108

![Imagem 7: 42 | 8159 | 01 / 02 / 2014 | 108](https://ajuda.sankhya.com.br/hc/article_attachments/9902854706199)

**Importante:** Na tela de Reajuste de Contratos Ativos, o sistema trará na grade somente os produtos cuja ocorrência é ativa, mas efetuará o reajuste dos produtos bonificados e cancelados, se configurado para tal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Cálculo do Índice de Reajuste no Contrato

O cálculo de acumulado em 12 meses é realizado com base nos últimos "12" (doze) meses, portanto, tomando como exemplo o mês de Maio para referência, o intervalo seria de 01/06/2014 a 30/05/2015, ou seja:

01/06/2014        -0,74        = (1 x (1+(-0,74/100))) = 0,993

01/07/2014        -0,61        = (0,993 x (1+(-0,61/100))) = 0,987

01/08/2014        -0,27        = (0,987 x (1+(-0,27/100))) = 0,984

01/09/2014         0,20        = (0,984 x (1+(0,20/100))) = 0,986

01/10/2014         0,28        = (0,986 x (1+(0,28/100))) = 0,989

01/11/2014         0,98        = (0,989 x (1+(0,98/100))) = 0,999

01/12/2014         0,62        = (0,999 x (1+(0,62/100))) = 1,004

01/01/2015         0,76        = (1,004 x (1+(0,76/100))) = 1,012

01/02/2015         0,27        = (1,012  x (1+(0,27/100))) = 1,005

01/03/2015         0,98        = (1,005 x (1+(0,98/100))) = 1,025

01/04/2015         1,17        = (1,025  x (1+(1,17/100))) = 1,037

01/05/2015         0,41        = (1,037 x (1+(0,41/100))) = 1,041

Subtraindo-se -1, temos 0,041; multiplicando por 100, obtemos 4,104.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Reajuste de Contratos com a Data Base de Reajuste

Atualmente, com uma periodicidade de 12 meses, tomemos o exemplo onde a data base do reajuste de um contrato é 01/05/2014; a data para reajuste encontrada será 01/03/2015, de forma que será reajustado utilizando os índices até esta data. No caso, seriam índices de 04/2014 a 03/2015.

Porém, existem empresas que realizam o reajuste dos contratos no próprio mês da data base de reajuste em um momento que já possuem o índice do mês anterior, ou seja, os índices utilizados serão os 12 últimos, realmente a partir da data base do reajuste. Neste exemplo, em que a data base de reajuste é 01/05/2014, o período para índices será de 05/2014 a 04/2015. Para que este comportamento ocorra, é necessário que o parâmetro **"Reajustar contrato à partir da data de reajuste? - REAJAPARTDTBASE"** esteja desativado. 

Com o parâmetro REAJAPARTDTBASE ligado, serão apresentados e exigidos para reajuste apenas os contratos cuja as referências não são maiores do que a data atual (data do servidor). Assim, os contratos serão reajustados considerando o índice do mês anterior. 

Com o referido parâmetro desativado, o sistema irá manter seu comportamento normal, baseando-se na seguinte fórmula:

- 1 mês até a data base do reajuste + frequência - 1

Exemplo:

Data base reajuste: 01/05/2014

Índice encontrados: **04/2014 - 03/2015**

índice: 0.78   01/04/2014

índice: -0.13  01/05/2014

índice: -0.74  01/06/2014

índice: -0.61  01/07/2014

índice: -0.27  01/08/2014

índice: 0.2    01/09/2014

índice: 0.28  01/10/2014

índice: 0.98  01/11/2014

índice: 0.62  01/12/2014

índice: 0.76  01/01/2015

índice: 0.27  01/02/2015

índice: 0.98  01/03/2015

Quando ativado, será utilizada a seguinte fórmula:

data base do reajuste + frequência – 1

Exemplo:

Data base reajuste: 01/05/2014

Índice encontrados: **05/2014 - 04/2015**

índice: -0.13  01/05/2014

índice: -0.74  01/06/2014

índice: -0.61  01/07/2014

índice: -0.27  01/08/2014

índice: 0.2    01/09/2014

índice: 0.28  01/10/2014

índice: 0.98  01/11/2014

índice: 0.62  01/12/2014

índice: 0.76  01/01/2015

índice: 0.27  01/02/2015

índice: 0.98  01/03/2015

índice: 1.17  01/04/2015

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Reajuste para Produtos Cancelados, Suspensos e Bonificados

A atualização de valores para produtos inativos (Bonificados, Cancelados e Suspensos) poderá ocorrer pois, pode ser necessário ativar o produto em um determinado momento futuro e, neste caso, o mesmo já deve estar com seu valor atualizado. Ao executar a rotina de reajuste, o sistema deverá gerar uma ocorrência com esta situação atual do produto.

Esta atualização envolve as seguintes configurações:

- O parâmetro **"Reajuste de Produtos Inativos em Contratos - REAJCONPRODINAT"**, quando habilitado, fará com que o sistema busque os códigos de ocorrências de produtos não ativos (definidos na tela de Preferências) e lance uma ocorrência de contrato usando o código de ocorrência correto, de acordo com a situação atual do produto. Se a situação do produto da ocorrência for incompatível com a situação atual do produto, então o sistema lança uma mensagem de erro e desfaz o reajuste.
- O parâmetro **"Ocorrência para Reajuste de Produtos Bonificados - CODOCORBON"** determina a ocorrência p/reajuste de Produtos Bonificados.
- O parâmetro **"Ocorrência para Reajuste de Produtos Cancelados - CODOCORCAN"** determina a ocorrência p/reajuste de Produtos Cancelados.
- O parâmetro **"Ocorrência para Reajuste de Produtos Suspensos CODOCORSUS"** determina a ocorrência p/reajuste de Produtos Suspensos.

**Observação:** As ocorrências configuradas nos parâmetros devem corresponder às ocorrências configuradas com os respectivos tipos.

Ao confirmar o Reajuste do Contrato, este irá inserir uma ocorrência igual configurada nos parâmetros para os produtos bonificados, cancelados ou suspensos e trará o preço com a data nova do reajuste efetuado.

![Imagem 8: Ao confirmar o Reajuste do Contrato , este irá inserir uma ocorrência igual configurada nos parâmetros para os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/9905323996183)

As tabelas de **"Ocorrências"** e de **"Preço do produto"** não permitem o lançamento de duas alterações na mesma data. Por exemplo, se o produto 20445, do contrato 2317 possui uma ocorrência dia 01/09/2014, não será possível incluir outra ocorrência na mesma data. Isso também acontece com o preço. Neste caso, o sistema localiza uma data ainda disponível nessas tabelas, ou seja, verifica no dia 02/09/2014 se também já existe, verifica no dia 03 e continua até encontrar uma data disponível.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)

## Contratos Inativos

Na realização de ajustes de contratos, se tratando de contratos que devem ser **"Inativados"**, a marcação de **"Ativo"** no contrato não é considerada nesse processo de inativação e nem mesmo em seu faturamento. O que é levado em consideração, é a situação dos produtos do contrato.

Em outras palavras, para inativar de fato um contrato impedindo qualquer ação sobre ele, é preciso também que se altere a situação de seus itens para uma das situações inativas, que são **"Suspenso"** ou **"Cancelado"**. Ou seja, você pode vincular ao contrato que será inativado, uma ocorrência cuja situação seja Suspenso ou Cancelado na tela [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), aba [Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprodutosservios).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos#top)
