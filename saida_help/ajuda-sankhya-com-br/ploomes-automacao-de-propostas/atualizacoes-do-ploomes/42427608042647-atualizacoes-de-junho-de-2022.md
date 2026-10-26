---
id: "42427608042647"
titulo: "Atualizações de Junho de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427608042647-Atualiza%C3%A7%C3%B5es-de-Junho-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:55Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6295155", "sync_hash_d545046c03ce"]
---

# Atualizações de Junho de 2022

- [03/06/2022] [Correção] No IOS quando a assinatura de um documento era muito grande retornava um erro impossibilitando o salvamento.
- [03/06/2022] [Correção] Para alguns usuários, o número de notificações de tarefas estava divergente do real número que deviria mostrar.
- [03/06/2022] [Correção] No app, quando apertávamos mais de uma vez para salvar a criação de um negócio devido à internet estar lenta, ocasionava a criação de 2 negócios duplicados em alguns casos.
- [03/06/2022] [Correção] Erros na criação offline do app, em alguns casos quando o usuário criava um cliente/negocio/tarefa e depois ficava on-line, essa criação entrava na fila de criação novamente, ocasionando um looping e criando várias coisas repetidas.
- [03/06/2022] [Correção] Ao realizar a alteração de horário em uma das etapas do checklist (salvando em seguida), e preencher o horário de outra etapa do checklist, o primeiro é alterado automaticamente.
- [08/06/2022] [Correção] Ao trocar de idioma o texto era lido como código e não era traduzido, após validação, corrigiram o problema e está traduzindo normalmente.
- [08/06/2022] [Correção] Ao duplicar uma automação genérica que tinha como umas das ações enviar um e-mail, se tivesse algum campo no assunto deste e-mail ele não reconhecia como campo, e no e-mail aparecia por exemplo [Cliente.Nome] ao invés de puxar o valor do nome do cliente.
- [08/06/2022] [Correção] Campos do tipo 'Data' ao serem editados o calendário que ele retorna estava ficando atrás do modal os dias das 2 últimas semanas, impossibilitando a marcação desses dias.
- [08/06/2022] [Correção] A limitação de visualização de uma sessão no Ploomes não estava ocorrendo, e por conta disso usuários que não tinha permissão para visualização estavam conseguindo visualizar.
- [08/06/2022] [Correção] As opções dos campos de opções pré-cadastradas estavam aparecendo por baixo do modal de edição, impossibilitando o usuário de selecionar alguns itens.
- [08/06/2022] [Correção] Fluxo de aprovação não executa na criação.
- [08/06/2022] [Correção] A aba "Empresas" estava sendo exportado porém o campo não.
- [08/06/2022] [Correção] Ao tentar exportar dados de produto da proposta, o erro 500 era exibido para o cliente.
- [09/06/2022] [Correção] As tarefas que vinham do Outlook para o Ploomes estavam com um limite de 255 caracteres na sua descrição.
- [09/06/2022] [Correção] Ao criar uma tarefa através de um negócio, a integração com o Outlook estava duplicando essa tarefa no Ploomes.
- [10/06/2022] [Correção] Campos de Conta corrente padrão (vendas) e Categoria padrão (vendas) são obrigatórios para vinculação inicial e não estavam sendo apresentados em uma nova integração do Omie antes de clicar em atualizar a integração.
- [10/06/2022] [Correção] Alguns usuários estavam recebendo diversas notificações de finalização de tarefas do outlook, indevidamente.
- [15/06/2022] [Correção] O campo de 'País' e 'Estado' não apareciam no formulário Mini de criação de Clientes, por isso algumas informações não podiam ser acessadas.
- [15/06/2022] [Correção] Existia um problema na relação entre os campos de 'Produto' com campos de documentos.
- [15/06/2022] [Correção] Não estava sendo permitido editar o campo 'Cidade' em edições/revisões de propostas/documentos.
- [15/06/2022] [Correção] Alguns clientes quando duplicavam uma proposta por dentro de um negócio, a mesma não respeitava o padrão de tela cheia definido na configuração.
- [15/06/2022] [Correção] O filtro 'Último negócio', para pessoas físicas não estava filtrando de forma correta e trazia alguns clientes com negociação.
- [15/06/2022] [Correção] Em uma configuração específica, opcionais estavam sendo erroneamente duplicados na transição de proposta para venda.
- [17/06/2022] [Correção] Uma mensagem de erro era disparada assim que tentasse salvar as alterações de dados devido a uma limitação de caracteres de um campo de cliente, já que o limite de caracteres do campo por onde se desejava alterar os dados era de 350.
- [17/06/2022] [Correção] Notificações de tarefas finalizadas estavam sendo duplicadas.
- [20/06/2022] [Correção] Alguns campos de venda no app não estavam sendo engatilhados igual na web.
- [20/06/2022] [Correção] Um campo de produto da venda não estava aparecendo no app, quando engatilhado.
- [20/06/2022] [Correção] Na criação de algumas propostas no app, o campo 'Responsável' estava sendo vinculado automaticamente, comportamento divergente da web.
- [23/06/2022] [Correção] Integração com Econodata estava com problemas para enviar clientes para o ploomes.
- [23/06/2022] [Correção] Ao selecionar o país como a dimensão de um relatório, estava aparecendo a sigla ISO ao invés do nome do país.
- [23/06/2022] [Correção] Em modelos de documento, o bloco "Assinatura simples" não estava funcionando corretamente.
- [23/06/2022] [Correção] Quando o ploomes estava com o idioma em inglês, ao criar um novo campo, ao invés de "Integer number" estava escrito "Whole number" em uma tradução direta e incorreta.
- [28/06/2022] [Correção] Ao clicar em salvar uma nova proposta, o alerta de erro no formulário estava desalinhado e fora do padrão das outras telas.
- [28/06/2022] [Correção] Ao editar algum documento abria a tela de edição pequena, mesmo com a configuração de tela cheia ativada na conta.
- [29/06/2022] [Correção] Ao criar uma meta separada por equipe, não estava sendo possível verificar a contribuição de cada equipe.
- [29/06/2022] [Correção] Devido à configuração do campo multilinha, as opções de edição dos campos do formulário de produto não apareciam.
- [29/06/2022] [Correção] Em um funil com a opção de gerar venda ao ganhar negocio não estava funcionando corretamente, em alguns casos não gerava a venda.
- [29/06/2022] [Correção] O filtro que fazem para ordenar coluna 'Cliente de Proposta' não está colocando Contact entre Quote e Name, dando erro OData
- [30/06/2022] [Correção] Ao criar contas testes, funis não estavam exibindo as etapas e nem as opções para editá-las
