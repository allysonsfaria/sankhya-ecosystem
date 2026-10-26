---
id: "42427412010135"
titulo: "Como Gerar um Relatório para Contar um Campo de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427412010135-Como-Gerar-um-Relat%C3%B3rio-para-Contar-um-Campo-de-Vendas"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:34Z"
rotulos: ["sync_hc", "ploomes_5452200", "ploomes", "sync_hash_9d1fa4a5c111"]
---

# Como Gerar um Relatório para Contar um Campo de Vendas

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- Selecione o tipo de Widget de sua preferência (recomenda-se **Tabela** ou **Gráfico de Barras** para facilitar a comparação entre os vendedores).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Venda**.
- Em **Selecione um operador**, escolha a opção **Soma**.
- No campo **Campo**, defina como **Comissão**.

## 3. Aplicação do Filtro

Vá até a seção de **Filtros** para restringir o relatório apenas ao período atual:

- **Campo:** Data (Venda)
- **Condição:** Igual a
- **Tipo:** Data Relativa
- **Período:** Este mês

## 4. Agrupamento dos Dados

- Localize a opção **Escolha como agrupar os dados**.
- Defina o critério de agrupamento como: **Responsável (Venda)**.
- O campo **Intervalo da data** pode ser deixado em branco ou desmarcado, já que o agrupamento principal será feito diretamente pelo nome do vendedor (Responsável) e o filtro já limita o período ao mês vigente.

## Segue abaixo uma imagem da configuração pronta

![Imagem 1: Segue abaixo uma imagem da configuração pronta](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2495905972/e1c86514d27e720dfa1b2b1dde1a/image.png?expires=1786536000&signature=9fd164e849334f0746d40de16c2646149419666f1f05b1641cbf11ca7fe9cbb4&req=diQuE8B%2BmIhYW%2FMW3nq%2Bga1BohaR0mUAHeafJePPvNDbdhitpVey7Nm9faTY%0AoTE4ET53BdCGTuMW6S8Xw4NkMrU%3D%0A)

Pronto! Salve as alterações para gerar o relatório. O gráfico ou tabela mostrará exatamente quanto cada vendedor acumulou em comissões dentro do mês corrente.
