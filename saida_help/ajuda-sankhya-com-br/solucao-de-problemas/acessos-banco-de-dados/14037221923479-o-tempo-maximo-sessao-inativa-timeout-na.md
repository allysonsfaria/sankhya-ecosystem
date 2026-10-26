---
id: "14037221923479"
titulo: "O Tempo máximo sessão inativa (Timeout) não está funcionando"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14037221923479-O-Tempo-m%C3%A1ximo-sess%C3%A3o-inativa-Timeout-n%C3%A3o-est%C3%A1-funcionando"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-10-02T12:18:32Z"
rotulos: ["Configuração", "Segurança", "Usuário", "Preferências", "Timeout de sessão Configuração de segurança Solução de problemas", "Problema de Timeout de Sessão Inativa", "timeout sessão segurança", "Timeout"]
---

# O Tempo máximo sessão inativa (Timeout) não está funcionando

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16920601182231) SITUAÇÃO:**

Sistema não apresenta a mensagem de timeout e permite que o usuário fique logado mesmo sem uso, independente do tempo configurado. Isso ocasiona problemas de segurança e consumo indevido de licenças.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16920601195543)CAUSA:**

Ocorre por falta de configuração.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16920636800407)SOLUÇÃO:**

**(1)** Configure o campo **"Tempo de Aplicativo inativo para finalizar"** no cadastro do usuário, aba **"Segurança";**

**(1)** Configure os parâmetros abaixo na tela **Preferências -** Configurações » Avançado » Preferências:

**"INATSESSTIMEOUT (Tempo máx.(min) que sessão será preservada sem uso)"**
**"SESSIONTIMEOUT '(Tempo máximo sessão inativa (em minutos)"**

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16920636805655)OBSERVAÇÃO:**

**(1)** Se mesmo assim o usuário não deslogar automaticamente de acordo com o tempo configurado quando está em inatividade, verifique na **"Administração do Servidor"**, aba **"Geral"**, se existe um argumento com o nome **"-Dignore.session.timeout=true"**. Caso exista essa configuração, o valor do parâmetro **"Tempo de Aplicativo inativo para finalizar"**, configurado na tela **"Usuários"**, aba Segurança e o parâmetro INATSESSTIMEOUT, configurado na tela Preferências são ignorados e o sistema passa a não considerar o tempo inativo da sessão.

**(1)** Neste caso, acesse o servidor de aplicações e altere o argumento para "false" ou retire o de dentro da pasta do Wildfly > bin, editando o arquivo 'standalone.conf.bat' em servidores Windows ou standalone.conf em servidores Linux e, em seguida, reinicie o sistema a partir do próprio servidor para que a alteração entre em vigor.

**(1)** Existe uma margem de erro de até 1 min para o tempo configurado.
