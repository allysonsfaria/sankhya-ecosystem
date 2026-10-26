---
id: "44010336439447"
titulo: "Como criar uma jornada para carrinho abandonado por e-mail"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010336439447-Como-criar-uma-jornada-para-carrinho-abandonado-por-e-mail"
trilha: "Flowbiz > Jornadas"
atualizado_em: "2026-10-05T18:36:01Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_8", "sync_hash_cc86fa55573e"]
---

# Como criar uma jornada para carrinho abandonado por e-mail

Neste artigo, você verá como criar uma jornada de carrinho abandonado por e-mail, com um tutorial em vídeo e um passo a passo detalhado ao longo do conteúdo.

<https://www.youtube.com/watch?v=rrUZDg2qtj8>

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=rrUZDg2qtj8)

Saiba como criar uma automação de carrinho abandonado por e-mail com o Jornadas e recupere suas vendas!

Para começar, clique em **Jornadas > Minhas Jornadas** e, em seguida, selecione **Criar Jornada > Carrinho Abandonado > E-mail > Selecionar**.

![Imagem 1: Para começar, clique em Jornadas > Minhas Jornadas e, em seguida, selecione Criar Jornada > Carrinho Abandonado >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010370665111)

## Na Etapa 1 - Configurações

insira o nome da sua jornada. Para facilitar, você pode clicar em **Utilizar Sugestão** e alterar o tempo de envio conforme desejado. Em seguida, clique em **Continuar**.

![Imagem 2: insira o nome da sua jornada. Para facilitar, você pode clicar em Utilizar Sugestão e alterar o tempo de envio conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/44010311545239)

## Na Etapa 2 - Dados do E-mail

Adicione o **assunto** que chame a atenção do cliente. É recomendado incluir a variável **%Customer:Name%** para personalização. Para isso, clique em **Adicionar Conteúdo Dinâmico** e escolha entre **Primeiro Nome** ou **Nome Completo**. **Dica:** Insira a variável seguida de um espaço e comece o assunto com letra maiúscula.

**Nome e E-mail do Remetente:** Preencha com o nome que aparecerá para os clientes. Insira um e-mail válido. Se o endereço informado não existir, desmarque a opção **"Usar as mesmas informações do remetente para resposta do e-mail"** e coloque um endereço válido.

**Importante:** Isso garante que, se o cliente responder à jornada, a resposta será direcionada para um e-mail válido.

Feito isso, clique em **Continuar**.

![Imagem 3: Feito isso, clique em Continuar .](https://ajuda.sankhya.com.br/hc/article_attachments/44010324699799)

## Na Etapa 3 - Conteúdo do E-mail

Selecione um modelo de template para iniciar a criação do e-mail. Você também pode usar a aba **Jornadas Anteriores** para selecionar uma jornada já existente como base.

![Imagem 4: Selecione um modelo de template para iniciar a criação do e-mail. Você também pode usar a aba Jornadas Anteriores para…](https://ajuda.sankhya.com.br/hc/article_attachments/44010345601943)

Adicione o conteúdo do e-mail e inclua a variável **%Link:CartRecovery%** em todas as imagens e botões. Isso garantirá que, ao clicar, o cliente seja redirecionado para o carrinho abandonado.

![Imagem 5: Adicione o conteúdo do e-mail e inclua a variável %Link:CartRecovery% em todas as imagens e botões. Isso garantirá que,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010355745303)

Adicione também um **Pré-cabeçalho** para complementar o e-mail com um texto atrativo.

![Imagem 6: Adicione também um Pré-cabeçalho para complementar o e-mail com um texto atrativo.](https://ajuda.sankhya.com.br/hc/article_attachments/44010356033687)

## Como Adicionar Logos e Banners no Editor de E-mail

Após selecionar o template, para adicionar o logo, localize o primeiro contêiner superior, clique no ícone de círculo e insira a imagem do logo desejado.

Para adicionar o banner, localize o contêiner onde ele será inserido, clique novamente no ícone de círculo, escolha a imagem do banner e adicione-a ao contêiner.

![Imagem 7: Para adicionar o banner, localize o contêiner onde ele será inserido, clique novamente no ícone de círculo, escolha a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010338343575)

## Galeria de Imagens

Certifique-se de que a variável **%Link:CartRecovery%** esteja aplicada nas imagens. Para isso, clique na imagem e selecione **Link para o Carrinho** na seção **Link**.

![Imagem 8: Certifique-se de que a variável %Link:CartRecovery% esteja aplicada nas imagens. Para isso, clique na imagem e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010356799639)

**Dica:**

Você pode adicionar um módulo em seu template. Como exemplo, no GIF, criamos um módulo de rodapé com as formas de pagamento e adicionamos a variável **%Link:CartRecovery%**, que permite que a pessoa clique e vá diretamente para o carrinho.

Para isso, clique em **Módulos,** selecione o modelo de sua escolha, arraste-o para o rodapé e escolha **Link para o Carrinho** na seção **Link** para garantir que a variável esteja devidamente configurada.

![Imagem 9: Para isso, clique em Módulos, selecione o modelo de sua escolha, arraste-o para o rodapé e escolha Link para o Carrinho…](https://ajuda.sankhya.com.br/hc/article_attachments/44010347612311)

## Observação Importante

No container de produtos do carrinho do cliente, os itens são dinâmicos, sendo puxados automaticamente do carrinho. No entanto, o botão vinculado aos produtos não redireciona os clientes para o carrinho, pois não é possível incluir a variável do carrinho nesse botão.

**Recomendação**: Para maximizar a eficácia do e-mail, torne-o chamativo antes de chegar à seção dos produtos. Alterar o rótulo do botão de "Comprar" para "Ver Detalhes" pode ser uma boa alternativa para incentivar a interação do cliente.

![Imagem 10: Recomendação : Para maximizar a eficácia do e-mail, torne-o chamativo antes de chegar à seção dos produtos. Alterar o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010326939031)

Após configurar o conteúdo do e-mail, clique em **Salvar Alterações** e depois em **Continuar**.

![Imagem 11: Após configurar o conteúdo do e-mail, clique em Salvar Alterações e depois em Continuar .](https://ajuda.sankhya.com.br/hc/article_attachments/44010327230359)

## Revisão

Antes de ativar a automação, envie um e-mail teste para verificar os links e o design da jornada criada.

Se desejar editar a jornada mais tarde, clique em **Salvar Rascunho**.
Para que a automação fique ativa imediatamente, clique em **Ativar Jornada**.

![Imagem 12: Se desejar editar a jornada mais tarde, clique em Salvar Rascunho . Para que a automação fique ativa imediatamente,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010374203415)

## Regra de reenvio

A Flowbiz permite selecionar se o usuário deseja enviar e-mail de recuperação de carrinho **sempre que o cliente dele retornar ao site** ou **apenas quando** **o carrinho tiver alguma alteração** (adicionou/removeu produto, preço mudou, quantidade mudou).

Para o usuário conseguir definir a regra, ele precisa:

- Ter a permissão de usuário do item "**Recuperador de Carrinho - Regra de envio**".
- Selecionar a regra desejada, que será exibida em Configurações.

**Importante:** Por padrão, a regra que estará ativada é "**Sempre que o cliente retornar ao site**".

## Considerações Finais

Ao seguir estes passos, você criará sua automação de carrinho abandonado com o **Jornadas da Flowbiz**, que vai impulsionar suas vendas e melhorar a experiência de seus clientes.

Se ficar com dúvidas, nossa equipe de Suporte está pronta para ajudar você pelo Chat. Entre em contato!
