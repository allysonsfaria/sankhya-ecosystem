---
id: "42427928677271"
titulo: "Tela de atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427928677271-Tela-de-atendimento"
trilha: "NEPPO: Personalização de atendimento > Ticket"
atualizado_em: "2026-08-11T16:13:52Z"
rotulos: ["sync_hc", "neppo_11567107", "neppo", "sync_hash_cf66cf588137"]
---

# Tela de atendimento

Permite ao agente registrar um ticket diretamente da interface de atendimento, centralizando a gestão de solicitações, incidentes ou demandas levantadas durante a conversa com o cliente.

**Personas**: Agente ou Supervisor agente

Para que as personas tenham acesso ao ticket, lembre-se de habilitar as permissões na tela de **Associação de Perfis a Regras**.

[GIF animado: Imagem 1: Para que as personas tenham acesso ao ticket, lembre-se de habilitar as permissões na tela de Associação de Perfis a…](https://ajuda.sankhya.com.br/hc/article_attachments/42636660529431)

[1 - Acesso a funcionalidade](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#1.-Acesso-%C3%A0-funcionalidade)

[2 - Campos do formulário de criação de ticket](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#2.-Campos-do-formul%C3%A1rio-de-cria%C3%A7%C3%A3o-de-ticket)

[3 - Funcionalidades adicionais](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#3.-Funcionalidades-adicionais)

[4 - Ações disponíveis](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#4.-A%C3%A7%C3%B5es-dispon%C3%ADveis)

[5 - Integrações e comportamentos](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#5.-Integra%C3%A7%C3%B5es-e-comportamentos)

[6 - Regras e restrições](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#6.-Regras-e-restri%C3%A7%C3%B5es)

[7 - Exemplos de uso](https://sankhya.zendesk.com/hc/pt-br/articles/42427928677271#7.-Exemplos-de-uso)

---

## 1. Acesso à funcionalidade

- A funcionalidade está disponível na tela de **atendimento** , durante uma conversa com o cliente.
- O agente acessa o botão de **Criar Ticket**, visível abaixo da área de digitação de mensagem, no canto inferior da tela.

  - [GIF animado: Imagem 2: O agente acessa o botão de Criar Ticket , visível abaixo da área de digitação de mensagem, no canto inferior da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/42636660529431)
- O agente consegue acessar o módulo de ticket e visualizar os tickets criados ou vinculado ao projeto que pertence. Para isso, é necessário habilitar a regra na tela de **Associação de Perfis a Regras**.

---

## 2. Campos do formulário de criação de ticket

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| **Projeto** | Dropdown | Sim | Projeto relacionado ao atendimento/ticket. |
| **Cliente** | Dropdown | Sim | Cliente vinculado ao ticket. Preenchido automaticamente com base na sessão ou selecionado manualmente. |
| **Tipo de ticket** | Dropdown | Sim | Classificação do ticket (ex: incidente, dúvida, solicitação). |
| **Prioridade** | Dropdown | Sim | Urgência da demanda (ex: Alta, Média, Baixa). |
| **Canal de comunicação** | Dropdown | Sim | Canal pelo qual o contato foi iniciado (ex: WhatsApp, Webchat, Instagram). |
| **Responsável** | Dropdown | Sim | Usuário ou agente responsável pelo ticket. |
| **Tempo de serviço (SLA)** | Campo de seleção/texto | Não | SLA desejado para resolução do ticket. Pode ser selecionado ou digitado. |
| **Título** | Texto curto | Sim | Nome do ticket, que representa de forma resumida o problema ou solicitação. |
| **Descrição** | Texto longo | Não | Detalhamento da demanda, podendo conter contexto adicional da conversa. |
| **Anexo** | Upload de arquivo | Não | Permite anexar imagens, documentos, prints etc. |
| **Protocolos relacionados** | Multiseleção | Não | Permitir relacionar um ticket a protocolos de atendimento. |
| **Tags** | Tags selecionáveis ou texto | Não | Palavras-chave para facilitar a busca e categorização de tickets. |
| **Tickets associados** | Busca e seleção | Não | Relaciona tickets já existentes com o novo ticket criado (ex: chamados em cadeia). |

---

## 3. Funcionalidades adicionais

- **Anexos**: O agente pode arrastar arquivos ou buscar no dispositivo.
- **Associação de tickets**: Útil para agrupar chamados similares ou complementares.
- **Tags**: Melhoram a organização e filtragem de tickets.

---

## 4. Ações disponíveis

| Botão | Ação |
| --- | --- |
| **Fechar** | Encerra o modal sem salvar os dados. |
| **Criar ticket** | Salva as informações e registra o ticket no sistema. Valida os campos obrigatórios antes da criação. |

---

## 5. Integrações e comportamentos

- Ao criar o ticket:

  - O ticket fica disponível no módulo de tickets com status inicial.
  - Ao criar o ticket, é exibido a informação como comentário na tela de atendimento.

    - ![Imagem 3: Ao criar o ticket, é exibido a informação como comentário na tela de atendimento.](https://ajuda.sankhya.com.br/hc/article_attachments/42636655214999)
  - O agente pode continuar a conversa normalmente após a criação.

---

## 6. Regras e restrições

- Campos obrigatórios precisam ser preenchidos para habilitar o botão “Criar Ticket”.
- A criação de ticket pode estar vinculada ao perfil do agente (tela de permissionamento).

---

## 7. Exemplos de uso

**Cenário 1 - Incidente técnico:**
Durante a conversa, o cliente relata que não consegue acessar a plataforma. O agente cria um ticket do tipo "Incidente", com prioridade alta, vinculando o projeto e o canal de origem (ex: WhatsApp).

**Cenário 2 - Solicitação de feature:**
O cliente sugere uma melhoria no sistema. O agente registra o ticket com tipo "Melhoria", vincula ao projeto e adiciona a tag “UX”.
