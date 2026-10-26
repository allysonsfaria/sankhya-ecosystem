---
id: "42427609969815"
titulo: "Atualizações de Agosto de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427609969815-Atualiza%C3%A7%C3%B5es-de-Agosto-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:14Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8218791", "sync_hash_5fb5a0414896"]
---

# Atualizações de Agosto de 2023

[03/08/2023] [Correção] E-mails enviados diretamente pelo provedor não estavam tendo suas respostas vinculadas em uma mesma thread no Ploomes.

[04/08/2023] [Correção] Ao criar um negócio no aplicativo com um campo de Checkbox preenchido por padrão como"não" e de preenchimento obrigatório, o campo não era preenchido com o valor padrão.

[04/08/2023] [Correção] Dentro do app, quando se tentava acessar a entidade de Clientes, no caso de não se ter nenhuma aba de clientes, o app entrava em carregamento infinito.

[04/08/2023] [Correção] Dentro do app, não havia alerta de erro quando tentávamos inserir anexo com o App Offline.

[07/08/2023] [Correção] Na integração com Exact Spotter, um campo específico de opções pré-cadastradas estava vindo sem propriedades obrigatórias no código e causava erro na criação das entidades configuradas (Negócio, Cliente e Contato).

[08/08/2023] [Correção] Contas que tiveram registro de interação criados pelo Zenvia e que a integração foi posteriormente desligada, não estavam exibindo o restante do histórico de interações no negócio.

[08/08/2023] [Correção] Ao criar uma proposta na tela cheia com novo negócio, não era possível por fórmula acessar os valores dos campos do cliente na via Proposta > Cliente.

[08/08/2023] [Correção] Estando o sistema na linguagem em Português (Portugal), pesquisa por NIF (equivalente ao CNPJ em Portugal) não retornava resultados no módulo de clientes.

[08/08/2023] [Correção] Ao criar uma publicação, havia problemas para restringir as publicações para um ou mais times. Foi corrigido para, caso o usuário não seja administrador, só seja possível restringir para as equipes que o usuário faz parte.
[08/08/2023] [Correção] Campos de opções pré-cadastradas com fórmula/valor padrão em produtos da Proposta, não estavam sendo engatilhados, consequentemente não estavam sendo exibidos ao gerar o documento, quando o produto era inserido através da opção "Dados do cliente".

[08/08/2023] [Correção] Ao criar uma automação cuja ação fosse criar um novo Negócio, não havia possibilidade de escolher qual estágio do funil selecionado o negócio seria criado. Com isso, caso o estágio fosse deletado, não seria possível alterar a automação para corrigir o estágio desejado. Na correção, foi adicionado um campo para selecionar o estágio em que o negócio será criado.

[08/08/2023] [Correção] Em vínculo de opcionais de produto, o relacionamento entre dois vínculos estava sendo propagado para outros produtos. Isto é, ao adicionar um vínculo que bloqueasse outros opcionais, essa regra também se aplicava a outros produtos da proposta, removendo ou bloqueando seleções.

[08/08/2023] [Correção] Em campos multilinha de Produto, quando o conteúdo ficava maior do que a tela reduzida poderia comportar, o conteúdo quebrava pra fora da tela, foi adicionado um scroll lateral para solucionar o problema.

[08/08/2023] [Correção] Uma validação antiga do Ploomes não permitia que, durante a edição, as opções de campos de opções pré-cadastradas de Produto da Proposta/Venda/Documentos pudessem ser puxados de outros campos. O comportamento não era correto e foi corrigido.

[08/08/2023] [Correção] Ao criar um novo negócio dentro do modal de vinculação de e-mail, ocorria um problema que o campo de "Contato" não filtrava apenas os contatos do "Cliente" do formulário. O problema acontecia com todos os formulários mini de Negócio. Com essa correção, o comportamento do campo de "Contato" é o mesmo do formulário normal.

[08/08/2023] [Correção] Em formulário externo, a seleção de campos não permitia a inserção de CPF e CNPJ no mesmo formulário. O filtro foi aprimorado para permitir a inserção de Cliente.CNPJ e Contato.CPF.

[08/08/2023] [Correção] Ao inserir um produto do cliente em uma Proposta, o Ploomes aguarda todas as fórmulas integradas terminarem para realizar a inserção. Porém, com uma internet lenta, as requisições tornam-se mais espaçadas, fazendo com que a inserção ocorresse antes do esperado. Foi corrigido adicionando uma tolerância para aguardar as requisições mesmo com a internet lenta.

[08/08/2023] [Correção] Relação entre vínculos estava entrando em conflito com sugestões e bloqueios e não priorizava o bloqueio quando haviam sugestões. Ao invés disso, a sugestão sobrepujava o bloqueio.

[08/08/2023] [Correção] Ao editar/revisar uma proposta, apenas a primeira opção de um campo de opções pré-cadastradas múltiplo era passado às variáveis via fórmula. Foi aplicada uma correção para serem passados todas as opções na edição/revisão e não apenas na criação.

[08/08/2023] [Correção] Campos múltiplos não podem ser usados em automações e devem ser bloqueados. Havia alguns problemas que permitiam alguns campos serem inseridos. Foi adicionado uma validação para bloquear todos os campos múltiplos de serem inseridos na edição da automação de registro de interação.

[08/08/2023] [Correção] Não existia um aviso de erro para compartilhamento via ClickSign quando o usuário tinha permissão para compartilhar, porém, não para editar.

[08/08/2023] [Correção] Não estava sendo possível puxar o valor do estágio atual, com uma fórmula, foi adicionado a propriedade que define qual estágio está o negócio e ao engatilhar a fórmula está puxando o valor corretamente.

[08/08/2023] [Correção] Ao tentar acessar um modelo de documento nas contas com whitelabel, estava tendo um carregamento muito demorado para puxar alguns arquivos estáticos para a apresentação da tela, chegando até a não conseguir pegar esses arquivos. O apontamento do mesmo foi para uma CDN onde o tempo de carregamento é superior.

[08/08/2023] [Correção] Ao remover anexos os que estavam abaixo deles eram clicados, fazendo com que fossem baixados ou abertos.

[08/08/2023] [Correção] Em relatórios beta, havia um problema com os operadores das métricas que alterava o valor de forma errada para "Vazio" ou "Diferente de vazio". O comportamento foi revisto e corrigido.

[08/08/2023] [Correção] Caso a integração com a receita federal fosse utilizada em um campo de CNPJ dentro de um checklist de Negócio, o campo de telefone da Empresa era limpo caso o CNPJ não tivesse um telefone cadastrado na receita. Foi corrigido para não sobrescrever o valor do campo de telefone caso ele esteja preenchido.

[08/08/2023] [Correção] Era possível inserir duração negativa nas tarefas.

[08/08/2023] [Correção] No módulo de negócios, ao pesquisar um negócio quebrando por tabela, dependendo da paginação que o usuário estivesse, não estava sendo possível buscar todos os negócios, buscava apenas o da paginação atual.

[08/08/2023] [Correção] Ao criar um filtro em abas, o campo 'Nome' da entidade 'Produto' era exibido duas vezes. O comportamento foi corrigido para remover essa opção excedente.

[08/08/2023] [Correção] Caso houvesse um campo de checklist de Negócio que estivesse vazio, ele não é exibido na página de Negócio, porém, seu preenchimento ainda era validado, resultando em erro e com isso, o usuário ficava impossibilitado de avançar o estágio do negócio. Foi corrigido filtrando todos os checklists vazios antes de realizar a validação de preenchimento e agora o botão de 'Avançar para a próxima etapa' é exibido corretamente.

[08/08/2023] [Correção] Não era possível visualizar página de negócios: requisição /GetApplicableChecklists retornava erro 404 (Not Found).

[08/08/2023] [Correção] Havia um problema na validação referente às permissões de um usuário para editar os anexos dos seus próprios registro de interações.

[08/08/2023] [Correção] Por conta da funcionalidade de traduções, algumas variáveis possuíam um apóstrofo em inglês. Com isso, alguma fórmulas do Ploomes não conseguiam identificar a variável por conta do conflito com as aspas no corpo da fórmula.

[08/08/2023] [Correção] O sistema permitia enviar documento via integração do Clicksign pela opção de whatsapp sem adicionar um e-mail, o que resultava em erro na integração.

[08/08/2023] [Correção] Opções de filtro em relatórios beta apresentam itens diferentes do esperado.

[08/08/2023] [Correção] Título de negócio apresentava espaçamentos removidos quando o texto era copiado diretamente negócio, e não do campo Negócio.Título

[08/08/2023] [Correção] Campo de formulário mini para a criação de contato não puxava a empresa do negócio.

[08/08/2023] [Correção] Ao adicionar conteúdo no bloco SENÃO de fórmula condicional, o front exibia a mensagem 'Preencha o campo SENÃO'.

[08/08/2023] [Correção] Usuários cuja permissão só possibilitava a visualização dos seus próprios e-mails estavam conseguindo visualizar registros de interações de e-mails enviados por outros usuários.

[09/08/2023] [Deploy de correção] Automação genérica para envio de e-mails não enviava e-mail à caixa de enviados do usuário definido como remetente.

[09/08/2023] [Correção] Edição em massa acumulava requisições na integração e ultrapassava o limite da api do Omie, causando erro nas atualizações.

[11/08/2023] [Correção] E-mails com registros de interação não são mais removidos quando o usuário remove/arquiva esse e-mail no provedor.

[14/08/2023] [Correção] Por conta de redirecionamentos de webhooks, a integração com Facebook Leads ficou indisponível entre os dias 12/08 e 14/08

[16/08/2023] [Correção] Inconsistência entre plataformas - usuário que não possui permissão para editar propostas tinha acesso ao botão "Revisar" dentro do app, o que não acontece na web.

[16/08/2023] [Correção] Inconsistência entre plataformas - em tarefas criadas para clientes cujo usuário não possuía visualização, o nome do cliente não aparecia no web, mas aparecia no app.

[16/08/2023] [Correção] No aplicativo, ao criar uma proposta que entra em vários fluxos de aprovação, os botões de "X" para fechar, "Cancelar" e "Enviar para aprovação" não funcionavam. Correção aplicada na versão 3.3.27 do App.

[16/08/2023] [Correção] No aplicativo, ao criar um negócio e inserir um anexo simples pelo 'menu' > 'editar negócio', após salvar o negócio o campo de anexo aparecia na tela do aplicativo sem a visualização do anexo. Essa visualização dava a possibilidade de inserir um novo anexo, porém ao sair do card e voltar o anexo não era salvo. Correção aplicada na versão 3.3.27 do App.

[16/08/2023] [Correção] Foi alterado um comportamento de relatórios legado para permitir que tabelas com métricas com mais de uma dimensão possam ser coloridas.

[17/08/2023] [Correção] Erro ao criar qualquer automação, solicitando preenchimento de campos que já estavam preenchidos.

[17/08/2023] [Correção] Exportação em massa de leads via Active Campaign não concluía corretamente, por atingir o limite de consultas na api.

[17/08/2023] [Correção] Na integração com a Omie, o campo método de pagamento estava integrando errado por conta de um erro na verificação da opção selecionada no Ploomes.

[22/08/2023] [Correção] Conteúdo do Link Web não era traduzido junto com a linguagem da conta.

[22/08/2023] [Correção] E-mail lido no gmail fica como não lido no Ploomes.

[24/08/2023] [Correção] No aplicativo, ao entrar em um documento criado e escrever algo no chat externo, ao clicar em enviar era exibido várias interações de usuário vazias e não salvava o comentário. Ao sair do chat externo e voltar, o chat externo ficava sem comentário nenhum (as interações de usuário sumiam). Correção aplicada na versão 3.3.28 do App.

[24/08/2023] [Correção] Ao criar/editar um filtro de tabela, era possível adicionar condições como "Campo de número inteiro maior que vazio" e outras condições que resultavam em erro.

[24/08/2023] [Correção] No aplicativo, pesquisar clientes pelo NIF não funcionava.

[24/08/2023] [Correção] Campo checkbox de proposta não reconhecia valor alterado para "SIM".

[24/08/2023] [Correção] No App estava aparecendo uma quantidade de seções relativas a quantidade de produtos do documento do negócio e que ficavam num loading infinito impossiblitando a edição.

[24/08/2023] [Correção] Visualização condicional em configuração em configuração que utilizava campo de negócio não funcionava.

[24/08/2023] [Correção] No código-fonte de modelos de proposta/venda, condicionais que verificavam se campos tinham o valor "diferente de" alguma coisa, não estavam funcionando corretamente.

[24/08/2023] [Correção] Erro visual no aplicativo que gerava uma circunferencia adicional na tela de calendário ao trocar de data.

[25/08/2023] [Correção] Ao configurar os campos de checklists e ao final criarmos um campo, ele apresenta uma inconsistência visual nos nomes dos campos que foram configurados anteriormente.

[25/08/2023] [Correção] Ao criar aba com filtro específico não retorna nenhuma tarefa, mesmo existindo.

[25/08/2023] [Correção] No formulário de configuração dos formulários externos, era possível por conta de um erro colocar um campo como chave mesmo em formulários com a finalidade de somente atualizar o cliente. Esse bug foi corrigido e além disso foi feita uma melhoria para alertar o usuário na hora da edição caso o formulário dele esteja com essa configuração incorreta.

[25/08/2023] [Correção] Ao criar um gráfico com valores numéricos não estava sendo possível retornar os valores exatos, muitas vezes arredondando ou mostrando números com menos casas decimais.

[25/08/2023] [Correção] Por conta de um débito técnico do CKEditor atual, um certo formato incorreto de código HTML fazia com que ele quebrasse. Foi aplicada uma correção no Front para remover esse padrão do HTML antes do CKEditor renderizar o código para a modificação visual.

[25/08/2023] [Correção] Ao criar contas de teste com o módulo de relatórios ativo, não

havia a opção de criar um Novo Painel e um Novo Gráfico no módulo de Relatórios Beta.

Isso ocorria por conta de um bloqueio no código, não era possível modificar painéis dos relatórios beta em contas de determinados planos. Esse bloqueio foi removido para que o comportamento fosse de acordo com a permissão do módulo, apenas, e não de acordo com o plano.

[28/08/2023] [Correção] Ao tentar acessar um modelo de documento nas contas com whitelabel, estava tendo um carregamento muito demorado para puxar alguns arquivos estáticos para a apresentação da tela, chegando até a não conseguir pegar esses arquivos.

[29/08/2023] [Correção] Alguns usuários não estavam conseguindo criar/modificar propostas geradas com o editor antigo.

[29/08/2023] [Correção] Em certas contas, automações de envio de e-mail pelo no-reply estavam com atraso no envio dos e-mails.

[30/08/2023] [Correção] Algumas informações de leads vindo do RD Station não eram integradas ao Ploomes, mesmo que o mapeamento de campos estivesse correto.

[31/08/2023] [Correção] Propostas que entram no filtro de um certo fluxo de aprovação não estavam entrando no fluxo de aprovação mesmo não tendo nenhum outro fluxo de aprovação em que essa proposta poderia ter entrado antes desse fluxo em questão. Foi corrigido o comportamento para as propostas entrarem no fluxo correto.
