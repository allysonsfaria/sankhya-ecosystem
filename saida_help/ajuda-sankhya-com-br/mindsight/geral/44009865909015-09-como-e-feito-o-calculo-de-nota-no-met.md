---
id: "44009865909015"
titulo: "09. Como é feito o cálculo de nota no Metas?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44009865909015-09-Como-%C3%A9-feito-o-c%C3%A1lculo-de-nota-no-Metas"
trilha: "Mindsight > Geral"
atualizado_em: "2026-10-05T18:24:41Z"
rotulos: ["sync_hc", "mindsight", "sync_hash_857c05f1a8fe", "mindsight_219746871219"]
---

# 09. Como é feito o cálculo de nota no Metas?

O resultado de uma meta é calculado em etapas. Primeiro, o sistema identifica o **percentual de atingimento** da meta. Em seguida, esse percentual é convertido em uma **nota**, de acordo com a escala configurada na rodada.

Quando existem várias metas, as notas são posteriormente consolidadas em uma nota final por meio de **média simples ou ponderada**.

## 1. Como é calculado o atingimento da meta?

O cálculo considera o valor **inicial**, o valor **esperado** e o valor **realizado**.

Existem dois tipos de metas:

### Metas progressivas

São aquelas em que **quanto maior o resultado, melhor**.

Exemplos: aumentar vendas, aumentar o número de entregas ou aumentar a receita.

O cálculo considera a evolução entre o valor inicial e o valor esperado e compara essa evolução com o resultado realizado.

**Exemplo:**

- Inicial: 100
- Esperado: 200
- Realizado: 150

A pessoa percorreu **50% do caminho entre o valor inicial e o esperado**, portanto, o atingimento é de **50%**.

### Metas reversas

São aquelas em que **quanto menor o resultado, melhor**.

Exemplos: reduzir custos, diminuir erros ou reduzir o número de reclamações.

**Exemplo:**

- Inicial: 100
- Esperado: 50
- Realizado: 75

A pessoa percorreu **50% do caminho entre o valor inicial e o esperado**, portanto, o atingimento é de **50%**.

> **Importante:** quando os valores inicial e esperado estão invertidos em relação ao tipo de meta, o sistema realiza ajustes no ponto de 0% para que o cálculo permaneça coerente.

## 2. Como o atingimento é transformado em nota?

Depois de calcular o percentual de atingimento, o sistema transforma esse resultado em uma **nota**, utilizando a escala configurada na rodada.

O cálculo utiliza **interpolação linear**, que permite calcular proporcionalmente uma nota quando o percentual de atingimento está entre dois níveis da escala.

Por exemplo, se uma faixa da escala corresponde a determinados percentuais de atingimento e notas, um resultado que fique no meio dessa faixa também receberá uma nota proporcional — evitando que resultados diferentes recebam exatamente a mesma nota.

Existem também limites para a escala:

- Atingimento abaixo da menor faixa → recebe a **menor nota** da escala.
- Atingimento acima da maior faixa → recebe a **maior nota** da escala.

## 3. Como é calculada a nota final quando existem várias metas?

Quando um participante possui mais de uma meta, as notas podem ser consolidadas por meio de **média simples ou média ponderada**, conforme a configuração definida no painel de metas.

### Média simples

Todas as metas possuem o mesmo peso.

**Exemplo:**

- Meta 1: nota **100**
- Meta 2: nota **80**
- Meta 3: nota **70**

**Cálculo:**

**(100 + 80 + 70) ÷ 3 = 83,3**

**Nota final: 83,3**

### Média ponderada

Cada meta possui um peso de acordo com sua importância.

**Exemplo:**

| Meta | Peso | Nota |
| --- | --- | --- |
| Meta 1 | 0,3 | 100 |
| Meta 2 | 0,2 | 80 |
| Meta 3 | 0,5 | 70 |

**Cálculo:**

**[(0,3 × 100) + (0,2 × 80) + (0,5 × 70)] ÷ (0,3 + 0,2 + 0,5)**

**= (30 + 16 + 35) ÷ 1**

**= 81**

**Nota final: 81,0**

## 4. Como são combinadas as metas individuais e as metas da área?

Quando o participante possui **metas individuais e metas da área**, a nota final também pode ser calculada por média simples ou ponderada, conforme a configuração.

**Exemplo:**

- Metas individuais: peso **0,5**, nota **81**
- Meta da área 1: peso **0,3**, nota **50**
- Meta da área 2: peso **0,2**, nota **100**

**Cálculo:**

**[(0,5 × 81) + (0,3 × 50) + (0,2 × 100)] ÷ (0,5 + 0,3 + 0,2)**

**= (40,5 + 15 + 20) ÷ 1**

**= 75,5**

**Nota final: 75,5**

## Resumindo

O cálculo segue esta lógica:

**Resultado realizado → % de atingimento → nota da meta → média das metas → nota final**

A nota final, portanto, depende tanto do **desempenho em cada meta** quanto dos **pesos configurados para cada uma delas**.

**Observação:** pequenas diferenças de casas decimais podem ocorrer devido a arredondamentos realizados pelo sistema ou por ferramentas como o Excel.
