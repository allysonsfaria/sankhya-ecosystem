---
id: "42427588152343"
titulo: "Atualizações de Agosto de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427588152343-Atualiza%C3%A7%C3%B5es-de-Agosto-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:10Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6445133", "sync_hash_201a87672e6e"]
---

# Atualizações de Agosto de 2022

[02/08/2022] [Correção] Sempre que o campo "Origem" do cliente era feito pela integração com o Spotter com o valor "IC", no Ploomes ele estava sendo registrado como "Indicação (Finder)".

[02/08/2022] [Correção] Quando tentávamos passar o estágio de uma negociação com checklists pendentes aparecia a mensagem 'Existem items obrigatórios no Checklist' e no caso o 'items' estava com M ao invés de N.

[03/08/2022] [Correção] No app estava aparecendo uma mensagem falando que os produtos foram removidos por não se encaixarem nos filtros definidos mesmo tendo produtos que se encaixavam nesse filtro.

[03/08/2022] [Correção] A integração com o Omie estava duplicando as vendas e às vezes até triplicando.

[04/08/2022] [Correção] Não era possível editar o formulário de negócio, já que não era exibido nas configurações de funil, tampouco era possível duplicar o funil na conta do cliente.

[04/08/2022] [Correção] O filtro de horário diferente de vazio não estava filtrando de forma correta.

[05/08/2022] [Correção] Quando os tipos de registro e tarefa eram bloqueados pelo usuário na versão web, elas seguiam sendo exibidos no app, possibilitando a criação delas normalmente.

[05/08/2022] [Correção] No app, não estava salvando a alteração por uma automação que preenchia o campo 'Título'.

[08/08/2022] [Correção] Ao importar uma planilha com números que tinha 3 casas decimais depois da vírgula o Ploomes entendia o valor errado na hora de preencher os campos.

[08/08/2022] [Correção] Formulário externo estava burlando bloqueio de voltar etapa.

[08/08/2022] [Correção] Ao fazer importação de alguns negócios, só subia a informação correta de uma empresa, das outras mapeadas da mesma forma não estava subindo.

[08/08/2022] [Correção] Campo de número inteiro não estava preenchendo no ploomes pelo formulário externo.

[08/08/2022] [Correção] Duplicidade no estado e linhas em branco na importação de clientes ocasionou vários erros de request na API.

[10/08/2022] [Correção] Valor de tabela do produto não estava sendo carregado corretamente na proposta, fazendo com que não fosse possível gerá-la.

[10/08/2022] [Correção] Campo de dados da empresa não era atualizado mesmo com o conteúdo inserido corretamente no (network).

[11/08/2022] [Correção] Formulário de criação de Deal no funil do cliente estava aparecendo em branco, mesmo com a requisição.

[11/08/2022] [Correção] Ao tentar excluir o campo do formulário, um erro era exibido. No entanto, se fosse feito o recarregamento da página, o campo não era exibido.

[11/08/2022] [Correção] Ao realizar a navegação entre automações com alguma delas estando em páginas avançadas, ao voltar pra anterior a mesma não exibia o conteúdo corretamente.

[11/08/2022] [Correção] Campo com edição restrita ficava liberado para perfis que não tinha liberação para editá-lo no app.

[11/08/2022] [Correção] Ao clicar no símbolo da receita federal para trazes os dados do CNPJ, não estava puxando as informações para o ploomes.

[11/08/2022] [Correção] A fórmula do campo de [Proposta do documento.Quantidade] apresentava uma quantidade de itens incorreta.

[11/08/2022] [Correção] Não estava aparecendo todos os formulários para serem mapeados na configuração da integração com o facebook leads.

[11/08/2022] [Correção] Cliente usava um filtro na tabela de produtos para aceitar somente o marcador padrão e tabelado e apenas produtos do cliente. Na lupa de busca funcionava, mas no próprio campo não.

[11/08/2022] [Correção] Com textos muito grandes a visualização com texto multilinha estava quebrando ao abrir a visualização expandida na tabela.

[12/08/2022] [Correção] Requisição para alterar marcadores estava sendo enviada sem o padrão documentado pelo Omie.

[16/08/2022] [Correção] Existiam alguns casos em que o telefone ainda estava sumindo no momento em que se "desintegra" com a receita, clicando no botão novamente. O telefone sumir estava bugando o formulário e fazendo com que fossem criados clientes sem campos obrigatórios preenchidos.

[16/08/2022] [Correção] Ao configurar campos com visualização condicional, a mesma não era respeitada e o campo era exibido para o usuário mesmo não estando configurado para ver.

[16/08/2022] [Correção] Ao abrir a criação de uma proposta em funil com limitação de modelo, a tela ficava carregando infinitamente, pois o usuário não tinha permissão para visualizar nenhum modelo. Foi criado um alerta avisando de que não há modelos de (proposta/documento/venda) disponíveis.

[16/08/2022] [Correção] Estava dando erro ao preencher formulário externo e mesmo assim era criado o negócio do ploomes.

[16/08/2022] [Correção] Estava dando erro ao preencher formulário externo e não estava criando nada no ploomes por conta desse erro.

[16/08/2022] [Correção] No formulário de cadastro de um novo cliente do tipo Empresa, ao fazer integração de dados do CNPJ com a Receita Federal, o campo [Cliente.Telefones] desaparecia.

[16/08/2022] [Correção] O cliente informou que ao acessar a seção de Funis Arquivados e fazer scroll down não era possível visualizar os funis elencados em determinado momento.

[16/08/2022] [Correção] A tela de edição de propostas estava lenta, em comparação a 2 meses atrás.

[16/08/2022] [Correção] O cliente informou que o filtro da seção do Funil 'SAC' não estava lendo como Ou, mas como E.

[16/08/2022] [Correção] Ao inserir produtos com o checkbox 'Proposta.Produto' marcado ou desmarcado, os atributos não ficam alinhados na lista de produtos já adicionados.

[16/08/2022] [Correção] O clientou relatou que ao duplicar um negocio, os checklists não estão sendo preenchidos no negocio filho.

[17/08/2022] [Correção] Ao criar algumas tarefas pelo Outlook, a integração com o Ploomes não conseguia resgatá-las.

[17/08/2022] [Correção] Ao vincular o campo [Proposta.Método de pagamento (Omie)] em um campo de venda, a informação não chegava corretamente no Omie, ia sempre como 'A vista'.

[23/08/2022] [Correção] Compartilhamento via LinkWeb com remetente do email integrado sempre chegava para o destinatário como no reply.

[23/08/2022] [Correção] Após deploy, na visualização em propostas, parâmetros de fórmulas comparativas com valor '0' não estavam funcionando corretamente.

[23/08/2022] [Correção] Importação estava duplicando grupos de produto já existentes mesmo com as configurações corretas.

[24/08/2022] [Correção] A área clicável do hiperlink quando um documento de proposta era convertido para PDF não era do mesmo tamanho da que era apresentada no documento original.

[25/08/2022] [Correção] Estamos enviando requisições adicionais quando da erro no Omie.

[25/08/2022] [Correção] URL do compartilhamento link web estava quebrado.

[26/08/2022] [Correção] Ocorria um erro que não exibia os negócios de um cliente.

[26/08/2022] [Correção] Na inclusão de documentos em negócios, estava apresentando que não haviam modelos e os modelos existentes simultaneamente.

[26/08/2022] [Correção] Remover tipo nas configurações de tarefa não refletia na criação de uma automação, que poderia criar tarefas do tipo removido.

[26/08/2022] [Correção] Tarefas criadas no Google Calendar não refletiam no Ploomes, mas o inverso ocorria normalmente.

[26/08/2022] [Correção] Ao visualizar os registros de interação, um filtro era indevidamente aplicado, onde só era possível removê-lo se fosse recarregada a página.

[26/08/2022] [Correção] Quando o formulário de cliente não possuía o campo "empresa", ao alterar um campo o cliente do tipo filial virava matriz.

[26/08/2022] [Correção] Ao tentar diminuir a coluna de uma tabela no modelo de documento de proposta, que possuía o campo [Produto.Índice], não era possível reduzir para uma largura menor do que o tamanho do texto "[Produto.Índice]".

[26/08/2022] [Correção] O filtro da tabela de produtos não funcionava corretamente, puxando produtos que não deveriam passar nele.
[26/08/2022] [Correção] Ao duplicar um negócio para um outro funil, os valores dos campos que não estavam inseridos no formulário do funil de destino não eram enviados.

[30/08/2022] [Correção] Campo com marcadores não exibia label com o nome completo.

[30/08/2022] [Correção] O campo de data, mesmo vazio, estava retornando para a fórmula um valor padrão com a data de hoje.
