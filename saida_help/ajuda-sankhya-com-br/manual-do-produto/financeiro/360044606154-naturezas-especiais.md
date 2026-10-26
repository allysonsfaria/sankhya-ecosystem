---
id: "360044606154"
titulo: "Naturezas Especiais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154-Naturezas-Especiais"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:28Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios Gerenciais", "Naturezas Especiais", "br.com.sankhya.fin.cad.naturezasespeciais", "Naturezas Especiais manual", "Impostos", "Financeiro", "Natureza", "Códigos e funções para cálculo de impostos", "Configurações para eventos financeiros e relatórios", "Ajustam descrições e geram impostos"]
---

# Naturezas Especiais

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312263562007) Módulo: Financeiro > Avançado
```

---

Nesta tela serão informadas as Naturezas Especiais para cada evento, financeiro, juros, multas, desconto, entre outras.

![Imagem 2: Nesta tela serão informadas as Naturezas Especiais para cada evento, financeiro, juros, multas, desconto, entre outras.](https://ajuda.sankhya.com.br/hc/article_attachments/4416130124567)

| ![Imagem 3: Nesta tela serão informadas as Naturezas Especiais para cada evento, financeiro, juros, multas, desconto, entre outras.](https://ajuda.sankhya.com.br/hc/article_attachments/42312263562647) | Por meio do parâmetro **"Descrição para Despesas c/cartório - DESPCART"**, você pode alterar a descrição do campo Despesas com Cartórios de acordo com sua necessidade. |
| --- | --- |

As naturezas informadas serão utilizadas nos seguintes Relatórios Gerenciais:

- [Fluxo de Caixa Matricial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606874);
- [Fechamento Financeiro Diário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606514);
- [Analítico por Natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606674);
- [Sintético por Centro de Resultado - Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114873);
- [Sintético por Natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606134);
- [Sintético por Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115033).

Ressaltamos que estes dois últimos serão utilizados quando na seção **"Apresentar resultado por"** estiver definida com opção **"C.Resultado/Natureza"**.

Se o título no Financeiro estiver com os campos **"Vlr Juros"**, **"Vlr Desconto"**, **"Vlr Multa"** gerados e todos os outros que também fizerem parte da tela Naturezas Especiais, ao visualizar os relatórios serão apresentados os valores para cada natureza utilizada, como uma espécie de rateio por naturezas.

A tela Naturezas Especiais conta também com dois campos para **"Outros Impostos Retidos"**.

Nos Relatórios Gerenciais, o sistema tratará os impostos mensais em naturezas separadas, se a marcação **"Considerar Naturezas Especiais"**, localizada na tela [Sintético por Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115033), estiver efetuada e forem informadas as naturezas na tela Naturezas Especiais.

![Imagem 4: Nos Relatórios Gerenciais , o sistema tratará os impostos mensais em naturezas separadas, se a marcação "Considerar…](https://ajuda.sankhya.com.br/hc/article_attachments/4416121566231)

| ![Imagem 5: Nos Relatórios Gerenciais , o sistema tratará os impostos mensais em naturezas separadas, se a marcação "Considerar…](https://ajuda.sankhya.com.br/hc/article_attachments/42312263562647) | O parâmetro **"Gerar impostos (ISS, INSS, IRF) no financeiro? - GERIMPOSTO"** quando habilitado gerará os impostos convencionais (IRF, ISS, INSS) no Financeiro. |
| --- | --- |

A seguir, trouxemos um exemplo de fórmula do [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) que irá gerar o valor do desdobramento bruto:

```
![Imagem 6: A seguir, trouxemos um exemplo de fórmula do Tipo de Negociação que irá gerar o valor do desdobramento bruto:](https://ajuda.sankhya.com.br/hc/article_attachments/42312263564567) VLRNOTA + IMPOSTONOTA(1, NUNOTA) + IF(ISSRETIDO = 'S', VLRISS, 0) + IF(INSSRETIDO = 'S',
 VLRINSS, 0)
```

A função ImpostoNota(CodImp,NUNota) será utilizada na fórmula do Tipo de Negociação, por exemplo: VLRNOTA + IMPOSTONOTA(1, NUNOTA).

---

**Sobre os campos CODIMP, CODINC e a tabela TGFDIN**

A TGFDIN é a tabela onde se encontram os Impostos da Nota, tais como, PIS, COFINS e CSLL. Os códigos CODIMP e CODINC são internos do sistema e compõem a tabela TGFDIN nos campos CODIMP (Código Imposto) e CODINC (Código Incidência). Vejamos abaixo a diferença entre estes dois códigos internos:

| **CODIMP**  **Código do Imposto (CODIMP TGFDIN)**   --- | | **CODINC**  **Código da Incidência (CODINC TGFDIN)**   --- | |
| --- | --- | --- | --- |
| ICMS | 1 | Geral | 0 |
| ST | 2 | Produto | 1 |
| IPI | 3 | Serviço | 2 |
| ISS | 4 | Frete | 3 |
| INSS | 5 | Seguro | 4 |
| PIS | 6 | Destaque | 5 |
| COFINS | 7 | Embalagem | 6 |
| IRF | 8 | Juro | 7 |
| CSLL | 9 |  | |

Para utilizar valores de impostos oriundos da tabela TGFDIN, é necessário utilizar a função PDES.

Os exemplos abaixo irão apresentar o valor total dos impostos PIS e COFINS por nota:

(1)** PIS:**

Val(Pdes('SUM(DIN.VALOR)','TGFDIN DIN','DIN.CODIMP=6 AND DIN.NUNOTA='+queTGFCAB.NUNOTA))

---

(1)** COFINS:**

Val(Pdes('SUM(DIN.VALOR)','TGFDIN DIN','DIN.CODIMP=7 AND DIN.NUNOTA='+queTGFCAB.NUNOTA))

---

(1)** Demais impostos:**

| **CODIMP**  **Código do Imposto (CODIMP TGFDIN)**   --- | |
| --- | --- |
| ICMS | 1 |
| ST | 2 |
| IPI | 3 |
| ISS | 4 |
| INSS | 5 |
| PIS | 6 |
| COFINS | 7 |
| IRF | 8 |
| CSLL | 9 |
