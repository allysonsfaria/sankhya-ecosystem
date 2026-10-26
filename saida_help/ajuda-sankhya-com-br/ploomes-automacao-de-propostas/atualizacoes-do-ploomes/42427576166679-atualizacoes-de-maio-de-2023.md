---
id: "42427576166679"
titulo: "Atualizações de Maio de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427576166679-Atualiza%C3%A7%C3%B5es-de-Maio-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:50Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7879640", "sync_hash_c0edc29abec6"]
---

# Atualizações de Maio de 2023

[02/05/2023] [Correção] Foi alterada a extensão do Whatsapp para obter o número e nome do contato sem a necessidade de abrir o painel de informações do contato.

[02/05/2023] [Correção] Ao gerar o PDF o número do item não a estava aparecendo.

[02/05/2023] [Correção] Ao gerar propostas preenchendo o campo "Desconto" com três dígitos após a vírgula pelo app, ele é arredondado e isso faz com que o valor das propostas fique errado.

[02/05/2023] [Correção] Havia um problema na extensão do Whatsapp em que a requisição para trazer os dados do contato não retornava nada, não possibilitando o cadastro ou visualização das informações do Cliente no Ploomes. A requisição foi corrigida e agora os dados são trazidos corretamente.

[02/05/2023] [Correção] Câmera em campos de imagem/anexo não estava funcionando no app.

[03/05/2023] [Correção] Gerador de PDF estava exibindo campos escondidos.

[04/05/2023] [Correção] Integração com Exact Spotter alterou dados de outro contato da base. /havia um problema na forma que buscávamos o contato no Ploomes para verificar se era atualização ou criação, fazendo com que contatos que viessem sem e-mail do Exact Spotter atualizassem contatos sem e-mail no Ploomes, foi resolvido alterando o filtro que usamos para buscar o cliente no Ploomes.

[06/05/2023] [Correção] Foi adiciona opção de permissão de exportação para o Power Bi nas configurações de perfil de usuário.

[08/05/2023] [Correção] Foi adicionado o caminho Negócio > Cliente > Empresa > (Outros Dados) nos campos.

[08/05/2023] [Correção] Para um usuário específico ao enviar um e-mail por dentro do ploomes, ele aparecia na caixa de enviados sem conteúdo algum, mesmo ele possuindo.
[15/05/2023] [Correção] Ao clicar para acessar a última página do e-mail dentro do Ploomes, a caixa de entrada aparecia vazia, mesmo tendo e-mails.

[15/05/2023] [Correção] Na integração com Clicksign, clientes que tivessem o carácter '/' no nome não estavam recebendo o documento assinado

[16/05/2023] [Correção] Os campos de data "Data de Início do Agendamento" e "Data de Fim do Agendamento" na integração com o Exact Spotter (versão nova) retornavam os valores com o fuso horário incorreto e isso fazia com que campos de data e horário fossem inseridos no Ploomes com valores incorretos. Esses valores passaram a ser convertidos para o fuso horário correto antes dos valores serem inseridos no Ploomes.

[17/05/2023] [Correção] Ao carregar a aba 'Mining e Metals', o carregamento quebrava, retornando o erro 408 - Query Timeout.

[18/05/2023] [Correção] Usuários não estavam conseguindo criar ou duplicar automações.

[18/05/2023] [Correção] Exportação de aba de negócios para o Power Bi estava puxando informações de outros funis.

[18/05/2023] [Correção] Um usuário criou um negócio cm um responsável inativo de mesmo nome do usuário. Como forma de prevenção o front faz um filtro removendo todos os inativos que passaram pelo back, fazendo uma dupla checagem.

[23/05/2023] [Correção] Campo com edição bloqueada de checklist era alterado após a automação preenchê-lo. Foi propagada a correção para desabilitar a função do botão "Salvar" dos campos de edição bloqueada dos checklists.

[23/05/2023] [Correção] Quando uma requisição de negócio fica muito complexa, o tempo de resposta pode demorar tanto que o backend retorna um erro. Não havia tratamento para esse erro no front, resultando num loading infinito sem feedback para o usuário.

[23/05/2023] [Correção] Não era possível visualizar os e-mails registrados na linha do tempo do negócio, por nenhum usuário.

[23/05/2023] [Correção] Ao tentar anexar arquivo da biblioteca acessando pelo cliente, o Ploomes não retornava nenhum resultado.

[23/05/2023] [Correção] Na tela de cliente o botão "Agendar Tarefa" não aparecia para usuários que não podem editar os clientes. Correção foi propagada para verificar se o usuário tem acesso ao módulo de tarefas e mostrar o botão.

[24/05/2023] [Correção] Foi realizada a remoção do campo de negócio "Equipes colaboradoras" de opções pré-cadastradas porque estava sem funcionalidade e estava sendo exibido por algum equívoco em algumas contas.

[24/05/2023] [Correção] Ao duplicar o modelo de conta pelo Ploomes Partners, dava erro ao tentar duplicar campos que foram deletados.

[24/05/2023] [Correção] Contas criadas pelo duplicador estavam com problema no filtro de contatos da empresa.

[25/05/2023] [Correção] E-mails não estavam chegando ao Ploomes se tivessem mais de 50 mensagens para serem integradas de uma vez.

[25/05/2023] [Correção] Em vez de aparecer no alerta o valor selecionado aparece "Vazio". Corrigido para mostrar o valor selecionado.

[25/05/2023] [Correção] Havia um problema ao adicionar os mesmos campos de Contato e Cliente dentro do assunto do email (por exemplo: [Contato.Nome] e [Cliente.Nome]) por conta de uma validação de duplicidade. A validação foi corrigida para permitir a inserção do campo.

[29/05/2023] [Correção] Exportação de aba de negócios para o Power BI estava dando erro de limite de dados, mesmo estando abaixo do limite.

[30/05/2023] [Correção] Automações e filtros que aplicavam a comparação de um campo multilinha diferente de vazio não estavam funcionando.

[31/05/2023] [Correção] Ao criar um negócio dentro da tela do cliente, o campo cliente vinha vazio no modal que abre da criação do negócio.

[31/05/2023] [Correção] O campo Website do Omie tinha um tamanho máximo de 60 caracteres, e, portanto, o campo não integrou, fazendo com que o Omie limpasse o conteúdo adicionado no campo pelo cliente no Ploomes.

[31/05/2023] [Correção] Não estava sendo possível realizar o mapeamento dos campos da integração do Facebook Lead Ads. Foi identificado na conta do cliente um erro para autorizar a integração e exibir os mapeamentos, relacionado à possibilidade de um usuário gerenciar diversas páginas do Facebook, mas não integrar todas. Foi adicionada uma verificação para tentar integrar apenas as contas marcadas durante a autorização, evitando os erros de permissão que estavam acontecendo.
