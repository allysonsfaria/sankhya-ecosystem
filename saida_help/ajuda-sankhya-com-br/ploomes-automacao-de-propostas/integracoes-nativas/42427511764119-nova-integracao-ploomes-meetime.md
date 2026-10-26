---
id: "42427511764119"
titulo: "Nova Integração Ploomes <> Meetime"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427511764119-Nova-Integra%C3%A7%C3%A3o-Ploomes-Meetime"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:04:37Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12739857", "sync_hash_a6acb5f6d5ab"]
---

# Nova Integração Ploomes <> Meetime

## 1) Sobre a Integração com a Meetime

A integração entre **Ploomes** e **Meetime** conecta o CRM ao fluxo de **prospecção por cadências**. Os **leads são iniciados no Ploomes** e **enviados automaticamente para a Meetime** por meio de **automações de funil**. A partir daí, **atividades de cadência** e **resultados (ganho/perda)** retornam para o Ploomes, mantendo o histórico centralizado no CRM e permitindo o acompanhamento ponta a ponta.

**Importante:** nesta versão, o envio ocorre apenas por automação de funil (Ploomes → Meetime). Depois que o negócio (card) está integrado, há sincronização bidirecional de campos (ex.: nome, telefone, status do negócio, campos associados). A Meetime não cria negócios no Ploomes, mas pode criar contatos no Ploomes quando forem leads associados ao mesmo negócio já integrado.

**Como funciona (visão rápida)**

- Você define uma etapa do funil no Ploomes que dispara o envio do lead para a Meetime.
- A Meetime executa a cadência (ligações, e-mails, reuniões).
- Atividades e desfechos do lead voltam para o Ploomes como Registros de Interação e atualização de status do negócio/motivos de perda.
- O histórico permanece centralizado no Ploomes.

---

## 2) Benefícios principais

- **Evita retrabalho**: reduz entrada dupla de dados; o envio é automático e o retorno de atividades e status é registrado no CRM.
- **Mantém dados consistentes**: sincroniza campos chave (cadência, responsável, status, motivo de perda) entre Ploomes e Meetime.
- **Automatiza a prospecção**: cria/inscreve o lead na Meetime a partir de regras do funil no Ploomes, sem passos manuais.
- **Melhora o controle do funil**: permite avanço automático de estágios conforme o resultado da cadência (ganho/perda) e concentra o acompanhamento no CRM.

---

## 3) Pré-requisitos

- Ter uma conta **ativa** na Meetime.

- Ter acesso ao **Token da API** da Meetime (a autenticação é por conta; ao ativar, vale para todos os usuários da conta Ploomes).
- Ter uma conta Ploomes com permissão para ativar **integrações plug-and-play** e configurar automações de funil.

---

## 4) Ativando a nova versão de integração Ploomes <> Meetime

## 4.1) Visão geral: ativação da integração

A ativação da integração é feita dentro do Ploomes. Para ativar a integração, siga o passo a passo:

#### 1. No Ploomes, vá em Administração → Integrações plug-and-play → Meetime.

![Imagem 1: 1. No Ploomes, vá em Administração → Integrações plug-and-play → Meetime .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811747496/c3e33de66b0716c6e3a2fbfa3bc6/image%2B-2826-29.png?expires=1786536000&signature=dbd61f961e2f9e5998c4b191a7ba47e12df00c53fd33a2fef150524f006f6603&req=dSgmF856moVWX%2FMW3nq%2BgX6jenQJQCTVvlqq65mjBK5G%2Fz2BP8XuSYRMlpNc%0A4pys9VCdyOA4v8OPhVrayFNI23o%3D%0A)

#### 2. Escolha o fluxo

- Na primeira tela, selecione **uma** das opções:

  - **Recebimento de leads ganhos** (fluxo anterior): cria/atualiza no Ploomes somente quando o lead é ganho na Meetime.
  - **Centralização de leads no CRM** (novo fluxo - recomendado e descrito nesta documentação): Ploomes → Meetime via automação de funil, com retorno de atividades, status e motivos para o Ploomes (histórico centralizado).
- Escolha **Centralização de leads no CRM** e clique em **Continuar** após a seleção.

![Imagem 2: Escolha Centralização de leads no CRM e clique em Continuar após a seleção.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811748172/bd6c93d237dfabbdfaf2cb4c9ac5/image+%2827%29.png?expires=1786536000&signature=157095bcf1f5467edbbec9e532e9bc45a5a07c535e92d3360249aa447a3bb43d&req=dSgmF856lYBYW%2FMW3nq%2BgVsT%2BEZxZ3vUok8LOp68%2FI6mkvsKf2ZbGAWemXBT%0AG7KaLkRlqN0I14Ts5tV8JDDqeEY%3D%0A)

**Importante:** o fluxo Recebimento de leads ganhos não pode ser usado na mesma conta junto com o fluxo Centralização de leads no CRM.

#### 3. Obtenha o Token da API (Meetime)

No painel da Meetime: Menu principal (direita) → Integrações → API. Copie o Token da conta (um token por conta).

![Imagem 3: No painel da Meetime: Menu principal (direita) → Integrações → API. Copie o Token da conta (um token por conta).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811749191/b45050122da555695e7c8f790d2c/image+%2828%29.png?expires=1786536000&signature=13293bce25d9d6415d12119cc5a3c2db93e58fc5e6c8d3a30945f03bf08d488a&req=dSgmF856lIBWWPMW3nq%2BgWM9oAizqab4nFlCTKaevfYhBLu022gqdjOTtOAD%0ADjjyoT%2BaECCDQ8DZO6FE1bXHZrY%3D%0A)

#### 4. Valide o Token no Ploomes

Cole o token no campo **Token da API** e clique em Validar token.

![Imagem 4: Cole o token no campo Token da API e clique em Validar token.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811749630/f94def8f63f7a1bd7166344eaa45/image+%2829%29.png?expires=1786536000&signature=a7d6d98b11f2f9a34af5172919fd29de20975f89a35e45dd7c90d22225202e6b&req=dSgmF856lIdcWfMW3nq%2BgcaOr3ozKKVUGy0q6gxgG%2FDUHLcI4qtxmIMQ5A1j%0AACY0Bgsn5bNDQQB6oxckgcCgFd0%3D%0A)

Nota: se o token for inválido/expirado, o Ploomes exibirá um toaster de erro como na imagem abaixo:

![Imagem 5: Nota: se o token for inválido/expirado, o Ploomes exibirá um toaster de erro como na imagem abaixo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811749942/d5fa20ad4b2f930f6e142d220bcd/image+%2830%29.png?expires=1786536000&signature=a6bdec86015c45a1ff6c3beacc12e4a92ca86d0d5e9905fd2b5776f69c963494&req=dSgmF856lIhbW%2FMW3nq%2BgXJviuubZjE9SYXJFed6311bxIyJjRfCCXH1VqXr%0A9qj0gdCy0tg4ngy%2BE81vMBFttoI%3D%0A)

#### 5. Habilite a integração

Com o token validado, clique em Habilitar integração.

![Imagem 6: Com o token validado, clique em Habilitar integração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811750287/80bd92df9595255586380113e9e7/image+%2831%29.png?expires=1786536000&signature=48ed841b8e88a34490b895b5e9f000cd8bb9a84792ee0bb4f108c69f798126ce&req=dSgmF857nYNXXvMW3nq%2BgcujLPhs2PCAaPQbITKd7Au3hJOLLgk0F15ixxjt%0AM9WKM3Lmw7VZ3sERLrEQShUA47E%3D%0A)

#### 6. Configure as seções “Leads” e “Vendedores”

Após habilitar, serão exibidas as configurações de **Leads** (mapeamentos e regras da integração) e **Vendedores** (sincronização de usuários). Os detalhes dessa configuração estão na sessão seguinte desta documentação.

![Imagem 7: Após habilitar, serão exibidas as configurações de Leads (mapeamentos e regras da integração) e Vendedores…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811750557/80103b665e4e15cb00ccbc26a988/image+%2832%29.png?expires=1786536000&signature=d404c1a545b01076e4cbc6adb0fb4433e74f75b072fbe3c1e5783c407068f66c&req=dSgmF857nYRaXvMW3nq%2BgXT57Uc4snez4vqajwK3ilU5Z3LoHbDW5yqi1UyQ%0Atwj9csELuya6pPQ%2BNmweLjli%2BXs%3D%0A)

Entraremos nos detalhes dessas configurações na sequência do artigo.

#### 7. Ative a integração

Depois de revisar e salvar as configurações, clique em Ativar integração.

![Imagem 8: Depois de revisar e salvar as configurações, clique em Ativar integração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811751184/b4ea51545d09157fe9cef2d6aff8/image+%2833%29.png?expires=1786536000&signature=8b1a22dd8fb749c3526e0d048f31ac9329ae4b85d1ed136187f5ec6d16f6e2c8&req=dSgmF857nIBXXfMW3nq%2Bgd1MuqwxaHpK7aSIXGKiJho7CW9He2WMBlHkje9V%0ARA5m%2FtXKSif4uIlpCW9Rrsv8xXU%3D%0A)

---

## 4.2) Configurando a sessão de Leads (Pessoas, Empresas e Negócios)

### Configuração da Seção Leads

Após ativar a integração, o usuário poderá iniciar a configuração da seção **Leads**.

Nessa etapa, a interface já indica que há criação e edição de dados entre Ploomes e Meetime.

Mais adiante nesta documentação será explicado detalhadamente como essas trocas acontecem; por enquanto, o foco aqui é apenas o processo de configuração.

![Imagem 9: Mais adiante nesta documentação será explicado detalhadamente como essas trocas acontecem; por enquanto, o foco aqui é…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811751923/0ff7f0a609a05a96a270037f7c5c/image+%2834%29.png?expires=1786536000&signature=c4994718bc2dee452c66e3079b356d8e6ec1afdb46e9479c072a66fe6ff52d83&req=dSgmF857nIhdWvMW3nq%2BgTP0Nuw5lLXh%2FjpyKFZWzNt0KtHpUtuXsat47QJf%0AlZWdBn%2BYURriwPWAqP5kmxik9Cg%3D%0A)

#### 1. Quais funis poderão enviar leads

O primeiro passo é definir quais funis do Ploomes poderão enviar leads para a Meetime. Ou seja, em quais funis será possível configurar automações de envio.

![Imagem 10: O primeiro passo é definir quais funis do Ploomes poderão enviar leads para a Meetime. Ou seja, em quais funis será…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811752378/e61935a6abff44262804112a4957/image+%2835%29.png?expires=1786536000&signature=08951f95291380d70ef02239f6f3467e88108eec39270a5e75eb5cc9dfe4986a&req=dSgmF857n4JYUfMW3nq%2BgYE7BDCKkPS2vcmt5ipW%2FfISOfqMK1uVg07qn2Mj%0AmXkoZhAFlBkOsopB0OHVe9ZZDo0%3D%0A)

Este campo é **múltiplo**, permitindo **selecionar mais de um funil** por conta.

É importante destacar que, nesta etapa, você apenas habilita os funis que terão acesso à automação de envio.

A **configuração da automação em si** (ou seja, o envio do lead para a Meetime ao atingir determinada etapa do funil) será feita diretamente dentro da tela de automações do funil.

**Importante:** habilitar um funil aqui não envia leads automaticamente — apenas permite que esse funil use a automação “Enviar lead para a Meetime” em suas regras.

![Imagem 11: Importante: habilitar um funil aqui não envia leads automaticamente — apenas permite que esse funil use a automação…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811752646/205274f7f6cb53021dd5199e1980/image+%2836%29.png?expires=1786536000&signature=3cb191e9e43bf1fc3aa3b465849cf4a8067651b14a1de3df0e2c17abc617cad7&req=dSgmF857n4dbX%2FMW3nq%2BgXiWaD32WMiHd%2BEGz8gmLNT0EI34ezFLHJisapAc%0AsFFmMB0XnrZMu0dx4JLyirvAwFU%3D%0A)

#### 2. O que fazer quando leads enviados forem ganhos na Meetime

Após configurar os funis habilitados para envio, é necessário definir o comportamento do Ploomes quando um lead for ganho na Meetime.

Em outras palavras, considerando que os negócios (cards) e leads estão integrados entre as plataformas, o ganho do lead na Meetime precisa refletir uma ação correspondente no Ploomes.

**Ações configuráveis ao ganhar um lead na Meetime**

Quando um lead integrado é marcado como ganho na Meetime, é possível definir qual será a ação aplicada automaticamente ao negócio correspondente no Ploomes:

- **Ganhar o negócio no Ploomes**
- **Manter o negócio na mesma etapa**
- **Avançar o negócio para uma etapa específica**

Exemplo: se o funil de “Prospecção” tiver uma automação configurada e o lead for ganho na Meetime, o Ploomes pode automaticamente marcar o negócio como ganho, movê-lo para a próxima etapa do funil ou mantê-lo na mesma etapa, conforme a ação definida.

![Imagem 12: Exemplo: se o funil de “Prospecção” tiver uma automação configurada e o lead for ganho na Meetime, o Ploomes pode…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811753113/46312f75a60e8c3cd52d29693c09/image+%2837%29.png?expires=1786536000&signature=de6c674009ccb446b248c761e9429534dc61010cec4e095142c0e2076f0d47f0&req=dSgmF857noBeWvMW3nq%2BgTuRA4Jb4po4nOlXZSjP2eQi%2FFfzkw%2BsJ4FYjqTl%0AGSNliNxxKJlcKMvU6zPqd3vr3Es%3D%0A)

**Lógica de exibição das configurações**

Para evitar conflitos entre cadências e funis, o Ploomes aplica regras específicas na exibição das opções:

- Para um mesmo funil e uma mesma cadência, só pode existir uma ação configurada.
- Ao selecionar um funil (primeiro dropdown), o Ploomes verifica quais cadências já estão vinculadas a esse funil com ações configuradas na Meetime.
- As cadências já utilizadas em outras configurações não aparecerão como opção no segundo dropdown (de cadências).

Essa lógica garante que não haja duplicidade de ações entre cadências associadas ao mesmo funil, mantendo a configuração limpa e sem sobreposições.

[GIF animado: Imagem 13: Essa lógica garante que não haja duplicidade de ações entre cadências associadas ao mesmo funil, mantendo a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811753762/70cf584f45cfbaa2625c9b1958e2/gif+meetime+cadencias+%281%29.gif?expires=1786536000&signature=5540dd24d405451754390bd7b96f499455e17c2131f0391dd10f7585e1381dce&req=dSgmF857noZZW%2FMW3nq%2BgZg9vChZjLbqq1XNsppIBIxFr%2F3BuWQDGzb1TVCj%0AJxvB1JWRem0OLtgqjvX3O0WoXJo%3D%0A)

---

## 4.3) Mapeamento de Campos

A sincronização entre **Ploomes** e **Meetime** conta com **campos pré-associados automaticamente** e **campos personalizáveis**, que o usuário pode associar manualmente.

É importante que os campos que serão associados já existam na Meetime.

No Ploomes, é possível criar novos campos diretamente durante o mapeamento — porém não é possível criar campos na Meetime a partir dessa tela.

**Entidades mapeáveis**

Três entidades do Ploomes podem ser associadas à mesma entidade de **Lead** na Meetime:

- Campos de Pessoa (Ploomes) ↔ Campos de Lead (Meetime)
- Campos de Empresa (Ploomes) ↔ Campos de Lead (Meetime)
- Campos de Negócio (Ploomes) ↔ Campos de Lead (Meetime)

#### 1. Pessoa ↔ Lead

Nesta seção, o usuário define quais campos do tipo Pessoa no Ploomes serão associados a campos de Lead na Meetime.

**Campos pré-associados (padrão da integração – não editáveis):**

- Nome (Pessoa) ↔ Nome (Lead)
- E-mail (Pessoa) ↔ E-mail (Lead)
- Telefone (Pessoa) ↔ Telefone (Lead)

  - Em caso de múltiplos telefones, **todos os números são enviados para a Meetime**.

![Imagem 14: Em caso de múltiplos telefones, todos os números são enviados para a Meetime .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811754902/abe5391fcc1143acde73c2b8f128/image+%2838%29.png?expires=1786536000&signature=03cc340f047dff141ce539267131ef215fc6b7fe60aad79faccab5b7fab0ab8d&req=dSgmF857mYhfW%2FMW3nq%2BgT%2FBZcoDbcvaJ2dXgLe2Rl96sgCaVJTkg3hdSL8F%0AZYV9%2FOQKuFxH6G3WqVLDDr29J4k%3D%0A)

#### 2. Empresa ↔ Lead

Nesta seção, o usuário define campos do tipo Empresa no Ploomes a serem associados a campos de Lead na Meetime.

**Campos pré-associados (padrão da integração – não editáveis):**

- Nome (Empresa) ↔ Nome (Lead)
- Telefone (Empresa) ↔ Telefone (Lead)

  - Em caso de múltiplos telefones, **todos os números são enviados para a Meetime**.

![Imagem 15: Em caso de múltiplos telefones, todos os números são enviados para a Meetime .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811755169/8e2a1b24ca7ee6c7a6ab1e71b455/image+%2839%29.png?expires=1786536000&signature=e112c7bf354da8d5336d079ac5f875804ecb4d3d28e3aff4a37bbd32a89e45f3&req=dSgmF857mIBZUPMW3nq%2BgTwp39sIpvN5CJFG1dsRmCZpML8ceAl0ftQphgxZ%0ABcqXvg7BsNo7EjY5e88Dzc3lEp0%3D%0A)

#### 3. Negócio ↔ Lead

Nesta seção, o usuário define campos do tipo Negócio no Ploomes para associar a campos de Lead na Meetime.

#### Campos pré-associados (padrão da integração – não editáveis):

- **Contatos Relacionados** ↔ **Leads associados a um mesmo negócio**

  - O campo nativo Contatos Relacionados no Ploomes representa os leads vinculados ao mesmo negócio.
  - **Ploomes → Meetime:** se um negócio for integrado com contatos relacionados, serão criados **múltiplos leads** na Meetime, todos associados ao mesmo negócio.

    - Importante: após a integração do card e do lead, **não é possível adicionar novos contatos relacionados pela Ploomes** para gerar leads na Meetime. Essa associação deve ser feita **antes do envio** do card pela automação de funil.
  - **Meetime → Ploomes:** após integrado, ao adicionar leads associados a um mesmo negócio na Meetime, serão criados **contatos relacionados** no Ploomes.
  - A integração **não cria duplicatas** de pessoas ou empresas na Ploomes:

    - Para **Pessoas**, o sistema verifica o **e-mail** antes de criar.
    - Para **Empresas**, o sistema verifica o **CNPJ** (quando mapeado) e o **Nome da Empresa**.
- **Responsável mais recente (Meetime)** ↔ **Responsável (Lead)**

  - Campo criado da Ploomes automaticamente na ativação da integração.
  - Define o responsável pelo lead no momento do envio e é atualizado caso o responsável mude na Meetime.
  - Pode ser alterado no Ploomes **até o envio do card** para a Meetime.
  - Após a integração, **só a Meetime pode atualizar** esse campo.
  - Caso o usuário tente alterar pelo Ploomes, o valor é revertido e é criado um **Registro de Interação** com o motivo do erro.
- **Responsável inicial (Meetime)** ↔ **Responsável (Lead)**

  - Campo da Ploomes de dados criado na ativação da integração, **não editável** no CRM.
  - Armazena quem foi o **primeiro responsável** pelo negócio, garantindo **rastreabilidade** histórica.
- **Cadência mais recente (Meetime)** ↔ **Cadência (Lead)**

  - Campo da Ploomes é criado na ativação da integração.
  - Armazena a **última cadência enviada** para a Meetime via automação de funil.
  - Campo **bloqueado para preenchimento manual**, atualizado automaticamente pela Meetime.
- **Cadência inicial (Meetime)** ↔ **Cadência (Lead)**

  - Campo da Ploomes é criado na ativação da integração.
  - Armazena a **primeira cadência enviada** para a Meetime.
  - Campo **somente para dados**, não pode ser alterado após o registro inicial.

![Imagem 16: Campo somente para dados , não pode ser alterado após o registro inicial.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811756752/2c2d1428d1776055a2ee5a3524ac/image+%2840%29.png?expires=1786536000&signature=8ea23bad3c40f0289b14992f74336a99eb97525381a03c26f1a136bba61d23c6&req=dSgmF857m4ZaW%2FMW3nq%2BgUagsCXojuN1QvWS6%2BSvcbHlv839GOgXLtdbU0vx%0ARTsHlekPzkt6AIRg2L0y34mI9nY%3D%0A)

#### Regras de Mapeamento de Campos (Ploomes ↔ Meetime)

Para manter a integridade e consistência dos dados, a tela de mapeamento aplica **filtros automáticos** que impedem associações entre **tipos de campos incompatíveis**.

**Exemplo:**

Não é possível associar um campo Número no Ploomes a um campo Seleção na Meetime, pois isso geraria inconsistência e falhas de interpretação na sincronização.

Essas restrições funcionam como uma camada de proteção, garantindo que o mapeamento entre plataformas ocorra de forma segura e coerente.

| **Campos Ploomes** | **Correspondência do tipo de campo na Meetime** |
| --- | --- |
| Texto Simples (250 caracteres) | Texto (255 caracteres) |
| Texto Multilinha | Texto longo |
| Número Inteiro | Texto (255 caracteres) |
| Moeda | Texto (255 caracteres) |
| Número com casas decimais ilimitadas | Texto (255 caracteres) |
| Opções pré-cadastradas | Campo de seleção, Texto (255 caracteres) |
| Data | Texto (255 caracteres) |
| Horário | Texto (255 caracteres) |
| Checkbox | Campo de seleção, Texto (255 caracteres) |
| CPF | Texto (255 caracteres) |
| CNPJ | Texto (255 caracteres) |
| % Porcentagem | Texto (255 caracteres) |
| Endereço | Texto (255 caracteres) |
| Imagem | Não suportado |
| Anexo | Não suportado |
| Cor | Não suportado |
| Desenvolvedor | Não suportado |
| Usuário | Campo de seleção, Texto (255 caracteres) |
| Produto | Campo de seleção, Texto (255 caracteres) |
| Cliente | Campo de seleção, Texto (255 caracteres) |
| Símbolo de moeda | Texto (255 caracteres) |

[GIF animado: Imagem 17: Texto (255 caracteres)](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811758414/831143b704539315ce958df695bc/gif+meetime+mapeamento+%281%29.gif?expires=1786536000&signature=c99370423ab75a437c9b3a5c6e2f12264e364d24be46f4848b665b7604fe4882&req=dSgmF857lYVeXfMW3nq%2BgRRT14qKcqmUbL%2BBA4if91mxX67%2BAwimu0KeiHNe%0Aj%2FYu9RcyR2RZPpFqhRgm0L50j5I%3D%0A)

---

## 4.4) Configuração da Seção de Vendedores (Usuários)

Ao ativar a integração, ocorre automaticamente a **sincronização dos usuários da Meetime com os usuários do Ploomes**.

Em outras palavras, **todo usuário existente na Meetime terá um correspondente no Ploomes**, garantindo que os responsáveis pelas cadências e leads estejam sincronizados.

O campo chave para essa sincronização é o e-mail. É por meio dele que o sistema identifica se deve associar um usuário existente ou criar um novo usuário na conta Ploomes.

#### Comportamento da sincronização

- **Meetime → Ploomes:** todos os usuários da Meetime são sincronizados com a conta Ploomes.

  - Usuários da Ploomes não são criados na Meetime.
- A sincronização é **contínua**: novos usuários criados na Meetime após a ativação também serão criados automaticamente no Ploomes.

#### Regras de criação e associação de usuários

A lógica aplicada durante a sincronização segue os seguintes cenários:

- Se o e-mail já existir na Ploomes:

  O usuário é associado ao usuário existente, sem alterações de nome ou perfil.
- Se o e-mail não existir e o nome estiver preenchido na Meetime:

  É criado um novo usuário no Ploomes, utilizando o nome e e-mail da Meetime, com o perfil definido pelo administrador.
- Se o e-mail não existir e o nome estiver em branco na Meetime:

  É criado um novo usuário no Ploomes utilizando o e-mail da Meetime como nome padrão, além do perfil selecionado.

#### Configuração do perfil padrão

A única configuração disponível nesta seção é a escolha do perfil de usuário padrão que será atribuído aos novos usuários criados pela integração.

Essa configuração é feita em um **campo do tipo dropdown**, que lista todos os **perfis disponíveis** na conta Ploomes.

Após selecionar o perfil e ativar a integração, todos os novos usuários criados a partir da Meetime já serão registrados no Ploomes com esse perfil padrão.

**Importante:** a manutenção dessa associação é contínua.

Qualquer novo usuário criado na Meetime após a ativação da integração também será criado automaticamente no Ploomes, preservando a correspondência entre as contas.

[GIF animado: Imagem 18: Qualquer novo usuário criado na Meetime após a ativação da integração também será criado automaticamente no Ploomes,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811759672/4b4c989c65d5a450a83515627b85/GIF+VENDEDORES+%281%29.gif?expires=1786536000&signature=cd6a2b373377d90da85800bfb2f030e1f4111735585c1edbbf0138b2f54dc906&req=dSgmF857lIdYW%2FMW3nq%2Bgba0U%2BnHUWmKfn3Oi2n6k3B%2F0C%2FN1AWtwXIoKwpF%0A1DfcA1H5busYJPB44FZO0m0koYM%3D%0A)

---

## 4.5) Configuração de Automação de Funil

Depois de ativar a integração, definir os funis habilitados e concluir o mapeamento de campos na tela de Integrações Plug and Play, o usuário poderá configurar automações de funil no Ploomes.

Essas automações determinam **quando** (em qual etapa do funil) e **como** (com base em filtros e gatilhos) os **leads serão enviados para a Meetime**.

A opção de automação ficará disponível **somente nos funis selecionados** durante a configuração da integração, permitindo **personalizar as regras de envio** conforme a necessidade de cada operação.

#### Como configurar

1. Acesse o **funil desejado**.
2. Clique em **“Configurar Automações”**.
3. Crie uma nova automação e defina os seguintes campos:

- **Descrição da Automação**

  Nome ou descrição livre para identificar a regra.
- **Gatilho**

  Define o momento em que o lead será enviado para a Meetime.

  Opções disponíveis:

  - **Card entrou neste estágio**
  - **Card reaberto neste estágio**

  Importante: os gatilhos “Card ganho” e “Card perdido” não podem ser utilizados para o envio à Meetime.

  Esses status representam o encerramento da prospecção:

  - Quando o lead é perdido na Meetime, o card correspondente é perdido no Ploomes.
  - Quando o lead é ganho na Meetime, o card pode ser ganho no Ploomes, conforme definido na configuração de Leads.

- **Filtros**

  Permitem definir **critérios adicionais** para o disparo da automação (ex.: tipo de produto, responsável, segmento etc.).
- **Ação ao ser disparada**

  Selecione a ação:

  **“Enviar lead para Meetime”**.

#### Automação: Enviar Lead para a Meetime

Ao configurar a automação, o usuário deverá definir **qual cadência da Meetime** será aplicada ao lead criado a partir do Ploomes.

O campo de seleção de cadência é integrado diretamente com as cadências ativas na conta da Meetime, garantindo que o usuário visualize e escolha entre as cadências existentes.

Assim, é possível determinar **para qual cadência** os leads enviados pela automação serão inscritos na Meetime.

#### Comportamento inicial da cadência

Além da escolha da cadência, o usuário deve definir **como o lead será inserido no fluxo de prospecção**:

- **Início imediato**

  O lead é enviado e **disponibilizado automaticamente** para execução na Meetime, iniciando a cadência assim que o lead é criado.
- **Aguardar início**

  O lead é enviado para a Meetime, mas **permanece aguardando o vendedor** iniciar manualmente a prospecção de novos leads.

[GIF animado: Imagem 19: O lead é enviado para a Meetime, mas permanece aguardando o vendedor iniciar manualmente a prospecção de novos leads.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1811760671/7a07e081876b47c492020999ddb9/gif+-+configurando+automa%C3%A7%C3%A3o+%281%29.gif?expires=1786536000&signature=aa6c279b45f14fc420c84c718c8c69d2582e631f6d6c4f255312ef3b4227b40d&req=dSgmF854nYdYWPMW3nq%2BgZcGOOeUlSfpDqxTwWSFt6YU33PFycswaDKaVEzy%0A5SEGRiogbIM6TOaRvldQAPEkBh4%3D%0A)

---

## 5. Utilizando a integração

Após **ativar a integração** e **configurar a automação de funil**, o novo fluxo da integração Ploomes ↔ Meetime já pode ser utilizado.

Abaixo, apresentamos um **exemplo prático** de como o processo ocorre do início ao fim.

#### 1. Exemplo de Configuração Utilizada

Neste exemplo, foi configurada uma automação para o **Funil de Novos Clientes** com os seguintes parâmetros:

- **Etapa de envio para a Meetime:** “Enviar para a Meetime”
- **Comportamento de leads ganhos:** o **card será marcado como ganho** no Ploomes
- **Cadência selecionada:** “Cadência de Prospecção”

[GIF animado: Imagem 20: Cadência selecionada: “Cadência de Prospecção”](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812655761/61a915298be6bbff777781005d0a/gif+meetime+2.gif?expires=1786536000&signature=80f93812fed378c9a104c8f159787144c3470b5ff4b61262c803eb50bc66f343&req=dSgmFM97mIZZWPMW3nq%2BgeYP3e1mMFL0s39SATyf0%2F0t1En4YIyGqT2W66JB%0AxNNPwVDQ%2BROZbjwfmpPLnlmTYL4%3D%0A)

[GIF animado: Imagem 21: GIF animado: Imagem 20: Cadência selecionada: “Cadência de Prospecção”](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812656375/e8df11c145e287e8df1dbf3d6149/gif+meetime+1.gif?expires=1786536000&signature=5b348efd7f1bc69bb0767b3b66054fe744c4999f27c353f4bc2046c59e479011&req=dSgmFM97m4JYXPMW3nq%2BgS8ss1Nkvn9Rv%2FOeCfW7jqOhAmb804hXF4amMii4%0AqZOkt2jj%2B9H4AryNWoIXeO7PPGg%3D%0A)

#### Importante - Campo de Contatos Relacionados

- **Campo de Contatos relacionados** — opcional, mas ao preencher com contatos da Ploomes, **geram múltiplos leads** vinculados ao mesmo negócio na Meetime

Assim, quando o card é enviado, todos os contatos relacionados são criados como leads associados ao mesmo negócio (mesmo DealID).

#### 2. Criação e Envio do Card

Um novo **card** é criado no funil, com os **campos principais preenchidos**, incluindo:

- **Cliente (Pessoa ou Empresa)**
- **Responsável mais recente (Meetime)** — campo que determina qual usuário sincronizado com a Meetime será responsável pelo lead

Quando o card é movido para a etapa “Enviar para a Meetime”, seja manualmente ou por outra automação, e atende aos filtros e gatilhos definidos, o lead é automaticamente criado na Meetime e atribuído ao responsável configurado.

[GIF animado: Imagem 22: Quando o card é movido para a etapa “Enviar para a Meetime”, seja manualmente ou por outra automação, e atende aos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812670780/88a716c5b3743f9fec1bfe40eb75/prospec%C3%A7%C3%A3o.gif?expires=1786536000&signature=47a7484c07b4f7d5bc528a7e5e6722e7d973c97562b967a64e9e5f04128a6eaa&req=dSgmFM95nYZXWfMW3nq%2BgXwshHjYxN955MsWqMsa6D4HdpFO77UU326HlY8u%0AWeEhXaw4ZX%2BbwVEEJez2PbEDA1A%3D%0A)

#### 3. Execução da Cadência na Meetime

Na Meetime, o responsável executa as **atividades da cadência de prospecção** configurada (ligações, e-mails, reuniões etc.).

Cada atividade registrada na Meetime gera um **Registro de Interação correspondente** no Ploomes, garantindo que o histórico de relacionamento permaneça centralizado.

Registros de interação a partir de atividades de cadência são criadas de acordo com o lead prospectado. A atividade de cadência executada é enviada para:

- A **Pessoa (Contato)** correspondente - seja contato principal ou contato relacionado do negócio
- O **Negócio (Card)** associado

[GIF animado: Imagem 23: O Negócio (Card) associado](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812673189/4e0e3691c4f96b130224fd5849f5/registro+de+atividade.gif?expires=1786536000&signature=42490027e0df2ea8e71525c591badccf932b259dcb1d23615c4ccd4fd8bad602&req=dSgmFM95noBXUPMW3nq%2BgVEfoflPa21Mcq%2BAwgPxOOxLFTxgvUNZqKvXRALu%0AjGkRO9Es6UDOvy%2FI5vI8wvOMvjY%3D%0A)

#### Correspondência entre Atividades e Registros

| Atividade na Meetime | Registro criado na Ploomes |
| --- | --- |
| Pesquisa | Registro simples |
| Ligação | Registro de telefone |
| E-mail | Registro de e-mail |
| Social Point | Registro simples |
| Social Point – WhatsApp | Registro de WhatsApp |
| Reunião | Registro de reunião |

#### 4. Adição de Novos Leads pela Meetime

Durante a prospecção, o usuário pode adicionar novos leads associados ao mesmo negócio diretamente pela interface da Meetime.
Esses leads adicionais são sincronizados e passam a aparecer no Ploomes como Contatos Relacionados do card original.

[GIF animado: Imagem 24: Durante a prospecção, o usuário pode adicionar novos leads associados ao mesmo negócio diretamente pela interface da…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812709703/5f307da73267d14a8d0b66529c17/adicionar+leads+na+meetime.gif?expires=1786536000&signature=06a82dc03dcb0b42a511bd0fd70331d52867d613c3b7bc064bc16a85614b3934&req=dSgmFM5%2BlIZfWvMW3nq%2Bgcoft5qglUikuuq0NO4uyK6mdVBYqE5%2FElStWlGi%0A4jtaohrdHkhpytgTBRU3X4XfZis%3D%0A)

#### 5. Movimentação de Etapa pela Meetime

Também é possível movimentar o lead pelas **etapas do funil integrado**, diretamente pela Meetime.

[GIF animado: Imagem 25: Também é possível movimentar o lead pelas etapas do funil integrado , diretamente pela Meetime.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812714553/8dc3a88b47e973b0581ea9ad9362/movimentar+pela+Meetime.gif?expires=1786536000&signature=d872edf402fd31aa63ba63d270a5603ebb8345c0179c582423aac1ec41cff02b&req=dSgmFM5%2FmYRaWvMW3nq%2BgZIbSN%2BrSB%2BYh7Do20W33xAUID%2FUmSktWc7z%2F76I%0Al8yuzGY%2FujAfAGN9n7f1SiZND5o%3D%0A)

**Importante:** se o funil no Ploomes possuir **checklists obrigatórios**, a movimentação **não ocorrerá** até que todos os itens sejam preenchidos.
Isso garante a integridade do processo de vendas e o cumprimento das regras configuradas.

#### 6. Conclusão da Cadência: Lead Ganho ou Perdido

Ao final da cadência, o usuário pode **ganhar** ou **perder** o lead.

O fluxo da integração se encerra quando o lead é ganho ou quando todos os leads vinculados ao negócio são perdidos.

#### 6.1 Lead Ganho

- Ao marcar um lead como **ganho na Meetime**, é possível definir se o negócio também será ganho, movimentado ou mantido na mesma etapa na Ploomes (opção configurável na integração).
- Caso existam **outros leads associados ao mesmo negócio**, a Meetime perguntará se o usuário deseja **perder os demais.**

[GIF animado: Imagem 26: Caso existam outros leads associados ao mesmo negócio , a Meetime perguntará se o usuário deseja perder os demais.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812717144/5b3b8bf02deffe1e623e008a442a/ganhar+lead.gif?expires=1786536000&signature=95db1ca54eca689f9a61987317099eb0ecf755deaf2ec3bffcf8f44fc18368d0&req=dSgmFM5%2FmoBbXfMW3nq%2BgW1igKXK3NE11JZa96Mp4HcNybX0nSCLNQ0gIQ0F%0AFl90KRw1t6iLZTiMdy8MCF0%2Bbos%3D%0A)

#### 6.2. Lead Perdido

- Ao marcar um lead como perdido na Meetime, é possível definir se o negócio também será perdido na Ploomes.
- Se houver mais de um lead associado, será perguntado se deseja perder os demais leads:

  - Caso **sim**, o negócio será perdido obrigatoriamente, e o **contato principal** será atualizado.
- Se todos os leads relacionados ao negócio forem marcados como perdidos, o card será automaticamente marcado como perdido na Ploomes.

Observação:

Diferente dos leads ganhos (que possuem configuração opcional de ação), **leads perdidos sempre resultam na perda do negócio** correspondente no Ploomes.

[GIF animado: Imagem 27: Diferente dos leads ganhos (que possuem configuração opcional de ação), leads perdidos sempre resultam na perda do…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1812729251/0328f10b6c17c5ef6f56e33fdbe9/perder+lead.gif?expires=1786536000&signature=b47adbebf95a69328637b33ac7e5f564d6e6329d7c4a88fac2daf7be52e9f073&req=dSgmFM58lINaWPMW3nq%2BgSArSnJl2e6PX%2FMbzT%2BGQ9QWQiH8op1iwBx0BcBg%0A2Vm806lj%2FbEX6eS2RfOakw54f6I%3D%0A)

#### 6.3 Sincronização de Motivos de Perda

Os **motivos de perda** são **sincronizados automaticamente** entre o Ploomes e a Meetime.
Essa sincronização garante que os motivos utilizados pelos vendedores na Meetime estejam sempre alinhados aos motivos configurados nos funis correspondentes da Ploomes.

**Como funciona**

- Todos os motivos de perda cadastrados no funil integrado da Ploomes são exibidos automaticamente na Meetime, no campo “Motivo de perda”.
- Quando o usuário for registrar a perda de um lead na Meetime, ele verá exatamente os mesmos motivos disponíveis na Ploomes.
- O motivo selecionado na Meetime será sincronizado de volta para o Ploomes, mantendo o histórico e os relatórios de perda consistentes entre as plataformas.

#### Regras importantes

- Apenas os motivos criados no funil correspondente da Ploomes aparecem na Meetime.
- Caso um motivo de perda seja excluído ou alterado na Ploomes, a mudança é refletida automaticamente na Meetime.
- Essa sincronização garante rastreabilidade total dos dados e evita divergências entre os relatórios de perda das duas plataformas.

#### 7. Envio de Anotações e Atualizações

Sempre que um lead integrado a um card é ganho ou todos os leads integrados a um card são perdido, as anotações da Meetime são enviadas para o Ploomes, criando registros no Contato principal e nos Contatos relacionados.

Quando um **lead relacionado é marcado como ganho ou perdido**, a atualização é enviada para:

- A **Pessoa (Contato)** correspondente
- O **Negócio (Card)** associado

Esse envio ocorre **mesmo que o negócio ainda esteja aberto**, garantindo que o histórico de interações permaneça atualizado em tempo real.

---

## 6. Glossário da Integração Ploomes ↔ Meetime

| Termo | Definição |
| --- | --- |
| **Lead (Meetime)** | Representa um contato em prospecção dentro da Meetime. É criado a partir de um card (negócio) enviado pelo Ploomes. |
| **Card / Negócio (Ploomes)** | Registro principal de oportunidade no Ploomes, que pode conter pessoa, empresa, produtos e informações de venda. É o item integrado à Meetime como lead. |
| **Contato Principal** | Pessoa vinculada ao negócio no Ploomes que será o lead principal na Meetime. |
| **Contatos Relacionados** | Pessoas adicionais vinculadas a um mesmo negócio no Ploomes. Na Meetime, correspondem a múltiplos leads associados ao mesmo DealID. |
| **Responsável mais recente (Meetime)** | Campo criado automaticamente na ativação da integração. Indica o responsável que será enviado para a Meetime e atualizado posteriormente pela plataforma. |
| **Responsável inicial (Meetime)** | Campo de registro histórico que armazena quem foi o primeiro responsável pelo lead no momento da criação. Não é editável. |
| **Cadência (Meetime)** | Sequência de atividades de prospecção (ligações, e-mails, reuniões, etc.) configurada na Meetime para execução automática ou manual. |
| **Cadência mais recente (Meetime)** | Campo criado no Ploomes que indica a última cadência enviada à Meetime. É atualizado pela integração. |
| **Cadência inicial (Meetime)** | Campo criado no Ploomes que registra a primeira cadência enviada à Meetime para o lead. Serve para rastreabilidade. |
| **Funil Integrado** | Funil do Ploomes habilitado para utilizar a automação “Enviar lead para a Meetime”. Somente os funis marcados podem disparar envios. |
| **Automação de Funil** | Regra configurada em um funil da Ploomes para determinar quando e como enviar um lead à Meetime (ex.: “Ao entrar na etapa X, criar lead na Meetime”). |
| **Token da API (Meetime)** | Código de autenticação usado para ativar a integração. Cada conta Meetime possui um token único. |
| **DealID (Meetime)** | Identificador único de um negócio dentro da Meetime. Agrupa todos os leads relacionados a um mesmo negócio originado do Ploomes. |
| **Registro de Interação (Ploomes)** | Registro automático criado no histórico do card conforme as atividades executadas na Meetime (ex.: ligação, e-mail, reunião). |
| **Checklist Obrigatório (Ploomes)** | Requisitos que impedem movimentação de etapa enquanto não forem preenchidos. Também são respeitados pela Meetime ao tentar mover leads de etapa. |
| **Motivo de Perda** | Campo padronizado de justificativa de perda de oportunidade. Sincronizado automaticamente entre Ploomes e Meetime. |
| **Pessoa Fantasma** | Pessoa criada automaticamente pela integração quando um card é enviado à Meetime sem contato associado. Serve apenas para garantir o vínculo do lead. |
| **Campo-chave (E-mail)** | Único campo usado pela Meetime para identificar e evitar duplicidade de leads. Todas as verificações de correspondência são baseadas nesse campo. |
| **Prioridade da Cadência** | Ordem de relevância definida na Meetime entre cadências. Usada para decidir qual cadência prevalece em casos de conflito (nova x existente). |
| **Fluxo Centralização no CRM** | Novo modelo de integração (recomendado), em que os leads são enviados da Ploomes para a Meetime via automação de funil, com sincronização bidirecional. |
| **Fluxo Recebimento de Leads Ganhos** | Modelo anterior de integração, em que apenas leads ganhos na Meetime criam negócios no Ploomes. Não pode ser usado junto com o fluxo novo. |

## 7. Perguntas frequentes

#### 1. Posso usar os dois fluxos da integração (Centralização no CRM e Leads Ganhos) ao mesmo tempo?

Não. Cada conta Ploomes pode utilizar apenas **um fluxo de integração por vez**. O fluxo recomendado é o **Centralização de Leads no CRM**, que oferece sincronização completa entre as plataformas.

---

#### 2. É possível enviar leads de qualquer funil?

Não. Somente **funis habilitados na configuração da integração** podem usar a automação “Enviar lead para a Meetime”.

---

#### 3. Preciso preencher todos os campos do card para enviar o lead?

#### Não, mas o lead só será criado na Meetime se o card tiver pelo menos um dos seguintes campos preenchidos:

- Contato Principal – Nome
- Contato Principal – E-mail
- Empresa – Nome

---

#### 4. O que acontece se o card tiver apenas uma empresa (sem contato)?

O Ploomes criará automaticamente uma **pessoa "fantasma"** para associar as informações à Meetime. Assim, toda informação do contato atualizada pela Meetime, atualizará a informação dessa pessoa correspondente.
Essa pessoa não é duplicada nem impacta registros reais de contatos.

---

#### 5. Como funciona o campo “Responsável mais recente (Meetime)”?

É o campo que define **quem será o responsável pelo lead** na Meetime.
Pode ser alterado no Ploomes até o envio do card; depois da integração, **só a Meetime pode atualizar esse valor**.

---

#### 6. E se o lead já existir na Meetime com o mesmo e-mail?

A Meetime usa o **e-mail como campo-chave** para identificar se um lead já existe.
Quando a Ploomes tenta enviar um lead com um e-mail que já está cadastrado, a integração segue esta lógica:

- Se o lead estiver fechado (ganho ou perdido), ele será reaberto na Meetime e entrará na nova cadência enviada pela Ploomes.
- Se o lead estiver aberto e a nova cadência tiver prioridade maior que a atual, o lead será atualizado com a nova cadência e com os dados mais recentes enviados pela Ploomes.
- Se o lead estiver aberto e a nova cadência tiver prioridade menor, nenhuma atualização será feita — o lead continuará com a cadência e as informações que já possui.

Essa regra garante que não haja duplicidade de leads e que apenas cadências mais relevantes ou recentes substituam as anteriores.

---

#### 7. Posso adicionar novos leads relacionados a um mesmo negócio?

Sim, mas com comportamentos diferentes dependendo do momento:

- **Antes da integração:**
  Se, ao criar o card na Ploomes, você preencher o campo Contatos Relacionados, todos esses contatos serão enviados juntos para a Meetime, tornando-se múltiplos leads associados ao mesmo negócio.
- **Depois da integração:**
  A criação de novos leads vinculados ao mesmo negócio deve ser feita diretamente pela Meetime.
  Se um novo Contato Relacionado for adicionado na Ploomes após o envio do card, ele não será sincronizado com a Meetime.

Em resumo: antes de enviar o card, os contatos relacionados são criados como leads na Meetime; depois de integrado, apenas a Meetime pode gerar novos leads associados ao mesmo negócio

---

#### 8. E se eu alterar o e-mail do contato na Ploomes depois da integração?

A Meetime **não permite duplicidade de e-mails**, pois o e-mail é o **campo-chave** que identifica cada lead.

- Se o novo e-mail já existir em outro lead na Meetime, a integração bloqueia a atualização e reverte o valor original no Ploomes.
  Nesse caso, é criado um Registro de Interação informando a tentativa e a reversão automática.
- Se o novo e-mail não existir na Meetime, a atualização é realizada com sucesso, e o novo endereço passa a ser o e-mail válido do lead sincronizado.

Esse comportamento evita duplicidade de leads e mantém a base de dados consistente entre as plataformas.

---

#### 9. Como os motivos de perda são sincronizados?

Todos os **motivos de perda do funil integrado na Ploomes** aparecem automaticamente listados na Meetime.
O vendedor seleciona o motivo diretamente na Meetime, e ele é **sincronizado de volta** para a Ploomes.

Para que o motivo apareça na Meetime, ele precisa existir na Ploomes no funil correspondente.

---

#### 10. O que acontece quando um lead é ganho ou perdido na Meetime?

O resultado do lead na Meetime impacta diretamente o negócio correspondente na Ploomes, de acordo com a configuração da integração.

- **Lead Ganho:**
  Quando um lead é marcado como ganho na Meetime, o negócio na Ploomes pode:

  - **Ser movimentado de etapa**,
  - **Permanecer na mesma etapa**, ou
  - **Ser marcado como ganho**, conforme definido nas configurações da conta.

  Se existirem outros leads associados ao mesmo negócio, é possível mantê-los abertos ou marcá-los como perdidos, encerrando o ciclo para todos.

- **Lead Perdido:**
  Quando um lead é marcado como perdido na Meetime, o negócio correspondente na Ploomes também pode ser marcado como perdido.
  Se todos os leads associados ao mesmo negócio forem perdidos, o negócio será automaticamente considerado perdido na Ploomes.

Esse comportamento garante que o status dos leads e dos negócios permaneça sincronizado entre as plataformas, mantendo o histórico e os relatórios consistentes.

---

#### 11. E se houver checklists obrigatórios no funil da Ploomes?

A Meetime **respeita as validações de checklist**.
Se houver pendências obrigatórias, a movimentação de etapa do lead não será permitida até que os itens sejam preenchidos no Ploomes.

---

#### 12. O que é encerrado quando o lead associado ao negócio é ganho ou perdido?

Quando um lead vinculado a um negócio é ganho ou perdido na Meetime, o fluxo da integração é encerrado para aquele negócio. Ou seja, novas atualizações de dados deixam de ser enviadas, mas todo o histórico permanece disponível nas duas plataformas.

O comportamento, porém, **depende se o negócio possui múltiplos leads associados**:

- **Negócio com apenas um lead:**

  - Assim que o lead é ganho ou perdido, o negócio é encerrado na Ploomes.
    Nenhum novo dado é sincronizado, e a integração é finalizada.
- **Negócio com múltiplos leads:**

  - Se um dos leads for ganho, o negócio na Ploomes pode avançar de etapa, manter-se na mesma etapa ou ser marcado como ganho, conforme as configurações da conta e a integração é finalizada para aquele negócio.
  - Se um lead for perdido, mas ainda houver outros leads em aberto, o negócio permanece ativo, e a integração continua funcionando normalmente.
  - Se todos os leads associados forem marcados como perdidos, o negócio é automaticamente marcado como perdido, e a integração é encerrada.

**Em resumo:** o encerramento da integração depende da existência de múltiplos leads.
Se houver apenas um lead, ela termina assim que ele é ganho ou perdido; se houver vários, ela só é encerrada quando um lead for ganho ou quando todos os leads associados forem perdidos.

---

#### 13. As atividades realizadas na Meetime aparecem no histórico da Ploomes?

Sim.
Cada atividade da cadência é automaticamente registrada como **Registro de Interação** correspondente (ex.: ligação → registro de telefone, e-mail → registro de e-mail, etc.).

---

#### 14. Posso mudar a cadência de um lead depois que ele foi enviado?

Não diretamente pelo Ploomes.
A alteração de cadência pode ser feita apenas **pela Meetime**. A informação será atualizada no campo da Ploomes em Cadência Mais Recente (Ploomes).

---

#### 15. Preciso atualizar manualmente usuários entre Ploomes e Meetime?

Não.
Os **usuários da Meetime são sincronizados automaticamente** com os usuários do Ploomes (associação via e-mail).
Novos usuários criados na Meetime também serão criados no Ploomes com o **perfil padrão configurado**.

---

#### 16. O que acontece se um funil for excluído da configuração da integração?

Ao remover um funil da integração, as automações “Enviar lead para a Meetime” configuradas nesse funil **deixarão de funcionar**, e nenhum novo lead será enviado.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts, casos de uso e webinars.

Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.

[![Imagem 28: Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048709993/04a3a627ef36962b2d850daa017e/Teste+03.png?expires=1786536000&signature=0dfe03704eb2b82dc858a529fb4467ae1870cc8aa2e4d5997ca6e1dcdfbeaa8b&req=diAjHs5%2BlIhWWvMW3nq%2BgbAxBczfip%2BrTT%2F0CbcSrC%2BevGha72HKXPpkVVct%0AcWuQvIQmJQ1uaJvILW7il7NlIss%3D%0A)](https://universidade.ploomes.com/courses/integracao-meetime)
