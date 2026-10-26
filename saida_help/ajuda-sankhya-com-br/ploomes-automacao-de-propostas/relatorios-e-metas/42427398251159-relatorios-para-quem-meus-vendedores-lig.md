---
id: "42427398251159"
titulo: "Relatórios: Para quem meus vendedores ligam?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427398251159-Relat%C3%B3rios-Para-quem-meus-vendedores-ligam"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:37Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452202", "sync_hash_9c5d079335cb"]
---

# Relatórios: Para quem meus vendedores ligam?

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- Selecione o tipo de Widget como **Tabela** (ideal para listar os nomes dos clientes).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Registro de interações**.
- Em **Selecione um operador**, escolha a opção **Contagem**.

## 3. Aplicação dos Filtros

Para isolar apenas as ligações feitas na última semana, vá até a seção de **Filtros** e adicione as duas regras abaixo:

- **Filtro 1 (Período):**

  - **Campo:** Data da criação (Registro de interação)
  - **Condição:** Igual a
  - **Tipo:** Data Relativa
  - **Período:** Últimos 7 dias
- **Filtro 2 (Tipo de Interação):**

  - **Campo:** Tipo (Registro de interação)
  - **Condição:** Igual a
  - **Valor:** Telefone

## 4. Agrupamento das Informações

- Localize a opção **Escolha como agrupar os dados**.
- Defina o critério de agrupamento como: **Cliente (Registro de interação)**.

![Imagem 1: Defina o critério de agrupamento como: Cliente (Registro de interação) .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2493507514/2df3e4ff09bbd3418723c40baee4/Screenshot+2026-06-22+144234.png?expires=1786536000&signature=20eb5c85d3a6f6aa4f4d30dfd8cd711a66cb82526f7ef8040c77d14cd13f96e0&req=diQuFcx%2BmoReXfMW3nq%2BgWcaViJRNWALEz1R3%2BnW6dP1TpttJqAjvGSOSpb9%0AOO20IV1nfqC6%2F4lQ%2B%2FaCRi%2BVLjc%3D%0A)

Pronto! Salve as alterações para gerar o relatório. Ele exibirá uma lista com os clientes que mais receberam ligações da sua equipe comercial nos últimos 7 dias, acompanhada da quantidade exata de contatos feitos para cada um.
