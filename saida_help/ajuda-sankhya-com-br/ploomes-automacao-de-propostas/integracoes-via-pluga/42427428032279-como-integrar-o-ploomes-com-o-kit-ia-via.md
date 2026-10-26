---
id: "42427428032279"
titulo: "Como integrar o Ploomes com o Kit IA (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427428032279-Como-integrar-o-Ploomes-com-o-Kit-IA-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:01:25Z"
rotulos: ["sync_hc", "ploomes", "ploomes_15363507", "sync_hash_19c1dece59e6"]
---

# Como integrar o Ploomes com o Kit IA (via Pluga)

**Observação:**

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

O Kit de IA da Pluga permite adicionar inteligência artificial em qualquer fluxo de automação com o Ploomes, sem precisar escrever um prompt ou configurar uma API manualmente. Você define o que quer que a IA faça de forma visual, e a Pluga cuida do resto nos bastidores.

Com ele, é possível:

- Classificar leads automaticamente como ICP ou Não-ICP assim que chegam ao Ploomes, eliminando triagem manual;
- Resumir anotações e informações de negócios para facilitar a leitura e a tomada de decisão do time;
- Extrair dados estruturados de textos livres (como e-mails e mensagens) e preencher campos no CRM;
- Traduzir conteúdos recebidos de leads internacionais antes de registrá-los no Ploomes.

Neste artigo, vamos detalhar o fluxo de classificação de leads: leads capturados no LinkedIn são avaliados pelo Kit de IA e registrados no Ploomes já segmentados, prontos para o time comercial agir.

## Requisitos

- Uma conta no [Ploomes](https://www.ploomes.com/);
- Uma conta na [Pluga](https://pluga.co/) (plano pago para fluxos multi-actions);
- Uma conta no [LinkedIn](https://www.linkedin.com/);
- Uma API Key do provedor de IA de sua preferência (Gemini, Claude, ChatGPT, entre outros).

## Passo a passo

Acesse a [Pluga](https://pluga.co/) e clique em **"Entrar"** ou em **"Cadastrar"** se este for o seu primeiro acesso;

![Imagem 1: Acesse a Pluga e clique em "Entrar" ou em "Cadastrar" se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453644862/cc9bfe7c610654b25b721d3670c2/6d89cba3-4f1e-4fd6-bf91-8b10376d55cb?expires=1786536000&signature=77ca5bcd4794562184a9210541f836972cfa626f9faf3455aafbc41a7d724a01&req=diQiFc96mYlZW%2FMW3nq%2BgdIQN4mno22udbs2HDvWw2tWXfiHsAGOJ7DOqMXV%0A3Hb0HAH4ZA1mrd0Gk9fEjCh5Mq4%3D%0A)

Na área de usuário, clique em **"Criar Automatização"** e dê um título para identificá-la no futuro;

[GIF animado: Imagem 2: Na área de usuário, clique em "Criar Automatização" e dê um título para identificá-la no futuro;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453648425/848e7ebbfac93073eac0d536e82a/image13.gif?expires=1786536000&signature=7553c1b23700c21fd34e67af854016d9da1c6df6ddbb818dcd5c34dd0a63afbe&req=diQiFc96lYVdXPMW3nq%2BgVZtJkKH1CXvCoXxq9kIJH32wClf3ApThxqDyb4H%0AID37lh0tds9r4k5aSNICEL8is%2F0%3D%0A)

---

## Conectando-se ao LinkedIn

Selecione o **LinkedIn Lead Ads** como ferramenta de origem e escolha o gatilho disponível para captura de leads. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 3: Selecione o LinkedIn Lead Ads como ferramenta de origem e escolha o gatilho disponível para captura de leads. Em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453650632/c24d62e11822fda867f9132d6845/f45fa6be-0608-49f0-be8e-66e6d0d36ec7?expires=1786536000&signature=48da970af00cabcffee7c502c7ac468ea72d87c9d2117d33427fe358a454b389&req=diQiFc97nYdcW%2FMW3nq%2BgasYZ8MIAw1ERfBXb4RrDOyXX8J8ufCIVhtRbt1b%0A8o8SDm7oRRPxWUXg3EmstKLu%2F%2BA%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser feito uma vez;

![Imagem 4: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser feito uma…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453651363/8679e510d1574e3f1c1f5f75b9ab/ad3d656c-84ec-45a6-a0d1-6e183dbe0ca4?expires=1786536000&signature=f183683c2137391cdd553cab311f9d60a3dd3bf10413048ef6c5edb1d2681956&req=diQiFc97nIJZWvMW3nq%2BgcPwWQ6M0J3%2FKBawPTAvvvnGAwFebtRqtMbemM93%0Adi7ju0OmJ8B1tELhnxqPVNoo8a0%3D%0A)

Se quiser, adicione filtros para refinar quais leads acionarão a automatização. Clique em **"Salvar e Continuar"** e, em seguida, em **"Conectar Nova Ferramenta"**;

![Imagem 5: Se quiser, adicione filtros para refinar quais leads acionarão a automatização. Clique em "Salvar e Continuar" e, em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453652310/b844bf2749720ac53b9c486fe7a8/95eddbdd-9b2d-4153-a147-84718e1149d6?expires=1786536000&signature=00a467120a617697705ef5fa6cff24e4532b04e2b4852cddf41375a3b5438998&req=diQiFc97n4JeWfMW3nq%2BgQnYEsC96%2Bhmm1TTQ%2B7vH55GE8OK8QjTckmWS0%2Bz%0A4CXuPNEyQPrmgJI6TMn0ivNBwHg%3D%0A)

---

## Classificando o lead com o Kit de IA

Escolha a ferramenta **Kit de IA** e a ação **"Classificar"**. Essa ação recebe os dados do lead e devolve exatamente uma das categorias que você definir, sem ambiguidade. Clique em **"Salvar e Continuar"**;

![Imagem 6: Escolha a ferramenta Kit de IA e a ação "Classificar" . Essa ação recebe os dados do lead e devolve exatamente uma das…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453654153/a50e18710616bd019f92c7cba115/df9c966a-9368-4943-9065-016aca9c6806?expires=1786536000&signature=95d09ae2bdf8345c6a80d7feac2874c1e87308f0feebe80ee7d5987e0e29d3e7&req=diQiFc97mYBaWvMW3nq%2BgRBRNU22xK2aDv%2FfTCctvJtYyga87%2F5lxWv9dmeB%0Ahr%2Bk9Vcue%2BFBaJYxbqzreDMpjzw%3D%0A)

Selecione o modelo de **IA** de sua preferência e insira a **API Key** correspondente;

![Imagem 7: Selecione o modelo de IA de sua preferência e insira a API Key correspondente;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453683768/cb5462234388ffe69b06d966013d/aafb30f2-ef88-4364-a4de-1fcc6fc397f3?expires=1786536000&signature=f5a14bc001fb813bd5eefe532c94984de0b0aa8732ddb5551821cb5b4e287d25&req=diQiFc92noZZUfMW3nq%2BgWubJxAYUqIsl%2Fcch9IS%2Bi2%2BhLs3h8c%2Bh9n3WXPM%0A2BHnUnO2g5fjQBhQUFjZgh3RLTI%3D%0A)

No campo **"Texto/Informação de entrada"**, mapeie os atributos do LinkedIn que a IA deve analisar, como cargo, empresa, setor e localização;

![Imagem 8: No campo "Texto/Informação de entrada" , mapeie os atributos do LinkedIn que a IA deve analisar, como cargo, empresa,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453684438/32569e87fa20ca14a2139226c17d/e3bb95ca-27e0-48ef-be55-929dbb4c5144?expires=1786536000&signature=26bad41d24305f84c99e834ab84dedc8de33c2244fc647ccccaeb7e256852088&req=diQiFc92mYVcUfMW3nq%2BgUh34wsJsWx7CZAzfmSe%2F54lZAMXjUchVBPv7liZ%0AZ6KuC97OM3x4Yp0qK6EPw%2BeD5RI%3D%0A)

Defina as categorias de classificação:

- **ICP** — descreva o perfil ideal: cargo de decisão, setor de atuação, porte da empresa;

Por exemplo:

```
Perfil com potencial real de compra: decisor ou influenciador direto na jornada de compra (CEO, Diretor Comercial, Gerente de Vendas, Head de Operações), atuando em empresa com operação estruturada de vendas — setores como indústria, distribuição, SaaS B2B ou serviços corporativos, com porte de médio a grande (acima de 50 colaboradores ou faturamento relevante).
```

- **Não-ICP** — descreva os perfis que não se enquadram no seu público-alvo.

Por exemplo:

```
Perfil sem aderência ao produto: estudantes, estagiários, profissionais autônomos ou freelancers, empresas de pequeno porte sem time comercial estruturado, perfis de setores sem fit com CRM (varejo B2C, ONGs, setor público) ou cargos operacionais sem poder de decisão ou influência na compra.
```

![Imagem 9: Por exemplo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453727453/36625359026207c322155620fad4/7e85c144-02db-46e5-a057-d5a1433a27ae?expires=1786536000&signature=024342e6cd1154e3decb810309efb06aa6f8f8caddb1917e8871813a3d20ee0a&req=diQiFc58moVaWvMW3nq%2BgdyIZGOzBxJ46DSmGdsxjIQUQmDvbgtHg%2FglREWz%0Az%2BED658IM%2FzGE8zr54rZDEdP7S4%3D%0A)

Clique em **"Salvar e Continuar"**;

---

## Dividindo o lead em rotas com o Roteador

Com o lead classificado, adicione o **Roteador** como próxima etapa. O Roteador é um componente da Pluga que permite criar caminhos condicionais dentro de uma única automatização, sem precisar duplicar fluxos. Clique em **"Conectar Nova Ferramenta"** e selecione o **Roteador**, além da ação “Correspondência única”;

![Imagem 10: Com o lead classificado, adicione o Roteador como próxima etapa. O Roteador é um componente da Pluga que permite criar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453728575/f3c4eff3b19407bddbd56a407fe6/42590902-9275-4596-bd26-1c4a234e45e7?expires=1786536000&signature=baa844ea6217549636faa10453dc455787c3ee2a829e12bff1d40b6a3865645f&req=diQiFc58lYRYXPMW3nq%2BgeCcb%2B%2BS9T5ff5jpJ1ZMLb2cESiZp2qXz0D92Zlb%0A4%2F%2Fcgl16CRgKv5rYvaSoeZ4Emok%3D%0A)

Configure duas rotas:

- **Rota A** — condição: a resposta do Kit de IA é exatamente igual a **"ICP"**. Esses leads serão encaminhados para o Ploomes com a criação de um negócio no funil de leads;
- **Rota B** — condição: a resposta do Kit de IA é diferente de **"ICP"**. Esses leads podem ser direcionados para uma ferramenta de e-mail marketing e um fluxo de renutrição, evitando o descarte prematuro de leads que ainda podem amadurecer.

![Imagem 11: Rota B — condição: a resposta do Kit de IA é diferente de "ICP" . Esses leads podem ser direcionados para uma…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453729954/e18888837548b7b5b39943fe460d/dcca2b1e-e270-42ed-99fc-942fb0dbff1e?expires=1786536000&signature=6fb8ed3ade7168b770a77c8654f5948487249732a9ac0791980e17a0aa4bbdbe&req=diQiFc58lIhaXfMW3nq%2BgeDDYnPC7MbqNn26emeIkN%2Bp%2Be1zh2PEsYpPuHeB%0ARrln1I41VY8ZsG7JTYDtOxs6bL8%3D%0A)

Clique em **"Salvar e Continuar"**;

## Rota A: Enviando o lead ICP para o Ploomes

Selecione o **Ploomes** como ferramenta de destino e escolha a ação **"Criar ou atualizar card"** ou **"Criar ou atualizar cliente"**, conforme o seu fluxo. Clique em **"Salvar e Continuar"**;

![Imagem 12: Selecione o Ploomes como ferramenta de destino e escolha a ação "Criar ou atualizar card" ou "Criar ou atualizar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453731307/af8a56b2a94a28683dab4580d408/d9e26752-f49a-41c2-ade2-55b10d120709?expires=1786536000&signature=b64e8202adc71c9063cbddb01de9f91dc4df10c8083e0359c897da6ad15030f7&req=diQiFc59nIJfXvMW3nq%2BgaQ2lOcbcfgG6jxHm8CIsn8aJy5SHPJM3J%2F48fSg%0AJGfWrFxL1nme0%2B7Ha1HXkEyqSBY%3D%0A)

Conecte sua conta no Ploomes clicando em **"Conectar Nova Conta"** e realize a autenticação, caso ainda não tenha feito isso;

![Imagem 13: Conecte sua conta no Ploomes clicando em "Conectar Nova Conta" e realize a autenticação, caso ainda não tenha feito…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453731804/ff207e5ea075eeb77bec5fd824a4/b01e6ac8-cd33-432f-a831-0a66d9497b37?expires=1786536000&signature=b0ec4d54bb3a8badb82af6347965eed08b0ed3d8c895a55cd5101e24f6082497&req=diQiFc59nIlfXfMW3nq%2BgcfR6uZxR9yqyKEoaKYyMeIlAHiQX3nwTV6nV3GQ%0AbuxV2LNlAehe8utIRzUFZVNmFX8%3D%0A)

Indique em qual funil e qual etapa será considerada para a criação do card, além de outras opções;

![Imagem 14: Indique em qual funil e qual etapa será considerada para a criação do card, além de outras opções;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453732315/6cdba73cf1f1360c22f7524ee3db/d110d88a-576f-4697-bec5-09558501c084?expires=1786536000&signature=b4d4e79c2848990ae4b54a34381d9cf083a91de7bfd3364b0e1eebd868820b60&req=diQiFc59n4JeXPMW3nq%2BgSYp6gzm8YF94yJ2cMLfCiRi1eEgOGwWlX6Uu2uL%0AnAy9QVuDX6oc0a7KNimkAG4MFMs%3D%0A)

Mapeie os campos: preencha nome, empresa, cargo e e-mail com os atributos vindos do LinkedIn;

![Imagem 15: Mapeie os campos: preencha nome, empresa, cargo e e-mail com os atributos vindos do LinkedIn;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453732634/9a62e1099060e9485556f0bf5b50/4094b99c-f131-4c1f-878e-622f48dbf9d9?expires=1786536000&signature=208dc248a3018ae80cf8e4ea6996e80b1b3ed7a1723e9e0b68079b7b2ef44670&req=diQiFc59n4dcXfMW3nq%2BgeM7%2Ft12H2b3UlIjQXUBc37PjM6uS%2FOyRzM2orqm%0Ay8tPNRfn%2F3ilysGSqJbYAwa3DbE%3D%0A)

Para registrar a classificação, selecione a resposta do **Kit de IA** em um campo personalizado do Ploomes — como um campo de qualificação ou tag do negócio. Clique em **"Salvar e Continuar"**;

![Imagem 16: Para registrar a classificação, selecione a resposta do Kit de IA em um campo personalizado do Ploomes — como um campo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453733041/80a11571384eecb52aa0b54a227a/136d1be3-6cb8-4174-be28-fddeaecacae3?expires=1786536000&signature=608fdf9809bd885b6023a42ca26f6cf73c60f913d9e0755879cba38b885079ed&req=diQiFc59noFbWPMW3nq%2BgZQtGKauqI7hoDODXcG3xW12x%2BZPVgss5FABayjR%0AnjBlTuq2ntByE6ZU0pO6hzdc8UU%3D%0A)

Prontinho. Agora, sempre que um novo lead for capturado no LinkedIn, o Kit de IA irá classificá-lo automaticamente e o resultado chegará ao Ploomes já segmentado — sem nenhuma triagem manual.

![Imagem 17: Prontinho. Agora, sempre que um novo lead for capturado no LinkedIn, o Kit de IA irá classificá-lo automaticamente e o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2453733477/7e2e47922b585ee64b3f5f4ddcda/c1f06796-c750-4232-a53b-387e7dfc4e2b?expires=1786536000&signature=4323180c52cf2b4e2533e9c72dbc369786706d00d0c723c44df20754338229ed&req=diQiFc59noVYXvMW3nq%2BgQpCQ3%2FxevJ9CKsB6mPl4AsvYPSte8OH8tkr%2BVPV%0AnOe9VXqFFG3qyVu8O3K919XP1qs%3D%0A)

Caso queira tratar leads ICP e Não-ICP de formas diferentes dentro do mesmo fluxo (por exemplo, criar um negócio apenas para leads ICP e registrar apenas o contato para os demais), configurando esses detalhes na **Rota B**.

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho. Para isso, é só clicar em **"Conectar Nova Ferramenta"**.

---

## Suporte

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar. É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar <https://pluga.zendesk.com/hc/pt-br/requests/new>.
