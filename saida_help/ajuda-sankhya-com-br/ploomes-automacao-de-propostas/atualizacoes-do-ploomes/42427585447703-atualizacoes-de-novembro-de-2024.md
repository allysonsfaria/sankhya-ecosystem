---
id: "42427585447703"
titulo: "Atualizações de Novembro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427585447703-Atualiza%C3%A7%C3%B5es-de-Novembro-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:40Z"
rotulos: ["sync_hc", "ploomes", "ploomes_10092144", "sync_hash_b8f66bdf306d"]
---

# Atualizações de Novembro de 2024

## [05/11/2024] [Correção]

- Foi corrigido um problema de duplicação de clientes na integração com o Omie. O sistema agora usa um cache temporário para armazenar o ID do cliente quando a primeira notificação de criação é recebida. Assim, ao receber uma segunda notificação quase simultânea, o sistema verifica o cache e evita a criação duplicada, realizando apenas uma atualização se o ID já estiver presente.
- Na integração com o Omie, ao clicar em 'Sincronizar Produtos', o Omie estava removendo a descrição detalhada dos itens, pois essa informação não era retornada na requisição original. Para corrigir essa questão, incluímos um parâmetro na requisição, solicitando que o campo de descrição detalhada seja retornado na resposta.

## [06/11/2024] [Correção]

- Ao selecionar um novo cliente ou card para salvar o vínculo de e-mail, o campo não estava exibindo as opções porque a função não estava chamando corretamente. A correção faz com que as opções apareçam sempre que o campo for clicado.
- Na criação ou edição de modelo de documentos com muitos campos, ocorriam timeouts. Apesar disso, a criação ou edição do documento era concluída, mas o usuário recebia um erro na tela. Havia um processo indevido no fluxo de geração de HTML, que gerava atrasos desnecessários e resultava no erro exibido.
- Agora, ao clicar no ícone de mapa ao lado do endereço do cliente no aplicativo, o usuário é redirecionado automaticamente para o Maps.
- No aplicativo, foi colocado um hardcode pra forçar o campo descrição da tarefa ser obrigatório.
- Problema com o renderizador de HTML que poderia causar crashs em alguns Androids específicos.

## [07/11/2024] [Correção]

- Quando um usuário com permissão para ver apenas as suas atividades acessava um registro de interação, ele conseguia ver as atividades dos outros usuários. Foi adicionada uma verificação para que nesses casos só mostre as atividades do usuário que está acessando.
- Agora, ao ganhar um negócio que possui mais de uma proposta, o modal de selecionar a proposta base para a geração da venda irá aparecer, como era antes.
- Agora, ao duplicar uma métrica em relatórios Beta, elas irão permanecer na ordem correta.
- Em automações, não estava sendo possível mapear campos dinâmicos múltiplos de opções pré-cadastradas. O problema foi corrigido.
- Na integração com o Google Calendar, tarefas finalizadas deixam de receber atualizações. Assim, após serem concluídas, elas permanecem inalteradas no calendário, preservando a integridade das informações.

## [12/11/2024] [Correção]

- No TinyMCE os caracteres especiais não eram formatados no código-fonte como acontecia no CKeditor, gerando problemas entre comparações de strings em campos multilinha. Esse comportamento foi corrigido.
- Ao criar proposta + deal em tela cheia, não era possível buscar dados do cliente usando o caminho Proposta > Cliente. O comportamento foi corrigido.
- Foi corrigido um problema no CPQ Beta, onde a mensagem de sucesso ao duplicar um produto era exibida em português, mesmo para usuários com o idioma configurado para inglês. Agora, o idioma da mensagem é exibido corretamente conforme as configurações do perfil do usuário.
- O objeto que continha a última proposta do negócio não era formatado corretamente, fazendo com que não fosse possível ler suas propriedades via fórmula na edição de vendas no formato modal.
- As imagens estavam sendo inseridas sem a URL e sem as dimensões configuradas no editor TinyMCE em modelos de e-mail. A correção foi aplicada, e agora as imagens estão sendo inseridas corretamente em modelos de e-mail.
- Ao criar proposta + deal em modal, em alguns casos acontecia um loop para definir as propriedades do responsável do negócio. Agora o código foi otimizado para não fazer requisições desnecessárias.
- Havia uma lógica para formatar datas para numeros no front sob certa condição, mas isso só poderia ser feito quando a fórmula era do tipo 'condicional' e essa verificação não estava sendo feita. Agora ela é feita corretamente evitando comportamentos inesperados.
- Ao modificar um campo não múltiplo para múltiplo, vai aparecer um modal informando que a mudança pode impactar a substituição do campo em modelos em HTML.
- A tela de compartilhamento exibia as opções de autenticação "WhatsApp" e "SMS" mesmo que essas opções não estivessem inclusas no plano do LetsSign do usuário. Agora as opções são exibidas de acordo com o plano contratado.

## [13/11/2024] [Correção]

- Na busca geral, foi adicionada a opção de abrir buscas em nova aba ao clicar em um resultado com o botão direito e em seguida em "Abrir link em nova aba", ou clicando com o scroll do mouse no resultado.
- Agora, em todos os planos é possível configurar a visualização em tabela ou kanban nas configurações do funil.
- Quando a proposta era criada pelo CPQ Beta, os campos dinâmicos não eram salvos corretamente se as informações não fossem preenchidas manualmente ou por fórmula. Como consequência, a proposta apresentava erros e não era integrada corretamente com o sistema Sankhya. Com a correção aplicada, os campos dinâmicos agora são sempre salvos, garantindo o funcionamento adequado e a integração correta com o Sankhya.

## [18/11/2024] [Correção]

- No formulário de registro de interação, ao usar fórmula de obrigatoriedade baseado no tipo do campo cliente, a fórmula não funcionava. Isso acontecia porque a mudança de cliente não era observada pela aplicação para rodar novamente a fórmula.
- Anteriormente, o campo de CNPJ era mapeável na integração RD ao nível da entidade de contato. Agora, o comportamento foi alterado da seguinte forma: no mapeamento de contatos: apenas o campo CPF é exibido; o CNPJ não aparece. No mapeamento de clientes: tanto os campos CPF quanto CNPJ estão disponíveis. No mapeamento de empresas: apenas o campo CNPJ é exibido.
- Ao excluir um produto na página de grupos, a tradução da ação no modal estava errada para espanhol e inglês. Agora funciona normalmente em todas as línguas.
- Na integração com o RD, identificamos que a interface de mapeamento de integrações exibia setas que poderiam sugerir a possibilidade de um mapeamento bilateral, mesmo para campos configurados como "apenas leitura". Ajustamos esse comportamento para que as setas sejam exibidas de acordo com as reais possibilidades de mapeamento de cada campo, garantindo maior clareza na interface.
- Em formulários externos a descrição de campos estava sem as quebras de linha. O problema foi corrigido.
- Agora, na página de negócios, ao abrir a aba de "Enviar e-mail" sem nenhum modelo selecionado a assinatura configurada vai aparecer corretamente.
- A mensagem de erro ao remanejar o negócio estava sendo exibida como código, ao invés de ser transformada em texto. Os desenvolvedores aplicaram a correção, e agora ela é mostrada como texto.
- Agora, ao editar um assunto de modelo de e-mail que contém variáveis, as variáveis irão continuar funcionando corretamente.
- No aplicativo havia uma falha no comportamento de um campo com restrição de edição configurada para apenas alguns usuários. O campo estava permitindo edição por usuários não autorizados. Identificamos que o problema era a ausência da verificação da propriedade "ValueEditable", responsável por controlar a habilitação ou desabilitação do campo conforme necessário. A verificação dessa propriedade foi implementada, corrigindo o comportamento.
- Adicionada permissão para upload de arquivos .rtf
- Identificamos que o problema ocorria durante o cadastro de clientes do tipo CPF, onde a tela permanecia em carregamento infinito e o processo não era concluído. A causa estava relacionada ao campo CPF, que, apesar de ser um campo de texto, estava sendo tratado como um número, o que resultava em um erro durante o processamento. Realizamos uma correção que assegura a conversão adequada do valor, solucionando o problema.
- No aplicativo, ao iniciar registro de visita do check-in a partir de uma tarefa, não estava passando as informações de 'Marcadores' para o registro. Além de realizar os expands corretos para sempre garantir as tags das tarefas, foi realizado a passagem das tags da tarefa para o registro do check-in.
- Quando o campo 'título' não estava presente no formulário de negócio, isso resultava em um cálculo incorreto e na atribuição do texto padrão 'Sem título' antes do envio para a API. Para resolver o problema, o desenvolvedor adicionou o título vindo da tela de Negócio durante a montagem inicial do formulário, garantindo que um título adequado fosse sempre utilizado, mesmo na ausência do campo específico.
- No aplicativo, os campos multi-linha com strings que não eram HTML não estavam concatenando corretamente quando o cálculo era feito de Produto para Bloco e de Bloco para Proposta. Isso acontecia porque o código estava erroneamente entrando na condição de soma numérica e tentava fazer um parseFloat na string, o que resultava em um NaN. O código foi ajustado para garantir que as strings de campos de texto e multi-linha que não sejam números sejam apenas concatenadas na string final, sem a aplicação do parseFloat.

## [21/11/2024] [Correção]

- Fórmulas integradas de Excel apresentavam um problema no retorno do valor esperado no campo de produto da proposta, causado pelo envio de variáveis booleanas como 'null'. Após a aplicação de uma correção pela equipe de desenvolvimento, as fórmulas agora estão funcionando corretamente, retornando o valor esperado ao ser acionada.

## [28/11/2024] [Correção]

- No modal de seleção de produtos em propostas/vendas e documentos, o filtro simples configurado no campo '[Produto da Proposta.Produto]' não estava sendo considerado, embora fosse levado em conta na seleção fora do modal. O comportamento foi corrigido, e agora o filtro configurado será considerado em ambos os casos.
- No modal de autenticação multifatorial, os textos não estavam sendo internacionalizados. Os desenvolvedores implementaram uma correção para esse problema.
- Ao criar uma venda a partir de uma proposta que contenha opcionais que não são aceitos pela venda, uma mensagem deveria aparecer informando que alguns opcionais foram removidos. A mensagem aparecia em algumas situações, mas em alguns casos não. Agora a mensagem aparece sempre.
- Usando a relação de opcionais (quando um opcional obriga ou sugere o outro), era possível burlar a regra de apenas um opcional no bloco de vínculos. Isso foi corrigido e agora uma mensagem é exibida para o usuário.
- Na configuração do filtro de blocos em documentos há um limite de quantos grupos, famílias e marcadores podem ser inseridos, mas não havia nenhuma indicação disso no frontend. Agora há uma mensagem indicando que o limite foi ultrapassado. Além disso, um scroll foi adicionado nesse modal para facilitar a visualização.
