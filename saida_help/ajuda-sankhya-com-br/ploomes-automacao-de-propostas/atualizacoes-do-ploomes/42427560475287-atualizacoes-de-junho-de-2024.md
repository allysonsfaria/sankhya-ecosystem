---
id: "42427560475287"
titulo: "Atualizações de Junho de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427560475287-Atualiza%C3%A7%C3%B5es-de-Junho-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:53Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9439962", "sync_hash_f22f29bb17cf"]
---

# Atualizações de Junho de 2024

[03/06/2024] [Correção] Nos relatórios beta, o campo de "Dias no estágio" não funcionava da forma correta.

[03/06/2024] [Correção] Ao adicionar um produto e apertar enter era retornado um erro, pois o método de adicionar produto estava sendo chamado com botão desabilitado, agora o método é chamado apenas com o botão habilitado.
[03/06/2024] [Correção] A seção "Vínculos de entidades" na biblioteca ao selecionar um anexo não tinha um scroll, impossibilitando a visualização ou remoção caso tenha mais vínculos do que o tamanho da página comportaria.

[03/06/2024] [Correção] Ao inserir um telefone muito longo em uma conta com a integração com Whatsapp ativada, na visualização de negócio/cliente, o ícone do Whatsapp ficava atrás do ícone de edição. O problema foi corrigido e em números longos também aparece uma tooltip ao passar o mouse em cima.

[03/06/2024] [Correção] O nome e tipo do opcional sumiam ao adicionar um novo produto. A correção foi realizada e agora os nomes e tipos não somem antes do modal fechar.

[03/06/2024] [Correção] Na criação de uma Proposta e Negócio, quando o contato de um novo negócio era alterado diretamente no modelo da proposta, o campo não era limpo ao trocar o cliente. Agora o campo fica vazio ao trocar de cliente.

[03/06/2024] [Correção] O erro mostrado quando se tentava remanejar um negócio com checklists pendentes era genérica. Foi adicionada uma mensagem mais explicativa.

[03/06/2024] [Correção] Foi adicionado o indicador, contagem e limitador de caracteres na criação e edição de motivo de perda, além de erros específicos caso o usuário consiga realizar uma requisição com mais de 50 caracteres. Além disso, foi corrigido um erro de manipulação de objeto que atualizava incorretamente o texto do motivo de perda editado mesmo quando a chamada retornava erro.
[03/06/2024] [Correção] Tamanho fixo do input de email escondia conteúdo excedente. Agora o input se comporta como no modal de compartilhamento de documento: sempre ocupa uma linha inteira, garantindo espaço suficiente para o texto.

[03/06/2024] [Correção] Ao fechar um modal de tarefa com o popover de "Finalizar com observações" aberto, o modal fechava e o popover "piscava" para outra posição da tela e depois fechava. Agora, o popover fecha corretamente.
[03/06/2024] [Correção] A listagem de ícones não fechava ao clicar para ordenar os elementos. Agora, ao ordenar, a listagem fecha normalmente.
[03/06/2024] [Correção] Na página de tarefas na visão de calendário, ao finalizar uma tarefa com repetição, a repetição só aparecia após atualizar a página. Agora, a repetição aparece após finalizar a tarefa, sem ser necessário atualizar a página.

[03/06/2024] [Correção] Quando o nome do cliente era muito grande, o ícone e o botão de expandir a seção ficavam desalinhados. Agora, para que isso não ocorra, foi adicionado um tooltip quando o nome é muito grande e ele ocupa um espaço limitado.

[03/06/2024] [Correção] Na visualização de funil, ao aplicar um filtro o valor total da coluna não era atualizado se a coluna não tivesse nenhum card. Agora, o valor é zerado corretamente quando aplicado um filtro.

[03/06/2024] [Correção] A opção de enviar comentários estava habilitada durante a chamada de exclusão, o que gerava conflito na atualização do estado com os comentários. Assim como já funcionava quando um comentários era enviado, agora o botão 'Enviar' também fica desabilitado enquanto o comentário é excluído. Além disso, mudanças em comentários pelo modal de tarefas agora refletem corretamente na visão de timeline das tarefas do dia.

[03/06/2024] [Correção] Adicionar um campo de vínculo sem campos associados fazia com que na criação da proposta a seção fosse exibida com bug do nome da variável. Agora campos nesse cenário serão omitidos na criação de proposta.

[03/06/2024] [Correção] Na importação de clientes, ao mapear uma empresa, era possível selecionar o campo de CPF nativo, que posteriormente ocupava o campo de CNPJ da empresa. Agora, o campo de CPF não pode ser selecionado para empresa. E ao mapear uma pessoa, a mesma lógica é aplicada para o campo de CNPJ nativo.

[03/06/2024] [Correção] Na criação de negócio, ao incluir uma proposta, campos com valor padrão relacionados ao cliente eram resetados. Agora, esses campos são resetados apenas se o cliente for alterado.

[03/06/2024] [Melhoria] Foi adicionada uma melhoria que consiste em transformar os checklists e seções das páginas de Cliente e Negócio em elementos colapsáveis. Os elementos agora podem ser abertos ou fechados para melhor visualização e, por padrão, o botão fica aberto, permitindo a visualização completa dos itens. Essa melhoria deve ser expandida e aplicada em diferentes partes do Ploomes futuramente.

[03/06/2024] [Correção] Melhoramos a performance de carregamento do Ploomes remanejando uma das verificações iniciais.

[04/06/2024] [Correção] Ao duplicar um negócio, os campos preenchidos de opções pré-cadastrados, não estavam duplicando os valores.

[06/06/2024] [Correção] Ao incluir um opcional, uma fórmula que soma os valores de todos os opcionais estava sendo chamada. No entanto, ao remover o opcional, o valor correspondente não era subtraído, resultando em um aumento incorreto do valor total. Foi implementada uma validação para verificar se o item obrigatório já existe no momento de adicionar ou remover um opcional. Se o item obrigatório já estiver presente, impedimos a duplicação. Com isso, os valores são calculados corretamente, evitando duplicações e erros no total final.

[06/06/2024] [Correção] Ao criar um produto no módulo de clientes, ao tentar executar uma fórmula que dependia do campo de cliente o valor vinha nulo. Foi feita uma correção para garantir que, sempre que o usuário interagir com o campo de cliente nesse módulo, o modelo será preenchido corretamente. Isso assegura que as fórmulas sejam disparadas de forma adequada e com os valores atualizados com os dados do cliente.

[06/06/2024] [Correção] Antes, os usuários podiam inadvertidamente tentar limpar alguns campos, como a data da tarefa ou o status do cliente, durante a edição dos valores, mas essa ação não causava qualquer alteração real, já que o backend ignora valores nulos na requisição de edição de alguns campos e mantém o valor já salvo. Agora, esses campos são tratados como obrigatórios durante a edição. Se um usuário tentar apagá-los, um aviso será exibido, impedindo o salvamento e informando sobre a impossibilidade de apagar o valor por meio de um toast.

[06/06/2024] [Correção] Na página de negócio, ao mudar de estágio as mensagens da timeline (histórico completo) às vezes sumiam e só apareciam ao atualizar a página. Agora, mesmo mudando de estágio as mensagens vão aparecer corretamente.
[06/06/2024] [Correção] Quando tínhamos um negócio com uma quantidade X de checklists cadastrados na etapa, com campos de anexo iguais (por exemplo, o Checklist 1 contém o campo X, e o Checklist 2 contém o mesmo campo X), ao duplicar o negócio, enviávamos uma requisição para duplicar os anexos de cada campo. No entanto, o algoritmo antigo do front-end pegava por índice e chave do campo, e não pelo ID do anexo duplicado. Isso fazia com que, ao duplicar os valores dos checklists, os anexos fossem salvos com o ID antigo, e não com o novo ID gerado pelo back-end, gerando assim o erro ao duplicar os Cards. Para resolver esse problema, houve um trabalho conjunto entre as equipes de front-end e back-end. O back-end agora nos envia uma propriedade indicando a origem do arquivo que foi duplicado, permitindo que o front-end faça o cruzamento de dados para duplicar com os IDs corretamente. Isso garante que, ao excluir o negócio duplicado, os anexos do negócio original não sejam afetados e não dê mais o erro ao duplicar os Cards.
[07/06/2024] [Correção] No aplicativo existia um erro que quebrava o banco de dados local e a requisição, o que ocasionava o carregamento ficar em um looping infinito ao abrir o App. Os desenvolvedores corrigiram isso, mas se o usuário atualizar a versão ainda com o carregamento "quebrado" pode não resolver, sendo necessário resetar o aplicativo e fazer o login novamente. Correção aplicada na versão 4.1.1 do App.

[07/06/2024] [Correção] Na configuração de checklists em negócios, ao selecionar um campo presente no formulário, o nome no formulário do negócio era modificado visualmente. Agora, o nome no formulário não é modificado.

[10/06/2024] [Correção] Nos módulos do sistema, quando aplicamos o modo de visualização por tabela, podemos criar e duplicar abas de visualização (no lado esquerdo). Anteriormente, as abas duplicadas não possuíam nenhuma sinalização para identificá-las como duplicadas. Agora, o nome destas abas duplicadas é criado no seguinte modelo: '[Cópia] - Nome da aba'

[10/06/2024] [Correção] No formulário de novo produto do cliente, ao não preencher um campo obrigatório e clicar no botão 'Salvar', aparecia um alerta descentralizado. Esse alerta teve seu estilo corrigido e, portanto, alinhado ao centro com relação ao botão de salvar.

[10/05/2024] [Correção] Em relatórios beta, foi modificado um trecho de código que estava aplicando filtros em campos que não deveriam ter filtros, pois não são entidades que exigem permissões, como no caso da entidade 'Equipe'.
[10/06/2024] [Correção] Ao acessar o modal de edição de estágios de venda, quando um dos estágios possuía um título longo o suficiente, ele não era exibido totalmente. Foi adicionado um Tooltip que exibe o título por completo quando o usuário passa o cursor do mouse em cima do estágio de venda.

[10/06/2024] [Correção] Ao adicionar campo de ID da proposta no modelo, ele aparecia como campo editável na criação ou edição da proposta. Como a criação do ID é de responsabilidade do backend e ele não pode ser alterado, o campo foi escondido na criação e na edição de proposta.
[10/06/2024] O frontend permitia mapear um campo com um valor padrão usando o caminho `cliente/contato/empresa > telefone`. No entanto, ao preencher esse campo, o valor retornava vazio, pois não havia como obter o valor correto dessa propriedade. Para resolver isso, bloqueamos a possibilidade de mapear esse caminho no `fieldPath`.

[10/06/2024] [Correção] Na configuração de funis, dentro da criação de checklists, ao tentar salvar uma checklist com o nome com mais de 100 caracteres ou descrição com mais de 200 caracteres, um erro acontecia, mas nenhuma mensagem aparecia na tela. Agora, o campo de nome foi limitado para 100 caracteres e o de descrição para 200.
[10/06/2024] [Correção] Por padrão quando há um texto com uma palavra muito grande, ele excede o tamanho da tag HTML em que está inserido. Foi aplicado uma propriedade que quebra esta palavra em linhas caso exceda o tamanho do elemento pai.
[10/06/2024] [Correção] Quando o nome de um painel em Relatórios Novo era muito grande, a formatação do topo da página ficava estranho, ou o título ultrapassava a área determinada. Foi adicionado o comportamento de ellipse para nomes muito grandes e um tooltip que mostra o nome completo nesses casos.
[10/06/2024] [Correção] Ao tentar mover um negócio em um funil com checklist incompleta, o modal com o aviso de itens obrigatórios faltantes não mostrava avisos para itens que dependiam do cliente associado ao negócio. Agora, os avisos que são mostrados na página de negócio também aparecem no modal.
[10/06/2024] [Correção] Na tela de preenchimento de proposta, se houvesse um tooltip e um modal fosse aberto, o tooltip continuava visível. Agora, enquanto o modal estiver aberto, o tooltip não ficará visível.
[10/06/2024] [Correção] O ícone do botão de edição (lápis) possuía um leve desalinhamento para baixo. A propriedade de estilização dele foi ajustada para garantir que sempre fique centralizado.
[10/06/2024] [Correção] Ao duplicar e imediatamente excluir o documento duplicado, usuário é corretamente retornada ao documento original. Entretanto, quando excluía na sequência o documento original, ele não era redirecionado à tela de documentos, e ficava preso a visualização do documento deletado. A condição foi corrigida para retornar o usuário à tela de documentos

[10/06/2024] [Correção] Quando o gráfico era muito pequeno e era aplicado um zoom, os botões do topo eram cortados. Foi adicionado um valor minimo de largura pro gráfico pra que isso não ocorra.

[10/06/2024] [Correção] Selecionar a opção vazia em 'aninhar em' na configuração de pasta voltava um erro para o usuário, e, tentar trocar o aninhamento e deletar a opção dava erro também.

[10/06/2024] [Correção] Em relatórios beta, ao clicar no botão que abria o dropdown no painel e tentar arrastar o item para ordenar o menu, o dropdown atrapalhava a movimentação por permanecer aberto. Agora o dropdown fecha ao arrastar um item.

[10/06/2024] [Correção] Quando existia mais uma lista com ordenação "draggable", onde podemos arrastar os componentes para a posição desejada, era possível arrastar um elemento de um menu para o outro, gerando erro na listagem e nas operações.
[10/06/2024] [Correção] Ao editar ou criar um documento no CKEditor, há uma configuração que permite dimensionar o tamanho das colunas de uma tabela. Para isso, o editor exibe um elemento ao passar o mouse sobre a coluna. No entanto, esse elemento estava sobrepondo o conteúdo da coluna, impedindo o usuário de editar os valores contidos nela. Agora é possível redimensionar a coluna e editar o conteúdo clicando exatamente encima do texto.

[10/06/2024] [Correção] Na integração com o RD Station, anteriormente, apenas trazíamos a origem do lead quando o webhook era proveniente de uma conversão. Agora, mesmo que o webhook não seja de uma conversão, validamos se existe uma última conversão. Caso exista, essa informação é preenchida.
[11/06/2024] [Correção] Ao duplicar um documento, os anexos dos campos de documento, bloco, produto e vínculo não eram duplicados também, e caso o usuário deletasse o documento duplicado, os anexos do original eram deletados.

Foi feita uma melhoria para duplicar os anexos de todas essas entidades em Propostas, Vendas e Documentos tanto no caso do modal como tela cheia.

[11/06/2024] [Correção] Em alguns módulos, ao interagir com um botão de paginação desabilitado ele mudava de cor, mesmo que o clique não funcionasse. Agora, ao clicar em um botão de passar página desabilitado, nada acontece.

[11/06/2024] [Correção] Este ícone era, na verdade, uma junção de dois elementos: um círculo cinza e um ícone branco em cima. Desse modo, o navegador não consegue manter os dois 100% centralizados. Por isso, essa abordagem foi substituída por um único ícone, que já é circulado por padrão.

[11/06/2024] [Correção] Antes, os usuários podiam inadvertidamente tentar limpar alguns campos, como a data da tarefa ou o status do cliente, durante a edição dos valores, mas essa ação não causava qualquer alteração real, já que o backend ignora valores nulos na requisição de edição de alguns campos e mantém o valor já salvo. Agora, esses campos são tratados como obrigatórios durante a edição. Se um usuário tentar apagá-los, um aviso será exibido, impedindo o salvamento e informando sobre a impossibilidade de apagar o valor por meio de um toast.

[11/06/2024] [Correção] Na integração com o DocuSign, os clientes que estiveram inativos por mais de 1 mês antes de 13/03/2024 terão o status de sua integração alterado para "Pendente". Além disso, o criador da integração será notificado sobre essa mudança.
[11/06/2024] [Correção] Ao inserir um produto, slide era fechado, mas botão permanecia com foco, o que acionava o método de adição de produto ao teclar Enter. Agora o foco é removido do botão depois que o produto é inserido e o slide fechado
[11/06/2024] [Correção] Nos campos de criação de um novo negócio, há uma regra condicional para exibição da pontuação no 'quick filter', e o campo de cliente não atendia essa regra. Portanto, era exibido sem a pontuação correta. Essa regra foi modificada afim de exibir os dois pontos para o campo de cliente.

[11/06/2024] [Correção] Em relatórios beta, quando um usuário com restrições de permissão de visualização de vendas adicionava um filtro rápido em um gráfico de venda, era retornado gráfico vazio.

[11/06/2024] [Correção] Quando o usuário clicava no limite do ícone de expandir campos, duas ações eram disparadas ao mesmo tempo (o clique do botão e abertura do collapsible) causando um bug no componente. Agora o erro não ocorre mais e só uma ação é disparada por clique.
[13/06/2024] [Melhoria] Em modal mini, na edição de proposta, a largura da coluna de inserção de produto estava seguindo o tamanho do cabeçalho com base no tamanho do texto. Agora esse tamanho esta setado com largura mínima de 150px em campos nativos, para que não haja quebra de linhas estranhas.

[13/06/2024] [Correção] Não registrávamos as criações, alterações e deleções em checklists dentro dos registros do Ploomes, alteramos esse comportamento e agora registramos essas informações.

[13/06/2024] [Correção] No app, ao editar um documento era exibido todos os modelos disponíveis da conta, sem filtrar por documentos de cliente ou de negócio. Agora, na edição de documento de cliente só são exibidos os modelos de documento de cliente e na edição de documento de negócio os modelos de documento de negócio.

[13/06/2024] [Correção] No app, ao minimizar as sessões da aba de dados de um cliente, o restante das sessões existentes sumiam. Agora foi adicionado tratamentos para renderizar o restante das sessões quando as primeiras são renderizadas.

[13/06/2024] [Correção] No app, a ordenação dos cards de negócio da tela de clientes estava incorreta. Fizemos uma correção para seguir o padrão da Web.

[13/06/2024] [Correção] No app, a notificação não estava sendo enviada ao marcar um usuário na descrição de um registro de interação. Subimos uma correção para que a notificação seja enviada.

[13/06/2024] [Correção] No app, foi corrigido o erro nas abas da tela de Clientes que não alterava no modo offline.
[13/06/2024] [Correção] No app, o tratamento de valor em campos de valor estava errado para valores menores que 1. Este comportamento foi corrigido.

[13/06/2024] [Correção] Correção de scroll no campo multinha para dispositivos IOS que fazia o campo ser sobreposto pelo teclado.
[13/06/2024] [Correção] Adicionada persistência de última aba selecionada na tela de clientes.
[13/06/2024] [Correção] Adicionado um loader enquanto faz a navegação para a tela, para evitar delay na tela de cliente.

[13/06/2024] [Correção] No app, foi corrigido um bug que ao acessar a criação de uma venda ou documento, aparecia o formulário de uma outra entidade que foi recém editada.
[13/06/2024] [Correção] A atualizar o e-mail de um singatário não era diferenciado a palavra com e sem acentos. Agora elas são diferenciadas corretamente.

[13/06/2024] [Correção] No app, foi adicionado tratamento para evitar que o marcador de usuário fique piscando em mapas no Android.

[13/06/2024] [Correção] Em automações, ao mapear os campos de uma automação que deve criar um negócio, se o usuário alterasse o funil selecionado, o campo de seleção de alguns campos não funcionava mais, Agora, os campos de seleção funcionam normalmente.
[14/06/2024] [Correção] Quando havia clliques rapidos no elemento ele era redirecionado para duas telas iguais, o que gerava comportamentos estranhos.
[14/06/2024] [Correção] Adição de sanitização de campo de porcentagem para valores especiais.

[14/06/2024] [Correção] Opções do campo nativo de status do cliente não possuía tradução em nenhuma linguagem do Ploomes.

[14/06/2024] [Correção] Adicionado tratamento para htmls renderizados nos cards de registro de interação do app mobile, com comportamento de expandir ou retrair dependendo do tamanho da descrição.

[14/06/2024] [Correção] No app, fizemos uma correção do espaçamento da seta que indica a mudança de estágio.
[14/06/2024] [Correção] Foi feita a adição de sincronização entre cabeçalho e formulário de tela de compartilhamento de whatsapp.

[14/06/2024] [Correção] No app, remoção de lógica que alterava o valor do calendário de tarefas através do campo de data em uma visualização de tarefa.

[14/06/2024] [Correção] No app, ao abrir o teclado numérico em Propostas ou Vendas, quando se fechava a venda ou proposta, o teclado numérico reaparecia brevemente.

[14/06/2024] [Correção] Adicionado menu de configuração na navegação de tarefas, dessa forma o app consegue navegar entre as telas sem causar problemas visuais.

[14/06/2024] [Correção] Correção de erro visual onde no app aparecia uma linha escura ao transitar entre comentários e dados em telas de registro de interação.

[14/06/2024] [Correção] Era possível sincronizar um novo modelo enquanto o App estava aberto, resultando em um formulario vazio. Agora o App verifica se existe o formulario do modelo sincronizado antes de exibi-lo.
[14/06/2024] [Correção] Correção de carregamento online da tarefa após edição para evitar duplo carregamento da tela de visualização.
[14/06/2024] [Correção] Foi necessário subir uma atualização pela loja dos dispositivos IOS devido a uma das ferramentas que estava com incompatibilidade com versões 17.0+ do IOS, dessa forma atualizamos a ferramenta para corrigir os problemas de crash e já é possível atualizar o App pela loja.

[14/06/2024] [Correção] Quando o app estava no modo offline, e a tela de atividades estava sem dados, o botão de adicionar registro de interação ficava desativado. Removemos a condição que impedia o aparecimento do botão flutuante, e agora é possível criar registros de interação no modo offline.
[18/06/2024] [Correção] Usuário que não conseguiam ver resultados do relatório ao aplicar filtro geral porque o trecho de código que verifica o filtro estava usando as permissões relacionadas à entidade base e não à do filtro, foi alterado para buscar sempre a entidade do filtro quando houver o filtro e está funcional agora.

[18/06/2024] [Correção] Surgiu um problema com a duplicação de alguns funis, o código foi corrigido.

[18/06/2024] [Correção] No WhatsApp, era possível cadastrar clientes com o mesmo número de telefone, mesmo quando o campo de telefone estava configurado como único no formulário do Ploomes. Implementamos uma lógica para verificar se o campo de telefone é único. Se for, realizamos uma validação para evitar a duplicação durante a criação de um cliente, para que assim não seja possível cadastrar um telefone já cadastrado no Ploomes.
[19/06/2024] [Correção] Campos com uma sequência de caracteres longa inserido em uma tabela podiam causar quebra de margem do pdf gerado, esse comportamento foi corrigido para fazer a quebra de linha e ajustar ao documento corretamente.

[19/06/2024] [Correção] Quando a API do Omie retornava um erro 500 na hora de consultar os produtos de alguma página, esse erro deveria ter cair no retry que tem no CB2.Callback, mas ele não funcionava conforme o esperado. Corrigimos esse problema no retry.

[20/06/2024] [Correção] Quando uma tarefa era aberta ou finalizada no modo de visualização em lista e com algum filtro selecionado (apenas finalizadas ou apenas abertas), a lista não atualizava. Agora a lista atualiza sempre que um status é alterado.

[20/06/2024] [Correção] Os itens adicionados em criação de grupo e família na tabela de produtos não apareciam na tela no momento em que eram criados, apenas fechando e abrindo a parte de criar novos produtos (no modal de criação de grupo) ou a parte de criar novos grupos (no modal de criação de família). Agora aparecem no momento da criação.

[20/06/2024] [Correção] Foi adicionada a ordenação por ID em requisições ao back-end para melhorar a performance. Ao inserir o ID como critério secundário na ordenação já existente, garantimos uma ordem consistente, especialmente em casos de duplicações. O ID será incluído junto com os critérios de ordenação que já são enviados no query param 'orderBy.'

[20/06/2024] [Correção] Quando um cliente tinha mais de um telefone, os telefones apareciam no tooltip em linhas diferentes e ficava um espaço em branco grande ao lado. O espaço foi removido para melhor visualização
[20/06/2024] [Correção] No formulário para adicionar um novo cliente (empresa ou pessoa), o campo de telefone possui um botão para selecionar a máscara desejada, que contém o ícone da bandeira do país selecionado. Esse ícone estava desalinhado. Foi aplicado um estilo para centralizá-lo no botão.

[20/06/2024] [Correção] Na configuração de funil, etapas com nomes muitos longos às vezes ultrapassavam o limite da caixa e faziam com que o símbolo de deletar e mover etapa ficassem fora da caixa. O problema foi corrigido.
[20/06/2024] [Correção] O ícone de check estava descentralizado na seção de opções pré-cadastradas, na finalização de tarefas e seleção de vínculos no modal de editar produto em venda/proposta. O problema foi corrigido.
[20/06/2024] [Correção] Em algumas páginas, campos de formulário do tipo porcentagem não eram apresentados com o separador de decimal correto para o idioma da conta do usuário. O problema foi resolvido.
[20/06/2024] [Correção] Campos de integração com plataformas externas (Omie, ClickSign, etc) não podem ser excluídos (a requisição de exclusão retorna erro), porém, a interface exibia o botão de exclusão (lixeira) normalmente para esses campos. Agora, quando um campo é de integração, esse botão não aparece.

[20/06/2024] [Correção] O campo "Cargo" nativo do Ploomes não estava enviando o valor corretamente via integração com o Sankhya. Foi corrigida a forma como o campo é enviado para que o valor integre corretamente.

[20/06/2024] [Correção] Algumas instabilidades no servidor de fórmula faziam com que o resultado calculado na API retornassem resultado incorreto. Foi alterado para caso ocorra uma instabilidade, a API calcular de outra maneira, retornando assim o valor correto.
[21/06/2024] [Correção] Quando um cliente era adicionado a uma tarefa, caso houvessem informações com palavras muito grandes, as mesmas ultrapassavam o limite do layout. Agora palavras muito grandes quebram para a próxima linha.
[21/06/2024] [Correção] O componente de edição de campo não possuía nenhuma verificação em casos de erro por falta de permissão do usuário, exibindo somente um erro genérico. Agora, quando o erro na edição do campo ocorre por falta de permissão do usuário, é exibida uma mensagem específica alertando a causa.
[21/06/2024] [Correção] No módulo de biblioteca, na edição de arquivo ou coleção, ao clicar em vincular entidade e clicar para editar algum dos campos da entidade na tabela, apareciam dois modais de edição. Agora, aparece apenas um modal de edição.

[21/06/2024] [Correção] Na integração Sankhya, estoques eram tratados como número inteiro, mas por conta de uma alteração no Sankhya que mudou o tipo o Ploomes não conseguia mais obter o estoque. Foi alterado para exibir o estoque como texto, assim se adequando a qualquer tipo que o Sankhya mandar.
[25/06/2024] [Correção] Checklists de um card poderiam manter o ícone de "seção com campos obrigatórios não preenchidos" mesmo com todos os campos obrigatórios preenchidos, esse comportamento foi corrigido
[25/06/2024] [Correção] O campo 'Adicionar contatos relacionados à tarefa de integração', presente na modal de agendamento de tarefa, não possuia um nome e aparecia como um campo sem nome para o usuário selecionar. Agora, esse campo está sendo ocultado do componente de seleção de campos, não aparecendo mais como uma opção para o usuário selecionar.

[25/06/2024] [Correção] Ao deletar categoria de vínculos de produtos, os vínculos desta categoria continuavam existindo. Agora com a correção, os vínculos também são deletados.

[25/06/2024] [Correção] Ao duplicar metas, existe um comportamento que adicionava texto no final dela para identificar a duplicação, porém, isso estava burlando o limite de 150 caracteres. Agora, caso o nome da meta + o que for adicionado ultrapassar 150 caracteres, não adicionaremos esse valor. Esse valor quando ultrapassado gerava um erro impedindo o usuário de realizar ações na meta, gerando assim um incômodo.
[26/06/2024] [Correção] Anteriormente, ao adicionar um novo telefone, a validação de campo vazio para campos obrigatórios não ocorria mais. Agora caso o usuário tente adicionar um valor vazio, o erro é mostrado na tela.

[26/06/2024] [Correção] Foi adicionado o campo "Impostos Embutidos" no mapeamento de vendas, na aba "informações adicionais". Ele só pode ser mapeado com campos de checkbox do Ploomes. O envio de valores desse campo é unilateral, apenas do Ploomes para o Omie.

[26/06/2024] [Correção] Na integração com o Sankhya, ao fazer a consulta de impostos, o Ploomes sempre mandava o nunota como 1, pois é o modelo padrão que vem em toda conta Sankhya, mas em casos onde essa nunota tivesse sido apagada, a consulta de impostos dava erro. Agora a integração vai prosseguir com a consulta buscando pelo menor nunota que encontrar na conta.

[27/06/2024] [Correção] Na integração com o Sankhya, quando o Sankhya não possuia o modelos de nota padrão 1 na conta, as consultas estavam retornando erro. Corrigimos para que agora, caso não possua a nota 1, serão feitas outras tentativas usando o menor modelo de nota que encontrarmos na conta.
[27/06/2024] [Correção] Na integração com o Omie, quando o usuário pressionava um botão de sincronização, a exportação ou importação de uma entidade era iniciada. Em alguns casos, itens criados durante o processo só eram integrados após a conclusão da sincronização.

[27/06/2024] [Correção] Quando uma janela de autenticação era aberta para ativar uma integração, uma extensão de captura de tela poderia abrir uma máscara por cima da página, impedindo a operação de ser realizada.
