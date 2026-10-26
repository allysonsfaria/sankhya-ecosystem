---
id: "9033927285911"
titulo: "Doca não pode ser liberada, pois, a Ordem de Carga: XXX não foi completamente enviada para expedição"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9033927285911-Doca-n%C3%A3o-pode-ser-liberada-pois-a-Ordem-de-Carga-XXX-n%C3%A3o-foi-completamente-enviada-para-expedi%C3%A7%C3%A3o"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:11:19Z"
rotulos: ["Ordem de Carga", "Configuração", "WMS", "Expedição", "Preferências", "CORE_E05125", "Situação na Liberação da Doca", "Erro CORE_E05125", "Solução para Encerrar OC", "Erro"]
---

# Doca não pode ser liberada, pois, a Ordem de Carga: XXX não foi completamente enviada para expedição

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16671968372247) MENSAGEM:**

[CORE\_E05125]: Doca não pode ser liberada, pois, a Ordem de Carga: XXX não foi completamente enviada para expedição.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16671938327703) SITUAÇÃO:**

Ao tentar liberar a doca a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16671938329623) SOLUÇÃO:**

![Imagem 4: Acesse a tela "Formação de Carga" (Caminho de acesso: Comercial » Rotinas » Ordem de Carga » Formação de Carga) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16671938331415) Acesse a tela **"Formação de Carga"** (Caminho de acesso: Comercial » Rotinas » Ordem de Carga » Formação de Carga), filtre a ordem de carga da doca que ira ser liberada e, através do botão **"Outras opções"**, encerre a OC manualmente através da opção **"Encerrar OC"**.

[GIF animado: Imagem 5: Acesse a tela "Formação de Carga" (Caminho de acesso: Comercial » Rotinas » Ordem de Carga » Formação de Carga) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/9352397679255)

![Imagem 6: Para que essa opção seja apresentada, ative o parâmetro "ENCERRAOCMANUAL-Encerrar ordem de carga manualmente?" Na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16671938332951) Para que essa opção seja apresentada, ative o parâmetro **"ENCERRAOCMANUAL-Encerrar ordem de carga manualmente?"**
Na tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências)

![Imagem 7: Para que essa opção seja apresentada, ative o parâmetro "ENCERRAOCMANUAL-Encerrar ordem de carga manualmente?" Na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16671968383127)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16671968386839) CAUSA:**

Quando o pedido é enviado para expedição através da opção **"Enviar para expedição"** ou o parâmetro **"ENCERRAOCMANUAL**" estiver habilitado e o envio foi realizado pela opção **"Enviar para expedição por OC"**, o fechamento da Ordem de Carga será manual.
