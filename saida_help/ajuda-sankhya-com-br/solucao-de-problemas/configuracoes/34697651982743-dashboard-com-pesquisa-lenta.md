---
id: "34697651982743"
titulo: "Dashboard com Pesquisa Lenta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34697651982743-Dashboard-com-Pesquisa-Lenta"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:26:49Z"
rotulos: ["Configuração", "Relatórios", "Parâmetros", "Construtor de Componentes de BI", "BI", "Dashboard com Pesquisa Lenta", "Tratamento Correto de Parâmetros NULL", "Relatórios via iReport", "Desempenho"]
---

# Dashboard com Pesquisa Lenta

**SITUAÇÃO:**

Dashboards criados no **Construtor de Componentes de BI** ou **Relatórios via iReport** apresentam lentidão significativa durante:

- Execução de pesquisas
- Pré-visualização de dados
- Carregamento inicial

**SOLUÇÃO:**

#### **(1)** Tratamento Correto de Parâmetros NULL

Para evitar lentidão, é **essencial** tratar parâmetros que podem receber valores vazios de forma adequada:

- **Regra Principal**

Sempre que um parâmetro de consulta puder vir vazio, force o NULL a ser interpretado como **string**, mesmo que o campo original seja numérico.

- **Boas Práticas**

- Trate NULL como texto, não como valor nulo do banco;

- Evite criar parâmetros com filtros de entidade sem torná-los obrigatórios;

- Use comparações que permitam ao banco utilizar índices.

#### Exemplos Práticos:

Caso um campo entidade em um filtro não seja obrigatório, ele poderá receber valor NULL, mas deve ser tratado como texto para que consulta entenda que não o precisa filtrar e evitar uma consulta longa.

**Forma Correta:**

```
UPPER(:P_CODPROD) = 'NULL' OR CODPROD = :P_CODPROD
```

A maneira abaixo causará lentidão na busca, pois o valor em :P\_CODPROD IS NULL será tratado como nulo e não como texto, assim não utilizando índices durante a consulta e buscando em toda a tabela

**Forma incorreta:**

```
CODPROD = :P_CODPROD OR :P_CODPROD IS NULL
```

**CAUSA:**

O banco de dados não consegue otimizar consultas com comparações NULL porque:

1. **Ambiguidade**: precisa determinar se deve buscar um valor específico ou registros com campo nulo;

2. **Índices ignorados**: comparações com `IS NULL` frequentemente ignoram índices;

3. **Varredura completa**: o banco precisa percorrer toda a tabela para garantir que encontrou todos os registros.
