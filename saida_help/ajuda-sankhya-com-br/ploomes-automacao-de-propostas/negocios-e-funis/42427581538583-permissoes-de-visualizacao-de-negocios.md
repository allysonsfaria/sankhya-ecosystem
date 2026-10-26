---
id: "42427581538583"
titulo: "Permissões de visualização de negócios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427581538583-Permiss%C3%B5es-de-visualiza%C3%A7%C3%A3o-de-neg%C3%B3cios"
trilha: "PLOOMES: Automação de propostas  > Negócios e funis"
atualizado_em: "2026-08-10T18:05:38Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5792607", "sync_hash_97647cc1c9fe"]
---

# Permissões de visualização de negócios

Em Negócos, assim como em Clientes, temos o campo **Responsável**, onde se seleciona um usuário que 'cuida' do negócio. Para definir mais de um usuário responsável pelo mesmo negócio, utilize o campo 'Usuários colaboradores'.

Na configuração de cada usuário, seleciona-se obrigatoriamente um **perfil de usuário**.

Veremos neste artigo como configurar os perfis para limitar as visualizações de negócios.

Em **Administração - Perfis de usuário**, selecione o perfil que deseja editar.

Vale notar que o perfil de **Administrador** não pode ser editado, pois tem acesso à conta inteira.

Recomendo limitar o número de administradores, já que podem editar campos e informações de pagamento.

As permissões de negócios são praticamente idênticas às de clientes, mas com algumas opções adicionais:

Tem acesso ao módulo de Negócios?

**Sim**

**Não**

Negócios que pode visualizar

**Nenhum**

**Sob sua responsabilidade/colaboração**

**Sob sua responsabilidade/colaboração, ou sob responsabilidade de membros de sua equipe**

**Todos**

**Se o cliente estiver sob responsabilidade/colaboração**

Negócios que pode editar

**Nenhum**

**Sob sua responsabilidade/colaboração**

**Sob sua responsabilidade/colaboração, ou sob responsabilidade de membros de sua equipe**

**Todos**

**Se o cliente estiver sob responsabilidade/colaboração**

Negócios que pode excluir

**Nenhum**

**Sob sua responsabilidade/colaboração**

**Sob sua responsabilidade/colaboração, ou sob responsabilidade de membros de sua equipe**

**Todos**

**Se o cliente estiver sob responsabilidade/colaboração**

Pode criar novos negócios?

**Sim**

**Não**

Pode ganhar e perder negócios?

**Sim**

**Não**

Pode reabrir negócios?

**Sim**

**Não**

Como vimos, o que muda é "**Se o cliente estiver sob responsabilidade/colaboração**" - Isso nos permite liberar o acesso ao negócio para o responsável do cliente, que não precisa necessariamente ser responsável pelo processo.

Na Ploomes, temos o exemplo do funil de chamados - O responsável do negócio nesse funil é um técnico, e não o responsável do cliente. O responsável pelo cliente ainda tem acesso aos cards do funil, por ter essa opção marcada.

Também temos como limitar quem pode ganhar, perder ou reabrir negócios.

## Permissão de visualização de funis

Na configuração do funil, é possível limitar quais usuários têm acesso ao processo, e consequentemente aos negócios nele inseridos.

![Imagem 1: Na configuração do funil, é possível limitar quais usuários têm acesso ao processo, e consequentemente aos negócios…](https://downloads.intercomcdn.com/i/o/430360523/b1ccbbcab3eb8848d38f6d73/image.png?expires=1786536000&signature=857a9ac8f45a033db0fabce5b644cb9e752e686bf9ede4473cc77438f5f01a6e&req=cCMnFc9%2BmINcFb4V1XW4gdWmrG9O9xEz5aXgZYdAG9KLbW%2FeAWzFD%2F3D02wt%0ARuV8cWJxqpWz%2FA0OOUqzVhEirw%3D%3D%0A)

É importante ressaltar que as automações de funil funcionam com base na permissão do usuário, então uma automação de "duplicar negócio em novo estágio" não funciona caso o usuário não tenha acesso ao funil de destino.
