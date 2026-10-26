---
id: "41307193691927"
titulo: "Tela Fluxo de caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro > Sankhya Finance"
atualizado_em: "2026-09-25T20:03:50Z"
rotulos: ["Relatórios", "Análise Financeira", "Movimentação Financeira", "Financeiro", "Fluxo de Caixa"]
---

# Tela Fluxo de caixa

Módulo: Financeiro
Caminho de acesso: Menu Principal › Sankhya Finance › Fluxo de caixa

Esta tela está disponível exclusivamente para clientes Sankhya Cloud.

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#oque)
- [Filtros disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#filtros)
- [Indicadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#indicadores)
- [Fluxo Projetado](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#projetado)
- [Insights](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#insights)
- [Resultado mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#mensal)
- [Fluxo líquido mensal por natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#liquido-natureza)
- [Fluxo por natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#natureza)
- [Análise de Aging](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#aging)
- [Distribuição por banco](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#banco)
- [Detalhamento ao clicar nos gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#detalhamento)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#pontos)

## O que é e para que serve

O **Fluxo de caixa** reúne entradas e saídas em uma visão integrada, com projeção de curto prazo, distribuição por natureza e análise de vencimentos. Use esta tela para responder se o caixa se sustenta nos próximos dias, de onde vem e para onde vai o dinheiro, e qual a idade dos valores a receber e a pagar. A tela é de consulta: não realiza lançamentos nem permite editar títulos.

Ela faz parte do conjunto de telas do Sankhya Finance; para entender como se encaixa na solução completa, consulte o [Guia Sankhya Finance](https://ajuda.sankhya.com.br/hc/pt-br/articles/41301087909655-Guia-Sankhya-Finance).

---

## Filtros disponíveis

Abra o painel de filtros pelo ícone no canto superior esquerdo. O indicador numérico ao lado do ícone mostra quantos filtros estão ativos. Todas as opções abaixo ficam reunidas no mesmo painel de filtro.

### Filtros principais

| **Filtro** | **O que faz** |
| --- | --- |
| **Período** | Intervalo de datas analisado |
| **Contas bancárias** | Restringe às contas selecionadas. Em branco, considera todas as contas ativas |
| **Empresa** | Restringe às empresas selecionadas |
| **Naturezas** | Restringe às naturezas selecionadas |
| **Centro de Resultado** | Restringe por centro de resultado |

### O que incluir

Defina quais tipos de lançamento entram nos gráficos e indicadores:

| **Opção** | **O que acrescenta** |
| --- | --- |
| **Recebidos** | Entradas já efetivadas |
| **Pagos** | Saídas já efetivadas |
| **A receber** | Entradas ainda não efetivadas |
| **A pagar** | Saídas ainda não efetivadas |
| **Previstos** | Lançamentos previstos, ainda não confirmados |
| **Saldo inicial** | Saldo das contas bancárias no início do período |

**⚠️ Atenção**

Ao menos uma dessas opções precisa estar marcada. Sem nenhuma, a tela não tem o que exibir.

### Opções de cálculo

Além de definir o que incluir, ajuste como os valores são calculados:

| **Opção** | **Efeito** |
| --- | --- |
| **Incluir contas inativas** | Considera também as contas bancárias desativadas |
| **Desconsiderar antecipação** | Exclui os títulos que participaram de antecipação bancária |
| **Considerar float** | Soma os dias de carência do tipo de título à data de vencimento |
| **Valores líquidos** | Usa o valor final do título, com acréscimos e deduções, em vez do valor bruto |

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Indicadores

Quatro cards no topo resumem o período filtrado.

![Indicadores · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541594005655)

| **Indicador** | **O que mostra** |
| --- | --- |
| Total Entradas | Soma dos valores efetivamente recebidos no período |
| Total Saídas | Soma dos valores efetivamente pagos no período |
| Resultado do período | Total Entradas menos Total Saídas |
| Saldo atual das contas | Saldo consolidado das contas bancárias consideradas |

**ℹ️ Nota**

Total Entradas e Total Saídas consideram apenas o que foi baixado, pelo valor da baixa. O Saldo atual das contas é a posição das contas no momento, e não depende do período filtrado.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Fluxo Projetado

Projeta o saldo dos próximos dias a partir dos títulos em aberto, para você antecipar se o caixa corre risco de ficar negativo.

![Fluxo Projetado · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541609273623)

A projeção parte do saldo atual e soma, dia a dia, os títulos em aberto conforme o vencimento. Título a receber aumenta o saldo; título a pagar reduz. A curva começa sempre na data atual.

**Controles**

- **Caixa** ou **Competência** — define o regime da projeção.
- **7**, **15**, **30** ou **90 dias** — define o horizonte projetado.

**Faixa de resultado** — acima do gráfico, uma faixa informa se o saldo se sustenta no horizonte escolhido. Quando a projeção indica saldo negativo, a faixa aponta a data prevista e alerta para o risco de ruptura de caixa.

**⚠️ Atenção**

O Fluxo Projetado considera apenas os filtros de **Contas bancárias** e **Empresa**. Os demais filtros da tela não o afetam. Isso está indicado no próprio painel.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Insights

Painel com leituras automáticas do recorte filtrado. A tela exibe até três insights por vez.

![Insights · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541609274263)

| **Insight** | **O que informa** |
| --- | --- |
| Títulos vencidos | Valor vencido e ainda não recebido, com sugestão de ação de cobrança |
| Comprometimento futuro | Quanto vence a pagar nos próximos 30 dias, contra quanto há a receber no mesmo prazo |
| Queima de caixa | Quantos meses seguidos o caixa consumiu mais do que gerou, e o acumulado do período |
| Saldo projetado negativo | Data em que o saldo projetado fica negativo e o valor previsto para essa data |

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Resultado mensal

Três gráficos mostram o resultado mensal sob ângulos diferentes: o saldo líquido de cada mês, a comparação lado a lado entre entradas e saídas, e a evolução do saldo real das contas bancárias.

### Valor Líquido por Mês

Mostra o resultado de cada mês — entradas menos saídas — em barras que sobem para o positivo e descem para o negativo. Barra para cima é mês com resultado positivo; barra para baixo é mês negativo. Use o gráfico para ver rapidamente em quais meses o caixa sobrou e em quais faltou. Clique em uma barra para abrir o detalhamento com os títulos do mês.
![Fluxo líquido mensal por natureza · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541609274519)

### Receitas × Despesas por Mês

Mostra as entradas e as saídas de cada mês lado a lado, em barras verdes (entradas) e vermelhas (saídas). A diferença visual entre elas mostra a folga ou o aperto do mês. Use o gráfico para comparar o ritmo de recebimentos e pagamentos ao longo do ano e antecipar meses em que as saídas superam as entradas. Clique em uma barra para abrir o detalhamento com os títulos do mês.

### Saldo Mensal

Mostra as entradas e as saídas de cada mês em barras, com uma linha de saldo real das contas bancárias sobreposta. A linha subindo indica caixa se recompondo; descendo, caixa se deteriorando. Use o gráfico para ter, num só lugar, a leitura do mês e a trajetória do saldo. Este gráfico não tem detalhamento ao clicar.

![Resultado mensal — Entradas vs Saídas · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541594008343)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Fluxo líquido mensal por natureza

Mostra a evolução mês a mês de cada natureza, em linhas.

![Fluxo líquido mensal por natureza · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541609274519)

Cada linha é uma natureza. Use o gráfico para acompanhar tendência por categoria e identificar a natureza responsável por um salto ou uma queda no mês.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Fluxo por natureza

Mostra o total movimentado por natureza no período, em barras horizontais, separando entradas de saídas pela cor.

![Fluxo por natureza · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541609278103)

Clique em uma barra para abrir o detalhamento com os títulos daquela natureza.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Análise de Aging — Recebimentos e Pagamentos

Mostra quanto há a receber e a pagar por faixa de prazo em relação à data atual.

![Análise de Aging · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43541594009495)

| **Faixa** | **O que representa** |
| --- | --- |
| A vencer (hoje) | Vencimento ainda não chegou |
| 1 a 30 dias | Vencido há até 30 dias — atraso recente |
| 31 a 60 dias | Vencido entre 31 e 60 dias — merece atenção |
| 61 a 90 dias | Vencido entre 61 e 90 dias — atraso relevante |
| 90+ dias | Vencido há mais de 90 dias — maior risco de inadimplência |

**ℹ️ Nota**

As cinco faixas são sempre exibidas, mesmo quando vazias, para facilitar a comparação visual.

Clique em uma barra para abrir o detalhamento com os títulos da faixa.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Distribuição por banco

Gráfico de rosca com a participação de cada banco no saldo total, acompanhado da tabela detalhada.

Use o painel para apoiar decisões de transferência entre contas e identificar concentração em um único banco.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Detalhamento ao clicar nos gráficos

Os gráficos com detalhamento abrem uma janela com o recorte clicado. A janela apresenta três cards de resumo — tipo, total de títulos e valor total — seguidos da lista paginada, com as colunas título, parceiro, natureza, data de negociação, vencimento, valor líquido e situação.

**ℹ️ Nota**

A Distribuição por banco é a única que exibe entradas e saídas juntas na mesma lista.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41307193691927-Tela-Fluxo-de-caixa#sumario)

---

## Pontos de atenção

- O Fluxo Projetado tem filtros próprios: ele responde apenas a Contas bancárias e Empresa. Se você filtrar por natureza ou centro de resultado e o gráfico não mudar, é esse o motivo.
- Os indicadores de topo são realizados: Total Entradas e Total Saídas somam apenas o que foi baixado. O que está a vencer aparece na projeção e no aging, não nesses cards.
- Saldo atual das contas não segue o período: ele é a posição do momento.
- Ao menos uma opção de inclusão precisa estar marcada. Com todas desmarcadas, a tela fica sem dados.
