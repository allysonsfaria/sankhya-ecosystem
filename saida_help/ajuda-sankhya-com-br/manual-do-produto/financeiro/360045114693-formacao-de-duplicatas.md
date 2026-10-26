---
id: "360045114693"
titulo: "Formação de Duplicatas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:42:31Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "Parceiro", "Movimentação Financeira", "jrxml", "Financeiro", "Renegociação", "Agrupar Títulos", "CONFINFRETEDUPL", "DUPEMPDIF", "Formação de Duplicatas", "IMPTITDUPL", "Reimpressão", "TRAVAALTDHMOV", "br.com.sankhya.mgefin.formacao.duplicata", "Formação de Duplicatas manual", "Filtros e agrupamentos", "Automatização de processos", "Impressão e vencimento"]
---

# Formação de Duplicatas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312417790359) Módulo: Financeiro > Rotinas
```

---

A Formação de Duplicatas pode ser utilizada com dois objetivos principais:

1. Agrupar vários títulos de cobrança de um Parceiro em um único documento, propiciando diminuição no número de boletos bancários (que acarretarão na diminuição do custo de cobrança), facilidade de visualização dos débitos do Parceiro, conciliação dos movimentos, entre outras vantagens;
2. Gerar duplicatas formais, ou seja, documentos que oficializam os débitos correspondentes as notas fiscais de vendas à prazo e que podem ser utilizados por exemplo, para desconto de títulos.

**Importante:** a tela Formação de Duplicatas não exibe financeiros com código de moeda diferente de zero, pois possui um filtro fixo de **"CODMOEDA = 0"**, ou seja, essa tela não está preparada para títulos com moedas.

Para facilitar sua navegação nas funcionalidades desta tela, acesse os links abaixo:

| [Considerações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#consideraesiniciais) |  | [Aba Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#abafiltros) |
| --- | --- | --- |
| [Aba Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#abapreferncias) |  | [Aba Reimpressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#abareimpresso) |
| [Grade Totais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#gradetotais) |  | [Formação de Duplicatas - Modo...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#formaodeduplicatas-modosimplificado) |
| [Exemplos de Formação de Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#exemplosdeformaodeduplicatas) |  | [Configuração da Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#configuraodaimpresso) |
| [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#parmetrosqueinfluenciamnestarotina) |  |  |

![Imagem 2: Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4415929002903)

## Considerações Iniciais

Temos a opção de criar filtros específicos para facilitar sua busca através do Painel de Filtros.

Ao acionar o botão **"Aplicar"**, será apresentada uma lista de títulos que obedecem às opções selecionadas e aos filtros configurados.

O botão ![Imagem 3: O botão "Configurar grade" pode ser utilizado para personalização da grade, onde podemos remover ou inserir campos na…](https://ajuda.sankhya.com.br/hc/article_attachments/16282578629911) **"Configurar grade"** pode ser utilizado para personalização da grade, onde podemos remover ou inserir campos na tela.

Você poderá utilizar a opção ![Imagem 4: Você poderá utilizar a opção "Remover selecionados" da tela, para manter apenas os demais na grade principal e de forma…](https://ajuda.sankhya.com.br/hc/article_attachments/16282371953687) **"Remover selecionados"** da tela, para manter apenas os demais na grade principal e de forma inversa, a opção ![Imagem 5: Você poderá utilizar a opção "Remover selecionados" da tela, para manter apenas os demais na grade principal e de forma…](https://ajuda.sankhya.com.br/hc/article_attachments/16282371959447) **"Remover não selecionados"**.

O botão ![Imagem 6: O botão "Processa a formação de Duplicatas" solicita a formação de duplicatas para os títulos que foram selecionados na…](https://ajuda.sankhya.com.br/hc/article_attachments/16282876673047) **"Processa a formação de Duplicatas"** solicita a formação de duplicatas para os títulos que foram selecionados na grade.

**Nota:** quando os títulos a serem agrupados forem de bancos distintos, será necessário informar os dados da conta bancária na tela demonstrada na imagem abaixo, que será apresentada nesse caso.

![Imagem 7: Nota: quando os títulos a serem agrupados forem de bancos distintos, será necessário informar os dados da conta…](https://ajuda.sankhya.com.br/hc/article_attachments/4415988925719)

Caso sejam selecionados títulos que possuam o mesmo **"Banco"**, **"Conta Bancária"** e **"Tipo de Título"**, e você acione o botão **"Formar Duplicatas"**, a tela aberta para confirmação da Formação de Duplicatas, já será apresentada com os campos mencionados preenchidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Aba Filtros

Nesta aba, são apresentados os principais filtros a serem utilizados para apresentação dos títulos.

![Imagem 8: Nesta aba, são apresentados os principais filtros a serem utilizados para apresentação dos títulos.](https://ajuda.sankhya.com.br/hc/article_attachments/4415989221271)

Através do campo **"Filtrar por"**, você pode determinar a data a ser considerada para apresentação dos financeiros. Temos três opções de escolha:

- Data de Vencimento;
- Data de Negociação;
- Data do Movimento.

O filtro rápido por **"Período"** é de preenchimento obrigatório. A partir dos dados inseridos neste filtro, serão selecionados todos os títulos que se encaixem no período indicado. Essa seleção inicial pode ser refinada por outros filtros na tela, que serão vistos a seguir.

Por meio do campo **"Tipo"**, você poderá realizar a filtragem de acordo com o tipo do documento, sendo possíveis três opções:

- **Ambos:** Serão filtrados e apresentados os títulos de receitas e despesas.
- **Receita:** Serão filtradas e apresentadas somente as receitas;
- **Despesa:** Serão filtradas e exibidas na tela somente as despesas;

A seção **"Agrupar títulos"** indica se os títulos deverão ser agrupados para formar as duplicatas, ou seja, o painel de agrupamento deve ser utilizado para agrupar vários títulos em uma única duplicata. Caso não seja necessário agrupar os títulos, desative a seção de agrupamento, de modo que haverá uma duplicata para cada título financeiro. Vale ressaltar que sempre serão formadas duplicatas a partir do agrupamento de títulos de um mesmo parceiro ou parceiro matriz.

Logo abaixo da seção Agrupar títulos, temos os campos a serem utilizados para o agrupamento; são eles:

- Parceiro Matriz;
- Empresa;
- Banco;
- Conta;
- Data de Negociação;
- Agrupar apenas se houver mais de um título.

Os agrupamentos dos títulos podem ser feitos por **"Parceiro Matriz"**, ao invés de ser apenas por **"Parceiro"**. O exemplo mais ilustrativo dessa opção, é a formação de duplicatas para um parceiro que possui várias lojas, de modo que existam títulos emitidos para a Loja 1, Loja 2, Loja 3. Como todas são filiais de uma loja matriz, o Sankhya Om pode gerar/agrupar os títulos para este único parceiro matriz, ao invés de fazer um agrupamento para cada loja.

Você pode agrupar os títulos realizando quebras por **"Empresa"**, **"Banco"** e **"Conta"**, ou seja, o sistema pode agrupar a mesma data de acordo com a seleção do filtro **"Período"**, que tenham sido emitidos pela mesma empresa, cuja cobrança seja no mesmo banco e na mesma conta bancária.

O filtro por **"Data de Negociação"** assumirá, como denominação, a opção escolhida no campo Filtrar por e, consequentemente, serão agrupados de acordo com a data definida.

As quebras de formação podem ser realizadas de acordo com a necessidade de agrupamento. O sistema permite que cada opção seja selecionada e processada em qualquer combinação com as demais. Por exemplo:

- Parceiro Matriz - Banco;
- Parceiro Matriz - Conta - Data de Vencimento;
- Parceiro Matriz - Banco - Conta - Data de Movimento.

A identificação dos controles, indica a ordem e o nível do agrupamento. O primeiro nível de agrupamento é sempre por Parceiro ou Parceiro Matriz. Em seguida, os campos Empresa, Banco, Conta e Data de Negociação.

A marcação **"Agrupar apenas se houver mais de um título"** pode ser utilizada nos casos em que você desejar formar duplicatas visando o agrupamento dos títulos. Quando um deles não resulta em agrupamento, a formação perde o sentido, uma vez que nada será agrupado. Se esta marcação estiver selecionada e apenas um título for apresentado, ao clicar no botão **"Formar Duplicatas"** será exibida a seguinte mensagem:

**"A opção 'Agrupar apenas se houver mais de um título' somente pode ser usada para vários títulos!"**

Quando o campo de **"Data de vencimento"** não é utilizado, a formação de duplicatas aplica o **"Ajuste no vencimento"**, ou seja, todos os títulos que fazem parte de uma mesma duplicata têm sua Data de Vencimento ajustada para uma única data.

Esta nova data pode ser:

- **Primeiro:** Menor vencimento dos títulos da duplicata (mais antigo), ou seja, será pega a primeira data de vencimento entre os títulos.
- **Último:** Será pego o maior vencimento dentre os títulos da duplicata (mais recente), ou seja, será considerada a última data de vencimento entre os títulos e as demais datas serão ajustadas de acordo com esta.
- **Média:** O vencimento de cada título para a data atual. O cálculo é realizado da seguinte forma: é calculada para cada título a diferença em dias entre a data de vencimento e a data atual. A média é calculada em dias dessas diferenças e então o resultado é subtraído da data atual. Ou seja, será feita uma média entre as datas de vencimento e ajustará todas em uma data "média".
- **Fixo:** Através desta opção, a nova data de vencimento será informada manualmente no campo que será habilitado ao lado:

**Observação:** se os títulos estiverem sendo agrupados por Data de Vencimento, as opções referentes ao Ajuste de Vencimento ficarão desabilitadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Aba Preferências

![Imagem 9: Aba Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/4416015523095)

#### Seção Renegociação

Caso exista agrupamento de títulos, uma renegociação pode ser gerada ao efetuar a marcação **"Gerar renegociação ao agrupar"**. Se esta marcação for selecionada, a cada agrupamento será gerado um novo título como ocorre na renegociação. Esta marcação não é indicada para títulos com Centros de Resultado, Naturezas ou Projetos diferenciados, pois na renegociação, o sistema pega as informações do primeiro título, podendo acarretar distorções nas análises gerenciais. Não gerando renegociação, os títulos serão agrupados e não perderão as informações dos títulos originais.

Quando agrupados os títulos, o sistema totalizará os **"Outros impostos"** por imposto, e os lançará para os novos títulos. Quando a marcação mencionada estiver selecionada, o sistema irá ratear os Outros impostos entre as parcelas e os lançará para os novos títulos.

**Nota:** não poderá haver um mesmo imposto com alíquotas diferentes em mais de um título que for agrupar. No momento de **"Gerar a Duplicata"**, será solicitada uma **"Conta Bancária"** e o sistema utilizará o caminho de impressora e modelo informado nesta conta.  A marcação **"Preservar o campo 'Desdobramento da Duplicata'"**deve ser utilizada juntamente com a marcação Gerar Renegociação ao agrupar. Ela permite que em uma renegociação de títulos, cujos fretes sejam extras nota, o desdobramento não seja perdido, permitindo assim, a correta geração do livro fiscal. Indica que o valor do desdobramento deve ser mantido, caso contrário ele é anulado.

**Observação:** a marcação Preservar o campo 'Desdobramento da Duplicata' só será habilitada se a marcação Gerar Renegociação ao Agrupar for efetuada.

Quando a marcação **"Imprimir"** for realizada, indicará que a duplicata deverá ser impressa.

Se uma renegociação for gerada, a marcação **"Calcular nosso número"** pode ser utilizada para a geração de um boleto (.txt), e você pode informar o número de títulos por boleto.

A marcação **"Qtd. de títulos por boleto"** poderá ser alterada quando a marcação Calcular nosso número for marcada. Através desta marcação, você pode decidir a quantidade de títulos por boleto. Abaixo temos dois exemplos:

(1)**Exemplo 1:**

Suponha que a seleção de títulos para agrupamento seja:

| Parceiro | Banco | Conta | Data de Vencimento | Valor |
| --- | --- | --- | --- | --- |
| 100 | 1 | 16 | 01/02/2022 | $200,00 |
| 100 | 1 | 16 | 01/02/2022 | $200,00 |
| 100 | 1 | 16 | 01/02/2022 | $200,00 |
| 200 | 1 | 16 | 01/02/2022 | $300,00 |
| 200 | 1 | 16 | 01/02/2022 | $300,00 |
| 200 | 1 | 16 | 01/02/2022 | $300,00 |

Foram escolhidas as seguintes opções:

1. A opção Agrupar títulos por banco, conta bancária e data de vencimento;
2. A opção Gerar renegociação ao agrupar;
3. A opção Imprimir.

O sistema irá gerar 2 duplicatas, uma para cada agrupamento do cliente. Uma no valor de $600,00 para o Parceiro 100 e outra no valor de $900,00 para o Parceiro 200 e irá imprimir as duplicatas.

**(1)** **Exemplo 2:**

Imagine que a seleção de títulos para agrupamento seja a mesma do exemplo 1:

Foram definidas as seguintes opções:

1. A opção Agrupar títulos por banco, conta bancária e data de vencimento;
2. A opção Gerar renegociação ao agrupar;
3. A opção Imprimir;
4. A opção Calcular nosso número;
5. A Qtd. de títulos por boleto igual a 2.

O sistema irá gerar 4 duplicatas diferentemente do exemplo 1, pois no exemplo 1 cada duplicata possuía 3 títulos e agora solicita-se que a quantidade de títulos por boleto seja 2, então serão formadas as seguintes duplicatas:

| Parceiro | Banco | Conta | Data de Vencimento | Valor |
| --- | --- | --- | --- | --- |
| Duplicata 1 > 400,00 | | | | |
| 100 | 1 | 16 | 01/02/2022 | $200,00 |
| 100 | 1 | 16 | 01/02/2022 | $200,00 |
| Duplicata 2 > 200,00 | | | | |
| 100 | 1 | 16 | 01/02/2022 | $200,00 |
| Duplicata 3 > 600,00 | | | | |
| 200 | 1 | 16 | 01/02/2022 | $300,00 |
| 200 | 1 | 16 | 01/02/2022 | $300,00 |
| Duplicata 4 > 300,00 | | | | |
| 200 | 1 | 16 | 01/02/2022 | $300,00 |

As duplicatas 2 e 4 possuem apenas 1 título cada, pois não pode misturar títulos de Parceiros diferentes. O agrupamento do Parceiro 100 foi divido em duas duplicatas para considerar 2 títulos por boleto.

**Importante:** para o campo Qtd. de títulos por boleto, será feita a seguinte validação: Só aceitar dois ou mais títulos por boleto. Caso seja feita a tentativa de inserção de uma quantidade menor que dois, a seguinte mensagem será apresentada:

**"Quantidade mínima de boletos por título deve ser 2!"**

#### Seção Outros

Se o número não for informado para gerar duplicatas de despesa, será utilizada a mesma sequência empregada para duplicatas de receita. Por meio da marcação **"Informar número para duplicata de despesa"** é possível informar números para duplicatas de despesa, já que geralmente estas vêm de fornecedores e já são numeradas.

Para que esta marcação seja habilitada, o campo Tipo da aba Filtros deverá estar definido como Despesa. Caso contrário, este campo ficará disponível, porém, desabilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Aba Reimpressão

![Imagem 10: Aba Reimpressão](https://ajuda.sankhya.com.br/hc/article_attachments/4416007863319)

Nesta aba, encontram-se as configurações para a reimpressão de duplicatas.

O campo **"Duplicatas"** permite a digitação do intervalo das duplicatas.

Por meio do campo **"Tipo"**, você realiza a filtragem de acordo com o tipo do documento, sendo possíveis três opções:

- **Ambos:** Serão filtrados e apresentados os títulos de receitas e despesas;
- **Receita:** Serão filtradas e apresentadas somente as receitas;
- **Despesa:** Serão filtradas e exibidas na tela somente as despesas.

O botão ![Imagem 11: O botão "Reimprimir" só ficará habilitado se o botão "Aplicar" da mesma aba estiver sido utilizado. Caso você informe…](https://ajuda.sankhya.com.br/hc/article_attachments/16282699121175) **"Reimprimir"** só ficará habilitado se o botão ![Imagem 12: O botão "Reimprimir" só ficará habilitado se o botão "Aplicar" da mesma aba estiver sido utilizado. Caso você informe…](https://ajuda.sankhya.com.br/hc/article_attachments/16282715593879) **"Aplicar"** da mesma aba estiver sido utilizado. Caso você informe os filtros, porém clicar no botão Aplicar da tela, o botão não ficará habilitado.

O botão Reimprimir solicita a reimpressão dos títulos selecionados na grade. O botão **"Formar Duplicatas"** solicita a formação de duplicatas para os títulos selecionados na grade. Uma vez definidos os filtros, clique no botão Formar Duplicatas para que sejam agrupados os títulos para o parceiro, segundo os critérios adotados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Grade Totais

Na parte inferior esquerda da tela, temos um breve resumo da formação de duplicata, com a quantidade de títulos de Receita e Despesa que serão agrupados, a quantidade de duplicatas a serem geradas e os valores da operação. Se a soma das receitas for maior que as despesas, o valor será positivo e será gerado um título de receita; se a soma das despesas for maior que as receitas, o valor será negativo e será gerado um título de despesa.

![Imagem 13: Na parte inferior esquerda da tela, temos um breve resumo da formação de duplicata, com a quantidade de títulos de…](https://ajuda.sankhya.com.br/hc/article_attachments/4416016503319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Formação de Duplicatas - Modo Simplificado

A tela Formação de Duplicatas possui diversas configurações em seu Painel de filtros, que determinam a forma como as duplicatas serão geradas, como por exemplo, agrupamento, novo vencimento, geração de boleto, impressão, número inicial de documento, entre outras.

Esta tela conta com um recurso que simplifica as configurações a serem nela realizadas, facilitando e agilizando sua utilização. Podemos configurar a tela, de modo que as duplicatas serão sempre geradas por qualquer pessoa, seguindo um padrão e sem a necessidade de um treinamento aprofundado em todas as opções que a tela oferece.

Para utilização deste recurso, é necessário que o parâmetro **"Tela de formação de duplicatas simplificada - FORMDUPLSIMPLES"**esteja ativado. Uma vez ativado o parâmetro mencionado, alguns campos de configuração da tela Formação de Duplicatas deixarão de serem apresentados. Observemos na imagem abaixo, que em comparação com o modo normal, no modo simplificado algumas opções da aba [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693#abafiltros) deixam de ser exibidas, bem como a aba [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693#abapreferncias) deixa de ser apresentada.

![Imagem 14: Para utilização deste recurso, é necessário que o parâmetro "Tela de formação de duplicatas simplificada -…](https://ajuda.sankhya.com.br/hc/article_attachments/4422775186199)

**Importante:** independente da forma como a tela é utilizada, em seu modo normal ou no formato simplificado, seu comportamento e finalidade não são alterados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Exemplos de Formação de Duplicatas

**(1)** **Exemplo 1**

Uma empresa realizou várias operações de compra junto a um Parceiro no período de 02/maio a 20/maio, no valor total de R$ 8.532,10. Estas compras estão distribuídas em 8 títulos diferentes, distribuídos em boletos de 3 bancos distintos, com várias datas de vencimento. A empresa negociou com seu cliente o pagamento do valor total de todas as compras em uma única data, 20/junho.

**Como agrupar estes títulos em um único documento?**

1. Filtrar os títulos por data de negociação, ou seja, pela data em que o negócio foi realizado;
2. Estabelecer o período de negociação;
3. Optar por agrupar todos os títulos em um único documento, sem fazer quebras por empresa, por banco, por conta ou por parceiro matriz;
4. Ajustar o vencimento para uma data fixa, 20/junho;
5. Indicar ao sistema que serão considerados apenas os títulos de despesa e que deve ser gerada uma renegociação para estes títulos;
6. Indicar ao sistema qual será o tipo de título do documento único a ser gerado;
7. Criar um filtro para indicar quais são os títulos a serem agrupados; no caso deste exemplo, é conveniente filtrar os títulos do Parceiro junto ao qual foram realizadas as compras;
8. Acionar o botão **"Aplicar"**, que apresentará a lista de títulos que obedecem às opções selecionadas e ao filtro elaborado; na base da tela será apresentado um breve resumo da formação da duplicata, com a quantidade de títulos de receita e despesa que serão agrupados, a quantidade de duplicatas a serem geradas e os valores da operação;
9. Formar a duplicata, clicando no botão **"Formar Duplicatas"**;
10. Informar os dados da conta bancária.

**(1)** **Exemplo 2**

Uma empresa fez várias operações de compra e venda com o mesmo Parceiro, que totalizaram R$ 5.703,03 em títulos a receber e R$ 3.971,69 em títulos a pagar, cada um deles com uma data de vencimento diferente. Agora, pretende-se fazer uma compensação entre as receitas e as despesas e agrupar a diferença em um único título, cuja data de vencimento será a maior data de vencimento dos títulos que fizerem parte desta operação de agrupamento e compensação.

**Como realizar esta operação?**

1. Filtrar os títulos por data de vencimento;
2. Estabelecer o período de vencimento dos títulos;
3. Optar por agrupar todos os títulos em um único documento, sem fazer quebras por empresa, por banco, por conta ou por parceiro matriz;
4. Ajustar o vencimento para a última data entre os títulos a serem agrupados e compensados;
5. Indicar ao sistema que serão considerados títulos de receita e títulos de despesa e marcar para gerar renegociação;
6. Indicar no sistema qual será o tipo de título do documento único a ser gerado;
7. Criar um filtro para indicar quais são os títulos a serem agrupados;
8. Acionar o botão **"Aplicar"**, que apresentará a lista de títulos que obedecem às opções selecionadas e ao filtro elaborado, sendo receitas em azul e despesas em vermelho;
9. Formar a duplicata;
10. Se necessário, informar os dados da conta bancária.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Configuração da Impressão

Para a impressão de duplicatas, você deve ter configurado um modelo .txt, na aba [Duplicata](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaduplicata) da tela Preferências da Empresa pois, no momento da impressão, a formação de duplicata buscará este modelo cadastrado.

Esse modelo precisa ser previamente cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

**Importante:** em [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), podemos verificar o caminho que está configurado através do parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**. O caminho está indicado no campo **"Texto"**. Salve os modelos de .txt na pasta informada nesse parâmetro.

**Observação:** o sistema está apto a realização de impressões de duplicatas em formato **"jrxml"**.

Para a impressão do boleto, o modelo deve ser cadastrado na aba [Boletos/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas) do cadastro de Contas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)

## Parâmetros que influenciam nesta rotina

Para que o sistema realize a impressão de duplicatas de forma agrupada, onde esta impressão é feita via Relatório Formatado, temos como configuração, o parâmetro **"Imprime todos os tit. na formação de duplicatas? - IMPTITDUPL"** que, por padrão, é ligado. Quando este é desativado, ao solicitar a impressão será gerada a impressão de uma duplicata agrupada.

Por exemplo, desativando o referido parâmetro, caso existam três títulos de um mesmo Parceiro e a formação de duplicatas for realizada agrupando por Parceiro, teremos como resultado apenas uma duplicata que referencia os três títulos.

Quando o parâmetro **"Conservar Dt.Negoc.em Parcelamentos/Renegociações? - NALTDTNEG"**estiver ligado, irá conservar a Data de Negociação dos títulos nos Parcelamentos/Renegociações.

**Nota:** quando renegociar títulos com datas de negociação diferentes, será considerada a menor data.

**Observação:** na tela de Movimentação Financeira, o parâmetro **"Proibir alterar Data de Movto? - TRAVAALTDHMOV"** deve estar desligado para que possa funcionar este parâmetro da data de negociação. Já na tela de Renegociação de Títulos, o referido parâmetro afeta apenas a Data de Movimento.

O parâmetro **"Permitir agrupar emp.diferente na form.duplicata? - DUPEMPDIF"** quando ativado, permitirá que na formação de duplicatas, sejam agrupados títulos de empresas diferentes.

Ainda na tela de Formação de Duplicatas, é possível que sejam considerados os títulos financeiros referentes à fretes que são gerados a partir de uma nota. Isso permite que esses títulos possam ter uma duplicata formada.

Dessa forma, ative o parâmetro **"Considera financeiro de frete na formação de dupl.? - CONFINFRETEDUPL"**, que habilitará a marcação **"Considera financeiro de frete p/ formar duplicata?"** na tela de Formação de Duplicatas em suas Preferências na aba **"Parâmetros"** quando o layout anterior estiver em uso.

[GIF animado: Imagem 15: Dessa forma, ative o parâmetro "Considera financeiro de frete na formação de dupl.? - CONFINFRETEDUPL" , que habilitará…](https://ajuda.sankhya.com.br/hc/article_attachments/13591559136919)

Quando o novo layout estiver selecionado, a marcação Considera financeiro de frete p/ formar duplicata? será exibida no pop-up **"Formar Duplicatas"**.

[GIF animado: Imagem 16: Quando o novo layout estiver selecionado, a marcação Considera financeiro de frete p/ formar duplicata? será exibida no…](https://ajuda.sankhya.com.br/hc/article_attachments/13591456495895)

O parâmetro **"Numeração Duplicatas Sequência por Empresa? - SEQNRODUPLI"** terá os seguintes comportamentos em nosso sistema para definir a numeração de formação de duplicatas:

1. Quando estiver desligado, será utilizada a numeração determinada pela configuração realizada nas Preferências da Empresa, aba [Duplicata](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaduplicata), ou seja, a rotina de Formação de Duplicatas irá respeitar a numeração informada no campo **"Última duplicata"** e somar +1.
2. Se o parâmetro estiver ligado, a numeração será Sequencial e única, independente da Empresa, e o campo Última duplicata da aba Duplicata das Preferências da Empresa ficará desabilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas#top)
