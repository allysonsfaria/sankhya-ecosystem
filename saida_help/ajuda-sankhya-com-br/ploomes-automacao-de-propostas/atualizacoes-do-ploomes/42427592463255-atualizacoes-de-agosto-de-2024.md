---
id: "42427592463255"
titulo: "Atualizações de Agosto de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427592463255-Atualiza%C3%A7%C3%B5es-de-Agosto-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:10Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_6b55ea9ad6b7", "ploomes_9691360"]
---

# Atualizações de Agosto de 2024

## [01/08/2024] [Correção]

- Quando um nome com mais de 100 caracteres era atribuído a um modelo de email, aparecia um erro genérico. Agora aparece uma mensagem de erro indicando que o limite de 100 caracteres foi ultrapassado.
- No módulo de biblioteca, ao tentar vincular uma entidade, quando o usuário clicava nas configurações da tabela o modal ficava atrás do menu. Agora, o modal aparece na frente.
- Automações desabilitadas exibiam o botão 'Salvar e executar agora', que não executava a automação justamente por ela estar desativada. Esse botão foi removido nesses casos, e agora automações desabilitadas só contam com o botão tradicional de 'Salvar'.
- Na modal de registros de interação, caso o nome de alguma entidade fosse muito grande (em Dados Básicos), em alguns casos, ocorria uma quebra de layout. Agora, não há mais esse problema, foi aplicado um truncate nos nomes das entidades.
- Corrigimos um problema na nossa API de formulas que ocasionava retornos vazios quando havia um escape em aspas (\"). Agora essas formulas funcionam normalmente e foi implementado um limite de tempo de execução (5s), caso esse limite seja excedido, irá retornar vazio ("").
- Agora não é mais necessário scrollar verticalmente até o final para conseguir ver a barra de scroll horizontal no modal de vincular entidades, no modal de editar arquivo e na visualização de tabela na biblioteca.
- Em formulários externos, campos que onde se pode selecionar opções (Responsável, Cliente, Opções pré-cadastradas) sumiam as opções no formulário externo após salvar ele, agora as opções aparecem normalmente.
- Na modal de criação de grupo, temos a opção de criar produtos vinculados à esse grupo que está sendo criado. Porém, havia a opção de editar o grupo desse produto, sendo que ele só pode possuir vínculo com o grupo que já está sendo criado. Agora, essa opção (de editar o grupo do produto) foi desabilitada para a modal de criação de grupo.

## [02/08/2024] [Correção]

- Ao puxar por fórmula um campo de proposta em documento, o valor só era buscado na criação, mas não funcionava corretamente na edição. O comportamento foi corrigido.
- Foi feito uma modificação no tamanho mínimo da exibição de campos do tipo 'Cliente' dentro de um produto da proposta, agora o campo está mais largo e a visualização está melhor.
- Na notificação de aprovação de proposta, o usuário que aparecia era o criador do negócio e não o criador da proposta. Agora, a notificação mostra o criador da proposta.
- Na edição de produto, na aba de produto do cliente, ao reordenar as colunas da tabela o título das colunas era reordenado, mas o conteúdo não seguia a reordenação. Agora, as colunas são reordenadas corretamente.
- Um usuário não administrador, ao tentar integrar com o Google Calendar pela primeira vez, recebia um erro de não autorizado.
- Integração Neppo. Modal de salvar sessão estava abrindo dentro do componente, impossibilitando a utilização. A correção faz o modal abrir no componente certo.
- Ao editar um campo multilinha de um produto já inserido, as fórmulas de bloco que o continham como variável não eram engatilhadas.
- Ao deletar uma opção padrão de um campo de opções pré-cadastradas, a mesma continuava sendo opção padrão, causando um erro no momento de preencher as opções na proposta e inserir o produto. Agora há um tratamento do erro e uma mensagem para o usuário. Além disso, foram feitas 3 melhorias de usabilidade na edição de opções, permitindo uma melhor agilidade na criação delas.

## [06/08/2024] [Correção]

- No app, aparecia um fundo roxo durante a animação de subida do teclado. Os desenvolvedores implementaram uma correção para esse fundo roxo não ser exibido.
- No app, a validação de limpar campo do tipo texto simples estava incorreta. Os desenvolvedores implementaram uma correção, e agora a validação está funcionando corretamente.
- No app, foi aplicada uma correção na montagem da url com filtro personalizado em negócios, havia uma lógica que fazia com que fosse adicionado um `$expand` em `Products` dentro de um `$expand` em `OtherProperties`, fazendo com que o GET de Negócios utilizando o filtro não funcionasse.

## [07/08/2024] [Correção]

- Os filtros de data no relatório beta não consideravam campos vazios quando era filtrado por data e utilizava data fixa ou relativa. Esse comportamento foi corrigido.
- No aplicativo, corrigido uma validação para limpar um campo do tipo Texto Simples em alguns casos e que era executada quando não deveria, esse bug foi corrigido na versão 4.6.1 do aplicativo.
- Os gráficos dos relatórios beta não contabilizavam as informações de usuários suspensos. Os desenvolvedores implementaram uma correção, e agora, informações de usuários suspensos também são contabilizadas.
- Na integração com o ActiveCampaign havia um problema na criação de um cliente pessoa, porque a requisição de criação sempre tentava utilizar o id da empresa (que não existia) ao buscar a deal na API2. Agora os ids que devem ser utilizados na busca são selecionados condicionalmente, de acordo com a configuração do cliente.

## [08/08/2024] [Correção]

- Quando o idioma era trocado no App, em alguns campos nativos o idioma anterior se mantinha. Correção foi aplicada e agora os campos são atualizados para o idioma selecionado.
- Na integração Omie foi feita uma correção para que os itens na fila não sejam substituídos. Além disso, também foi alterado como manipulamos os kits dentro da nossa API.
- Ao ganhar um negócio cujo cliente está com o status Inativo, o status do cliente era automaticamente alterado para Ativo. Esse comportamento foi removido. Agora, quando um negócio de um cliente com status Inativo é ganho, ele permanece com status Inativo.

## [12/08/2024] [Correção]

- Para evitar o problema de instabilidade na comunicação com a API da Clicksign durante a adição de um novo assinante, foram implementadas três tentativas de reenvio em caso de falha na comunicação com a API da Clicksign.

## [13/08/2024] [Correção]

- Foi corrigido o retorno do @OData.context nas requisições da API2 que retornavam com http e quebravam consultas via PowerBI.
- Quando uma automação executava em paralelo, em alguns casos uma sobrescrevia a ação da outra, e gerava uma inconsistência no resultado. Foi adicionado um lock por automação (configuração da conta).

## [14/08/2024] [Correção]

- Ao tentar enviar um e-mail com o campo "Assunto" vazio, um erro era apresentado e o envio era impedido, pois a requisição não permitia um campo vazio. Para resolver esse problema, os desenvolvedores implementaram uma correção que tornou o preenchimento do campo "Assunto" obrigatório.
- As mensagens de e-mail não estavam aparecendo em telas pequenas do Safari. Sendo assim, os desenvolvedores implementaram uma correção que ajustou o estilo da página para permitir a visualização.
- O caminho Venda.Contato.Empresa não funcionava via fórmulas. Agora ele funciona buscando corretamente o nome da empresa.
- Em alguns casos a integração do Facebok Leads Ads criava negócios apenas com vínculos de contato, mesmo que uma empresa fosse criada. Corrigimos o problema para que ambos os vínculos sejam criados.
- Quando duas ações alteravam a quantidade de tarefas ao mesmo tempo, apenas uma delas era contabilizada. Isso podia ocorrer caso algum usuário criar uma tarefa enquanto outro cria ou em caso duas automações executem ao mesmo tempo, e aí apenas uma das ações alterava o contador, ficando com o valor incorreto. Foi adicionado um bloqueio para evitar esse comportamento.
- No dia 13/08 ocorreu por causa da subida referente a automações, para que automações do tipo Proposta/Venda/Documento atualizassem o documento apenas no fim da ultima execução, isso causou um loop na execução de automações em algumas contas. Essa subida foi revertida no dia 14/08.

## [15/08/2024] [Correção]

- Quando tínhamos nomes de entidade muito grandes, o layout do gerador de filtro ultrapassava a tela impossibilitando a configuração dos filtros.

  Houve uma melhoria na arquitetura de estilização do componente de gerador de filtros, deixando cada célula da configuração mais responsiva e impedindo que quebre.
- Não existia uma mensagem de erro quando tentávamos salvar um filtro novo sem configurar os parâmetros. Agora, quando o usuário tenta salvar o filtro sem nenhum parâmetro aparece uma mensagem alertando.
- Os formulários externos agora verificam se estão sendo criados/editados a partir de um funil específico. Se sim, o campo 'Selecionar funil' já vem autopreenchido, e sem possibilidade de edição.
- Ao abrir um e-mail da pasta de Enviados diretamente pela URL, na barra de ferramentas aparecia o botão de mover e-mail, mas não é possível enviar um e-mail enviado para outra pasta. Agora, ao abrir o e-mail enviado diretamente pela URL, o botão de mover não aparece.
- Antes, quando editávamos tarefas todos os campos eram re-enviados, o que gerava um bug no calendário, expulsando contatos relacionados da tarefa, e também deixava mais lenta a API, agora, só enviaremos os campos necessários e que realmente foram alterados.
- Os formulários externos agora verificam se estão sendo criados/editados a partir de um funil específico. Se sim, o campo 'Selecionar funil' já vem autopreenchido, e sem possibilidade de edição.
- Fórmula com campo dinâmico em formulário mini de cliente agora está puxando os valores dos campos dinâmicos e do responsável do cliente para o cálculo corretamente.
- Erros de formulário externo relacionados à campos de negócios de não apareciam na criação do formulário.
- Formulário mini de criação não tinha tratativas de erro caso houvesse campo obrigatório.
- Era possível criar filtros com a condição de contém e não contém com valor nulo. Agora, aparece uma mensagem de erro informando que isso não pode ser feito.
- Agora existe mais uma mensagem que informa ao usuário que em importação, ao mapear o campo "Nome da Cidade", é obrigatório que as informações do campo estejam preenchidas.
- A validação das checklists ocorria em paralelo com a mudança de estado, o que causava um bug: quando havia duas checklists com filtros de opções diferentes, ao alternar entre essas opções, ambas passavam pela validação devido ao paralelismo. Isso fazia com que o botão para avançar para o próximo estágio desaparecesse. Os desenvolvedores implementaram uma correção, e agora esse problema foi resolvido.

## [16/08/2024] [Correção]

- Algumas requisições para validar informações dos usuários no Ploomes estavam demorando muito para serem executadas, o que causava um atraso significativo na sincronização de e-mails de alguns usuários. Sendo assim, realizamos o cache dessas requisições para evitar lentidões.
- Na integração com o Omie, quando a opção "As vendas feitas no Omie não serão sincronizadas com o Ploomes" estava ativada, alterações realizadas no Omie em vendas criadas dentro do Ploomes não estavam sendo sincronizadas.

## [19/08/2024] [Correção]

- No app, foi adicionado um filtro anual para garantir que os itens do calendário sejam recarregados ao mudar de ano.
- No app, quando não havia um título nem um contato relacionado, o aplicativo exibia a mensagem "No Title". Para resolver essa divergência entre o formulário e a tela de visualização, foi adicionada a variável de idioma selecionado, garantindo que campos sem título sejam exibidos corretamente.
- No app, não possuia tratamento para criação de documentos sem cliente. Foi adicionado esse tratamento através de um alerta de erro ao tentar criar um documento sem cliente vinculado.
- No app, foi implementado tratamento para evitar múltiplas interações rápidas, prevenindo a abertura simultânea de opções na tela do cliente.
- No app, foi adicionado um controle de frequência das interações do usuário na tela de proposta.
- No app, foi corrigido problema de limpeza prematura das opções de modelo, que agora ocorre após a navegação.
- No app, uma alteração de estado desnecessário na navegação ocasionava a re-renderização de tola a tela. A alteração do estado foi removida.
- No app, ao tentar criar uma proposta dava erro de card obrigatório, mesmo estando dentro de um card. Comportamento corrigido na versão 4.8.0 do app.

## [20/08/2024] [Correção]

- No app, ajustado comportamento para desabilitar a seleção de cliente ao editar negócio, igualando à versão web.
- No app, anteriormente, ao criar uma venda com moeda diferente de real, ainda era apresentado R$ ao visualizar as vendas do negócio. Agora o comportamento vai buscar o tipo de moeda baseando no id que vem do documento e assim atribuir o valor correto da moeda.
- No app, havia uma constante com nome "document\_title" para representar o título do documento quando não se tinha valor ainda. Foi adicionado um titulo genérico de carregamento.
- No App, ao criar um registro de interação com marcador, quando editamos e o removemos, ao salvar o registro ele mostrava como se o marcador não tivesse sido removido. Havia uma divergência nos dados que eram passados no retorno da edição do registro de interação. Foi adicionado um tratamento para lidar com a inconsistência dos dados. Correção aplicada na versão 4.8.0 do App.
- O app agora permite inserir e salvar HTML no texto de descrição do registro de interação.
- No app, mudava por instantes o nome do modelo para você não possui modelos ao editar e salvar uma proposta, documento ou venda, esse comportamento foi corrigido.
- No app, foram corrigidos bugs que impediam a criação de negócios em funis recém-criados. Agora, o app bloqueia a criação de negócios sem formulário e realiza mais consultas durante a sincronização dos formulários.
- No app, faltava um tratamento para lidar com a troca de conexão na timeline. Os desenvolvedores adicionaram esse tratamento, mapeando o estado de conexão atual.
- No app, foi corrigido um erro de formatação que impedia a exibição do símbolo # antes do número da proposta no card.
- No app, foi adicionado um botão de limpeza nos campos de endereço, anexo e cor em seus respectivos modais.
- A barra de busca geral não estava sobrepondo o cabeçalho da página.

## [21/08/2024] [Correção]

- Na integração com o DocuSign, o campo "Assunto do email de requisição de assinatura" não era obrigatório, mas é essencial para o funcionamento da integração. Agora não é mais possível ativar a integração com o Docusign sem que esse campo esteja preenchido
- No App, cliente tipo Pessoa Física tinha a permissão de preencher o campo CNPJ. Se um checklist solicitasse CPF e CNPJ, caso colocasse uma pessoa e editasse o CNPJ no checklist, o valor digitado pulava para o campo do CPF. Agora não é mais permitido e as mensagens são exibidas: "Cliente do tipo Pessoa não possui CNPJ." (no campo de CNPJ, em negócios com cliente tipo Pessoa) e "Cliente do tipo Empresa não possui CPF." (no campo de CPF, em negócios com cliente tipo Empresa). Foi corrigido na versão 4.8.1 do App.
- Quando um usuário fazia duas alterações ou criações de campos em sequência, o cache corria o risco de ficar desatualizado, ignorando a última modificação. Para evitar esse problema, adicionamos uma validação durante o salvamento do cache, que verifica se houve alguma alteração nesse intervalo de tempo.

## [22/08/2024] [Correção]

- Agora, ao remover o cliente em tabela de negócios ou dentro da página de negócios, uma mensagem de confirmação aparece informando que, ao remover o cliente, o contato também será removido.
- Na entidade de produto da proposta, existia dois campos de produto do cliente no

  mapeamento de valor padrão, porém, o segundo era adicionado depois que bloqueávamos os campos inválidos. Isso gerava uma ambiguidade, pois, além de existir um campo duplicado na configuração, todos os campos de produto do cliente do duplicado vinham desbloqueados, parecendo que poderiam ser mapeados. No entanto, ao inseri-los, nada aconteceria. Agora, só existirá um campo de produto do cliente no mapeamento.
- No app, ao criar um filtro no bloco de produto no modelo, após de já criado um documento com um produto que não se encaixa no filtro, era criado um bloco de produto vazio no documento depois de uma edição.

## [23/08/2024] [Correção]

- Usuários sem permissão no painel não conseguirão mais redimensionar ou mover painéis, mesmo que apenas visualmente, nos relatórios beta.
- Na página de negócio, ao remover o cliente, o contato também será removido.
- A subida realizada no dia 22/08 continha um erro no código que quebrava a execução de algumas formulas com determinadas configurações, o código foi corrigido.
- Em relatórios beta, ao remover qualquer filtro, exceto o último, todos os valores dos filtros eram resetados. Agora, é possível remover um filtro sem afetar os demais.
- Nas ações de automação, agora todo o caminho de campos aparecerá, permitindo a identificação exata de qual campo selecionado está sendo modificado, mesmo quando entrarmos em outra entidade para selecionar um campo.
- Foram adicionadas novas perguntas opcionais na pesquisa de NPS. Agora, se o usuário usar alguma das palavras-chave (confuso, intuitivo ou complexo) uma nova pergunta vai aparecer para que o usuário detalhe o problema.
- Quando o HTML dava erro dentro da tarefa, a conversão quebrava e a tela de tarefa ficava em branco. Os desenvolvedores implementaram uma correção para lidar com esses erros de HTML, garantindo que a tela da tarefa não fique mais em branco.

## [28/08/2024] [Correção]

- Um delay no processamento das mensagens fez com que o serviço responsável por criar registros de interação enviasse a mesma mensagem duas vezes para que o registro fosse criado. Sendo assim, os desenvolvedores implementaram uma otimização no processamento de mensagens e na criação dos registros de interação
- Uma subida recente impedia o pleno funcionamento da nossa API de cacheamento de entidades que é utilizada pelos relatórios beta e ocasionava na lentidão principalmente em casos de várias requisições simultãneas. Fizemos a reversão da subida e o problema foi corrigido.
- Em alguns casos vendas estavam sendo duplicadas porque a notificação de "venda incluída" do Omie era processada antes que a venda criada na Ploomes tivesse sido vinculada corretamente à venda correspondente no Omie. Agora, após a criação da venda no Omie, o ID da venda na Ploomes é armazenada fora da entidade temporariamente, em um cache. Quando a notificação de "venda incluída" é recebida, ao invés de validar se já existe um vínculo entre as vendas nos campos da entidade, o sistema verifica se esse ID existe no cache. Se estiver, o sistema realiza apenas a atualização necessária, evitando a duplicação de registros.

## [30/08/2024] [Correção]

- Não estava sendo possível preencher valores decimais com 0 em campos do tipo valor decimal. Ex: 0.1, 0.5, 0.7, etc... Também ocorria um arredondamento do valor decimal para inteiro em campos de quantidade de Produto. Os comportamentos foram corrigidos.
- Tivemos um problema de conexão com a fila do RD Station pois a API estava em uma versão antiga. Sendo assim, os desenvolvedores atualizaram a versão da API.
- Em campos com fórmulas que recebem como parâmetro um valor HTML de um campo multilinha, o App não estava reconhecendo esse valor como HTML. Isso causava uma modificação no valor, e quando a fórmula calculava, o parâmetro não atendia exatamente a condição esperada pela fórmula, fazendo com que não funcionasse. Os desenvolvedores corrigiram a verificação de HTML e agora esse parâmetro não sofre mais nenhuma transformação indevida.
- Contatos já existentes não eram adicionados à tarefa na integração com o Outlook quando as tarefas eram integradas ao Ploomes. Os desenvolvedores corrigiram o comportamento para adicionar os contatos de acordo com o e-mail utilizado no convite do Outlook.
- Na integração com o Omie, campos não mapeados estavam sendo removidos da integração, correção foi realizada para a integração não modificar esses campos.
