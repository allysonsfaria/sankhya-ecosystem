---
id: "42427579338007"
titulo: "Atualizações de Setembro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427579338007-Atualiza%C3%A7%C3%B5es-de-Setembro-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:24Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9828959", "sync_hash_143835e65400"]
---

# Atualizações de Setembro de 2024

## [03/09/2024] [Correção]

- Ao editar um documento, em alguns casos, o front tentava erroneamente buscar os produtos da proposta para fazer um 'vínculo', mas isso não deveria acontecer na edição. O problema foi corrigido.
- Não era possível criar vínculos de marcadores iguais mesmo estando em categorias diferentes. O comportamento foi corrigido e agora este problema não ocorre mais.

## [04/09/2024] [Correção]

- Na integração Omie, o campo "Utilizar os seguintes endereços de e-mail" era mapeável em vendas de produto, mas não em ordens de serviço do Omie. Adicionamos a possibilidade de fazer esse mapeamento.
- Em exportações de abas para Excel, usuários sem permissão para visualizar um campo em uma aba, ao exportarem a aba, o campo que o usuário não possui permissão de visualização era exportado com seus respectivos valores na planilha. Correção foi aplicada.
- O recebimento de contatos vindos do Active estava inconsistente devido há subida de uma versão antiga da nossa API. Os desenvolvedores alteraram a versão e os leads voltaram a integrar normalmente.
- Com a opção 'Quando o contato não tiver uma empresa no RD, criar uma empresa no Ploomes chamada "Empresa do [contato]"' marcada, ao criar uma empresa que não existe no RD, mas já existe no Ploomes, sem preencher o nome da empresa no RD, era alterado o nome da empresa já existente para "Empresa do [contato]". Agora, nesse caso específico, o nome atual será mantido.
- A extensão Ploomes para WhatsApp poderia em alguns casos não carregar informações do contato e negócios, aprimoramos a busca para corrigir o comportamento. Correção aplicada na versão 0.0.1.33 da extensão.
- Anteriormente, ao tentar vincular um e-mail, o sistema não permitia a vinculação se o cliente estivesse somente como contato do card. Os desenvolvedores implementaram uma correção, e agora é possível selecionar tanto quando é cliente quanto contato do card.

## [05/09/2024] [Correção]

- Ao excluir a opção padrão de um campo de opção pré-cadastrada ela continuava como padrão e causava um erro.
- Ao editar uma proposta que já havia sido aceita externamente, não era enviado um novo e-mail para o destinatário.
- No app, ao criar uma proposta e revisar logo em seguida, depois excluir a revisão feita, comentários feitos no chat externo não eram exibidos.
- Não era possível excluir uma categoria de vínculo que tivesse algum vínculo apagado. Os desenvolvedores corrigiram esse comportamento, e o problema não ocorre mais.

## [06/09/2024] [Correção]

- Ao criar uma tarefa no IOS ou Web, adicionar um usuário em descrição da tarefa, faz com que ele seja relacionado automaticamente e receba uma notificação da tarefa. O mesmo não acontecia no Android, onde o usuário ficava apenas como um comentário na descrição.
- No app, ao editar um documento de cliente na tela do cliente, era possível tornar o mesmo, um documento de negócio, mesmo sem ter nenhum negócio vinculado a ele. Correção aplicada na versão 4.10.0
- No app, ao deletar uma venda, o aplicativo volta para tela de todas as vendas, onde a venda que está sendo deletada ficava visível e, clicando nela o usuário estava sendo direcionado para dentro da venda com tudo vazio e carregando infinitamente. Correção aplicada na versão 4.10.0
- No Modo Offline do app, os Negócios não estavam salvando o `LastQuoteId` das Propostas geradas offline. Os desenvolvedores implementaram uma correção e agora este problema não ocorre mais.
- Na integração com o DocuSign, documentos enviados via whatsapp e SMS não eram marcados como assinados no Ploomes, o comportamento foi corrigido.
- No app, ao tentar criar/editar algum cliente sem preencher o campo telefone (quando o campo não é obrigatório), era disparada uma mensagem de erro. O comportamento foi corrigido e o problema não ocorre mais.

## [09/09/2024] [Correção]

- Os campos de endereço não estavam sendo limitados até 200 caracteres corretamente. O problema foi resolvido.
- Agora existe uma limitação em arquivos de e-mail, tarefa e biblioteca. Qualquer extensão diferente da lista seguinte irá voltar um erro para o usuário. Extensões válidas: '.doc', '.docx', '.xlsx', '.xls', '.csv', '.png', '.jpg', '.jpeg', '.pdf', '.txt', '.odt', '.ppt', 'pptx', '.odp', '.gif', '.mp4', '.mp3', '.zip', '.rar', '.wmv', '.mov', '.bmp', '.tiff', '.mkv', '.avi', '.aac', '.flac', '.rm', '.rmvb'.
- Ao mover colunas numa tabela, a barra azul que indicava os movimentos não estava desaparecendo. Os desenvolvedores implementaram uma correção e agora esse problema não ocorre mais.
- Era possível adicionar o campo 'Produtos' no formulário de clientes, mas o campo não era funcional. Agora, não é possível adicionar o campo nos formulários.
- Negócios ao serem remanejados estavam com um erro relacionado à deal origem, agora não existe mais e todos serão remanejados normalmente.
- Nos relatórios beta, ao clicar em um item em gráficos de registro de interação, é levado até a página do registro.
- Quando o usuário não tem permissão para visualizar um negócio preenchido em um campo, antes aparecia em branco o valor do campo, agora aparecerá preenchido com "Sem permissão para visualizar o Negócio". O usuário poderá alterar o campo em formulário, porém em checklist o campo ficará bloqueado para a alteração.
- Ao criar um formulário externo com algum campo de opção pré-cadastrada, ao reabrir o formulário para editar, os campos expandiam e cobriam o input inteiro, impossibilitando a adição de novas opções, a não ser quando removido um dos campos.
- Ao tentar finalizar uma tarefa quando ela está num estágio deletado, ou, quando outra pessoa finalizou simultaneamente, gerará erros personalizados informando o usuário o que aconteceu.
- Ao selecionar qualquer anexo em email ele era considerado inválido. Esse comportamento foi corrigido.

## [16/09/2024] [Correção]

- Nas versões com a feature de meta nova (\_\_goals), não estava sendo possível fechar os menus laterais no Ploomes. Os desenvolvedores implementaram uma correção, e agora esse problema não ocorre mais.
- Mesmo com o perfil configurado para a língua en-US, as datas eram exibidas no formato DD/MM/AAAA sempre. Agora elas são exibidas para o usuário no formato MM/DD/AAAA.
- O Active não suporta campos customizados numéricos em contatos. Adicionamos a possibilidade de mapear campos de Linha de Texto do Active para campos de número inteiro do Ploomes. Os valores serão convertidos e integrados caso o campo contenha um número inteiro válido.
- O tamanho mínimo foi definido para os campos do tipo cliente em uma tarefa específica, mas esse tamanho mínimo não poderia existir em algumas partes do sistema. Agora o tamanho está correto em todos os lugares.

## [17/09/2024] [Correção]

- Ao duplicar proposta + card, em alguns casos específicos envolvendo anexos um erro ocorria devido uma validação incorreta no código. Agora a duplicação sempre vai funcionar como esperado
- Ao usar em fluxos de aprovação o campo "Proposta.Produtos", ao atualizar dados e modelo o documento caia no fluxo mesmo tendo produtos. O problema foi corrigido.

## [18/09/2024] [Correção]

- O número de algumas vendas estava sendo deletados em atualizações vindas do Omie. Isso ocorria devido a conversão de alguns objetos não possuírem o número da venda preenchido. Os desenvolvedores ajustaram a manipulação dessa informação e esse campo não deve mais ser deletado.
- Alterações vindas do Omie estavam sobrescrevendo/removendo campos já existentes no Ploomes quando alguns campos não estavam preenchidos nas requisições que chegavam ao Ploomes. Eliminamos campos não preenchidos nas requisições de atualizam que poderiam apresentar esse comportamento.

## [20/09/2024] [Correção]

- No App, os campos numéricos preenchidos com 0 não apareciam na Aba de Dados. Os desenvolvedores implementaram uma correção e esse problema não ocorre mais.
- No aplicativo, ao preencher Checklists no iOS, caso a lista fosse grande o suficiente para criar um scroll, quando abríamos para preencher os últimos campos, o teclado estava sobrepondo o campo e não permitia que o usuário enxergasse o que está digitando, além da dificuldade de clicar no botão de salvar. Agora o teclado empurra o campo para cima. Correção aplicada na versão 4.11.1.
- Correção de visualização de campos mais abaixo na tela quando usuário usa o teclado. Correção aplicada na versão 4.11.1.

## [24/09/2024] [Correção]

- O campo Proposta.Modelo não retornava em fórmulas no CPQ novo. O problema foi corrigido.
- Um campo com opção vazia não era tratado corretamente em fórmulas dentro do formulário do CPQ novo. Agora ele é lido corretamente nas variáveis.
- Uma pequena indisponibilidade na api2 causou erros inesperados que interromperam a integração da assinatura de um documento do Clicksign com o Ploomes. Adicionamos tratamentos e retries para novos casos de erro incluindo o que impactou nesse chamado.
- Em relatórios beta, alguns relatórios não estavam aparecendo. Isso foi provocado por uma atualização nos navegadores (Chrome, Edge 129), o problema foi corrigido com uma alteração no CSS de relatórios.

## [26/09/2024] [Correção]

- Os dados do contato não estavam sendo formatados corretamente, fazendo que não fosse possível buscar via fórmula o telefone do contato em algumas situações. O problema foi corrigido.
- No modal de criação de vínculos de produto, caso o formulário iniciasse com uma seção, a seção ficava parcialmente atrás do texto no modal.
- As automações permitiam a criação de filtros muito complexo/grande que quebravam ao ser construídos, essa é uma limitação do ODataAgora, portanto a correção foi sobre a possibilidade de criar filtros complexos/grandes, agora ao tentar salvar uma automação que tenha filtros inválidos, um erro aparecerá na tela impedindo o usuário e notificando-o.
- Um erro acontecia no front ao tentar ler o campo 'Negócio.Criador.Equipes' na edição de um negócio. Agora a variável é lida corretamente.
- Foi feito uma melhoria no back de CPQ, para que o tempo de processamento e salvamento de um modelo de documento seja menor, evitando timeouts.
- Em uma requisição de criação ou edição de propostas, o usuário conseguia passar um DealId e, no objeto, colocar dados de outro negócio, podendo burlar fluxos de bloqueio, por exemplo. Agora sempre usaremos o dealId e descartaremos o objeto deal.
- O parâmetro de preload foi adicionado nas requisições para inserir produtos de cliente via dados do cliente, tornando-as mais rápidas e evitando timeouts.
- As exibições condicionais que utilizam campos do tipo "String" em alguns modelos poderiam falhar caso o texto contivesse caracteres especiais, devido à possibilidade de serem armazenados com uma codificação diferente. Sendo assim, os desenvolvedores implementaram um tratamento na comparação de textos nas condicionais para garantir que eles sejam validados corretamente, mesmo quando codificados de maneira distinta.
- Agora os campos nativos 'Estado' e 'Cidade' podem ser inseridos em formulários de cliente.
- Foram adicionados os seguintes tipos de extensões em anexos permitidos: '.wav' , '.cdr', '.opus', '.ogg', '.svg' e '.psd'.
- Ao alterar o estágio de um negócio através de uma automação de funil, o webhook gerado indicava que o negócio já estava no novo estágio, esse comportamento foi corrigido.
- Na página de negócio, ao ganhar o negócio, nenhuma proposta era marcada como a proposta ganha, agora, a última proposta aberta será a proposta ganha. Com isso, se a automação de criar venda ao ganhar negócio estiver ativa, a venda criada vai ser associada a essa última proposta.
- No relatório antigo, o agrupamento de semana contabilizava começando pela segunda, mas o total contabilizava começando pelo domingo, agora, sempre começará a contabilizar pelo domingo.
- Na tela de criação de negócio + proposta, ao inserir um cliente, as fórmulas com campos de contato eram engatilhadas e vice-versa. O comportamento foi corrigido para seguir corretamente o fieldpath da variável.
- Antes, ao agendar uma nova tarefa sem atualizar a página, a data ficava como o dia atual. Os desenvolvedores corrigiram esse comportamento, e o problema não ocorre mais.
- Timeouts em uma requisição na API2 causavam erros na integração ao enviar documentos para o LetsSign. Otimizações foram implementadas nessa consulta, reduzindo os tempos de carregamento ao enviar um documento para assinatura.
- Na configuração de permissões por perfil de usuário, a ordem das opções foi alterada e foi adicionando um tooltip para explicar o funcionamento da opção "Incluir negócios onde o cliente está sob responsabilidade/colaboração" de negócios, além disso, essa opção agora é desabilitada se a permissão for para "Todos" ou "Nenhum".
- Agora no resumo, a contagem de Deals criadas que era baseada na data de início, agora será baseada na data de criação.

## [27/09/2024] [Correção]

- Agora o campo de aniversário ('birthday") na entidade de clientes (Contacts) não aceita mais datas inválidas via API.
- Antes, era possível inserir várias vezes o mesmo campo no formulário de Vínculos. Os desenvolvedores realizaram uma alteração para remover valores duplicados de uma tabela que fazia o front-end não atualizar o cache corretamente, resolvendo o problema.

## [30/09/2024] [Correção]

- Os eventos de teclado funcionavam na busca mesmo quando o modal estava fechado. Foi adicionada uma limitação para os eventos de pressionar as setas ou o enter só funcionem caso o modal de busca estiver aberto.
- Antes, não era possível buscar contatos pertencentes a qualquer empresa ao tentar adicionar um contato na tabela de negócios. Agora, a busca funciona normalmente.
- Na descrição de tarefas, caracteres fora do intervalo ASCII/Latin1, como certos caracteres Unicode, causavam erros que afetavam a visualização das tarefas do dia, no modo lista e ao exibir a tarefa. Agora, esses caracteres são aceitos, ampliando a compatibilidade.
- Corrigimos um bug relacionado a criação e edição de automações que criam novo negócio em um funil que o campo "Negócios Derivados" faça parte de seu formulário.
- Ao deletar um negócio, caso haja negócios originados dele, os negócios derivados perdem a referência ao negócio origem.
- Em tabelas dinâmicas, o tooltip para elementos longos não era exibido em algumas situações. A lógica para exibição de tooltips foi alterada e agora, ele é mostrado corretamente em todos os casos.
- Ao adicionar uma imagem no cadastro do cliente apareceria uma mensagem de sucesso mesmo que o upload não tivesse sido feito corretamente. Agora uma mensagem de erro adequada deve aparecer ao tentar fazer o upload de uma imagem com formato inválido ou corrompida.
- Nos arquivos de translate, havia um erro na palavra "maiúsculas" tanto em português do Brasil quanto de Portugal. Agora a palavra foi corrigida nos dois arquivos.
- Em campos de filtros, o símbolo '#' estava sendo substituído por '%23' após salvar o filtro, agora o campo permanece como '#' corretamente.
