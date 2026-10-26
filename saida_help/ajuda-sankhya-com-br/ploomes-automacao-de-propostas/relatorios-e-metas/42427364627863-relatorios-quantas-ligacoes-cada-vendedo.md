---
id: "42427364627863"
titulo: "Relatórios: quantas ligações cada vendedor faz por dia?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427364627863-Relat%C3%B3rios-quantas-liga%C3%A7%C3%B5es-cada-vendedor-faz-por-dia"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:36Z"
rotulos: ["sync_hc", "ploomes_5452201", "ploomes", "sync_hash_0a78375daa31"]
---

# Relatórios: quantas ligações cada vendedor faz por dia?

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- Selecione o tipo de Widget de sua preferência (recomenda-se **Tabela** ou **Gráfico de Barras Empilhadas**).

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Registro de interação**.
- Em **Selecione um operador**, escolha a opção **Contagem**.
- O campo **Campo** pode ser deixado em branco ou preenchido automaticamente pelo sistema, já que o operador de contagem calculará o volume total de registros.

## 3. Aplicação dos Filtros

Vá até a seção de **Filtros** e adicione os seguintes critérios para isolar apenas as ligações telefônicas da última semana:

- **Filtro 1 (Período):**

  - **Campo:** Data da criação (registro de interação)
  - **Condição:** Igual a
  - **Tipo:** Data Relativa
  - **Período:** Últimos 7 dias
- **Filtro 2 (Meio de Contato):**

  - **Campo:** Tipo (Registro de interação)
  - **Condição:** Igual a
  - **Valor:** Telefone

## 4. Agrupamento e Intervalo dos Dados

- Localize a opção **Escolha como agrupar os dados** e adicione os dois níveis de quebra abaixo:

  1. **Criador (registro de interação)** (indica o vendedor que fez a ligação)
  2. **Data da criação (registro de interação)**
- No campo **Intervalo da data**, mude a definição para **Dia**.

## Abaixo uma imagem da configuração pronta

![Imagem 1: Abaixo uma imagem da configuração pronta](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2495502898/3b613cc3f11d53935ae36e79253a/Captura+de+tela+2026-06-23+111510.png?expires=1786536000&signature=a6a47f760cbca75208dd668c6d14121f401826f6fd8dd8bbb57492151b0101d8&req=diQuE8x%2Bn4lWUfMW3nq%2BgdGYAjwvleqy9dCVqd1ThboxsZHqwsr3eRFwA6YI%0Avy6aW1hgxcENqVntj8Xbs1zujSc%3D%0A)

Pronto! Salve as alterações para gerar o relatório. O resultado será uma visão detalhada que mostra o volume diário de ligações de cada vendedor ao longo dos últimos 7 dias.
