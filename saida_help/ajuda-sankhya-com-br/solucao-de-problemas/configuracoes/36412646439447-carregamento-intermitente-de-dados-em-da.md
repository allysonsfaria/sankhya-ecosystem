---
id: "36412646439447"
titulo: "Carregamento intermitente de dados em dashboards"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36412646439447-Carregamento-intermitente-de-dados-em-dashboards"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:23:01Z"
rotulos: ["SQL", "Configuração", "Relatórios", "Dashboards", "DBExplorer", "BI", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Carregamento intermitente", "Dados em dashboards", "Dashboards do BI"]
---

# Carregamento intermitente de dados em dashboards

**SITUAÇÃO:**

Ao aplicar filtros em relatórios e dashboards do BI, os dados não são exibidos na primeira tentativa.

Nesses casos, é preciso **clicar** mais de uma vez em ''**Aplicar Filtro''** ou ''**Atualizar''** para que as informações apareçam.

Esse comportamento ocorre de forma intermitente, ou seja, alguns componentes de BI são afetados, enquanto outros funcionam normalmente.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36412646431511)SOLUÇÃO:**

**(1)** Revise as consultas SQL utilizadas nos componentes de BI.

**(2)** Em seguida, remova as conversões de datas desnecessárias como **TO\_DATE**, **TO\_TIMESTAMP**, **CAST**, ou outras manipulações manuais aplicadas nos parâmetros.

(O Sankhya já envia parâmetros de data devidamente tratados pela aplicação. Quando a consulta realiza uma nova conversão sobre esses valores, pode ocorrer arredondamentos ou interpretações divergentes, resultando no comportamento intermitente.)

- Em vez de usar conversões como:

```
BETWEEN TO_DATE(CAST(TO_TIMESTAMP(:PERIODO.INI, 'yyyy-mm-dd') AS DATE), 'DD/MM/YYYY')
```

- Utilize diretamente os parâmetros fornecidos pelo sistema:

```
BETWEEN :PERIODO.INI AND :PERIODO.FIN
```

Caso a consulta tenha sido construída pela unidade, é necessário que o autor revise o código.

**OBSERVAÇÃO:**
Esse mesmo problema pode ser reproduzido no **DBExplorer,** quando a consulta aplica conversões adicionais. Porém, ao executar diretamente no banco de dados, o comportamento não ocorre, o que reforça que a aplicação já trata corretamente as datas e que a duplicidade de conversões é o ponto crítico da inconsistência.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36412646431895)CAUSA:**

A intermitência ocorre porque os parâmetros de período enviados pela aplicação já chegam ao banco com o tratamento adequado. Quando a consulta SQL aplica conversões adicionais, como **TO\_DATE**, **TO\_TIMESTAMP**, **CAST** ou manipulações manuais, o valor pode ser truncado, arredondado ou interpretado de forma diferente, gerando resultados inconsistentes.
