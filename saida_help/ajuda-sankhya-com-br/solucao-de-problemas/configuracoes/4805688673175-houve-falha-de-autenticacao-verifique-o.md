---
id: "4805688673175"
titulo: "Houve falha de autenticação. Verifique o usuário e senha - Office365"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4805688673175-Houve-falha-de-autentica%C3%A7%C3%A3o-Verifique-o-usu%C3%A1rio-e-senha-Office365"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:18:36Z"
rotulos: ["Configuração", "SMTP", "Autenticação", "Office365", "não apagar", "CORE_E04536", "Falha de Autenticação no CORE_E04536", "Erro"]
---

# Houve falha de autenticação. Verifique o usuário e senha - Office365

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16344233615383) MENSAGEM**:

CORE\_E04536 - Houve falha de autenticação. Verifique o usuário e senha. Saiba mais!

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16344218095511) CAUSA:**

O incidente ocorre quando mesmo o usuário e senha do e-mail tenha sido testado o login via navegador com sucesso.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16344233620631) SOLUÇÃO:**

Use o Centro de administração do Microsoft 365 para habilitar ou desabilitar o AUTH SMTP em caixas de correio específicas:

![Imagem 4: Abra o Centro de administração do Microsoft 365 e vá para: Usuários > Usuários ativos.](https://ajuda.sankhya.com.br/hc/article_attachments/16344218105495) Abra o [Centro de administração do Microsoft 365](https://admin.microsoft.com/) e vá para: **Usuários** > **Usuários ativos.**

![Imagem 5: Selecione o usuário e no sobrevoo exibido clique em Email .](https://ajuda.sankhya.com.br/hc/article_attachments/16344233629207) Selecione o usuário e no sobrevoo exibido clique em **Email**.

![Imagem 6: Na seção Aplicativos de email, clique em Gerenciar aplicativos de email .](https://ajuda.sankhya.com.br/hc/article_attachments/16344218114327) Na seção **Aplicativos de email,** clique em **Gerenciar aplicativos de email**.

![Imagem 7: Verifique a configuração SMTP autenticada: caso esteja desmarcada/desabilitada, faça a marcação para que fique…](https://ajuda.sankhya.com.br/hc/article_attachments/16344218118423) Verifique a **configuração SMTP autenticada:** caso esteja desmarcada/desabilitada, faça a marcação para que fique habilitada/check, conforme print abaixo.

![Imagem 8: Verifique a configuração SMTP autenticada: caso esteja desmarcada/desabilitada, faça a marcação para que fique…](https://ajuda.sankhya.com.br/hc/article_attachments/15776028055063)

![Imagem 9: Quando terminar, clique em Salvar alterações .](https://ajuda.sankhya.com.br/hc/article_attachments/16344218120983) Quando terminar, clique em **Salvar alterações**.

**Observação:** feito isso basta realize o teste de envio conforme abaixo.

**» Envio de Mensagens » Servidor SMTP**

![Imagem 10: » Envio de Mensagens » Servidor SMTP](https://ajuda.sankhya.com.br/hc/article_attachments/15776001167639)
