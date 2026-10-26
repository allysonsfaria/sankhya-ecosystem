---
id: "38022411799959"
titulo: "Como fazer recálculo do preço de tabela e validar movimentações de estoque após a venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022411799959-Como-fazer-rec%C3%A1lculo-do-pre%C3%A7o-de-tabela-e-validar-movimenta%C3%A7%C3%B5es-de-estoque-ap%C3%B3s-a-venda"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-07-22T14:02:11Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "Vendas", "Estoque", "Sankhya"]
---

# Como fazer recálculo do preço de tabela e validar movimentações de estoque após a venda

## Recálculo de preço e movimentações de estoque

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Após realizar diversas compras do PRODUTO R com custos distintos e em períodos diferentes, a Axis Ltda. identificou a necessidade de atualizar o preço de venda praticado. Essa decisão tem como objetivo garantir que o valor comercializado esteja alinhado à realidade fiscal, gerencial e de margem esperada pela empresa.

**Tarefa:** Siga as orientações indicadas para recalcular o preço de venda do PRODUTO R com base nos custos atualizados. Em seguida, emita uma nota de venda considerando todos os itens disponíveis em estoque e valide as movimentações de estoque geradas por esta nota de saída.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Recalcule o preço**

**Acesse**: Comercial » Avançado » Recálculo do Preço de Tabela pela Fórmula de Precificação

- Nos campos **Período de movimento** e **Data de vigor**, informe o intervalo de datas desejado.
- Informe sua empresa
- No campo **Tabela**, selecione **TABELA CASE CUSTOS**
- Em seguida, informe  a fórmula **100 - FÓRMULA - MODELO ACELERADORES**
- Acione o botão “**Recalcular**”

**Observação**: O parâmetro "**Alt. Tab/Fórmula Recálculo Preço Form.Precificação? - ALTTABFORRECPRE**" precisa estar habilitado, para que seja possível a alteração de tabelas que possuem origem diferente de '**zero**'.

2. **Emita a nota de vendas de todos os produtos do estoque**

**Acesse:** Comercial » Consulta » Portal de Vendas

- No **Tipo de Movimento**, selecione **Nota de venda**.
- Clique em “**+**” (**Novo documento - Opções**) e escolha o tipo de operação de **VENDA NF-E**
- Preencha as informações essenciais do cabeçalho
- No painel de itens, informe o produto cadastrado na preparação da jornada e informe a **quantidade total disponível em estoque**
- Confirme a nota.

Esta movimentação será refletida no **Kardex** e **Gerência de Produtos**.

3. **Conferência da movimentação de estoque**

#### Gerência de Produtos

**Acesse**: Comercial » Gerente » Gerência de Produtos

- Nos campos Período de Negociação, informe o intervalo entre a data de implantação e a data da venda.
- Busque o **Produto** cadastrado na preparação.
- **Aplique** os filtros para buscar os dados

**Aba Extrato**

- Dt. Ent/Sai. - **Data da entrada ou saída (compra e venda)**
- Qtd. Neg. - **Quantidade Negociada (A saída sera sinalizada com “-”)**

**Aba Estoque**

- Saldo - **deve estar igual a 0 após a venda total**

#### Kardex

**Acesse:** Comercial » Relatórios » Kardex

**Período**

- Data inicial: **[data da implantação]**
- Data final: **[data da venda]**

**Tipo de relatório**

- Tipo Custo: **Com ICMS**
- Tipo Consulta: Com Giro e Sem GIro

**Filtros**

- Informe sua empresa
- Informe o produto cadastrado na preparação desta jornada

**Outras opções**

- Marque a opção **“Imprimir produtos sem estoque e sem giro”**
- Clique em “**Gerar Kardex**” para emitir o relatório

**O documento gerado deve refletir todas as movimentações do produto, desde a data de implantação até a venda e baixa total do estoque.**
