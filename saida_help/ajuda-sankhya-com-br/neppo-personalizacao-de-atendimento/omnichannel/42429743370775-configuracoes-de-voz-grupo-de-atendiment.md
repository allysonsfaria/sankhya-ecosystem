---
id: "42429743370775"
titulo: "Configurações de voz (grupo de atendimento)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429743370775-Configura%C3%A7%C3%B5es-de-voz-grupo-de-atendimento"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T15:53:17Z"
rotulos: ["sync_hc", "neppo", "neppo_291176467", "sync_hash_40249f053776"]
---

# Configurações de voz (grupo de atendimento)

Este manual detalha as configurações avançadas para o canal de **Voz** na plataforma Neppo, focando na criação e personalização de filas de atendimento telefônico. O objetivo é permitir a construção de uma central de atendimento inteligente e totalmente customizada, definindo exatamente como as chamadas de voz são recebidas, distribuídas e gerenciadas pela equipe.

## CONFIGURAÇÕES DE VOZ (GRUPO DE ATENDIMENTO)

### INFORMAÇÕES GERAIS

**Nome da fila:** Nome da fila para identificação na busca e Dashboard

**Ramal\*:** Número de ramal da fila (para discagem direta e redirecionamentos)

**Selecione a música de espera:** Música de espera ou anúncio de espera tocado quando o cliente entrar na fila

**Prefixo do nome do discador:** Prefixo usado para identificar o cliente

**Descrição:** Descrição da fila

**Gravar\*:** Habilitar/desabilitar a gravação da chamada na fila

![Imagem 1: Gravar*: Habilitar/desabilitar a gravação da chamada na fila](https://ajuda.sankhya.com.br/hc/article_attachments/42637391568023)

### CONFIGURAÇÕES DE CHAMADA

**Estratégia de toque da fila\*:** Estratégia para distribuição das chamadas pelo PABX. Opções disponíveis:

- **Agente com Menor Tempo de Conversa:** O agente que tocará é aquele que teve o menor tempo de conversa.
- **Agente com Menos Chamadas:** O agente que tocará é aquele que teve menos chamadas.
- **Agente com Maior Ociosidade:** O agente que tocará é aquele que ficou ocioso por mais tempo, dependendo do seu nível de categoria.
- **Tocar Todos:** Todos os agentes tocam simultaneamente.
- **Aleatório:** Os agentes tocarão aleatoriamente, sem uma ordem específica.
- **Tocar Progressivamente:** Os agentes tocarão da mesma forma que de cima para baixo e progredirão até que cada agente termine tocando.
- **Round Robin:** Tocará o próximo agente disponível na fila.
- **Sequencialmente por Ordem do Agente:** Os agentes tocarão em sequência de acordo com a categoria e a ordem das categorias.
- **De Cima para Baixo:** O agente tocará em ordem, começando pelo número um.

**Aplicar regra de nível\***: Para separar a prioridade de cada agente no atendimento das ligações por grupo.

**Regra de segundo nível de espera\*:** Tempo de espera até enviar o atendimento para outro nível (grupo), caso habilitado.

**Regra de nível sem agente, sem espera:** Se habilitado, não haverá tempo de espera até o próximo grupo, caso os agentes do grupo mais prioritário não estiverem disponíveis.

**Regra de espera multiplicado pelo nível:**

- **Sim:** A quantidade de segundos que o cliente espera até a próxima categoria. Esse valor aumentará (multiplicará) se a opção Nível de Multiplicação de Espera da Regra de Categoria estiver marcada como verdadeira.
- **Não:** Se a opção Nível de Multiplicação de Espera da Regra de Categoria estiver marcada como falsa, então, após a passagem da quantidade definida de segundos, as categorias serão executadas em ordem, sem espera.

**Ação de tempo limite:** Qual será a ação após o tempo limite definido para a fila.

**Descartar abandonado após\*:** Descartar como ligação abandonada, caso seja passado esse tempo definido sem segundos sem atendimento.

**Permitido Retorno de Abandonadas:**

- **Sim :** A configuração está habilitada. Permite que uma chamada retome sua posição na fila, mas apenas no número de segundos definido em "descartar abandonado após".
- **Não :** A configuração está desabilitada.

**Tempo máximo de espera\*:** Tempo limite de espera definido para esta fila.

**Tempo máximo de espera sem agente\*:** Tempo limite de espera definido para esta fila caso os agentes estejam offline. Padrão é 0 para desativado. O valor está em segundos e definirá o tempo que a fila deve ficar vazia (sem agentes conectados, em chamada ou não) antes de desconectar todos os membros. Esse princípio protege contra desconectar todos os membros que estão aguardando se todos os agentes saírem acidentalmente.

**Tempo máximo de espera sem tempo de agente localizado\*:** Tempo limite de espera definido para esta fila caso os agentes estejam offline. Padrão é 5. Qualquer valor está em segundos e definirá o período de tempo após o max-wait-time-with-no-agent ser atingido para rejeitar novos chamadores. Isso permite que clientes sejam desconectados se nenhum agente estiver conectado por mais de 5 segundos, mas novos chamadores após esses 5 segundos podem ter um limite inferior.

![Imagem 2: Tempo máximo de espera sem tempo de agente localizado*: Tempo limite de espera definido para esta fila caso os agentes…](https://ajuda.sankhya.com.br/hc/article_attachments/42637391763863)

### MENSAGENS E SAUDAÇÕES

**Selecione a saudação da fila:** Música ou áudio tocado na entrada da fila.

**Som de Anúncio:** áudio de anúncio tocado na fila.

**Frequência de Anúncio (Segundos):** De quantos em quantos segundos o áudio de anúncio será tocado na fila.

![Imagem 3: Frequência de Anúncio (Segundos): De quantos em quantos segundos o áudio de anúncio será tocado na fila.](https://ajuda.sankhya.com.br/hc/article_attachments/42637331285911)

### CONFIGURAÇÕES AVANÇADAS

**Pontuação com base de tempo\***:

- **Fila -** O tempo para priorização do cliente começa a contar quando ele entra na fila;
- **Sistema -** O tempo para priorização do cliente começa a contar quando ele entrou no PABX a primeira vez, independente das transferências;

**Pontuação com base no tempo em segundos:** O tempo em segundos será adicionado na pontuação atual do cliente (baseado em fila ou sistema) de forma a priorizar artificialmente sua posição no atendimento. É usado para priorizar uma fila em relação a outras.

**Tecla de Saída:** Tecla usada para sair da fila.

![Imagem 4: Tecla de Saída: Tecla usada para sair da fila.](https://ajuda.sankhya.com.br/hc/article_attachments/42637374879639)

### AGENTE

**Nível:** Nível do agente dentro do grupo, o qual define a ordem em que ele será escolhido dentro do grupo/nível para receber o atendimento.

![Imagem 5: Nível: Nível do agente dentro do grupo, o qual define a ordem em que ele será escolhido dentro do grupo/nível para…](https://ajuda.sankhya.com.br/hc/article_attachments/42637348355351)
