---
id: "42427395850775"
titulo: "Relatório: visualizando tarefas atrasadas por usuários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427395850775-Relat%C3%B3rio-visualizando-tarefas-atrasadas-por-usu%C3%A1rios"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:33Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452198", "sync_hash_b9f231425cf1"]
---

# Relatório: visualizando tarefas atrasadas por usuários

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- Selecione o tipo de Widget de sua preferência (recomenda-se **Gráfico de Barras** ou **Tabela**).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Tarefa**.
- Em **Selecione um operador**, escolha a opção **Contagem**.
- O campo **Campo** pode ser deixado em branco, pois o sistema calculará o volume total de registros encontrados.

## 3. Aplicação do Filtro

Vá até a seção de **Filtros** para garantir que apenas as tarefas em aberto sejam contabilizadas:

- **Campo:** Finalizada (Tarefa)
- **Condição:** Igual a
- **Valor:** Não

## 4. Agrupamento dos Dados

- Localize a opção **Escolha como agrupar os dados**.
- Defina o critério de agrupamento como: **Usuário (Tarefa)**.
- O campo **Intervalo da data** pode ser deixado em branco, visto que o foco do relatório é o volume acumulado atual por pessoa, independentemente do período de criação.

## Segue abaixo uma imagem com a configuração pronta

![Imagem 1: Segue abaixo uma imagem com a configuração pronta](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2496042318/7b130825c93357dfdd31de5ac065/image.png?expires=1786536000&signature=f62faf073c74851f108513a92b937ff15a5f3f3286319cc04a2ca3e6691be340&req=diQuEMl6n4JeUfMW3nq%2BgXWT74WEl5Yp44T5tDqZyOJ5waqhguYVJehi%2B4Cj%0ALhrCoTOyyN58uj%2BUhtuc3DpAJUk%3D%0A)

Pronto! Salve as alterações para gerar o relatório. Agora você terá uma visão clara de quantas tarefas cada usuário possui pendentes para execução.
