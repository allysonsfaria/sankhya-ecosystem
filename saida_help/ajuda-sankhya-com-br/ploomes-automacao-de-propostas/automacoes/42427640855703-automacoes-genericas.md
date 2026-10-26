---
id: "42427640855703"
titulo: "Automações genéricas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427640855703-Automa%C3%A7%C3%B5es-gen%C3%A9ricas"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-11T16:14:05Z"
rotulos: ["sync_hc", "ploomes", "ploomes_9786685", "sync_hash_72db2cc8efd7"]
---

# Automações genéricas

As automações permitem conexões entre processos, seja preenchendo dados, criando novos negócios, criando tarefas de alerta com condições de data...

Também permitem que sejam feitos cálculos automáticos dentro do sistema, atribuição de responsabilidade e outras facilitações.

## Como configurar automações

Para acessar o módulo, clique em [Administração - Automações](https://app10.ploomes.com/administration/automations)

![Imagem 1: Para acessar o módulo, clique em Administração - Automações](https://downloads.intercomcdn.com/i/o/1194618921/bcbb9a64bc54078afb01ec49/image.png?expires=1786536000&signature=cde92cc84d7427c1561124eff4bba98b1a05390c11e5d13a8bacc665ee73c392&req=dSEuEs9%2FlYhdWPMW3nq%2BgVTfwdXLCvQZ72pitGB7RqbBnxmlkH9SKDhBTn5K%0AAyKqQZA7GUFY1F13CX%2BhbuG%2FoBw%3D%0A)

A **Entidade** da automação é onde vai acontecer o **gatilho**. Se, por exemplo, quero preencher um dado de cliente quando um negócio for ganho, a entidade será "Negócio", pois independente da ação estar preenchendo dados de cliente, o gatilho foi um negócio.

![Imagem 2: A Entidade da automação é onde vai acontecer o gatilho . Se, por exemplo, quero preencher um dado de cliente quando um…](https://downloads.intercomcdn.com/i/o/1194619416/5a030b80e2d07a97be6f24d2/image.png?expires=1786536000&signature=16c89e0e3f8305635ebea8c936a94673bae4277ac0a272fb72783697958406bf&req=dSEuEs9%2FlIVeX%2FMW3nq%2BgT2i5HixfGDEYdniVgXvnwnArukty7wkFIfrUtBt%0AVj2%2BRDlK9dzYJ8c%2B0n0oVZrVR8s%3D%0A)

Para configurar uma automação, selecione uma entidade e clique em "Nova automação".

São 4 configurações básicas:

## 1. Descrição

Preencha o título da automação com uma descrição breve do que ela faz. É importante documentar bem a automação, para que facilite a manutenção da conta no futuro. Uma boa prática é escrever qual é o processo de qual essa automação faz parte.

Exemplo: "VENDAS | Alocação de novo cliente SP"

## 2. Gatilho

![Imagem 3: 2. Gatilho](https://downloads.intercomcdn.com/i/o/1152288932/cd7cd3640569ceb2e567a60d/image.png?expires=1786536000&signature=7acb8d6a7082e55f5b4238ccfe3679efd78ced0d3f07f02c78f72b576e215c78&req=dSEiFMt2lYhcW%2FMW3nq%2BgbyXC5KD8mfUDG4smftb2EqC7Y%2BBwEVUxbPbDzj9%0ABZFPys8W03GFLhlrRHOOix%2Bl%2B%2Bw%3D%0A)

"Gatilho" quer dizer "Quando essa automação vai rodar?".

As opções variam de entidade em entidade, dependendo do comportamento de cada funcionalidade do sistema. Os gatilhos disponíveis são:

## Quando o item for criado

Dispara na criação da entidade selecionada.

## Quando o item for editado

Esse gatilho executa a automação sempre que a **entidade selecionada for editada**.
Você pode configurá-lo de duas formas:

#### 1. Sem escolher campos específicos

A automação será disparada **toda vez que qualquer campo do item for alterado**.
Use essa opção quando qualquer modificação já justificar a execução (ex.: atualizar o status quando qualquer campo do negócio for editado, mudar o responsável quando qualquer campo do cliente for editado, editar um valor etc.).

#### 2. Com campos específicos

Você pode escolher **entre 1 e 4 campos** que servirão como filtro para o gatilho.
Nesse caso, a automação será disparada **somente quando um desses campos for editado**.

Exemplo: se você selecionar os campos Status e Responsável, a automação rodará sempre que **um OU outro** for alterado.

⚙️ **Importante**: o operador usado entre os campos é sempre **“OU”**, ou seja, basta **um** dos campos selecionados ser alterado para que a automação seja executada.

![Imagem 4: ⚙️ Importante : o operador usado entre os campos é sempre “OU” , ou seja, basta um dos campos selecionados ser alterado…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1764256746/06721fb3a40561087a36bfea9488/image.png?expires=1786536000&signature=94050aca52a21efba5f93e1160ccf958d2288d847c357b44a0991d6ae8962a76&req=dSchEst7m4ZbX%2FMW3nq%2Bgadrb7WUvlgOV1erlmtIJXUSn6V3XcXanlXsyJDW%0AIO6owhs752rjI5LFlCus64y3DCk%3D%0A)

## Quando o item for excluído

Dispara na deleção da entidade selecionada.

## Quando o negócio for ganho

Dispara quando um negócio no funil é marcado como 'ganho'. É recomendado filtrar por funil, dependendo da necessidade.

## Quando o negócio for perdido

Dispara quando um negócio no funil é marcado como 'perdido'. É recomendado filtrar por funil, dependendo da necessidade.

## Quando o negócio for reaberto

Dispara quando um negócio no funil que está ganho ou perdido for reaberto. É recomendado filtrar por funil, dependendo da necessidade.

## Periodicamente

As automações periódicas rodam para todos os itens da entidade que se encaixam com o filtro configurado, então é importante filtrar para que não rodem desnecessariamente, pois podem causar uma fila de disparos ou uma alteração em massa indesejada. **Reforçamos que não existe reversão de edições no Ploomes**, então uma automação periódica que roda para todos os negócios zerando o valor, por exemplo, pode causar um problema imenso na conta.

![Imagem 5: As automações periódicas rodam para todos os itens da entidade que se encaixam com o filtro configurado, então é…](https://downloads.intercomcdn.com/i/o/1152298845/cfa3d835beccd8fd4ed5bd86/image.png?expires=1786536000&signature=0836148316b69e5af9f3c8559712d8b252b7a568acfdace071b95e618bc32eb0&req=dSEiFMt3lYlbXPMW3nq%2BgY%2B%2FtHVIaSY6QvUL2naCjy4WWjl597oxK9UhLO5V%0AQrEPe%2Bk4J%2FH1cHR1NzpM1%2Fw0vqI%3D%0A)

Para configurar a automação periódica, definimos se roda a cada x dias, semanas, meses ou anos - e a data e hora da primeira execução.

Também recomendamos a configuração de uma [trava](https://sankhya.zendesk.com/hc/pt-br/articles/42427675341079#h_3b48a437db) nas automações periódicas

## Quando a proposta/venda/documento for aprovada ou reprovada

Esse disparo é referente ao fluxo de aprovação interno no Ploomes. Quando um aprovador der seu parecer, a automação será disparada.

## Quando a proposta/venda/documento for aprovada ou reprovada (Online)

Esse disparo é referente ao aceite pelo cliente via Link Web. Quando o botão 'aceitar' ou 'recusar' for clicado no link web, a automação roda.

## Quando a tarefa for finalizada

A automação roda quando uma tarefa for finalizada.

## Quando a tarefa for reaberta

A automação roda quando uma tarefa finalizada é reaberta.

## 3. Filtro

Os filtros limitam quais itens serão afetados por uma automação. São a parte mais importante da automação, e devem ser configurados com cautela.
[Clique aqui para aprender a paramentrizar filtros.](https://sankhya.zendesk.com/hc/pt-br/articles/42427447489815)

Abaixo, alguns exemplos de filtros e gatilhos:

**Dispara para os clientes que foram criados a exatamente 120 dias**

![Imagem 6: Dispara para os clientes que foram criados a exatamente 120 dias](https://downloads.intercomcdn.com/i/o/1167151397/95acc9ddf31e3c44bb9ed2e0/image.png?expires=1786536000&signature=bf13fa4b1cc8f1c6dfab6a75b20f4cc31511f2d218aa9c138af3dae9d2aa94e3&req=dSEhEch7nIJWXvMW3nq%2BgQx0j1NokYMEtGEy9ypRH1BRxmEDnrGz6m9XRHMT%0Auvve1eJ6Ax17%2B6CNaZu7eLCmRFk%3D%0A)

**Dispara para vendas com valor maior que R$50.000**

![Imagem 7: Dispara para vendas com valor maior que R$50.000](https://downloads.intercomcdn.com/i/o/1167152997/f55015a36638a304fc7f9b23/image.png?expires=1786536000&signature=6e0e9477b78c1a788ba06dc377865d53335bc1ca3c034b2e7df82c50ee5243ca&req=dSEhEch7n4hWXvMW3nq%2BgZqqFgCgg7QN%2FxEMwVipPKHMXfnMOxfM0ek8r5Jl%0AqR72xed4iXJIf1iSczd9XzsIT9w%3D%0A)

**Dispara para negócios ganhos por uma equipe específica no funil de vendas**

![Imagem 8: Dispara para negócios ganhos por uma equipe específica no funil de vendas](https://downloads.intercomcdn.com/i/o/1167154483/406ce84a5a92390a0d358af5/image.png?expires=1786536000&signature=3afc613a4dad028d643b89ded5b765fc3f6bd18bafc373c27c31b11b2c341a00&req=dSEhEch7mYVXWvMW3nq%2Bgdohw5SUL9k7cn4Zhbj8kwLTFxEqrkK5hQd3harf%0AVqZGWW%2FXx8jukEo2KoooWtQTHqQ%3D%0A)

## 4. Ações

As automações podem ter mais de uma **ação**.

A Ação da automação define o que vai ser executado, e todas as edições são referentes ao item do **gatilho.**

![Imagem 9: A Ação da automação define o que vai ser executado, e todas as edições são referentes ao item do gatilho.](https://downloads.intercomcdn.com/i/o/1152344171/f861bc7100b56ba7ace79c93/image.png?expires=1786536000&signature=c7781f42e96e7900c2308b41364f2c6380ba333e1783a013d423d63f8316129a&req=dSEiFMp6mYBYWPMW3nq%2BgWhk55vRRn15pLD4pLAqscnSB%2BFermHWuEyY0KA%2F%0AOsaJ7N3ppeNABOEdRC3ikOeehGI%3D%0A)

### Editar dados

Edita um campo especificado.

Primeiro, selecionamos o campo a ser editado:

![Imagem 10: Primeiro, selecionamos o campo a ser editado:](https://downloads.intercomcdn.com/i/o/1152390307/ac8fd38daf0f131a0f89b9a3/image.png?expires=1786536000&signature=ca4da32ebc57fe61a8b99b5b89fd8205a6245c0bae12b9f5e343544f742d58b1&req=dSEiFMp3nYJfXvMW3nq%2Bgf8q3Zj3jxzqvYz%2F4RmtY5EfrSCHVGPC9A4l%2FoFg%0AspxVGlrRzhA1DdndCBD70WmgzEE%3D%0A)

Depois, selecionamos o tipo de preenchimento:

![Imagem 11: Depois, selecionamos o tipo de preenchimento:](https://downloads.intercomcdn.com/i/o/1152391380/7ab814d80c1e6fc71e12c205/image.png?expires=1786536000&signature=bd603d0ec01954b084f0e33129870466ac942d6c70676b15303f2ca19a935e93&req=dSEiFMp3nIJXWfMW3nq%2BgTpnJ3nVxAGZd813qnx%2Bmd5E5uvV%2BzV1dhWK8WhU%0Amp7wU4VOJDggxRBQNxK%2FBEsKtAo%3D%0A)

em "Valor estático, preencho um valor fixo

![Imagem 12: em "Valor estático, preencho um valor fixo](https://downloads.intercomcdn.com/i/o/1152391760/00ca78babf8deb7e92cb1bff/image.png?expires=1786536000&signature=6c42d708d92533fbd4fdce5d4c05091c386c0789a31f7b6b2f63441ac1efe59f&req=dSEiFMp3nIZZWfMW3nq%2BgSgroD9vlsSBNatHuumHRuL52G9QLw9LuC0auT5j%0A%2FJYxNRm4reEDmUO2QgPx8NeqfQg%3D%0A)

Em "Puxar valor de um campo", seleciono o campo que vai ser puxado:

![Imagem 13: Em "Puxar valor de um campo", seleciono o campo que vai ser puxado:](https://downloads.intercomcdn.com/i/o/1152392341/25ea766c28469403e9941deb/image.png?expires=1786536000&signature=a72f982c5b5f274c30f5352b89d48425f3f4ab4a5075ecdde276f4e96c64cfc5&req=dSEiFMp3n4JbWPMW3nq%2BgYl5B8%2FPk3M%2Bfv7Vt97NoukZT%2FKUqkogguGNrqzz%0AC79sCEJF3UAGkfVteZiso29lsgQ%3D%0A)

E em "Fórmula", configuro uma fórmula em JavaScript para definir o valor resultante:

![Imagem 14: E em "Fórmula", configuro uma fórmula em JavaScript para definir o valor resultante:](https://downloads.intercomcdn.com/i/o/1152393090/4353dbe722f872c654319177/image.png?expires=1786536000&signature=7f207abe9835a6ee24925ffe4c88947d83cc088d63136d1ebc7c8249afa598b6&req=dSEiFMp3noFWWfMW3nq%2BgR7natvfEJGIgyi%2F4VDvYkXEKvmcxwI4PTZUXwPo%0AjfAfWMB0iiAO%2F8tX5cYCN3bZBz8%3D%0A)

![Imagem 15: E em "Fórmula", configuro uma fórmula em JavaScript para definir o valor resultante:](https://downloads.intercomcdn.com/i/o/1152393491/0ff47b1d4494542f164f2b0f/image.png?expires=1786536000&signature=85856f2c4b1a389e20b671fe107ca6ae5764f8f499ed97160ccd504a93669307&req=dSEiFMp3noVWWPMW3nq%2BgfxuWKeX68yYg2su1g2Y22BEeIF1F0MVWMc5oltv%0AvPVMLbKtM6HtFxYf%2FJAQ2EtbVB4%3D%0A)

### Enviar e-mail

Dispara um email para o remetente selecionado.

![Imagem 16: Dispara um email para o remetente selecionado.](https://downloads.intercomcdn.com/i/o/1152394720/cf3ea557da3698c19bd1b945/image.png?expires=1786536000&signature=8cc546708c32be2df1e95ac1237a1737e438cf9ce0700de671bd915cdd25e62b&req=dSEiFMp3mYZdWfMW3nq%2BgVTQpaPldwFwZcfKoB9ScbqTmEd4QMMXPUNNDLyV%0AEzOXkWE3ay5zNT%2FG4zom3g1tzFg%3D%0A)

Primeiro, seleciono o tipo de remetente:

![Imagem 17: Primeiro, seleciono o tipo de remetente:](https://downloads.intercomcdn.com/i/o/1152395228/7cd48c8ffaa3d90476f0923a/image.png?expires=1786536000&signature=83d81639aa4f3e015f11b130be19a9d9305e476fa65d8e988d4d493957eca96c&req=dSEiFMp3mINdUfMW3nq%2BgW8%2BRZZKswTBwyedEHnNPcHxxiaziVIJT30A6byV%0ADKfr%2F49e043jUQjxk7PDwJJ9duI%3D%0A)

E-mail automático será disparado por [no-reply@ploomes.com](mailto:no-reply@ploomes.com).

Com Usuário pré-definido e Usuário do campo, selecionamos um usuário que vai ser o remetente desse email via integração SMTP. É necessário ativar a integração de e-mails antes.

[Clique aqui para integrar seu email](https://sankhya.zendesk.com/hc/pt-br/articles/42427670947991)

Agora, selecionamos um usuário que será notificado caso a automação falhe. A automação pode falhar caso o destinatário não exista ou o remetente não tenha um email configurado.

![Imagem 18: Agora, selecionamos um usuário que será notificado caso a automação falhe. A automação pode falhar caso o destinatário…](https://downloads.intercomcdn.com/i/o/1152397799/c653a630b09875c114b6cce4/image.png?expires=1786536000&signature=31e1f6d2ef6533a2b8a77fc54c57239f27fe98a9c3c5416f7d0a03cfaa67c976&req=dSEiFMp3moZWUPMW3nq%2BgdWut6nmxuiyvEaMKoea6TFxD0aHxgE7ZdRlVe5G%0ABwuWF7Z3uiezqXT0IARisvlOLlo%3D%0A)

Em "**Selecione campo de e-mail para o destinatário ou escreva e-mails separados por ponto e vírgula"**, selecionamos quem vai receber esse email. Se for direcionado para o cliente, por exemplo, uso o campo de cliente "e-mail".

⚠️**ATENÇÃO**: se eu preencher por exemplo o campo "Cliente" do negócio, a automação vai considerar o nome do cliente como destinatário, o que resultará em um erro.

![Imagem 19: ⚠️ ATENÇÃO : se eu preencher por exemplo o campo "Cliente" do negócio, a automação vai considerar o nome do cliente…](https://downloads.intercomcdn.com/i/o/1152399668/1fe6a9ac626909ea6906bab6/image.png?expires=1786536000&signature=cdae4913b8aba20db10d8defe385549f98c94a5009316fc17679fb8b43503752&req=dSEiFMp3lIdZUfMW3nq%2BgXY2brU8tgCktQh1bzS7HU%2FLNHQPsFD8UvYcNSCM%0AU9HCepmPOFqZXHp4fdfIAM2ikuA%3D%0A)

E, por fim, configuramos o assunto e conteúdo do e-mail. É possível inserir campos customizados no botão "Campos", e editar o HTML do email em "Código-fonte".

⚠️**ATENÇÃO**: O Ploomes não é um sistema de e-mail marketing, e seu provedor não o reconhecerá como e-mail marketing. O disparo de emails por automações periódicas pode causar um bloqueio da parte do seu provedor de e-mails.

### Criar tarefa

Cria uma tarefa respeitando os campos confiugrados. Configure o usuário a receber a tarefa, tipo, título, descrição e data, além de outros detalhes. A Data pode ser definida para x dias depois da automação - para que a tarefa seja criada para o dia em que a automação rodou, preencha '0' dias após a automação.

![Imagem 20: Cria uma tarefa respeitando os campos confiugrados. Configure o usuário a receber a tarefa, tipo, título, descrição e…](https://downloads.intercomcdn.com/i/o/1152404011/357046a7b27d6eb56eff8f03/image.png?expires=1786536000&signature=e72012612d2f0fb578bd4deaae053a0531d90879f3e28782485d4ed9a37495e0&req=dSEiFM1%2BmYFeWPMW3nq%2BgZa73ORAU8YY8%2B3KyuWKp5bbwgmrffhMmGM4qKKp%0ACyUQYzkg8e0TQY2R1GpBXSIwadM%3D%0A)

Os campos livres, como "título", também podem ser preenchidos por título, como na ação "Editar dados".

### Criar negócio

Cria um novo negócio.

Defina o funil e estágio em que o negócio será criado, e o formulário do funil será espelhado na configuração da automação. Os campos podem ser puxados de outro campo (baseado com o campo do negócio gatilho) ou calculados por fórmula.

![Imagem 21: Defina o funil e estágio em que o negócio será criado, e o formulário do funil será espelhado na configuração da…](https://downloads.intercomcdn.com/i/o/1152408113/76667e9fe1067aa7ef20b050/image.png?expires=1786536000&signature=3772b97fa126f3da41b0c82daaaea59f345ecf174af02b1b0fcdeec1b3868d7d&req=dSEiFM1%2BlYBeWvMW3nq%2BgblHLqGQ1U9uQl7g1qcGNy4mYhs4JZ4Z39kTgRu3%0AQKCkQ4iaJnZb8gxuAlSaNPdr9aQ%3D%0A)

### Criar registro de interação

Cria um registro de interação. Os campos espelham o formulário de novo registro de interação.

![Imagem 22: Cria um registro de interação. Os campos espelham o formulário de novo registro de interação.](https://downloads.intercomcdn.com/i/o/1152408800/44dad43acaf7d68e4e3d3b02/image.png?expires=1786536000&signature=207edf463e6c888345913469e3fe1ffb8d2c84eecc3d8ab5f6053de216320976&req=dSEiFM1%2BlYlfWfMW3nq%2BgYqG5vd7RtB7cpg2HFp2IqkFfm8AmCLiUB4ckL4E%0A3hV47MLreSkhBx3CbVEsCGWaq9k%3D%0A)

### Perder negócio

Roda apenas em automações de negócio - perde um negócio com o motivo de perda espcificado

![Imagem 23: Roda apenas em automações de negócio - perde um negócio com o motivo de perda espcificado](https://downloads.intercomcdn.com/i/o/1152411281/e2d08d2feb27e7a3f526fb52/image.png?expires=1786536000&signature=fdda962a863e42fdb0f5885f251cf964f969a66b6280ba1d8dd6de3d1a3f1eaf&req=dSEiFM1%2FnINXWPMW3nq%2BgQQyshDW52guzb7bs7AuASOGFp0C%2FflE9NBeaXcT%0A%2BWglsgneOdLc%2B5hCevqnGczkVZA%3D%0A)

### Ganhar Negócio

Ganha um negócio. Roda em automações em que o item que engatilha a automação, pode ter um card diretamente associado a ele:

- Negócio
- Venda
- Proposta
- Tarefa
- Documento

![Imagem 24: Documento](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1711560056/86cf683641f473e5b59e972738e2/image.png?expires=1786536000&signature=9f87c9bc0f408a3215725f82af1cf83f0f76ba84af681a64440c4b651a60621a&req=dScmF8x4nYFaX%2FMW3nq%2BgSBiREC80VbIbCfALis%2FkbxTdP28pAp%2FMhZHupyO%0ATlWVrpwQtKHmzR6PxMswuhjTkW0%3D%0A)

Ponto de atenção: essa automação irá ignorar as seguintes configurações de funil:

1. **Ganhar card apenas na última etapa** **→** independente dessa configuração, o card será ganho pela automação em qualquer etapa em que ela for engatilhada.
2. **Pode ganhar cards neste pipe** → mesmo com essa configuração desativada, se a automação for engatilhada, o card será ganho neste pipe.
3. **Nova venda ao ganhar card** → mesmo com essa configuração ativada, não será aberta uma janela de criação de nova venda quando a automação rodar.

## Configurando travas na automação

Uma automação que roda com a edição de um item, ou vasculha a base todos os dias, por exemplo, precisa rodar apenas uma vez para cada item que se encaixe nos filtros. O que podemos fazer para garantir isso é incluir nas **ações** da automação algo que impeça que caia no **filtro** da mesma. Podemos criar um novo campo para isso, da seguinte maneira:

Nas ações, selecione "Editar dados". Garanta que essa seja a primeira ação a rodar.

![Imagem 25: Nas ações, selecione "Editar dados". Garanta que essa seja a primeira ação a rodar.](https://downloads.intercomcdn.com/i/o/1152413493/c74fd6f2e35024c212529880/image.png?expires=1786536000&signature=18a32da8e03d2679244054f3669b83b8cc3902df123f39c9d95b2fcd805b8c07&req=dSEiFM1%2FnoVWWvMW3nq%2BgYXnozcjy7doDGdU70EGzcLqZgKcdxZ4GusG5JPb%0AIjKua7whrt5CRM8bAI%2BFf%2Bzd19c%3D%0A)

Selecione "Criação rápida" e configure o campo com um bom nome e o tipo 'checkbox' (verdadeiro ou falso):

![Imagem 26: Selecione "Criação rápida" e configure o campo com um bom nome e o tipo 'checkbox' (verdadeiro ou falso):](https://downloads.intercomcdn.com/i/o/1152414227/fd60b8194a5546dcb41ae9a4/image.png?expires=1786536000&signature=b15090b81ac1e97b31fd5f78018b70033f90469103d345c236ad060a52ad744b&req=dSEiFM1%2FmYNdXvMW3nq%2BgTAaalz4yc9ihSYCkXVfwdVsqYyRY81Ehw2RYwH2%0AxCOzJ%2BvmTR8BLhrXMeG5XDQmjLg%3D%0A)

Vamos preencher esse campo com o valor estático Sim:

![Imagem 27: Vamos preencher esse campo com o valor estático Sim:](https://downloads.intercomcdn.com/i/o/1152416171/16ad95f08a4945a4e9e852d5/image.png?expires=1786536000&signature=1741ff3df411b7fd52d4e640e9673a5f40d986a10135e2de59bdbc8c26efdfac&req=dSEiFM1%2Fm4BYWPMW3nq%2BgWCN7vM0vDVKberVeSrXfem0ymK%2FUMD4PY7FOlKO%0A7pZ3XgySnf9bNjojwLkhboi2UbI%3D%0A)

Agora, salve a automação, feche-a e abra novamente - isso faz com que o campo esteja disponível para ser inserido nos **filtros**:

![Imagem 28: Agora, salve a automação, feche-a e abra novamente - isso faz com que o campo esteja disponível para ser inserido nos…](https://downloads.intercomcdn.com/i/o/1152416498/3f5ff0a9896ae27062c01fe7/image.png?expires=1786536000&signature=7fda4908e760cfce28564649e6cee49acf0ced77f2e9e4788456864ee9bda19e&req=dSEiFM1%2Fm4VWUfMW3nq%2Bgf3szsY%2BbTzPaE15FKnl%2Bsuofev3FZLBAYU1pn4p%0ARZf%2BExkke11%2B%2FY2nSZHAUSSMCW8%3D%0A)

A lógica é:

A automação só roda se o bloqueio não estiver ativo, e quando roda, ativa o bloqueio.

Isso garante que automações não rodem sem necessidade na conta, o que aumenta a performance do sistema e impede filas e lentidões em outras automações.
