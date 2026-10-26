---
id: "44010601308439"
titulo: "Como integrar sua caixa de e-mail à Meetime"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010601308439-Como-integrar-sua-caixa-de-e-mail-%C3%A0-Meetime"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:42:10Z"
rotulos: ["sync_hc", "meetime", "meetime_340", "sync_hash_116deb1a45d7"]
---

# Como integrar sua caixa de e-mail à Meetime

A integração com a caixa de e-mails permite o disparo de e-mails através da atividade em uma cadência com apenas dois cliques, dando agilidade ao processo de prospecção, além de gerar notificações em sistema quando o lead abre, responde ou clica em links adicionados ao corpo do e-mail. Com essa integração o e-mail é enviado através da caixa de saída do usuário, garantindo maior entregabilidade aos envios.

## Como fazer?

Acessando a **Meetime** > **Menu** > **Integrações** > **Caixa de e-mail** > **Iniciar Integração**

---

![Imagem 1: Acessando a Meetime > Menu > Integrações > Caixa de e-mail > Iniciar Integração](https://ajuda.sankhya.com.br/hc/article_attachments/44010601574423)

Após isso o usuário será direcionado para o Nylas, que possui um mecanismo que ajuda a descobrir qual é o provedor de e-mail da conta. Para provedores maiores como Google Workplace (Gmail/G-suite) e Exchange (Office365/Microsoft), para concluir o processo basta inserir a senha do e-mail e conceder permissão de acesso à conta\*.

![Imagem 2: Após isso o usuário será direcionado para o Nylas, que possui um mecanismo que ajuda a descobrir qual é o provedor de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010587332247)

\*A integração com Google Workplace é liberada apenas domínios empresariais, ou seja, @ [empresa.com.br](http://empresa.com.br/)

no caso de contas Google Workplace é necessário realizar a configuração de whitelabel. Para entender como realizar esse processo acesse [esse](https://suporte.meetime.com.br/hc/pt-br/articles/360026399314-Autoriza%C3%A7%C3%A3o-Whitelabel) artigo.

Já contas como Yahoo, Outlook ou outros servidores será necessário realizar a integração avançada, com configuração de IMAP/SM. Nesta etapa, além de autenticar a senha da conta, será preciso fornecer informações relativas ao servidor de e-mail.

Temos [um artigo](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1778167533-documentacao-tecnica-_-integracao-de-caixa-com-o-microsoft-outlook-microsoft-365) com a documentação técnica sobre a integração de caixa com o Microsoft Outlook/Microsoft 365. Este artigo foi desenvolvido para auxiliar o time técnico responsável pela administração da conta e pela configuração das permissões necessárias para a integração.

## Integração avançada na caixa de e-mail

A integração avançada é realizada acessando a opção de configurações de IMAP customizada:

![Imagem 3: A integração avançada é realizada acessando a opção de configurações de IMAP customizada:](https://ajuda.sankhya.com.br/hc/article_attachments/44010602172951)

As informações requeridas para esse processo de integração avançada são duas, o IMAP e SMTP. Será necessário inserir o endereço e a porta dos servidores (com suporte a conexões seguras/SSL):

![Imagem 4: As informações requeridas para esse processo de integração avançada são duas, o IMAP e SMTP. Será necessário inserir o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010587738647)

- IMAP é o protocolo utilizado para a leitura e sincronização das mensagens da caixa de e-mail.
- SMTP é o protocolo utilizado para o envio de e-mails pela integração;

Essas informações podem ser obtidas nas configurações de conta do usuário no provedor de e-mail. Normalmente são administrados pela equipe de TI.

Há ainda especificidades para cada servidor de e-mail, gostaríamos de destacar duas aqui: configurações no Outlook e no Yahoo.

### Outlook

**1. Configurações** > **Opções**

**2.** Para contas Outlook de novo layout **> Configurações > Configurações de exibição completa > E-mail > Sincronizar e-mail.** Deve-se então copiar os nomes dos servidores IMAP e SMTP.

\*Para realizar a integração avançada é necessário que o seu serviço de e-mail tenha suporte a conexões seguras para IMAP e SMTP. Por padrão, o protocolo IMAP tem sua versão segura na porta 993 e o SMTP na porta 587. O servidor deve ter SSL/TLS habilitado ou conseguir fazer o upgrade para uma conexão segura utilizando STARTTLS. Verifique com a TI da sua empresa se o serviço de e-mail se tem esse suporte.

### Yahoo

Já usuários do Yahoo podem ter dificuldades na autenticação da senha, uma vez que o sistema restringe o acesso de sistemas terceiros. Para liberar o acesso basta seguir os passos:

**Configuração da conta** > **Segurança da conta** > Habilitar a opção “**Permitir apps que usam método de acesso menos seguros**”

Agora é só refazer a integração e o acesso estará liberado.

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
