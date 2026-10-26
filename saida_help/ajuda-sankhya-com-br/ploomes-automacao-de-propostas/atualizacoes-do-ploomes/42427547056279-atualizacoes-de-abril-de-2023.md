---
id: "42427547056279"
titulo: "Atualizações de Abril de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427547056279-Atualiza%C3%A7%C3%B5es-de-Abril-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:12Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7245862", "sync_hash_b583ff5fd9b1"]
---

# Atualizações de Abril de 2023

[03/04/2023] [Correção] Criação do caminho (field path) registro de interação>negócio>negócio origem.

[03/04/2023] [Correção] No lembrete de uma tarefa recebida pelo e-mail, mostrava o horário com 3 horas a menos do horário real da tarefa.

[03/04/2023] [Correção] Usuários recebiam mensagem de erro no envio de dados do formulário, porém o negócio ainda assim era criado.

[03/04/2023] [Correção] Na configuração de Funil, há a opção 'Para quais funis um negócio pode ser ?', que estava com uma inconsistência visual não deixando claro que a opção é para permitir/bloquear o remanejamento dos Negócios.

[03/04/2023] [Correção] Negócio mostrava que não tinha tarefas na visualização de funil, mas ao clicar no ícone do card aparecia tarefas agendadas. Acontecia com tarefas agendadas para o dia de hoje.

[05/04/2023] [Correção] Ao excluir um documento volta para página anterior que o usuário estava usando.

[05/04/2023] [Correção] Em filtros de aba campos de 'Texto Multilinha' estavam sendo lidos como campos de 'Texto Simples'

[05/04/2023] [Correção] Ao salvar um usuário de integração com e-mail que já existe, a mensagem de erro não era equivalente a tal problema, além de zerar todos os campos preenchidos.

[05/04/2023] [Correção] Campo "Address" que preenche automaticamente o campo de CEP "Brazilian Zip Code", preenchia o CEP com um traço "-" e não era possível salvar dessa maneira, somente retirando o traço. Foi alterado um comportamento do Ploomes quando o idioma da conta não está em PT-BR. Agora, todos os idiomas preenchem e salvam o CEP corretamente.

[05/04/2023] [Correção] Ao definir campos ocultos como obrigatórios em um formulário e não preenchê-los, não aparece nenhum indicador de que o campo obrigatório vazio estava oculto. Para resolver tal problema, adicionamos uma nova mensagem de erro para abranger também este caso.

[05/04/2023] [Correção] Ao adicionar o campo "Produto da Venda" nas métricas de relatórios (versão antiga) o formulário não trazia as informações e dava erro na exibição do mesmo. Para tal, foi removida a possibilidade de inserção do respectivo campo na criação de métricas de relatórios.

[05/04/2023] [Correção] Mensagem de erro com problema ao salvar o filtro de opções em campos com possuem tal opção. Foi corrigida a mensagem e a mesma apresenta o conteúdo "Tente novamente mais tarde" de maneira correta.

[06/04/2023] [Correção] Em algumas contas não estava sendo possível entrar no Ploomes pela Microsoft.

[10/03/2023] [Correção] Ao revisar uma proposta e salvá-la, o negócio que a continha não teve o campo [Negócio.Valor] modificado.

[12/03/2023] [Correção] Estávamos com problemas na autenticação dos tokens com o Outlook Calendar.

[13/04/2023] [Correção] Ao recarregar a página editando uma Deal específica, ela volta para a tela de Criação de Deal.

[14/04/2023] [Correção] Alguns clientes não estavam conseguindo acessar o modulo de e-mails.

[17/03/2023] [Correção] Quando um dos leads da lista já tivesse um negócio aberto, a integração com o Econodata finalizava a importação ignorando os demais da lista.

[18/04/2023] [Correção] Produto cadastrado no Omie não era exibido na base do Ploomes porque a integração com o Ploomes não aceitou a URL da imagem do produto com mais de 300 caracteres.

[19/04/2023] [Correção] Ao modificar responsável de um cliente no Ploomes, a integração do Omie mudava essa informação, colocando no lugar o usuário do responsável anterior.

[19/04/2023] [Correção] Estávamos com problemas para puxar campos da integração Exact Spotter.

[20/04/2023] [Correção] Por nunca ter sido implementado, o campo de cópia oculta (CCO) não estava presente no formulário de e-mail dentro de um Negócio ou Cliente. A correção adicionou esse campo no formulário e, a partir de agora, é possível enviar e-mails com cópia oculta a partir da página de Negócio e Cliente.

[24/04/2023] [Correção] O Ploomes estava fazendo diversas requisições que não eram necessárias na hora da criação de um novo negócio, retiramos essas requisições.

[24/04/2023] [Correção] O filtro por data dentro de cliente não estava trazendo documento, mesmo que no filtro de documento estivesse retornando.

[24/04/2023] [Correção] Opção de integrar CNPJ da Receita Federal no Ploomes não estava disponível quando o idioma da conta era alterado.

[24/04/2023] [Correção] Se não clicarmos no botão de FILTRO, o front não exibe a quantidade de registros que serão afetados pela automação, o que impede o usuário de prevenir erros.

[24/04/2023] [Correção] O gráfico não estava carregando por trazer uma coluna com index NaN.

[25/04/2023] [Correção] Ao filtrar por estágio do negócio no gráfico em relatórios beta, não era exibido o funil pertencente, sendo impossível identificar o estágio correto.

[25/04/2023] [Correção] Ao clicar em um produto com vínculo ele seleciona todos os vinculados, mas não trava a obrigatoriedade.

[25/04/2023] [Correção] Ao clicar em um produto com vínculo ele seleciona todos os vinculados, mas não trava a obrigatoriedade.

[28/04/2023] [Correção] Algumas automações que enviam e-mails estavam enviando esses e-mails sem o corpo.
