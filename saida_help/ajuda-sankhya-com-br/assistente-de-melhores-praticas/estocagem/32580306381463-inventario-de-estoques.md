---
id: "32580306381463"
titulo: "Inventário de Estoques"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32580306381463-Invent%C3%A1rio-de-Estoques"
trilha: "Assistente de Melhores Práticas > Estocagem"
atualizado_em: "2026-07-22T14:30:59Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "WMS", "Estoque"]
---

# Inventário de Estoques

### Descrição

A funcionalidade **Inventário de Estoques** permite configurar processos de cópia, contagem, ajuste e análise de inventário, assegurando controle preciso sobre as quantidades armazenadas. As etapas compreendem a criação de tipos de operação, modelos de ajuste, controle de numeração e liberação dos acessos apropriados aos usuários responsáveis.

Ela oferece os seguintes recursos:

- **Cópia de Estoques:** Registro das quantidades em uma data de corte para fins de comparação.
- **Contagem Física:** Registro das quantidades reais encontradas em estoque.
- **Ajustes de Estoque:** Correções das diferenças entre o que foi copiado e o que foi contado.
- **Análise de Estoque:** Consulta e emissão de relatórios de contagem e divergência.
- **Liberação de Acessos:** Concessão automática dos acessos necessários aos responsáveis por cada etapa do inventário.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os grupos e/ou usuários responsáveis pela **cópia de estoques**.
3. Clique em **"Avançar"** para visualizar o resumo.
4. Revise os dados apresentados e clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- **Cópia, Contagem e Ajustes de Estoque:** Consultar, Incluir e Alterar
- **Relatórios de Inventário (405 e 407):** Consultar
- **Kardex, Gerência de Produtos e Consulta de Produtos:** Consultar, Incluir e Alterar

**Tabelas atualizadas**

- **TGFTOP – Tipos de Operação:** Inclusão e ativação das TOPs 1195 e 1495.
- **TGFNUM – Numeração:** Criação da base de numeração **"VENDA"** (modelo 55) com série 1 para empresas ativas, se ainda não existente.
- **TGFCAB – Modelos de Ajuste:** Criação de modelos de entrada e saída vinculados a cada empresa ativa.
- **TGFEMP – Empresas:** Atualização dos campos Modelo Ajuste de Entrada de Estoque (NOTAENTAJUSTEST) e Modelo Ajuste de Saída de Estoque (NOTASAIAJUSTEST) com os modelos de ajuste criados.

**![995dfb79-29b4-43bb-afbe-10f31d50936f](https://ajuda.sankhya.com.br/hc/article_attachments/32580322106263) Vale saber**

Sabia que ao usar o inventário de estoque de forma consistente, você consegue ter uma visão mais clara do seu fluxo de produtos? Isso pode te ajudar a identificar gargalos, otimizar compras e até mesmo prever demandas futuras. Uma estratégia de gestão de estoque bem afinada faz toda diferença no sucesso do seu negócio.
