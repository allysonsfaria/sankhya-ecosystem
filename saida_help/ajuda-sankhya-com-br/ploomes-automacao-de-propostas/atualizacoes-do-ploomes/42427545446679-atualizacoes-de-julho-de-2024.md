---
id: "42427545446679"
titulo: "Atualizações de Julho de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427545446679-Atualiza%C3%A7%C3%B5es-de-Julho-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:57Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9553018", "sync_hash_bd17131ece56"]
---

# Atualizações de Julho de 2024

## [01/07/2024] [Correção]

- Usuário sem permissão para visualizar vendas estava conseguindo ver expandir os relatórios de vendas. Agora, há uma condição para verificar se a entidade é Venda e se o usuário tem permissão.

## [02/07/2024] [Correção]

- Ao abrir um registro de interação onde o nome do cliente é muito grande, o nome do cliente ultrapassava o limite e abria um scroll horizontal. Agora o componente ocupa apenas o espaço disponível.
- Usuário de conta que não possuía o módulo Leads ativado conseguia criar novos leads utilizando o atalho 'Shift + L'. Agora, há uma verificação para não permitir o acesso à modal de criação de novos Leads caso o usuário não tenha permissão de criação OU pertença a uma conta que não tem o módulo ativado.
  A disposição de alguns ícones no ploomes estava desalinhada e instável ao dar zoom. Foram feitos ajustes nas partes de timeline de atividades, relatórios beta e informações do cliente em documentos.
- Quando estávamos editando o código fonte para enviar um email, o último caracter não era enviado, ou caso colássemos um valor, o valor anterior era enviado ao invés do novo.
- As versões antigas do Safari não aceitam algumas expressões que estavam sendo usadas. Então foram trocadas para um padrão que não quebra a aplicação no Safari.
- Negócio origem não estava aparecendo nos caminhos de filtro.
- A ação de "Executar agora" uma automação faz com que o cálculo se baseie no dia atual + o horário configurado, ignorando o campo de "Começa em". Agora, adicionamos um modal que informa a próxima data de execução baseado num cálculo do dia de hoje + o que você configurou (5 Anos por exemplo)
- No mapeamento de campos em automações, qualquer campo de número inteiro ficava destacado em vermelho ao ser preenchido com zero. Agora, isso só ocorre para o campo nativo de número do negócio.
- No aplicativo, o criar um registro de interação pelo ícone de criação na página inicial, quando adicionava o cliente a tela ficava em branco. O problema ocorria devido a um componente no código que não possuía utilidade dentro da tela e estava causando o erro. Os desenvolvedores removeram o componente em telas que estava causando tela branca em casos específicos e a correção foi aplicada na versão 4.3.1 do App.
- Correção de formulas em telefones, ocultação de seção em casos específicos e escolha de quem pode editar um campo dentro do App.

## [03/07/2024] [Correção]

- Corrigido problema de inversão de dia e mês em algumas datas no app, garantindo que os valores sejam mantidos corretamente.
- Os filtros do relatório Beta não traziam os dados certos, isso acontecia pois as permissões do usuário não estavam sendo enviadas corretamente. Para resolver isso, os desenvolvedores ajustaram o sistema para sempre considerar todas as permissões necessárias, garantindo assim, que os filtros funcionem.

## [04/07/2024] [Correção]

- Nas configurações do sistema, ao alterar qualquer configuração, salvar e abrir o modal de configurações novamente, as mudanças salvas não apareciam, só apareciam ao atualizar a página. Agora, as mudanças aparecem sem precisar atualizar a página.
- A editar um título que excedia a quantidade de caracteres permitida, era mostrada uma mensagem de erro genérica. Agora aparece um aviso direcionado para esse caso.

## [05/07/2024] [Correção]

- No aplicativo, no módulo de tarefas ao filtrar por "Tarefas dos outros" o aplicativo não exibia nenhuma tarefa, comportamento foi corrigido na versão 4.4.1 do aplicativo.
- No aplicativo, no módulo de Resumo o filtro da tela de Atividades aparecia indevidamente na tela de Tarefas do dia, comportamento foi corrigido na versão 4.4.1 do aplicativo.
- No aplicativo, quando um campo de anexo estava vazio ele não era exibido. Comportamento foi corrigido na versão 4.4.1 do aplicativo.
- Ao criar um negócio pelo formulário de email agora é feito uma validação para saber se está com um cliente preenchido no formulário mini do negócio, se não estiver preenche o valor que está no campo de cliente no formulário de email.
- No app, o formulário checklist estava com um processo onde alguns campos que não estavam preenchidos não estavam sendo renderizados. Esse processo foi removido, visto que estava gerando bugs onde campos não preenchidos que deveriam aparecer estavam ocultos.
- Os campos obrigatórios de bloco vazios não eram destacados ao salvar um documento/venda/proposta. O comportamento foi corrigido.
- Em tela cheia, carregamento de venda com mais de 20 produtos não estava sendo feito corretamente quando um dos itens era removido devido ao filtro da venda, e isso travava o usuário na tela de loading. Descobrimos que, para esses casos, faltava um parâmetro que indicava que o carregamento do template estava concluído. O parâmetro foi adicionado e o carregamento normalizado, de forma que que o usuário siga para a visualização da venda atualizada após remoção do item.

## [08/07/2024] [Correção]

- Na integração com o Omie, em alguns casos, a opção 'As vendas feitas no Omie não serão sincronizadas com o Ploomes' não era respeitada, resultando na criação de vendas no Ploomes mesmo quando essa opção estava marcada. Esse problema foi corrigido e agora essa opção é respeitada sempre.
- Na primeira sincronização com o Omie, não estávamos importando as Ordens de Serviço do Omie para o Ploomes. Agora, elas são devidamente importadas após as Vendas de Produto.
- A mensagem de confirmação de exclusão de registro de interação estava com duas interrogações. Agora, a mensagem está corrigida.
  Mesmo após deletar um campo, os formulários nos quais ele aparecia ficavam com um campo sem rótulo ocupando espaço na edição. Agora, após deletar um campo, ele será removido de todos os forms.
  Na página de negócios, ao tentar alterar o contato com um cliente do tipo Pessoa selecionado, era possível fazer uma busca por contatos, mas não era possível salvar o contato selecionado. Agora, o campo de contato é bloqueado quando o cliente é do tipo Pessoa e não é possível fazer uma busca por contatos.
- Não era possível deletar o logo da empresa em "Dados da empresa", agora é possível remover esse logo e também os logos do módulo WhiteLabel.
- Não era verificado se o usuário tinha acesso aos módulos de E-mail e Tarefas para a exibição dos seus respectivos botões do menu. Agora, essa verificação foi adicionada, e se o usuário não tiver acesso a algum desses módulos, o botão dele será ocultado.
- Na integração com o RD Station, corrigimos um problema em que os campos não eram exibidos na tela plug-and-play quando o token da integração estava expirado. Agora, o token é atualizado no momento que o usuário entra na tela, garantindo que os campos sejam exibidos corretamente.
- Não estava sendo possível criar pastas no módulo de Biblioteca porque as requisições estavam muito lentas gerando erro ao criar as pastas, agora, as requisições estão fragmentadas em partes menores melhorando a desempenho do módulo.
- Adicionamos para mapeamento o campo "Site da Empresa (apenas leitura)" na integração com o RD Station.
- Para ampliar as possibilidades de mapeamento no RD Station, alteramos o campo 'Origem' para permitir não apenas a vinculação a campos de texto simples, mas também a campos de opções pré-cadastradas.
- Os relatórios beta não estavam sincronizando algumas entidades como registro de interação por conta de uma falha no processo de normalização dessas entidades. Essa falha foi resolvida e agora essas entidades são devidamente sincronizadas.

## [11/07/2024] [Correção]

- Campos preenchidos pelo Meetime que excediam o limite de caracteres do Ploomes estavam causando problemas na integração. Foi feita uma correção para garantir que, quando um campo exceder o limite máximo de caracteres do Ploomes, ele não seja preenchido.
- E-mails não estavam sendo recebidos na caixa de entrada do Ploomes. O problema ocorria devido a um alto uso do nosso sistema que fez com que o processamento de mensagens de um cliente atrapalhasse o recebimento de mensagens de e-mail dos demais clientes. Foi uma alta demanda não prevista e os desenvolvedores corrigiram o comportamento para não ocorrer mais este problema.
- Nome do campo de ações da deal não estava traduzido, agora está em todas as línguas.

## [12/07/2024] [Correção]

- Estava sendo possível mapear campos do Omie sem ser com campos equivalentes do Ploomes porque antes os dois campos de mapeamento ficavam abertos. Foi realizada a correção e agora ao abrir um campo, o outro campo desse mapeamento vai fechar.
- Ao fechar um modal com popovers de edição abertos, os popovers demoravam para fechar fazendo com que fossem para outra posição da tela e então fechassem. Agora, as janelas de edição fecham com o modal.
- O formulário de filtro segue regras parecidas com as de outros formulários. Uma dessas regras determina que, se o campo possui a propriedade 'disabled' com valor 'true', o campo será bloqueado no Front-end. Para filtros, esse bloqueio não faz sentido, portanto, foi removido.
- Em E-mails, ao remover um vínculo de uma conversa, há uma modal de confirmação. O texto dessa modal possuía alguns erros gramáticos, que agora foram corrigidos.
- Quando um usuário de suporte estava configurado nas permissões de um painel, caso ele saísse da conta, o campo bugava e não voltava informação de usuário nenhum. Agora, ele volta apenas os usuários que ainda existem na conta.
- Toda vez que vinha um evento do back estava sendo somado, fazendo com que se você faz a validação muitas vezes vai aparecer um toaster para cada uma. A correção fez a limpeza dos eventos para aparecer somente a validação atual.
  O atalho para abrir email dentro do módulo de Emails é "C", porém, já existe um atalho para abrir email fora do módulo, que é "Shift + E", agora, a tecla "C" funcionará apenas dentro do módulo.
- Campo de moeda podia ser configurado como chave, mas a verificação não funcionava. Agora, a verificação nos campos do tipo moeda funciona corretamente.
- Na refatoração da modal de compartilhamento de proposta, o botão 'Adicionar link de visualização' acabou sendo não mapeado e, portanto, removido. Esse botão, agora, foi inserido novamente na modal.
- Registros de interação na timeline do resumo que tinham clientes ou negócios com um nome muito grande quebravam a visualização, ultrapassando o nome da tela. Agora, não ocorre mais, quebrando sempre o nome do cliente ou negócio em linhas abaixo e mantendo o padrão do modal.
- No relatórios beta, quando tínhamos mais de duas métricas com agregações diferentes, o único drilldown que funcionáva era o último, pois, não existia diferenciação na tela por métrica.

## [15/07/2024] [Correção]

- Na integração com o Omie, quando recebíamos dois webhooks de produtos, um de Produto.Alterado e outro de Produto.MovimentacaoEstoque para o mesmo produto apenas o webhook de Produto.MovimentacaoEstoque era processado pela fila. Como resultado, as alterações contidas no webhook de Produto.Alterado eram descartadas.
- Agora na integração do Omie quando o campo estiver vazio a integração vai tentar sincronizar o vendedor e mesmo o vendedor não existindo no Omie, a venda será integrada.
- Na integração com o RD Station, os botões 'Qual ação no negócio do Ploomes gera uma venda no lead referente do RD Station?' e 'Quando uma venda for criada no Ploomes, criar ou atualizar o contato no RD Station' não estavam funcionando completamente como deveriam. Os desenvolvedores implementaram uma correção, e agora eles funcionam corretamente.

## [18/07/2024] [Correção]

- Um erro causado por um deploy do dia 17/07 resultou em buscas com erro na api2. Ajustamos as consultas na api2 para que ocorram corretamente.
- Títulos muito grandes de checklist quebravam o layout na modal de 'checklists pendentes'. Foi aplicada uma quebra de linha em textos muito grandes para evitar a quebra de layout.
- Na visualização em lista do módulo de Tarefas, ao abrir um modal inline para edição e finalizar a tarefa do modal, quando concluíamos a edição, dava um erro, mas salvava corretamente a edição. Agora o erro que antes aparecia indevidamente não aparece mais.
- Na tela de configuração do campo desenvolvedor o limite de tamanho original da área de preview estava incorreto tanto para mais, quanto para menos. Além disso, um scroll desnecessário aparecia quando o campo era muito pequeno. O comportamento foi corrigido.
- Ao fazer upload de uma imagem muito grande ou com erro dentro da tela de edição de modelos de documento, não havia nenhuma indicação de erro para o usuário. Agora há erros para imagens inválidas, acima do tamanho limite (10mb) e de formato incorreto.
- Fórmula no campo de total da proposta não estava sendo engatilhada quando usuário removia uma seção de produtos, mas estava sendo engatilhada na duplicação, o que causava discrepância no valor total - ou seja, aumentava o valor ao duplicar seção, mas não subtraía o valor correspondente quando a seção era removida. Ajustamos para que a remoção de seção também seja gatilho para a fórmula que calcula o valor total da proposta.
- Ao puxar por fórmula um campo de proposta em documento, o valor só era buscado na criação, mas não funcionava corretamente na edição. O comportamento foi corrigido.
- Em negócio, podemos enviar e-mails através da linha do tempo. Porém, especificamente nas mensagens enviadas por esse local, a assinatura de e-mails do usuário era intermitente: hora era enviada normalmente, hora desaparecia. Agora, essa intermitência foi resolvida.
- Edição inline estava estilizada de uma forma que se estivesse inserida num componente que tem scroll, ele era feito parte do scroll, ao invés de aparecer encima de qualquer elemento da tela.
- Ao duplicar uma proposta, o template de documento estava sendo redefinido para o padrão da conta. Agora o mesmo modelo da proposta original está sendo usado na proposta duplicada.
- Caso o nome de um estágio contivesse muitos caracteres, ao escolher um estágio numa ação de automação, a opção grande quebraria o modal, fazendo com que o texto quebrasse e saísse da tela.
- Em Relatórios Beta, se o usuário clicasse em deletar um painel e mantivesse o cursor sobre um gráfico, o tooltip permanecia na tela até o cursor passar sobre outro gráfico. Foi adicionada uma função que remove o tooltip sempre que há uma troca entre painéis.
- Nomes de produtos muito grandes na configuração de grupo de produto saiam da tela.
- Em automações, quando uma entidade possui o nome muito grande, o layout da modal acaba quebrando. Os botões de 'Nova automação', 'Configurações' e o input de 'Busca por nome' são empurrados da tela, impedindo o usuário de utilizá-los. A estilização da listagem de automações foi alterada para garantir a integridade do layout e o acesso às funcionalidades de automação.
- Quando um checklist possuía um nome muito grande (atingindo ou próximo de atingir o limite de caracteres), ao duplicá-lo, era exibido um erro genérico para o usuário, pois ocorria erro ao tentar adicionar o prefixo '[ Cópia ]' para identificação, pois o nome do novo checklist ultrapassava o limite de caracteres. Agora, nesses cenários específicos, o prefixo '[ Cópia ]' não é adicionado, para não impedir o usuário de duplicar seu checklist.
- Mapeamento de campo do tipo anexo no valor padrão em formulário externo foi bloqueado, o campo não pode ter valor padrão, isso já era algo que existia, porém, no mapeamento do formulário externo não tínhamos removido.
- O frontend exibe o documento como "assinatura via Clicksign ativada" porque o front verifica o valor do campo "Disparado (Clicksign)" mas o endpoint de desligar assinatura só remove o Id do Clicksign do documento, mantendo o "Disparado" como verdadeiro. Corrigimos para que ambos os campos sejam editados corretamente.
- Quando temos uma automação genérica que, ao criar um novo negócio, envia-o para outro estágio (que não o inicial), essa automação é executada com sucesso, mas, na tela do negócio recém criado, em alguns momentos, ainda constava como se ele estivesse no estágio inicial. Esse problema foi corrigido, e agora o componente que mostra o estágio atual do negócio é atualizado corretamente conforme a automação.
- Colocar um intervalo com datas vazias, quebrava a visualização da página. Uma correção foi feita para evitar o comportamento.
- Anteriormente, utilizávamos a injeção de código no campo de desenvolvedor através de um iframe. No entanto, a forma como estávamos renderizando o elemento na tela estava prejudicando o carregamento dos demais elementos, causando uma lentidão considerável de cerca de 14 segundos. A melhoria realizada consistiu em implementar uma renderização paralela que não interfere nos outros elementos da tela. Com isso, conseguimos reduzir o tempo de carregamento para 6 segundos.
- Ao preencher um campo de data com a mesma data por fórmula várias vezes seguidas, de forma intermitente, a data não era formatada. Esse bug foi corrigido, e além disso, foi implementado suporte para que os campos do tipo data aceitem o formato "AAAA-MM-DD" para preenchimento em fórmulas (anteriormente apenas o formato "DD/MM/AAAA" era aceito).

## [22/07/2024] [Correção]

- Agora, na integração com o Omie, também utilizamos os webhooks do tipo 'LocalEstoque'. Isso nos permite evitar requisições desnecessárias à API do Omie, reduzindo significativamente a ocorrência de erros.
- O cliente não era capaz de receber leads de um determinado formulário do Facebook devido ao tamanho do nome da página e das perguntas superior ao limite do campo que armazena essa informação em nosso banco.

## [23/07/2024] [Correção]

- Ao gerar mensagens para anexar na planilha com logs, a lista de mensagens vinha com objetos nulos que não possuiam tratamento e quebravam a lógica de importações e fazia com que ela nunca finalizasse. Foi implementado uma lógica para remover os valores nulos da lista de mensagens para resolver esse problema.
- Ajustada a lógica do aplicativo para mapear dados do cliente e do contato, garantindo a renderização correta do campo CPF. Correção aplicada na versão 4.4.4 do Aplicativo.
- Automações com ação de deletar em Clientes e Negócio não estavam funcionando, os desenvolvedores implementaram uma correção, e agora essas automações funcionam corretamente.
- Havia lentidão na criação de documentos, o que fazia com que alguns deles excedessem o tempo limite de criação. Para resolver isso, foi feita uma alteração para melhorar a performance.

## [24/07/2024] [Correção]

- O app foi atualizado para adicionar automaticamente "Sem título" ao criar negócios sem título, alinhando-o ao comportamento da Web.
- No app, ao finalizar tarefas, o toast de sucesso permanecia na tela. Isso ocorria porque os toasts eram "empilhados" em sequencia, o que ocasionava no travamento do componente. Os desenvolvedores implementaram uma correção, e agora o toast anterior é fechado antes de abrir um novo.
- O app estava tentando acessar valores mesmo após a exclusão do registro, levando ao crash. Foi adicionado o tratamento para verificar se esses valores ainda existem antes de acessar.
- Varias ações de finalização de tarefas eram feitas em sequencia mas como não havia tratamento de espera algumas delas não eram de fato finalizadas.
- No app, o tratamento de fórmula foi ajustado para disparar mesmo quando o campo está nulo, convertendo o valor nulo em texto vazio.
- Na integração com o Docusign, a URL de refresh token usada pelo Polling estava incorreta, o que causava a falha no processo de renovação do token. Os desenvolvedores implementaram uma correção, e agora a URL está correta.

## [25/07/2024] [Correção]

- A condição para verificar se o usuário possui metas foi adicionada, controlando a exibição da aba de metas.
- Em formulários, se o usuário tivesse uma seção com um campo obrigatório, apagasse a seção e tentasse salvar, um erro ocorria e o botão de salvar ficava carregando infinitamente. Agora, não é mais possível remover uma seção que contém um campo obrigatório.
- Em documentos de negócio, através de uma consulta no banco offline, o aplicativo estava validando o documento como tendo um negócio sem cliente de forma incorreta. Para resolver isso, foi adicionada uma consulta online do negócio para verificar se o mesmo possui cliente ou não, assim, destravando criação/edição de documentos vinculados a negócios que não foram completamente baixados pelo aplicativo.

## [26/07/2024] [Correção]

- A condição para o botão de reabrir propostas compartilhadas não estava funcionando como esperado. Agora, o botão é ocultado e exibido corretamente.

## [29/07/2024] [Correção]

- A mensagem de nova empresa/pessoa estava com o nome do novo item em negrito. Agora, o nome não fica mais em negrito.
- Na tela de resumo, quando havia somente um funil no widget de negócios, o select de funis era ocultado. Dessa forma, o Front-end não exibia em nenhum lugar o nome do funil. Agora, o select passa a aparecer nesses casos, e, quando aberto, exibe a mensagem ''Você possui apenas um funil" (comportamento padrão do Ploomes).
- Na modal de remoção de vínculos de e-mail, o ícone de fechar estava desalinhado. Agora foi corrigido e está centralizado.
- O botão genérico de expandir informações, que aparece em várias áreas do Ploomes, estavam com seu ícone descentralizado. Agora, isso está corrigido, e o ícone está alinhado corretamente.
- Quando configurávamos filtros com campos de opção pré-cadastradas no relatório beta, se trocássemos um campo que já continha opções, ele mantinha as opções de outro campo, gerando inconsistência e filtros incorretos.
- Na visualização de negócios em tabela, ao remover o cliente, o campo de contato era bloqueado e não era possível remover o contato associado. Agora, quando removemos o cliente ou mudamos para um cliente do tipo pessoa, o contato é removido antes do campo ser bloqueado.
- Ao acessar o modal de tarefa, e depois a aba 'Dados do cliente', havia uma quebra de layout caso o nome de um contato fosse muito grande. Agora, nesses casos, o texto se limita a aparecer apenas dentro da modal, com reticências e com um tooltip informando o nome completo do contato.
- Campos que nós montamos para salvar no Ploomes, dependendo de como eram recebidos do Meetime, não eram integrados devido à quantidade de caracteres. Sendo assim, foi adicionada uma verificação para esses campos compostos, igual feito para os que são recebidos do Meetime.
- Quando um campo de porcentagem era utilizado na criação de um gráfico nos relatórios beta (principalmente em operações como soma, média e valores máximo e mínimo), as barras e legendas do gráfico ficavam mal diagramadas. Os desenvolvedores implementaram uma correção, e agora a visualização fica correta.
- A aplicação salvava o último funil selecionado no GeneralData. Quando esse funil era arquivado, o sistema tentava encontrá-lo na lista de funis ativos (não arquivados). Se o funil não fosse encontrado, o sistema exibia o primeiro da lista geral de funis (que contém tanto os arquivados quanto os ativos) no módulo de resumo. Agora, o sistema seleciona, por padrão, o primeiro da lista de funis ativos.
- Ao remanejar negócios, as fórmulas perdiam a fonte de informações, não traziam os dados, e não calculavam os resultados. Os desenvolvedores implementaram uma correção e, agora, as fórmulas estão funcionando corretamente.

## [30/07/2024] [Correção]

- Ao adicionar marcadores, e depois remover algum, todos os marcadores voltavam a aparecer no campo "Adicione produtos filtrados por marcador como vínculos". Isso ocorria pois, no momento de montar a lista de entidades (Produto, Grupo ou Marcador), o componente estava verificando se havia aquela entidade na lista de vínculos atuais. Porém essa verificação estava falhando. Agora isso foi corrigido, e se a entidade já estiver vinculada ao produto, ela não aparece na lista de opções de vínculo.
- Ao ler via fórmula um campo multilnha, quebras de linha e espaços 'tab' eram convertidos para <br> e <p> no valor da variável, causando erros e bugs. O comportamento foi corrigido para não adicionar <br> e <p> adicionais no retorno da fórmula.
- Ao inserir opcionais, em alguns casos todos os opcionais eram inseridos, mesmo sem estarem configurados como padrão. Agora eles só são adicionados se estiverem configurados, como esperado.
- Não era possível ler por fórmula valores da entidade 'Cliente.Empresa' no formulário de negócio.
- Ao abrir dados do cliente, nas páginas de edição e criação de proposta, documento e venda, se alguma aba tivesse nome muito grande, as últimas abas iam para a linha abaixo e não era possível selecionar elas. Agora, é possível visualizar todas as abas.
- Ao abrir dados do cliente, nas páginas de edição e criação de proposta, documento e venda, se alguma aba tivesse nome muito grande, as últimas abas iam para a linha abaixo e não era possível selecionar elas. Agora, é possível visualizar todas as abas.
- Em propostas, na seção de 'Itens adicionados', ao remover produto com vínculo padrão e inseri-lo novamente, o vínculo padrão não vinha marcado. Foi corrigido para manter o comportamento da seção 'Novo item', em que, ao adicionar um produto com vínculo padrão, ele vem marcado por default

## [31/07/2024] [Correção]

- Ao abrir um novo documento de cliente, o formulário estava vindo em branco por conta de um parâmetro incorreto no código.
- Ao adicionar, remover e adicionar novamente um produto na proposta, por conta de um erro no código, o valor dos campos de opções pré-cadastradas com filtro por fórmula era substituído pelas opções das variáveis da fórmula. O comportamento foi corrigido mantendo o campo vazio como esperado.
- A duplicação causada por certos mapeamentos de empresa e pessoa feitos no bloco de negócio sobrescreviam os vínculos feitos ao negócio criado. Corrigimos o tratamento desses mapeamentos para que não afetem vínculos.
- Ao editar um bloco de produtos no configurador de documentos, caso no filtro do bloco houvesse algum grupo/família ou marcador que foi deletado, nenhuma sinalização era feita para o usuário, e nem mesmo era possível remover o item com problemas. Agora o front irá sinalizar o erro e será possível remover do filtro o item que foi excluído.
- Havia um problema de criação múltipla de tickets na Movidesk para clientes com e-mails iguais. Com a correção, agora o ticket é criado apenas para o cliente específico do negócio.
