---
id: "31675937800855"
titulo: "Verificação em duas etapas está desativada na sua conta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31675937800855-Verifica%C3%A7%C3%A3o-em-duas-etapas-est%C3%A1-desativada-na-sua-conta"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:32:28Z"
rotulos: ["Configuração", "Segurança", "Autenticação", "Google", "Sankhya ID", "Passos para resolver", "Razão do erro", "Detalhe do erro", "está desativada na sua conta", "Verificação em duas etapas", "Erro"]
---

# Verificação em duas etapas está desativada na sua conta

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31675937778839) **MENSAGEM:**

Como a verificação em duas etapas está desativada para sua conta, não é possível usar esse método como segunda etapa de verificação. Entre em contato com sua administrador para receber ajuda.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31675937782423)SOLUÇÃO:**

![Imagem 3: Com o usuário/e-mail administrador do domínio, entre na tela "Administrador" do gerenciamento de domínios do google…](https://ajuda.sankhya.com.br/hc/article_attachments/32038485398679) Com o usuário/e-mail administrador do domínio, entre na tela **"Administrador"** do gerenciamento de domínios do google (ícone do meio da primeira linha):

![Imagem 4: Com o usuário/e-mail administrador do domínio, entre na tela "Administrador" do gerenciamento de domínios do google…](https://ajuda.sankhya.com.br/hc/article_attachments/31675935573911)

![Imagem 5: Pesquise por "Verificação em duas etapas" :](https://ajuda.sankhya.com.br/hc/article_attachments/32038481665559) Pesquise por **"Verificação em duas etapas"**:

![Imagem 6: Pesquise por "Verificação em duas etapas" :](https://ajuda.sankhya.com.br/hc/article_attachments/31675937783191)

![Imagem 7: Nas configurações da verificação em duas etapas do domínio, selecione "Permitir que os usuários ativem a verificação em…](https://ajuda.sankhya.com.br/hc/article_attachments/32038485402519) Nas configurações da verificação em duas etapas do domínio, selecione **"Permitir que os usuários ativem a verificação em duas etapas"** e em **"Aplicação"** deixe como **"Desativar"** (dessa forma não é obrigatório que todos os usuários façam essa configuração) e depois salve essas informações:

![Imagem 8: Nas configurações da verificação em duas etapas do domínio, selecione "Permitir que os usuários ativem a verificação em…](https://ajuda.sankhya.com.br/hc/article_attachments/31675935578775)

![Imagem 9: Entre no e-mail que estava sendo configurado como remetente em Servidor SMTP ou Contas SMTP. Em seguida, clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/32038481669783) Entre no e-mail que estava sendo configurado como remetente em Servidor SMTP ou Contas SMTP. Em seguida, clique no perfil e depois em **"Gerenciar sua conta do google"**:

![Imagem 10: Entre no e-mail que estava sendo configurado como remetente em Servidor SMTP ou Contas SMTP. Em seguida, clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/31675937784599)

![Imagem 11: Depois pesquise por "Verificação em duas etapas" :](https://ajuda.sankhya.com.br/hc/article_attachments/32038592290967) Depois pesquise por **"Verificação em duas etapas"**:

![Imagem 12: Depois pesquise por "Verificação em duas etapas" :](https://ajuda.sankhya.com.br/hc/article_attachments/31675935579671)

![Imagem 13: Crie e/ou ative a verificação em duas etapas (após cadastrar alguma 2° verificação, precisa ativar):](https://ajuda.sankhya.com.br/hc/article_attachments/32038592292247) Crie e/ou ative a verificação em duas etapas (após cadastrar alguma 2° verificação, precisa ativar):

![Imagem 14: Crie e/ou ative a verificação em duas etapas (após cadastrar alguma 2° verificação, precisa ativar):](https://ajuda.sankhya.com.br/hc/article_attachments/31675935586199)

![Imagem 15: Quando ativado, vai ficar marcado da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/32038622070679) Quando ativado, vai ficar marcado da seguinte forma:

![Imagem 16: Quando ativado, vai ficar marcado da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/31675935586711)

![Imagem 17: Agora a configuração "Senhas de app" :](https://ajuda.sankhya.com.br/hc/article_attachments/32038622071063) Agora a configuração **"Senhas de app"**:

![Imagem 18: Agora a configuração "Senhas de app" :](https://ajuda.sankhya.com.br/hc/article_attachments/31675937790103)

- Após criar a senha de app, salve a senha, pois não é possível revê-la depois (se perder essa, crie uma nova)
- Coloque na senha das configuração de "Servidor SMTP" e/ou "Contas SMTP" onde estiver configurando o remetente dos envios de e-mail
- Com isso, se as outras configurações no Servidor SMTP ou Contas SMTP estiverem certas, o envio deve funcionar.

**Observação:** pode ser que o sistema continue apresentando o erro "Houve falha de autenticação. Verifique o usuário e senha", verifique se no log aparece "Too many login attempts, please try again later.", pois no sistema esse erro pode aparecer mascarado pelo erro de autenticação. O "Too many login attempts, please try again later." é do google, informando que tiveram muitas tentativas de acesso e por isso bloqueou o e-mail temporariamente (geralmente de 12 a 24 hrs), aguarde esse período e tente o envio novamente.

**![Imagem 19: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31675935569303)CAUSA:**

Problema ocorre ao tentar configurar a verificação em duas etapas para posteriormente ativar a "Senhas de app" do google. Essa configuração é necessária, pois o servidor SMTP e as contas SMTP não aceitam mais a senha de login do e-mail. Durante o processo, é exibido o erro: "Houve falha de autenticação. Verifique o usuário e a senha.".

Erro aparece quando a verificação em duas etapas não está habilitada para uso naquele domínio.
