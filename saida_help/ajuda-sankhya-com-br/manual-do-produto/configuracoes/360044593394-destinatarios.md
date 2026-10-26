---
id: "360044593394"
titulo: "Destinatários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593394-Destinat%C3%A1rios"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:44:00Z"
rotulos: ["manual", "SMS", "Configuração", "WMS", "Parceiro", "Liberação de Limites", "Email", "Destinatários", "Notificação", "Servidor de SMTP", "br.com.sankhya.bim.destinatarios", "Destinatários manual", "ENDACESSEXTWGE", "Destinatário", "Financeiro"]
---

# Destinatários

Nesta tela configura-se parte do serviço de envio de liberações pendentes por e-mail e SMS; configura-se um Destinatário através de seu número de celular e e-mail.

![D1](https://ajuda.sankhya.com.br/hc/article_attachments/360060976174)

No campo **"Código do Destinatário"** informa-se o código referente ao exercício que está sendo cadastrado. Este preenchimento poderá ser realizado automaticamente, ou de forma manual; esta definição é feita através do botão ![Imagem 2: No campo "Código do Destinatário" informa-se o código referente ao exercício que está sendo cadastrado. Este…](https://ajuda.sankhya.com.br/hc/article_attachments/16343697345943) **"Configuração de tela"**, opção **"Numeração..."**, localizado no lado superior direito da tela.

O campo **"Nome do Destinatário"** está destinado ao preenchimento da denominação do destinatário.

A marcação **"Ativo"** quando efetuada, determina que as mensagens da fila de envio poderão ser encaminhadas aos destinatários. Por outro lado, quando desmarcada, tem-se que o destinatário não está apto a receber mensagens.

**Aba Geral**

**Celular:** Informa-se o número do celular do destinatário com o seguinte formato: 551199999999, sendo 55 o código do país, 11 o DDD e 99999999 o número do celular;

**E-mail:** Informar o endereço de e-mail juntamente com o símbolo arroba. Exemplo: [usuario@sankhya.com.br](mailto:usuario@sankhya.com.br)

**Cód. Usuário:** Este campo é destinado ao código do usuário, que se utilizado como liberador; serão analisados os dados do destinatário para envio do e-mail e SMS.

No campo **"Cód. Parceiro"** destina-se ao preenchimento do parceiro relacionado ao destinatário que está sendo cadastrado.

O campo **"Código do Contato"** recebe o contato ligado ao parceiro anteriormente informado, e que consequentemente está ligado ao destinatário.

Além disto, para utilizar esta funcionalidade faz-se necessário realizar as seguintes configurações:

- Informar no parâmetro **"Endereço para acesso externo ao WGE - ENDACESSEXTWGE"** o endereço do servidor de aplicação para o link do e-mail que será enviado, para que assim, as solicitações de liberação possam ser visualizadas;
- Na tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494) deve-se configurar os dados do servidor para envio de e-mail's;
- Também deve-se configurar na tela [Modem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106313) os dados para envio do SMS;
- No [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), botão **"Outras Opções..."**, opção **"Limites para Liberação"** deve-se observar o seguinte:

Se a marcação **"Enviar E-mail"** encontra-se efetuada pois, assim, ao clicar em **"Salvar"**, será encaminhado um e-mail para o mesmo cadastrado na tela Destinatários, com o link para efetuar-se as liberações.

Caso a marcação **"Enviar SMS"** esteja realizada, ao solicitar a liberação de limites e clicando-se em Salvar, uma mensagem será direcionada para o celular configurado no Cadastro de Destinatários.

**Nota:** as notificações serão enviadas para o e-mail do primeiro destinatário encontrado com esta informação e o mesmo aplica-se ao SMS.

**Observação:** na notificação via e-mail, o link para a página de liberação de solicitações possui validade de 15 dias. Caso o link seja inválido, a interface não será acessada, e uma mensagem de erro será apresentada.

- No pop-up **"Liberações Solicitadas"** das Centrais tem-se a marcação **"Notificação"**, sendo que esta deverá encontrar-se efetuada para que seja encaminhado o e-mail ou SMS de solicitação para liberação de limites.

**Aba Perfis Associados**

A aba **"Perfis Associados"** será alimentada por meio das configurações realizadas na tela [Perfil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593414). Nesta aba, realiza-se a inserção do perfil relacionado ao Destinatário.

![D2](https://ajuda.sankhya.com.br/hc/article_attachments/360061906993)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593394-Destinat%C3%A1rios#top)
