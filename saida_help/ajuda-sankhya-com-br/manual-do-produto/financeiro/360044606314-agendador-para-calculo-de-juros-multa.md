---
id: "360044606314"
titulo: "Agendador para Cálculo de Juros/Multa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:39:06Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Juros", "Agendamento", "Financeiro", "Agendador para Cálculo de Juros/Multa", "br.com.sankhya.fin.agendador.calculo.juro.multa", "Agendador para Cálculo de Juros/Multa manual", "Agendamento cálculo juros/multa", "Parâmetros influenciam rotina", "Configuração horário e filtro", "Multa"]
---

# Agendador para Cálculo de Juros/Multa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312289617431) Módulo: Financeiro > Avançado > Agendadores
```

---

Esta tela realiza o Agendamento do Cálculo de Juros/Multa a partir da configuração do filtro e do horário que será executado o cálculo.

| [Descrição da Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#descriodatela) | [Tabela do Banco de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#tabeladobancodedados) |
| --- | --- |
| [Processamento do Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#processamentodoarquivoderetorno) | [Exemplo do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#exemplodoprocesso) |
| [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#parmetrosqueinfluenciamnestarotina) |  |

![Imagem 2: Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360091690734)

## Descrição da Tela

Além do botão para filtro personalizado, existem ainda os campos **"Tipo de Título"**, **"Natureza"**, **"Centro de Resultado"**, **"Projeto"** e **"Conta Bancária"**, que são utilizados também como filtros ao efetuar o agendamento.

No campo **"Horário de Execução"** informe a hora que será utilizada para efetuar o agendamento. O Agendamento será efetuado uma vez ao dia, portanto, se já foi efetuado o agendamento do dia, o próximo será feito no mesmo horário configurado.

O sistema calculará os juros e multas para todos os financeiros de receita com a data de vencimento anterior a data da execução da rotina, com o campo nosso número preenchido, com a conta bancária informada (será utilizada para gerar a linha digitável e o código de barras), que não sejam títulos de provisão, que não estejam baixados e, se houverem filtros na tela de agendador, eles também serão utilizados.

Você pode configurar no parâmetro **"Dias p/ novo vencimento de títulos reprocessados - DIASNOVOVENC"** a quantidade de dias que será acrescida à data de vencimento para calcular a nova data de vencimento do título; caso a nova data seja no sábado ou domingo, ela será alterada para a segunda-feira e os juros e as multas serão calculados para todos os dias até a nova data de vencimento. Como por exemplo:

Caso tenhamos um título de receita cujo vencimento seja no dia 15/08/2012. Suponhamos que neste parâmetro esteja configurado para 10 dias. Então, o novo vencimento do título será a Data Atual + 10 dias. Suponhamos que a Data Atual seja 01/09/2012, o novo vencimento será dia 11/09/2012.

Caso a data atual seja 05/09/2012 o vencimento teria que ser dia 15/09/2012, mas será armazenada a data 17/09/2012, pois nos dias 15 e 16 será final de semana.

O percentual usado para calcular o juros e a multa, virá do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) quando houver, conforme o exemplo da imagem abaixo. Caso o Parceiro não tenha uma configuração específica, o sistema irá utilizar o percentual de juros configurado no parâmetro **"Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO"**, o percentual de multa do parâmetro **"Percentual da multa - PERCMULTA"** e o tipo de juros do parâmetro **"Cálculo de juro simples ou composto - JUROSIMPLES"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#top)

## Tabela do Banco de Dados

O Agendamento buscará os títulos e será efetuado o cálculo de juros e multa em conformidade com o que estiver configurado, seja parâmetro ou dados do Cadastro do Parceiro e gravará as informações na tabela TGFHJUR. Esta contém os campos:

- **NUFIN:** Número Único do Título;
- **DHJUR:** A data em que foi efetuado o agendamento do cálculo de juros e multa;
- **VLRJURO:** O valor de Juros calculados pelo agendamento considerando a data de vencimento do título até a data de vencimento calculada pelo agendador e aplicando o percentual informado seja pelo Cadastro do Parceiro ou parâmetros;
- **VLRMULTA:** O valor de Multa calculado pelo agendamento considerando o percentual informado seja pelo Cadastro do Parceiro ou parâmetros;
- **CODBARRA:** Código de Barras Calculado através dos dados da conta bancária informada no título na rotina de movimentação financeira;
- **LINHADIGITAVEL:** Linha Digitável Calculada através dos dados da conta bancária informada no título na rotina de movimentação financeira;
- **DTVENC:** A data de vencimento resultante do processo de agendamento levando em consideração o parâmetro **"Dias p/ novo vencimento de títulos reprocessados - DIASNOVOVENC"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#top)

## Processamento do Arquivo de Retorno

No momento de processar o arquivo de retorno no EDI bancário, o sistema consegue encontrar o título e fazer a sua baixa de maneira correta, para isso, é necessário que a marcação **"Obter o valor do título do próprio título"** do botão de **"Preferências"**,  seja selecionada, pois virá no arquivo um valor do título diferente ao que está na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874). O valor do título já virá com o valor de juros e multas anteriormente calculados.

![Imagem 3: No momento de processar o arquivo de retorno no EDI bancário, o sistema consegue encontrar o título e fazer a sua baixa…](https://ajuda.sankhya.com.br/hc/article_attachments/360091691074)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#top)

## Exemplo do Processo

Parâmetros:

- **Dias p/ novo vencimento de títulos reprocessados - DIASNOVOVENC** = 10;
- **Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO** = 0,20;
- **Percentual da multa - PERCMULTA** = 9;
- **Cálculo de juro simples ou composto - JUROSIMPLES** = Ligado;
- **Dias de carência para atraso - DIASCAR** = 2

Tela de [Cadastros de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) aba [Juros/Multas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abajurosmultas):

Parceiro 155 - Parceiro sem juros configurado;

Parceiro 156 -  juros simples / 2% de juros / 1% de multa;

Parceiro 157 - juros compostos / 2% de juros / 1% de multa.

Tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874):

Criados os títulos abaixo:

Parceiro 155, número único 895943943;

Parceiro 156, número único 895945945;

Parceiro 157, número único 895946946.

Nosso número deve ter obrigatoriamente mais de 7 dígitos, todos com vencimento para 01/04/2014.

Tela Agendador para cálculo de juros/Multa:

Filtro: Parceiros 155, 156, 157;

Tipo de título - 0;

Natureza - 1.01.06.01;

Centro de Resultado - 105002;

Projeto - 10001000;

Conta bancária - 10;

Horário de execução 16:27.

Ao simular a baixa, os valores de juros e multas são calculados conforme as configurações acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#top)

## Parâmetros que influenciam nesta rotina

No parâmetro **"Dias p/ novo vencimento de títulos reprocessados - DIASNOVOVENC"** você configura a quantidade de dias que será acrescida à data de vencimento para calcular a nova data de vencimento do título;

Informe no parâmetro **"Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO"** o percentual de juros;

Aponte no parâmetro **"Percentual da multa - PERCMULTA"** o percentual de multa;

Através do parâmetro **"Cálculo de juro simples ou composto - JUROSIMPLES"** você indica o tipo de juros.

Os seguintes parâmetros necessitam estar desabilitados para que seja efetuado o calculo dos dias de vencimento corretamente:

- **"Folga na Segunda? - FOLGASEG"**;
- **"Folga na Terça? - FOLGATER"**;
- **Folga na Quarta? - FOLGAQUA"**;
- **Folga na Quinta? - FOLGAQUI"**;
- **Folga na Sexta - FOLGASEX"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606314-Agendador-para-C%C3%A1lculo-de-Juros-Multa#top)
