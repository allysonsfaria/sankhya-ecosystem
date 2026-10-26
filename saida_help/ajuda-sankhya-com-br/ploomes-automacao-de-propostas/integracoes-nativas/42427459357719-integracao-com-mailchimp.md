---
id: "42427459357719"
titulo: "Integração com MailChimp"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427459357719-Integra%C3%A7%C3%A3o-com-MailChimp"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:41Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452446", "sync_hash_74f05f2c2477"]
---

# Integração com MailChimp

Este artigo detalha o funcionamento da integração entre o Ploomes e o Mailchimp. Você aprenderá como realizar a autenticação da integração e quais requisitos necessários para enviar suas lista de contatos do Ploomes para o Mailchimp, a fim de utilizá-las em campanhas de e-mail marketing.

## 1) Sobre o Mailchimp

O **Mailchimp** é uma plataforma de automação de marketing e serviço de e-mail marketing. Ela permite que empresas criem, enviem e analisem campanhas de e-mail e anúncios, além de gerenciar listas de contatos e segmentar audiências para fortalecer o relacionamento com os clientes.

## 2) Objetivos da Integração

A integração entre Ploomes e Mailchimp permite enviar os contatos (Pessoas) de uma aba selecionada para uma l**ista exclusiva** no Mailchimp criada automaticamente pelo Ploomes dentro da sua conta MailChimp. Facilitando campanhas de e-mail marketing segmentadas.

## 3) Pré-requisitos para o funcionamento da integração

Para que o envio de contatos ocorra com sucesso, os registros devem cumprir as seguintes condições:

- O cliente deve ser obrigatoriamente do tipo **Pessoa**.
- O campo **E-mail** do cliente deve estar devidamente preenchido com apenas um único endereço de e-mail. Caso haja mais de um e-mail informado no cadastro, a integração desse contato não será realizada.
- A opção **Recebe E-mail Marketing** deve estar marcada como **Sim**.
- O usuário do **Mailchimp** precisa estar inserido na aba ou a aba ter visualização para todos. Para mais detalhes, verifique o tópico [6.1](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427459357719-Integra%C3%A7%C3%A3o-com-MailChimp#h_c93292d2d1)

## 4) Como ativar a integração

1. Acesse **Administração > Integrações Plug and Play > Mailchimp**.

   ![Imagem 1: Acesse Administração > Integrações Plug and Play > Mailchimp .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1855146293/045645058764b0c6bcf0ed7bd618/mceclip0.png?expires=1786536000&signature=27abebf777689ce8e540667e3e7d0b0e5f6fd4d73657318d8c2976c5c8dca5e7&req=dSgiE8h6m4NWWvMW3nq%2BgSwhO1qhjcersI6vLAYHHmYgvoprIm%2FdTbBqGgsL%0AtxLZj0J7Xss6rVVZjJvYA0tNnhI%3D%0A)
2. Clique em **Habilitar integração.**

   ![Imagem 2: Clique em Habilitar integração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1855174237/40434e912e9fd4459477e4487714/image.png?expires=1786536000&signature=eda83832bd62b5e96d6960f1be1c6513864210cb25f59b9634f69a8646eb8c0a&req=dSgiE8h5mYNcXvMW3nq%2BgRb1tDGeMFuj9v98a9Xrxpj0E7XFpJNNVixFMk%2F%2F%0Atdd2bDtK0K5SmiWiIIdI1qlLR%2B4%3D%0A)
3. Clique em **Autorizar integração** e faça login na sua conta MailChimp.

   ![Imagem 3: Clique em Autorizar integração e faça login na sua conta MailChimp.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1855174496/6e138b029a7172267c035d992bab/image.png?expires=1786536000&signature=5345da3f37b4ccd05dfcb48522849e602033953d2b5e86981a5da9f06752a284&req=dSgiE8h5mYVWX%2FMW3nq%2BgUXQ7re%2F5027jQCyZUz2vxG6O7s0jR7k45F5bGYt%0AXslbDDfd5BAhLSK5Szk0ODPT3Gw%3D%0A)
4. Após concluir o login, clique em **Ativar integração** para finalizar.

   ![Imagem 4: Após concluir o login, clique em Ativar integração para finalizar.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1855175615/a879f89670d118759a38f90b3e39/image.png?expires=1786536000&signature=a90874d84d9429147de255163e68c0ef572012524b35b858d35a4017628fc40e&req=dSgiE8h5mIdeXPMW3nq%2BgepVNB2BrAwMjSRoKZaXkzoF7dTizE5%2FyiQRGE3L%0ABvYGA8l73bxvlDQKPYwL12TDRNc%3D%0A)

## 6) Como integrar uma aba com o MailChimp

## 6.1) Criar a aba com os filtros necessários

- Acesse o módulo **Clientes**.
- Clique em **Nova aba**.
- Adicione as seguintes condições:

  - **Tipo de Cliente > igual a > Pessoa**
  - **E-mail > diferente de > vazio**
  - **Recebe E-mail Marketing > igual a > "Sim"**

[GIF animado: Imagem 5: Recebe E-mail Marketing > igual a > "Sim"](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2105149045/222bccf81cc59725a1dc978b2300/testes5.gif?expires=1786536000&signature=903f39a6059fad908d843940d5c7feb57e074debb8d288da7f47700f02a0b860&req=diEnE8h6lIFbXPMW3nq%2BgaWnkPNw2je1Q5McZdWskxlrlkH%2Fn4fdnvyfUrOZ%0AgymnL2jQeNSnJyIXgTdpvvHrrkc%3D%0A)

- Caso a aba esteja configurada com acesso restrito a usuários específicos, acesse a opção **“Quem pode ver essa aba”**, pesquise por **Mailchimp** e adicione o usuário.

  Se não houver necessidade de restrição, mantenha a configuração de visualização definida como **“Todos da empresa”**, garantindo que o acesso permaneça liberado para todos os usuários incluindo o usuário do **Mailchimp**.

![Imagem 6: Se não houver necessidade de restrição, mantenha a configuração de visualização definida como “Todos da empresa” ,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2105167673/994cb086d0b7b940e245e6d02d9e/image.png?expires=1786536000&signature=0c534f1b41cafb5a17d99b34787e45fa59c748ab9b6be6b9c1697ca4c1f3ad61&req=diEnE8h4modYWvMW3nq%2BgVB5Fu4k2%2FilAMC%2BD19hwU2p4rum7kWlZIQwkQNX%0AhkDmQJtJltkN1LScvkQK2R2aXcA%3D%0A)

- Após isso, clique em **Salvar**.

⚠️ **Atenção:** esses filtros garantem que a aba contenha apenas contatos elegíveis para envio ao Mailchimp.

Veja mais em: [Abas e filtros em Clientes](https://sankhya.zendesk.com/hc/pt-br/articles/42427671827479)

## 6.2) Enviar ao Mailchimp

1. Selecione a aba criada.
2. Passe o mouse sobre o nome da aba.
3. Clique em **⚙️ Ações da aba**.

   ![Imagem 7: Clique em ⚙️ Ações da aba .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1855182640/90ec720927c9498046a08c353476/image.png?expires=1786536000&signature=df443b852796616f1be393699065af5eba3a1bdadf6393d2b8cc313914d09db6&req=dSgiE8h2n4dbWfMW3nq%2BgWAUraEQNjqSuFmBLVt5nvMFpQtIT0ZVGd5nDRyD%0AknOgYkZy8IEYkN%2BQLIEnGAdER3E%3D%0A)
4. Selecione **Integrar ao MailChimp**.

   ![Imagem 8: Selecione Integrar ao MailChimp .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1855183531/16c57c35d1dffee52eaa779d575e/image.png?expires=1786536000&signature=84484c1d6b6dd7e237b5ff13018b7386520cd3e1f3ea53da80b5313ce7d5e928&req=dSgiE8h2noRcWPMW3nq%2BgcXPb%2F13PG6mghbA8iXY8kmTrNKYvRnRqdIutTzp%0Ab081H0XYX%2FiQ6gQqW%2BoD%2F5IiYLU%3D%0A)

Após o envio, o sistema exibirá uma **mensagem de sucesso no canto inferior direito** da tela.

## 7) Observações importantes

O plano gratuito do Mailchimp permite apenas **1 lista**, que já é criada automaticamente quando a conta é criada.

Como o Ploomes sempre cria uma nova lista para enviar os contatos, isso entra em conflito com a limitação do plano gratuito.

Se você utiliza o plano Free, existem duas opções:

**1. Excluir a lista padrão:**

Solicitar ao suporte do Mailchimp a exclusão da lista criada automaticamente.
Assim, o Ploomes poderá criar a nova lista necessária para a integração.

**2. Atualizar o plano:**

Assinar o plano **Essentials** (ou superior), que permite a criação de mais de uma lista.

⚠️ **Atenção:** Sem realizar uma dessas ações, a integração **não conseguirá enviar contatos**.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 9: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1445044930/b7dc2a99721560a0a3cfbe0c0937/Intercom+e+Active+%28com+CTA%29.png?expires=1786536000&signature=2708b3bf2c454a339e2f06640388c4491ec42e2c503bcdc86a2a539ffa97c568&req=dSQjE8l6mYhcWfMW3nq%2BgS40E3u9imi8C60NGn7CHtyyIKEgTMQWKciKCHFG%0AfPf9rjJshb0P0lNJkxHLFpd1AfQ%3D%0A)](https://universidade.ploomes.com/courses/integracao-mailchimp-2)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
