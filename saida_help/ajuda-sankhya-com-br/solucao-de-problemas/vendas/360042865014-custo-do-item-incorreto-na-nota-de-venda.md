---
id: "360042865014"
titulo: "Custo do item incorreto na nota de venda (TGFITE.CUSTO)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865014-Custo-do-item-incorreto-na-nota-de-venda-TGFITE-CUSTO"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-19T21:32:48Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Custo", "Nota Fiscal", "Preferências", "Ajuste o parâmetro \"GOL-TIPOCUSTO\"", "Valor incorreto do custo dos itens", "Escolha o custo correto: Reposição Gerencial etc", "Artigo atualizado KCS", "CVE - KCS"]
---

# Custo do item incorreto na nota de venda (TGFITE.CUSTO)

**SITUAÇÃO:**
Ao realizar emissão de nota pela tela **"Central de Vendas"** (Comercial >> Rotinas >> Central de Vendas), o custo dos itens está com valor incorreto (TGFITE.CUSTO) ou apresenta divergências no Custo Gerencial.

O **"Custo Gerencial"** é um componente fundamental para a gestão de estoque e precificação no ERP Sankhya. Erros no cálculo deste custo podem impactar diretamente relatórios, inventários e análises financeiras.

**SOLUÇÃO E CONFIGURAÇÕES:**

### 1. Verificação do parâmetro GOL-TIPOCUSTO

**(1)** Acesse a tela **"Preferências"** (Configurações >> Avançado >> Preferências), pesquise pelo parâmetro **"GOL-TIPOCUSTO"** e veja qual valor está no campo **"Inteiro"**. Este parâmetro define qual custo é gravado no item das vendas e pedidos (TGFITE.CUSTO), e também o custo considerado na rentabilidade e na margem de contribuição. O sistema usa o último custo registrado do produto, do tipo escolhido.

**(2)** Considere os seguintes valores suportados:
0 - Custo de Reposição | 1 - Custo Gerencial | 2 - Custo Variável | 3 - Custo Médio sem ICMS | 4 - Custo Médio com ICMS | 5 - Entrada sem ICMS | 6 - Entrada com ICMS | 7 - Custo Médio Gerencial (disponível com o parâmetro **GOL-CUSMEDGER** ligado).

**(3)** Este parâmetro pode ser configurado pelas preferências do **"Gerente On-Line - GOL"** (Comercial >> Gerente >> Gerente On-Line - GOL) >> **"Margem de Contribuição"** campo **"Custo a ser considerado"**. A alteração vale para todos os usuários.

**(4)** Acesse **"Variação de Custos de Produtos"** (Comercial >> Consulta >> Variação de Custos de Produtos), pesquise pelo produto e verifique a necessidade da empresa para o ajuste no parâmetro.

**(5)** Acesse a nota de venda novamente (ainda não confirmada) e redigite o produto para que o custo seja recalculado conforme a alteração.

### 2. Ajuste da fórmula de custo

Se o custo calculado ainda estiver incorreto após o ajuste do parâmetro:

• **Atenção:** o campo **"Usar como Preço"** da TOP não altera o custo do item: ele define o **preço unitário** a partir de um custo. Em TOP de venda, ele normalmente fica como **"Preço de Venda"**. Configurá-lo como um custo faz a venda sair com preço igual ao custo.
• Caso utilize fórmula personalizada, revise a expressão na tela **"Fórmulas de Custo/Preço"** (Comercial >> Avançado >> Fórmulas >> Fórmulas de Custo/Preço) para garantir que contempla ICMS, IPI, ST, Frete, entre outros. A fórmula é vinculada ao produto (ou à empresa) e calcula o custo das entradas; é esse custo que a venda usa.
• Após o ajuste, realize o recálculo do custo pela tela **"Recálculo de Custos"** (Comercial >> Avançado >> Recálculo de Custos).

### 3. Casos especiais: bonificação e custo zerado

**Produtos Bonificados:** para que as entradas bonificadas tenham custo zero, inclua na fórmula a condição **IF(queTOP.BONIFICACAO = 'S', 0, <fórmula atual>)**. Atenção: entradas com custo zero reduzem o custo médio do produto.
**Custo zerado:** ocorre quando o sistema não localiza custo registrado para o produto. Acesse a tela **"Recálculo de Custos"** (Comercial >> Avançado >> Recálculo de Custos), processe para o período e redigite o produto na nota. Se o parâmetro **"Cálculo de Custo assíncrono"** (CALCCUSTOASSINC) estiver ativo, o custo das entradas é calculado em segundo plano; aguarde o processamento antes de lançar a venda.

**CAUSA:** Configurações inadequadas no parâmetro **"GOL-TIPOCUSTO"**, custo do produto ausente ou desatualizado, ou inconsistências nas fórmulas de custo vinculadas ao produto.
