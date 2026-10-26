---
id: "42429510389911"
titulo: "Pesquisar tickets"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429510389911-Pesquisar-tickets"
trilha: "NEPPO: Personalização de atendimento > Ticket"
atualizado_em: "2026-08-11T15:49:43Z"
rotulos: ["sync_hc", "neppo", "neppo_207126532", "sync_hash_96a63fecbe45"]
---

# Pesquisar tickets

O objetivo da funcionalidade é permitir que os usuários visualizem e filtrem todas as ocorrências (tickets) abertas dentro do sistema, com possibilidade de criar novos tickets, pesquisar por tickets específicos, aplicar filtros e identificar rapidamente status e responsáveis.

![Imagem 1: O objetivo da funcionalidade é permitir que os usuários visualizem e filtrem todas as ocorrências (tickets) abertas…](https://ajuda.sankhya.com.br/hc/article_attachments/42637273281943)

---

## 1. Barra de filtros

- **Campo de busca:** Pesquisar tickets por título ou ID.
- **Filtros adicionais:**

  - **Projeto:** Dropdown para selecionar o projeto relacionado ao ticket.
  - **Status:** Dropdown para filtrar tickets pelo status.
  - **Responsável:** Dropdown para filtrar pelo responsável designado.
  - **ID:** Permite buscar um ticket específico pelo seu **identificador único**.
  - **Cliente:** Filtra os tickets vinculados a um determinado cliente
- **Botão "Filtrar":** Aplica os filtros selecionados.
- **Botão "Criar Ticket":** (localizado no canto superior direito) abre o drawer o de criação de ticket.
- **Download/exportação** no lado direito: faz o download dos itens selecionados em CSV

---

### 3. Aba de visualização

- **Geral:** Lista todos os tickets do sistema.
- **Meus Tickets:** Lista somente os tickets atribuídos ao usuário logado.

---

## Tabela de Tickets

| Coluna | Descrição |
| --- | --- |
| **ID** | Identificador único do ticket (ex: `validacao-1`). |
| **Título** | Título ou resumo da ocorrência registrada. |
| **Status** | Indicação visual do progresso do ticket (ex: `Para Fazer`, com tag laranja). |
| **Responsável** | Avatar e nome do responsável pelo ticket. |

---

## Funcionalidades adicionais

- **Setas vermelhas (↑):** Indicadores visuais que representam prioridade do ticket.
- **Paginação:** Controle de linhas por página e navegação entre páginas na parte inferior direita da tabela.

---

## Comportamentos esperados

- Ao clicar no botão “Criar Ticket”, o usuário é redirecionado o drawer de novo ticket.
- Ao selecionar filtros e clicar em “Filtrar”, a lista é atualizada conforme os critérios escolhidos.
- A aba “Meus Tickets” mostra apenas os tickets atribuídos ao usuário autenticado.
- O botão de busca realiza a filtragem instantânea de tickets pelo texto digitado.
