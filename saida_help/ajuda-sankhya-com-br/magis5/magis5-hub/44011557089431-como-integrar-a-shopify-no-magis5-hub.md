---
id: "44011557089431"
titulo: "Como integrar a Shopify no Magis5 HUB?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011557089431-Como-integrar-a-Shopify-no-Magis5-HUB"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:07:01Z"
rotulos: ["sync_hc", "magis5", "magis5_204055258240", "sync_hash_390bd64501b7"]
---

# Como integrar a Shopify no Magis5 HUB?

## Entenda como integrar o Magis5 HUB com a Shopify.

### Antes de começar:

---

A partir de **Janeiro de 2024**, a Shopify passou a adotar uma **nova regra para o envio de dados fiscais via API.**

Agora, apenas lojas que utilizam o plano Shopify ou superior terão os dados fiscais incluídos nas transações. Para contas no **plano Basic** criadas antes de Janeiro de 2024, nada muda: os dados fiscais continuam sendo retornados normalmente pela API.

No entanto, contas criadas **a partir de Janeiro de 2024 no plano Basic não terão mais esses dados disponíveis via API**. Caso seja necessário acessar essas informações, será preciso fazer o upgrade para o plano Shopify ou superior.

**Recomendamos verificar o plano atual da sua conta para garantir que você está recebendo todos os dados necessários.**

Em caso de dúvidas, consulte a documentação atualizada ou entre em contato com o suporte.

**Informações importantes antes de integrar sua Shopify:**

Para garantir o bom funcionamento da plataforma, atente-se a estes pontos fundamentais:

- **Comissões:** A Shopify cobra uma taxa por transação que varia entre **0,5% e 2%**, dependendo do plano contratado.
- **Emissão de Etiquetas:** A Shopify não emite etiquetas nativamente. No momento, essa funcionalidade está disponível apenas para clientes que utilizam as integrações com os [Correios](https://ajuda.sankhya.com.br/como-integrar-o-correios?hsLang=pt-br), [Intelipost](https://ajuda.sankhya.com.br/como-integrar-a-intelipost-com-o-magis5?hsLang=pt-br) ou [Mandaê](https://ajuda.sankhya.com.br/como-integrar-a-mandae-com-o-magis5-hub?hsLang=pt-br)

### Gerando o token na Shopify

Acesse a plataforma da [Shopify](https://accounts.shopify.com/lookup?rid=7b6a13ce-7d4d-47fc-90ee-c67d0c859d45&verify=1775054379-hV6vh%2BoJXrWCo%2Bx9uYu7VLUXoZqML%2BTOLQNsvNR6yGI%3D) utilizando seu e-mail e senha. Em seguida, vá até a opção **“Configurações”** no menu.

![Imagem 1: Acesse a plataforma da Shopify utilizando seu e-mail e senha. Em seguida, vá até a opção “Configurações” no menu.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-02-46-32-2071-PM.png?width=284&height=638&name=image-png-Apr-01-2026-02-46-32-2071-PM.png)

No painel administrativo, acesse a seção **“Domínios”**. Em seguida, localize e copie o domínio que termina com **myshopify.com**. Guarde essa informação para uso posterior na integração no Magis5 HUB.

![Imagem 2: No painel administrativo, acesse a seção “Domínios” . Em seguida, localize e copie o domínio que termina com…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-02-58-27-9797-PM.png?width=249&height=511&name=image-png-Apr-01-2026-02-58-27-9797-PM.png)

💡 **Dica:**

Abra um bloco de notas no seu computador e organize previamente todos os dados necessários para a integração. Isso facilitará o processo e ajudará você a se orientar melhor durante as etapas.

Em seguida, na mesma tela, localize a opção **“Apps”** e clique nela. Dentro da tela de aplicativos, selecione a opção **“Desenvolver apps no Dev Dashboard”**.

![Imagem 3: Em seguida, na mesma tela, localize a opção “Apps” e clique nela. Dentro da tela de aplicativos, selecione a opção…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-03-08-10-1736-PM.png?width=670&height=336&name=image-png-Apr-01-2026-03-08-10-1736-PM.png)

Você será redirecionado para tela **"dev dashboard"** da Shopify clique em **"Create app"**

![Imagem 4: Você será redirecionado para tela "dev dashboard" da Shopify clique em "Create app"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-03-24-43-3064-PM.png?width=670&height=195&name=image-png-Apr-01-2026-03-24-43-3064-PM.png)

Clique em **“Create app”**. Em seguida, dentro de **“Start from Dev Dashboard”**, informe o **“App name”** e finalize clicando em **“Create”**.

![Imagem 5: Clique em “Create app” . Em seguida, dentro de “Start from Dev Dashboard” , informe o “App name” e finalize clicando em…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-03-30-40-2755-PM.png?width=670&height=283&name=image-png-Apr-01-2026-03-30-40-2755-PM.png)

Na seção "**URLs"**, localize o campo **"App URL"** e informe o endereço do Magis5: **<https://app.magis5.com.br>.**

![Imagem 6: Na seção " URLs" , localize o campo "App URL" e informe o endereço do Magis5: https://app.magis5.com.br .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2026-05-23-19-1542-PM.png?width=1279&height=506&name=image-png-Jul-31-2026-05-23-19-1542-PM.png)

Ainda dentro da seção **“Versions”**, localize a opção **“Access”** e clique em **“Select scopes”**.

![Imagem 7: Ainda dentro da seção “Versions” , localize a opção “Access” e clique em “Select scopes” .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-03-41-17-6722-PM.png?width=670&height=299&name=image-png-Apr-01-2026-03-41-17-6722-PM.png)

Ao acessar a opção de seleção de scopes, marque **todas** as opções disponíveis dentro dessa categoria.

![Imagem 8: Ao acessar a opção de seleção de scopes, marque todas as opções disponíveis dentro dessa categoria.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2026-05-13-50-8341-PM.png?width=670&height=417&name=image-png-Jul-31-2026-05-13-50-8341-PM.png)

![Imagem 9: Ao acessar a opção de seleção de scopes, marque todas as opções disponíveis dentro dessa categoria.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2026-05-17-03-1053-PM.png?width=670&height=312&name=image-png-Jul-31-2026-05-17-03-1053-PM.png)

![Imagem 10: Ao acessar a opção de seleção de scopes, marque todas as opções disponíveis dentro dessa categoria.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2026-05-15-11-7994-PM.png?width=670&height=301&name=image-png-Jul-31-2026-05-15-11-7994-PM.png)

![Imagem 11: Ao acessar a opção de seleção de scopes, marque todas as opções disponíveis dentro dessa categoria.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2026-05-16-23-6207-PM.png?width=670&height=310&name=image-png-Jul-31-2026-05-16-23-6207-PM.png)

⚠️ **É imprescindível que todas as opções dentro dessa sessão sejam devidamente selecionadas.**

Role um pouco a pagina ate encontrar a opção **"Redirect URLs"**, dentro da caixa de texto cole a seguinte URL:

**https://app.magis5.com.br/v2/admin/integrations/channel/insert.php?channel=shopify&channelType=store**

⚠️ **A url precisa ser exatamente igual sem faltar nem adicionar nenhum caractere.**

![Captura de tela 2026-04-27 152401](https://ajuda.magis5.com.br/hs-fs/hubfs/Captura%20de%20tela%202026-04-27%20152401.jpg?width=670&height=169&name=Captura%20de%20tela%202026-04-27%20152401.jpg)

![Captura de tela 2026-04-27 152336](https://ajuda.magis5.com.br/hs-fs/hubfs/Captura%20de%20tela%202026-04-27%20152336.jpg?width=670&height=101&name=Captura%20de%20tela%202026-04-27%20152336.jpg)

Após marcar todas as opções disponíveis, clique em **“Done”** para salvar as alterações. Em seguida, role até o final da página e clique em **“Release”** para concluir a operação.

![Imagem 14: Após marcar todas as opções disponíveis, clique em “Done” para salvar as alterações. Em seguida, role até o final da…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-03-55-31-6902-PM.png?width=670&height=572&name=image-png-Apr-01-2026-03-55-31-6902-PM.png)

O **nome da versão (Version Name)** digite **"1.0**. Em seguida, clique novamente em **“Release”**.

![Captura de tela 2026-04-27 152632](https://ajuda.magis5.com.br/hs-fs/hubfs/Captura%20de%20tela%202026-04-27%20152632.jpg?width=670&height=145&name=Captura%20de%20tela%202026-04-27%20152632.jpg)

![Imagem 16: O nome da versão (Version Name) digite "1.0 . Em seguida, clique novamente em “Release” .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-03-58-59-4320-PM.png?width=670&height=302&name=image-png-Apr-01-2026-03-58-59-4320-PM.png)

Após processar, a versão do Magis será criada e você poderá confirmar que está **ativa**.

![Imagem 17: Após processar, a versão do Magis será criada e você poderá confirmar que está ativa .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-04-02-18-3773-PM.png?width=670&height=157&name=image-png-Apr-01-2026-04-02-18-3773-PM.png)

Para visualizar o token, acesse **“Settings”**. Na seção **“Credenciais”**, serão exibidos o **“Client ID”** e o **“Secret”**. Copie essas informações e guarde-as da mesma forma que fez com o ["Domínio"](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011557089431-Como-integrar-a-Shopify-no-Magis5-HUB#Token) no passo anterior.

![Imagem 18: Para visualizar o token, acesse “Settings” . Na seção “Credenciais” , serão exibidos o “Client ID” e o “Secret” . Copie…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-04-16-28-2719-PM.png?width=670&height=150&name=image-png-Apr-01-2026-04-16-28-2719-PM.png)

### Integrando a Shopify no Magis5 HUB

⚠️ **IMPORTANTE:**

**Com as informações do "[Dominio](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011557089431-Como-integrar-a-Shopify-no-Magis5-HUB#Token)", [“Client ID” e o “Secret”](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011557089431-Como-integrar-a-Shopify-no-Magis5-HUB#clientesecret), acesse o Magis5 HUB, essa informações serão necessárias para realizar a integração**

Feito o login no Magis5, vá para **"Configurações"**, depois até **"Integrações"** e por último clique em **"Lojas Virtuais "**.

![Imagem 19: Feito o login no Magis5, vá para "Configurações" , depois até "Integrações" e por último clique em "Lojas Virtuais " .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-04-50-25-4250-PM.png?width=670&height=229&name=image-png-Apr-01-2026-04-50-25-4250-PM.png)

Na página de integrações, clique em **"Adicionar nova integração"**.

![Imagem 20: Na página de integrações, clique em "Adicionar nova integração" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-04-51-17-3606-PM.png?width=619&height=238&name=image-png-Apr-01-2026-04-51-17-3606-PM.png)

### Como fazer o preenchimento da aba "Integração"

Selecione a opção **Shopify** no campo marketplace

![Captura de tela 2026-04-27 153333](https://ajuda.magis5.com.br/hs-fs/hubfs/Captura%20de%20tela%202026-04-27%20153333.jpg?width=670&height=163&name=Captura%20de%20tela%202026-04-27%20153333.jpg)

Preencha os 3 campos disponíveis no Magis5 HUB.

**- E-mail/Código da loja:** preencha com o **"Client ID" (ID do cliente)

- Token de acesso:** preencha com o **"Secret" (Chave secreta)**

**- Url da loja:** Insira o domínio da sua loja na **[Shopify](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011557089431-Como-integrar-a-Shopify-no-Magis5-HUB#Token) (terminado com myshopify.com).**

Após o preenchimento dos campos clique em **"Realizar Integração"

![Captura de tela 2026-04-27 154604](https://ajuda.magis5.com.br/hs-fs/hubfs/Captura%20de%20tela%202026-04-27%20154604.jpg?width=670&height=230&name=Captura%20de%20tela%202026-04-27%20154604.jpg)**
Você será redirecionado para a Shopify. , clique em **“Install**” para concluir a instalação do app do Magis5.

![Captura de tela 2026-04-27 155914](https://ajuda.magis5.com.br/hs-fs/hubfs/Captura%20de%20tela%202026-04-27%20155914.jpg?width=421&height=304&name=Captura%20de%20tela%202026-04-27%20155914.jpg)

Ao final do processo, você será redirecionado para o Magis5 HUB, conclua o restante do preenchimento dos campos.

**- Nome da sua loja:** você deverá colocar um nome que identifique sua loja no painel do Magis5.

**- Código da sua loja no ERP:**esse campo é alimentado com o código que identificará os pedidos dentro do seu ERP.

Segue a orientação de como prosseguir de acordo com cada sistema:

**- Bling:** dentro da sua conta responsável pelo controle de estoque no Magis5, você deve efetuar o passo a passo indicado no tutorial: [Como preencher o campo "Código da sua loja no ERP" utilizando o Bling!](https://sankhya.zendesk.com/hc/pt-br/articles/44011376979607) 

**- Faturador Magis5:**não há necessidade de preencher o campo caso utilize o faturador Magis5 como controlador de estoque. 

**- ERP Magis5:**você deverá informar o código do empreendimento responsável pelo faturamento dos pedidos dessa loja. 

**- Integração via API:**você deverá solicitar ao desenvolvedor ou suporte do seu ERP para que ele gere o código interno que identifica os pedidos dessa loja quando criados no ERP.

**- Omie:** você deverá efetuar o cadastro de um vendedor dentro da sua conta Omie. Esse vendedor deverá ter o mesmo nome da sua loja que será integrada, exemplo: Nome da Loja - Shopify
Após isso, é necessário solicitar ao suporte do Omie, o ID desse vendedor na API. O suporte irá lhe informar um código, ao qual deve ser incluso no campo "Código da sua loja no ERP" dentro do Magis5. 

**- Sankhya:** você deverá efetuar o cadastro de um vendedor dentro da sua conta Sankhya. Esse vendedor deverá ter o mesmo nome da sua loja que será integrada, exemplo: Nome da Loja - Shopify
Após isso, é necessário solicitar ao suporte do Sankhya, o ID desse vendedor na API. O suporte irá lhe informar um código, ao qual deve ser incluso no campo **"Código da sua loja no ERP"** dentro do Magis5. 

**- Código do vendedor:** Caso utilize o Magis ERP como principal, você deverá cadastrar um novo usuário no empreendimento informado no campo Código ERP. Para isso basta seguir o passo a passo indicado no tutorial: [[Magis ERP] Como preencher o campo "Código do vendedor" utilizando o Magis ERP](https://ajuda.magis5.com.br/como-preencher-o-campo-c%C3%B3digo-do-vendedor-utilizando-o-magis-erp?hsLang=pt-br)

Caso utilize outro ERP principal, esse campo é alimentado somente na condição que a loja que esta sendo integrada é do tipo oficial do Mercado Livre.

### Como fazer o preenchimento da aba "Empresas"

![Imagem 24: Como fazer o preenchimento da aba "Empresas"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-04-03-05-3254-PM.png?width=670&height=312&name=image-png-Apr-11-2025-04-03-05-3254-PM.png)

As informações cadastradas nessa aba vão alimentar os dados referente ao remetente na declaração de conteúdo.

**Nome -** deverá ser informado a Razão Social do CNPJ vinculado ao marketplace que será integrado.

**CNPJ -** deverá ser informado o CNPJ cadastrado na conta do marketplace que será integrado. 

**Inscrição Estadual -** deverá ser informado a IE cadastrado na conta do marketplace que será integrado.  

**Estado -** deverá ser selecionado o Estado a que pertence o cadastro do CNPJ vinculado a conta do marketplace que será integrado.

### Como fazer o preenchimento da aba "Notas fiscais"

**ERP emissão nota fiscal -**você deverá selecionar o ERP cadastrado no Magis5 que será responsável para emissão da nota fiscal. 

Caso sua loja **não faça a emissão de nota fiscal**, é necessário selecionar o ERP destinado ao controle de estoque.

1. **Habilitando a emissão automática de notas fiscais**Para ativar a emissão automática as seguintes opções deverão ser ativas:

   **1º** - Gerar nota fiscal de forma automática
   **2º** - Emitir nota fiscal de forma automática 
   **3º** - Gerar/Emitir nota fiscal automaticamente quando o pedido for para o status de Ag. Separação 
   **5º** - Aguardar etiqueta no marketplace para imprimir a declaração de conteúdo/nota fiscal 
   **7º** - Mostrar itens dos pedidos na declaração de conteúdo/Nota Fiscal 
   **8º** - Mostrar itens dos pedidos na declaração de conteúdo/Nota Fiscal 
   **9º** - Imprimir nota fiscal

**Observação:** as opções desmarcadas na imagem possuem detalhes importantes que são explicados a seguir. Leia atentamente o próximo tópico e, em caso de dúvidas, entre em contato com o suporte da Magis5.

![Imagem 25: Observação: as opções desmarcadas na imagem possuem detalhes importantes que são explicados a seguir. Leia atentamente…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-04-20-59-8681-PM.png?width=670&height=468&name=image-png-Apr-11-2025-04-20-59-8681-PM.png)

**Observações sobre as flags:**

Flag nº 3 - Gerar/Emitir nota fiscal automaticamente quando o pedido for para o status de Ag. Separação

- **se necessitar que a emissão das notas fiscais ocorra somente quando realizar a expedição dos pedidos, ela deverá ficar DESMARCADA.**

Flag nº 4 - Emitir nota fiscal de forma automática para pedidos flex

- **deverá ser MARCADA caso você precise emitir notas fiscais para os pedidos na modalidade de envio FLEX.**

Flag nº 6 - Adicionar o valor do frete automaticamente na nota fiscal

- **deverá ser MARCADA caso você tenha obrigatoriedade fiscal de destacar o valor do frete na nota fiscal (consulte sua contabilidade).**
- **se decidir trabalhar SEM o destaque do frete, é necessário verificar com o marketplace se eles aceitam a nota fiscal sem esse valor destacado.**

Flag nº 7 - Mostrar itens dos pedidos na declaração de conteúdo/Nota Fiscal

- **deverá ser DESMARCADA caso não queira visualizar a informação dos  itens vendidos na etiqueta de nota fiscal.**

Flag nº 8 - Imprimir nota fiscal

- **deverá ser DESMARCADA caso não deseje realizar a impressão da etiqueta de nota fiscal.**

2. **Desativando a emissão automática de notas fiscais**Para interromper a emissão automática de notas fiscais, somente as opções citadas devem se manter ativas:

**5º**- Aguardar etiqueta no marketplace para imprimir a declaração de conteúdo/nota fiscal 
**7º**- Mostrar itens dos pedidos na declaração de conteúdo/Nota Fiscal 
**8º**- Imprimir nota fiscal

![Imagem 26: 5º - Aguardar etiqueta no marketplace para imprimir a declaração de conteúdo/nota fiscal 7º - Mostrar itens dos pedidos…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-14-2025-05-17-41-0206-PM.png?width=670&height=426&name=image-png-Apr-14-2025-05-17-41-0206-PM.png)

**Observação sobre as flags:**

Flag nº 5 - Aguardar etiqueta no marketplace para imprimir a declaração de conteúdo/nota fiscal

- **deverá ser DESMARCADA caso você NAO utilize integração logística (Correios, Intelipost ou Mandaê) conectada a Magis5 para emitir etiqueta de envio para os pedidos ou caso o marketplace não forneça via API a etiqueta de envio para o Magis5.**

Flag nº 7 - Mostrar itens dos pedidos na declaração de conteúdo/Nota Fiscal

- **deverá ser DESMARCADA caso não queira visualizar a informação dos  itens vendidos na etiqueta de declaração de conteúdo.**

Flag nº 8 - Imprimir nota fiscal

- **deverá sempre permanecer marcada mesmo que não vá emitir nota fiscal.**

**Atenção:** caso deseje trabalhar com a emissão automática de notas fiscais desativada, o processo para efetuar o faturamento dos pedidos **deverá ser de forma manual**, indo até a tela de: Expedição>Picking>Bloco de Separação, selecionando os pedidos e clicando na opção **"Gerar/Emitir notas fiscais".**

![Imagem 27: Atenção: caso deseje trabalhar com a emissão automática de notas fiscais desativada, o processo para efetuar o…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-01-2026-06-31-52-4239-PM.png?width=670&height=280&name=image-png-Apr-01-2026-06-31-52-4239-PM.png)

### Como fazer o preenchimento da aba "Margens e custos"

**Esta seção aplica-se exclusivamente a usuários que utilizam a ferramenta de precificação automática do Magis5.**

Para entender como funciona a precificação automática basta clicar no link a seguir: [Como utilizar a precificação automática do Magis5?](https://sankhya.zendesk.com/hc/pt-br/articles/44010711255319)

Caso **não utilize** nossa ferramenta de precificação, os campos disponíveis nessa aba deverão ficar vazios.

### Como fazer o preenchimento da aba "Depósitos"

**Observação:** se para o marketplace que esta integrando você deseja efetuar a **configuração de baixa de estoque dos pedidos fulfillment dentro do ERP**, é necessário **acionar o time de Suporte da Magis5 para efetuar a configuração.**

Caso **NÃO** tenha necessidade, os campos **"Código do depósito fulfillment"**, **"Código da sua loja ERP no fulfillment"** e "**Código do vendedor no fulfillment"** devem ficar vazios.

![Imagem 28: Caso NÃO tenha necessidade, os campos "Código do depósito fulfillment" , "Código da sua loja ERP no fulfillment" e "…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-05-59-53-5963-PM.png?width=664&height=131&name=image-png-Apr-11-2025-05-59-53-5963-PM.png)

Para otimizar o controle do seu estoque, o sistema oferece duas opções de baixa de estoque automática quando um pedido é recebido do marketplace;

1. **Baixa em um Único Depósito:** Selecione um depósito específico para que a baixa de estoque ocorra sempre a partir dele, independentemente da disponibilidade em outros locais.
2. **Priorização de Depósitos:** Defina uma ordem de prioridade entre seus depósitos. O sistema buscará o item no primeiro depósito da lista. Caso não haja estoque suficiente, prosseguirá para o próximo depósito na ordem definida, e assim por diante.

**Opção 1 - Como configurar a baixa de estoque em um único depósito**
Deverá selecionar nesta tela o depósito que os pedidos de venda deverão descontar estoque, o preenchimento deve ser feito da seguinte forma:

1. seleciono o depósito
2. no campo prioridade incluo o valor "1"

![Imagem 29: no campo prioridade incluo o valor "1"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-06-02-36-9169-PM.png?width=670&height=368&name=image-png-Apr-11-2025-06-02-36-9169-PM.png)

**Opção 2 - Como configurar a priorização de depósitos para baixa de estoque**

Como funciona?

1. **Tentativa de baixa no depósito prioritário:** O sistema verificará se há estoque disponível no depósito designado como prioritário (o que está alimentado o campo prioridade com o valor 1).
2. **Verificação de estoque insuficiente:**Caso o depósito prioritário não possua estoque suficiente para atender ao pedido, o sistema avançará para o próximo depósito na lista de prioridades.
3. **Tentativa de baixa no depósito secundário (e subsequentes):** O sistema tentará baixar o estoque do próximo depósito na ordem de prioridade (o que está alimentado o campo prioridade com o valor 2).

Com isso, basta selecionar os depósito e indicar a ordem de baixa de acordo com a imagem a seguir:

![Imagem 30: Com isso, basta selecionar os depósito e indicar a ordem de baixa de acordo com a imagem a seguir:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-06-07-08-7894-PM.png?width=670&height=397&name=image-png-Apr-11-2025-06-07-08-7894-PM.png)

### Como fazer o preenchimento da aba "Comissão"

O Magis5 define comissões padrão para cada marketplace integrado. No entanto, caso você trabalhe com uma taxa de comissão **distinta** daquela predefinida pelo sistema, é **obrigatório** informar o valor correto nesta aba.

Para conferir as comissões padrões utilizadas basta clicar no link:
[Comissões Padrão para precificação automática](https://ajuda.magis5.com.br/entenda-a-comiss%C3%A3o-padr%C3%A3o?hsLang=pt-br)

Caso **não utilize** nossa ferramenta de precificação, os campos disponíveis nessa aba deverão ficar vazios.

### Como fazer o preenchimento da aba "Impressoras"

Os campos disponíveis nessa aba devem ficar vazios.

### Como fazer o preenchimento da aba "Logística"

Se for utilizar alguma integração logística como: Correios, Intelipost ou Mandaê para a emissão de etiquetas de envio da loja que esta integrando, em primeiro momento deve deixar os campos "Integração Logística Correios" e "Dados da Transportadora" definidos como "Selecione" e após concluir a integração do marketplace, acione nosso time de suporte para lhe apoiar na configuração dessa aba.

### Como fazer o preenchimento da aba "Envio"

Essa aba somente é preenchida quando possui a integração logística Intelipost conectada ao Magis5. Caso você **não utilize** essa integração logística, os campos apresentados nessa aba devem ficar vazios.

### Como fazer o preenchimento da aba "Etiqueta"

Nessa aba é possível selecionar quais dados você deseja que apareçam disponíveis na etiqueta de nota fiscal ou de declaração de conteúdo. As opções podem ser marcadas de forma distinta.

Após ter finalizado o preenchimento das abas necessárias, para concluir o processo de integração basta estar clicando na opção **"Realizar Integração"**.

**Observação:** a loja que acabou de integrar será exibida no painel principal do Magis5 somente após a importação do primeiro pedido de venda.

### Atualização de token

Quando a integração apresentar o token expirado,  identificado pelo indicador na cor amarela e pela mensagem **"Token expirado"**  será necessário atualizar o token para que a integração volte a funcionar corretamente.

![Imagem 31: Atualização de token](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-27-2026-01-36-03-8495-PM.png?width=670&height=47&name=image-png-Jul-27-2026-01-36-03-8495-PM.png)

Para realizar essa atualização, é necessário abrir um chamado junto à nossa **equipe de [Suporte](https://ajuda.sankhya.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br)**, que fará a renovação do token de forma adequada, restabelecendo o funcionamento completo da integração.
