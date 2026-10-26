---
id: "44011110844823"
titulo: "Como enviar leads para a Meetime usando o Zapier"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011110844823-Como-enviar-leads-para-a-Meetime-usando-o-Zapier"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:55:20Z"
rotulos: ["sync_hc", "meetime", "meetime_359", "sync_hash_572c32898e77"]
---

# Como enviar leads para a Meetime usando o Zapier

Antes de tudo, será necessário que você possua uma conta no Zapier.

## Passo a passo:

1. Já no sistema, você deverá clicar para criar um “Zap”, nome dado para as integrações construídas por lá.
2. Clique em cima de Trigger e escolha a plataforma de onde os leads vão sair e pesquisar em "Search apps". Nesse exemplo, vamos utilizar o RD Station.

![Imagem 1: Clique em cima de Trigger e escolha a plataforma de onde os leads vão sair e pesquisar em "Search apps". Nesse exemplo,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011111172503)

1. Em "Trigger event" escolha qual será o gatilho que deve ocorrer para que o lead seja enviado para a Meetime. Em "Account", faça login na plataforma escolhida.

![Imagem 2: Em "Trigger event" escolha qual será o gatilho que deve ocorrer para que o lead seja enviado para a Meetime. Em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011088604567)

1. Clique em "Action" e procure por "Meetime" em "Search apps".

![Imagem 3: Clique em "Action" e procure por "Meetime" em "Search apps".](https://ajuda.sankhya.com.br/hc/article_attachments/44011089090967)

1. Em "Action event" escolha a opção "Start a New Prospection".

![Imagem 4: Em "Action event" escolha a opção "Start a New Prospection".](https://ajuda.sankhya.com.br/hc/article_attachments/44011072712471)

1. Em "Account" você irá copiar a sua chave de API da Meetime. Para encontrá-la, entre na Meetime usando um perfil de Administrador, clique no seu nome no canto superior direito da tela > Integrações >API > Copiar

![Imagem 5: Em "Account" você irá copiar a sua chave de API da Meetime. Para encontrá-la, entre na Meetime usando um perfil de…](https://ajuda.sankhya.com.br/hc/article_attachments/44011094364951)

1. Cole a chave na página aberta no Zapier e clique em Continuar.

![Imagem 6: Cole a chave na página aberta no Zapier e clique em Continuar.](https://ajuda.sankhya.com.br/hc/article_attachments/44011105700503)

1. Na seção "Configure", vamos configurar o que irá acontecer com o lead quando ele entrar na Meetime.

![Imagem 7: Na seção "Configure", vamos configurar o que irá acontecer com o lead quando ele entrar na Meetime.](https://ajuda.sankhya.com.br/hc/article_attachments/44011105908375)

Cadência: Em qual cadência configurada na Meetime o lead será inserido

Ignorar o erro se o lead já possuir uma prospecção ativa: Recomendamos que esse campo fique como “True”. Caso contrário, se o lead sendo disparado já existir na Meetime e ainda não estiver finalizado, não conseguirá ser criado no nosso sistema e o Zapier continuará tentando criá-lo (dando retry). Isso pode fazer com que em uma das tentativas, dias depois, o Zapier consiga criá-lo na Meetime.

1. Ainda na etapa “Action”, os campos dos leads na Meetime (como E-mail, Nome Completo, Empresa) poderão ser preenchidos com o que vier do sistema que disparará os leads (nesse exemplo, RD Station) - o Zapier permite fazer essa associação. Para isso, é só clicar no ícone de + logo abaixo do nome dos campos.

![Imagem 8: Ainda na etapa “Action”, os campos dos leads na Meetime (como E-mail, Nome Completo, Empresa) poderão ser preenchidos…](https://ajuda.sankhya.com.br/hc/article_attachments/44011073567895)

1. Por fim, na última etapa, chamada “Test”, você poderá testar a integração e confirmar a criação do lead na Meetime.

![Imagem 9: Por fim, na última etapa, chamada “Test”, você poderá testar a integração e confirmar a criação do lead na Meetime.](https://ajuda.sankhya.com.br/hc/article_attachments/44011121508119)

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).C
