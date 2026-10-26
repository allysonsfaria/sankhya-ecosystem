---
id: "42427573438615"
titulo: "Atualizações de Março de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427573438615-Atualiza%C3%A7%C3%B5es-de-Mar%C3%A7o-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:44Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9046925", "sync_hash_c89c90b58377"]
---

# Atualizações de Março de 2024

[04/03/2024] [Correção] Existia um problema de permissão de visualização no módulo de relatórios beta, no qual um usuário conseguia ver negócios de outro usuário sem ter as permissões adequadas.

[04/03/2024] [Correção] Ao inserir algumas caracteres científicos como por exemplo o caractere "e" no valor padrão de campos numéricos, estava aceitando, causando erro de valor inválido nos campos. Foi resolvido observando os valores que serão inseridos no campo e fazendo a validação removendo as letras e deixando apenas números.

[04/03/2024] [Correção] Ao preencher um Card no Negócio, era possível preencher algum cliente aleatório, e isso não era permitido no back-end. Foi feito um desenvolvimento no front-end para bloquear o campo de cliente caso o negócio esteja preenchido.

[04/03/2024] [Correção] Na edição de proposta, se havia um opcional bloqueando outro, mesmo sem estar marcado, essa regra era aplicada ao editar uma proposta no formato modal. Uma verificação foi adicionada no código para só ativar o bloqueio quando realmente o opcional está marcado.

[04/03/2024] [Correção] Ao editar o fluxo de aprovação, caso alguma das condições tivesse uma data vazia, em alguns momentos ela era enviada como a data do dia.

[04/03/2024] [Correção] Foi adicionado preload nas contas que tem pentest ativo.

[04/03/2024] [Correção] Ao editar um modelo de e-mail e depois inserir um novo contato, a edição do usuário não estava sendo aplicada.

[05/03/2024] [Correção] Anteriormente, na integração com o Omie, os campos multilinha eram enviados do Ploomes para o Omie com tags HTML. Agora, nos passamos a remover essas tags, e enviando apenas o conteúdo do campo.
[05/03/2024] [Correção] Em Relatórios Beta não estava sendo exibido a coluna de "Total" da Venda na visualização de detalhamento do gráfico (Drilldown) em gráficos que utilizam a entidade de Venda. Comportamento foi corrigido.

[07/03/2024] [Correção] Os textos de horas na linguagem em inglês, estava sem o AM ou PM, e com isso estava com padrão de 24 horas e não de 12 horas como é o normal na língua inglesa.

[07/03/2024] [Correção] Anteriormente, o limite de caracteres da propriedade "Nome" para campos de opções do formulário externo era de 150. No entanto, ao tentar inserir uma string de 200 caracteres (que é o limite para nomes de clientes), retornava erro ao inserir no banco de dados. Para resolver esse problema, o limite foi aumentado de 150 para 200 caracteres.

[07/03/2024] [Correção] Nas configurações de formulário, o tamanho máximo de caracteres permitido no nome da seção no back-end era de 60, mas o front permitia inserir até 200, causando erros. O limite foi corrigido e uma mensagem de erro agora é exibida caso o nome da seção ultrapasse 60 caracteres.

[07/03/2024] [Correção] Caso o e-mail do usuário não retornasse para o front no modal de compartilhamento de documentos, era exibida a opção 'E-mail do usuário (undefined)'. O comportamento foi corrigido para a opção não ser exibida nesse caso.
[07/03/2024] [Correção] Ao estar na tela de metas no aplicativo, o mesmo estava trocando automaticamente a aba de metas para a aba de resumo ao fechar e reabrir. Foi corrigido na versão 4.0.21.
[07/03/2024] [Correção] O aplicativo não informava que não dava para fazer uma venda ou documento sem ter um cliente ligado a um negócio. Isso fazia com que a tela de venda ficasse carregando indefinidamente depois do formulário. Agora, foi adicionado um aviso ao validar o formulário para verificar se há um contato vinculado ao negócio. Foi corrigido na versão 4.0.21.

[07/03/2024] [Correção] No aplicativo, na tela de cliente, a ordem da listagem de negócios foi refeita priorizando as "em aberto" primeiro (das mais recentes até mais antigas), e depois ganhas e perdidas (da mais recente até as mais antigas).

[07/03/2024] [Correção] No aplicativo, o cálculo da posição de cada estágio no funil estava incorreta, fazendo com que a lista parasse no estágio cortado. O cálculo foi refeito para agora mostrar o estágio corretamente na tela.

[07/03/2024] [Correção] O aplicativo agora verifica se uma tarefa ultrapassará um mês no calendário antes de calcular sua duração completa. Se isso ocorrer, o aplicativo preenche automaticamente o restante do mês com a tarefa, em vez de realizar o cálculo completo.

[07/03/2024] [Correção] Ao criar uma proposta em documentos em formato de modal, na parte de adicionar um produto, aparece uma lista de produtos onde podemos clicar na caneta para editar, com isso, se fecharmos o modal de inclusão de produto e deixar o tooltip aberto, ele não fechava. Foi corrigido isso da seguinte forma, ele valida se o modal está aberto, se não, será fechado o tooltip.

[07/03/2024] [Correção] Ao excluir um produto aparece uma mensagem de confirmação, se o usuário ficar apertando a tecla enter várias vezes, aparecia o modal de confirmação de acordo com a quantidade interagido. Foi feito uma correção para aparecer apenas uma vez ao clicar.

[07/03/2024] [Correção] Na tela de envio de e-mails, só eram listados até 10 contatos do cliente, pois havia um hardcoded muito antigo no front-end limitando isso.

[07/03/2024] [Correção] Ao adicionar dois telefones em clientes, e preencher apenas o último, estava trazendo apenas o primeiro telefone adicionado, ou seja, um campo sem informações, foi adicionado uma validação para remover os telefones que não foram preenchidos ao clicar em salvar.

[07/03/2024] [Correção] Agora quando tarefas do Ploomes forem integradas ou com o Google ou com Outlook, aparecerão ícones dentro e no calendário que registram que a integração foi feita com sucesso.

[07/03/2024] [Correção] O modal de opções de metas não estava sendo fechado durante outras interações do usuário, como scrollar metas e trocar entre resumo e metas. Agora o modal é fechado durante o scroll das metas e trocas entre resumo e metas.
[07/03/2024] [Correção] O aplicativo não marcava no calendário as tarefas que eram do último dia do mês. Foi feita uma correção para que as tarefas apareçam no calendário.

[07/03/2024] [Correção] Ao movimentar os cards de metas, o comportamento de mudar de posição não estava sendo respeitado.

[07/03/2024] [Correção] Ao criar uma meta com o título muito grande, estava quebrando o layout e com isso consequentemente quebrava a função de arrastar, podendo movimentar o card para o infinito na esquerda.

[07/03/2024] [Correção] Ao modificar o logo em dados da empresa, o logo era salvo antes do usuário clicar em salvar, mas como não havia nenhuma mensagem de erro ou sucesso, isso não ficava claro para o usuário. As mensagens de erro foram adicionadas.

[07/03/2024] [Correção] O código do legado módulo de leads não tinha nenhuma verificação para saber se o módulo estava ativo na conta do usuário. Foi implementada essa verificação.
[07/03/2024] [Correção] Pesquisa de produtos na proposta não estava retornando o produto pesquisado, às vezes retornava o produto e às vezes não. O campo de seleção de produtos não estava cancelando as requisições de pesquisa anteriores, e com isso, ao digitar enquanto estava carregando, não estava trazendo os produtos conforme o texto pesquisado. Foi adicionado uma condição para cancelar todas as requisições de pesquisa enquanto o usuário digita, e com isso a requisição final sempre virá atualizada.

[08/03/2024] [Correção] Modal de integração de tarefas aparece vazio quando o perfil está utilizando a língua espanhol.

[11/03/2024] [Correção] Na integração com o Omie, ao receber uma atualização no produto, quando ocorria um erro durante a consulta à tabela de estoque no Omie, não era realizada uma nova tentativa, resultando em uma tabela de estoque vazia no Ploomes.

[11/03/2024] [Correção] Caso a cor da conta seja cinza, acabava provocando uma confusão nos estágios de negócios por conta de ser a mesma cor (cinza) que o estágio não avançado.

[11/03/2024] [Correção] Na integração com o Active Campaign, a chave de duplicidade é estabelecida pelo campo 'Id (Active Campaign)'. Caso esse campo não esteja preenchido, a validação é realizada através do campo de e-mail do cliente. Entretanto, a validação por e-mail não estava ocorrendo conforme o esperado, resultando na criação de clientes duplicados em alguns casos. O comportamento foi corrigido.

[11/03/2024] [Correção] Na integração de tarefas com o Outlook, quando o campo 'Criar contatos externos do Outlook caso não existam no Ploomes?' estava marcado, ao remover qualquer usuário de uma tarefa, a tarefa era excluída imediatamente. Agora, verificamos se o usuário removido é o organizador da tarefa, caso não seja, não realizamos a exclusão.

[11/03/2024] [Correção] Na integração com o RD Station, a validação por duplicidade é realizada através do e-mail do cliente. Em alguns casos, quando esse e-mail continha caracteres pouco usuais, como o caractere '+', a validação não estava ocorrendo como esperado, resultando na criação de clientes duplicados no Ploomes.

[12/03/2024] [Correção] Propostas/Documentos gerados vinham com o nome dos campos e não com os valores inseridos.

[13/03/2024] [Correção] Usuário não conseguia visualizar o modal de integrações por conta de um problema na migração antiga do Calendar para a nova.

[13/03/2024] [Correção] A busca na API-2 pelo estado que foi informado na importação não levava em conta o país, assim quando haviam dois estados com a mesma sigla em países diferentes, o importador não sabia qual usar e ficava em branco.

[14/03/2024] [Correção] A integração com o DocuSign era desabilitada automaticamente em 15 dias caso não fosse usada, porque os tokens de acesso da API do DocuSign expiravam com a inatividade. Adicionamos uma ciclagem eventual dos tokens para que não expirem mais, assim não desligando mais a integração.

[14/03/2024] [Correção] Ao salvar um documento sem título, o botão de salvar era bloqueado de forma permanente.

[14/03/2024] [Correção] Ao abrir várias abas no Ploomes, estava travando a tela roxa de login sem apresentar nenhum erro de requisição ou de script

[14/03/2024] [Correção] Nomes de módulos muito grandes ficavam cortados na barra lateral, agora, vão ter tooltip quando passar o mouse em nomes cortados e quando minimizarem os módulos.
[14/03/2024] [Correção] Todos os campos do Ploomes do tipo número estavam aceitando caracteres científicos ao digitar e ao colar um valor. Porém, no caso de inserir campos na Proposta, o campo de "Quantidade", por exemplo, aceitava inserir o caractere 'e', mas não deixava inserir o Produto na Proposta. Comportamento foi corrigido, por exemplo, campos de "Quantidade" e de "Desconto" não permitem mais adicionar o caractere 'e'.

[14/03/2024] [Correção] Ao registrar vários telefones no Ploomes e deixássemos o primeiro campo sem preencher, não estava sendo possível retornar o telefone que de fato foi preenchido.

[14/03/2024] [Correção] Por conta de atualizações recentes, a integração com o Facebook Leads deixou de vincular alguns negócios aos respectivos clientes. A criação desse vínculo foi corrigida.

[14/03/2024] [Correção] O app estava com a ordenação de metas diferente da Web. Agora o app ordena os painéis nativamente e os que não estão com uma ordenação definida são colocados no fim da lista, assim como na Web.
[14/03/2024] [Correção] Não era possível salvar a opção selecionada do campo "Moeda", nativo do Ploomes, na tela do Cliente e na tela de Negócio não era possível editar o campo "Moeda", somente exibia a moeda padrão cadastrada em administração.
[14/03/2024] [Correção] Algumas ações não estavam tratadas no App para mostrar o subtítulo do card corretamente como na Web. Essas ações foram verificadas e adicionadas na criação do subtítulo do card em histórico de venda, seguindo o formato da web.

[14/03/2024] [Correção] Em criação/edição de documentos, não estava sendo possível editar um campo do tipo imagem inserido na proposta.

[14/03/2024] [Correção] Ao cancelar a mudança do idioma do usuário, estava aparecendo um erro genérico para o usuário que não tem sentido sendo que o mesmo não tomou uma ação de salvar.

[14/03/2024] [Correção] Havia uma inconsistencia no nome de uma das abas de usuário, "Suas Exportações", estava com a segunda palavra em maiúsculo, sendo que as outras não estavam.

[14/03/2024] [Correção] No app, campo de CNPJ em checklist não tinha verificação, possibilitando o usuário de preencher o campo com o CNPJ incompleto ou invalído.

[14/03/2024] [Correção] Em publicações, ao comentar em alguma publicação, não estava salvando o estado dos comentários, só atualizava apenas quando recarregar a página.

[14/03/2024] [Correção] Em checklist que deveria apenas aparecer os produtos do cliente estava aparecendo todos.

[15/03/2024] [Correção] Diferente do Web, o App estava mostrando o campo de cliente e negócio na criação de uma tarefa pela tela de um negócio. Agora o app esconde esses campos na criação e edição de tarefas vindas por esse fluxo.

[15/03/2024] [Correção] Ao criar um negócio, o cliente do tipo pessoa estava vindo com a sigla do seu estado em seu nome, como se estivesse no cadastro. Foi removido a concatenação que estava causando esse problema.

[15/03/2024] [Correção] Na tela de configuração de documentos, o nome das páginas não tinha limite de caracteres. O limite foi adicionado conforme o permitido pelo back-end, e além disso foi feita uma refatoração do CSS para deixar aquela região das páginas um pouco melhor, para evitar algumas sobreposições que estavam ocorrendo.

[15/03/2024] [Correção] Quando não havia imagem nos dados da empresa, a visualização da imagem ficava quebrada, e dependendo das dimensões da imagem inserida, ela ficava distorcida. Foi feita uma melhoria para deixar um logo padrão caso não haja logo e a imagem não fica mais distorcida caso tenha dimensões retangulares.

[15/03/2024] [Correção] O App não estava levando em conta o painel padrão definido pelo usuário na Web no momento de carregamento inicial das metas. Agora o app observa qual o último painel navegado pelo usuário na Web e já pré-seleciona este.

[18/03/2024] [Correção] Em Relatórios Beta, ao ter um painel com permissões por perfil de usuário, quando trocávamos o perfil de um usuário para este poder visualizar e editar o painel, não permitia o usuário a editar o painel.

[18/03/2024] [Correção] Na integração com o Omie, quando alterava o valor total do serviço de venda, o Ploomes não estava espelhando o valor, pois estava considerando somente a soma dos produtos e não o valor total, que pode ser alterado por cálculos de impostos. Agora os devidos valores são considerados.

[20/03/2024] [Correção] Na configuração de funil era possível selecionar ícone vazio.
[20/03/2024] [Correção] No aplicativo, em alguns casos na criação de uma nova entidade, a mensagem de sucesso aparecia de forma incompleta na tela. Correção propagada na versão 4.0.23 do App.

[20/03/2024] [Correção] No aplicativo, era feita a validação do campo CPF apenas no momento de criação do formulário, agora o mesmo acontece no momento que preenche o campo. Correção propagada na versão 4.0.23 do App.
[20/03/2024] [Correção] No aplicativo campos com fórmula externa que eram usados somente para preencher outros campos estava se preenchendo de forma errada. Correção propagada na versão 4.0.23 do App.

[20/03/2024] [Correção] O campo 'Enviar convite às pessoas relacionadas' não era exibido na visualização da tarefa e na sua edição o valor estava sempre false. Correção propagada na versão 4.0.23 do App.

[20/03/2024] [Correção] Com um modal de campo aberto, ao fechar ele, era feito um scroll automático até o campo de texto que estava anteriormente sendo digitado. Correção propagada na versão 4.0.23 do App.

[20/03/2024] [Correção] Campo de opção pré-cadastrada não puxava seu valor padrão no formulário de venda quando existia proposta preenchida no mesmo negócio. Correção aplicada na versão 4.0.23 do app.

[20/03/2024] [Correção] Não havia um limite de caracteres para o campo do nome do cliente, quebrando a criação do cliente.

[20/03/2024] [Correção] Caso fosse preenchido um endereço de outro país, o campo país continuava mostrando Brasil. Correção aplicada na versão 4.0.23 do app.

[20/03/2024] [Correção] Não era permitido alterar o modelo de documento na revisão de uma proposta. Correção aplicada na versão 4.0.23 do app.

[20/03/2024] [Correção] Na lista de vendas, caso a venda seja de valor 0, não aparecia o valor no titulo do card. Correção aplicada na versão 4.0.23 do app.

[20/03/2024] [Correção] O campo 'Enviar convite às pessoas relacionadas' estava sempre desabilitado na edição de uma tarefa. Correção aplicada na versão 4.0.23 do app.

[20/03/2024] [Correção] Os valores dos produtos do cliente não estavam sendo resgatados pelo App durante a visualização da checklist e assim ela não era preenchida. Os produtos do cliente agora são resgatados da API ao carregar o negócio, sendo assim possível visualizar o preenchimento do campo caso tenha sido. Correção aplicada na versão 4.0.23 do app.

[20/03/2024] [Correção] A tela da lista de tarefas do app estava com uma lentidão muito grande para carregar as tarefas do mês visualizado, foi reajustado a query da API para melhorar a performance.

[20/03/2024] [Correção] O campo "título" da proposta estava sem limite de caracteres.

[20/03/2024] [Correção] No aplicativo, a barra "/" não estava incluída para pesquisas por CNPJ, CPF e telefone, dessa forma ao adicionar a "/" na busca, o aplicativo não retornava os clientes pelo CNPJ. A barra / foi adicionada para buscas por CNPJ na correção propagada na versão 4.0.23 do App.

[20/03/2024] [Correção] Abas de clientes estavam com a ordenação errada, desrespeitando a ordem configurada pelo usuário.

[21/03/2024] [Correção] Horário de notificações agora não segue mais cor do whitelabel para evitar que fique invisível em cores muito escuras.

[21/03/2024] [Correção] Quando um usuário não pode ver um campo de uma aba, não era possível que ele ordenasse a coluna.

[25/03/2024] [Correção] No aplicativo o tratamento da configuração da meta estava diferente da Web, levando em conta mostrar a porcentagem somente quando a opção estivesse marcada. O tratamento foi ajustado para agora quando a opção estiver marcada o App irá mostrar somente a porcentagem, igual ao Web, caso contrário o App mostra a quantidade e porcentagem. Correção aplicada na versão 4.0.24 do App.

[25/03/2024] [Correção] Por conta de um campo excluído, as ações de automações que tinham esse campo ficavam quebradas. O problema foi corrigido ignorando esse campo.

[25/03/2024] [Correção] Estilização de filtro simples quebrava quando existia filtros com nomes muito grandes, agora, existe um limite de tamanho do dropdown, e caso o nome não caiba completamente, terá um tooltip para que possa ver o nome completo.

[25/03/2024] [Correção] Na modal de criação de novo campo, caso fosse escolhido um valor padrão e o tipo do campo fosse modificado, o campo adicionado como padrão não era removido, e o dropdown de escolha de campo continuava aberto. Os dois comportamentos foram corrigidos, trazendo uma melhor consistência para aquela tela.

[25/03/2024] [Correção] Em comentários de Proposta/Venda/Documento, caso você clicasse muito rápido para comentar, era possível comentar a mesma coisa mais de uma vez.

[25/03/2024] [Correção] Alguns usuarios estavam com lentidão ao abrir o app, isso por conta das ações feitas offline

[25/03/2024] [Correção] Na integração com o Active Campaign, quando a opção 'Não criar o negócio caso já exista um aberto para o cliente' estava marcada, anteriormente, se já existisse um negócio aberto no Ploomes para o lead correspondente, não ocorria uma edição no negócio existente para atualizar seus campos quando ocorria algum gatilho no Active Campaign. Agora, essa edição é realizada, garantindo a atualização dos campos do negócio no Ploomes.

[25/03/2024] [Correção] O mapeamento do campo [VendaProduto.Transportadora] do Omie para o Ploomes não estava ocorrendo corretamente.

[26/03/2024] [Correção] No aplicativo ao acessar o módulo de funil o App fechava. O problema que ocorria era que ao montar os filtros na tela de seleção de funil, o aplicativo fechava caso tentasse ler uma propriedade de um campo que ainda não existia no banco offline. Agora o aplicativo recupera essa informação online caso ela não exista. A correção foi propagada na versão 4.0.24 do App.

[25/03/2024] [Correção] Adicionada verificação do acesso do perfil do usuário ao módulo de metas e corrigido problema em que o usuário sempre conseguia ver as metas, independentemente da permissão. Agora o aplicativo resgata a informação de acesso do perfil do usuário e exibe as metas com base nisso.

[26/03/2024] [Correção] Em fórmulas, o formato de data esperado pelo campo de data estava variando conforme a idioma, fazendo com que fórmulas que foram configuradas para o PT-BR (DD/MM/AAAA) não funcionem no formato americano (MM/DD/AAAA), por exemplo. Foi feito um tratamento no front-end para converter dinamicamente as datas conforme a linguagem, de forma que o retorno esperado seja sempre DD/MM/AAAA independente do formato apresentado para o usuário.

[26/03/2024] [Correção] Link da documentação do dataplace substituia a URL da própria aba que você está, agora abre uma nova aba.

[26/03/2024] [Correção] Quando nome de meta era muito grande, empurrava os botões para baixo e a tela para o lado.

[26/03/2024] [Correção] Mensagens de compartilhamento link web nas atualizações de proposta/venda/documento não estavam com o espaçamento correto.

[26/03/2024] [Correção] Ao criar um gráfico no modo de relatórios Beta, na parte de criar filtros, ao abrir o dropdown estava cortando algumas opções, impossibilitando o usuário de seleciona-las.

[26/03/2024] [Correção] O usuário não estava conseguindo colar o valor copiado nos campos do tipo numérico.

[26/03/2024] [Correção] O tooltip do campo de estágio não aparecia quando o filtro de estágio de funil era selecionado no formulário do filtro.

[26/03/2024] [Correção] No módulo de relatórios, não estava gerando os dados do gráfico de mapa por Estado corretamente por conta da sigla, exemplo, o Back estava retornando: SP, porém existe uma limitação do Google Charts que precisamos colocar a sigla do País primeiro, ficando BR-SP. A correção foi realizada para puxar os dados (Dimensão do gráfico) por Estado.

[26/03/2024] [Correção] Formatação de campos de data segue a língua do usuário, caso esteja em inglês, o formato de data com mês antes do dia será adicionado no código fonte.

[28/03/2024][Correção] Agora no resumo nos negócios criados do dia, caso o nome passe do limite do componente ele adiciona '...' e uma tooltip do conteúdo.

[28/03/2024][Correção] Agora quando o nome da entidade no gerador de documento ultrapassar o tamanho do card, um tooltip aparecerá informando o resto do que está escrito.

[28/03/2024][Correção] Ao visualizar o menu lateral direto em todos os negócios, caso o nome da entidade fosse muito grande o texto vazava, agora, terá ellipsis e um tooltip para quando isso ocorrer.

[28/03/2024][Correção] Botão de fechar configuração de opcionais do produto estava com o 'X' descentralizado.
