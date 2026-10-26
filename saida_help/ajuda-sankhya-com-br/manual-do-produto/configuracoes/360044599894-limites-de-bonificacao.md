---
id: "360044599894"
titulo: "Limites de Bonificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599894-Limites-de-Bonifica%C3%A7%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:49:25Z"
rotulos: ["manual", "Configuração", "Parceiro", "Liberação de Limites", "Descontos", "TOP", "Bonificação", "Desconto de bonificação", "Evento 23", "Limites", "Limites de Bonificação", "br.com.sankhya.com.avancado.limitesbonificacao", "Limites de Bonificação manual", "Financeiro", "Controle de Limites para Pedidos e Descontos: Configuração e Utilização", "Venda Mais"]
---

# Limites de Bonificação

Esta tela poderá ser utilizada para cadastrar limites que permitirão um controle sobre os Pedidos e Descontos bonificados. Os referidos limites necessitam ser liberados em um determinado período de tempo, sendo que, o intervalo deve ser dentro de um mesmo mês.

![Imagem 1: Esta tela poderá ser utilizada para cadastrar limites que permitirão um controle sobre os Pedidos e Descontos…](https://ajuda.sankhya.com.br/hc/article_attachments/360078400393)

Através do campo **"Filtrar por usuário"**, você pode refinar a busca dos limites já cadastrados.

O usuário do sistema que será configurado para o limite em questão, é indicado por meio do campo **"Usuário"**.

Nos campos **"Data Inicial"** e **"Data Final"** informe os períodos pertinentes ao começo e ao fim da liberação para o limite cadastrado.

O campo **"Limite Bonificação"** possibilita que você informe o valor máximo que o usuário configurado poderá liberar.

Essa rotina é utilizada, por exemplo, na confirmação de uma nota de venda configurada com um [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), com a opção **"Bonificação"** acionada e um parceiro que permita Desconto de Bonificação. Ao confirmar a nota, o sistema irá abrir o pop-up de solicitação de Liberação de Limites com o evento [23-Bonificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#23-bonificao). Dessa forma, ao selecionar o liberador, serão exibidos os liberadores cadastrados na tela Limites de Bonificação.

O campo **"Bonificação"**, do Cadastro de Tipos de Operação - TOP, influencia esta rotina da seguinte forma:

- Se a marcação Bonificação presente na TOP estiver realizada, ao proceder com uma Venda utilizando-a, é aberto o pop-up de solicitação de **"Liberação de Limites"** para o evento 23 - Bonificação, no valor total da nota.
- Com a marcação Bonificação não realizada, será solicitada a liberação para o evento 23 - Bonificação com base na somatória dos valores informados no campo Bonificação dos itens.

Na tela de solicitação de liberação de limites para bonificação, será sugerido pelo sistema o Gerente do Vendedor para liberação.

- Para isso, faça a ligação pelos campos Funcionário e Empresa presentes no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (aba **"Identificação"**) e no [Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores) (aba **"Geral"**). Faz-se a associação informando os mesmos códigos nos campos Funcionário e Empresa em ambos os cadastros.
- Na tela de liberação, quando o evento for de Bonificação e o Usuário Liberador possuir mais de um período, é aberta uma tela para que o usuário escolha qual dos períodos será utilizado. Para validar o limite do Liberador no Período, será utilizado o somatório das notas liberadas pelo mesmo.

Para impressão do valor da bonificação dos itens em Txt's, utilize a variável **"vdb01"**.

**Nota:** quando o parâmetro **"Usa desconto FOB - DESCFOB"** estiver habilitado e o Tipo de Operação - TOP comportar a **"Bonificação"**, ao proceder com uma Venda, o sistema lançará o valor apontado na tela [Desconto Máx. por Grupo/Tabela de Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600274-Desconto-M%C3%A1x-por-Grupo-Tabela-de-Pre%C3%A7o), campo **"% Desconto Máximo"** contido para o campo **"% de desconto"** do item.
