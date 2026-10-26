---
id: "39322152787095"
titulo: "(Portal RH),  \"Esqueci a senha ou primeiro acesso?\" ou não recebendo o e-mail com a senha de primeiro acesso."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39322152787095--Portal-RH-Esqueci-a-senha-ou-primeiro-acesso-ou-n%C3%A3o-recebendo-o-e-mail-com-a-senha-de-primeiro-acesso"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-21T15:17:22Z"
rotulos: ["Configuração", "Funcionários", "SMTP", "Portal RH", "Acesso", "Artigo criado KCS", "Sankhya RH - KCS", "Primeiro Acesso"]
---

# (Portal RH),  "Esqueci a senha ou primeiro acesso?" ou não recebendo o e-mail com a senha de primeiro acesso.

O colaborador não consegue acessar o aplicativo **"Pessoas+"** (Portal RH), sendo direcionado para a tela de **"Esqueci a senha ou primeiro acesso?"** ou não recebendo o e-mail com a senha de primeiro acesso.

###

### SITUAÇÃO

Esta situação ocorre quando o colaborador tenta realizar o login no aplicativo **"Pessoas+"**, mas não consegue acessar o sistema. O problema pode estar relacionado a diferentes causas, como:

- Colaborador possui cadastros duplicados no sistema (funcionário desligado e recontratado).
- Acesso ao Portal RH não foi liberado corretamente.
- E-mail de primeiro acesso não foi recebido devido a falhas na configuração SMTP.
- Configurações de e-mail do colaborador estão vinculadas ao cadastro incorreto.

### SOLUÇÃO

Para resolver o problema de acesso ao aplicativo **"Pessoas+"**, siga os passos abaixo:

**(1)** Verifique se existe cadastro duplicado do colaborador no sistema. Caso exista um registro de funcionário desligado e outro ativo, remova o e-mail associado ao registro do funcionário desligado.

**(2)** Acesse a tela **"Acessos Pessoal Mais"** e libere o acesso ao Portal RH para o colaborador.

 **(3)** Caso o colaborador não receba o e-mail com a primeira senha, verifique a configuração da conta SMTP. Acesse a tela **"Servidor SMTP"** (Configurações » Avançado » Envio de Mensagens » Servidor SMTP) ou **"Contas SMTP"** (Configurações » Avançado » Envio de Mensagens » Contas SMTP) e valide se as credenciais de usuário e senha estão corretas.

Artigos para apoio revisão configuração:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/4406041274647-Configura%C3%A7%C3%A3o-de-conta-SMTP-no-Pessoal>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/26925309052183-Tela-smtp-e-contas-smtp-email-de-teste-%C3%A9-enviado-com-sucesso-mas-na-fila-n%C3%A3o-consegue-fazer-a-valida%C3%A7%C3%A3o-do-usu%C3%A1rio-e-senha>

**(4)** Se necessário, configure a **"Senha de App"** do Gmail seguindo as orientações do artigo sobre configuração de senha de app para e-mails corporativos.

<https://ajuda.sankhya.com.br/hc/pt-br/articles/10018281372951--Usar-Gmail-no-sistema-Sankhya-com-ativa%C3%A7%C3%A3o-em-duas-etapas>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/29900464543639-Houve-falha-de-autentica%C3%A7%C3%A3o-Verifique-o-usu%C3%A1rio-e-senha-ao-cadastrar-e-mail-Gmail-google-ou-Outlook-microsoft>

**(5)** Após ajustar as configurações de e-mail, remova o acesso ao portal e libere-o novamente para que o sistema envie um novo e-mail de primeiro acesso.

**(6)** Valide com o colaborador se o e-mail foi recebido e se o acesso ao Portal RH está funcionando corretamente.

**(7)** Caso o colaborador consiga acessar mas não visualize os holerites, verifique a liberação das folhas para o Portal RH na tela **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas).

![Imagem 1: (5) Após ajustar as configurações de e-mail, remova o acesso ao portal e libere-o novamente para que o sistema envie um…](https://ajuda.sankhya.com.br/hc/article_attachments/41272035960599)

### CAUSA

O problema de acesso ao aplicativo **"Pessoas+"** pode ser causado por:

- **Cadastros duplicados:** quando o colaborador foi desligado e recontratado, permanecendo com dois registros no sistema, sendo que o e-mail pode estar vinculado ao cadastro inativo.
- **Falta de liberação de acesso:** o acesso ao Portal RH não foi concedido através da tela **"Acessos Pessoal Mais"**.
- **Falha na autenticação SMTP:** configurações incorretas de usuário e senha na conta SMTP impedem o envio do e-mail com a senha de primeiro acesso.
- **Ausência de senha de app:** para e-mails corporativos do Gmail, é necessário configurar a senha de aplicativo ao invés da senha comum de login.
