---
id: "360044594214"
titulo: "Processo Recálculo de Custos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214-Processo-Rec%C3%A1lculo-de-Custos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:19:34Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Custos", "Cálculo de custos médio", "Recálculo de Custos", "br.com.sankhya.com.mov.recalculocustos", "Recálculo de Custos manual", "Configuração", "Atualização", "TOP", "Exclusão de Custos", "Fórmula de Precificação", "Cálculo de Custos de Entrada", "Comercial"]
---

# Processo Recálculo de Custos

```
 Módulo: Comercial > Avançado
```

## O que é e para que serve

O Recálculo de Custos é uma ferramenta que permite realizar o recálculo de custos de produtos a partir de movimentações de entrada — notas de compra, produção etc. Essa funcionalidade é útil em casos de alterações em fórmulas de precificação (fórmulas de custo/preço) necessárias, devido a redefinições em políticas de custeio e precificação. A rotina não recalcula custos de produtos com **Uso do Produto** definido como "Matéria-Prima".

![Imagem 1: O Recálculo de Custos é uma ferramenta que permite realizar o recálculo de custos de produtos a partir de movimentações…](https://ajuda.sankhya.com.br/hc/article_attachments/4406750748951)

## Como usar a rotina

As movimentações consideradas para o recálculo são as de entrada que tenham a **Precificação** do Tipo de Operação (TOP) diferente de "Não atualizar custo nem preço de venda".

**ℹ️ Nota**

A fórmula de precificação utilizada nesta rotina e no **Recálculo do Preço de Tabela pela Fórmula de Precificação** é a mesma.

### Período de Negociação

**Período de Negociação** — trata-se da data de negociação. Informe o intervalo que será verificado para efetuar o recálculo.

Ao abrir a tela de recálculo de custos e ao confirmar uma nota que gere cálculo de custo, são apresentadas as seguintes mensagens:

Quando o parâmetro **Data para atualização de custo (DTPATUCUST)** está configurado como "Negociação":

"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos "Dt. Negociação". Foi identificado que você está usando configuração diferente do que é atualmente permitido, entre em contato com a Sankhya para se informar sobre as consequências de usar esta configuração."

Quando o parâmetro `DTPATUCUST` está configurado como "Movimentação ou Faturamento":

"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos "Dt. Negociação". Foi identificado que você possui configuração diferente de "Dt. Entrada/Saída", para não ver esta mensagem novamente, basta ajustar o parâmetro "Data para atualização de custo" (DTPATUCUST) colocando a opção "Entrada/Saída", quando o parâmetro "DTPATUCUST" está igual a "Negociação"."

Para que as mensagens não sejam apresentadas, configure o parâmetro `DTPATUCUST` para "Entrada/Saída".

> ℹ️ **Por que o sistema sempre considera a data de Entrada/Saída?** O comportamento é fixo por determinação fiscal e contábil: a data de Entrada/Saída (DTENTSAI) é a única data que garante consistência para fins de apuração de custos, tributos e relatórios contábeis. Por isso, independentemente da opção configurada no parâmetro DTPATUCUST, o sistema sempre usará essa data como referência. Para entender melhor como esse parâmetro afeta a tela Atualização de Custos, consulte o artigo [Atualização de Custos].

### Botões da rotina

- **Excluir custos manuais/tarifas do período** — ao clicar neste botão, serão excluídos os cadastros lançados manualmente pelas rotinas de **Atualização de Custos** e **Atualização de Custos (por filtro)**.
- **Excluir custos do período** — ao clicar neste botão, serão excluídos os custos que estão dentro do período especificado provenientes das movimentações cujas TOPs estejam configuradas para atualizar custo no campo **Precificação**.

**⚠️ Atenção**

O filtro personalizado foi projetado originalmente sem suporte ao levantamento encadeado de insumos. Quando aplicado para um produto acabado, o cálculo considera apenas o Produto Acabado selecionado, ignorando os Produtos Intermediários (PIs) e Matérias-Primas (MPs) a ele associados. Isso pode resultar em custos incompletos ou incorretos.

**Impactos:**

• Custos de produção apurados sem considerar todos os insumos vinculados ao PA.

• Divergência nos relatórios de custo quando o filtro de produto é utilizado.

• Risco de decisões baseadas em dados de custo incompletos.

**Evite utilizar o filtro por Produto Acabado para cálculos de custo que dependam do levantamento completo da cadeia de insumos. Caso necessite de um cálculo preciso, execute o processo sem o filtro de produto.**

- **Calcular Custos de Entrada** — serão calculados os custos dentro do período e filtros informados, dos produtos cujo **Uso do Produto** seja diferente de "Matéria-Prima" e cujas movimentações estejam confirmadas e atualizando custos. Ao realizar o cálculo, será considerada uma ordenação dinâmica para os produtos.

**ℹ️ Nota**

Se o parâmetro **Custo por Empresa (CUSTOPOREMP)** estiver habilitado, o campo **Empresa** será exibido na tela. Se o parâmetro **Controla Custos por Controle (CUSTOPORCONT)** estiver ligado, o recálculo de custo considerará o **Controle** do produto.

**ℹ️ Nota**

Para realizar o recálculo de custos de produção em situações nas quais os códigos dos Produtos Acabados (PAs) forem menores que o código de suas Matérias-Primas (MPs) — ou seja, os PAs forem criados antes de suas MPs —, a ordem dos produtos deve ser invertida. Para isso, ative o parâmetro **Ordena produto decrescente ao calcular custo produção (ORDDESCCUSPROD)**.

## Pontos de atenção

O sistema apresenta a variação de preço de venda ao confirmar uma nota de compra cuja TOP esteja configurada para precificar. Se o parâmetro **Apresentar variação de preço na NF de compra (APRVARPNFCOMPRA)** estiver habilitado, o sistema apresenta a mensagem:

"Houve variação no preço de venda. Deseja visualizar os produtos com variação?"

Ao clicar em **Sim**, é apresentada a variação do preço em relação à última data de vigor da tabela de preço, ignorando o dia da confirmação da nota de compra.
