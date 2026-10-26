---
id: "44010953221655"
titulo: "Como integrar a Bonifiq com a Flowbiz (atualização de pontos)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010953221655-Como-integrar-a-Bonifiq-com-a-Flowbiz-atualiza%C3%A7%C3%A3o-de-pontos"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:51:33Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_149", "sync_hash_25926f9ca7e2"]
---

# Como integrar a Bonifiq com a Flowbiz (atualização de pontos)

A Bonifiq oferece integração com a Flowbiz para atualizar automaticamente o saldo de pontos dos seus clientes. Isso permite personalizar campanhas informando o saldo atual de cada contato, sem precisar atualizar manualmente.

**Neste tutorial, você vai aprender como:**

- Criar um campo personalizado para armazenar os pontos
- Gerar a chave de API
- Montar a URL de integração
- Configurar o webhook dentro da Bonifiq

⚠️ **Importante**: Essa integração **não dispara e-mails** automaticamente. Ela apenas atualiza os dados no CRM da Flowbiz.

## 1. Crie o campo personalizado "Pontos" na sua lista

Acesse uma lista na Flowbiz, vá até o menu lateral e clique em **Campos Personalizados**. Em seguida, clique no botão “**Criar novo campo personalizado**”.

Preencha os dados conforme a imagem e salve.

Esse campo será usado para armazenar os pontos atualizados de cada contato.

![Imagem 1: Esse campo será usado para armazenar os pontos atualizados de cada contato.](https://ajuda.sankhya.com.br/hc/article_attachments/44010939235223)

Após salvar, identifique o **Field ID** do campo criado. Ele será usado na URL do webhook.

![Imagem 2: Após salvar, identifique o Field ID do campo criado. Ele será usado na URL do webhook.](https://ajuda.sankhya.com.br/hc/article_attachments/44010964777623)

## 2. Copie o ID da lista

Esse ID também será necessário para montar a URL de integração. Você encontra o ID da lista no topo da tela, ao lado do nome da lista.

![Imagem 3: Esse ID também será necessário para montar a URL de integração. Você encontra o ID da lista no topo da tela, ao lado do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010965028247)

## 3. Gere a chave de API na Flowbiz

Clique no seu nome no canto superior direito e acesse a opção **Chaves da API**.

Clique em “Criar nova chave”, dê um nome de identificação e salve.

![Imagem 4: Clique em “Criar nova chave”, dê um nome de identificação e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/44010969086743)

![Imagem 5: Clique em “Criar nova chave”, dê um nome de identificação e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/44010969270167)

Copie e guarde essa chave com segurança, pois ela será usada na URL.

## 4. Monte a URL de integração

Utilize o modelo abaixo e substitua os valores destacados:

[https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**SUACHAVEDEAPI**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**SEU_ID_DE_LISTA**&EmailAddress=%7B%7BCustomer.Email%7D)[SUACHAVEDEAPI](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**SUACHAVEDEAPI**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**SEU_ID_DE_LISTA**&EmailAddress=%7B%7BCustomer.Email%7D)[&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**SUACHAVEDEAPI**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**SEU_ID_DE_LISTA**&EmailAddress=%7B%7BCustomer.Email%7D)[SEU\_ID\_DE\_LISTA](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**SUACHAVEDEAPI**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**SEU_ID_DE_LISTA**&EmailAddress=%7B%7BCustomer.Email%7D)[&EmailAddress={{Customer.Email}](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**SUACHAVEDEAPI**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**SEU_ID_DE_LISTA**&EmailAddress=%7B%7BCustomer.Email%7D)}&CustomField**SEU\_ID\_DE\_CAMPO\_PERSONALIZADO**={{EarnedPoints}}&IPAddress=123456789&UpdateIfExists=true

**Exemplo com os valores preenchidos:**

[https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**abc123xyz**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**19719**&EmailAddress=%7B%7BCustomer.Email%7D)[abc123xyz](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**abc123xyz**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**19719**&EmailAddress=%7B%7BCustomer.Email%7D)[&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**abc123xyz**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**19719**&EmailAddress=%7B%7BCustomer.Email%7D)[19719](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**abc123xyz**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**19719**&EmailAddress=%7B%7BCustomer.Email%7D)[&EmailAddress={{Customer.Email}](https://mbiz.mailclick.me/api.php/Subscriber.Subscribe?APIKey=**abc123xyz**&Command=Subscriber.Subscribe&ResponseFormat=JSON&ListID=**19719**&EmailAddress=%7B%7BCustomer.Email%7D)}&CustomField34659={{EarnedPoints}}&IPAddress=**34661**&UpdateIfExists=true

## 5. Cadastre o Webhook na Bonifiq

Agora que a URL está pronta, acesse o painel da Bonifiq e vá até o menu **API** → **+ Credencial de API** → escolha “Webhook”.

Preencha os campos da seguinte forma:

- **Ativado**: marque esta opção no topo da tela
- **Nome**: Flowbiz
- **URL**: cole a URL que você gerou
- **Tópicos**: selecione “Ponto Adicionado”

**E-mail técnico**: preencha com um e-mail válido para alertas

![Imagem 6: E-mail técnico : preencha com um e-mail válido para alertas](https://ajuda.sankhya.com.br/hc/article_attachments/44010940140311)

## Teste a integração

Você pode testar manualmente a atribuição de pontos na Bonifiq e conferir se o saldo foi atualizado no campo da Flowbiz. O dado será refletido automaticamente no perfil do contato e pode ser usado em campanhas, segmentações e mensagens.

Se tiver dúvidas, fale com o nosso time de suporte.
