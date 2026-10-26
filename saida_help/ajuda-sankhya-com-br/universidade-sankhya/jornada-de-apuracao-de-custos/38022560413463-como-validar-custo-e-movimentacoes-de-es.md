---
id: "38022560413463"
titulo: "Como validar custo e movimentações de estoque após remessa de demonstração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022560413463-Como-validar-custo-e-movimenta%C3%A7%C3%B5es-de-estoque-ap%C3%B3s-remessa-de-demonstra%C3%A7%C3%A3o"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-07-22T14:02:07Z"
rotulos: ["Custos", "Relatórios", "Remessa", "Nota Fiscal", "Estoque", "ERP Sankhya"]
---

# Como validar custo e movimentações de estoque após remessa de demonstração

## Validação de custos e movimentação de estoque

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** O PRODUTO R tem gerado resultados expressivos para a Axis Ltda., abrindo portas para novas oportunidades e fortalecendo parcerias estratégicas. Visando ampliar a presença no mercado, uma empresa parceira propôs expor o produto em uma ação de marketing para testar sua aceitação junto ao público-alvo. Para viabilizar essa iniciativa, a Axis Ltda. realizou uma remessa de demonstração, enviando 100 unidades do item sem transferência de propriedade, mantendo-o registrado como parte do estoque próprio. Nessa situação, é fundamental validar se a movimentação foi corretamente registrada no sistema, assegurando que o custo permaneça íntegro e que as saídas de estoque estejam alinhadas ao tipo de operação, evitando distorções nos relatórios gerenciais.

**Tarefa:** Siga as orientações indicadas abaixo para emitir uma remessa de demonstração e em seguida valide se houve impacto no custo médio do produto e estoque. 

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Emita a nota de remessa**

**Acesse:** Comercial » Consulta » Portal de Vendas 

- No **Tipo de Movimento**, selecione **Nota de venda**
- Clique em “**+**” (**Novo documento - Opções**) e escolha o tipo de operação de **REMESSA PARA DEMONSTRAÇÃO**
- Preencha as informações essenciais do cabeçalho e aponte as datas de **Negociação**, **Entrada/saída** e **Faturamento** para **10/06/2025** (data sugerida, esta é uma simulação e pode ser adaptada conforme as movimentações e contexto reais da sua base de testes)
- No painel de itens, informe:

  - Produto: **o item cadastrado na preparação da jornada**
  - Quantidade: **100**
- Confirme a nota.

2. **Consulte a movimentação de estoque**

**Acesse**: Comercial » Gerente » Gerência de Produtos

- No **Período de negociação** informe a data apontada na nota de remessa para demonstração
- Busque o **Produto** cadastrado na preparação.
- **Aplique** os filtros para buscar os dados

**Aba Extrato**

- Dt. Ent/Sai. - **Data de Entrada e Saída (Data da remessa)**

**Aba Estoque**

- Saldo - **1000**

3. **Valide o custo médio do produto e a movimentação de estoque**

**Kardex**
**Acesse:** Comercial » Relatórios » Kardex

**Período**

- Data inicial: **[data da remessa]**
- Data final: **[data da remessa]**

**Tipo de relatório**

- Tipo Custo: **Com ICMS**
- Tipo Consulta: Com Giro e Sem GIro

**Filtros**

- Informe sua empresa
- Informe o produto cadastrado na preparação desta jornada

**Outras opções**

- Marque a opção **“Imprimir produtos sem estoque e sem giro”**
- Clique em “**Gerar Kardex**” para emitir o relatório

**Neste procedimento, você poderá confirmar, por meio do relatório, que não há impacto no Kardex, pois, como não ocorre transferência de propriedade, o produto permanece registrado no seu estoque, mesmo estando fisicamente em poder de terceiros.**
