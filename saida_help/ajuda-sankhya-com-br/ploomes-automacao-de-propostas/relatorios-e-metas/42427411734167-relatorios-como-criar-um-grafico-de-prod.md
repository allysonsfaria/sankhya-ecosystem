---
id: "42427411734167"
titulo: "Relatórios: como criar um gráfico de produto por venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427411734167-Relat%C3%B3rios-como-criar-um-gr%C3%A1fico-de-produto-por-venda"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:28Z"
rotulos: ["sync_hc", "ploomes_5452196", "ploomes", "sync_hash_110db100ecea"]
---

# Relatórios: como criar um gráfico de produto por venda

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- Selecione o tipo de Widget de sua preferência (recomenda-se **Gráfico de Barras** para comparar o faturamento entre os produtos ou **Tabela**).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Produto da venda**.
- Em **Selecione um operador**, escolha a opção **Soma**.
- No campo **Campo**, defina como **Total (Produto da venda)**.

## 3. Aplicação do Filtro

Vá até a seção de **Filtros** para restringir os dados apenas às movimentações do período vigente:

- **Campo:** Data da venda
- **Condição:** Igual a
- **Tipo:** Data Relativa
- **Período:** Este mês

## 4. Agrupamento dos Dados

- Localize a opção **Escolha como agrupar os dados**.
- Defina o critério de agrupamento como: **Produto (Produto da venda)**.
- O campo **Intervalo da data** deve ser deixado em branco, já que as informações serão agrupadas diretamente pelo nome de cada produto e o filtro de período já delimita o mês atual.

## Segue abaixo uma imagem da configuração pronta

![Imagem 1: Segue abaixo uma imagem da configuração pronta](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2501566230/7152c188ce45d196d540b8f0a403/image.png?expires=1786536000&signature=946f7d323f2051a40d20c56342f41fb2a95f5b0aac1670007c94714054c628e4&req=diUnF8x4m4NcWfMW3nq%2BgRECQtZAJQKWU10KANK%2Fuoyl%2FJAAn9A8zCs3nQs9%0AUY1QY3XhyJxupIjfTBb%2FydJUnII%3D%0A)

Pronto! Salve as alterações para gerar o relatório. O widget mostrará em tempo real o valor total arrecadado com a venda de cada um dos seus produtos ao longo do mês.
