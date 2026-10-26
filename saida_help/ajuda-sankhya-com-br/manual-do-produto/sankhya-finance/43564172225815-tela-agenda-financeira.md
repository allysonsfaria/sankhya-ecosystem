---
id: "43564172225815"
titulo: "Tela Agenda financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro > Sankhya Finance"
atualizado_em: "2026-09-26T11:54:10Z"
---

# Tela Agenda financeira

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#o-que-e-e-para-que-serve)
- [A regra que organiza a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#a-regra-que-organiza-a-tela)
- [Filtros disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#filtros-disponiveis)
- [Cards de resumo](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#cards-de-resumo)
- [Gráfico Fluxo do período](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#grafico-fluxo-do-periodo)
- [Resumo do período](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#resumo-do-periodo)
- [Insights do período](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#insights-do-periodo)
- [A pagar × A receber, Despesas × Receitas e Comparativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#paineis-comparativos)
- [Lista de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#lista-de-titulos)
- [Detalhes do título](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#detalhes-do-titulo)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#pontos-de-atencao)

**Módulo:** Sankhya Finance

**Caminho de acesso:** Menu Principal › Sankhya Finance › Agenda financeira

Esta tela está disponível exclusivamente para clientes Sankhya Cloud.

## O que é e para que serve

A **Tela Agenda financeira** reúne receitas e despesas em uma única linha do tempo, com o dia como eixo: o que vence no período, o que já foi liquidado, o que está vencido e se o saldo do período fecha positivo. Use-a para responder três perguntas do dia a dia da tesouraria — o que ainda precisa entrar e sair até o fim do período, em que dias a concentração é maior, e se o resultado fecha no azul — e planejar a semana ou o mês a partir disso.

Ela não substitui a **Gestão financeira**, que é onde você trabalha título a título: a Agenda é a leitura de calendário, a Gestão é a operação.

Ela faz parte do conjunto de telas do Sankhya Finance; para entender como se encaixa na solução completa, consulte o [Guia Sankhya Finance](https://ajuda.sankhya.com.br/hc/pt-br/articles/41301087909655-Guia-Sankhya-Finance).

---

## A regra que organiza a tela

Antes de olhar os painéis, entenda como um título é posicionado no período — essa regra vale para todos os cards, gráficos e listas da tela:

- **Título em aberto e provisão** — o período é confrontado com a **Data de vencimento**.
- **Título baixado** — o período é confrontado com a **Data da baixa**.

Ou seja: o que ainda não foi liquidado aparece no dia em que vence; o que já foi liquidado aparece no dia em que foi liquidado.

**ℹ️ Nota**

Títulos renegociados ficam fora de todos os números da tela.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Filtros disponíveis

Abra o painel de filtros pelo ícone no canto superior esquerdo da tela. O indicador numérico ao lado do ícone mostra quantos filtros estão ativos

![Imagem 1: Abra o painel de filtros pelo ícone no canto superior esquerdo da tela. O indicador numérico ao lado do ícone mostra…](https://ajuda.sankhya.com.br/hc/article_attachments/43567689742231)

### Período

Informe as datas **De** e **Até**, digitando ou pelo calendário. O botão **Hoje** volta para a data atual.

**⚠️ Atenção**

O período máximo é de **366 dias**. Recortes maiores não são aceitos.

### Empresa

Informe o código ou o nome da empresa. Sem seleção, a tela considera todas as empresas que o seu usuário tem permissão para ver.

### Tipo

Duas marcações que definem a natureza dos títulos considerados:

- **Receitas**
- **Despesas**

### Situação

Quatro marcações que definem quais situações entram na tela:

- **Real** — títulos efetivos.
- **Provisão** — títulos provisionados. Só têm efeito quando a preferência Provisão também está ligada.
- **Pendentes** — títulos ainda não liquidados.
- **Baixados** — títulos já liquidados.

### Preferências

Sete marcações que mudam o que a tela calcula e exibe:

- **Valor líquido (receitas)** — exibe as receitas pelo valor líquido em vez do valor bruto.
- **Valor líquido (despesas)** — o mesmo para as despesas.
- **Baixa futura** — trata o título baixado com data de baixa posterior a hoje como se estivesse em aberto. Nesse caso ele passa a ser posicionado pela data de vencimento.
- **Títulos antecipados** — inclui na tela os títulos que participaram de antecipação de recebíveis. Desligada, esses títulos desaparecem de todos os totais e listas.
- **Provisão** — habilita a exibição de títulos provisionados. Funciona em conjunto com a marcação Provisão do bloco Situação.
- **Float** — soma os dias de carência do tipo de título à data de vencimento, deslocando o título no calendário. Aplica-se apenas a títulos em aberto; título baixado sempre aparece na data da baixa.
- **Rateio** — desdobra o título rateado em uma linha por rateio.

**ℹ️ Nota**

Com **Valor líquido** desligado, a tela usa o valor do desdobramento nos títulos em aberto e o valor da baixa nos títulos liquidados. Ligada, usa o valor líquido: soma multa e juros quando o tipo indica cobrança, despesas de cartório, valor do vendor e impostos; subtrai descontos, IRRF, ISS e INSS retidos e desconto de cartão; e aplica variação cambial, juros e multa de negociação e liberações.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Cards de resumo

Cinco cards no topo da tela abrem a leitura, cada um com o valor e a quantidade de títulos.

![Cards de resumo · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43567673234967)

| **Card** | **O que soma** |
| --- | --- |
| Saldo do período | (A receber + Recebidos) − (A pagar + Pagos) |
| A receber | Títulos de receita em aberto, mais as provisões de receita quando a preferência Provisão está ligada |
| Recebidos | Títulos de receita liquidados no período |
| A pagar | Títulos de despesa em aberto, mais as provisões de despesa quando a preferência Provisão está ligada |
| Pagos | Títulos de despesa liquidados no período |

**ℹ️ Nota**

Com a preferência **Rateio** ligada, a contagem exibida abaixo de cada card passa a contar linhas de rateio, e não títulos. Um título com três rateios conta como três.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Gráfico Fluxo do período

Logo abaixo dos cards, o gráfico mostra a distribuição diária de entradas e saídas dentro do período filtrado — é onde você enxerga em que dias a movimentação se concentra.

![Gráfico Fluxo do período · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43567689744919)

### O que o gráfico exibe

Quatro séries, uma por combinação de natureza e situação:

- **Recebidos** — receitas liquidadas, posicionadas pela data da baixa.
- **A receber** — receitas em aberto, posicionadas pela data de vencimento.
- **Pagos** — despesas liquidadas, posicionadas pela data da baixa.
- **A pagar** — despesas em aberto, posicionadas pela data de vencimento.

Com a preferência Provisão ligada, o gráfico ganha mais duas séries: **Provisão de receita** e **Provisão de despesa**.

### Modos de leitura

- **Diário** — o valor de cada dia isoladamente.
- **Acumulado** — o valor somado desde o início do período.

Dia sem título aparece com valor zero, para que a linha não tenha interrupção. Use o controle deslizante abaixo do gráfico para navegar em períodos longos, e o botão de expandir para ampliar o painel.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Resumo do período

Ao lado do gráfico, o painel Resumo do período traduz a mesma leitura em três grupos de números.

![Resumo do período · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43567689746583)

| **Grupo** | **Linha** | **O que representa** |
| --- | --- | --- |
| Saldos | Em aberto | A receber − A pagar |
|  | Baixado | Recebidos − Pagos |
| Baixas | Atrasadas | Saldo das baixas ocorridas depois do vencimento, receitas menos despesas |
|  | Antecipadas | Saldo das baixas ocorridas antes do vencimento, receitas menos despesas |
| Totais | Pago + a pagar | Compromisso total de saída no período |
|  | Recebido + a receber | Expectativa total de entrada no período |

**ℹ️ Nota**

Baixa ocorrida exatamente na data de vencimento não entra em Atrasadas nem em Antecipadas: ela é classificada como baixa no prazo.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Insights do período

Fechando a leitura do topo da tela, o painel Insights traz leituras automáticas do recorte filtrado — cada um só aparece quando a condição correspondente é observada nos dados; por isso nem sempre os cinco são exibidos ao mesmo tempo.

![Insights do período · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43567673238039)

| **Insight** | **O que informa** |
| --- | --- |
| Vencidos represados | Quantidade e valor dos títulos em aberto com vencimento anterior a hoje |
| Poucos títulos, muito valor | Quantidade e valor dos títulos de R$ 20.000 ou mais, considerando abertos e liquidados |
| Saldo projetado negativo | Primeiro dia do período em que o saldo acumulado fica negativo |
| Pico de saída | Dia de maior saída no período e quanto ele representa do total de saídas |
| Concentração em um parceiro | Parceiro de maior volume no período e quanto ele representa do total |

Os insights respeitam todos os filtros e preferências ativos na tela.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## A pagar × A receber, Despesas × Receitas e Comparativo

Na faixa inferior da tela, três painéis colocam o período sob perspectivas diferentes.

![Painéis comparativos · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43567673238295)

- **A pagar × A receber** — confronta apenas o que está em aberto no período, para você ver de que lado pende o saldo ainda não liquidado.
- **Despesas × Receitas** — confronta o total do período, somando realizado e previsto de cada lado.
- **Comparativo** — confronta Recebidos e Pagos do período filtrado com o mesmo recorte de datas no ano anterior, com a variação percentual. Considera somente títulos liquidados, posicionados pela data da baixa.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Lista de títulos

Use o link **Ver títulos**, no canto superior direito da tela, para abrir a lista dos títulos que compõem os números. Clicar em um card de resumo abre a lista já no recorte correspondente.

![Lista de títulos · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43567689750423)

### Recortes disponíveis

**Tudo**, **A receber**, **Recebidos**, **A pagar**, **Pagos** e **Vencidos**.

### Colunas

Situação, Nº Financeiro, Empresa, Parceiro, Tipo, Tipo de título, Emissão, Vencimento, Data da baixa, Valor original, Juros, Multas, Descontos, Valor líquido, Conciliado, Provisão e Rateio.

A lista é paginada e a ordenação é aplicada sobre o recorte inteiro, não apenas sobre a página exibida.

### Situação do título

A coluna Situação apresenta um status por título, avaliado nesta ordem de precedência:

1. Antecipado
2. Renegociado
3. Compensado
4. Baixado parcial
5. Baixado
6. Vencido
7. Aberto

O que define que um título está baixado é a **Data da baixa** preenchida.

**ℹ️ Nota**

Com a preferência **Rateio** ligada, o título rateado aparece como uma linha por rateio. As cinco colunas de valor — Valor original, Juros, Multas, Descontos e Valor líquido — são rateadas pelo percentual de cada rateio; as demais colunas repetem o conteúdo do título. Título sem rateio continua aparecendo em uma linha única.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Detalhes do título

Selecione um título na lista para abrir o painel de detalhes, com os campos que não cabem na grade.

| **Campo** | **Conteúdo** |
| --- | --- |
| Parceiro | Nome do parceiro |
| Número da nota | Número da nota que originou o título |
| Tipo de operação | Descrição do tipo de operação |
| Vencimento | Data de vencimento |
| Data da baixa | Data da baixa, quando houver |
| Natureza | Descrição da natureza, e se é receita ou despesa |
| Tipo | Real ou Provisão |
| Banco | Banco vinculado ao título |
| Centro de resultado | Centro de resultado do título |
| Projeto | Projeto do título |
| Histórico | Histórico registrado no título |
| Valor original | Valor do desdobramento |
| Valor líquido | Valor líquido apurado |

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43564172225815-Tela-Agenda-financeira#sumario)

---

## Pontos de atenção

### Duas datas organizam a mesma tela

Título em aberto aparece pelo vencimento; título liquidado aparece pela data da baixa. Ao comparar a Agenda com outra tela, confira qual data cada uma usa antes de concluir que há divergência.

### A preferência Float move só o que está em aberto

Ela soma a carência do tipo de título à data de vencimento. Título liquidado continua na data da baixa, sem deslocamento.

### Títulos antecipados somem quando a preferência está desligada

Se o total da Agenda não bater com a Gestão financeira, confira essa marcação antes de qualquer outra coisa.

### Provisão depende de duas marcações

O título provisionado só aparece quando a preferência Provisão e a situação Provisão estão ligadas ao mesmo tempo.

### Rateio muda a contagem

Com a preferência ligada, os contadores passam a contar linhas de rateio, não títulos. O valor total não muda; a quantidade, sim.

### Renegociados estão fora

Nenhum número da tela considera títulos renegociados.

### Período máximo de 366 dias

Para análises mais longas, use o Fluxo de caixa ou o Comparativo.
