---
id: "42427576475927"
titulo: "Atualizações de Junho de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427576475927-Atualiza%C3%A7%C3%B5es-de-Junho-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:54Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_e4cf9e270bad", "ploomes_7973482"]
---

# Atualizações de Junho de 2023

[01/06/2023] [Correção] Corrigido erro "Fail to get user configs", quando o usuário tentava enviar uma proposta via link web.

[01/06/2023] [Correção] Ao inserir um filtro de contém em campos de 'texto multilinha', o conteúdo do texto do filtro sumia após salvado.

[01/06/2023] [Correção] Ao tentar recuperar a senha estava travando o usuário na tela roxa de carregamento do Ploomes devido a um de requisição ao salvar os dados do usuário. Foi corrigido colocando uma tratativa e erro quando a requisição falhar.

[06/06/2023] [Correção] Usuários estavam obtendo erro de ultrapassar limite de criação de automações, mesmo estando abaixo dos limites.

[06/06/2023] [Correção] Não gera resultado em gráficos porque está filtrando por data da última atualização e o front-end não pode permitir esse campo para filtrar.

[12/06/2023] [Correção] Tela de relatórios antigo apresentava lentidão para carregar os gráficos. O Frontend barrava o carregamento de gráficos para uma fila de 3 em 3 em todas as abas, agora está criando uma nova fila quando muda de aba. Fazendo com que gráficos de abas diferentes não barrem o carregamento deles.

[12/06/2023] [Correção] Ao tentar acessar uma conta bloqueada/expirada, estava travando na tela roxa de loading e não tinha nenhuma ação.

[12/06/2023] [Correção] Busca na barra de pesquisa geral não retornava resultados caso uma das consultas desse problema.

[12/06/2023] [Correção] Campos de Negócio adicionados no modelo da proposta não apresentavam seu conteúdo na proposta gerada.

[12/06/2023] [Correção] Ao adicionar produtos do cliente a uma Proposta/Venda através da aba "Dados do Cliente", as fórmulas que dependiam dos campos desses produtos não eram engatilhadas. Foi corrigido para propagar as fórmulas enquanto os produtos são inseridos.

[12/06/2023] [Correção] Em algumas contas, os botões de compartilhamento de documento não estavam executando as ações.

[14/06/2023] [Correção] Valor da proposta aparecia zerado no app quando editado manualmente no web.

[14/06/2023] [Correção] Ao criar negócio pelo APP Ploomes, o título do card ficava com o conteúdo incorreto

[14/06/2023] [Correção] Fórmula do campo [Proposta.Valor] não engatilhava no app, apenas na versão web.

[15/06/2023] [Correção] Modal de cancelamento de importação estava com erro no texto, trazendo a palavra deseja duas vezes. Foi corrigido.

[19/06/2023] [Correção] Relatório beta retornava vazio mesmo que o filtro aplicado em aba de registro de interação retornasse uma quantidade de itens diferente de nulo.

[19/06/2023] [Correção] Relatório beta ficava em looping em um filtro específico do cliente, melhoraram a performance e busca do relatório o que resolveu o problema.

[20/06/2023] [Correção] Contador de tarefas apresenta quantidade de tarefas pendentes incoerente com a real quantidade delas no Ploomes.

[21/06/2023] [Correção] Módulo de clientes, negócios e documentos não carregava os dados no front do Ploomes, devido ao carregamento do cache enviado pelo back que trazia informações de um formulário que não existia mais na conta.

[21/06/2023] [Correção] Ao tentar duplicar um card com um campo de anexo preenchido com um anexo que já foi apagado, o front não apresentava mensagem de erro e se mantinha em um loading infinito.

[21/06/2023] [Correção] Usuário de integração Omie atualizava o valor do pedido de venda após a criação do mesmo.

[21/06/2023] [Correção] Links do PowerBI não estavam aparecendo para copiar.

[21/06/2023] [Correção] Usuários estavam conseguindo mudar a visualização de e-mails de outros usuários sem a permissão deles.

[21/06/2023] [Correção] No aplicativo, ao compartilhar uma proposta via WhatsApp, o campo de telefone do contato vinculado não estava retornando preenchido.

[23/06/2023] [Correção] Na integração Omie utilizamos um serviço de cache para buscar os dados de campos mapeados e outras informações. Algumas informações não estavam vindo do cache.

[26/06/2023] [Correção] Na integração com o Omie alguns campos que estavam zerados não estavam sendo considerados na integração.

[26/06/2023] [Correção] No integração com o Omie era feita uma conversão errada do valor para inteiro no caso dos serviços.

[26/06/2023] [Correção] Importações nos servidores da Europa pararam de funcionar.

[29/06/2023] [Correção] E-mails enviado ao endereço mail.ploomes.com não aparecem na caixa de entrada do Ploomes.
