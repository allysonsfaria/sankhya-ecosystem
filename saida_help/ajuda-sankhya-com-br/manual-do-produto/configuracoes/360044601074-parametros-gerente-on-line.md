---
id: "360044601074"
titulo: "Parâmetros - Gerente On-line"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601074-Par%C3%A2metros-Gerente-On-line"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:02Z"
rotulos: ["Configuração", "Relatórios Gerenciais", "Parâmetros", "DIAS_INAD", "EDITMP", "GOL-COMISSAO", "GOL-CUSTOVEMMP", "GOL-DATACOMPRA", "GOL-DATADEVCPA", "GOL-DATADEVVDA", "GOL-DATAMARGEM", "GOL-DATAVENDA", "GOL-QTDEPARC", "GOL-QTDEPROD", "GOL-SOMAOUTROS", "GOL-TEMCOMISSAO", "GOL-TIPOCUSTO", "Parâmetros - Gerente On-line manual", "Preferências", "br.com.sankhya.comercial.analise.con.gerente.online", "TEMMILHARNTDEC", "GOL-PRECCUSTO", "Título: Parâmetros Essenciais para Configuração do Gerente On-line", "MAXDIASFILGOL", "Gerente On-Line"]
---

# Parâmetros - Gerente On-line

Vejamos aqui os parâmetros que influenciam na ferramenta [Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line):

**Usar soma do custo da Matéria Prima? - GOL-CUSTOVEMMP:** Quando este parâmetro estiver ligado, análises de rentabilidade do Gerente On-Line, das centrais e das gerências serão afetadas. Ele habita um painel com o valor total dos custos das matérias primas na aba MP da Central de Vendas; além disso, este painel necessita que o parâmetro **"Soma dos custos das MPs no produto principal? - EDITMP"** esteja habilitado.

**Soma o vlr outros ao total da nota? - GOL-SOMAOUTROS:** Este parâmetro influencia no resultado apresentado no campo **"Total"** das análises **"Resultados Gerais"** e **"Vendas por Tipo"**. Se estiver **"Ativado"**, será considerado o valor do campo **"Outros"**, dos **"Totais"** da nota, na apresentação do resultado.

**Observações:**

**(3)**Em relação ao cálculo do Gasto Variável, será possível realizar a personalização do mesmo através de uma função criada no banco de dados (que retorne o valor do Gasto Variável), conforme a necessidade de cada empresa. Diante disto, para que o cálculo seja efetuado de acordo com a personalização, deve-se configurar o parâmetro **"Função p/ Calculo Gasto Variavel Central/Portal - CALGAVARCENPORT"**, inserindo no campo **"Texto"** (tela Preferências), necessariamente, o nome desta função. Caso o parâmetro acima mencionado não encontre-se configurado com o nome da função personalizada, tem-se que será utilizada a fórmula de cálculo nativa do sistema.

**(3)**Para o correto funcionamento da função, deve-se informar os parâmetros **"P\_NUNOTA"** e **"P\_SEQUENCIA"** na mesma.

**(3)**Através do parâmetro **"Função p/ Ativar o Cálculo do Gasto Variavel Centr - CALGACENPORGOL"**, você poderá definir se deseja utilizar a personalização do cálculo do Gasto Variável no Gerente On-line - GOL e/ou no Portal/Central de Vendas, de acordo com as seguintes opções:

- Ambos;
- Apenas Central/Portal;
- Apenas GOL.

**(3)**O sistema lerá a opção definida no parâmetro de chave CALGACENPORGOL e, conforme a opção marcada, ele executará o valor definido no parâmetro de chave CALGAVARCENPORT, caso possua.

**(3)**Para o controle do parâmetro CALGACENPORGOL temos nas [Preferências do Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line), aba [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abamargemdecontribuio), o campo **"Gasto variável personalizado"** para que você escolha a opção para exibição no Gerente On-line - GOL e/ou no Portal/Central de Vendas.

Através do parâmetro **"Período a ser considerado no cálculo do Estoque Médio - GOL-PERESTMED"** define-se quantos meses serão usados para realizar o cálculo do **"Estoque Médio"** relativo ao **"Prazo Médio de Estoques - PME"** do Ciclo Operacional Financeiro do Gerente On-line.

Quando o parâmetro **"Habilitar consolidação automática Gerente Online? - AUTOCONSGOLEVO"** estiver desligado, o sistema não irá gerar as consolidações automaticas.

Alguns parâmetros podem ser definidos através das [Preferências do Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line) ou por meio da tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), são eles:

**Aba Geral**

**Dias para considerar um título perdido - DIAS\_INAD:** Defina neste parâmetro a quantidade de dias após o vencimento para considerar um título uma inadimplência.

**Data a ser considerada na Compra - GOL-DATACOMPRA:** Determine aqui, a data de compra para análise dos resultados. Tem-se as opções **"Negociação"**, **"Movimentação"**, **"Faturamento"**, **"Validade"** ou **"Entrada/Saída"**.

**Data a ser considerada na devolução de Compra - GOL-DATADEVCPA:** Aponte a data de devolução de compras para análise dos resultados. Dentre as opções Negociação, Movimentação, Faturamento, Validade ou Entrada/Saída.

**Data a ser considerada na Venda - GOL-DATAVENDA:** Defina neste parâmetro a data de venda para análise dos resultados. Tem-se as opções Negociação, Movimentação, Faturamento, Validade ou Entrada/Saída.

**Data a ser considerada na devolução de Venda - GOL-DATADEVVDA:** Tem-se aqui a data de devolução de vendas para análise dos resultados. Tem-se as opções Negociação, Movimentação, Faturamento, Validade ou Entrada/Saída.

**Quantidade de Parceiros a visualizar - GOL-QTDEPARC:** Por meio deste parâmetro, você indicará a quantidade de parceiros utilizada na análise **"Vendas por Parceiros"**.

**Quantidade de Produtos - GOL-QTDEPROD:** Informe neste parâmetro a quantidade de produtos utilizada na análise "Vendas por Produtos".

**Aba Margem de Contribuição**

**Data para Gastos Fixos - GOL-DATAMARGEM:** Defina neste parâmetro, a data que o sistema considera para apuração dos gastos fixos do período.

**Custo a ser considerado - GOL-TIPOCUSTO:** Aponte através deste parâmetro, o custo a ser considerado na análise do CMV (Custo da  Mercadoria Vendida).

**GOL-TEMCOMISSAO - GOL-TEMCOMISSAO:** Descreva aqui, as comissões calculadas pelo sistema que influenciam nos resultados obtidos nas análises.

**GOL-COMISSAO - GOL-COMISSAO:** Com este parâmetro determine a comissão que será considerada nos cálculos da coluna Gastos Variáveis. Este parâmetro quando configurado pela tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) informa-se o valor correspondente a cada opção; à frente de cada opção, pode-se notar seu respectivo valor. São elas:

- **Fixa - 0:** Por esta opção, determina-se um percentual fixo para o cálculo da comissão, informando-o no espaço à frente.
- **Nota - 1:** Esta opção define que as comissões irão obedecer aos respectivos percentuais informados nas notas ([Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)).
- **Vendedor - 2:** Definindo-se este campo com esta opção, a comissão será calculada com base na configuração feita no [Cadastro de Vendedores/Compradores > aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral).
- **Produto - 3:**Por esta opção, a comissão será calculada com base na configuração feita no [Cadastro de Produtos > aba Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abavenda).
- **Tipo de Negociação - 4:** Esta opção determina que as comissões seguirão as configurações feitas no [Cadastro de Tipos de Negociação > aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas).

**Considera Tipo Impresso Kit da TOP no GOL? - CONSKITTOPGOL:** quando estiver ligado e for realizada uma análise, de acordo com a configuração do campo **"Kit/Componentes - Impressão e Livro Fiscal"** da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) teremos:

- **KIT:** Irá considerar o produto pai;
- **KIT e Componentes:** Serão considerados seus componentes;
- **Componentes:** Serão considerados seus componentes.

**Observação:** se o parâmetro acima estiver desligado e for realizada a análise, serão considerados sempre apenas os componentes do KIT.

**Usar % Custo Variável do cad.de Vendedores? - GOL-CVVEND:** Com este parâmetro ligado, o sistema irá considerar o campo **"% Custo Variável"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral) do cadastro de [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores) ao realizar a análise de rentabilidade da nota conforme o resultado das vendas de cada vendedor.

**Verifica se tem milhar e no tem decimal - TEMMILHARNTDEC:** Com este parâmetro ligado, ao exportar o relatório no formato Excel, os dados não serão apresentados com casa decimal, mas terão o ponto separador de milhar.

**GOL-PRECCUSTO - GOL-PRECCUSTO:** este parâmetro determina qual campo será utilizado nas consultas para calcular os custos que serão apresentados no gráfico [Ciclo Operacional Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line#ciclooperacionalfinanceiro). Os valores possíveis são:

- 0 - Reposição;
- 1 - Gerencial;
- 2 - Variável;
- 3 - Médio sem ICMS;
- 4 - Médio com ICMS;
- 5 - Entrada com ICMS;
- 6 - Entrada sem ICMS.

Por padrão, o campo **"Valor"** deste parâmetro virá configurado com a opção 0-Reposição.

**Observação:** a combinação "-1" não se aplica ao **Sankhya Om**.

**Nota:** na tela [Gerente On-Line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613), na aba [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abamargemdecontribuio) localizada no botão **"Configurações"**, o campo **"Custo a ser considerado"** não interfere no retorno do custo para os Dados Ciclo Operacional Financeiro.

**Máximo de dias para filtrar registros no GOL - MAXDIASFILGOL:** por meio deste parâmetro, é possível definir o limite máximo de dias permitido para consultas no Gerente On-line. O sistema validará a data inicial informada e, caso o limite de dias seja excedido, exibirá uma mensagem de alerta ao usuário e bloqueará a execução da consulta.

**Observação:** este parâmetro é válido somente para os dados online e não se aplica aos processos de consolidação.

Os parâmetros abaixo foram criados para tornar o carregamento de informações na tela do GOL mais rápido e eficiente, especialmente quando a base de dados é muito grande. Sem esses ajustes, o sistema busca todos os dados disponíveis, o que pode demorar bastante. Com os parâmetros configurados, o usuário pode escolher quais informações deseja carregar, evitando demoras desnecessárias, são eles:

**Otimização para Receita/Despesa GOL - GOL-OTIMCOMPRA**: é utilizado para otimizar a busca de informações sobre compras. Ao ativá-lo, o sistema carrega apenas os dados essenciais dessa área, evitando buscas demoradas e deixando a navegação mais rápida.

**Otimização para Venda GOL - GOL-OTIMVENDA**: melhora a desempenho quando se trata de vendas. Com ele, apenas os dados mais importantes desse setor são carregados, acelerando a exibição das informações na tela.

**Otimização para Receita/Despesa GOL - GOL-OTIMRECDESP**: ajuda a organizar melhor as consultas financeiras, como receitas e despesas. Com esse ajuste, o sistema evita buscas muito amplas, carregando apenas os dados necessários para um acesso mais rápido.

Um exemplo de índice que pode ser configurado nesses parâmetros é: **/\*+index(TGFFIN TGFFIN\_I03)\*/.**

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601074-Par%C3%A2metros-Gerente-On-line#top)

![Imagem 1: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16695075508759) Acesse também:

[Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line)

[Botões topo da tela - Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110773-Bot%C3%B5es-no-topo-da-tela-Gerente-On-line)

[Preferências - Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line)

[Visualização/Impressão - Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112273-Visualiza%C3%A7%C3%A3o-Impress%C3%A3o-Gerente-On-line)
