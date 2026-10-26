---
id: "26020491481751"
titulo: "Configurações Necessárias para Geração do LCDPR / Q100"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26020491481751-Configura%C3%A7%C3%B5es-Necess%C3%A1rias-para-Gera%C3%A7%C3%A3o-do-LCDPR-Q100"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:23Z"
rotulos: ["Configuração", "Impostos", "Financeiro", "Natureza", "Configurações Necessárias para Geração do LCDPR / Q100", "LCDPR", "Produtor Rural"]
---

# Configurações Necessárias para Geração do LCDPR / Q100

A geração do Livro Caixa Digital do Produtor Rural (LCDPR) é obrigatória para pessoas físicas que se enquadram em determinadas condições. As situações que tornam obrigatória a geração da LCDPR são as seguintes:

#### Situações que Tornam Obrigatória a Geração da LCDPR

**![Imagem 1: Receita Bruta Anual : Quando o produtor rural pessoa física obtiver receita bruta anual superior a R$ 4,8 milhões.](https://ajuda.sankhya.com.br/hc/article_attachments/26071482175383) Receita Bruta Anual**: Quando o produtor rural pessoa física obtiver receita bruta anual superior a R$ 4,8 milhões.

**![Imagem 2: Participação em Consórcio](https://ajuda.sankhya.com.br/hc/article_attachments/26071472030231) Participação em Consórcio**

**![Imagem 3: Exploração de Atividade Rural em Condições de Solidariedade](https://ajuda.sankhya.com.br/hc/article_attachments/26071482176407) Exploração de Atividade Rural em Condições de Solidariedade**

**![Imagem 4: Alienação de Bens Imóveis](https://ajuda.sankhya.com.br/hc/article_attachments/26071482177047) Alienação de Bens Imóveis**

**![Imagem 5: Obtenção de Receita](https://ajuda.sankhya.com.br/hc/article_attachments/26071482178455) Obtenção de Receita**

**![Imagem 6: Exemplo Prático](https://ajuda.sankhya.com.br/hc/article_attachments/26071472040087)  Exemplo Prático**

**Situação**: Um produtor rural atua na agricultura e possui uma fazenda onde cultiva soja. Em 2023, a receita bruta da venda de soja alcançou R$ 5 milhões.

**Obrigatoriedade**: como a receita bruta anual ultrapassou o limite de R$ 4,8 milhões, ele está obrigado a gerar e enviar o Livro Caixa Digital do Produtor Rural (LCDPR) à Receita Federal.

Neste livro, deverá registrar todas as receitas e despesas relacionadas à sua atividade rural, permitindo um controle mais detalhado e transparente para fins de fiscalização tributária.

#### 1° Passo

**Tela - Cadastro de Parceiros -** Configurações > Cadastros > Parceiros

- **Aba Fiscal:**
  - Classificação ICMS: selecione **"Produtor Rural"**;
  - Marque a opção **"Produtor tem NF's";**
  - Preencha o campo **"CPF Prod. Rural" com o CPF do produtor rural".**

####

#### 2° Passo

**Tela Empresa -** Comercial > Preferências > Empresa

- **Aba Livro Caixa Digital Produtor Rural:**
  - Marque a opção **"Gera informações para o Livro Caixa Digital Produtor Rural";**
  - Preencha os seguintes campos:
    - **"Cod. CAFIR"**
    - **"Cod. CAEPF"**
  - Campo **"Tipo de Exploração":** definir o tipo
  - Na mesma aba, do grid inferior > incluir o parceiro produtor rural cadastrado anteriormente;
  - Percentual de Exploração: definir e informar o percentual de exploração.

**Observação:** Essas informações são essenciais para o registro Q100, usado no cálculo do valor de entrada e saída.

#### 3° Passo

**Tela Cadastro de Naturezas de Receitas e Despesas -** Configurações > Cadastros > Gerencial > Natureza de Receitas e Despesas

- **Crie Natureza de ‘Receita’ para ser usada em lançamentos que representar ‘Receita’**
  - Marque a opção **"Gera informações para o Livro Caixa Digital Produtor Rural"**.
- **Crie Natureza de ‘Despesa’ para se usada em lançamentos que representar ‘Despesa’**
  - Marque a opção Gera informações para o Livro Caixa Digital Produtor Rural.

####

#### 4° Passo

**Tela  Cadastro de Contas Bancárias -** Configurações > Cadastros > Bancários > Contas

- Campo **"Desconsiderar Conta na Geração do Livro Caixa Digital do Produtor Rural" "não"**pode estar

#### 5° Passo

**Tela Impostos -** Configurações > Cadastros > Impostos

- **Crie Imposto SENAR:**
  - **Campo "Tipo":** coluna "Calcular" marcada;
  - **Campo "Tipo Imposto":** selecione "SENAR";
  - **Campo "Usar para itens da nota":** escolha "Preço da Nota";
  - **Campo "Base para Impostos do Financeiro":** selecione "Valor do Pagamento".

- **Abas Parceiro / TOP / Empresa :** Informe o parceiro cadastrado anteriormente.
  - **Campo "Calcular":** marque "Sim";
  - **Campo "Na nota":** deixe marcado "Já incluso";
  - **Campo "No Financeiro Origem Financeiro":** deixe "Nenhum";
  - **Campo "No Financeiro Origem Estoque":** selecione "Subtrair";
  - **Alíquota:** informe alíquota pertinente ( Apenas para  abas TOP/ Empresa / Produto)
  - **Na nota:** marque "Já incluso".

####

#### 6° Passo

**Tela Tipos de Título -** Financeiro > Arquivos > Cadastros > Tipos de Título

- **Aba "Geral":** no campo "Tipo Documento Rural", preencha conforme necessário.
- **Nota:** certifique-se de que o título lançado na Movimentação Financeira esteja configurado corretamente.

#### 7° Passo

**Tela Tipos de Negociação -** Comercial > Arquivo > Cadastros > Tipos de Negociação

- **Criar Tipo de Negociação:**
  - **Aba Parcelas:**
    - **Parcela 1 ( Receita):** informe Natureza Receita.

- **Parcela 2 ( Despesa):** informe Natureza Despesa;
- **Campo Tipo de Parceiro:** Selecione "C - Constante";
  - **Campo Parceiro:** Informar o parceiro Produtor Rural
  - **Campo Fórmula:**  VALORIMPOSTO(X,'V'), onde X é o número do imposto criado.
- **Campo Tipo de Financeira (REC/DESP):** Escolha "Usar da Natureza Padrão".

#### 8° Passo

**Tela Preferências -** Configurações > Avançado > Preferências

- No parâmetro **NATTITNAONOT**, informe a natureza de **‘Despesa’** criada na etapa anterior.

###

#### 9° Passo

**Lançamento da Nota Fiscal -** Comercial > Consulta > Portal de Vendas ou,

Comercial > Consulta > Portal de Compras ( nota de venda deve estar aprovada)

###

#### 10° Passo

**Movimentação Financeira -** Financeiro > Rotinas > Movimentação Financeira

- Título deve estar baixado;
- A data da baixa deve estar dentro do período informado no LCDPR ( não pode ser nula)

#### 11° Passo

**Geração do Livro Caixa Digital Produtor Rural (LCDPR)**

**Tela Livro Caica Produtor Rural - LCDPR -** Livros Fiscais > Conexão > Livro Caixa Produtor Rural - LCDPR

- **Produtor:** informe o parceiro utilizado;
- **Data Inicial e Final:** informe o período desejado;
- **Aba Geral: preencha de acordo com o cenário da empresa**
  - Clique em **“Processar”**.

####

#### Aba Q100 - Verificação do Registro Q100

**Exemplo de geração:**

- **Imposto:** Q100|20042022|160|001|110207|1|Pagamento ref NF N 110207 SEFAZ PE|10572014000133|2|000|3118|3376235|P
- **Receita:** Q100|20042022|160|001|110207|1|Recebimento ref NF N 110207 PARCEIRO PF|12508370657|1|15590|000|4932117|P
