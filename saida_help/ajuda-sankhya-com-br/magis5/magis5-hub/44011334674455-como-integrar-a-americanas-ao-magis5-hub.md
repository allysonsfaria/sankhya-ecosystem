---
id: "44011334674455"
titulo: "Como integrar a Americanas ao Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011334674455-Como-integrar-a-Americanas-ao-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:02:05Z"
rotulos: ["sync_hc", "magis5", "magis5_204055206966", "sync_hash_cfdc077e6fe8"]
---

# Como integrar a Americanas ao Magis5 Hub?

## Entenda como Integrar a Americanas no Magis5 Hub

### Antes de começar:

---

Para integrar a Americanas ao Magis inicialmente precisará acessar a plataforma Americanas [Acesse a plataforma](https://vendedores.americanas.com.br/v3/login) com o seu e-mail e senha.

Quando estiver logado em sua conta Americanas, no menu na lateral esquerda vá em "**Segurança"** e depois em **"Gestão de Usuário"**

![Imagem 1: Quando estiver logado em sua conta Americanas, no menu na lateral esquerda vá em " Segurança" e depois em "Gestão de…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-02-31-19-6011-PM.png?width=670&height=389&name=image-png-May-27-2025-02-31-19-6011-PM.png)

Após clicar em **Gestão de Usuário** será exibido em telas os Usuários localize qual e-mail seria o Usuário **ADMIN**, você consegue visualizar se o e-mail seria o ADMIN editando o cadastro, a informação do E-mail ADMIN será necessária para a integração no Magis5 HUB.
![Imagem 2: Quando estiver logado em sua conta Americanas, no menu na lateral esquerda vá em " Segurança" e depois em "Gestão de…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-02-37-55-5490-PM.png?width=670&height=262&name=image-png-May-27-2025-02-37-55-5490-PM.png)

![Imagem 3: Quando estiver logado em sua conta Americanas, no menu na lateral esquerda vá em " Segurança" e depois em "Gestão de…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-02-39-51-5461-PM.png?width=324&height=467&name=image-png-May-27-2025-02-39-51-5461-PM.png)

### Obtendo o token API

Para integrar o Magis5 Hub com o marketplace Americanas, é necessário obter o token na própria plataforma da Americanas.
Ainda no painel da Americanas, acesse o menu lateral, vá até a opção **"Integrações"** e, em seguida, selecione **"Credenciais API",** em Credenciais visualize a informação de token copie essa informação, pois ela será utilizada na  integração com o Magis5 Hub.

![Imagem 4: Para integrar o Magis5 Hub com o marketplace Americanas, é necessário obter o token na própria plataforma da…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-05-43-48-2030-PM.png?width=670&height=211&name=image-png-May-27-2025-05-43-48-2030-PM.png)

### Integrando a Americanas com o Magis5 Hub

No Magis5 Hub, vá até **"Configurações"**, depois até**"Integrações"** e por último clique em **"Marketplaces"**. 

![Imagem 5: No Magis5 Hub, vá até "Configurações" , depois até "Integrações" e por último clique em "Marketplaces" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-05-48-01-9585-PM.png?width=614&height=359&name=image-png-May-27-2025-05-48-01-9585-PM.png)

Na página de integrações, clique em **"Adicionar nova integração"**.

![Imagem 6: Na página de integrações, clique em "Adicionar nova integração" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-25-2025-06-50-25-1040-PM.png?width=554&height=266&name=image-png-Apr-25-2025-06-50-25-1040-PM.png)

### Como fazer o preenchimento da aba "Integração"

**Selecione "Americanas"** no campo marketplace e preencha os campos conforme orientação abaixo: 

![Imagem 7: Selecione "Americanas" no campo marketplace e preencha os campos conforme orientação abaixo:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-05-51-16-4714-PM.png?width=670&height=153&name=image-png-May-27-2025-05-51-16-4714-PM.png)

**- Nome da sua loja:** você deverá colocar um nome que identifique sua loja no painel do Magis5.

**- Código da sua loja no ERP:**esse campo é alimentado com o código que identificará os pedidos dentro do seu ERP.

Segue a orientação de como prosseguir de acordo com cada sistema:

**- Bling:** dentro da sua conta responsável pelo controle de estoque no Magis5, você deve efetuar o passo a passo indicado no tutorial: [Como preencher o campo "Código da sua loja no ERP" utilizando o Bling!](https://ajuda.magis5.com.br/para-que-serve-o-campo-c%C3%B3digo-da-sua-loja-no-erp-e-como-utiliza-lo?hsLang=pt-br) 

**- Faturador Magis5:**não há necessidade de preencher o campo caso utilize o faturador Magis5 como controlador de estoque. 

**- ERP Magis5:**você deverá informar o código do empreendimento responsável pelo faturamento dos pedidos dessa loja. 

**- Integração via API:**você deverá solicitar ao desenvolvedor ou suporte do seu ERP para que ele gere o código interno que identifica os pedidos dessa loja quando criados no ERP.

**- Omie:** você deverá efetuar o cadastro de um vendedor dentro da sua conta Omie. Esse vendedor deverá ter o mesmo nome da sua loja que será integrada, exemplo: Nome da Loja - Americanas
Após isso, é necessário solicitar ao suporte do Omie, o ID desse vendedor na API. O suporte irá lhe informar um código, ao qual deve ser incluso no campo "Código da sua loja no ERP" dentro do Magis5. 

**- Sankhya:** você deverá efetuar o cadastro de um vendedor dentro da sua conta Sankhya. Esse vendedor deverá ter o mesmo nome da sua loja que será integrada, exemplo: Nome da Loja - Americanas
Após isso, é necessário solicitar ao suporte do Sankhya, o ID desse vendedor na API. O suporte irá lhe informar um código, ao qual deve ser incluso no campo "Código da sua loja no ERP" dentro do Magis5. 

**- Loja Oficial:**essa flag deve ser marcada apenas em integrações Mercado Livre

**- E-mail/Código da loja:**esse campo deve ser preenchido com a informação do E-mail [ADMIN](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011334674455-Como-integrar-a-Americanas-ao-Magis5-Hub#EmailADMIN) cadastrado no portal Americanas

**- Token de acesso:**esse campo deve ser preenchido com a informação de [TOKEN](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011334674455-Como-integrar-a-Americanas-ao-Magis5-Hub#TokenAmericanas) copiada no portal da Americanas**.**
**- Código do vendedor:** caso utilize o Magis ERP como principal, você deverá cadastrar um novo usuário no empreendimento informado no campo Código ERP. Para isso basta seguir o passo a passo indicado no tutorial: [[Magis ERP] Como preencher o campo "Código do vendedor" utilizando o Magis ERP](https://ajuda.magis5.com.br/como-preencher-o-campo-c%C3%B3digo-do-vendedor-utilizando-o-magis-erp?hsLang=pt-br)

Caso utilize outro ERP principal, esse campo é alimentado somente na condição que a loja que esta sendo integrada é do tipo oficial do Mercado Livre.

### Como fazer o preenchimento da aba "Empresas"

![Imagem 8: Como fazer o preenchimento da aba "Empresas"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-04-03-05-3254-PM.png?width=670&height=312&name=image-png-Apr-11-2025-04-03-05-3254-PM.png)

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
   **9º** - Imprimir nota fiscal

**Observação:** as opções desmarcadas na imagem possuem detalhes importantes que são explicados a seguir. Leia atentamente o próximo tópico e, em caso de dúvidas, entre em contato com o suporte da Magis5.

![Imagem 9: Observação: as opções desmarcadas na imagem possuem detalhes importantes que são explicados a seguir. Leia atentamente…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-04-20-59-8681-PM.png?width=670&height=468&name=image-png-Apr-11-2025-04-20-59-8681-PM.png)

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

![Imagem 10: 5º - Aguardar etiqueta no marketplace para imprimir a declaração de conteúdo/nota fiscal 7º - Mostrar itens dos pedidos…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-14-2025-05-17-41-0206-PM.png?width=670&height=427&name=image-png-Apr-14-2025-05-17-41-0206-PM.png)

**Observação sobre as flags:**

Flag nº 5 - Aguardar etiqueta no marketplace para imprimir a declaração de conteúdo/nota fiscal

- **deverá ser DESMARCADA caso você NAO utilize integração logística (Correios, Intelipost ou Mandaê) conectada a Magis5 para emitir etiqueta de envio para os pedidos ou caso o marketplace não forneça via API a etiqueta de envio para o Magis5.**

Flag nº 7 - Mostrar itens dos pedidos na declaração de conteúdo/Nota Fiscal

- **deverá ser DESMARCADA caso não queira visualizar a informação dos  itens vendidos na etiqueta de declaração de conteúdo.**

Flag nº 8 - Imprimir nota fiscal

- **deverá sempre permanecer marcada mesmo que não vá emitir nota fiscal.**

**Atenção:** caso deseje trabalhar com a emissão automática de notas fiscais desativada, o processo para efetuar o faturamento dos pedidos **deverá ser de forma manual**, indo até a tela de: Expedição>Picking>Bloco de Separação, selecionando os pedidos e clicando na opção "Gerar/Emitir notas fiscais".

![Imagem 11: Atenção: caso deseje trabalhar com a emissão automática de notas fiscais desativada, o processo para efetuar o…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-May-27-2025-06-19-31-6113-PM.png?width=670&height=261&name=image-png-May-27-2025-06-19-31-6113-PM.png)

### Como fazer o preenchimento da aba "Margens e custos"

**Esta seção aplica-se exclusivamente a usuários que utilizam a ferramenta de precificação automática do Magis5.**

Para entender como funciona a precificação automática basta clicar no link a seguir: [Como utilizar a precificação automática do Magis5?](https://sankhya.zendesk.com/hc/pt-br/articles/44010711255319)

Caso **não utilize** nossa ferramenta de precificação, os campos disponíveis nessa aba deverão ficar vazios.

### Como fazer o preenchimento da aba "Depósitos"

**Observação:** se para o marketplace que esta integrando você deseja efetuar a **configuração de baixa de estoque dos pedidos fulfillment dentro do ERP**, é necessário **acionar o time de Suporte da Magis5 para efetuar a configuração.**

Caso **NÃO** tenha necessidade, os campos **"Código do depósito fulfillment"**, **"Código da sua loja ERP no fulfillment"** e "**Código do vendedor no fulfillment"** devem ficar vazios.
![Imagem 12: Caso NÃO tenha necessidade, os campos "Código do depósito fulfillment" , "Código da sua loja ERP no fulfillment" e "…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-05-59-53-5963-PM.png?width=670&height=131&name=image-png-Apr-11-2025-05-59-53-5963-PM.png)

Para otimizar o controle do seu estoque, o sistema oferece duas opções de baixa de estoque automática quando um pedido é recebido do marketplace;

1. **Baixa em um Único Depósito:** Selecione um depósito específico para que a baixa de estoque ocorra sempre a partir dele, independentemente da disponibilidade em outros locais.
2. **Priorização de Depósitos:** Defina uma ordem de prioridade entre seus depósitos. O sistema buscará o item no primeiro depósito da lista. Caso não haja estoque suficiente, prosseguirá para o próximo depósito na ordem definida, e assim por diante.

**Opção 1 - Como configurar a baixa de estoque em um único depósito**
Deverá selecionar nesta tela o depósito que os pedidos de venda deverão descontar estoque, o preenchimento deve ser feito da seguinte forma:

1. seleciono o depósito
2. no campo prioridade incluo o valor "1"

![Imagem 13: no campo prioridade incluo o valor "1"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-06-02-36-9169-PM.png?width=670&height=368&name=image-png-Apr-11-2025-06-02-36-9169-PM.png)

A configuração mostrada na imagem acima direciona todos os pedidos de venda da loja que esta integrando para que o estoque seja debitado exclusivamente do depósito denominado "Primário".

**Opção 2 - Como configurar a priorização de depósitos para baixa de estoque**

Como funciona?

1. **Tentativa de baixa no depósito prioritário:** O sistema verificará se há estoque disponível no depósito designado como prioritário (o que está alimentado o campo prioridade com o valor 1).
2. **Verificação de estoque insuficiente:**Caso o depósito prioritário não possua estoque suficiente para atender ao pedido, o sistema avançará para o próximo depósito na lista de prioridades.
3. **Tentativa de baixa no depósito secundário (e subsequentes):** O sistema tentará baixar o estoque do próximo depósito na ordem de prioridade (o que está alimentado o campo prioridade com o valor 2).

Com isso, basta selecionar os depósito e indicar a ordem de baixa de acordo com a imagem a seguir:

![Imagem 14: Com isso, basta selecionar os depósito e indicar a ordem de baixa de acordo com a imagem a seguir:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Apr-11-2025-06-07-08-7894-PM.png?width=670&height=397&name=image-png-Apr-11-2025-06-07-08-7894-PM.png)

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

**Observação:** a loja que acabou de integrar será exibida no painel principal do Magis5 somente após a importação do primeiro pedido de venda.
