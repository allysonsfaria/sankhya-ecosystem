---
id: "42427556656663"
titulo: "Atualizações de Março de 2023"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427556656663-Atualiza%C3%A7%C3%B5es-de-Mar%C3%A7o-de-2023"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:02:45Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7057373", "sync_hash_6261cc7f8dd0"]
---

# Atualizações de Março de 2023

[02/03/2023] [Correção] O caminho utilizado para puxar as informações da proposta de origem do Documento estava tentando ler as informações de [Venda.Proposta Origem]. Foi corrigido para utilizar o caminho que puxe de [Documento.Proposta Origem].

[02/03/2023] [Correção] Em e-mails, abas de "Rascunho" e "Enviados" possuía opção de mover os e-mails para outras caixas, mas ação não funcionava.

[02/03/2023] [Correção] Inconsistência ao enviar e-mails dentro do ploomes.

[02/03/2023] [Correção] Ao editar um anexo através da edição inline, o link para acessar o arquivo não era atualizado, mantendo a URL do anexo anterior. O problema estava na ausência do código que atualiza essa variável, que foi adicionado e o problema parou de ocorrer.

[02/03/2023] [Correção] Em alguns casos não era possível editar uma aba, aparecia em branco a janela para executar ações.

[02/03/2023] [Correção] Adição da integração Dataplace na lista de integrações Plug and Play.

[06/03/2023] [Correção] Ao abrir a opção de "editar etiqueta" em conversas no **Whatsapp Business**, com a extensão da Ploomes ativada, a mesma fechava o modal que continham as etiquetas e com isso era impossível atualizar as informações.
[06/03/2023] [Correção] Em formulário externo não era possível inserir '0' para incrementar o valor do campo decimal.

[07/03/2023] [Correção] Quando deletamos um grupo, o sistema solicita que selecionamos um grupo para fazer a transferências dos produtos, porem, isso não estava ocorrendo e estava deletando os produtos daquele grupo e não fazendo a transferência.

[07/03/2023] [Correção] Documentos podiam ser criados sem o título via API.

[08/03/2023] [Correção] Rota de automação de campo de anexo em negócio origem para negócio derivado adicionada.

[09/03/2023] [Correção] Ao clicar na opção "Limpar dados do navegador" dentro do Ploomes, o mesmo não deletava o Cookie responsável por armazenar a user-key do usuário. Agora, ao realizar a ação, além de tudo que já acontecia, os cookies também são removidos.

[09/03/2023] [Correção] Ao realizar pesquisas dentro do módulo de bibliotecas, o mesmo não trazia as informações, bem como deixava a respectiva tela sem nenhuma informação.

[09/03/2023] [Correção] Os cards de negócios, propostas e vendas na tela de resumo apresentava texto inconsistente com o filtro respectivo para mostrar a contagem de itens. Ao colocar o filtro como "eu", o mesmo traz todos os itens no qual o usuário é responsável do negócio. Porém, o título apresentado era "negócios criados", "Propostas Geradas" e "Vendas Realizadas". Para tal, agora quando o filtro for "eu" o título será "Meus Negócios", "Minhas Propostas" e "Minhas Vendas".

[09/03/2023] [Correção] Campo chave permitia burlar a regra caso a alteração fosse salva antes da requisição de validação de duplicação fosse feita.

[09/03/2023] [Correção] Ao abrir a página de criação de propostas diretamente pelo respectivo módulo, a mesma ficava com loading infinito, impossibilitando a criação de propostas.

[09/03/2023] [Correção] Algumas vendas criadas no ploomes estavam duplicando no Omie e depois duplicando no ploomes.

[09/03/2023] [Correção] Pasta "Caixa de Saída" do e-mail não sincronizava e aparecia vazia.

[10/03/2023] [Correção] Campo "Segmento" não estava sendo mostrado como campo padrão no mapeamento, embora seja. Agora o campo aparece como um campo padrão no mapeamento da integração fazendo relação com o campo "Mercado" do Exact Spotter.

[13/03/2023] [Correção] Ao criar um campo no modal de criação rápida, estava sendo possível ultrapassar o limite de 60 caracteres no título do campo, foi adicionado um valor padrão de no máximo 60 caracteres para impedir o usuário de ultrapassar o limite.

[13/03/2023] [Correção] Negócios criados sem cliente apresentavam problema no checklist caso houvesse um campo de "Cliente do Negócio", todos os campos subsequentes do checklist perderiam sua validação e mostrariam o ícone de campo não preenchido, mesmo se estivesse com valor. Foi corrigido alterando uma condicional que trata a validação de Negócios sem cliente.

[13/03/2023] [Correção] Ao inserir um produto ao criar uma Proposta/Venda, o formulário não ocultava os campos que, por padrão, deveriam ser ocultos. Foi corrigido adicionando uma validação para os campos que estiverem marcados "Ocultar por padrão" não serem exibidos em seções de Propostas/Vendas/Documentos ao inserir um novo produto.

[13/03/2023] [Correção] Ao finalizar uma chamada com o Zenvia em um card, a gravação era salva com uma task de telefone noutro negócio.

[13/03/2023] [Correção] Em alguns casos, adicionar um produto na proposta fazia o aplicativo fechar em aparelhos android.

[15/03/2023] [Correção] Ao editar/criar um modelo de proposta e tentar incluir um novo campo ao lado do outro, o novo campo incluído selecionava uma posição aleatória e inseria no documento.

[15/03/2023] [Correção] Não estava aparecendo o botão para avançar o estágio no checklist em alguns negócios, mesmo podendo avançar o estágio.

[15/03/2023] [Correção] Ao editar/criar um modelo de proposta e tentar incluir um novo campo ao lado do outro, o novo campo incluído selecionava uma posição aleatória e inseria no documento.

[15/03/2023] [Correção] Ao editar/criar um modelo de proposta e tentar excluir um campo no modelo e abrir o código-fonte, sumia todo o HTML do modal.

[16/03/2023] [Correção] Ao receber e-mails, algumas mensagens não estavam chegando à caixa de entrada do Ploomes e, por consequência, não criavam vínculos para os respectivos Contatos e Negócios.

[16/03/2023] [Correção] E-mail não vinculava no compatilhamento LinkWeb, aparecendo apenas '#{{e-mail}}' e não puxando o email integrado do usuário.

[17/03/2023] [Correção] Ao tentar entrar em alguns formulários externos estava sendo exibido uma mensagem informando que 'Não foi possível localizar um formulário'.

[21/03/2023] [Correção] Ao perder um negócio, ocorria de perder com um motivo de outro funil.

[23/03/2023] [Correção] Não estava sendo possível abrir formulários externos que possuíam campos personalizados.

[23/03/2023] [Correção] Opção de Exportar para o PowerBI não era exibida mesmo quando o usuário fazia parte de uma equipe com permissões para realizar a exportação. Foi corrigido adicionando na condicional de exibição, uma validação para checar as equipes que o usuário faz parte.

[23/03/2023] [Correção] Ao abrir a configuração de campos nativos, a opção de definições linguísticas não funcionava. Agora, a mesma (opção) estará desativada, impossibilitando o clique na mesma.

[24/03/2023] [Correção] Ao clicar no botão código-fonte de um campo do tipo multilinha que tenha o CKEditor, estava desabilitando o mesmo impossibilitando o usuário de voltar ao modo visualização.

[24/03/2023] [Correção] Erro de contagem nos Ids, estávamos somando o Id para a integração Omie de forma incremental, porém, lá eles levam como quantidade, o que acabava gerando erros ao bater no limite de produtos, que seria até o item 200, e como era incremental, caso uma proposta fosse alterada e o produto fosse trocado 200 vezes, daria erro para subir a alteração pro Omie.

[30/03/2023] [Correção] No aplicativo, quando o perfil do usuário não tinha permissão de cadastrar vendas, não aparecia o módulo de Vendas dentro de Cliente, mesmo podendo visualizar por outros caminhos.

[30/03/2023] [Correção] Ao entrar na aba de cliente o usuário não conseguia entrar nas configurações, algumas vezes abrindo com muito tempo de espera.

[30/03/2023] [Correção] Em vínculo de produto o produto filho não estava com o visual de obrigatoriedade, mas era obrigatório fazendo o usuário se confundir na hora de preencher os dados corretamente.

[31/03/2023] [Correção] Um campo não poderia ser variável em uma fórmula de preenchimento caso não estivesse presente no texto da fórmula e fosse utilizado na fórmula de exibição ou edição. Estava faltando no código uma validação referente ao escopo da variável formula.
