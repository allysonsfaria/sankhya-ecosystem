---
id: "42427413780247"
titulo: "Integração com o RD Station"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427413780247-Integra%C3%A7%C3%A3o-com-o-RD-Station"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:06Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452447", "sync_hash_92bbb3da7507"]
---

# Integração com o RD Station

## Por que integrar a solução ao Ploomes?

Por essa integração, você envia os leads gerados no RD Station ao Ploomes de forma automática, bem como informa ao RD Station o resultado da prospecção de cada lead para que possa analisar de forma efetiva os resultados de suas ações de marketing.

## Casos de Uso da Integração

Com essa integração, você pode configurar o envio de leads do RD Station para o Ploomes quando uma oportunidade for marcada ou ao realizar uma conversão, realizando assim um fluxo de entrada.

As informações dos leads são distribuídas no Ploomes entre pessoa (dados como nome, cargo e informações de contato) e empresa (dados como nome da empresa, setor e nº de funcionários).

Também existe a opção de criar um novo negócio para esse lead, para que assim se inicie o processo comercial baseado no funil de vendas do Ploomes.

As configurações da integração permitem criar também um fluxo de envio de informações do Ploomes para o RD, ou seja, um fluxo de saída. As possibilidades são:

- Quando um contato for criado no Ploomes, criá-lo no RD Station como lead caso esse ainda não exista;
- Quando um negócio for fechado (gerando uma venda ou perda), criar o lead no RD Station (caso ainda não exista), baseado no contato do negócio referente no Ploomes;
- Mudar o estágio do funil de lead para cliente no RD Station quando uma venda for registrada no Ploomes;
- Mudar o estágio do funil do lead no RD, de acordo com a escolha do usuário, quando uma negociação for perdida.

**Seletor de funil para engatilhar criação de venda no RD Station**

Ao inserir a opção “Ganhar card” ou “Ganhar proposta” no campo “Qual ação no card do Ploomes gera uma venda no lead referente do RD Station?”, será exibido abaixo o campo “Selecione quais funis engatilharão o comportamento acima:”, que permite a inserção de funis da conta.

![Imagem 1: Ao inserir a opção “Ganhar card” ou “Ganhar proposta” no campo “Qual ação no card do Ploomes gera uma venda no lead…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1454966357/6366f1c1c452bb86286ad2381241/AD_4nXcRD6blVgU-iyQ5F1j7q0MUJ2tdfuNEl7_CHn5PTyZz7asUEu9RY-UNmWk3pt784vDEGlgaP7dZDFIymhPmaumhHcd9YaOt6ozxHGhTVwMIrEBMmKaoHI_e36xN24IOhFs323_WvQ?expires=1786536000&signature=b679fcf2a842a171f132a0f1c20e19e3e1b9f56db1e90d9c4d6637aad274d52e&req=dSQiEsB4m4JaXvMW3nq%2BgUdyHikXClInkyoqBWpNL4hxFdIvgRLZM60H9rEv%0AI%2B22cmZj%2B5mNUF%2FLXdiHKgCoZyI%3D%0A)

Os funis que estiverem dentro do campo serão aqueles que ao terem a ação selecionada realizada criará venda no RD Station. Caso não haja funil selecionado, todos serão considerados.

## Tipo de Integração

Esta integração envia dados do Ploomes para o RD Station e do RD Station para o Ploomes, portanto é uma integração de entrada e saída de dados.

## Possibilidades da Integração

A integração permite que os leads registrados no RD Station Marketing sejam enviadas diretamente para o Ploomes, por conversão, marcação de oportunidade ou URL de Callback. Os leads são registrados como pessoa, empresa e, caso o usuário escolha, novo negócio.

Caso o dono do Lead esteja preenchido, o vendedor responsável será notificado diretamente no CRM. Além disso, é possível escolher em qual funil e estágio do negócio cada lead será direcionado dentro do Ploomes.

Todos os campos do RD Station, sendo eles personalizados ou padrão, podem ser configurados apontando para campos do Ploomes, assim garantindo uniformidade de dados nos dois softwares.

Após o processo de venda referente a um negócio no Ploomes ser concluído, todas as informações retornam ao RD Station Marketing.

Quando uma negócio é ganho, a integração retorna o valor da venda, move o Lead para o estágio do funil Cliente e atualiza os valores dos campos personalizados que foram alterados durante o processo.

Em caso de perda de uma oportunidade, o motivo da perda é registrado no motivo de perda de oportunidade do Ploomes e ainda pode ser atualizado em um campo personalizado criado no RD, o que permite criar uma segmentação para um fluxo de automação de recuperação da oportunidade perdida. Os valores de campos alterados durante o processo também são atualizados no lead do RD Station.

No fluxo de saída de informações, é possível também criar um novo lead no RD a partir de um contato criado no Ploomes, ou não em sua criação, mas apenas quando esse passar por um ganho ou perda.

## Observações importantes

- Somente contatos do tipo pessoa serão atualizados no RD Station! Um negócio ganho ou perdido de uma empresa no Ploomes, por exemplo, só atualizará o lead referente se esta empresa tiver um contato vinculado ao Ploomes.

- A verificação de duplicidade é realizada com base no e-mail do lead. Se um cliente do tipo pessoa com esse e-mail já existir no Ploomes, ele será atualizado com as informações mais recentes em vez de criar um cliente novo. Isso garante que os dados do lead sejam mantidos atualizados no sistema, evitando duplicatas desnecessárias.
- Caso o usuário não realize o mapeamento de nenhum campo de negócio, por padrão será criado com o nome ‘Oportunidade do RD Station’.
- A entidade de negócios funciona de forma unilateral, só recebemos as informações do RD Station, não enviamos nada para lá.
- Sempre que um evento é convertido, um registro de interação é automaticamente criado dentro do Cliente/Negócio no Ploomes.

- Uma observação importante a ser considerada é que atualmente não é possível utilizar o campo "URL Pública" no Ploomes devido a uma limitação da nova API de webhooks do RD Station. É possivel verificar essa mudança através desse [link](https://developers.rdstation.com/reference/como-migrar-webhooks-rdsm?lng=pt-BR#observa%C3%A7%C3%B5es-importantes).

- Por padrão o campo ‘Responsável’ é preenchido com o valor do campo ‘Dono do Lead’, só que esse preenchimento tem suas peculiaridades que são:

  - No processo de preenchimento do campo "Responsável" no Ploomes, é utilizado o valor do campo de e-mail presente no campo "Dono do Lead" no RD Station. É realizada uma busca nos usuários do Ploomes para verificar se existe algum usuário com o mesmo e-mail. Se um usuário com o e-mail correspondente é encontrado, esse usuário é designado como responsável pelo cliente no Ploomes. No entanto, é importante destacar algumas peculiaridades desse comportamento:
  - O preenchimento do campo responsável irá ocorrer em Empresa, Pessoa e Negócio(caso escolhido na configuração).
  - No caso de uma empresa no RD Station possuir mais de um lead integrado, o campo "Responsável" dessa empresa no Ploomes será atualizado com base no responsável do último lead criado. Para isso, é verificado se existe um usuário cadastrado no Ploomes com o mesmo e-mail do responsável do último lead. Se houver um usuário correspondente, esse usuário será designado como responsável no Ploomes. Caso não haja um usuário cadastrado com esse e-mail, o responsável permanecerá o mesmo do lead anterior.
  - No caso de um lead ser criado sem o preenchimento do campo "Dono do Lead" ou com um e-mail nesse campo que não corresponda a nenhum usuário registrado no Ploomes, porém possuindo informações de uma empresa, ao ser integrado no Ploomes, o campo "Responsável" será preenchido com base no responsável designado para essa empresa no Ploomes. No entanto, em relação aos Negócios, o campo "Responsável" permanecerá vazio por padrão.
- Anteriormente, a origem do lead era registrada apenas quando o webhook resultava de uma conversão. Agora, mesmo que o webhook não esteja associado a uma conversão, verificamos se houve uma conversão anterior. Se houver, essa informação é preenchida em inglês. Por exemplo, uma origem desconhecida será registrada no Ploomes como: Unknown | unknown.

## Passo-a-passo: Como realizar a integração

## No RD Station

No canto superior direito da tela do RD, clique no nome de sua conta.

Após isso, clique em integrações.

Na tela de integrações, no canto superior direito, logo abaixo do nome da conta, clique em Pesquisar Integrações.

[![Imagem 2: Na tela de integrações, no canto superior direito, logo abaixo do nome da conta, clique em Pesquisar Integrações.](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330532/2c84cce1a5f12eae5bebd486/upload_4392286031967817765?expires=1786536000&signature=513984784e3efe96ab71451cb5571271c80fdfc6f4e3a002e5f382b77ca41d5c&req=dyYuFcp%2BmIJdFb4V1XW4gSZNyCcJiN7eKUykSlyCivMVmXmjeQlMpYNoPOCX%0AWQcjrD5uMDqu4oMsrAIo0R3Ayw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148317/f9df3cb4498b23c01fe7c452/TDCJhg9zpvqO3DyUP0QIWKyiwTAsAAhbmcP5sONBo5MMuUMLtkJqUS16IrJ8tzVvprB60Af7Sy3EvLHkvwecVVjYLSoc9nzVjHUVjopE6l-ByyKwKIu7O4GUFnJms_SKCJe8hr0l?expires=1619802000&signature=86d939a274adece9239028132bf9dc31e41325d3c35d5de59d0827d28d42bfee)

Então, na [App Store do RD Station](https://appstore.rdstation.com/pt-BR), clique na categoria CRM.

Após isso, procure por Ploomes e habilite a integração.

No Ploomes:

**Primeiro passo**

Dentro do Ploomes, acesse o módulo em Administração e clique em "Integrações Plug and Play":

![Imagem 3: Dentro do Ploomes, acesse o módulo em Administração e clique em "Integrações Plug and Play":](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330542/31452b9e4783f6a333fb1f8e/mceclip0.png?expires=1786536000&signature=3a01a0fcfc82dc2c6899df101ffc74bb0309c7342d64dc50900b19dee9b08862&req=dyYuFcp%2BmIVdFb4V1XW4gZlqQ%2B5KcaDpJzaxT8CmK3zNXgOOXafeKti80eaK%0A71uaUoWHI1QhuHUR%2FY69bmL19g%3D%3D%0A)

Agora, selecione a opção “RD Station”:

![Imagem 4: Agora, selecione a opção “RD Station”:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330552/193d721ea8bf52a25b23e085/mceclip1.png?expires=1786536000&signature=919750d7b015c60d5c4583ebecdefcab324275c045d069093cf51b74fcf0a033&req=dyYuFcp%2BmIRdFb4V1XW4gdYbcKrSQeYOUWhQbp4EB6dAu1SyNt30cZ51wYlm%0Au2X9E7dFx5xkP5U96laB2XZEMw%3D%3D%0A)

**Segundo passo**

Clique em “Habilitar” > “Autorizar integração” e escolha qual é a sua conta do RD Station na qual deseja que a integração seja habilitada:

[![Imagem 5: Clique em “Habilitar” > “Autorizar integração” e escolha qual é a sua conta do RD Station na qual deseja que a…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330558/0698a269d7325b5df947444d/upload_13976730747214580325?expires=1786536000&signature=e5dbacfe355eb6aba30ad0b933567821afbe7caca0e7936977c90586e2809347&req=dyYuFcp%2BmIRXFb4V1XW4gegugLJt2eImUF1vbKCksXpEIUmWxYhyLTOBmwhw%0Ambf4SK40xZu7hfbWKmztEG1EwQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148335/a1ef4f78d11b643d33a1d9d6/Q9avqoDpf2SRyg8CJhOrRS9HKmckaxUJ-MeIX29iwN6g8w8a-kxRPq44rgjIS-WPOGkpje10GtTUqBoeOxS3S-CdroaXukevS-gEqDmBatA4htu7UWFXXCUGjlh8DPKC_1Oglxr0?expires=1619802000&signature=1b393790ea7035c8f91f88488544610ac0ae001766186056d51439780ca1c884)

**Terceiro passo**

[![Imagem 6: Terceiro passo](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330566/0a892500c3b2d7243f87c41f/upload_12869689144268619373?expires=1786536000&signature=2d8f4d3ba46b7b9e8c4ad9b32fc7bfd19b894a64c690d469e949b7765e73bd09&req=dyYuFcp%2BmIdZFb4V1XW4gf30irvRKdxViCilAPFRbM4TlVjbVDi1qgIui9%2FA%0AdQOQ45cv%2Fmt4kK8ZrmxyohkNiA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148338/fea8ea4eff5192a47622c10b/UCMoJJmFzsSBqL67X_z9oVsjCwfMsSGQ0PwiCyq7X7gVkyO1cjluoKfIIzNjeL09UB0tb-sj0aNzuPq5ZeRwRcidKgBbLnuuENi1Z5MgYW8hh2nxPU-_UYz0CpsDKP1QGcAGwXaU?expires=1619802000&signature=ccdb2a1742de91141272e2e7356243b53f6e0dc8c160f71197fa21a0cad968fa)

Pronto! A partir daqui, a integração já está habilitada. Entretanto é necessário configurar o comportamento da aplicação.

[![Imagem 7: Pronto! A partir daqui, a integração já está habilitada. Entretanto é necessário configurar o comportamento da…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330574/a33d6da5978b372bfdf2c3fb/upload_15148063712936882671?expires=1786536000&signature=b6e1ff7d27b05f55a9a547d13333ed864732835fc0428befc6b908373b61d113&req=dyYuFcp%2BmIZbFb4V1XW4gYL29a2sWErXlIW%2FUmbGBTVeTEwz6MF76G9bbqaU%0AleWMBkUHH6cKMn7dRj6%2BqahHpQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148340/7273cd0b7ddd905998a74eea/gbtXArHNlYi03ByCUvOKFGgBcOijEDuKWtcRPnWOa66m84V8qEgD-XWZyzuLouARMRlkGbjNg5_8s4EYgmH_fYvYy4Sk060CFd7ZWvYQAgNh7rpsMHP2-IPGzR4-bkJH97X5azx7?expires=1619802000&signature=fc2b8bd2d9ce7907bc1680ac813d4b8fc965d975b033ca06d884db6ef99383d1)

Primeiro é necessário definir quando os leads serão enviados do RD Station para o Ploomes: quando converter ou com marcação de oportunidade.

Nessa etapa existe também a possibilidade de, caso o lead do RD não tenha empresa cadastrada, criá-la no Ploomes com o nome “Empresa do [lead]”. Isso porque a entidade “empresa” precisa ser criada no Ploomes de qualquer forma.

**Quarto passo**

Nessa etapa define-se quais entidades serão criadas no Ploomes a partir dos leads vindos do RD Station. O usuário pode escolher entre criar uma Empresa e Pessoa, ou uma empresa, pessoa e negócio.

Aqui também define-se para qual estágio do funil de negócios os leads do RD Station serão enviados quando a integração ocorrer.

[![Imagem 8: Aqui também define-se para qual estágio do funil de negócios os leads do RD Station serão enviados quando a integração…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330587/59a056cbb1b55e64ef96ca2d/upload_15980934843179132376?expires=1786536000&signature=696356b4bef5d52ea61d7a7c357d71304a7c2dbfc72678e883821e7c03156bda&req=dyYuFcp%2BmIlYFb4V1XW4gToN%2FJth%2B1HYzCAlSg7hiMdSetkMiHyWuE48E%2BcX%0A79sG%2FOps1gmLZmszXSdhhnLqZA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148341/c6296afdc9ce3c29caea8668/1Tpl-ZTMLJRTsDPzi1_QmD06jPnICwjpKwPrycL3NGjPLLB0mnTPKQM3kugCFgdRYPFOaVPP0kK8z-nYjJ4HJcorw0dCMRqbIeG_a7LzNHTJVNhJMAl5KZ94n7I8bIND2gwgWBsu?expires=1619802000&signature=a51677d6f4c1b320c67982021298c658047daf9da5b91f6f3ae52c3994b5dbec)

**Quinto passo**

O passo seguinte serve para configurar, principalmente, os fluxos de saída. Ou seja, as configurações de envio de informações do Ploomes para o RD Station.

[![Imagem 9: O passo seguinte serve para configurar, principalmente, os fluxos de saída. Ou seja, as configurações de envio de…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330597/ef429bf293bfc16a9f82501b/upload_3576139568905763440?expires=1786536000&signature=9080d65dc01c6fb6938a7fc183a8f9c67d56be582bc308447e4f0570dc6ce5a3&req=dyYuFcp%2BmIhYFb4V1XW4gQPwrorhOZMzzuffpJ3IO6MVv7Uu5SLD9%2BiV2FFv%0AhC26Vzf7Kr%2B7JbvRKhwZ5kFNbw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148344/0a47bff82902b84bc631c5e6/skM0ttQT4aUqpEhrlWPI4d_c-YwAdvBJSrQR7rULeQM78Yn4FrAWOnuFcJYsKpPsyYK0OqDngciulp3wfwlmHlampaPw_Ir25RlOciJTJZUr_Brh4KEI8HnnYxbMf2hMzzOuxwJ-?expires=1619802000&signature=2b3d9884a1c05eaa7fe52735afbbf1d7f24df9417709de02655e4bc1e2fcee7a)

**Sexto passo**

[![Imagem 10: Sexto passo](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330603/df3419bef78f6e0d4f74ad12/upload_9276200588702337343?expires=1786536000&signature=510f40ab2c95490bf098263aa99d623d968a327210ad465764f9dd591e0207e4&req=dyYuFcp%2Bm4FcFb4V1XW4gWeODq%2FAfX7L8UuEts0CmcZ9KGuOLrVqGhWyGYyG%0ApyQEUpfzuYnArRTGXw6Y56QKQA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148354/d4e4f41b0167defe6782d960/zt4OM4dFEw9VlgDwEkxOpT4d-iBNfadPGdiSg2arq86uUrZwm2QjNhlDBhNEnMr7gNHZJB0-h8JudwsXk-U2N39_og_Us2fbrnHU7a1O0m-Do7NuynYngVHNiSc_p4KWHGxZYp6y?expires=1619802000&signature=e3c33fc59a89f8bc89ee72745fd03b201c9dd7d00dccc862d3ec7a8d19029102)

O passo seguinte também está relacionado aos fluxos de saída. Aqui estão as configurações voltadas a como o RD deve ser alimentado quanto aos fechamentos de negócios no Ploomes.

- Definição de qual ação no negócio do Ploomes gera uma venda no lead do RD: Nova venda em estágio, ganhar negócio ou ganhar proposta
- Em estágio da venda, define-se qual estágio no Ploomes marca a venda no RD: Aguardando pagamento ou pagamento realizado

Também são definidos o estágio do funil do RD Station para qual o lead é movido quando uma venda é fechada ou perdida no Ploomes. É possível mover os leads para Cliente, Lead ou Lead Qualificado.

**Sétimo passo**

[![Imagem 11: Sétimo passo](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330616/a30cfdb85ff1e6209c6c6b24/upload_1214382078919078233?expires=1786536000&signature=d689f13ac9521059cbab9a9cea088fa5cdc9bb131c3c5c438456f6a95ec2a7c0&req=dyYuFcp%2Bm4BZFb4V1XW4gcbmVcA%2FN2ZdFAVaegK%2FQBX0rGH2OLaWC57%2FVIXP%0AMe5KRH2xLFR6%2B4SZBhL2N1dMBw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148357/7be41938f077309747b1db41/NRTjPHNQKrkcfRXZ6o01Tkj7t_rBEsxQlervI3o3zerWThqmX0H-rKUpu_aZ88CH3x2klblIxvsz6IA4dvq50alJDXKtpAW9LQt2-Ts-vYluvCfn51laD9CN4WclpTSU9hJm-s4T?expires=1619802000&signature=cb63b0a01f5d52a8dee3f806ada6f2d071011cb6cc44e37456258bb9fcdfadb1)

Por fim são feitos os apontamentos de campos do RD Station para o Ploomes. Os campos padrão, como nome, e-mail, telefone e celular já apontam para os mesmos campos no Ploomes.

Os outros podem ser definidos de acordo com a necessidade do usuário. Campos personalizados, criados no RD ou no Ploomes, podem ser adicionados nas combinações.

**Oitavo passo**

Por fim, é exibida a URL de call-back da integração entre Ploomes e RD Station. Esta pode ser adicionada nos fluxos de automação do RD para mover leads de forma baseada nos fluxos.

[![Imagem 12: Por fim, é exibida a URL de call-back da integração entre Ploomes e RD Station. Esta pode ser adicionada nos fluxos de…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330624/3043cdad4a6a26cee9ec89c6/upload_2311227094936831692?expires=1786536000&signature=cd59d8c4bf2d91a51a7485e92924ef019ae5af8100114fc80ba7a68f622452e7&req=dyYuFcp%2Bm4NbFb4V1XW4gV4enNrF0PLRQ42G5HaZjkFz2MSxbGjs5hOf95gr%0A0SqftSlJE54QSRy9havJVzMUcQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/101148363/4c2ce91b5ef98dbf6b4a08bc/GtVmZQ2TRBVTLkTU9SoFwNHnLI1J5fUa--4s_rmhi7mrw7HxT0xqqBx4rPaL8nPik03jt6uXMt7tCVb7lVGscanWrMQR-5tJao3qEH71fUbaz0xS_Pf7nKZlVwr5_THKCq3q-pg1?expires=1619802000&signature=2702aedb17564d81a9dbe49f75a3a3a079c6886390ebf8fbebbdd152502b3c8d)

- Na integração temos a opção de impedir que um Lead vindo do RD crie um novo negócio no Ploomes caso esse já exista e esteja ativo. Esse card ativo é um card em "aberto".

![Imagem 13: Na integração temos a opção de impedir que um Lead vindo do RD crie um novo negócio no Ploomes caso esse já exista e…](https://downloads.intercomcdn.com/i/o/808241792/eb69227623d2317e9d78cf27/Untitled.png?expires=1786536000&signature=e88d893fbadba8b505442c1aad532771ca2ab71f0e956c8e78f31d999805a177&req=fCAvFM1%2FmohdFb4V1XW4gbDFQ3ftYGIp57VMH93ITkz0wrD0BICXi5x%2FHskB%0A2PKG%2FKoDFdogdK0jxXai7RWU9w%3D%3D%0A)
