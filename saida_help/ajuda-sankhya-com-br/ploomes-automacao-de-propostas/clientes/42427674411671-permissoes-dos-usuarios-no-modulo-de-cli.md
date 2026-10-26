---
id: "42427674411671"
titulo: "Permissões dos usuários no módulo de Clientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427674411671-Permiss%C3%B5es-dos-usu%C3%A1rios-no-m%C3%B3dulo-de-Clientes"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-11T16:14:02Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7924985", "sync_hash_254d074ba862"]
---

# Permissões dos usuários no módulo de Clientes

## Perfis de usuário

As permissões são configuradas pelos **Administradores** de acordo com cada Perfil, Nelas é possível escolher o que o usuário daquele Perfil poderá ou não fazer, como criar, visualizar, excluir, editar, entre outros.

Para acessar as permissões, seguimos o caminho:

Administração > Perfis de usuário > Seleciona o perfil desejado > Cliente

![Imagem 1: Administração > Perfis de usuário > Seleciona o perfil desejado > Cliente](https://downloads.intercomcdn.com/i/o/745480515/aa1c67e668143b64a0943779/perfil.png?expires=1786536000&signature=5932170c9954cd22f7de23135ffedf22bf88bea152984ce3ff837c03e01d1c5f&req=cyQiEsF%2BmIBaFb4V1XW4gWut7WcMolzT0PmiO7zN5SVfJuHWpr5c0gMBR9vo%0AKwYSWrtR9tH4jKCpJrKjwUw0bQ%3D%3D%0A)

![Imagem 2: Administração > Perfis de usuário > Seleciona o perfil desejado > Cliente](https://downloads.intercomcdn.com/i/o/745480847/7241aaef7f8054e736a31da6/perfil+2.png?expires=1786536000&signature=09c43a1ada956db288cae397d9742e8a98695d69a02ebad9fa15a240741520da&req=cyQiEsF%2BlYVYFb4V1XW4gVyh1e0eernWxheYTdRRy8P2ziTrbEFgxMsFGuia%0AbD0RRMtnJuKytiWZWkoyabdH%2FA%3D%3D%0A)

Nela é possível configurar quais clientes o usuário pode visualizar, editar, excluir, se pode cadastrar empresas, pessoas e as permissões referentes aos produtos do cliente.

As opções das permissões são com base nos campos de usuário (responsabilidade/colaboração ou equipes) e algumas de sim ou não (como: tem acesso ao módulo de clientes?)

Se o usuário não tiver a permissão para visualizar um cliente, não poderá visualizar tarefas, negócios, propostas, vendas vinculados a esse cliente.

Essa entidade tem ligação direta com **produtos do cliente, anexos, registros de interação, tarefa, venda e documento de cliente.**

As permissões de **Produtos do Cliente** são configuradas nas permissões de clientes (na parte inferior dos campos):

![Imagem 3: As permissões de Produtos do Cliente são configuradas nas permissões de clientes (na parte inferior dos campos):](https://downloads.intercomcdn.com/i/o/530856461/68335c259250924100e9ea94/image.png?expires=1786536000&signature=978977ea53b2d805ebb19573ab35bc5c83b4e8114793d582b04756f2665df312&req=cSMnHsx4mYdeFb4V1XW4gXccSX3sfuO%2BhucUnUouNcIAbaTsM0%2BxIOqZ1auB%0ASE80%2BNiONJ03mgukgbMs7MQ6fA%3D%3D%0A)

Só será possível ter acesso ao produto do cliente, se tiver acesso ao cliente.

Os **Anexos** poderão ser visualizados se tiver acesso à entidade que o anexo foi inserida, por exemplo: cliente - só se tiver acesso ao cliente, negócio - só se tiver acesso ao negócio e assim por diante.
Caso o Anexo esteja na Biblioteca, dependerá das permissões da pasta do usuário.

Todos os usuários podem fazer **Registros de Interação** na entidade que possuem permissão de visualização, porém, é possível definir se um usuário pode editar ou excluir um registro de interação que ele criou.

As permissões de **Tarefas** são configuradas em Outros e nelas é possível definir se o usuário possui ou não acesso ao módulo. Caso não tenha acesso, o calendário aparecerá vazio e uma mensagem de erro amarela surgirá no canto inferior direito informando que não pode acessar esse módulo.

É importante reforçar que o usuário tem acesso apenas às tarefas pessoais (ele inserido como usuário), tarefas vinculadas a cliente/negócios que possui acesso (sem o usuário estar inserido). É possível ser inserido em uma tarefa onde não possui permissão de visualizar o negócio/cliente, porém, não conseguirá acessar essas entidades.

![Imagem 4: As permissões de Tarefas são configuradas em Outros e nelas é possível definir se o usuário possui ou não acesso ao…](https://downloads.intercomcdn.com/i/o/530852744/fdd1235229adb4be63720713/image.png?expires=1786536000&signature=795a08ac1dcee49aa1a793461ec6397b95cb8f45664a236c4ccc9875a6b0ad11&req=cSMnHsx8moVbFb4V1XW4gSyIzhblofQQq0ZFCc28h5wvtHpqiQWIu7Ebs8Kv%0A0Mcg%2Bg%2BTpx3VgIez3VHxJnZp2Q%3D%3D%0A)

Os documentos de **Venda** e **Documentos de Cliente**, só são acessíveis se tiver acesso à visualização do cliente, porém, ambos possuem suas permissões de edição, exclusão, cadastramento e compartilhamento.

É possível criar uma venda sem negócio, mas não é possível criar uma venda sem cliente.

## Campos e permissões

Para utilização correta das permissões, é importante entendermos a diferença entre os campos 'Responsável’, ‘Usuários Colaboradores’ e ‘Criador’

- O **Responsável** é o usuário que você seleciona para cuidar do cliente. Sendo um campo editável, mas permite apenas 1 valor (usuário).
- O **Usuário Colaborador** você utiliza quando precisa definir mais de um usuário responsável pelo mesmo cliente. Sendo um campo também editável e que permite mais de 1 usuário.
- O **Criador** é o usuário que criou aquele cliente, ficando salvo seu nome para controle. Não é um campo editável e não garante permissão de acesso.

![Imagem 5: O Criador é o usuário que criou aquele cliente, ficando salvo seu nome para controle. Não é um campo editável e não…](https://downloads.intercomcdn.com/i/o/745494978/1e7d5936a95a9bf591b3e104/resp.png?expires=1786536000&signature=37c7c18d9a82f55d4fff2eb17216568c8f16bf079decd00fc1e2619540997794&req=cyQiEsB6lIZXFb4V1XW4gXjXMlEQseIabvI7%2BNv%2F%2FBg6z4EwDJ9doDTvq1VA%0AfrEKsmfsAuDbylmE177tfB9zLA%3D%3D%0A)

## Minhas atividades x todas as atividades

Dentro da página do seu cliente, no canto inferior direito, temos disponível as visualizações "Minhas atividades" e "Todas as atividades".

Estas visualizações determinam se você pode visualizar apenas as suas atividades ou de todos os colaboradores.

A opção "todas as atividades" pode não estar disponível para você, de acordo com a configuração de permissão do seu perfil de usuário.

![Imagem 6: A opção "todas as atividades" pode não estar disponível para você, de acordo com a configuração de permissão do seu…](https://downloads.intercomcdn.com/i/o/745501850/bf5453d91ca32c2699dcb5f0/2023-05-19+11_11_28-.png?expires=1786536000&signature=9de0304027588ed7d941696434f13ea1a8dfe930f86fd6c0f8e215b3057bf1fb&req=cyQiE8l%2FlYRfFb4V1XW4gcFsvdrmICaLu%2BEWwulsJCfJ2T2bC7cUFjGD0n%2Bc%0AH%2B6SS4%2FZI1qf6NhmoyjeyVxoQQ%3D%3D%0A)

Em 'Outros', dentro das permissões do perfil, temos "Atividades que pode visualizar"

Esta opção delimita sua visualização dos registros dentro da página do cliente.

![Imagem 7: Esta opção delimita sua visualização dos registros dentro da página do cliente.](https://downloads.intercomcdn.com/i/o/745504415/df7a0ae36df9eb5a3534d1e1/image.png?expires=1786536000&signature=a2e33117cda3e089c3f416c891f8a57248ec4f4066da1d8d3175317d76656aa6&req=cyQiE8l6mYBaFb4V1XW4gc27GteS%2BQxYIYwp9bmQF3wDNu2xUqi9XC1g42BH%0AzO1J7EON0fksXBzfKw5BZtbDqw%3D%3D%0A)

![Imagem 8: Esta opção delimita sua visualização dos registros dentro da página do cliente.](https://downloads.intercomcdn.com/i/o/745504032/e782d8d85704d5b85c85063d/image.png?expires=1786536000&signature=c54f0ec8a13403bd511a58dd35881f39fc0340236f454417867b8d2efdca0af1&req=cyQiE8l6nYJdFb4V1XW4gXB50LMkk2bwUZgCORyZ2uqQieEh6lP2YFvobrZv%0A837MvoHPix3bCUkkQCUT%2F7Nwyw%3D%3D%0A)

## Visualização e equipes

Dentro de todas as opções de visualizações e permissões, temos a opção

'**Sob responsabilidade de membros de sua equipe',** esta opção coloca em prática mais um ponto do Ploomes, que são as equipes.

Cada usuário pode fazer parte de uma mesma equipe e as permissões de visualizações ficam pautadas por equipe, quando selecionada essa opção.

![Imagem 9: Cada usuário pode fazer parte de uma mesma equipe e as permissões de visualizações ficam pautadas por equipe, quando…](https://downloads.intercomcdn.com/i/o/745512603/3496390d92ecb026c7dd96fa/equipe+1.png?expires=1786536000&signature=92d975bcfb94c761777718cb968e0f89120ce6b2e0cce7660ecd4486eae0a141&req=cyQiE8h8m4FcFb4V1XW4gfUlruvp94lGfRgWrCpCYaOpexdVcIWPzCEWtWDn%0ACb9%2BBl7olTNTYEYzMAW1oeGoRg%3D%3D%0A)

![Imagem 10: Cada usuário pode fazer parte de uma mesma equipe e as permissões de visualizações ficam pautadas por equipe, quando…](https://downloads.intercomcdn.com/i/o/745512755/9d780b5914df4fcdd1027680/equipe+2.png?expires=1786536000&signature=e32c3fdd38fde2f73db3d0d16e6a05fdfcef8fc1bba2a7d0a9a0f0674dcddc57&req=cyQiE8h8moRaFb4V1XW4gf2HqmO6tnMfjd5IJJ%2BVkJNYoEDZ5F1lL704s2gF%0Aoe81aMMZcqxBnXgxhhWf0q%2FKUg%3D%3D%0A)

![Imagem 11: Cada usuário pode fazer parte de uma mesma equipe e as permissões de visualizações ficam pautadas por equipe, quando…](https://downloads.intercomcdn.com/i/o/745512894/895c6337080e53b1138a2fbb/equipe+3.png?expires=1786536000&signature=ee13d18ee7d083cf668c94bd1d8644b6d822510352d5b71ebc9d335d276d7ffc&req=cyQiE8h8lYhbFb4V1XW4gecdA2wMjOV9TbuGi8FEf3PI99m99kte5x127jTr%0ABxTSvWQijVNAufLtRkRk4CUjFA%3D%3D%0A)

**Para saber mais sobre o módulo de Produto de cliente**, clique aqui.

## Permissão no campo

Temos a opção de limitar a edição de um campo diretamente dentro do campo.

Ao acessar o formulário, acesse a edição do campo que deseja limitar a edição:

![Imagem 12: Ao acessar o formulário, acesse a edição do campo que deseja limitar a edição:](https://downloads.intercomcdn.com/i/o/753499354/f402f93374ca3cc3cc864239/image.png?expires=1786536000&signature=a86ea7c9eb8d033eba275830a382f55586fe1732e448d93ddc1d518b02623519&req=cyUkEsB3noRbFb4V1XW4gWYSgNTuGmsB4Gh9cYxEG%2B7xkkVEuhq1iOXetWfl%0AzrPnN4Ma%2FYsESvfNG34ujf6rUA%3D%3D%0A)

![Imagem 13: Ao acessar o formulário, acesse a edição do campo que deseja limitar a edição:](https://downloads.intercomcdn.com/i/o/753501389/d9bcc066b167d9d8a4d92055/image.png?expires=1786536000&signature=7bf7eaf71cdd8541471a9aea4099a61becbbc89082add3a0a9353ed31176e727&req=cyUkE8l%2FnolWFb4V1XW4gdQVuXkVLAtM1YmW0fpC0JpHCTPop4DLwOAsfBk1%0AKRxs85907fb6wQx%2B21E7Bp0xOA%3D%3D%0A)

Você pode selecionar quais usuários ou equipes podem editar este campo, além de ligar o bloqueio da edição por padrão e selecionar regras

![Imagem 14: Você pode selecionar quais usuários ou equipes podem editar este campo, além de ligar o bloqueio da edição por padrão e…](https://downloads.intercomcdn.com/i/o/753502485/0a2011b4bc3f2d9778890f44/image.png?expires=1786536000&signature=c99532b6d276b9a225ac9755590803b040f267d1ae614b763629bf0886d1ab40&req=cyUkE8l8mYlaFb4V1XW4gbZph%2BEMG9tRKIyh7j%2FOfTDimT3t3axQb2xSI0VX%0ALTCtJxsUANvXAIh9Nb1kKXRFWg%3D%3D%0A)

![Imagem 15: Você pode selecionar quais usuários ou equipes podem editar este campo, além de ligar o bloqueio da edição por padrão e…](https://downloads.intercomcdn.com/i/o/753503255/79ff8a9e941fd90b3e18ba22/image.png?expires=1786536000&signature=be1ca79470ac652cebcbe0c40dada5736f699b0e08ebc39fdc93391d740cb414&req=cyUkE8l9n4RaFb4V1XW4gWWkdZWKnOds6DypPwOfQ9vuaFAw24mGOFW522ak%0AOC7oNSYydo67X41as8Qi%2Feos4A%3D%3D%0A)

Para casos de uso no módulo de clientes, [clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/42427495033495).

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat.

##
