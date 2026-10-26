---
id: "42427543805975"
titulo: "Atualizações de Novembro de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427543805975-Atualiza%C3%A7%C3%B5es-de-Novembro-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:41Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8556509", "sync_hash_ef8ed7a2967e"]
---

# Atualizações de Novembro de 2023

[01/11/2023] [Correção] Em Relatórios Beta havia um erro na visualização dos gráficos relacionado a permissões. O problema ocorria devido ao relatório se perder na hora de buscar as permissões por se tratar de usuários individuais.

[01/11/2023] [Correção] Atualizações do powerbi sendo canceladas.

[03/11/2023] [Correção] Integração com o Google Calendar estava duplicando tarefas.

[03/11/2023] [Correção] Ao enviar, via e-mail, o arquivo que conter um dos caracteres especias : "\/ : \* ? " <> |" no nome, eles serão substituídos por "\_".

[06/11/2023] [Correção] Na integração com o ClickSign, após remover um signatário que já havia assinado um documento, ao adicioná-lo novamente a integração estava criando novas entradas com o mesmo endereço de e-mail no ClickSign.

[06/11/2023] [Correção] A integração com o LetsSign não oferecia a funcionalidade de adicionar signatários a um documento após o envio para assinatura. No entanto, essa funcionalidade foi implementada e agora é possível adicionar signatários mesmo após o envio do documento para assinatura.

[06/11/2023] [Correção] Gráficos do tipo indicador em relatórios beta retornavam a soma com valor incorreto, decorrente de falta de sincronização de dados.

[06/11/2023] [Correção] Na integração com o Omie, antes, caso houvessem dois clientes com o mesmo CNPJ, ao deletar um dos clientes pelo Omie, os dois eram deletados no Ploomes porque a busca na deleção era feita com base no CNPJ. Agora essa busca é feita com base apenas no Id Omie, removendo a possibilidade de deleções indesejadas.

[06/11/2023] [Correção] Na integração com o Omie, a tabela de estoque não era preenchida com o valor padrão do Omie ao criar um novo produto, apenas ao realizar a primeira movimentação. Agora preenchemos a tabela de estoque com o valor do Omie na criação dos produtos também.

[07/11/2023] [Correção] Ao fazer uma ligação após criar um registro da ligação anterior o contador do tempo da ligação não estava resetando, começando a contabilizar pelo tempo da anterior. A correção faz o reset do timer quando cria um registro da ligação.

[07/11/2023] [Correção] Ao interagir com os opcionais que contém sugestões, estava causando uma inconsistência na usabilidade, selecionávamos uma nova opção e ele checava a sugestão ao invés da nova opção selecionada.

[07/11/2023] [Correção] Opção de Mailchimp não aparece, mesmo tendo integração.

[07/11/2023] [Correção] Nos relatórios beta, ao criar um gráfico de tabela com agregação do tipo soma, alguns totais eram calculados de forma incorreta pois estava sendo considerada no cálculo a contagem de itens. Este erro foi corrigido.

[07/11/2023] [Correção] Durante o preenchimento da proposta, ao tentar preencher o valor padrão de um campo do tipo data da entidade produto da proposta havia um erro de conversão quando esse valor padrão tinha como origem um campo da entidade proposta. Foi feita uma correção para que o valor seja lido corretamente.

[07/11/2023] [Correção] Registros de ligações estavam vinculando ao primeiro cliente que fez a ligação, a correção fez vincular ao cliente certo, avisando ao usuário que o registro atual vai ser excluído, colocando assim os dados certos do cliente da ligação.

[07/11/2023] [Correção] Ao editar uma proposta, o caminho Proposta > Cliente não estava trazendo todos os dados do cliente em fórmulas. O comportamento foi corrigido.

[07/11/2023] [Correção] Ao duplicar o card, a requisição /BulkDuplicate retornava erro 401 Unauthorized, porque havia anexos deletados.

[07/11/2023] [Correção] Atualmente ao salvar uma automação sem filtros, é guardado anda assim um id de um filtro daquela automação, mesmo estando vazio. Em contas antigas, algumas automações eram salvas sem nenhum tipo de filtro, e o id desses filtros era salvo como 'null'. Ao acessar a configuração dessas automações, o front tentava acessar as informações do filtro e não conseguia, fazendo a página ficar em loading infinito. Foi feita a correção para que o front não tente buscar as informações caso não haja um id de filtro.

[07/11/2023] [Correção] Drilldown de Análise história de funil não estava pegando a entidade do gráfico para conseguir fazer o link corretamente.

[07/11/2023] [Correção] Ploomes não salvava as configurações de permissões definidas em relatórios beta quando um perfil de usuário fazia essa ação.
[08/11/2023] [Correção] No aplicativo pelo sistema iOS, ao compartilhar proposta, documento ou venda pelo WhatsApp, sem selecionar o cliente ou com um cliente que não tenha o telefone cadastrado, o link era enviado 'quebrado' não sendo possível clicar no link. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] Os campos de empresa do Ploomes mapeados para campos do lead no RD não eram enviados ao lead corretamente. Adicionamos as tratativas necessárias para que tanto campos de empresa quanto contato integrem corretamente com o Lead do RD.

[08/11/2023] [Correção] A caixa de carregamento após ganhar o negócio não estava sumindo, dessa forma o usuário ficava preso em um carregamento. A lógica para sumir com essa caixa foi ajustada para que ela desapareça quando necessário.

[08/11/2023] [Correção] No aplicativo, ao estar utilizando o idioma português de Portugal, o campo "NIF" configurado como de preenchimento obrigatório, não era exibido no App ao criar ou editar Clientes. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] O aplicativo apresentava lentidão ao finalizar tarefas pelo checkbox. Correção aplicada na versão 4.0.3 do App.
[08/11/2023] [Correção] No aplicativo, fórmulas de visualização de alguns campos não estavam funcionando no formulário de Pessoa. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] No aplicativo, ao criar um registro de interação com marcadores selecionados, a visualização ficava quebrada sem nome e cor. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] No aplicativo, o formulário por padrão apresentava os dados básicos nas primeiras posições, causando divergência da web quando havia modificação de posições. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] No aplicativo, tarefas criadas/editadas para mais de 4 anos de diferença com o ano de hoje quebravam o calendário da tela de tarefas. Isso foi corrigido criando um alerta que explica para o usuário que não é possível criar/editar tarefas com essa data e impedindo que ele salve esse tipo de alteração. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] O aplicativo estava montando algumas requisições com base em um filtro que não estava funcionando quando era usado na API. Foi criada uma verificação que impeça a geração dessas requisições. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] Independente do tipo do registro de interação, o aplicativo fazia o check-in verificado (deveria apenas no de visita). Correção aplicada na versão 4.0.3 do App.
[08/11/2023] [Correção] No aplicativo, ao criar um novo negócio com o Modo Offline ativado não era possível adicionar um campo o qual é obrigatório para que formulário seja salvo, além do fato, da tela de carregamento infinito que fica tela que não deveria aparecer. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] Erro ao duplicar proposta e negócio - Todos os anexos que pertencem à algum negócio deletado irão ser vinculados ao negócio atual, resolvendo assim o problema da duplicação quando um anexo de um negócio origem for excluido.

[08/11/2023] [Correção] Em formulários de documentos, o campo de "proposta de origem" é oculto na versão web de forma nativa, mas não no aplicativo, o que causava crash no app ao selecionar o campo. Essa configuração foi adicionada e agora ele não aparece mais.

[08/11/2023][Correção]Os campos de cliente e contato estavam sendo considerados os mesmo, fazendo sempre pegar ou só de contato ou só cliente, trazendo valores errados

[08/11/2023] [Correção] No aplicativo, tarefas com duração de 1 dia ou mais não eram exibidas em todos os dias do período, somente no primeiro dia da tarefa. Correção aplicada na versão 4.0.3 do App.

[08/11/2023] [Correção] O campo "order\_products" não tinha a inversepropertykey "order\_product\_order".

[08/11/2023] [Correção] Campos de cliente duplicado criados pelo usuário de "Automação Ploomes e email" fazia com que a página do template da proposta ficasse travada por uns segundos.

[08/11/2023] [Correção] No aplicativo, ao clicar várias vezes em um item da lista da tela de contatos estava fazendo com que o usuário navegasse várias vezes para a mesma tela, fazendo com que ele tenha que voltar também várias vezes para retornar a lista. Correção aplicada na versão 4.0.4 do App.

[08/11/2023][Correção] Editar células vazias em campos multilinha fazia com que o cursor na hora de de digitar pulasse de uma célula para a mais próxima que possuía algo escrito, como precisava de algo entre as tags spans para não acontecer o problema, foi inserido entre eles um caractere do html que representa o vazio &nbsp;

[08/11/2023] [Correção] No aplicativo, ao tentar criar um novo documento em negocio que ja possui alguma proposta criada resultava em um loading infinito na sessão de produto/serviço. Correção aplicada na versão 4.0.4 do App.

[08/11/2023] [Correção] No aplicativo, durante a edição de proposta, formulas em formulário de produto que usavam o modelo da proposta não calculavam corretamente. Correção aplicada na versão 4.0.4 do App.
[08/11/2023] [Correção] No aplicativo, ao digitar no campo de contato relacionado ao criar uma tarefa para um cliente Empresa, o App não estava trazendo todos os contatos que existem na base, igual na web. Correção aplicada na versão 4.0.3 do App.

[09/11/2023][Correção] Relatório de coluna vertical não estava começando com zero em alguns casos, foi feita uma correção para que começasse dessa forma.

[10/11/2023] [Correção] No aplicativo, quando a lista de produtos possuía tanto o filtro de marcadores quanto de famílias, o app usava um OU para filtrar ao invés de um E. Correção aplicada na versão 4.0.4 do App.

[10/11/2023] [Correção] O app estava crashando quando o usuário clicava em um dos campos da checklist da conta enquanto estava editando outro campo. Foi adicionado o código que impede essa quebra ao clicar em um campo da checklist.

[10/11/2023] [Correção] Ao utilizar a extensão do WhatsApp, ao clicar muitas vezes na mesma conversa, estavam sendo feitas duas consultas para retornar os dados, isso impactou o backend do Ploomes inteiro, causando lentidão em alguns shards. Foi solucionado o problema, e agora ao clicar várias vezes, só é feita uma consulta.

[10/11/2023] [Correção] A cada vez que um campo de checklist era salvo, o Ploomes fazia um scrolldown na página do card e não voltava para o topo.

[13/11/2023] [Correção] No aplicativo, para alguns usuários o app estava fechando ao abrir a tela de negócios. Correção aplicada na versão 4.0.4 do App.

[15/11/2023] [Correção] Inconsistência na média de dias no estágio em relatórios beta por falta de ressincronização de dados.

[16/11/2023] [Correção] Relatórios não gravava cliente do negócio como nulo.

[16/11/2023] [Correção] Adicionada tradução para espanhol em todos os campos que eram utilizados no drilldown no relatório e que não existiam em código hardcoded.

[20/11/2023] [Correção] Em relatórios beta, alguns gráficos que filtravam por equipe não estavam exibindo os resultados corretamente.

[21/11/2023] [Correção] Quando um funil estava configurado para a ação da automação ser realizada por usuário de automação, ao disparar o gatilho, os registros das alterações estavam ficando antes do registro do gatilho.

[22/11/2023] [Correção] O campo descrição não aparecia como um campo de preenchimento obrigatório ao criar novo registro de interação.

[22/11/2023] [Correção] Havia um problema no mapeamento de campos do Omie onde campos de Data não dinamicos, não eram convertidos corretamente. Foi realizado o ajuste de colocar a conversão nesses campos.

[22/11/2023] [Correção] Automação genérica de tarefa com gatilho de quando o item for excluido não estava executando.

[22/11/2023] [Correção] Campo Atividade Economica da integração Econodata vinculado ao campo origem por padrão.

[22/11/2023][Correção] Alteração de responsável de empresa com muitos contatos não funcionava, foi adicionada uma melhoria de performance para que fosse possível fazer a alteração.

[22/11/2023][Correção] Campo "Cliente.Relação" estava bloqueado para que novas opções pré-cadastradas fossem adicionadas a ele e o chamado foi aberto para que o campo fosse desbloqueado.

[24/11/2023] [Correção] A ordenação do aplicativo para a lista de contatos não estava sendo a mesma que no web. Corrigido na versão 4.0.5 do app.
[24/11/2023] [Correção] No aplicativo, ao pesquisar por clientes do tipo Empresa, em vez de retornar os resultados, retornava uma lista de clientes tipo Pessoa sem nomes. Corrigido na versão 4.0.5 do App.

[24/11/2023] [Correção] O carregamento de filtro de negócios feita pelo app em geral era muito lento. Agora o app resgata parte das informações pelo banco offline para melhorar o tempo de carregamento da tela. Corrigido na versão 4.0.5 do App.

[24/11/2023][Correção] O app estava gerando uma request inválida com base em um dos filtros de negócios. Foram criadas regras na geração da request que respeitem as regras da API.

[24/11/2023][Correção] Anteriormente, quando um usuário mapeava mais de um campo do Active em apenas um campo do Ploomes, o respectivo campo não era preenchido. Agora, o campo será preenchido corretamente. Se valores estiverem presentes nos dois campos, como 'Campo 1' e 'Campo 2', por exemplo, a integração irá preencher com o último campo mapeado, nesse caso, o 'Campo 2'.

[27/11/2023] [Correção] Quando opcionais eram removidos por não se encaixarem no filtro durante a duplicação de uma proposta, não estava sendo exibido um aviso do ocorrido para o usuário.

[27/11/2023] [Correção] Ao clicar para gerar uma nova venda a partir de uma proposta e trocar o modelo de venda padrão para algum outro modelo que tenha blocos de produto diferentes, o bloco do modelo de venda anterior ficava salvo em memória, fazendo com que as fórmulas calculassem com valores incorretos. O problema foi corrigido mantendo em memória apenas os dados do bloco de produtos do modelo atual.

[27/11/2023] [Correção] Ao entrar pelo Ploomes Partners não estava atualizando os usuários de suporte com acesso recente nas permissões dos painéis em Relatórios Beta, agora ao entrar no módulo de Relatórios Beta é feita a atualização de usuários para poder selecioná-los nas permissões do painel.

[27/11/2023] [Correção] Ao editar/criar um modelo de documento, no menu da lateral esquerda existe uma seção de opções gerais, onde o campo "Campo de total das parcelas do modelo" estava triplicando um valor, foi incluído uma validação para não retornar valores com o mesmo ID.

[27/11/2023] [Correção] Ao exibir o resultado de uma fórmula em um campo de casas decimais ilimitadas, o Ploomes sempre fixava as casas decimais do resultado em 5 depois da vírgula. Foi feita uma melhoria para que agora seja retornado até 12 casas depois da vírgula, respeitando a quantidade.

[27/11/2023] [Correção] Ao digitar um nome que não existe nos campos de select, estava retornando duas opções no final da lista de criar, por exemplo, uma nova empresa, porém ao dar scroll aparecia mais opções e essas duas opções acabava se perdendo no meio das outras. Foi adicionado uma função para sempre jogar sugestões para criar algo novo, no final das opções.

[27/11/2023] [Correção] Ao finalizar uma tarefa com observações, o campo 'Contatos Relacionados' não estava filtrando os contatos do cliente, como é feito ao criar um registro de interação. Foi corrigido para que o comportamento seja o mesmo.

[27/11/2023][Correção] Quando o gráfico de tabela não tem valor na primeira métrica não estava exibindo os dados corretamente. A correção tratou de verificar as outras métricas para conseguir mostrar o dado corretamente.

[27/11/2023][Correção] Ao mudar de uma data com valor para adicionar para uma data que não precisa desse valor estava salvando o valor errado.

[27/11/2023][Correção] Ao editar a operação do filtro das métricas dos Relatórios Beta, geravam erros, não editava tudo que era esperado. Isso causava erros na edição das operações. O problema foi corrigido.

[27/11/2023][Correção] Ao salvar os dados da empresa a tela com as alterações não era atualizada, o que fazia perder referência da última alteração. A correção forçou a atualização do cache, mostrando os dados atualizados.

[27/11/2023][Correção] Ao configurar a opção de "Para quais funis um negócio pode ser remanejado?" na configuração do funil e navegar para um negócio dele sem atualizar a página, os funis para quais ele poderia ser remanejado não estavam atualizados conforme configurado.

[27/11/2023][Correção] Quando um campo é deletado, por conta de um débito técnico, o backend não consegue removê-lo das ações de automações, e ao editar uma automação com um campo que foi deletado, o front tentava procurar o campo que não existia mais, causando um erro. O problema foi corrigido ignorando campos deletados nessa situação.

[27/11/2023][Correção] Ao editar o campo de contato relacionado de tarefa via formulário mini, não filtrava pelo cliente, puxando todos os contatos da base.

[27/11/2023] [Correção] Ao entrar na configuração dos fluxos de aprovação, a condição do campo 'Equipes' não estava aparecendo para o usuário por conta de uma situação inesperada, o campo estava sendo confundido pelo front com o campo 'Marcadores'. O erro foi corrigido e agora a equipe selecionada será exibida corretamente.

[27/11/2023] [Correção] Ao acessar uma página onde fosse exibido um registro de interação contendo o padrão "<[algum texto qualquer]>" no firefox, havia um erro de conversão, pois o firefox interpretava esse padrão como uma tag HTML sempre, mesmo quando ela não era (ela pode ser um e-mail, por exemplo: <[ploo@ploomes.com](mailto:ploo@ploomes.com)>).

[27/11/2023] [Correção] No formulário modal de propostas, quando o campo tipo de frete estava vazio, por conta de um caso não previsto no código, sua variável era retornada como uma string vazia ('') ao invés de null como é esperado. O problema foi corrigido.

[27/11/2023] [Correção] O problema era que o campo de Contato não estava sendo apagado assim que o usuário limpava o campo de Cliente. Agora, quando o campo de Cliente é limpado, o campo de Contato também será limpado automaticamente.

[27/11/2023] [Correção] Ao criar uma exibição condicional em documentos, o front não adicionava a propriedade "condition-field-path-id" com o fieldPath do campo da condicional, e em alguns casos, isso fazia com que a condicional não funcionasse. Foi feita uma correção para que esse parâmetro seja adicionado sempre ao configurar uma exibição condicional.

[27/11/2023] Nas tabelas dinâmicas, o campo de contato do negócio estava sempre bloqueado, independente do tipo de cliente inserido. O comportamento foi corrigido para que esse campo só seja bloqueado quando não houver cliente ou o cliente do negócio seja do tipo pessoa.

[27/11/2023] [Correção] Ao acessar o modal de canais de atendimento, o link do formulário externo de professional services estava quebrado. O link foi corrigido com o formulário atual.

[27/11/2023] [Correção] Painel de relatórios beta apresentava alguns gráficos com o padrão de datas agrupadas por dia no padrão americano yyyy-MM-dd, em vez do brasileiro, dd/MM/yyyy.
[27/11/2023] [Correção] Para um usuário de uma conta não estava sendo exibido algumas informações quando ele navegava pelo Google Chrome. Ao entrar na tela inicial do Ploomes, estava ocorrendo um erro no código, assim, a visualização de alguns componentes não estava funcionando como esperado.

[27/11/2023] [Correção] Modal de confirmação de deleção em checklists só aparecia uma vez. Correção faz aparecer toda vez que clicar em excluir.
[28/11/2023] [Correção] Ao criar um campo de opções pré-cadastradas em um formulário e clicar logo em seguida para editá-lo sem salvar o formulário, não era possível ver nem editar as opções que haviam sido criadas. O problema foi corrigido para que seja possível editar normalmente mesmo antes de salvar o formulário.

[28/11/2023] [Correção] Campo de Contato estava engatilhando o campo de cliente, a correção colocou uma validação para checar o campo e engatilhar a forma corretamente.

[28/11/2023] [Correção] Quando se tem um campo que usa outro em uma fórmula, ao limpar esse campo usado na fórmula o campo não era limpo também.

[28/11/2023] [Correção] A integração do google calendar estava duplicando tarefas.

[28/11/2023] [Correção] O campo de "Buscar emails a partir de" estava duplicado e na mensagem de erro, ao voltar mais dias do que o permitido, estava exibindo código do desenvolvimento na mensagem.
[28/11/2023] [Correção] Campo de adicionar anexo e o anexo sumiam ao passar o mouse na entidade de tarefas, foi adicionado um loader também para informar ao usuário quando está carregando o anexo.
[28/11/2023] [Correção] Ao criar uma entidade a partir do formulário mini, caso o nome digitado no campo de opções inicial fosse maior do que o permitido no nome daquela entidade e a pessoa clicasse em 'Novo', o front contava incorretamente a quantidade de caracteres gerando um erro visual. O problema foi corrigido.
[28/11/2023] [Correção] Quando a conta estava em inglês, o termo agenda no calendário de tarefas era traduzido como 'Agenda'. O termo foi modificado para 'Schedule'.

[28/11/2023] [Correção] Erro de fluxo de bloqueio com campo de checkbox no filtro mostrava como se o valor fosse igual a "true" ou "false" e foi corrigido para mostrar "sim" e "não" de acordo com a linguagem do sistema.
[28/11/2023] [Correção] Quando a linguagem do usuário estava em inglês, o texto do tooltip (moldura flutuante "pop up" que abre quando passa-se o mouse) da busca de clientes tinha algumas irregularidades. O problema foi corrigido.

[28/11/2023] [Correção] Opcionais de produtos estava repetindo na geração da proposta. Correção fez um filtro para remover os duplicados.

[28/11/2023] [Correção] Ao editar uma venda, por conta de um erro no código, o campo de total das parcelas não estava sendo definido, fazendo com que o total fosse considerado como zero. O problema foi corrigido.
[28/11/2023] [Correção] A linha do cabeçalho estava com uma cor diferente das demais do modal de edição de campos.
[28/11/2023] [Correção] Ao configurar colunas de uma aba da tabela dinâmica, era possível selecionar o campo negócio origem mesmo já estando dentro do negócio origem, dando possibilidade de fazer uma seleção que não é aceita pelo backend, o que causava erros. Esse tipo de configuração foi bloqueado.
[28/11/2023] [Correção] Ao deletar uma tarefa no modo de visualização de tabela não estava removendo a linha da tabela. Correção realizada, agora ao deletar uma tarefa nessa visualização, a tabela é atualizada para virem os itens corretos.

[28/11/2023] [Correção] Ao filtrar os opcionais para seleção na proposta, por conta de um erro no código, os opcionais já marcados eram levados em consideração na contagem, causando erro nos filtros. O problema foi corrigido.

[28/11/2023] [Correção] Ao criar um novo estágio nas configurações do funil, não era possível ordenar os estágios sem antes atualizar a página. O comportamento foi corrigido para que seja possível editar a ordem no momento da criação do novo estágio.

[28/11/2023] [Correção] No módulo de e-mails, ao abrir um e-mail e clicar em "responder todos", não estava colocando os contatos de e-mails correto no campo de cópia.

[28/11/2023] [Correção] Nos checklsits, era possível adicionar os campos nativos 'Negócio.Tarefas'/'Cliente.Tarefas', mas esses dois campos nunca tiveram funcionalidade alguma no checklist. A inserção de ambos foi bloqueada.

[28/11/2023][Correção] Campo de usuário colocaborador estava sendo bloqueado por ser múltiplo.

[28/11/2023][Correção] Ao duplicar um negócio que possuía negócios derivados, caso o formulário de criação do negócio contenha o campo 'negócios derivados', os negócios derivados do card pai eram passados para o card filho. Foi feita uma melhoria para que nessa situação os cards derivados não sejam modificados.
[28/11/2023][Correção] Agora nos formulários, o campo desenvolvedor não terá mais limite de altura. Caso ele ultrapasse os 300px da altura limite inicial, por meio de um botão é possível expandí-lo. Além disso, é possível na própria configuração do campo definir que ele já venha expandido por padrão.
[28/11/2023][Correção] No módulo de Biblioteca, era possível acessar a configuração do formulário de coleção antes de criar a coleção, porém, não era possível configurar o formulário antes de ter a coleção criada. Foi removida a possibilidade de mapear campos antes da criação do formulário.
[28/11/2023][Correção] Aoatualizar a página no Ploomes, um dos dados da biblioteca de cache era lido de forma inválida por conta de um erro no código, o que causava um erro no console. O problema foi corrigido.

[28/11/2023] [Correção] Ao colocar um Cliente em registro de interação estava filtrando por ele, mas não vinculava corretamente quando salvava um novo contato relacionado. A correção está vinculando corretamente pelo Id.

[28/11/2023] [Correção] O envio de um Id utilizado no Omie para identificar atualizações em produtos de uma venda ocasionalmente era enviado errado, resultando em duplicações no Omie.

[28/11/2023] [Correção] Foi desabilitado as opções de 1 para muitos no mapeamento de campos na automação.

[28/11/2023] [Correção] Em contas com relatórios Beta, era possível editar os painéis já existentes e abas mesmo sem ter o módulo de relatórios habilitado. O comportamento foi corrigido para que fiquem bloqueados assim como acontece nos relatórios antigos.

[28/11/2023] [Correção] Ao duplicar/revisar um documento e modificar o modelo, caso o modelo que será utilizado tenha um filtro na seção de opcionais diferente do anterior, os opcionais eram ocultados mas não removidos do modelo, causando erros ao gerar o documento. O comportamento foi corrigido para que esses opcionais sejam removidos ao clicar no produto (no formulário do tipo modal) e ao abrir o documento (no formulário do tipo tela cheia).

[28/11/2023] [Correção] Ao criar ou editar negócio estava permitindo a criação do negócio com valor 0, mesmo dando nulo. A correção barrou a criação e edição desse campo para ser 0, mostrando uma mensagem específica quando tenta salvar.

[28/11/2023] [Correção] Quebra do rodapé estava quebrando porque uma classe do código estava conflitando. Como correção foi alterado nossa classe no front, porque estava com um nome muito genérico, podendo ocasionar outras vezes o mesmo problema.

[28/11/2023] [Correção] Nas métricas do relatório quando não temos o módulo de Lead ativo, não vai aparecer a opção para filtrar por informações de Lead.

[29/11/2023] [Correção] No aplicativo, ao abrir o formulário mini de criação de contato a empresa não era vinculada. Correção aplicada na versão 4.0.6 do app.

[29/11/2023] [Correção] Check in verificado não aparece quando é feito.

[29/11/2023][Correção] Ao adicionar um cliente/contato, o front faz um GET no backend para pegar todas as informações do contato. Durante esse intervalo de tempo, o usuário consegue clicar no botão de salvar, burlando algumas fórmulas. Foi adicionado um delay para que isso não ocorra mais.

[20/11/2023] [Correção] Uma venda criada no Ploomes integrou com o Omie com um produto a menos, por conta desse produto estar com a família errada no Ploomes. Apesar da venda ser criada no Ploomes, erros não tratados resultaram em erros ao salvar o Id Omie, impossibilitando a identificação posterior de duplicidade, causando duplicações no Omie ao editar a venda. Foi adicionada uma nova verificação para que isso não ocorra mais.

[29/11/2023][Correção] Os opcionais estavam com a ordem que apareciam no dropdown, não com a ordenação por adição.

[29/11/2023][Correção] Existia uma diferença na frase entre web e app quando não há negócios em uma etapa do funil. Foi corrigido e os dois estão iguais.

[29/11/2023][Correção] Uma frase do modal de bloqueio estava divergente entre web e aplicativo. Foi corrigido e estão iguais.

[29/11/2023][Correção] Era possível alterar estágio do negócio mesmo que ele esteja finalizado pelo APP. Foi corrigido e isso não ocorre mais.

[29/11/2023][Correção]Busca por 0 em cliente não estava retornando valor quando tinha o 0 no meio do número, Corrigido para mostrar mesmo que esteja no meio do telefone.

[29/11/2023][Correção] No app, campo "Cliente" não era exibido no card de registro de interação. A partir da versão 4.0.6, agora passa a ser exibido.

[29/11/2023][Correção] Problemas no mapeamento dinâmico para identificar as entidades corretas causavam o envio incorreto de informações de imposto para o Omie. Ajustamos as entidades corretas a serem mapeadas para corrigir o comportamento.

[30/11/2023] [Correção] Foi corrigido um problema de duplicação de vendas quando sincronizadas pelo botão de integração do Omie.

[30/11/2023] [Correção] Relatórios estava alterando permissões sozinho. Foi feita uma correção para que isso não ocorra mais.
