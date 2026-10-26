---
id: "9852751790871"
titulo: "Ordem de carga já foi enviada para o WMS, não pode mais ser utilizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9852751790871-Ordem-de-carga-j%C3%A1-foi-enviada-para-o-WMS-n%C3%A3o-pode-mais-ser-utilizada"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:05:44Z"
rotulos: ["Ordem de Carga", "Configuração", "WMS", "Preferências", "WMS_E00645", "OC já enviada", "OC encerrada e não reutilizável", "Habilite \"ENCERRAOCMANUAL\"", "Erro"]
---

# Ordem de carga já foi enviada para o WMS, não pode mais ser utilizada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19480890692631) MENSAGEM:**

[WMS\_E00645] Ordem de carga já foi enviada para o WMS, não pode mais ser utilizada.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19480890702999) SITUAÇÃO:**

Ao enviar para expedição por OC a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19480890709271) CAUSA:**

Ocorre quando a OC já foi enviada para separação e foi encerrada não permitindo o envio novamente.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19480919318167) SOLUÇÃO:**

Caso seja necessário o envio da mesma OC para expedição mais de uma vez pela tela formação de carga, habilite o parâmetro **ENCERRAOCMANUAL.** Assim, o fechamento da OC acontecerá de forma manual, permitindo o vínculo de pedidos e o envio quantas vezes forem necessária.

Caso deseje habilitar este parâmetro, acesse a tela **Preferências** (Caminho de acesso á tela: Configurações » Avançado » Preferências), informe a chave do parâmetro '**ENCERRAOCMANUAL-Encerrar ordem de carga manualmente?'** e ligue-o.

![Imagem 5: Caso deseje habilitar este parâmetro, acesse a tela Preferências (Caminho de acesso á tela: Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/19480890716183)
