---
id: "42427585181079"
titulo: "Atualizações de Outubro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427585181079-Atualiza%C3%A7%C3%B5es-de-Outubro-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:37Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9948000", "sync_hash_3c5408645799"]
---

# Atualizações de Outubro de 2024

## [01/10/2024] [Correção]

- No modal de novo grupo/família há um slide lateral que permite criar produto/grupo. O formulário de criação quebrava caso houvesse uma seção vazia ou mais seções configuradas nos formulários, pois aquele formulário não oferece suporte à elas. Foi feita uma correção para que os campos sejam exibidos corretamente sem as seções.
- A classe que usávamos para interpretar a nota fiscal vinda do Omie estava parametrizada com tipos de dados diferentes, o que impedia o acesso aos dados da nota e, consequentemente, sua importação para o Ploomes. Ajustamos os tipos de dados de acordo com a documentação do Omie, e isso deve resolver o problema.

## [02/10/2024] [Correção]

- Nas configurações de campo, era possível partindo de um campo da entidade produto da proposta/venda/documento usar o caminho Partes > Produto, que não funciona. Este caminho agora não irá mais aparecer para ser configurado.
- Caso um campo de usuário em documentos estivesse configurado para puxar como valor padrão o criador da mesma, um erro acontecia no front. Agora o campo busca corretamente o criador e funciona normalmente.
- Ao enviar um email na tela de cliente e negócio foi adicionado um ícone de campo obrigatório para facilitar o entendimento que o campo é obrigatório antes de clicar em "enviar"
- Ao acessar um modelo de documento, caso houvessem muitos grupos/famílias/marcadores nos filtros dos blocos o front fazia uma request muito pesada para o backend, que às vezes nem mesmo era suportada. Essa requisição foi otimizada, e uma lógica foi implementada para separar em duas ou mais requisições caso haja muitos grupos/famílias/marcadores no filtro.
- As fórmulas não estavam buscando corretamente a informação sobre o 'tipo' do cliente durante as edições de propostas. Os desenvolvedores implementaram uma correção e o problema não ocorre mais.
- Na aplicação de compartilhamento de documentos, ao abrir a página com o HTML de um documento que tivesse muitas imagens, havia um problema na lógica para definir o tamanho nas páginas, fazendo algumas ficarem cortadas de forma intermitente. Agora, há uma lógica melhor para o carregamento para evitar que esse problema aconteça.
- Nos documentos em formato tela, a aba de seleção de produtos de cliente trazia as colunas configuradas no formulário mini, e não na aba de produtos de cliente da tela de clientes, como é no formato modal. Agora o comportamento é o mesmo, trazendo os campos da tela do cliente sempre.
- Ao selecionar uma conversa no whatsapp depois que a lista de mensagens atualiza, os contatos na extensão não são atualizados, a correção atualizou a tecnologia usada para fazer a mudança correta dos itens da lista e apresentar o contato correspondente a mensagem selecionada.
- Na integração com o WhatsApp, o evento que faz o contato atualizar não estava sendo chamado em alguns momentos por falta de precisão no click das mensagens. A correção alterou a forma de pegar a mensagem clicada, fazendo o evento do click pegar sempre a mensagem correta.

## [07/10/2024] [Correção]

- Na integração de e-mail, a Microsoft estava dando timeout para pegar as informações das pastas do usuário. Os desenvolvedores implementaram uma correção e o problema não ocorre mais.

## [08/10/2024] [Correção]

- Não estava sendo possível colocar e-mail como público.

## [09/10/2024] [Correção]

- Ao alterar os usuários da tarefa, a repetição era sempre alterada para 'dias'. Os desenvolvedores implementaram uma correção e o problema não ocorre mais.
- Foram adicionadas as seguintes extensões como permitidas em anexos: .kmz, .kml, .dwg, .gpx, .bak e .fld.

## [10/10/2024] [Correção]

- No aplicativo, ao abrir um checklist de qualquer Negócio a tela ficava em branco e precisava ser reiniciada. Identificamos que o problema no Checklist estava sendo causado por um campo de número inteiro, introduzido em uma atualização anterior, que provocava falhas no sistema. Essa falha foi corrigida na versão 4.11.3 do aplicativo.

## [14/10/2024] [Correção]

- Ao inserir um caractere especial no campo de CNPJ no aplicativo para Android, a máscara de formatação era desconfigurada. Esse problema foi corrigido na versão 5.0.0, garantindo que a máscara funcione corretamente independentemente dos caracteres digitados.
- Em metas, os objetos agora são inicializados de forma padronizada para evitar erros de incompatibilidade de arquitetura.

## [15/10/2024] [Correção]

- Todos os componentes de filtro de campo que possuem a opção "vazio" e "não vazio" estão com um indicativo visual melhor, igual o que há em texto simples e multilinha.

## [18/10/2024] [Correção]

- A API responsável por processar os anexos vindos do Outlook estava com um problema de paralelismo durante os picos do dia. Para resolver o problema, os desenvolvedores adicionaram uma fila para processar as requisições sem ter esse problema de paralelismo.

## [23/10/2024] [Correção]

- Campos mapeados da integração Active Campaign não estavam enviando informações para o Ploomes. Identificamos que o problema foi causado por um erro de digitação no parâmetro, que estava configurado como 'first\_campaing', impedindo a coleta adequada de 'first\_campaign'.

## [24/10/2024] [Correção]

- O fluxo de aprovação poderia passar do tamanho da tela sem nenhuma tratativa, foi adicionado um limite para a altura do modal de fluxo de aprovação no CPQ Beta.
- O fluxo de aprovação permitia que o texto da descrição do alerta vazasse para além do espaço reservado caso o texto não contivesse espaços no CPQ Novo, foi aplicado um tratamento para esses casos.
- Fórmulas dos campos nativos "Desconto" não eram executadas nem apareciam no console no CPQ Novo, agora funcionam normalmente.

## [25/10/2024] [Correção]

- Na aba de vincular e-mails, quando o nome do módulo de negócio for muito grande vai ser reduzido e elipsado e mostra o texto completo no tooltip.

## [28/10/2024] [Correção]

- Agora ao criar uma pasta na biblioteca existe um limite de 200 caracteres no nome. Mesmo via API agora não é retornado mais um erro genérico.
- Em alguns casos do CRUD de tarefas, aparecia dois loaders da criação/edição/exclusão. Agora fizemos um tratamento para aparecer apenas um.

## [29/10/2024] [Correção]

- A aplicação que inicializava a conta nos relatórios beta estava com um problema para verificar se uma entidade possui ou não tarefas agendadas, pois ao consultar diretamente pela chave estrangeira, o valor não existia e retornava como 'falso'. Foi realizado uma correção para que busque diretamente pelo Id da entidade para consultar os valores corretos.
- A visualização da tabela dinâmica estava sendo afetada quando um campo de opções continha valores inválidos (nulos). Agora, esses valores são representados por uma tag vazia, permitindo que a tabela dinâmica seja exibida corretamente. Assim, o usuário pode visualizar e remover as opções com erro, se necessário.
- Alguns webhooks recebidos na integração com o DocuSign não eram devidamente processados, atualizamos o processamento dos webhooks para se adequar ao formato recebido.
