---
id: "42427430297495"
titulo: "Como integrar o Ploomes com o Claude (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427430297495-Como-integrar-o-Ploomes-com-o-Claude-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:01:50Z"
rotulos: ["sync_hc", "ploomes", "ploomes_15137290", "sync_hash_5d5f9b0a9560"]
---

# Como integrar o Ploomes com o Claude (via Pluga)

**Observação:**

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

Conectar o Ploomes ao Claude via Pluga permite que a IA atue como uma camada de processamento inteligente dentro do seu fluxo comercial. O Claude interpreta os dados que chegam do Ploomes, como informações de um card, dados de uma proposta ou o perfil de um cliente, e os transforma em análises, textos ou estruturas prontas para uso, sem nenhum trabalho manual;

O resultado são automatizações que vão além de mover dados de um lugar para outro: cada registro chega ao destino já enriquecido, qualificado ou com contexto gerado automaticamente pelo Claude;

Alguns exemplos do que é possível fazer:

- A cada card ganho no Ploomes, enviar os dados da negociação ao Claude para gerar automaticamente um e-mail de boas-vindas personalizado e disparar via Gmail;
- Quando um card chegar a uma etapa específica do funil, acionar o Claude para gerar uma proposta comercial estruturada com base nos dados do negócio e do cliente;
- A cada nova proposta criada no Ploomes, usar o Claude para extrair e resumir os principais pontos e registrar o resumo em uma planilha de acompanhamento no Google Sheets;
- Quando um card for perdido no Ploomes, enviar os dados ao Claude para que ele analise as informações e gere uma anotação de diagnóstico, enviada automaticamente ao canal do time de vendas no Slack;
- A cada cliente criado no Ploomes, acionar o Claude para enriquecer o perfil com uma análise de potencial com base nos dados cadastrais e registrar as observações no próprio Ploomes.

Como o Claude é sempre o intermediário da automatização e não a origem, você pode combiná-lo com qualquer gatilho disponível no Ploomes, card criado, card ganho, card perdido, card em etapa de funil, proposta criada, cliente criado, entre outros, e enviar o resultado para qualquer ferramenta de destino integrada à Pluga.

## Requisitos

- Uma conta no [Ploomes](https://app10.ploomes.com/login);
- Uma conta na [Pluga](https://pluga.co/);
- Acesso ao [Claude](https://www.anthropic.com/api) (via API da Anthropic).

**Nota:** automatizações com IA exigem pelo menos três ferramentas, com o Claude como intermediário, e utilizam o recurso de integrações multi-actions, disponível nos [planos pagos](https://pluga.co/precos/) da Pluga.

## Passo a passo

Neste artigo você encontra casos de uso prontos para implementar com o Claude e o Ploomes via Pluga. Os três primeiros passos são comuns a todos os casos — faça-os uma única vez e avance direto para o caso que faz mais sentido para o seu contexto:

- **1. Como qualificar automaticamente cards ganhos no Ploomes com o Claude e notificar o time de vendas no Slack**, ideal para times comerciais que querem que cada negócio fechado gere automaticamente uma comunicação interna personalizada e registrada.
- **2. Como gerar resumos de propostas criadas no Ploomes com o Claude e registrar em uma planilha**, ideal para times que precisam acompanhar o histórico de propostas de forma organizada, sem digitação manual.

Acesse a [Pluga](https://pluga.co/) e clique em **"Entrar"** ou em **"Cadastrar"** se este for o seu primeiro acesso.

![Imagem 1: Acesse a Pluga e clique em "Entrar" ou em "Cadastrar" se este for o seu primeiro acesso.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388865454/0cfba94d05afb8d05012c4a51946/fc0509ad-50e3-4ddc-a8b1-4d4470499020?expires=1786536000&signature=475db6d31ea6f91dfc1e770c9a050a3bc871d0308bc3b00524ea570f0479027e&req=diMvHsF4mIVaXfMW3nq%2BgaWoQs5K6CyGNRkIrs1H1j9L7KnXeRwgbRNdYzyX%0A%2FaLjhKG5Hi8jXQYhC%2Fua8zOZC1w%3D%0A)

Na área de usuário da Pluga, clique em **"Criar Automatização"**.

[GIF animado: Imagem 2: Na área de usuário da Pluga, clique em "Criar Automatização" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388902135/ee1bffaa94875ce9d6b231dd2c35/image21.gif?expires=1786536000&signature=2cba97658cd80b68c27d98e787efbd011809e7b6f01abfa87a6555f8bdd07cb2&req=diMvHsB%2Bn4BcXPMW3nq%2BgXDzoan1DkuRCuSVAgnD0ZEPP0GlHabxSvMOch5q%0AEZ%2FuX7%2BTnEiKmbqXqG%2BOMLLgLBM%3D%0A)

Dê um título para a sua automatização e siga para o caso de uso desejado abaixo.

---

## 1. Qualificar automaticamente leads capturados no Facebook Lead Ads

Quando um card for marcado como ganho no Ploomes, os dados do negócio e do cliente são enviados ao Claude, que gera automaticamente um resumo qualificado da venda. Em seguida, uma notificação é disparada no canal do time de vendas no Slack com esse resumo, reduzindo a necessidade de comunicados manuais e garantindo que o time fique informado em tempo real sobre cada negócio fechado;

## Conectando-se ao Facebook Lead Ads

Selecione o **Facebook Lead Ads** como ferramenta de origem e o gatilho **"Nova resposta em um anúncio"**. Clique em "Salvar e continuar";

![Imagem 3: Selecione o Facebook Lead Ads como ferramenta de origem e o gatilho "Nova resposta em um anúncio" . Clique em "Salvar e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388922443/d16c2b3ee1f90e4c95339910b655/a66853a8-a5fc-44ab-91b1-ce042da68190?expires=1786536000&signature=b03490187acd075180090448d692c90412137c54ac16d6f29dce245cbccf99f6&req=diMvHsB8n4VbWvMW3nq%2BgRatfPLepWNq2NR%2BGlya3N0Cdt7lLbG1dPFoBZx9%0Aqp7GrCQ1n29uz%2BwUw8BhVZFzgZw%3D%0A)

Conecte sua conta do Facebook clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Importante: a conta conectada precisa ter o maior nível de acesso à Página para que a automatização funcione corretamente;

![Imagem 4: Conecte sua conta do Facebook clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388929000/a1ceb0c6d17112a6426de10abe22/47b47a6b-99e6-4624-9c46-5f1d82986fe8?expires=1786536000&signature=e94ee8af49e10ea42e1877b72356a5898784a1467926d8ae8ec2ad63fe6ed63b&req=diMvHsB8lIFfWfMW3nq%2BgYGZf8d%2BMyyyp8iG%2B6FCxEaBwh1goN4yFKJwZLg9%0AUNizEN6QUYxOVQXAwTZmGVj0DUc%3D%0A)

Selecione a **página** vinculada à campanha e o **formulário** que será monitorado. Clique em "**Salvar e continuar**";

![Imagem 5: Selecione a página vinculada à campanha e o formulário que será monitorado. Clique em " Salvar e continuar ";](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388931754/ebc74b8952d78d18a893cbe7f7c8/65a75446-d3fc-4958-b2e3-60003fe20aff?expires=1786536000&signature=f1667bee2cf4b5f67be38337bb9de45c50d3af3feea6375dfb760ebff502c0a3&req=diMvHsB9nIZaXfMW3nq%2BgXbj2qqCgJZ4E0ydGny0GHi%2FmO3MI4Uod9M%2F17ru%0A%2FGVv67rp28%2BI0zghnyPy%2BbicNNw%3D%0A)

Se quiser, configure filtros para ativar a automatização apenas quando os dados atenderem a critérios específicos. Clique em "**Conectar Nova Ferramenta**";

![Imagem 6: Se quiser, configure filtros para ativar a automatização apenas quando os dados atenderem a critérios específicos.…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388933737/b046a3aa0488daa065a5312b8038/13453ad0-60bb-497c-a2b4-cf43108b0ec6?expires=1786536000&signature=ad633d3822895accd356926b229dfa59dc02a8a1da711405fd44b880a15516de&req=diMvHsB9noZcXvMW3nq%2Bga6WzLfOPJA8SGHCUSO%2BDIET3TRShaJN14Yn826%2B%0A0YerIRynV1cbVJhGusYs3%2Bl0xa0%3D%0A)

---

## Configurando o Claude

Selecione o **Claude** e a ação **"Iniciar conversa"**. Clique em **"Salvar e continuar";**

![Imagem 7: Selecione o Claude e a ação "Iniciar conversa" . Clique em "Salvar e continuar";](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388936830/b44b0b39541e5f43b6ac845b8f2b/48113c18-1f70-4d0d-b30b-89ee7dae863e?expires=1786536000&signature=54b88e75c2b9f504ab3f7bb32ec53b6094a9c27f25d3ee4d326640af1814fd53&req=diMvHsB9m4lcWfMW3nq%2BgR8bfiwjdlwI6oOtiqmFjwHnGiNMoy8ZeSE%2B9O6K%0At4iWICzO1xaIq%2FZ9g03kpaA%2F0%2Bc%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação com a sua conta da Anthropic. Esse processo só precisa ser feito uma única vez;

![Imagem 8: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação com a sua conta da Anthropic. Esse…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2388940009/3ab59a73b988b4e767e774318531/6317121c-2c42-4b0e-8262-2c201cba850a?expires=1786536000&signature=07e8babb73781e4f3c467442273b770ee3dd75c65e6e4f32eb9d1ab8d397b8f2&req=diMvHsB6nYFfUPMW3nq%2Bgen3b3TRiwkAWzYuH2I9n131JQVqmltqZN2TB57O%0AQpvIVyNmLKfKvvRngN4J0hl533I%3D%0A)

No campo **"Mensagem (prompt de comando)"**, cole o modelo abaixo e ajuste conforme necessário. Use o botão **"Inserir infos"** para mapear as variables com os dados recebidos do Ploomes;

**Modelo de prompt — Caso 1**

```
Você é o responsável pela qualificação dos leads enviados ao CRM. Vou fornecer as informações do lead e os dados do anúncio em que ele converteu. O nome da campanha identifica o produto ou linha de produtos sendo comercializado. O Adset Name indica a segmentação de público para o qual o anúncio foi veiculado. O Ad Name revela o argumento de venda específico utilizado naquele criativo (exemplos: "parcelamento sem juros", "frete grátis", "entrada facilitada", "localização privilegiada", "área de lazer completa").

Dados do lead:
- Nome: {full_name}
- E-mail: {email}
- Telefone: {phone_number}
- Campanha: {campaign_name}
- Argumento do anúncio: {ad_name}

Com base nessas informações, elabore o perfil deste lead indicando:
1. A qual segmentação ele pertence
2. Qual argumento de venda motivou a conversão
3. Qual produto ou grupo de produtos ele demonstrou interesse

Escreva em formato de parágrafo curto, direto e objetivo, sugerindo uma primeira abordagem de vendas personalizada. Não faça nenhuma sugestão que dê continuidade à conversa.

Regras:
- Use apenas as informações fornecidas, não invente dados
- Tom direto e útil para o time de vendas
```

![Imagem 9: Modelo de prompt — Caso 1](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389024055/6611116ad6e95544f91414eb43a2/c93f5c94-1a4f-4f13-8c99-a43108c8197a?expires=1786536000&signature=79ab8dbdb759ca3d4961e1b820c310ec34f4f2d9e0f24eb078f35842883fface&req=diMvH8l8mYFaXPMW3nq%2Bgdv0MZNdRCxWUQtI6wgIkhuviGLM0oykZjpEWGbA%0A3RGsuaOfwoNmkbYzHubZ%2BKCrTbc%3D%0A)

**Atenção:** antes de ativar a automatização, teste o prompt diretamente na interface do Claude. Cole um exemplo real de dados de um card do Ploomes e verifique se o resultado está como esperado. Só ative a automatização depois que o retorno estiver consistente.

No campo **"Instruções de Sistema"**, defina o comportamento do modelo. Exemplo:

```
Você é um especialista em qualificação de leads para times comerciais. Interprete os dados de formulários e metadados de anúncios do Facebook Lead Ads e transforme-os em perfis objetivos e acionáveis. Trabalhe exclusivamente com as informações fornecidas, nunca invente dados. Seja direto, claro e útil para o time de vendas." Ao finalizar, clique em "Salvar e continuar" e em "Conectar Nova Ferramenta;
```

![Imagem 10: No campo "Instruções de Sistema" , defina o comportamento do modelo. Exemplo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389137167/0496b08a225316f3376349ff2989/8e805ac5-5c57-4fc8-9c35-4aceed48d232?expires=1786536000&signature=092d89ac1138b8bbfeb4f6d94f5e2f9aefadd60d9f7cf9c7ddd8aa952ef301d1&req=diMvH8h9moBZXvMW3nq%2BgbZqEMM08gMt29TwhNWuWEtjAK5D9ugYwuyuN7pb%0A2FdN%2FuqCsKGSZY7M%2FiNJ31dnt6I%3D%0A)

---

## Atualizando card no Ploomes

Selecione o Ploomes e a ação **"Criar ou atualizar card"**. Clique em "Salvar e continuar";

![Imagem 11: Selecione o Ploomes e a ação "Criar ou atualizar card" . Clique em "Salvar e continuar";](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389176298/f1308ff7248b1b30dafb42625e96/0d805b97-8eee-4085-925c-c12bc55b10ed?expires=1786536000&signature=e0c525f4017045edfca88596f7b3082c556675cfb1b7518ea4e4c3c30b3f2f4b&req=diMvH8h5m4NWUfMW3nq%2BgQQlx41F%2FGFa3G2OO5LYddOgUQtyOIe1AaNzb%2FxR%0AvQQS6FZ0H4Pb2u4KsaAmVWdSRSU%3D%0A)

Conecte sua conta do Ploomes clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez;

![Imagem 12: Conecte sua conta do Ploomes clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389189094/d5fee715da1a5708b4eb03c96367/4efdad69-b470-47de-93a4-3171d716c70f?expires=1786536000&signature=695d034962600fa2ae1826f534054f61329aed66119cb3de38de3b2912a64991&req=diMvH8h2lIFWXfMW3nq%2BgUREQP1sF3gkXBW1gls0kB%2FtxNNQjefWZ3igpM0I%0AF%2FnQUMaNnh2OaaDTLZ0FX5OPSto%3D%0A)

Selecione o **funil** e a **etapa** em que o negócio será criado ou atualizado;

![Imagem 13: Selecione o funil e a etapa em que o negócio será criado ou atualizado;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389189998/8f3d720f20578d4de0c5c3c1eeac/f2cbf87c-f5a8-47ad-9f9b-dc74e7237f8e?expires=1786536000&signature=37beecae1ad7b2859d6fb09e0d5561264b80bc55ca3c72e16e7ecd4fe65bda99&req=diMvH8h2lIhWUfMW3nq%2BgRBVXIULYlBmb11rf4LPVXpiA7b%2FlNjrE3f9qL16%0A3LWcOK%2BRL5uXO5ZFysL77X1dmac%3D%0A)

Mapeie os campos obrigatórios: título do negócio e tipo de contato (empresa ou pessoa). Use o botão **"Inserir infos"** para preencher os demais campos com os dados do lead recebidos do Facebook Lead Ads, como nome, e-mail e telefone;

![Imagem 14: Mapeie os campos obrigatórios: título do negócio e tipo de contato (empresa ou pessoa). Use o botão "Inserir infos"…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389195761/2d5d09f2c1db6f567d4ec12aea35/b0bdf56e-fbba-4489-a3df-bbfb4e64eed8?expires=1786536000&signature=694b05416603597d6dd8f6bb89bc56a51784dbfd56f2049c665b53e9494cd3a1&req=diMvH8h3mIZZWPMW3nq%2BgTMO7QVbZP0RWyHfr4f1opnpitSfeJLanFHK2XwU%0AOAmmO6wYBFx08%2F0NRtW%2FEMIdogQ%3D%0A)

Para registrar o perfil gerado pelo Claude, insira a resposta da IA no campo personalizado de preferência, criado no seu funil do Ploomes;

![Imagem 15: Para registrar o perfil gerado pelo Claude, insira a resposta da IA no campo personalizado de preferência, criado no…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389196518/34ca70eccd6ad8b881e31d6339bc/adb7eb0c-c158-4912-9f94-4d50928add13?expires=1786536000&signature=888788450bde03716a152323d276f7469b3d8299ab2bda213f5d6b51fe95defd&req=diMvH8h3m4ReUfMW3nq%2BgbR2O9RaxV6zj6c8lDunKChvA%2FxpRd%2B0hYUwuZ5j%0ALUG5EKYKDwjsL%2FKHmytWEFdG%2B%2F4%3D%0A)

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi action. Para isso, é só clicar em **"Conectar Nova Ferramenta"**.

![Imagem 16: Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389197270/4b6efa684d224e1435c59fac6875/d5ddce69-8f0f-4489-b261-5d08f75499a9?expires=1786536000&signature=0448b64328bf0f2ba35f6c4f046e4e483f29d70aab6f39dda3914189b2f012b6&req=diMvH8h3moNYWfMW3nq%2BgaYPNcHZ8gwNReivIxAhPtBg0YL9fLywfbAT0h9m%0AITufcFxlJYtZM%2BSnyPSpMxMAdow%3D%0A)

---

## 2. Captura de e-mail de cotação para o Ploomes

Quando um e-mail de cotação chegar em uma guia ou marcador específico do Gmail, o Google Gemini extrai automaticamente as informações relevantes, como empresa, produto, valor e prazo, e cria ou atualiza um negócio diretamente no **Ploomes**, sem nenhuma entrada manual;

## Conectando-se ao Gmail

Selecione o **Gmail** como ferramenta de origem e o gatilho **"Novo e-mail em guia ou marcador"**. Clique em **"Salvar e continuar"**;

![Imagem 17: Selecione o Gmail como ferramenta de origem e o gatilho "Novo e-mail em guia ou marcador" . Clique em "Salvar e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389200985/ebdd1aaa862fe58ed28e9e93c6a5/485b0575-92d8-4e3a-aa8f-10a48002a805?expires=1786536000&signature=168e3f584292cf0d7e01094ba6199b4dfe22bb5f7aa3bcc84bcd3f984eddee64&req=diMvH8t%2BnYhXXPMW3nq%2BgeYZjGf%2Boq3oxFPndYytGCdtKrHkLdqOUG6PFYhN%0ArEZVyPZscrx%2BldGgmgIbF6q7TpY%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez;

![Imagem 18: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser realizado…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389202341/7c6bb9c5040ce83e18c0b3567e67/1e8a610a-ed1c-46e5-99c8-964f111806c7?expires=1786536000&signature=6adb5f149db7116894d18b2613461d09bbcae11509252b7df12b97cb90e58ac0&req=diMvH8t%2Bn4JbWPMW3nq%2BgZtb2GAjc%2F0uh198ol%2FKcE3OOCxbRIHG042ECjAC%0AN0FytKR5bRGOpUlWqCVu0lHwPEQ%3D%0A)

Defina a guia ou marcador que será monitorado. Dica: crie um marcador dedicado no Gmail — como "cotações" — e aplique-o manualmente ou via filtro automático nos e-mails de cotação;

![Imagem 19: Defina a guia ou marcador que será monitorado. Dica: crie um marcador dedicado no Gmail — como "cotações" — e aplique-o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389203147/210bb26a71e79f1ab4a47827cc65/8f2fa42b-8680-429b-8432-d1df5b08f4a9?expires=1786536000&signature=e5c03fe7a7648f224d9eee50f6f8ca9c008ce5225b8ca73314156c39cd4fc6c0&req=diMvH8t%2BnoBbXvMW3nq%2BgRYS4H9%2Boig3WlBxLi2NELVx%2Fecr6NRtJ7fl7U6d%0ApmaneXF%2F3%2FyHoFPerEbu%2Fz3Nhv4%3D%0A)

Se quiser, configure filtros adicionais para refinar os e-mails capturados. Clique em **"Conectar Nova Ferramenta"**;

![Imagem 20: Se quiser, configure filtros adicionais para refinar os e-mails capturados. Clique em "Conectar Nova Ferramenta" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389204016/3fd894a8d2d92e0fff69f509ee4b/5c037b14-2c08-42fe-af43-9cb302f4e0e2?expires=1786536000&signature=1653bed9341196a85be59b1820cc0f9a137be8abe74ff86428941ae84262288b&req=diMvH8t%2BmYFeX%2FMW3nq%2BgfXY0%2Bi1HwKS0Y3COc2XHl90Rg5RG5A5xf5VrUDa%0A64SZK27j%2B96xyJ2qP2hwGLF0pbc%3D%0A)

---

## Extraindo dados com o Claude

Selecione o Claude e a ação **"Extrair dados estruturados"**. Clique em **"Salvar e continuar"**;

![Imagem 21: Selecione o Claude e a ação "Extrair dados estruturados" . Clique em "Salvar e continuar" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389205276/7bf10ce45b56fa6e74a8842c1dfc/18032d54-ac4b-4008-8dc2-13284b73cedd?expires=1786536000&signature=5f868af1674087eab05bd2fdb53b309df6a78d2b29abc1caf6b08dc773975dc0&req=diMvH8t%2BmINYX%2FMW3nq%2Bge0eq4NbG%2FY2odEg7XcsJ3P%2Fh5PHcjbOTx3NFuui%0A5E6gBev3WHy7PaVs%2F2kiBAB36X4%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação com a sua conta da Anthropic. Esse processo só precisa ser feito uma única vez;

![Imagem 22: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação com a sua conta da Anthropic. Esse…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389206041/083ccc8d014d924f649dc581bc05/5577d2d8-5133-41f4-ab61-ef79f7f39de4?expires=1786536000&signature=3d8879f507b0985e8b271d89c7214a765c4b93cfd93169f5993a31e8a263d76a&req=diMvH8t%2Bm4FbWPMW3nq%2Bge97hXbpQoD6%2FM%2FXBymliEfgqGb45%2FmRG8b28Dwy%0AkXbxcg03AfV0JpuDGxYvphqH0eE%3D%0A)

No campo **"Texto a ser transformado em dados estruturados"**, use o botão **"Inserir infos"** para mapear os dados da proposta recebidos do Ploomes, como valor, produtos, cliente e descrição.

![Imagem 23: No campo "Texto a ser transformado em dados estruturados" , use o botão "Inserir infos" para mapear os dados da…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389206750/f711dbdd3cc0de67e496503b2f95/2b4f6c23-c22f-4c10-8bed-4912cb1e889f?expires=1786536000&signature=a38145227345e9d0334688c7671e294b9810dd598c8d4db3a4b888450d4428da&req=diMvH8t%2Bm4ZaWfMW3nq%2BgduLephbEypAvp8fx37MlPkPbp31T6u6jonqoD7f%0AGVthWNTnVSaIHV5MOo%2FS9hFUIS4%3D%0A)

No campo **"Instruções de Sistema"**, cole o prompt abaixo e ajuste os campos de extração conforme necessário.

**Modelo de prompt — Caso 2**

```
Você é um assistente especializado em análise de propostas comerciais B2B. Receberá os dados de uma proposta criada no CRM e deverá identificar e estruturar campos que serão preenchidos no CRM.
```

![Imagem 24: Modelo de prompt — Caso 2](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389212734/7d7b8cd80978dab5f588eb16fd6b/acfc5629-3706-4ac0-b2aa-804408b5af48?expires=1786536000&signature=991a287ef8c9ce694a79989c6f0f20af422ead4c460560febe4658da518dcc88&req=diMvH8t%2Fn4ZcXfMW3nq%2BgVoZ%2Fn3R%2FEkB6bayIa5POLuVZ%2FaQfi7W4RRShgay%0AvnJJYLzev09yowLsXWNLtCr1b%2Bs%3D%0A)

Indique a **quantidade de campos** que você deseja extrair e defina o nome e tipo de cada parâmetro, por exemplo: **cliente**, **valor\_total**, **produtos**, **responsavel** e **resumo**. Ao finalizar, clique em **"Salvar e continuar"** e em **"Conectar Nova Ferramenta"**

, cliente: nome do cliente ou empresa

, resumo: parágrafo curto com os principais pontos da proposta, voltado para o time comercial

, valor\_total: valor total da proposta

, produtos: lista dos produtos ou serviços incluídos

, responsavel: nome do vendedor responsável

![Imagem 25: , responsavel: nome do vendedor responsável](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389217211/4e46a12df62b868299c324819e59/b36fa14b-e1d8-4b8f-b147-27890e9dcaf0?expires=1786536000&signature=c17ac06eba8c2e917446ca123b733f08f162559035269a10f77b3c27dfc759df&req=diMvH8t%2FmoNeWPMW3nq%2Bgf5fjFxAMM5SrgrtJCA%2ByL4g1f%2BPXovwi2sHMD4F%0AX6U2f9VLhIMvnG7Tn7gHJiCDXvs%3D%0A)

Ao finalizar, clique em **"Salvar e continuar"** e em **"Conectar Nova Ferramenta"**;

---

## Registrando o Card no Ploomes

Selecione o **Ploomes** e a ação **"Criar ou atualizar card"**. Clique em **"Salvar e continuar"**.

![Imagem 26: Selecione o Ploomes e a ação "Criar ou atualizar card" . Clique em "Salvar e continuar" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389220340/97ba17a34de3ca24aca515a6696a/ee2dd711-49fa-411c-80c6-ff48b5c9dbbf?expires=1786536000&signature=c66e1ba25022e4af2a57fb6ca4b3dbb6bef3c857fcdb1a99e4b31a30ba9fcab1&req=diMvH8t8nYJbWfMW3nq%2BgXroJnm7UoPgdcGgA%2Bt7reD4As41ViDqfn53WWWu%0AzlCFsjUqCmGv%2Bmkwnnlqe2CGwtk%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Caso seja a sua primeira vez conectando a sua conta do **Ploomes**, clique em "Veja o passo a passo para encontrar suas chaves de acesso" e siga o breve tutorial;

![Imagem 27: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser realizado…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389221466/cc3513acd6181a2e9b00b1d0f2ac/480e2a9a-2c93-40c3-b002-66d17eaecf15?expires=1786536000&signature=9813e83c7ba22551441ccaeeae12273cbaadde9b0fc01cc2f13819a0eecfb845&req=diMvH8t8nIVZX%2FMW3nq%2BgdbmNSXbMAXL6jSQeG2iy4xxAV0QXH52OICYt4bp%0AlH2M1hyPeUAcu6HxNzZTCZRh23A%3D%0A)

Selecione o **funil** e a **etapa** em que o negócio será criado ou atualizado;

![Imagem 28: Selecione o funil e a etapa em que o negócio será criado ou atualizado;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389228404/2aa4ae99807fda6dc7d86cce20ac/4f25e600-15fa-4e48-8ef3-02f5ce9e75a8?expires=1786536000&signature=f83eb0a6fb3411164af2993080e25c71444db5e253ef21ddf96744e41a37cdde&req=diMvH8t8lYVfXfMW3nq%2BgViM3OqgLvssmnpdGBb7D1xw4zp2%2FB5DKeV%2Fj1pX%0AHNQCII9oIOeF0OKiUMfO6ResEQI%3D%0A)

Mapeie os campos usando as informações extraídas pelo Claude. O **título** e o **Email** são obrigatórios. Use o botão **"Inserir infos"** para selecionar os campos retornados pelo Claude, como cliente, resumo, valor\_total, produtos, responsável, contato\_nome, produto\_servico e observacoes;

![Imagem 29: Mapeie os campos usando as informações extraídas pelo Claude. O título e o Email são obrigatórios. Use o botão "Inserir…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389229711/78bc7f687f0006cbcbf9799f8fb4/9d28047d-ade4-4d2c-8907-069e07a5cc75?expires=1786536000&signature=68cffe045246696f02e9e5ab05443fdcb4673fa259bf2f25665a565e864e2d00&req=diMvH8t8lIZeWPMW3nq%2BgUNxgQNttDM%2BCbYV3LAFDkLbazZw7x%2BW5M%2B2Mqm%2B%0ANijT0laCcEQEMr9jVBUjcu0rWCo%3D%0A)

Clique em **"Finalizar Automatização"**. Prontinho. Agora, sempre que uma nova proposta for criada no Ploomes, o Claude extrairá e estruturará as informações automaticamente em seu CRM.

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi action. Para isso, é só clicar em **"Conectar Nova Ferramenta"**.

![Imagem 30: Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2389231762/b3db11ba3928b5abbf6ab0c8f91b/79f60ece-64cb-4866-bc28-f8c0f6d820f6?expires=1786536000&signature=8e140c273cd22808a5b947a78fc0a343fcb58f34097ac1b9b80f385402b5edfa&req=diMvH8t9nIZZW%2FMW3nq%2Bgd7A4Pfnk1LmduyJADqOipcy2NYQn5slDeAty%2B6f%0A9CFcwhwlXU3kB6MvAEv4AFXCucU%3D%0A)

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar. É só enviar um e-mail para suporte@pluga.co ou acessar <https://pluga.zendesk.com/hc/pt-br/requests/new>.
