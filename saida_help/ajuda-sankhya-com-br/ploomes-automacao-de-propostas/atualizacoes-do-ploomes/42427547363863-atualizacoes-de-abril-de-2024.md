---
id: "42427547363863"
titulo: "Atualizações de Abril de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427547363863-Atualiza%C3%A7%C3%B5es-de-Abril-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:15Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9148852", "sync_hash_6d80638488cb"]
---

# Atualizações de Abril de 2024

[01/04/2024] [Correção] Ao baixar um documento em pdf, textos muito longos acabavam ultrapassando o limite da página ao invés de quebrar a linha.

[01/04/2024] [Correção] Na integração de tarefas com o Outlook 365, quando o campo 'Criar contatos externos do Outlook caso não existam no Ploomes?' estava desmarcado, não era possível remover usuários que estavam integrados. Quando um usuário tentava fazê-lo, o Outlook os preenchia novamente depois de alguns segundos.

[02/04/2024] [Correção] Ao criar uma nova empresa e colocar um valor de longitude e latitude inválido, era mostrado um de erro genérico sem especificar o motivo de não criar a empresa.

[02/04/2024] [Correção] No aplicativo ao utilizar o caractere"-" ao procurar um CNPJ (ex: 123.456.789/0001-01 e colocar na pesquisa "123.456.789/0001-") não retornava nada. O App não tinha tratativa para a utilização do caractere '-' nos campos de busca, deixando a listagem vazia e dando a impressão de que nada foi encontrado. Correção aplicada na versão 4.0.25 do App.

[02/04/2024] [Correção] No aplicativo na visualização de um documento, o texto no campo de e-mail na aba de compartilhar estava sendo cortado na parte superior. A falta de ajuste de altura fazia com que o texto escrito fosse cortado. Correção aplicada na versão 4.0.25 do App.

[02/04/2024] [Correção] Foi adicionado um modal de aviso para o usuário caso ele esteja enviando um documento para assinar via Letssign e um dos assinantes use certificado digital.

[02/04/2024] [Correção] Na linha do tempo na página inicial, estava quebrando o layout dos cards apenas quando existia registro de ligação do zenvia.

[03/04/2024] [Correção] Ao exportar gráfico do tipo indicador, estava vindo com a primeira coluna vazia.

[03/04/2024] [Correção] Ao clicar no gráfico para analisar os valores, estava apresentando dados escritos com "Data inválida", foi corrigido para manter o valor vazio caso a data seja inválida.

[03/04/2024][Correçao] Quando o usuário estava na tela de nova venda em formato modal e atualizava a tela, o front perdia as informações da proposta, negócio, cliente e etc. Foi feita uma melhoria nessa tarefa para que apareça novamente o modal de escolha de proposta, caso haja mais do que uma no card, e as informações sejam puxadas novamente da proposta de origem.

[03/04/2024][Melhoria] Foram feitas diversas melhorias no formulário de integrações para evitar erros do usuário ao ativar/atualizar a integração do Omie.

[03/04/2024][Correçao] Em Relatórios Beta, quando tentávamos selecionar o texto arrastando com o mouse numa renomeação de painel, o botão do painel vinha junto.

[03/04/2024][Correçao] Em algumas contas, o Google Calendar não estava mudando de tela após clicar no botão de ativar a integração.
[04/04/2024][Correção] Campo de nome da aba tinha um limite fixo de 150 caracteres, mas visualmente não tinha um contador e nem limitava o valor do nome da aba. Foi corrigido através da adição de um contador e um limite para o campo.

[04/04/2024][Correção] A ordenação de opcionais de produtos estava muito pesada, o que gerava uma alta demora caso houvesse muitos opcionais. O modo de fazer a ordenação foi modificado, tornando ela agora mais rápida e eficiente.
[04/04/2024][Correção] Botão de fechar o modal de um módulo na administração desaparecia quando o nome do módulo era muito grande.

[04/04/2024][Correção] Impossibilitado colocar letras em caixa alta no campo presente na seção 'Sua caixa de e-mails' na tela 'Configurações de Email'.
[04/04/2024][Correção] Tarefas criadas entre 00:00 e 00:59 estavam sendo salvas com uma propriedade dizendo que não foi registrado as horas na mesma. Foi corrigido o problema tirando a trava que dizia que a tarefa estava sem horas.

[04/04/2024][Correção] Ícone de erro na proposta/venda/documento estava desalinhado.

[04/04/2024][Correção] Na configuração de perfil de usuário, se o nome da entidade fosse muito grande, o botão ultrapassaria o modal, agora, ele tem um tamanho máximo e tem uma reticência quando quebrar.

[04/04/2024][Correção] Ao gerar uma nova venda, o usuário estava sendo encaminhado para o modal de seleção de proposta sempre ao dar F5, mas não era feita uma verificação se pode gerar propostas no funil. Agora é feita uma verificação para ver se é permitido gerar propostas no funil.

[04/04/2024][Correção] Em metas, os botões de "Nova Meta" e "Exibir" estavam invertidos. Voltamos ao padrão que seria "Exibir" e depois "Nova meta".

[04/04/2024][Correção] Os ícones de adicionar ou remover um telefone, estavam desalinhados e com os ícones grandes.

[04/04/2024][Correção] A ordenação de seções dentro de um modelo de documento havia parado de funcionar. Foi corrigido e agora é possível reordenar novamente.

[04/04/2024] [Correção] Ao interagir com um campo que calculava alguma formula externa, as requisições estavam sendo feitas duplicadas.

[04/04/2024][Correção] Na subida da nova versão da integração com o Facebook Leads no dia 06/03, surgiram alguns bugs que causavam erros de mapeamento dinâmico de diversos tipos de campos, principalmente de opção pré-cadastrada na integração. Corrigimos as conversões de valores e criações de opção pré-cadastrada para corrigir o problema.

[04/04/2024][Correção] Ao revisar a edição dos produtos na proposta, anexos estavam sendo inadvertidamente removidos quando o usuário removia o valor do campo, mesmo sem salvar a edição. Agora, os anexos serão efetivamente excluídos somente quando o usuário optar por salvar a edição e, posteriormente, salvar a proposta.

[04/04/2024][Correção] Agora ao tentar alterar o perfil do proprio usuário ou de um AccountOwner aparecerá um erro na tela e o retorno de erro 401 com uma mensagem explicando o problema.
[05/04/2024][Correção] Ao duplicar uma meta estava aparecendo o campo de "Adicionar contatos relacionados à tarefa da integração" que só deveria aparecer na tela de tarefa com integração de calendário ativa. Foi corrigido e agora deve aparecer apenas um campo do tipo checkbox (sem toggle) com as opções "sim" ou "não".

[05/04/2024][Correção] Em relatórios beta, ao selecionar um filtro relacionado à tarefa de origem em um gráfico de registro de interação, o mesmo sempre fazia um filtro de permissões para trazer apenas os registros que sejam de tarefas que o usuário pode ver. Porém, quando o filtro é "Registro de interação igual a vazio", o mesmo não deveria realizar esse filtro, porque ele quer exatamente os registros que não possuem nenhuma tarefa associada. Para isso, foi criado um filtro adicional para trazer todos os registro onde tarefa de origem e nula.

[05/04/2024][Correção] O aviso de confirmação para excluir um marcador não aparecia após a primeira vez que um marcador havia sido deletado, agora ele aparece em qualquer deleção.

[08/04/2024] [Correção] Na integração com o Outlook, quando o usuário integrava com um e-mail diferente do e-mail dele no Ploomes e havia no Ploomes algum outro usuário com o e-mail que ele usou para integrar ao Outlook, em alguns casos ao criar uma tarefa o usuário que criou a tarefa era removido e o outro usuário era adicionado. Agora quando ocorre isso, são adicionado os 2 usuários na tarefa e nenhum é removido.

[08/04/2024] [Correção] Ao mapear manualmente o campo de telefone do ActiveCampaign para o campo de telefone do Ploomes (mapeamento esse que é fixo por padrão, sem necessidade de ser mapeado manualmente), o telefone não era preenchido no Ploomes ao integrar um lead. Agora o campo será preenchido mesmo caso o mapeamento também seja feito manualmente.

[08/04/2024] [Correção] Ao editar as propostas, caso as seções fossem duplicadas ou removidas sem alterar os produtos, um erro acontecia na geração do HTML. Foi feito um tratamento no que era enviado para corrigir o problema.
[08/04/2024] [Correção] Em filtros, era possível fazer caminhos recursivos nas entidades, como empresa > contato > empresa > contato e etc. Foi adicionado um limite para evitar que o usuário faça um filtro que não é aceito pelo back-end.

[08/04/2024] [Correção] Ao editar um documento, os modelos não eram filtrados pelo tipo de documento, fazendo com que modelos incorretos aparecessem para serem selecionados. Este erro foi corrigido e agora o dropdown só irá apresentar os modelos corretos de acordo com o tipo de documento (de cliente ou de negócio).

[09/04/2024] [Correção] Na integração com o Power BI, quando o usuário configurava o intervalo de atualização da aba para 24 horas ou qualquer outro múltiplo de 24, a atualização não ocorria. Corrigimos esse problema e agora a atualização ocorre corretamente.

[10/04/2024] [Correção] Na integração com o RD Station, ao mapear o campo "Telefone" na empresa, o mesmo estava chegando duplicado no Ploomes.

[10/04/2024] [Correção] O App não estava ajustado para mostrar a barra de tipos de registro na tela de edição de um registro de interação. Agora é possível editar o tipo, igual na web.

[10/04/2024] [Correção] Ao criar um filtro rápido em um painel dos relatórios beta e duplicar o painel origem, o filtro rápido não funcionava no painel cópia.

[11/04/2024] [Correção] Notificações push (aquelas que ficam no topo do celular) não levavam para entidade correspondente à notificação recebida. O problema foi corrigido.

[11/04/2024] [Correção] Requisições de criação de registro de interação foram otimizadas.

[11/04/2024][Correção] Foi aplicada uma correção para alinhar e centralizar o ícone do botão de excluir estágio de vendas.
[11/04/2024][Correção] Foi adicionado um tratamento para evitar que nomes de modulos muito grandes invadam o espaço do botão de sincronização no aplicativo mobile. Correção aplicada na versão 4.0.26 do App.

[11/04/2024][Correção] No campo do nome do estágio de vendas foi adicionado um limitador para que o usuário não consiga colocar um nome com mais de 100 caracteres.
[11/04/2024][Correção] Tratamento adicionado para mostrar o texto de "Carregando..." enquanto o carregamento da lista de documentos não é finalizado. Correção aplicada na versão 4.0.26 do App.
[11/04/2024][Correção] Agora o app não envia comentários vazios, evitando o aparecimento do loading desnecessário. Correção aplicada na versão 4.0.26 do App.
[11/04/2024][Correção] Corrigido filtro no formulário de proposta, funis que não permitem criação de propostas são removidos das opções ao criar um negócio a partir do campo. Correção aplicada na versão 4.0.26 do App.
[11/04/2024][Correção] No funil de negócio foi adicionado uma restrição para que os botões não desalinhem, caso não caibam na tela, será possível arrastar um scroll para a direita para a visualização.
[11/04/2024][Correção] As opções de edição/exclusão de produto de cliente estavam habilitadas no App de forma incorreta pois ainda cabe um projeto para desenvolve-las por completo, dessa forma, elas foram removidas. Correção aplicada na versão 4.0.26 do App.
[11/04/2024][Correção] Nome da entidade de "Produtos do cliente" na configuração de formulário estava com as primeiras letras em minúsculo.
[11/04/2024][Correção] Ao colocar um campo de endereço na seção de produtos em documento da proposta, ao gerar o documento e interagir com o campo, agora não irá mais omitir a lista de opções sugeridas.

[11/04/2024][Correção] Quando a primeira seção do formulário estava vazia, todos os campos sem seção eram colocados nela por conta de um filtro incorreto. O comportamento foi corrigido.

[11/04/2024][Correção] Quando o usuário não tinha permissão para editar produto de cliente, o erro exibido era "tente novamente mais tarde", confundindo o usuário. O erro agora avisa que o usuário não tem autorização.
[11/04/2024][Correção] No aplicativo foi adicionada uma nova checagem para mostrar o nome do cliente corretamente embaixo do título do negócio na tela de visualização do negócio. Correção aplicada na versão 4.0.26 do App.

[11/04/2024][Correção] Quando um usuário inseria uma opção em outra língua, era exibido nos relatórios beta aquela opção na língua do usuário que inseriu, sem levar em conta o usuário que está consultando o relatório.

[11/04/2024][Correção] Foi alterado o HTML responsável pelos links de rastreio para não dar problemas em mensagens com algumas formatações específicas.

[11/04/2024] [Correção] Requisições de criação de registro de interação foram otimizadas

[11/04/2024] [Correção] O aplicativo resetava o número de telefone do cliente ao mudar a máscara do campo.

[11/04/2024] [Correção] O app permitia o envio de comentários vazios, mas a API bloqueava, dessa forma o usuário observava o botão carregando.

[11/04/2024] [Correção] Em IPhones muito novos, o formulario de compartilhar pelo WhatsApps fechava o App após um período de tempo.

[12/04/2024] [Correção] Ao criar um perfil de usuário com nome maior que 50 caracteres, era retornado um erro genérico. Isso acontecia, pois não possuía uma tratativa no código para tamanho de campos, portanto o erro estourava pelo lado do banco de dados. Para corrigir isso, colocamos uma tratativa para validar o valor que vem do payload e assim retornar erro 400.

[12/04/2024][Correção] Quando negócios de um estágio tinham moedas diferentes, o texto da moeda aparecia duplicado na informação do estágio. O comportamento foi corrigido.

[12/04/2024][Correção] Caracteres especiais estavam quebrando quando inseridos no nome de seção de proposta/venda/documento.

[12/04/2024][Correção] Ao tentar inserir imagens na galeria com o formato diferente de BMP, GIF, EXIF, JPG, PNG, ou TIFF não era exibido um erro.

[12/04/2024][Correção] Campo de cliente em tarefa ultrapassava o limite do campo quando ele tinha um nome muito grande.

[14/04/2024] [Correção] Ocorria erro ao criar proposta exibindo a mensagem "Tente novamente mais tarde". O erro ocorria devido à tentativa de inserir no banco de dados um valor que excedia os 200 caracteres definidos para o campo do nome do arquivo PDF. Os desenvolvedores limitaram o valor para inserir 200 caracteres no nome do arquivo para poder salvar a proposta normalmente e não gerar a mensagem de erro.

[15/04/2024] [Correção] Ícones de filiais eram sempre de pessoa, nunca de empresa, mesmo que a filial configurada fosse uma empresa. Corrigimos o comportamento.

[15/04/2024] [Correção] Não tinhamos controle de conflito entre dois reviews de proposta concorrentes. Quando mais de um review acontece ao mesmo tempo, apenas um deles cria uma revisão e os outros acabam criando propostas novas. Implementamos um controle para esse tipo de conflito

[15/04/2024] [Correção] Ao duplicar um negócio, a propriedade do criador não era setada, fazendo com que fosse lida como '0' por fórmulas. O comportamento foi corrigido para trazer os dados do usuário que está duplicando.

[15/04/2024] [Correção] Não existia uma tratativa para exibição condicional em cima de campos múltiplos como Marcadores.

[16/04/2024] [Correção] Foi resolvido o problema que impedia a autorização do Calendário do Outlook de ser autorizado via OAuth. Agora usuários devem conseguir integrar sem problemas.

[16/04/2024] [Correção] A mensagem de aviso ao trocar de idioma possuía um erro gramatical e foi adequado ao padrão da lingua portuguesa. Correção aplicada na versão 4.0.27 do App.

[16/04/2024] [Correção] Campo de negócio agora é escondido na edição de um registro de interação. Correção aplicada na versão 4.0.27 do App.
[16/04/2024] [Correção] Ao concluir uma tarefa com observação vindo pela tela de visualização de cliente, o App redirecionava incorretamente o usuário para a listagem de clientes. Agora ao concluir, ele redireciona para o cliente que estava sendo visualizado. Correção aplicada na versão 4.0.27 do App.
[16/04/2024] [Correção] Era possível finalizar uma tarefa antes do mapa carregar, resultando no checkin verificado. Correção aplicada na versão 4.0.27 do App.
[16/04/2024] [Correção] Na tela de idioma, caso o idioma selecionado seja igual ao já salvo no app, o botão de salvar fica desabilitado. Correção aplicada na versão 4.0.27 do App.

[16/04/2024] [Correção] No app, em marcações de usuários, não havia filtro para pegar somente usuários ativos. Correção aplicada na versão 4.0.27 do App.

[16/04/2024] [Correção] No aplicativo quando o usuário acessava o módulo de funil, o aplicativo fechava. O problema do App fechar quando o usuário acessava a tela de funis ocorria porque existiam campos com fórmulas que utilizam o próprio campo como valor e esses campos estavam sendo utilizado nos filtros. Isso causava um looping infinito entre o próprio campo da fórmula referenciando ele mesmo que causava o erro. Correção foi realizada removendo uma verificação que não era necessária para o filtro e causava o looping e aplicada na versão 4.0.27 do App.

[16/04/2024] [Correção] Na listagem de negócios, a ordem dos cards estava diferente entre Web e App. Correção aplicada na versão 4.0.27 do App.
[16/04/2024] [Correção] Campo de data do Meetime está mapeado com um campo de Tipo Texto do Ploomes na entidade de Negócio e esse campo de Texto estava sendo preenchido pelo Meetime com a data invertida. O problema ocorria porque não estávamos fazendo um tratamento dos campos do tipo data vindos dos Webhooks, logo, Timezones diferentes estavam sendo salvos de maneira equivocada. Correção foi propagada, agora buscamos a configuração no Ploomes e fazemos a conversão dos campos.
[16/04/2024] [Correção] No aplicativo estava havendo uma lentidão no carregamento da tela de lista de contatos que sempre buscava os valores das abas de forma online. Agora o App sempre carrega as abas da lista de clientes através do Banco Offline. Correção aplicada na versão 4.0.27 do App.
[16/04/2024] [Correção] No form externo, quando trocávamos de língua, a label dos campos padrões do sistema não trocavam para o idioma selecionado, agora eles são traduzidos conforme o idioma selecionado.

[17/04/2024] [Correção] Ao tentar inserir um campo em uma fórmula de um campo nativo do Ploomes, não permitia inserir novos campos. O problema surgia quando excluíamos um campo do sistema que era utilizado em uma fórmula de campo nativo. Nesse caso, o campo não era removido automaticamente da fórmula. Isso resultava em erros ao tentar executar a fórmula, já que ela tentava acessar o valor do campo excluído. Para resolver isso, fizemos o mesmo comportamento já presente nas fórmulas de campos dinâmicos para os campos nativos: ao excluir um campo, ele será removido de todas as fórmulas onde é utilizado como variável.
[17/04/2024] [Correção] Em módulos do sistema, ao alterar os nomes da entidade de negócios para um nome extenso dentro do limite do campo não permitia salvar o nome. Alinhamos o limite de caracteres do campo no front-end com o do banco de dados, aumentando o tamanho máximo da coluna no banco para 100 caracteres. Anteriormente, o campo no front-end permitia a inserção de até 100 caracteres, mas a coluna correspondente no banco estava limitada a apenas 50 caracteres. Agora, ambos os limites são consistentes, permitindo armazenar até 100 caracteres.
[17/04/2024] [Correção] Agora ao ultrapassar o valor máximo de campos numéricos na proposta, venda e documento, um erro voltará informando-o que existem campos ultrapassando o limite.
[17/04/2024] [Correção] Foi adicionado uma tratativa para limitar nome de novos usuários na aba de administração, evitando erros genéricos quando o limite era ultrapassado.

[17/04/2024] [Correção] O banco de dados permite 160 caractéres para o nome de uma automação para poder prefixar o nome das automações criadas com "Cópia - ". Por conta disso, a regra de negócio da API-2 só permite até 150 caractéres, porém a atualização de automações não está enforçando essa regra, o que pode levar a cenários onde não é possível duplicar uma automação por seu nome ter sido atualizado com mais de 150 caractéres.

[17/04/2024] [Correção] O backend validava se o funil permitia perder cards antes de realizar uma edição em massa na situaçao do card, mas agora isso não é mais realizado e a edição em massa "burla" a regra.
[18/04/2024] [Correção] O nome de personalização do PDF não era atualizado quando mudado o modelo de uma proposta.

[18/04/2024] [Correção] Foi adicionado ao gerador de documentos uma ordenação das seções para seguir a ordem de inserção no banco de dados. Com isso, na geração as seções sempre devem corresponder a ordem que aparece na edição.

[18/04/2024] [Correção] Extensão com Whatsapp não exibia informações necessárias, do contato, alguns navegadores ou computadores que são inferiores e estão configurados para otimizar as execuções de animações, estava impedindo que obtivéssemos os dados corretamente, e com isso não estava sendo possível fazer a requisição para o Ploomes. Foi removido essa funcionalidade, e agora vamos obter as informações através de um determinado tempo que foi adicionado.

[18/04/2024] [Correção] Quando havia alguma lentidão para carregar os marcadores, o espaço para digitar o texto de pesquisa de marcadores ficava com tamanho reduzido temporariamente. As duas operações agora não dependem uma da outra para evitar esse problema.

[19/04/2024] [Correção] O campo de checkbox "Dados autorizados" foi deletado.

[19/04/2024] [Correção] Melhoramos a estrutura do HTML na tabela de estoque do Omie. Com isso, a tabela agora é exibida de forma mais clara e organizada, facilitando a compreensão e leitura dos dados.

[22/04/2024] [Correção] A integração com o Facebook Leads ao criar negócios não estava preenchendo os campos dinâmicos, mesmo quando estes estavam mapeados.

[23/04/2024] [Correção] Ao atualizar a integração com o Active Campaign, em alguns casos, uma notificação de erro era enviada ao usuário, indicando um mapeamento inválido, mesmo quando o mapeamento estava correto.

[23/04/2024] [Correção] O campo nativo Última mudança de estágio, estava sendo exibido no mapeamento de campos em automações, porém, não era possível inseri-lo em um formulário, então, o campo foi removido da opção de seleciona-lo no mapeamento em automações.
[23/04/2024] [Correção] No aplicativo, após o reset (ou realizar o login pela primeira vez), a lista de clientes não carregava. Correção aplicada na versão 4.0.28.

[23/04/2024] [Correção] No aplicativo não havia verificação de campo chave dentro de checklist. Correção aplicada na versão 4.0.28.

[25/04/2024] [Correção] Ao enviar email sem assunto por negócio, a mensagem exibida estava parcialmente traduzida e não havia ponto de interrogação no final da frase.

[25/04/2024] [Correção] Quando a aba tinha um nome muito grande, o tooltip ficava fora da posição correta, que é em cima da aba. O comportamento foi corrigido.

[25/04/2024] [Correção] No modal de confirmação da criação de usuário em inglês, o termo "Are you sure" estava sem um espaço, fazendo com que colasse no resto da mensagem.

[25/04/2024] [Correção] Ao retornar um valor 'Infinity' para um campo via fórmula (por exemplo ao dividir um valor por zero), esse valor era interpretado como válido para preencher o campo obrigatório, mas esse valor era ignorado e transformado em vazio pois o backend não o aceita. Isso fazia com que a obrigatoriedade de um campo fosse burlada. O comportamento foi corrigido interpretando 'Infinity' como vazio.

[25/04/2024] [Correção] Em vínculo de produto era possível inserir uma quantidade máxima menor que a quantidade mínima.

[25/04/2024] [Correção] No modal de criar um novo negócio, com um campo de cliente que ocupa duas colunas ao abrir o formulário mini de criação de um novo cliente, o mini modal estava saindo da tela, foi criado uma função para não deixar o formulário sair do campo de visão do usuário.

[25/04/2024] [Correção] O botão de fechar vínculos de produto estava desalinhado.

[25/04/2024] [Correção] O exportador não permitia a exportação de abas vazias. Passamos a permitir na integração que atualizações, ao não encontrar dados para exportar, retornem uma planilha vazia ao PowerBI.

[26/04/2024] [Correção] Ao abrir o formulário Mini de negócio, o campo estágio e os botões de ação não estavam sendo renderizados corretamente por conta de um erro no código. O problema foi corrigido.

[26/04/2024] [Correção] Por padrão, a integração com o Meetime verifica a duplicidade de empresas pelo CNPJ. No entanto, se o campo não estiver mapeado ou se a informação do CNPJ não for fornecida pelo Meetime, a empresa não era criada. Agora, nesse cenário, a validação de duplicidade é feita com base no nome, e a empresa é criada mesmo sem o CNPJ.

[26/04/2024] [Correção] Quando editamos ou criamos um produto na proposta, temos um campo de busca por nome ou código. No entanto, ao inserir informações, estávamos realizando duas requisições pesadas ao backend, resultando frequentemente em timeouts, especialmente em casos em que os usuários tinham uma grande quantidade de itens registrados. Para resolver essa questão, desenvolvemos um novo endpoint no backend para agilizar a obtenção desses itens. Além disso, foi necessário ajustar o fluxo no frontend para conectar-se a essa nova API e garantir a correta exibição dos dados.

[29/04/2024] [Correção] O usuário podia editar o responsável de um cliente (pessoa) relacionado a uma empresa, porém essa mudança não é permitida e não era aplicada no backend. Agora esse campo é bloqueado caso o cliente seja relacionado a uma empresa.

[29/04/2024] [Correção] O botão de atualizar arquivo na bilbioteca não estava funcionando. Foi feito o ajuste da rota utilizada no front e agora o botão funciona corretamente.

[29/04/2024] [Correção] Mensagem de página não encontrada não estava aparecendo na entidade de clientes e produtos.

[29/04/2024] [Correção] Em formulários externos era possível mapear os campos Pessoa.Empresa, Pessoa.Empresas, Contato.Empresa e Contato.Empresas, o que causava certos problemas. Esses campos não podem mais ser mapeados.
[29/04/2024] [Correção] Descrições longas em fluxos de aprovação estavam ultrapassando o tamanho da tela.

[29/04/2024] [Correção] Em clientes, ao comentar em algum card em Próximos Passos, não estava a atualizando a quantidade de comentários, só atualizava após recarregar a página. Agora, o número de comentários é atualizado sem precisar recarregar a página.

[29/04/2024] [Correção] Máscara de telefone segue a língua da conta, caso seja português, ela preenche com a máscara brasileira, e, caso não tenha, não preenche. Porém, quando a língua da conta estava diferente de português (Brasil), a máscara era retirada mesmo quando o campo estava configurado.

[29/04/2024] [Correção] Agora estágios de vendas tem tooltip contendo o nome do estágio caso ele tenha um nome muito grande que ultrapasse o tamanho do elemento.
[29/04/2024] [Correção] Modal de confirmação de atualização de dados de modelo não estava traduzido.
[29/04/2024] [Correção] O input de nome de filtro foi limitado a 150 caracteres, com o contador indicando ao usuário o tamanho do nome e o limite. Além disso, caso o usuário consiga burlar essa tratativa, a mensagem de erro será mais específica.
[29/04/2024] [Correção] Ao inserir uma nova logo da conta em dados da empresa e atualizar a tela, a logo anterior continuava a ser exibida, apesar de já ter sido modificada, pois o cache local não era atualizado. O comportamento foi corrigido.

[29/04/2024] [Correção] No campo de upload de logo em dados da empresa era possível adicionar qualquer tipo de arquivo, mesmo só sendo possível adicionar imagens. Um restrição com mensagem de erro foi feita para alertar o usuário que não foi possível trocar o logo por conta do formato incorreto do arquivo.

[29/04/2024] [Correção] Consultas de controle do produto e valor unitário agora funcionam pra proposta no APP.

[29/04/2024] [Correção] Em documentos, quando um opcional estava com os campos obrigatórios vazios e o usuário tentava salvar, era emitido um erro para o usuário mas os campos não eram destacados como no resto do sistema. Essa funcionalidade foi adicionada para melhorar a experiência dos usuários, tanto no formulário tela cheia quanto no modal. Além disso, no formulário modal não havia ícone para sinalizar que um campo de opcional é obrigatório.

[29/04/2024] [Correção] Na criação de produto, quando tentamos adicionar vínculos, o botão de verificar o vínculo aparece, porém, na criação do produto, o vínculo só é de fato criado quando terminamos de salvar o produto pai.Na criação de produto, quando tentamos adicionar vínculos, o botão de verificar o vínculo aparece, porém, na criação do produto, o vínculo só é de fato criado quando terminamos de salvar o produto pai.

Agora, esse botão de ir direto para o vínculo não aparece mais na criação, e também, você agora consegue remover vínculo mesmo na criação do produto, o que antes não era possível.

[29/04/2024] [Correção] Ao tentar salvar campo sem título, aparecia uma mensagem de campo destacado obrigatório, porém, não destacava nenhum campo.

[29/04/2024] [Correção] No menu lateral, ao selecionar uma aba enquanto está com um formulário com alterações pendentes e em seguida selecionando Cancelar no popup de confirmação de saída da página, a nova aba clicada permanecia ativa mesmo sem ter navegado para outra página. Agora a aba só é alterada quando se tem a confirmação de saída de página.

[29/04/2024] [Correção] Ao teclar Enter no input estava acontecendo uma tentativa inesperada de submissão do formulário, comportamento prevenido a partir de agora.

[29/04/2024] [Correção] Ao atualizar dados e modelo, uma nova propriedade agora é enviada ao back-end para que fluxos de aprovação sejam validados corretamente.
