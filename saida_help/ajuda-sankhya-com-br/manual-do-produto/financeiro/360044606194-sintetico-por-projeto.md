---
id: "360044606194"
titulo: "Sintético por Projeto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:38Z"
rotulos: ["AJUDA DO SKW", "manual", "Relatórios", "Movimentação Financeira", "Projeto", "Centro de Resultado", "Relatórios Gerenciais", "Financeiro", "Sintético por Projeto", "br.com.sankhya.fin.rel.sinteticoprojeto", "Sintético por Projeto manual", "Natureza", "Mostra receitas despesas e saldo por Projeto", "PDF ou Excel; configurações de data e moeda", "Ajuste por natureza centro de resultado e projeto"]
---

# Sintético por Projeto

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312293624599) Módulo: Financeiro > Relatórios > Gerenciais
```

---

Este relatório conduz os lançamentos de receitas e/ou despesas e saldo líquido apurado, concentrando as informações de recebimento e custas por Projeto.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#abageral)                                                                    [Aba Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#abaavan%C3%A7ado)

[Botão Visualizar em PDF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#bot%C3%A3ovisualizarempdf)                                         [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 2: Botão Visualizar em PDF Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4407758784663)

São demonstradas três colunas com Análises Verticais, que facilitam a análise do desempenho de um Projeto em comparação com o resultado total da empresa. Vejamos o conceito de cada uma delas:

- A coluna %T.Proj é uma análise da estruturação de um determinado grupo de Projetos, ou seja, nesta coluna visualiza-se o quanto um projeto contribuiu na composição do resultado total apurado no **"Projeto Pai"** (de Nível imediatamente superior na Hierarquia).
- A coluna %T.Rec exibe a comparação do Resultado do Projeto com as Receitas Totais do Período, sendo um apontador de Contribuição ou Comprometimento.
- A coluna %T.Desp, por sua vez, confronta o resultado do Projeto com as Despesas Totais do Período, servindo como indicador da composição das despesas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#top)

## Aba Geral

Do lado esquerdo desta aba, pode-se configurar filtros por **"Natureza"**, **"Centro de Resultado"** e **"Projeto"**.

![Imagem 3: Do lado esquerdo desta aba, pode-se configurar filtros por "Natureza" , "Centro de Resultado" e "Projeto" .](https://ajuda.sankhya.com.br/hc/article_attachments/4407763870615)

Por meio do botão **"Adicionar"**, pode-se pesquisar um item a ser acrescentado na lista. Ao acioná-lo, será aberta a tela de pesquisa. Ao clicar sobre um item nesta tela, o sistema irá inseri-lo o item na lista. Marcando-se o item escolhido com o **"v"** localizado antes de seu código/descrição, o mesmo será utilizado para filtragem.

O botão **"Remover"** irá retirar os itens selecionados da lista. Para selecionar um item na lista basta clicar sobre ele. O item selecionado ficará na cor **verde**. Para selecionar mais de um item, pressione a tecla **"Ctrl"** do teclado, e clique sobre os itens desejados.

**Observação:** itens selecionados para remoção são aqueles que estão com a cor verde e não os que têm a caixa de seleção marcada.

O botão **"Limpar"** irá remover todos os itens da lista.

Pode-se também configurar outros filtros através do botão ![Imagem 4: Pode-se também configurar outros filtros através do botão "Filtros" , localizado acima dos campos desta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/16583814366359) **"Filtros"**, localizado acima dos campos desta aba.

**Importante:** a criação dos filtros de **"Natureza"**, **"Centro de Resultado"** e **"Projeto"** através do **"Assistente de filtro"** para notas que possuem rateio, deverá ser realizada da seguinte forma:

Ao clicar no Assistente de filtro e optar pela opção **"Criar um novo filtro"**, deve-se informar manualmente somente as expressões conforme os exemplos abaixo:

**(1)** Para a natureza 3020100 - Aluguel/IPTU e 3020200 - Limpeza e conservação, a expressão será:

/\*intervalo NATUREZA 3020100:3020200 intervalo\*/

**(1)** Para o Centro de Resultado 10200 - Recursos Humanos e 100300 - Contábil, tem-se a expressão:

/\*intervalo CR 10200:100300 intervalo\*/

**(1)** Para o Projeto 1010000 - Imobiliário e 1020000 - Administrativo, a expressão:

/\*intervalo PROJETO 1010000:1020000 intervalo\*/

Ressaltando que as expressões devem seguir este padrão, tendo como modificação apenas os números de cadastro da Natureza, Centro de Resultado e Projeto. Após inserir a expressão, aponta-se um nome para o filtro criado e caso deseje que o mesmo seja aplicado de imediato basta acionar a opção **"Aplica filtro ao concluir"**.

![Imagem 5: Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que…](https://ajuda.sankhya.com.br/hc/article_attachments/26183101883799) Ao criar um campo adicional na TGFFIN, é necessário configurá-lo na view VGFFIN para que as telas e funcionalidades que utilizam a tabela Financeiro visualizem o referido campo.

Para que o sistema apresente o relatório, devem ser definidos os períodos de análise.

Os intervalos de **"Data de Negociação no Período"** e **"Data do Movimento no Período"** podem ser utilizados para restringir a consulta, para uma análise por competência.

Informe na Data de Negociação no Período, o intervalo de tempo dos títulos que deseja visualizar. Nos lançamentos, a Data da Negociação é a data da emissão do documento.

Na seção Data de Movimento no Período, informe o período da movimentação financeira, ou seja, o período em que os títulos foram registrados no sistema.

**Nota:** quando o parâmetro **"Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER"** estiver ativado, todos os textos que referenciam a data de movimento serão trocados por data de Entrada e Saída. Os filtros e as consultas que utilizam DHMOV passam a utilizar DTENTSAI (visível no monitor de consultas).

Sob a ótica financeira, a análise pode ser realizada considerando títulos pendentes, baixados ou ambos. Para restringir a consulta neste sentido, selecione **"Pendentes"**, **"Baixados"** ou ambos conforme a necessidade, e informe o **"Período de análise"** para as opções escolhidas.

![Imagem 6: Sob a ótica financeira, a análise pode ser realizada considerando títulos pendentes, baixados ou ambos. Para restringir…](https://ajuda.sankhya.com.br/hc/article_attachments/4407758817943)

A partir deste momento, defina algumas especificidades a serem apresentadas no relatório:

![Imagem 7: A partir deste momento, defina algumas especificidades a serem apresentadas no relatório:](https://ajuda.sankhya.com.br/hc/article_attachments/4407758829975)

Determine entre os títulos de **"Receita"**, **"Despesa"** ou **"ambos"**. Além disso, se serão considerados os títulos "Reais" ou os "Provisionados".

Ao marcar a opção **"Imprime faixa nos detalhes"**, o sistema colore as linhas do relatório em seus detalhes.

Por meio da marcação **"Requisições"**, incluem-se os lançamentos gerados pelas TOP's de Requisição.

Ao marcar a opção **"Produção"**, serão também visualizadas as notas de Produção.

Juntamente as opções Requisições e Produção, consta um filtro no qual pode-se especificar as notas de Requisição ou Produção.

Quando a opção **"Tratar Devol.de Compra como Desp.Negativa** e **Devol.de Venda como Rec.Negativa"** for marcada, as devoluções de venda e de compra serão deduzidas das receitas e despesas, respectivamente.

**Importante:** vale salientar que as requisições são tratadas no relatório de modo que seus valores serão **"negativos"** e as devoluções de requisição com valores **"positivos"**, de modo a se obter no fim a diferença entre estes valores. Vejamos um simples exemplo:

Requisição = R$100,00

Devolução de Requisição = R$50,00

Saldo = R$50,00

#### Apresentar resultado por:

Nesta opção deve-se indicar a forma de apresentação do resultado, sendo possível, três marcações distintas:

- Projeto;
- Projeto/Natureza;
- Projeto/C.Resultado.

Caso seja feita a escolha do agrupamento por **"Projeto"**, deve-se indicar apenas o **"Grau"** de detalhamento. Sendo a opção de agrupamento por **"Projeto/Natureza"** ou **"Projeto/C.Resultado"**, além do **"Grau"** indica-se também um **"Grau Interno"**.

O **"Grau"** e o **"Grau Interno"** se referem ao nível hierárquico do cadastro da **"Natureza"**, **"Centro de Resultado"** ou **"Projeto"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#top)

## Aba Avançado

![Imagem 8: Aba Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/4407758841239)

#### Seleção das Contas:

Se marcada, a opção **"Apenas Contas Ativas"**, o sistema irá avaliar apenas as operações realizadas com as contas **"Ativas"**.

Referente à **"Imprime Saldos"**, serão impressos os saldos das contas no final do relatório.

Ao preencher o campo **"Saldos Referentes à data"**, o sistema trará o(s) saldo(s) apurado(s) na data informada nesse campos.

Os botões **"Marcar Todas"** e **"Desmarcar Todas"** auxiliam na seleção de contas da grade.

Determine a **"Moeda"** que será considerada nas análises, quando houver transações financeiras em moedas estrangeiras.

#### Data para converter a moeda:

Defina a data a ser considerada para conversão da moeda. Pode-se escolher dentre as seguintes opções:

- **Negociação:** Converte pela data de negociação do Título. Usado quando o valor de conversão for fixado na data de negociação;
- **Vencimento:** Converte pela data de vencimento do Título. Usado quando a conversão ocorrer na data de vencimento;
- **Baixa:** Converte pela data da baixa. Usado quando o valor for convertido na data da baixa do Título;
- **Fixa:** Converte conforme um valor fixo informado no cadastro de moedas. Normalmente usado em negociações contratuais que estipulam um valor fixo de conversão durante a vigência do contrato

A opção **"Considerar Renegociações"**, quando selecionada, o sistema irá buscar os títulos renegociados no período.

Referente à opção **"Considerar Naturezas Especiais"**, esta buscará os dados cadastrados em Naturezas especiais localizado em **"Financeiro > Avançado > Naturezas especiais"**.

Por meio da opção **"Imprime Valor Líquido"**, o sistema analisa os valores marcados em **"Financeiro > Preferências > Componentes do valor líquido"**.

Imprima os filtro selecionados por meio da opção **"Imprime Filtros"**. Caso selecione esta opção, os filtros Data de Negociação no Período, Data do Movimento no Período, Vencendo no Período e Baixados no Período serão apresentados na impressão do relatório.

![Imagem 9: Para a geração dos valores, é necessário selecionar as naturezas analíticas. O sistema cria um relatório sintético a…](https://ajuda.sankhya.com.br/hc/article_attachments/26183101883799) Para a geração dos valores, é necessário selecionar as naturezas analíticas. O sistema cria um relatório sintético a partir dessas naturezas. Contudo, no relatório descritivo, as naturezas exibidas corresponderão às naturezas sintéticas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#top)

## Botão Visualizar em PDF

No alto da tela, temos o botão ![Imagem 10: No alto da tela, temos o botão "Visualizar em PDF" . Através dele você escolhe como deseja visualizar o relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/16583893700631) **"Visualizar em PDF"**. Através dele você escolhe como deseja visualizar o relatório gerencial, se **"em PDF"** ou **"em Planilha"**.

![Imagem 11: No alto da tela, temos o botão "Visualizar em PDF" . Através dele você escolhe como deseja visualizar o relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/15506365115927)

**Observação:** caso seja feita a exportação em planilha, será levada apenas a exportação do dados de forma bruta da consulta realizada a partir dos filtros, não sendo considerados os dados da aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#abaavan%C3%A7ado) e não será demonstrado cabeçalho e totalizadores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#top)

## Parâmetros que influenciam neste relatório

O parâmetro **"Usa data de entradas e saídas nos relatórios gerenciais? - DTENTSAIRELGER"**, quando ativado, além do comportamento normal, que altera todos os textos e consultas que referenciam a data de movimento pela **"Data de Entrada"** e **"Data de Saída"**, deixa de exibir a data de movimento na coluna "Emissão" e passa a exibir a **"Data de entrada e saída"**. O título da coluna **"Emissão"** não sofre alteração, independente de o parâmetro estar ou não ligado.

Para consultar o artigo referente aos Relatórios Formatados, acesse o link [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606194-Sint%C3%A9tico-por-Projeto#top)
