---
id: "42427411453335"
titulo: "Relatórios: Tarefas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427411453335-Relat%C3%B3rios-Tarefas"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:23Z"
rotulos: ["sync_hc", "ploomes_5452188", "ploomes", "sync_hash_be47a0bdacc2"]
---

# Relatórios: Tarefas

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- No campo **Tipo de Widget**, selecione a opção **Barra** (recomenda-se barras verticais ou agrupadas).

## Configuração da Métrica 1: Visitas Pendentes

## 2. Dados e Filtros (Visitas)

- Na primeira métrica do widget, configure os seguintes campos:

  - **Módulo do sistema:** Tarefas
  - **Selecione um operador:** Contagem
  - **Campo:** Deixe em branco.
- Vá até a seção de **Filtros** desta primeira métrica e adicione as duas regras abaixo:

  - **Filtro 1:** Tipo (Tarefas) **>** igual a **>** Visitas
  - **Filtro 2:** Finalizadas? **>** igual a **>** Não

    ![Imagem 1: Filtro 2: Finalizadas? > igual a > Não](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2504449571/68094aedfdfc40146f04174f280a/image.png?expires=1786536000&signature=6e68d339c4b6f5d95cfca0cdfe0ec33ed887949e34d4aef2a691b08eda0aab89&req=diUnEs16lIRYWPMW3nq%2BgdNw1mLva9Xu3kOZ80Kf24lxFA7IEkUtOtIN5oqx%0AVEDQQDFerT%2BBHB79RquAc%2F0X5nw%3D%0A)

## Configuração da Métrica 2: Reuniões Pendentes

## 3. Adicionar Segunda Métrica

- Dentro do mesmo widget, clique no botão para **Adicionar Nova Métrica**.
- Configure os seguintes campos:

  - **Módulo do sistema:** Tarefas
  - **Selecione um operador:** Contagem
  - **Campo:** Deixe em branco.
- Vá até a seção de **Filtros** desta segunda métrica e configure para identificar as reuniões em aberto:

  - **Filtro 1:** Tipo (Tarefas) **>** igual a **>** Reuniões
  - **Filtro 2:** Finalizadas? **>** igual a **>** Não

![Imagem 2: Filtro 2: Finalizadas? > igual a > Não](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2504450804/d1ba7ca0feafab75c360e49a00d2/image.png?expires=1786536000&signature=b62f6b00bd4ceb2c5b9533d6a6b04df69df51a7d4e9918535d1fa9a54ce77f62&req=diUnEs17nYlfXfMW3nq%2Bgfai7Aq47nDn7R4GJlfXpPBSdoyI95%2B%2Fd4SABT9S%0AiMQOl7L9xchQQZ4lMLN5MjkDjZQ%3D%0A)

## Configuração da Métrica 3: WhatsApp Pendente

## 4. Adicionar Terceira Métrica

- Clique mais uma vez no botão para **Adicionar Nova Métrica**.
- Configure os seguintes campos:

  - **Módulo do sistema:** Tarefas
  - **Selecione um operador:** Contagem
  - **Campo:** Deixe em branco.
- Vá até a seção de **Filtros** desta terceira métrica para isolar os contatos de WhatsApp em aberto:

  - **Filtro 1:** Tipo (Tarefas) **>** igual a **>** Whatsapp
  - **Filtro 2:** Finalizadas? **>** igual a **>** Não

![Imagem 3: Filtro 2: Finalizadas? > igual a > Não](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2504451546/747f85801cf6fff2be5a1bcb475f/image.png?expires=1786536000&signature=b13f952c29796f457d6943b4107b83a9723b9af0578a204f085df9af370445df&req=diUnEs17nIRbX%2FMW3nq%2BgSC6EoPSl9urQSABgcaUwT7JBZvd93otApCnchOh%0AO0%2Ff5BFTET0oUbNqOsdVc0Cu5%2Fk%3D%0A)

## 5. Agrupamento Final do Gráfico

- Após configurar as três métricas, vá até a seção principal de agrupamento do widget:
- No campo **Escolha como agrupar os dados**, defina como: **Tarefas** (ou o critério geral do widget para exibir as barras lado a lado).
- O campo **Intervalo da data** deve ser deixado em branco, pois o foco é o volume acumulado de pendências atuais.

![Imagem 4: O campo Intervalo da data deve ser deixado em branco, pois o foco é o volume acumulado de pendências atuais.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2504451834/25f21f9e8d35458b78c78d42e8a4/image.png?expires=1786536000&signature=9cff61c5f8f707c90d91a1c1e4fb70753519c29931a3e2f33fab78fb27bc24a6&req=diUnEs17nIlcXfMW3nq%2BgafFFgFBzXQLDG%2BarEOQViIXmTSSD%2BgRxJCBwY6E%0A2YE8Ek6OEth65e7gtmsaWVebazo%3D%0A)

Pronto! Salve as alterações. O seu gráfico de barras agora mostrará três colunas distintas (uma para cada tipo de atividade), facilitando o controle sobre a agenda e os compromissos pendentes da empresa.
