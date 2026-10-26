---
id: "42430126738839"
titulo: "Central de Campanhas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430126738839-Central-de-Campanhas"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T17:13:37Z"
rotulos: ["sync_hc", "neppo", "neppo_394887173", "sync_hash_b0e64a569dc6"]
---

# Central de Campanhas

A **Central de Campanhas** é uma dashboard de gerenciamento que permite ao usuário visualizar, monitorar e criar campanhas de comunicação multicanal (WhatsApp, Email, etc.) em um único lugar. A tela fornece métricas rápidas de desempenho (KPIs) e uma listagem detalhada das execuções.

Inicialmente esta tela esta configurada para canais de WhatsApp e E-mail, apenas

Índice:

[Etapa 1 - Canal](https://sankhya.zendesk.com/hc/pt-br/articles/42430098826007)

[Etapa 2 - Configurações](https://sankhya.zendesk.com/hc/pt-br/articles/42430130137879)

[Etapa 3 - Destinatários](https://sankhya.zendesk.com/hc/pt-br/articles/42430179886231)

[Etapa 4 - Conteúdo](https://sankhya.zendesk.com/hc/pt-br/articles/42430224406551)

[Etapa 5 - Enviar](https://sankhya.zendesk.com/hc/pt-br/articles/42430193034647)

![Imagem 1: Etapa 5 - Enviar](https://ajuda.sankhya.com.br/hc/article_attachments/42639444596119)

## 1. Visão geral

A **Central de Campanhas** é a tela responsável por **centralizar a gestão, acompanhamento e auditoria** de campanhas de envio multicanal. Ela permite ao usuário:

- Obter uma visão consolidada de volume e saúde dos envios (KPIs);
- Localizar campanhas por busca e filtros;
- Acompanhar status, performance e responsáveis;
- Acessar ações operacionais por campanha (via menu de ações).

---

## 2. Objetivo da tela

Garantir **controle operacional e visibilidade executiva** sobre campanhas, reduzindo tempo para:

- Identificar falhas e campanhas com baixa entrega/leitura;
- Localizar rapidamente uma campanha específica (nome, grupo ou template);
- Auditar execução (responsável, data/hora, destinatários e resultados);
- Criar novas campanhas com menor fricção.

---

## 3. Estrutura e componentes

### 3.1 Cabeçalho da página

- **Título:** Central de Campanhas
- **Subtítulo:** Gerencie todas as suas campanhas multicanal em um só lugar
- **Ação “Atualizar” (ícone):** Recarrega os indicadores e a listagem conforme filtros vigentes.
- **Botão primário “Nova Campanha”:** Direciona para o fluxo de criação de campanha.

---

### 3.2 Indicadores (KPIs)

Os indicadores fornecem uma leitura imediata do comportamento das campanhas no contexto atual (considerando filtros e aba selecionada).

![Imagem 2: Os indicadores fornecem uma leitura imediata do comportamento das campanhas no contexto atual (considerando filtros e…](https://ajuda.sankhya.com.br/hc/article_attachments/42639504885783)

1. **Total de mensagens**
   Exibe o volume total de mensagens processadas.
2. **Taxa de sucesso**
   Exibe o percentual de mensagens entregues com sucesso.
   Abaixo do percentual, exibe o total absoluto de entregas (ex.: “X entregues”).
3. **Envios ativos**
   Quantidade de campanhas com envio em andamento no momento.
4. **Falhas**
   Quantidade de mensagens com erro de entrega.
5. **Agendados**
   Quantidade de campanhas programadas para execução futura.

**Requisito:** KPIs devem refletir o mesmo recorte aplicado à tabela (aba + busca + filtros).

---

### 3.3 Busca e filtros

A área de refinamento permite segmentar e localizar campanhas de forma rápida.

![Imagem 3: A área de refinamento permite segmentar e localizar campanhas de forma rápida.](https://ajuda.sankhya.com.br/hc/article_attachments/42639475697175)

- **Campo de busca:** “Buscar por nome, grupo ou template…”
  Deve pesquisar por:

  - Nome da campanha
  - Nome/identificador do grupo
  - Nome do template
- **Filtro de Canal:** padrão “Todos os Canais”
  Exemplo de canais visíveis na tela: WhatsApp e Email.

![Imagem 4: Filtro de Canal: padrão “Todos os Canais” Exemplo de canais visíveis na tela: WhatsApp e Email.](https://ajuda.sankhya.com.br/hc/article_attachments/42639445127063)

- **Filtro de Status:** padrão “Todos status”
  Exemplos observados: Ativo, Agendado, Concluído.

![Imagem 5: Filtro de Status: padrão “Todos status” Exemplos observados: Ativo, Agendado, Concluído.](https://ajuda.sankhya.com.br/hc/article_attachments/42639505336855)

| **Status** | **Indicador Visual (Badge)** | **Definição Funcional** | **Comportamento Esperado** |
| --- | --- | --- | --- |
| **Ativo** | **Verde** | A campanha está vigente e habilitada. | **Para Recorrentes:** A automação está ligada e aguardando o próximo gatilho de disparo.    **Para Padrão:** A campanha foi criada e está pronta para processamento. |
| **Agendado** | **Azul** | O envio está programado para uma data/hora futura. | O sistema aguarda o timestamp definido para iniciar o processo de envio automaticamente. Nenhuma mensagem é enviada antes desse horário. |
| **Executando** | **Amarelo** | O processamento das mensagens está acontecendo neste momento. | O sistema está iterando pela lista de contatos e despachando as mensagens. As métricas de "Envios Ativos" no dashboard são incrementadas. |
| **Concluído** | **Verde** | Todo o fluxo da campanha foi finalizado. | **Para Recorrentes:** O período de recorrência terminou.    **Para Padrão:** Todas as mensagens da lista foram processadas (entregues ou falhadas). |
| **Pausado** | **Amarelo** | A campanha foi interrompida temporariamente pelo usuário. | O sistema suspende novos disparos até que o status seja alterado manualmente para "Ativo" novamente. |
| **Falhou** | **Vermelho** | Ocorreu um erro crítico que impediu a continuidade da campanha. |  |

---

### 3.4 Segmentação por tipo de envio

A tela apresenta duas categorias de campanha:

- **Envios padrão**

  - ![Imagem 6: Envios padrão](https://ajuda.sankhya.com.br/hc/article_attachments/42639490380439)
- **Envios recorrentes**

  - ![Imagem 7: Envios recorrentes](https://ajuda.sankhya.com.br/hc/article_attachments/42639463085335)
  - Execuções de recorrentes

    ![Imagem 8: Execuções de recorrentes](https://ajuda.sankhya.com.br/hc/article_attachments/42639459405719)
  - ![Imagem 9: Execuções de recorrentes](https://ajuda.sankhya.com.br/hc/article_attachments/42639463595799)

**Finalidade:** separar campanhas de disparo “pontual” (padrão) das campanhas com execução recorrente (recorrentes), mantendo consistência de visualização e operação.

---

## 4. Listagem de campanhas (tabela)

A tabela é o núcleo operacional da tela. Ela apresenta campanhas com os principais atributos para acompanhamento e auditoria.

### 4.1 Colunas e significado

- **Nome da Campanha:** Identificador principal da campanha.
- **Canal:** Canal de envio (ex.: WhatsApp, Email).
- **Grupo:** Agrupamento/conta/provedor associado ao envio (ex.: “360dialogv3”, “gsuite”).
- **Status:** Situação da campanha (ex.: Ativo, Agendado, Concluído).
- **Tipo:** Indica se o envio é **Imediato** ou **Agendado**.
- **Template:** Template utilizado.

  - ![Imagem 10: Template: Template utilizado.](https://ajuda.sankhya.com.br/hc/article_attachments/42639491283863)
- **Destinatários:** Total de contatos incluídos na campanha.

  - ![Imagem 11: Destinatários: Total de contatos incluídos na campanha.](https://ajuda.sankhya.com.br/hc/article_attachments/42639491548695)
- **Performance:** Indicadores por campanha:

  - ![Imagem 12: Performance: Indicadores por campanha:](https://ajuda.sankhya.com.br/hc/article_attachments/42639464379799)
  - **Entregue (%)** com barra de progresso
  - **Lida (%)** quando suportado pelo canal
- **Data/Hora:** Registro do momento de execução ou agendamento.
- **Responsável:** Usuário que executou/configurou a campanha (ou atribuição em grupo).
- **Ações:** Menu de contexto (⋮) para operações.

---

## 5. Ações por campanha

Cada linha apresenta um menu de ações (⋮) destinado a operações relacionadas à campanha.

**Recomendação de governança (regra de negócio):**

- O conjunto de ações disponíveis.

  - Ex.: campanhas concluídas não devem permitir edição, apenas visualização.
  - Ex.: campanhas agendadas podem permitir editar/cancelar.
  - Ex.: campanhas ativas podem permitir acompanhar/pausar (se aplicável).

---

## 6. Paginação

A listagem possui paginação com:

- **Seletor de linhas por página**
- **Indicador de intervalo exibido** (ex.: 1–10 de 76)
- **Navegação** entre páginas

---

## 7. Estados da interface (obrigatórios)

Para garantir previsibilidade e robustez, a tela deve suportar:

- **Carregamento:** skeleton/placeholder em KPIs e tabela.
- **Sem resultados (filtros/busca):** mensagem orientativa e opção de limpar filtros.
- **Vazio (sem campanhas criadas):** mensagem e CTA para “Nova Campanha”.
- **Erro de carregamento:** feedback claro e ação de “Tentar novamente”.
- **Sem permissão:** esconder/neutralizar CTAs e ações restritas, com orientação adequada.
