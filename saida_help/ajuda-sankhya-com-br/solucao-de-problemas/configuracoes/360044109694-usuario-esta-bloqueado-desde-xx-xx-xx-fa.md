---
id: "360044109694"
titulo: "\"Usuário está bloqueado desde XX/XX/XX. Favor solicitar o desbloqueio ao administrador do sistema ou aguarde o desbloqueio automático programado para YY/YY/YYYY \""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109694--Usu%C3%A1rio-est%C3%A1-bloqueado-desde-XX-XX-XX-Favor-solicitar-o-desbloqueio-ao-administrador-do-sistema-ou-aguarde-o-desbloqueio-autom%C3%A1tico-programado-para-YY-YY-YYYY"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-04T15:35:08Z"
rotulos: ["#criadoRoger", "#Revisadoclaudio", "Configuração", "Segurança", "Controle de Acessos", "Usuário", "Usuário Bloqueado", "Solicitação de Desbloqueio", "Controle de Acesso", "Erro"]
---

# "Usuário está bloqueado desde XX/XX/XX. Favor solicitar o desbloqueio ao administrador do sistema ou aguarde o desbloqueio automático programado para YY/YY/YYYY "

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16807154958615) MENSAGEM :**

"Usuário está bloqueado desde XX/XX/XX. Favor solicitar o desbloqueio ao administrador do sistema ou aguarde o desbloqueio automático programado para YY/YY/YYYY ".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16807095371415) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Solicite que o Implantador, Gerente, com as devidas permissões, acesse:](https://ajuda.sankhya.com.br/hc/article_attachments/16807154969239) Solicite que o Implantador, Gerente, com as devidas permissões, acesse:

- Tela **"Usuários"** (Caminho de acesso: Configurações » Controle de Acesso);
- Selecione o usuário bloqueado;
- Botão 'Outras Opções' [...];
- Clique em "**Remover bloqueios de Acesso**";

![Imagem 4: Solicite ao usuário tentar o acesso novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16807154973207) Solicite ao usuário tentar o acesso novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16807154977559) CAUSA:**

Ocorre mediante tentativas excedidas de login incorretas, levando ao bloqueio do usuário.

(1)** Parâmetros:**

(2)** LOGTEMP:** determina a quantidade de vezes para tentativa incorretas de login. Zero ou menor que zero será considerada 3 tentativas e haverá o bloqueio.

(2)** LOGBLOQ:** determina quantidade de dias para desbloqueio automático. Maior que zero, passa a bloquear.
