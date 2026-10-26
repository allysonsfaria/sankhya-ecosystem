---
id: "42427559435031"
titulo: "Atualizações de Março de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427559435031-Atualiza%C3%A7%C3%B5es-de-Mar%C3%A7o-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:43Z"
rotulos: ["sync_hc", "ploomes", "ploomes_10714213", "sync_hash_115534f48ed0"]
---

# Atualizações de Março de 2025

## [05/03/2025] [Correção]

- Ajuste no aplicativo para o preenchimento automático de campos ao consultar o CNPJ na Receita Federal. Embora o recurso já estivesse em funcionamento, o Código e a Descrição do CNAE não eram preenchidos. Essa limitação foi corrigida na versão 6.0.10 do aplicativo.
- No app, foi removida a validação de criação de documentos sem cliente, já que na web não é feita essa validação.
- Quando o usuário não tinha permissão de excluir produtos, ainda assim, na edição em massa, ele podia ver e clicar no botão de exclusão em massa. Agora o botão vai aparecer apenas caso o usuário tenha essa permissão.
- Os desenvolvedores corrigiram a requisição que testa se os filtros da seção estão corretos na hora de configurar o modelo do documento.
- Corrige a função que monta a request de produtos de cliente.
- Ao duplicar venda ou documento dentro do negócio, em algumas situações era possível alterar o cliente, e isso causava erros. O comportamento foi corrigido.
- Um erro estava acontecendo ao tentar preencher produtos de uma seção usando uma fórmula externa. O comportamento foi corrigido.

## [06/03/2025] [Correção]

- Quando um usuário não tinha permissão para ver clientes que não é responsável, ele não conseguia ver o nome do contato na página de negócio, porém na visualização de funil o nome do cliente aparecia, independente da permissão. Agora, ao invés de ver o nome do cliente, o usuário vê "Cliente indisponível".

## [10/03/2025] [Correção]

- APP - O envio da propriedade "Creator" dentro do objeto da proposta enviado ao backend fazia com que alguns fluxos de aprovação fossem ignorados, agora eles são respeitados.
- Aplicativo - Corrigimos um comportamento onde o aplicativo não respeitava obrigatoriedade de campos por perfis de usuário.
- APP - O campo de porcentagem possuía uma trava que impedia as fórmulas de serem calculadas caso a chave do campo tivesse \_discount. Essa trava foi removida caso o campo tenha fórmula de obrigatoriedade ou visualização.
- APP - Durante a edição de proposta, a fórmula interna do campo de opções pré-cadastradas de proposta não era calculada, resultando na falha do filtro dos itens do campo. Criamos o caminho para acessar os campos de Produto de cliente em fluxos de aprovação.
- Mudamos a Atualização do Amout da Venda no Ploomes após atualização da Ordem de Serviço no Omie. Agora o cálculo é feito com basem em outra fórmula.
- Corrigimos a pesquisa por opcionais, onde havia um erro na pesquisa por código.
- Em uma mudança passada, foi alterada a ordem de declaração de algumas funções, fazendo com que o iFrame (que mostra o conteúdo do campo dev) fosse carregado antes de ser declarado e ficasse em load infinito. O problema foi corrigido e agora o conteúdo é carregado corretamente.

## [13/03/2025] [Correção]

- Os desenvolvedores adicionaram um contador de caracteres no campo de destinatário em automação que envia e-mail. Além disso, bloqueia o usuário de escrever mais do que 250 caracteres.
- Ajustado o modelo `cliente.cidade` para o formato do frontend, garantindo que valores padrão sejam aplicados corretamente aos campos de cidade.
- Corrigimos um problema em que o timeout na criação de propostas retornava um erro incorreto para o frontend e APIs, permitindo o envio de novas requisições indevidamente. Nesta atualização, otimizamos as queries e aprimoramos o processamento da API e do gerador de HTML na criação e edição de vendas, propostas e documentos.
- O iframe do campo dev não estava funcionando corretamente, portanto não setava a altura e não aparecia o conteúdo. Agora o problema foi resolvido e a altura sempre é calculada.
- Mudança na soma no valor total das vendas da integração Omie no Ploomes, considerando o valor dos serviços.
- Uma deleção de grupo de produtos permite migrar os produtos do grupo que será excluído para outro grupo ou deletá-los na mesma ação. Acontece que, ao realizar essa ação em grupos com mais de 100 produtos, apenas os primeiros 100 eram migrados, enquanto o restante ficava sem destino. Agora, a funcionalidade está com o comportamento esperado.
- Antes, tarefas antigas eram enviadas ao Ploomes sempre que o usuário as editava no Outlook. Para solucionar isso, os desenvolvedores colocaram para apenas trazer edições e inclusões do Outlook após a data de hoje.
- O código que valida valores únicos em campos chave foi otimizado para que campos de número inteiro também sejam validados corretamente.
- Foi corrigido o comportamento do campo de data no formulário de inserção de produtos do CPQ, que não estava sendo limpo ao inserir um novo produto.

## [18/03/2025] [Correção]

- O iframe do campo dev na criação de negócios e propostas não estava aparecendo devido a uma refatoração recente. Foi revertida a refatoração e aplicada uma solução mais simples que resolveu o problema.
- Agora as fórmulas dos opcionais calculam na edição do documento, desde que os opcionais não estejam selecionados, que é como o legado funciona nesses casos.
- Alguns campos não estavam sendo validados no endpoint responsável por retornar ao front-end a mensagem indicando se o item (venda, proposta ou documento) entrou no fluxo de aprovação. Como resultado, em vez da mensagem correta, um erro genérico era exibido, impedindo o salvamento da edição ou criação. Os desenvolvedores implementaram a correção para o problema.

## [21/03/2025] [Correção]

- Corrigimos um problema onde o campo de moeda nos vínculos e blocos não era mantido ao salvar uma venda. Além disso, ao editar propostas ou documentos, os campos de moeda apareciam vazios, o que agora foi ajustado. Também adicionamos uma melhoria para garantir que as informações de moeda dos opcionais de venda, proposta e documento sejam carregadas corretamente.
