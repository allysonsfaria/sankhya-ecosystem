---
id: "42427345932183"
titulo: "Relatórios de mapa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427345932183-Relat%C3%B3rios-de-mapa"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:13Z"
rotulos: ["sync_hc", "ploomes_5452181", "ploomes", "sync_hash_c9ffb7102103"]
---

# Relatórios de mapa

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** (ou Novo Widget) na sua tela de dashboards ou relatórios.
- No campo **Tipo de Widget**, selecione a opção **Mapa**.
- Defina as configurações de escala desejadas (ex: escolha a escala por **Estados** para visualizar o mapa do Brasil).

## 2. Configuração dos Dados e Métrica

- Clique em **Adicionar** para configurar a métrica de leitura:

  - **Módulo do sistema:** Clientes
  - **Selecione um operador:** Contagem
  - **Campo:** Pode ser deixado em branco ou definido como ID do Cliente (para garantir uma contagem única de cada cadastro).

## 3. Aplicação do Filtro

- Vá até a seção de **Filtros**.
- Para este exemplo, **deixe a seção de filtros vazia**, permitindo que o sistema puxe e contabilize toda a base de clientes ativa na sua conta.

## 4. Dimensão e Agrupamento dos Dados

- Localize a opção **Escolha como agrupar os dados** (ou campo de Dimensão do mapa).
- Defina o critério de agrupamento como: **Estado** (ou Estado do cliente).
- O campo **Intervalo da data** deve ser deixado em branco, pois a divisão será estritamente territorial.

## Segue abaixo uma imagem da configuração pronta:

![Imagem 1: Segue abaixo uma imagem da configuração pronta:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2511925159/d26c2ddca1b5fa06941a1a8a2366/image.png?expires=1786536000&signature=54d8e2a2ced183d17d34806a4299d0bf41820e5d678a35e95615c871b79b4dc5&req=diUmF8B8mIBaUPMW3nq%2BgRCPEfl5ETTazf5L6tegP5tZA9cYqvOqybPzXXqj%0AY2IHOk%2BErsmim8Isbv%2Bu4AqeeCg%3D%0A)

📌 **Dica de Suporte:** Se algum cliente não for contabilizado no mapa, verifique se o endereço dele está vinculado ao Google Maps no cadastro, garantindo que os campos de Latitude e Longitude estejam preenchidos automaticamente.

Pronto! Salve as alterações. O mapa será gerado colorindo ou inserindo marcadores nos estados de acordo com o volume de clientes que você possui em cada região do país.
