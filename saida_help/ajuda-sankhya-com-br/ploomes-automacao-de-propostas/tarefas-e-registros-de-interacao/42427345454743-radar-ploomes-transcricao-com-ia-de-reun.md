---
id: "42427345454743"
titulo: "Radar Ploomes | Transcrição com IA de reuniões online"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427345454743-Radar-Ploomes-Transcri%C3%A7%C3%A3o-com-IA-de-reuni%C3%B5es-online"
trilha: "PLOOMES: Automação de propostas  > Tarefas e registros de interação"
atualizado_em: "2026-08-10T18:00:06Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14458798", "sync_hash_84f95b6a33c8"]
---

# Radar Ploomes | Transcrição com IA de reuniões online

## 1) Sobre o Transcrição com IA de reuniões online

A **Transcrição com IA de reuniões online** é uma funcionalidade do Ploomes que transcreve e resume automaticamente suas reuniões realizadas por videoconferência. Ao final de cada reunião, o sistema gera uma transcrição completa em texto e um resumo inteligente com base em instruções personalizáveis, tudo vinculado diretamente ao histórico do cliente, negócio ou tarefa dentro do CRM. O objetivo da funcionalidade é exclusivamente **a transcrição e o resumo**: nenhum arquivo de áudio ou vídeo da reunião fica disponível para o usuário.

Com essa funcionalidade, sua equipe elimina a necessidade de anotações manuais durante as reuniões e garante que informações importantes (como compromissos, valores discutidos e próximos passos) fiquem registradas automaticamente no Ploomes, disponíveis para consulta a qualquer momento. Você receberá apenas os textos prontos (transcrição e resumo), nunca a gravação da reunião.

A funcionalidade opera em dois modos:

- **Entrada automática via tarefa:** O bot identifica automaticamente os links de reunião nas tarefas do Ploomes e solicita entrada na sala **2 minutos antes do início**, sem necessidade de ação manual. Este é o fluxo principal da funcionalidade.
- **Acionamento manual:** O usuário cola o link de uma reunião diretamente no Ploomes, ideal para reuniões externas ou não planejadas.

  - Por exemplo: quando você recebe um link de videoconferência via WhatsApp e deseja que aquela conversa também seja transcrita e registrada no CRM.

---

## 2) Pré-requisitos

- Possuir o módulo **Transcrição com IA de reuniões online** contratado e habilitado na conta Ploomes.
- Ter a **permissão de uso da funcionalidade de IA** atribuída ao seu usuário por um administrador.
- Realizar as reuniões no idioma **Português** (único idioma suportado nesta versão).
- Utilizar uma das plataformas de videoconferência suportadas: **Google Meet** ou **Microsoft Teams**.

---

## 3) Configurando o Transcrição com IA de reuniões online

A configuração do módulo é realizada pelo **administrador da conta** e envolve quatro etapas principais: habilitação do módulo, definição de permissões, cadastro de Modelos de Resumo e definição do Prompt Padrão.

---

## 3.1) Habilitando o módulo

Para ativar a funcionalidade de transcrição com IA na sua conta:

1. Acesse a **Administração da conta**.
2. Navegue até o menu **Módulos do Sistema**.
3. Localize o módulo **Transcrição com IA de reuniões online** e habilite-o.
4. Ative a transcrição de reuniões.

![Imagem 1: Ative a transcrição de reuniões.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240387689/aa9a9c1d843447c758662c8700d2/image.png?expires=1786536000&signature=fb513af2751e2aa12325d5cb55e09c5cccd9e472f3cd1950957ff3972763d6ba&req=diIjFsp2modXUPMW3nq%2BgURiVpwIZbfahwK6VxFF6H22pHqudkQsdqFqCNP6%0Ai4GrLKyFOmaRwNHSFdb0rRSa704%3D%0A)

Ao ativar a funcionalidade, as configurações específicas (permissões e prompts) ficam disponíveis para edição.

---

## 3.2) Configurando permissões de uso

Com a funcionalidade habilitada, o próximo passo é definir **quais usuários** terão acesso à funcionalidade:

1. Dentro das configurações do módulo, acesse a seção de **Permissões**.
2. Adicione os **usuários** que devem ter acesso à Transcrição com IA.

![Imagem 2: Adicione os usuários que devem ter acesso à Transcrição com IA.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240389666/aff58f18a037b94e4d05ccd63342/image.png?expires=1786536000&signature=ae7eead6717167dc1e8a8b9800e1dc54b4d134a0d0aab05af5c9f840805357d4&req=diIjFsp2lIdZX%2FMW3nq%2BgbTxOLc%2FuJ%2FPgubiOkAk%2BvruEJVHOcFPf7w6jk%2BL%0ASwMy%2F4d4BwmtPwX1Kb3vp6dMcVo%3D%0A)

A permissão funciona como um filtro de interface e de atuação:

- Usuários com permissão **visualizam** o botão de acionamento manual do bot, o checkbox de controle da IA dentro das tarefas e o campo de Modelo de Prompt nas tarefas.
- Usuários sem permissão **não visualizam e não interagem** com nenhum desses componentes.
- Para a **entrada automática**, o bot só solicitará ingresso em reuniões de tarefas onde **ao menos um** dos usuários incluídos na tarefa possua permissão ativa, garantindo a privacidade da equipe.

---

## 3.3) Gerenciando Modelos de Resumo

Os Modelos de Resumo são as instruções que orientam a IA sobre **como resumir** cada transcrição. O módulo já vem com um **Modelo padrão** pré-configurado, pronto para uso. O administrador pode editar as instruções desse modelo e também criar novos modelos para diferentes contextos de reunião.

**Editando o Modelo padrão:**

1. Dentro das configurações do módulo, acesse a seção de **Modelos de Resumo**.
2. Localize o **Modelo padrão** e clique no ícone de edição.
3. Ajuste as instruções do prompt conforme a necessidade da sua operação.
4. Salve as alterações.

![Imagem 3: Salve as alterações.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240407510/81bcee1407a148d29288017e86f7/image.png?expires=1786536000&signature=2e6d6bad078e2d965511802d605093787a160a0aa3079622cb1df4168730a499&req=diIjFs1%2BmoReWfMW3nq%2BgV4vfH%2BOONdmVffD6oV11v4bUArxj2NsKBWKab4k%0AuSyAtOs6FdTvbEAs%2BHiAcSbs9p0%3D%0A)

O Modelo padrão funciona como uma **rede de segurança**: ele será utilizado pela IA sempre que nenhum outro modelo for selecionado manualmente na tarefa e nenhuma regra de automação definir um modelo específico (é necessário ter o módulo de Workflow contratado para configurar automações). Dessa forma, mesmo que nenhuma escolha ativa seja feita, a IA sempre terá instruções para gerar o resumo.

**Criando novos modelos:**

1. Clique em **Novo Modelo**.
2. Preencha o **Título do Resumo** (nome que identifica o modelo) e o **Prompt do Resumo** (instruções detalhadas para a IA sobre como resumir a transcrição).
3. Salve o modelo.

![Imagem 4: Salve o modelo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240408420/fd00fbcafac57454b73aaf48a374/image.png?expires=1786536000&signature=64f88363f90818359d77e229ce469d2770187351eddbcb86415e9eefa9204188&req=diIjFs1%2BlYVdWfMW3nq%2BgQ3LrEVXtlzsHmeIs6Cd5G0pUK%2Ff9Z0HPj4N%2BtjU%0AyGsa5ajQ0xd3Zwy4ECxf%2F6lSTlk%3D%0A)

Você pode criar quantos modelos forem necessários, formando uma biblioteca de tipos de resumo para sua conta. Exemplos:

- **Resumo Comercial:** instruções para a IA focar em valores negociados, prazos e compromissos assumidos.
- **Resumo Técnico:** instruções para a IA focar em escopo, requisitos levantados e decisões técnicas.
- **Resumo de Implantação:** instruções para a IA focar em etapas de entrega, pendências e responsáveis.

Os títulos cadastrados aparecerão como opções selecionáveis no **campo de Modelo de Resumo dentro das tarefas**, permitindo que cada reunião utilize o modelo mais adequado ao seu contexto.

**Importante:** Como o Modelo de Resumo é um **campo de tarefa**, ele também pode ser preenchido automaticamente por meio de **Automações Genéricas de Tarefa (funcionalidade dentro do Módulo de Workflow)**. Isso significa que você pode criar regras para que o modelo seja escolhido automaticamente com base em critérios como responsável da tarefa, etapa do negócio ou qualquer outro gatilho disponível nas automações do Ploomes.

---

## 3.4) Seleção dinâmica de Modelos de Resumo via Automação

Para automatizar a escolha do Modelo de Resumo com base em regras de negócio, é necessário ter o Módulo de Workflow contratado. É possível utilizar as **Automações Genéricas de Tarefa** do Ploomes:

1. Acesse a configuração de **Automações Genéricas**.
2. Clique em automação de Tarefa.
3. Crie uma nova automação com os gatilhos e filtros desejados.
4. Na ação da automação, configure o preenchimento do campo **Modelo de Resumo** com o modelo desejado.

Essa configuração permite criar regras inteligentes para a escolha automática do resumo. Por exemplo:

- "Sempre que uma tarefa for de responsabilidade do usuário **Antonio**, selecionar automaticamente o modelo **Resumo de Implantação**."
- "Sempre que uma tarefa estiver vinculada a um negócio na etapa **Proposta Enviada**, selecionar o modelo **Resumo Comercial**."

Caso nenhuma automação seja disparada para uma determinada tarefa, o sistema utilizará o **Modelo padrão** configurado no módulo.

---

## 4) Utilizando o Transcrição com IA de reuniões online

## 4.1) Entrada automática via tarefa

Este é o fluxo principal da funcionalidade. O bot identifica automaticamente os links de reunião presentes na descrição das tarefas do Ploomes e solicita entrada na sala de forma autônoma, sem necessidade de ação manual por parte do usuário.

**Como funciona:**

O sistema monitora as tarefas dos usuários com permissão de IA. Quando uma tarefa contém um link do **Google Meet** ou **Microsoft Teams** na descrição, o bot solicita automaticamente a entrada na reunião **2 minutos antes do horário de início** agendado.

**Exemplo prático:** João é um usuário com permissão de IA configurada na administração. Toda tarefa em que João estiver incluído como participante terá o bot solicitando entrada automática na reunião vinculada. O bot lerá o link contido na descrição da tarefa e pedirá para ingressar na sala 2 minutos antes do início.

**Importante:**

- Para que o bot solicite entrada, basta que **ao menos um** dos usuários incluídos na tarefa possua permissão de IA ativa. Não é necessário que todos os participantes da tarefa tenham permissão.
- **Regra de unicidade:** Apenas **um bot por reunião** é permitido. Se tanto a entrada automática quanto o acionamento manual forem direcionados para o mesmo link, o sistema aceitará apenas a primeira solicitação que chegar.

**Controles disponíveis dentro da tarefa:**

Usuários com permissão de IA visualizam dois controles importantes dentro de cada tarefa:

- **Checkbox (botão de Transcrição Automática) de desabilitação do bot:** Permite desativar a entrada automática do bot para aquela tarefa específica. Por padrão, **o checkbox vem ativo** em toda tarefa criada (ou seja, o bot entrará automaticamente). Caso o usuário desative o checkbox, o bot não solicitará entrada naquela reunião.

  - **Atenção:** Embora apenas usuários com permissão de IA visualizem o checkbox de Transcrição automática, a escolha (ativo ou desativo) **vale para todos** os participantes da tarefa. Se João desativar o bot, ele ficará desativado para todos os envolvidos naquela tarefa — inclusive para Maria, que também possui permissão de IA.
- **Campo de Modelo de Prompt:** Permite alterar o tipo de resumo que será gerado para aquela reunião específica. O campo exibe os Modelos de Resumo cadastrados pelo administrador na configuração do módulo.

![Imagem 5: Campo de Modelo de Prompt: Permite alterar o tipo de resumo que será gerado para aquela reunião específica. O campo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240421103/9ce4872e65aec0430c12ded4baee/image.png?expires=1786536000&signature=77193c9c341a32cc4e6061b74ce3d50be7f7cedf07270a016393800bca79630a&req=diIjFs18nIBfWvMW3nq%2BgTCKqE0l9M96Au7DxTb1OzaKI1uRniktwZcT9Zg%2F%0AliThKdvHaCiLOTPIWXVty2x2v8I%3D%0A)

**Dica:** Por se tratar de um **campo de tarefa**, o Modelo de Prompt também pode ser preenchido automaticamente via **Automações Genéricas de Tarefa** (é necessário ter o módulo de Workflow contratado para configurar automações). Isso permite criar regras como: "Para todas as tarefas do responsável Antonio, selecionar automaticamente o modelo Resumo de Implantação." Caso nenhuma automação seja disparada e nenhuma escolha manual seja feita, o sistema utilizará o **Prompt Padrão** definido na configuração do módulo.

---

## 4.2) Acionamento manual

O acionamento manual é um fluxo complementar que permite enviar o bot de transcrição para reuniões que não foram agendadas como tarefas no Ploomes, como links recebidos via WhatsApp, e-mail ou outras fontes externas.

**Colando o link da reunião:**

1. Acesse a **tela de Tarefas** no Ploomes.
2. Clique no botão de **Transcrição IA disponível**.
3. No modal que será exibido, cole o **link da reunião** no campo indicado.

![Imagem 6: No modal que será exibido, cole o link da reunião no campo indicado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240430010/64571b2263c5de0da36ee8b5e9fa/image.png?expires=1786536000&signature=4ab2ed2a381405690a5a325885461d9a4532936d08a6dde7cc90fc9f1c9345aa&req=diIjFs19nYFeWfMW3nq%2BgbjBPFwjdcAvySFj3Gm73RQ6J7ADH4rWWBPeahQo%0A9t6cg9jhD%2BfiZG4mVGB2FsO21%2Fw%3D%0A)

O sistema validará automaticamente se o link pertence a uma das plataformas suportadas: **Google Meet** ou **Microsoft Teams**. Somente links identificados como pertencentes a essas plataformas permitirão o avanço no fluxo.

**Vinculando entidades (Cliente, Negócio e Tarefa):**

Após colar um link válido, o próximo passo é vincular a reunião às entidades corretas no CRM. Essa vinculação garante que a transcrição e o resumo sejam salvos no lugar certo do histórico.

![Imagem 7: Após colar um link válido, o próximo passo é vincular a reunião às entidades corretas no CRM. Essa vinculação garante…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240430803/cc307fda50f45b927f1a86846b68/image.png?expires=1786536000&signature=d1bad706e242af9b31a77322fd7e1dd0545c9240f3df41ab275da70574f36a99&req=diIjFs19nYlfWvMW3nq%2BgfwsNTT62%2BW7r8oX16levnmYqf0L1lGNN9tiNpPR%0AYmYk%2Fag6tyaWfrODAgpcy6PSCQU%3D%0A)

O sistema aplica regras de **preenchimento automático inteligente** para agilizar esse processo:

- **Ao selecionar um Negócio:** o campo **Cliente** é preenchido automaticamente com o proprietário (cliente) daquele negócio, caso o negócio tenha um cliente vinculado.
- **Ao selecionar uma Tarefa:** os campos **Cliente** e/ou **Negócio** são preenchidos automaticamente com as entidades vinculadas àquela tarefa, caso existam dentro da Tarefa.
- **Ao selecionar um Cliente:** as opções de **Negócios** e **Tarefas** são filtradas para exibir apenas os registros pertencentes ao cliente selecionado.

**Regra obrigatória:**

- Para enviar o bot à reunião, é necessário ter **no mínimo um Cliente ou Negócio ou Tarefa vinculados**.

**Enviando o bot:**

- Com o link validado e as entidades vinculadas corretamente, clique no botão para **enviar o bot** à reunião.

---

## 4.3) Participação do bot na reunião

Independentemente do modo de acionamento (automático ou manual), o bot **sempre solicita permissão** para ingressar na chamada. Conforme as diretrizes de conformidade (LGPD), um dos participantes da reunião deve aceitar a entrada.

**Atenção:** Caso a entrada do bot seja recusada por um participante, o sistema registrará automaticamente essa negativa nos registros de interação das entidades vinculadas (veja a seção Cenário de entrada negada mais adiante).

---

## 4.4) Encerramento da participação do bot

O bot encerra sua participação e inicia o processamento dos dados em duas situações:

- **Remoção manual:** um participante remove o bot da chamada.
- **Timeout de segurança:** o bot permanece sozinho na sala por mais de **10 minutos** sem nenhum outro participante.

O timeout de segurança existe para evitar gravações infinitas de salas vazias — caso todos os participantes saiam da reunião e esqueçam do bot, ele se desconectará automaticamente.

---

## 4.5) Processamento e geração de conteúdo

Após o encerramento da participação, o sistema executa automaticamente o seguinte fluxo de processamento:

1. **Transcrição:** o áudio é convertido em texto, gerando a transcrição completa da reunião.
2. **Resumo:** a IA processa a transcrição utilizando as instruções do **Modelo de Prompt** configurado e gera o resumo da reunião.

Todo o processamento é realizado no idioma Português de forma fixa. O sistema não tenta detectar ou interpretar outros idiomas.

**Nota:** O arquivo de áudio **não fica disponível** para o usuário final. Você receberá apenas a transcrição textual e o resumo gerado pela IA.

## 4.6) Destino dos dados gerados

O local onde a transcrição e o resumo são salvos depende de como a reunião foi vinculada:

**Com Tarefa vinculada com cliente e/ou negócio vinculado:**

Quando há uma tarefa vinculada (seja pela entrada automática ou pelo acionamento manual) com cliente e/ou negócio, o sistema:

- **Finaliza automaticamente** a tarefa vinculada.
- Alimenta o **Registro de Interação de Finalização de Tarefa** (comportamento padrão do Ploomes) do negócio ou cliente com o **resumo na descrição** e a **transcrição em anexo**.
- Inclui um **indicativo visual** (label/tag **"Registro automático"**) no registro, sinalizando que o conteúdo foi gerado automaticamente.

![Imagem 8: Inclui um indicativo visual (label/tag "Registro automático" ) no registro, sinalizando que o conteúdo foi gerado…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2240437363/5beab038a75579c2215c378b5136/image.png?expires=1786536000&signature=98f6f610dd9046b775437381bd9ae3131450781d6960b617777fef1079415e84&req=diIjFs19moJZWvMW3nq%2BgSqnODM%2BM6fPaxthNychcr2nPDoAUBFlfbovavgp%0A95C0fySofWMsSUdPEWR0PE4Fkeg%3D%0A)

**Com Tarefa vinculada sem cliente e sem negócio vinculado:**

Quando não há cliente e negócio vinculado a uma tarefa, o sistema:

- Salva o resumo e a transcrição como anexos da tarefa

**Sem Tarefa vinculada (apenas Cliente e/ou Negócio — somente via acionamento manual):**

Quando não há tarefa vinculada, o sistema:

- Cria um **novo Registro de Interação** no histórico das entidades vinculadas (Cliente e/ou Negócio).
- Insere o **resumo na descrição** e a **transcrição em anexo**.
- Inclui o **indicativo visual "Registro automático"** no registro.

---

## 4.7) Cenário de entrada negada

Caso o bot tenha sua entrada recusada na reunião por um dos participantes e haja **Cliente ou Negócio vinculado**, o sistema:

- Cria automaticamente um **Registro de Interação** no histórico das entidades vinculadas.
- O corpo do registro conterá a mensagem informativa: **"O bot de transcrição com IA não teve sua entrada permitida na reunião."**
- O registro também recebe o indicativo **"Registro automático"**.

Esse comportamento garante que a recusa não seja um evento silencioso — sua equipe terá visibilidade clara no CRM de que o bot tentou participar da reunião, mas foi impedido por uma ação humana.

---

## 5) Limitações do Transcrição com IA de reuniões online

- O sistema opera **exclusivamente no idioma Português**. Reuniões realizadas em outros idiomas não terão transcrição e resumo adequados.
- **Não há detecção automática de idioma** — todo o áudio é processado partindo da premissa de que a fala é em português.
- **O player de áudio ou vídeo da reunião não fica disponível** para o usuário final. Apenas a transcrição textual e o resumo são entregues.
- As plataformas suportadas nesta versão são exclusivamente **Google Meet** e **Microsoft Teams**.
- Apenas **um bot por reunião** é permitido — se a entrada automática e o acionamento manual forem direcionados ao mesmo link, o sistema aceita apenas a primeira solicitação.
- O checkbox de desabilitação do bot na tarefa é **compartilhado** entre todos os participantes: se um usuário desativar, a desativação vale para todos na tarefa.

---

## 6) F.A.Q.

1. **O bot entra automaticamente em todas as minhas reuniões?**

   1. O bot entra automaticamente apenas nas reuniões vinculadas a **tarefas do Ploomes** em que você esteja incluído como participante, desde que você possua permissão de IA ativa e o checkbox do bot esteja habilitado na tarefa. Reuniões fora do Ploomes (links recebidos por WhatsApp, por exemplo) precisam ser registradas via acionamento manual.
2. **Quando exatamente o bot solicita entrada na reunião?**

   1. Na entrada automática via tarefa, o bot solicita entrada **2 minutos antes do horário de início** agendado na tarefa. No acionamento manual, a solicitação acontece logo após o envio.
3. **O que acontece se ninguém selecionar um Modelo de Resumo na tarefa?**

   1. O sistema utilizará automaticamente o **Modelo padrão** que já vem pré-configurado no módulo. Dessa forma, a IA sempre terá instruções para gerar o resumo, mesmo que nenhuma escolha manual ou automação tenha sido aplicada (é necessário ter o módulo de Workflow contratado para configurar automações).
4. **Posso automatizar a escolha do Modelo de Resumo?**

   1. Sim. Como o Modelo de Resumo é um **campo de tarefa**, ele pode ser preenchido automaticamente por meio de **Automações Genéricas de Tarefa** (é necessário ter o módulo de Workflow contratado para configurar automações). Você pode criar regras baseadas em qualquer gatilho disponível nas automações do Ploomes, como responsável da tarefa, etapa do negócio vinculado, entre outros.
5. **Posso utilizar a Transcrição com IA em reuniões realizadas em inglês ou espanhol?**

   1. Não. Nesta versão, a funcionalidade opera exclusivamente no idioma **Português**. O sistema não realiza detecção automática de idioma e processará todo o áudio partindo da premissa de que a fala é em português.
6. **Por que o bot não entrou na minha reunião?**

   1. Existem algumas possibilidades:

      1. Um participante da reunião **recusou a entrada** do bot na sala. Nesse caso, verifique o histórico da entidade vinculada — haverá um registro informando a recusa.
      2. O **checkbox do bot** pode ter sido desativado na tarefa por outro participante.
      3. Você pode não ter **permissão de uso** da funcionalidade de IA atribuída pelo administrador.
      4. O link presente na descrição da tarefa pode não pertencer a uma **plataforma suportada** (Google Meet ou Microsoft Teams).
      5. Já pode haver **outro bot ativo da Ploomes** naquela reunião (apenas um bot por reunião é permitido).
7. **Se eu desabilitar o bot em uma tarefa, isso afeta os outros participantes?**

   1. Sim. O checkbox de desabilitação é **compartilhado**. Se você desativar o bot em uma tarefa, ele ficará desativado para todos os participantes daquela tarefa, mesmo que outros usuários também possuam permissão de IA.
8. **O bot grava áudio ou vídeo acessível para mim?**

   1. Não. O usuário final recebe apenas a **transcrição textual** e o **resumo** gerados pela IA.
9. **Se eu vincular uma Tarefa ao acionar o bot manualmente, a tarefa será finalizada?**

   1. Sim. Quando há uma tarefa vinculada, o sistema **finaliza automaticamente** essa tarefa ao concluir o processamento e utiliza o Registro de Interação de Finalização de Tarefa para armazenar o resumo e a transcrição.
10. **Como sei que um Registro de Interação foi gerado pela IA?**

    1. Todo registro criado pela funcionalidade (seja de finalização de tarefa, novo registro ou registro de entrada negada) contém o indicativo visual **"Registro automático"**, facilitando a identificação da origem do conteúdo.
11. **O que acontece se o bot ficar sozinho na reunião?**

    1. Se todos os participantes saírem e o bot permanecer sozinho na sala por mais de **10 minutos**, ele encerrará automaticamente sua participação e iniciará o processamento dos dados capturados até aquele momento.
12. **Posso criar mais de um Modelo de Resumo?**

    1. Sim. Além do Modelo padrão que já vem pré-configurado, você pode criar quantos modelos forem necessários, formando uma biblioteca de tipos de resumo adaptados a diferentes contextos (comercial, técnico, implantação, etc.).

---

## Glossário

1. **Registro de Interação:** Entrada no histórico de um Cliente ou Negócio dentro do Ploomes, que documenta atividades, contatos e eventos relevantes. A Transcrição com IA utiliza registros de interação para armazenar os resumos e transcrições gerados.
2. **Modelo de Resumo:** Conjunto de instruções (título + prompt) que orienta a IA sobre como resumir uma transcrição. O módulo já vem com um Modelo padrão pré-configurado, e o administrador pode editá-lo ou criar novos modelos para diferentes contextos de reunião. Dentro das tarefas, aparece como um campo selecionável e configurável via automação.
3. **Modelo padrão:** Modelo de Resumo que já vem pré-configurado no módulo. É utilizado automaticamente pela IA quando nenhum outro modelo é selecionado manualmente ou via automação. O administrador pode editar suas instruções a qualquer momento.
4. **Entidade:** Elemento central do CRM ao qual os dados são vinculados. No contexto desta funcionalidade, as entidades são: **Cliente**, **Negócio** e **Tarefa**.
5. **Automação Genérica de Tarefa:** Recurso do módulo workflow que permite criar regras automáticas baseadas em gatilhos e filtros para executar ações em tarefas, como selecionar automaticamente um Modelo de Resumo.
6. **Bot de Transcrição:** Participante virtual que entra na reunião para capturar o áudio. Ele solicita permissão de entrada (conforme LGPD) e, ao final, processa a gravação para gerar a transcrição e o resumo.
7. **Checkbox de desabilitação do bot:** Controle presente dentro de cada tarefa que permite desativar a entrada automática do bot para aquela reunião específica. Visível apenas para usuários com permissão de IA, mas com efeito compartilhado entre todos os participantes da tarefa. Vem ativo por padrão.
8. **Timeout de segurança:** Mecanismo que encerra automaticamente a participação do bot após 10 minutos sozinho na sala, evitando gravações de reuniões vazias.
9. **Badge "Registro automático":** Indicativo visual presente nos Registros de Interação gerados pela funcionalidade, sinalizando que o conteúdo foi criado automaticamente pela inteligência artificial.
