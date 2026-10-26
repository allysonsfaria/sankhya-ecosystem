---
id: "4406041274647"
titulo: "Como configurar a conta SMTP para envio de e-mails"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4406041274647-Como-configurar-a-conta-SMTP-para-envio-de-e-mails"
trilha: "Manual do Produto > Pessoas+ > Implantação e Acessos do Pessoas+ > Usuários e Permissões do Pessoas+"
atualizado_em: "2026-10-02T15:00:27Z"
rotulos: ["Configuração", "Relatórios", "Contas", "SMTP", "Portal RH", "Como configurar conta SMTP no Pessoal+", "conta SMTP", "FPCODSMTP", "Configuração de contas SMTP", "Recuperação de senha e relatórios", "Teste de envio e configuração padrão", "Pessoal+"]
---

# Como configurar a conta SMTP para envio de e-mails

Através da configuração realizada na tela [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP), é possível realizar o envio de e-mails utilizando a conta padrão da empresa como remetente das mensagens, permitindo que o funcionário destinatário identifique facilmente a origem da mensagem através do e-mail do remetente.

A configuração de Contas SMTP é aplicada por diversos processos nos quais o envio de e-mails é utilizado. No caso do Pessoal+, essa conta servirá para o envio do e-mail de recuperação de senha do usuário do [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433), envio de relatórios, entre outros.

Para melhor compreensão, considere que uma determinada empresa utilize o Gmail como servidor de e-mails e deseja configurar sua conta padrão para o envio dos e-mails disparados pela solução.

---

![Imagem 1: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16950962876311) **Informações adicionais:**

- As configurações já virão preenchidas na base modelo com um exemplo válido para o servidor de e-mails do Google. Diante disso, se esse for o serviço utilizado pela empresa é preciso apenas modificar o usuário e senha com um e-mail e senha próprios da empresa que está sendo implantada.
- Se o fornecedor do serviço de e-mail da sua empresa for outro, verifique com seu departamento de TI quais são as informações do servidor STMP desse fornecedor.

---

Desse modo, acesse a tela Contas SMTP e clique no botão **"Atualizar"**, assim, serão apresentados os dados que acompanham a base modelo. Para modificar, basta informar os dados corretos do e-mail da empresa nos campos **"Remetente"** e **"Usuário"**, informe também a **"Senha"** da conta de e-mail.

![Imagem 2: Desse modo, acesse a tela Contas SMTP e clique no botão "Atualizar" , assim, serão apresentados os dados que acompanham…](https://ajuda.sankhya.com.br/hc/article_attachments/21010109964567)

Ao acionar a marcação **"Conta padrão"** a conta cadastrada será usada como conta padrão na ausência de configuração específica para os diferentes processos onde é utilizada.

Para validar a configuração realizada, acione o botão **"Enviar** **e-mail** **de** **teste"** na parte superior da tela. Assim, será aberto um pop-up para ser informado o e-mail do destinatário para simulação de envio. 

![Imagem 3: Para validar a configuração realizada, acione o botão "Enviar e-mail de teste" na parte superior da tela. Assim, será…](https://ajuda.sankhya.com.br/hc/article_attachments/21010109976855)

Agora, acesse a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834) e localize o parâmetro **"Conta STMP - FPCODSMTP"**. Esse parâmetro é utilizado para definir qual a configuração que será utilizada para o envio de e-mails provenientes do Pessoal+. Desse modo, no campo **"Inteiro"** informe o código da Conta SMTP criada. 

![Imagem 4: Agora, acesse a tela Preferências e localize o parâmetro "Conta STMP - FPCODSMTP" . Esse parâmetro é utilizado para…](https://ajuda.sankhya.com.br/hc/article_attachments/21010109985047)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406041274647-Como-configurar-a-conta-SMTP-para-envio-de-e-mails#top)
