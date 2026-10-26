---
id: "360045115793"
titulo: "Analítico por Centro de Resultado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:45:31Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Movimentação Financeira", "Projeto", "Centro de Resultado", "Relatórios Gerenciais", "Analítico por Centro de Resultado", "br.com.sankhya.fin.rel.analiticocentroresultado", "Analítico por Centro de Resultado manual", "Financeiro", "Natureza", "Relatório Analítico", "Configuração e Filtros", "Opções Avançadas"]
---

# Analítico por Centro de Resultado

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312495209495) Módulo: Financeiro > Relatórios > Gerenciais
```

---

O relatório gerencial Analítico por Centro de Resultado tem a função de exibir os dados referentes a todas as receitas e despesas envolvendo a conta selecionada, agrupando as informações por Centro de Resultado.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#abageral)                                                                    [Aba Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#abaavan%C3%A7ado)

[Botão Visualizar em PDF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#bot%C3%A3ovisualizarempdf)                                         [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 2: Botão Visualizar em PDF Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4407757637271)

## Aba Geral

Do lado esquerdo desta aba, você pode configurar filtros por **"Natureza"**, **"Centro de Resultado"** e **"Projeto"**.

![Imagem 3: Do lado esquerdo desta aba, você pode configurar filtros por "Natureza" , "Centro de Resultado" e "Projeto" .](https://ajuda.sankhya.com.br/hc/article_attachments/4407757654935)

Através do botão **"Adicionar"**, você pode pesquisar um item a ser acrescentado na lista. Ao acioná-lo, será aberta a tela de pesquisa. Clicando sobre um item nesta tela, o sistema irá inserir o mesmo na lista. Ao marcar o item escolhido com o , localizado antes de seu código/descrição, este será utilizado para filtragem.

O botão **"Remover"** irá retirar os itens selecionados da lista, sendo que, para selecionar um item na lista, basta que você clique sobre ele. O item selecionado ficará na cor verde. Para selecionar mais de um item, pressione a tecla **"Ctrl"** do teclado e clique sobre os itens desejados.

**Observação:** Itens selecionados para remoção são aqueles que estão com a cor verde e não os que têm a caixa de seleção marcada.

O botão **"Limpar"** removerá todos os itens da lista.

Você também pode configurar outros filtros através do botão ![Imagem 4: Você também pode configurar outros filtros através do botão "Filtros" , localizado acima dos campos desta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/16082405411223) **"Filtros"**, localizado acima dos campos desta aba.

**Importante:** A criação dos filtros de Natureza, Centro de Resultado e Projeto através do Assistente de filtro para notas que possuem rateio, deverá ser realizada da seguinte forma:

Ao clicar no botão e optar pela opção ![Imagem 5: Ao clicar no botão e optar pela opção "Cadastrar Filtro (ctrl+F8)" , informe manualmente somente as expressões conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/16082402809111) **"Cadastrar Filtro [ctrl+F8]"**, informe manualmente somente as expressões conforme os exemplos abaixo:

- Para a Natureza 3020100 - Aluguel/IPTU e 3020200 - Limpeza e conservação, a expressão será:

                /\*intervalo NATUREZA 3020100:3020200 intervalo\*/

- Para o Centro de Resultado 10200 - Recursos Humanos e 100300 - Contábil, tem-se a expressão:

                /\*intervalo CR 10200:100300 intervalo\*/

- Para o Projeto 1010000 - Imobiliário e 1020000 - Administrativo, a expressão:

                 /\*intervalo PROJETO 1010000:1020000 intervalo\*/

Ressaltando que as expressões deverão seguir este padrão, tendo como modificação apenas os números de cadastro da Natureza, Centro de Resultado e Projeto. Após inserir a expressão, aponte um nome para o filtro criado e, caso deseje que o mesmo seja aplicado de imediato, basta que você acione a marcação **"Aplica filtro ao concluir"**.

![Imagem 6: Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que…](https://ajuda.sankhya.com.br/hc/article_attachments/26182978513175) Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que utilizam a tabela Financeiro visualizem o referido campo.

Para que o sistema apresente o relatório, defina os períodos de análise.

Os intervalos de **"Data de Negociação no Período"** e **"Data do Movimento no Período"** podem ser utilizados para restringir a consulta, para uma análise por competência.

![Imagem 7: Os intervalos de "Data de Negociação no Período" e "Data do Movimento no Período" podem ser utilizados para restringir…](https://ajuda.sankhya.com.br/hc/article_attachments/4407757689367)

Informe no campo **"Data de Negociação no** **Período"**, o período de Negociação dos títulos que você deseja visualizar. Nos lançamentos, a Data da Negociação é a data da emissão do documento.

No campo **"Data de Movimento no Período"**, informe o período da Movimentação Financeira, ou seja, o período em que os títulos foram registrados no sistema.

**Nota:** Quando o parâmetro **"Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER"** estiver habilitado, fará com que todos os textos que referenciam a data de movimento, sejam trocados por data de Entrada e Saída. Os filtros e as consultas que utilizam DHMOV passam a utilizar DTENTSAI (visível no monitor de consultas).

Sob a ótica financeira, a análise pode ser realizada considerando os títulos pendentes, baixados ou ambos. Para restringir a consulta, selecione as marcações **"Pendentes"**, **"Baixados"** ou ambos, conforme a necessidade e informe o **"Período de análise"** para as opções escolhidas.

![Imagem 8: Sob a ótica financeira, a análise pode ser realizada considerando os títulos pendentes, baixados ou ambos. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/4407757709591)

A partir deste momento, você define algumas especificidades a serem apresentadas no relatório:

![Imagem 9: A partir deste momento, você define algumas especificidades a serem apresentadas no relatório:](https://ajuda.sankhya.com.br/hc/article_attachments/4407763108887)

Determine entre os títulos de **"Receita"**, **"Despesa"** ou ambos e, além disto, se serão considerados os títulos **"Reais"** ou os **"Provisionados"**.

Efetuando a marcação **"Imprime faixa nos detalhes"** o sistema irá colorir as linhas do relatório em seus detalhes.

Caso você acione a marcação **"Imprime Observação de** **Requisição"**, fará com que as observações de requisição sejam impressas no relatório.

Através da marcação **"Requisições"**, serão incluídos os lançamentos gerados pelas TOP's de Requisição.

Se a marcação **"Produção"** estiver realizada, também serão visualizadas as notas de Produção.

**Observação:** Juntamente às marcações Requisições e Produção, consta um filtro no qual você poderá especificar as notas de Requisição ou Produção.

Quando a marcação **"Tratar Devol.de Compra como Desp.Negativa e Devol.de Venda como Rec.Negativa"** for efetuada, fará com que as Devoluções de Venda e de Compra sejam deduzidas das receitas e despesas, respectivamente.

**Importante:** As requisições são tratadas no relatório de modo que seus valores serão **"Negativos"** e as Devoluções de Requisição com valores **"Positivos"**, de modo a obter, no fim, a diferença entre estes valores. Abaixo, temos um simples exemplo:

Requisição = R$100,00

Devolução de Requisição = R$50,00

Saldo = R$50,00

A marcação **"Imprimir histórico completo"** será exibida na tela caso o parâmetro **"Usar cache de disco em relatórios gerenciais? - USACACHEDKFIN"** esteja ligado. Se você habilitar esta marcação, fará com que seja apresentado todo o conteúdo no histórico na impressão do relatório; caso contrário, será exibida apenas a primeira linha.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#top) 

## Aba Avançado

![Imagem 10: Aba Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/4407757760919)

Caso a marcação **"Apenas Contas Ativas"** esteja efetuada, o sistema avaliará apenas as operações realizadas com as contas **"Ativas"**.

Quando a marcação **"Imprime Saldos"** estiver realizada, serão impressos os saldos das contas no final do relatório.

O sistema trará o saldo apurado na data informada no campo **"Saldos Referentes à data"**.

Os botões **"Marcar Todas"** e **"Desmarcar Todas"** auxiliam na seleção de contas da grade.

No campo **"Moeda"**, determine a moeda que será considerada nas análises, quando houver transações financeiras em moedas estrangeiras.

Na grade **"Data para converter a** **moeda"**, defina a data a ser considerada para conversão da moeda, dentre as seguintes opções:

- **Negociação:** Converte pela Data de Negociação do Título. Usado quando o valor de conversão for fixado na data de negociação;
- **Vencimento:** Converte pela Data de Vencimento do Título. Usado quando a conversão ocorrer na data de vencimento;
- **Baixa:** Converte pela Data da Baixa. Usado quando o valor for convertido na data da baixa do Título;
- **Fixa:** Converte conforme um valor fixo informado no cadastro de moedas. Normalmente, usado em negociações contratuais que estipulam um valor fixo de conversão durante a vigência do contrato.

Determine na grade **"Ordenar por data de"** através de qual data será feita a ordenação dos dados, de acordo com as seguintes possibilidades:

- Negociação;
- Vencimento;
- Baixa.

Selecionando a marcação **"Considerar Renegociações"**, o sistema buscará os títulos renegociados no período.

Por meio da marcação **"Imprime Valor Líquido"** serão analisados os valores marcados em [Componentes do valor líquido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607174).

Habilitando a marcação **"Imprime** **Filtros"**, serão impressos os filtros selecionados. Caso você selecione esta marcação, os filtros **"Data de Negociação no Período"**, **"Data do Movimento no Período"**, **"Vencendo no Período"** e **"Baixados no Período"** realizados, serão apresentados na impressão do relatório. Além de que, no filtro Baixados no Período teremos o ícone ![Imagem 11: Habilitando a marcação "Imprime Filtros" , serão impressos os filtros selecionados. Caso você selecione esta marcação,…](https://ajuda.sankhya.com.br/hc/article_attachments/360099494493) que contém uma explicação sobre o filtro que o auxiliará no seu uso.

A marcação **"Totalizar por** **dias"**, quando efetuada, totalizará os resultados diariamente.

**Observação:** Nos Relatórios Gerenciais Analíticos e sintéticos mensais por Centro de Resultados, Natureza ou Projeto, a última página do relatório trará as contas que não foram escolhidas na aba saldos, mas que influenciaram no total geral do relatório.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#top)

## Botão Visualizar em PDF

No alto da tela, temos o botão ![Imagem 12: No alto da tela, temos o botão "Visualizar em PDF" , através dele você escolhe como deseja visualizar o relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/16082432575895) **"Visualizar em PDF"**, através dele você escolhe como deseja visualizar o relatório gerencial, se **"em PDF"** ou **"em Planilha"**.

![Imagem 13: No alto da tela, temos o botão "Visualizar em PDF" , através dele você escolhe como deseja visualizar o relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/4407757808279)

**Observação:** Caso seja feita a exportação em planilha, será levada apenas a exportação do dados de forma bruta da consulta realizada a partir dos filtros, não sendo considerados os dados da aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#abaavan%C3%A7ado) e não será demonstrado cabeçalho e totalizadores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#top)

## Parâmetros que influenciam esta rotina

**Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER:** quando ativado, além do comportamento normal que altera todos os textos e consultas que referenciam a data de movimento pela **"Data de Entrada"** e **"Data de Saída"**, deixa de exibir a data de movimento na coluna **"Emissão"** e passa a exibir a **"Data de entrada e saída"**. O título da coluna Emissão não sofre alteração, independente de o parâmetro estar ou não ligado.

Para consultar o artigo referente a rotina Relatórios Formatados, acesse o link [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115793-Anal%C3%ADtico-por-Centro-de-Resultado#top)
