---
id: "33123422537111"
titulo: "Mesmo aplicando um percentual de desconto maior do que o desconto máximo do tipo de negociação o sistema não valida o evento 1"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33123422537111-Mesmo-aplicando-um-percentual-de-desconto-maior-do-que-o-desconto-m%C3%A1ximo-do-tipo-de-negocia%C3%A7%C3%A3o-o-sistema-n%C3%A3o-valida-o-evento-1"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:29:36Z"
rotulos: ["Produtos", "Configuração", "Impostos", "TOP", "Venda Mais", "Mesmo aplicando um percentual de desconto maior do que o desconto máximo", "do tipo de negociação o sistema não valida o evento 1.", "desconto", "lançamento de venda", "Erro"]
---

# Mesmo aplicando um percentual de desconto maior do que o desconto máximo do tipo de negociação o sistema não valida o evento 1

**SITUAÇÃO:**

Ao realizar um lançamento de venda e aumentar o valor unitário de um item, o sistema passa a permitir um desconto no total da nota que excede o limite máximo definido no tipo de negociação.

**Exemplo de cálculo realizado pelo sistema nesse cenário:**

**(2)** **Dados do Lançamento:**

Produto 1: Valor de tabela R$ 160,00 | Valor praticado na venda R$ 160,00

Produto 2: Valor de tabela R$ 4,00  | Valor praticado na venda R$ 54,00

Desconto máximo do Tipo de Negociação: 3%

Desconto no total da nota: 25,93% | Valor desconto

(2)** No cálculo o sistema:**

- some o valor total dos produtos (valor praticado na venda, ou seja, considerando a alteração manual), subtraindo-se o desconto aplicado no total da nota: 214,00 - 55,49 = 158,51;
- some o valor de tabela dos produtos x quantidade negociada = 164,00;
- encontre a diferença entre esses valores: 164,00 - 158,51 = 5,49
- encontre a relação desse valor com o valor de tabela dos produtos: 
   
  160,00 + 4,00 = 164,00

  (5,49 / 164,00) x 100 = 3,35%
- compare esse percentual com o percentual máximo do tipo de negociação: 
   
  3,35% > 3% ----> sendo maior que o % máximo do Tipo de Negociação, o sistema solicita liberação.

(2)** Alterando novamente o valor do produto no Lançamento para R$ 55,00:**

- some o valor total dos produtos com base no valor praticado na venda, ou seja, considerando alterações manuais; e subtraia o desconto aplicado no total da nota: 215,00 - 55,75 = 159,25;
- some o valor de tabela dos produtos x quantidade negociada = 164,00;
- encontre a diferença entre esses valores: 164,00 - 159,25 = 4,75
- encontre a relação desse valor com o valor de tabela dos produtos:

  160,99 + 4,00 = 164,00

  (4,75 / 164,00) x 100 = 2,89%
- compare esse percentual com o percentual máximo do tipo de negociação
   
  2,89% > 3% ----> sendo menor que o % máximo do Tipo de Negociação não solicita a liberação

**CAUSA:**

Esse comportamento normalmente ocorre quando há uma alteração manual no valor de venda do produto, pois mesmo que seja alterado o valor na venda, a base de cálculo do sistema para avaliar o desconto máximo continua sendo o preço de tabela dos produtos do lançamento.
