---
id: "42427572788119"
titulo: "Atualizações de Outubro de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427572788119-Atualiza%C3%A7%C3%B5es-de-Outubro-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:38Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8444331", "sync_hash_39ccc3a9c04e"]
---

# Atualizações de Outubro de 2023

[03/10/2023] [Correção] Integração Meetime estava triplicando contatos no mesmo cliente, com o mesmo Id do Meetime. Na criação de pessoas encontramos alguns logs de busca por duplicidade de Id Meetime que falharam por muitas tentativas e isso acabou triplicando os contatos. O desenvolvedor subiu a correção adicionando uma trava para as criações serem processadas uma por uma para evitar esses erros.

[04/10/2023] [Correção] Contas com alto volume de automações e possíveis automações em loop geravam muitos eventos para a fila do Omie, causando horas de atraso nessa conta. Agora comparamos as alterações para ignorar webhooks que não causaram nenhuma alteração na entidade.

[04/10/2023] [Correção] Foram corrigidos problemas relacionados a mapeamentos da conta origem para o modelo no duplicador de contas.

[04/10/2023] [Correção] Em algumas contas, a exportação de abas para excel não estavam iniciando corretamente.

[04/10/2023] [Correção] Na integração com o Clicksign, uma requisição na API2 para buscar o documento a ser compartilhado esporadicamente causava timeout pela complexidade da consulta, acarretando erros na integração. Dividimos a requisição em duas partes, reduzindo o tempo de resposta e evitando novos timeouts.

[04/10/2023] [Correção] Atualizações da venda não apareciam nos registros do Ploomes

[05/10/2023] [Correção] Filtro de telefone na entidade de contato não estava sendo criado de forma correta.

[05/10/2023] [Correção] Fórmulas de campos de cliente da proposta e cliente do negócio não estavam com os valores aparecendo na edição da proposta, mesmo que na criação fossem puxados seus respectivos valores.

[05/10/2023] [Correção] Ao incluir um produto nos produtos da proposta, as variáveis de fórmula dos filtros por fórmula eram 'resetadas', fazendo com que o filtro parasse de funcionar. Foi feita a correção para que esse 'reset' não aconteça ao inserir o item.
[05/10/2023] [Correção] Ao criar registro de interação pelo card no funil, o retorno dos contatos relacionados não filtrava pelo cliente inserido automaticamente.

[05/10/2023] [Correção] Relatórios beta apresentando dados diferentes dos relatórios antigo. Onde gráficos com os mesmos filtros possuíam valores divergentes.

[05/10/2023] [Correção] Botão de salvar estava com tradução errada para o espanhol.

[05/10/2023] [Correção] Em campos de opções pré-cadastradas, ao buscar um valor e apagar repetidas vezes, em alguns momentos a busca falhava e no campo apareciam várias sugestões de criação de itens novos pesquisados anteriormente. Isso acontecia por conta de um erro na função que limpava as pesquisas anteriores. Este erro foi corrigido.

[05/10/2023] [Correção] Valor padrão de campo de formulários externos não estava salvando ao colocar um valor "0". Foi corrigido e agora o valor padrão do campo aceita colocar o valor "0", impedindo que ele seja "null" (vazio).

[05/10/2023] [Correção] Em relatórios Beta, troca de campos de opções vazio/não vazio para outro campo deste tipo nos filtros, em edição, estavam alterando o filtro.
[05/10/2023] [Correção] Em relatórios Beta, após salvamento o gráfico ficava em carregamento infinito/"bombinha" (mesmo os duplicados).

[05/10/2023] [Correção] Ao criar um negócio e adicionar o usuário colaborador igual ao responsável era exibida uma mensagem de aviso e não deixava adicionar. O comportamento foi corrigido e agora é permitido o usuário ser tanto o responsável quanto colaborador.

[05/10/2023] [Correção] Opção de exportar dados de um gráfico indicador em relatórios beta não funcionava.

[05/10/2023] [Correção] Ao digitar mais lento na busca geral, mostrava que não tinha valores, apesar da busca ainda não ter terminado, confundindo o usuário achando que não tem valor. Agora a pesquisa espera a busca acabar para tirar o carregamento e assim mostrar os resultados.

[05/10/2023] [Correção] Informações de coluna de aba sumiam quando a tela do Ploomes era recarregada.

[06/10/2023] [Correção] No app, o botão de baixar proposta aparecia mesmo quando ela ainda estava pendente de aprovação.

[06/10/2023] [Correção] Não estava sendo possível inserir produto do cliente em formulários de proposta.

[06/10/2023] [Correção] Quando o cliente possui muitas automações dá erro ao salvar.

[06/10/2023] [Correção] Funis que possuíam muitos checklists configurados, estavam apresentando problemas para abrir a página de criaçã e edição de checklists.

[06/10/2023] [Correção] Na configuração de fórmula do tipo integrada, estava com problema quando incluído JSONPath na parte de preencher campos com o resultado da fórmula, o motivo é que a função que estava sendo executada não pegava o caminho inteiro do JSON, e com isso, pegava apenas a primeira propriedade. Agora é possível acessar todo o caminho do objeto de retorno.

[06/10/2023] [Correção] Perfil de usuária era 'Revenda Silver' e ela não tinha permissão para ver outros usuários e mesmo assim conseguia vê-los.

[06/10/2023] [Correção] No aplicativo, em campos HTML com fórmula que concatenava os campos HTML de cada produto, essa concatenação não era possível.

[09/10/2023] [Correção] Em alguns documentos compartilhados compartilhados via link web, não estava sendo possível baixar o pdf.

[10/10/2023] [Correção] O gráfico "Reuniões do dia" do tipo Indicador não retornava a quantidade exata de cards abertos no dia.

[11/10/2023] [Correção] No aplicativo, quando estava habilitado o modo de "Trabalhar offline", ao criar uma tarefa, não eram exibidos os ícones dos tipos de tarefa (ex. Simples, Teleconferência, E-mail, etc.).

[11/10/2023] [Correção] No aplicativo, ao criar uma tarefa e selecionar os usuários, estavam sendo exibidos os usuários inativos e permitindo selecioná-los na tarefa.

Ao salvar a tarefa, ela salvava alguns usuários que estão inativos.

[11/10/2023] [Correção] No aplicativo, as funções de "Finalizar" e "Finalizar com observação" em tarefas estavam com o mesmo comportamento de redirecionar para o formulário de 'Finalizar com observação'.

[11/10/2023] [Correção] No aplicativo, ao criar uma tarefa pelo Cliente ou pelo Negócio, ele vinha selecionado com a data da última seleção feita no calendário de tarefas.
[11/10/2023] [Correção] No aplicativo, campos de porcentagem não tinham limite de quantidade de caracteres. Agora possui o mesmo limite da Web de 9 caracteres.

[11/10/2023] [Correção] No aplicativo, antes não havia os títulos: "Editar Proposta", "Revisar Proposta", "Editar Venda" e "Revisar Venda", ao editar ou revisar uma proposta, ou venda sempre aparecia "Editar/Revisar Documento" no topo da tela. Agora, os títulos citados foram adicionados.

[11/10/2023] [Correção] No aplicativo, o app fechava e exibia a mensagem "o app Ploomes apresenta falhas contínuas" ao tentar gerar uma proposta.

[11/10/2023] [Correção] Erro em importação de clientes utilizando o campo "Tipo Cliente".

[11/10/2023] [Correção] No aplicativo, caso o funil estivesse configurado para criar venda ao ganhar negócio, mas o modulo de venda estivesse desabilitado da conta, ele seguia com a criação da venda no iOS e impedia de dar ganho no Android.

[11/10/2023] [Correção] Algumas fórmulas na criação de proposta estavam causando crash no aplicativo, fazendo-o com que fechasse sozinho.

[11/10/2023] [Correção] No aplicativo, ao trocar a visualização dos cards existia um delay que não carregava os negócios do estágio em exibição a menos que mudasse de estágio e voltasse novamente.

[11/10/2023] [Correção] Não estava sendo possível habilitar integração com o Mailchimp.

[11/10/2023] [Correção] No aplicativo, ao fazer login pelo modo offline, clientes e negócios criados não estavam subindo para o modo online.

[11/10/2023] [Correção] No aplicativo, ao clicar para editar venda, o App travava, não permitindo preencher nenhum campo.

[11/10/2023] [Correção] No aplicativo, ao compartilhar um documento por WhatsApp no sistema iOS, a mensagem estava quebrada, impossibilitando a leitura e o funcionamento do link para abrir o documento.

[11/10/2023] [Correção] Contador de tarefas contabilizando errado.

[11/10/2023] [Correção] No aplicativo, algumas fórmulas causavam travamento no app ao inserir produto na proposta.

[16/10/2023] [Correção] Automação não preenchendo campo de anexo.

[16/10/2023] [Correção] Adicionamos uma mensagem de erro para quando tentar enviar um email via automação que possua o assunto maior que 150 caracteres ou os destinatários maiores que 500 caracteres (somados), o que é esperado que não funcione por ser uma limitação.

[16/10/2023] [Correção] Gráficos de relatórios beta não finalizavam a sincronização de dados.

[18/10/2023] [Correção] Ao inserir um produto da proposta, as fórmulas que buscavam informações do produto não eram engatilhadas por conta de um problema de tempo de execução entre as fórmulas. Uma correção foi aplicada para corrigir o problema.

[23/10/2023] [Correção] O campo 'Cidade de Prestação de Serviço' era enviado em toda criação de Ordem de Serviço no Omie, sobrescrevendo regras de preenchimento desse campo que foram configuradas no Omie do cliente. Adicionamos um novo campo,

"Não preencher cidade de prestação de serviço na criação de ordens de serviço", na integração que permite desabilitar o envio desse campo ao criar vendas com serviços pelo Ploomes.

[24/10/2023] [Correção] No aplicativo, quando editávamos uma Venda, ao selecionar um novo modelo, eram exibidos os modelos de Proposta em vez de exibir os modelos de Venda. Ocorria o mesmo quando tentávamos editar um Documento. Correção aplicada na versão 4.0.1 do App.

[24/10/2023] [Correção] No aplicativo, ao estar no modo Offline no App e alterar para Online, era exibido uma tela branca e após para tela de carregamento e às vezes demorava um tempo para carregar, aproximadamente 3 minutos. Correção aplicada na versão 4.0.1 do App.
[24/10/2023] [Correção] No aplicativo, era possível preencher campos de contato de checklist de Cards que não possuíam Contato na versão da revitalização do App. Correção realizada na versão 4.0.1 onde agora é bloqueado o preenchimento desses campos quando o Card não possui Contato.

[24/10/2023] [Correção] Implementado um mecanismo para buscar nomes de campos em outros idiomas quando não for encontrado um nome no idioma do usuário.

[24/10/2023] [Correção] No aplicativo, quando passávamos os meses muito rápido, o calendário perdia o formato tradicional e ficava com a data "2022-01-20" (dependendo do mês) aparecendo. Correção aplicada na versão 4.0.1 do App.

[24/10/2023] [Correção] O problema ocorrido era uma duplicidade no envio da venda gerada em funis que tinham as opções "Criar venda automaticamente ao ganhar negócio" e "Nova venda ao ganhar negócio" marcadas. Para solucionar isso, fizemos uma mudança na forma como as informações são enviadas quando um negócio é concluído. Agora, garantimos que, se houver uma venda associada, ela será enviada junto com as informações do negócio, evitando duplicações.

[24/10/2023] [Correção - Subida de hotfix] Ordens de serviço geradas pelo usuário no Ploomes não integravam com o Omie. Os webhooks de criação retornavam o erro "Object reference not set to an instance of an object.".
[24/10/2023] [Correção] No aplicativo, não era possível editar os telefones do cliente tipo Pessoa. O problema ocorria quando o cliente Pessoa possuía mais de um telefone, ao editar o segundo telefone o formulário acusava que possuía campos obrigatórios e não permitia salvar o cliente com 2 telefones, era necessário deixar somente com um telefone para salvar. Correção aplicada na versão 4.0.1 do App.

[24/10/2023] [Correção] No aplicativo, estava travando no carregamento inicial para usuários que não possuíam metas cadastradas na tela inicial. Correção aplicada na versão 4.0.1 do App.

[24/10/2023] [Correção] No aplicativo, ao reabrir um negócio no offline, aparecia uma caixinha carregando na tela do usuário que só desaparecia caso o usuário arrastasse ela para baixo. Isso foi resolvido removendo essa caixa de carregamento após a reabertura do negócio offline. Correção aplicada na versão 4.0.1 do App.

[24/10/2023] [Correção] Timeout ao abrir a última página do histórico de automações.

[24/10/2023] [Correção] No aplicativo o campo de responsável do formulário mini de cliente não era preenchido automaticamente.

[25/10/2023] [Correção] Permissões de painel em Relatórios Beta estava com uma inconsistência que salvava as permissões como "Todos da empresa" em vez do que o usuário estava mandando.

[26/10/2023] [Correção] Cards ganhos e Cards em aberto derivados de um Card origem, estavam ficando com motivos de perda do Card de origem. Estava acontecendo com todos os Cards derivados. Foi feito uma modificação na parte de criação de Negócio para sempre garantir que a propriedade de motivo de perda esteja vazia ao fim da criação do Negócio.

[26/10/2023] [Correção] Filtro de tarefas agendadas não funciona.

[26/10/2023] [Correção] Na extensão do Whatsapp, informações da integração não estava sendo exibida caso os cookies não fossem encontrados.

[26/10/2023] [Correção] Ao salvar um valor com resultado de fórmula como "Infinity" que é resultante de uma fórmula incorreta, a proposta era zerada.

[26/10/2023] [Correção] Não existia um retorno de erro informando que o assunto de uma automação de email passou de 200 caracteres (É esperado via fórmula)

[27/10/2023] [Correção] No aplicativo, ao ter a Autenticação multifator ativa, não estava permitindo inserir o código de autenticação. Correção aplicada na versão 4.0.2 do App.

[27/10/2023] [Correção] No aplicativo, no formulário de Negócio estava acontecendo um problema ao rodar fórmulas que utilizavam as propriedades de estágio e funil dos Negócios. Ao montar o formulário, as variáveis dessa fórmula não estavam conseguindo acessar o valor do estágio e do funil, e por isso iniciavam como vazias, o que fazia essas fórmulas não conseguirem rodar. Correção aplicada na versão 4.0.2 do App.

[27/10/2023] [Correção] No aplicativo, algumas fórmulas perdiam a referência de váriaveis que eram adicionados como gatilho, fazendo com que não calculasse corretamente.

[27/10/2023] [Correção] No aplicativo não era possível pesquisar clientes a partir da razão social ou CNPJ.

[27/10/2023] [Correção] No aplicativo, ao editar uma tarefa e colocar um cliente, a opção 'Finalizar com observação' só era exibida quando saia da tarefa e voltava.

[27/10/2023] [Correção] Tarefa excluída aparecia na listagem e só saia quando quando era atualizada a tela.

[27/10/2023] [Correção] No aplicativo, dentro de um funil de negócios, com mais de um estágio, na visualização da coluna de primeiro estágio, ao tentar movimentar card para a esquerda ia para a direita.

[27/10/2023] [Correção] No aplicativo, um usuário não conseguia finalizar/finalizar com observações tarefas que foram criadas por outro usuário, diferente do comportamento na web.

[27/10/2023] [Correção] No aplicativo, era possível criar um novo contato a partir de um cliente pessoa, no campo de contatos relacionados da tarefa. Incluindo o cliente pessoa como empresa do contato criado.

[27/10/2023] [Correção] No aplicativo, os textos do alerta de fluxo de aprovação na proposta mostravam "vazio" no lugar de "0".

[27/10/2023] [Correção] No aplicativo, quando era criada uma proposta, não caia no fluxo de aprovação de bloqueio, somente quando tentava editá-la era bloqueada.

[27/10/2023] [Correção] No aplicativo, os filtros não eram mostrados em ordem alfabética.

[27/10/2023] [Correção] O app não estava funcionando corretamente ao filtrar negócios, ele não exibia negócios ao utilizar filtro.

[27/10/2023] [Correção] Na integração com o Outlook foi adicionado um aviso da limitação de tarefas recorrentes.

[30/10/2023] [Correção] Problema no duplicador de contas ao duplicar modelo que possui uma automação utilizando campo de integração nativa.

[30/10/2023] [Correção] Filtro simples aplicado ao funil de negócios não retornava resultados, quebrando a requisição, apresentando o erro 408 Query Timeout.

[30/10/2023] [Correção] Ao criar um registro de interação, a descrição do registro, bem como outros campos, ficavam duplicados, caso o usuário abrisse o registro sem atualizar a tela. Foi aplicada a correção para não duplicar mais os campos.

[30/10/2023] [Correção] Tela branca em relatórios por causa de uma variável tentando pegar um valor inexistente.

[30/10/2023] [Correção] Foi adicionado um ícone com um tooltip ao editar as regras de um perfil, na seção de atividades que pode visualizar, o motivo é que não estava tão claro para o usuários como funcionava essa permissão.

[30/10/2023] [Correção] Ao criar um negócio sem cliente, era possível no checklist preencher o contato do negócio, pois o mesmo não ficava bloqueado como na tela de edição. Foi feita uma tratativa para bloquear o campo de contato nesta situação.

[30/10/2023] [Correção] Ao deletar um filtro rápido em relatórios beta, o Ploomes retornava o nome dele como 'Undefined'.

[30/10/2023] [Correção] Após adicionar um produto de cliente na proposta, ao substituir o produto, o filtro não estava sendo aplicado.

[30/10/2023] [Correção] Ao editar um fluxo de aprovação com marcador, não aparecia a cor desse marcador.

[30/10/2023] [Correção] Ao criar/editar uma proposta/venda ou documento o campo contato tinha comportamentos diferentes em cada documento, era possível por exemplo em alguns adicionar contato mesmo quando o cliente era do tipo pessoa, alguns só permitiam isso na edição, e não na criação, e outros não filtravam os contatos do cliente, enquanto uns filtravam.

[30/10/2023] [Correção] Ao criar/editar uma proposta/venda ou documento o campo contato tinha comportamentos diferentes em cada documento, era possível por exemplo em alguns adicionar contato mesmo quando o cliente era do tipo pessoa, alguns só permitiam isso na edição, e não na criação, e outros não filtravam os contatos do cliente, enquanto uns filtravam.

[30/10/2023] [Correção] Ao editar as variáveis da fórmula, o front estava buscando qual editar pela sequência, e não pelo campo. Por conta disso, quando em uma fórmula havia mais de uma variável e na outra apenas uma delas, era editada a variável errada. Foi aplicada uma correção para que a variável seja editada de acordo com o campo, e não com a sequência.

[30/10/2023] [Correção] Na integração com o Zenvia, caso o Ploomes não obtivesse retorno da consulta com o Zenvia, o áudio acabava sendo perdido e o registro de interação não era criado.

[30/10/2023] [Correção] Usuários que tinham o perfil trocado para um com diferentes permissões, ainda estava visualizando os funis da permissão antiga.

[30/10/2023] [Correção] Ao usar um filtro em funil de negócios, o Ploomes retorna erro 408 Query Timeout na requisição GET em /Deals.

[30/10/2023] [Correção] Alguns gráficos de relatórios beta estavam exibindo no drilldown tarefas que não possuiam cliente, logo, o usuário não conseguia visualizá-la.
[30/10/2023] [Correção] Layout do áudio do Zenvia estava quebrando quando o campo era pequeno por não ter tamanho mínimo. Foi corrigido.

[31/10/2023] [Correção] Ao configurar uma automação que cria um negócio em suas ações, o campo de estágio do funil não vinha com o primeiro estágio como padrão, e quando esse funil escolhido possuía apenas um estágio, o campo ficava travado e não permitia a escolha. O comportamento foi corrigido mantendo o campo bloqueado mas selecionando automaticamente o único estágio disponível.

[31/10/2023] [Correção] Gráficos de coluna não ordenavam pelas métricas, fazendo com que a ordenação do usuário fosse ignorada.

[31/10/2023] [Correção] Foi adicionada mais uma camada de validação de CNPJ na criação de cliente, quando o campo for obrigatório e o usuário digitar e sair do campo.
[31/10/2023] [Correção] Em relatórios Beta, quando um gráfico possuía um filtro com um campo contendo operação de "Não vazio" e alteramos o valor de outro campo, esse filtro alterava para "Vazio". Foi adicionada uma verificação para corrigir e poder identificar corretamente o filtro com esse operador.

[31/10/2023] [Correção] Campos dos checklists de Negócios estavam sendo limpos quando criava automaticamente uma nova checklist.
