---
id: "42427587345175"
titulo: "Atualizações de Janeiro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427587345175-Atualiza%C3%A7%C3%B5es-de-Janeiro-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:01Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_01d26813224c", "ploomes_8779091"]
---

# Atualizações de Janeiro de 2024

[04/01/2024] [Correção] Fluxo de aprovação utilizando o campo de nome do estágio do card da proposta, documento ou venda não funcionava.

[04/01/2024][Correção] Webhooks não estavam sendo criados no RD Station, impedindo a integração de levar leads do RD para o Ploomes.

[05/01/2024] [Correção] Quando um campo de texto ultrapassava o limite máximo de caracteres (via fórmula, por exemplo), o formulário não ficava válido novamente, apenas quando fechado e reaberto.

[05/01/2024] [Correção] Era possível em campos do tipo inteiro adicionar o valor 999999999 e logo depois acrescentar um, adicionando 1000000000, o que não deveria ser permitido. O comportamento foi corrigido.

[05/01/2024] [Correção] Nos campos de número inteiro, era possível ainda assim uma vírgula, que seria ignorada posteriormente. Foi feita uma correção para não permitir mais vírgulas nos campos do tipo inteiro.

[05/01/2024] [Correção] Na configuração de permissões de acesso, o termo "Sob responsabilidade de membros de sua equipe" era diferente em alguns módulos, dando a entender que o comportamento era diferente, quando na verdade não era. O termo foi padronizado em todos os módulos.

[05/01/2024] [Correção] Aspas simples em filtragem de abas dava erro e não voltava nada.

[05/01/2024] [Correção] Janela de compartilhamento de proposta em branco.

[05/01/2024] [Correção] Formato de data na linguagem em inglês do sistema agora corresponde com o formato utilizado nos Estados Unidos de Mês/Dia/Ano.

[05/01/2024] [Correção] Ao importar produtos, o campo "Nome do Grupo de Produto" era marcado para detectar duplicidade de forma obrigatória. Foi feita uma modificação para que seja padrão e recimendado, mas não obrigatório.

[05/01/2024] [Correção] Ao mudar por automação uma proposta aceita externamente, o front continuava exibindo o 'Aceita externamente' na página da proposta (ao lado dos botões de ganhar e perder), mesmo essa proposta não estando mais com status de aceita externamente.

[05/01/2024] [Correção] Possibilidade de adicionar UM caractere 'e' dentro de checklist de campo inteiro.

[05/01/2024] [Correção] Na tela de configuração de funil, ao desmarcar a opção 'Pode gerar {nome da entidade} neste funil', o campo para decidir se naquela entidade seria usada a configuração global para modelos ficava aberto, levando a erros. O comportamento foi corrigido para bloquear e exibir um aviso para o usuário com um tooltip.

[05/01/2024] [Correção] Na configuração de fórmulas, ao adicionar uma variável que já existia em outra fórmula do mesmo campo, o Ploomes colocava com o nome do campo sempre, e não o nome da variável que já existia, causando erros. O comportamento foi corrigido para o esperado, que é colocar o nome da variável caso ela já exista, ou o nome do campo caso a variável seja nova.

[05/01/2024] [Correção] Foi aumentado o tempo de processamento de uma request para o mesmo item de 1 para 3 minutos na integração do Omie para que, em casos de intermitência, consigamos finalizar as operações.

[05/01/2024] [Correção] Renomear coleções na biblioteca clicando com o botão direito e selecionando a opção de renomear não funcionava.

[05/01/2024] [Correção] Em checklists e dados básicos, ao clicar com o botão direito do mouse e em abrir em uma nova guia, o Ploomes não abria de fato o item, mas sim uma nova guia na página inicial. Foi feita uma melhoria para possibilitar esse caminho ou o botão do meio do mouse para abrir em uma nova aba. O mesmo foi feito para a tabela dinâmica.

[05/01/2024] [Correção] Ao configurar um fluxo de aprovação e escolher um campo de anexo, era possível escolher um anexo e colocar como condição. Mas isso não fazia sentido pois além de não ser aceito pelo backend, os anexos seriam comparados pelo Id, logo sempre iriam cair no fluxo. O problema foi corrigido bloqueando de inserir anexos, fazendo com que só seja possível colocar a condição como igual a vazio ou diferente de vazio.

[05/01/2024] [Correção] Um erro ao remover pelo Ploomes signatários que foram removidos primeiro pelo LetsSign impossibilitava os documentos do Ploomes de serem finalizados quando todos assinavam. Passamos a tratar o erro da requisição para garantir que os signatários possam ser removidos do Ploomes também, destravando documentos de serem concluídos nesses casos.
[05/01/2024] [Correção] Ao buscar opções de um campo em alguns casos, por um erro no código, a busca estava sendo feita usando apenas números, não incluindo pontos ou barras. O comportamento foi corrigido para buscar exatamente o que o usuário digitou sempre.

[08/01/2023] [Correção] Nossa API estava considerando o e-mail enviado de dentro do Ploomes como sendo diferente daqueles que estava na pasta de enviados do Google

[09/01/2023] [Correção] E-mails enviados pelo card do cliente estão gerando duplicidade.

[15/01/2024] [Correção] Ao tentar salvar documento no modal, com título contendo mais de 200 caracteres, não era exibido nenhum alerta e o documento não era gerado.

[15/01/2024] [Correção] Opções em filtros dos relatórios beta estavam ficando uma em cima da outra.

[15/01/2024] [Correção] Ao adicionar um número muito grande em um campo de moeda ele ficava com um simbolo de infinito. O problema foi corrigido.

[15/01/2024] [Correção] Ao ganhar um negócio, caso o usuário estivesse com uma aba de negócio aberta e editasse algo em outra aba que impedisse de ganhar aquele negócio, caso o usuário clicasse em ganhar na primeira aba, não era possível ganhar e nenhum erro era apresentado na tela. O problema foi corrigido adicionando um aviso.

[15/01/2024] [Correção] Não estava sendo possível acessar carregar alguns documentos por conta de um timeout em uma requisição, foi adicionado uma propriedade na requisição de documentos chamada preload para trazer os dados de forma mais rápida, evitando o erro.

[15/01/2024] [Correção] Na tela de criação de campos, caso fosse selecionada a opção de exibir para um ou mais usuários e nenhum usuário fosse adicionado, ao salvar o botão ficava em loading infinito. O comportamento foi corrigido.

[15/01/2024] [Correção] Quando o card de uma tarefa não tinha título, o front exibia erroneamente o texto para adicionar um card. O problema foi corrigido exibindo o texto 'Sem título' conforme a língua do usuário nestes casos.

[15/01/2024] [Correção] Ao dar zoom na tela de documentos ou clientes, caso a seção lateral de Menu estivesse aberta, o cabeçalho que contém os botões de pesquisa ficava sobreposto sobre ela.

[15/01/2024] [Correção] No Docusign existia um conflito entre tipos de compartilhamentos de documento que impedia a retirada de signatários já inseridos no compartilhamento Y por já ter existido no compartilhamento X.

[15/01/2024] [Correção] Ao criar uma nova proposta, um campo de opções iniciava aberto mesmo já estando preenchido com um valor padrão.

[15/01/2024] [Correção] Tela de filtro simples era montada com base no formulário do funil padrão da conta, o que fazia com que, se o funil fosse deletado, a tela de filtro simples ficava em branco. Foi corrigido para o filtro sempre buscar o formulário do funil atual.

[15/01/2024] [Correção] Em filtros, a condição usando anexo não suporta comparações entre eles, então essa possibilidade foi bloqueada, permitindo selecionar o campo mas apenas com as operações "Igual a vazio" ou "Diferente de vazio".

[15/01/2024] [Correção] O campo 'contatos relacionados' de registro de interação mostrava sempre apenas contatos do cliente na edição, e não mostrava outros da conta ao pesquisar como é na criação. O comportamento foi corrigido.

[15/01/2024] [Correção] Ao clicar em atualizar dados e modelo, o payload da requisição enviado para o backend estava sem uma informação, causando erros no fluxo de aprovação. O problema foi corrigido.

[16/01/2024] [Correção] Por conta de um erro de subida, não estava sendo possível autorizar a integração do DocuSign.

[16/01/2024] [Correção] Um formato diferente do esperado em alguns campos dos leads do Econodata causou erros na importação dos leads ao Ploomes. Foram adicionados tratamentos para formatos diferentes desses campos, corrigindo a importação.

[16/01/2024] [Correção] O App não estava resgatando as informações de negócio e contato da proposta durante o modo offline, impedindo de carregar a aba de informações.

[16/01/2024] [Correção] A verificação de funil selecionado pelo usuário agora é feita durante o clique do botão de negócios, antes dele navegar para alguma tela.

[18/01/2024] [Correção] No app, ao pesquisar caracteres especiais o aplicativo crashava.

[18/01/2024] [Correção] Alterações em propriedade "ChangeNoLogin" do usuário não estavam sendo mostradas nos registros de modificação.

[18/01/2024] [Correção] Ao editar um documento no aplicativo, os produtos previamente inseridos sumiam.

[18/01/2024] [Correção] O app não estava buscando o ultimo login valido durante a transição entre modo online e offline, impossibilitando usuários de acessar o app em modo offline. A forma de buscar o ultimo login foi corrigida para apontar para o registro correto de ultimo login valido.

[18/01/2024] [Correção] No app, campo de Latitude e Longitude não eram preenchidos após inserir um endereço vinculado a busca do Google.

[18/01/2024] Negócios que tivessem configuradas checklists que utilizavam filtro com campo de cliente diferente de vazio poderiam ser dados como ganhos com a checklist pendente.

[18/01/2024] [Correção] O app não estava reconhecendo que nenhuma alteração havia sido feita no checkbox e assim ao tentar salvar o valor contido nele era zerado.

[18/01/2024] [Correção] No app, qualquer movimento horizontal feito na tela de atividades disparava uma função que realizava a troca entre resumo e metas.

[18/01/2024] [Correção] Foi adicionado a janela de aviso de tentativa de ganho de negócio sem contato e com as configurações de “Nova venda ao ganhar negócio” e “Criar venda automaticamente ao ganhar negócio” ativadas, além do tratamento de todo o comportamento esperado.

[18/01/2024] [Correção] Alterações do cliente de um produto de cliente gerava uma limpeza em propostas, vendas e documentos, tirando todas as referências que existiam para aquele produto de cliente. Foi corrigido esse comportamento para não arrancar o produto do cliente da proposta após essa alteração.

[19/01/2024] [Correção] Não era possível definir a linguagem de formulário externo, mesmo se a conta estivesse configurada para outra língua.

[19/01/2024] [Correção] Ordenação de opcionais agora segue a ordenação do produto pai ao salvar e dentro da proposta/venda/documento.

[19/01/2024] [Correção] Ao tentar criar um novo negócio na tela de um negócio, por conta de um erro no código, o front estava entendendo que era a edição daquele negócio, e não um novo, levando a erros no valor padrão dos campos.

[19/01/2024] [Correção] Ao editar um documento, os produtos previamente inseridos sumiam. Foi corrigido esse problema.

[19/01/2024] [Correção] A integração com o Omie identificava como duplicidade os produtos pelo código OU pelo Id Omie. Alteramos isso, agora é priorizado o Id Omie. Caso não seja encontrado, a verificação é feita pelo código do produto.

[19/01/2024] [Correção] Quando o usuário trocava a linguagem da conta, existiam problemas relacionados a utilização de campo checkbox (Sim/Não). Foi corrigido para que leia somente true or false e não seja impactado por conta da troca de idioma

[22/01/2024] [Correção] Quando uma venda criada no Ploomes continha a mesma adição de produto mais de uma vez, cada produto adicional com observações distintas era enviado para o Omie com a observação do primeiro item repetido.

[23/01/2024] [Correção] Antes o campo de "Última mudança de estágio" era exibido em abas/filtros.

[23/01/2024] [Correção] Usuários com permissão para ver apenas clientes que são colaboradores perdiam a permissão (durante o processo de criação) para ver clientes que eram criados por eles em empresas nas quais eram colaboradores. Para corrigir foi implementada uma lógica para fazer a união dos usuários colaboradores da empresa com os do cliente sendo criado.

[24/01/2024] [Correção]Ao salvar ou editar um registro de interação, o mapa se tornava transparente, sendo possível ver o plano de fundo do celular.

[24/01/2024] [Correção] O campo de anexo em checklist não enviava corretamente os arquivos pelo android.

[24/01/2024] [Correção] Após criar uma tarefa com um intervalo de repetição definido, ao tentar editar a opção de intervalo (dia, semana, mes, ano) não era alterada visualmente no app.

[24/01/2024] [Correção] Quando a seção tinha pelo menos 1 produto, não estava sendo possível remove-la no app, ao tentar editar ou revisar proposta.

[24/01/2024] [Correção] O app, ao excluir uma proposta de um negócio que possuia mais de uma proposta, estava definindo a lista de propostas como vazia por alguns momentos.

[24/01/2024] [Correção] No App, em funil que possui a configuração habilitada "Passagem por todos os estágios obrigatória", não era possível voltar várias etapas, ele não exibia o modal indicando que o estágio do Negócio foi alterado. Corrigido na versão 4.0.13.

[25/01/2024] [Correção] Nos filtros de registro de interação estava quebrando ao selecionar um ou mais itens.

[25/01/2024] [Correção] Ao usar o botão de transcrição de fala, ele usava a linguagem da conta para identificar as palavras ditas pelo usuário. A lógica foi modificada para utilizar a linguagem configurada no perfil do usuário.

[25/01/2024] [Correção] O campo do tipo checkbox configurado para ser obrigatório não estava mostrando o ícone informando que o campo não estava preenchido.

[25/01/2024] [Correção] Ao importar uma planilha inválida, era exibida a mensagem "Formato de planilha inválido.", que dava a entender que a extensão da planilha estava incorreta. O termo foi trocado para "A planilha enviada apresentou erros."

[25/01/2024] [Correção] Ao compartilhar propostas via link web, apenas o e-mail dos destinatários era salvo, resultando no nome ficando registrado como Null. Isso causava a impossibilidade de compartilhar via Docusign e outros serviços. A correção consistiu em tornar possível salvar junto do e-mail o nome do destinatário que é enviado.

[25/01/2024] [Correção] Ao remover um opcional, em alguns casos, fórmulas que usavam seus dados não eram recalculadas.

[25/01/2024] [Correção] Título de painéis exibia um erro quando tentava inserir valores maiores do que seu limite, mesmo que visualmente ainda estivesse com 200 caracteres.

[25/01/2024] [Correção] Ao mover uma meta de lugar com o titulo muito grande, estava quebrando totalmente o layout e sem limite de onde seria possível movimentar o mesmo.

[25/01/2024] [Correção] Ao criar um novo campo, não estava sendo possível salvar no cache local e por esse motivo não estava sendo possível inserir o campo nos formulários.

[25/01/2024] [Correção] Ao copiar mensagens do whatsapp para o Ploomes usando a extensão, por conta de uma mudança feita no próprio whatsapp, estava sendo adicionado o horário no fim da mensagem copiada. O problema foi corrigido para trazer apenas o texto como era antes.

[25/01/2024] [Correção] No caso de alguns gráficos de relatórios beta, o sistema não estava tratando da forma correta dados que poderiam vir como número ou texto, o que fazia a visualização do restante do relatório ficar em branco.

[25/01/2024] [Correção] Ao duplicar um negócio, o front fazia uma requisição em checklists que não era muito otimizada. Refatoramos o código e removemos essa requisição para tornar o processo mais simples.
[25/01/2024] [Correção] Ao criar uma meta com um titulo grande, estava quebrando o layout. Foi feito um ajuste que colocará três pontinhos na frase que for muito longa para não quebrar o layout, e com isso um tooltip será apresentado ao passar o mouse no titulo.

[25/01/2024] [Correção] Não era exibido nenhuma mensagem de alerta ou alguma bordar vermelha no campo que indicaria que o título da meta estava muito grande.

[25/01/2024] [Correção] Ao configurar checklists, nas condições de avanço, caso um campo fosse múltiplo era permitido no front adicionar multiplos valores, mas isso não era aceito pelo back, gerando um erro. A configuração foi restrita para permitir apenas um valor sempre para cada condição.

[25/01/2024] [Correção] Mensagem de deleção irreversível ao deletar painéis ou gráficos no relatórios beta foi removida.

[25/01/2024] [Correção] Ao enviar o e-mail, caso o HTML dele fosse mal otimizado, a visualização de preview no registro de interação ficava em branco. O código foi melhorado para formatar de forma mais eficiente removendo alguns espaços desnecessários no início do HTML.

[25/01/2024] [Correção] Ao editar as variáveis da fórmula ou usar o botão "Calcular fórmula", em algumas situações a fórmula ficava marcada como inválida ou válida incorretamente. O comportamento foi corrigido.

[25/01/2024] [Correção] Em relatórios beta quando o nome do painel era muito grande, acabava empurrando os botões para fora da tela.

[25/01/2024] [Correção] Configuração de acesso ao módulo de negócios estava com letra maiúscula mesmo estando no final da frase.

[25/01/2024] [Correção] A paginação de biblioteca impede o acesso à paginação dos arquivos.

[25/01/2024] [Correção] Em contas com whitelabel, não estava sendo possível exibir as imagens dos tipos de gráficos ao criar/editar.

[26/01/2024] [Correção] Novo gerador de PDF não tinha as fontes do MS Windows instaladas.

[26/01/2024] [Correção] No gerador de PDF ao colocar texto justificado, em um campo que seria preenchido por um texto extenso, o texto ultrapassava o limite da tabela.

[26/01/2024] [Correção] Foram feitos ajustes no gerador de PDF para lidar melhor com recursos em horários de pico.

[26/01/2024] [Correção] Quando uma tag h no código-fonte do modelo de um documento possuia um conteúdo muito extenso, o pdf gerado apresentava um erro nas páginas com essa tag. Foi corrigido com a subida do novo gerador de html.

[30/01/2024] [Correção] Quando o usuário estava tentando selecionar a conversa dele na extensão do whatsapp, não estava sendo possível copiar o texto da mensagem.

[30/01/2024] [Correção] Valores nulos na data de expiração dos links da nova versão do PowerBI causavam erros ao buscar os dados do link.

[30/01/2024] [Correção] Não estava sendo possível criar gráficos em determinadas contas por conta de uma condição do backend. Foi feito um ajuste para o frontend se adequar a condição.
