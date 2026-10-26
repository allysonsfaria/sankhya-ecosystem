---
id: "42427452917527"
titulo: "Automações de funil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427452917527-Automa%C3%A7%C3%B5es-de-funil"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-11T16:14:49Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5782881", "sync_hash_4454038bc8e4"]
---

# Automações de funil

As automações de funil no Ploomes permitem executar ações automáticas sempre que um card atinge uma **determinada condição** no funil, como entrar em um estágio, ser ganho, perdido ou reaberto. Com isso, é possível economizar tempo, padronizar processos e reduzir tarefas manuais.

Você pode, por exemplo, configurar uma automação para enviar um e-mail de boas-vindas sempre que um card for marcado como "ganho", ou criar uma tarefa de follow-up assim que ele entrar em um novo estágio. Entre as **ações disponíveis** estão: editar dados, alterar ou duplicar cards, enviar e-mails, criar tarefas e até marcar o card como perdido.

Neste artigo, vamos explorar como funcionam essas automações, desde a escolha do gatilho até a definição das ações que devem ser executadas.

## Como configurar:

Na [configuração das etapas do funil](https://sankhya.zendesk.com/hc/pt-br/articles/42427677266455), clique em 'Configurar automações' na etapa desejada, e clique em "**Nova automação**".

![Imagem 1: Na configuração das etapas do funil , clique em 'Configurar automações' na etapa desejada, e clique em " Nova automação…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1623980768/38617bcb35765b2cc3fd289df519/image.png?expires=1786536000&signature=34c84fb2a8209194cd4468a712a513d8d76fad93e484e2eb94287cef078bc82c&req=dSYlFcB2nYZZUfMW3nq%2BgUqemBjQ%2BulpqKrkYrAAYXYAgXzm8R%2FNrmcTtNue%0AkAk7us615wyNZZ0aL0l7lDMtXFc%3D%0A)

## 1. Descrição

Preencha o campo de descrição com um resumo claro do que a automação faz. Documentar bem cada automação é essencial para facilitar o entendimento e a manutenção da conta no futuro, especialmente em ambientes com múltiplos usuários ou processos complexos.

## 2. Gatilho

Em seguida, preencha o campo de **gatilho**, ou seja, defina **quando a automação deve ser executada**. O gatilho representa o momento exato em que a regra será disparada, como, por exemplo, quando um card entra em um estágio, é ganho, perdido ou reaberto.

![Imagem 2: Em seguida, preencha o campo de gatilho , ou seja, defina quando a automação deve ser executada . O gatilho representa…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1764274239/1322fe527fd4a69dc3198de6a82c/image.png?expires=1786536000&signature=be781dfc4787104d2ab6d716049d77fb73dbfec42996d7e671fb83da2ddd52e9&req=dSchEst5mYNcUPMW3nq%2BgQ14YAA5g7GhSRH66uY3wgBGG9McmB3PH6Rp%2B116%0Atnx8iwRlJGegq4EQuq124qTtDaI%3D%0A)

### Regras do gatilho: Negócio editado neste estágio

Esse gatilho executa a automação sempre que a entidade selecionada for editada em um estágio específico.
Você pode configurá-lo de duas formas:

#### 1. Sem escolher campos específicos

A automação será disparada **toda vez que qualquer campo do item for alterado**.
Use essa opção quando qualquer modificação já justificar a execução (ex.: atualizar o status quando qualquer campo do negócio for editado, editar um valor etc.).

#### 2. Com campos específicos

Você pode escolher **entre 1 e 4 campos** que servirão como filtro para o gatilho.
Nesse caso, a automação será disparada **somente quando um desses campos for editado**.

Exemplo: se você selecionar os campos Status e Responsável, a automação rodará sempre que **um OU outro** for alterado.

⚙️ **Importante**: o operador usado entre os campos é sempre **“OU”**, ou seja, basta **um** dos campos selecionados ser alterado para que a automação seja executada.

## 3. Filtro

O **filtro da automação** é opcional, assim como acontece nos checklists. Ele serve para definir **em quais condições a automação deve ser executada**.
Você pode utilizá-lo para segmentar ainda mais os cenários em que a ação deve ocorrer.

 [Clique aqui para ver mais sobre filtros.](https://sankhya.zendesk.com/hc/pt-br/articles/42427447489815)

Veja abaixo um exemplo de filtro, onde a automação só será executada **se o negócio tiver vindo do funil de vendas**:

![Imagem 3: Veja abaixo um exemplo de filtro, onde a automação só será executada se o negócio tiver vindo do funil de vendas :](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1623980762/1871b32285ef33ae304568ed27cd/image.png?expires=1786536000&signature=365ea3aaecd26ec14075f840260cf09e749057d6616e86d20d0e096478ad12da&req=dSYlFcB2nYZZW%2FMW3nq%2BgfQI7yMldeUHrfBJd281HBOIYHBTeaM1pPuP7E9H%0AY9TzUDBG%2BKqRLRpMcmevpzM0b%2FQ%3D%0A)

## 4. Ações

No campo **"Ao ser disparada, o que a automação deve fazer?"**, você define as **ações** que serão executadas quando a automação for ativada.

É possível adicionar uma ou mais ações em sequência, dependendo da lógica que deseja automatizar. Veja abaixo as opções disponíveis:

- **Editar dados**: preenche ou altera automaticamente campos do card, data de fechamento, responsável, entre outros.
- **Alterar estágio do card**: move o card para um novo estágio do funil de forma automática.
- **Duplicar card em novo estágio**: cria uma cópia do card e posiciona no estágio desejado, útil em processos paralelos.
- **Enviar e-mail**: dispara automaticamente um e-mail com base em um modelo previamente configurado.
- **Criar tarefa**: gera uma nova tarefa associada ao card, que pode ser atribuída a um usuário específico, com prazo e descrição definidos.
- **Perder card**: marca o card como perdido automaticamente, solicitando o motivo da perda conforme as configurações da conta.
- **Ganhar card:** marca o card como ganho automaticamente.

![Imagem 4: Ganhar card: marca o card como ganho automaticamente.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642608425/a1222b0e1d3a019ea6c4f5044b1b/image.png?expires=1786536000&signature=580cece0276c6f2208992858bb181a19d5869342698dac3aff2229a694675052&req=dSYjFM9%2BlYVdXPMW3nq%2BgeqNQT8gHrxsNWU2sqNCgWonq5oD5nehtaARHFWK%0AIsGDaPq0D8kyZQ077WoNdI3W20E%3D%0A)

## Editar dados

Nessa ação, você deve **selecionar o campo que será editado** e definir o **valor que será preenchido automaticamente**, usando a opção de preenchimento com **Valor estático**.

![Imagem 5: Nessa ação, você deve selecionar o campo que será editado e definir o valor que será preenchido automaticamente ,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1623980778/e4af0c092d60271cc5a3b7caa1fb/image.png?expires=1786536000&signature=952b0307c4d66f07006f2e70175e608bb5c4bec7cec5ca6e22a6cce67f797e52&req=dSYlFcB2nYZYUfMW3nq%2BgRKIqWDbLKfa1SYj2Aa0YBWVu3DpsoXfOPPWmQHE%0A6oWlokOxuYrZm9VEMaYu7XWc6lg%3D%0A)

O preenchimento dinâmico — puxando o valor de outro campo ou utilizando uma fórmula em JavaScript — **só é possível nas** [automações genéricas](https://sankhya.zendesk.com/hc/pt-br/articles/42427640855703). Em automações de funil, o valor deve ser inserido manualmente.

Também temos a opção de limpar valores específicos de campos múltiplos.

Nessa opção, você deve selecionar um **campo múltiplo** para ser editado, e escolher quais opções deseja limpar do campo.

No caso abaixo, quando a automação rodar, se o campo "Marcadores" estiver preenchido com as opções

- Opção 1
- Alto potencial
- Urgente

Após a automação rodar, o campo seguirá preenchido apenas com a "Opção 1".

![Imagem 6: Após a automação rodar, o campo seguirá preenchido apenas com a "Opção 1".](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1669095128/9e3dd2bf8d98a2003b8f929def7a/image.png?expires=1786536000&signature=b75701b1cc1901bbdfb6b989953944de965a1d613086c4271176a59890f79c3d&req=dSYhH8l3mIBdUfMW3nq%2BgTLZOUUOjlvn1Mbawn1bolQdytRjEE0Gd0eVcrEY%0AMhWmPK%2FRtcsViKKaLD%2BLITaVwUU%3D%0A)

## Alterar estágio do negócio

Essa ação permite **mover automaticamente o negócio para um novo estágio do funil**.

⚠️ **Atenção:** negócios marcados como **ganhos** ou **perdidos** não podem ter o estágio alterado. Por isso, essa automação só funciona com os gatilhos **"Quando o negócio for reaberto"** ou **"Quando o negócio entrou nesse estágio"**.

Além disso, se houver **um checklist pendente**, o negócio também **não será movido de estágio**. Para evitar esse bloqueio, **insira o mesmo filtro da automação nas** [condições do checklist](https://sankhya.zendesk.com/hc/pt-br/articles/42427646964375)

Por fim, **selecione o novo estágio** para onde o negócio deve ser movido.

![Imagem 7: Por fim, selecione o novo estágio para onde o negócio deve ser movido.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1623980785/191e972518600a1ae0f1193eb379/image.png?expires=1786536000&signature=55006fbdde2810f09267298963865fe932718f432dee37413907b6b5fa80185d&req=dSYlFcB2nYZXXPMW3nq%2Bgcfsxl4HTbAJzaYtLVFlSVJnxoFXrZbY3UjPAX99%0APXytIIbnrBgvmq6aNQHTltPFdCw%3D%0A)

## Duplicar negócio em novo estágio

Essa ação permite **criar uma cópia do negócio em outro estágio**, normalmente em outro funil, enquanto mantém o original no estágio atual.

💡 **Recomendação:** use essa automação no último estágio de um funil com o gatilho **"Quando o item for ganho"**. Isso é útil, por exemplo, para **encaminhar negócios do funil de prospecção para o funil de vendas**, mantendo o histórico separado.

Essa prática permite **marcar o negócio como ganho** quando ele concluir sua jornada em um funil e, ao mesmo tempo, **iniciar um novo negócio no funil seguinte**, garantindo rastreabilidade e controle sobre cada etapa do processo.

Para configurar, **selecione o novo estágio** onde o negócio duplicado será criado.

![Imagem 8: Para configurar, selecione o novo estágio onde o negócio duplicado será criado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1623980776/c106e66a7507d6dade13fa1551e0/image.png?expires=1786536000&signature=b3366ad81f3ef9328aa5fef78bfbcf8f7bf88d879c2c93e98c45e867cb5d55cf&req=dSYlFcB2nYZYX%2FMW3nq%2BgcN45peF3KPtONaRjzGCFMZOzj0DqUYdUst3LX4%2F%0AFhjo4hCd76Gm%2F7EQN3Afxz%2BRUzo%3D%0A)

## Enviar e-mail

Essa ação permite **disparar automaticamente um e-mail** para o destinatário selecionado.

1. **Remetente:** escolha o tipo de envio.

   - Selecione **"E-mail automático"** para enviar via `no-reply@ploomes.com`.
   - Caso algum usuário tenha **SMTP configurado**, ele também poderá ser selecionado como remetente.
2. **Destinatário:** defina para quem o e-mail será enviado.

   - Pode ser um **campo dinâmico**, como o e-mail do contato do negócio.
   - Ou um **destinatário fixo**, como o e-mail do time financeiro.
3. **Conteúdo:** configure o **assunto** e o **corpo do e-mail**.

📌 **Dica:** personalize o conteúdo usando **placeholders** disponíveis na aba “Campos”, como o nome do cliente, nome do negócio, entre outros.

![Imagem 9: 📌 Dica: personalize o conteúdo usando placeholders disponíveis na aba “Campos”, como o nome do cliente, nome do…](https://downloads.intercomcdn.com/i/o/428107844/6c200dedf02ab02d7bb259a5/image.png?expires=1786536000&signature=bc353517cfab28ec0606ceaefbdaca1de245c7123ebee8077b0cc6029e4ff21f&req=cCIvF8l5lYVbFb4V1XW4gYGy5IygDXTz5XKnJtSo92B6rfleMbXVozj2pO6M%0AqFr2Rcva8deukRVG5DDX24usfw%3D%3D%0A)

## Criar tarefa

Essa ação permite **gerar automaticamente uma tarefa** para os usuários definidos, com prazo contado a partir da data em que o gatilho da automação for acionado.

Você pode **personalizar a tarefa** preenchendo os seguintes campos:

- **Responsável:** selecione o usuário ou campo dinâmico que receberá a tarefa.
- **Prazo:** defina em quantos dias (ou horas) após o gatilho a tarefa será criada.
- **Descrição:** adicione instruções ou informações relevantes para execução da tarefa.
- **Título da tarefa:** dê um nome claro para facilitar o acompanhamento.

Essa ação é ideal para garantir follow-ups, alinhamentos internos ou qualquer atividade que não pode ser esquecida.

- ![Imagem 10: Essa ação é ideal para garantir follow-ups, alinhamentos internos ou qualquer atividade que não pode ser esquecida.](https://downloads.intercomcdn.com/i/o/428109479/772860d6577f41b8528e10a8/image.png?expires=1786536000&signature=4a48f8f8353b9fe52354f9b5ef22baed052b178e023c5235da6d93507a26a425&req=cCIvF8l3mYZWFb4V1XW4gRRgAQTfhj0oO42FsJbgNLFkG%2B%2BeMi0TXy1BDEsc%0AKCP4PZQkVfSiF6bfAo4TjZhbfQ%3D%3D%0A)

## Perder negócio

Essa ação permite **marcar automaticamente o negócio como perdido**.

Para configurar, **selecione o motivo de perda** desejado. Todos os negócios perdidos por essa automação terão esse motivo registrado, de forma padronizada.

Essa ação é útil para filtrar e analisar perdas por categoria, além de manter o funil sempre atualizado.

![Imagem 11: Essa ação é útil para filtrar e analisar perdas por categoria, além de manter o funil sempre atualizado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642609877/340a881e3cb214a09317af192945/image.png?expires=1786536000&signature=e45dc0c9c9068f199708d7728d99c710b6834d4273bd214bcb994c4a1eceba17&req=dSYjFM9%2BlIlYXvMW3nq%2BgR%2FAyh0Fd7FcmAhwggkwg5WyzTuJhrmdIkWbFEin%0AWL7%2BUImShvCctJaz3gXvVcgh37o%3D%0A)

## Ganhar negócio

Essa ação permite **marcar automaticamente o negócio como ganho**, desconsiderando as regras de funil:

- “ganhar apenas na última etapa”
- “não permitir ganhar cards em determinada etapa”.

![Imagem 12: “não permitir ganhar cards em determinada etapa”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1642617082/5a7c910ceb8ae95574c51390bfd7/image.png?expires=1786536000&signature=57abfecd92d8ea3aaa7442c4029d3a89b9b1684cda804ed12158d9ef8ef41e94&req=dSYjFM9%2FmoFXW%2FMW3nq%2Bgad1pzT2tXLGfEQSt3nFpeEMegm0Qm9f%2FKehfofs%0AxoipoeShylK88UjV78N7PAufPew%3D%0A)

## Pontos de atenção

As automações de funil, por padrão, **rodam com as permissões do usuário que executa o gatilho**. Ou seja, se esse usuário **não tiver acesso ao funil de destino**, a automação **não será executada** corretamente.

Exemplo: se a automação duplica um negócio para o funil de vendas e o usuário não tem acesso a esse funil, ela será bloqueada.

Para evitar esse tipo de problema, você pode ativar a opção **"Executar automações com o usuário de automação"** nas configurações do funil.

![Imagem 13: Para evitar esse tipo de problema, você pode ativar a opção "Executar automações com o usuário de automação" nas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1623980784/ebd9acd3589cbce201fd76c54328/image.png?expires=1786536000&signature=812ecd0fcba052fecf2fffbcd0e225f6f3dd528cb16d7c354e24cb12d82bdbc6&req=dSYlFcB2nYZXXfMW3nq%2BgbZMhSFvH7%2BqGTQPaHGInLcBCfJ0bm7sbNyIn0G8%0AlUH3JoKv87dKsNKcsv1JC17edYk%3D%0A)

Como mencionado anteriormente, **automações de funil não podem movimentar negócios que estejam marcados como "ganhos" ou "perdidos"**, nem avançar negócios que tenham **checklists pendentes**.

Dica: se for necessário mover o negócio mesmo com checklist pendente, alinhe os filtros da automação e do checklist.

**Atenção ao disparo de e-mails:** se configurado incorretamente, um e-mail automático pode ser enviado ao cliente no momento errado. Sempre valide os filtros e o gatilho com cuidado antes de ativar a automação.

Se a automação já tiver a ação **"Perder card"**, **as seguintes ações não poderão ser adicionadas em sequência**:

1. **Perder card novamente:** um card já perdido não pode ser perdido outra vez. Para isso, seria necessário **reabri-lo** antes.
2. **Alterar estágio do card:** não é possível mover o card de estágio após ele ter sido marcado como perdido.
3. **Ganhar card:** um card já perdido não pode ser ganho. Para isso, seria necessário **reabri-lo** antes.

Vale destacar que a ação **"Perder card"** pode ser adicionada **após qualquer outra ação** dentro da mesma automação, desde que respeitadas as limitações mencionadas acima.

Se a automação já tiver a ação **"Ganhar card"**, **as seguintes ações não poderão ser adicionadas em sequência**:

1. **Perder card:** um card já ganho não pode ser perdido. Para isso, seria necessário **reabri-lo** antes.
2. **Alterar estágio do card:** não é possível mover o card de estágio após ele ter sido marcado como perdido.
3. **Ganhar card:** um card já ganho não pode ser ganho outra vez. Para isso, seria necessário **reabri-lo** antes.

Vale destacar que a ação **"Ganhar card"** pode ser adicionada **após qualquer outra ação** dentro da mesma automação, desde que respeitadas as limitações mencionadas acima.
