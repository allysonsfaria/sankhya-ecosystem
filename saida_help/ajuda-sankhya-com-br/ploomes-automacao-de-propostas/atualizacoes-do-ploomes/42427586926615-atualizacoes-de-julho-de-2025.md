---
id: "42427586926615"
titulo: "Atualizações de Julho de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427586926615-Atualiza%C3%A7%C3%B5es-de-Julho-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:56Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11699004", "sync_hash_e62c579f5630"]
---

# Atualizações de Julho de 2025

## [01/07/2025] [Correção]

- Identificamos que o erro 500 ao trocar o responsável do cliente estava sendo causado por uma configuração incorreta nas triggers (gatilhos) do banco de dados. Fizemos um ajuste nos filtros dessas triggers, adicionando a verificação do ID da conta (accountId), o que garantiu que elas atuem apenas nos dados corretos. Com isso, o problema foi resolvido.
- Foi corrigido um problema em que, ao ocorrer um erro relacionado ao envio de e-mails — mas que não era gerado diretamente pela automação em si —, o e-mail de notificação era enviado com a mensagem e o motivo em branco. Agora, nesses casos em que a automação não retorna um erro explícito, será exibida uma mensagem padrão informando que houve uma falha na autorização do e-mail do remetente. Caso o erro persista, o cliente será orientado a entrar em contato com o suporte.
- Na integração com o Docusign os documentos não estavam ficando salvos no cliente após a finalização das assinaturas. Identificamos que o problema ao realizar o download dos documentos foi causado por uma intermitência na API do DocuSign. Para mitigar esse tipo de situação, implementamos uma lógica de retry (tentativas automáticas de repetição) para realizar o download do documento, evitando que esse erro ocorra novamente.
- Corrigimos um problema na integração com o RD Station que impedia o preenchimento do campo "Origem do cliente" ao importar leads para o Ploomes. Isso acontecia porque, em alguns casos, os dados retornavam nulos e não havia uma tratativa adequada para lidar com essa situação. Agora, a tratativa necessária foi aplicada garantindo que o campo seja preenchido corretamente.
- Na integração com o Clicksign, identificamos que, em alguns casos, o documento assinado não estava sendo anexado automaticamente na aba Anexos do cliente, devido a uma falha ao tentar baixar o arquivo na Clicksign. Para evitar que isso volte a acontecer, implementamos mecanismos que repetem a tentativa de download automaticamente, como medida preventiva para garantir que o documento seja obtido com sucesso e anexado corretamente.

## [02/07/2025] [Correção]

- Não estava sendo possível tornar alguns e-mails públicos, pois o sistema não conseguia identificar o e-mail de origem da thread. Esse e-mail de origem poderia ter sido excluído ou não, e, por isso, o remetente não era localizado corretamente. Como consequência, a inserção do registro de interação falhava. Para solucionar o problema, os desenvolvedores implementaram uma consulta com verificação null-safe, de forma que, caso o e-mail de origem não seja encontrado, o sistema utiliza o remetente do e-mail em questão.
- Ao criar uma venda, o campo de responsável não estava sendo preenchido corretamente com o valor padrão. Isso ocorria porque o sistema buscava esse valor com base no nome do usuário, e como havia duas usuárias com o mesmo nome na conta, ele acabava selecionando a primeira usuária cadastrada. Fizemos um ajuste nesse comportamento e, agora, o responsável é definido corretamente ao abrir o formulário de venda.
- O botão de expandir no campo multilinha da tabela dinâmica de produtos só era exibido para usuários com permissão de edição de produtos. Ajustamos esse comportamento, e agora o botão será exibido independentemente da permissão de edição de produtos, permitindo assim a visualização completa das informações do campo de texto multilinha.
- Foram corrigidos os links da Neppo que estavam vindo com espaço na frente, o que fazia com que as imagens não carregassem.

## [03/07/2025] [Correção]

- Após uma atualização de segurança, o envio de imagens no chat parou de funcionar porque o sistema deixou de reconhecer corretamente a autorização necessária para exibir as imagens. Foi ajustada a forma como essas imagens são carregadas, garantindo que a autorização seja enviada de maneira segura e garantindo a exibição das imagens.
- Adição de um retry em caso de erro retornado pela Microsoft no get de attachments.
- Imagens de alta resolução adicionadas em campos de imagem de propostas pelo aplicativo estavam sendo exibidas com qualidade inferior em comparação à mesma imagem inserida pela plataforma web. Identificamos que a biblioteca responsável por importar imagens da galeria no aplicativo não estava configurada para manter a qualidade máxima. Ajustamos essa configuração para garantir que as imagens agora sejam carregadas com a melhor resolução possível. Correção aplicada na versão 7.1.1 do App.

## [04/07/2025] [Correção]

- Nos relatórios, a coluna Id sempre é retornada na requisição feita ao abrir o Drilldown; no entanto, o front-end a esconde. O problema era que, em alguns idiomas, como o espanhol, por exemplo, o back-end retornava a coluna como Identificacion, e o front-end entendia que ela deveria ser exibida. O desenvolvedor corrigiu para que o back-end retorne sempre como Id, permitindo que o front-end continue escondendo a coluna corretamente.
- Estava ocorrendo erro nas exportações de aba para PowerBI. O erro na exportação ocorria quando era usado o parâmetro 'preload' na consulta para buscar os dados na API2. Foi adicionado o 'order by' requirido para as consultas que usam o parâmetro 'preload' feitas pelo exportador para corrigir o erro.

## [07/07/2025] [Correção]

- No CPQ Beta, foi corrigido um problema em que a ordenação dos produtos não era mantida corretamente em todos os pontos do sistema, fazendo com que voltasse ao estado anterior em algumas situações. Agora, ao reordenar um produto, a nova ordem é aplicada de forma consistente e permanece correta.
- Identificamos que os campos com fórmulas não estavam sendo calculados corretamente no aplicativo, embora funcionassem normalmente na versão web. Correção aplicada na versão 7.1.1 do App.

## [08/07/2025] [Correção]

- APP – Corrigido um erro que impedia a criação de clientes diretamente pelo formulário de Check-In. Com a correção, agora é possível cadastrar clientes normalmente por esse fluxo.
- APP - Corrigido um erro em que fórmula usando campo do Funil não deixava o formulário terminar de carregar gerando load infinito.

## [10/07/2025] [Correção]

- Identificamos que, ao criar uma nova pasta na Biblioteca e atualizar a página, o menu lateral exibia múltiplas pastas com o nome “Nova Pasta”. Isso ocorria devido a um filtro incorreto na requisição de listagem, que fazia com que o sistema retornasse pastas repetidas. Realizamos o ajuste necessário nesse filtro e, agora, apenas a pasta criada é exibida corretamente após a atualização da página, sem duplicações.

## [11/07/2025] [Correção]

- Agora, ao clicar em um arquivo .PDF, o download será iniciado automaticamente. Já os arquivos .PNG e .JPEG serão abertos no navegador para visualização.
- Em relatórios, os casos de tabelas com mês estava pegando a ordenação padrão, usada para datas normais. Para corrigir o problema, o desenvolvedor criou um tratamento especifico para ordenar datas de meses.

## [14/07/2025] [Correção]

- Ao editar em massa tarefas que foram criadas sem horário definido, o horário era atualizado corretamente na visualização de tabela, mas não aparecia ao abrir a tarefa. Isso ocorria porque uma propriedade de exibição no sistema não era atualizada com o campo de horário. Corrigimos esse comportamento para que o horário seja exibido corretamente tanto na tabela quanto dentro da tarefa, garantindo mais consistência e clareza nas informações.
- Havia um problema que impedia a alteração do tipo de tarefa. Isso acontecia porque o sistema enviava uma informação desatualizada na requisição, o que gerava um erro de CORS (falha de comunicação entre sistemas). A equipe de desenvolvimento corrigiu essa informação, e agora a troca de tipo de tarefa funciona normalmente.
- APP - A propriedade CreatorId não estava sendo inicializada corretamente ao criar novo documento no app, causando bugs em fórmulas que tivessem relação com esse valor. Sendo assim, os desenvolvedores implementaram uma correção para carregar a propriedade ao criar um novo documento.

## [15/07/2025] [Correção]

- Não existia implementação para esconder o cliente no card de negócio. Sendo assim, o que o desenvolvedor fez foi adicionar um tratamento para esconder o nome do cliente no card quando não se tem permissão ao módulo.
- Foi corrigido um problema que impedia a exportação de algumas abas para o Power BI, que apresentavam a mensagem "Erro ao atualizar" e, ao acessar as configurações da aba, exibiam o aviso de que a exportação já estava em andamento. A falha era causada por duas situações: queries OData com estrutura incorreta e ausência de validação para valores nulos. As queries foram ajustadas e a verificação de valores nulos foi implementada, permitindo que as exportações voltassem a funcionar normalmente.
- Quando o cliente do negócio também estava no campo 'Contatos relacionados' e haviam múltiplos contatos relacionados, o seletor de funil na página de cliente estava contando o negócio mais de uma vez. Os desenvolvedores implementaram uma correção e agora a contagem foi atualizada para evitar duplicação.

## [17/07/2025] [Correção]

- Em e-mails havia uma inconsistência/intermitência no salvamento de anexos e imagens, que estava relacionado ao uso do semáforo no processo. O que o desenvolvedor fez foi remover o semáforo para resolver essa instabilidade.
- Em algumas situações, os cards estavam pulando estágios. Isso acontecia porque a atualização não reconhecia que o estágio havia sido alterado em todos os pontos necessários. Visualmente parecia correto, mas, internamente, a informação estava inconsistente. Para resolver o problema, o desenvolvedor ajustou o fluxo de atualização para garantir que o estágio seja corretamente refletido em todos os locais que o utilizam.
- Campos de formulário às vezes vinham vazios do cache, o que fazia com que aparecessem vazios durante a edição, apesar de estarem preenchidos na entidade. Foi criado um código preventivo que evita com que erros assim impossibilitem a usabilidade, apenas ignorando o que não vier corretamente.

## [21/07/2025] [Correção]

- Identificamos que a fila de integração com o RD Station estava travada devido a um tempo limite (timeout) configurado no Redis, que é a ferramenta que gerencia temporariamente essas informações. Esse tempo limite estava impedindo que novas integrações fossem processadas, causando acúmulo na fila. Ajustamos essa configuração, removendo o timeout, e com isso a fila voltou a ser processada normalmente.

## [22/07/2025] [Correção]

- Os valores de checkbox não eram tratados corretamente nos registros de modificação, voltando como "Sim" mesmo quando o changelog mostrava "false". O que o desenvolvedor fez foi alterar a lógica para comportar todos os valores, "--" para vazio, "Sim" para "true" e "Não" para "false".

## [23/07/2025] [Correção]

- Corrigimos um problema em que o signatário, ao receber o e-mail do DocuSign, era direcionado para editar o documento em vez de assinar. Isso ocorria porque o valor padrão do campo de assinatura estava sendo salvo sem as barras necessárias. A partir de agora, as barras são adicionadas corretamente durante a configuração. Para que a correção seja aplicada, é necessário salvar novamente os campos de assinatura nos modelos afetados.

## [25/07/2025] [Correção]

- Não estava sendo possível ativar a integração com o Econodata, retornando erro. Foi identificado que uma informação nova adicionada na configuração das integrações estava causando um erro e impedindo o funcionamento correto. O time de desenvolvimento fez os ajustes necessários para corrigir e permitir a ativação da integração.
- No aplicativo foi corrigido um problema que impedia a seleção das abas de clientes em dispositivos Android. A falha acontecia porque o toque não era reconhecido ao tentar trocar para a aba de contatos. A correção já está disponível na versão 7.1.7 do aplicativo.

## [29/07/2025] [Correção]

- Identificamos que, ao selecionar filtros com data relativa (como “Últimos N dias” ou “Próximos N dias”) nos relatórios 3.0, era exibido um campo para inserir uma data fixa em vez de um campo numérico para definir a quantidade de dias, semanas ou meses desejada. Isso ocorria porque as propriedades do campo de data fixa estavam sendo reutilizadas incorretamente no campo de data relativa. Ajustamos esse comportamento separando as propriedades de cada tipo de input. Agora, o campo de data relativa possui sua própria configuração, garantindo que os filtros exibam o tipo de input correto conforme o contexto selecionado.
- Foi corrigido um erro que impedia o administrador de adicionar usuários no painel de relatórios V3 ao utilizar a opção de permissão para "Um ou mais usuários". Nessa situação, era retornado o erro 500 Internal Server Error. O problema acontecia porque o sistema tentava converter um identificador de usuário (armazenado no banco em um formato maior – 64 bits) para um tipo menor (32 bits), o que causava um erro interno na aplicação. A correção foi feita ajustando a consulta ao banco de dados para desconsiderar esse identificador na leitura, já que ele não é utilizado pela aplicação. Com isso, o erro deixou de ocorrer.
