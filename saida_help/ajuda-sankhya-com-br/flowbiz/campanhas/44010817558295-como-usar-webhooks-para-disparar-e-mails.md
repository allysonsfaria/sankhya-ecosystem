---
id: "44010817558295"
titulo: "Como Usar Webhooks para Disparar E-mails Automáticos na Flowbiz."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010817558295-Como-Usar-Webhooks-para-Disparar-E-mails-Autom%C3%A1ticos-na-Flowbiz"
trilha: "Flowbiz > Campanhas"
atualizado_em: "2026-10-05T18:47:27Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_145", "sync_hash_c7b2617dc93f"]
---

# Como Usar Webhooks para Disparar E-mails Automáticos na Flowbiz.

**Webhooks são ferramentas poderosas que permitem automatizar o envio de e-mails com base em eventos externos.** Vamos te guiar, passo a passo, de forma clara e simples, para configurar essa automação na plataforma Flowbiz.

Antes de ativar seu primeiro envio automático por Webhook, é importante garantir que você já tenha:

- ## Uma conta Flowbiz ativa.
- ## Criado uma Lista de contatos onde os e-mails serão armazenados.
- ## Acesso à sua chave de API (API Key).
- ## Gerar chave API na Flowbiz:

Com o mouse por cima do nome da conta:

Selecione **“Criar chave da API”**

![Imagem 1: Selecione “Criar chave da API”](https://ajuda.sankhya.com.br/hc/article_attachments/44010817773207)

Coloque um nome, ou descrição para a função da chave e salve a chave da API:

![Imagem 2: Coloque um nome, ou descrição para a função da chave e salve a chave da API:](https://ajuda.sankhya.com.br/hc/article_attachments/44010818044823)

Ela irá ser listada com as demais chaves da conta, podendo ser copiada e utilizada na função que desejar.

## Criando um Envio Automático com Gatilho Webhook

**1.** Acesse o painel da Flowbiz normalmente com seu login. Vá em **Listas > Clique sobre o nome da sua lista > Envios Automáticos > Criar Envio Automático.**

Preencha o **nome da sua automação**. Em **Gatilho Principal**, selecione: **Chamada de Webhook** (como mostrado na imagem abaixo):

![Imagem 3: Preencha o nome da sua automação . Em Gatilho Principal , selecione: Chamada de Webhook (como mostrado na imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/44010805936279)

Se quiser, você pode selecionar "**Condições adicionais"** para filtrar ainda mais quem receberá o e-mail no caso dos **Segmentos**.

No final da página, você montará o conteúdo do e-mail que será enviado **assim que o Webhook for chamado**. **Salve sua automação.**

## 3. Como Saber o ID da Sua Automação

Depois de salvar, observe a URL no seu navegador. O número ao final da URL (por exemplo, 17025 na imagem) é o ID da Automação. Você vai usá-lo na chamada da API para disparar o e-mail.

## 4. Disparando a Automação via Webhook

Com sua automação criada, você poderá dispará-la usando uma chamada de API como esta:

**curl --location --request POST \ '**<https://news.mailclick.me/api.php/AutoResponder.Webhook?ResponseFormat=JSON&AutoresponderID=XXXXX&EmailAddress=email%40gmail.com&Command=AutoResponder.Webhook&APIKey=sua-api-key>**'**

Substitua os valores:

**XXXXX** → pelo ID da automação.

**email%**[40gmail.com](http://40gmail.com) → pelo e-mail que deverá receber o envio.

**sua-api-key** → pela sua chave de API pessoal.

1. Cadastrando um Contato Antes do Disparo (opcional)

Caso o e-mail ainda não esteja na sua lista, cadastre-o assim:

**curl --location --request POST \ '**<https://news.mailclick.me/api.php/Subscriber.Subscribe?Command=Subscriber.Subscribe&APIKey=sua-api-key&ResponseFormat=JSON&ListID=XXXXX&EmailAddress=email%40gmail.com&IPAddress=10.1.1.1&CustomFieldYYYYY=ValorTesteParaNome&Updateifexists=true>**'**

📌 Lembre-se de substituir:

**ListID=XXXXX** → pelo ID da sua lista.

**EmailAddress=** → pelo e-mail do contato.

**CustomFieldYYYYY=ValorTesteParaNome** → pelo campo personalizado e valor (caso use).

**Updateifexists=true** → garante que ele será atualizado se já existir.

1. Qual Endpoint Usar?

Certifique-se de usar o endpoint correto da sua conta Flowbiz. Verifique com seu time de suporte qual está ativo:

<https://mbiz.mailclick.me/api.php>

<https://news.mailclick.me/api.php>

📘 **Documentação Oficial**

Você também pode conferir a documentação técnica do Webhook da Flowbiz [aqui](https://flowbiz.readme.io/docs/introducao).

Em caso de dúvidas, não hesite em nos acionar no chat da ferramenta!
