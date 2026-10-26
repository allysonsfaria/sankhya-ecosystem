---
id: "44010617615383"
titulo: "Configuração de domínio e subdomínio para publicação da Landing Page"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010617615383-Configura%C3%A7%C3%A3o-de-dom%C3%ADnio-e-subdom%C3%ADnio-para-publica%C3%A7%C3%A3o-da-Landing-Page"
trilha: "Flowbiz > Landing Pages"
atualizado_em: "2026-10-05T18:41:51Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_60", "sync_hash_b6b0e1fdf0d7"]
---

# Configuração de domínio e subdomínio para publicação da Landing Page

Após editado todo o conteúdo e integrado com uma Lista na Flowbiz, é hora de publicar sua Landing Page! Este é também o momento de definir a **URL**, ou seja, o endereço virtual da LP. Este endereço **sempre será constituído por um subdomínio seguido pelo seu domínio**.

Por exemplo: [teste.flowbiz.com.br](http://teste.flowbiz.com.br), sendo “**teste**” o subdomínio e “[flowbiz.com.br](http://flowbiz.com.br)” o domínio.

![Imagem 1: Por exemplo: teste.flowbiz.com.br , sendo “ teste ” o subdomínio e “ flowbiz.com.br ” o domínio.](https://ajuda.sankhya.com.br/hc/article_attachments/44010612789527)

No exemplo usamos a palavra “**teste**”, mas você pode escolher a palavra de sua preferência para ser o subdomínio da sua URL.

**Mas atenção:** você **não pode** usar “**www**” como subdomínio se já tiver essa entrada do **tipo A** cadastrada no painel do domínio escolhido.

Após definir como você deseja o link da sua LP, **é necessário criar a seguinte entrada no painel onde o seu domínio está hospedado:**
**Entrada:** seu subdomínio aqui
**Tipo:** CNAME
**Conteúdo:** [landingpages.mailclick.me](https://landingpages.mailclick.me/)

Seguindo o exemplo da URL [teste.flowbiz.com.br](http://teste.flowbiz.com.br), a entrada ficará assim:

**Entrada:** teste
**Tipo:** CNAME
**Conteúdo:** [landingpages.mailclick.me](http://landingpages.mailclick.me)
Após a entrada ser inserida no painel do seu domínio, para publicá-la basta ir em “Publicar” e selecionar o domínio, conforme imagem abaixo:

![Imagem 2: Entrada: teste Tipo: CNAME Conteúdo: landingpages.mailclick.me Após a entrada ser inserida no painel do seu domínio,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010600455831)

## IMPORTANTE!

- Mesmo você podendo criar e publicar várias LPs, **você pode cadastrar apenas um domínio** para ser utilizado em todas elas.

- **Não há limitação de quantos subdomínios você pode cadastrar**, porém, para cada subdomínio escolhido é necessário repetir o processo de inserir a entrada no painel onde o seu domínio está hospedado.

- Se não quiser criar um novo subdomínio e inserir a entrada no painel do domínio toda vez que for publicar uma LP, **você pode usar um mesmo subdomínio para diferentes LPs**. Para isso, basta mudar o conteúdo que vem após a **/** no link. Exemplos:

[teste.flowbiz.com.br](http://teste.flowbiz.com.br)**/captação**

[teste.flowbiz.com.br](http://teste.flowbiz.com.br)**/ebook**

[teste.flowbiz.com.br](http://teste.flowbiz.com.br)**/curso**

Desta forma, neste exemplo só é preciso inserir a entrada para o subdomínio “**teste**” uma única vez no painel onde está hospedado o domínio.

Caso fique com alguma dúvida, não hesite em nos acionar no chat da ferramenta.
