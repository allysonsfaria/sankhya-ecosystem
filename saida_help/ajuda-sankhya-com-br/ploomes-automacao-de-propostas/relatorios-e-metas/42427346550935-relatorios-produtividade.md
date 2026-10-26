---
id: "42427346550935"
titulo: "Relatórios: Produtividade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427346550935-Relat%C3%B3rios-Produtividade"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:00:25Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452191", "sync_hash_4afbd1861d7c"]
---

# Relatórios: Produtividade

## 1. Inicialização do Widget

- Clique em **Novo Gráfico** na sua tela de dashboards ou relatórios.
- No campo **Tipo de Widget**, selecione a opção **Tabela**.

## 2. Configuração dos Dados e Métrica

- No campo **Módulo do sistema**, selecione **Registro de interação**.
- Em **Selecione um operador**, escolha a opção **Contagem**.
- O campo **Campo** pode ser deixado em branco, pois o sistema calculará o volume absoluto de interações criadas.

## 3. Aplicação do Filtro de Período

Vá até a seção de **Filtros** para analisar o histórico recente da operação:

- **Campo:** Data da criação
- **Condição:** Igual a
- **Tipo:** Data Relativa
- **Período:** Últimos N meses
- **Valor:** 6

## 4. Agrupamento das Informações

- Localize a opção **Escolha como agrupar os dados** e adicione os dois níveis de quebra abaixo:

  1. **Criador** (para identificar o usuário que realizou a atividade)
  2. **Tipo** (para separar se foi telefone, e-mail, reunião, etc.)
- O campo **Intervalo da data** deve ser deixado em branco, uma vez que a tabela organizará os volumes de forma consolidada por pessoa e por canal dentro do semestre avaliado.

## Segue abaixo uma imagem da configuração pronta

![Imagem 1: Segue abaixo uma imagem da configuração pronta](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2501582253/d3327ecdcc878eb76ab0c2eadd82/Screenshot+2026-06-25+232115.png?expires=1786536000&signature=03adbe985afb0db5756ef19cb64ac38003e9f69ae292afe4b6f8b257447c09e9&req=diUnF8x2n4NaWvMW3nq%2BgWcCYrMf3lR18HS%2FWq52vqdFXdJGIif1Pv73VbW9%0AYvUcP7Vokz%2F2rGuyvB0WZompOy8%3D%0A)

Pronto! Salve as alterações para gerar o relatório. O resultado será uma tabela detalhada que mostra o volume total de cada tipo de interação realizada individualmente pelos membros da sua equipe nos últimos 6 meses.
