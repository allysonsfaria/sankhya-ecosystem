---
id: "38022295234327"
titulo: "Como validar o custo e a movimentação de estoque após entradas com valores distintos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022295234327-Como-validar-o-custo-e-a-movimenta%C3%A7%C3%A3o-de-estoque-ap%C3%B3s-entradas-com-valores-distintos"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-07-22T14:02:13Z"
rotulos: ["Produtos", "Custos", "Configuração", "Relatórios", "Estoque"]
---

# Como validar o custo e a movimentação de estoque após entradas com valores distintos

## Validação de custos e movimentação de estoque

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Durante um evento sazonal no ano anterior, o PRODUTO R registrou um alto volume de vendas na Axis Ltda.. Para se preparar com antecedência neste novo ciclo, a empresa optou por adquirir o estoque máximo de dois fornecedores distintos, garantindo o abastecimento necessário para atender a demanda com segurança.

Nesse cenário, é fundamental validar o comportamento do custo médio no sistema, já que os valores unitários de compra são diferentes, e também acompanhar a movimentação de entrada no estoque, assegurando que os itens estejam devidamente registrados e disponíveis para venda conforme o planejamento.

**Tarefa:** Siga as orientações indicadas abaixo para validar o custo e movimentação de estoque gerada pelas  entradas do PRODUTO R em valores distintos.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Os custos apresentados devem:**

- Corresponder à média dos valores registrados no lançamento das notas de compra com valores distintos (R$**1,7985**).
- Refletir no Custo C/ICMS os critérios definidos nas configurações realizadas na fórmula e configurações de rentabilidade. (R$**1,8225**).

1. **Validação de custos**

**Variação de Custos de Produtos**

**Acesse**: Comercial » Consulta » Variação de Custos de Produtos 

**Filtros rápidos**

- Informe o código do produto adquirido.
- No campo **Intervalo de Atualização**, preencha com a data da movimentação registrada na nota de compra do produto.
- Em seguida, clique em **Aplicar** para realizar a busca.

**Importante:**

- Essa consulta traz uma visão consolidada sobre a evolução dos custos do item, apontando Data Atualização, Custo Médio com e sem ICMS, Custo Variável e Custo Gerencial entre outros dados relevantes sobre o custo do produto.  Esses indicadores são fundamentais para compreender a formação do custo ao longo do tempo e identificar possíveis distorções que afetem a análise de rentabilidade e precificação.
- Esta rotina é alimentada pela tabela TGFCUS e apresenta um cálculo por dia.

**Recomendação:**

Ajuste a grade e reorganize as colunas de acordo com a prioridade de visibilidade, utilizando o botão **“Configurações”**. Se necessário, utilize o recurso de exportação para **PDF** com base na grade exibida. 

**DBExplorer**

**Acesse**: Configurações » Avançado » DBExplorer

- Clique em “+ Consulta” (Nova aba de Consulta)
- Na aba query 1 cole a expressão:

SELECT \* FROM TGFCUSITE WHERE CODPROD = 5000 AND DTATUAL = '25/05/2025' 
A data informada acima deve ser a mesma utilizada nas compras de valores distintos. 

2. **Consulte a movimentação de estoque**

**Acesse**: Comercial » Gerente » Gerência de Produtos

- No **Período de negociação** informe a data apontada nas notas de compra de valores distintos.
- Busque o **Produto** cadastrado na preparação.
- **Aplique** os filtros para buscar os dados

**Aba Extrato**

- Dt. Ent/Sai. - **Data de Entrada e Saída (Data da compra)**

**Aba Estoque**

- Saldo - **4000**
