---
id: "42427451459991"
titulo: "Como integrar o Ploomes com o ChatGPT (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427451459991-Como-integrar-o-Ploomes-com-o-ChatGPT-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:01:52Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12406725", "sync_hash_c3b8a6e9d7a7"]
---

# Como integrar o Ploomes com o ChatGPT (via Pluga)

**Observação**:

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

Com a integração entre o Ploomes e o ChatGPT via Pluga, você insere inteligência artificial diretamente no seu fluxo de vendas, sem precisar alternar entre sistemas ou fazer trabalho manual. O ChatGPT atua como uma etapa intermediária: recebe os dados do Ploomes, interpreta e processa as informações de acordo com as instruções que você definir, e entrega o resultado pronto para a ferramenta de destino.

Alguns exemplos do que é possível fazer:

- Quando um card avançar para a etapa de proposta no Ploomes, usar o ChatGPT para gerar automaticamente um e-mail de follow-up personalizado e salvá-lo como rascunho no Gmail, pronto para o vendedor revisar e enviar com um clique;
- Assim que um card entrar em uma nova etapa do funil, acionar o ChatGPT para gerar um briefing completo do lead e enviar automaticamente para o canal do time de vendas no Slack, com contexto, pontos de atenção e sugestão de abordagem;
- A cada proposta criada no Ploomes, usar o ChatGPT para redigir um e-mail de apresentação comercial personalizado com base nos dados do negócio, produtos e perfil do cliente;
- Quando um card for marcado como perdido, acionar o ChatGPT para gerar uma análise de diagnóstico e registrar automaticamente a anotação no Ploomes para consultas futuras;
- Classificar leads automaticamente como quente, morno ou frio com base nas informações do card, e atualizar campos personalizados no próprio Ploomes, sem nenhuma digitação.

Essa flexibilidade é possível porque o ChatGPT suporta ações como **"Iniciar conversa"** e **"Extrair dados estruturados"**, que podem ser combinadas com qualquer gatilho do Ploomes: card criado, card em etapa de funil, card ganho, card perdido, proposta criada, entre outros.

## Requisitos

- Uma conta no [Ploomes](https://app10.ploomes.com/login);
- [Créditos](https://platform.openai.com/settings/organization/billing/overview) em uma conta de API da OpenAI;
- Uma conta na [Pluga](https://pluga.co/).

**Nota:** automatizações com IA exigem pelo menos três ferramentas, com o ChatGPT como intermediário, e utilizam o recurso de integrações multi-actions disponível nos [planos pagos](https://pluga.co/precos/) da Pluga.

## Passo a passo

Neste artigo você encontra dois casos de uso prontos para implementar com o ChatGPT e o Ploomes via Pluga. Os primeiros passos — acesso à Pluga e criação da automatização — são comuns a ambos. Faça-os uma única vez e avance direto para o caso que faz mais sentido para o seu contexto:

- **1. Como gerar um e-mail de follow-up personalizado baseado na etapa do funil e salvar como rascunho no Gmail** — ideal para times comerciais que querem que cada avanço de card no Ploomes gere automaticamente uma comunicação personalizada e pronta para envio, sem nenhuma digitação.
- **2. Como criar um briefing do lead para o vendedor quando o card avança no pipeline e notificar o time no Slack** — ideal para operações em que o contexto do lead precisa chegar rapidamente ao vendedor no momento certo, sem que ele precise buscar as informações no CRM.

Acesse a [Pluga](https://pluga.co/) e clique em **"Entrar"** ou em **"Cadastrar"** se este for o seu primeiro acesso;

![Imagem 1: Acesse a Pluga e clique em "Entrar" ou em "Cadastrar" se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380908669/6c202b057a443ebd0087f99f000f/c26ecbf0-4691-4497-9727-ba2379e94257?expires=1786536000&signature=3e994aeafcd87cb41db3370a4289b7ea9e3d2dea5e9649b2a11d643bf3558f0b&req=diMvFsB%2BlYdZUPMW3nq%2BgcBJOd%2BY8cCqgQYAi4v29n5elduorR6e%2BQBNT4eD%0A00QHTcCZqCb3Q1tCpkwxA%2F90nq8%3D%0A)

Na área de usuário da Pluga, clique em “**Criar Automatização**”;

![Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380909722/b33c57259e168a8e119949ea91aa/08a16630-1c01-4280-9abd-7ac4f0e92472?expires=1786536000&signature=00b1fde691c7f65d5cc27321fd67579dff05a95faccfcc2b0b165f3969f60a16&req=diMvFsB%2BlIZdW%2FMW3nq%2Bgcaq8zj1ra8cQwqPgjEdwmZZUL86aljYBP5XRF%2F%2F%0ATm3%2B7H23tEKgIKXQXnke%2BKYa4V8%3D%0A)

Dê um título para a sua automatização - isso vai ser útil caso você queira editá-la no futuro - e siga para o caso de uso desejado abaixo;

![Imagem 3: Dê um título para a sua automatização - isso vai ser útil caso você queira editá-la no futuro - e siga para o caso de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380910358/c179d2a001a95a51a39be76f37b1/256961ea-0b8a-446e-904a-b4bb19f2a570?expires=1786536000&signature=1e123bc487e70eb0dd2293b1ff1208d95e6a5bca9b3bd99e7424ddaaa07386fa&req=diMvFsB%2FnYJaUfMW3nq%2BgWtwtZBAgSvCbKF9ykDZ39oKHHu0VXpv4le7HvQa%0Aq64Mf%2BWDg44jbXtgYAMX4ULXHhM%3D%0A)

---

## 1. Como gerar um e-mail de follow-up personalizado baseado na etapa do funil e salvar como rascunho no Gmail

Quando um card avançar para uma etapa específica do funil no Ploomes como "Proposta enviada" ou "Aguardando retorno" os dados do negócio e do cliente são enviados ao ChatGPT, que gera automaticamente um e-mail de follow-up personalizado e contextualizado. O texto é então salvo como rascunho no Gmail do vendedor responsável, pronto para revisão e envio com um clique sem nenhuma digitação manual.

## Conectando-se ao Ploomes

Selecione o **Ploomes** como ferramenta de origem e o gatilho **"Card alcança etapa no funil"**. Clique em **"Salvar e Continuar"**;

![Imagem 4: Selecione o Ploomes como ferramenta de origem e o gatilho "Card alcança etapa no funil" . Clique em "Salvar e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380911305/f9a96328bc98fc0dd61b41bededf/96a4d884-11cf-490e-8a94-31c8fa7008ad?expires=1786536000&signature=0eaa9d7d893271c2c1d0fec475f9c81c83cdb59be30d6f623e95adf171ea9765&req=diMvFsB%2FnIJfXPMW3nq%2BgSR%2FJhcU8Y9OL%2BEH%2Fo2oM3FKbcc4ILK%2FHk56apoD%0Ac13LOZZRIRzNf%2FFOBIaX3wx8tao%3D%0A)

Conecte sua conta do Ploomes clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Ao criar outras automatizações com o Ploomes, sua conta já aparecerá listada entre as contas conectadas. Caso seja a sua primeira vez, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 5: Conecte sua conta do Ploomes clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380911993/b08cb5fbc3dcefe167ac589d7c17/8fbde4aa-bbf2-432d-a2af-f70bdd9f77df?expires=1786536000&signature=3b7e297e1df68dcfd9f7b6ce3e087a3229dbd3be1c6e4f7843093fbd3ad121be&req=diMvFsB%2FnIhWWvMW3nq%2Bga3IwadEVKQigbJTZFolUR0eLzqi7uDFcuMBVGPW%0A9O%2B0jQm4olk20Jtt4mOj4lkhtXw%3D%0A)

Selecione o **funil** e a **etapa** que acionarão a automatização - por exemplo, "Proposta enviada" ou "Aguardando retorno". Clique em **"Salvar e Continuar"**;

![Imagem 6: Selecione o funil e a etapa que acionarão a automatização - por exemplo, "Proposta enviada" ou "Aguardando retorno".…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380912650/d7642201ef662ebaf28b1a90250d/75377290-0fac-486e-9690-b12b28bc9e92?expires=1786536000&signature=4e2830273738ecfbbc2274b7c90aad9909882b5819d60db4f44a67f9d8e5e2cd&req=diMvFsB%2Fn4daWfMW3nq%2BgV6DQsXUWQ9XuX6THQE6kaR7%2F9vHWezkxQkZ57C5%0AWA99kFnUE6Jv9Ky66xUfi6QdXsw%3D%0A)

Se quiser, configure filtros adicionais para restringir a automatização a cards com características específicas como valor mínimo, produto ou responsável. Clique em **"Conectar Nova Ferramenta"**;

![Imagem 7: Se quiser, configure filtros adicionais para restringir a automatização a cards com características específicas como…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380913200/ffed85132c1b5914caeb5ced6841/f1f5ce70-1ef6-4b12-84c0-84013c9b8d12?expires=1786536000&signature=d5f8caa64d1c9b5f2d49525227c71cfc485d2c7734676631fee8d11dd8eb90b2&req=diMvFsB%2FnoNfWfMW3nq%2BgdolgQQLNIU2wBOWs1w2E12YM1dYijNrNmYXqczw%0AyEjXpg5FRlqn%2BCtnIj6gQju%2BvE8%3D%0A)

---

## Transformando dados com ChatGPT

Selecione o **ChatGPT** e a ação **"Iniciar conversa"**. Essa ação envia os dados recebidos do Ploomes para o ChatGPT e retorna uma resposta gerada pela IA de acordo com as instruções do prompt. Clique em **"Salvar e Continuar"**;

![Imagem 8: Selecione o ChatGPT e a ação "Iniciar conversa" . Essa ação envia os dados recebidos do Ploomes para o ChatGPT e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380913840/a1860ab3cc9937aa8b2b7770165f/7ca4e008-e711-4b1b-9f03-6a5b6986cd32?expires=1786536000&signature=50aaff079a965ba96cd9dcb1020cf00c918487d46e06f0eadeffaad47c03632b&req=diMvFsB%2FnolbWfMW3nq%2BgXSOKMjIowfMUbZRhYZptsFcyJ1Tz%2Fwr%2F8uTBhYi%0ANblNqscoBbphzP7pHKhpLJQePzg%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação com a sua API Key da OpenAI. Esse processo só precisa ser feito uma única vez. Caso não saiba como encontrar sua API Key, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga os passos indicados;

![Imagem 9: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação com a sua API Key da OpenAI. Esse processo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380914668/e36b267826a6e160633c46029b18/efe9b8ae-6527-45f3-989b-6acd3216785c?expires=1786536000&signature=873325d5ccd6df23cc8918474dbad3d2358a77425fadb5812b570448ebb9140d&req=diMvFsB%2FmYdZUfMW3nq%2BgQNtH5YSxzQxJc8VC1QZ5gt32UFhtkVoHfLafxMN%0A5be8aWJiDDSA89%2FFw8QuYTRguFM%3D%0A)

No campo **"Mensagem (prompt de comando)"**, cole o modelo abaixo e use o botão **"Inserir infos"** para mapear as variáveis com os dados recebidos do Ploomes substituindo cada campo indicado pelo atributo correspondente.

**Modelo de prompt Caso 1**

```
Você é um assistente comercial especializado em comunicação B2B. Vou fornecer os dados de um negócio que avançou de etapa no CRM. Com base nessas informações, escreva um e-mail de follow-up personalizado, profissional e persuasivo para enviar ao lead.
Dados do negócio:
- Nome do contato:
- Empresa:
- Etapa atual do funil:
- Valor da proposta:
- Status:
O e-mail deve seguir esta estrutura:
1. Saudação personalizada com o nome do contato
2. Abertura que retoma o contexto da conversa ou da etapa atual, sem parecer genérica
3. Reforço do valor da solução com base no produto de interesse
4. Chamada para ação clara  responder ao e-mail ou agendar uma conversa
5. Encerramento cordial com o nome do vendedor responsável
Regras: use apenas as informações fornecidas  nunca invente dados. Seja objetivo, com tom consultivo. Máximo de 200 palavras. Parágrafos curtos.
```

![Imagem 10: Modelo de prompt Caso 1](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380921971/017e67ae3d4f63becdf8291f522d/e8656f44-9fe8-408f-ba5c-8b3bc1e2b66b?expires=1786536000&signature=e6143d3ba5ea2368811231fa93bbc56a4eb1d0e507023ce1fefba62b1596714e&req=diMvFsB8nIhYWPMW3nq%2BgSi%2BCIF7UPpNCRrWbqBOb0FwPRvsvpH%2FsfGIUlnM%0ApAtJVPj5PpzmG0TSiTrqmWV0FYM%3D%0A)

No campo **"Instruções de Sistema"**, defina o comportamento geral do modelo. Exemplo:

```
Você é um assistente comercial especializado em comunicação B2B. Escreva e-mails persuasivos e profissionais com base nas informações fornecidas. Adapte o tom ao contexto e perfil do cliente. Use ortografia impecável, linguagem clara e parágrafos curtos. Nunca acrescente informações que não foram fornecidas.
```

Selecione o **modelo** do ChatGPT que será utilizado. Por padrão, a integração da Pluga utiliza o modelo **4.1 mini**, que já está habilitado para buscas na web. Se preferir um modelo diferente, consulte a [lista completa de modelos compatíveis](https://pluga.zendesk.com/hc/pt-br/articles/42497214251155) disponíveis na Central de Ajuda da Pluga. Clique em **"Salvar e Continuar"** e em **"Conectar Nova Ferramenta"**;

![Imagem 11: Selecione o modelo do ChatGPT que será utilizado. Por padrão, a integração da Pluga utiliza o modelo 4.1 mini , que já…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380923119/b065c6650013b01fdf2ec7943d70/9238d2e8-b6e9-45b0-a5e2-9b1e13a4094c?expires=1786536000&signature=c59f07eaa2cb662889c10e527ffa895d43438defc36dba29358e3a4b9ced16bb&req=diMvFsB8noBeUPMW3nq%2BgZFMEsiszDbvr4TPg2g8SryQ59VgnKVKFfZ3d9%2Fh%0AAts7281qj1IlQ76yD89YDiPl75g%3D%0A)

| **Atenção:** antes de ativar a automatização, teste o prompt diretamente na interface do ChatGPT. Cole um exemplo real de dados de um card do Ploomes e verifique se o e-mail gerado está com o tom, estrutura e tamanho esperados. Só ative depois que o resultado estiver consistente. |
| --- |

---

## Salvando o rascunho no Gmail

Selecione o **Gmail** e a ação **"Criar rascunho"**. Clique em **"Salvar e Continuar"**;

![Imagem 12: Selecione o Gmail e a ação "Criar rascunho" . Clique em "Salvar e Continuar" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380926422/e171b2fe924483d62d856da6eed6/0e65aa40-6fd1-4063-afae-f398c155e816?expires=1786536000&signature=8bb7f75be7968fb0fa064153a24e9359e3ba4627681b6c8c8cba160759e99a06&req=diMvFsB8m4VdW%2FMW3nq%2BgQGKjuoeffzVrmcNogGGGtVQzS6l1EY3Lyta8tLl%0ASMVFjPfD3TV%2FsfqxGmnBZ9hohq8%3D%0A)

Conecte sua conta do Google clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez;

![Imagem 13: Conecte sua conta do Google clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380926967/d231b274e44eee4cd67af045964e/f525e0dd-17f5-49cc-9e2b-1c71cdd449e6?expires=1786536000&signature=1d829da03b059ba943353b59250b71da5c2cc933c83ac1c3d175958ea9d6360d&req=diMvFsB8m4hZXvMW3nq%2Bgf4yZpvrV67U2wIXfIT9OWaviCFeMfwv3M6p%2BmpI%0AWNm%2FhHctFljP2yF9DpGYJICGfcc%3D%0A)

Configure os campos do rascunho:

- **Para:** insira o e-mail do contato via **"Inserir Infos"** > e-mail do contato
- **Assunto:** crie uma linha de assunto combinando dados do card por exemplo, o nome da empresa e o produto de interesse usando **"Inserir Infos"**
- **Mensagem:** selecione a resposta gerada pelo ChatGPT via **"Inserir Infos"**

![Imagem 14: Mensagem: selecione a resposta gerada pelo ChatGPT via "Inserir Infos"](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380928698/3a08cf6b014250e3a7ad5188d069/3b64bbd9-b6a9-4b68-bce6-bee9e0d111e5?expires=1786536000&signature=69c1cab753880edefc07160d3982e5afc1cf362368ca68c19a0d56903547ecb3&req=diMvFsB8lYdWUfMW3nq%2BgQ%2FjkDczgGdbKIAoayhYynkmzMlE9OklzsghYEpz%0AKQXHgTs%2BY8xSYUAMbgiaPOqz9%2BI%3D%0A)

Clique em **"Salvar e Continuar"** e depois em **"Finalizar Automatização"**;

![Imagem 15: Clique em "Salvar e Continuar" e depois em "Finalizar Automatização" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2380929221/b717d405c1e25f124d772bf99e37/bdf06606-987a-4dcc-ae92-f1840a48c267?expires=1786536000&signature=04a45b26de88f3338bcc1ef2c64f330b4346bdd0c4d1025c75bcc5d1d66c66e3&req=diMvFsB8lINdWPMW3nq%2BgV%2FghrWi%2BkUlmijwVZFIfJT4DETdA9rsniD1VFP%2F%0AhmGcw7UZ%2BvaoiYomvJwvxNhKsn8%3D%0A)

Prontinho. Agora, sempre que um card chegar à etapa configurada no Ploomes, o ChatGPT gerará automaticamente um e-mail de follow-up personalizado e o rascunho estará disponível no Gmail do vendedor pronto para envio com um clique.

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi action. Para isso, é só clicar em **"Conectar Nova Ferramenta"**.

---

## 2. Como criar um briefing do lead para o vendedor quando o card avança no pipeline e notificar o time no Slack

Quando um card entrar em uma etapa estratégica do funil como "Reunião agendada" ou "Negociação" os dados do negócio e do contato são enviados ao ChatGPT, que gera automaticamente um briefing completo do lead: contexto da oportunidade, pontos de atenção e sugestão de abordagem. Esse briefing é enviado em seguida para o canal do time de vendas no Slack, garantindo que o vendedor chegue preparado para cada interação, sem precisar buscar informações no CRM;

## Conectando-se ao Ploomes

Selecione o **Ploomes** como ferramenta de origem e o gatilho **"Card alcança etapa no funil"**. Clique em **"Salvar e Continuar";**

![Imagem 16: Selecione o Ploomes como ferramenta de origem e o gatilho "Card alcança etapa no funil" . Clique em "Salvar e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382099873/16292b86170e4245f2d5c4fece8b/e398af99-3ea1-4487-8bb9-38d227a81dd8?expires=1786536000&signature=7d076c03175e060d41606c31874f6ee376ee7ec855d5b7333733366887c99b42&req=diMvFMl3lIlYWvMW3nq%2BgRxVz4CRrsOfaIZ%2FO9S%2BDZyWOj4xFmSg12Uu1%2F2o%0AS4udGiNKajhE9J5lnEh%2Fkqx9wLw%3D%0A)

Conecte sua conta do Ploomes clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Caso seja a sua primeira vez, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 17: Conecte sua conta do Ploomes clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382100873/6184885aa4cf6c52cd803691f0f8/b4fcd16c-012c-4bb4-9595-0c12c51c10b4?expires=1786536000&signature=38c08cc20beff76ec4938ceb9fd4346f9b9d0783660db5afc90f92ed5e4b3aa5&req=diMvFMh%2BnYlYWvMW3nq%2Bgfm9wzOmhaGwxRxFdff8%2Bogtp1%2BNXAhV0ZJU4DSD%0ApS7SGjFL7ZjWiRc3mAprAnwOhSY%3D%0A)

Selecione o **funil** e a **etapa** que acionarão a automatização por exemplo, "Reunião agendada" ou "Em negociação". Clique em **"Salvar e Continuar";**

![Imagem 18: Selecione o funil e a etapa que acionarão a automatização por exemplo, "Reunião agendada" ou "Em negociação". Clique em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382101597/b258acfeb4dd12140b8c1cd64493/3ea2b53a-b6b8-4182-8815-6b246337d66d?expires=1786536000&signature=03d21eb3507c63a97b3df099ac45961a9c2e016bc05d5290460f74756de00c98&req=diMvFMh%2BnIRWXvMW3nq%2BgQfF8QuMtWpu2GvVk9IyJz8R8faMG%2Bk%2FDRgOB%2Feu%0AFOqtvZSgClImIdtxSeddBWiJePU%3D%0A)

Se quiser, configure filtros para segmentar ainda mais os cards que acionarão a automatização por valor, produto, responsável ou qualquer campo personalizado do Ploomes. Clique em **"Conectar Nova Ferramenta";**

![Imagem 19: Se quiser, configure filtros para segmentar ainda mais os cards que acionarão a automatização por valor, produto,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382102378/50dc13aea4e67c189aea5a493ecd/97103e40-00a8-47eb-a7cd-c0e307bc6801?expires=1786536000&signature=188799dbb8cfa33bffa2aa8be50c9032001a1a553ce08ccbc20c78ba24ab6be1&req=diMvFMh%2Bn4JYUfMW3nq%2Bgcrem8XoZK492Ucs%2B38ZyxS4qN%2BiSdXRhKxWzMz2%0ASYxISxAWbY1AZQXH36Vf615TXRo%3D%0A)

## Transformando dados com ChatGPT

Selecione o **ChatGPT** e a ação **"Iniciar conversa"**. Clique em **"Salvar e Continuar";**

![Imagem 20: Selecione o ChatGPT e a ação "Iniciar conversa" . Clique em "Salvar e Continuar";](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382103032/b759170a27f8db8f8e967427b16d/1354cbba-21f8-4ca3-8d52-4ec2fce43371?expires=1786536000&signature=e404b5cf57cfef66f45353492b2f91279e981bd68c33226fa426e137be130e2f&req=diMvFMh%2BnoFcW%2FMW3nq%2Bgd3kngqzzh1ImNj1feS8pHVwN8SnltEtPkSf8V8x%0A26nzDz1y4DICNxRxAqcd%2FCWR1pQ%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação com a sua API Key da OpenAI. Esse processo só precisa ser feito uma única vez;

![Imagem 21: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação com a sua API Key da OpenAI. Esse processo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382103894/6a9cef862444e5eadb2b8a1ab9d4/ed814a56-4c64-465f-bea2-bc9ddbdbc2ef?expires=1786536000&signature=34dd791745bc8925da9f9e458681afd30ac3378749fa1d0e78fbb1bb3eaf4a1c&req=diMvFMh%2BnolWXfMW3nq%2BgayvGNsEyKv47AxVzeWr1AnkHFRIpuIYttZkECeY%0ASmJCKdBbyXtaimG2tXBux7%2B6yf0%3D%0A)

No campo **"Mensagem (prompt de comando)"**, cole o modelo abaixo e use o botão **"Inserir Infos"** para mapear cada campo indicado com o atributo correspondente do Ploomes;

**Modelo de prompt Caso 2**

```
Você é um assistente comercial B2B. Um lead acabou de avançar para uma etapa importante do funil de vendas. Vou fornecer as informações do negócio. Gere um briefing objetivo e acionável para o vendedor responsável, cobrindo os seguintes pontos: 1. Resumo do negócio (2-3 linhas): quem é o lead, o que está sendo negociado e em qual etapa está 2. Contexto relevante: informações de empresa, cargo e produto de interesse que ajudam a personalizar a abordagem 3. Pontos de atenção: o que o vendedor deve observar ou verificar antes da próxima interação 4. Sugestão de abordagem: como iniciar ou retomar o contato de forma assertiva nesta etapa Dados do negócio: - Título do card: [inserir via "Inserir Infos" → título do card] - Nome do contato: [inserir via "Inserir Infos" → nome do contato] - Empresa: [inserir via "Inserir Infos" → empresa] - Cargo: [inserir via "Inserir Infos" → cargo] - Etapa atual: [inserir via "Inserir Infos" → etapa do funil] - Produto de interesse: [inserir via "Inserir Infos" → nome dos produtos] - Valor do negócio: [inserir via "Inserir Infos" → valor total] - Vendedor responsável: [inserir via "Inserir Infos" → dono do card] Regras: use apenas as informações fornecidas  nunca invente dados. Seja direto e útil para o vendedor. Limite o briefing a 250 palavras. Use marcadores curtos para os pontos 2, 3 e 4.
```

![Imagem 22: Modelo de prompt Caso 2](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382105268/77df9fc34832d85d86a4f28d72e3/a187bbfd-3a44-4882-a3be-1e2a327db872?expires=1786536000&signature=4993bd51476ccfa71fe713ad6dfc826d224199f7bb5e0321e6ec6c2276607a43&req=diMvFMh%2BmINZUfMW3nq%2BgXiLN6JRZjZWFqUPqbE6rF1BxFaGvWoHldCf8m8%2F%0AbfV9Cc1ndxLrLkhDnYOQF9Qbt1Q%3D%0A)

No campo **"Instruções de Sistema"**, defina o comportamento do modelo. Exemplo:

```
Você é um assistente especializado em apoio a times de vendas B2B. Seu papel é transformar dados de CRM em briefings claros e acionáveis para vendedores. Seja direto, objetivo e organize as informações de forma que o leitor entenda o contexto rapidamente. Nunca invente dados  trabalhe apenas com o que foi fornecido.
```

![Imagem 23: No campo "Instruções de Sistema" , defina o comportamento do modelo. Exemplo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382106076/877243afd97d335bf2ce322145f5/1d55b97b-b3f2-46f7-8d35-2f811a6f1795?expires=1786536000&signature=ab478a6079d2c421ff16fc84c6306a634639eb40e382f333f86b4adfcea04d25&req=diMvFMh%2Bm4FYX%2FMW3nq%2BgYKPWjdhc8Q2x7SMZWpTSM%2BhMcD%2BohZc3oJ3F7JH%0AKonNVpu6bTbgramFEiaNY1OSg6Y%3D%0A)

Selecione o **modelo** do ChatGPT que será utilizado. Por padrão, a integração da Pluga utiliza o modelo **4.1 mini**. Clique em **"Salvar e Continuar"** e em **"Conectar Nova Ferramenta";**

| **Atenção:** antes de ativar a automatização, teste o prompt diretamente na interface do ChatGPT. Cole um exemplo real de dados de um card do Ploomes e verifique se o briefing gerado está com a estrutura, tamanho e tom esperados. Só ative depois que o resultado estiver consistente. |
| --- |

## Notificando o time de vendas no Slack

Selecione o **Slack** e a ação **"Enviar mensagem em um canal"**. Clique em **"Salvar e Continuar";**

![Imagem 24: Selecione o Slack e a ação "Enviar mensagem em um canal" . Clique em "Salvar e Continuar";](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382107557/62139160eab4fe924c49bfa51bb7/bbf3d2cf-a1b9-41a9-83d9-71b91a4c2308?expires=1786536000&signature=2b617eeac8b85afda91beb54950e795276cd7f5f50465bec1cabdd86d2837162&req=diMvFMh%2BmoRaXvMW3nq%2BgSki%2FlTIsf2ZwNNgndePCNmCRYqxgGJ9W5RUC2kC%0ApdqS59vL%2Bowy7prToE6cMV9JwL0%3D%0A)

Conecte sua conta do Slack clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez;

![Imagem 25: Conecte sua conta do Slack clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382108533/ca032d80f1e48217d47d5f275434/1d8b0a9c-d0fb-470d-8795-97a5f36135a2?expires=1786536000&signature=50fa18d518deb7b45d551917a4576a9dbfeafcbe49f6ce77b7d4dc63bd85c494&req=diMvFMh%2BlYRcWvMW3nq%2BgYnf4E3ubRj5q0ik9fLacjEKezI0ks%2Bl6NL95o6W%0A4LNL456fwcJ0g259a0HqrE%2B4sy8%3D%0A)

Selecione o **canal** onde o briefing será enviado, por exemplo, o canal do time de vendas ou um canal específico por funil. Configure a **mensagem** usando o botão **"Inserir Infos"** para incluir:

- O nome do contato e da empresa — para identificar rapidamente o lead
- A etapa do funil em que o card entrou
- O briefing gerado pelo ChatGPT — como corpo principal da mensagem
- O nome do vendedor responsável — para deixar claro quem deve agir

![Imagem 26: O nome do vendedor responsável — para deixar claro quem deve agir](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382109214/08e3d7508ee49e223abf9082e703/b9228582-9117-4a51-9973-1585d8235b78?expires=1786536000&signature=211698f9bc986e74d6e7b2cef6ae6e42744ad84ae194d25464e601273f4ef06d&req=diMvFMh%2BlINeXfMW3nq%2BgRSWfQZNcE5hQ4F09FiSxdhucCgeGAFQcLUhye76%0AQgVdng2l2sgS9gtglFRS01aR%2FXg%3D%0A)

Clique em **"Salvar e Continuar"** e depois em **"Finalizar Automatização";**

![Imagem 27: Clique em "Salvar e Continuar" e depois em "Finalizar Automatização";](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2382112685/6cea539b5f7572743109e1cc063c/a440147b-5576-464b-bce3-42f7c466c820?expires=1786536000&signature=37606f2c8ff8f5e232c61bf3549e1aa2e71e4800189bd5cdffd67da6a42aef08&req=diMvFMh%2Fn4dXXPMW3nq%2BgfGR0oX%2FFCPji55x7JU1vezQ5GYlMUJIY8qFLidd%0A6cPehB67QHx2GRSW%2FG4pG%2Bqe35I%3D%0A)

Prontinho. Agora, sempre que um card avançar para a etapa configurada no Ploomes, o ChatGPT gerará automaticamente o briefing do lead e o time de vendas receberá a notificação no Slack com contexto completo e pronto para ação;

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi action. Para isso, é só clicar em **"Conectar Nova Ferramenta";**

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
