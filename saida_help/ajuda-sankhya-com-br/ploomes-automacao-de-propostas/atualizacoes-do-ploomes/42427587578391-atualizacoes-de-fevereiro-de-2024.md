---
id: "42427587578391"
titulo: "Atualizações de Fevereiro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427587578391-Atualiza%C3%A7%C3%B5es-de-Fevereiro-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:04Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8899274", "sync_hash_08f8a9e3888e"]
---

# Atualizações de Fevereiro de 2024

[01/02/2024] [Correção] No app, a interação com o campo multilinha foi reformulada. Agora em qualquer plataforma não é mais possível pinçar/arrastar por dentro do campo enquanto estiver no formulário. Porém, agora é sempre possível pressionar o campo e observar/interagir com o modal de edição. Esse comportamento funcionará até quando o campo estiver bloqueado.

[01/02/2024] [Correção] Anteriormente, os produtos que apresentavam estoques zerados no Omie eram transferidos para o Ploomes sem qualquer preenchimento no campo 'Tabela de Estoque (Omie)', quando o ideal seria que fossem preenchidos com o valor zero.

[01/02/2024] [Correção] O android estava tendo conflitos de gestos e interações com a propriedade que levava a lista de modelos para frente na tela. Essa propriedade foi removida somente para Androids, dessa forma a lista volta a funcionar normalmente.

[01/02/2024] [Correção] O app estava enviando para a API muitas informações da proposta durante o fluxo de aprovação, dessa forma a API aceitava as infos do app e não realizava buscas dentro do servidor, levando à respostas não atualizadas e não consistentes sobre as validações do fluxo.

[01/02/2024] [Correção] Ao converter proposta em uma nova venda o app não considerava como válido o valor 0 para campos numéricos. Esse comportamento foi corrigido na versão 4.0.14 do app.

[01/02/2024] [Correção] Campo de opção pré-cadastrada não puxava corretamente o valor padrão de outro campo de opção pré-cadastrada quando convertia proposta para uma nova venda. Esse comportamento foi corrigido na versão 4.0.14 do app.

[01/02/2024] [Correção] Não havia um tamanho definido para o título de metas no app, fazendo com que, dependendo do tamanho do texto e da tela do usuário quebrasse o layout. Esse comportamento foi corrigido na versão 4.0.14 do app.

[01/02/2024] [Correção] Diferente do web, no app, quando se criava um documento a partir da tela de negócio os campos de cliente e negócio apareciam. Esse comportamento foi corrigido na versão 4.0.14 do app.

[01/02/2024] [Correção] O botão de cancelar o modal de permissão de localização do app não permitia o usuário sair do modal. Agora o usuário consegue sair ao cancelar, mas não terá acesso ao check-in e nem ao componente de mapa do registro de tipo visita. Esse comportamento foi corrigido na versão 4.0.14 do app.
[02/02/2024] [Correção] Ao clicar em compartilhar proposta por e-mail ocorria o erro "Documento url missing" e não permitia enviar o e-mail com a proposta. O problema ocorreu devido ao sistema de envio de e-mails que usa o gerador de PDF enviando URLs com duas barras e com a mudança na tecnologia do gerador essas duas barras passaram a ser interpretadas de forma diferente causando o erro citado que já foi corrigido.

[05/02/2024] [Correção] Por conta de um erro no código, não era possível criar novas cidades no campo nativo cidades. O problema foi corrigido.

[05/02/2024] [Correção] Era possível selecionar o campo Cliente.Contatos nos formulários externos, mas esse campo não pode ser mapeado lá. Foi feito um filtro para esse campo não aparecer para seleção.

[05/02/2024] [Correção] Uma mudança no backend passou a obrigar os filtros a terem um atributo Name. Foi feita uma tratativa no frontend para se adequar à essa mudança.

[05/02/2024] [Correção] O consumidor da fila consumiu o webhook de alteração do cliente diversas vezes simultaneamente por conta de uma lentidão ao confirmar o consumo do primeiro webhook, criando contatos duplicados. Aumentamos o tempo de timeout para fazer essa confirmação.

[05/02/2024] [Correção] Foi criado uma validação para o campo do tipo Cor ao criar/editar um checklist. Estava sendo possível colocar qualquer sequência de caracteres, ou seja, cores que não seriam válidas.

[05/02/2024] [Correção] Ao gerar a proposta a ordenação definida no produto pai não era seguida.

[05/02/2024] [Correção] Foi feita uma revisão da tela de pagamento, removendo o formulário e bloqueando alguns campos que não deveriam ser editados.

[05/02/2024] [Correção] O ícone da Ploomes não estava aparecendo na tela de login nas contas com whitelabel, por conta de onde estava sendo apontada a imagem.

[05/02/2024] [Correção] Uma automação em específico do cliente estava com a data em formato errado, e por esse motivo estava quebrando as automações, foi preciso realizar uma alterações para converter data inválida em uma data válida.

[05/02/2024] [Correção] Os ícones de duplicar bloco e remover bloco estavam descentralizados.

[05/02/2024] [Correção] Em contas com whitelabel cadastrado, não estava sendo possível apresentar o título correto na aba da página de login. Foi adicionado um campo novo nas configurações de whitelabel para poder customizar o nome da aba da tela de Login.

[06/02/2024] [Correção] Ao remover e inserir novamente um opcional, em algumas situações, o valor da fórmula não era calculado novamente, levando a erros.

[06/02/2024] [Correção] Em formulário externo de edição de negócio, caso o negócio já possuísse um cliente, ao invés de editá-lo ele estava removendo o cliente e substituindo por um novo. Foi feita a correção para ele apenas criar um novo se o negócio não possuir cliente, caso contrário ele edita o já preenchido.

[06/02/2024] [Correção] Ao adicionar/editar um produto na proposta modal, caso as fórmulas demorassem para calcular, era possível salvar a proposta sem que elas calculassem. O botão de salvar agora fica bloqueado por alguns segundos após inserir/editar o produto em propostas, vendas e documentos no modal.

[06/02/2024] [Correção] Ao configurar um checklist com uma condição maior/menor que, caso o valor comparado fosse vazio, o front entendia que o checklist era válido (vazio menor que 100 por exemplo), mas o backend acusava como inválido e não permitia a passagem da etapa. O comportamento foi corrigido adequando o front ao comportamento do backend, onde vazio não pode ser menor ou maior que nada.

[07/02/2024] [Correção] A requisição do Calendar para buscar os calendários por padrão retorna 100 resultados, ocultando o demais caso o usuário tenha mais de 100 calendários em sua conta. Aumentamos esse limite para 250.

[07/02/2024] [Correção] Por conta de um erro no código, algumas fórmulas não eram calculadas quando o produto era inserido no modal de criação de proposta + negócio. O problema foi corrigido.

[07/02/2024] [Correção] Ao deletar uma seção de um form, mesmo removendo os campos da seção previamente, esses campos eram deletados. O problema foi corrigido salvando os campos antes de deletar de fato a seção.

[08/02/2024] [Correção] Por conta de um erro no código, o cache do form no front não era atualizado mais ao salvar o formulário, fazendo com que alterações no campo só fossem refletidas ao dar um F5 na página. O comportamento foi corrigido.

[08/02/2024] [Correção] Por conta de uma atualização no intercom, foi necessário adicionar mais um parâmetro nas configurações.

[08/02/2024] [Correção] Um erro no código estava causando um erro no console relacionado à tooltips. O problema foi corrigido.
[08/02/2024] [Correção] Relatório Beta não estava retornando os dados comparando com o mesmo gráfico no módulo de relatórios atual. O Beta retornava como gráfico vazio.

Foi Adicionada uma verificação para garantir que a consulta encontre o tipo certo para retornar os dados no gráfico do relatório beta.

[08/02/2024] [Correção] Botão de adicionar e remover telefones estava com o ícone maior do que o próprio botão, o tamanho do botão foi ajustado para comportar o ícone.

[08/02/2024] [Correção] Nos relatórios beta não era possível incluir um filtro no gráfico com a função "não contém".

[08/02/2024] [Correção] Em alguns lugares do sistema, o nome da entidade negócios não aparecia conforme o nome configurado no módulo. O problema foi corrigido nas abas e filtros.

[09/02/2024] [Correção] Ao fazer a exclusão de um cliente, o backend considerava também os dados já excluídos anteriormente, o que tornava a requisição mais complexa e lenta.

[09/02/2024] [Correção] E-mails para usuários em espanhol não eram enviados.

[09/02/2024] [Correção] Integração D4sign retornava erro 500 quando o usuário tenta atualizar valor do campo de proposta UUID Doc D4sign via API.

[14/02/2024] [Correção] Os nomes dos idiomas disponíveis no sistema do app estavam com sua gramática incorreta. Esses nomes foram corrigidos.

[14/02/2024] [Correção] O app não possuía um tratamento para caso o usuário clicasse rapidamente em dois campos com modal. Foi adicionado um tratamento para que o usuário não consiga abrir outro modal de campo enquanto estiver abrindo o primeiro.

[14/02/2024] [Correção] O app sempre formatava o campo de data para dia/mês/ano, independente do idioma ser inglês. A formatação do formato inglês para usuários com o sistema no idioma inglês foi adicionada. Agora o campo de data mostrará a data no formato mês/dia/ano.

[14/02/2024] [Correção] A forma que o botão flutuante era renderizado não permitia que ele conseguisse sobrepor todos os componentes da tela. Agora, o botão flutuante da tela de contatos é levado para mais a frente na tela, dessa forma sobrepondo todos os outros componentes.

[14/02/2024] [Correção] O app não estava formatando os apóstrofos na busca de um cliente de forma correta antes de enviar para a API. Dessa forma qualquer ' ou " quebrava o app. Foi adicionado o tratamento para esses casos.

[14/02/2024] [Correção] Os campos de checklist estavam com o fluxo de anexos desatualizados comparado aos campos normais. A função que faz busca do anexo em dispositivo Android foi atualizada para manter consistente o nome do arquivo escolhido.

[15/02/2024] [Correção] Os usuários não estavam conseguindo visualizar o Histórico de Faturamento da conta por conta de um problema de ids muito grandes no banco de dados. Foi corrigido aumentando o tamanho dos números que a estrutura no código suporta.

[15/02/2024] [Correção] No app, ao criar uma tarefa com cliente vinculado era exibido apenas o nome do cliente e não o título da tarefa. Correção foi aplicada na versão 4.0.17 do app.
[15/02/2024] [Correção] Campo de Estado de Cidade (Cidade → Estado) estava com o ícone de edição habilitado na visualização por aba, mesmo não sendo possível a sua edição e exibindo erro ao tentar realizar a edição. Foi corrigido, agora o ícone não está mais sendo exibido.

[15/02/2024] [Correção] Campo de porcentagem no app não estava permitindo inserir vírgula ou ponto, impossibilitando o usuário de preencher valores decimais.

[15/02/2024] [Correção] Ao criar negócio sem título, o Ploomes salvava o card com "No Title", em vez de "Sem título".

[15/02/2024] [Correção] Na criação de proposta, quando cai no fluxo de aprovação relacionado a um cliente, e eu altero, o fluxo continua exibindo o cliente anterior. Agora, quando o usuário troca o cliente preenchido na proposta, o campo de negócio é zerado, com isso, além de tratar o problema de um cliente e negócio que não possuem vínculos criarem uma proposta, também evita erros de fluxo de aprovação.

[15/02/2024] [Correção] Dentro do filtro do campo de Produtos, o campo de ID não aparece, assim não sendo possível filtrar produtos por ID. Todos os campos nativos de ID estavam sendo escondidos por padrão. Agora, caso o campo seja referente ao id de um produto, esse campo não será escondido.

[15/02/2024] [Correção] Em aparelhos com o a versão 8 do Android, o app fechava ao tentar abrir.

[16/02/2024] [Correção] Ao baixar um novo Modelo após a inicialização do app, a lógica de construção de formulário atualizava esse modelo de forma incompleta, resultando em formulários vazios.

[16/02/2024] [Correção] Ao utilizar formulário externo para atualização de cliente era criado novo cliente.

[17/02/2024] [Correção] Ao trocar de linguagem, o app apenas traduzia itens estáticos como por exemplo: "Editar cliente", desconsiderando os campos nativos. O comportamento foi corrigido.

[17/02/2024] [Correção] Após atualização da versão do App para dispositivos Android, não houve a configuração de uma nova permissão para notificações em Android 13. Essa permissão foi adicionada e agora Android 13+ podem habilitar/desabilitar notificações.

[19/02/2024] [Correção] Botão para fechar modal de assinar o Ploomes estava desalinhado.

[19/02/2024] [Correção] Mensagem de campo duplicado aparecia incorretamente. A lógica de verificação foi corrigida, agora levando em conta a linguagem e valor.

[19/02/2024] [Correção] Caso o usuário tivesse um campo de numero inteiro obrigatório e tentasse adicionar o décimo carácter, a validação de obrigatoriedade quebrava e impedia de salvar o formulário.

[19/02/2024] [Correção] Ao clicar várias vezes na lupa de procurar produtos dentro de uma proposta/venda/documento, várias janelas eram abertas, agora, apenas uma por vez é aberta.

[20/02/2024] [Correção] A lista de documentos/propostas/vendas não estava observando e se atualizando ao haver edições em documentos/propostas/vendas. Agora, ao alterar um documento/proposta/venda as listas irão atualizar automaticamente.
[20/02/2024] [Correção] O app não possuía tratamento para atualizar a soma dos valores de um funil após criar/editar/deletar um negócio. Agora, quando um negócio é criado/editado/excluido, a soma dos valores de um funil será atualizada.

[20/02/2024] [Correção] A checagem que o app fazia para mostrar ou não as opções de edição e exclusão do registro de interação não estavam funcionando no modo OFF. Essa checagem foi ajustada para aparecer corretamente no modo OFF, além de levar em conta agora as permissões de edição e exclusão de registros de interação do Perfil do usuário.

[20/02/2024] [Correção] O app não estava atualizando o indicador no topo da tela de meta e resumo durante o evento do usuário arrastar a tela para o lado.

[20/02/2024] [Correção] Em metas, o app não estava atualizando a lista após o usuário selecionar algum filtro. Agora, quando o usuário fecha o modal de opções de filtro, o app atualiza a lista de metas automaticamente.

[20/02/2024] [Correção] No RD Station, quando a opção 'Quando um negócio for ganho no Ploomes, criar ou atualizar o contato no RD Station' estava marcada, mas, a opção no campo 'Qual ação no negócio do Ploomes gera uma venda no lead referente do RD Station?' estava marcada com alguma opção diferente de 'Ganhar Negócio', ao ganhar o negócio o lead não era atualizado/criado no RD Station, ocasionando em um comportamento divergente.

[20/02/2024] [Correção] Quando recebíamos uma venda do Omie, não havia uma verificação para determinar se o responsável estava ativo no Ploomes ao ser adicionado. Implementamos uma validação para garantir que apenas usuários ativos sejam atribuídos como responsáveis.

[20/02/2024] [Correção] Havia um problema com a requisição feita para atualizar as integrações. O erro foi corrigido.

[22/02/2024] [Correção] Dependendo do endereço pesquisado no campo de busca por endereço vinculado ao Google, a API da própria Google retornava um CEP incompleto, preenchendo o campo de CEP de forma errada. Esse caso acontecia em CEPs que continham final -000. Agora o app possui um tratamento para esses casos.

[22/02/2024] [Correção] Campo 'Cliente' estava aberto para ser alterado na edição de um registro de interação no app.

[22/02/2024] [Correção] Ao buscar negócio com aspas simples (') em um registro de interação, o app crashava.

[22/02/2024] [Correção] Ao buscar negócio com aspas simples (') em funil, o app crashava.

[22/02/2024] [Correção] No app, estava sendo possível clicar rapidamente em algum campo opção pre cadastrada e no botão de "adicionar produto/serviço" e isso fazia o modal do campo abrir dentro da tela de Produto. Foi adicionada uma checagem para impedir que a tela de Produto e modal sejam abertos ao mesmo tempo.

[22/02/2024] [Correção] Os campos de Latitude e Longitude se tornaram abertos para o usuário preencher manualmente, possibilitando a inserção de coordenadas invalidas. Agora o app possui uma tratativa para esses casos.

[22/02/2024] [Correção] Não estava sendo definido na API a ordem que as assinaturas deveriam vir ao APP. Foi adicionada uma ordenação padrão nos campos de assinaturas vindos da API.

[22/02/2024] [Correção] O app não estava calculando a lista de negócios quando vazia e no modo offline, resultando em um load infinito. Uma checagem que levava a esse erro no calculo foi removida, e dessa forma a lista agora também aparece quando está vazia e no modo offline.

[22/02/2024] [Correção] O campo [Documento.Número] era editável, mesmo sendo autoincrementado pelo banco.

[22/02/2024] [Correção] Campo de produtos de documento não retornava em aba de negócios porque o LastDocument retornava null quando a requisição GET em Deals retornava os dados do card.

[23/02/2024] [Correção] Anteriormente, na integração com o DocuSign, a busca pelos campos de assinatura no documento só considerava aqueles que estavam presentes no momento da sua criação. Isso resultava na não exibição de campos adicionados posteriormente no modelo de documento. Foi realizada uma atualização para corrigir esse comportamento, e agora todos os campos, independentemente de quando foram adicionados ao modelo, são listados no modal de compartilhamento.

[28/02/2024] [Correção] No app, a lista de tarefas na tela de cliente estava com a ordenação errada. Agora o app ordena as tarefas por ordem crescente, respeitando a data e horário que a tarefa irá acontecer.

[28/02/2024] [Correção] Ao criar nova proposta com a opção de cor, se a cor utilizada no campo de cor fosse preta, branca ou similar, o aplicativo quebrava com o valor inválido de matiz. Agora, o aplicativo verifica se a cor possui um matiz válido. Se não for, considera como zero, o que é esperado.

[28/02/2024] [Correção] O componente antigo foi removido por possuir uma má usabilidade e agora são mostrados os novos toasters de loading quando o usuário altera um campo da checklist.

[28/02/2024] [Correção] Não havia um modal para avisar ao usuário quando ele tenta salvar a assinatura sem assinar. Esse modal foi adicionado.

[28/02/2024] [Correção] Ao tentar habilitar a integração com o Calendar, o front exibia um pop-up de sucesso na ação, porém ao fechar o modal da integração e abri-lo novamente, o Ploomes o mostrava desabilitado.

Caso o usuário clicasse 2 vezes em "Habilitar integração", o front exibia a mensagem de erro "Erro! Autorize a integração".

[29/02/2024] [Correção] Na integração com o LeadLovers, se um lead chegasse sem uma empresa associada no Ploomes, era verificado se existia alguma empresa no Ploomes com o nome ou a Razão Social vazios. Se uma empresa correspondente fosse encontrada nessas condições, ela era vinculada ao lead, resultando em uma associação equivocada.
