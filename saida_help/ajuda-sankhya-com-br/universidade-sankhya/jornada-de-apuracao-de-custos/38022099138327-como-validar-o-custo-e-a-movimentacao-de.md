---
id: "38022099138327"
titulo: "Como validar o custo e a movimentação de estoque após a implantação do produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022099138327-Como-validar-o-custo-e-a-movimenta%C3%A7%C3%A3o-de-estoque-ap%C3%B3s-a-implanta%C3%A7%C3%A3o-do-produto"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-07-22T14:02:18Z"
rotulos: ["Produtos", "Custos", "Configuração", "Relatórios Gerenciais", "Estoque", "Implantação"]
---

# Como validar o custo e a movimentação de estoque após a implantação do produto

## Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A Axis Ltda. passou a trabalhar com o PRODUTO R, e a gestão determinou que o custo desse item fosse acompanhado de perto desde o início, com envolvimento integrado entre as áreas da empresa. O objetivo é evitar qualquer descontrole que possa impactar a margem ou comprometer decisões estratégicas ao longo do tempo, garantindo que a realidade física do estoque esteja sempre alinhada aos relatórios gerenciais.

**Tarefa:** Siga as orientações indicadas e valide o custo atual do PRODUTOR, bem como sua movimentação de estoque, com base nos registros gerados na implantação de estoque.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Os custos apresentados devem:**

- Corresponder ao valor registrado no lançamento de Implantação de Estoque (R$**1,3256**).
- Refletir no Custo C/ICMS os critérios definidos nas configurações realizadas na fórmula e configurações de rentabilidade. (R$**1,3654**).

1. **Validação de custos**

**Variação de Custos de Produtos**

**Acesse**: Comercial » Consulta » Variação de Custos de Produtos 

**Filtros rápidos**

- Informe o código do produto implantado na preparação desta jornada.
- No campo **Intervalo de Atualização**, preencha com a data da movimentação registrada na nota de implantação do produto.
- Em seguida, clique em **Aplicar** para realizar a busca.

**Importante:**

- Essa consulta traz uma visão consolidada sobre a evolução dos custos do item, apontando Data Atualização, Custo Médio com e sem ICMS, Custo Variável e Custo Gerencial entre outros dados relevantes sobre o custo do produto.  Esses indicadores são fundamentais para compreender a formação do custo ao longo do tempo e identificar possíveis distorções que afetem a análise de rentabilidade e precificação.
- Esta rotina é alimentada pela tabela TGFCUS e apresenta um cálculo por dia.

**Recomendação:**

Ajuste a grade e reorganize as colunas de acordo com a prioridade de visibilidade, utilizando o botão **“Configurações”**. Se necessário, utilize o recurso de exportação para **PDF** com base na grade exibida. 

**Planilha de conferência**

- **Faça uma cópia** da planilha de validação: [Conferência de custos - Fórmula 100](https://docs.google.com/spreadsheets/d/1SYLDKxFNFFChQIVOmR0M02qEipD-Xl_LRr849B230sY/edit?usp=drive_link)
- Em seguida, informe o valor unitário na célula indicada e pressione Enter para que o cálculo seja processado automaticamente.
  Os cálculos da planilha devem refletir o custo apontado no sistema.

**Dashboard** **ACELERADORES | AUDITOR CUSTO - FÓRMULA PADRÃO**

- Informe o nro. único da nota de implantação e valide os custos.

2. **Consulte a movimentação de estoque**

**Acesse**: Comercial » Gerente » Gerência de Produtos

- No **Período de negociação** informe a data apontada na nota de implantação.
- Busque o **Produto** cadastrado na preparação.
- **Aplique** os filtros para buscar os dados

**Aba Extrato**

- Dt. Ent/Sai. - **Data de Entrada e Saída (Data da implantação)**

**Aba Estoque**

- Saldo - **1000**

#### Correção e Repetição

- Esteja atento às datas informadas para que
