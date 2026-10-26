---
id: "38022032016663"
titulo: "Apuração de Custos no ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022032016663-Apura%C3%A7%C3%A3o-de-Custos-no-ERP-Sankhya"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-08-06T19:49:13Z"
rotulos: ["Custos", "Configuração", "Relatórios Gerenciais", "Estoque", "Financeiro", "ERP Sankhya"]
---

# Apuração de Custos no ERP Sankhya

## Conceitos fundamentais

A apuração de custos é um pilar essencial para empresas que desejam manter controle financeiro e competitividade. No ERP Sankhya, ela não se resume a um cálculo único — envolve conceitos, regras e parâmetros que impactam diretamente relatórios fiscais e gerenciais.  Quando feita corretamente, garante preços justos, margens preservadas e decisões mais seguras.

O primeiro passo é entender a diferença entre **custos** e **despesas**:

- **Custos** → todos os gastos diretamente ligados a ter o produto pronto para revenda ou produção.
  Exemplos: compra de insumos, mão de obra direta, embalagens utilizadas na venda, frete de mercadorias para revenda.
- **Despesas** → gastos para manter a empresa funcionando, sem relação direta com a produção ou revenda.
  Exemplos: aluguel, compra de máquinas para ativo fixo, frete de maquinário.

Separar corretamente evita distorções nos relatórios e mantém a precificação alinhada à realidade.

No ERP Sankhya, o custo é formado através de **fórmulas** que podem incluir componentes fiscais, operacionais e variáveis. Caso a empresa não configure fórmulas próprias, o sistema aplica uma fórmula interna que calcula com base nas entradas de notas — não permitindo custo zero, salvo por fórmulas personalizadas.

As modalidades de custo no Sankhya são:

- **Custo de Reposição** → valor para recomprar o produto, considerando impostos como IPI, baseado na última compra.
- **Custo com/sem ICMS** → custo fiscal definido pelo regime tributário.
- **Custo Variável** → agrega custos fiscais e variáveis (comissões, impostos sobre vendas, custo financeiro), usado em análises de rentabilidade.
- **Custo Gerencial** → usado para precificação, incluindo margem de lucro desejada.

**Formação de Preço e Atualização de Custo**

O ponto de partida para configurar custos no Sankhya é o **regime tributário** da empresa, que define a lógica das fórmulas.
As fórmulas podem ser configuradas:

- **Por empresa** → uma regra única para todos os produtos (mais comum em empresas comerciais).
- **Por produto** → regras específicas, aplicadas em indústrias, kits ou importados com particularidades de custo.

A atualização do custo acontece automaticamente na entrada de notas fiscais quando as **TOPs** estão configuradas para alimentar estoque e custo, ou manualmente.
O sistema pode ser parametrizado para impedir atualização com valores inferiores aos vigentes.

O cálculo do custo médio segue o método de **Média Ponderada Móvel**:

**Custo Médio = (Valor total do estoque anterior + Valor da nova compra) ÷ (Quantidade anterior + Quantidade adquirida)**

Para que a composição seja correta, é essencial que saldos anteriores, compras e vendas estejam registrados corretamente.
Somente movimentações que alteram a titularidade do produto são consideradas — transferências internas, por exemplo, não entram no cálculo.

#### Qual o papel do Kardex?

O **Kardex** é o extrato de todas as movimentações que afetam custo ou propriedade do produto, sejam fiscais ou não fiscais.
Ele utiliza o método de **Média Ponderada Móvel** e recalcula o custo a cada nova entrada no mesmo dia, considerando **quantidade** e **custo**.

**Lógica do cálculo**:

1. Saldo inicial (quantidade × custo médio)
2. (+) Entradas (quantidade × custo da nota)
3. (–) Saídas (quantidade × custo médio vigente)
4. (=) Saldo final (quantidade × novo custo médio ponderado)

**Ordem de processamento**:

1. Reprocesso de produção de Produto Acabado (PA)
2. Entradas de produtos
3. Devoluções de venda com custo calculado
4. Saídas de produtos
5. Devoluções de venda sem custo calculado

**Premissas para evitar divergências**:

- Operações que atualizam estoque devem atualizar também o custo.
- Não registrar saídas antes da entrada da nota de compra.
- Apenas movimentações de estoque próprio aparecem no Kardex.
- Transferências internas e envios para terceiros (industrialização, consignação, demonstração, conserto) não aparecem.
- Notas fiscais não confirmadas afetam o custo médio, mesmo sem aparecer no Kardex.

**Situações especiais**:

- **Movimentação com terceiros** → não altera custo.
- **Notas complementares** → alteram custo; devem referenciar a nota original e estar configuradas corretamente.
- **Transferências entre empresas** → alteram custo por mudança de titularidade entre CNPJs.
- **Devoluções de venda** → utilizam o custo da nota de origem.

#### Tabelas e Ajuste de Saldos

O Sankhya armazena as informações de custo e estoque nas tabelas:

- **TGFCUS** → custo diário por produto.
- **TGFCUSITE** → custo por item de nota.
- **TGFEST** → quantidades em estoque.
- **TGFESE** → movimentações para cálculo do custo médio.

Divergências podem ser corrigidas pela tela **Verificação de Saldo de Estoque**, que recalcula todas as entradas e saídas para restaurar a consistência.

A apuração correta de custos no ERP Sankhya combina conhecimento conceitual, configuração adequada e disciplina operacional.

Com esses elementos alinhados, a empresa garante preços corretos, relatórios confiáveis e uma visão real da rentabilidade.
