---
id: "25076930206743"
titulo: "Nenhum e-mail de administradores foi definido. Veja o manual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25076930206743-Nenhum-e-mail-de-administradores-foi-definido-Veja-o-manual"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:46:15Z"
rotulos: ["Configuração", "Segurança", "Nenhum e-mail de administradores foi definido. Veja o manual. ", "Erro", "Autorização de Customizações", "Administrador"]
---

# Nenhum e-mail de administradores foi definido. Veja o manual

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25076915604887) **MENSAGEM:**

Nenhum e-mail de administradores foi definido. Veja o manual.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25076915607575)**SOLUÇÃO:**

Houve várias melhorias na segurança do sistema, incluindo a implantação da tela **"Autorização de Customizações"**.

Esta ferramenta tem como objetivo principal permitir que o Administrador responsável pelo Sistema tenha controle total sobre o que pode ou não ser executado em seu ambiente. Independentemente do usuário que tenha criado ou importado a customização no Sistema (inclusive o SUP), nada será executado até que seja efetivamente liberado.

Recomenda-se a leitura do artigo **"[Autorização de Customizações](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567)"** e a realização das configurações necessárias.

A inclusão do e-mail para a liberação da Autorização de Customizações deve ser feita pela equipe responsável pelo seu TI, no caso de servidor local. Para servidores em nuvem, a inclusão deve ser feita pela empresa responsável.

Seguem abaixo as versões disponíveis com o novo recurso:

**(1)** **4.21** em diante com data de compilação igual ou superior a 22/Fev/2024, independente do build;
**(1)** **4.23** com build **193** ou superior, independente da data de compilação.
**(1)** **4.24** com build **115** ou superior, independente da data de compilação.
**(1)** **4.25** com build **61** ou superior, independente da data de compilação.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25076930203543)**CAUSA:**

O erro acontece ao tentar gerar um código de liberação de uma personalização sem possuir a tela Autorização de Customizações ou mesmo sem que ela esteja devidamente configurada.
