---
id: "42427577645719"
titulo: "Atualizações de Dezembro de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427577645719-Atualiza%C3%A7%C3%B5es-de-Dezembro-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:07Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8681994", "sync_hash_5664e97c4df6"]
---

# Atualizações de Dezembro de 2023

[01/12/2023] [Correção] Em Relatórios Beta, os gráficos não finalizavam a sincronização, havia uma consulta que era feita com nome errado por conta de um erro de digitação e foi corrigido.
[04/12/2023] [Correção] Correção da verificação para usar o código correto que vem no webhook do Omie, resolvendo o problema de atualização de produtos indevídos.

[05/12/2023] [Melhoria] Foram criados os estados do México.

[06/12/2023] [Correção] As opções de botões a serem clicados no aplicativo e na web depois de um alerta, quando a proposta saia do fluxo de aprovação depois de uma edição, eram distintas. O botão "Descartar proposta" no app realizava a mesma função de "Cancelar edição". Corrigido na versão 4.0.7 do app.

[06/12/2023] [Correção] No aplicativo, o alerta de fluxo de aprovação de uma proposta, não exibia o texto que tinha sido inserido no campo de alerta, mas sim um texto padrão. Corrigido na versão 4.0.7 do app.

[06/12/2023] [Correção] No aplicativo, o nome do fluxo de aprovação em uma proposta não era exibido na mensagem. Corrigido na versão 4.0.7 do app.

[06/12/2023] [Correção] A integração não trazia os campos customizados de conta e negócio do ActiveCampaign, agora estamos consultando eles diretamente de lá, nas entidades de cliente/pessoa trás os campos de Conta e Pessoa, e a entidade de negócio trás os campos de Conta e negócio no mapeamento do Ploomes.

[06/12/2023] [Correção] O campo Prospecção.Vendedor.Nome no mapeamento de campo estava com a ExternalFieldKey errada, fazendo com que viesse o nome do lead ao invés do nome do vendedor, subimos uma correção nesse ExternalFieldKey, e será precisa remover esse campo do mapeamento e incluir novamente.

[07/12/2023] [Correção] O tempo de carregamento para carregar os negócios dentro da tela de clientes estava muito elevado. Subiu uma melhoria no desempenho das requisições para melhorar o carregamento.

[07/12/2023] [Correção] Ao pesquisar um contato e clicar no mesmo, não estava puxando os dados corretamente daquele contato. Foi feita uma grande melhoria no sistema, agora podemos pegar número de contatos do tipo comercial (isso não era possível na versão anterior), além de estar mais eficaz e também mais confiável obter os dados corretos. Foi implementado uma melhoria que quando o usuário obtém os dados necessários, irá fechar automaticamente as informações dos contatos que precisamos abrir do lado esquerdo para obter as informações do usuário.

[08/12/2023] [Correção] Campos de Cliente mapeados na integração do RD Station não estavam vindo para o lead do Ploomes mesmo preenchido no RD Station. Correção propagada, agora o cliente deve vir com os campos atualizados do RD Station.

[11/12/2023] [Correção] Ao configurar as métricas de um painel no relatório antigo, as dimensões não estavam sendo limitadas conforme o tipo de gráfico, e o usuário estava conseguindo colocar muitas dimensões, quebrando o gráfico.

[11/12/2023] [Correção] Um usuário sem permissão para criar nova venda/documento/proposta conseguia ver na tela o botão de criação de novas propostas, vendas e documentos quando entrava por cliente e não havia itens nessas respectivas entidades.

[11/12/2023] [Correção] Borda de configuração de campos ficava com espessuras diferentes quando usávamos determinado zoom no monitor.
[11/12/2023] [Correção] Por conta de uma configuração incorreta no CSS, a borda das opções dos itens não aparecia em Checklists e em alguns outros locais. O problema foi corrigido.
[11/12/2023] [Correção] Nas configurações dos formulários, quando o nome de um campo era muito grande e sem espaços, acontecia uma sobreposição dos títulos dos campos. O problema foi corrigido.
[11/12/2023] [Correção] Campo de "Notificar contatos relacionados" em tarefas foi alterado para um nome mais condizente com sua funcionalidade e foi adicionado uma tooltip (moldura flutuante "pop up" que abre quando passa-se o mouse) para quem passar o mouse ver mais detalhes.

[11/12/2023] [Correção] Ao duplicar um card, os campos de checklist (que não estão no formulário) precisavam ser adicionados no card novo, então as informações do campo antigo eram todas copiadas e adicionadas ao novo, e entre essas informações estavam as opções do campos múltiplos. Isso fazia com que as opções fossem sempre copiadas, mesmo quando removidas. O comportamento foi corrigido copiando elas apenas caso não tenham sido alteradas no formulário.

[11/12/2023] [Correção] Botão de entrar em microsoft quebrava o texto quando estava na linguagem es.

[11/12/2023] [Correção] Ao acessar o um link de edição de negócio por um meio externo, o responsável do negócio era trocado para o usuário atual, pois o front entendia que aquilo era uma criação de negócio.

[11/12/2023] [Correção] Ao duplicar um card com anexos, caso o campo de anexo estivesse presente em dois checklists diferentes, o anexo do campo era criado duas vezes no card derivado. O comportamento foi corrigido para criar apenas um anexo nessa situação.

[11/12/2023] [Correção] Ao acessar o um link de edição de negócio por um meio externo, o formulário utilizado era o do último funil acessado pelo usuário, e não o daquela deal.

[11/12/2023] [Correção] No formulário mini de criação de clientes, caso algum campo usasse em suas variáveis um campo do criador, não era buscado o usuário atual, como acontece no formulário normal. O comportamento foi corrigido para que as variáveis dessas fórmulas sejam preenchidas corretamente para serem calculadas conforme seus campos de gatilho.

[11/12/2023] [Correção] Scroll não aparece para ver itens que estão sendo renderizados abaixo da tela no gráfico de análise histórica do funil. Correção mostra o scroll quando necessário.

[11/12/2023] [Correção] Ao interagir com um checklist que existe uma condicional para que outro checklist seja mostrado em tela, estava modificando a posição do scroll do usuário, causando confusão além de ser uma experiência de usuário ruim. Foi criado um skeleton indicando que está sendo carregado as opções do checklist, mantendo uma altura fixa dos componentes, além de não modificar a posição do scroll do usuário.

[11/12/2023] [Correção] Inicialização do chat intercom não estava acontecendo, fazendo o chat não abrir. Correção ajustou a inicialização do chat para funcionar independente de outras requisições que estavam impedindo de rodar.

[11/12/2023] [Melhoria] Na configuração do formulário externo em negócios, ao mapear o tipo da empresa como pessoa, não era possível escolher o CPF nos campos do formulário, apenas CNPJ. O comportamento foi alterado para permitir os campos de acordo com o tipo do cliente.

[11/12/2023] [Correção] Data do drilldown de Relatórios Beta de gráficos utilizando datas de registro de interação estavam com um dia a menos por considerar data com fuso horário. Correção realizada, agora dentro do drilldown a data corresponde com a data do gráfico.

[11/12/2023] [Correção] Os ícones de tarefa de cliente não condiziam com o tipo do cliente, agora, se for um contato vai aparecer o Ícone de contato corretamente.

[12/12/2023] [Correção] Abas não estavam carregando quando cliente não tinha integração com o PowerBi e não tinha filtro nas abas.

[12/12/2023] [Correção] Quando um produto tinha um opcional vinculado por meio de marcador, ao remover o opcional sem remover o produto antes, esse produto ficava 'salvo', e caso o opcional fosse adicionado novamente, ele já vinha com o produto selecionado, ao invés de abrir a lista.

[12/12/2023] [Correção] Visualização da caixa para inserir texto na entidade de chat estava quebrada, impossibilitando o envio de mensagens.

[12/12/2023] [Correção] Ao interagir com uma checklist condicional estava quebrando sua visualização.

[12/12/2023] [Correção] Frase de cancelamento de conta no Ploomes deixava ambiguidade com relação ao acesso à conta.

[12/12/2023] [Correção] Na criação de propostas, caso a proposta estivesse em formato modal e houvessem multiplos blocos de vínculos com filtros diferentes, alguns blocos de vínculos não apareciam por conta de um erro no código. O problema foi corrigido

[13/12/2023] [Correção] Na integração com o ClickSign, quando ocorria algum erro por parte da Ploomes no envio do documento para assinatura, o feedback desse erro não era mostrado ao usuário. Fizemos uma correção e, agora, caso ocorra algum erro interno, o usuário é notificado e pode consultar detalhes do erro dentro do cliente vinculado a esse documento.

[13/12/2023] [Correção] Ao duplicar um negócio o tipo do campo contato não estava sendo passado, fazendo com que calculasse a fórmula e passasse o valor errado. A correção ajustou a requisição para passar o tipo do contato e passar o valor apenas pelo campo de cliente.

[14/12/2023] [Correção] O tooltip ao passar o mouse encima de algum campo de seleção, como o de cliente, só era verificado se ele fosse maior que 20 caracteres, porém, essa verificação em campos maiores não faz sentido, foi corrigido para apenas aparecer o tooltip caso a informação quebre e não apareça inteiro

[18/12/2023] [Correção] A configuração de obrigatoriedade padrão do campo de descrição dos registros de interação no APP estava definida somente durante a criação. Foi adicionada essa configuração para edições de registros de interação.

[18/12/2023] [Correção] O aplicativo estava configurado para abrir o teclado automaticamente quando o usuário entrasse pela primeira vez na aba de comentários. Correção aplicada na versão 4.0.9 do app.

[18/12/2023] [Correção] O fluxo de resgate de motivos de perda em negócios recém criados foi corrigido para que eles sempre apareçam.

[18/12/2023] [Correção] Havia um bug no exportador em que em que abas/filtros com datas relativas as vezes apresentavam divergências entre a quantidade de dados exportador e a quantidade de linhas que apareciam no front, isso porque o frontend e o exportador estavam usando critérios diferentes para a filtragem dos dados.

[18/12/2023] [Correção] Alterado o comportamento do App de remover o contato do negócio ao não encontrar o cliente do negócio. Agora, só será removido quando o usuário remover o cliente ou mudar para um cliente que não seja empresa.

[19/12/2023] [Correção] Ordenação de métricas ao passar o mouse sobre gráfico não estava na ordem que era mostrada sem passar o mouse.

[19/12/2023] [Correção] Filtro de data relativa em relatórios beta estava passando operações que não existem para esse filtro. A correção faz com que o valor da operação resete ao entrar em data relativa impedindo de ocorrer o erro.

[19/12/2023] [Correção] Fórmula não puxa o ultimo atualizador do Negócio. Foi corrigido para que atualizasse e puxasse normalmente.

[19/12/2023] [Correção] Ordenação de relatórios está confundindo o index com a ordenação que o front passou. A correção corrige a numeração da ordenação na hora da criação de funil.

[19/12/2023] [Correção] Quando um documento era reprovado no fluxo de aprovação, o front exibia na lista de aprovadores um símbolo de 'certo' em todos, ao invés de um 'X' como era o esperado.

[19/12/2023] [Correção] Ao criar cliente por formulário mini, era possível clicar rápido no botão de salvar e gerar um cliente duplicado.

[19/12/2023] [Correção] Campo de produtos dentro de Proposta não funciona, mas estava deixando entrar nos campos de Proposta, causando confusão na hora de fazer fórmulas.

[19/12/2023] [Correção] Ao sair e voltar da visualização de tabela em negócios, não mantém a ultima aba selecionada. Correção ajustou para voltar com a aba selecionada anteriormente.

[19/12/2023] [Correção] O campo tipo % não aceitava valores de formula que passassem seu limite, resultando em um crash do app

[19/12/2023] [Correção] Contato do negócio não estava sendo puxado ao criar proposta caso o campo estivesse configurado no modelo.

[19/12/2023] [Correção] Os produtos adicionado na seção não eram lidos de forma correta pelo app, e isso levava a exclusão os produtos já adicionados ao adicionar uma nova seção. Isso foi corrigido através da busca do produto adicionado dentro do banco OFF, sendo assim possível realizar a leitura necessária dos dados do produto de forma rápida e leve.

[19/12/2023] [Correção] Filtros de data relativa não funcionavam quando o computador estava configurado para um horário maior que o UTC.

[19/12/2023] [Correção] Ao configurar um e-mail para ser enviado em ações de automações, campos múltiplos não eram destacados com uma cor rosa ao passar o mouse como acontece na configuração da proposta. Uma melhoria foi feita para que isso também aconteça na ação de automações. Foi feita uma melhoria para exibir como vermelho linhas que possuam uma multiple-field-key.

[19/12/2023] [Correção] Ao criar um filtro para puxar dados de cliente pelo Id, o Ploomes só permitia filtrar por IDs que possuam até 9 dígitos. A correção tira esse limite quando o campo for Id.

[19/12/2023] [Correção] No aplicativo, ao puxar o valor padrão de um campo do tipo opção pré-cadastrada cujo o nome dessa opção tem o mesmo nome em outro campo de opção pré-cadastrada resultava em um conflito de nomes, puxando o ID errado.

[19/12/2023] [Correção] Ao passar o mouse em anexo na entidade da biblioteca, a cor do texto era igual a cor do fundo do tooltip, dificultando a leitura do titulo do anexo. Agora o tooltip está com a cor do texto legível.

[20/12/2023] [Correção] A criação de contatos via api (integração, importação) vinha com o TypeId do telefone 0.

[20/12/2023] [Correção] Era possível ganhar Negócio com Proposta em aprovação. O que ocorria é que no front eram feitas algumas validações para confirmar se uma oportunidade podia ser ganha ou perdida. Porém, essas validações eram feitas somente pelo lado do front e não pelo back, o que podia às vezes fazer com que ele ganhasse de maneira indevida em alguns casos, já que o botão iria estar aparecendo pelo lado do front. Para evitar isso, essas mesmas validações foram incluídas no backend, para barrar no caso de ter uma Proposta em aprovação. Uma observação é que usuários de automação não são barrados por essas validações.

[21/12/2023] [Correção] Com o preload na requisição em abas de clientes apenas a primeira página retornava.

[22/12/2023] [Correção] A URL base que usamos para fazer integração com Zenvia será descontinuada, por esse motivo alteramos essa URL para que os clientes não sejam afetados em um futuro próximo.

[22/12/2023] [Correção] Ao tentar criar negócio pelo formulário mini quando não estava com o campo de Título configurado, voltava um erro dizendo que não foi possível criar o negócio, porém, criava mesmo assim.

[22/12/2023] [Correção] Ao realizar importação de Clientes pelo Excel, os telefones estavam sendo criados sem a máscara e isso estava impactando no uso do botão da extensão do WhatsApp, como estão sem o código 55, é exibido que o número compartilhado pela URL é inválido. Adicionamos uma nova funcionalidade para o botão do WhatsApp, ao clicar, abrimos um modal que permite a configuração da máscara antes de ir realmente à página com o número do contato no WhatsApp.

[22/12/2023] [Correção] Ao Abrir uma seção de produtos, na edição ou criação de uma proposta, estava travando bastante a interação de collapse e os textos estava flutuando na seção. Isso só acontecia quando tínhamos muitas seções.

[22/12/2023] [Correção] Ao pesquisar cliente ou alguma opção pré-cadastrada com requisição contendo preload, o retorno não vinha correto.

[22/12/2023] [Correção] Vendas estavam utilizando a configuração de tela cheia da proposta (configurada nos módulos do sistema) quando no funil estava selecionado para utilizar a configuração global.

[26/12/2023] [Correção] Foi feito um lock para evitar que automações executem de forma concorrente.

[26/12/2023] [Correção] Título de sessão dinâmica some ao mudar o idioma.

[28/12/2023] [Correção] No aplicativo, durante o fluxo de aprovação que busca a Equipe do criador da proposta, o App estava sempre mostrando esse valor como vazio no alerta, mesmo quando o usuário criador participava de alguma equipe. Foi adicionada a configuração que busca o valor da equipe do criador da proposta durante o fluxo de aprovação.

[28/12/2023] [Correção] Alterado comportamento do app offline quando gera uma nova proposta, evitando que fique em carregamento infinito.

[28/12/2023] [Correção] A lógica de verificação de modulo de propostas foi atualizada para verificar diretamente nas propriedades do perfil e conta do usuário se ele possui o modulo de propostas tanto online como offline.

[28/12/2023] [Correção] No aplicativo, o campo Título em documentos não possuía um limite de 200 caracteres assim como na Web, resultando em uma falha de criação ao enviar a requisição ao backend.

[28/12/2023] [Correção] Tela do app fica em branco ao tentar criar uma nova tarefa

[28/12/2023] [Correção] Foram feitos ajustes no comportamento de obrigatoriedade do campo de telefones do APP, impedindo valores vazios.

[04/01/2024] [Correção] A integração do LeadLovers criava marcadores vazios quando o campo estava mapeado mas não as tags do Leadlovers não eram enviadas no webhook. Corrigimos esse comportamento para ignorar tags vazias.
