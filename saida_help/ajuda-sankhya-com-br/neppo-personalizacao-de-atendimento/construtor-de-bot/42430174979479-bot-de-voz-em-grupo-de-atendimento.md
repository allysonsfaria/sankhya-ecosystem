---
id: "42430174979479"
titulo: "Bot de voz em grupo de atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430174979479-Bot-de-voz-em-grupo-de-atendimento"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:59:06Z"
rotulos: ["sync_hc", "neppo", "neppo_476643331", "sync_hash_efcb57b33a5b"]
---

# Bot de voz em grupo de atendimento

Este documento descreve o processo completo para **associar um Bot de Voz a um Grupo de Atendimento**, permitindo que chamadas recebidas sejam atendidas inicialmente por um bot e, quando necessário, encaminhadas para agentes humanos via **URA (Unidade de Resposta Audível)**.

O fluxo garante:

- Padronização da jornada de voz
- Escalabilidade do atendimento
- Integração clara entre automação e atendimento humano

**Versões mínimas:**
Versão neppochat-server 2.10.1000
Versão bot-server 1.1.173
Versão voice-gateway 2.5.82
Versão voice-service 1.0.27

---

## Pré-requisitos

Antes de iniciar, o cliente deve garantir que:

- O **canal de voz** esteja ativo no ambiente
- O usuário possua permissão para:

  - Criar bots
  - Criar e editar grupos de atendimento
  - Configurar URA

---

## Etapas do processo

### 1. Criação do bot de Voz

**Objetivo:** Definir o agente automatizado que fará o primeiro atendimento da chamada.

**Passos:**

1. Acesse o módulo **Construtor de Bot de Voz**
2. Crie um novo bot
3. Salve e publique o bot

**Resultado esperado:**
Bot de voz disponível para associação a grupos de atendimento.

---

### 2. Criação do grupo de atendimento

**Objetivo:** Definir o grupo responsável por receber chamadas transferidas do bot ou iniciar atendimentos.

**Passos:**

1. Acesse o módulo **Grupos de Atendimento**
2. Crie um novo grupo
3. Configure o grupo

---

### 3. Ativação do canal de voz no grupo

**Objetivo:** Habilitar o grupo para operar atendimentos por voz.

![Imagem 1: Objetivo: Habilitar o grupo para operar atendimentos por voz.](https://ajuda.sankhya.com.br/hc/article_attachments/42639516000023)

**Passos:**

1. Dentro do grupo criado, localize a seção **Canais de atendimento**
2. Marque o checkbox **Canal de voz**

**Regra importante:**

> Sem o canal de voz habilitado, o grupo **não aparecerá** para associação na URA.

---

### 4. Vincular o bot ao grupo (Agente de inicialização)

**Objetivo:** Definir qual bot iniciará o atendimento quando uma chamada entrar no grupo.

![Imagem 2: Objetivo: Definir qual bot iniciará o atendimento quando uma chamada entrar no grupo.](https://ajuda.sankhya.com.br/hc/article_attachments/42639516175383)

**Passos:**

1. Ainda na configuração do grupo, localize o campo **Agente de Inicialização**
2. Selecione o **Bot de Voz** previamente criado
3. Salve o grupo

**Comportamento esperado:**

- As chamadas direcionada a este grupo será iniciada pelo bot

---

### 5. Configurar o grupo de voz no menu URA

**Objetivo:** Tornar o grupo acessível a partir do fluxo de URA.

![Imagem 3: Objetivo: Tornar o grupo acessível a partir do fluxo de URA.](https://ajuda.sankhya.com.br/hc/article_attachments/42639516442647)

**Passos:**

1. Acesse o módulo **URA**
2. No menu ou fluxo desejado:

   - Selecione o **Grupo de Atendimento de Voz**
