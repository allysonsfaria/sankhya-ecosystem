---
id: "38022176408343"
titulo: "Como validar o custo e a movimentação de estoque após entrada com valor padrão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022176408343-Como-validar-o-custo-e-a-movimenta%C3%A7%C3%A3o-de-estoque-ap%C3%B3s-entrada-com-valor-padr%C3%A3o"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-07-22T14:02:16Z"
rotulos: ["Produtos", "Custos", "Configuração", "Relatórios Gerenciais", "Estoque", "Sankhya"]
---

# Como validar o custo e a movimentação de estoque após entrada com valor padrão

## Validação de custos e movimentação de estoque

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A inclusão do PRODUTO R no portfólio da Axis Ltda. trouxe bons resultados, devido à sua alta margem e excelente aceitação no mercado. Mesmo com o item já consolidado no catálogo, é essencial manter o acompanhamento contínuo do custo e da movimentação de estoque, assegurando a integridade das informações que alimentam os relatórios gerenciais.

Recentemente, foi realizada uma compra de 1.000 unidades com valor unitário fixo, e agora é necessário validar se o custo foi corretamente atualizado e se a movimentação de entrada foi registrada de forma consistente no estoque, garantindo que o preço de venda permaneça alinhado à realidade operacional e financeira da empresa.

**Tarefa:** Siga as orientações indicadas abaixo para validar o custo e movimentação de estoque gerada pela entrada do PRODUTO R.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Os custos apresentados devem:**

- Corresponder ao valor registrado no lançamento da nota de compra com valor padrão (R$**1,7756**).
- Refletir no Custo C/ICMS os critérios definidos nas configurações realizadas na fórmula e configurações de rentabilidade. (R$**1,8289**).

1. **Validação de custos**

**Variação de Custos de Produtos**

**Acesse**: Comercial » Consulta » Variação de Custos de Produtos 

**Filtros rápidos**

- Informe o código do produto adquirido.
- No campo **Intervalo de Atualização**, preencha com a data da movimentação registrada na nota de compra do produto.
- Em seguida, clique em **Aplicar** para realizar a busca.

**Importante:**

- Essa consulta traz uma visão consolidada sobre a evolução dos custos do item, apontando Data Atualização, Custo Médio com e sem ICMS, Custo Variável e Custo Gerencial entre outros dados relevantes sobre o custo do produto. Esses indicadores são fundamentais para compreender a formação do custo ao longo do tempo e identificar possíveis distorções que afetem a análise de rentabilidade e precificação.
- Esta rotina é alimentada pela tabela TGFCUS e apresenta um cálculo por dia.

**Recomendação:**

Ajuste a grade e reorganize as colunas de acordo com a prioridade de visibilidade, utilizando o botão **“Configurações”**. Se necessário, utilize o recurso de exportação para **PDF** com base na grade exibida. 

**Planilha de conferência**

- **Faça uma cópia** da planilha de validação do custo médio: [Verificação de custo médio - Oficina](https://docs.google.com/spreadsheets/d/169k9kbILvFdUaGlNxC9wtgpUVvSOc_u3lRlZQpYB7yE/edit?usp=drive_link)
- Em seguida, informe o valor unitário da compra e implantação nas células indicadas e pressione Enter para que o cálculo seja processado automaticamente.
  Os cálculos da planilha devem refletir o custo apontado no sistema.

2. **Consulte a movimentação de estoque**

**Acesse**: Comercial » Gerente » Gerência de Produtos

- No **Período de negociação** informe a data apontada na nota de compra de valor padrão.
- Busque o **Produto** cadastrado na preparação.
- **Aplique** os filtros para buscar os dados

**Aba Extrato**

- Dt. Ent/Sai. - **Data de Entrada e Saída (Data da compra)**

**Aba Estoque**

- Saldo - **2000**
