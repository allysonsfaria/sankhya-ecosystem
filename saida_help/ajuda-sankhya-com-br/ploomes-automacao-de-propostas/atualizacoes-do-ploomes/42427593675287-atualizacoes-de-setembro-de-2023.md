---
id: "42427593675287"
titulo: "Atualizações de Setembro de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427593675287-Atualiza%C3%A7%C3%B5es-de-Setembro-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:23Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_5bb11800ac6d", "ploomes_8321747"]
---

# Atualizações de Setembro de 2023

[01/09/2023] [CORREÇÃO] No formulário externo era permitido adicionar o campo "Tipo", que em teoria define o tipo do cliente, mas é impossível definir o tipo do cliente durante o preenchimento do form externo.

[01/09/2023] [CORREÇÃO] Recarregar tela na edição de Deal com configuração de escolher funil não voltava para a edição.

[01/09/2023] [CORREÇÃO] Antes de alterar o estágio de um negócio, havia uma validação que poderia ocasionar erros, caso a ordenação dos estágios estivesse com problema. Foi reforçada essa validação para evitar que esse tipo de erro aconteça.

[01/09/2023] [CORREÇÃO] Foi alterada a estilização dos vínculos de produtos que, caso o nome do produto fosse extenso fazia com que os texto se sobrepusessem.

[01/09/2023] [CORREÇÃO] Ao clicar no ícone do WhatsApp em algum contato do cliente, estava sendo incluído o 55 antes do número para todos os casos, independente se seria número do Brasil ou não, foi padronizado que quando houver mascara do Brasil será adicionado o 55 na frente, caso contrário seguirá com o próprio número que o usuário cadastrou.

[01/09/2023] [CORREÇÃO] Era permitido a criação de filtros que verificavam se um campo decimal era "maior que", "maior ou igual a", "menor que" ou "menor ou igual a" a um valor nulo, o que resultava em erro da operação.

[01/09/2023] [CORREÇÃO] Ao criar um campo dinâmico e inserir no formulário de registro de interação, não estava validando quando o usuário registrava algo, ou seja, possibilitando deixar um campo vazio e não passar por validação no front, foi corrigido e agora conseguimos validar se o campo está vazio ou não.

[01/09/2023] [CORREÇÃO] Ao adicionar um parâmetro na URL no módulo de criar um novo documento, agora é possível ser direcionado para o modelo que o usuário passou no parâmetro "modelId", ou seja, caso o usuário crie uma URL da seguinte forma: [https://www.app10.ploomes.com/deal/{id\_deal}/newdocument?modelId={id\_modelo}](https://www.app10.ploomes.com/deal/%7Bid_deal%7D/newdocument?modelId=%7Bid_modelo%7D) será selecionado automaticamente o modelo, caso não exista, aparecerá uma mensagem dizendo que não existe o modelo que o usuário buscou.

[01/09/2023] [CORREÇÃO] Campo com uma fórmula sem variáveis estava engatilhando na web, causando um comportamento incorreto e divergente entre web e mobile.

[01/09/2023] [CORREÇÃO] Campo de filtro em relatórios beta estava bloqueado, não permitindo edição.

[01/09/2023] [CORREÇÃO] Proposta estava entrando no fluxo de bloqueio que não deveria ao tentar "Atualizar dados e modelo". Na criação da proposta, não entrava no fluxo de bloqueio, porém quando o cliente editava a proposta e após isso tentava atualizar dados e modelo sim. Havia um problema ao enviar os dados ao backend para validar os fluxos de aprovação ao clicar em "Atualizar dados e modelo". Foi feita a correção do que é enviado para o backend para resolver o problema.

[01/09/2023] [CORREÇÃO] Em formulário mini de criação de empresa, ao mudar o responsável da empresa o Ploomes não estava buscando o valor dos campos customizados, o que resultava em algumas fórmulas não sendo calculadas corretamente.

[01/09/2023] [CORREÇÃO] Ao fazer uma busca numa tabela utilizando o campo de filtro rápido, caso a tabela estivesse em uma página avançada, não era exibido nada por conta da página não ser a primeira. Foi corrigido fazendo com que a tabela sempre volte à primeira página ao aplicar o filtro digitado pelo usuário.

[01/09/2023] [Correção] Seção de propostas em negócio e no cliente apresentavam informações incoerentes.

[01/09/2023] [Correção] Na tela de criação de filtros dos relatórios beta não estavam sendo exibidos somente os marcadores da entidade selecionada, e sim todos da conta.

[01/09/2023] [Correção] Ao excluir um fluxo de aprovação e criando outro logo em seguida gerava um problema que não carregava o novo fluxo na lista. Foi corrigido.

[04/09/2023] [CORREÇÃO] Integração com Exact Spotter não criava lead no Ploomes se o campo de telefone 1 da empresa for marcado como opcional no Spotter e estiver vazio na criação.

[04/09/2023] [CORREÇÃO] Mapeamento da integração do Meetime havia perdido a referência dos campos personalizados.

[06/09/2023] [CORREÇÃO] Falha na obrigatoriedade de campo de formulário externo.

[06/09/2023] [CORREÇÃO] Por conta de divergências na forma como cada navegador trata a estilização do HTML, no Firefox o botão do campo de anexo não estava sendo exibido. Foi alterada a estrutura para uma forma compatível com todos os navegadores.[06/09/2023] [CORREÇÃO] Em formulários externos, ao preencher um campo obrigatório de opções pré-cadastradas e remover seu valor, a obrigatoriedade não era respeitada e criava mesmo com o campo vazio.

[08/09/2023] [CORREÇÃO] No aplicativo, campos-chave não ficavam com a chave vermelha ao inserir um valor que já existe na conta.

[08/09/2023] [CORREÇÃO] No aplicativo, pesquisa de endereço não estava autocompletando.

[08/09/2023] [CORREÇÃO] Campos nativos não tinham seus títulos traduzidos pelo Ploomes quando o idioma era alterado para o espanhol.

[08/09/2023] [CORREÇÃO] Edição em massa em aba de negócios não alterava responsável.

[11/09/2023] [CORREÇÃO] Relatórios velho computando errado ao utilizar data relativa igual aos últimos 7 dias.

[11/09/2023] [CORREÇÃO] Cliente possui somente uma imagem no rodapé do modelo de proposta em que ao fazer o download em PDF ficava um espaçamento no final da página, criando uma faixa em branco depois da imagem. O problema acontecia por usar paginação no modelo de proposta, foi realizada a correção para não exibir mais essa faixa branca ao usar paginação.

[12/09/2023] [CORREÇÃO] Alguns dados do novo exportador do Power Bi estavam saindo com incongruências em relação ao exportador antigo.

[12/09/2023] [CORREÇÃO] Campos de anexo de formulário externo não funcionavam.

[12/09/2023] [CORREÇÃO] Os campos de Número (Endereço), Código Postal Internacional, Código e Descrição CNAE não estavam funcionando como chave.

[13/09/2023] [CORREÇÃO] Tarefas editadas no Ploomes não estavam atualizando no Google Calendar.

[13/09/2023] [CORREÇÃO] Formulário externo ao ser preenchido exibia mensagem de erro, porém cliente era criado mesmo apresentando erro. O erro estava sendo causado pelos campos-chave de data que não estavam funcionando. Correção foi propagada e agora os campos-chave de data funcionam corretamente.

[14/09/2023] [CORREÇÃO] Ao editar as colunas de uma aba, o campo 'Nome' da entidade 'Produto' era exibido duas vezes. O comportamento foi corrigido para remover essa opção excedente.

[14/09/2023] [CORREÇÃO] Campos de opções pré-cadastradas não estavam salvando a opção selecionada como valor padrão. Correção foi propagada para salvar corretamente.

[14/09/2023] [CORREÇÃO] Ao tentar adicionar um filtro simples a um campo de Negócio do tipo Cliente, esta dando erro para "tentar mais tarde".

[14/09/2023] [CORREÇÃO] Ao fazer uma modificação visual na proposta, e editar a proposta em seguida, ao salvar a edição, os produtos da proposta não estavam sendo exibidos.

[14/09/2023] [CORREÇÃO] Ao criar um registro de interação finalizando uma tarefa com observações, o campo de data não era preenchido automaticamente no formulário como acontece em outros locais do front. Foi feita uma melhoria para que essa data seja preenchida automaticamente ao abrir o formulário.

[14/09/2023] [CORREÇÃO] Ao tentar fazer edição em massa de um campo bloqueado, o Ploomes não permitia inserir o campo, mas não havia uma mensagem explicando o motivo. Foi adicionada uma mensagem de erro que será disparada quando o usuário tentar adicionar um campo nessa situação no menu de edição em massa.

[14/09/2023] [CORREÇÃO] Quando a descrição de uma tarefa tinha tags html, a visualização quebrava e a tarefa ocupava todo o espaço do texto contido nela ao invés de apenas mostrar uma linha da descrição.

[14/09/2023] [CORREÇÃO] Foi feita uma correção para que a cor do elemento de carregamento da tela de e-mails fosse a mesma da tela de relatórios beta.

[14/09/2023] [CORREÇÃO] Salvar uma automação periódica com data retroativa gerava diversos problemas na execução da automação. Para evitar esse tipo de problema, travamos a criação de automações com data retroativa.

[14/09/2023] [CORREÇÃO] Atualizar dados e modelo de uma proposta não funcionava caso o usuário tivesse marcado a opção de obrigar as parcelas. Foi corrigido o problema.

[14/09/2023] [CORREÇÃO] Quando o último caractere do cliente da negociação era um ponto, havia um erro para definir a extensão do arquivo, fazendo com que ele assumisse uma extensão desconhecida.

[14/09/2023] [CORREÇÃO] Todos os lugares que estava sendo mostrada as tabelas dinâmicas, exemplo, módulo de cliente em visualização por tabela, estava sendo executada duas requisições iguais nos seus respectivos end-points para ser construída a tabela, foi solucionado o problema.

[14/09/2023] [CORREÇÃO] Campo de moeda não aparecia no formulário de criação/edição de produtos da proposta.

[14/09/2023] [CORREÇÃO] Quando um documento era bloqueado por fluxo de aprovação no formato de tela cheia e o usuário clicava em 'descartar', o usuário não estava sendo redirecionado para a tela de negócio, conforme esperado. Foi feita uma correção para que esse redirecionamento aconteça.

[14/09/2023] [CORREÇÃO] Na opção de configurar fórmula temos alguns códigos prontos que o usuário pode usar, porém, ao adicionar esses códigos que contém conversão de data, exemplo (Data + X dias), as automações não rodavam, porque estava convertendo para o padrão brasileiro (DD/MM/YYYY). Esses códigos de conversão de data foram modificados para converter para padrão ISO (YYYY-MM-DD), que é o padrão que o campo de data aceita para poder rodar as automações da forma correta.

[14/09/2023] [CORREÇÃO] Ao tentar adicionar signatário no campo de e-mail da tela de compartilhamento via clicksign, o front retornou a mensagem de erro "Telefone já inserido".

[14/09/2023] [CORREÇÃO] Mudar o nome da métrica dos relatórios, no módulo Beta, só era possível quando a métrica era acessada.

[14/09/2023] [CORREÇÃO] Ao editar o responsável usando o formulário mini, o front apresentava um carregamento contínuo, não sendo possível salvar nem mesmo cancelar a edição.

[14/09/2023] [CORREÇÃO] Busca geral de Clientes no app não estava retornando resultado, apenas ficando em looping como se ainda estivesse buscando.

[14/09/2023] [CORREÇÃO] Integração com o LetsSign não anexava no cliente os documentos após serem assinados.

[16/09/2023] [CORREÇÃO] Ao criar contato via importação de registro de interação, contato estava sendo criado como do tipo empresa ao invés do tipo pessoa.

[18/09/2023] [CORREÇÃO] Quando o título do negócio tinha muitos caracteres e a tela do usuário era pequena, os botões ganhar/perder eram empurrados para a direita sumindo da tela.

[18/09/2023] [CORREÇÃO] Na edição de uma proposta, ao trocar de modelo, caso o modelo anterior já não tivesse um campo de vínculo de produto da proposta que puxe a família do produto via fórmula, no novo modelo essa família não era encontrada por fórmula.

[18/09/2023] [CORREÇÃO] Campos dos checklists de Negócios estavam sendo limpos quando era criado automaticamente uma nova checklist. Comportamento foi corrigido.

[18/09/2023] [CORREÇÃO] Ao gerar uma venda, o front procurava o último modelo utilizado pelo usuário ao invés do modelo padrão na tela de cliente. Foi corrigido para que ele use o modelo padrão, e só use o último utilizado caso não haja um modelo padrão.

[18/09/2023] [CORREÇÃO] Ao inserir um produto em produtos da venda do modelo "Encomenda Direta", o campo [Produto da Venda.Data de Entrega] retornava outro conteúdo que não o de data para preenchimento.

[18/09/2023] [CORREÇÃO] Campo de produto do cliente aparecia com uma mensagem "Negócio não tem undefined" em checklists.

[18/09/2023] [CORREÇÃO] Áudios do Zenvia não estavam carregando no Ploomes.

[18/09/2023] [CORREÇÃO] Ao tentar modificar os filtros dos indicadores na tela de inicio, estava dando erro por conta dos dados que o front estava enviado para o back, e assim, não atualizava os valores com os filtros corretos! além disso, foi incluído uma melhoria para enviar apenas os dados necessários para serem modificados no back.

[18/09/2023] [CORREÇÃO] Ao criar uma formula condicional, o cliente estava inserindo alguns códigos extensos, porém essa funcionalidade não foi feita para ter códigos mais complexos, como, por exemplo um condicional if com escopo (if("[Client.Bairro]"==="") {...}), com isso, estava quebrando algumas automações. Foi feita uma validação para o usuário usar de forma correta o módulo.

[18/09/2023] [CORREÇÃO] Os campos [Negócio.Empresa] e [Negócio.Cliente] são do tipo Cliente e, ao serem adicionados em formulário de novo negócio e terem o conteúdo preenchido, tinham o conteúdo resetado, ou seja, eram limpados.

[18/09/2023] [CORREÇÃO] O campo [Proposta.Alerta - Segmento do cliente] do tipo texto simples não retornava o valor definido na fórmula dele para retornar o campo [Cliente.Criador] quando era engatilhado no formulário de criação de uma proposta.

[18/09/2023] [CORREÇÃO] Não era exibido nenhuma mensagem de erro quando um usuário tentava usar um metódo de envio que não possuia acesso no LetsSign.

[18/09/2023] [CORREÇÃO] Em ordem de serviço, a integração com o Omie não estavam aplicando as edições devidas no lado Ploomes pro Omie após muitas atualizações.

[18/09/2023] [CORREÇÃO] Para alguns usuários, aba superior do Ploomes não estava aparecendo.

[20/09/2023] [CORREÇÃO] Botão "Trazer Vendas de Produto/Ordens de Serviço para o Ploomes" da integração com o Omie não estava trazendo as ordens de serviço.

[20/09/2023] [CORREÇÃO] O lead "Alessandro Aqua&Flor" não integrou no Ploomes porque possuía o caractere especial "&".

[21/09/2023] [CORREÇÃO] Em contas duplicadas os filtros de checklist não funcionam.

[22/09/2023] [CORREÇÃO] No aplicativo, quando criávamos tarefa com um fuso diferente do UTC do Brasil, ele não seguia o funcionamento na web e alterava as horas de acordo com a diferença do UTC, isso gerava inconsistencias entre App e Site, onde tarefas eram jogadas para o dia anterior em alguns casos.

[26/09/2023] [CORREÇÃO] Devido ao formato dos webhooks do ActiveCampaign, era feita uma conversão para numérico de todos os campos possíveis de converter. Por conta disso, CNPJs com 0 no começo era convertidos para numérico e perdiam os primeiros caracteres com 0, salvando o valor errado no Ploomes.

[28/09/2023] [CORREÇÃO] No app quando o usuário vai cadastrar um novo cliente, as seções de "Localização", "Informações Financeiras" e "Entrega" não permitem a edição, como se estivessem bloqueado. Mesma coisa acontece dentro de um cadastro já existente, quando se vai tentar editar o cliente.

[28/09/2023] [CORREÇÃO] Não conseguimos gerar propostas em negócios que foram criados no OFF, porém é possível criar propostas através do módulo de documentos ou através de outros negócios.

[28/09/2023] [CORREÇÃO] Quando o formulário de cliente possui o campo ID e tentasse fazer uma edição, não era apresentado a atualização dos dados do cliente após clicar em salvar alterações.

[28/09/2023] [CORREÇÃO] O problema era que informações salvas no formulário de finalização de tarefa com observação não estavam sendo mandados para o servidor. Isso foi corrigido incluindo os valores que não eram enviados na requisição de envio para o servidor.

[28/09/2023] [CORREÇÃO] O banco off não estava salvando uma propriedade dos negócios que o filtro de negócio necessitava para filtrar. Isso foi corrigido incluindo essa propriedade na estrutura do banco off.

[28/09/2023] [CORREÇÃO] Não era possível descartar um valor editado em um campo de checklist clicando no botão "x". Isso foi corrigido através do descarte do valor inserido e a restauração do valor antigo existente caso o usuário clique no "x".

[28/09/2023] [CORREÇÃO] O app estava somente incrementando contatos durante a edição de campos múltiplos, e não estava excluindo os valores que deveriam ser removidos. Foi corrigido trocando a incrementação dos valores pela substituição dos valores antigos pelos novos.

[28/09/2023] [CORREÇÃO] No app, foi verificado que estava tendo uma instabilidade no recebimento de notificações, algumas notificações não estavam chegando, ou estavam demorando muito para chegar.

[28/09/2023] [CORREÇÃO] O problema era que o app estava sempre puxando uma variável da formula pelo banco off e não pelo servidor, mesmo quando ela não existia no banco off, assim não executando a formula. Foi corrigido isso, agora a informação necessária é requisitada para o servidor quando ela não existe e salva no banco off.

[28/09/2023] [CORREÇÃO] Quando tínhamos o campo "Id" inserido no formulário do cliente e este cliente possui CNPJ. Quando tentamos realizar a edição e salvar, é retornado um erro "Já existe um cadastro com o mesmo CNPJ".

[28/09/2023] [CORREÇÃO] A lista de contatos de uma companhia estava visualmente duplicando um contato já existente na lista quando outro era adicionado. Foi corrigido através de uma recarregamento correto da lista após a criação de um novo contato.

[28/09/2023] [CORREÇÃO] No aplicativo, na tela de criação de proposta acessado através do Cliente, ao trocar o modelo de proposta, o Negócio que estava selecionado era desvinculado do campo. O app estava remontando todo o formulário quando se trocava de modelo, e isso zerava o negócio inserido depois da montagem. Agora foi corrigido e está mantendo o negócio durante as remontagens do formulário.

[28/09/2023] [CORREÇÃO] Ao criar clientes através do aplicativo, os campos sem preenchimentos eram apresentados como "null", tanto no app quanto no web, quando deveriam somente deixar o campo em branco.

[28/09/2023] [CORREÇÃO] Na integração com o Docusign, clientes que possuisem caractere '&' no nome não estavam recebendo o documento assinado.

[28/09/2023] [CORREÇÃO] Na integração com o Clicksign, documentos não eram salvos como anexo após a última assinatura porque em alguns casos era feita uma verificação de "todos já assinaram" com base no estado do documento antes de ser atualizado. Agora a verificação é sempre com base no documento atualizado, evitando que esse erro ocorra novamente.

[29/09/2023] [CORREÇÃO] Menu propriedades de lista numerada não era exibido na proposta.
