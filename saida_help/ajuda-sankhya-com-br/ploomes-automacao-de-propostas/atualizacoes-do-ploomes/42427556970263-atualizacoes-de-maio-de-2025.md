---
id: "42427556970263"
titulo: "Atualizações de Maio de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427556970263-Atualiza%C3%A7%C3%B5es-de-Maio-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:48Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_8604647a56a4", "ploomes_11205060"]
---

# Atualizações de Maio de 2025

## [05/05/2025] [Correção]

- Havia um erro nos relatórios (versão 3.0) ao tentar mostrar gráficos quando o campo "Negócios derivados" era usado. Isso aconteceu porque o sistema estava buscando uma informação com o nome errado. Em vez de procurar pelo nome correto ("OriginDealId"), ele procurava por outro nome ("DealId"). Por causa disso, os gráficos não funcionavam. O problema foi resolvido ajustando essa informação diretamente no sistema.

## [06/05/2025] [Correção]

- Adicionado scroll na lista de pastas do módulo de e-mails, permitindo a visualização completa quando há muitas pastas. Antes, algumas pastas ficavam inacessíveis por não haver rolagem disponível.
- No aplicativo, foi corrigido um problema no módulo de clientes que impedia a atualização correta da listagem ao trocar de aba no modo offline. A filtragem de contatos não era aplicada conforme o filtro da aba selecionada. Agora, os filtros funcionam corretamente tanto no modo online quanto offline. Correção aplicada na versão 6.6.4 do app.
- Estavam sendo adicionados os caracteres `amp;` a mais quando o caractere `&` é enviado em campo de tipo texto em formulário externo. O backend realiza uma sanitização dos valores recebidos por meio do formulário externo para remover possíveis códigos maliciosos. Durante esse processo, o caractere `&` é convertido para `&amp;`. Para corrigir esse comportamento, implementamos um decodificador de HTML que converte esses caracteres codificados de volta para sua forma original — por exemplo, `&amp;` é convertido novamente em `&`.
- Corrigido um erro que alterava o assunto e removia o e-mail base ao trocar o modelo em uma resposta. Esse comportamento fazia com que a mensagem fosse enviada em uma nova thread, perdendo o contexto da conversa original. Agora, o assunto e o e-mail base são preservados corretamente ao mudar o modelo.
- CPQ Beta não aceitava arrays e objetos como valores válidos para campos de texto. Agora, arrays e objetos são aceitos como valores válidos em campos de texto, sendo convertidos em string previamente.

## [07/05/2025] [Correção]

- Ao enviar uma imagem pelo módulo de chat 'Conversas' do Ploomes, ela aparecia corrompida (ou 'quebrada') para o destinatário. Foi revertida uma implantação que alterou o link dos anexos em geral do sistema e que deixava os anexos inacessíveis dentro do chat.

## [08/05/2025] [Correção]

- Ao editar campos diretamente na tela de propostas, um erro genérico “Tente novamente mais tarde” era exibido quando a falha ocorria devido a um bloqueio por fluxo de aprovação — informação visível apenas na resposta da requisição. Para resolver isso, o modal de aprovação foi adicionado às edições realizadas nas tabelas dinâmicas de Proposta, Venda e Documento, garantindo que o usuário seja informado corretamente e possa seguir com o fluxo adequado.
- Ocorria um erro em que a proposta era alterada, mas a requisição ia sem os produtos. Corrigida a montagem de Payloads para que a criação de entidades do CPQ não sejam criadas com erro.

## [13/05/2025] [Correção]

- Ao criar uma automação de funil que alterava um campo do tipo desenvolvedor, foi identificado um problema: ao modificar o conteúdo do campo e salvar, a interface permanecia na tela de configurações do campo desenvolvedor. Esse comportamento ocorria porque não tinha nada que diferenciasse o ID dos modais, sendo assim, o sideSlide tentava fechar o modal de automação genérica. Para corrigir o problema, o desenvolvedor adicionou um parâmetro para diferenciar os dois modais.
- Foi corrigido um problema na validação dos fluxos de aprovação com mais de um campo que, ao editar o campo na tabela dinâmica de Proposta/Venda/Documentos, exibia um erro genérico em vez de apresentar o modal correspondente. Agora, o modal do fluxo de aprovação é exibido corretamente nesses casos.
- No aplicativo, ao realizar o check-in de uma tarefa de visita salva com a data de 07/05/2025, por exemplo, a data era incorretamente alterada para o dia anterior (06/05/2025). Isso ocorria porque, ao abrir o formulário de check-in, o valor do campo de data era transformado considerando o fuso horário, quando, na verdade deveria apenas ser formatado para exibição. Foi adicionada uma função que impede que a formatação visual da data leve em conta o fuso horário, garantindo que a data exibida permaneça correta. Correção disponível a partir da versão 6.8.1 do aplicativo.
- Quando o campo [Cliente.Empresa] era preenchido com valor padrão, o formulário de edição de clientes quebrava, gerando um looping de requisições e em alguns casos impossibilitava o preenchimento de alguns campos. A recursividade foi removida, deixando apenas as chamadas das requisições necessárias.
- No app, quando o campo era triggado pelo OriginField não havia uma validação para se esse OriginField deveria ou não também triggar as outras fórmulas e isso estava fazendo o Valor triggar a fórmula interna que usava o valor antigo. Foi feita uma validação que não trigga caso o campo Origin não esteja entre os FormulaVariables.

## [14/05/2025] [Correção]

- Ao pesquisar um produto para adicioná-lo como vínculo na tela do produto, a busca não era realizada ao utilizar o scroll do mouse ou ao pressionar a tecla "Enter". Foi corrigido um problema no código que causava uma falha na requisição de produtos durante a inserção de opcionais. Agora, ao inserir o produto, a requisição é executada corretamente para buscá-lo.
- Foi adicionado no CPQ Beta alguns campos fixos no formulário de documento. Como, por exemplo, o campo de "Título".
- Campos multilinha não exibiam dados de DecimalValue vindos de fórmulas Excel no CPQ Legado. Ao preencher um campo multilinha com um DecimalValue vindo de uma fórmula excel, o tinyMCE removia o valor por não ser uma string. Agora o valor é convertido para garantir compatibilidade.
- O ícone de fórmulas era exibido nos campos mesmo que o formulário não permitisse a execução de fórmulas. Agora ele só irá aparecer nos forms que permitem.

## [15/05/2025] [Correção]

- Corrigimos um problema que impedia a exibição correta dos negócios ao tentar vincular um e-mail a outro cliente. A falha foi causada por uma alteração anterior na interface, que acabou afetando o filtro de negócios. Agora, ao selecionar um cliente, os negócios relacionados a ele são exibidos corretamente.

## [20/05/2025] [Correção]

- Quando não havia o mapeamento do campo de telefones de Clientes na integração do RD Station, estava sendo atribuído uma lista vazia que sobrescrevia os telefones salvos anteriormente no Ploomes. Foi adicionada uma validação para evitar que os dados de telefone continuem sendo sobrescritos.

## [22/05/2025] [Correção]

- Corrigimos o comportamento da duplicação de negócios no CPQ Beta. Antes, ao duplicar um negócio, o sistema abria automaticamente o mesmo modelo de documento do original, sem exibir a tela de seleção de templates. Agora, assim como no CPQ atual, a tela de seleção é exibida também na duplicação, garantindo uma experiência consistente tanto na criação quanto na duplicação de documentos.
- O campo de unidade de medida da integração com o Sankhya não estava sendo preenchido corretamente no CPQ Beta, devido a uma variável que não recebia valor. Esse comportamento foi corrigido em outra tarefa, que ajustou o tratamento de valores em fórmulas integradas — anteriormente, quando o JSONPath configurado não encontrava nenhum valor, o retorno era tratado de forma incorreta. Após essa correção, o campo de unidade de medida voltou a carregar corretamente o valor padrão da proposta ao criar uma venda.
- No CPQ beta, no formulário de novo negócio e nova proposta, informações preenchidas no negócio não refletiam na proposta após alterar o modelo. Esse comportamento foi corrigido.
- No CPQ beta, quando o Json path em uma fórmula integrada não era encontrado, era atribuído o valor false ao campo. O comportamento foi corrigido e agora o campo não é preenchido.
- No CPQ beta estava ocorrendo um erro ao criar negócio + proposta sem produtos inseridos quando o funil não tem o campo de criador do negócio. Agora com a correção, quando o criador do negócio estiver vazio, ele é preenchido com o criador da proposta.
- App - estávamos com um erro no tratamento de notificação de comentários, onde sempre tentava levar pra um registro de interação ou tarefa e acabava não funcionando para propostas e afins. Sendo assim, os desenvolvedores fizeram uma correção na lógica para que a navegação funcione corretamente.
- No aplicativo, o campo [Produto da proposta .Controle produto (Sankhya)] apresentava lentidão ao exibir as opções, ao inserir um produto na proposta.

  Esse problema foi causado por uma atualização recente, realizada para corrigir outro chamado, que acabou gerando um efeito colateral inesperado.

  Realizamos ajustes na função responsável pelo carregamento das fórmulas, adicionando condições que evitam bloquear fórmulas que precisam ser executadas corretamente. Correção aplicada na versão 6.9.0 do aplicativo.
- Identificamos que, em contas com a integração Sankhya ativa, consultas em tempo real estavam sendo disparadas indevidamente ao abrir a edição de uma venda no CPQ Beta. Isso fazia com que o campo "Dev" fosse recalculado mesmo durante edições, o que não era o comportamento esperado. O problema foi corrigido e, a partir de agora, o cálculo do campo "Dev" será realizado apenas durante a criação da venda, conforme o funcionamento previsto.
- Mobile: Campos de template não estavam sendo colocados automaticamente em vendas e documentos que não tem o campo assim como é feito em propostas. Isso causava um problema na hora de rodar fórmulas que usam variáveis de template e o formulário não abria, impedindo a criação das vendas. Foram adicionados via hardcode os campos para vendas e documentos assim como ja estava sendo feito em propostas.
- Mobile:
