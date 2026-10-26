---
id: "https://developer.sankhya.com.br/docs/portal-do-desenvolvedor"
titulo: "Portal do Desenvolvedor Sankhya"
url: "https://developer.sankhya.com.br/docs/portal-do-desenvolvedor"
atualizado_em: "2025-11-10T23:34:41.000Z"
---

# Portal do Desenvolvedor Sankhya

A nova versão do **[Portal do Desenvolvedor](https://areadev.sankhya.com.br)** (também conhecido como *Área do Desenvolvedor* ou *Dev Portal*) adota um novo paradigma de criação, propriedade e gestão de soluções desenvolvidas sobre a plataforma Sankhya.

A missão é clara: acelerar a **inovação**, **empoderar** desenvolvedores e **transformar** a forma como construímos soluções.

<Callout icon="📢" theme="default">
  ### Mais do que uma atualização visual, essa versão representa uma mudança de paradigma!

  Deixamos de lado projetos isolados e adotamos um ecossistema baseado em **soluções compostas por componentes** – como add-ons e integrações.

  Ou seja: se antes um **add-on** era considerado uma solução, **agora ele é um componente dentro dela.**
</Callout>

E a mudança na **autoria das soluções** continua: numa solução de uso exclusivo e interno da empresa, somente um usuário do Portal do Desenvolvedor devidamente habilitado e vinculado à própria empresa pode criar esta solução, mesmo que esta seja desenvolvida por um parceiro de software (desenvolvedor externo).

Este manual descreve as **principais funcionalidades do[Portal do Desenvolvedor](https://areadev.sankhya.com.br)**, orientando o usuário na gestão de acessos, criação e publicação de soluções.

## Perfis de Usuários

Os usuários do Portal do Desenvolvedor podem ter 3 níveis de acesso:

* **Administrador**: permissão para gerenciar os dados da empresa, fazer a gestão de acessos e publicar soluções no Marketplace.
* **Desenvolvedor**: permissão para criar, editar e gerenciar soluções adicionadas aos grupos aos quais está vinculado.
* **Desenvolvedor externo**: permissão para editar soluções compartilhadas com ele, podendo adicionar e editar componentes.

| Ação                                                                                                                                                                                                                                   | Administrador | Desenvolvedor | Desenvolvedor Externo |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ | :------------ | :-------------------- |
| Visualizar e alterar dados da empresa (menu *Dados da empresa*)                                                                                                                                                                        | ✅             | ❌             | ❌                     |
| Convidar usuário para o Portal (menu *Gestão de acessos*)                                                                                                                                                                              | ✅             | ❌             | ❌                     |
| Criar grupos, adicionar usuários aos grupos e gerenciar permissões dos grupos (menu *Gestão de acessos*)                                                                                                                               | ✅             | ❌             | ❌                     |
| Criar soluções (menu *Minhas soluções*), que podem ser comerciais ou exclusivas, dependendo das permissões da empresa ao qual o usuário está vinculado (usuário precisa estar vinculado a um grupo com permissão para *Criar solução*) | ✅             | ✅             | ❌                     |
| Editar soluções, podendo criar e editar componentes dentro da solução (soluções adicionadas aos grupos aos quais o usuário está vinculado)                                                                                             | ✅             | ✅             | ✅                     |
| Publicar no Marketplace (depende das permissões da empresa ao qual o usuário está vinculado)                                                                                                                                           | ✅             | ❌             | ❌                     |
| Gerenciar versões (de soluções adicionadas aos grupos aos quais o usuário está vinculado)                                                                                                                                              | ✅             | ✅             | ❌                     |
| Gerenciar clientes beta (atribuição e acesso controlado)                                                                                                                                                                               | ✅             | ✅             | ✅                     |

<br />

## Dados da empresa

*Disponível apenas para usuários nível Administrador*

O menu **Dados da Empresa** reúne as principais informações da sua organização, como razão social, CNPJ, contatos de suporte e comercial, conforme demostrado na imagem abaixo:

<Image align="center" src="https://files.readme.io/e29763a9b3fe8f3aa230fc6c02f9cacc62a7a45cefd2f3acacc3279de4339822-Portal_do_Dev___Dados_da_empresa.jpg" />

* **Resumo da empresa**: Descritivo do que é a sua empresa, seus produtos ou serviços oferecidos e seus principais diferenciais. Este resumo será exibido no Marketplace.
* **Contato Suporte**: Dados do responsável pelo suporte técnico. Esses dados ficarão disponíveis para os clientes que precisarem de suporte técnico através da tela "Minhas Soluções" (disponível no Sankhya OM dos clientes a partir da versão 4.35+).

> 🚧 Atenção:
>
> É recomendável utilizar um **telefone para suporte compatível com Whatsapp ou chatbot**. A tela 'Minhas soluções' (disponível no Sankhya OM dos clientes a partir da versão 4.35+), onde os dados de suporte ficarão visíveis, integra com Whatsapp.

* **Contato Comercial**: Dados para atendimento comercial, como responsável, telefone e e-mail. Esses dados servem para os clientes interessados em adquirir suas soluções via Marketplace.

<br />

## Minhas soluções

*As soluções disponíveis aqui para o usuário, seja qual for o seu nível de acesso, serão apenas as soluções associadas aos grupos aos quais esse usuário está vinculado.[Veja como conceder permissão para acessar a Portal do Desenvolvedor](https://developer.sankhya.com.br/reference/concedendo-acesso-a-colaboradores).*

No menu **Minhas soluções**, é possível administrar todo o ciclo de vida das soluções que sua empresa desenvolve e disponibilizá-las no Marketplace da Sankhya.

<Image align="center" src="https://files.readme.io/2b532d28839a93cd3688f746be5fb6e9867eb3280a9a9e1f22fb072a4719fe15-Portal_do_Dev___Minhas_solucoes.jpg" />

Dentro desse menu, o usuário poderá efetuar as seguintes ações:

* Gerar chave de assinatura
* Criar uma solução
* Adicionar e editar componentes da solução criada (um componente pode ser um add-on, API Gateway, etc)
* Gerenciar os clientes da solução (quando for uma solução de uso comercial)
* Gerenciar os dados da solução que serão exibidos no Marketplace (quando for uma solução de uso comercial)

<br />

### Criar nova solução

Para criar uma nova solução, basta clicar no botão "**Criar solução**" apresentado no menu "**Minhas soluções**".

Ao clicar,  será apresentado um formulário para preenchimento das seguintes informações:

* **Nome da solução**: Insira o título da solução, que será exibido no Portal do Desenvolvedor. Essa informação pode ser editada posteriormente. Campo obrigatório.
* **Descrição da solução**: Descreva o problema de negócio que a solução irá resolver.
* **Essa solução será disponibilizada para outros clientes no Marketplace?**: essa pergunta define o uso da solução. Se for uma solução de uso interno e exclusivo da empresa que a está desenvolvendo, o usuário deverá marcar a opção *Não, é para uso exclusivo da minha empresa*. Se for uma solução comercial, que será publicada no Marketplace, o usuário deverá marcar a opção *Sim, será comercializada*.

> 🚧 Atenção: Esta definição NÃO poderá ser alterada posteriormente. Certifique-se de que esse é o uso correto antes de continuar.

* Para usuários de empresas que não possuem permissão para publicar no Marketplace da Sankhya, a opção *Não, é para uso exclusivo da minha empresa* já estará marcada.
  * *Exemplo 1: Se você é um desenvolvedor de um cliente Sankhya, e está desenvolvendo uma solução de uso interno para a sua empresa, esta é a opção correta.*
  * *Exemplo 2: Se você é um cliente Sankhya e contratou uma empresa terceira para desenvolver uma solução de uso exclusivo e interno no seu ambiente, você deverá criar uma solução de uso exclusivo. Ao adicioná-la a um grupo na etapa seguinte, certifique-se de que o desenvolvedor externo contratado esteja vinculado a tal grupo e com as devidas permissões de acesso.*
* Para usuários de empresas que possuem permissão para publicar no Marketplace da Sankhya, a opção *Sim, será comercializada* estará disponível.
* **Quais grupos essa solução vai atender?\*** : Escolha os grupos que terão acesso a essa solução. Os grupos disponíveis ficarão visíveis após a classificação da solução como uso comercial ou exclusivo.

Após preenchimento dos campos, o usuário deverá clicar no botão "**Criar nova solução**".  O usuário será redirecionado para a tela **Detalhes da solução** , onde poderá adicionar componentes e iniciar o desenvolvimento.

### Editar a solução e adicionar componentes

Agora uma solução pode ser composta por diversos componentes, como por exemplo add-ons e API Gateways.

Ao criar uma nova solução, será necessário adicionar os componentes desejados separadamente.

> 🚧 Os componentes criados não poderão ser excluídos posteriormente.

<Image align="center" src="https://files.readme.io/af50682a4e589262435012f3d48a0e22d7e05d09902eb9030bba742c93a5b374-Portal_Dev___Detalhes_da_solucao.jpg" />

Ao clicar no botão **Adicionar componente** , o usuário será redirecionado para a tela **Criar componente**.

O **tipo de componente** selecionado determinará as informações exibidas no formulário e as abas correspondentes. Para mais detalhes, consulte as seções dedicadas a cada componente nesta documentação.

<Image align="center" src="https://files.readme.io/41d067f1b6db1eb34a8260c23159d6d6698f3330ad52f1e2752778903139ed93-Portal_Dev_-_Criar_componente.jpg" />

**Clientes da solução (disponível apenas para soluções de uso comercial)**

A aba **Clientes**está disponível exclusivamente para soluções do tipo *Comercial*.

Nesta aba o usuário tem uma visão consolidada de todos os clientes possuem acesso à solução, independentemente da versão do Sankhya Om que os clientes estão utilizando.

<Image align="center" src="https://files.readme.io/090f14f3407beba26e61db648fa306019072b953f80e89fe79d9914eb5906c87-Clientes.jpg" />

Nesta aba é possível editar os clientes já existentes ou adicionar novos clientes. Para adicionar novos clientes, clique no botão "Adicionar cliente".

![](https://files.readme.io/8b836f3ae658331d3dc88c54c9003fcd22642bebe0ace4b3c494100b61b8e124-image.png)

<br />

> 🚧 Atenção
>
> O botão "**Salvar Alteração**" do pop-up "**Novo Cliente**" só será habilitado caso TODOS os campos obrigatórios forem preenchidos.

<br />

**Marketplace (disponível apenas para soluções de uso comercial)**

A aba **Marketplace** está disponível exclusivamente para soluções do tipo *Comercial*.\
Nesta aba o usuário pode cadastrar o anúncio da solução no Marketplace Sankhya, tornando-a visível para clientes interessados.

![](https://files.readme.io/d823955321cb5d2cf4f65cf5a1f354172858144dacd5c5032a452ccb2de178b9-image.png)

<br />

Na aba *Marketplace* o usuário pode:

* Criar um novo anúncio;
* Salvar como rascunho para finalizar depois;
* Publicar o anúncio da solução no Marketplace.

> ❗️ Criar uma solução do tipo Comercial não significa que ela ficará visível automaticamente no Marketplace.
>
> Para que isso aconteça, o usuário deverá cadastrar e publicar o anúncio na aba Marketplace, dentro da própria solução.

Para instruções detalhadas sobre como cadastrar um anúncio, consulte a[ documentação dedicada ao Marketplace](https://developer.sankhya.com.br/docs/marketplace-beta).

## Componente: Add-on

### Gerar uma chave de assinatura de um add-on

A chave de assinatura é um elemento crucial para garantir a integridade e autenticidade do seu add-on no Marketplace. Ela assegura que o add-on não será modificado após a publicação e, em caso de qualquer manipulação indevida, o autor será imediatamente notificado.

Para gerar a chave de assinatura, basta clicar no botão "**Assinatura do add-on**", conforme exemplificado abaixo:

<Image align="center" src="https://files.readme.io/e4d18329855d5fbeb174aafb01f75c0bfe8f197d77cc6e9b544c637b22e92c80-Portal___Chave_1.jpg" />

Feito isso, basta ler as instruções, aceitar os termos e clicar no botão de "**Download da chave**".

![](https://files.readme.io/b8d919f8915d98601d0981ffd9c29784697c174d4d2d273481dc519c9b760300-image.png)

Após clicar no botão, um arquivo será baixado para a sua máquina com o seguinte nome: "**sign\_key.key**"

> ❗️ Importante!
>
> A chave de assinatura é um dado sensível e deve ser armazenada com segurança. Recomendamos não compartilhá-la publicamente.
>
> Sempre que gerar uma nova chave de assinatura, certifique-se de alterar o arquivo ao publicar uma nova solução no Portal do Desenvolvedor.

### Gerenciar versões de um add-on

A aba "**Versões**", disponível dentro do componente tipo *add-on*, é utilizada para gerenciar e controlar todas as versões do add-on. Nela você pode cadastrar novas versões, manter um histórico de atualizações e definir qual versão deste componente estará disponível.

<Image align="center" src="https://files.readme.io/1fe14a545af83018880c6f6146e1d37664789a7e5b550e5bd63ae11cac96a272-Detalhes_componente_add-on_-_Versoes.jpg" />

Para criar uma nova versão, basta clicar no botão "**Criar nova versão**", que o sistema apresentará um pop-up com os seguintes campos:

* **Projeto**: Campo do tipo anexo para o upload do arquivo da solução.
* **Notas de versão**: Campo do tipo texto para detalhes referente ao histórico de alterações daquela versão, como as mudanças, correções e novas funcionalidades.

A flag "**Instalação somente em ambiente de teste**" permite instalar a versão apenas no ambiente de homologação (teste) do cliente.

<Image align="center" src="https://files.readme.io/0a472739068f540ce1e8c8a193da4d82a2d5a810075c65e5010d82b2aa8a1b95-Componente_add-on_-_nova_versao.jpg" />

Após preencher os campos, clique no botão "**Criar versão**". O sistema criará uma nova versão para sua solução com o status inicial como "**Desenvolvimento**".

<Image align="center" src="https://files.readme.io/3b152a6925761088afc115a096960b79a1b578d0c240137d9c1b397029850ffb-Add-on_-_desenvolvimento.jpg" />

Os possíveis status de uma versão são:

* **Publicado:** A versão principal que está disponível para o(s) cliente(s). Apenas uma versão pode estar com este status.
* **Inativo/Desenvolvimento/Homologação:** Versões que não estão visíveis para o(s) cliente(s), mas que podem ser utilizadas para testes internos ou disponibilizadas para clientes específicos.

<br />

> 🚧 Importante
>
> É possível criar uma versão diretamente pelo Add-on Studio, utilizando o comando ./gradlew publish -Pemail="seuemail" -Ppassword="suasenha". Com esse comando você cria uma versão de status "**Desenvolvimento**".
>
> Caso informe o argumento -PpublishPlace=true no comando acima, o status da versão será "**Publicado**".

<br />

## Compartilhadas comigo

No menu **"Compartilhadas comigo"** é possível realizar as mesmas operações de manutenção de soluções existentes no menu **"Minhas Soluções"**.

Neste menu, é possível editar as soluções nas quais você atua como desenvolvedor externo. Você pode criar novas versões, atualizar informações da solução e gerenciar os dados vinculados a ela. Aqui **não será** possível efetuar as seguintes operações:

* Criar novas soluções
* Gerenciar lista de clientes

<Image align="center" src="https://files.readme.io/78e3f143abb0cf3082f6d678da74c968bcaab6bb995e7eb5e98554eecdb1d53a-Compartilhadas_comigo.jpg" />

## Gestão de Acessos

Esta seção permite gerenciar os usuários com acesso ao Portal do Desenvolvedor e o que cada um pode fazer, através de um sistema de usuários e grupos de permissão. A tela principal é dividida em duas abas: **Usuários** e **Grupos**.

<Image align="center" src="https://files.readme.io/61cdfd123a64b74fb3502cce4d951311ad039dd24ba724f3bd2d05ecfc31d9f6-Portal_-_Gesto_de_Acessos.jpg" />

Dentro desse menu conseguimos efetuar as seguintes ações:

* Convidar um usuário
  * Editar as permissões do usuário
  * Remover o usuário dos acessos
* Criar grupos
  * Editar os dados do grupo

### Convidando usuário

Para adicionar um novo membro à sua área de desenvolvedor, clique no botão **Convidar Usuário**.

Na tela "**Convidar Usuário**", as seguintes opções estarão disponíveis:

* **Email:** Insira o e-mail do usuário a ser convidado. Para convidar múltiplos usuários, insira os e-mails separados por vírgula.
* **Atribuição do usuário:** Selecione o nível de acesso geral do usuário:
  * **Administrador:** Acesso total à gestão do portal.
  * **Desenvolvedor / Desenvolvedor Externo:** Acessos limitados, controlados pelos grupos de permissão.
* Clique no botão "**Salvar**" para enviar o convite.

Após enviar o convite, o usuário aparecerá na listagem de usuários na aba **"Usuários"**. Caso o usuário não possua conta no Sankhya ID, receberá um e-mail para realizar seu cadastro, e o status do convite ficará como **Enviado**, até que ele finalize o cadastro.

Após envio do convite para o usuário (para níveis de acesso *desenvolvedor ou desenvolvedor externo*), o usuário com nível Administrador deve:

* Adicionar o usuário ao grupo de acesso desejado.
* Confirmar que o grupo tem as permissões corretas.
* Se necessário, o próprio usuário Administrador deverá se adicionar ao grupo para acessar as soluções associadas àquele grupo.
* Para adicionar um usuário a um grupo, esse usuário já deve ter sido convidado ao Portal do Desenvolvedor.

Caso o usuário possua uma conta no Sankhya ID, o status do convite será ativo, conforme exemplificado abaixo.

<br />

### Criando grupos

Os grupos são a forma mais eficiente de organizar as permissões. Um grupo é uma combinação de permissões específicas, soluções vinculadas e usuários membros. Os usuários só conseguem visualizar e gerenciar as soluções que pertencem aos grupos dos quais fazem parte.

<Image align="center" src="https://files.readme.io/8dbc5fa704d92a631aed983e978333631f1eeaffbd3a83ad72fa5e3dbd70f548-Portal_Dev_-_grupos.jpg" />

Para criar um novo grupo siga os passos abaixo:

* Na tela de **"Gestão de acessos"**, selecione a aba **"Grupos"**.
* Clique no botão **"Adicionar Grupo"**.
* Preencha o campo "**Nome**" e selecione quais as permissões o grupo vai possuir. As permissões podem ser diferentes para Soluções públicas (uso comercial) e Soluções exclusivas (uso interno), conforme exemplo abaixo:

<Image align="center" src="https://files.readme.io/f0b85171c854f9ac73d86ac7d4575a3e32e533d816d10b0dd639db279f2ffea9-Portal_dev_-_editar_grupo.jpg" />

Após inserir os dados do grupo, vá para a aba **Soluções** e adicione as soluções ao seu grupo:

* Nesta aba você consegue vincular quais as soluções farão parte deste grupo. Os membros do grupo só poderão interagir com as soluções listadas aqui. Clique em **Adicionar** para buscar e associar as soluções.
* Além de adicionar uma solução, é possível também removê-la do seu grupo.

E por fim vá para a aba **"Usuários"** e adicione os usuários ao seu grupo:

* Nesta aba você consegue adicionar os usuários que farão parte deste grupo e, consequentemente, herdarão suas permissões e acesso às soluções vinculadas. Clique em **Adicionar** para buscar e associar os usuários.
* Além de adicionar um usuário, é possível também removê-lo do seu grupo.

Após configurar as três abas, clique em **Salvar** para criar o grupo.
