---
id: "38022633927575"
titulo: "Como validar custo e movimentações de estoque após devolução de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38022633927575-Como-validar-custo-e-movimenta%C3%A7%C3%B5es-de-estoque-ap%C3%B3s-devolu%C3%A7%C3%A3o-de-venda"
trilha: "Universidade Sankhya > Jornada de Apuração de Custos"
atualizado_em: "2026-07-22T14:02:06Z"
rotulos: ["Produtos", "Custos", "Relatórios Gerenciais", "Estoque", "Devolução", "ERP Sankhya"]
---

# Como validar custo e movimentações de estoque após devolução de venda

## Validação de custos e movimentação de estoque

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Após as vendas que resultaram no esgotamento do estoque do PRODUTO R, um dos clientes solicitou a devolução de 200 itens da compra, motivado por arrependimento.

Essa operação exige atenção especial, pois a devolução implica a entrada do produto no estoque, com a atualização automática do custo baseada na nota fiscal de origem.

O correto registro dessa movimentação é essencial para manter a integridade das informações no Kardex e assegurar que os relatórios gerenciais reflitam a realidade física e financeira do estoque.

**Tarefa:** Siga as orientações indicadas e emita a devolução parcial da venda registrada na aula “Como fazer recálculo do preço de tabela e validar movimentações de estoque após a venda”.

Em seguida, valide o impacto dessa movimentação no custo e no estoque do produto, analisando as informações apresentadas no Kardex.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Emita a nota de devolução**

**Acesse:** Comercial » Consulta » Portal de Vendas 

- No **Tipo de Movimento**, selecione **Devolução de venda**
- Informe os clitérios e aplique os filtros rápidos para localizar a nota emitida na aula “Como fazer recálculo do preço de tabela e validar movimentações de estoque após a venda”
- Clique em “**Dev./Est.**”
- Na janela **Dev./Est.** confirme se a TOP informada é **DEVOLUÇÃO DE VENDA - NF PRÓPRIA** e em seguida conclua a solicitação
- Informe no painel de itens, informe a quantidade (**200**) produtos devolvidos
- Confirme a nota.

2. **Consulte a movimentação de estoque**

**Acesse**: Comercial » Gerente » Gerência de Produtos

- No **Período de negociação** informe a data apontada na nota de remessa para demonstração
- Busque o **Produto** cadastrado na preparação.
- **Aplique** os filtros para buscar os dados

**Aba Extrato**

- Dt. Ent/Sai. - **Data de Entrada e Saída (Data da devolução)**

**Aba Estoque**

- Saldo - **1200**

3. **Valide o custo médio do produto e a movimentação de estoque**

**Kardex**
**Acesse:** Comercial » Relatórios » Kardex

**Período**

- Data inicial: **[data da implantação]**
- Data final: **[data da devolução]**

**Tipo de relatório**

- Tipo Custo: **Com ICMS**
- Tipo Consulta: Com Giro e Sem GIro

**Filtros**

- Informe sua empresa
- Informe o produto cadastrado na preparação desta jornada

**Outras opções**

- Marque a opção **“Imprimir produtos sem estoque e sem giro”**
- Clique em “**Gerar Kardex**” para emitir o relatório

**Este relatório apresentará todas as movimentações de estoque e, ao analisá-lo, você poderá certificar-se de que:**

- **O custo médio do produto está correto**
- **Houve ruptura total do estoque no período analisado**
- **Não ocorreu impacto no custo ou no estoque após a saída para demonstração**
- **O custo médio dos produtos devolvidos está aderente ao custo registrado na operação de origem.**
