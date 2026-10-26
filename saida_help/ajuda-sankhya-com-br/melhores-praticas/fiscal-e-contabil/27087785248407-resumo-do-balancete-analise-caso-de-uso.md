---
id: "27087785248407"
titulo: "Resumo do Balancete - Análise / Caso de Uso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27087785248407-Resumo-do-Balancete-An%C3%A1lise-Caso-de-Uso"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:40:10Z"
rotulos: ["Configuração", "Relatórios", "Contas", "Análise", "Financeiro", "Resumo do Balancete - Análise / Caso de Uso"]
---

# Resumo do Balancete - Análise / Caso de Uso

Na Tela Balancete de verificação é possível gerar o balancete com resumo.

O **resumo do balancete** é uma versão simplificada do balancete contábil, que apresenta de forma consolidada as principais contas da empresa, como Ativo, Passivo, Patrimônio Líquido, Receitas e Despesas. Ele oferece uma visão geral da situação financeira da empresa, facilitando a análise sem muitos detalhes.

#### Configurações necessárias:

(1)**Gerar resumo do balancete de verificação:** deve estar marcada

Ao marcar essa opção, os campos para informar a conta de grau 1 de cada grupo ficarão disponíveis.

![Imagem 1: Ao marcar essa opção, os campos para informar a conta de grau 1 de cada grupo ficarão disponíveis.](https://ajuda.sankhya.com.br/hc/article_attachments/27122668658071)

**"Importante:** o campo **"Conta grau 1 custos"** será apresentado somente  quando o parâmetro **"CTBCUSRESUMO"** estiver ligado.

![Imagem 2: "Importante: o campo " Conta grau 1 custos" será apresentado somente quando o parâmetro "CTBCUSRESUMO" estiver ligado.](https://ajuda.sankhya.com.br/hc/article_attachments/27087785239191)

(2)** Usando o Exemplo Vamos analisar os valores**

**Importante:** sempre que se tratar de uma conta de natureza **Credora**, lançamentos a Crédito aumentam o saldo da conta e lançamentos a Débito diminuem o saldo da conta.

Sempre que se tratar de uma conta de natureza **Devedora**, lançamentos a Débito aumentam o saldo e lançamentos a Crédito diminuem o saldo.

(2)**Analisando por linha tem-se o seguinte resultado:**

- **Ativo**

Saldo Anterior: **189.274.132,08 D**

Lançamentos a Débito no período: **25.006.450,79 ( soma ao Saldo anterior)**

Lançamentos a Crédito no período: **28.814.358,75 ( subtrai ao Saldo anterior)**

Saldo Atual: **185.466.224,12 D**

- **Passivo** (conta de natureza credora, lançamento a crédito aumenta, lançamento a débito diminui )

Saldo Anterior: **175.356.952,37 C**

Lançamentos a Débito no período: **5.019.764,66  ( subtrai ao Saldo anterior)**

Lançamentos a Crédito no período: **2.900.709,31 ( soma ao Saldo anterior)**

Saldo Atual: **173.237.897,00 C**

**Observação:** a mesma análise pode ser feita para as linhas ‘Contas de resultado - Receitas (Natureza credora) e Contas de Resultado - Custo / Despesa (natureza devedora)’

(2)**Analisando por coluna tem-se o seguinte resultado:**

- **Pegando a coluna Saldo Atual**

Ativo  **185.466.224,12D**

Passivo     **173.237.897,00C**

Contas de Resultado - Receita   **90.502.908,00C**

Contas de Resultado - Custo/ Despesa  **78.713.222,03D**

**185.466.224,12**

**(-) 173.237.897,00**

**(-) 90.502.908,00**

**+ 78.713.222,03**

**—--------------------**

**438.641,12**
