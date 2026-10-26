---
id: "32564278235031"
titulo: "Formação do Preço de Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32564278235031-Forma%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda"
trilha: "Assistente de Melhores Práticas > Precificação"
atualizado_em: "2026-07-22T14:31:00Z"
rotulos: ["Configuração", "Parceiro", "Vendas", "Tabelas de Preço", "Preço de Venda"]
---

# Formação do Preço de Venda

### Descrição

A funcionalidade **Formação do Preço de Venda** permite configurar critérios e regras para definição dos preços praticados nas operações comerciais, com base em variáveis como custo de aquisição, região de venda, perfil de cliente, tipo de negociação ou combinação desses fatores.
Ela oferece os seguintes recursos:

- **Criação de Tabelas de Preço:** Criação e manutenção da tabela principal e de suas variações, com definição de percentual de acréscimo ou decréscimo.
  - **Parametrização:** Aplicação de parâmetros para refletir os critérios de segmentação da política de preços.
  - **Vinculação por Critério:** Atribuição das tabelas de preços com base em critérios como região, parceiro, empresa ou tipo de negociação.
  - **Liberação de Acessos:** Concessão automática de acessos aos usuários responsáveis pela formação e manutenção dos preços.

### Como instalar

- Clique em **"Iniciar"**.
  - Selecione os grupos e/ou usuários responsáveis pela formação de preços de venda.
  - Informe se existem múltiplas tabelas de preços.
  - Caso existam variações, selecione o critério que define a segmentação (região, parceiro, empresa etc.).
  - Defina a **Tabela de Preço Principal**.
  - Cadastre as tabelas dependentes com seus respectivos percentuais de variação.
  - Atribua as tabelas aos registros conforme o critério definido (vendedor, parceiro, etc.).
  - Clique em **"Avançar"** para revisar a configuração.
  - Clique em **"Instalar"** para concluir o processo.

### Detalhes da instalação

**Acessos liberados**

- Formação de Preços (Atualização Preço de Venda)
  Permissões: Incluir, Alterar, Consultar
- Cadastro de Tabelas de Preço
  Permissões: Incluir, Alterar, Consultar
- Atualização Preço de Venda pela Compra
  Permissões: Incluir, Alterar, Consultar
- Simulação de Negociação
  Permissões: Incluir, Alterar, Consultar
- Recalculo em Massa de Tabelas de Preço
  Permissões: Incluir, Alterar, Consultar
- Consulta Variação de Preços
  Permissões: Incluir, Alterar, Consultar

**Tabelas atualizadas**

- **TGFNTA – Tabela de Preço (Cabeçalho)**
  Criação da tabela principal (código 0) e de todas as tabelas derivadas informadas, com os nomes e percentuais correspondentes.
- **TGFTAB – Variação de Preço (Percentuais)**
  Definição dos percentuais de variação entre as tabelas.

**Parâmetros (TSIPAR)**

- **TIPTABPRECOS:** Define o critério principal de segmentação de preços.
- **EMPPRODIMPOST:** Ativa o uso de imposto por empresa, se necessário.

**Vínculo da Tabela de Preço (conforme critério selecionado):**

- **TSIREG:** Região do vendedor ou do parceiro.
- **TGFPAR:** Parceiro.
- **TGFTPV:** Tipo de Negociação.
- **TGFNPV:** Tipo de Negociação x Vendedor.
- **TGFPAEM:** Empresa x Parceiro.
- **TGFTPP:** Perfil.
- **TSILOC:** Local.

![Imagem 1: Vale saber](https://ajuda.sankhya.com.br/hc/article_attachments/32564248639639) **Vale saber**

Planejar os seus preços de venda com estratégia é essencial para o sucesso do seu negócio. É importante pensar não só nos seus custos, mas também no valor que o seu produto ou serviço tem para o cliente, e como os preços dos concorrentes influenciam a sua estratégia. Uma tabela de preços bem estruturada te ajuda a ter mais controle e flexibilidade na hora de negociar, além de maximizar seus lucros!
