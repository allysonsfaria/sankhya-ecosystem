---
id: "4413020620439"
titulo: "Inserir favicon no site"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4413020620439-Inserir-favicon-no-site"
trilha: "Dúvidas Frequentes > E-commerce"
atualizado_em: "2026-07-22T15:20:42Z"
rotulos: ["Configuração", "Cache", "#publicadoHyago", "Envie o arquivo no painel: Aparência -> Arquivos do site", "Crie favicon: 50x50 formato .ico nome favicon.ico", "Configure TAG no painel: Configurações -> Loja limpe o cache", "Aparência", "Site", "Arquivos do site"]
---

# Inserir favicon no site

Favicon é uma pequena imagem presente dentro da aba do navegador, geralmente, o mais utilizado é a logo da empresa. Abaixo, temos um exemplo de favicon:

![Imagem 1: Favicon é uma pequena imagem presente dentro da aba do navegador, geralmente, o mais utilizado é a logo da empresa.…](https://ajuda.sankhya.com.br/hc/article_attachments/15696722126103)

Para inserir o favicon no site, realize as seguintes configurações:

![Imagem 2: Crie a imagem do Favicon, de sua preferência, com as seguintes configurações:](https://ajuda.sankhya.com.br/hc/article_attachments/16192750013591) Crie a imagem do Favicon, de sua preferência, com as seguintes configurações:

| **Tamanho:** 50x50  **Formato do arquivo:** .ico  **Nome do arquivo:** favicon.ico |
| --- |

![Imagem 3: Insira o arquivo no painel administrativo](https://ajuda.sankhya.com.br/hc/article_attachments/16192736586391) Insira o arquivo no painel administrativo

Após realizar a criação do arquivo de ícone, acesse o caminho: **Painel Administrativo -> Aparência -> Arquivos do site**

![Imagem 4: Após realizar a criação do arquivo de ícone, acesse o caminho: Painel Administrativo -> Aparência -> Arquivos do site](https://ajuda.sankhya.com.br/hc/article_attachments/15696727575959)

![Imagem 5: Envie arquivos](https://ajuda.sankhya.com.br/hc/article_attachments/16192736587927) Envie arquivos

Clique no botão **"Enviar arquivos"**, selecione o arquivo desejado. Após inserir, o mesmo ficará salvo no diretório do painel administrativo, conforme a imagem abaixo:

![Imagem 6: Clique no botão " Enviar arquivos" , selecione o arquivo desejado. Após inserir, o mesmo ficará salvo no diretório do…](https://ajuda.sankhya.com.br/hc/article_attachments/15696767706007)

![Imagem 7: Configure a TAG](https://ajuda.sankhya.com.br/hc/article_attachments/16192750019607) Configure a TAG

Após ter realizado o upload do arquivo para o painel administrativo, realize a configuração da TAG, para que o site reconheça o arquivo inserido. Para realizar a configuração, primeiramente acesse o caminho: **Painel Administrativo -> Configurações -> Loja.** Dentro dessa tela, localize o número da loja, pois no script seguinte iremos utilizar este número.

Campo: **"Número da loja"**

Ainda nessa tela, insira o script abaixo, dentro do campo **Metas Tags.**

<link type="image/icon" rel="shortcut icon" href="/lojas/**Número da loja**/favicon.ico" />

Veja um exemplo de TAG, utilizando a loja de numero 2101.

![Imagem 8: Veja um exemplo de TAG, utilizando a loja de numero 2101.](https://ajuda.sankhya.com.br/hc/article_attachments/15696799289751)

![Imagem 9: Limpe o Cache](https://ajuda.sankhya.com.br/hc/article_attachments/16192750021143) Limpe o Cache

Após realizar as configurações, limpe o cache da loja e do navegador. Em seguida, realizado esses passos, o favicon será apresentado com sucesso.
