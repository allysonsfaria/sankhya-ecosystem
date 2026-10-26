---
id: "42430492752919"
titulo: "Componente Redirecionar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430492752919-Componente-Redirecionar"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:05:32Z"
rotulos: ["sync_hc", "neppo", "neppo_858000408", "sync_hash_92a92ae8ea96"]
---

# Componente Redirecionar

O componente **Redirecionar** transfere o atendimento para outro destino: **Fila de atendimento**, **Grupo de atendimento**, **Agente**, **Fila do agente**, **Item do fluxo**, e **Pesquisa de satisfação**. É o componente que faz a ponte entre o bot e o atendimento humano.

---

## Visão geral

Use o Redirecionar quando a conversa deve sair do controle do fluxo atual:

- **Grupo de atendimento** — transfere para um grupo de atendentes (informado pelo nome do grupo).
- **Agente** — transfere para um atendente específico (informado pelo usuário do agente). Opcionalmente, permite indicar também o **grupo** de destino, possibilitando redirecionar para agentes de grupos diferentes do grupo do bot (ver seção Tipo Agente — Grupo (opcional)).
- **Fila do agente** — transfere para a fila de um agente
- **Item do fluxo** — desvia para outro fluxo do bot (segue e **não volta**, diferente do componente Executar).
- **Fila de atendimento** — envia o usuário para a fila, opcionalmente com mensagem.
- **Pesquisa de satisfação** — dispara a pesquisa configurada na plataforma.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Redirecionar**.

---

## Tipo Agente — Grupo (opcional)

No tipo **Agente**, além do agente é possível informar um **grupo** de destino. Isso permite redirecionar o atendimento para agentes pertencentes a grupos diferentes do grupo onde o bot está, eliminando o isolamento de filas entre bots e agentes de outras frentes de atendimento.

### Interface (UI)

- **Seleção de Agente** — listagem completa dos agentes ativos no ambiente, com suporte a variáveis para redirecionamento dinâmic.
- **Seleção de Grupo (opcional)** — campo exibido de forma condicional após a seleção de um agente válido, listando apenas os grupos vinculados àquele agente. Também aceita variáveis, resolvidas em tempo de execução para os IDs de destino.

### Regras de negócio e comandos

O comando executado depende dos parâmetros configurados:

| Configuração | Comando executado |
| --- | --- |
| Agente + Grupo | `FORWARD_AGENT_QUEUE` — o atendimento sai do fluxo do bot e vai direto para a fila do agente no grupo especificado |
| Agente + Grupo + Mensagem | `FORWARD_AGENT_QUEUE_WITH_MESSAGE` — mesmo comportamento, com a mensagem contextual exibida ao operador que recebe o atendimento |

![Imagem 1: FORWARD_AGENT_QUEUE_WITH_MESSAGE — mesmo comportamento, com a mensagem contextual exibida ao operador que recebe o…](https://ajuda.sankhya.com.br/hc/article_attachments/42639807481495)

### Validações fora do escopo (tratar no fluxo)

O componente **não valida** antes de redirecionar:

- se o agente está **online**;
- se o agente **permanece vinculado** ao grupo selecionado;
- se o redirecionamento ocorre dentro do **horário de atendimento**.

Essas validações devem ser feitas **previamente, na construção do fluxo do bot** (ex.: consulta de horário/feriado via Neppo API antes do redirecionamento).

---

## Comportamento

- O redirecionamento é **terminal para o fluxo atual**: no tipo Fluxo, a execução segue no destino e **não retorna** ao ponto de origem (para chamar um fluxo como sub-rotina e voltar, use o componente **Executar**).
- Nos tipos Grupo/Agente/Fila, o bot encerra sua participação e o atendimento passa ao controle humano ou à fila.
- A mensagem opcional é enviada ao usuário antes/junto da transferência (ex.: aviso de fora do horário de atendimento).
- Internamente gera uma ação `redirect` com o tipo de destino (ex.: `type_redirect: "queue"` com comando `SEND_MESSAGE_AND_REDIRECT_TO_QUEUE`; tipo Agente com grupo usa `FORWARD_AGENT_QUEUE` / `FORWARD_AGENT_QUEUE_WITH_MESSAGE`).

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção:

**Fila de espera com mensagem** (fluxo "Fora do Horário de Atendimento") — quando a verificação de horário/feriado indica que não há atendentes, o usuário recebe a mensagem de plataforma e vai para a fila:

- Tipo: **Fila de espera**
- Mensagem: `{{mensagemPlataforma}}` (texto configurado na plataforma, obtido via Neppo API)

**Transferência para grupo** (fluxo "[Funções] Tratativas Excedidas") — após 3 respostas inválidas no menu, o bot avisa "Seu atendimento será direcionado para o nosso time." e executa o fluxo de transferência, que redireciona para o grupo passado como argumento (`{"Grupo": "Quero ser Aluno"}`).

---

## Boas práticas e limitações

- Sempre envie uma **mensagem de contexto** antes de transferir (o que está acontecendo e por quê).
- Antes de redirecionar a grupo ou agente, valide **horário de atendimento e feriados** (padrão do exemplo real: consulta via Neppo API + desvio para fila fora do horário).
- No tipo Agente com grupo, valide também no fluxo se o **agente está online** e **vinculado ao grupo** — o componente não faz essas verificações.
- Confira a grafia exata do **nome do grupo** e do **usuário do agente** — o destino é resolvido por nome.
- Lembre-se: redirecionamento para fluxo **não retorna**; se precisar voltar, use **Executar**.
- Centralize a transferência em um fluxo reutilizável parametrizado pelo nome do grupo (padrão "[Transferir Atendimento]" do exemplo real).
