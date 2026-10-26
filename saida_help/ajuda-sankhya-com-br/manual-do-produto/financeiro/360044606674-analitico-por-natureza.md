---
id: "360044606674"
titulo: "Analítico por Natureza"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:40:34Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Projeto", "Centro de Resultado", "Relatórios Gerenciais", "Financeiro", "Natureza", "Analítico por Natureza", "br.com.sankhya.fin.rel.analiticonatureza", "Analítico por Natureza manual", "Relatório Analítico", "Configuração e Filtros", "Opções Avançadas"]
---

# Analítico por Natureza

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312336662551) Módulo: Financeiro > Relatórios > Gerenciais
```

---

O relatório gerencial **"Analítico por Natureza"** apresenta informações detalhadas dos títulos como **"Vencimento"**, **"Nome do Parceiro"**, **"Histórico"** e **"Valor"** agrupando por Natureza.

Apresenta informações de fechamento financeiro, informando o saldo inicial das contas, a movimentação do mês, receitas e despesas, gerando o saldo final do período analisado.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#abageral)                                                                    [Aba Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#abaavan%C3%A7ado)

[Botão Visualizar em PDF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#bot%C3%A3ovisualizarempdf)                                         [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 2: Botão Visualizar em PDF Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4407762677911)

## Aba Geral

Do lado esquerdo desta aba, pode-se configurar filtros por **"Natureza"**, **"Centro de Resultado"** e **"Projeto"**.

![Imagem 3: Do lado esquerdo desta aba, pode-se configurar filtros por "Natureza" , "Centro de Resultado" e "Projeto" .](https://ajuda.sankhya.com.br/hc/article_attachments/4407757043223)

Através do botão **"Adicionar"**, você pode pesquisar um item a ser acrescentado na lista. Ao acioná-lo, será aberta a tela de pesquisa. Ao clicar sobre um item nesta tela, o sistema irá inserir o item na lista. Marcando o item escolhido com o  localizado antes de seu código/descrição, o mesmo será utilizado para filtragem.

O botão **"Remover"** irá retirar os itens selecionados da lista. Para selecionar um item na lista basta clicar sobre ele. O item selecionado ficará na cor verde. Para selecionar mais de um item, pressione a tecla **"Ctrl"** do teclado e clique sobre os itens desejados.

**Observação:** Itens selecionados para remoção são aqueles que estão com a cor verde e não os que têm a caixa de seleção marcada.

O botão **"Limpar"** removerá todos os itens da lista.

Você também pode configurar outros filtros através do botão ![Imagem 4: Você também pode configurar outros filtros através do botão "Filtro" , localizado acima dos campos desta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/16082673269655) **"Filtro"**, localizado acima dos campos desta aba.

**Importante:** A criação dos filtros de Natureza, Centro de Resultado e Projeto através do botão Filtros para notas que possuem rateio, deverá ser realizada da seguinte forma:

Ao clicar no botão e optar pela opção ![Imagem 5: Ao clicar no botão e optar pela opção "Cadastrar Filtro (F8)" , informe manualmente somente as expressões conforme os…](https://ajuda.sankhya.com.br/hc/article_attachments/16082651000471) **"Cadastrar Filtro [F8]"**, informe manualmente somente as expressões conforme os exemplos abaixo:

Para a natureza 3020100 - Aluguel/IPTU e 3020200 - Limpeza e conservação, a expressão será:

/\*intervalo NATUREZA 3020100:3020200 intervalo\*/

Para o Centro de Resultado 10200 - Recursos Humanos e 100300 - Contábil, tem-se a expressão:

/\*intervalo CR 10200:100300 intervalo\*/

Para o Projeto 1010000 - Imobiliário e 1020000 - Administrativo, a expressão:

/\*intervalo PROJETO 1010000:1020000 intervalo\*/

Ressaltando que as expressões deverão seguir este padrão, tendo como modificação apenas os números de cadastro da Natureza, Centro de Resultado e Projeto. Após inserir a expressão, aponte um nome para o filtro criado.

![Imagem 6: Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que…](https://ajuda.sankhya.com.br/hc/article_attachments/26182880628503) Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que utilizam a tabela Financeiro visualizem o referido campo.

Para que o sistema apresente o relatório, devem ser definidos os períodos de análise.

Os intervalos de **"Data de Negociação no Período"** e **"Data de Movimento no Período"** podem ser utilizados para restringir a consulta, para uma análise por competência.

![Imagem 7: Os intervalos de "Data de Negociação no Período" e "Data de Movimento no Período" podem ser utilizados para restringir…](https://ajuda.sankhya.com.br/hc/article_attachments/4407762656663)

**Observação:** Quando houver rateio, automático ou não, o relatório trará a natureza do rateio independente das outras naturezas que foram cadastradas no registro (Movimentação Financeira, Centrais, entre outros).

Informe no campo Data de Negociação no Período o período de Negociação dos títulos que deseja-se visualizar. Nos lançamentos, a Data da Negociação é a data da emissão do documento.

No campo Data de Movimento no Período informe o período da Movimentação Financeira, ou seja, o período em que os títulos foram registrados no sistema.

**Nota:** Quando o parâmetro **"Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER"** estiver habilitado, todos os textos que referenciam à data de movimento serão trocados por data de Entrada e Saída. Os filtros e as consultas que utilizam DHMOV passam a utilizar DTENTSAI (visível no monitor de consultas).

Sob a ótica financeira, a análise pode ser realizada considerando os títulos pendentes, baixados ou ambos. Para restringir a consulta, neste sentido, selecione **"Pendentes"**, **"Baixados"** ou ambos, conforme a necessidade e informe o **"Período de análise"** para as opções escolhidas.

![Imagem 8: Sob a ótica financeira, a análise pode ser realizada considerando os títulos pendentes, baixados ou ambos. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/4407762646807)

A partir deste momento, defina algumas especificidades a serem apresentadas no relatório:

![Imagem 9: A partir deste momento, defina algumas especificidades a serem apresentadas no relatório:](https://ajuda.sankhya.com.br/hc/article_attachments/4407762636183)

Determine entre os títulos de **"Receita"**, **"Despesa"** ou ambos e, além disto, se serão considerados os títulos **"Reais"** ou os **"Provisionados"**.

Efetuando a marcação **"Imprime faixa nos detalhes"**, o sistema irá colorir as linhas do relatório em seus detalhes.

Acionando a marcação **"Imprime Observação de** **Requisição"**, as observações de requisição serão impressas no relatório.

Através da marcação **"Requisições"**, serão incluídos os lançamentos gerados pelas TOP's de Requisição.

Caso a marcação **"Produção"** esteja realizada, também serão visualizadas as notas de Produção.

**Observação:** Juntamente às marcações Requisições e Produção, consta um filtro no qual você pode especificar as notas de Requisição ou Produção.

A marcação **"Desconsiderar financeiro de frete extra nota"** definirá se os financeiros de frete extra nota serão considerados ou não ao visualizar o relatório Analítico por Natureza.

Quando a marcação **"Tratar Devol.de Compra como Desp.Negativa e Devol.de Venda como Rec.Negativa"** for efetuada, fará com que as devoluções de venda e de compra sejam deduzidas das receitas e despesas, respectivamente.

**Importante:** Vale salientar que as requisições são tratadas no relatório de modo que seus valores serão **"Negativos"** e as devoluções de requisição com valores **"Positivos"**, de modo a obter, no fim, a diferença entre estes valores. Abaixo, temos um simples exemplo:

Requisição = R$100,00

Devolução de Requisição = R$50,00

Saldo = R$50,00

A marcação **"Imprimir histórico completo"** será exibida na tela caso o parâmetro **"Usar cache de disco em relatórios gerenciais? - USACACHEDKFIN"** esteja ligado. Se você habilitar esta marcação, fará com que seja apresentado todo o conteúdo no histórico na impressão do relatório; caso contrário, será exibida apenas a primeira linha.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#top) 

## Aba Avançado

![Imagem 10: Aba Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/4407762631447)

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

Determine na grade **"Ordenar por data de"**, através de qual data será feita a ordenação dos dados. Temos as seguintes possibilidades:

- Negociação;
- Vencimento;
- Baixa.

Selecionando a marcação **"Considerar Renegociações"**, o sistema buscará os títulos renegociados no período.

Caso utilize a marcação **"Considerar Naturezas Especiais"** será possível utilizar uma das naturezas especiais relacionadas a um financeiro, saiba mais acessando o artigo: [Naturezas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154-Naturezas-Especiais). 

**Observação:** para que os valores das Naturezas Especiais sejam exibidos no relatório, é necessário informar a natureza financeira do título à qual cada natureza especial está vinculada.

Por meio da marcação **"Imprime Valor Líquido"** serão analisados os valores marcados em [Componentes do valor líquido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607174).

Habilitando a marcação **"Imprime Filtros"** serão impressos os filtros selecionados. Caso você selecione esta marcação, os filtros realizados: **"Data de Negociação no Período"**, **"Data do Movimento no Período"**, **"Vencendo no Período"**, e **"Baixados no Período"**, serão apresentados na impressão do relatório.

A marcação **"Totalizar por** **dias"**, quando efetuada, totalizará os resultados diariamente.

**Observação:** Nos Relatórios Gerenciais Analíticos e sintéticos mensais por Centro de Resultados, Natureza ou Projeto, a última página do relatório trará as contas que não foram escolhidas na aba saldos, mas que influenciaram no total geral do relatório.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#top)

## Botão Visualizar em PDF

No alto da tela, temos o botão ![Imagem 11: No alto da tela, temos o botão . Através dele você escolhe como deseja visualizar o relatório gerencial, se "em PDF" ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16082828613911). Através dele você escolhe como deseja visualizar o relatório gerencial, se **"em PDF"** ou **"em Planilha"**.

![Imagem 12: No alto da tela, temos o botão . Através dele você escolhe como deseja visualizar o relatório gerencial, se "em PDF" ou…](https://ajuda.sankhya.com.br/hc/article_attachments/4407762622743)

**Observação:** Caso seja feita a exportação em planilha, será levada apenas a exportação do dados de forma bruta da consulta realizada a partir dos filtros, não sendo considerados os dados da aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#abaavan%C3%A7ado) e não será demonstrado cabeçalho e totalizadores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#top)

## Parâmetros que influenciam esta rotina

**Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER:** quando ativado, além do comportamento normal que altera todos os textos e consultas que referenciam a data de movimento pela **"Data de Entrada"** e **"Data de Saída"**, deixa de exibir a data de movimento na coluna "Emissão" e passa a exibir a **"Data de entrada e saída"**. O título da coluna Emissão não sofre alteração, independente de o parâmetro estar ou não ligado.

Para consultar o artigo referente a rotina Relatórios Formatados, acesse o link [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674-Anal%C3%ADtico-por-Natureza#top)
