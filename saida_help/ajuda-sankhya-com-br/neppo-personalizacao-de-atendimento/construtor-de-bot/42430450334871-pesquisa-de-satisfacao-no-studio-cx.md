---
id: "42430450334871"
titulo: "Pesquisa de Satisfação no Studio CX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:05:15Z"
rotulos: ["sync_hc", "neppo", "neppo_858000221", "sync_hash_cac46517beec"]
---

# Pesquisa de Satisfação no Studio CX

## Pesquisa de Satisfação no Studio CX

- [Pesquisa de Satisfação no Studio CX](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#Pesquisa-de-Satisfacao-no-Studio-CX)
  - [1. Contexto](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#1-Contexto)
  - [2. Objetivo do produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#2-Objetivo-do-produto)
  - [3. Objetivos de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#3-Objetivos-de-negocio)
  - [4. Escopo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#4-Escopo)
  - [5. Regras de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#5-Regras-de-negocio)
  - [6. Jornada esperada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#6-Jornada-esperada)
  - [7. Templates e configurações padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#7-Templates-e-configuracoes-padrao)
  - [8. Criar pesquisa personalizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#8-Criar-pesquisa-personalizada)
  - [9. Configurações do fluxo no Builder](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#9-Configuracoes-do-fluxo-no-Builder)
  - [10. Vinculo do agente de Pesquisa ao Grupo de Atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#10-Vinculo-do-agente-de-Pesquisa-ao-Grupo-de-Atendimento)
  - [11. Exemplo de uso (cenário prático)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#11-Exemplo-de-uso-cenario-pratico)
  - [12. Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#12-Boas-praticas)
  - [13. Perguntas frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430450334871-Pesquisa-de-Satisfa%C3%A7%C3%A3o-no-Studio-CX#13-Perguntas-frequentes-FAQ)

**Resumo executivo**

Migramos a Pesquisa de Satisfação para dentro do Builder (Studio CX), tornando-a um fluxo conversacional estruturado, configurável e versionável. Agora você cria, compõe e publica NPS, CSAT e Pergunta Aberta como agentes, com gatilhos, regras, status, versionamento e armazenamento estruturado das respostas, sem depender da tela antiga.

## 1. Contexto

**Aviso para clientes single tenant**

Clientes single tenant manterão a tela antiga em modo somente leitura até a descontinuação e uso definido no novo módulo.

**Descontinuação:** ocorrerá após a migração completa das pesquisas antigas (JavaScript) para o novo módulo no bot-server multitenant.

A Pesquisa de Satisfação era gerida em uma tela dedicada, com configuração própria e fora do fluxo conversacional do Studio CX. Isso limitava flexibilidade, versionamento e reaproveitamento de componentes. A nova abordagem centraliza a orquestração no Studio CX, permitindo que a pesquisa seja um fluxo nativo, com as mesmas capacidades dos demais fluxos conversacionais.

[GIF animado: Imagem 1: A Pesquisa de Satisfação era gerida em uma tela dedicada, com configuração própria e fora do fluxo conversacional do…](https://ajuda.sankhya.com.br/hc/article_attachments/42639737576727)

## 2. Objetivo do produto

Permitir que pesquisas de satisfação sejam criadas e editadas no Studio CX, utilizando os mesmos componentes, regras, governança e versionamento já existentes para fluxos conversacionais.

## 3. Objetivos de negócio

- Centralizar a orquestração da jornada no Builder.
- Reduzir complexidade técnica e débitos arquiteturais.
- Aumentar a flexibilidade de configuração.
- Melhorar governança e versionamento.

## 4. Escopo

### Incluído

- Nova categoria de fluxo: **Pesquisa**.
- Templates padrão: **NPS**, **CSAT**, **Pergunta Aberta**.
- Criação de pesquisas personalizadas com múltiplas perguntas.
- Controle de status (ativo/inativo) e versionamento.
- Registro estruturado das respostas, vinculado ao atendimento.
- Feedback condicional para respostas negativas (configurável).
- Mensagem de agradecimento após conclusão.
- Controle de envio por tipo de agente (Bot, Agente, Supervisor).
- Parâmetro de inatividade (min, h, d).
- Limite de respostas inválidas e mensagem orientativa.

### Fora do escopo

- Reformulação inicial de relatórios analíticos.
- Mudança estrutural do modelo de métricas existente.
- Novos tipos de entrada “lista e botões”.
- Distinção por tipo de atendimento (ativo/receptivo).

## 5. Regras de negócio

- RN01: Apenas uma pesquisa ativa por gatilho de encerramento por canal.
- RN02: Sem resposta do cliente → atendimento encerra normalmente.
- RN03: Não reabrir sessões já finalizadas.
- RN04: Em múltiplas perguntas, respeitar a ordem definida no Builder.

## 6. Jornada esperada

1. Atendimento é encerrado.
2. Sistema identifica pesquisa ativa vinculada ao evento.
3. Fluxo da pesquisa inicia automaticamente.
4. Cliente responde às perguntas.
5. Respostas são registradas.
6. Sessão é finalizada.

## 7. Templates e configurações padrão

### NPS (0–10)

- Pergunta (editável): “De 0 a 10, quanto você recomendaria nosso atendimento?”
- Descrição da escala (fixa): “0 = nada provável, 10 = extremamente provável”.
- Respostas (oculta): escala de 0 a 10.
- Feedback aberto (ativo por padrão para 0–6; editável): “O que te levou a dar essa nota?”
- Agradecimento (editável): “Obrigado por responder nossa pesquisa!”
- Adicionar pesquisa: Apenas template NPS por instância adicionada.

### CSAT (1–5)

- Pergunta (editável): “Qual o seu nível de satisfação com o nosso atendimento?”
- Respostas (editável, visível): Muito insatisfeito, Insatisfeito, Neutro, Satisfeito, Muito satisfeito.
- Feedback aberto (ativo por padrão para respostas 1–3; editável): “O que podemos melhorar?”
- Agradecimento (editável): “Obrigado por responder nossa pesquisa!”
- Adicionar pesquisa: Apenas template CSAT por instância adicionada.

### Pergunta Aberta

- Pergunta (editável): “Gostaria de deixar algum comentário sobre o atendimento?”
- Resposta: campo de texto livre.
- Feedback: não aplicável (a resposta já é aberta).
- Agradecimento (editável): “Obrigado pelo seu feedback!”
- Adicionar pesquisa: Apenas template Pergunta Aberta por instância adicionada.

**Regras gerais entre templates**

O envio do feedback aberto é condicionado à resposta anterior quando aplicável (ex.: detratores NPS ou insatisfeitos CSAT). Todas as perguntas e mensagens são editáveis, exceto a estrutura da escala no NPS (0–10).

## 8. Criar pesquisa personalizada

Monte pesquisas a partir dos templates NPS, CSAT e Pergunta Aberta, podendo adicionar o mesmo template várias vezes e combinar entre si (ex.: CSAT + NPS + Pergunta Aberta).

### Estrutura da criação

- Ao clicar em “Criar pesquisa”, abre-se um drawer lateral à direita com:

• Nome da Pesquisa (obrigatório, sem espaços; usar underscore).
• Descrição (opcional).

### Regras de composição

- Obrigatório conter ao menos 1 template principal.
- Permite múltiplas perguntas por pesquisa.
- Permite definir obrigatoriedade por pergunta.
- Permite configurar feedback condicional por pergunta quando aplicável.

## 9. Configurações do fluxo no Builder

### Gatilhos

- Evento suportado: Encerramento do atendimento.
- RN01 reforçada: apenas uma pesquisa ativa por gatilho e por canal (regra em breve)

### Status e versionamento

- Estados: Ativo/Inativo; apenas versões publicadas podem ser ativadas.
- Versionamento do fluxo permitindo, publicação e histórico.

### Inatividade e sessão

- Tempo de inatividade parametrizável (minutos, horas, dias).
- Ao exceder o tempo configurado, o fluxo direciona para “Encerrar sessão” (RF14).

### Validação de respostas

- Definição de limite de respostas incorretas (RF12).
- Mensagem de orientação com sugestões válidas quando houver erro (RF13).

### Controle por tipo de agente

- Filtrar e condicionar o envio por Bot, Agente e Supervisor.

## 10. Vinculo do agente de Pesquisa ao Grupo de Atendimento

Após salvar e publicar o agente, ele precisa ser vinculado ao grupo de atendimento no campo **Agente de finalização**

![Imagem 2: Após salvar e publicar o agente, ele precisa ser vinculado ao grupo de atendimento no campo Agente de finalização](https://ajuda.sankhya.com.br/hc/article_attachments/42639761594775)

**Lembrete**

Agentes de Pesquisa devem ser vinculados em **Agente de finalização**. Se o cliente for single-tenant, aparecerão as duas opções: **Agente de finalização** e **Selecione uma pesquisa de satisfação**. Deve ser selecionado o **Agente de finalização**.

## 11. Exemplo de uso (cenário prático)

1. Você publica um “Agente de Pesquisa” com feedback ativo (selecione as repostas que ativa o
   feedback).
2. Insere no fluxo de inicialização o componente redirecionar
   **Tipo de redirecionamento: Pesquisa de satisfação**
3. Vincula o agente ao grupo.
4. Ao encerrar um atendimento, o gatilho dispara a pesquisa automaticamente.
5. O cliente responde,
6. Se resposta igual a selecionada no feedback o agente envia: “O que te levou a dar essa nota?”, se não, passa para o próximo passo.
7. As respostas são salvas no registro do atendimento.
8. O fluxo envia mensagem de agradecimento e finaliza a sessão.

**Lembrete**

No fluxo do agente de inicialização deve ter o componente redirecionar:
**Tipo de redirecionamento: Pesquisa de satisfação**

![Imagem 3: No fluxo do agente de inicialização deve ter o componente redirecionar: Tipo de redirecionamento: Pesquisa de satisfação](https://ajuda.sankhya.com.br/hc/article_attachments/42639727860119)

## 12. Boas práticas

- Ative feedback aberto apenas onde gere insight acionável.
- Evite perguntas redundantes entre NPS e CSAT para reduzir abandono.
- Defina inatividade compatível com o canal (ex.: prazos menores em chat síncrono).
- Use preview (RF10) para validar experiência antes de publicar.

## 13. Perguntas frequentes (FAQ)

Não. A regra RN01 permite apenas uma pesquisa ativa por gatilho de encerramento por canal. Use versionamento para alternar entre variações.

O atendimento é encerrado normalmente (RN02). Se ultrapassar o tempo de inatividade configurado, o fluxo segue para encerrar sessão (RF14).

Não. A pesquisa não reabre sessões já finalizadas (RN03).

Não. Deve seguir a normalização com underscore (RF09), por exemplo: pesquisa\_pos\_atendimento.

- <https://kale-search-48771074.figma.site/%5D>

---

**Pronto para começar**

Abra o Builder, crie um novo fluxo na categoria **Pesquisa**, selecione seu template inicial (NPS, CSAT ou Aberta), ajuste perguntas/feedback/inatividade, configure o gatilho de encerramento, publique e ative.
