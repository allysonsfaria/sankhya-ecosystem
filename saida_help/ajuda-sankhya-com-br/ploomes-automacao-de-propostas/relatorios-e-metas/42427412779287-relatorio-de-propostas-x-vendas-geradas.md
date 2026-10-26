---
id: "42427412779287"
titulo: "Relatório de propostas x vendas geradas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427412779287-Relat%C3%B3rio-de-propostas-x-vendas-geradas"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:39Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452203", "sync_hash_c40de12d5a7f"]
---

# Relatório de propostas x vendas geradas

## Configuração da 1ª Métrica (Propostas)

## 1. Inicialização e Tipo de Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- Selecione o tipo de Widget desejado (ex: Gráfico de Linhas, Barras ou Tabela Comparativa).

## 2. Configuração dos Dados (Propostas)

- No campo **Módulo do sistema**, selecione **Proposta**.
- Em **Selecione um operador**, escolha a opção **Contagem**.

## 3. Filtro e Agrupamento (Propostas)

- Na seção de **Filtros**, configure o período:

  - **Campo:** Data de criação (Proposta)
  - **Condição:** Igual a
  - **Tipo:** Data Relativa
  - **Período:** Últimos N meses
  - **Valor:** 6
- Em **Escolha como agrupar os dados**, defina como: **Data de criação (Proposta)**.
- No campo **Intervalo da data**, selecione **Mês**.

## Abaixo uma imagem da configuração pronta:

![Imagem 1: Abaixo uma imagem da configuração pronta:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2493406371/dcdee54c9811c902355373f8df19/Screenshot+2026-06-22+135143.png?expires=1786536000&signature=1c1b57ca359f039161fec89bf22ae547954c13783c3245599ffa217fdc818175&req=diQuFc1%2Bm4JYWPMW3nq%2BgQEYx%2BUfzrgcqv4CiR5b1jxmHaQeUCUVk%2BR%2FytxL%0AdIT5POJVTMmCtAknk3TMD%2F7sQno%3D%0A)

## Configuração da 2ª Métrica (Vendas)

## 4. Adicionar Nova Métrica

- Dentro do mesmo widget, clique no botão para **Adicionar Nova Métrica** (ou adicionar nova série de dados).

## 5. Configuração dos Dados (Vendas)

- No campo **Módulo do sistema** desta nova métrica, mude para **Venda**.
- Em **Selecione um operador**, escolha a opção **Contagem**.

## 6. Filtro e Agrupamento (Vendas)

- Na seção de **Filtros** da segunda métrica, configure:

  - **Campo:** Data de criação (Venda)
  - **Condição:** Igual a
  - **Tipo:** Data Relativa
  - **Período:** Últimos N meses
  - **Valor:** 6
- Em **Escolha como agrupar os dados**, defina como: **Data de criação (Venda)**.
- No campo **Intervalo da data**, selecione **Mês**.

Pronto! Salve as alterações para gerar o gráfico comparativo, que mostrará lado a lado o volume de propostas criadas e de vendas geradas nos últimos 6 meses.

## Abaixo uma imagem da configuração pronta:

![Imagem 2: Abaixo uma imagem da configuração pronta:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2493407879/13f23a68317ba7320d41c2884ae0/image.png?expires=1786536000&signature=9c50af36bcc77e500be1612571597541d82a8a152c39976610ec1ef0dfa0fffa&req=diQuFc1%2BmolYUPMW3nq%2BgenZjt8D00JfZ7Ou3pyfk%2FEEnSK3yx%2BvWJwvJN81%0AZCNxUEPvG0wxG6vnSltbloAGZmg%3D%0A)
