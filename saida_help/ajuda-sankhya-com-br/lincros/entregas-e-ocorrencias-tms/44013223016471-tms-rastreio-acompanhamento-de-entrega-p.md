---
id: "44013223016471"
titulo: "[TMS] - Rastreio/Acompanhamento de entrega para cliente final"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013223016471--TMS-Rastreio-Acompanhamento-de-entrega-para-cliente-final"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T19:50:15Z"
rotulos: ["sync_hc", "lincros", "lincros_13432870", "sync_hash_bd1e286100c9"]
---

# [TMS] - Rastreio/Acompanhamento de entrega para cliente final

**Menu**: Cadastros Gerais > Configurações da empresa > Ocorrências

**Objetivo**: Permitir que o cliente final realize o rastreio/acompanhamento da entrega por meio de um link, sem a necessidade deste realizar login no TMS.

**Considerações:**

— Nota fiscal deve estar importada no TMS;— Status da nota fiscal diferente de gerado;
— Nota fiscal com conhecimento vinculado;

**Configurando as ocorrências:**Para que o cliente final (destinatário da carga) rastreie o seu pedido, você deve configurar no cadastro de ocorrência **(Ocorrências por empresa)** para enviar um e-mail ou SMS ao destinatário da carga com o link para rastreio.

**1. Via SMS**Na tela de Ocorrências por empresa, acessar o cadastro da ocorrência desejada, em seguida clicar na aba SMS e marcar a opção Enviar SMS, preenchendo em seguida o texto que deseja enviar. Caso deseje enviar o link, marcar a flag **"Enviar link no SMS"**.

![Imagem 1: 1. Via SMS Na tela de Ocorrências por empresa, acessar o cadastro da ocorrência desejada, em seguida clicar na aba SMS…](https://ajuda.sankhya.com.br/hc/article_attachments/44013190361495)

O cliente receberá um SMS com o link para rastrear sem a necessidade de realizar login no sistema. O link é semelhante a este: <https://www.transpofrete.com.br/default/rastreio/mercadoria/rastreioCliente.xhtml?tokenRastreio=>**token de rastreio**O **token de rastreio** é gerado no momento do envio do SMS e é único do cliente. Possui uma validade que por padrão é de 7 dias. Passado o tempo de validade do token, para reativar ele é necessário lançar novamente um evento ocorrência, com isso ele é reativado pela mesma quantidade de dias da primeira vez.
**2. Via e-mail**

Na tela de Ocorrências por empresa, acessar a aba "E-mail" e marcar a flag **"Enviar email destinatário"**

![Imagem 2: O cliente receberá um SMS com o link para rastrear sem a necessidade de realizar login no sistema. O link é semelhante…](https://ajuda.sankhya.com.br/hc/article_attachments/44013206327319)

Ao ser lançada esta ocorrência, será disparado um e-mail ao destinatário da nota fiscal.

**3. Envio do link manualmente**

É possível enviar o link manualmente diretamente na nota fiscal no botão **"Ações > Enviar"**

![Imagem 3: Ao ser lançada esta ocorrência, será disparado um e-mail ao destinatário da nota fiscal. 3. Envio do link manualmente É…](https://ajuda.sankhya.com.br/hc/article_attachments/44013175853207)

**Tela de rastreio**

A tela disponibilizada fica conforme abaixo.

![Imagem 4: A tela disponibilizada fica conforme abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/44013206541719)

**OBS:**Caso a ocorrência lançada esteja marcada como Visualização restrita em seu cadastro, ela não será exibida para o cliente.

Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
