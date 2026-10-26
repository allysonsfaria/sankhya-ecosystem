---
id: "42427578688151"
titulo: "Atualizações de Setembro de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427578688151-Atualiza%C3%A7%C3%B5es-de-Setembro-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:17Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6531673", "sync_hash_a0161ea1e4a6"]
---

# Atualizações de Setembro de 2022

[02/09/2022] [Correção] Não era possível editar o campo 'Disparar pelo E-mail' quando se desejava compartilhar uma proposta utilizando um link web.

[02/09/2022] [Correção] Quando a proposta tinha mais de 20 itens, e estava no modo tela cheia ela não carregava para gerar a venda.

[02/09/2022] [Correção] Um filtro simples aplicado a um funil puxava os campos de outro funil que havia sido selecionado anteriormente.

[02/09/2022] [Correção] Ao adicionar um cliente no formulário de Novo Negócio , um espaço em branco era exibido, deslocando o campo de [Negócio.Cliente] para a direita.

[02/09/2022] [Correção] Estava sendo ignorado a obrigatoriedade do campo de endereço mesmo estando configurado, permitindo a criação de clientes com esse campo vazio.

[02/09/2022] [Correção] Estava dando erro na importação de arquivos para a biblioteca pois esses arquivos ultrapassavam o limite de tamanho, ajustamos esse limite para 25mb.

[02/09/2022] [Correção] Mesmo após excluir uma pasta, era possível ter acesso a ela quando se fazia uma consulta pela API.

[06/09/2022] [Correção] Texto padrão do bloco de opcionais não trazia o product-part-code, por isso não aparecia a opção de "exibir tabela de vínculos".

[06/09/2022] [Correção] Importação com texto simples de nome de produto com mais de 200 caracteres dava erro, não importava, e não aparecia o erro.

[07/09/2022] [Correção] As automações configuradas em um estágio de um funil mudavam para outro estágio ao duplicá-lo.

[07/09/2022] [Correção] Quando o checklist, com um campo de opções pre-cadastradas, estava com a condição para avanço uma das opções como "diferente", se o campo estivesse em branco deveria estar liberado para seguir, mas isso não estava ocorrendo.

[07/09/2022] [Correção] Campo Data.Documento mesmo sendo inserida, ao gerar o documento o campo puxava a data do dia atual, apenas obedecendo quando inserida manualmente na edição do documento após a criação.

[07/09/2022] [Correção] Condicional não respeita condição aplicada no código-fonte do modelo de documento de proposta.

[08/09/2022] [Correção] O campo [Cliente.Razão social] tinha seu valor alterado para 0 ao final do cadastro de uma nova empresa.

[08/09/2022] [Correção] Erro ao aplicar não lido em E-mail, quando havia filtros.

[13/09/2022] [Correção] Os webhooks de clientes recém migrados para o shard 5 não estavam subindo corretamente.

[13/09/2022] [Correção] Mensagem de erro exibida na planilha ao final da importação e, mesmo assim, a importação era feita normalmente.

[15/09/2022] [Correção] No app, um determinado usuário estava criando diversos cards automaticamente ao logar.

[16/09/2022] [Correção] No app, quando um usuário tentava acessar um funil, era deslogado da conta, tendo que refazer o acesso.

[19/09/2022] [Correção] No app, quando um usuário preenchia um checklist de um negócio, ao salvar, o usuário era deslogado da conta, tendo que refazer o acesso.

[19/09/2022] [Correção] Ao preencher o campo de CEP, o autocomplete do campo de endereço não preenchia o campo automaticamente sem você clicar na tela.

[19/09/2022] [Correção] Os campos [Cliente.Estado] e [Cliente.País] apareciam indevidamente ao selecionar uma opção pré-cadastrada, cujo filtro aplicado não dava indícios das condições inseridas nele trazerem ambos os campos.

[19/09/2022] [Correção] Não estava sendo possível mover cards para outro estágio manualmente.

[19/09/2022] [Correção] Seção com campo de produtos do cliente estava filtrando incorretamente os produtos do campo.

[19/09/2022] [Correção] Campos dinâmicos de texto simples ou multilinha que usavam filtros igual à vazio estavam com filtro incorreto no código, impossibilitando a filtragem correta.

[19/09/2022] [Correção] O campo de endereço estava abrindo a lista para edição mesmo estando bloqueado.

[19/09/2022] [Correção] Ao abrir uma seção da proposta, a aba acabava quebrando e travando, tendo que reiniciar ou fechar.

[19/09/2022] [Correção] O campo de telefone quando estava respeitando fórmula de bloqueio quando não deveria, agora respeita apenas o "bloquear edição por padrão".

[19/09/2022] [Correção] Ao acessar os logs de modificação no Ploomes, as linhas que exibiam as atualizações apareciam em um lugar diferente do esperado.

[20/09/2022] [Correção] Compartilhamento LinkWeb estava impossibilitando a alteração de modelo personalizado.

[20/09/2022] [Correção] Fórmula de subtração em entidade de produto de cliente apagava o valor.

[21/09/2022] [Correção] O campo "Aviso" de proposta deveria aparecer somente quando a proposta era inválida, mas no app ele aparecia mesmo para uma proposta válida.

[21/09/2022] [Correção] Título alterado do pdf era ignorado na criação e utilizava o título padrão.

[21/09/2022] [Correção] Campo [Proposta.Ordem de Compra] possuía uma fórmula de bloqueio de edição, que funcionava corretamente no web, mas no app apresentava erros.

[21/09/2022] [Correção] No servidor da Europa, as importações não estavam funcionando, carregando infinitamente sem sucesso.

[21/09/2022] [Correção] Ao logar, o usuário ficava numa tela branca com uma mensagem "{HOME.DASHBOARD translate}" que era um erro do código que quebrava a visualização.

[22/09/2022] [Correção] Os horários das tarefas estavam sendo alterados para 00:00 ao fazer uma edição no campo de data via tabela dinâmica de tarefas ou então via edição em massa.

[26/09/2022] [Correção] Algumas vendas não eram integradas ao zapier na primeira tentativa, precisava engatilhar duas ou três vezes para subir.

[26/09/2022] [Correção] Bug fazia com que quebrasse o layout não permitindo a edição de cliente da tarefa.

[28/09/2022] [Correção] A vinculação de e-mails à clientes cadastrados na conta não estava funcionando como deveria.

[29/09/2022] [Correção] Tarefas após integrar no Ploomes e ter o cliente ou tipo inserido, no Outlook o horário da tarefa ficava incorreto.
