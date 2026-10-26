---
id: "42427576967447"
titulo: "Atualizações de Julho de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427576967447-Atualiza%C3%A7%C3%B5es-de-Julho-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:59Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_f96a699fe776", "ploomes_6376506"]
---

# Atualizações de Julho de 2022

- [04/07/2022] [Correção] Fórmula comentada estava apresentando erro no testar fórmula.
- [04/07/2022] [Correção] Ao tentar editar uma proposta, o campo de cidade não estava mostrando o valor selecionado e também impedindo o usuário de editar as informações do mesmo.
- [04/07/2022] [Correção] Em relatórios quando se tinha uma dimensão com campo de data e os dados retornados não tinham o campo preenchido, retornava o mês como 0NaN e não como vazio.
- [08/07/2022] [Correção] Ao dar aceite/recusar em um linkweb, estava dando para reabrir, modificar visualmente e compartilhar novamente e ele se mantinha aceito/recusado.
- [08/07/2022] [Correção] Número de negócios não estava aparecendo na lista de funis quando a conta possuía um número elevado de funis.
- [08/07/2022] [Correção] Link para acessar formulário externo estava quebrado e dando erro 500.
- [11/07/2022] [Correção] Algumas empresas não eram criadas na integração com o ActiveCampaign
- [13/07/2022] [Correção] A integração com o Whatsapp dava erro quando o número cadastrado no ploomes começava com um 0.
- [13/07/2022] [Correção] Fórmulas de campo de proposta com variáveis de campos de negócio não executavam corretamente quando proposta e negócio eram criados juntos em tela cheia
- [13/07/2022] [Correção] Quando um opcional bloqueava outro opcional obrigatório e em seguida o desbloqueava, a obrigatoriedade não funcionava mais.
- [13/07/2022] [Correção] Estava apresentando erro 'Tente novamente mais tarde' na criação de uma negociação e mesmo assim o negócio era criado.
- [13/07/2022] [Correção] Ao tentar salvar uma fórmula invalida, estava aparecendo erroneamente o erro "Preencha o campo SENAO", mas deveria mesmo exibir o erro "Erro ao criar fórmula!"
- [13/07/2022] [Correção] A fórmula condicional contendo campos de porcentagem era salvada, mas seus valores não eram retornados ao campo, fazendo com que o usuário sobrescrevesse com um valor vazio caso tentasse salvar novamente.
- [14/07/2022] [Correção] Campos de produto na tela reduzida de edição de propostas estavam "disparando sozinhos".
- [14/07/2022] [Correção] Campo do Nome do Contato e do Telefone não aparecem no documento.
- [15/07/2022] [Correção] Tarefa está inserindo usuários de forma automática mesmo após retira-los.
- [15/07/2022] [Correção] O campo 'Estoque Omie' no ploomes não estava sendo atualizado sempre quando tinha alguma mudança no estoque do Omie.
- [15/07/2022] [Correção] Por conta de uma atualização do WhatsApp Web tivemos que mudar a forma de copiar modelos de mensagem, agora quando clicamos no modelo escolhido, a mensagem vai para a área de transferência, bastando um ctrl+v para colar esse texto na caixa de mensagem e utilizá-lo normalmente.
- [15/07/2022] [Correção] O campo de título e da label do botão de aceitar os Termos de Uso e Política de Privacidade apresentavam um preenchimento indevido, usando tags em vez de uma string correta.
- [15/07/2022] [Correção] Em alguns clientes, a barra de carregamento ficava aparecendo mesmo não tendo nada carregando na tela.
- [15/07/2022] [Correção] A quantidade de propostas e vendas não era exibida no layout do Ploomes, mesmo que houvesse uma quantidade maior que 0 em cada uma delas.
- [15/07/2022] [Correção] Ao acessar à conta do cliente e tentar fazer a ordenação de alguns funis, a ordenação feita não permanecia caso a página fosse recarregada ou se se mudasse de seção no Ploomes e se retornasse em seguida aos funis.
- [15/07/2022] [Correção] Cliente informou que o Ploomes apresentava lentidão em geral, principalmente nas telas que exibiam os relatórios.
- [15/07/2022] [Correção] Ao acessar o painel de relatórios, notava-se que havia o desalinhamento nalgumas colunas, sendo que umas estavam deslocadas à esquerda e outras à direita, impactando na visualização dos dados.
- [15/07/2022] [Correção] Em automações avançadas de produto, ao editar o campo de marcadores de produto, os marcadores inseridos deveriam permanecer no campo de valor quando se abre novamente as configurações para editar a automação.
- [19/07/2022] [Correção] Em uma proposta com opcionais que se bloqueiam, os conteúdos dos opcionais bloqueados e eles estavam indo para a proposta final.
- [19/07/2022] [Correção] A integração com o Facebook Leads estava criando clientes com números no lugar dos nomes, descobrimos que eram de formulários não mapeados no ploomes.
- [19/07/2022] [Correção] Integração com Mailchimp só exportava valores do campo 'Recebe email marketing' null
- [20/07/2022] [Correção] Ao exportar algum arquivo para a biblioteca, era gerado um erro, o qual se tratava de incompatibilidade de versões entre o frontend e o backend.
- [20/07/2022] [Correção] A integração com Exact não estava preenchendo campos de data.
- [21/07/2022] [Correção] Na integração com o Omie, o valor padrão de etapa não estava indo como '10' que seria a primeira etapa, mas sim, '00' o que nulava o valor de etapa para o cliente.
- [21/07/2022] [Correção] Algumas vendas não estavam subindo do ploomes para o omie.
- [21/07/2022] [Correção] Alguns clientes estavam com problema no sincronismo do provedor com os e-mails do ploomes.
- [22/07/2022] [Correção] O campo de CEP quando vazio, exibia alguns zeros no lugar.
- [22/07/2022] [Correção] Os campos opcionais de produto da proposta quando bloqueados por mais de 2 campos, impossibilitavam a seleção dos mesmos.
- [22/07/2022] [Correção] Campos de opções pré-cadastradas não estavam carregando todas as opções.
- [22/07/2022] [Correção] Alguns campos na conta do cliente não apresentavam algumas palavras no idioma que ele havia configurado.
- [22/07/2022] [Correção] Não estava sendo possível duplicar negócios para outros funis.
- [22/07/2022] [Correção] Descrição do passo a passo para integrar estava desatualizada de acordo com as novas diretrizes, o que impossibilitava ativá-la.
- [28/07/2022] [Correção] A página de revisão/edição de proposta não carregava, gerando uma tela de carregamento interminável para alguns clientes.
- [29/07/2022] [Correção] Um campo de opções pré-cadastradas, se estivesse marcado com uma opção excluída, não permitia mais a edição.
- [29/07/2022] [Correção] Não era possível ao cliente mover algum arquivo da biblioteca quando a seção lateral que exibia as pastas estava aberta.
- [29/07/2022] [Correção] Ao clicar em excluir campo, aparecia uma mensagem de erro mesmo o campo sendo excluído normalmente.
- [29/07/2022] [Correção] Ao inserir um item com nome grande na definição de filtros, o mesmo ficava com exibição quebrada, além de não exibir o nome do campo no elemento ao passar o mouse sob o item.
