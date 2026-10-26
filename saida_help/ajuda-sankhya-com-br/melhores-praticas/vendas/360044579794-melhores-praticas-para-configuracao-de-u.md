---
id: "360044579794"
titulo: "Melhores Práticas para configuração de um Vendedor visualizar apenas seus lançamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579794-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-de-um-Vendedor-visualizar-apenas-seus-lan%C3%A7amentos"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:28Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "Movimentação Financeira", "Financeiro", "#ciadoRoger", "Restringa acessos a lançamentos específicos", "Vincule vendedor e empresa no cadastro do usuário", "Configure filtros para visualização de dados"]
---

# Melhores Práticas para configuração de um Vendedor visualizar apenas seus lançamentos

Existem alguns processos da área Comercial que requer que seus vendedores visualizem e façam movimentações somente com determinados clientes de sua respectiva carteira, ou seja, restrição para que outros vendedores não visualizem lançamentos originados de outro vendedor.

Vejamos a seguir uma boa prática para configuração desta restrição.

O Sistema Sankhya/Jiva W existe uma expressão chamada: **ctx[usuario\_logado]** e **ctx[emp\_usu\_logado].**

- Vejamos a configuração básica.

1. Acesse o sistema com o usuário SUP
2. Configurações » Controle de Acesso » Usuários
   No cadastro do usuário, vincule o Código do Vendedor, no campo 'Vendedor'
   Vincule o código da Empresa(se desejar), no campo 'Empresa'
3. Acesse a Rotina desejada. [Exemplo: Financeiro » Rotinas » **Movimentação Financeira**]
4. Clique para abrir o 'Assistente de Filtro'.
5. Clique em 'Editar filtro padrão'.
6. Escolha uma das opções de filtro indicada abaixo e cole nesta opção
7. Salve o registro.

**Observação**: Somente o usuário SUP tem permissão de inserir/alterar e excluir este filtro padrão. Os usuários não visualizara esta opção, portanto não poderá altera-lo ou exclui-lo.

- Vejamos um exemplo de uso das expressões na rotina de 'Movimentação Financeira'.

Abaixo foram definidas três possibilidades para configurar tal filtro:

![Imagem 1: Desta forma o USUÁRIO 'XXXXX', visualiza apenas títulos que ele mesmo lançou e para a empresa que está vinculada ao seu…](https://ajuda.sankhya.com.br/hc/article_attachments/19196223882647) Desta forma o USUÁRIO 'XXXXX', visualiza apenas títulos que ele mesmo lançou e para a empresa que está vinculada ao seu cadastro e o usuário SUP visualiza tudo.

( ctx[usuario\_logado] <> 0 and
Financeiro.CODEMP = ctx[emp\_usu\_logado] AND
Financeiro.CODUSU = ctx[usuario\_logado] ) or
ctx[usuario\_logado] = 0

![Imagem 2: Se desejar que apenas o USUÁRIO 'XXXXX', visualize apenas títulos que são da Empresa 2(por exemplo), independente de…](https://ajuda.sankhya.com.br/hc/article_attachments/19196223885719) Se desejar que apenas o USUÁRIO 'XXXXX', visualize apenas títulos que são da Empresa 2(por exemplo), independente de quem lançou o título use apenas o filtro abaixo, usuário SUP visualiza tudo:

( ctx[usuario\_logado] <> 0 and
Financeiro.CODEMP = ctx[emp\_usu\_logado]) or
ctx[usuario\_logado] = 0

![Imagem 3: Se desejar que apenas o USUARIO 'XXXXX', visualize apenas títulos que ele próprio lançou independente da empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/19196223892119) Se desejar que apenas o USUARIO 'XXXXX', visualize apenas títulos que ele próprio lançou independente da empresa vinculada ao usuário, use o filtro dessa forma,o usuário SUP visualiza tudo:

( ctx[usuario\_logado] <> 0 AND
Financeiro.CODUSU = ctx[usuario\_logado] ) or
ctx[usuario\_logado] = 0
