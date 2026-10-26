---
id: "42427622317463"
titulo: "Como integrar o Ploomes com o Conta Azul Financeiro (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427622317463-Como-integrar-o-Ploomes-com-o-Conta-Azul-Financeiro-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:06:29Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11559203", "sync_hash_df34f763a5f6"]
---

# Como integrar o Ploomes com o Conta Azul Financeiro (via Pluga)

**Observação:**

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

## Pluga | Como integrar o Ploomes com o Conta Azul Financeiro

## O que esta integração faz?

A cada **proposta** **ganha** no Ploomes, criar automaticamente um **contas a receber** no Conta Azul Financeiro.

**OU**

A cada **card** marcado como **"ganho"** no Ploomes, criar automaticamente um **contas a receber** no Conta Azul Financeiro.

## Requisitos

- Uma conta no Ploomes;
- Uma conta no Conta Azul, com acesso ao módulo financeiro;
- Uma conta na [Pluga](https://pluga.co/).

## Criando uma integração entre Ploomes (origem) → Conta Azul Financeiro (destino)

1. Acesse a [Pluga](https://pluga.co/) e clique em “**Entrar**” ou em “**Cadastrar”** se este for o seu primeiro acesso;

   ![Imagem 1: Acesse a Pluga e clique em “ Entrar ” ou em “ Cadastrar” se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566959925/16db895b8b5b504cb2ad6f55ca06/AD_4nXczBiOp-Aiz0fZYE4O_IQkG274JPZRx_Y5ExZV9578LCyB8olOEoWPo25QeasJwsx748ls3N5aRs_8lg7_RFz8tE1fY72T0fbIFJjJ5bR5vlVI0x39NuNLGPT5DlVdx1Yj-vN78UA?expires=1786536000&signature=18b000d5672ffd5efd79e84721c7f2b7e14cab6b4fdc9a48a257a070afe1ae67&req=dSUhEMB7lIhdXPMW3nq%2BgQ%2F0bts1VSL4sXE6YqRQLO3bvd%2BjTXy53rpcEHN3%0AWO6ZoaLkBKApkA0dLOCmcQWoo3k%3D%0A)
2. Na área de usuário da Pluga, clique em “**Criar Automatização**”;

   ![Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566959935/2c13f8cfe571f5e11291a4a7c357/AD_4nXc9NRRWWLL0lL7eALmEb_ZGCPSOp1Ky0Mmd1au4wnV6k3U6lURiz34Hb9WXYr0L8GhIcebkCoGTYoW0mexxWMAzYoFLOeND1KmBFeHp_YQwDWWy5M5pMUHEIAW9leAjU85KnqdF?expires=1786536000&signature=5a849d042f997ac28fc303f8598c4181e4c3b272a24e41770d52ab853d54e773&req=dSUhEMB7lIhcXPMW3nq%2Bga4Qd3NhQeIUyYcLOGDsNmpmLRJUKr9h1Kel13s9%0AolEU0G7UhaWr6tm0gmUz9zUDWpM%3D%0A)
3. Dê um título para a sua automatização;

   ![Imagem 3: Dê um título para a sua automatização;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566961858/9ffda1028fa49ddb7605e18dab7e/AD_4nXek1Fo5liODIJLisy7_754kRWcqgKoZfelQHYI21Mw7bRCiUia0t3Bb7JQ78m-KffxDymk8QqTciAduuBreBeUPWhK3cD0LIvvk6tM2M3jGOzwOFoBPwYdm-SK4-usSmhh4ZXCWwA?expires=1786536000&signature=ca512770113be45da9fe4f61c7a6c70bd486763ced9621bb355827b69ffc2f5f&req=dSUhEMB4nIlaUfMW3nq%2BgYvZZZ6%2Br6NbiYOpt2OKb3kWZSvFH6iElwO5CaVs%0AU5UzOATekcUbSCJezq28B158LeE%3D%0A)
4. Selecione a ferramenta que dará início a automatização. Neste caso de uso, selecionaremos o Ploomes. Escolha também o gatilho, ou seja, o acontecimento na ferramenta que dará início à sua automatização. Neste caso de uso vamos selecionar “**Card ganho**”, e clique em “**Continuar**”;

   ![Imagem 4: Selecione a ferramenta que dará início a automatização. Neste caso de uso, selecionaremos o Ploomes. Escolha também o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566962056/97b6236b5d1d514d41217a57e0c5/AD_4nXddQ61kStbqfKD9pC8CPRgTDkKtkYYSiszVmmWTQc8hnCbXEAwMZP8z0S7UrGffmsESMAkVp6RSiRlJp1m4hm2-TzcITkWHCmccYtxZL5AlS7RvzZE8V7Ui3ywAlA4sn8q-nlFvhQ?expires=1786536000&signature=802b99082fb2ccec296232b3655778aeda00dcaab963dbaf587a245c57bc6e96&req=dSUhEMB4n4FaX%2FMW3nq%2BgReK%2FLiWxhBXiEuqkJCR8U8SE3jICaJJQWBC1fXu%0ALhW%2BAwL7d7BG%2FrNhyekVK1es0YM%3D%0A)
5. Conecte sua conta no Ploomes. Basta clicar em “**Conectar Nova Conta**” e realizar a autenticação. Esse processo só precisa ser realizado uma única vez. Ao criar outras automatizações com o Clicksign, sua conta já aparecerá listada entre as contas conectadas Caso seja a sua primeira vez conectando a sua conta do Ploomes, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

   ![Imagem 5: Conecte sua conta no Ploomes. Basta clicar em “ Conectar Nova Conta ” e realizar a autenticação. Esse processo só…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566962172/0b8d449380449e2f71a92e2e0bda/AD_4nXcfxdOnOxFH_xR1_V0VNh9UvaEzO04MsxyrhdZ0UnFOjxjiOkLow0Su72QKyXEeA1GO4k3gO-REs5oMyPmrkb-WZkpY__BG6Pqvbm4CZ4og_jP766lN92C1cBUE_84O9hNHtOdbAg?expires=1786536000&signature=fbffc85cc2e9de40b05bcbae246e8b6067bd68848d957908f19639f8219c9024&req=dSUhEMB4n4BYW%2FMW3nq%2BgQdhmvsnayiWbvkR8dhLOw2wEb7N2BSLGKnerUwg%0AtCMMKtnaJ5ZtdGTUJvqqsOnZwOs%3D%0A)
6. Neste passo, você pode filtrar as informações que serão utilizadas na sua automatização. Por exemplo, é possível selecionar quais funis do Ploomes devem ser considerados para iniciar a automatização, ou optar por aplicar a todos os funis;

   ![Imagem 6: Neste passo, você pode filtrar as informações que serão utilizadas na sua automatização. Por exemplo, é possível…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566962432/f0e4cd061548e3881dbaa5bc4b4e/AD_4nXf0louj8Dbx-I8wuGQoYSs9i_fqWEzbHallaZ45WwHJX8RbpW7AeQd8MipwMMWEToASXwWPal_nyjOSuWsTHz5Lfoa1UqXaEsgHpa90mDuJaSjunZR2A06JNU0CVbL70OVTExC2?expires=1786536000&signature=518e383051df1bca3200f735880bef49a9cd85de602640ab12d269cc4845f8e0&req=dSUhEMB4n4VcW%2FMW3nq%2BgddziJcZInEEN3FHaSnJZY1qaFnkZF8kZ%2BOgaquj%0AmzGkQgQp3J7flHYEE%2BJtSbdTveI%3D%0A)
7. Com a sua conta da Ploomes configurada, clique em **“Conectar Nova Ferramenta”**;

   ![Imagem 7: Com a sua conta da Ploomes configurada, clique em “Conectar Nova Ferramenta” ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566962586/49483fd1b07853e1e2f654b698a3/AD_4nXcJSS49G7-UKsQvx_YgWXZtUdyI0j_-NnstlK4Qgxyw0Sex0x_ykiwqp7MGEuF3SInGokVnkJzXHp9PEtnwu7nrlbVeSD-7ImNGlKG8pv2IzC3deJApC41QvhfFzybU6zmiauvcGA?expires=1786536000&signature=df20209fbeaf1fecd3f6521c9f657f45591e682674265761a05503d23b1f6383&req=dSUhEMB4n4RXX%2FMW3nq%2BgZfsLtY46YpJL0J9oHfYrKNu5Tduwr1L0e9A6Ak3%0ArrUGwspP2ACL4tEG0gJ88iBqcvk%3D%0A)
8. Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “**Conta Azul Financeiro**” e uma ação, ou seja, a tarefa que será executada na ferramenta de destino. Neste caso, selecione **“Criar contas a receber”** e clique em **“Continuar”**;

   ![Imagem 8: Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “ Conta Azul…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566962717/c57d2bf8e2784fe65941425aa227/AD_4nXdHUXh2hYNzx6-RqZlPZj8aVBllvFuR0Se_vhHbaF2JQW23UVPrhqafZA-LmTaO8irA982cvj-5M15JUOJQzczXw1GnXcBP0VmiquKldw4xqh_jl-Fhn0LhmXmlYqix6FqSIWwkAQ?expires=1786536000&signature=07bb2e94c5ba046b0ce35df185168813cc2fac68c000d97cac7046c74e333c3e&req=dSUhEMB4n4ZeXvMW3nq%2BgQzOCiRJ%2BWXbv1bO%2B%2FBUbVoBsENyT0yngqBvw0ML%0A%2FESn%2Fb9QvSccY6HCW%2FOAT0qnZns%3D%0A)
9. A etapa seguinte é a de autenticação. É nela que você vai conectar a sua conta do Conta Azul Financeiro. Esse processo, também, só precisa ser realizado uma única vez.

   ![Imagem 9: A etapa seguinte é a de autenticação. É nela que você vai conectar a sua conta do Conta Azul Financeiro. Esse processo,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566962848/57a9f91de6a88dc97c7c4d924fdc/AD_4nXe0hgUi-B60PYfEaL2-StDTrhR87KcQFhqEloMtNM0xIZPiAz0j2ifXEBHuKO5Ss8B2Y2l2kHu1ExTaNJ6HD2hEW0L570SSoFwROOwz288_ImGpBwKLY4wt4marI1msFOotL01VPg?expires=1786536000&signature=244d2e313b4ec696d230f9322034456035227771c6196f4125b647e3b4788392&req=dSUhEMB4n4lbUfMW3nq%2BgXzNRIGuWtXfahdhOrg%2FaaN2viUeeRBAywSUtNkc%0ARc2lhIao5Zs3DA5TUDdXvYMhjlM%3D%0A)
10. No último passo, você definirá quais informações do Ploomes preencherão cada um dos campos do Contas à Receber. Os campos **“Data de competência**”, **“Valor”**, **“Observação”**, **“Descrição”**, **“Conta”**, **“Categoria”**, **“Nome do cliente”**, **“Tipo do cliente”** e **“Tipo de papel”** são obrigatórios. Você pode inserir dados do Ploomes em cada campo usando o botão **“Inserir infos”**.

    ![Imagem 10: No último passo, você definirá quais informações do Ploomes preencherão cada um dos campos do Contas à Receber. Os…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566963319/3cfbad2d4a34f303e7016fe993a8/AD_4nXe436yeBRBPL-jbdmXWLJc_JGNkEYTLodLD2PB9P5FDFvVQ_-1bRMo81jmkMUkkLRBZDObryA620Cz9ob9fuUgboMI2iu7AY7KDrG8wolyq19WuCjxsBFjIbISe9n326_0cZ_NyMA?expires=1786536000&signature=7a844aa9155cb753ccebed7c615eb5c81609bffdb5d45d04fe242c9a0a98e8ed&req=dSUhEMB4noJeUPMW3nq%2BgSIIc4zObJh56t2qANugirropALlhT3sV%2FMSeZLg%0AAtZj4SJUnQ7%2BuSL5HTtVCevsTCs%3D%0A)
11. Após configurar essas opções, clique em **“Continuar”**.

    ![Imagem 11: Após configurar essas opções, clique em “Continuar” .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1566963468/f7f17e9d4ebeb258ed6ef8f14841/AD_4nXfySzavy0AXlZUuCgXaJ7kbbLl9p2npaD6MTQbjLQICoUqz6aSlcIRzsnfZxbGSkJq69bT8eot8keiQbO4nY21JK0RnYa0ET9ip5fv7BxFiQUZSdLX4y5qROGGy6ad2EnPdOgmjcQ?expires=1786536000&signature=bfd4556dee52b24139d7ac2b6bc4cb4ce4a2ac1ea2b3e7dcb72aae7bfc214b2b&req=dSUhEMB4noVZUfMW3nq%2BgdC0M3UDhnzJWm95m9LlLeALh0eN%2F8bm5q8yjj25%0Au4g5GaP2XHkYDU%2BG1hX8JZyt5dI%3D%0A)

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização **multi action**. Para isso, é só clicar em **“Conectar Nova Ferramenta”**.

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
