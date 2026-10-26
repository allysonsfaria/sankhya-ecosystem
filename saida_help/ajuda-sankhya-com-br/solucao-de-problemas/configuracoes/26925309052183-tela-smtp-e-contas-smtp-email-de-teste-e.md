---
id: "26925309052183"
titulo: "Tela smtp e contas smtp, email de teste é enviado com sucesso, mas na fila não consegue fazer a validação do usuário e senha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26925309052183-Tela-smtp-e-contas-smtp-email-de-teste-%C3%A9-enviado-com-sucesso-mas-na-fila-n%C3%A3o-consegue-fazer-a-valida%C3%A7%C3%A3o-do-usu%C3%A1rio-e-senha"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-13T13:36:19Z"
rotulos: ["Configuração", "Email", "Passos para resolver", "Razão do erro", "Detalhe do erro", "na fila não consegue fazer a validação do usuário e senha", "Tela smtp e contas smtp", "email de teste é enviado com sucesso", "Jobs", "Servidor de Aplicação", "Argumento VM"]
---

# Tela smtp e contas smtp, email de teste é enviado com sucesso, mas na fila não consegue fazer a validação do usuário e senha

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26945814066839) **SITUAÇÃO:**

Tela smtp e contas smtp, email de teste é enviado com sucesso, mas na fila não consegue fazer a validação do usuário e senha.

![Imagem 2: Tela smtp e contas smtp, email de teste é enviado com sucesso, mas na fila não consegue fazer a validação do usuário e…](https://ajuda.sankhya.com.br/hc/article_attachments/26925309024663)

![Imagem 3: Tela smtp e contas smtp, email de teste é enviado com sucesso, mas na fila não consegue fazer a validação do usuário e…](https://ajuda.sankhya.com.br/hc/article_attachments/26925331135895)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26925331143575)SOLUÇÃO:**

Na tela da **"Administração"** verifique se, no Argumento da VM, o parâmetro Dsankhyaw.schedule.disable=true está ligado. Pois, ele desativa todos os jobs do sistema. Para que os e-mails sejam enviados, esse parâmetro precisa estar desabilitado ou não existir na base. Importante entender o motivo desse parâmetro estar ligado na base de produção, normalmente esse parâmetro fica ligado nas bases de teste. Esse argumento fica dentro do servidor de aplicação

**Exemplo:**/home/mgeweb/Wildfly\_Producao/bin/standalone.conf, edite o arquivo standalone.conf, identifique o argumento e coloque como falso ou retire esse argumento. Depois o servidor precisa ser reiniciado.

![Imagem 5: Exemplo: /home/mgeweb/Wildfly_Producao/bin/standalone.conf, edite o arquivo standalone.conf, identifique o argumento e…](https://ajuda.sankhya.com.br/hc/article_attachments/26925309034135)

O teste de e-mail é para fazer a validação dos dados cadastrais. Mesmo sendo validado, o sistema precisa que o job esteja funcionando corretamente para que os e-mails sejam enviados.
