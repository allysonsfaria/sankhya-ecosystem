---
id: "37886593403031"
titulo: "Como configurar o Servidor SMTP e a Conta SMTP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37886593403031-Como-configurar-o-Servidor-SMTP-e-a-Conta-SMTP"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-09-18T18:29:34Z"
rotulos: ["Configuração", "Segurança", "Email", "SMTP", "Sistema"]
---

# Como configurar o Servidor SMTP e a Conta SMTP

## O que é servidor e conta SMTP?

A configuração do servidor e da conta SMTP é essencial para o correto envio de e-mails pelo sistema Sankhya. Esse processo permite que o sistema envie mensagens automaticamente em diversas rotinas, como envio de Ordens de Serviço, boletos, relatórios, notificações e recuperação de senha, sem necessidade de intervenção manual.

O servidor **SMTP (Simple Mail Transfer Protocol)** é o serviço responsável por realizar o envio desses e-mails. Ao configurar corretamente essa funcionalidade, o sistema consegue se comunicar com o provedor de e-mail da empresa, garantindo que as mensagens sejam transmitidas com segurança e eficiência. No Sankhya, é necessário configurar tanto o servidor SMTP quanto a conta de envio.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/846022455)

#### Registre em sua base o Servidor SMTP conforme dados apresentados

1. Configuração do **Servidor SMTP**

- Acesse a tela **Servidor SMTP**

**Menu:** Configurações » Avançado  »  Envio de Mensagens » Servidor SMTP

Neste exemplo, faremos a configuração utilizando os dados do **Gmail**. No entanto, é importante reforçar que cada empresa deverá utilizar as informações específicas do seu provedor de e-mail. Preencha os campos da tela conforme indicado abaixo:

- **Servidor SMTP:** informe “**smtp.gmail.com**”
- **Porta**: informe 587.
- **Tipo de Conexão:** selecione a opção Segura com TLS.
- **Remetente:** adicione o email da empresa.
- **Usuário:** informe o email do responsável pelo envio da mensagem.
- **Senha**: senha do email cadastrado no campo usuário.
- Clique no botão **Confirmar**.

No caso do Gmail, será necessário acessar sua conta Google e realizar a liberação de acesso de app menos seguros. 

- No navegador, conectado a sua conta, clique sobre sua foto (perfil de sua conta) acesse a opção **“Gerenciar sua Conta do Google”**.
- Clique na aba **“Segurança”** e localize a opção **“Acesso a app menos seguro”**, essa opção deve estar ativada.
- Retorne a tela **Servidor SMTP** no Sankhya.
- Preencha o campo **Destinatário** com um e-mail para testes e clique em **Testar**.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/846022418)

#### Registre em sua base conforme conta de e-mail responsável pelo envio

1. Configuração da **Conta SMTP**

- Acesse a tela **Contas SMTP**

**Menu:** Configurações » Avançado  » Envio de Mensagens » Contas SMTP

Para usuários de outros provedores de e-mail, as configurações devem seguir as diretrizes específicas definidas por eles. Este guia utiliza o exemplo de uma conta G-mail.

- Clique em **+ Novo registro** e preencha os campos:
- **Servidor SMTP:** informe o servidor smtp.gmail.com (Ex. para Outlook: smtp-mail.outlook.com)
- **Porta**: 587.
- **Tipo de Conexão:** Segura com TLS
- **Remetente:** Adicione o seu e-mail ou de sua empresa que fará os envios
- **Usuário:** Informe o mesmo e-mail indicado no campo anterior
- **Senha:** Indique a senha usada para acessar o e-mail informado
- Marque a opção **'Conta Padrão'** caso queira utilizar esta conta como modelo principal nas próximas operações.
- Clique em **Salvar**.

**Atenção**:

- Para o Gmail será preciso configurar em sua conta a autenticação de 2 fatores.
- Caso utilize o provedor Outlook, será preciso realizar as configurações OAuth.

2. **Teste de conexão**

- Clique no botão **Enviar e-mail de teste**.
- Informe um e-mail de destinatário para o teste.
- Verifique se recebeu o e-mail em sua caixa de entrada.

3. **Observações importantes**

- Mantenha as informações de senha sempre atualizadas.
- Verifique as configurações específicas do seu provedor de e-mail.
- Certifique-se que as portas e protocolos de segurança estão corretos.
- Em caso de múltiplas empresas, pode ser necessário configurar contas diferentes para cada uma.
