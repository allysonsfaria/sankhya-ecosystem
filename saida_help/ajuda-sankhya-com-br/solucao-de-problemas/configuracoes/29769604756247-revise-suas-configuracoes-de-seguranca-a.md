---
id: "29769604756247"
titulo: "Revise suas configurações de Segurança. Algumas opções de segurança estão desativadas e podem impactar a proteção do sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29769604756247-Revise-suas-configura%C3%A7%C3%B5es-de-Seguran%C3%A7a-Algumas-op%C3%A7%C3%B5es-de-seguran%C3%A7a-est%C3%A3o-desativadas-e-podem-impactar-a-prote%C3%A7%C3%A3o-do-sistema"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:36:51Z"
rotulos: ["Configuração", "Segurança", "Autenticação", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Revise suas configurações de Segurança", "Algumas opções de segurança estão desativadas", "Dsnk.strong.password.high.privilegies", "Dsnk.use.action.auth", "Senhas"]
---

# Revise suas configurações de Segurança. Algumas opções de segurança estão desativadas e podem impactar a proteção do sistema

![Imagem 1: AVISO:](https://ajuda.sankhya.com.br/hc/article_attachments/29769604745495) **AVISO:**

Revise suas configurações de segurança

Algumas opções de segurança estão desativadas e podem impactar a proteção do sistema.

**-Dsnk.use.action.auth -** autorização de customizações

**-Dsnk.strong.password.high.privilegies** - validação de senhas fortes para usuários com acessos privilegiados

![Imagem 2: -Dsnk.strong.password.high.privilegies - validação de senhas fortes para usuários com acessos privilegiados](https://ajuda.sankhya.com.br/hc/article_attachments/29877168350231)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29881714434711)SOLUÇÃO:**

Este é um alerta de segurança exibido para o usuário SUP ao realizar o login no sistema. Ele exibe as flags que estão desabilitadas, mas que são recomendadas para estar ativadas.
Recomenda-se a ativação da preferência **Dsnk.strong.password.high.privilegies** para aumentar a segurança da aplicação.
Ao ativá-la, todos os usuários com acessos privilegiados serão obrigados a alterar suas senhas para senhas mais robustas no próximo login.
Usuários com acessos privilegiados são aqueles que possuem permissões para acessar telas administrativas do sistema, tais como:

- Criação de telas personalizadas;
- Administração do Sistema;
- Criação de dashs;
- Ações Agendadas.

Referente a preferencia **Dsnk.use.action.auth**recomenda-se seguir as configurações do artigo [Autorização de Customizações](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/29769575298071)CAUSA:**

Esse é um aviso implementado a partir da Versão 4.33 que visa alertar o administrador do sistema sobre a necessidade de aprimorar a segurança.
