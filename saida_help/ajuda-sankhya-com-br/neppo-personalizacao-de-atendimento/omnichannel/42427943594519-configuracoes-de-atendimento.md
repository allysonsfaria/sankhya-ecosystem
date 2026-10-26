---
id: "42427943594519"
titulo: "Configurações de atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T15:34:02Z"
rotulos: ["sync_hc", "neppo", "neppo_25068964", "sync_hash_e969b25ff193"]
---

# Configurações de atendimento

Este manual detalha as **Configurações de Atendimento**, o núcleo administrativo da plataforma Neppo onde toda a estrutura e as regras da operação são definidas. O objetivo é permitir que o administrador configure de ponta a ponta como os atendimentos serão recebidos, distribuídos, gerenciados e mensurados.

- [GRUPO DE ATENDIMENTO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento#GRUPO-DE-ATENDIMENTO)
- [PESQUISA DE SATISFAÇÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento#PESQUISA-DE-SATISFACAO)
- [CLASSIFICAÇÃO DE ATENDIMENTO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento#CLASSIFICACAO-DE-ATENDIMENTO)
- [CLIENTES](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento#CLIENTES)
  - [Atributos de Clientes](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento#Atributos-de-Clientes)
- [USUÁRIOS](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427943594519-Configura%C3%A7%C3%B5es-de-atendimento#USUARIOS)

## GRUPO DE ATENDIMENTO

Menu > Configurações >  Atendimento > Grupo de Atendimento

Na tela Grupos de Atendimentos teremos os grupos  já cadastrados, as informações não podem ser apagadas da plataforma, portanto caso uma determinado grupo não deva ficar mais ativo, realize a desativação em Status ![Imagem 1: Na tela Grupos de Atendimentos teremos os grupos já cadastrados, as informações não podem ser apagadas da plataforma,…](https://ajuda.sankhya.com.br/hc/article_attachments/42636644419095) .

Para editar um grupo clique no mesmo e para realizar o cadastro de um novo grupo basta clicar no

![Imagem 2: .](https://ajuda.sankhya.com.br/hc/article_attachments/42636641862167).

![Imagem 3: .](https://ajuda.sankhya.com.br/hc/article_attachments/42636656615191)

**Cadastro dos Grupos de Atendimento**

Na tela Cadastrar Grupo siga o passo a passo abaixo:

● Coloque o nome que deseja dar ao grupo de atendimento  que deve ser o mesmo cadastrado no fluxo de atendimento e selecione a operação a qual esse grupo será vinculado.

Obs. Os demais itens não são obrigatórios.

![Imagem 4: Obs. Os demais itens não são obrigatórios.](https://ajuda.sankhya.com.br/hc/article_attachments/42636656784151)

● Selecione um **agente de inicialização**, que será o BOT para iniciar o atendimento ou o bot de transferência, o tipo vai depender de qual grupo está sendo cadastrado.
Caso seja um grupo pai (grupo principal) será o bot de atendimento, onde está toda a estrutura de dados em árvore para atendimento via chat e no  grupo filho(grupo onde é realizado atendimento humano) normalmente estará o bot de transferência ou nenhum bot .

O campo "Necessidade de agente online" deverá ter a opção NÃO marcada.

![Imagem 5: O campo "Necessidade de agente online" deverá ter a opção NÃO marcada.](https://ajuda.sankhya.com.br/hc/article_attachments/42636642482455)

● Após adicionar um bot, é possível que ao flegar em Configurar Inatividade seja configurado uma ação para quando o cliente está sendo atendido pelo bot, isso pode ocorrer tanto porque o cliente não deu continuidade no fluxo ou também por estar tendo sua solicitação sendo tratada pelo bot.
Para cadastrar informe, **Tempo de inatividade** informe o período, em **Tempo em**  se será em Segundos, Minutos, Horas ou Dias e qual será a **Ação**: Enviar para Grupo, Enviar para Fila ou Fechar Atendimento.

![Imagem 6: ● Após adicionar um bot, é possível que ao flegar em Configurar Inatividade seja configurado uma ação para quando o…](https://ajuda.sankhya.com.br/hc/article_attachments/42636662750487)![Imagem 7: ● Após adicionar um bot, é possível que ao flegar em Configurar Inatividade seja configurado uma ação para quando o…](https://ajuda.sankhya.com.br/hc/article_attachments/42636617258519)

● **Agente de inatividade** e **Agente de finalização** serão necessários em casos específicos de customizações do bot.

![Imagem 8: ● Agente de inatividade e Agente de finalização serão necessários em casos específicos de customizações do bot.](https://ajuda.sankhya.com.br/hc/article_attachments/42636657814807)

● Selecione a pesquisa de satisfação e a classificação que deseja adicionar, itens que previamente já foram adicionados dentro das telas de Pesquisa de Satisfação e Classificação de Atendimento.

![Imagem 9: ● Selecione a pesquisa de satisfação e a classificação que deseja adicionar, itens que previamente já foram adicionados…](https://ajuda.sankhya.com.br/hc/article_attachments/42636658046871)

● Após adicionar os itens é necessário informar se o envio da pesquisa e a realização da classificação serão obrigatórias.

![Imagem 10: ● Após adicionar os itens é necessário informar se o envio da pesquisa e a realização da classificação serão…](https://ajuda.sankhya.com.br/hc/article_attachments/42636646020503)

● Em **Nome mostrado na mensagem** podemos optar por mostrar o nome da empresa, nome do agente ou nenhum nome.

![Imagem 11: ● Em Nome mostrado na mensagem podemos optar por mostrar o nome da empresa, nome do agente ou nenhum nome.](https://ajuda.sankhya.com.br/hc/article_attachments/42636630564631)![Imagem 12: ● Em Nome mostrado na mensagem podemos optar por mostrar o nome da empresa, nome do agente ou nenhum nome.](https://ajuda.sankhya.com.br/hc/article_attachments/42636658584087)

Exemplo de conversa com nome da empresa:

![Imagem 13: Exemplo de conversa com nome da empresa:](https://ajuda.sankhya.com.br/hc/article_attachments/42636664181655)

● Em **Gestão de fila** informaremos de que forma ocorrerá a distribuição dos atendimentos.

![Imagem 14: ● Em Gestão de fila informaremos de que forma ocorrerá a distribuição dos atendimentos.](https://ajuda.sankhya.com.br/hc/article_attachments/42636677771159)

Essa distribuição pode ocorrer de 5 formas:
**Circular:** Direciona os atendimentos sequencialmente entre a fila formada por agentes logados.
**Randômico:** Direciona atendimentos aleatoriamente para os agentes.

**Prioridade do Agente:**  Direciona atendimentos conforme a prioridade cadastrada nos usuários Agentes. Quanto maior o número cadastrado, maior a prioridade para receber os atendimentos.
**Menor tempo de Atendimento:** Direciona o atendimento para o agente que estiver com menor tempo de atendimento.
**Menor número de atendimento:** Direciona o atendimento para o agente com o menor número de atendimentos totais.

![Imagem 15: Prioridade do Agente: Direciona atendimentos conforme a prioridade cadastrada nos usuários Agentes. Quanto maior o…](https://ajuda.sankhya.com.br/hc/article_attachments/42636677928343)

● Em **Configurações do Grupo** estarão funções que serão habilitadas ou não habilitadas no grupo. Abaixo a descrição ao que se refere cada item e em negrito as que normalmente são selecionadas.

**Envio ativo de SMS:** Configuração que possibilita que o usuário da plataforma entre em contato com o cliente de forma ativa através do SMS.

**Envio ativo de Voz:** Opção que deve ser selecionada quando o grupo é relacionado ao canal de Voz.

**Envio ativo de Whatsapp:** Configuração que possibilita que o usuário da plataforma entre em contato com o cliente de forma ativa através do Whatsapp (Essa opção deve ser marcada exclusivamente no grupo principal, onde está configurado o gateway, pois todos os envios são realizados a partir desse grupo).

**Envia template Whatsapp?:** A opção deverá ser flegada apenas no grupo pai (principal)  caso o cliente utilize a API Oficial do Whatsapp e Facebook(Essa opção deve ser marcada exclusivamente no grupo principal, onde está configurado o gateway, pois todos os envios são realizados a partir desse grupo).

**Envio ativo de Email:** Configuração que possibilita que o usuário da plataforma entre em contato com o cliente de forma ativa através do E-mail.

**Envio ativo de Telegram:** Configuração que possibilita que o usuário da plataforma entre em contato com o cliente de forma ativa através do Telegram.

**Atendimento prioritário para o agente:** Configuração que possibilita que os atendimentos definidos como prioritários sejam redirecionados diretamente para o Agente.

**Redirecionar atendimento por desconexão do agente:** Configuração que possibilita que os atendimentos ativos de um agente sejam redirecionados para a fila de atendimento quando ocorrer a desconexão do mesmo. Essa opção deve estar marcada para que não ocorra o encerramento do atendimento após a desconexão do agente.

**Envio automático de atendimento para pendente:** Com essa opção marcada os atendimentos ficam como pendente após um tempo determinado sem interação por parte do cliente.

Ao flegar a opção,  será aberta dentro de  **Temporizadores/Inatividade** a possibilidade de informar o tempo em minutos.

![Imagem 16: Ao flegar a opção, será aberta dentro de Temporizadores/Inatividade a possibilidade de informar o tempo em minutos.](https://ajuda.sankhya.com.br/hc/article_attachments/42636678114071)![Imagem 17: Ao flegar a opção, será aberta dentro de Temporizadores/Inatividade a possibilidade de informar o tempo em minutos.](https://ajuda.sankhya.com.br/hc/article_attachments/42636659519255)

**Parceiro Whatsapp/Facebook:** A opção deverá ser flegada caso o cliente utilize a API Oficial do Whatsapp e Facebook.

**Transferir para agentes em pausa:** Função que permite a transferência para agentes em pausa.

**Posição da fila por período:** Função que permite que os clientes que estiverem na fila recebam a notificação da sua posição a cada valor de minutos definido no temporizador.
Ao flegar a opção,  será aberta dentro de  **Temporizadores/Inatividade** a possibilidade de informar o tempo em minutos.

![Imagem 18: Posição da fila por período: Função que permite que os clientes que estiverem na fila recebam a notificação da sua…](https://ajuda.sankhya.com.br/hc/article_attachments/42636631761687)

Com a flag desmarcada os clientes recebem a posição quando suas posições forem alteradas.
**Somente Receptivo:** Com essa opção marcada o agente não terá permissão de enviar mensagens.

**Permissão de envio de áudio:** Configuração que permite que o agente envie áudio ao cliente.

**Permissão de envio de imagem:** Configuração que permite que o agente envie imagem ao cliente.

**Permissão de envio de vídeo:** Configuração que permite que o agente envie vídeo ao cliente.

**Permissão de envio de documentos:** Configuração que permite que o agente envie documentos  ao cliente.

![Imagem 19: Permissão de envio de documentos: Configuração que permite que o agente envie documentos ao cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/42636670083607)

● Em **Temporizadores/Inatividade** informe os campos conforme abaixo:

**Aviso de inatividade(%)**
Insira a porcentagem desejada para quando aproximar do tempo de inatividade enviar

o aviso:“O protocolo está próximo de atingir o tempo de inatividade!” por grupo de

atendimento.

**Tempo de inatividade(minutos)**
Insira o tempo de inatividade em minutos para quando o cliente parar de interagir

com o BOT ou atendente o atendimento seja encerrado.Obs: Inatividade 24hs padrão

**SLA Inicial**
Configuração do tempo ideal de atendimento, apenas para relatório, sem impacto no fechamento da interação em si.

**Encerrar atendimento por inatividade**
Insira se o encerramento por inatividade se dará somente por parte do cliente ou se será por parte do cliente e do agente.

**Aviso de inatividade de parceiro (minutos)**
O campo será aberto ao flegar o campo “Parceiro Whatsapp/Facebook” em “Configurações de grupo”. Insira quanto tempo para a sessão Whatsapp encerrar, que a mensagem de aviso de atingimento da inatividade deve ser enviada.

**Tempo para agente interagir(minutos)**
Insira o tempo que o agente poderá demorar para responder um atendimento que ele

recebeu.

**Delay de envio de mensagem ativa para usuários que estão com sessão ativa (minutos). (0 para desativar)**
A opção permite o agendamento do envio ativo se o cliente estiver com um atendimento aberto e o agente enviar um ativo no mesmo número, o envio será agendado conforme o tempo estabelecido. Se o tempo cadastrado for 0 (zero) o envio será feito na mesma hora.

![Imagem 20: Delay de envio de mensagem ativa para usuários que estão com sessão ativa (minutos). (0 para desativar) A opção permite…](https://ajuda.sankhya.com.br/hc/article_attachments/42636678934679)

● Em **Associação de Agentes,** adicione os atendentes que atenderão no grupo, no grupo pai (principal) todos os agentes deverão estar adicionados, já nos demais grupos (grupos filhos) devem ser adicionados os atendentes de acordo com os respectivos setores.

Você pode pesquisar os usuários e utilizar os botões para incluir ou retirar os agentes do grupo:

![Imagem 21: Você pode pesquisar os usuários e utilizar os botões para incluir ou retirar os agentes do grupo:](https://ajuda.sankhya.com.br/hc/article_attachments/42636665655575)![Imagem 22: Você pode pesquisar os usuários e utilizar os botões para incluir ou retirar os agentes do grupo:](https://ajuda.sankhya.com.br/hc/article_attachments/42636679275799)

● Em **Permissão de transferência entre grupos** informe os grupos para os quais a transferência será permitida.

Inclusão dos grupos para os quais a transferência será permitida.
Você pode pesquisar os grupos e utilizar os botões para incluir ou retirar os grupos para transferência:

![Imagem 23: Inclusão dos grupos para os quais a transferência será permitida. Você pode pesquisar os grupos e utilizar os botões…](https://ajuda.sankhya.com.br/hc/article_attachments/42636694275607)![Imagem 24: Inclusão dos grupos para os quais a transferência será permitida. Você pode pesquisar os grupos e utilizar os botões…](https://ajuda.sankhya.com.br/hc/article_attachments/42636679678231)

Após o cadastro de todas as informações, clique em **SALVAR.**

## PESQUISA DE SATISFAÇÃO

Menu > Configurações >  Atendimento > Pesquisa de Satisfação

| ![Imagem 25: A pesquisa de satisfação permite mensurar quanto o seu cliente ficou satisfeito com o atendimento recebido.](https://ajuda.sankhya.com.br/hc/article_attachments/42636694737687) A pesquisa de satisfação permite mensurar quanto o seu cliente ficou satisfeito com o atendimento recebido. |
| --- |

Na tela Pesquisa de Satisfação teremos as pesquisas  já cadastradas, as informações não podem ser apagadas da plataforma, portanto caso uma determinada pesquisa não deva ficar mais ativa, realize a desativação em Status ![Imagem 26: Na tela Pesquisa de Satisfação teremos as pesquisas já cadastradas, as informações não podem ser apagadas da…](https://ajuda.sankhya.com.br/hc/article_attachments/42636648880407).

Obs. Ao desativar uma pesquisa ela será desassociada de todos os grupos de atendimento configurados com ela.

Para editar uma pesquisa clique na mesma e para realizar o cadastro de uma nova pesquisa basta clicar no ![Imagem 27: Para editar uma pesquisa clique na mesma e para realizar o cadastro de uma nova pesquisa basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951).

![Imagem 28: Para editar uma pesquisa clique na mesma e para realizar o cadastro de uma nova pesquisa basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636633543831)

Na tela de Pesquisa de Satisfação preencha as informações conforme abaixo:

**Nome da pesquisa:** O nome da pesquisa de satisfação não pode conter espaços, pois será criado um bot com o mesmo nome. Na utilização deste, o mesmo será substituído por underscore ('\_').
**Selecione o tipo de pesquisa:**
**ABERTO:** O cliente receberá uma pergunta e poderá dissertar de forma livre como foi a experiência dele com a empresa.

**CSAT:** Funciona através de uma pergunta onde o cliente terá a possibilidade de usar alternativas como “satisfeito”, “indiferente”, “pouco satisfeito”, “ótimo”, “regular”, “ruim” para avaliar a experiência no atendimento.
**NPS:** Usa uma pergunta para qual o cliente deve atribuir uma nota ao atendimento que vai de 0 a 10. Na escala, o 0 pode representar algo como “péssimo”, e o 10 algo como “excelente ”.
**Pode ser utilizado mais de um tipo de pesquisa.**
**Envio da Pesquisa de Satisfação:** Selecionar quais serão os usuários que ao finalizar o atendimento a pesquisa será enviada, Bot, Agente e Supervisor Agente.

![Imagem 29: CSAT: Funciona através de uma pergunta onde o cliente terá a possibilidade de usar alternativas como “satisfeito”,…](https://ajuda.sankhya.com.br/hc/article_attachments/42636695532951)![Imagem 30: CSAT: Funciona através de uma pergunta onde o cliente terá a possibilidade de usar alternativas como “satisfeito”,…](https://ajuda.sankhya.com.br/hc/article_attachments/42636649566743)

Após cadastrada a pesquisa é necessário adicioná-la  dentro do **Grupo de Atendimento**.

Menu > Configurações >  Atendimento > Grupos de Atendimento

Nessa tela você verá todos os grupos do ambiente, para cadastrar um novo grupo, basta clicar no + ou acesse um grupo existente.

![Imagem 31: Nessa tela você verá todos os grupos do ambiente, para cadastrar um novo grupo, basta clicar no + ou acesse um grupo…](https://ajuda.sankhya.com.br/hc/article_attachments/42636649753239)

Em **Selecione uma pesquisa de satisfação** escolha qual pesquisa deverá ser enviada ao cliente dentro daquele grupo específico e se o envio é obrigatório ou não.

![Imagem 32: Em Selecione uma pesquisa de satisfação escolha qual pesquisa deverá ser enviada ao cliente dentro daquele grupo…](https://ajuda.sankhya.com.br/hc/article_attachments/42636681055255)![Imagem 33: Em Selecione uma pesquisa de satisfação escolha qual pesquisa deverá ser enviada ao cliente dentro daquele grupo…](https://ajuda.sankhya.com.br/hc/article_attachments/42636672848535)

Após selecionar a pesquisa clique em ![Imagem 34: Após selecionar a pesquisa clique em .](https://ajuda.sankhya.com.br/hc/article_attachments/42636668093207) .

## CLASSIFICAÇÃO DE ATENDIMENTO

Menu > Configurações >  Atendimento > Classificação de Atendimento

| ![Imagem 35: É um recurso que permite a tabulação do motivo do atendimento, permite que a empresa organize os atendimentos de acordo…](https://ajuda.sankhya.com.br/hc/article_attachments/42636694737687) É um recurso que permite a tabulação do motivo do atendimento, permite que a empresa organize os atendimentos de acordo com o assunto tratado. |
| --- |

Na tela Classificação de Atendimento teremos as classificações  já cadastradas, as classificações não podem ser apagadas da plataforma, portanto caso uma determinada classificação não deva ficar mais ativa, realize a desativação em Status ![Imagem 36: Na tela Classificação de Atendimento teremos as classificações já cadastradas, as classificações não podem ser apagadas…](https://ajuda.sankhya.com.br/hc/article_attachments/42636648880407) .

![Imagem 37: Na tela Classificação de Atendimento teremos as classificações já cadastradas, as classificações não podem ser apagadas…](https://ajuda.sankhya.com.br/hc/article_attachments/42636668319639)

Para editar uma pesquisa clique na mesma e para realizar o cadastro de uma nova classificação basta clicar no ![Imagem 38: Para editar uma pesquisa clique na mesma e para realizar o cadastro de uma nova classificação basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951).

Após selecionar o ![Imagem 39: Após selecionar o , você irá incluir o nome da classificação em Nível Principal e no é possível adicionar os motivos e…](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951), você irá incluir o nome da classificação em Nível Principal  e no ![Imagem 40: Após selecionar o , você irá incluir o nome da classificação em Nível Principal e no é possível adicionar os motivos e…](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951) é possível adicionar os motivos e sub-motivos que poderão ser categorizados pelo agente.

![Imagem 41: Após selecionar o , você irá incluir o nome da classificação em Nível Principal e no é possível adicionar os motivos e…](https://ajuda.sankhya.com.br/hc/article_attachments/42636673564823)

Após cadastrar a classificação clique em ![Imagem 42: Após cadastrar a classificação clique em .](https://ajuda.sankhya.com.br/hc/article_attachments/42636668093207).

Após cadastrada a classificação é necessário adicioná-la  dentro do **Grupo de Atendimento**.

Menu > Configurações >  Atendimento > Grupos de Atendimento

Nessa tela você verá todos os grupos do ambiente, para cadastrar um novo grupo, basta clicar no + ou acesse um grupo existente.

![Imagem 43: Nessa tela você verá todos os grupos do ambiente, para cadastrar um novo grupo, basta clicar no + ou acesse um grupo…](https://ajuda.sankhya.com.br/hc/article_attachments/42636650835863)

Em **Selecione uma classificação,** escolha qual classificação deverá ser enviada ao agente dentro daquele grupo específico e se a classificação é obrigatória ou não.

![Imagem 44: Em Selecione uma classificação, escolha qual classificação deverá ser enviada ao agente dentro daquele grupo específico…](https://ajuda.sankhya.com.br/hc/article_attachments/42636685702807)![Imagem 45: Em Selecione uma classificação, escolha qual classificação deverá ser enviada ao agente dentro daquele grupo específico…](https://ajuda.sankhya.com.br/hc/article_attachments/42636702624791)

Após selecionar a classificação clique em ![Imagem 46: Após selecionar a classificação clique em .](https://ajuda.sankhya.com.br/hc/article_attachments/42636668093207).

## CLIENTES

Menu > Configurações >  Atendimento > Clientes> Clientes

| ![Imagem 47: Base de clientes cadastrados na plataforma.](https://ajuda.sankhya.com.br/hc/article_attachments/42636694737687)Base de clientes cadastrados na plataforma. |
| --- |

Na tela Clientes teremos os clientes já cadastradas, as informações não podem ser apagadas da plataforma, portanto caso queira desativar um cliente para que o mesmo não possa mais entrar em contato com a empresa desative em Status ![Imagem 48: Na tela Clientes teremos os clientes já cadastradas, as informações não podem ser apagadas da plataforma, portanto caso…](https://ajuda.sankhya.com.br/hc/article_attachments/42636648880407).

Para editar um cliente  clique no mesmo e para realizar o cadastro de um novo cliente basta clicar no ![Imagem 49: Para editar um cliente clique no mesmo e para realizar o cadastro de um novo cliente basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951) .

Para adicionar o  cliente, basta seguir o passo a passo abaixo:
 ● Coloque o nome a ser exibido no histórico do cliente.

![Imagem 50: Para adicionar o cliente, basta seguir o passo a passo abaixo: ● Coloque o nome a ser exibido no histórico do cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/42636651317399)

● Em  nome do usuário  realizamos o preenchimento conforme o padrão estabelecido, ao clicar em

![Imagem 51: é possível visualizar qual é esse padrão.](https://ajuda.sankhya.com.br/hc/article_attachments/42636674407447) é possível visualizar qual é esse padrão.

![Imagem 52: é possível visualizar qual é esse padrão.](https://ajuda.sankhya.com.br/hc/article_attachments/42636674661911)

Após o campo preenchido e salvo não é possível editá-lo.

● O campo com a bandeira do Brasil é de preenchimento do número do telefone do cliente.

![Imagem 53: ● O campo com a bandeira do Brasil é de preenchimento do número do telefone do cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/42636651883415)

Os números de telefone celular e fixo só terão êxito no cadastro caso sejam nacionais.

● Coloque o e-mail do cliente que será associado à plataforma. O campo só aceita um e-mail por número de telefone.

![Imagem 54: ● Coloque o e-mail do cliente que será associado à plataforma. O campo só aceita um e-mail por número de telefone.](https://ajuda.sankhya.com.br/hc/article_attachments/42636652011415)

● Coloque a data de nascimento do cliente com dia, mês e ano.

![Imagem 55: ● Coloque a data de nascimento do cliente com dia, mês e ano.](https://ajuda.sankhya.com.br/hc/article_attachments/42636698611351)

● Campo não obrigatório que possibilita que o nome do cliente seja mostrado no envio da mensagem de plataforma message.inactive.info enviada no  início do atendimento.

![Imagem 56: ● Campo não obrigatório que possibilita que o nome do cliente seja mostrado no envio da mensagem de plataforma…](https://ajuda.sankhya.com.br/hc/article_attachments/42636703722647)![Imagem 57: ● Campo não obrigatório que possibilita que o nome do cliente seja mostrado no envio da mensagem de plataforma…](https://ajuda.sankhya.com.br/hc/article_attachments/42636675516183)

● O campo de CPF ou CNPJ precisa ser selecionado corretamente. Note que um número de

celular não pode ser associado a CPF em conjunto com CNPJ.

![Imagem 58: celular não pode ser associado a CPF em conjunto com CNPJ.](https://ajuda.sankhya.com.br/hc/article_attachments/42636719691543)

● Após selecionar o campo de CPF ou CNPJ, é necessário preencher a informação dos números correspondentes a ele.

![Imagem 59: ● Após selecionar o campo de CPF ou CNPJ, é necessário preencher a informação dos números correspondentes a ele.](https://ajuda.sankhya.com.br/hc/article_attachments/42636719887255)

● Coloque o nível de prioridade do cliente.

![Imagem 60: ● Coloque o nível de prioridade do cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/42636704446231)

● Preencha o atributo do cliente.

![Imagem 61: ● Preencha o atributo do cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/42636704649367)

● Preencha o campo do valor do atributo

![Imagem 62: ● Preencha o campo do valor do atributo](https://ajuda.sankhya.com.br/hc/article_attachments/42636676310551)

● O símbolo ![Imagem 63: ● O símbolo , localizado do lado direito e inferior da tela, ao lado de valor do](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951), localizado do lado direito e inferior da tela, ao lado de valor do

atributo, quando selecionado, abre mais um espaço de atributo e valor do atributo, o que mostra que um cliente pode estar relacionado a mais de um atributo.

![Imagem 64: atributo, quando selecionado, abre mais um espaço de atributo e valor do atributo, o que mostra que um cliente pode…](https://ajuda.sankhya.com.br/hc/article_attachments/42636720534679)

Após concluir o Cadastro do Cliente, basta clicar em SALVAR para concluir o processo, ou cancelar para a não conclusão.

![Imagem 65: Após concluir o Cadastro do Cliente, basta clicar em SALVAR para concluir o processo, ou cancelar para a não conclusão.](https://ajuda.sankhya.com.br/hc/article_attachments/42636720722839)

Para incluir os contatos de forma massiva clique no símbolo ![Imagem 66: Para incluir os contatos de forma massiva clique no símbolo para baixar a planilha e realize o preenchimento conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/42636688500887) para baixar a planilha e realize o preenchimento conforme abaixo:

**Os itens obrigatórios são NETWORK, COUNTRY CODE, PHONE NUMBER e DISPLAY NAME, mas os demais itens podem ser adicionados.**

**NETWORK -** Preencher de canal número o canal é. Ex: WHATSAPP

**COUNTRY CODE -** Código do país (Brasil é 55)

**PHONE NUMBER -** Número de telefone no formato DDD + número de telefone com nove dígitos

**DISPLAY NAME -** Nome do contato

**CPF/CNPJ -** (Não é obrigatório)

**EMAIL -** (Não é obrigatório)

**GROUP -** Nome do grupo de atendimento que deseja vincular o contato. (Não é obrigatório)

**AGENT -** Nome de usuário do agente que deseja vincular ao contato, nos casos em que houver carteirização cadastrada no bot. (Não é obrigatório)

**ATTRIBUTE -** Informação extra de cadastro. (Não é obrigatório)

**ATTRIBUTE'S VALUE -** Valor da informação extra de cadastro. (Não é obrigatório)

![Imagem 67: ATTRIBUTE'S VALUE - Valor da informação extra de cadastro. (Não é obrigatório)](https://ajuda.sankhya.com.br/hc/article_attachments/42636685245335)

Obs. Recomendamos a utilização de arquivos CSV com menos de 2000 linhas.

Após preencher as informações clique no ![Imagem 68: Após preencher as informações clique no para importar a planilha preenchida.](https://ajuda.sankhya.com.br/hc/article_attachments/42636688999959) para importar a planilha preenchida.

Ao realizar a importação da planilha, os contatos que estiverem no formato correto e ainda não cadastrados na plataforma irão ser incluídos no sistema normalmente, caso seja identificado algum erro, o sistema irá sinalizar, clique no item a ser ajustado.

![Imagem 69: Ao realizar a importação da planilha, os contatos que estiverem no formato correto e ainda não cadastrados na…](https://ajuda.sankhya.com.br/hc/article_attachments/42636685565719)

Após clicar ajuste a informação e clique em **SALVAR**.

![Imagem 70: Após clicar ajuste a informação e clique em SALVAR .](https://ajuda.sankhya.com.br/hc/article_attachments/42636736015255)

Após o item ser ajustado clique em **REENVIAR** para que o contato seja adicionado.

![Imagem 71: Após o item ser ajustado clique em REENVIAR para que o contato seja adicionado.](https://ajuda.sankhya.com.br/hc/article_attachments/42636689510551)

### Atributos de Clientes

Menu > Configurações >  Atendimento > Clientes> Atributos de clientes

| ![Imagem 72: Os atributos são informações extras que podem ser adicionadas no cadastro dos clientes.](https://ajuda.sankhya.com.br/hc/article_attachments/42636694737687)Os atributos são informações extras que podem ser adicionadas no cadastro dos clientes. |
| --- |

Na tela Atributos de Clientes teremos os atributos  já cadastrados, os atributos não podem ser apagadas da plataforma, portanto caso um determinado atributo não deva ficar mais ativa, realize a desativação em Status ![Imagem 73: Na tela Atributos de Clientes teremos os atributos já cadastrados, os atributos não podem ser apagadas da plataforma,…](https://ajuda.sankhya.com.br/hc/article_attachments/42636648880407).

Para editar um atributo  clique no mesmo e para realizar o cadastro de um novo atributo basta clicar no ![Imagem 74: Para editar um atributo clique no mesmo e para realizar o cadastro de um novo atributo basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951).

![Imagem 75: Para editar um atributo clique no mesmo e para realizar o cadastro de um novo atributo basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636736397591)

Informe a Descrição e clique em Ativar para que o atributo fique disponível para utilização.

![Imagem 76: Informe a Descrição e clique em Ativar para que o atributo fique disponível para utilização.](https://ajuda.sankhya.com.br/hc/article_attachments/42636722263575)

Após preencher as informações clique em **SALVAR**.

## USUÁRIOS

Menu > Configurações >  Atendimento > Usuários

| ![Imagem 77: A plataforma possui 4 tipos de usuário, Administrador, Supervisor, Supervisor Agente e Agente. O usuário administrador…](https://ajuda.sankhya.com.br/hc/article_attachments/42636694737687)A plataforma possui 4 tipos de usuário, Administrador, Supervisor, Supervisor Agente e Agente.  O usuário administrador pode fazer todo tipo de configuração e monitoramento disponível no sistema. Como supervisor, possui acesso ao dashboard e ao relatório de níveis de serviço de acordo com o liberado pelo administrador. Já o agente  acessa a um ambiente diferente, focado nas funcionalidades de atendimento ao cliente. |
| --- |

Na tela Usuários teremos os usuários já cadastradas, as informações não podem ser apagadas da plataforma, portanto caso um determinado usuário não deva mais realizar o acesso a plataforma, desative em Status ![Imagem 78: Na tela Usuários teremos os usuários já cadastradas, as informações não podem ser apagadas da plataforma, portanto caso…](https://ajuda.sankhya.com.br/hc/article_attachments/42636648880407).

Para editar um usuário  clique no mesmo e para realizar o cadastro de um novo usuário basta clicar no ![Imagem 79: Para editar um usuário clique no mesmo e para realizar o cadastro de um novo usuário basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951).

![Imagem 80: Para editar um usuário clique no mesmo e para realizar o cadastro de um novo usuário basta clicar no .](https://ajuda.sankhya.com.br/hc/article_attachments/42636754210455)

Após selecionar o ![Imagem 81: Após selecionar o , você será direcionado a página de Cadastro de Usuário .](https://ajuda.sankhya.com.br/hc/article_attachments/42636671708951),  você será direcionado a  página de **Cadastro de Usuário**.

Selecione primeiro qual tipo de usuário.

![Imagem 82: Selecione primeiro qual tipo de usuário.](https://ajuda.sankhya.com.br/hc/article_attachments/42636754811031)

**USUÁRIO ADMINISTRADOR**

Preencha os dados conforme abaixo:

**IDENTIDADE DO USUÁRIO**

Nome a ser exibido (Nome do usuário)
Nome de usuário (Nome utilizado para logar na plataforma)
**PERFIL**
Selecione o perfil do usuário
**EMPRESA**
Selecione a empresa
**DATA DE NASCIMENTO**

Não obrigatório
**CONTATO**
Telefone e E-mail
**SENHA**
OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS MAIÚSCULAS E CARACTERES ESPECIAIS.
Caso queira que o usuário possa alterar a senha no primeiro login, selecione a opção abaixo:

![Imagem 83: Não obrigatório CONTATO Telefone e E-mail SENHA OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS…](https://ajuda.sankhya.com.br/hc/article_attachments/42636755206807)![Imagem 84: Não obrigatório CONTATO Telefone e E-mail SENHA OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS…](https://ajuda.sankhya.com.br/hc/article_attachments/42636755500311)

**USUÁRIO AGENTE**

Preencha os dados conforme abaixo:

**IDENTIDADE DO USUÁRIO**

Nome a ser exibido (Nome do usuário)
Nome de usuário (Nome utilizado para logar na plataforma)
**PERFIL**
Selecione o perfil do usuário
**DATA DE NASCIMENTO**

Não obrigatório
**CONTATO**
Telefone e E-mail
**SENHA**
OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS MAIÚSCULAS E CARACTERES ESPECIAIS.
Caso queira que o usuário possa alterar a senha no primeiro login, selecione a opção abaixo:

![Imagem 85: Não obrigatório CONTATO Telefone e E-mail SENHA OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS…](https://ajuda.sankhya.com.br/hc/article_attachments/42636723200535)

**ATENDIMENTOS SIMULTÂNEOS**

Quantidade de atendimentos que o agente poderá fazer ao mesmo tempo (0 a 80)

**PRIORIDADE**
Caso a gestão de fila, ou seja a distribuição dos atendimentos será por prioridade é necessário atribuir um número ao agente, quanto maior o número atribuído mais atendimentos o agente receberá.
**DEPARTAMENTO (Não obrigatório)**
**TOKEN SOCIAL (Não obrigatório)**
**CHAVE DE INTEGRAÇÃO (Não obrigatório)**
**HORÁRIO DE TRABALHO**
Funcionalidade que permite a configuração de horário de trabalho para o Agente para que o mesmo acesse a plataforma apenas somente durante o período selecionado.
**PERMISSÕES DO AGENTE**
Funções que serão habilitadas ou não habilitadas ao agente.

**Visualizar todos os históricos(Grupos associados)** **:** Permissão para que o agente possa visualizar os históricos das operações que o agente faz parte.
**Visualizar todos os históricos(Operações associadas)** **:** Permissão para que o agente possa visualizar os históricos das operações que o agente faz parte.
**Histórico Confidencial** **:** Flegue essa opção caso queira que o histórico do agente não fique disponível para os demais)

**Registrar ligação telefônica? :**  Flegar caso utilizem o produto Voz
**Atender por voz :** Flegar caso utilizem o produto Voz

Canal de atendimento: Neppo Voz Nuvem
Ramal de atendimento: Nº ramal do agente
Senha canal de atendimento
**Pausar ao receber ligação por voz.**

![Imagem 86: Canal de atendimento: Neppo Voz Nuvem Ramal de atendimento: Nº ramal do agente Senha canal de atendimento Pausar ao…](https://ajuda.sankhya.com.br/hc/article_attachments/42636707429143)

**USUÁRIO SUPERVISOR**

Preencha os dados conforme abaixo:

**IDENTIDADE DO USUÁRIO**

Nome a ser exibido (Nome do usuário)
Nome de usuário (Nome utilizado para logar na plataforma)
**PERFIL**
Selecione o perfil do usuário
**OPERAÇÃO**
Associação de uma operação específica ao usuário Supervisor, para que o mesmo tenha acesso às informações e manutenções apenas da operação em que está associado.
Você pode pesquisar as operações e utilizar os botões para vincular ou desvincular as operações do cadastro do Supervisor:
1- Incluir um ou mais operações.
2- Incluir todas as operações de forma massiva.
3- Retirar um ou mais operações.
4- Incluir todas as operações de forma massiva.

**DATA DE NASCIMENTO**

Não obrigatório
**CONTATO**
Telefone e E-mail
**SENHA**
OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS MAIÚSCULAS E CARACTERES ESPECIAIS.
Caso queira que o usuário possa alterar a senha no primeiro login, selecione a opção abaixo:

![Imagem 87: Não obrigatório CONTATO Telefone e E-mail SENHA OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS…](https://ajuda.sankhya.com.br/hc/article_attachments/42636723200535)

**HORÁRIO DE TRABALHO**
Funcionalidade que permite a configuração de horário de trabalho para o Agente para que o mesmo acesse a plataforma apenas somente durante o período selecionado.

![Imagem 88: HORÁRIO DE TRABALHO Funcionalidade que permite a configuração de horário de trabalho para o Agente para que o mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/42636756549655)

**USUÁRIO SUPERVISOR AGENTE**

Preencha os dados conforme abaixo:

**IDENTIDADE DO USUÁRIO**

Nome a ser exibido (Nome do usuário)
Nome de usuário (Nome utilizado para logar na plataforma)
**PERFIL**
Selecione o perfil do usuário
**OPERAÇÃO**
Associação de uma operação específica ao usuário Supervisor, para que o mesmo tenha acesso às informações e manutenções apenas da operação em que está associado.
Você pode pesquisar as operações e utilizar os botões para vincular ou desvincular as operações do cadastro do Supervisor:
1- Incluir um ou mais operações.
2- Incluir todas as operações de forma massiva.
3- Retirar um ou mais operações.
4- Incluir todas as operações de forma massiva.

**DATA DE NASCIMENTO**

Não obrigatório
**CONTATO**
Telefone e E-mail
**SENHA**
OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS MAIÚSCULAS E CARACTERES ESPECIAIS.
Caso queira que o usuário possa alterar a senha no primeiro login, selecione a opção abaixo:

![Imagem 89: Não obrigatório CONTATO Telefone e E-mail SENHA OBS. DEVE CONTER MAIS DE 7 CARACTERES, LETRAS, NÚMEROS, LETRAS…](https://ajuda.sankhya.com.br/hc/article_attachments/42636723200535)

**ATENDIMENTOS SIMULTÂNEOS**

Quantidade de atendimentos que o agente poderá fazer ao mesmo tempo (0 a 80)
**PRIORIDADE**
Caso a gestão de fila, ou seja a distribuição dos atendimentos será por prioridade é necessário atribuir um número ao agente, quanto maior o número atribuído mais atendimentos o agente receberá.
**DEPARTAMENTO (Não obrigatório)**
**TOKEN SOCIAL (Não obrigatório)**
**CHAVE DE INTEGRAÇÃO (Não obrigatório)**
**HORÁRIO DE TRABALHO**
Funcionalidade que permite a configuração de horário de trabalho para o Agente para que o mesmo acesse a plataforma apenas somente durante o período selecionado.
**PERMISSÕES DO AGENTE**
Funções que serão habilitadas ou não habilitadas ao agente.

**Visualizar todos os históricos(Grupos associados)** **:** Permissão para que o agente possa visualizar os históricos das operações que o agente faz parte.
**Visualizar todos os históricos(Operações associadas)** **:** Permissão para que o agente possa visualizar os históricos das operações que o agente faz parte.
**Histórico Confidencial** **:** Flegue essa opção caso queira que o histórico do agente não fique disponível para os demais)

**Registrar ligação telefônica? :**  Flegar caso utilizem o produto Voz
**Atender por voz :** Flegar caso utilizem o produto Voz

Canal de atendimento: Neppo Voz Nuvem
Ramal de atendimento: Nº ramal do agente
Senha canal de atendimento
**Pausar ao receber ligação por voz.**

![Imagem 90: Canal de atendimento: Neppo Voz Nuvem Ramal de atendimento: Nº ramal do agente Senha canal de atendimento Pausar ao…](https://ajuda.sankhya.com.br/hc/article_attachments/42636707668503)

Para adicionar os  usuários na plataforma de forma massiva baixe o Excel clicando no item ![Imagem 91: Para adicionar os usuários na plataforma de forma massiva baixe o Excel clicando no item preencha as informações que…](https://ajuda.sankhya.com.br/hc/article_attachments/42636738065559)preencha as informações que são as mesmas contidas na tela e importe clicando no ![Imagem 92: Para adicionar os usuários na plataforma de forma massiva baixe o Excel clicando no item preencha as informações que…](https://ajuda.sankhya.com.br/hc/article_attachments/42636770134679).

![Imagem 93: Para adicionar os usuários na plataforma de forma massiva baixe o Excel clicando no item preencha as informações que…](https://ajuda.sankhya.com.br/hc/article_attachments/42636691878551)

Para realizar a edição de um usuário já cadastrado basta clicar nesse usuário, editar os dados e clicar em **SALVAR**.
