---
id: "29418548848023"
titulo: "Não foi possível validar que o ambiente atual não é de produção, o acesso remoto não pode ser iniciado nesse ambiente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29418548848023-N%C3%A3o-foi-poss%C3%ADvel-validar-que-o-ambiente-atual-n%C3%A3o-%C3%A9-de-produ%C3%A7%C3%A3o-o-acesso-remoto-n%C3%A3o-pode-ser-iniciado-nesse-ambiente"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:37:06Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "br.com.sankhya.mge.conf.AcessoRemoto", "Não foi possível validar que o ambiente atual não é de produção o acesso remoto não pode ser iniciado nesse ambiente", "Erro", "Documentos Fiscais Eletrônicos"]
---

# Não foi possível validar que o ambiente atual não é de produção, o acesso remoto não pode ser iniciado nesse ambiente

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/29418546165399) **MENSAGEM:**

Não foi possível validar que o ambiente atual não é de produção, o acesso remoto não pode ser iniciado nesse ambiente, verifique as informações de registro de base e ambiente NFE

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29418548845719) **SOLUÇÃO:**

Observe se na tela **"Administração do servidor"**, aba **"Registro de base de dados",** a base está registrada como **Teste** ou **treinamento.** Caso esteja como não registrada irá gerar o erro.

![Imagem 3: Observe se na tela "Administração do servidor" , aba "Registro de base de dados", a base está registrada como Teste ou…](https://ajuda.sankhya.com.br/hc/article_attachments/29421555726231)

Verifique também na tela **"Empresa"**(Caminho: Comercial » Preferências » Empresa),  aba **"Documentos fiscais eletrônicos",** sub aba **"NF-e/NFC-e",** se o campo **"Ambiente NF-e/NFC-e"** das empresas está marcado como **"Homologação"** ou **"Não usa"** para todas as empresa cadastradas (caso haja mais de uma).

![Imagem 4: Verifique também na tela "Empresa" (Caminho: Comercial » Preferências » Empresa) , aba "Documentos fiscais…](https://ajuda.sankhya.com.br/hc/article_attachments/29421571745943)

![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/29421397664535)**CAUSA:**

Registro de base ou ambiente NFE como produção.
