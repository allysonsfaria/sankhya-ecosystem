---
id: "360044109334"
titulo: "Usuário/Senha inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109334-Usu%C3%A1rio-Senha-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-17T11:16:56Z"
rotulos: ["Configuração", "Segurança", "Usuário", "Senha", "CORE_E01428", "CORE_E01434", "CORE_E02093", "Verificação de Usuário", "Recuperação de Senha", "Configuração de E-mail", "Erro"]
---

# Usuário/Senha inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18802423949335) MENSAGEM:**

[CORE\_E01428] Usuário/Senha inválido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18802423971735) CAUSA:**

A mensagem está sendo apresentada pois os dados registrados na tela de usuários (Configurações > Controle de Acessos > Usuários), não condizem com o que está sendo digitado no login.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18802408479767) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 4: Verificar se o Caps Lock (tecla que ativa letras maiúsculas) em seu teclado está ativo, pois no acesso se leva em conta…](https://ajuda.sankhya.com.br/hc/article_attachments/18802408483223) Verificar se o Caps Lock (tecla que ativa letras maiúsculas) em seu teclado está ativo, pois no acesso se leva em conta letras maiúsculas e minúsculas.

![Imagem 5: Apague as informações digitadas em USUÁRIO e as digite novamente, pode acontecer de existir algum espaço em branco no…](https://ajuda.sankhya.com.br/hc/article_attachments/18802408487959) Apague as informações digitadas em USUÁRIO e as digite novamente, pode acontecer de existir algum espaço em branco no momento do login.

![Imagem 6: Caso as opções 1 e 2 não sejam suficientes, acione a opção “Esqueci minha senha” : Sistema irá disparar um e-mail para…](https://ajuda.sankhya.com.br/hc/article_attachments/18802423961495) Caso as opções 1 e 2 não sejam suficientes, acione a opção “Esqueci minha senha” : Sistema irá disparar um e-mail para o e-mail cadastrado na aba 'Identificação' do cadastro do usuário. No e-mail vai um link que quando acessado encaminha um novo e-mail com a nova senha.

- Para que esse e-mail seja enviado, é necessário o Servidor SMTP estar devidamente configurado, o parâmetro **ENDACESSEXTWGE**estar com o endereço de acesso externo e o cadastro do usuário estar com o campo “**E-mail**" (Aba Identificação) preenchido.

![Imagem 7: Se as opções acima não estiverem devidamente configuradas, entre em contato com o usuário implantador que detém acesso…](https://ajuda.sankhya.com.br/hc/article_attachments/18802408497047) Se as opções acima não estiverem devidamente configuradas, entre em contato com o usuário implantador que detém acesso ao usuário SUP, para que ele cadastre uma nova senha pela tela “Usuários”.

- Configurações > Controle de Acesso > Usuários, na aba “Identificação”, inserir uma nova senha no campo “Senha”.
