---
id: "42427414227479"
titulo: "Integração Neppo - Automação de envio ativo de WhatsApp"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427414227479-Integra%C3%A7%C3%A3o-Neppo-Automa%C3%A7%C3%A3o-de-envio-ativo-de-WhatsApp"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:16Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12554434", "sync_hash_b6d97e85175d"]
---

# Integração Neppo - Automação de envio ativo de WhatsApp

## 1) Sobre automação de envio ativo

O envio ativo de mensagens do WhatsApp via **Neppo** permite configurar **automações no Ploomes** (tanto **genéricas** quanto de **funil**) para disparar mensagens de forma automática, seguindo condições previamente definidas.

Essa funcionalidade garante **agilidade na comunicação com clientes**, fortalece o relacionamento e otimiza processos comerciais.

[GIF animado: Imagem 1: Essa funcionalidade garante agilidade na comunicação com clientes , fortalece o relacionamento e otimiza processos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771095429/64a2e01b4ec2aa37b5f643eb5938/automa%C3%A7%C3%A3o+de+etapa.gif?expires=1786536000&signature=264e39f70d88d2f9e9a597257afebe016f04a325a6bc4656e778640e14132706&req=dScgF8l3mIVdUPMW3nq%2BgTQm%2Bxz%2BcBNnxDV9jtb83T01l8tAZ11A8fCfT5b7%0ASvtyrHOmFB6hftX1RoOOnNJ%2B8ZM%3D%0A)

⚠️ **Atenção:** cada envio gera um **custo adicional** na sua conta Neppo. Configure suas automações com cuidado para evitar disparos desnecessários e cobranças indevidas!

---

## 2) Pré-requisitos

- Ter pelo menos **um modelo de mensagem aprovado pela Meta** dentro da Neppo.
- Ter o módulo de Workflow contratado no Ploomes.
- Para automações periódicas: ter o **limitador de envios configurado** na tela de integração Neppo (veja seção 3.3).

---

## 3) Como configurar

## 3.1) Criar ou editar automação

1. Acesse o **módulo de automações** no Ploomes.
2. Crie uma nova automação ou edite uma existente (genérica ou de funil).
3. Defina as **condições e filtros** de disparo.
4. Adicione a ação **"Envio ativo de mensagem do WhatsApp"**.
5. Configure os campos obrigatórios da mensagem.

[GIF animado: Imagem 2: Configure os campos obrigatórios da mensagem.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771096630/7641f933f62c419379e85a11fea7/nova+automa%C3%A7%C3%A3o.gif?expires=1786536000&signature=23400c3c8b45a18dbd1933d37034c985ad3e3a1f0b83cdabdaab2d895304a96e&req=dScgF8l3m4dcWfMW3nq%2BgWIadGDW0%2BbPpkV%2BRD9Dq4dJOGccizjKygLIUmt3%0A8QpeSXM%2Fzw%2FmcOPFafDm4ekvv5U%3D%0A)

Configure com cuidado o gatilho e o filtro de execução da automação e adicione validações, pois disparos errôneos geram custos potencialmente elevados.

## 3.2) Configurar a mensagem

Ao adicionar a ação, os seguintes campos estarão disponíveis:

- **Remetente (opcional):**

  - Usuário fixo.
  - Campo dinâmico (ex.: agente responsável).

  [GIF animado: Imagem 3: Campo dinâmico (ex.: agente responsável).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771103955/5d13f5e75429ca8fb6cd71c194a7/remetente.gif?expires=1786536000&signature=25b9a929fc8a0abb87ddc247d4170273c8ccf2824c58ddbda2d8dba1d1daa173&req=dScgF8h%2BnohaXPMW3nq%2BgSlQMO8oIaUJQW355gjHeJBzJQcDAUda6kJrvrdc%0AMw0S5hIVWAXOW6QJCpee3kFnDqE%3D%0A)

- **Destinatário:**

  - Campo dinâmico (ex.: telefone do cliente em formato DDI + DDD + número).
  - Número fixo (input manual com DDI + DDD).
  - É possível enviar a mensagem para todos os números cadastrados ou somente o primeiro.

[GIF animado: Imagem 4: É possível enviar a mensagem para todos os números cadastrados ou somente o primeiro.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771104396/9351661980a448a585101c28fc37/destinatario.gif?expires=1786536000&signature=e811841bb09ff79c2776ff444219fd03d580a80389b908be3aa3204a5d76d376&req=dScgF8h%2BmYJWX%2FMW3nq%2BgbgA3embvtd9qTonYX4wgMl1xqQ8KweKoYJ3Gze5%0AJyb4vTAEN5oJM9ErPieIjVQ%2B0Bo%3D%0A)

- **Grupo de atendimento (Neppo):** grupo responsável pelo envio.
- **Modelo de mensagem:** selecione entre os modelos aprovados no grupo.

  [GIF animado: Imagem 5: Modelo de mensagem: selecione entre os modelos aprovados no grupo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771104672/9a40536290a2f0eb5165604d0763/Grupo+de+atendimento+e+modelo+de+mensagem.gif?expires=1786536000&signature=cea6c9782a1dca19eadee3a72f0538cba7a705ceda51eae33c006726dba93ba9&req=dScgF8h%2BmYdYW%2FMW3nq%2BgdCMdaV0ZIkwc36D8u9MSBG0mS6nPloHcmaxFEbs%0Av6VSyEH1%2BvTGjk6jXLfjDtpoy5w%3D%0A)
- **Parâmetros dinâmicos:**

  - Personalização com campos da entidade (ex.: "Olá {nome}").

[GIF animado: Imagem 6: Personalização com campos da entidade (ex.: "Olá {nome}").](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771104871/1725c3a4634f97da651738952018/parametros.gif?expires=1786536000&signature=0963aa75147086d9b50360bdff48bcd4935bccf0a1310c4e103c32f8c62d5efa&req=dScgF8h%2BmYlYWPMW3nq%2BgRf3yReysGt87J%2BVAqwS5DuQbf%2FIMMozkNdOce0%2F%0ADA4CNJbwnB%2BaZOg1NleAJCEHI84%3D%0A)

- **Anexo (se o modelo permitir):**

  - Mapeamento de campo (somente 1 anexo).

Ao salvar a automação, você receberá um lembrete para verificar os gatilhos e filtros configurados.

![Imagem 7: Ao salvar a automação, você receberá um lembrete para verificar os gatilhos e filtros configurados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771103475/cc61b9051624e28b230efed9b0c3/image.png?expires=1786536000&signature=9dba3776e2b555f84a9d47353e78776aed09ac963e06bb1204f9d055fbc47842&req=dScgF8h%2BnoVYXPMW3nq%2BgZuPT87k4HzhodIpgyb8s6K1zw7h6jJqY3rx93UQ%0AL1FVaiLGkUUFx8uNMHa0BRj3UK4%3D%0A)

---

## 3.3) Limitador de envios ativos

O limitador permite definir uma **cota máxima de envios ativos por período**, controlando o volume de disparos feitos por automações. Essa configuração é obrigatória para utilizar automações periódicas (agendadas) e funciona também para automações genéricas e de funil.

A configuração é feita na **tela de integração Neppo** no Ploomes:

1. Acesse a tela de configuração da integração Neppo.
2. Ative o limitador de envios.
3. Defina o **período** (ex.: Mensal). Ao selecionar, o sistema exibe uma legenda com as datas do ciclo atual (ex.: "De 01/03/2026 até 31/03/2026").
4. Defina o **limite máximo** de envios para o período (número inteiro positivo).

Na mesma tela, você pode acompanhar o **status de consumo** da cota:

- **Contador de progresso** — mostra quantos envios foram realizados em relação ao limite (ex.: 85/100).
- **Badge "Limite atingido"** — aparece quando a cota é preenchida, junto com a quantidade de automações que foram bloqueadas.

![Imagem 8: Badge "Limite atingido" — aparece quando a cota é preenchida, junto com a quantidade de automações que foram bloqueadas.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2243142060/1f6bbbd5e956409a96b99e3c1320/image.png?expires=1786536000&signature=da114ad2bc4a23aa6d6bbcd1298dea7a9bc9da1307a2e7e5ba124040fd7e75db&req=diIjFch6n4FZWfMW3nq%2BgaZzjOqs%2B3Fe7u12MvWrTHnjmRexhBShLgEuFnTO%0AC82BaJ5me0abGXfFCsf5DDSjvRA%3D%0A)

⚠️ Quando o limite é atingido, **nenhum envio ativo por automação será realizado** até o próximo ciclo. As automações bloqueadas geram um **registro de interação** na timeline do contato com os detalhes do bloqueio (nome da automação e conteúdo da mensagem).

## 3.4) Execução da automação

- Automações periódicas (agendadas) estão disponíveis para envio ativo de WhatsApp, **desde que o limitador de envios esteja configurado**.
- Cada disparo fica registrado no **histórico de automações**.

  ![Imagem 9: Cada disparo fica registrado no histórico de automações .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771107019/b20b9befd1d2479b6bdf05e1b538/image.png?expires=1786536000&signature=cf57886f69051128641f0a8a9c7d8686162c75786933be6e5f77667d8ffb4065&req=dScgF8h%2BmoFeUPMW3nq%2BgS%2Fdh2A33znJNTznMAw7ynUjKJZ6YvoLb23LVgAZ%0A7TvgptjavaRTBKz4CZpbzMr9AIY%3D%0A)

---

## 4) Limitações e Observações

1. **Formato de telefone**

   - O número deve estar no formato **DDI + DDD + número**. Caso contrário, o envio falhará.
2. **Anexos**

   - Apenas **um anexo por envio** via mapeamento.
   - O modelo precisa prever anexo e estar aprovado pela Meta.
   - O arquivo enviado deve ser do mesmo tipo aprovado (ex.: PDF, imagem).
   - O arquivo deve estar num campo do Ploomes.
3. **Remetente**

   - Se o remetente selecionado **não for agente da Neppo**, o envio ocorrerá sem remetente.
4. **Custo por envio**

   - Cada mensagem enviada representa um **custo na sua conta Neppo**.
5. **Parâmetros da mensagem**

   - Todos os parâmetros devem estar preenchidos para que seja efetuado o disparo. Caso a opção de "Puxar valor de um campo" esteja selecionada, este campo deve estar preenchido — do contrário a automação irá gerar um erro.
6. **Automação periódica**

   - Disponível **somente com o limitador de envios ativo**. Sem o limitador configurado, automações periódicas não podem utilizar a ação de envio ativo de WhatsApp.
7. **Limite de envios**

   - Quando a cota do período é atingida, todos os envios ativos por automação são bloqueados até a renovação automática do ciclo. Um registro de interação é criado na timeline do contato informando o bloqueio.

---

## 5) Boas práticas 📌

- **Sempre revise os filtros da automação antes de ativar.**
- Evite condições muito amplas que possam gerar **alto volume de disparos** inesperados.
- Valide previamente o formato do campo de telefone para reduzir falhas de envio.
- **Configure o limitador de envios** com uma cota compatível com seu volume real de comunicação. Isso evita custos inesperados e garante que automações periódicas funcionem de forma controlada.
- Acompanhe o **contador de consumo** na tela de integração Neppo para antecipar quando a cota estiver próxima do limite.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
