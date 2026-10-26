---
id: "44012162758551"
titulo: "[TMS] - Criação de Perfil e Validação de Permissões"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012162758551--TMS-Cria%C3%A7%C3%A3o-de-Perfil-e-Valida%C3%A7%C3%A3o-de-Permiss%C3%B5es"
trilha: "Lincros > TMS > Sistema - TMS"
atualizado_em: "2026-10-05T19:21:43Z"
rotulos: ["sync_hc", "lincros", "lincros_13434267", "sync_hash_7f67aa80b305"]
---

# [TMS] - Criação de Perfil e Validação de Permissões

**Problema Relatado pelo Cliente:** O cliente relatou a necessidade de criar um novo perfil de usuário no sistema e atribuir as permissões adequadas para que o usuário possa realizar suas funções. O cliente não está familiarizado com o processo de configuração de perfis e permissões no sistema.

## Passo a Passo para Resolver o Problema:

**1. Acessar o TMS com um Usuário Administrado**r:

É necessário acessar o TMS com um usuário que tenha vinculado um perfil administrador.

Para validar se o seu perfil é administrador, navegue por essa tela: Sistema > Acesso > Usuário > Usuários da empresa.

Informe o seu nome de usuário no campo "Nome" ou "E-mail", dessa forma:

![Imagem 1: Informe o seu nome de usuário no campo "Nome" ou "E-mail", dessa forma:](https://ajuda.sankhya.com.br/hc/article_attachments/44012147036183)

Clique no código e, ao acessá-lo, navegue até a aba "Perfis". O perfil administrador deve estar incluído dessa forma:

![Imagem 2: Clique no código e, ao acessá-lo, navegue até a aba "Perfis". O perfil administrador deve estar incluído dessa forma:](https://ajuda.sankhya.com.br/hc/article_attachments/44012147215255)

## 2. Criar Novo Perfil de Usuário:

Após as validações acima, navegue até a tela: Sistema > Acesso > Perfis.

Com ela aberta, clique em "Novo", dessa forma:

![Imagem 3: Com ela aberta, clique em "Novo", dessa forma:](https://ajuda.sankhya.com.br/hc/article_attachments/44012147354775)

Após clicar em "Novo", uma nova tela deve ser apresentada exatamente igual a esta:

![Imagem 4: Após clicar em "Novo", uma nova tela deve ser apresentada exatamente igual a esta:](https://ajuda.sankhya.com.br/hc/article_attachments/44012163438743)

O campo "Nome" se refere ao nome de usuário, que pode ser um nome da sua escolha.

O campo "Caminho do DashBoard" e "Indicador personalizado" pode ser deixado em branco.

Abaixo explico o que cada uma das flags do campo "Perfis" significa:

- **Alterar unidade:** Permite alterar unidades da empresa.
- **Administrador**: O perfil terá todos os privilégios de um usuário Administrador (padrão Lincros).
- **Criar usuários Webservice**: Permite criar usuários webservice.
- **Autorizar usuário de transportadora**: Permite ao perfil autorizar usuários de transportadora que solicitam acesso via portal do transportador (Para mais informações, acessar o artigo [TMS] - Autorizar acesso de usuário de transportadora).
- **Autorizar usuário de cliente**: Permite ao perfil autorizar usuários de cliente que solicitam acesso via portal do cliente.

## 3. Atribuição de Permissões ao Perfil:

Após a criação do perfil, para incluir as permissões, como por exemplo: visualizar a tela de faturas, NF-e e/ou CT-e e afins, deve ser aberto um ticket com o time de suporte, sendo necessário incluir as permissões que deseja que o perfil tenha.

Caso deseje saber quais permissões um perfil criado previamente no TMS possui, pode ser usado o relatório "Relatórios > Permissões por perfil" que está disponível nessa tela: Relatórios > Permissões por perfil.

Ao chegar na tela, você vai se deparar com ele assim:

![Imagem 5: Ao chegar na tela, você vai se deparar com ele assim:](https://ajuda.sankhya.com.br/hc/article_attachments/44012177446551)

No campo "Perfil" inclua o nome do perfil que você deseja visualizar e, após isso, clique em visualizar para ver em tela ou exportar para encaminhar o Excel via e-mail.

Pegando de exemplo o perfil Analista nativo do TMS, o layout do relatório ficará assim:

![Imagem 6: Pegando de exemplo o perfil Analista nativo do TMS, o layout do relatório ficará assim:](https://ajuda.sankhya.com.br/hc/article_attachments/44012192486423)

Ao exportá-lo ou visualizá-lo, o layout de saída é dessa forma:

![Imagem 7: Ao exportá-lo ou visualizá-lo, o layout de saída é dessa forma:](https://ajuda.sankhya.com.br/hc/article_attachments/44012148028695)
