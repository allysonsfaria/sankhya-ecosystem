---
id: "360044616373"
titulo: "ORA-28001: the password has expired"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616373-ORA-28001-the-password-has-expired"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:05Z"
rotulos: ["#RevisadoWellington", "Configuração", "Segurança", "Senha Expirada", "Erro", "Banco de Dados", "ORA-28001"]
---

# ORA-28001: the password has expired

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16782953379095) MENSAGEM:**

[ORA-28001]: the password has expired.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16782953387415) CAUSA:**

Ocorre quando a senha do usuário do banco de dados SANKHYA tenha expirado. Sendo necessário que um DBA Master acesse o banco de dados com permissões de administrador e execute o reset da senha.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16782984570135) SOLUÇÃO:**

![Imagem 4: Solicite que a equipe de TI/DBA da Empresa acesse com um aplicativo de gerenciamento de banco de dados, com o usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/16782953383191) Solicite que a equipe de TI/DBA da Empresa acesse com um aplicativo de gerenciamento de banco de dados, com o usuário **SYS** (A senha para acesso ao Banco de Dados é de responsabilidade do DBA).

![Imagem 5: Execute os comandos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16782953384727) Execute os comandos abaixo:

**(1)** Comando para definir que a senha nunca mais expire:

**ALTER PROFILE DEFAULT LIMIT PASSWORD\_LIFE\_TIME UNLIMITED;**

**(1)** Comando para passar ao banco uma nova senha:
**ALTER USER SANKHYA IDENTIFIED BY novasenha**

**(1)** Em seguida, restaure a senha já utilizada para o usuário:
**ALTER USER SANKHYA IDENTIFIED BY  senha do usuário sankhya**
