---
id: "42427557232919"
titulo: "Atualizações de Maio de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427557232919-Atualiza%C3%A7%C3%B5es-de-Maio-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:51Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6187652", "sync_hash_b904a00a3923"]
---

# Atualizações de Maio de 2022

- [03/05/2022] [Correção] Adicionamos um acento no campo 'Última atualização' da entidade de Negócios, pois antigamente não tinha, dificultando a localização do mesmo.
- [03/05/2022] [Correção] O filtro 'Data de criação - relativa' não estava filtrando corretamente nas automações que possuíam esse filtro.
- [03/05/2022] [Corrigido] Automações com nome muito grande não estavam duplicando o card.
- [04/05/2022] [Corrigido] Requisições iniciais estavam quebrando e demorando para subir no mobile (sistema operacional Android 11)
- [05/05/2022] [Corrigido] Ao inserir uma quantidade razoável de colunas, a caixa para inserir mais fica pequena, dificultando a visualização dos campos.
- [05/05/2022] [Correção] Nas permissões do ploomes a permissão de usuários estava como: Usuário que pode visualizar, no singular, quando deveria ser: Usuários que pode visualizar.
- [05/05/2022] [Correção] Ao compartilhar uma proposta por e-mail, o modelo estava preenchendo os campos com os valores da última proposta do negócio, ao invés de usar os valores da proposta a ser enviada.
- [05/05/2022] [Correção] Ao usar o campo [Negócio.Proposta] em um checklist que verificava se o negócio tinha propostas, na tela estava aparecendo o botão adicionar duplicado e um dos botões estava sem funcionar.
- [05/05/2022] [Correção] Ao acessar um cliente não estava aparecendo os Negócios/Documentos/Vendas que estavam vinculados a ele.
- [05/05/2022] [Correção] Os negócios de um funil com a opção de gerar venda ao ganhar negócio, não estava reconhecendo o cliente vinculado a ele e aparecia uma mensagem de confirmação informando que não tinha cliente vinculado, mesmo quando, na verdade tinha.
- [05/05/2022] [Corrigido] Quando se criava/editava um checklist, o front repete todos os itens já adicionados aparentando ficar iguais ao item sendo editado.
- [05/05/2022] [Corrigido] Existia um problema na relação entre campos de usuário de produto da proposta com um campo de usuário de cliente.
- [05/05/2022] [Correção] Usuários que não possuíam permissão para gerar propostas, estavam conseguindo clicar nessa opção quando estavam no app, ao fazer isso ela ficava carregando sem parar, agora ao clicar em 'Nova Proposta' apresenta uma mensagem de erro, informando que o usuário não possui permissão.
- [05/05/2022] [Corrigido] Ao criar um documento derivado de uma proposta, produtos que eram da proposta continuavam inseridos, mesmo que não fizessem parte do filtro da tabela de produtos do documento criado.
- [05/05/2022] [Correção] Ao clicar em nova venda, os campos ficavam carregando infinitamente e não estava sendo possível gerar a venda.
- [05/05/2022] [Correção] Quando você tinha um campo de valor de produto da proposta que é usado no [Bloco.Total], depois de inserido o produto, se você abrisse a edição dele e mudasse o valor para outro valor e voltasse ao que você salvou anteriormente e apertar para salvar, a fórmula do [Bloco.Total] não era engatilhada.
- [05/05/2022] [Correção] Se você tivesse um registro de interação ou campo multilinha que possuísse a tag <style> utlizada para estilização, o estilo estava 'vazando' para fora do componente e afetando a tela toda.
- [05/05/2022] [Corrigido] Termos de serviço da Europa não estavam sendo apresentados no primeiro acesso do usuário do servidor europeu.
- [05/05/2022] [Corrigido] Importação com problemas para apresentar progresso nos hostsets 2, 3, 4, 5, 6, 7, 11 e 12.
- [05/05/2022] [Corrigido] O histórico de e-mail estava cortando os e-mails mais antigos, de modo que a sua leitura ficava limitada.
- [05/05/2022] [Corrigido] O aplicativo para celulares estava fechando sozinho ao tentar abir o módulo de tarefas em contas de Portugal.
- [05/05/2022] [Correção] Alguns campos do tipo 'Endereço' que possuíam formulas, estavam sendo engatilhados, porém, o conteúdo não estava aparecendo no campo.
- [05/05/2022] [Correção] Em vários locais do sistema não estava aparecendo o símbolo do 'lápis' usado para editar os campos, e quando clicávamos em cima do campo estava aparecendo uma mensagem de 'Não é possível editar esse campo' mesmo o usuário possuindo permissão para isso.
- [05/05/2022] [Correção] Quando o zoom da tela estava abaixo de 90% não estava sendo possível editar o título de tarefas, ao clicar no lápis de edição não abria para colocar o título novo.
- [05/05/2022] [Corrigido] Para alguns clientes a caneta para editar alguns campos de lead não estavam aparecendo, ao tentar editar apresentava mensagem de erro.
- [05/05/2022] [Correção] Alguns clientes estavam com instabilidade para ver registros de interação de negócios que possuíam mais de 10 registros.
- [05/05/2022] [Correção] Ao inserir e salvar o valor da proposta junto à integração Robopac, os valores eram zerados.
- [05/05/2022] [Correção] Ao duplicar modelos de proposta não apresentavam erro e nem duplicavam.
- [05/05/2022] [Corrigido] Ao configurar uma empresa para requisitar todas as negociações que ela é matriz do cliente adicionado ele faz a mesma requisição para clientes do tipo pessoa.
- [06/05/2022] [Correção] A Tabela de produtos padrão estava vindo com o código-fonte comentado, e por conta disso não estava aparecendo no modelo de documento.
- [06/05/2022] [Correção] Alguns usuários não estavam conseguindo visualizar o conteúdo de pastas, por que estas pastas não eram públicas e estavam mostrando a configuração delas como pública erroneamente.
- [09/05/2022] [Correção] Se um cliente e um contato fossem criados com o mesmo telefone, a integração do Exact Spotter gerava o negócio com dois contatos iguais.
- [10/05/2022] [Correção] Quando tentamos excluir um perfil de usuário na edição do mesmo, aparece uma mensagem para transferir os usuários que possuem esse perfil, e essa mensagem estava aparecendo um 'código' ao invés de 'Selecione um perfil para transferir os usuários'.
- [10/05/2022] [Correção] A visualização estava sobrepondo os itens de baixo ao expandir os vínculos na categoria do produto pai.
- [10/05/2022] [Correção] Se a ampliação da tela aplicada estivesse alta, ao tentar editar um campo na visualização de tabela, o modal ficava "fora" da tela, impossibilitando a edição do mesmo. A correção redefine a posição de abertura (direita ou esquerda) de maneira mais precisa.
- [11/05/2022] [Corrigido] Ao configurar as permissões de registro de interação, após salvar, as opções configuradas não eram exibidas.
- [12/05/2022] [Correção] Quando a integração com o Spotter criou um negócio, ele vinculou o contato criado duas vezes, como cliente e como contato.
- [13/05/2022] [Correção] No documento, alguns campos de contato quando dentro de uma tabela de produtos não estavam puxando os valores corretos e em alguns casos não puxavam nada.
- [16/05/2022] [Correção] O cálculo da capacidade de armazenamento da biblioteca estava considerando os usuários inativos também.
- [16/05/2022] [Correção] No armazenamento da biblioteca, não mostrava corretamente a quantidade de dados que estavam sendo armazenados, apresentando apenas 0,00 GB.
- [18/05/2022] [Correção] Quando a regra do fluxo de bloqueio era "Igual a (vazio)" não estava sendo feito o filtro e por conta disso algumas vendas caiam indevidamente no fluxo.
- [18/05/2022] [Correção] Fórmula configurada específica não recebendo o valor de um dos campos adicionados como variável.
- [19/05/2022] [Correção] O usuário era obrigado a mapear um estágio em um formulário externo de atualização.
- [20/05/2022] [Correção] No formulário externo o campo 'telefone' que era um campo chave, estava cadastrando novamente ao invés de atualizar o contato existente com esse telefone.
- [23/05/2022] [Correção] As opções de edição e exclusão do comentário do registro de interação só estavam aparecendo ao clicar em visualizar o registro.
- [23/05/2022] [Correção] Ao aplicar um filtro de negócios como "diferente de vazio", o mesmo não estava funcionando corretamente, gerando confusão para os usuários.
- [23/05/2022] [Correção] Ao excluir um modelo de documento, em alguns momentos o modal para confirmar a exclusão não estava aparecendo.
- [23/05/2022] [Correção] Ao fazer uma fórmula condicional usando datas, não funcionava por conta do formato da data não ser compatível com a data que irá realizar a comparação.
- [25/05/2022] [Correção] No idioma Português (Portugal) alteramos a palavra 'Venda' por 'Encomenda' na parte de documentos.
- [25/05/2022] [Correção] Adicionado bloqueio nas ações de automação para impedir a escolha de campos do tipo anexo.
- [25/05/2022] [Correção] O campo "Proposta Origem" não funcionava em fórmulas na edição em vendas, apenas na criação. Portanto, foi removido a possibilidade de adicionar esse campo em fórmulas, mas ainda é permitido em vínculos.
- [25/05/2022] [Correção] Nomes dos campos recém-criados ficam espelhados, porém, apenas visualmente.
