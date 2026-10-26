---
id: "42430459468695"
titulo: "Categorias - Refatoração Visual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430459468695-Categorias-Refatora%C3%A7%C3%A3o-Visual"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:05:25Z"
rotulos: ["sync_hc", "neppo", "neppo_858000263", "sync_hash_4dff10d48e07"]
---

# Categorias - Refatoração Visual

## Categorias — Refatoração Visual

Refatoração visual e reposicionamento da tela de **Categorias** dentro do Studio CX, sem alterações nas regras de negócio ou funcionalidades existentes.

**Novo caminho de navegação:** `Studio CX > Configurações > Categoria`

---

## Objetivo

Centralizar o gerenciamento de categorias na área de configurações do Studio CX, mantendo o comportamento atual da funcionalidade e aplicando melhorias de design e experiência do usuário.

[GIF animado: Imagem 1: Centralizar o gerenciamento de categorias na área de configurações do Studio CX, mantendo o comportamento atual da…](https://ajuda.sankhya.com.br/hc/article_attachments/42639745028503)

---

## Escopo

### O que muda

| Item | Descrição |
| --- | --- |
| Localização no menu | Tela movida para `Studio CX > Configurações > Categoria` |
| Layout e design | Adequações visuais seguindo o novo padrão da plataforma |
| Componentes | Botões, tabelas e formulários atualizados conforme design system |
| Hierarquia visual | Melhorias de organização e legibilidade da interface |

### O que não muda

- Regras de negócio
- Funcionalidades existentes
- Modelo de dados
- Integrações

---

## Funcionalidades Mantidas

### Cadastro de categorias

Criar, editar e remover categorias de agentes.

### Associação de categorias a agentes

Categorias criadas ficam disponíveis na seleção durante a configuração dos agentes.

### Exibição nos templates do construtor

Ao associar um agente a uma categoria, a categorização continua exibida nos templates do construtor.

---

## Jornada — Nova Categoria

1. Usuário clica em **Nova Categoria**.
2. **drawer lateral**

   - Nome (obrigatório)
   - Descrição (obrigatório)
   - Ícone — seleção de ao menos um (obrigatório)
3. O botão **Salvar** fica ativo somente após o preenchimento de todos os campos obrigatórios.
4. Ao salvar, a categoria aparece na tabela e na seleção de categorias.

[GIF animado: Imagem 2: Ao salvar, a categoria aparece na tabela e na seleção de categorias.](https://ajuda.sankhya.com.br/hc/article_attachments/42639774981015)

---

### Design

Interface segue o novo padrão visual da plataforma

Componentes respeitam o design system — <https://kale-search-48771074.figma.site/>

### Funcionalidade

É possível criar categorias

É possível editar categorias

É possível remover categorias

Categorias aparecem na tabela

Categorias aparecem na seleção durante construção do agente

Ao excluir uma categoria, o agente perde o vínculo mas não sofre outras alterações

### Compatibilidade

Nenhuma funcionalidade atual sofre regressão

Categorias já existentes permanecem funcionais

---

## Impacto Esperado

- Melhor organização do menu de configurações do Studio CX
- Navegação mais intuitiva para o usuário
- Padronização visual da plataforma
- Maior consistência na gestão de agentes e categorias
