---
id: "42427406136983"
titulo: "Relatórios: Produtos mais vendidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427406136983-Relat%C3%B3rios-Produtos-mais-vendidos"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-10T18:02:38Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452213", "sync_hash_37541a332fb5"]
---

# Relatórios: Produtos mais vendidos

## 1. Definição da Métrica Principal

Nesta etapa, estamos estabelecendo o "o quê" será calculado.

- **Título da Métrica:** Selecione **Produtos da Proposta**.
- **Operador:** Escolha **Soma** (isso garantirá o acúmulo dos valores em vez de apenas contar as linhas).
- **Campo de Produto da Proposta:** Selecione **Quantidade**.

  ![Imagem 1: Campo de Produto da Proposta: Selecione Quantidade .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220004164/38013aa2cc7fb2634c645faf1ae4/Screenshot+2026-03-30+145547.png?expires=1786536000&signature=e7651cfdeaba3640e506e50cd834992560af8d25b6f6e426b06e6496cb546fd2&req=diIlFsl%2BmYBZXfMW3nq%2BgapvDv40N9Iwlg1FUgBBqf3BJ7phQ8vZdxdAytv8%0AQ82DJkdolqlksygovLfgj5DhWt0%3D%0A)

## 2. Refinamento com Filtros (Segmentação)

Para evitar que dados irrelevantes poluam sua análise, aplicamos uma regra de corte:

- Adicionei um filtro onde o campo **Valor do Produto** (ou Preço Unitário) seja **Superior a 100**.

  **Dica:** Isso é útil para focar em produtos de maior ticket médio e desconsiderar itens de baixo valor ou acessórios.

  ![Imagem 2: Dica: Isso é útil para focar em produtos de maior ticket médio e desconsiderar itens de baixo valor ou acessórios.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220007147/70b3bf1f4c99bc57eeed84ff584f/Screenshot+2026-03-30+14473012.png?expires=1786536000&signature=3fe4ff6091b08ccb4190e8c761ef56a0dc57809f342923c645c73248aed2edc0&req=diIlFsl%2BmoBbXvMW3nq%2Bgae2AUbHaHC8bjWyRlkWCdTFsIACtmrVbuxlOHBd%0A4EtvlKFY7id4hg%2BQ9hYn7cCgSig%3D%0A)

## 3. Agrupamento e Visualização

Agora, definimos como esses dados serão organizados visualmente:

- Em **Escolha como agrupar os dados**, selecione **Produto**.

  - Resultado esperado: O sistema exibirá uma lista (ou gráfico) com o nome de cada produto e a soma total de unidades vendidas para cada um, respeitando o filtro de valor acima de R$ 100,00.

    ![Imagem 3: Resultado esperado: O sistema exibirá uma lista (ou gráfico) com o nome de cada produto e a soma total de unidades…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220008902/93550cd32f3c9be6a41e38b1276d/Screenshot+2026-03-30+144915.png?expires=1786536000&signature=7de80129c369dfce8d5716aadb49c2c150ac276d846729200ec82bcb517564a3&req=diIlFsl%2BlYhfW%2FMW3nq%2BgRFctOyMIwMXWzfUi%2FTOeHeNrynTVJeOSxtkf6NE%0ARTIjr%2BN4vmoRIRVO%2F4hkd2MkqFY%3D%0A)
