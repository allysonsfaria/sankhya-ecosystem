---
id: "33686820808215"
titulo: "Manual de Configuração e Uso do APP SOP Logística"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33686820808215-Manual-de-Configura%C3%A7%C3%A3o-e-Uso-do-APP-SOP-Log%C3%ADstica"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T14:28:35Z"
rotulos: ["Produtos", "Configuração", "Veículos", "Parceiro", "Integração", "Sankhya ID", "Interface", "APP", "APP SOP Logística", "Gateway", "Manual de Configuração e Uso do APP SOP Logística", "Logística"]
---

# Manual de Configuração e Uso do APP SOP Logística

### Configuração Usuário:

Preencha os seguintes campos na tela de cadastro de usuário:

- **Sankhya ID:** Email do usuário utilizado na identificação do Sankhya ID;
- **CPF:** CPF do usuário para validação de login;
- **Grupo de Usuário:** Código do grupo de usuário. O grupo/usuário precisa ter acesso às telas que geram registro pelo aplicativo, sendo abastecimento ou checklist;
- **Parceiro:** No cadastro do Parceiro, é necessário criar o cadastro com o mesmo CPF vinculado ao usuário;
- **Perfil de Acesso ao Aplicativo:**

  - **Frentista:** Visualiza todos os cadastros de veículos;
  - **Motorista:** Visualiza somente o veículo vinculado a ele;
- **Tipo de Usuário:**

  - **Interface:** Possibilita que o usuário efetue o login no SankhyaOm por meio da tela de login;
  - **Integração:** Viabiliza o login através das APIs disponibilizadas pela Sankhya;

**(1)** Usuário de Integração para configuração do Gateway deve ser do tipo Integração.

![Imagem 1: (1) Usuário de Integração para configuração do Gateway deve ser do tipo Integração.](https://ajuda.sankhya.com.br/hc/article_attachments/33686825238167)

### Configuração Gateway:

Preencha os seguintes campos na tela de cadastro do gateway:

- **Endereço Sankhya:** URL para acesso ao Sankhya;
- **Nome:** nome de identificação desta configuração de integração;
- **Tipo de Ambiente:** de acordo com o registro da Base (Produção/Teste).

Insira um novo registro e, em seguida, configure os seguintes campos:

- **Aplicação:** Busque por APP Logística;
- **Parceiro:**
- **Status:** Marque para ativar;
- **Cód. Usuário:** Busque o código do usuário de integração;
- **Token Integração:** Código do Token da Aplicação para Login via APP.

![Imagem 2: Token Integração: Código do Token da Aplicação para Login via APP.](https://ajuda.sankhya.com.br/hc/article_attachments/33686825239447)

### Logando no APP:

Efetue o download do aplicativo. Vale destacar que a descrição do APP é: **SOP Logística**.

Antes da tela de login será necessário a inclusão do Token. Esse Token é o código gerado na tela do gateway.

Após informado o token, será liberado o acesso ao aplicativo. Sendo que o login é o CPF é a **senha é a mesma utilizada no Sankhya ID.**

![Imagem 3: Após informado o token, será liberado o acesso ao aplicativo. Sendo que o login é o CPF é a senha é a mesma utilizada…](https://ajuda.sankhya.com.br/hc/article_attachments/33688578771095)

Após realizado o login no APP, através do Menu, pode ser realizada a sincronização para obter os dados do ERP.

As demais rotinas no menu como: Abastecimento e Checklist, iniciam o processo de lançamento do registro dentro do APP.

![Imagem 4: As demais rotinas no menu como: Abastecimento e Checklist, iniciam o processo de lançamento do registro dentro do APP.](https://ajuda.sankhya.com.br/hc/article_attachments/33688546798487)

### Configurações para uso APP - Abastecimento:

Antes de iniciar o uso do aplicativo para os lançamentos do abastecimento, é necessário que as configurações dentro do Sankhya tenham sido concluídas, caso contrário o aplicativo não funcionará corretamente, devido a falta de parametrização.

**(1)** **Para registro do abastecimento interno é necessário seguir as seguintes configurações:**

Na tela de Parceiros (Configurações » Cadastros » Parceiros), crie um parceiro com um nome sugestivo, por exemplo **"Bomba Interna"**.

![Imagem 5: Na tela de Parceiros (Configurações » Cadastros » Parceiros), crie um parceiro com um nome sugestivo, por exemplo…](https://ajuda.sankhya.com.br/hc/article_attachments/33688578777751)

Em seguida, ainda no cadastro do parceiro, preencha o campo **"Empresa Preferencial"** com o código da empresa onde está localizada a bomba.

![Imagem 6: Em seguida, ainda no cadastro do parceiro, preencha o campo "Empresa Preferencial" com o código da empresa onde está…](https://ajuda.sankhya.com.br/hc/article_attachments/33688578779031)

Na aba **"TMS"**, marque os campos de **"Posto"** e **"Posto Interno"**.

![Imagem 7: Na aba "TMS" , marque os campos de "Posto" e "Posto Interno" .](https://ajuda.sankhya.com.br/hc/article_attachments/33688546802967)

Na tela **"Empresas"** (Configurações » Cadastros » Empresas), na aba **"TMS"**, no campo **"Local Abastecimento Interno"** informe o código do local de estoque que irá controlar o saldo da bomba.

![Imagem 8: Na tela "Empresas" (Configurações » Cadastros » Empresas), na aba "TMS" , no campo "Local Abastecimento Interno"…](https://ajuda.sankhya.com.br/hc/article_attachments/33688578783127)

Na tela **"Veículos"** (Configurações » Cadastros » Veículos), preencha o campo **"Combustível"** com o tipo de combustível que aquele veículo pode utilizar.

Em seguida, preencha os campos de **"Validado pelo Transporte"** e **"Cavalo".** Caso contrário, o veículo não será encontrado no apontamento do abastecimento pelo aplicativo.

Além disso, o campo de **"Tipo de Veículo",** na aba **"TMS"** precisa ser preenchido, geralmente possuindo as opções:

- 1-TERCEIRO
- 2-AGREGADO
- 3-PRÓPRIO

![Imagem 9: 3-PRÓPRIO](https://ajuda.sankhya.com.br/hc/article_attachments/33688546807191)

Na tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) preencha o campo **"Tipo de Combustível"**. Este campo tem as mesmas opções do cadastro do veículo. Isso é necessário para criar uma relação do cadastro do produto com o combustível do veículo.

![Imagem 10: Na tela "Produtos" (Configurações » Cadastros » Produtos » Produtos) preencha o campo "Tipo de Combustível" . Este…](https://ajuda.sankhya.com.br/hc/article_attachments/33688546808983)

Na tela  **"Configurações Gestão de Frota"**, aba **"Geral"**, no quadro de abastecimento, preencha os campos:

- Tipo de Vlr Unitário Abastecimento;
- Tipo de Negociação Requisição;
- TOP Requisições;
- Natureza Requisições
- Gerar Requisição Automático (deve estar marcado)

![Imagem 11: Gerar Requisição Automático (deve estar marcado)](https://ajuda.sankhya.com.br/hc/article_attachments/33688546811671)

Ainda na tela  Configurações Gestão de Frota, aba **"Usuários p/ Req. Abast. Automática"**, inclua o usuário de integração.

![Imagem 12: Ainda na tela Configurações Gestão de Frota , aba "Usuários p/ Req. Abast. Automática" , inclua o usuário de integração.](https://ajuda.sankhya.com.br/hc/article_attachments/33688578790039)

### Manual de Uso APP - Abastecimento:

(1)** Concluídas as configurações descritas acima, o próximo passo será o uso do aplicativo**

Ao iniciar um processo de abastecimento é aberto a tela para realizar a leitura do QR do veículo. Caso o veículo não possua QR code, basta usar a opção de Digitar.

Em seguida, serão apresentados os campos: **"Veículo", "Motorista" e "Local de Abastecimento"**. Preencha-os com as opções disponíveis, de acordo com a configuração. Em seguida, clique em **"Avançar"**.

![Imagem 13: Em seguida, serão apresentados os campos: "Veículo", "Motorista" e "Local de Abastecimento" . Preencha-os com as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/33688578791319)

A próxima etapa será o preenchimento dos dados do combustível. Para isso, preencha os campos: **"Combustível", "Odômetro", "Quantidade (em litros)", "Tanque Cheio?"**.

Se houver a necessidade de registrar alguma imagem, use o recurso de anexar foto, no qual pode-se tirar uma foto ou usar uma foto tirada anteriormente que esteja na galeria.

Ao clicar em Confirmar, será apresentada a mensagem de que o registro foi concluído com sucesso.

![Imagem 14: Ao clicar em Confirmar, será apresentada a mensagem de que o registro foi concluído com sucesso.](https://ajuda.sankhya.com.br/hc/article_attachments/33689632839959)

Através do ícone de abastecimento, presente no rodapé do aplicativo, é possível validar todos os abastecimentos que foram realizados, como um formato de histórico.

![Imagem 15: Através do ícone de abastecimento, presente no rodapé do aplicativo, é possível validar todos os abastecimentos que…](https://ajuda.sankhya.com.br/hc/article_attachments/33689611103895)

### Configurações para uso APP - Checklist

Antes de iniciar o uso do aplicativo para os lançamentos do checklist, é necessário que as configurações dentro do Sankhya tenham sido concluídas, caso contrário o aplicativo não funcionará corretamente devido a falta de parametrização.

(1)** Para registro do checklist é necessário seguir as seguintes configurações:**

Na tela **"Tipo de Checklist Operacional"**, é necessário que sejam criados os tipos, como por exemplo: Checklist para Viagem, Checklist para Oficina.

![Imagem 16: Na tela "Tipo de Checklist Operacional" , é necessário que sejam criados os tipos, como por exemplo: Checklist para…](https://ajuda.sankhya.com.br/hc/article_attachments/33689611105047)

A tela **"Modelo de Checklist operacional"** é local em que acontecerá efetivamente o cadastro dos modelos, sendo agrupados por tipo de checklist, conforme cadastrado anteriormente.

- **Descrição:** de livre definição por parte da empresa;
- **Tipo de Checklist:** escolher qual tipo se refere ao modelo que está sendo criado;
- **Usuário/Data e Hora:** obtém esses dados automaticamente no momento do cadastro;
- **Ativo:** se este modelo está em uso ou não;
- **Gerar OS:** marcando este campo é possível que seja gerado uma OS após a conclusão do Checklist;
- **Exige KM/Odômetro:** com esta opção marcada, no momento do checklist  está informação torna-se obrigatória;
- **Exige Entrada/Saída:** esta marcação vai exigir que seja lançado um checklist para entrada e outro para saída, totalizando 2 lançamentos. Caso seja feito apenas o de entrada, ao enviar o checklist para o Sankhya, o Status irá permanecer com **Em Andamento**, até que seja realizado o lançamento. Por isso, ao **marcar esse campo, deve-se atentar para realização de 2 lançamentos, representando a entrada e a saída do veículo**.

![Imagem 17: Exige Entrada/Saída: esta marcação vai exigir que seja lançado um checklist para entrada e outro para saída,…](https://ajuda.sankhya.com.br/hc/article_attachments/33689611107607)

Concluído o lançamento do cabeçalho do modelo, preencha a aba **"Itens do Checklist"**. Nela, devem ser criados os itens que farão parte do checklist. Além disso, poderá ser exigido pela configuração, o envio de fotos de acordo com o cadastro de cada item. Por padrão, ao marcar o campo de **"Exigir Foto"**, o mínimo de foto exigido será 1, caso a quantidade não tenha sido definida no campo de quantidade mínima.

![Imagem 18: Concluído o lançamento do cabeçalho do modelo, preencha a aba "Itens do Checklist" . Nela, devem ser criados os itens…](https://ajuda.sankhya.com.br/hc/article_attachments/33690528477079)

A Sub-Aba **"Não Conformidade"**, será utilizada para vincular quais são as possíveis inconformidades que podem ocorrer. Da mesma forma que o cadastro anterior, também pode exigir o envio de fotos para justificativa da não conformidade.

![Imagem 19: A Sub-Aba "Não Conformidade" , será utilizada para vincular quais são as possíveis inconformidades que podem ocorrer.…](https://ajuda.sankhya.com.br/hc/article_attachments/33689611112727)

A aba **"Veículos"** serve para que sejam vinculados os veículos que podem utilizar este modelo de checklist.

![Imagem 20: A aba "Veículos" serve para que sejam vinculados os veículos que podem utilizar este modelo de checklist.](https://ajuda.sankhya.com.br/hc/article_attachments/33690528479511)

Para registro das não conformidades do checklist, estas devem ser cadastradas na tela **"Não Conformidades Checklist"**. O cabeçalho é formado por uma descrição e um campo para mencionar se este cadastro está ativo ou não.
Abaixo há a aba **"Produtos"**, na qual podem ser sugeridos produtos e uma quantidade para a correção da não conformidade.

![Imagem 21: Para registro das não conformidades do checklist, estas devem ser cadastradas na tela "Não Conformidades Checklist" . O…](https://ajuda.sankhya.com.br/hc/article_attachments/33690528480663)

A aba **"Serviços",** por sua vez, serve para indicar quais serviços podem ser executados para correção da não conformidade.

![Imagem 22: A aba "Serviços", por sua vez, serve para indicar quais serviços podem ser executados para correção da não conformidade.](https://ajuda.sankhya.com.br/hc/article_attachments/33690528481303)

Após concluído o lançamento do checklist pelo aplicativo, as informações serão armazenadas, no **SankhyaOM,** na tela **"Consulta Checklist Operacional".**

![Imagem 23: Após concluído o lançamento do checklist pelo aplicativo, as informações serão armazenadas, no SankhyaOM, na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/33690528487575)

### Manual de Uso APP - Checklist:

Ao iniciar o processo de registro do checklist, serão solicitadas a inclusão dos campos: **"Unidade (Empresa)", o "Modelo do Checklist", "Veículo" e o "Odômetro"**.

Em seguida, serão mostrados quantos itens serão verificados neste checklist, que neste exemplo é composto de 2 itens. Para dizer que está OK, escolha o ícone do **“joinha para cima”** ou, caso seja identificado algum problema, escolha o ícone do **“joinha para baixo”**.

![Imagem 24: Em seguida, serão mostrados quantos itens serão verificados neste checklist, que neste exemplo é composto de 2 itens.…](https://ajuda.sankhya.com.br/hc/article_attachments/33691205461783)

Concluído a etapa anterior de apontamento, com registro de fotos e observações. Em seguida,  realize uma assinatura e envie para o Sankhya através do ícone do **“Aviãozinho”** no canto superior direito.

![Imagem 25: Concluído a etapa anterior de apontamento, com registro de fotos e observações. Em seguida, realize uma assinatura e…](https://ajuda.sankhya.com.br/hc/article_attachments/33691404232599)
