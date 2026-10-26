---
id: "42427465890327"
titulo: "Integração com Facebook Leads Ads"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427465890327-Integra%C3%A7%C3%A3o-com-Facebook-Leads-Ads"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:39Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452431", "sync_hash_d447351a03f9"]
---

# Integração com Facebook Leads Ads

Esta documentação detalha o funcionamento da integração entre o Ploomes e o Facebook Lead Ads. Você aprenderá como os leads capturados em formulários da Meta são enviados automaticamente para o CRM, quais comportamentos podem ser configurados e as regras gerais de comunicação entre os sistemas.

## 1) Sobre o Facebook Lead Ads

O **[Facebook Lead Ads](https://web.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-forms)** é uma solução de anúncios da Meta que permite criar e veicular campanhas nas plataformas da marca, como **Facebook e Instagram**. Um dos formatos disponíveis é o de **formulários de captação de leads**, que simplificam o processo de inscrição do cliente final.

## 2) Objetivos da Integração

A integração com o Ploomes tem como objetivo importar automaticamente os leads capturados nos formulários do Facebook Lead Ads para a conta do CRM, facilitando o acompanhamento e o gerenciamento das oportunidades geradas.

Com a integração ativa, esses leads são enviados diretamente para o Ploomes, respeitando o **mapeamento de campos configurado em cada formulário**, garantindo maior agilidade no contato e melhor aproveitamento das oportunidades comerciais.

## 3) Escopo geral da integração

Por meio da integração, todos os leads que preencherem formulários do **Facebook Lead Ads** vinculados à página integrada no Ploomes — incluindo formulários originados de outras plataformas, como Instagram — serão enviados para o CRM.

Ao chegar no Ploomes, os leads podem ser utilizados para criar **pessoas, empresas e negócios**, de acordo com as configurações definidas pelo usuário.

Vale destacar que a comunicação é **unidirecional**: o Ploomes recebe dados do Facebook, mas **não envia informações de volta** para a plataforma de anúncios. Alterações feitas no Ploomes não serão refletidas no Facebook Lead Ads.

O envio é realizado via **webhooks**, o que significa que os leads são transmitidos assim que o formulário é preenchido. Em condições normais, a integração ocorre quase em tempo real, podendo haver pequenas variações em cenários de alto volume.

## 4) Ativando a Integração no Ploomes

**Para integrar é necessário que o usuário tenha permissão de administrador na página do Facebook**.

Na Ploomes, acessar o painel de integração pelo caminho: **Administração > Integrações Plug-and-Play > selecione a integração com o Facebook:**

![Imagem 1: Na Ploomes, acessar o painel de integração pelo caminho: Administração > Integrações Plug-and-Play > selecione a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642793787/558bc3a461b80eca3409eb98e7ac/AD_4nXeebYnOT-ERJfk1VaJT0qKg2nNjmSbP66TzE-yGnD0lIA7z8N8yhPN9OgzQQm6t46h9KoLsSagsFEdfK_aGaCtK81sWzHFtE0w9AN_T8V7i4nJJbPnA6AWPl3cnoZOiLBDlA7ndrxX_FdwZOXHentWr60j2?expires=1786536000&signature=5bf20407331acaa6f6274a0a7080bb6659b37cb9c227164602f49d31d5c35c26&req=dSYjFM53noZXXvMW3nq%2BgYRbfcl56u%2BOaNQ0p0HEWaLJALAUgoWxgkrOFZej%0AxN7V%2BIBDdAP34h6yi8k6VjB7Xig%3D%0A)

Clique em **“Habilitar integração”** e depois em **“Autorizar integração”**. Um pop-up vai abrir no navegador. Caso haja algum usuário do Facebook logado no momento da autorização, o pop-up vai perguntar se deseja conectar seu usuário ao Ploomes, quais páginas você deseja integrar, e exibir as permissões requeridas pela integração.

Pontos importantes:

- É importante que todas as permissões sejam aceitas, caso contrário a integração pode não funcionar corretamente.
- É obrigatório que o usuário logado fazendo essa autorização tenha o perfil de **administrador** **de todas as páginas que deseja integrar**. Apenas assim ele poderá fornecer todas as permissões que a integração precisa para funcionar.
- Caso **não** haja usuário logado, o pop-up apresentará uma tela de login no Facebook ao abrir.

![Imagem 2: Caso não haja usuário logado, o pop-up apresentará uma tela de login no Facebook ao abrir.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330098/b87dc9320519e7513d487c0c/mceclip2.png?expires=1786536000&signature=35826fc031e3564901941436f7aa98e77d7dca68f9e3b8242cc5e2bd1a9be535&req=dyYuFcp%2BnYhXFb4V1XW4gRS8AuaNW0O4D3rBdGIh7kUksXvssrKd7OVLMt3f%0A1wF5c5v2SY%2F4cBSwbVx8Yj72aw%3D%3D%0A)

Todas as páginas selecionadas serão inscritas na integração (pelos webhooks).

![Imagem 3: Todas as páginas selecionadas serão inscritas na integração (pelos webhooks).](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330107/0cd6a6fc05d0ba39520da965/mceclip3.png?expires=1786536000&signature=ee6a4989c219c0cfdf1d61dd352fd1eaca7e54d575ed9554859ecdea757b3ee1&req=dyYuFcp%2BnIFYFb4V1XW4gRsYWKYjk7lNwOYy47MfDIkBg3%2BGxogmk%2Fg0M682%0AmoGAjmDdeFU%2Bpak3DAN1ujjT%2FA%3D%3D%0A)

Para finalizar, clique em “Concluir” e a configuração no Facebook estará pronta!

Caso a autorização tenha sido feita com sucesso, uma notificação aparecerá na tela e a integração ficará marcada como autorizada.

Após isso, é necessário selecionar o comportamento a ser realizado quando recebermos leads do Facebook entre três opções:

![Imagem 4: Após isso, é necessário selecionar o comportamento a ser realizado quando recebermos leads do Facebook entre três…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642797825/2d14a0a2b7882e47d6dc87264bb6/AD_4nXf9W-SkjoLgeTcXcVUk3dgNP8hFpV3AxLFQ2HMKmJ_M4j_gshY8k0VPagtQ7pMKa3uIxvkFSA75cLrp6yGVoYjfwvUYogSFNSXYbkasc9mrpLhbaGu6sSLWxL42l-G1Yq4lkrn1qqiYxdU21Ow_jhpRfFUE?expires=1786536000&signature=984f629f601da29b7d994b5bf6bde798d872472973ff67aded9b8716a9b20577&req=dSYjFM53moldXPMW3nq%2BgSgXZ6VZfyt0aX%2F5B7qp7ifCjJ1tPcXixuwM9b%2F0%0AJ%2BOcLNVnuCals4hAxc%2Fye93wFig%3D%0A)

Caso a opção envolva a criação de negócios, é necessário selecionar em qual estágio de funil ele será criado e se devemos criar um novo negócio ou atualizar o anterior caso o mesmo lead seja enviado duas vezes pelo Facebook.

![Imagem 5: Caso a opção envolva a criação de negócios, é necessário selecionar em qual estágio de funil ele será criado e se…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642797519/4d2304e4d386cbb296bcc147a2b0/AD_4nXdWrsvtq30n2bOhx1mSxxd3mOpscrd0NSNxzYzapq9kxRqO6GOLCn0DQvcdKq-Fh5nBVk_PXzkEg25T5h9-ciBUIfvfr47n5NgMHGHpAbBzXMnsHCtZSOkhlMYROlWkMjE0_VF-VnvZWoRst-f3yOjRr2I_?expires=1786536000&signature=b0e843f1f094f57e753c844d022301f9b7cde6f3676857a2c892dd0714da1438&req=dSYjFM53moReUPMW3nq%2BgSs3GZD0X8CQDNX3lEECSik1A1yDjLFplfbk9zph%0AyEVlQ%2FHZJFMxUp7y27g6beJohoE%3D%0A)

Diferente das demais integrações, não existem mapeamentos padrão na integração com o Facebook, por conta da possibilidade de integrar múltiplos formulários de múltiplas páginas diferentes. Ao exibir as opções de mapeamento, serão exibidas as páginas integradas:

![Imagem 6: Diferente das demais integrações, não existem mapeamentos padrão na integração com o Facebook, por conta da…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642798082/3c9c8ae6a0164388a5641c6451cc/AD_4nXcfEB0SE-xtz2H2bkzNqxr15CQcJpAAHbYESKu5VrHNCJuiFhu2k1LvOS6l17LXwUKxuD0sVYLO6-darKN2iotNKl2qRZaqg3mb0HzT3yOIjS869uDRlJXEWV-HettD6Cs1h7rtgmQT4lUGS3O7dP3nGXS6?expires=1786536000&signature=43f6f2ef48a1633e882e543e86b758b4a05f2965526763b79d1a2103f3ac3a27&req=dSYjFM53lYFXW%2FMW3nq%2BgYUyVzkOlmpYnHlPAICzA7C0lDGKhVQJZnMha4QC%0A0%2F%2Fub8yPSAlgZJvEgQQaMkxaVlg%3D%0A)

Selecionando uma, serão exibidos os **formulários** dessa página:

![Imagem 7: Selecionando uma, serão exibidos os formulários dessa página:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642798387/7688c78c335c39db38ec1093c3fc/AD_4nXfnlS8Q_NkhCk35kLgmuy49TkjniX_JPfeJ6Vw6N23s-Vwx5ySUYClv9ApGmM2scfhOhfRmZZgrv6UK6IDOkiRtXY8ze1jeXzm3AqOH2uYnIQn8ZiTGh7nHlCZJiwSAuyn7DL5OqfRE7Bxp504vKefR3Mk?expires=1786536000&signature=ccd2095e333fa5f86050d32e202e6e653b6b396a06f4b18d92a76440ac115132&req=dSYjFM53lYJXXvMW3nq%2BgbkFTdlIu2H7HH1Z91CGNzY%2F8fPd%2Fcctzjr5zSE3%0ADUKdM953gyNGw2v71CRocyprO6U%3D%0A)

E dentro do formulário, os campos dele para serem mapeados:

![Imagem 8: E dentro do formulário, os campos dele para serem mapeados:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642798665/0ba57769b6414c01254c3df418c1/AD_4nXddwUFKKgcqQXej33Qgqh3mm4NAtprlomw6HiUPAm0O8OAIyTmf_5RRKwn0LmWsfbpSZz1SOXFEgajXgSybVfh4p9M-r5FxE4mAVlFoYNxIqRQyWUNwvU1kuMWISf_64AxvMZYtr4nr9TgooT4P4c1kL3w3?expires=1786536000&signature=af5962f0577abb29a27b431b9e8a492e8f0dbe7ff34f3cfab6205f1db5d297a0&req=dSYjFM53lYdZXPMW3nq%2BgdRUeGQjYNG3h8TjDuMM3WUSr0SkbukMd4ILwKhD%0Aiwqjafn8lIvv4DroAzA40X27oOo%3D%0A)

## 5) Mapeamento dos campos

As possibilidades de mapeamento são diversas, mas há 3 campos **obrigatórios** para serem mapeados antes dos demais (é necessário realizar esses mapeamentos para cada formulário que deseja integrar, mas apenas se configurou para criar a entidade):

1. No mapeamento de cliente, mapear algum campo do Facebook para **Cliente.Nome**
2. No mapeamento de contato, mapear algum campo do Facebook para **Contato.Nome**
3. No mapeamento de negócio, mapear algum campo do Facebook para **Negócio.Título** (obrigatório apenas caso a criação de negócios esteja habilitada

Além disso, a integração do Ploomes com o **Facebook Lead Ads** oferece suporte a **todos os campos nativos** da plataforma, assim como a **todos os tipos de perguntas personalizadas** criados nos formulários.

![Imagem 9: Além disso, a integração do Ploomes com o Facebook Lead Ads oferece suporte a todos os campos nativos da plataforma,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642809806/baf083c09fe74c745f7ce79a0c3a/AD_4nXeqNcxu04VxyZ0C6Xgsml5CyMbS3duI15fs3Ag3oL2JrOVWNp1d2Sh3U_YvbhFWwJg-Qa52amm5tvW6VQ8gxmAynfcvr8Rpq5aL7Jbx6a4AtpeecVSQQYekaxS8KbUYoEtVzT75MACemWXKo1JPxFwjQVsJ?expires=1786536000&signature=0e1013e7704c1743b814dd71c99b266131adb2eceadd34f58fdaa5145a7666d6&req=dSYjFMF%2BlIlfX%2FMW3nq%2BgcI%2FSXUg1%2FOf5Mpub6WY5TPgFo8HkNbPQ3N7H%2BE0%0A8wyiUhHrKLIjD6y5Z3dFN52B8K8%3D%0A)

## Campos de Resposta Curta, Condicionada e Hora Marcada

- Podem ser mapeados para **campos de texto simples** ou **multilinha** do Ploomes, independentemente do valor informado.
- Também é possível mapear para **campos numéricos**, porém o valor só será integrado corretamente se a resposta for **totalmente numérica**, sem espaços ou caracteres adicionais.
- **Recomendação:** quando possível, utilize **perguntas de múltipla escolha** para restringir as respostas do lead ou mantenha o uso de campos de texto simples para evitar inconsistências.

## Perguntas de Múltipla Escolha

- Podem ser mapeadas para **campos de Opção Pré‑Cadastrada** do Ploomes.
- **Atenção:** se as opções de resposta contiverem **acentos ou espaços**, o Ploomes poderá gerar variações indesejadas no nome da opção (por exemplo: substituir espaços por “\_”, remover acentos ou converter para letras minúsculas).

**Exemplo:**

- Opção no Facebook: `1 - A`
- Resultado no Ploomes: `1_-_a`

No exemplo acima, a opção foi criada no Ploomes por um usuário como “1 - A” porque esta é uma das possíveis respostas no Facebook, na intenção de que essa fosse a opção utilizada pela integração ao integrar os leads. Porém, ao integrar um lead que selecionou a opção “1 - A” no Facebook, a integração criou e utilizou a opção “1\_-\_a”.

![Imagem 10: No exemplo acima, a opção foi criada no Ploomes por um usuário como “1 - A” porque esta é uma das possíveis respostas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642810330/5d559020df94a04f601952e53a5c/AD_4nXcwCUSes-Un4myiCVmGoMXpEs_lIe7Sb2t__07rzdJKHmjeAxSJL3QH6Q9CV1psZlo3kBEJxO-6dbpDsx3MiwZnIIqptR6MWJSGdhtOKwmCd8uz71lPYFZG0_YC104fXH3m0iC_9AHMDqS1dWr-RBbfsJNU?expires=1786536000&signature=294e5b71a856610d0a4483b112e3352fa6be600a981b4b5ae852a8f3f1befb94&req=dSYjFMF%2FnYJcWfMW3nq%2BgW5lxW%2FTfRscHst3VDs7MuMpbWML%2BUA7eroro1iv%0ARQTogKK9XXKPm2RaOS9iHQEAHEk%3D%0A)

Para resolver isso, é necessário alterar como os nomes dos campos são exibidos ao exportar os leads no Facebook:

Na tela de perguntas do formulário, vá em **Configurações > Configurações do formulário > Nomes dos campos:**

![Imagem 11: Na tela de perguntas do formulário, vá em Configurações > Configurações do formulário > Nomes dos campos:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642799754/91b83472687c7234a42ace7b54db/AD_4nXceaLEYK-8QNZPFYCFqES0iXZvUfJByCs0J-UnNmMrvDkNKfJ91Iw5CqY9RCaXh0eIGXt7NwMgBfZ3ajCm3EieEOz8DAd7WqeB4gUV5liUSkXOlouy4aIuC-OTsidT20G0XG0kWj0AL7jXxofup_Arft02E?expires=1786536000&signature=827b11793c54b07b95e676af0d7840ff7b618ed1e70611ee99820f7cf8657726&req=dSYjFM53lIZaXfMW3nq%2BgVtmGtByj1BA0mDFmWH3oQKoQVm%2FpkS%2BMi9N0iN1%0A%2Bm7iA9YLjR7YTAQj%2B0Hx2o5EMoA%3D%0A)

Nessa tela, as perguntas e respostas presentes no formulário serão exibidas, e será possível a forma como os valores das opções serão integrados por padrão.

Na mesma tela, revise as perguntas e respostas e **defina como os valores devem ser exportados** para o Ploomes:

![Imagem 12: Na mesma tela, revise as perguntas e respostas e defina como os valores devem ser exportados para o Ploomes:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642800034/752bd24a96c9c701f3c520387f6c/AD_4nXeJ77Gp0R-715StlXhUPLXShQuHlntywJy0Oer8qux_ZltECcfrqXvQnM2wId_w1-f2QEKzrZSTRZCVc8fgeh0z80RtahdRqBUocDDthRosivkr_WC5VDEnGRGcSEJTw2zpCf3zKvTNA0PRy_w99RG1aWk?expires=1786536000&signature=1901c21d295557bf8205828b2e8b5d2d810be18d866f2ff01bf5d2688361102f&req=dSYjFMF%2BnYFcXfMW3nq%2BgZRsC1ILI8cxU0Oxr%2BgtEVHYnnQhbcEYuY5t1wSN%0ABJeuCUKnMqgmLnBgLGFdGoKox7E%3D%0A)

Ao salvar, as opções serão integradas de forma consistente, evitando problemas de formatação.

## 6) Informações importantes

### 6.1) Integração por Página do Facebook

- Cada **página do Facebook** pode ser integrada apenas com **uma única conta do Ploomes**.
- Para integrar a mesma página em outra conta do Ploomes, é necessário **remover todos os mapeamentos existentes** relacionados a essa página na conta anterior.

### 6.2) Identificação de Duplicidades

A integração realiza verificações para evitar a criação de registros duplicados ao importar leads:

#### Pessoas

- Se o campo **E-mail (nativo do Ploomes)** estiver mapeado no formulário do Facebook, ele será utilizado para identificar duplicidades.
- Caso o e-mail **não esteja mapeado**, a identificação é feita pelo campo **“Id (Facebook Lead Ads)”**, criado automaticamente pela integração.

#### Empresas

- A duplicidade é verificada inicialmente pelo campo **“Id (Facebook Lead Ads)”** (campo customizado).
- Se não houver correspondência, é utilizada a correspondência pelo **Nome (nativo do Ploomes)**.

#### Negócios

- O sistema verifica se o negócio **pertence ao cliente** e se o **status está ativo** antes de criar ou atualizar.

### 6.3) Campos criados automaticamente pela Integração

Além do campo **“Id (Facebook Lead Ads)”**, a integração cria também o campo **“Formulário de origem (Facebook)”** em contatos e empresas.
Este campo identifica **qual formulário originou o lead**, permitindo o uso em automações, filtros e relatórios.

### 6.4) Compatibilidade com Versões Anteriores

- Em versões antigas da integração (e na documentação anterior), todos os mapeamentos — **contato, cliente e negócio** — eram configurados apenas na aba **“Mapear campos de Negócios”**.
- Nessa configuração, os mapeamentos obrigatórios eram:

  - `Negócio.Título`
  - `Negócio.Contato`
  - `Negócio.Contato.Empresa`

Estes mapeamentos ainda funcionam para contas antigas, mas **recomendamos** que novas configurações sejam feitas **separando os mapeamentos por entidade** (Pessoa, Empresa e Negócio) para facilitar manutenção e organização.

---

## FAQ

### 1. Tenho mais de um formulário. Preciso mapear os campos duas vezes?

**Sim.** Cada formulário do Facebook Lead Ads possui seus próprios campos, mesmo que tenham o mesmo nome. Portanto, é necessário mapear os campos **individualmente** para cada formulário.

### 2. Meus leads estão vindo com um código ao invés do nome. Por quê?

Isso ocorre quando os campos **Nome do Contato** ou **Nome da Empresa** não foram mapeados.

- Nesse caso, o Ploomes utiliza o **código do lead** gerado pelo Facebook para permitir a criação da Pessoa e da Empresa, já que o campo Nome é obrigatório.

### 3. Como identificar formulários diferentes na lista de mapeamento?

No mapeamento, os campos aparecem **separados por pontos**, indicando:

- **Página > Formulário (Ad) > Nome do Campo**

Exemplo**:**

![Imagem 13: Exemplo :](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642815496/f48ccd77c8adbef722ac2d9a27b7/mceclip4.png?expires=1786536000&signature=9dfdea457cdb7b5e6cd0f31463ed3c0580f62c7cf7de4a4d0e0670642ba32909&req=dSYjFMF%2FmIVWX%2FMW3nq%2BgVUK2yF71x6ixVy5X3W%2F3YiXk63Wyf5d5Lx49Zdn%0A778qdprByskbcvwUH6xCUtzMtOw%3D%0A)

### 4. Fiz todo o procedimento corretamente, mas os Negócios não estão sendo criados. O que fazer?

Verifique se **os campos obrigatórios** do formulário de **Clientes e Negócios** estão devidamente mapeados.

- Se algum campo obrigatório não estiver mapeado, a integração **não criará** o Negócio ou o Cliente.

### 5. É possível saber de qual campanha veio o Lead?

Não. O criador do lead sempre será identificado como **Facebook** e não há informação nativa da campanha específica.

- Porém, é possível criar **um campo personalizado na campanha do Facebook** e mapear esse campo para o Ploomes, garantindo que a informação seja registrada.

### 6. Existe algum mapeamento padrão obrigatório para que a integração funcione?

Sim. Se a integração estiver configurada para criar **Empresa, Pessoa e Negócio**, os seguintes campos precisam ser mapeados (por campanha):

- `Cliente.Nome`
- `Negócio.Título`
- `Contato.Nome`

### 7. Como realizar testes de envio de Leads?

O **Facebook Developers** permite o envio de leads de teste.

- Apenas **administradores da página** conseguem realizar o teste e precisam estar **logados** na conta para executá-lo.
- Link para testes: [Lead Ads Testing Tool](https://developers.facebook.com/tools/lead-ads-testing)

### 8. Como identificar um erro no envio de Leads pelo Developers?

- Utilize o **ID de aplicativo do Ploomes**: `1002969563443299`.
- O Facebook Developers exibirá o **erro diretamente na página** de testes, facilitando o diagnóstico.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 14: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2080377347/4d02230337cf2d2211654472390a/image.png?expires=1786536000&signature=34306b0ddfc3588824f46890b47749406942fab4fecff5bdc327512514ac84e9&req=diAvFsp5moJbXvMW3nq%2BgclS2dETcYMc4Y6Yxi%2BABV5ApD7g6xIwHhqGeGmb%0AFIGAqx%2FozY%2FLrBZ0%2Flakjs54N8Y%3D%0A)](https://universidade.ploomes.com/courses/integracao-facebook-lead-ads)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com)
