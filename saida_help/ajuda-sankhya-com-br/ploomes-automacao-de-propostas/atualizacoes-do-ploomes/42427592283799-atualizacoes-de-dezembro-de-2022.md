---
id: "42427592283799"
titulo: "Atualizações de Dezembro de 2022"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427592283799-Atualiza%C3%A7%C3%B5es-de-Dezembro-de-2022"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:08Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_27ac94c79774", "ploomes_6531685"]
---

# Atualizações de Dezembro de 2022

[05/12/2022] [Correção] Quando entravamos na modificação visual de algumas propostas o navegador simplesmente parava de responder, revertemos a subida que causou isso.

[09/12/2022] [Correção] O campo [Proposta.Banco] do tipo texto simples não puxou informações de [Cliente.Grupo] do tipo opções pré-cadastradas

[12/12/2022] [Correção] Alguns e-mails não estavam aparecendo nos registros de interação por conta de uma instabilidade momentânea.

[13/12/2022] [Correção] Não era possível fazer download de arquivos pelo front do Ploomes.

[13/12/2022] [Correção] Ao duplicar um card, alguns itens iam duplicados, principalmente campos de marcadores, do tipo Cliente e do tipo Opções pré-cadastradas.

[13/12/2022] [Correção] Ao fazer exportação da aba de Clientes, a planilha enviada continha uma quantidade inferior ao que era exibido no Ploomes.

[13/12/2022] [Correção] App estava fechando inesperadamente ao tentar editar dados de clientes.

[13/12/2022] [Correção] Campo usado em fórmula faltando em formulário externo impedia de salvar nova entrada.

[13/12/2022] [Correção] Em alguns negócios, o marcador estava indo como duplicado assim que o cliente duplicava o negócio original
[13/12/2022] [Correção] Mensagem de erro de limitação de caracteres no título ao criar campo de funil de negócio era exibida, mesmo que o front apresentasse um máximo de 60.
[13/12/2022] [Correção] O campo "Proposta aprovada" estava com preenchimento automático com "sim", havia negócios que não há proposta, ele permanecia como sim.
[13/12/2022] [Correção] Ao tentar fazer upload via API, documentos não eram enviados.

[14/12/2022] [Correção] Metas com valores muito altos atrapalhavam a exibição na tela de relatórios.

[16/12/2022] [Correção] Mensagem de confirmação de exclusão de itens em campo de opções pré-cadastradas era exibida com intermitência.
[16/12/2022] [Correção] Opções pré-cadastradas apareciam indevidamente para o usuário, mesmo que já fossem deletadas.
[16/12/2022] [Correção] Usando um CNPJ válido, após integrar os dados com a Receita Federal, o campo [Cliente.E-mail] tem seu conteúdo resetado.
[16/12/2022] [Correção] Campo de Multinha como valor padrão de um campo de Texto Simples, apresentando indevidamente todos os caracteres do campo de texto multilinha

[19/12/2022] [Correção] Chamado criado para reverter os deletes em Contacts realizados no dia 16/12/2022 por volta das 10:30 pelos usuários 'Luccas Muraro' e 'Isabella N. Praça'.

[21/12/2022] [Correção] Ao tentar enviar e-mail dentro de um negócio selecionando um modelo de e-mail que contém um anexo, o anexo não era removido quando trocava o modelo para "nenhum".

[21/12/2022] [Correção] Ao enviar e-mail com alguns campos, não aparecia o conteúdo do campo e sim o nome dele.

[21/12/2022] [Correção] Ao cadastrar no campo de razão social um código ERP na frente do nome da razão social (Ex. 1234 - Nome Razão Social), não era possível retornar o cliente ao realizar uma busca no módulo de cliente por esse código.

[21/12/2022] [Correção] Ao tentar criar contato em negócio usando formulário mini de cliente, uma mensagem de erro e de sucesso ao criar contato eram exibidas ao mesmo tempo e o contato era criado.

[22/12/2022] [Correção] Ao gerar uma nova automação de funil ou automação genérica, a mensagem de erro era exibida: "Atenção! Preencha os campos corretamente", sendo que todos os campos estavam preenchidos.

[22/12/2022] [Correção] Na integração com Omie clientes sem CPF ou CNPJ estavam sendo verificados como duplicados, o que acabava sobrepondo informações de outros clientes ou contatos embaralhando informações de alguns clientes.

[23/12/2022] [Correção] Havia um problema na visualização de anexos, eles abriam, porém, dava erro e ficavam sem visualização.

[26/12/2022] [Correção] Campo de venda aparecia indevidamente em pedido de venda mesmo sem estar adicionado no modelo usado, além de bater no endpoint errado.

[26/12/2022] [Correção] Não era possível salvar clientes do tipo empresa nem pessoa. Um erro era exibido no console e nenhuma requisição era feita.
