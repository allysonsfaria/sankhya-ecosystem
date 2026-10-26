---
id: "360044616093"
titulo: "Não é possível enviar a notificação com as solicitações de liberação pois o liberador \"XXXXX\" não está cadastrado como destinatário de SMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616093-N%C3%A3o-%C3%A9-poss%C3%ADvel-enviar-a-notifica%C3%A7%C3%A3o-com-as-solicita%C3%A7%C3%B5es-de-libera%C3%A7%C3%A3o-pois-o-liberador-XXXXX-n%C3%A3o-est%C3%A1-cadastrado-como-destinat%C3%A1rio-de-SMS"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:25Z"
rotulos: ["#criadoRoger", "CORE_E03070", "SMS", "Configuração", "Liberação de Limites", "Destinatários", "Problema no Envio de Notificação", "Erro"]
---

# Não é possível enviar a notificação com as solicitações de liberação pois o liberador "XXXXX" não está cadastrado como destinatário de SMS

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18789289206551) MENSAGEM:**

[CORE\_E03070] Não é possível enviar a notificação com as solicitações de liberação pois o liberador "XXXXX" não está cadastrado como destinatário de SMS.
Verifique se está cadastrado na tela de Destinatários e preencha o campo "Celular".

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18789316012311) SITUAÇÃO:**

Ao tentar confirmar a liberação de limites de um documento, a seguinte mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18789289216407) CAUSA:**

Ocorre quando o usuário que possui alçada para algum evento que está cadastrado para 'receber SMS' com a notificação da solicitação de liberação de limites, não está cadastrado em Destinatários e/ou não possui o número do telefone celular vinculado a este cadastro.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18789316019479) SOLUÇÃO:**

![Imagem 5: Configurações » Avançado » Envio de Mensagens » Destinatários:](https://ajuda.sankhya.com.br/hc/article_attachments/18789289223319) Configurações » Avançado » Envio de Mensagens » Destinatários:

- Se a rotina de Liberação de Limites, envia um SMS para o celular do liberador, é preciso cadastrar o celular nesta tela e vincular o usuário Liberador.

![Imagem 6: Caso não faça o uso de envio de SMS, pode desmarcar o envio de SMS acessando:](https://ajuda.sankhya.com.br/hc/article_attachments/18789316032023) Caso não faça o uso de envio de SMS, pode desmarcar o envio de SMS acessando:

- Configurações » Controle de Acesso » Usuários
- Botão: Outras Opções>>Liberação de Limites
- Selecione os eventos e desmarque a opção 'Envio SMS'

![Imagem 7: Após o ajuste, volte a selecionar os usuários novamente para liberação de Limites.](https://ajuda.sankhya.com.br/hc/article_attachments/18789289230231) Após o ajuste, volte a selecionar os usuários novamente para liberação de Limites.
