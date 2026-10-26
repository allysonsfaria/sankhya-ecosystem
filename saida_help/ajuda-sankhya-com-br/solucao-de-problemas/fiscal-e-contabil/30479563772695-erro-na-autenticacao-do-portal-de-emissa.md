---
id: "30479563772695"
titulo: "Erro na autenticação do Portal de emissão de NFS-e de Florianopólis - SC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30479563772695-Erro-na-autentica%C3%A7%C3%A3o-do-Portal-de-emiss%C3%A3o-de-NFS-e-de-Florianop%C3%B3lis-SC"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:35:42Z"
rotulos: ["Configuração", "Cidades", "Prefeituras", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro na autenticação com o provedor da prefeitura", "autenticação do Portal de emissão de NFS-e de Florianopólis", "Erro", "Artigo atualizado KCS", "Inscrição Municipal (IM)", "Docs Eletrônicos - KCS"]
---

# Erro na autenticação do Portal de emissão de NFS-e de Florianopólis - SC

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30479563755927) **MENSAGEM:**

"java.lang.Exception: Erro na autenticação com o provedor da prefeitura, verifique o usuário e senha cadastrado nas preferências da Empresa. Esse erro pode ter ocorrido por falta de conexão com a Internet."

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30479563760663)SOLUÇÃO:**

![Imagem 3: Valide se as informações de login e senha no portal da Prefeitura de Florianopólis - SC estão corretos e funcionando…](https://ajuda.sankhya.com.br/hc/article_attachments/30528194551831) Valide se as informações de login e senha no portal da Prefeitura de Florianopólis - SC estão corretos e funcionando normalmente.

**![Imagem 4: Atenção: não se esqueça de que no portal da prefeitura de Florianopólis - SC a autenticação é feita pelo número da…](https://ajuda.sankhya.com.br/hc/article_attachments/30528184543511) Atenção:** não se esqueça de que no portal da prefeitura de Florianopólis - SC a autenticação é feita pelo **número da Inscrição Municipal do Prestador.**

![Imagem 5: Atenção: não se esqueça de que no portal da prefeitura de Florianopólis - SC a autenticação é feita pelo número da…](https://ajuda.sankhya.com.br/hc/article_attachments/30528412458007)

**(1)** Caso a **tentativa de login no portal da Prefeitura não se realize**, solicite uma recuperação de senha junto ao Provedor da Prefeitura.

![Imagem 6: Por outro lado, se as credenciais de acesso ao portal da prefeitura estiverem corretas e o login acontecer normalmente,…](https://ajuda.sankhya.com.br/hc/article_attachments/30528184544791) Por outro lado, se as credenciais de acesso ao portal da prefeitura estiverem corretas e o login acontecer normalmente, no Sankhya OM, acesse a tela **"Preferência da Empresa"** (Comercial » Preferências » Empresa), vá até a aba **"Documentos Fiscais Eletrônicos",** depois clique na sub aba **"NFS-e >> Geral"** e cadastre o  **"Código do contribuinte da NFS-e",** que corresponde ao número da inscrição municipal.

![Imagem 7: Por outro lado, se as credenciais de acesso ao portal da prefeitura estiverem corretas e o login acontecer normalmente,…](https://ajuda.sankhya.com.br/hc/article_attachments/30528412459159)

![Imagem 8: Por fim, salve as alterações e tente gerar a Nota Fiscal novamente .](https://ajuda.sankhya.com.br/hc/article_attachments/30528194556311) Por fim, **salve as alterações e tente gerar a Nota Fiscal novamente**.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30479563762199)CAUSA:**

Problema ocorre devido falha na autenticação com o WebService do Provedor da Prefeitura. Uma vez que o portal da prefeitura de Florianopólis - SC usa a inscrição municipal para o login, e não o CNPJ como comumente acontece em outros portais.
