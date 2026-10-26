---
id: "42427622227735"
titulo: "Como integrar o Ploomes com o Facebook Custom Audiences (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427622227735-Como-integrar-o-Ploomes-com-o-Facebook-Custom-Audiences-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:06:28Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11680664", "sync_hash_3ea5d99f9763"]
---

# Como integrar o Ploomes com o Facebook Custom Audiences (via Pluga)

**Observação:**

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

## Pluga | Como integrar o Ploomes com o Facebook Custom Audiences

## O que esta integração faz?

A cada **proposta** **criada** no Ploomes, adicionar automaticamente o contato a uma audiência personalizada no Facebook Custom Audiences.

**OU**

Quando o **card alcançar uma determinada etapa no funil** do Ploomes, adicionar lead a uma audiência personalizada no Facebook Custom Audiences.

## Requisitos

- Uma conta no Ploomes;
- Uma conta do Facebook conectada na Pluga que tenha acesso a uma conta de anúncios;
- Uma conta na [Pluga](https://pluga.co/).

## Criando uma integração entre Ploomes (origem) → Facebook Custom Audiences (destino)

1. Acesse a [Pluga](https://pluga.co/) e clique em “**Entrar**” ou em “**Cadastrar”** se este for o seu primeiro acesso;

   ![Imagem 1: Acesse a Pluga e clique em “ Entrar ” ou em “ Cadastrar” se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595431717/c09276efec0fef6176ce8c5f3e1d/AD_4nXczBiOp-Aiz0fZYE4O_IQkG274JPZRx_Y5ExZV9578LCyB8olOEoWPo25QeasJwsx748ls3N5aRs_8lg7_RFz8tE1fY72T0fbIFJjJ5bR5vlVI0x39NuNLGPT5DlVdx1Yj-vN78UA?expires=1786536000&signature=37b8878e7210c7fc62e052a053980f63f1ed5b3ed6770475e476df3f9a226faf&req=dSUuE819nIZeXvMW3nq%2BgT4neoEOhRuvdGOhDkH9mzU8zXoxp6z73K%2B%2BpIkl%0A8LR8oE47jGg6clxSRJn5vlbqXzY%3D%0A)
2. Na área de usuário da Pluga, clique em “**Criar Automatização**”;

   ![Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595431720/fc77cd3aede6bd995cb388178bf7/AD_4nXc9NRRWWLL0lL7eALmEb_ZGCPSOp1Ky0Mmd1au4wnV6k3U6lURiz34Hb9WXYr0L8GhIcebkCoGTYoW0mexxWMAzYoFLOeND1KmBFeHp_YQwDWWy5M5pMUHEIAW9leAjU85KnqdF?expires=1786536000&signature=e684fa0688993a5bcf788e4abfadca8f1babb2f375cf0d1a8b881b903489e8d6&req=dSUuE819nIZdWfMW3nq%2BgfjPA4vH7zcSNo6JX%2Fa9uW3ezuBXgcjlEp5xp3b3%0ApekeB0ml2jIBpFlk0JZYrgQ15o4%3D%0A)
3. Dê um título para a sua automatização. Isso vai ser útil caso você queira editá-la no futuro;

   ![Imagem 3: Dê um título para a sua automatização. Isso vai ser útil caso você queira editá-la no futuro;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595437661/dc5b062cce597d8b1394a28603da/AD_4nXduFe_laBxusqmUZLlljv6Yo8mbEK6MV6UgGKKUMBpdEtrIYgnn44Jd8GABozly7z952qF3lSi1nI4bXD1khKo-b_ZYu3stwDbHTSa-RR8yBs6C4YRYkMgBEo2xfxsZmyDo1i3DXA?expires=1786536000&signature=394751e3fda4b3478a5324e2d055a67efa45cddefe0ad4fa9652ae7a1cfb2efd&req=dSUuE819modZWPMW3nq%2BgQrnQ4plpS8uOyMHdY61BsxTc0HxXwr0gOlP1yjG%0AusHT0Cq4dF2u%2BKs8WMhY6gO4Ggk%3D%0A)
4. Selecione a ferramenta que dará início a automatização. Neste caso de uso, selecionaremos o Ploomes. Escolha também o gatilho, ou seja, o acontecimento na ferramenta que dará início à sua automatização. Neste caso de uso vamos selecionar “**Card alcança etapa no funil**”, e clique em “**Continuar**”;

   ![Imagem 4: Selecione a ferramenta que dará início a automatização. Neste caso de uso, selecionaremos o Ploomes. Escolha também o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595438765/2a409b991e2441f2087e089b840b/AD_4nXdniPhEvfNlU4ASBb-DIH6pi2is0bDsC8rLiYuWGJ0EOow5K2lkILytHDpfpQnmteESyUVlIk2czKi49KbuaeRRvIny7ByTJFMZ9y2L5v4j9l_7AHjBgmNU1mbBQIaj1_J2EmhIoA?expires=1786536000&signature=12259b90436be9006113a5e54a94dce91d83ecca87b4f80ece6704d2032fb179&req=dSUuE819lYZZXPMW3nq%2BgSYiFFe8IYh4QNrWgKG7xRQjuyh0GeMOUzC1MZaa%0Aj19%2BPSLOXrPPFhcm9xdIVOw3q7s%3D%0A)
5. Conecte sua conta no Ploomes. Basta clicar em “**Conectar Nova Conta**” e realizar a autenticação. Esse processo só precisa ser realizado uma única vez. Ao criar outras automatizações com o Ploomes, sua conta já aparecerá listada entre as contas conectadas. Caso seja a sua primeira vez conectando a sua conta do Ploomes, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

   ![Imagem 5: Conecte sua conta no Ploomes. Basta clicar em “ Conectar Nova Conta ” e realizar a autenticação. Esse processo só…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595440762/9d1f4578cffe6ba10331377845b6/AD_4nXdczJfVWLWT0UmOJHcxX6z1nur7mCRtqEaGCtQMZrLu3y5G7JvQtZtl2n88zAppwLwpMzP-qCM8YBPutGengX5Qu4siA-4HS3CdGGar4DRwsEcDdwtGfYjPxHld8CbEsdUP4Hff?expires=1786536000&signature=b4452bb3aa5fb1d446060e4396221e7900d1d63678c14d7a2d7db4db9cf49258&req=dSUuE816nYZZW%2FMW3nq%2BgWPCDldd1b2xlIjOsfSpidpPfpdgXS8UqI9WZmuv%0Acxeqc9Ko2W8%2FENQTpJ5kA54lZNY%3D%0A)
6. Em seguida, escolha qual o funil e etapa que, quando alcançado, irá disparar a sua automatização;

   ![Imagem 6: Em seguida, escolha qual o funil e etapa que, quando alcançado, irá disparar a sua automatização;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595441392/5d6f2965d4ea0e3db58c6caff0d7/AD_4nXdYXmY93IFWA8_hhe9WPs4JL0onrajN-zUFjKisOo7uTHidddNWJW0F1gMjBPX2jAz133woHejXku-gxwt8WikxUePVz2ghfM2CJoM5d6myWu-w3vTUNjSunGTvxenxuMYIQ10wew?expires=1786536000&signature=50fb1261e6392235cb7be2d57b801a677cf3128eca0094e3ea366d98e0a7f4c4&req=dSUuE816nIJWW%2FMW3nq%2Bgb7fOo1hzhUFA2da098TLSRlqnnxUjfrOEpaI7H%2B%0A0sKXBsCXIIyB%2BppyI9rxFzPMhcg%3D%0A)
7. Neste passo, você pode definir filtros a partir dos dados enviados pelo Ploomes. Assim, é possível estabelecer uma condição para que a automatização seja executada somente quando critérios específicos forem atendidos.

   ![Imagem 7: Neste passo, você pode definir filtros a partir dos dados enviados pelo Ploomes. Assim, é possível estabelecer uma…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595442180/e954a7cf0633fb3b2c22b2fbc62a/AD_4nXfRtcZPrPLMOeMUKWaK6X0nGGhKo8iF2CoKQUnD9oaqjxlluke0ZOgr5X5-C6QwKECumC3b-aLnAyu6z6Qcjf47zYdPdr-ICttIsH9x8rurPIle3mlxvXnMcUQLhIyepg7bJm3N?expires=1786536000&signature=c0b13806734d77047d819d2adf1f6716e86880055e3694a0188c1c352960b60c&req=dSUuE816n4BXWfMW3nq%2BgW3ZBYzfg3hK5OwUwGcgMEtds7bOx9NKXtUft1oy%0AaHMCknPrLO0piUrbvEsozRzzfK8%3D%0A)
8. Com a sua conta da Ploomes configurada, clique em **“Conectar Nova Ferramenta”**;

   ![Imagem 8: Com a sua conta da Ploomes configurada, clique em “Conectar Nova Ferramenta” ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595442826/b23d9ff116cb25b0d8a5b39f47da/AD_4nXfyOTl_CrZTPX1LKaGXoirO6GMZhM8F760VxoUamTLvgYnCRdunK3F3BE0NsZMfxHklQWnbB-e2WS5xLydjtaMOWUYHoK52AUcjxEQznVcTfSZOfNkaAYgIKRNLxfZ3hZEcJMszVg?expires=1786536000&signature=1013f43fbe14c03d69999be8ffadf5513adbf621660284a3c358a2c3a1a5681a&req=dSUuE816n4ldX%2FMW3nq%2BgTSlcQsZsp9IYMGxmz8xys8jDWMWq%2FkKq28xH5CB%0Ag%2FBlbTXx3HyTv4sx%2B%2FWdI0ABcgU%3D%0A)
9. Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “**Facebook Custom Audiences**” e uma ação, ou seja, a tarefa que será executada na ferramenta de destino. Neste caso, selecione **“Adicionar lead a uma audiência personalizada”** e clique em **“Continuar”**;

   ![Imagem 9: Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “ Facebook Custom…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595443337/24cffd5a270bf7cbe77c939b6ef5/AD_4nXfkL6kz14g-GkjsgfD4P9a3lKaJkqCSf43YWN4k6Hkvs_xnFHqkzyXppXZkg2FSzOfZmgNp1LYN2LJYDhXHbx0ifMuXkYHNwjEp8B8A-tQwlhq0z3b7TDAYyKwjQXEejYC1_Ouu?expires=1786536000&signature=1b4e34e4dab3e8ef258f5ee633aa059467536e9863ab7fc65eae3cc769ca22a2&req=dSUuE816noJcXvMW3nq%2BgZ4d32O%2FILEQLj%2B5HBFA4fO5fV%2BrSK32hsetuRKH%0AukTp7HXgUjPzMrUGdzigeAMCHAE%3D%0A)

Para que sua automatização funcione como o esperado, **é necessário que a conta do Facebook conectada na Pluga tenha acesso a uma conta de anúncios**.

Caso você não possua uma conta de anúncio, você pode criá-la através deste [link](https://www.facebook.com/business/tools/ads-manager/get-started). A conta de anúncio precisa ter acesso a uma lista de público personalizada, do tipo **"Lista de clientes”**.

10. Em seguida, você precisa conectar a sua conta. Basta clicar em **“Conecte Sua Conta”** e realizar a autenticação. Essa etapa só precisa ser realizada na primeira conexão de cada ferramenta. Caso você crie uma nova integração com o Facebook Custom Audiences, sua conta já aparecerá entre as contas conectadas.

![Imagem 10: 10. Em seguida, você precisa conectar a sua conta. Basta clicar em “Conecte Sua Conta” e realizar a autenticação. Essa…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595444757/0e6186c094e1c745401ae81dac6c/AD_4nXcDm_XIN_cb5-2g3pM2SchyfnY1ZPa67wVXQdYis9LYdGp8Mc7oDgbZqhjjj-8Ue5Bc9Mj_sF--reyEFs0C7JSrDKfxuBb9zqxcsE3AS-2Lh1K-uXQ8brbn5LaeODuITvxaNofcjg?expires=1786536000&signature=bda281081160efe287dbf7f6157caabb86a261fa3abf50d597a7127d6bb5c3a0&req=dSUuE816mYZaXvMW3nq%2BgVdbmt%2FlV5iwPv4%2Fh5HruwUPmEnPP6I9LjUR7suL%0Asp3xbq4iOfmpGM2lbGx9%2B9RNNkY%3D%0A)

11. Após a autenticação da conta, ajuste as opções do Facebook Lead Ads que serão a base para a sua automatização. Selecione a conta de anúncio, além da audiência customizada que vai receber os novos contatos a partir da integração. Feito isso, clique em **“Continuar”**.

![Imagem 11: 11. Após a autenticação da conta, ajuste as opções do Facebook Lead Ads que serão a base para a sua automatização.…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595445404/2923f7627226116ab130efed7e8e/AD_4nXfk2nGJgM_KRWtZjnsL0_sR2154pTBMmY3gGNnNyBKYHop2EUBvYp3HadwhtBpBllTlIuNSbsOSVml-XW8RRsIPVobxa6j6yJxSYEC4q_ytHpp7dVTfFrr-yDmOPj2ZvjBs7AhQRQ?expires=1786536000&signature=d96981f6cae5f9101c52404ac9b6062346c120ce157beafcc689dd3fd6d54e87&req=dSUuE816mIVfXfMW3nq%2BgYNrXuTwBKm6cr6su3NeVYiSrr83NPoAZOI4sXio%0Ath%2BTxC5b3QVk54OwpkfFSBqLEyw%3D%0A)

12. No último passo, você deve definir quais informações constarão em cada campo do novo lead na Audiência. Preencha os campos **“Email do lead”** e **“Celular do lead”** e em seguida clique em continuar. Você pode importar dados do Ploomes através do botão **“Inserir infos”**, presente em cada um dos campos. Após configurar essas opções, clique em **“Continuar”**.

![Imagem 12: 12. No último passo, você deve definir quais informações constarão em cada campo do novo lead na Audiência. Preencha os…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595446115/e05306a85aa9292ac4b73a84895a/AD_4nXfv3XL9jHqInna-zKeRHv4ou6K8W63J83ygySacVgvzOCsQvU4c_5iSlKXVz3_QlYN8bR3TdhK6SStGf2tvjUuZP3NuwmtjWJg-20o7sLMX_A0Pfp4s32sCcKVHN5nimk_kuBtr9w?expires=1786536000&signature=6a165021c395f7d997056bb134dd24f7f1c428bb481b84817dc55712e53cb2bc&req=dSUuE816m4BeXPMW3nq%2BgXZWSKeGERWenN%2BTQP%2Fniq7Nn4Yo%2B2HEVDw%2Baof%2F%0ASFU2R6%2BFtYKGOVn9ijr%2BObizAuM%3D%0A)

13. Ao terminar a personalização desses campos, é só clicar em “**Finalizar automatização**” no fim da página e pronto. Está criada a sua automatização.

![Imagem 13: 13. Ao terminar a personalização desses campos, é só clicar em “ Finalizar automatização ” no fim da página e pronto.…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1595447762/d01ca284c58bcdf2d9bafec55612/AD_4nXfY0h6jCjP9jpqNZxqCaYcSC2P6rPhDJtIF-U2fVRJp0UJXVWM0HKf-9F6HV4nXx_lh8ge45Tz124961yP-h9V5DpCmKMzk9FEP30tXeXfdV8GHUbawRzph8vSEvkHtBawRaIIrjg?expires=1786536000&signature=fe8637dd80f8c7b4f5c47068284839b02bcf17bd641c8dc16ac91f4b5a0b86e8&req=dSUuE816moZZW%2FMW3nq%2BgcK3taGS5LSs1yOiJkCaSwPsu2vKdb2%2B3%2Fj7pQOq%0AYK3TyoIWkc2ToaSXyjvvIBkH0Ig%3D%0A)

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização **multi action**. Para isso, é só clicar em **“Conectar Nova Ferramenta”**.

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
