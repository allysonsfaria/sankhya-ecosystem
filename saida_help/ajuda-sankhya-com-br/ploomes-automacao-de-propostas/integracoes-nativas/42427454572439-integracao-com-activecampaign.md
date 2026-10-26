---
id: "42427454572439"
titulo: "Integração com ActiveCampaign"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427454572439-Integra%C3%A7%C3%A3o-com-ActiveCampaign"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:02:44Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6592686", "sync_hash_405f2e924426"]
---

# Integração com ActiveCampaign

Este artigo detalha o funcionamento da integração entre o Ploomes e o ActiveCampaign. Você aprenderá como utilizar as automações baseadas em webhooks para criar clientes e negócios no CRM.

## 1) Sobre o ActiveCampaign

O **ActiveCampaign** é uma plataforma de automação de marketing que permite criar fluxos de manipulação e ações com contatos captados. Através da funcionalidade de **Automações**, o sistema utiliza gatilhos (como a abertura de um e-mail ou a inserção de uma tag) para disparar consequências específicas, como o envio de notificações ou e-mails padronizados.

## 2) Objetivos da Integração

A integração entre o ActiveCampaign e o Ploomes tem como objetivo transformar leads gerados nas automações de marketing em oportunidades estruturadas no CRM, garantindo mais agilidade e eficiência no processo comercial.

Por meio do uso de webhooks, os dados dos contatos são enviados automaticamente ao Ploomes, permitindo a criação de empresas, pessoas e/ou negócios conforme a configuração definida.

Além disso, a integração conecta ações de marketing diretamente ao funil de vendas, possibilitando movimentações automáticas e garantindo maior padronização e controle, com definição de funis, estágios e regras para evitar duplicidade de negócios

## 3) Pré-requisitos

Para configurar a integração corretamente, certifique-se de possuir:

- **Conta Ativa**: possuir acesso a uma conta ActiveCampaign.
- **Acesso de Administrador**: permissão para criar e editar integrações plug-and-play no Ploomes.
- **Configuração de Gatilhos**: ter definido previamente quais ações no ActiveCampaign devem disparar o webhook para o Ploomes.

  ##

## 4) Escopo geral

## 4.1) Comportamento da integração

No ActiveCampaign um gatilho pode disparar diversos tipos de ações. Uma dessas ações é um webhook. Portanto, é possível criar uma automação que, a partir de um gatilho definido, envia informações do contato para o Ploomes através de um webhook.

Ao receber as informações do lead através da integração, o Ploomes pode criar um dos seguintes comportamentos, a definir pelo usuário:

**● Criar empresa, pessoa e negócio;**

**● Criar pessoa e negócio ou**

**● Criar empresa e pessoa.**

![Imagem 1: ● Criar empresa e pessoa.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191501630/45c8fb3012b6f3a4880ebdf7fa1b/unnamed.png?expires=1786536000&signature=e65f98b4596f7f956f7d49b5ae75d5acd75cfab6dde2742ee9af4a0d56bc3db6&req=diEuF8x%2BnIdcWfMW3nq%2BgSshNZMZ0iiCXv8247ekHQ9c9BzDWHcdfGaa9Yl1%0A%2B7prKcQnK40fAvrYAD4PzjVMjFc%3D%0A)

Caso a opção selecionada inclua Negócio, o usuário precisará preencher mais algumas opções:

- Estágio do funil de negócios para onde o lead do ActiveCampaign será enviado.
- Opção para impedir ou não que um Lead vindo do ActiveCampaign crie um novo negócio no Ploomes caso esse já exista e esteja aberto.

Conforme a imagem abaixo, a comunicação da integração se comporta de forma unilateral, isto é, sempre do Active ao Ploomes.

![Imagem 2: Conforme a imagem abaixo, a comunicação da integração se comporta de forma unilateral, isto é, sempre do Active ao…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191504509/0f530c307019f1195a126e31e289/unnamed+%281%29.png?expires=1786536000&signature=1dad8b69b08712494276d7f43b9454b1c138f5fcd648dda1062a1578e56a3989&req=diEuF8x%2BmYRfUPMW3nq%2Bgc2Qi05K25jIVU9YylUxK2qSccsPVD0%2BFgRilTTn%0AlV7zsbb0A2Tyy%2BemiGHRBRafi0Q%3D%0A)

## 4.2) Detalhamento do Escopo

No ActiveCampaign um gatilho pode disparar diversos tipos de ações. Uma dessas ações é um webhook. Portanto, é possível criar uma automação que, a partir de um gatilho definido, envia informações do contato e da conta para o Ploomes através de um webhook.

O usuário pode definir quais campos do ActiveCampaign vão ser enviados ao Ploomes. É possível passar as informações dos contatos e contas do ActiveCampaign para campos de pessoas, empresas e negócios do Ploomes.

Cada entidade integrada apresenta suas próprias particularidades e comportamentos. A seguir, cada entidade é detalhada com informações importantes.

**1. Cliente/Empresa**

As contas do ActiveCampaign são convertidas em clientes do tipo 'Empresa' no Ploomes. Existe apenas um campo fixo no mapeamento: o nome da conta no ActiveCampaign, que é integrado ao campo [Empresa.Nome] no Ploomes.

Mapeamento fixo de campos:

- Nome da empresa (ActiveCampaign) ⇔ Nome (Ploomes);

**2. Contato**

A entidade de Contato, por sua vez, está relacionada aos Contatos do ActiveCampaign, os quais são transferidos para o Ploomes como clientes do tipo **Pessoa**.

**Mapeamento fixo de campos:**

- Primeiro nome do Contato (ActiveCampaign) ⇔ Nome (Ploomes);
- Segundo nome do Contato (ActiveCampaign) ⇔ Nome (Ploomes);
- Email (ActiveCampaign) ⇔ E-mail (Ploomes);
- Telefone (ActiveCampaign) ⇔ Telefones (Ploomes);
- Cargo (ActiveCampaign) ⇔ Cargo (Ploomes);

**3. Negócio**

A entidade de negócio não possui mapeamento fixo, uma vez que o usuário tem a opção de escolher se deseja utilizar ou não essa entidade na integração.

## 4.3) Observações importantes

- A validação de duplicidade do contato é feita através do E-mail ou pelo Id (Active Campaign), caso o mesmo já esteja preenchido.
- A validação de duplicidade da empresa é realizada pelo **Nome**.
- Se o contato não estiver associado a uma conta no ActiveCampaign e a opção na configuração da integração estiver ativada para criar a empresa, esta será criada com o nome "**Empresa de [Nome e Sobrenome do Contato]**".
- Para uma integração eficaz com o Ploomes, sugerimos configurar os webhooks diretamente nas automações dentro do ActiveCampaign, conforme detalhado no tópico 5 a relacionado as [Instruções de Ativação da Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427454572439-Integra%C3%A7%C3%A3o-com-ActiveCampaign#h_2746ece034). Embora seja possível cadastrar webhooks em **Configurações > Desenvolvedor > Gerenciar Webhooks,** não recomendamos esse método para integrar com o Ploomes.

## 4.4) Campos personalizados

Assim como o Ploomes, o ActiveCampaign permite a criação de campos personalizados de diferentes tipos. A seguir, apresentamos a lista desses campos e seus respectivos tipos no Ploomes.

Recomendamos que sigam esse padrão para maior compatibilidade.

![Imagem 3: Recomendamos que sigam esse padrão para maior compatibilidade.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191575685/4b73918ba1f8abb639b4ff9c4ac9/image.png?expires=1786536000&signature=f61234a81e7af59a2baba1aa3f043ff9c3c20f00bb69fa4fd4a69ff994e41ba1&req=diEuF8x5mIdXXPMW3nq%2BgcrFAW45WwdEcSWccSYtuEtJzbyW75%2FjbTzAPMjo%0A1MrGea67h4Tss4m6wPxVj%2FheQKg%3D%0A)

## 5) Como integrar com ActiveCampaign no Ploomes

No Ploomes, acesse a tela de integrações plug&play, no menu de administração:

![Imagem 4: No Ploomes, acesse a tela de integrações plug&play, no menu de administração:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2120270600/9792d5d0c8a980e78d5ec8631a29/NwxtWehZEJ0sKKolfjLipltR2fNUAYeaiqYTWdXQdPWqvsG6hF14QRDa8eOiLa14x-h7PjCS9d5oN2I9uLB_nU0J2BHoU5db6zaMaMfudIcxSd8iHsWS2ICrQmjkkym8tdKD43r1-3Ds0?expires=1786536000&signature=4b4b80e92a43c519a1ff2091070d0603f2e70a271ce7dadd12c2a281a038e749&req=diElFst5nYdfWfMW3nq%2BgaNNExdcFVJqz35SOlCnhEsyIymSkDovfKDzrg08%0AKa98KxR8m6JseF3UU9R8KnmRfxI%3D%0A)

1. Selecione ActiveCampaign

   ![Imagem 5: Selecione ActiveCampaign](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2120270607/49ff5b3d2ed2e93b9400ce1cc748/mceclip0.png?expires=1786536000&signature=1cb5f4059c6f86d6db28a84268f4fce4242b1fa0750b33231b1ff3616ea3e5fe&req=diElFst5nYdfXvMW3nq%2BgT70vqct08QB3HWpoCF3rl7VS4AdQk3r72yewuGp%0ARsEQN4k84YHICj%2FaNf%2BRjwGSHTY%3D%0A)
2. Clique em "Habilitar integração", e depois em "Autorizar integração".

   ![Imagem 6: Clique em "Habilitar integração", e depois em "Autorizar integração".](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191537748/c5abdb9bc8b80a08300fe62c944b/unnamed+%283%29.png?expires=1786536000&signature=1a99b2e6c648bc555b3d3d246ab397295ef137a64b76fd5c711cefcd47d1ca6e&req=diEuF8x9moZbUfMW3nq%2BgRMNW6NFMmhoaIDZArJlDy58D9eNL8pocjoucXHj%0ALvIsJPv4SrpufjnvrtK2Cr%2BeCp0%3D%0A)
3. Entre em sua conta no ActiveCampaign. No menu lateral, entre em Configurações > Desenvolvedor, em seguida, copie a URL e a Chave.

   ![Imagem 7: Entre em sua conta no ActiveCampaign. No menu lateral, entre em Configurações > Desenvolvedor, em seguida, copie a URL…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191538220/2f90713ba4fc551ca5d0512e7030/unnamed+%282%29.png?expires=1786536000&signature=8d0588cdcfa01478159c13093f470b7f9e308de8c23ae09370750bb1cde0a33d&req=diEuF8x9lYNdWfMW3nq%2BgQ2G4AM3YdyY1I4VKhFaewZUz%2BEJv12O5SeRYwvt%0AJ%2Bjwo1en2LBwo44r5%2FGP9CSYs24%3D%0A)
4. Volte ao Ploomes e clique em "Autorizar Integração". Isso abrirá uma nova guia, onde você deverá inserir a URL e a Chave copiadas anteriormente. Após isso clique em “Confirmar”.

   ![Imagem 8: Volte ao Ploomes e clique em "Autorizar Integração". Isso abrirá uma nova guia, onde você deverá inserir a URL e a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191540461/a3242f8fc90a69e08b49a80ab28f/unnamed+%284%29.png?expires=1786536000&signature=590851cc767c3bed10545bb4a663575ec632a05a2a52ae811a6e4415a0b8d4ac&req=diEuF8x6nYVZWPMW3nq%2Bge8JeagGOopoJrUc4xf6rGUkJEnV2LXWU%2FOjC7tt%0A%2FuygEe7GlembFyhXKCbBsyI5%2Bg0%3D%0A)
5. Configure o mapeamento da integração

Nessa etapa define-se quais entidades serão criadas no Ploomes a partir dos contatos vindos do ActiveCampaign. O usuário pode escolher entre as opções abaixo:

![Imagem 9: Nessa etapa define-se quais entidades serão criadas no Ploomes a partir dos contatos vindos do ActiveCampaign. O…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191542606/6ae4737f910a9417d593d7a55cff/unnamed+%285%29.png?expires=1786536000&signature=369d3f1daf270401fa25cc84f7010ee22e0fefb2edffe244006bbd69c440376f&req=diEuF8x6n4dfX%2FMW3nq%2BgU0MxMZIUnH1w9tgj3rMQUqOGae%2BOCeV2Hu2Mw0u%0A5Cb2wyZZRS%2BwEy5eo41Ie39vJAA%3D%0A)

Se optar por criar negócios, você deverá informar em qual estágio o negócio será criado e se a integração irá criar negócios caso já exista um aberto para o cliente.

![Imagem 10: Se optar por criar negócios, você deverá informar em qual estágio o negócio será criado e se a integração irá criar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191547534/eb09bc7056ae4062994dad170007/unnamed+%286%29.png?expires=1786536000&signature=847f92f5588582eb96ddc6ca99f2aa94f6452a80f710d1da6f9351244e5c6d05&req=diEuF8x6moRcXfMW3nq%2BgVdxfxXRc7yMdKJP2oOGCiqdCdc19RHe5ATDU6p%2B%0AuNsmmB%2FogIoOCyvTQkMliUx9Z6E%3D%0A)

6. Após finalizar a configurar, clique em "Ativar integração":

![Imagem 11: 6. Após finalizar a configurar, clique em "Ativar integração":](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191551089/17b57cbe8f7968b515e706bc36a8/unnamed+%288%29.png?expires=1786536000&signature=bd44f15e85deed5747c90fe6784fa3523315bc92c8026d7414f7597680f840f3&req=diEuF8x7nIFXUPMW3nq%2BgWH3Wq0EC2lMN73Y%2Fvi73v8luxgJRdBvgRUUJuGl%0A4m65ye8ead60t1l0VR86qneSDNA%3D%0A)

7. A URL de callback da integração entre Ploomes e ActiveCampaign é exibida. Copie-a para adicionar à automação no ActiveCampaign.

![Imagem 12: 7. A URL de callback da integração entre Ploomes e ActiveCampaign é exibida. Copie-a para adicionar à automação no…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191552860/668f5f4ab3e6a3ee8e7b90480dc6/unnamed+%289%29.png?expires=1786536000&signature=db7d56322fb683b425ce67f0d7f72ea33b17939e2ff0a21c6ac5f59d3ec2c370&req=diEuF8x7n4lZWfMW3nq%2BgabA79YcMIxcp%2Fr6l7NaVucAzXcJcfMxH6Q5NEMP%0AUpJhNglbl5UiXD0D31R5ikpG3uo%3D%0A)

## 6) Como criar uma automação no ActiveCampaign

1. Volte em sua conta no ActiveCampaign. No menu lateral, entre em Automações, em seguida, clique em “Criar uma automação”.

   ![Imagem 13: Volte em sua conta no ActiveCampaign. No menu lateral, entre em Automações, em seguida, clique em “Criar uma automação”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191554121/4ac68973c3e8a155b751ee034fdc/unnamed+%2810%29.png?expires=1786536000&signature=74f348967ed5a56ce1ce558e1698dd039dc00a676edfba4eb565a070ed908ba3&req=diEuF8x7mYBdWPMW3nq%2BgT4JUyoNkO4ekZU96765B4q%2FKrs%2Bp3FA919GAG%2Fh%0AmZvZipSI5RIX4QEI1BVkwm4Ac1w%3D%0A)
2. O sistema vai fornecer alguns modelos de automações prontos. Para facilitar a
   explicação, este exemplo vai usar a opção de “Começar uma automação do zero”.

   ![Imagem 14: O sistema vai fornecer alguns modelos de automações prontos. Para facilitar a explicação, este exemplo vai usar a opção…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191556424/769ae4300bd871ace7b95370d665/unnamed+%2811%29.png?expires=1786536000&signature=0c9134083ac45f98f0626e8c1a5d858d292d67b1e0cde204e834852ea58515b4&req=diEuF8x7m4VdXfMW3nq%2BgTn3iJZLRV2KHLTxyrvETq07z7phgBD7HZMs3sy9%0A0rRy%2FCbAogEB1lcepfG4%2BL%2Bi65Y%3D%0A)
3. O sistema vai pedir para criar um gatilho para seu fluxo. Crie o gatilho conforme
   desejar.

   ![Imagem 15: O sistema vai pedir para criar um gatilho para seu fluxo. Crie o gatilho conforme desejar.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191557081/30a9eaf16688d529cef751e66658/unnamed+%2812%29.png?expires=1786536000&signature=271818ada19961d0c706bfbadef40161fb6bf5c0373fcae3166400c4b428296b&req=diEuF8x7moFXWPMW3nq%2BgbIAfq9z2WdxMuws5NspiX5832fhMCAAFH%2BIJs0i%0AEP%2BpCOXT%2Bx5QWQnppca0c5e0tuk%3D%0A)
4. Depois, será a hora de adicionar uma ação. Escolha a opção “Condições e fluxo de trabalho” no menu da esquerda. Dentro das opções selecione “Webhook”.

   ![Imagem 16: Depois, será a hora de adicionar uma ação. Escolha a opção “Condições e fluxo de trabalho” no menu da esquerda. Dentro…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191558208/d6826387bfce50cdf85994ac4cd7/unnamed+%2813%29.png?expires=1786536000&signature=e1872c338cdc074ffb324cb5bfd8f031db85bb0800aba1b2fed2192adfc8332e&req=diEuF8x7lYNfUfMW3nq%2BgdfKWIY8uiK9g%2BdEGtKOptTrfudIkxyzETm9gB70%0AKSm3NgpAopuP9teJS%2FOqehjNjcU%3D%0A)
5. No modal que foi aberto, cole a URL de callback que você copiou do Ploomes e clique em “Salvar”.

   ![Imagem 17: No modal que foi aberto, cole a URL de callback que você copiou do Ploomes e clique em “Salvar”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191559296/1f80dcfdb410d5d387682d1b8e63/unnamed+%2814%29.png?expires=1786536000&signature=d9cb1314e1e5b4ec390faf65301b3d56eb262d9658653e773e34480b39c52d29&req=diEuF8x7lINWX%2FMW3nq%2BgYxKRd7FiFty7dryCUbq0p%2BzTWADuZp%2BmzrkO9Ps%0A%2BpHvNvxJNJ1pJFQVsUwlo3PuUkE%3D%0A)
6. Nomeie sua automação como desejar, salve e clique em “Ativo”.

   ![Imagem 18: Nomeie sua automação como desejar, salve e clique em “Ativo”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2191560295/9b2ab5d0da3771aa397639fe3213/unnamed+%2815%29.png?expires=1786536000&signature=085911688af264ebd339f4e5820243cd1b09fab3512d01216671b72df92cb19d&req=diEuF8x4nYNWXPMW3nq%2BgVLvXr%2B9s1PNYOCwKJhT574%2BKgK7gtpR6xetd9AG%0AHr2kGKBmtDhQhxF8S%2BmokOyEN1U%3D%0A)

Pronto! A integração está agora totalmente configurada e pronta para ser utilizada.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 19: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1420816492/88aa9f7f1f579985114acb367be1/Integra%C3%A7%C3%A3o+-+ActiveCampaign.png?expires=1786536000&signature=3f3c0525b95cc1d8d722740bae29c880e50a07e57fb07d41ae2b8c411c67ac70&req=dSQlFsF%2Fm4VWW%2FMW3nq%2BgenTj%2FoyUrywiJEuwDX1iKWmoHKiCtDYcsFNkUgj%0AIWxTI9Um%2BvPhjpeyWsKQ331wEmY%3D%0A)](https://universidade.ploomes.com/courses/integracao-active-campaign)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com)
