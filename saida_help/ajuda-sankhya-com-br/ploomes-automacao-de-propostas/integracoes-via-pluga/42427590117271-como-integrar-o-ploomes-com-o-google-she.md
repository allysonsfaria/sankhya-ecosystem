---
id: "42427590117271"
titulo: "Como integrar o Ploomes com o Google Sheets (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427590117271-Como-integrar-o-Ploomes-com-o-Google-Sheets-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:05:27Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9011073", "sync_hash_d04862957a40"]
---

# Como integrar o Ploomes com o Google Sheets (via Pluga)

**Observação**:

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

A **cada linha criada ou atualizada** no Google Sheets, criar ou atualizar um cliente;

A **cada nova linha adicionada** no Google Sheets, criar ou atualizar um card no Ploomes;

Ou então, a cada **proposta criada** no Ploomes, inserir uma nova linha (ou múltiplas linhas no caso de oportunidades com mais de um produto/serviço), dentre outras opções.

## Requisitos

- Uma conta no [Ploomes](https://app10.ploomes.com/login);
- Acesso ao [Google Sheets](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fcreate&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fcreate&ifkv=AdBytiPq6113sDYR7G5Aatnec5iqr0FZstBdjyDKEmNRlvOFswAA1DCvyUR48PU9Eo8PbrL4ICkdiw&ltmpl=sheets&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1660369125%3A1752518826683071);
- Uma conta na [Pluga](https://pluga.co/).

---

## Criando uma conta na Pluga

Acesse a Pluga e clique em “**Entrar**” ou em “**Cadastrar”** se este for o seu primeiro acesso;

![Imagem 1: Acesse a Pluga e clique em “ Entrar ” ou em “ Cadastrar” se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841184/919604997643da8e61d9cea1d60a/93a688f8-968b-4d41-b02a-e0a653e466f8?expires=1786536000&signature=6ffdb70924e48b8179f405a4d0b53dc89ec6813dded35254cfa09ec6adaa8c77&req=dSgnFcF6nIBXXfMW3nq%2BgdcvfhcSzywupFEfmPN%2Beta2PnRkpR0mgg6ItCjk%0AqZUgfAAmZuAEBAyrMSU9hy%2Bp5tE%3D%0A)

Na área de usuário da Pluga, clique em “**Criar Automatização**”;

![Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841179/96776b6f21e8eea8b8d82c9f97e1/AD_4nXfUVzHLaSn7LsIvZB9QpT0696aGNJEbOB1PxNbKGIXrdOwXRGNk3BPghnlrUl_rn4RicYNbh1_gJ68aS5nxw3GFMNyusloliCJgB18Rv0enM4hOyMPZQ54U-lRTATRPX-OZ3U6ZsQ?expires=1786536000&signature=a92266b99b5f1eaa09efef2c30d8b69e1a558bde8e856d790b5ee317af2261e3&req=dSgnFcF6nIBYUPMW3nq%2BgRwoKEneB5%2B1SC%2FZuslt45pJ%2BFQon2Hu575XG2ur%0As5QxmS%2B43pVF%2F6f0zglEDKSBShM%3D%0A)

Dê um título para a sua automatização;

![Imagem 3: Dê um título para a sua automatização;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841180/c03d85a3af4a79de4ccddc51005f/2283e5a0-28f0-4730-be1d-b698d7c95c03?expires=1786536000&signature=19eeeb1b03805e72242f0a9dd686404a50e5d6205b6f3a51f9fa87431636aea2&req=dSgnFcF6nIBXWfMW3nq%2BgV4LRrj499Wbdsu9hz%2FjmYDXCCoUbHiBUPLWPDbo%0ArazL8kiURCzovLJAkoVvETHnBRM%3D%0A)

## Criando uma integração entre Google Sheets (origem) e Ploomes (destino)

Selecione a ferramenta que dará início à automatização. Neste caso de uso, vamos selecionar o **Google Sheets**. Escolha também o gatilho, ou seja, o evento na ferramenta de origem que dará início à sua automatização. Neste caso de uso, escolhemos **“A cada linha criada/atualizada”**. E em seguida clicamos em **“Continuar”**;

![Imagem 4: Selecione a ferramenta que dará início à automatização. Neste caso de uso, vamos selecionar o Google Sheets . Escolha…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841183/2211f744c40fb45a2a2513825c7c/92091e2d-a6c0-44c7-a203-518bc31c2205?expires=1786536000&signature=513131615aa4999e988a90d2657017f456ae331b5a3d52781ceb0a5f7903caeb&req=dSgnFcF6nIBXWvMW3nq%2BgU1%2FnJ8MEQcNM76h2sFoKqqlDsRqqlif1XiE2wpQ%0AccXo0KHL25R7YsO8%2FkzxElgXzbQ%3D%0A)

A etapa seguinte é a de autenticação. É nela que você vai conectar a sua conta do **Google Sheets**. Esse processo é realizado apenas uma vez, dessa forma, ao criar outras automatizações com o Google Sheets, sua conta já aparecerá listada entre as contas conectadas. Após a conexão, clique em **“Salvar e Continuar”**;

![Imagem 5: A etapa seguinte é a de autenticação. É nela que você vai conectar a sua conta do Google Sheets . Esse processo é…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841190/aa8c9d49cb5d7c8d9ed9cde3d445/c218c828-1642-48c8-bd8f-7cdcb81fd11c?expires=1786536000&signature=d3b75fa9183f26ba1bc1ac36cedc80b5e96c0a38437b006f1177c8b205a36d60&req=dSgnFcF6nIBWWfMW3nq%2BgTReZcHM4ydwJM9xlB6hAsTWDrlOO2vNXABMtzMK%0A2a9gBdnmQDhp4czA9ymhWw0BO4I%3D%0A)

Ajuste a planilha que será utilizada e a aba de onde os dados serão captados, inserindo na primeira linha, em cada coluna, as informações de cabeçalho que você deseja utilizar. Feito isso, está tudo pronto para seguir com a sua integração. Em seguida, clique em **“Continuar”**;

![Imagem 6: Ajuste a planilha que será utilizada e a aba de onde os dados serão captados, inserindo na primeira linha, em cada…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841195/61b7d4d3cb59d4b38e79ef25555c/317c1a72-0536-4d4b-89bc-03b14ca3eac0?expires=1786536000&signature=0b386723adda9712bc8bb1b07c5eb646abc121352b0ef0da98c1d1bda046e754&req=dSgnFcF6nIBWXPMW3nq%2BgaQaNAb445XWpNw2ch6cEGKXYbj98EMlNyX7Q8oP%0ATxQjtyZN7xQH2uB32I6%2B28yiWzY%3D%0A)

Clique em **“Conectar Nova Ferramenta”** e selecione o **Ploomes**. Logo após, escolha a ação que será realizada, ou seja, a tarefa que será executada na ferramenta de destino. Para seguir com este caso de uso, vamos escolher **“Criar ou atualizar cliente”**;

![Imagem 7: Clique em “Conectar Nova Ferramenta” e selecione o Ploomes . Logo após, escolha a ação que será realizada, ou seja, a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841177/f1fa783ffd3867875c8ae5ebca46/07035894-afc5-44cb-8bde-7cf03a8720dd?expires=1786536000&signature=b4513b1b40c875734655495b0cf94deea8589703378c41c925e4521c4eb4dd0b&req=dSgnFcF6nIBYXvMW3nq%2BgQJfK5U6IHCiTw1Xb2D8Ahw8bbXyJ5jga9KZ9ieN%0AsriNblGyPUdsswC3%2BTlS1sY2Ufs%3D%0A)

Conecte a chave da conta do Ploomes que deseja integrar. Esse processo também só precisa ser feito uma única vez, já que nas próximas automatizações sua conta já estará salva. Caso não saiba como encontrar sua API Key, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga os passos indicados;

![Imagem 8: Conecte a chave da conta do Ploomes que deseja integrar. Esse processo também só precisa ser feito uma única vez, já…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841178/8cf3fd4f65f1c485159d701aff04/a6e153eb-fc43-4359-8b04-a1da6214b5d7?expires=1786536000&signature=2d5c2060086c2da578539afa759d991081d9d78e839e358fe43cd24e119f44a0&req=dSgnFcF6nIBYUfMW3nq%2BgQXWBHDOuNzvPAgI0%2FtjZRiijhXReyCP3tmeDKNe%0ALwLSkMFLdvS2WHM1mUS7FcKht2k%3D%0A)

No próximo passo, você pode inserir dados coletados do Google Sheets, como **nome** e **e-mail**, clicando no botão **“Inserir infos”**. No item **“Atualizar pessoa baseado em”**, um novo cadastro de pessoa será criado, a não ser que encontre dentro das opções de **CPF,** **E-mail** ou **Nome** um pré-cadastro existente.

![Imagem 9: No próximo passo, você pode inserir dados coletados do Google Sheets, como nome e e-mail , clicando no botão “Inserir…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841182/ed0d8284e8cef6b46fac96de2c16/2eeaf8c0-bfec-428b-b653-649f0d0b525c?expires=1786536000&signature=e0f4065b124e0e759f6cac788e8ac7e764163969882290864c52bfea2ef527c1&req=dSgnFcF6nIBXW%2FMW3nq%2BgX57bqksI09elKSS1CT5tZJ70FPwA99AZKqP9RP%2F%0A%2B8Z0envtwXcPMavRIsijnlp%2Butw%3D%0A)

Prontinho. Agora, quando uma linha for criada ou atualizada em uma planilha do Google Sheets, um cadastro de cliente será criado ou atualizado no Ploomes.

![Imagem 10: Prontinho. Agora, quando uma linha for criada ou atualizada em uma planilha do Google Sheets, um cadastro de cliente…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841191/2d3e78710282f7d04e239c78dbc7/58e1ce05-d56c-4b3c-9e63-94785e65a70b?expires=1786536000&signature=05726ef1efb5a2af98ebbd93b75de53f1ee3b7edf77c70577f0ab2bda8253a42&req=dSgnFcF6nIBWWPMW3nq%2BgRM0U08MerYeCq7kZiOYnJwoEcnoD9xZxfIIlUhM%0AcoH9TObP9ZvcOv88kqfSaFlGjn0%3D%0A)

## Criando uma integração entre Ploomes (origem) e Google Sheets (destino)

Agora, trabalharemos um caso de uso em que o Ploomes é a ferramenta de origem. Escolheremos também o gatilho, ou seja, o acontecimento na ferramenta que dará início à sua automatização. Neste caso de uso vamos selecionar “**Proposta criada**”, e clicar em “**Continuar**”;

![Imagem 11: Agora, trabalharemos um caso de uso em que o Ploomes é a ferramenta de origem. Escolheremos também o gatilho, ou seja,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841181/03d3fcb5f10d2bbabe18ee6d7e00/bed8c475-b051-4033-ba7e-7bdadc5a1480?expires=1786536000&signature=28e913a9fc8fa688cbc5351665cecfb054c9e394c4d18580fc76cb0ddab1bc68&req=dSgnFcF6nIBXWPMW3nq%2BgURWFlX3rKRlUajDjRU3Uenv9j3LUi9Cj1OywLth%0AALJ9lpp7if20mARfYdzvtZZhY60%3D%0A)

Conecte sua conta no Ploomes, clicando em “**Conectar Nova Conta**” e realizando a autenticação. Ao criar outras automatizações, sua conta já aparecerá listada entre as contas conectadas. Caso seja a sua primeira vez conectando a sua conta do Ploomes, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 12: Conecte sua conta no Ploomes, clicando em “ Conectar Nova Conta ” e realizando a autenticação. Ao criar outras…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841197/5f5be831006f804478e3dd5ff306/e9244787-6dd7-44fa-b09b-d0ae23a256ba?expires=1786536000&signature=31207ceede79599ac53ce8c84ca7e6fe5d3ffd642bd02b02460879016ae29ce8&req=dSgnFcF6nIBWXvMW3nq%2Bgf0R%2BtD0ysMCu8S7mxFL3EH7uPcAC84sDHlylWcQ%0AeoCZVxe3ktMVmUSawDDtBe7I9ys%3D%0A)

Caso queira, você também pode **criar filtros** para a automatização usando como critério qualquer um dos campos do Ploomes. Você pode adicionar múltiplos critérios a um filtro, e a forma como eles se relacionam determina o comportamento da sua automatização. Para adicionar mais de um critério, utilize os botões **“E”** ou **"OU”**.

Para nosso exemplo, iremos considerar apenas leads que estejam em um pipeline específico do Ploomes (“Pipeline:Nome = Pipeline da Pluga”) e que o total de produtos negociados somem R$1.000,00 (“Produtos: Total da venda >= 1.000,00”). Em seguida, clicar em “Salvar e Continuar”;

![Imagem 13: Para nosso exemplo, iremos considerar apenas leads que estejam em um pipeline específico do Ploomes (“Pipeline:Nome =…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841192/7ae6dc0699351929734a1418a5e5/a13ba98d-1629-413f-96a6-1b71dc2ae00c?expires=1786536000&signature=32daa6b6053528f4d94e8d27bd99d30167da77ea8deb0e0de51564fbeb27c8b7&req=dSgnFcF6nIBWW%2FMW3nq%2BgTXCTVf9b3c0NC%2F5eAdJrMgYkw51HwJVuFDTaiBz%0AvdnNJoqyg7K8VQqmqnKEgYwYhRc%3D%0A)

Com a sua conta da Ploomes configurada, clique em **“Conectar Nova Ferramenta”**;

![Imagem 14: Com a sua conta da Ploomes configurada, clique em “Conectar Nova Ferramenta” ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841196/300ac8bc644d24e54a8a45a2158f/774781ed-1439-42e1-bd12-d2ec89f41b46?expires=1786536000&signature=720f9aec2dc8c0c29036a40dfc3cd355801144dbc0cb80930ba8c8f3a1905ece&req=dSgnFcF6nIBWX%2FMW3nq%2BgeDH%2FKONPwi9Gf2HVp1iCB33ETOnplww9wVpEw0d%0AwtAEesk%2FsOjyi9cyTsgEwBq5PI4%3D%0A)

Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “**Google Sheets**” e uma ação, ou seja, a tarefa que será executada na ferramenta de destino. Neste caso, selecione **“Inserir múltiplas linhas em planilha (apenas para vendas com mais de um produto)”** e clique em **“Salvar e Continuar”**;

![Imagem 15: Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “ Google Sheets ” e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841200/99b1f2eef240609a2ebe2586cf0a/5e7127bc-b884-4823-8493-a4a1a486df04?expires=1786536000&signature=8123adaba72933026b9495ed04d1b999ae12d7e866dedaf94493228eab602644&req=dSgnFcF6nINfWfMW3nq%2BgeXZQD%2Br%2BS7AWlXC9H2sc7Y%2FNaw1K%2B0YJyAP6z2D%0ArjP5XPblwL9Gz6FmdlOID5NCkTs%3D%0A)

Em seguida, conecte-se à sua conta associada ao **Google Sheets**, e clique em **“Salvar e Continuar”**;

![Imagem 16: Em seguida, conecte-se à sua conta associada ao Google Sheets , e clique em “Salvar e Continuar” ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841187/8402ad12c4e27ec8e27eb5853fdd/4acb9daf-bb50-444e-b6c2-7d111cb3bb29?expires=1786536000&signature=8ecc0155a6e8de3ba51bdeed88ab445360717649157ee605a33e2f55c99cb5f1&req=dSgnFcF6nIBXXvMW3nq%2BgZsYeoDni06TbDcTqCcAxH1e0548UUOLdj7aK2L%2B%0A0ElSuc%2BPr%2FpBi1XtkNiLUTFhMnM%3D%0A)

Selecione a **planilha**, além da **página** onde a automatização enviará informações para atualizar ou criar uma nova linha. Certifique-se que a sua planilha esteja apta para funcionar com as automatizações. Para isso, é importante que contenha algum dos seguintes itens, categorizados em suas respectivas colunas:

- **Item – nome**
- **Item – quantidade**
- **Item – preço**
- **Item – código**

Caso não existam colunas que correspondam, elas serão criadas automaticamente para você, e os dados de nome, quantidade, preço e código dos itens serão inseridos nessas novas colunas. Apenas estes campos de item variam de linha para linha. Os demais dados se repetem para cada item registrado. Em seguida, clique em “Salvar e Continuar”;

![Imagem 17: Caso não existam colunas que correspondam, elas serão criadas automaticamente para você, e os dados de nome,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841189/6908f0825cb01f21aedda4812314/9031b397-29bb-4022-8e9c-de02b3e1dead?expires=1786536000&signature=299ed983d45bc8d655c6a9f70b826f802f170ad025709895fb69149cb22cec20&req=dSgnFcF6nIBXUPMW3nq%2Bgc2FSukA7Rs0gSKYLc2nMq8HVQyMaaHCSWQVDAJ%2F%0AQryypnIVM050GiwcIbXtjN93r2E%3D%0A)

No mapeamento clique em **“Preencher campos com IA”** e as informações serão inseridas automaticamente! Confira se fazem sentido para a sua automatização. Caso não façam, clique em “Inserir Infos” e selecione a melhor opção;

[GIF animado: Imagem 18: No mapeamento clique em “Preencher campos com IA” e as informações serão inseridas automaticamente! Confira se fazem…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803853822/048c9b0cca83908efd87359e7a38/forms+externo+cria%C3%A7%C3%A3o2.gif?expires=1786536000&signature=ab7f3bfcffa7ad9b1e8853273b81d1d0672bae463ebb848da1ac2676310fcc38&req=dSgnFcF7noldW%2FMW3nq%2BgZYBDrSbTLiC5xbEUXBARCQa%2FG3eWM6pK360jYz1%0Aw555J3bV2WBUicnHIaJXJ6sFIoo%3D%0A)

Escolha com qual **lista de múltiplos itens** você deseja trabalhar nesta integração. Também, selecione os itens que serão preenchidos em sua planilha. Em seguida, clique em “Salvar e Continuar”;

![Imagem 19: Escolha com qual lista de múltiplos itens você deseja trabalhar nesta integração. Também, selecione os itens que serão…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841188/78f5e63273195d3f5db7f7f2506e/29fa72a1-abc5-4b78-8ae7-1559e79d1000?expires=1786536000&signature=3e03164cd672fc9b4578c5385db6771b5187f64ffdd4cee2d37c19ca61d39731&req=dSgnFcF6nIBXUfMW3nq%2BgWRUIbzANsRwaMINI9pGqikFC%2FnHk2UYYMrU8Y5f%0AX8ruI%2F%2FZR9AMRhfjuON2%2FD0AMS4%3D%0A)

Depois de preencher todas as informações necessárias, é só clicar em “**Finalizar Automatização”**.

Prontinho! Agora, toda vez que uma oportunidade for ganha no Ploomes, as informações dos produtos negociados serão preenchidas em uma planilha.

![Imagem 20: Prontinho! Agora, toda vez que uma oportunidade for ganha no Ploomes, as informações dos produtos negociados serão…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1803841199/5eef8db25d9bf4771a67b51d12da/79b4f47b-91e9-413e-826d-0489aef2e945?expires=1786536000&signature=9c80bc95b4869c7f37d557e28bceee7d58ed229ec595a3520b3edc11ff199de0&req=dSgnFcF6nIBWUPMW3nq%2BgbfutumtVb4XeCbxrJ%2FOnztbuAVTjrRZaz6pfjv0%0AkQpU62ppyqtpC6qua1cQl1ZYUAY%3D%0A)

Se preferir, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização **multi action**. Para isso, é só clicar em **“Conectar Nova Ferramenta”**.

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
