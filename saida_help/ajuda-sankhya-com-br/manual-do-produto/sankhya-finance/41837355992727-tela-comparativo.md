---
id: "41837355992727"
titulo: "Tela Comparativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro > Sankhya Finance"
atualizado_em: "2026-09-25T20:02:52Z"
rotulos: ["Relatórios", "Análise Financeira", "Financeiro", "Sankhya Cloud", "Comparativo"]
---

# Tela Comparativo

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo#o-que-e-e-para-que-serve)
- [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo#filtros)
- [Indicadores (KPIs)](https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo#indicadores-kpis)
- [Maiores Diferenças](https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo#maiores-diferencas)
- [Análise Detalhada por Categoria](https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo#analise-detalhada-por-categoria)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41837355992727-Tela-Comparativo#pontos-de-atencao)

**Módulo:** Sankhya Finance

**Caminho de acesso:** Menu Principal › Sankhya Finance › Comparativo

Esta tela está disponível exclusivamente para clientes Sankhya Cloud.

A tela Comparativo confronta dois períodos e mostra a variação de receitas e despesas por natureza, com diferença absoluta (em R$) e percentual. Ela responde "o que mudou de um intervalo para o outro e onde" — mês atual contra o anterior, um ano contra outro, ou duas janelas quaisquer, sempre lado a lado.

Não é o lugar para detalhar título a título — isso fica com a Gestão financeira — nem para projetar o futuro: o foco é o realizado de dois recortes já definidos, com dados lidos direto do Sankhya Om.

Ela faz parte do conjunto de telas do Sankhya Finance; para entender como se encaixa na solução completa, consulte o [Guia Sankhya Finance](https://ajuda.sankhya.com.br/hc/pt-br/articles/41301087909655-Guia-Sankhya-Finance).

![Imagem 1: Ela faz parte do conjunto de telas do Sankhya Finance; para entender como se encaixa na solução completa, consulte o…](https://ajuda.sankhya.com.br/hc/article_attachments/41839581417495)

Tela Comparativo de Períodos · 07/2026

**ℹ️ Nota**

A tela é atualizada automaticamente. O topo direito mostra a data e a hora da última atualização e o botão **Recarregar página**.

## Filtros

### Granularidade

Acima dos filtros de período, o seletor **Dia** · **Semana** · **Mês** · **Ano** define a unidade de comparação entre os dois períodos.

### Períodos e demais filtros

- **Período A** — intervalo de datas do primeiro período. É a base do cálculo de variação percentual.
- **Período B** — intervalo de datas do segundo período, comparado contra o Período A.
- **Naturezas** — seleção das naturezas (categorias) consideradas na comparação.
- **Tipo de Data** — base de data usada para enquadrar os títulos em cada período. No print, está em **Caixa**.
- **Empresa** — seleção de empresas; consolida os valores das empresas escolhidas.

## Indicadores (KPIs)

Três cards resumem a variação entre os dois períodos. Cada card traz o valor da diferença e um selo com a variação percentual.

### Diferença Receita

Variação da receita total entre o Período A e o Período B, em R$, com o percentual no selo.

### Diferença Despesa

Variação da despesa total entre os dois períodos, em R$, com o percentual no selo.

### Diferença Líquida

Variação do resultado (receita menos despesa) entre os dois períodos, em R$, com o percentual no selo.

![Indicadores · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43561272932887)

##

## Maiores diferenças

Dois gráficos de barras horizontais mostram as 10 maiores diferenças por natureza, separadas em Receita e Despesa. Cada barra é a variação daquela natureza entre o Período A e o Período B; a cor indica o sentido da variação. É a leitura rápida de onde a mudança se concentrou.

![Maiores Diferenças · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43561286866071)

## Análise detalhada por categoria

Tabela com a comparação completa, natureza por natureza. Os valores são em R$ e a variação percentual é calculada com o Período A como base. As linhas são agrupadas em Receita, Despesa e Resultado líquido, com os totais de cada grupo em destaque.

### Colunas

| Coluna | O que mostra |
| --- | --- |
| Receita/Despesa | Natureza (categoria) da linha, dentro do grupo Receita ou Despesa |
| Período A | Valor da natureza no Período A |
| Período B | Valor da natureza no Período B |
| Diferença | Período B menos Período A, em R$ (positivo em verde, negativo em vermelho) |
| Variação % | Variação percentual em relação ao Período A, com selo colorido |

As linhas de grupo (Receita e Despesa) trazem o total do grupo em cada período e a diferença correspondente. A linha **Resultado líquido**, no rodapé da tabela, consolida receita menos despesa por período e a diferença entre eles.

![Análise Detalhada por Categoria · 09/2026](https://ajuda.sankhya.com.br/hc/article_attachments/43561272937623)

## Pontos de atenção

### Período A é a base da variação percentual

A variação percentual — nos cards, nos gráficos e na tabela — é sempre calculada tomando o **Período A** como base. Ao inverter os períodos, os percentuais mudam.

### Comparação por natureza

Toda a tela quebra os valores por natureza (categoria). A escolha no filtro **Naturezas** define quais categorias entram na comparação.

### Variação de 0%

Quando o Período A é zero, não há base para calcular a variação percentual, e a tela exibe 0%. A diferença em reais continua correta — leia a coluna **Diferença** nesses casos.
