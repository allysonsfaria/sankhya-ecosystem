---
id: "42427362070935"
titulo: "Integrador em Branco: criando e gerenciando integrações personalizadas no Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427362070935-Integrador-em-Branco-criando-e-gerenciando-integra%C3%A7%C3%B5es-personalizadas-no-Ploomes"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-03T12:56:46Z"
rotulos: ["sync_hc", "ploomes_16052887", "sync_hash_70b539459f73", "ploomes"]
---

# Integrador em Branco: criando e gerenciando integrações personalizadas no Ploomes

## 1) Sobre o Integrador em Branco

O **Integrador em Branco** é uma ferramenta que permite criar fluxos de integração visuais dentro do próprio Ploomes, conectando o CRM a sistemas externos — como o Sankhya ou qualquer API HTTP — sem exigir desenvolvimento customizado.

Um fluxo é composto por um **gatilho** (o que inicia a execução) e uma sequência de **nós** conectados no canvas do editor, cada um responsável por uma etapa: fazer uma requisição, ler ou gravar um registro, transformar dados, tomar uma decisão ou repetir uma ação sobre uma lista.

Na prática, a funcionalidade cobre seis frentes:

- **Organização e navegação:** os fluxos ficam agrupados em pastas dentro de Administração, com busca e movimentação entre pastas.
- **Editor de fluxos:** canvas com nós arrastáveis para gatilhos, requisições HTTP, ações no Ploomes e no Sankhya, transformação de dados, IA, código customizado, decisões e loops.
- **Cofre de chaves de autenticação (KeysVault):** um local centralizado para cadastrar e gerenciar as credenciais usadas pelos fluxos.
- **Geração de fluxos por IA:** é possível descrever em linguagem natural o fluxo desejado e a IA (Ploo) monta e configura os nós automaticamente, além de permitir refinar fluxos já existentes.
- **Execução resiliente:** cada conta processa suas integrações de forma isolada, com escalabilidade automática e retomada de execuções interrompidas sem reprocessamento.
- **Logs, versionamento e validação:** toda execução gera um registro consultável, cada publicação gera uma versão restaurável, e os dados gravados no Ploomes por um fluxo passam pelas mesmas regras de deduplicação de qualquer outro registro.

---

## 2) Pré-requisitos

- Ser **administrador da conta Ploomes**. O acesso à tela de Integrações Personalizadas, a criação de fluxos e o gerenciamento de chaves são funcionalidades exclusivas de administradores.
- Ter o **módulo de IA da Ploomes contratado**, caso deseje usar os nós de IA (Perguntar à IA, Resumir Texto, Classificar Texto, Extrair Dados Estruturados, Executar Agente) ou o assistente de geração de fluxos e código por IA. Sem o módulo contratado, esses recursos ficam visíveis, porém desabilitados.
- Ter as **credenciais do sistema externo** que deseja integrar em mãos antes de configurar um nó de ação ou requisição — por exemplo, um AppToken do Sankhya ou o token de API de outro sistema.
- Para integrar com o **Sankhya**, ter acesso à API pública do Sankhya (AppToken da conta) e saber se a integração deve apontar para o ambiente de Sandbox ou de Produção.

---

## 3) Configurando o Integrador em Branco

## 3.1) Acessando a tela de Integrações Personalizadas

Acesse **Administração → Integrações Personalizadas**. A tela abre sempre na aba **Fluxos**, com as abas **Chaves de autenticação** e **Logs** disponíveis ao lado.

Se nenhuma pasta ainda foi criada na conta, a tela exibe apenas o botão **Nova pasta**.

## 3.2) Organizando fluxos em pastas

Os fluxos são organizados em pastas — por exemplo, uma pasta por sistema externo integrado (Sankhya, SAP, Totvs).

## 3.2.1) Criando, renomeando e excluindo pastas

- Para criar uma pasta, clique em **Nova pasta** e informe um nome único na conta. Não há limite de quantidade de pastas.
- Para renomear, acesse a pasta e use a opção de renomear. Os fluxos dentro dela não são afetados.
- Para excluir uma pasta vazia, a remoção é imediata. Para excluir uma pasta com fluxos, o sistema exibe a lista de fluxos que serão afetados e exige confirmação explícita — a exclusão remove a pasta e todos os fluxos nela, interrompendo imediatamente qualquer execução em andamento. **Essa ação é irreversível.**

## 3.2.2) Localizando e movendo fluxos

Dentro de uma pasta, a listagem exibe número sequencial, nome do fluxo, criador, última atualização e data de criação. Um campo de busca filtra os fluxos por nome em tempo real.

Para mover um fluxo entre pastas, use a opção de mover e selecione a pasta de destino — ou crie uma pasta nova diretamente nesse fluxo, sem precisar sair da tela. Mover um fluxo é uma ação puramente organizacional: não afeta a configuração nem interrompe execuções em andamento.

## 3.3) Configurando o cofre de chaves de autenticação (KeysVault)

O KeysVault centraliza as credenciais usadas pelos nós dos seus fluxos, na aba **Chaves de autenticação**.

## 3.3.1) Criando uma chave

Ao criar uma chave, informe:

- **Descrição/Identificação:** nome único na conta, imutável após o cadastro.
- **Valor da credencial**, que fica mascarado (exibindo só os caracteres finais) assim que salvo.
- **Tipo de conteúdo:** application/json, text/plain ou base64.
- **Data de expiração** (opcional).
- **Status inicial:** habilitada ou desabilitada.

Também é possível criar uma chave direto na hora de configurar um nó que exige autenticação, sem sair do editor.

## 3.3.2) Editando, habilitando e desabilitando chaves

Na listagem (ordenada por ID de criação), cada chave mostra ID, versão, status, data de atualização e data de expiração, com destaque visual para chaves expiradas.

- Editar o **valor** de uma credencial incrementa a versão automaticamente e exibe um alerta se a chave já estiver em uso por algum fluxo — a nova credencial passa a valer na próxima execução desses fluxos.
- **Desabilitar** uma chave é aplicado de forma imediata e sem alerta prévio: qualquer fluxo que dependa dela passa a falhar na execução seguinte.
- O ID técnico da chave nunca muda, e não há opção de excluir uma chave nesta versão da funcionalidade.

## 3.4) Criando um fluxo manualmente no editor

Ao criar um fluxo dentro de uma pasta, o canvas abre em branco. A toolbar do editor oferece as ações Importar JSON, Exportar JSON, Versões e Avaliar fluxo.

## 3.4.1) Montando a estrutura no canvas

- Use o componente **"+"** no final da sequência (ou entre dois nós já conectados) para adicionar um novo nó.
- Nós que geram múltiplos caminhos (Filtro, Decisão IF-ELSE) exibem um "+" para cada ramo.
- Arraste um nó para reposicioná-lo — as conexões se ajustam automaticamente.
- Ao remover um nó do meio da sequência, o nó anterior e o posterior são reconectados automaticamente.
- Todas as alterações são salvas em **rascunho** automaticamente, em tempo real — não existe botão "Salvar" separado do rascunho.

## 3.4.2) Configurando o gatilho

Todo fluxo tem exatamente um gatilho, escolhido entre:

- **Gatilho Periódico:** a cada X minutos (1 a 59), a cada hora, todos os dias, todas as semanas, a cada mês, ou uma expressão Cron com timezone.
- **Gatilho Webhook:** gera uma URL de callback — que só é exibida depois que o nó é testado pela primeira vez.
- **Evento no Ploomes:** disparado por criação ou atualização de Cliente, Negócio, Produto, Proposta ou Venda.

É possível trocar o tipo de gatilho a qualquer momento, sem excluir o nó — a troca marca o fluxo como pendente de teste.

## 3.4.3) Adicionando nós de ação, transformação e controle

- **Requisição HTTP:** método (GET, POST, PUT, PATCH, DELETE), URL, autenticação (nenhuma, básica, Bearer Token ou chave do cofre), cabeçalhos, parâmetros, corpo (JSON, Form Data ou Raw, com variáveis de nós anteriores), timeout de até 60 segundos e seis opções de comportamento em caso de falha.
- **Ações Ploomes:** 20 nós (Criação, Leitura, Edição e Deleção para Cliente, Negócio, Produto, Proposta e Venda), sempre autenticados por uma chave do cofre associada a um usuário Ploomes — toda ação fica registrada no log de auditoria do Ploomes em nome desse usuário.
- **Ações Sankhya:** 15 nós — Criação, Edição e Leitura para Parceiro, Contato de Cliente, Produto e Grupo de Produto; Leitura para CabecalhoNota e ItemNota; e um nó único "Criar Documento" que cria CabecalhoNota e seus ItemNota em uma única requisição. A autenticação usa uma chave do cofre com o AppToken do Sankhya — o Ploomes troca esse token por um Bearer Token automaticamente. Cada nó escolhe individualmente o ambiente (Sandbox ou Produção).
- **Transformação e agregação:** o nó de Mapeamento de Campos remapeia campos de entrada para saída (sem conversão de tipo); o nó de Agregação aplica COUNT, SUM, AVG, MIN ou MAX sobre uma lista.
- **IA (Ploo):** Perguntar à IA, Resumir Texto, Classificar Texto, Extrair Dados Estruturados e Executar Agente — disponíveis apenas com o módulo de IA contratado.
- **Código, decisão e loop:** o nó de Código executa JavaScript customizado (com opção de gerar o código via IA); o nó de Decisão (IF-ELSE) ramifica o fluxo em N caminhos com condições configuráveis; o nó de Loop itera sobre uma lista, executando os nós internos para cada item.

## 3.5) Criando um fluxo com a IA (Ploo)

No editor, abra o chat da IA (à esquerda do canvas) e descreva o fluxo desejado em linguagem natural — é possível anexar arquivos de contexto (PDF, Excel, CSV ou imagem).

A IA pode conduzir uma entrevista rápida para reunir detalhes que faltarem, depois exibe uma **prévia do plano** com os nós que pretende criar e o que cada um fará. Nada é inserido no canvas até você confirmar o plano; se rejeitar, pode enviar um novo prompt refinado.

Depois de confirmado, os nós entram no canvas já configurados (incluindo código JavaScript e mapeamento de campos entre sistemas, quando aplicável) e podem ser editados livremente, como qualquer fluxo manual. O mesmo chat serve para **refinar um fluxo já existente** — peça alterações específicas ("troque o gatilho por um webhook", "adicione um filtro antes do nó 4") e confirme o novo plano proposto.

## 3.6) Testando e publicando um fluxo

Um fluxo só entra em produção depois de **publicado**, e só pode ser publicado quando todos os nós estiverem com o status **"testado"**.

- Teste um nó individualmente ou o fluxo inteiro pela toolbar do editor. Os resultados aparecem no painel lateral de logs de teste, separado dos logs de produção.
- Enquanto houver alterações não publicadas, o editor exibe um banner com as opções **Descartar alterações** ou **Publicar**.
- Use **Exportar JSON** para baixar a última versão publicada do fluxo, e **Importar JSON** para carregar um fluxo em outra conta — a importação sempre marca todos os nós como pendentes de teste.
- O botão **Avaliar fluxo** analisa a configuração e aponta, nó a nó, recomendações de boas práticas (paginação, respeito ao header Retry-After em erros 429, backoff exponencial, entre outras). A avaliação é apenas informativa e não bloqueia a publicação.

---

## 4) Utilizando o Integrador em Branco

## 4.1) Acompanhando a execução dos fluxos

Depois de publicado, o fluxo passa a ser executado conforme o gatilho configurado. Cada conta processa suas execuções de forma isolada — o volume de outras contas não afeta a performance da sua. Se uma execução for interrompida por uma falha de infraestrutura, ela é retomada automaticamente a partir do ponto em que parou, sem reprocessar etapas já concluídas.

## 4.2) Consultando os logs de execução

Na aba **Logs**, a listagem consolidada mostra todas as execuções da conta, da mais recente para a mais antiga, com pasta, nome do fluxo, status, horários de início e término, duração e mensagem de erro.

Clique em uma execução para ver o detalhe: tempo de cada nó e o body de request e response de cada etapa. Credenciais e tokens nunca aparecem nos logs — são mascarados antes de qualquer gravação.

Use os filtros de **Período**, **Pasta**, **Fluxo** e **Status** para localizar execuções específicas — eles podem ser combinados e são aplicados automaticamente. O filtro de Fluxo é encadeado ao de Pasta.

## 4.3) Recebendo notificações de falha

Sempre que uma execução falhar, o criador do fluxo recebe uma notificação in-app e por e-mail, com nome do fluxo, pasta, tipo e mensagem do erro, e um link direto para o log daquela execução. Se o criador não for mais um usuário ativo da conta, a notificação vai para o administrador. Essa notificação pode ser desativada nas configurações — mas a desativação vale para todos os fluxos da conta, não é possível desativar por fluxo individual.

## 4.4) Consultando o histórico e restaurando uma versão anterior

Cada publicação gera uma nova versão, com data, autor e um resumo das alterações (sugerido automaticamente e editável). Acesse o botão **Versões** na toolbar para ver as últimas 10 versões do fluxo.

Para avaliar um rollback, selecione uma versão anterior: o canvas se divide, mostrando a versão candidata à esquerda e a atual à direita. Ao confirmar o rollback, o rascunho é substituído pela versão escolhida, todos os nós voltam ao status "pendente de teste" e uma nova versão é registrada no histórico. Execuções em andamento no momento do rollback não são interrompidas — elas terminam com a versão que estava publicada. A versão restaurada só entra em produção depois de testada e publicada novamente.

## 4.5) Escalonando a capacidade de execução

Se a conta atingir o limite de execuções simultâneas do plano contratado, as execuções excedentes são enfileiradas (nunca descartadas), e esse status aparece nos logs. O aumento de capacidade é negociado comercialmente e configurado pelo time de Negócio da Ploomes — não há uma tela de autoatendimento para isso. Depois de configurado o aumento, o administrador da conta passa a ver a capacidade contratada e o consumo do período atual, com alertas quando o uso se aproxima do limite.

---

## 5) Limitações

- **Ações do Sankhya não incluem deleção.** Os nós de Ações Sankhya oferecem Criação, Edição e Leitura (e, para CabecalhoNota/ItemNota, apenas Leitura) — não há nó de exclusão para nenhuma entidade do Sankhya.
- **Não há operação em lote nativa.** Tanto nas Ações Ploomes quanto nas Ações Sankhya, processar múltiplos registros de uma vez exige compor o fluxo com um nó de Loop — exceto na criação de documento (CabecalhoNota + ItemNota), que já aceita múltiplos itens por natureza da própria operação.
- **O timeout de um nó de Requisição HTTP é limitado a 60 segundos.**
- **O histórico de versões guarda as últimas 10 versões.** Ao ultrapassar esse limite, a versão mais antiga é descartada automaticamente e não pode ser recuperada.
- **O chat da IA não mantém histórico entre sessões de refinamento.** Cada vez que o painel é reaberto em um fluxo existente, a conversa começa do zero.
- **A notificação de falhas de execução é configurada de forma global.** Não é possível ativá-la ou desativá-la fluxo a fluxo.
- **Os nós de IA nativa consomem exclusivamente créditos do módulo de IA da Ploomes.** Não é possível usar chaves de provedores externos (OpenAI, Anthropic, etc.) nesses nós — apenas no nó de Requisição HTTP genérico, configurado manualmente.
- **O nó "Criar Documento" do Sankhya não garante atomicidade.** Se o cabeçalho for aceito e algum item for rejeitado, o comportamento de criação parcial depende exclusivamente de como a própria API do Sankhya trata a requisição.
- **O rollback nunca interrompe execuções em andamento**, mas também não é aplicado direto em produção: ele afeta apenas o rascunho, exigindo nova publicação para valer.
- **A avaliação de boas práticas ("Avaliar fluxo") é apenas uma recomendação.** Ela não impede salvar ou publicar um fluxo que não siga as práticas sugeridas.
- **O escalonamento de capacidade não é ilimitado nem self-service.** Sempre define um novo limite fixo, maior que o anterior, e depende de negociação comercial.
- **A validação por deduplicação depende do módulo Deduplicador estar disponível na conta.** Sem ele, essa camada de proteção contra duplicidade de registros não se aplica às gravações feitas por fluxos.

---

## 6) FAQ

**Só administradores podem criar e gerenciar fluxos de integração?**

Sim. O acesso à tela de Integrações Personalizadas, a criação de fluxos e o gerenciamento de chaves do cofre são exclusivos de administradores da conta, sem distinção por plano contratado.

**Preciso ter o módulo de IA da Ploomes contratado para usar o Integrador em Branco?**

Não. Os nós de gatilho, requisição HTTP, ações Ploomes e Sankhya, transformação e código estão disponíveis para qualquer conta. Apenas os cinco nós de IA e o assistente de geração/refinamento de fluxos e código por IA exigem o módulo de IA contratado.

**O que acontece se eu excluir uma pasta que tem fluxos ativos?**

O sistema mostra a lista de fluxos que serão afetados e pede confirmação explícita. Ao confirmar, a pasta e todos os fluxos dentro dela são excluídos, e qualquer execução em andamento é interrompida imediatamente. Essa ação não pode ser desfeita.

**Posso publicar um fluxo com nós que ainda não foram testados?**

Não. A publicação só é permitida quando todos os nós do fluxo estiverem com o status "testado". Enquanto houver nós pendentes, o botão Publicar retorna erro.

**O que acontece com uma chave do cofre que eu desabilito?**

Todos os fluxos que dependem dela passam a falhar na próxima execução que tentar usá-la. A desabilitação é imediata e não exibe alerta prévio, diferente da edição do valor da credencial (que avisa se a chave já está em uso).

**Como faço para reverter uma alteração que quebrou meu fluxo em produção?**

Acesse o histórico de versões pelo botão "Versões" no editor, compare a versão anterior com a atual no canvas dividido, e confirme o rollback. Depois, teste os nós novamente e publique para que a versão restaurada volte a valer em produção.

**Consigo excluir um registro do Sankhya usando o Integrador em Branco?**

Não. Os nós de Ações Sankhya não incluem uma operação de deleção para nenhuma entidade.

**Uma execução falhou por instabilidade momentânea — vou perder o processamento?**

Não. O motor de execução salva um cursor de continuação a cada etapa concluída e retoma a execução automaticamente a partir desse ponto, sem reprocessar o que já foi feito.

**Quem recebe a notificação quando uma execução falha?**

O criador do fluxo, por in-app e e-mail. Se o criador não for mais um usuário ativo da conta, a notificação é enviada ao administrador.

**Posso aumentar o número de execuções simultâneas da minha conta?**

Sim, mas por negociação comercial — não existe um botão de autoatendimento para isso dentro do produto. Depois de configurado pelo time de Negócio da Ploomes, você acompanha a capacidade contratada e o consumo do período na interface.

---

## 7) Glossário

- **Fluxo:** a integração configurada no editor, composta por um gatilho e uma sequência de nós conectados.
- **Nó:** cada etapa de um fluxo — pode ser um gatilho, uma ação, uma transformação, uma decisão ou um loop.
- **Canvas:** a área visual do editor onde os nós são posicionados e conectados.
- **Gatilho:** o nó que inicia a execução de um fluxo. Pode ser Periódico, Webhook ou Evento no Ploomes.
- **Rascunho:** o estado de um fluxo com alterações ainda não publicadas, salvo automaticamente em tempo real.
- **Publicar:** ação que coloca a versão atual do rascunho em produção, exigindo que todos os nós estejam testados.
- **KeysVault (Cofre de chaves):** local centralizado de cadastro e gestão das credenciais de autenticação usadas pelos nós dos fluxos.
- **AppToken:** credencial de acesso à API do Sankhya, trocada automaticamente pelo Ploomes por um Bearer Token temporário antes de cada execução.
- **Cursor de continuação:** mecanismo interno que registra o ponto exato em que uma execução parou, permitindo retomá-la sem reprocessamento em caso de interrupção.
- **Rollback:** ação de restaurar o rascunho de um fluxo para uma versão anterior do histórico.
- **Diff (resumo de versão):** descrição em linguagem natural, gerada automaticamente, das alterações realizadas entre duas versões de um fluxo.
- **Node de Código:** nó que executa JavaScript customizado dentro de um fluxo.
- **Loop:** nó que repete a execução dos nós internos para cada item de uma lista.
- **Decisão (IF-ELSE / Router):** nó que ramifica o fluxo em diferentes caminhos conforme condições configuradas.
- **Deduplicador:** módulo do Ploomes responsável por validar registros contra duplicidade antes da gravação, aplicado também aos dados criados ou editados por fluxos de integração.
- **HPA (escalabilidade automática):** mecanismo de infraestrutura que ajusta a capacidade de processamento conforme a demanda, de forma transparente ao usuário.
