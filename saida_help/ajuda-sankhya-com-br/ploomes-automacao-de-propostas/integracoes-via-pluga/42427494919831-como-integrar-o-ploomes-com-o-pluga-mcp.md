---
id: "42427494919831"
titulo: "Como integrar o Ploomes com o Pluga MCP (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427494919831-Como-integrar-o-Ploomes-com-o-Pluga-MCP-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:04:22Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12976362", "sync_hash_ff787c2d3474"]
---

# Como integrar o Ploomes com o Pluga MCP (via Pluga)

**Observação**:

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

O Pluga **MCP** **(Model Context Protocol)** é uma tecnologia que conecta modelos de IA às automações da Pluga. Na prática, ele funciona como uma ponte entre sua IA e as ferramentas que você utiliza, como Ploomes, Google Sheets, Slack e Trello.

Quando configurado, o MCP atua como o ponto de partida de uma automatização. Ou seja, você envia um comando em linguagem natural para sua IA – por exemplo, "crie um novo card no Ploomes" – e o MCP se encarrega de acionar a ação configurada automaticamente no CRM. Por exemplo:

- Durante uma reunião com um cliente, você percebe uma nova oportunidade de venda;
- Em vez de parar a conversa para acessar o Ploomes e criar manualmente o card, você simplesmente pede à IA: "Crie uma oportunidade no Ploomes para a empresa XYZ, produto W, valor R$ 1.000, etapa de Proposta. Pesquise informações sobre a empresa e adicione no campo de observações";
- A IA processa o pedido, busca dados públicos relevantes sobre a empresa e aciona o Pluga MCP, que cria o card no Ploomes com todas as informações estruturadas, permitindo que você mantenha o foco na conversa com o cliente.

Com isso, você elimina tarefas manuais, ganha tempo e a oportunidade de deixar o seu fluxo de vendas ainda mais inteligente.

---

## Requisitos

- Uma conta no [Ploomes](https://app10.ploomes.com/login);
- Uma conta na [Pluga](https://pluga.co/).
- Uma IA compatível com o Pluga MCP, como ChatGPT (conta Plus ou superior).

**Nota:** Cada automatização com o MCP conecta uma IA a uma ação de destino. Se quiser realizar mais de uma ação (como criar um card e enviar um e-mail), será preciso criar automatizações separadas.

---

## Criando uma conta na Pluga

Acesse a Pluga e clique em “**Entrar**” ou em “**Cadastrar”** se este for o seu primeiro acesso;

![Imagem 1: Acesse a Pluga e clique em “ Entrar ” ou em “ Cadastrar” se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861274/ae54e0f37731db9644c414464b52/b2437904-7bf1-41e7-aa3b-813462a66e02?expires=1786536000&signature=fcd5f00152b6ab4eeb50c842d8863233a13cc2c38d63708549f46219410d9919&req=dSgiHsF4nINYXfMW3nq%2BgQ6Ah5muEWCoeoSwQHZJsuT4j54xIdU%2B8eanNn%2BJ%0A%2BDwFzU15%2BIl7DQW1iLjGxmQUipE%3D%0A)

Na área de usuário da Pluga, clique em “**Criar Automatização**”;

![Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858898075/666689c22afc0927fe227678a8d7/d493c2fe-a220-42ef-bf48-d07e416de24b?expires=1786536000&signature=e2d78fa5fa3099ac9419e5e0441a35d4cd5c17edc95ef10c9dfa20c3bbf17d1f&req=dSgiHsF3lYFYXPMW3nq%2BgdLmS51oxJTZluqp%2BhbE9L72RZIo96DytjUZ1rdh%0ASKxkNAUkRzl%2F3rSSxvi6iBYcRY8%3D%0A)

Dê um título para a sua automatização;

![Imagem 3: Dê um título para a sua automatização;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861269/c5b87aa88c0d1ecf888bdd32874c/5fc485c9-829d-4e8d-ab7f-353704b5efc7?expires=1786536000&signature=b4788edbcb787e640794911c316507c894dc4b818c5a07923b3900788054cfbf&req=dSgiHsF4nINZUPMW3nq%2BgeYL7QiyQW1a%2BUlHCAdiVNWNws7ownZPUxrwwTSG%0A4%2FyvdFWZUW4efNvyFDsTRJtC91E%3D%0A)

---

## Conectando-se ao Pluga MCP

Na etapa de criação da automatização, selecione o **Pluga MCP** como ferramenta de origem. Escolha o gatilho "**Nova chamada MCP**" e clique em "**Salvar e continuar**". Esse gatilho é responsável por acionar a automatização sempre que sua IA enviar um comando via MCP;

![Imagem 4: Na etapa de criação da automatização, selecione o Pluga MCP como ferramenta de origem. Escolha o gatilho " Nova chamada…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861287/55b364b8dc5b4e742958880024e9/4e408661-fc5a-41bd-9a0b-53a21f0cadbe?expires=1786536000&signature=dd4950dbc887ed2f213867d0965e02a154f2c8a678a53315414cfeef0b3bfc8e&req=dSgiHsF4nINXXvMW3nq%2BgRJRB2a6xx4MF%2FSTFGBVbl7%2BLn8JEXAzCQc0xKiU%0AwFgVW9wufiBv7O%2Bw%2FEa1E%2Fc6kXo%3D%0A)

Após salvar, a Pluga gerará uma **URL exclusiva**, sendo essa URL o elo entre sua IA e a automatização configurada. Copie o link, que será utilizado mais a frente na etapa de conexão direta com a IA;

![Imagem 5: Após salvar, a Pluga gerará uma URL exclusiva , sendo essa URL o elo entre sua IA e a automatização configurada. Copie…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861281/904d2267be3100b95f5123a330f2/b9eb4079-586e-46af-9118-38d843ae881f?expires=1786536000&signature=f94587dde86f759b8c696e99d8e2460c9ed9b28e3d1dc5b3ce8cb13ffe8b7586&req=dSgiHsF4nINXWPMW3nq%2BgRdHZ4OiQgt3qfjJkcfthyq4047EUiZLkFF%2FMJ1v%0AFz8Pzq4TLxiDaOlou2cWfalgTFY%3D%0A)

---

## Conectando o MCP à ferramenta de IA

[GIF animado: Imagem 6: Conectando o MCP à ferramenta de IA](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861273/6ed13f50e468e18d532d9e9aa1d0/cd2457b3-cb56-42aa-b642-d11fcbbdf962?expires=1786536000&signature=bbfa3624ea106544d1b2bfe2815af5e4ce0ea4f31d03ab0f375e48d740cd2383&req=dSgiHsF4nINYWvMW3nq%2BgeDtRM8x801t37YMNPdLJUwYFncgzY98iiL15q%2Fv%0At%2BFIJ9K2F%2FFArLRcEivwIEgpYBs%3D%0A)

Role a janela até o final, e clique em “[Configurações Avançadas](https://chatgpt.com/#settings/Connectors/Advanced)”. Em seguida, ative o Modo desenvolvedor;

![Imagem 7: Role a janela até o final, e clique em “ Configurações Avançadas ”. Em seguida, ative o Modo desenvolvedor;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861277/73c2e2a9116c27f814e58b28edd8/c18cc3fc-5963-42aa-be95-451ad5c9f014?expires=1786536000&signature=d09da1ab4d8625ec9c61df438e711b01172e1dfdf61991940e1fb206b3539a18&req=dSgiHsF4nINYXvMW3nq%2BgR2s2qqt4sBwrxn0IfLb%2BvHn74Uf1r%2F3xWlR6eop%0ABo20Vezt8Ers%2ByopsVnKNZi9XHU%3D%0A)

Retorne à aba de “[Conectores](https://chatgpt.com/#settings/Connectors)”, e clique em **“Criar”**, ao lado de “Navegar Conectores”;

![Imagem 8: Retorne à aba de “ Conectores ”, e clique em “Criar” , ao lado de “Navegar Conectores”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861286/8bcb01fdeca0dae86a882be86269/e5444f52-70d7-4f58-be5c-e514470fb5ba?expires=1786536000&signature=317b48e1bb8a0f7f12615679b7acd39baff6980e43fccb87cdd8a9e7e7a3d06b&req=dSgiHsF4nINXX%2FMW3nq%2BgWVdZxWmMWIVmORuBrPfz7egWTaPCwWDEl2oP0E2%0Abn7V6fnE7G%2BH3TMQ2pn%2F7drknNg%3D%0A)

Preencha as informações do novo conector, selecionando um ícone e preenchendo a descrição do conector. Cole a URL de integração que você pegou anteriormente na Pluga.

Em “Autenticação”, selecione a opção **“Sem autenticação”**, além de marcar a opção **“☑ Eu confio neste aplicativo”**. Em seguida, clique em **“Criar”**;

![Imagem 9: Em “Autenticação”, selecione a opção “Sem autenticação” , além de marcar a opção “☑ Eu confio neste aplicativo” . Em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861280/eebd191bb02d1240faf6191cfe69/1aed563c-c45c-4741-8fa0-5b518c0ba1e6?expires=1786536000&signature=96c4ace2b6a00133f9ab957a8927013e6555a487c603a4a5eaf5ce1f6088afef&req=dSgiHsF4nINXWfMW3nq%2BgadTzhbBGUM9P6c%2FnF2wkQoXvxd2DR5HGn%2Fp9r8F%0AovkVQ91hACRownhyCGXWxF9kZHo%3D%0A)

---

## Conectando-se ao Ploomes

Agora, como o Pluga MCP já foi adicionado ao ChatGPT, é hora de conectar o Ploomes à sua automatização. Clique em "**Conectar nova ferramenta**" e selecione o **Ploomes**. Além disso, selecione "**Criar ou atualizar card**" como ação, ou seja, a tarefa que será executada na ferramenta destino;

![Imagem 10: Agora, como o Pluga MCP já foi adicionado ao ChatGPT, é hora de conectar o Ploomes à sua automatização. Clique em "…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861275/6ffab8e0e4c74b321d92d909984f/8f25bcd5-8864-4bad-8113-b906d4e81e79?expires=1786536000&signature=c9c4b5f93d9306203751d796a58a4347e768bafaff4655b2e5483832b56c70dc&req=dSgiHsF4nINYXPMW3nq%2BgQigjwhirgVC4H%2B2UbsJ8bsuEat3InL4tHsS5xib%0AxkHtkFp0whwGouX7JonfLIrZQNY%3D%0A)

Conecte sua conta no Ploomes, clicando em “**Conectar Nova Conta**” e realizando a autenticação. Ao criar outras automatizações, sua conta já aparecerá listada entre as contas conectadas. Caso seja a sua primeira vez conectando a sua conta do Ploomes, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 11: Conecte sua conta no Ploomes, clicando em “ Conectar Nova Conta ” e realizando a autenticação. Ao criar outras…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861283/96e9fdd8ef91cc1be266c92b431b/9f350303-732f-4dc2-b1f1-24e98dd0d460?expires=1786536000&signature=364ccc945456139582be44593679054b4a97571ba46070ddce2c5e8698a00a4c&req=dSgiHsF4nINXWvMW3nq%2BgTEM06NhpTtE1ECU6asTWDg%2F4aARGpbnGyTWGPWI%0AUR1qabEA5LyyNL6Uatf2gSBObKg%3D%0A)

No passo seguinte, selecione o **funil**, além da **etapa do funil** em que o card será adicionado ou atualizado;

![Imagem 12: No passo seguinte, selecione o funil , além da etapa do funil em que o card será adicionado ou atualizado;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861276/015035febf8fa3e5b17ec2a8a205/91501300-9015-45bc-9134-2b1669f3ed85?expires=1786536000&signature=b1fd6b6a1e5a12f1b3a1694d7c7675ee785b2d58fdfcdcf1624674050bcf2409&req=dSgiHsF4nINYX%2FMW3nq%2BgX7w9terAEIvnJmTl0cy138t297XXMnxzNAK%2BrW4%0ACqYFhd46M1I0WTck2H6tfSld7v8%3D%0A)

No passo seguinte, mapeie os campos que serão preenchidos no Ploomes. É obrigatório definir o **título do card**. Você também pode configurar campos personalizados do Ploomes, como valor da oportunidade, produtos/serviços, responsável pelo card, entre outros campos disponíveis na sua conta. Em campos de preenchimento livre, é possível que você insira dados gerados por IA clicando no botão "**Inserir infos**". Estes, serão interpretados e selecionados automaticamente pela inteligência artificial, através das informações obtidas no contexto.

No item "**Cards a atualizar**", você pode definir se os cards poderão ser atualizados ou se a automatização sempre deverá criar novos. Caso nenhuma opção seja selecionada, um novo card será criado.

![Imagem 13: No item " Cards a atualizar ", você pode definir se os cards poderão ser atualizados ou se a automatização sempre…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861278/b13793898f95d7753882f68b4305/70911147-fed8-493f-9730-f43e99e83289?expires=1786536000&signature=8ee91d97d25d3c79a36dc961577ecd468660054ebe2ab0bd3fbdce64cb4097ed&req=dSgiHsF4nINYUfMW3nq%2BgXXoXDfj4b6qPk94%2Bw%2Bzxvf8bqWW3XTt7c%2FK7x35%0ALlQw2HpMCVFAJLMP2HrYe7oCAZ8%3D%0A)

Prontinho. Clique em "**Finalizar Automatização**" e você já conseguirá acionar a sua ferramenta de IA para enriquecer os seus fluxos comerciais;

![Imagem 14: Prontinho. Clique em " Finalizar Automatização " e você já conseguirá acionar a sua ferramenta de IA para enriquecer os…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861271/6093a20fc6d60db22dad94113630/b265bbbb-612a-428b-bbe9-4fc0c5b21547?expires=1786536000&signature=566d302891bacfb1bdf4bfdcb7d498e1f782946b89615b974865ea54dd249fe9&req=dSgiHsF4nINYWPMW3nq%2BgXMYO%2FBkFmJN2e3683tqN2UVyAug4qy5yA03f%2FjC%0AYFS0ciIG1RmxHEmOkHCbPZvRMzc%3D%0A)

---

## Gerando ações no Ploomes diretamente do ChatGPT

Depois de conectar o Pluga MCP, teste se está tudo funcionando. Entre na [interface de chat](https://chatgpt.com/) do ChatGPT, e você verá que a área de conversa está agora marcada com uma borda laranja, o que indica que o modo de desenvolvedor está ativo nas suas configurações;

![Imagem 15: Depois de conectar o Pluga MCP, teste se está tudo funcionando. Entre na interface de chat do ChatGPT, e você verá que…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861268/1cc1f7b061bd2e18c706f8e69d2b/21bd8207-ca1b-4537-ae18-21074e76a1cb?expires=1786536000&signature=4b08f06554d500fddbe9caee217ee089872151483ad31afec097b4fce18e06e5&req=dSgiHsF4nINZUfMW3nq%2Bgfdugy7kavIYEuW2draw%2BjQA7KSP2Etn4k1Ouhuu%0A%2BOZGQHkcB4lIR0%2Fw6XN7ACZ2yco%3D%0A)

No campo de mensagem, clique em **“+”** e selecione o conector que você nomeou. Pergunte ao ChatGPT: “O Ploomes está conectado?”, e ele vai confirmar, caso esteja tudo certo;

![Imagem 16: No campo de mensagem, clique em “+” e selecione o conector que você nomeou. Pergunte ao ChatGPT: “ O Ploomes está…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861279/f64a568c9fd36e48542aac8374d9/058ec297-8bdd-4b6b-bd20-3fd196e21634?expires=1786536000&signature=3da801b94a47b22863a95cf0a0316ad26ce77b027e8f3411830778da1dec8236&req=dSgiHsF4nINYUPMW3nq%2BgQ%2FawfQn%2FNdcNNT1bXoHUrN%2FHdosit6UTLvkl6R2%0ATMBknRTd16O4%2BBSPufbywKmsrxs%3D%0A)

Em seguida, insira o prompt que irá trabalhar em sua automatização. Por exemplo:

```
Quero criar uma nova oportunidade no Ploomes. O nome da empresa é [NOME DA EMPRESA]. Pesquise informações atualizadas sobre essa empresa — como setor de atuação, tamanho, principais produtos, notícias recentes e dados de contato públicos — e adicione esse contexto no campo de observações do card. O valor estimado da oportunidade é R$ [VALOR] e o produto de interesse é [NOME DO PRODUTO].
```

![Imagem 17: Em seguida, insira o prompt que irá trabalhar em sua automatização. Por exemplo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861270/30be9821a0e7bdbb438deca0d00b/c2f07be6-b6cf-41b2-8c84-fbd2ee1983eb?expires=1786536000&signature=548efcefd26f75627a5a3cee3753487939f8c00637f94b0996b789719126614e&req=dSgiHsF4nINYWfMW3nq%2BgWAs6w8TNQRnZYVImoMkgwj5F6cueFsZTE8wnLw9%0AVp10gUpVHBSsGNOehrKFtM5B%2Fs8%3D%0A)

**Leve em consideração que o ChatGPT não realiza buscas na web quando há um conector selecionado.** Por isso, deixe sem nenhum conector momentaneamente, caso queira realizar algum tipo de pesquisa.

Após ter o retorno adequado, selecione novamente o conector e envie o comando para criar o card no Ploomes;

![Imagem 18: Após ter o retorno adequado, selecione novamente o conector e envie o comando para criar o card no Ploomes;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1858861282/477b931c403352746921369d7100/0655ffca-bf8b-4e6b-9281-01efc5390705?expires=1786536000&signature=761748ae341cea9649a24f9d21872abe4c1bc55a05534b09153b84c536bc4921&req=dSgiHsF4nINXW%2FMW3nq%2BgUSrlhAGvQn3YV9nCIQfup73UzT1zD6Qfuif%2FMK3%0AFREZbLMo8dlLvXNLnv7IMI2%2FsJA%3D%0A)

Na primeira vez que você utilizar o recurso, o ChatGPT vai te pedir para confirmar a ação. Clique na opção "**Lembrar nesta conversa**" para que ele não repita a pergunta a cada comando.

Em seguida, clique em "**Confirmar**" e a ação será executada diretamente no seu Ploomes.

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização **multi action**. Para isso, é só clicar em **“Conectar Nova Ferramenta”**.

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
