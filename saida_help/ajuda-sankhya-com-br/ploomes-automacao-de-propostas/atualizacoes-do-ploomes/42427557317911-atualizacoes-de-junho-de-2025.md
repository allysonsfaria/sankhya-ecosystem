---
id: "42427557317911"
titulo: "Atualizações de Junho de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427557317911-Atualiza%C3%A7%C3%B5es-de-Junho-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:52Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11525951", "sync_hash_8d360bbe1e46"]
---

# Atualizações de Junho de 2025

## [02/06/2025] [Correção]

- Era possível tentar criar um produto com mais do que 200 caracteres nos documentos em formulário modal, e isso causava erros no popover. Os desenvolvedores subiram uma correção e agora o texto é cortado em 200 caracteres.
- Na versão 6.10.0 do aplicativo mobile, foi corrigido um problema na fórmula do campo [Proposta.Valor], que calcula a soma do valor total dos produtos na proposta. O erro ocorria quando o modelo de proposta não utilizava o campo [Bloco.Total], do qual a fórmula dependia. Enquanto no sistema web esse campo é incluído via hardcode para garantir o funcionamento, essa lógica ainda não existia no mobile. A correção implementa esse mesmo contorno, assegurando o cálculo correto também no app.
- O modal do código-fonte de campos multilinha não estavam sendo salvos quando eram fechados. Agora o evento correto é disparado para salvar as alterações ao fechar o modal.

## [03/06/2025] [Correção]

- Em checklists, filtros em campos múltiplos descendo de Contatos verificavam apenas clientes do tipo Empresa, causando comportamentos indesejados em algumas contas. Foi corrigido para que em casos de filtro com campo múltiplo descendo de Contato, filtre apenas pessoas.

## [05/06/2025] [Correção]

- Nas metas, em gráficos que exibem a média de valores, o backend estava calculando a média de cada valor separado e enviando para o frontend. E o frontend por sua vez, só somava os valores da média, o que fazia o valor vir errado. Os desenvolvedores mudaram no backend para retornar o valor da soma e o valor da contagem, enquanto o frontend vai fazer a média baseada nesses valores.
- Ao clicar em algumas notificações enquanto estávamos na tela de "Resumo", elas não estavam sendo abertas. Isso ocorria porque, na rota de selfinfo, faltavam as subrotas para acessar Tarefas, E-mails e Registros de Interação. Os desenvolvedores corrigiram o problema, adicionando as subrotas necessárias.
- No CPQ Beta foi corrigido um problema em que as fórmulas externas estavam sendo recalculadas ao editar uma proposta. Esse comportamento estava incorreto, pois as fórmulas externas devem ser processadas apenas no momento da criação da proposta, e não durante a edição. Agora, o sistema mantém o mesmo comportamento da versão legada, impedindo o recálculo automático dessas fórmulas ao abrir o formulário de uma proposta existente.
- Corrigimos um problema de desempenho que causava erro de timeout ao tentar acessar a tela com todos os funis no novo seletor. A falha impedia a exibição correta dos funis. Para resolver isso, otimizamos a query responsável pela contagem de negócios na página principal, garantindo que os dados sejam carregados de forma mais eficiente e sem interrupções.

## [06/06/2025] [Correção]

- Ao acessar a tela de recuperação de senha por meio do link recebido por e-mail, o texto era exibido em Português, mesmo quando o dispositivo do usuário estava configurado para Inglês ou Espanhol. Esse comportamento foi corrigido, e agora a tela é exibida no idioma correspondente à configuração do dispositivo.

## [09/06/2025] [Correção]

- Ao utilizar um fluxo de aprovação que considerava o número de revisões de uma proposta, a condição não era avaliada corretamente. Isso acontecia porque a validação do fluxo era realizada antes da criação da nova revisão, o que fazia com que a contagem de revisões estivesse desatualizada no momento da checagem. Foi adicionada uma condição que permite que fluxos de aprovação baseados no número de revisões funcionem corretamente mesmo antes da criação completa da nova revisão. Dessa forma, o sistema agora engloba esses casos e aplica corretamente as regras definidas no fluxo.

## [10/06/2025] [Correção]

- Foram corrigidos os problemas visuais de escrita na tela de modularização, especialmente em dispositivos com diferentes tamanhos de tela.
- Por padrão, os modais de importação mostravam um aviso sobre o campo 'responsável', porém a entidade Registro de Interação não possui esse campo. Sendo assim, os desenvolvedores removeram a mensagem no modal de importação de Registros de Interação.
- No iOS, o download de arquivos anexados em registros de interação eram abertos no Safari, que possui uma limitação que ignora o back e faz o download nomeando o arquivo com um código aleatório. Agora, o download é feito dentro do app, possibilitando o controle sobre o nome do arquivo baixado.
- Mesmo com a opção "Nova venda ao ganhar negócio" do funil "Vendas" estando inativa, a seção de Vendas segue disponível para visualização dos usuários em algumas contas, o que foi corrigido.

## [11/06/2025] [Correção]

- As exportações de abas para Excel não estavam sendo concluídas devido à ausência de configuração de autoescalonamento em uma das aplicações do projeto. Isso impediu o ajuste automático de recursos conforme a demanda, impactando o funcionamento do serviço. Após identificarmos a causa, realizamos o escalonamento manualmente para estabilizar a aplicação e normalizar as exportações.
- Na integração com o Docusign, as informações de um contato já presentes no documento estavam sendo retiradas se tentávamos adicionar o mesmo contato novamente em um documento já finalizado. Agora, vamos validar se o documento já está finalizado antes de tentar inserir o signatário, se já estiver, só iremos retornar uma mensagem de erro para o usuário.
- Função Drag and Drop foi adicionada a campos de anexo no CPQ Beta.

## [12/06/2025] [Correção]

- Foi corrigido um problema no drilldown do gráfico em relatórios que exibia negócios fora do filtro aplicado. Isso ocorria porque, ao haver valores vazios, nenhuma dimensão era enviada para o backend, fazendo com que os dados retornados desconsiderassem os filtros definidos.
- Foi corrigido um problema na integração com o Meetime que fazia com que campos de “Negócio” de opções pré-cadastradas, fossem preenchidos com códigos contendo letras e números (como se fossem chaves ou tokens). Isso ocorria quando havia erro na requisição de valores ao Meetime, e os campos eram preenchidos com uma chave padrão. Agora, caso a requisição falhe, os campos não serão mais preenchidos automaticamente, evitando informações incorretas no Ploomes.

## [13/06/2025] [Correção]

- Foi corrigido um erro que impedia a ativação do módulo de Documentos nas contas. O problema ocorria porque a propriedade DocumentModule estava ausente na API do Partners. A propriedade foi adicionada pela equipe de desenvolvimento, normalizando o processo de habilitação do módulo.

## [16/06/2025] [Correção]

- Corrigido problema que impedia o anexo de arquivos com extensão .xml em registros de interação e no envio de e-mails.

## [17/06/2025] [Correção]

- Nas permissões de perfil, havia uma opção chamada 'Pode criar abas?'. Os desenvolvedores a alteraram para 'Pode criar abas, reordenar itens e alterar colunas de abas?'.
- Existia uma regra no código que deixava o campo de cliente obrigatório, ou quando existia o campo de negócio, deixava ele como obrigatório. Porém isso gerava uma inconsistência quando um cliente queria criar registro apenas vinculado à cliente, impedindo-o de realizar a ação. O que os desenvolvedores fizeram foi remover essa regra, deixando para o usuário configurar da melhor forma, e quando não existir vínculo, uma mensagem será exibida informando que precisa de pelo menos um vínculo para criar o registro.
- Foi corrigido um erro visual onde a barra superior com os ícones desaparecia após o clique no ícone de acessos de usuários do suporte.
- Campos de Leads estavam utilizando propriedades erradas quando utilizados em filtros. Agora são utilizadas as propriedades corretas.

## [18/06/2025] [Correção]

- APP - Os campos Cliente e Negocio não são mais configurados pelo código do App, agora eles seguem o que foi configurado na conta. Além disso, caso ambos não estejam preenchidos, o App retorna um aviso dizendo que não é possível criar um registro sem negócio e sem cliente.
- Campo 'Responsável' de tarefas estava disponível mesmo quando a flag não estava ativada, o que quebrava tabelas que utilizavam esse campo como coluna.

## [23/06/2025] [Correção]

- A URL do lembrete de tarefa foi alterada de "<https://app.ploomes.com/>" para "<https://app10.ploomes.com/>".
- Identificamos que algumas mensagens não estavam sendo entregues corretamente ao consumidor da fila do Meetime, o que estava impactando o funcionamento da integração. Para resolver o problema, removemos um componente intermediário que fazia parte do fluxo de comunicação com a fila, permitindo que a integração funcione de forma mais direta e estável. Com essa alteração, o envio das mensagens foi normalizado.

## [25/06/2025] [Correção]

- Identificamos que, ao ativar o módulo de formulários externos, não era possível salvar os formulários. Isso acontecia porque, durante a consulta, o sistema estava buscando os módulos antigos cadastrados em account, e não os módulos atualizados que ficam em accountModules. Os desenvolvedores atualizaram a lógica da consulta para considerar os módulos presentes em accountModules. Com isso, o salvamento dos formulários externos agora funciona normalmente após a ativação do módulo.

## [30/06/2025] [Correção]

- Quando uma conta que utiliza o SSO da Microsoft tinha a senha expirada, acontecia um erro em que o usuário tentava atualizar sua senha mas não conseguia logar no Ploomes. Uma lógica que deveria rodar apenas quando o usuário estivesse logado estava rodando neste momento, o que quebrava a execução. Agora isso só roda se existir informações de "self".
