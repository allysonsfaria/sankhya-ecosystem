---
id: "42427585317143"
titulo: "Atualizações de Outubro de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427585317143-Atualiza%C3%A7%C3%B5es-de-Outubro-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:39Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6531678", "sync_hash_7e55aa8c615d"]
---

# Atualizações de Outubro de 2022

[03/10/2022] [Correção] Quando cliente ultrapassava o limite da integração por hora com o Facebook Leads, os excedentes não eram adicionados posteriormente.

[03/10/2022] [Correção] A duplicação de automações estava dando erro 500 em alguns casos.

[04/10/2022] [Correção] Campos de horas estavam vindo com uma diferença de 3 horas do Exact Sales, corrigimos essa diferença do nosso lado.

[06/10/2022] [Correção] Outlook Calendar não estava integrando as tarefas.

[07/10/2022] [Correção] Quando a automação fazia uma atualização que entrava em uma regra de negócio de bloqueio, dava um erro não mapeado.

[07/10/2022] [Correção] Vendas não estavam caindo corretamente no fluxo de aprovação quando criadas.

[07/10/2022] [Correção] Ao habilitar no funil a geração automática da venda, o valor padrão do campo não estava sendo obtido.

[07/10/2022] [Correção] Formulários externos estavam dando erro de submissão quando um campo múltiplo era marcado como chave.

[07/10/2022] [Correção] Ao duplicar múltiplas automações de uma só vez, o modo como era feito as requisições fazia com que algumas duplicadas fossem perdidas.

[07/10/2022] [Correção] Campo [Proposta.Dados Bancários] desaparecia das variáveis da fórmula após ser adicionado.

[07/10/2022] [Correção] Usuário desejava alterar a configuração do campo padrão [Produtos.Desconto] aplicando uma fórmula de Excel, mas a fórmula inserida não era possível salvá-la.

[07/10/2022] [Correção] Campo [Negócio.Curso] adicionado como variável na configuração de fórmula de uma automação não permitia o funcionamento correto dela, somente quando removido.

[13/10/2022] [Correção] Usuário limitado a visualizar somente membros da sua equipe, estava conseguindo colocar uma usuária que não era de sua equipe como responsável de um negócio.

[13/10/2022] [Correção] Ao tentar fazer exportação de dados, o carregamento dos dados no Power BI apresentava o erro 504 'Gateway Time-out'.

[14/10/2022] [Correção] Integração com o Spotter não estava refletindo alterações e também quando desciam as alterações, eram duplicadas.

[14/10/2022] [Correção] Ao tentar criar/editar uma tarefa, o seletor de data é configurado com o formato da data e a linguagem a ser utilizada. O problema é que no momento que o campo carregava os valores, a configuração é perdida, voltando ao padrão de "MM/DD/YYYY" no formato americano. Para corrigir, adicionou-se o código de configuração do formato e data em cada atualização de data, desse modo, as configurações iniciais nunca são perdidas.

[20/10/2022] [Correção] Não estava sendo possível mapear o campo CNPJ do ploomes com o do Rd Station.

[20/10/2022] [Correção] Não estava possível a conversão de leads.

[21/10/2022] [Correção] Funcionalidade de privar ou deixar público os e-mails não estavam funcionando corretamente, afetando inclusive os vínculos.

[24/10/2022] [Correção] Algumas abas antigas estavam em desacordo com a regra, consequentemente exibindo para usuários que não teriam acesso às mesmas.

[24/10/2022] [Correção] O campo [Proposta.Desconto] estava retornando 'infinity'.

[24/10/2022] [Correção] Na visualização por mapa de tarefas, estava com erro e não apareciam algumas tarefas mesmo com o endereço correto no Google Maps.
[25/10/2022] [Correção] O texto antigo da parte de registros de interação nas permissões de usuários podia gerar um mal-entendido com relação aos privilégios de edição e exclusão dos registros de interação. Para deixar mais claro, o time de UX sugeriu outro texto deixando explícito que a opção possibilita a exclusão e edição dos seus próprios registros.

[25/10/2022] [Correção] Após salvar o telefone do contato, salvar o registro de interação e enviar pelo WhatsApp somente era possível quando a página era recarregada.

[25/10/2022] [Correção] Campos de Checkbox estavam aparecendo o valor padrão mesmo quando não tinha nenhum valor no formulário.

[25/10/2022] [Correção] Cliente possuia erro no campo "Cidade" onde a mensagem "Negócio não tem contato" aparecia no lugar do preenchimento, mesmo com todas as configurações estando corretas.

[25/10/2022] [Correção] Aparecia o campo de 'Adicionar Arquivo' em registro de interação mesmo o usuário não sendo o criador.

[25/10/2022] [Correção] Proposta estava carregando infinitamente ao salvar e não salvava.

[25/10/2022] [Correção] Ao retirar um produto já inserido na proposta e tentar inseri-lo novamente, os valores estavam sendo zerados.

[25/10/2022] [Correção] Opcionais de produtos não estavam sendo exibidos corretamente na criação e edição.

[25/10/2022] [Correção] Não era possível abrir o modal com informações do item ao clicar em um campo multilinha da tabela dinâmica.

[25/10/2022] [Correção] Os comentários feitos em registros de interação não apareciam também no lugar onde deveria ser exibido o nome do autor do comentário.

[25/10/2022] [Correção] Campos de opções pré-cadastradas não apresentavam seu conteúdo quando o card era duplicado.

[25/10/2022] [Correção] O campo nativo de desconto não permite a inserção manual de fórmulas. Isso acontece devido à fórmula integrada do campo ter comportamento circular com fórmula de outros campos.

[25/10/2022] [Correção] Campo do tipo data tinha seu conteúdo alterado eventualmente quando um campo numérico que deveria engatilhá-lo era manipulado.

[25/10/2022] [Correção] Ao duplicar negócio, o card era passado somente com as informações necessárias para a criação, enquanto o restante dos campos iam vazios.

[25/10/2022] [Correção] Os campos multilinha das tarefas não estavam sendo mostrados corretamente. As tags HTML não eram renderizadas como esperadas e a visualização ficava quebrada. O problema estava na ausência de um atributo que realiza essa renderização. Bastou adicioná-lo para corrigir o problema.

[26/10/2022] [Correção] Integração com o Omie estava limpando campo "Telefone" do cliente após uma alteração.

[26/10/2022] [Correção] Campos de multilinha não estavam quebrando a linha corretamente.

[28/10/2022] [Correção] No mapeamento da integração com o Omie, o campo de razão social do Omie estava vindo para o Nome do Ploomes, agora corrigido, está vindo corretamente para o campo de Razão Social do Ploomes.

[31/10/2022] [Correção] Automações de negócio estavam com filtro errado no código, era exibido corretamente na tela, porém, ao ser executada não atendia aos filtros.

[31/10/2022] [Correção] Integração com RD dava problema no mapeamento do campo CNPJ quando vinha para o Ploomes como número.
