---
id: "32317400113047"
titulo: "Apuração de Custos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32317400113047-Apura%C3%A7%C3%A3o-de-Custos"
trilha: "Assistente de Melhores Práticas > Precificação"
atualizado_em: "2026-07-22T16:11:57Z"
rotulos: ["Produtos", "Custos", "Configuração", "TOP", "Estoque"]
---

# Apuração de Custos

### Descrição

A funcionalidade **Apuração de Custos** permite configurar e gerenciar os usuários responsáveis pela apuração e recálculo dos custos, além de automatizar a atualização de informações nos produtos e tipos de operação.
Ela oferece os seguintes recursos:

- Acesso às rotinas de **variação de custos**, **atualização de custos com ou sem filtros**, e **recálculo de custos** com permissão para inclusão, alteração e consulta;
- Atualização automática dos produtos com a **fórmula de custo padrão**;
- Marcação dos tipos de operação que movimentam estoque para que atualizem custos.

Essas ações garantem maior controle sobre o custo dos produtos e contribuem para uma gestão mais precisa da rentabilidade e da precificação.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **usuários e/ou grupos** responsáveis pela apuração de custos.
3. Clique em **"Avançar"**.
4. Revise o resumo com os dados selecionados.
5. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos**

- Variação de Custos dos Produtos
- Atualização de Custo
- Atualização de Custos com Filtro
- Recálculo de Custos

**Tabelas Atualizadas**

- **TGFPRO**
  - Fórmula de Custo/Preço (CODFORMPREC): atualizado com a fórmula padrão (1)
- **TGFEMP**
  - Fórmula de Custo/Preço (CODFORMPREC): atualizado com a fórmula padrão (1)
- **TGFTOP**
  - Precifica (PRECIFICA): marcado como **"C"** (Atualiza somente custo) para TOPs que atualizam estoque (ATUALEST = **'E'** - Entrar)
