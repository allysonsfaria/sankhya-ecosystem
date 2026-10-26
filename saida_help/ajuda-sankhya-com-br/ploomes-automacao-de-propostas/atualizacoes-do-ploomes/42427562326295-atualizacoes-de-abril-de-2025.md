---
id: "42427562326295"
titulo: "Atualizações de Abril de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427562326295-Atualiza%C3%A7%C3%B5es-de-Abril-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:11Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11047108", "sync_hash_c7b95c9b18eb"]
---

# Atualizações de Abril de 2025

## [01/04/2025] [Correção]

- Ao modificar o código da seção de produtos, o sistema exibirá um alerta informando que essa alteração pode remover produtos de documentos já gerados.

## [02/04/2025] [Correção]

- A tela de logs da integração Sankhya agora exibe todos os eventos nos registros, e a seleção da entidade Sankhya pesquisada passou a ser obrigatória, tanto para exportações quanto para importações. Além disso, o período inicial e final já vem pré-selecionado com a data do dia, facilitando a consulta.

## [03/04/2025] [Correção]

- Havia um erro no funcionamento do filtro de data por intervalo nos relatórios 2.0 (Beta). Por causa disso, o gráfico mostrava uma quantidade incorreta de valores. A equipe de desenvolvimento identificou e corrigiu o problema, e agora os dados exibidos estão corretos.
- O posicionamento do dropdown sempre ficava abaixo do campo, às vezes ele saía da tela. Foi então ajustado para que o dropdown mude de posição caso não caiba na tela.

## [07/04/2025] [Correção]

- Existia um loop no código que estava causando loop de notificações de integração com o Outlook. Esse loop foi removido.

## [08/04/2025] [Correção]

- Agora, quando uma badge aparece dentro da tabela de produtos do documento, ela não ocupará 100% da largura do campo. Em vez disso, seguirá o tamanho adequado ao conteúdo, garantindo uma exibição mais harmoniosa.
- Em contas com integração Sankhya ativa e que possuam consultas de impostos, a fórmula em Produto da Venda responsável pela consulta de impostos não retornava dados ao inserir números decimais no campo de Quantidade.
  A fórmula foi alterada para permitir que quando a Quantidade fosse um número decimal (por exemplo, 0,1 ou 4,3) a consulta aos impostos e alíquotas de ICMS e/ou IPI fossem realizadas sem erro.
- Ao clicar na calculadora do cabeçalho da tabela de opcionais, o esperado é que as fórmulas de todos os opcionais fossem logadas no console, mas isso não estava acontecendo. Agora elas são logadas como esperado. Um problema na ordem dos logs também foi corrigido, tanto para opcionais, quando para produtos.

## [09/04/2025] [Correção]

- Em contas com integração Sankhya ativa, a seção **Exportações** dentro da aba de **Registros do Sankhya** estava com o filtro de data incorreto, realizando a busca na API acrescentando 3 horas no horário atual, por conta do fuso horário. Este filtro foi corrigido para realizar a busca com o horário correto.
- APP - O filtro do campo de opção pré-cadastrada não funcionava em casos específicos, porque os valores usados na fórmula dependiam de valores que já existiam na proposta, por conta disso não eram passados para a sessão, agora eles são carregados corretamente.
- APP - A fórmula de obrigatoriedade não era aplicada corretamente durante a edição de documentos no aplicativo. O problema foi corrigido na versão 6.5.1 do app.

## [10/04/2025] [Correção]

- Devido a uma alteração no backend, o envio do ID da proposta/venda/documento que estava sendo duplicado, fazia com que o duplicado caísse nos fluxos de aprovação do original. Os desenvolvedores corrigiram o problema e agora o ID é removido antes do salvamento de uma proposta/venda/documento duplicado.
- Ao tentar enviar um e-mail, o sistema não estava mostrando sugestões de clientes e usuários com e-mail cadastrado. Corrigimos esse problema adicionando uma verificação para garantir que os dados necessários existam antes de serem usados, evitando o erro que impedia o funcionamento correto da sugestão de e-mails.

## [15/04/2025] [Correção]

- No CPQ Beta, corrigimos um problema que acontecia ao tentar editar um campo de texto com várias linhas em um opcional do produto. Ao clicar na opção "Código Fonte" para editar o conteúdo em HTML, o campo era fechado automaticamente e voltava para a tela anterior, impedindo a edição. Agora, a edição em HTML funciona normalmente, sem fechar o campo de forma inesperada.
- Ao criar um cliente utilizando o formulário mini, o campo "Nome do cliente" não era preenchido automaticamente. Isso ocorria porque o model não estava sendo atualizado com o texto inserido no campo "Cliente".

  Foi aplicada uma correção para que, ao abrir um formulário mini, caso exista texto no campo "Cliente" e o campo "Nome" também esteja disponível, ambos os valores sejam vinculados corretamente.

## [16/04/2025] [Correção]

- Ao inserir um signatário nas integrações de assinatura era possível deixar um espaço entre o .com e o br. A validação foi corrigida para não permitir isso.
- Foi corrigido um problema na api2 que ocorria ao editar um campo do tipo cliente com valor padrão apontando para ele mesmo, o que fazia o fieldPath ser sobrescrito incorretamente. No backend, passou-se a persistir o OriginFieldFieldPathId quando apenas o OriginFieldKey for enviado no PATCH de Fields. Além disso, foi corrigido um erro em uma função executada antes da vinculação dos campos padrão, que impedia essa etapa de ocorrer corretamente.

## [17/04/2025] [Correção]

- Corrigimos a exibição de valores monetários de campos dinâmicos de tipo Moeda em e-mails enviados por automações, que agora mostram corretamente os centavos (casas decimais).
- Corrigimos um erro que causava a remoção de campos no PDF da proposta quando emojis estavam no nome do campo. Isso ocorria devido à forma como os modelos lidavam com emojis usando HTML e CSS. Caso modelos antigos ainda apresentem o problema, atualize os dados da venda ou o modelo da proposta.
- APP - Não havia o tratamento de adicionar o `WonQuoteId` dentro da ação de ganhar um negócio, agora tem.
- APP - A condição para exibição do botão estava errada quando o formulário era de edição, o mesmo acontecia no tratamento dos dados antes de serem enviados para a API resultando no reset do tempo para "00:00", foi adicionado as condições corretas para corrigir o problema.

## [20/04/2025] [Correção]

- APP - Ajuste na abertura do whatsapp no Android devido a uma limitação do sistema. Agora, o redirecionamento para a Play Store ocorre apenas quando o app não está instalado.
- APP - Foi realizada algumas melhorias e correções no campo do tipo 7 (Opções pré-cadastradas).

## [22/04/2025] [Correção]

- Foi feita a correção do código do gerador de html e agora ele possui uma ordenação fixa baseada necessariamente na ordem em que os produtos foram preenchidos no formulário.
- A integração com o RD Station foi ajustada para evitar a criação de empresas duplicadas no Ploomes. Anteriormente, ao identificar um contato já existente, não havia verificação se a empresa correspondente com o mesmo CNPJ já estava cadastrada, o que podia gerar duplicidades. Agora, foi adicionada essa verificação, garantindo que uma nova empresa só será criada se não houver outra com o mesmo CNPJ.
- Agora é possível definir o template de documentos no CPQ Beta por meio de um parâmetro na rota — assim como já era possível no CPQ atual. Essa funcionalidade também foi expandida para propostas e vendas no CPQ Beta.
- Ao duplicar um negócio em que o funil limita os modelos de proposta era possível gerar uma proposta usando qualquer modelo da conta. Agora eles são filtrados também como esperado.
- Foi corrigido um problema no envio de documentos para assinatura pelo LetsSign, que ocorria ao adicionar o e-mail como signatário. Mesmo com erro retornado pela API, o sistema exibia uma mensagem de sucesso e não mostrava falhas ao usuário. Agora, o erro real é corretamente exibido, permitindo identificar quando o envio do documento falhar.
- Ao tentar editar um campo excluído no modelo de documentos, nada acontecia. Agora há um toaster para explicar para o usuário qual o erro.

## [23/04/2025] [Correção]

- Corrigimos um problema que impedia a criação de tarefas pelo botão genérico “+” no primeiro acesso à conta Ploomes. Ao fazer o primeiro login, o usuário era direcionado para a URL `/selfinfo`, que não possuía as rotas necessárias para abrir os modais de criação de tarefa, negócio e outros. As rotas necessárias foram adicionadas, e agora a funcionalidade está disponível normalmente.

## [24/04/2025] [Correção]

- Corrigido um problema onde retornos de fórmula Excel preenchiam o campo incorretamente em algumas instâncias
- No app, o tratamento de certos valores dentro da conversão de proposta para venda estava quebrando, foi adicionado mais proteção no tratamento para corrigir o problema.

## [25/04/2025] [Correção]

- Correção de tradução no tooltip da opção "Replicar valores abaixo na meta". Foi corrigido um problema em que o tooltip dessa opção era exibido em português, mesmo quando o idioma do usuário estava configurado como inglês ou espanhol. Agora, as traduções foram adicionadas e o texto será exibido corretamente no idioma selecionado.

## [28/04/2025] [Correção]

- Não estava sendo possível salvar edições no formulário externo devido à ausência da propriedade de cor no payload enviado pelo front-end. A propriedade foi adicionada, resolvendo o problema.
- O limite de 5 MB por arquivo nos formulários externos foi ampliado para 25 MB, atendendo à necessidade de clientes que utilizam arquivos maiores.

  Além disso, a forma de processamento dos arquivos no backend foi atualizada, e o frontend foi ajustado para garantir compatibilidade com essa nova lógica.
