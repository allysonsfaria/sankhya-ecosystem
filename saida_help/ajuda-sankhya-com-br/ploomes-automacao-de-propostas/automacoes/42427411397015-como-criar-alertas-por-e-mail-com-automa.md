---
id: "42427411397015"
titulo: "Como criar alertas por e-mail com automações genéricas para os principais eventos dos seus Negócios?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427411397015-Como-criar-alertas-por-e-mail-com-automa%C3%A7%C3%B5es-gen%C3%A9ricas-para-os-principais-eventos-dos-seus-Neg%C3%B3cios"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:22Z"
rotulos: ["sync_hc", "ploomes_5452246", "ploomes", "sync_hash_1ff545677902"]
---

# Como criar alertas por e-mail com automações genéricas para os principais eventos dos seus Negócios?

Com o recurso de Automações do Ploomes, é possível criar Negócios e alertas sobre os principais eventos dos seus processos. Neste artigo, serão apresentadas algumas possibilidades de envio automático de e-mails para acompanhar os principais eventos das negociações no funil. Como exemplo, será considerado o cenário em que um Coordenador de Vendas precisa ser informado, em tempo real, sobre as atualizações das negociações.

## Visão geral

Para criar uma nova automação genérica, acesse **Administração > Automações**. Em seguida, selecione a entidade **Negócio** (a nomenclatura pode variar conforme a configuração da conta) e clique em **Nova automação**.

Ao criar uma nova automação, é necessário preencher as seguintes informações:

- **Descrição da automação**
  Informe um nome que permita identificar facilmente a automação.

- **Quando a automação deve ser disparada**
  Defina o gatilho que fará com que a automação seja executada.

- **Filtro**
  Caso necessário, adicione condições para que a automação seja executada apenas em situações específicas. Assim, é possível refinar quando a automação deve ocorrer, de acordo com critérios definidos.

- **Ao ser disparada, o que a automação deve fazer?**
  Selecione a ação que será realizada automaticamente após o disparo da automação.

![Imagem 1: Ao ser disparada, o que a automação deve fazer? Selecione a ação que será realizada automaticamente após o disparo da…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224739344/c78779136af30942d6ab07a2d241/image.png?expires=1786536000&signature=1a0de55a09a6fa29efb82e30880a8576351db13b3bf8ce3eeadf750d10dc6842&req=diIlEs59lIJbXfMW3nq%2BgR3Keo9VbuyRQCRwBHSdYWoom3J0mxbrgDf2PROt%0AAp8pfWBtnrZSjWrbK9kgQeOLHFM%3D%0A)

## Gatilhos disponíveis nas automações

Ao configurar uma automação genérica, é necessário definir o gatilho, ou seja, o evento que fará com que a automação seja executada. Abaixo estão os principais gatilhos disponíveis:

**1. Quando o item for criado**

Este gatilho é acionado sempre que um novo negócio é criado no funil.
É ideal para notificar o início de uma negociação, garantindo que os responsáveis tenham visibilidade desde o primeiro contato.

**2. Quando o item for editado**

Este gatilho é disparado sempre que alguma informação do item é modificada. Pode ser utilizado em conjunto com filtros para reagir a mudanças específicas, como alteração de status, responsável, estágio ou campos personalizados.

**3. Quando o item for excluído**

Este gatilho ocorre quando um item é removido do sistema. Pode ser utilizado para registrar essa ação ou notificar responsáveis sobre a exclusão.

**4. Quando o negócio for ganho**

Este gatilho é acionado quando um negócio é marcado como ganho. É indicado para processos de pós-venda, como envio de e-mails de boas-vindas ou início de fluxos internos.

**5. Quando o negócio for perdido**

Este gatilho é disparado quando um negócio é definido como perdido. Pode ser utilizado para enviar notificações ou iniciar ações de recuperação.

**6. Quando o negócio for reaberto**

Este gatilho ocorre quando um negócio que já foi fechado (ganho ou perdido) é reaberto. É útil para retomar processos comerciais e notificar os responsáveis sobre a reativação da negociação.

**7. Periodicamente**

Este gatilho permite executar automações em intervalos de tempo definidos (como diariamente, semanalmente, etc.). É ideal para monitoramentos, lembretes e ações recorrentes baseadas em tempo, como verificar negócios sem atualização.

A imagem abaixo apresenta os gatilhos disponíveis para configuração das automações:

![Imagem 2: A imagem abaixo apresenta os gatilhos disponíveis para configuração das automações:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224693956/5ab956893bf1ba900aaf5b9ff442/image.png?expires=1786536000&signature=954ee0e251f4d5185941a628b75ccd75bfccb6a8e51c2d5a2e1463b70edff184&req=diIlEs93nohaX%2FMW3nq%2BgY2kcuqZAUMdW4ETSd6GT%2Bs2IBtcwb471GbsVtzb%0AG5nHwyzqxWBDL5iroXWQ4B5Tm1I%3D%0A)

## Ação de enviar e-mails

Neste artigo, o foco é criar alertas automáticos por e-mail. Portanto, será utilizada a ação de envio de e-mail. Ao selecionar essa opção, será necessário preencher os seguintes campos:

**a) Tipo de remetente**
Define em nome de quem o e-mail será enviado. É possível utilizar um remetente automático (no-reply@ploomes.com), um usuário pré-definido ou o usuário de um campo.

**b) Usuário para notificação de falha**
Selecione um usuário que será avisado caso ocorra falha no envio do e-mail.

**c) Destinatário do e-mail**
Escolha um campo de e-mail ou informe manualmente os destinatários (separados por ponto e vírgula).

**d) Assunto do e-mail**
Defina o título da mensagem. É possível utilizar campos para personalização.

**e) Conteúdo do e-mail**
Informe a mensagem que será enviada. Também é possível utilizar campos para compor o conteúdo automaticamente.

![Imagem 3: e) Conteúdo do e-mail Informe a mensagem que será enviada. Também é possível utilizar campos para compor o conteúdo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224829136/ce9156bbb2c9cc1ca17f1cef4b2f/image.png?expires=1786536000&signature=3a2388bdd07bacdec089e1a9f1dda75541712838a62c8edd0142cd66e3885032&req=diIlEsF8lIBcX%2FMW3nq%2BgZKWxaAL5FgexY0pfUW3UsvuQeEZPGXPGee8xMp1%0AQ9AR8vnbZtK3HIAG3nlfjJBjKI4%3D%0A)

## Sugestões de configuração

Após compreender os campos que devem ser preenchidos, deve-se configurar as automações. Como sugestão, são apresentados abaixo quatro cenários que ajudam a tornar o processo mais ágil e a dar visibilidade aos envolvidos.

Para utilizar os modelos de mensagem, basta copiar o código disponibilizado em cada link e colar no campo **Código fonte**, conforme demonstrado a seguir:

[GIF animado: Imagem 4: Para utilizar os modelos de mensagem, basta copiar o código disponibilizado em cada link e colar no campo Código fonte…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224772884/88054461455ec627457cbec0b845/vivaldi_ANzMIsGUwC.gif?expires=1786536000&signature=b130a319d51109bd16010c4708e36792a8cf6de640237b14fad0762ef9522f1f&req=diIlEs55n4lXXfMW3nq%2Bga9Wiz9T98oWvPIOP5ahFAHKhswGXcInDeJyrH87%0APF4aMdNFCcRlb5ltwbdkj0VBLnE%3D%0A)

---

## Sugestão 1 - Alertar que um negócio foi criado em um estágio específico

**Gatilho**: Quando o item for criado

**Filtro**: Estágio - igual a - [Nome do estágio]

**Modelo de mensagem sugerido**: **[Clique aqui para acessar](https://docs.google.com/document/d/1iCmvguwof7VJVtpn7TG56g8XbmXaSbdt1TcGwqEe16U/edit)**

[GIF animado: Imagem 5: Modelo de mensagem sugerido : Clique aqui para acessar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224793702/1bf290b7a2e42ea437b6b0140c31/vivaldi_9k6C2T2gPG.gif?expires=1786536000&signature=b664b5e28cad4aad8977daedc544e89ea2a2c15c2cee0537e2074c2d96c4876f&req=diIlEs53noZfW%2FMW3nq%2BgYVXDL6DZ%2FtDvdIJSO2s3qVlUz8nwbzRZwsXkgnE%0AQtCylMWGXv7lwKmlylmIp7K%2FW%2BQ%3D%0A)

---

## Sugestão 2 - Alertar que um negócio atingiu determinada etapa

**Gatilho**: Quando o item for editado

**Quais edições disparam a automação**: Negócio > Estágio

**Filtro**: Estágio - igual a - [Nome do estágio]

**Modelo de mensagem sugerido**: **[Clique aqui para acessar](https://docs.google.com/document/d/1vb7KZzUVhovBrNs2UyjjPerjt1eu8A3U044rZiKUTGQ/edit)**

[GIF animado: Imagem 6: Modelo de mensagem sugerido : Clique aqui para acessar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224802160/dc49813a846d4d00a9e7bde9a676/vivaldi_EcUrQHKJWC.gif?expires=1786536000&signature=7d28d8c6d5771441d4014f56795777672bbef74981741a01b67024b01cd4d678&req=diIlEsF%2Bn4BZWfMW3nq%2Bgc1Yfzk9o0WxuiupExz5SvtpEfioFo%2BjgcvVIsGu%0AFlN29E0a4yQ%2FOcaj0oTuShCw2Qw%3D%0A)

---

## Sugestão 3 - Alertar que um negócio foi ganho em um estágio específico

**Gatilho**: Quando o negócio for ganho

**Filtro**: Estágio - igual a - [Nome do estágio]

**Modelo de mensagem sugerido**: **[Clique aqui para acessar](https://docs.google.com/document/d/1QE2iJ1xFdIKDzMCLfUhdOiCkCwXwOAR28JHIgmIbpNA/edit)**

[GIF animado: Imagem 7: Modelo de mensagem sugerido : Clique aqui para acessar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224809103/8dc3f964ed5683c605092849d202/vivaldi_QTJsKTCKex.gif?expires=1786536000&signature=76d42a390380784797cafb18e379a63179f10358b66ee40f27f9d603f7040174&req=diIlEsF%2BlIBfWvMW3nq%2BgczB68nrcIuDUiSIz0uaCTzyGGfHfIWEUzp3dnaa%0A1yDHmnk12JMFFumSdSR86h196Rg%3D%0A)

---

## Sugestão 4 - Alertar que um negócio foi perdido em um estágio específico

**Gatilho**: Quando o negócio for perdido

**Filtro**: Estágio - igual a - [Nome do estágio]

**Modelo de mensagem sugerido**: **[Clique aqui para acessar](https://docs.google.com/document/d/15gXk5O32tHKYk6hCPfHcwQ0Fi5ZM-dxfCjawbg3pYdo/edit)**

[GIF animado: Imagem 8: Modelo de mensagem sugerido : Clique aqui para acessar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224823478/ad08bdd1110d1f1f51994fe46d43/vivaldi_5QOBchhM0t.gif?expires=1786536000&signature=03cf5a326ff28d1213442765b87381825eb22daf941fc9f9cf56d489a1e74dbe&req=diIlEsF8noVYUfMW3nq%2BgUU6PReSVbU7RfsdMyO30CgsqxeGhcNr4me5EQ6a%0ApWc0IyAOiEdWNj%2BdPQeneGNMlE4%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
