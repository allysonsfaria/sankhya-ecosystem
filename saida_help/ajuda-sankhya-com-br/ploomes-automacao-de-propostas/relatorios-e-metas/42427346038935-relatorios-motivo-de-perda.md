---
id: "42427346038935"
titulo: "Relatórios: Motivo de perda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427346038935-Relat%C3%B3rios-Motivo-de-perda"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:14Z"
rotulos: ["sync_hc", "ploomes_5452187", "ploomes", "sync_hash_d001c6888f61"]
---

# Relatórios: Motivo de perda

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- No campo **Tipo de Widget**, selecione a opção **Tabela** (excelente para listar e ordenar os motivos com clareza).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Negócio**.
- Em **Selecione um operador**, escolha a opção **Contagem**.
- O campo **Campo** pode ser deixado em branco, pois o sistema calculará o volume absoluto de registros encontrados.

## 3. Aplicação dos Filtros

Vá até a seção de **Filtros** e adicione os seguintes critérios para isolar as perdas recentes:

- **Filtro 1 (Período):**

  - **Campo:** Data de criação
  - **Condição:** Igual a
  - **Tipo:** Data Relativa
  - **Período:** Últimos 30 dias
- **Filtro 2 (Status do Negócio):**

  - **Campo:** Situação
  - **Condição:** Igual a
  - **Valor:** Perdida

## 4. Agrupamento dos Dados

- Localize a opção **Escolha como agrupar os dados**.
- Defina o critério de agrupamento como: **Motivo de perda**.
- O campo **Intervalo da data** deve ser deixado em branco, uma vez que a tabela consolidará as quantidades diretamente por motivo dentro do intervalo de 30 dias.

  Segue abaixo uma imagem da configuração pronta:

  ![Imagem 1: O campo Intervalo da data deve ser deixado em branco, uma vez que a tabela consolidará as quantidades diretamente por…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2511881528/b8226a3e64776320d228cbcf640a/Captura+de+tela+2026-06-30+114215.png?expires=1786536000&signature=2219d550eb8f6ebfb3d93fdb753801e09433a82b15d5936662b6245e87a06c2c&req=diUmF8F2nIRdUfMW3nq%2BgbPw8iiENbwtUVAp0tqQBbEJXZItOztVK1RcmCJP%0AdCLKWfG0BENY6Bwo1pCxw0X2uZY%3D%0A)

Pronto! Salve as alterações para gerar o relatório. O resultado será uma lista com os motivos de perda ordenados por volume, ajudando a entender o porquê de os clientes não estarem fechando com a sua empresa.
