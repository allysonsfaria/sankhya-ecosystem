---
id: "42427379255063"
titulo: "Relatório: valor das vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427379255063-Relat%C3%B3rio-valor-das-vendas"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:26Z"
rotulos: ["sync_hc", "ploomes_5452193", "ploomes", "sync_hash_9713d71ce831"]
---

# Relatório: valor das vendas

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- No campo **Tipo de Widget** (ou Tipo de Gráfico), selecione a opção **Indicador** (também conhecido em alguns sistemas como Cartão ou Número Geral).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Vendas**.
- Em **Selecione um operador**, escolha a opção **Soma**.
- No campo **Campo**, defina como **Valor (Venda)**.

## 3. Aplicação do Filtro

Vá até a seção de **Filtros** para isolar apenas o faturamento obtido dentro do período vigente:

- **Campo:** Data (venda)
- **Condição:** Igual a
- **Tipo:** Data Relativa
- **Período:** Este ano

## 4. Agrupamento e Intervalo dos Dados

- Os campos **Escolha como agrupar os dados** e **Intervalo da data** devem ser deixados **em branco / desmarcados**.

Nota: Como o formato selecionado é um "Indicador", o sistema não precisa desmembrar os dados em linhas ou colunas. Ele irá apenas somar tudo e exibir um único grande número consolidado na sua tela.

## Segue abaixo uma imagem da configuração pronta

![Imagem 1: Segue abaixo uma imagem da configuração pronta](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2501576425/3210ac7238f13cdeece4b143bcc0/image.png?expires=1786536000&signature=7873cab9d7e98d801681d31a7f20d2736593c6b597936cfeb3baa7a5bf20f3dc&req=diUnF8x5m4VdXPMW3nq%2BgZcTLd6Wq8eWvBnTU3%2BkjbOVGAcAMYZRDD2ukdHX%0Ac%2FLzV%2B491Xk66R7%2FiYO4bQ8dioA%3D%0A)

Pronto! Salve as alterações. O widget agora exibirá em destaque no seu dashboard o valor total faturado pela sua empresa desde o dia 1º de janeiro até o momento.
