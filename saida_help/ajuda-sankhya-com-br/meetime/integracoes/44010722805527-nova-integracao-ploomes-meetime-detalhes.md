---
id: "44010722805527"
titulo: "Nova integração Ploomes <> Meetime - detalhes e como ativar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010722805527-Nova-integra%C3%A7%C3%A3o-Ploomes-Meetime-detalhes-e-como-ativar"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:46:46Z"
rotulos: ["sync_hc", "meetime", "meetime_346", "sync_hash_c760a7d35e0e"]
---

# Nova integração Ploomes <> Meetime - detalhes e como ativar

A nova integração entre Ploomes e Meetime permite a centralização no CRM. Agora leads e oportunidades são unificados em um só lugar, garantindo maior visibilidade e controle durante todo o processo comercial.

## Sobre a integração

A integração entre Ploomes e Meetime conecta o CRM ao fluxo de prospecção por cadências.

Os leads são iniciados no Ploomes e enviados automaticamente para a Meetime através das automações de funil. Com isso, as atividades de cadência e resultados (ganho/perdido) realizados na Meetime são enviados para o Ploomes.

Observação: Nessa versão, o envio ocorre somente no sentido Ploomes > Meetime. Depois que o negócio está integrado, há sincronização bidirecional de campos (ex: nome, telefone e status do negócio).  A Meetime não cria negócios no Ploomes, mas pode criar contatos quando forem leads associados ao mesmo negócio já existente no Ploomes.

## Como funciona?

1. Você define uma etapa do funil no Ploomes que irá disparar o envio do lead para a Meetime.
2. Dentro da Meetime você executará as atividades da cadência (ligações, e-mails, reuniões).
3. Os resultados dos leads e as atividades realizadas na Meetime voltam para o Ploomes como Registro de Interação e atualização de status do negócio ou motivos de perda.
4. O histórico permanece centralizado no Ploomes.

## Quais os benefícios?

- Evita retrabalho: como o envio de atividades e status é automático e o retorno é registrado no CRM, reduz a duplicidade de dados.
- Mantém dados consistentes: sincronização de campos entre Ploomes e Meetime.
- Prospecção automatizada: cria o lead na Meetime conforme as regras do funil no Ploomes, sem processos manuais.
- Melhora o controle do funil: permite o avanço automático de estágios conforme o resultado (ganho/perdido) e concentra o acompanhamento no CRM.

## Pré-requisitos

- Ter uma conta ativa na Meetime.
- Ter acesso ao Token da API da Meetime (você pode verificar [aqui](https://suporte.meetime.com.br/hc/pt-br/articles/26604018404505-Bot%C3%A3o-de-gerar-token-de-API-Atualiza%C3%A7%C3%A3o-12-2023) como acessar na Meetime). A autenticação é por conta, então ao ativar, vale para todos os usuários da conta Ploomes).
- Ter uma conta Ploomes com permissão para ativar integrações plug-and-play e configurar automações de funil.

## Como ativar?

### Passo 1: Acessar tela de configurações no Ploomes

No Ploomes, acesse Administração > Integrações plug-and-play > Meetime > Escolher versão "Centralização de leads no CRM"

![Imagem 1: No Ploomes, acesse Administração > Integrações plug-and-play > Meetime > Escolher versão "Centralização de leads no CRM"](https://ajuda.sankhya.com.br/hc/article_attachments/44010762147223)

### Passo 2: Acessar a tela de integrações da Meetime

Agora na Meetime, clique na sua foto no canto superior direito > Integrações > API > Copie o Token da conta

![Imagem 2: Agora na Meetime, clique na sua foto no canto superior direito > Integrações > API > Copie o Token da conta](https://ajuda.sankhya.com.br/hc/article_attachments/44010746479511)

### Passo 3: Colar o token da API no Ploomes

Retornando para o Ploomes, cole o token no campo "Token de Integração" > Validar Token. Com o token validado, clique em "Habilitar Integração".![Imagem 3: Retornando para o Ploomes, cole o token no campo "Token de Integração" > Validar Token. Com o token validado, clique em…](https://ajuda.sankhya.com.br/hc/article_attachments/44010762734999)

### Passo 4: Configure a seção Leads (Pessoas, Empresas e Negócios).

Nessa etapa, a interface já indica que há criação e edição de dados entre Ploomes e Meetime. Os detalhes dessa configuração estão na sessão seguinte da documentação.

![Imagem 4: Nessa etapa, a interface já indica que há criação e edição de dados entre Ploomes e Meetime. Os detalhes dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/44010791820439)

**Quais funis poderão enviar leads**

O primeiro passo é definir quais funis do Ploomes poderão enviar leads para a Meetime e ficarão disponíveis para configurar automações de envio.

- Este campo é **múltiplo**, permitindo **selecionar mais de um funil** por conta.
- Nesta etapa, você apenas habilita os funis que terão acesso à automação de envio. A configuração da automação será feita diretamente dentro da tela de automações do funil.

![Imagem 5: Nesta etapa, você apenas habilita os funis que terão acesso à automação de envio. A configuração da automação será…](https://ajuda.sankhya.com.br/hc/article_attachments/44010767372439)

**O que fazer quando leads enviados forem ganhos na Meetime**

Quando um lead integrado é marcado como ganho na Meetime, é possível definir qual será a ação aplicada automaticamente ao negócio correspondente no Ploomes:

- Avançar o negócio para uma etapa específica
- Manter o negócio na mesma etapa
- Ganhar o negócio no Ploomes

![Imagem 6: Ganhar o negócio no Ploomes](https://ajuda.sankhya.com.br/hc/article_attachments/44010747671703)

**Lógica de exibição das configurações**

O Ploomes aplica regras específicas na exibição das opções:

- Para um mesmo funil e uma mesma cadência, só pode existir uma ação configurada.
- Ao selecionar um funil, o Ploomes verifica quais cadências já estão vinculadas a esse funil com ações configuradas na Meetime.
- As cadências já utilizadas em outras configurações não aparecerão como opção no segundo dropdown (cadências).

![Imagem 7: As cadências já utilizadas em outras configurações não aparecerão como opção no segundo dropdown (cadências).](https://ajuda.sankhya.com.br/hc/article_attachments/44010754205207)

### Passo 5: Mapeamento dos campos

A sincronização da integração possui campos pré-associados automaticamente e campos personalizáveis que o usuário pode associar manualmente.

- É importante que esses campos já existam na Meetime.

**Entidades mapeáveis**

Três entidades podem ser associadas à mesma entidade de lead na Meetime:

- Campos de Pessoa (Ploomes) <> Campos de Lead (Meetime)
- Campos de Empresa (Ploomes) <> Campos de Lead (Meetime)
- Campos de Negócio (Ploomes) <> Campos de Lead (Meetime)

### Pessoa <> Lead

Nesta seção, o usuário define quais campos do tipo Pessoa no Ploomes serão associados a campos de Lead na Meetime.

Campos pré-associados padrão da integração e não editáveis: Nome, E-mail e Telefone.

Obs: Em caso de múltiplos telefones, todos os números são enviados para a Meetime.

Para adicionar novos campos, basta clicar em "Nova relação de campos", selecionar o campo no Ploomes e na Meetime.

![Imagem 8: Para adicionar novos campos, basta clicar em "Nova relação de campos", selecionar o campo no Ploomes e na Meetime.](https://ajuda.sankhya.com.br/hc/article_attachments/44010754439703)

### Empresa <> Lead

Nesta seção, o usuário define campos do tipo Empresa no Ploomes que serão associados a campos de Lead na Meetime.

Campos pré-associados padrão da integração e não editáveis: Nome e Telefone.

Obs: Em caso de múltiplos telefones, todos os números são enviados para a Meetime.

![Imagem 9: Obs: Em caso de múltiplos telefones, todos os números são enviados para a Meetime.](https://ajuda.sankhya.com.br/hc/article_attachments/44010764460311)

### Negócio <> Lead

Nesta seção, o usuário define campos do tipo Negócio no Ploomes para associar a campos de Lead na Meetime.

### Campos pré-associados (padrão da integração – não editáveis):

### Contatos Relacionados <> Leads associados a um mesmo negócio

O campo Contatos Relacionados no Ploomes representa os leads vinculados ao mesmo negócio.

- **Ploomes > Meetime:** se um negócio for integrado com contatos relacionados, serão criados múltiplos leads na Meetime, todos associados ao mesmo negócio.

Importante: após a integração do card e do lead, não é possível adicionar novos contatos relacionados pela Ploomes para gerar leads na Meetime. Essa associação deve ser feita antes do envio do card pela automação de funil.

- **Meetime > Ploomes:** após integrado, ao adicionar leads associados a um mesmo negócio na Meetime, serão criados contatos relacionados no Ploomes.
- A integração não cria duplicatas de pessoas ou empresas na Ploomes:

Para Pessoas, o sistema verifica o e-mail antes de criar.

Para Empresas, o sistema verifica o CNPJ (quando mapeado) e o Nome da Empresa.

- **Responsável mais recente (Meetime) ↔ Responsável (Lead)**
- Campo criado da Ploomes automaticamente na ativação da integração.
- Define o responsável pelo lead no momento do envio e é atualizado caso o responsável mude na Meetime.
- Pode ser alterado no Ploomes até o envio do card para a Meetime.
- Após a integração, só a Meetime pode atualizar esse campo.
- Caso o usuário tente alterar pelo Ploomes, o valor é revertido e é criado um Registro de Interação com o motivo do erro.
- **Responsável inicial (Meetime) ↔ Responsável (Lead)**

Campo da Ploomes de dados criado na ativação da integração, não editável no CRM.

Armazena quem foi o primeiro responsável pelo negócio, garantindo rastreabilidade histórica.

- **Cadência mais recente (Meetime) ↔ Cadência (Lead)**

Campo da Ploomes é criado na ativação da integração.

Armazena a última cadência enviada para a Meetime via automação de funil.

Campo bloqueado para preenchimento manual, atualizado automaticamente pela Meetime.

- **Cadência inicial (Meetime) ↔ Cadência (Lead)**

Campo da Ploomes é criado na ativação da integração.

Armazena a primeira cadência enviada para a Meetime.

Campo somente para dados, não pode ser alterado após o registro inicial.

![Imagem 10: Campo somente para dados, não pode ser alterado após o registro inicial.](https://ajuda.sankhya.com.br/hc/article_attachments/44010793611671)

### Regras de Mapeamento de Campos (Ploomes <> Meetime)

Para manter a integridade e consistência dos dados, a tela de mapeamento aplica **filtros automáticos** que impedem associações entre **tipos de campos incompatíveis**.

**Exemplo:**

Não é possível associar um campo Número no Ploomes a um campo Seleção na Meetime, pois isso geraria inconsistência e falhas de interpretação na sincronização.

Essas restrições funcionam como uma camada de proteção, garantindo que o mapeamento entre plataformas ocorra de forma segura e coerente.

**Campos Ploomes**

**Correspondência do tipo de campo na Meetime**

![Imagem 11: Correspondência do tipo de campo na Meetime](https://ajuda.sankhya.com.br/hc/article_attachments/44010798530711)![Imagem 12: Correspondência do tipo de campo na Meetime](https://ajuda.sankhya.com.br/hc/article_attachments/44010794024727)

![Imagem 13: Correspondência do tipo de campo na Meetime](https://ajuda.sankhya.com.br/hc/article_attachments/44010776663063)

### Passo 6: Configuração da Seção de Vendedores (Usuários)

- Ao ativar a integração, ocorre automaticamente a sincronização dos usuários da Meetime com os usuários do Ploomes. Com isso, todo usuário existente na Meetime terá um correspondente no Ploomes.
- O campo chave para essa sincronização é o e-mail. É por meio dele que o sistema identifica se deve associar um usuário existente ou criar um novo usuário na conta Ploomes.
- A sincronização é contínua: novos usuários criados na Meetime após a ativação serão criados automaticamente no Ploomes.

Regras de criação e associação de usuários:

- Se o e-mail já existir no Ploomes, o usuário é associado ao usuário existente, sem alterações de nome ou perfil.
- Se o e-mail não existir e o nome estiver peenchido na Meetime, é criado um novo usuário no Ploomes, utilizando o nome e e-mail da Meetime, com o perfil definido pelo administrador.
- Se o e-mail não existir e o nome estiver em branco na Meetime, é criado um novo usuário no Ploomes utilizando o e-mail da Meetime como nome padrão, além do perfil selecionado.

### Passo 7: Configuração do perfil padrão

A única configuração disponível nesta seção é a escolha do perfil de usuário padrão que será atribuído aos novos usuários criados pela integração.

Essa configuração é feita em um campo de seleção, que lista todos os perfis disponíveis na conta Ploomes. Após selecionar o perfil e ativar a integração, todos os novos usuários criados a partir da Meetime já serão registrados cno Ploomes com esse perfil padrão.

A manutenção dessa associação é contínua, então todo novo usuário criado na Meetime após a ativação da integração também será criado no Ploomes automaticamente.

![Imagem 14: A manutenção dessa associação é contínua, então todo novo usuário criado na Meetime após a ativação da integração…](https://ajuda.sankhya.com.br/hc/article_attachments/44010799508503)

### Passo 8: Configuração de Automação de Funil

As automações de funil determinam quando (em qual etapa do funil) e como (com base em filtros e gatilhos) os leads serão enviados para a Meetime.

A automação só ficará disponível nos funis selecionados durante a integração (Passo 4), permitindo personalizar as regras de envio conforme a necessidade de cada operação.

1. Acesse o funil desejado clicando em Pipes > Funil que irá aparecer conforme os seus configurados > Todos os funis >

![Imagem 15: Acesse o funil desejado clicando em Pipes > Funil que irá aparecer conforme os seus configurados > Todos os funis >](https://ajuda.sankhya.com.br/hc/article_attachments/44010777177495)

1. Clique no funil desejado

   ![Imagem 16: Clique no funil desejado](https://ajuda.sankhya.com.br/hc/article_attachments/44010795360535)
2. Clique em Menu > Configurar funil

   ![Imagem 17: Clique em Menu > Configurar funil](https://ajuda.sankhya.com.br/hc/article_attachments/44010777928599)
3. Agora, você vai definir em qual etapa do funil você deseja que o lead seja disparado para a Meetime. Após escolher, selecione Configurar automações > Nova automação.
4. ![Imagem 18: Defina os seguintes campos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010785048855)Defina os seguintes campos abaixo:

Descrição - Nome ou descrição live para identificar a regra.

Gatilho - Define o momento em que o sead será enviado para a Meetime. Opções disponíveis: "Negócio entrou neste estágio" / "Negócio reaberto neste estágio".

Filtros - Permite definir critérios adicionais para o disparo da automação (ex: tipo de produto, responsável, segmento etc).

Ao ser disparada, o que a automação deve fazer - Selecione a ação "Enviar lead para Meetime".

![Imagem 19: Ao ser disparada, o que a automação deve fazer - Selecione a ação "Enviar lead para Meetime".](https://ajuda.sankhya.com.br/hc/article_attachments/44010807914903)

```
5. Nessa etapa, aparecerá uma lista de seleção com todas as suas cadências existentes na Meetime.  É necessário definir em qual cadência o lead enviado pelo Ploomes será aplicado na Meetime.
```

![Imagem 20: Ao ser disparada, o que a automação deve fazer - Selecione a ação "Enviar lead para Meetime".](https://ajuda.sankhya.com.br/hc/article_attachments/44010801421847)

```
6. É necessário definir como o lead será inserido no fluxo de prospecção:
```

- Início imediato: o lead é enviado e fica "Ativo" na Meetime;
- Aguardar início: o lead é enviado e fica como "Esperando Início", para que o vendedor puxer o lead manualmente quando necessário.

![Imagem 21: Aguardar início: o lead é enviado e fica como "Esperando Início", para que o vendedor puxer o lead manualmente quando…](https://ajuda.sankhya.com.br/hc/article_attachments/44010808398103)

Após salvar essas configurações, a integração entre Meetime e Ploomes foi finalizada.

Nesse artigo, você pode verificar mais detalhes de [Como funciona a nova Integração entre Ploomes e Meetime](https://suporte.meetime.com.br/hc/pt-br/articles/53079209424281/live_preview/01KF3D7Y7DPCZRGE5C0CVG0M7R).

**Glossário da Integração Ploomes <> Meetime**

Card / Negócio (Ploomes): Registro principal de oportunidade no Ploomes, que pode conter pessoa, empresa, produtos e informações de venda. É o item integrado à Meetime como lead.

Contato Principal: Pessoa vinculada ao negócio no Ploomes que será o lead principal na Meetime.

Contatos Relacionados: Pessoas adicionais vinculadas a um mesmo negócio no Ploomes. Na Meetime, correspondem a múltiplos leads associados ao mesmo DealID.

Responsável mais recente: Campo criado automaticamente na ativação da integração. Indica o responsável que será enviado para a Meetime e atualizado posteriormente pela plataforma.

Responsável inicial: Campo de registro histórico que armazena quem foi o primeiro responsável pelo lead no momento da criação. Não é editável.

Funil Integrado: Funil do Ploomes habilitado para utilizar a automação “Enviar lead para a Meetime”. Somente os funis marcados podem disparar envios.

Automação de Funil: Regra configurada em um funil da Ploomes para determinar quando e como enviar um lead à Meetime (ex.: “Ao entrar na etapa X, criar lead na Meetime”).

Registro de Interação: Registro automático criado no histórico do card conforme as atividades executadas na Meetime (ex.: ligação, e-mail, reunião).

Checklist Obrigatório: Requisitos que impedem movimentação de etapa enquanto não forem preenchidos. Também são respeitados pela Meetime ao tentar mover leads de etapa.

Pessoa Fantasma: Pessoa criada automaticamente pela integração quando um card é enviado à Meetime sem contato associado. Serve apenas para garantir o vínculo do lead.

Campo-chave (E-mail): Único campo usado para identificar e evitar duplicidade de leads. Todas as verificações de correspondência são baseadas nesse campo.

Fluxo Centralização no CRM: Novo modelo de integração (recomendado), em que os leads são enviados da Ploomes para a Meetime via automação de funil, com sincronização bidirecional.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
