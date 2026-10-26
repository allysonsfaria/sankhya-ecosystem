---
id: "42427559330583"
titulo: "Atualizações de Novembro de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427559330583-Atualiza%C3%A7%C3%B5es-de-Novembro-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:42Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6531680", "sync_hash_604a2cb05d54"]
---

# Atualizações de Novembro de 2022

[03/11/2022] [Correção] Ao alterar o estágio de uma venda que estava em um fluxo de aprovação, a venda saia do fluxo, mas a notificação se mantinha.

[03/11/2022] [Correção] Senha forte não aceitava '@', '!' e outros caracteres especiais como primeiro caractere, e reclamava de ',' e '.' como caractere especial.

[03/11/2022] [Correção] Fluxo de aprovação não funcionava ao verificar a rota de contato do negócio.

[03/11/2022] [Correção] Id de planilha de importação era exibido de forma errada por conta de conflito com outro id.

[03/11/2022] [Correção] Quando um comentário era feito dentro de um registro de interação, ao clicar na notificação eramos direcionados para a entidade que aquele registro de interação está vinculado, e não para o registro de interação que foi feito o comentário.

[03/11/2022] [Correção] Quando campos CNPJ, CPF e ZipCode vinham vazios não passavam na condição de importação.

[03/11/2022] [Correção] Quando o e-mail do remetente era obtido de um campo multilinha, automação não enviava o e-mail corretamente.

[03/11/2022] [Correção] Texto em negrito dentro do documento de proposta "engolia" espaçamentos e outros caracteres na sequência do texto.

[04/11/2022] [Correção] Sincronização de cards no aplicativo estava gerando inconsistências e gerando duplicatas ao visualizar.

[04/11/2022] [Correção] Não estava sendo possível criar uma proposta no app por conta de uma regra de bloqueio executada de forma errada.

[04/11/2022] [Correção] Campo aparecia no app mesmo estando oculto na web, causando erros ao realizar automações.

[04/11/2022] [Correção] Campo no app não estava respeitando a regra de bloqueio.

[04/11/2022] [Correção] Ao fazer a sincronização pelo app, ele não baixa todos os negócios e também não baixa somente os do usuário.

[04/11/2022] [Correção] Mensagem no app não deixava claro que funcionalidade de visualização de e-mail está disponível somente na versão web.

[07/11/2022] [Correção] Era permitido colocar o valor padrão de um campo de opções pré-cadastradas como ele mesmo, porém, isso gera um erro esperado, então, foi bloqueado essa configuração incorreta.

[07/11/2022] [Correção] Ao preencher o campo chave 'CPF' de negócio era possível colocar o mesmo valor em vários negócios diferentes.

[08/11/2022] [Correção] Usuário mencionado em uma tarefa em registros de interação não aparecia nas notificações da cliente, mesmo tendo todas as permissões.

[08/11/2022] [Correção] Arquivos na biblioteca com nomes cortados devido ao tamanho, não exibiam o label com o nome completo.

[08/11/2022] [Correção] Ao clicar em "visualizar" em um registro de interação de e-mail, não estava sendo exibido o conteúdo da mensagem.

[08/11/2022] [Correção] O filtro feita na criação de uma nova pessoa para verificar se o e-mail era duplicado, não era muito eficiente, principalmente em casos com muito itens para serem filtrados, e isso estava ocasionando erro.

[08/11/2022] [Correção] Erro de importação quanto a limite de tamanho excedido era exibido como uma mensagem de erro genérica.

[08/11/2022] [Correção] Criação de venda não estava funcionando.

[08/11/2022] [Correção] Estava dando erro ao tentar integrar o CNPJ pela receita federal.

[08/11/2022] [Correção] Ao adicionar '&' no código-fonte de um campo de texto multilinha e puxar o valor dele para outro campo, apresentava uma inconsistência, trazendo o nome do campo ao invés do '&'.

[08/11/2022] [Correção] Ao editar a data de uma tarefa, por padrão o campo de endereço estava abrindo uma lista com o endereço da tarefa, impossibilitando a visualização do resto das informações até o usuário clicar fora do campo de endereço.

[08/11/2022] [Correção] Não estava sendo possível salvar checklists com o campo [Cliente.Endereço] e [Contato.Endereço] quando eles estavam com a condição para avanço vazia.

[08/11/2022] [Correção] Em uma importação com linhas em que os valores estavam no formato incorreto, a mensagem de erro estava sendo exibida na coluna errada no modal de confirmação de importação.

[08/11/2022] [Correção] Na criação de uma automação de funil, quando se escolhia uma ação para criar/editar dados, o formulário e os ícones dos funis não apareciam.

[08/11/2022] [Correção] Integração RD Station estava ativa e mesmo assim alguns negócios de certos funis não eram enviados para o RD.

[08/11/2022] [Correção] Campo [Venda.Estado do cliente] não puxa dados do campo [Estado.Sigla], conforme configuração da fórmula.

[08/11/2022] [Correção] Ao fazer quebra de linha no preenchimento de um campo de texto multilinha, a quebra era feita duas vezes, deixando um espaçamento muito grande.

[08/11/2022] [Correção] Campo do tipo Usuário não permitia vincular nenhum outro campo a ele como valor padrão.

[09/11/2022] [Correção] Campos de endereço estavam bloqueados para edição por conta de falha de conexão com o Google Maps.

[09/11/2022] [Correção] Quando um usuário não tinha permissão para EDITAR produtos, o mesmo estava conseguindo fazer alterações nos vínculos, porém as mesmas não eram salvas e mesmo assim dava uma mensagem de sucesso. Agora, caso o usuário não tenha permissão para EDITAR produtos, o mesmo fica bloqueado de editar os vínculos.

[09/11/2022] [Correção] Campos de usuários em fórmulas de Vendas e Documentos não estavam funcionando.

[09/11/2022] [Correção] Ao atualizar senhas simples, será necessária a inserção de no mínimo 8 caracteres.

[09/11/2022] [Correção] Havia uma falha na inclusão de opcionais, fazendo com que as opções não fossem exibidas.

[09/11/2022] [Correção] Formulário de edição de cliente não funcionava quando a página era recarregada ou o link era aberto em outra aba. Adicionou-se uma requisição para puxar os dados do cliente para edição para esses dois casos.

[09/11/2022] [Correção] Campos de opções pré-cadastrada com valor padrão e com regra de visualização configurada não persistia os valores quando campo era escondido e exibido novamente.

[09/11/2022] [Correção] O formulário de criação e edição de cliente estavam compartilhando o mesmo escopo de dados, fazendo com que os campos puxassem o valor da empresa em vez de deixar em branco para um novo cliente.

[09/11/2022] [Correção] Vendas diferentes geradas a partir de propostas diferentes estavam puxando valores da mesma proposta.

[09/11/2022] [Correção] Erros de login não estavam aparecendo para alguns usuários.

[09/11/2022] [Correção] Bug na visualização de um campo de proposta, sendo possível ver somente quando se alterava o responsável pela tarefa e voltava para o original.

[09/11/2022] [Correção] Na integração com o Omie, o limite de tempo para realizar a sincronização foi aumentado, evitando 'timeouts'.

[10/11/2022] [Correção] Ao fazer a exclusão em massa a partir de uma aba, o erro 500 era retornado, não permitindo a inicialização do processo de exclusão.

[10/11/2022] [Correção] Ao realizar importação de produtos, o campo "Nome" aparecia duas vezes.

[10/11/2022] [Correção] O nome dos campos nos registros de informação em negócio não estavam aparecendo o informativo em nomes muito grandes.

[16/11/2022] [Correção] Ao criar venda com produtos e serviços para o Omie, estava com algumas inconsistências no código que apagavam o produto ou o serviço por entrar em conflito de entidade no Omie.

[17/11/2022] [Correção] Nomes de produtos muito grande não estava aparecendo completos quando passávamos o mouse em cima.

[17/11/2022] [Correção] O usuário alegava que os campos do tipo Cliente [Cliente.Distribuidor] e [Cliente.Revenda] redirecionavam para a página de contato, mas que não o faziam depois de um tempo.

[17/11/2022] [Correção] No módulo de Biblioteca, os usuários de perfil não ADM tinham acesso ao botão de excluir itens, mesmo que tal ação não fosse permitida a eles.

[17/11/2022] [Correção] Duplicação de Negócio falhava quando partia de funis onde o formulário do negócio não possuía um campo customizado. O código tentava validar as propriedades customizadas do Negócio, mas não encontrava nenhuma. Foi adicionada uma validação para evitar esse problema.

[17/11/2022] [Correção] O problema ocorria estando na penúltima página de uma tabela e, após remover alguns itens da tabela, tentava-se avançar para a próxima página, se o montante de itens restante alterasse a quantidade total de páginas, esse avanço de página produzia um erro.

[17/11/2022] [Correção] Ao criar um filtro simples para buscar tarefas com alguns usuários, a visualização desses usuários não era exibida como deveria.

[17/11/2022] [Correção] Um fluxo muito específico onde um checklist 'A' de um campo de cliente do negócio era alterado após ser revelado por outro checklist 'B'. Se o checklist 'A', ao ser alterado, alterasse a visualização de outros checklists, todos os valores preenchidos sumiam.

[17/11/2022] [Correção] Campo de [Negócio.Responsável] aparecia sempre vazio em um negócio mesmo que os registros de modificação mostrassem o contrário.

[17/11/2022] [Correção] Ao responder um e-mail enviado por mim mesmo, o campo "para" é preenchido com os mesmos destinatários do e-mail original. Caso seja a ação "responder todos", o campo "CC" é preenchido com as mesmas cópias do e-mail original e "CCO" com as mesmas cópias ocultas.

[17/11/2022] [Correção] Ao duplicar negócio, o campo de valor está sendo zerado após mudar o funil.

[21/11/2022] [Correção] App deslogava ao tentar acessar a entidade negócios que possuía um filtro muito pesado.

[21/11/2022] [Correção] Alguns registros de e-mail estavam duplicando.

[21/11/2022] [Correção] Na integração do Omie, algumas vendas estavam duplicando por conta de um erro no código.

[21/11/2022] [Correção] No app, ao entrar em negócios, estava deslogando o usuário.

[22/11/2022] [Correção] Na integração do omie, algumas informações não estavam sendo sincronizadas corretamente, ao alterar no Ploomes, por exemplo, o Omie encaminhava uma edição com a informação que estava antes da alteração.

[23/11/2022] [Correção] No aplicativo ao clicar em Workflows o usuário era deslogado do App.

[24/11/2022] [Correção] Ao passar o mouse sobre o nome de um marcador, o tooltip com o nome completo estava abaixo da edição inline impossibilitando a visualização.

[24/11/2022] [Correção] O nome da cidade no Ploomes (BIRITIBAMIRIM ) estava divergindo do registro da Receita Federal (BIRITIBA-MIRIM) quando era feita a inscrição do cliente.

[24/11/2022] [Correção] Descrição das tarefas estavam sendo renderizadas sem um atributo CSS que garante a quebra de linha do texto. A correção adicionou esse atributo para formatar o texto conforme o usuário escreveu.

[24/11/2022] [Correção] Usuários inativos no Ploomes eram listados como opções válidas para envio de e-mails na configuração de qualquer automação.

[24/11/2022] [Correção] Campo de endereço do contato em formulário mini obtia o nome da empresa, ao invés do endereço.

[24/11/2022] [Correção] Cidade "Passa Quatro" na Receita Federal estava cadastrada no Ploomes como "Passa-Quatro".

[24/11/2022] [Correção] Ao passar o mouse sobre o nome do marcador como por exemplo para alterá-lo dentro de um funil, a visualização do nome aparecia atrás da janela que mostra o marcador.

[24/11/2022] [Correção] Ao usar o campo de data em fórmula de campo de produto da proposta, o mesmo estava com comportamento inconsistente, apresentando o valor do campo de data ao remover o produto, não ao inserir.

[24/11/2022] [Correção] Não estava sendo possível criar uma formula puxando o estágio da venda.

[24/11/2022] [Correção] Listagem e edição de formulários externos no Ploomes estavam com lentidão quando haviam campos múltiplos com muitas opções listadas nos mesmos.

[24/11/2022] [Correção] Botões de ganhar e perder não apareciam em cards de alguns funis na conta do cliente.

[30/11/2022] [Correção] Não era possível fazer edição de campo de contato [Cliente.Nome] no formulário de negócio.
