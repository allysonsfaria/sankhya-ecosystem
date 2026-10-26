---
id: "44011080023319"
titulo: "Como impedir a execução do pop-up em determinadas páginas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011080023319-Como-impedir-a-execu%C3%A7%C3%A3o-do-pop-up-em-determinadas-p%C3%A1ginas"
trilha: "Flowbiz > Campanhas"
atualizado_em: "2026-10-05T18:54:10Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_1173", "sync_hash_14638a82048f"]
---

# Como impedir a execução do pop-up em determinadas páginas

Este tutorial orienta como configurar o GTM (Google Tag Manager) para **impedir que o popup seja exibido em páginas específicas do seu site.**

---

## Passo 1: Criar uma Nova Tag no Google Tag Manager

Acesse sua conta do Google Tag Manager.

No menu lateral, clique em **Tags** e selecione **Nova**.

Nomeie a tag de forma clara, como **Bloqueio de Popup**.

Em Tipo de Tag, selecione **HTML Personalizado**.

No campo de código, insira o seguinte script:

`<script> window.mb_ignore_popup = true; </script>`

Marque a opção **Support para document.write**.

## Passo 2: Configurar o Acionador

Clique em **Acionadores** e selecione **Novo**.

Escolha o tipo de acionador **Exibição de Página**.

Selecione **Algumas Exibições de Páginas**.

Configure a regra da seguinte forma:

**Page Path → Não é igual a → /**

Isso garantirá que o **popup seja executado apenas** na página inicial (**Home**), impedindo sua exibição em todas as demais páginas do site.

## Passo 3: Salvar e Publicar

Clique em **Salvar** para concluir a criação da tag e do acionador.

No menu principal, clique em **Enviar** para **publicar** as alterações.

---

Agora, o pop-up não será mais exibido nas páginas especificadas.
