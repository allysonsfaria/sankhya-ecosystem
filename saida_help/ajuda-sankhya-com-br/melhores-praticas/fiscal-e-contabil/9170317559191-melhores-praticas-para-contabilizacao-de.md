---
id: "9170317559191"
titulo: "Melhores práticas para contabilização de Baixas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9170317559191-Melhores-pr%C3%A1ticas-para-contabiliza%C3%A7%C3%A3o-de-Baixas"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:09:58Z"
rotulos: ["Fórmulas", "Movimentação Financeira", "TOP", "Contabilização", "Financeiro", "Recebidos/pagos vs. compensados", "Usar função Val() para validação correta", "Valores nulos ou zero dificultam a validação"]
---

# Melhores práticas para contabilização de Baixas

**(1)** Na contabilização dos recebimentos e pagamentos quando se utilizada a mesma top de baixa, a diferenciação entre os títulos que foram recebidos/pagos dos títulos quer foram compensados se dá pelo número da compensação registrada no movimento financeiro.

Acontece que as vezes esta informação nos títulos não compensados fica com valor igual a zero ou nulo, o que dificulta sua validação na fórmula de contabilização.

(1)** Então, considerando as fórmulas de contabilização abaixo exemplificadas:**

Títulos recebidos/pagos:
Debito : IF(Formula.NUCOMPENS = 0, Formula.VLRBAIXA, 0)
Crédito: IF(Formula.NUCOMPENS = 0, Formula.VLRBAIXA, 0)

Títulos compensados:
Debito : IF(Formula.NUCOMPENS <> 0, Formula.VLRBAIXA, 0)
Crédito: IF(Formula.NUCOMPENS <> 0, Formula.VLRBAIXA, 0)

Para que o sistema faça a correta validação do conteúdo retornado pela expressão Formula.NUCOMPENS, independente se o número da compensação está com valor nulo e ou preenchido com valor igual ou diferente de zero, é preciso converter o valor retornado pela expressão Formula.NUCOMPENS utilizando a função Val().

(1)** Ficando então as fórmulas exemplificadas anteriormente no seguinte formato:**

Títulos recebidos/pagos:
Debito : IF(Val(Formula.NUCOMPENS) = 0, Formula.VLRBAIXA, 0)
Crédito: IF(Val(Formula.NUCOMPENS) = 0, Formula.VLRBAIXA, 0)

Títulos compensados:
Debito : IF(Val(Formula.NUCOMPENS) <> 0, Formula.VLRBAIXA, 0)
Crédito: IF(Val(Formula.NUCOMPENS) <> 0, Formula.VLRBAIXA, 0)
