---
id: "44010840513431"
titulo: "Como inserir o script de integração de assinantes para plataforma Tray."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010840513431-Como-inserir-o-script-de-integra%C3%A7%C3%A3o-de-assinantes-para-plataforma-Tray"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:47:32Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_134", "sync_hash_c29cb3ab331b"]
---

# Como inserir o script de integração de assinantes para plataforma Tray.

Esta documentação orienta o passo a passo para inserir um script de integração na sua loja **Tray** utilizando o **Google Tag Manager (GTM).**

O processo é simples e não requer conhecimento avançado em programação.
**1.** Para a primeira etapa, poderá seguir o video tutorial, para inserir o script base do funcionamento da integração: [Assista ao vídeo](https://youtu.be/IRznO_5IH1k)

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=IRznO_5IH1k)

**2.** Em seguida, vamos precisar configurar a **variável** Nonce, para isso:
**Siga no canto esquerdo > Variáveis.**
Clique em **Nova** > **Nomeie para "nonce"**

![Imagem 1: 2. Em seguida, vamos precisar configurar a variável Nonce, para isso: Siga no canto esquerdo > Variáveis. Clique em…](https://ajuda.sankhya.com.br/hc/article_attachments/44010827819287)

Clique sobre: "**Configuração da Variável**".

E selecione "**Elemento DOM**".

Método de seleção: **"ID" ou "Código" (Depende do idioma do seu GTM)**

Código do elemento: **gtmScript**

Nome do atributo: **data-hash**

![Imagem 2: Nome do atributo: data-hash](https://ajuda.sankhya.com.br/hc/article_attachments/44010806439063)

Prontinho, a integração já foi finalizada, basta publicar as alterações e chamar nosso suporte para validar!
