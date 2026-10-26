---
id: "42427573974807"
titulo: "Atualizações de Maio de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427573974807-Atualiza%C3%A7%C3%B5es-de-Maio-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:49Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_811875828e3d", "ploomes_9286935"]
---

# Atualizações de Maio de 2024

[02/05/2024] [Correção] Agora os links referentes as tarefas de lembretes enviados por e-mail estão atualizados. Antes era enviado o link do Ploomes old.

[02/05/2024] [Correção] Na criação de filtros, o nome da entidade ficava errado na primeira vez que o filtro era aberto. O problema foi corrigido, o nome da entidade esperada aparece corretamente.

[02/05/2024] [Correção] Antes, quando um cliente era criado ou editado no Omie e chegava na integração, duas verificações eram feitas. Primeiro, se havia um cliente com o mesmo Id (Omie) no Ploomes. Se não, era verificado se existia um cliente com o mesmo CPF/CNPJ. Se encontrado, o cliente era editado com base nas informações recebidas, resultando na substituição do Id (Omie) caso o mesmo estivesse preenchido.

Agora, além da verificação do CPF/CNPJ, também é verificado se o cliente já tem um Id (Omie) preenchido. Se sim, outro cliente é criado, em vez de editar o existente.

[03/05/2024] [Correção] Atualizada a forma de envio para a integração ClickSign, conforme a documentação da mesma.

[06/05/2024] [Correção] O App não possuía tratamento para os registros de interação que possuíam HTML em suas descrições. Esse tratamento foi adicionado. Agora o App irá renderizar o HTML de forma correta na timeline das atividades no módulo de 'Resumo'.

Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] A tag de contato não estava sendo inserida nos cards de automação do App, ao contrário do Web. Agora ela foi adicionada na timeline. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] Foi corrigido um bug na filtragem da API do app que quebrava a lista de documentos. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] A lógica de filtragem das abas no modo offline foi corrigida para funcionar no modo offline. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] Caracteres especiais estavam sem tratamento na busca por negócios. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] Foi adicionado o tratamento que retorna o usuário para a tela do negócio após finalizar uma tarefa com observação. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] Agora o link das propostas possuem uma restrição de acesso. Foi incluído a metatag que bloqueia os navegadores de encontrar os links presentes nas páginas e os indexar.

[06/05/2024] [Correção] Estava sendo possível alterar o cliente no registro de interação vindo pela tela de negócio. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] Ao criar Tarefas a partir de um negócio, tanto o cliente quanto o próprio negócio não estavam ocultos. Correção aplicada na versão 4.0.30 do App.

[06/05/2024] [Correção] Em alguns casos específicos, o campo estado era apresentado como obrigatório quando tinha o campo cidade no formulário. Correção aplicada na versão 4.0.30 do App.
[06/05/2024] [Correção] No aplicativo a fórmula no campo de desconto não era acionada. Correção aplicada na versão 4.0.30 do App.
[06/05/2024] [Correção] Não havia uma centralização da opção quando selecionada nas abas. Essa centralização ao selecionar foi adicionada. Correção aplicada na versão 4.0.30 do App.

[07/05/2024] [Correção] Na visualização de funil, estágios com nome muito longo eram truncados, mas não havia tooltip para visualização do nome completo. Agora, ao passar o mouse em cima de um nome longo, o nome completo será mostrado.

[07/05/2024] [Correção] O campo de corpo do e-mail estava sendo resetado com o conteúdo do modelo de e-mail ao atualizar os destinatários. Foi alterado para persistir o conteúdo já editado pelo usuário.

[07/05/2024] [Correção] Ao adicionar um opcional em uma situação específica, as fórmulas que usavam seus parâmetros não calculavam.

[07/05/2024] [Correção] O campo estágio do negócio aparecia duas vezes na lista de campos da edição em massa.

[07/05/2024] [Correção] Em funis de negócio, o carregamento infinito fazia com que os Cards ficassem fora da ordem esperada, ficando diferente da ordem vista no aplicativo.

O problema foi corrigido.

[07/05/2024] [Correção] Na página inicial o widget de tarefas do dia não renderizava a descrição de uma tarefa que continha tags HTML corretamente. O problema foi resolvido.

[07/05/2024] [Correção] Fórmulas de opcional que não executavam em proposta no modo janela agora funcionam normalmente.

[07/05/2024] [Correção] O caminho Proposta Origem não estava funcionando para campos padrão em Documentos. O comportamento foi corrigido para que passe a funcionar normalmente, assim como acontece em Vendas.

[07/05/2024] [Correção] Mensagem de aviso de quando o usuário está renomeando um painel e ultrapassa 200 caracteres estava sem a descrição e o título.

[08/05/2024] [Correção] Ao atualizar apenas a logo da empresa, sem salvar o formulário em dados da empresa, o backend não está atualizando o lastupdateDate, fazendo o cache do frontend ficar desatualizado.
[08/05/2024] [Correção] Aumentamos o tempo de timeout configurado na contagem da quantidade de itens para exportação de uma aba de 20 para 60 segundos.

[08/05/2024] [Correção] No modal de escolha de produtos em documentos a requisição para trazer produtos do cliente não respeitava os filtros de grupo, família e marcador, deixando o usuário adicionar produtos que não eram permitidos. O comportamento foi corrigido.

[10/05/2024] [Correção] Ao integrar um documento em uma conta do Clicksign e interagir com o documento de qualquer forma (nova assinatura, abrir tela de assinaturas do Ploomes, etc.) após alternar a conta, a API do Clicksign rejeita acesso ao documentos da conta antiga com o token da nova, desautorizando a integração. Adicionamos tratamentos para não desautorizar a integração nesse caso específico.
[07/05/2024] [Correção] Em vendas ou documentos, quando compartilhamos o documento via email, cada destinatário adicionado duplicava a assinatura no conteúdo, isso não ocorre mais.

[09/05/2024] [Correção] Quando uma edição era feita no negócio pelo RD Station, o campo de responsável pelo negócio não era atualizado.

[13/05/2024] [Correção] Problemas de indisponibilidade do exportador não tratados acarretavam em diversos problemas na atualização de abas no PBI. Foram adicionados tratamentos para diversos erros e retries para atualizações com falha por conta de indisponibilidade, e foram realizados ajustes no exportador para reduzir diversos tipos de erros que eram comuns e impediam abas de atualizarem.

[13/05/2024] [Correção] A recente indisponibilidade no exportador causou erros inesperados na integração, deletando algumas exportações do PowerBI. Adicionamos tratamentos e consistência para esse e outros casos de erros no exportador, evitando comportamentos indesejados.
[14/05/2024] [Correção] Foi colocada uma configuração para que, caso seja adicionada uma palavra grande na descrição do formulário, ela quebre e vá para a próxima linha
[14/05/2024] [Correção] O App não tinha tratamento para impedir a navegação da tela de lista de notificações para um documento que havia sido excluído. Esse tratamento foi adicionado checando se o documento existe antes de navegar até ele.
[14/05/2024] [Correção] Agora o App não trava mais ao retirar o campo Cliente do formulário de registro de interação.

[14/05/2024] [Correção] O App fechava caso atualizasse algum checklist, mas era um caso especifico onde as abas carregavam depois que uma função de levar o usuário para a ultima aba selecionada era acionada.

[14/05/2024] [Correção] Não é possível mais colocar um arquivo inválido em formulários externos.

[14/05/2024] [Correção] Na visualização de vínculos da biblioteca não aparecia o nome dos negócios. O problema foi resolvido adicionando o atributo na tabela.
[14/05/2024] [Correção] Ao adicionar um arquivo no campo de anexo e, em seguida, selecionar um novo arquivo, o sistema não estava conseguindo atualizar corretamente o anexo com o novo arquivo escolhido. Agora esse comportamento não deve mais ocorrer e o anexo deve ser atualizado corretamente.

[16/05/2024] [Correção] Nas informações da proposta foi corrigido o posicionamento do botão de edição, o mantendo fixo caso a informação tenha um tamanho grande e haja um scroll. Além disso, limitamos o evento de clique para não triggar o comportamento do campo de seleção de marcadores para resolver o dropdown abrindo ao clicar na tag.
[16/05/2024] [Correção] Ao digitar um comentário na página de visualizar oportunidade e pressionar o botão imediatamente depois, o comentário era cortado. Agora, o comentário fica completo.
[16/05/2024] [Correção] Na criação de novas propostas, dependendo do valor e quantidade de parcelas, o valor da primeira parcela ficava negativo. O problema foi resolvido.
[16/05/2024] [Correção] Na página do perfil do usuário, usuários não administradores não conseguiam ver as suas equipes. Agora, qualquer usuário consegue ver as equipes que participa.
[16/05/2024] [Correção] A mensagem de erro mostrada quando o usuário tentava editar uma proposta já revisada era genérica e não explicava o problema. Foi adicionada uma mensagem específica para esse caso.
[16/05/2024] [Correção] Ao utilizar campos de seleção múltipla, como campos de marcadores, o dropdown com a lista de marcadores piscava depois do usuário clicar em um dos marcadores já selecionados, dificultando a seleção de novos itens. Agora, ao clicar em um dos marcadores já selecionados o dropdown não aparece piscando.
[16/05/2024] [Correção] Algumas telas de confirmação de deleção estavam sem interrogação.

[16/05/2024] [Correção] No registro de interações, ao inserir uma descrição com múltiplos espaços entre as palavras, os espaçamentos não estavam sendo preservados corretamente.

[16/05/2024] [Correção] Ao introduzir uma nova condição no checklist, foi notado que estava sendo possível salvar sem uma validação da lógica da condição criada. Para solucionar isso, foi implementada uma validação que destaca em vermelho os campos que necessitam ser preenchidos e exibe uma mensagem orientando o usuário a preencher corretamente a condição.
[16/05/2024] [Correção] Ao remover um opcional que foi vinculado por grupo no formulário modal de documentos e adicionar novamente, o produto que havia sido escolhido não era reiniciado.
[16/05/2024] [Correção] Quando o usuário digitava um número muito grande, aparecia o símbolo de infinito no campo e ao clicar fora do campo, o valor zerava. Foi adicionado um limitador de caracteres no campo para que esse erro não ocorra.

[16/05/2024] [Correção] Estava ocorrendo uma concorrência de eventos onmouseleave entre o botão e o botão aninhado. Foi inserido um tempo para garantir que a função do botão principal seja disparada corretamente.

[16/05/2024] [Correção] Ao tentar salvar uma proposta contendo um valor muito grande, um erro acontecia e o botão de salvar carregava infinitamente. Agora, o erro é tratado e o botão de salvar funciona como esperado.
[16/05/2024] [Correção] A opção de vincular na edição de campos não mostrava a tradução correta para a entidade ou o nome correto para campos customizáveis.
[16/05/2024] [Correção] O dropdown de seleção de módulo do sistema não estava fechando quando havia clique do usuário fora dele. Foi corrigido para que ele passe a fechar quando essa interação ocorre.

[16/05/2024] [Correção] Agora o campo Negócio Origem > Estágio não está mais bloqueado em automações de estágio que tenham como gatilho, ganhar, perder ou reabrir o negócio.

[16/05/2024] [Correção] Em formulários de negócio, quando havia múltiplos contatos ou clientes com o mesmo nome, a opção de criar um novo contato/cliente estava sendo ocultada. Essa opção só reaparecia quando o usuário inseria um caractere diferente no campo de busca.
[17/05/2024] [Correção] Campos múltiplos de opção pré-cadastrada em filtros caiam em uma regra de que não pode existir condições de avanço múltiplas, e isso afetava a geração de filtro, gerando um filtro errado. O comportamento foi corrigido.
[20/05/2024] [Correção] Agora ao compartilhar um domumento via email a url do documento e a logo no final do documento segue a configuração do whitelabel.

[20/05/2024] [Correção] Foram adicionadas as versões do título da página em todas as línguas e sempre que a língua do formulário for trocada, a página irá acompanhar a mudança.

[20/05/2024] [Correção] Ao incluir links nas descrições dos campos em um formulário externo, o layout estava sendo prejudicado, pois os navegadores, por padrão, não quebram os textos dos links em várias linhas. Para resolver esse problema, foi implementada uma correção no front-end, permitindo que os textos dos links sejam quebrados em várias linhas.
[21/05/2024] [Correção] Ao inserir um opcional na edição/criação de uma proposta em modo modal, não estava engatilhando as formulas da forma correta.

[21/05/2024] [Correção] Quando havia erro no formulário de checklist, a mensagem fazia o botão descer no container e esconder parte do conteúdo. Agora o erro está na mesma linha do botão.
[21/05/2024] [Correção] Ao adicionar um produto opcional na proposta, o campo de seleção de produto não estava sendo resetado para vazio. Foi corrigido para que o campo seja limpo, possibilitando a seleção de um novo produto sem a necessidade de que o usuário limpe o campo.

[21/05/2024] [Correção] Ao criar um formulário externo e o campo de Estágio fosse obrigatório no sistema (Não no form externo), dava um erro impedindo a criação ou edição do formulário externo, porém, já existe um seletor obrigatório de estágio no formulário externo. E, mapear estágio não funcionava, agora ele só aceita o estágio que está mapeado no formulário externo.

[21/05/2024] [Correção] O ícone de erro ao tentar salvar um relatório antigo inválido ficava desalinhado dos outros elementos. Foi adicionada uma estilização com flexbox para garantir que todos os itens fiquem alinhados.

[21/05/2024] [Correção] Em um negócio com checklist utilizando o campo "Possui tarefas agendadas", ao agendar uma tarefa, o ícone da checklist mudava, mas o campo continuava mostrando "Não" e impedia o avanço de etapa ou ganhar o negócio. Agora, ao agendar uma tarefa, o campo da checklist irá funcionar corretamente, assim como os botões para avançar de etapa e ganhar o negócio.
[21/05/2024] [Correção] Título de negócio muito grande ultrapassava o limite do card na timeline de tarefas. Agora o conteúdo ocupa uma linha, e títulos muito grande tem elipse para esconder o que ultrapassar o espaço disponível
[21/05/2024] [Correção] Na página de relatórios, ao tentar editar ou adicionar um painel com um nome maior com mais de 200 caracteres um erro ocorria e um título longo "quebrava" a página, ele não era truncado e a página apresentava o comprimento do nome inteiro, mas nenhuma barra de scroll aparecia, sendo necessário diminuir o zoom da página para acessar o menu lateral. Agora o campo de nome de painel é limitado até 200 caracteres e títulos longos são truncados corretamente.
[21/05/2024] [Correção] Os elementos como nome do contato e valor do negócio são renderizados apenas quando suas condições de existência são atendidas. Para o valor do negócio, a div agora só é mostrada quando o valor não é vazio, evitando sua exibição desnecessária.
[21/05/2024] [Correção] No módulo de negócios ao preencher um campo único de CPF, uma mensagem de erro piscava ao digitar um CPF inválido. Agora a mensagem não pisca e aparece apenas se o CPF não for único.
[21/05/2024] [Correção] Ao atualizar dados e modelo de um documento, o botão de deletar o documento desaparecia, mesmo com o usuário tendo permissão para deletá-lo.
[21/05/2024] [Correção] Quando era criado um registro de interação e era adicionado anexos, estavam sendo criados um registro para cada anexo adicionado, ao atualizar a página, os registros criados voltavam a ser 1 só e a ordenação normalizava. Quando os arquivos eram atualizados, o novo resultado era adicionado no começo da lista de registros de interação ao invés de substituir o antigo, fazendo com que fossem mostrados vários registros repetidos na tela. Agora a versão atualizada substitui a antiga na lista e é exibido somente 1 registro de interação.
[21/05/2024] [Correção] Caixa de mensagem não estava sendo indicada como campo inválido ao tentar enviar publicação vazia. Agora o campo é identificado como inválido com a borda vermelha.
[21/05/2024] [Correção] Relatórios de parcelas de propostas ou vendas não estavam funcionando.

[21/05/2024] [Correção] Quando dois usuários tentavam revisar uma proposta simultaneamente, um erro genérico era mostrado. Agora o usuário é avisado que está tentando revisar uma versão que não é a mais recente.
[24/05/2024] [Correção] O botão de enviar vendas para o Omie poderia causar a criação de vendas duplicadas, o comportamento foi corrigido.

[24/05/2024] [Correção] Quando o painel editado tinha um nome maior do que o campo permite (por ser uma cópia), o valor ficava zerado na edição. Foi retirada essa restrição e agora o valor mostrado no campo é o nome do painel com caracteres reduzidos.

[27/05/2024] [Correção] Usuários com limitação de visualização de negócios conseguiam ver negócios que não possuiam responsável pelo relatório beta. Com a correção, agora, negócios sem responsável também passam pelo filtro de permissão de visualização.

[28/05/2024] [Correção] Notificações do tipo 'push' de quando um usuário é marcado em um registro de interação agora está mais coerente. Antes era "X marcou você em um registro de contato", agora é "X marcou você em um registro de interação".

[28/05/2024] [Correção] Erros na api do exportador ao iniciar uma atualização de link fazem o link não atualizar. Foi adicionado retry para o caso mais frequente desses erros.

[29/05/2024] [Correção] O aplicativo agora exibe os campos de latitude e longitude desabilitados, alinhando seu comportamento com a versão web. Correção aplicada na versão 4.1.0 do App.

[29/05/2024] [Correção] Foi corrigido o cálculo da tela no App para garantir que o desfoque seja aplicado corretamente em pop-ups de confirmação, como ao trocar o idioma.

[29/05/2024] [Correção] Na exportação de planilhas de negócios, estava sendo aplicado o fuso horário do computador nos campos dinâmicos de tipo Data, fazendo com que a data mostrada na planilha fosse diferente da presente no Ploomes, dependendo do fuso. Foi corrigido para sempre seguir o valor que está no Ploomes, idependente do fuso do computador.

[29/05/2024] [Correção] O App não atualizava a lista de tarefas corretamente quando o usuário se retirava de uma tarefa, esse caso especial foi corrigido.
[31/05/2024] [Correção] Correção de falha que ocorria ao criar tarefas quando alguns valores da proposta estavam vazios, adicionando tratamento para evitar crashes. Correção aplicada na versão 4.1.0 do App.

[31/05/2024] [Correção] O problema dos campos de imagem que permaneciam como preenchidos após a exclusão da imagem foi resolvido, alterando a forma que o App remove o valor do campo. Correção aplicada na versão 4.1.0 do App.
[31/05/2024] [Correção] O app não estava atualizando a lista de tarefas corretamente após um usuário retirar a si mesmo de uma tarefa. O tratamento para esse caso foi adicionado, realizando a atualização necessária após a alteração.
[31/05/2024] [Correção] No formulario de criação de um novo negócio, o campo Contato ficava visível e editável mesmo ainda não tendo preenchido o campo Cliente. Agora o App esconde o campo de Contato e só aparece caso o usuário insira um cliente do tipo empresa. Correção aplicada na versão 4.1.0 do App.
[31/05/2024] [Correção] No aplicativo após alterar o cliente de um Card/Negócio, o contato salvo anteriormente não era removido também. O campo de contato agora é limpo automaticamente quando o usuário troca o cliente, evitando contatos incorretos vinculados a negócios. Correção aplicada na versão 4.1.0 do App.
[31/05/2024] [Correção] Após qualquer ação em tarefas, o App não atualizava a lista corretamente, dessa forma tarefas já excluídas ainda apareciam. A atualização da lista de tarefas no App foi corrigida para evitar que tarefas excluídas continuem aparecendo após qualquer ação do usuário. Correção aplicada na versão 4.1.0 do App.
[31/05/2024] [Correção] O app agora verifica corretamente a permissão de edição de negócios ao carregar as informações do usuário, impedindo edições por usuários sem permissão. Correção aplicada na versão 4.1.0 do App.
