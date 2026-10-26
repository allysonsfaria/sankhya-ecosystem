---
id: "360044606134"
titulo: "Sintético por Natureza"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:23Z"
rotulos: ["AJUDA DO SKW", "manual", "Relatórios", "Movimentação Financeira", "Projeto", "Centro de Resultado", "Sintético por Natureza", "br.com.sankhya.fin.rel.sinteticonatureza", "Sintético por Natureza manual", "Relatórios Gerenciais", "Financeiro", "Natureza", "Receitas despesas e saldo por natureza", "\"%T.Nat\" (contribuição) \"%T.Rec\" (receitas) \"%T.Desp\" (despesas)", "Natureza Centro Projeto e período"]
---

# Sintético por Natureza

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312323937431) Módulo: Financeiro > Relatórios > Gerenciais
```

---

Neste relatório, são apresentados os lançamentos de receitas e/ou despesas e saldo líquido apurado, resumindo as informações de recebimento e gastos por natureza. São apresentadas três colunas com Análises Verticais, que simplificam a pesquisa do desempenho de uma natureza em comparação com o resultado total da empresa. Vejamos abaixo o detalhamento de cada uma delas:

A coluna **"%T.Nat"** é uma análise da composição de um determinado grupo de Naturezas, ou seja, aqui se pode verificar o quanto uma natureza contribuiu na composição do resultado total apurado na **"Natureza Pai"** (de Nível imediatamente superior na Hierarquia). Se observar uma natureza de primeiro Nível, portanto, esta coluna apresentará a contribuição deste conjunto de naturezas na composição do Resultado Geral do Período.

A coluna **"%T.Rec"** demonstra a comparação do resultado da Natureza com as Receitas Totais do Período. Como as naturezas recebem, essencialmente, lançamentos de Receita ou de Despesa, podem-se extrair a partir desta informação duas análises:

![Imagem 2: Se tratando de uma natureza de receitas, você visualiza sua contribuição com as receitas totais;](https://ajuda.sankhya.com.br/hc/article_attachments/16583507412887) Se tratando de uma natureza de receitas, você visualiza sua contribuição com as receitas totais;

![Imagem 3: No caso de uma natureza de despesas, você pode analisar o comprometimento das receitas provocado por esta natureza.](https://ajuda.sankhya.com.br/hc/article_attachments/16583492608919) No caso de uma natureza de despesas, você pode analisar o comprometimento das receitas provocado por esta natureza.

A coluna **"%T.Desp"**, por sua vez, compara o resultado da Natureza com as Despesas Totais do Período, servindo como indicador da composição dos gastos.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#abageral)                                                                    [Aba Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#abaavan%C3%A7ado)

[Botão Visualizar em PDF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#bot%C3%A3ovisualizarempdf)                                         [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 4: Botão Visualizar em PDF Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4407762198551)

## Aba Geral

Do lado esquerdo desta aba, você pode configurar filtros por **"Natureza"**, **"Centro de Resultado"** e **"Projeto"**.

![Imagem 5: Do lado esquerdo desta aba, você pode configurar filtros por "Natureza" , "Centro de Resultado" e "Projeto" .](https://ajuda.sankhya.com.br/hc/article_attachments/4407756928279)

Através do botão **"Adicionar"**, você pode pesquisar um item a ser acrescentado na lista. Ao acioná-lo, será aberta a tela de pesquisa. Ao clicar sobre um item nesta tela, o sistema irá inserir o item na lista. Marcando o item escolhido com o  localizado antes de seu código/descrição, o mesmo será utilizado para filtragem.

O botão **"Remover"** irá retirar os itens selecionados da lista. Para selecionar um item na lista basta clicar sobre ele. O item selecionado ficará na cor **verde**. Para selecionar mais de um item, pressione a tecla **"Ctrl"** do teclado e clique sobre os itens desejados.

**Observação:** itens selecionados para remoção são aqueles que estão com a cor verde e não os que têm a caixa de seleção marcada.

O botão **"Limpar"** removerá todos os itens da lista.

Você também pode configurar outros filtros através do botão ![Imagem 6: Você também pode configurar outros filtros através do botão "Filtros" , localizado acima dos campos desta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/16583602364439) **"Filtros"**, localizado acima dos campos desta aba.

**Importante:** a criação dos filtros de Natureza, Centro de Resultado e Projeto através do botão Filtros para notas que possuem rateio, deverá ser realizada da seguinte forma:

Ao clicar no botão e optar pela opção ![Imagem 7: Ao clicar no botão e optar pela opção "Cadastrar Filtro (F8)" , informe manualmente somente as expressões conforme os…](https://ajuda.sankhya.com.br/hc/article_attachments/16583585561751) **"Cadastrar Filtro [F8]"**, informe manualmente somente as expressões conforme os exemplos abaixo:

**(1)** Para a natureza 3020100 - Aluguel/IPTU e 3020200 - Limpeza e conservação, a expressão será:

/\*intervalo NATUREZA 3020100:3020200 intervalo\*/

**(1)** Para o Centro de Resultado 10200 - Recursos Humanos e 100300 - Contábil, tem-se a expressão:

/\*intervalo CR 10200:100300 intervalo\*/

**(1)** Para o Projeto 1010000 - Imobiliário e 1020000 - Administrativo, a expressão:

/\*intervalo PROJETO 1010000:1020000 intervalo\*/

Ressaltando que as expressões deverão seguir este padrão, tendo como modificação apenas os números de cadastro da Natureza, Centro de Resultado e Projeto. Após inserir a expressão, aponte um nome para o filtro criado.

![Imagem 8: Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que…](https://ajuda.sankhya.com.br/hc/article_attachments/26183036852503) Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que utilizam a tabela Financeiro visualizem o referido campo.

Para que o sistema apresente o relatório, devem ser definidos os períodos de análise.

Os intervalos de **"Data de Negociação no Período"** e **"Data de Movimento no Período"** podem ser utilizados para restringir a consulta, para uma análise por competência.

![Imagem 9: Os intervalos de "Data de Negociação no Período" e "Data de Movimento no Período" podem ser utilizados para restringir…](https://ajuda.sankhya.com.br/hc/article_attachments/4407756345751)

Informe no campo Data de Negociação no Período o período de Negociação dos títulos que deseja-se visualizar. Nos lançamentos, a Data da Negociação é a data da emissão do documento.

No campo Data de Movimento no Período informe o período da Movimentação Financeira, ou seja, o período em que os títulos foram registrados no sistema.

**Nota:** quando o parâmetro **"Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER"** estiver habilitado, todos os textos que referenciam à data de movimento serão trocados por data de Entrada e Saída. Os filtros e as consultas que utilizam DHMOV passam a utilizar DTENTSAI (visível no monitor de consultas).

Sob a ótica financeira, a análise pode ser realizada considerando os títulos pendentes, baixados ou ambos. Para restringir a consulta, neste sentido, selecione **"Pendentes"**, **"Baixados"** ou ambos, conforme a necessidade e informe o **"Período de análise"** para as opções escolhidas.

![Imagem 10: Sob a ótica financeira, a análise pode ser realizada considerando os títulos pendentes, baixados ou ambos. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/4407762231831)

A partir deste momento, defina algumas especificidades a serem apresentadas no relatório:

![Imagem 11: A partir deste momento, defina algumas especificidades a serem apresentadas no relatório:](https://ajuda.sankhya.com.br/hc/article_attachments/4407756399383)

Determine entre os títulos de **"Receita"**, **"Despesa"** ou ambos e, além disto, se serão considerados os títulos **"Reais"** ou os **"Provisionados"**.

Efetuando a marcação **"Imprime faixa nos detalhes"**, o sistema irá colorir as linhas do relatório em seus detalhes.

Através da marcação **"Requisições"**, serão incluídos os lançamentos gerados pelas TOP's de Requisição.

Caso a marcação **"Produção"** esteja realizada, também serão visualizadas as notas de Produção.

**Observação:** juntamente às marcações Requisições e Produção, consta um filtro no qual você pode especificar as notas de Requisição ou Produção.

Quando a marcação **"Tratar Devol.de Compra como Desp.Negativa e Devol.de Venda como Rec.Negativa"** for efetuada, fará com que as devoluções de venda e de compra sejam deduzidas das receitas e despesas, respectivamente.

**Importante:** vale salientar que as requisições são tratadas no relatório de modo que seus valores serão **"Negativos"** e as devoluções de requisição com valores **"Positivos"**, de modo a obter, no fim, a diferença entre estes valores. Abaixo, temos um simples exemplo:

Requisição = R$100,00

Devolução de Requisição = R$50,00

Saldo = R$50,00

**Seção Apresentar resultado por**

Nesta seção, indique a forma de apresentação do resultado, sendo possível, três marcações distintas:

- Natureza;
- Natureza/C.Resultado;
- Natureza/Projeto.

Caso seja feita a escolha do agrupamento por **"Natureza"**, indique apenas o **"Grau"** de detalhamento. Sendo a opção de agrupamento por **"Natureza/C.Resultado"** ou **"Natureza/Projeto"**, além do **"Grau"**, você deve indicar também um **"Grau Interno"**.

O Grau e o Grau Interno se referem ao nível hierárquico do cadastro da **"Natureza"**, **"Centro de Resultado"** ou **"Projeto"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#top) 

## Aba Avançado

![Imagem 12: Aba Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/4407762250903)

Caso a marcação **"Apenas Contas Ativas"** esteja efetuada, o sistema avaliará apenas as operações realizadas com as contas **"Ativas"**.

Quando a marcação **"Imprime Saldos"** estiver realizada, serão impressos os saldos das contas no final do relatório.

O sistema trará o saldo apurado na data informada no campo **"Saldos Referentes à data"**.

Os botões **"Marcar Todas"** e **"Desmarcar Todas"** auxiliam na seleção de contas da grade.

No campo **"Moeda"** determine a moeda que será considerada nas análises, quando houver transações financeiras em moedas estrangeiras.

Na grade **"Data para converter a moeda"** defina a data a ser considerada para conversão da moeda. Você pode escolher dentre as seguintes opções:

- **Negociação:** Converte pela Data de Negociação do Título. Usado quando o valor de conversão for fixado na data de negociação;
- **Vencimento:** Converte pela Data de Vencimento do Título. Usado quando a conversão ocorrer na data de vencimento;
- **Baixa:** Converte pela Data da Baixa. Usado quando o valor for convertido na data da baixa do Título;
- **Fixa:** Converte conforme um valor fixo informado no cadastro de moedas. Normalmente, usado em negociações contratuais que estipulam um valor fixo de conversão durante a vigência do contrato.

Selecionando a marcação **"Considerar Renegociações"**, o sistema buscará os títulos renegociados no período.

A marcação **"Considerar Naturezas Especiais"** busca os dados cadastrados em [Naturezas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154-Naturezas-Especiais).

Por meio da marcação **"Imprime Valor Líquido"** serão analisados os valores marcados em [Componentes do valor líquido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607174).

Habilitando a marcação **"Imprime Filtros"** serão impressos os filtros selecionados. Caso você selecione esta marcação, os filtros realizados: **"Data de Negociação no Período"**, **"Data do Movimento no Período"**, **"Vencendo no Período"**, e **"Baixados no Período"**, serão apresentados na impressão do relatório.

**Nota:**os relatórios **"Analítico por Natureza"**, **"Sintético por Natureza"** e **"Sintético por Natureza - Mensal"**, consideram a natureza informada nas requisições.

**Observação:** para a geração dos valores, é necessário selecionar as naturezas analíticas. O sistema cria um relatório sintético a partir dessas naturezas. Contudo, no relatório descritivo, as naturezas exibidas corresponderão às naturezas sintéticas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#top)

## Botão Visualizar em PDF

No alto da tela, temos o botão ![Imagem 13: No alto da tela, temos o botão "Visualizar em PDF" . Através dele você escolhe como deseja visualizar o relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/16583602367639) **"Visualizar em PDF"**. Através dele você escolhe como deseja visualizar o relatório gerencial, se **"em PDF"** ou **"em Planilha"**.

![Imagem 14: No alto da tela, temos o botão "Visualizar em PDF" . Através dele você escolhe como deseja visualizar o relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/4407756520855)

**Observação:** Caso seja feita a exportação em planilha, será levada apenas a exportação do dados de forma bruta da consulta realizada a partir dos filtros, não sendo considerados os dados da aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#abaavan%C3%A7ado) e não será demonstrado cabeçalho e totalizadores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#top)

## Parâmetros que influenciam esta rotina

O parâmetro **"Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER"**, quando ativado, além do comportamento normal que altera todos os textos e consultas que referenciam a data de movimento pela **"Data de Entrada"** e **"Data de Saída"**, deixa de exibir a data de movimento na coluna "Emissão" e passa a exibir a **"Data de entrada e saída"**. O título da coluna Emissão não sofre alteração, independente de o parâmetro estar ou não ligado.

Para conhecer mais sobre os Relatórios Formatados, acesse o artigo [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134-Sint%C3%A9tico-por-Natureza#top)
