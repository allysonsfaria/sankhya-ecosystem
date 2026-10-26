---
id: "44011160669335"
titulo: "Como criar uma jornada de carrinho abandonado com o WhatsApp API no Jornadas PRO"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011160669335-Como-criar-uma-jornada-de-carrinho-abandonado-com-o-WhatsApp-API-no-Jornadas-PRO"
trilha: "Flowbiz > Jornadas"
atualizado_em: "2026-10-05T18:57:18Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_155", "sync_hash_cf9181da4975"]
---

# Como criar uma jornada de carrinho abandonado com o WhatsApp API no Jornadas PRO

O Módulo Jornadas PRO utiliza o WhatsApp API Oficial da ©Meta para automatizar a recuperação de vendas de forma prática e eficiente pelo WhatsApp. Com mensagens personalizadas no tom da sua marca, ele engaja clientes no canal mais utilizado pelos brasileiros, aumentando conversões e otimizando resultados!

## Nota importante:

Embora a loja não possa responder diretamente às mensagens enviadas, é possível configurar uma resposta automática genérica com informações de contato. Isso permite que os clientes entrem em contato caso tenham dúvidas, contribuindo para uma melhor experiência e maior taxa de conversão.

Para isso, basta acessar o menu da conta, navegar até **Integrações** > **WhatsApp** e marcar a opção **Ativar resposta automática**.

![Imagem 1: Para isso, basta acessar o menu da conta, navegar até Integrações > WhatsApp e marcar a opção Ativar resposta…](https://ajuda.sankhya.com.br/hc/article_attachments/44011176919831)

**Observação:** O custo por conversa aberta pela Meta é de USD 0,06 (seis centavos de Dólar), aproximadamente R$0,36.

## Criando Templates para WhatsApp API

O primeiro passo para criar sua jornada é configurar os templates de mensagem no WhatsApp API. Acesse o menu da sua conta e vá até **Templates** > **WhatsApp API (Automação)**.

![Imagem 2: O primeiro passo para criar sua jornada é configurar os templates de mensagem no WhatsApp API. Acesse o menu da sua…](https://ajuda.sankhya.com.br/hc/article_attachments/44011135656727)

Clique em **Criar Template** e selecione a opção **Template de WhatsApp API (Automação).**

![Imagem 3: Clique em Criar Template e selecione a opção Template de WhatsApp API (Automação).](https://ajuda.sankhya.com.br/hc/article_attachments/44011099631767)

Dê um nome ao template. O prefixo padrão "mb\_" já está incluído e não pode ser alterado. Após esse prefixo, você pode criar o nome que desejar, como por exemplo: "mb\_carrinho\_abandonado\_01".

![Imagem 4: Dê um nome ao template. O prefixo padrão " mb_ " já está incluído e não pode ser alterado. Após esse prefixo, você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/44011146195351)

O cabeçalho é opcional, exibido em negrito (até 45 caracteres), mas não aceita emojis.

![Imagem 5: O cabeçalho é opcional, exibido em negrito (até 45 caracteres), mas não aceita emojis.](https://ajuda.sankhya.com.br/hc/article_attachments/44011129114007)

**Dica:** Caso queira usar emojis na saudação, você pode inserir no corpo da mensagem, clicando no ícone da **Carinha**. Também é possível formatá-la em negrito, selecionando a frase e clicando no ícone da letra **B**.

![Imagem 6: Dica: Caso queira usar emojis na saudação, você pode inserir no corpo da mensagem , clicando no ícone da Carinha .…](https://ajuda.sankhya.com.br/hc/article_attachments/44011146817687)

## Mensagem

Insira o conteúdo da mensagem no campo **Corpo da Mensagem**.

![Imagem 7: Insira o conteúdo da mensagem no campo Corpo da Mensagem .](https://ajuda.sankhya.com.br/hc/article_attachments/44011137551255)

**Dica:** você pode adicionar variáveis dinâmicas para personalizar sua mensagem, na opção **Adicionar conteúdo dinâmico**.

## Por exemplo:

1. Coloque o cursor do mouse ao lado direito da primeira saudação e selecione a variável **{{1}}** > **CLIENTE** > **Nome do Cliente** para incluir o primeiro nome do cliente na mensagem de forma automática.
2. Na variável **{{2}}** > **PERSONALIZADO** > **Texto Livre**, recomendamos incluir um Cupom de Desconto para incentivar a conversão.
3. Utilize a variável **{{3}}** > **PERSONALIZADO** > **Texto Livre** para especificar a porcentagem de desconto oferecida, se aplicável.

Em seguida, marque a opção **Visualizar a mensagem com o conteúdo dinâmico**, para ver como ficou.

![Imagem 8: Em seguida, marque a opção Visualizar a mensagem com o conteúdo dinâmico , para ver como ficou.](https://ajuda.sankhya.com.br/hc/article_attachments/44011163196311)

## Importante:

O rodapé do template já inclui, por padrão, a mensagem: "Para não receber mais nossas mensagens, responda 'PARAR'." Essa configuração é fixa e não pode ser alterada, pois garante conformidade com as boas práticas de comunicação e as políticas de uso do WhatsApp API, preservando a reputação e a funcionalidade do seu número.

![Imagem 9: O rodapé do template já inclui, por padrão, a mensagem: "Para não receber mais nossas mensagens, responda 'PARAR'."…](https://ajuda.sankhya.com.br/hc/article_attachments/44011164509591)

## Botão de Ação

Após editar seu template, você pode configurar o botão de ação (opcional), por exemplo: “Finalizar Agora”, “Garanta agora”, etc.

**Observação:** Ao lado do botão de ação, o link para o carrinho já vem configurado por padrão, garantindo praticidade e alinhamento com a finalidade da jornada.

![Imagem 10: Observação: Ao lado do botão de ação, o link para o carrinho já vem configurado por padrão, garantindo praticidade e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011139786263)

Após preencher o template, visualize a mensagem para conferir se está correta. Em seguida, clique em **Enviar template para aprovação**.

![Imagem 11: Após preencher o template, visualize a mensagem para conferir se está correta. Em seguida, clique em Enviar template…](https://ajuda.sankhya.com.br/hc/article_attachments/44011152965783)

## Aprovação do Template:

Após enviar o template de WhatsApp, ele será enviado para análise pela Meta. Esse processo é obrigatório e pode levar **até 24 horas** para ser concluído, embora geralmente seja finalizado em apenas alguns minutos.

Você pode acompanhar o status diretamente na lista dos templates de WhatsApp. Assim que aprovado, o status será alterado para “Ativo”.

![Imagem 12: Você pode acompanhar o status diretamente na lista dos templates de WhatsApp. Assim que aprovado, o status será…](https://ajuda.sankhya.com.br/hc/article_attachments/44011153195415)

**Por exemplo:** EM ANÁLISE.

![Imagem 13: Por exemplo: EM ANÁLISE.](https://ajuda.sankhya.com.br/hc/article_attachments/44011153398807)

Após atualizar a página: ATIVO.

![Imagem 14: Após atualizar a página: ATIVO.](https://ajuda.sankhya.com.br/hc/article_attachments/44011132231703)

## Criando a Jornada

Acesse o menu **Jornadas**, vá em **Minhas Jornadas** e clique em **Criar Jornada**.

Em seguida, escolha a opção **Carrinho Abandonado WhatsApp API (Automação)**.

![Imagem 15: Em seguida, escolha a opção Carrinho Abandonado WhatsApp API (Automação) .](https://ajuda.sankhya.com.br/hc/article_attachments/44011153825943)

## Nome da Jornada

Insira o nome da sua jornada. Para facilitar, você pode clicar em **Utilizar Sugestão** e alterar o tempo de envio conforme desejado. Em seguida, clique em **Continuar**.

![Imagem 16: Insira o nome da sua jornada. Para facilitar, você pode clicar em Utilizar Sugestão e alterar o tempo de envio conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/44011132691223)

## Atenção!

Ao criar um novo template, os dados da jornada atual serão descartados. O novo template passará por aprovação da Meta, o que pode levar **até 24 horas**. Após aprovado, selecione-o para continuar a configuração.

![Imagem 17: Ao criar um novo template, os dados da jornada atual serão descartados. O novo template passará por aprovação da Meta,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011132898071)

Selecione o template aprovado pela Meta e clique em **Selecionar**.

![Imagem 18: Selecione o template aprovado pela Meta e clique em Selecionar .](https://ajuda.sankhya.com.br/hc/article_attachments/44011167828631)

O conteúdo dinâmico será exibido, permitindo que você revise as informações das variáveis e do template como um todo. Em seguida, clique em **Salvar edição** e depois em **Continuar**.

![Imagem 19: O conteúdo dinâmico será exibido, permitindo que você revise as informações das variáveis e do template como um todo.…](https://ajuda.sankhya.com.br/hc/article_attachments/44011142199063)

É possível enviar uma mensagem de teste para o número de celular desejado antes de ativar a jornada. Embora esse passo seja opcional, recomendamos que você faça o teste para garantir que tudo esteja correto. O custo por teste é de USD 0,06 (seis centavos de dólar), aproximadamente R$0,36. Após verificar, clique em **Ativar Jornada**.

![Imagem 20: É possível enviar uma mensagem de teste para o número de celular desejado antes de ativar a jornada. Embora esse passo…](https://ajuda.sankhya.com.br/hc/article_attachments/44011168497431)

Se a jornada não tiver segmentação, basta fechar a tela de "Reordenar Prioridade de Envio" para ativá-la imediatamente. Após isso, ela aparecerá como ativada. Ao clicar em Editar, você poderá realizar as seguintes ações: editar, reordenar a prioridade, visualizar, desativar ou remover.

![Imagem 21: Se a jornada não tiver segmentação, basta fechar a tela de "Reordenar Prioridade de Envio" para ativá-la imediatamente.…](https://ajuda.sankhya.com.br/hc/article_attachments/44011201163159)

## Importante!

Sempre que editar e enviar um template para análise, as jornadas vinculadas serão desativadas até a aprovação.

## Veja no GIF o caminho simplificado:

Menu da conta > Templates > WhatsApp API (Automação) > Editar e enviar template > Status: EM ANÁLISE > Jornadas > Minhas Jornadas > Status: DESATIVADA

Após a aprovação, reative a jornada normalmente.

![Imagem 22: Após a aprovação, reative a jornada normalmente.](https://ajuda.sankhya.com.br/hc/article_attachments/44011201638935)

Agora você sabe como criar uma jornada de carrinho abandonado com o WhatsApp API no Jornadas PRO!

Se ficar com dúvidas, nossa equipe de Suporte está pronta para ajudar você pelo Chat. Entre em contato!
