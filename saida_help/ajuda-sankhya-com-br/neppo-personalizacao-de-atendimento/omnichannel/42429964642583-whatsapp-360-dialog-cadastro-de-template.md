---
id: "42429964642583"
titulo: "WhatsApp 360 Dialog - Cadastro de Templates"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T15:58:35Z"
rotulos: ["sync_hc", "neppo", "neppo_345243664", "sync_hash_3c3de3546e18"]
---

# WhatsApp 360 Dialog - Cadastro de Templates

Este manual detalha o processo de ponta-a-ponta para a configuração de **Templates do WhatsApp**, que são essenciais para o envio de mensagens ativas.

O objetivo é guiar o administrador pelas duas fases obrigatórias do processo: primeiro, a criação e aprovação do template junto à Meta (Facebook/360) e, segundo, o cadastro desse template já aprovado dentro da plataforma Neppo.

- [CRIANDO UM TEMPLATE](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#CRIANDO-UM-TEMPLATE)
  - [Visão geral da interface do usuário do modelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Visao-geral-da-interface-do-usuario-do-modelo)
  - [Processo de verificação de modelo do Facebook para a API WhatsApp](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Processo-de-verificacao-de-modelo-do-Facebook-para-a-API-WhatsApp)
  - [Crie um modelo de mensagem do WhatsApp](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Crie-um-modelo-de-mensagem-do-WhatsApp)
  - [Criação de modelos de mídia](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Criacao-de-modelos-de-midia)
- [Importante:](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Importante)
  - [Adicionar Template (Empresa)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Adicionar-Template-Empresa)
  - [Editar Cadastro de Template](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429964642583-WhatsApp-360-Dialog-Cadastro-de-Templates#Editar-Cadastro-de-Template)

## CRIANDO UM TEMPLATE

O processo de cadastro de template está disponível nos **documentos do 360** nesse link: [Templates](https://docs.360dialog.com/docs/account-management/the-360-client-hub/template-management-ui#sample-templates)

Cada conta tem seu próprio conjunto de **Templates,** com um limite máximo de 250 modelos de mensagens.

Para acessar seus modelos de mensagem, encontre o número WABA ao qual deseja adicionar um modelo de mensagem e clique no botão **Manage Templates** conforme a imagem abaixo.

![Imagem 1: Para acessar seus modelos de mensagem, encontre o número WABA ao qual deseja adicionar um modelo de mensagem e clique…](https://ajuda.sankhya.com.br/hc/article_attachments/42637451443607)

### Visão geral da interface do usuário do modelo

Esta é a página inicial do Gerenciamento de Modelos, onde você pode obter uma visão geral de todos os modelos do seu número.

![Imagem 2: Editar modelo](https://ajuda.sankhya.com.br/hc/article_attachments/42637493547031) Editar modelo

![Imagem 3: Adicione um idioma diferente a um modelo](https://ajuda.sankhya.com.br/hc/article_attachments/42637479652119) Adicione um idioma diferente a um modelo

![Imagem 4: Replicar modelo.](https://ajuda.sankhya.com.br/hc/article_attachments/42637508343191) Replicar modelo.

![Imagem 5: Apagar modelo.](https://ajuda.sankhya.com.br/hc/article_attachments/42637508552343) Apagar modelo.

![Imagem 6: Apagar modelo.](https://ajuda.sankhya.com.br/hc/article_attachments/42637508744855)

### Processo de verificação de modelo do Facebook para a API WhatsApp

As mensagens modelo devem ser enviadas ao Facebook para revisão antes de estarem disponíveis para uso. O status desta revisão pode ser visto pela cor do idioma do modelo.

● **Rascunho:** Os modelos com fundo cinza estão em modo de rascunho e ainda não foram enviados para revisão pelo Facebook

![Imagem 7: ● Rascunho: Os modelos com fundo cinza estão em modo de rascunho e ainda não foram enviados para revisão pelo Facebook](https://ajuda.sankhya.com.br/hc/article_attachments/42637480370455)

● **Pendente:** Os modelos pendentes têm um fundo amarelo. O Facebook está verificando a solicitação do modelo. Aguarde até que mais informações sejam fornecidas pelo Facebook.

![Imagem 8: ● Pendente: Os modelos pendentes têm um fundo amarelo. O Facebook está verificando a solicitação do modelo. Aguarde até…](https://ajuda.sankhya.com.br/hc/article_attachments/42637452789911)

● **Aprovado:** Seu modelo foi aprovado pelo Facebook e pode ser usado para enviar mensagens de modelo aos seus clientes.

![Imagem 9: ● Aprovado: Seu modelo foi aprovado pelo Facebook e pode ser usado para enviar mensagens de modelo aos seus clientes.](https://ajuda.sankhya.com.br/hc/article_attachments/42637494683799)

● **Rejeitado:** Este modelo foi rejeitado. Reveja os nossos documentos de mensagens de modelo para obter ajuda com a aprovação de mensagens de modelo.

![Imagem 10: ● Rejeitado: Este modelo foi rejeitado. Reveja os nossos documentos de mensagens de modelo para obter ajuda com a…](https://ajuda.sankhya.com.br/hc/article_attachments/42637468615319)

### Crie um modelo de mensagem do WhatsApp

Para criar um modelo de mensagem, clique no botão azul **Add Template** na página inicial. Ao criar seu modelo, você precisará incluir as seguintes informações:

**● Nome do modelo**

○ O nome só pode conter caracteres alfanuméricos minúsculos e sublinhados (\_)

**●Categorias de modelo**
**Utilidade:** Templates que facilitam uma solicitação, transação ou atualização específica e consentida pelo cliente sobre uma transação em andamento. Exemplos são notificações pós-compra e faturas recorrentes.
**Autenticação:** Os templates que permitem a uma empresa autenticar usuários com senhas de uso único, potencialmente em vários passos durante o processo de login (p. ex., verificação de conta, recuperação de conta, palavra secreta).
**Marketing:** Os templates que incluem promoções ou ofertas, atualizações informacionais ou convites para clientes responderem/tomarem ação.

Toda conversa que não se qualifica como mensagem de utilidade ou autenticação é uma conversa de marketing.
**Obs. Os valores cobrados para realizar os envios variam de acordo com a categoria do modelo.** [Consulte aqui](https://developers.facebook.com/docs/whatsapp/pricing#how-it-works)

**● Permitir mudança de categoria\***
Selecionar SIM ou NÃO.
\*Habilitar a mudança de categoria permite que a meta atribua qualquer categoria que eles determinem ser apropriada e recomendamos ter isso ativado para evitar modelos rejeitados devido à categorização incorreta.

Ressaltamos que os modelos ainda podem ser rejeitados por outros motivos não relacionados à sua categorização.

**● Linguagem de template**

○ Preencha em português (PT-BR), mesmo que o template esteja em outro idioma, pois a plataforma está configurada nesse idioma. Caso a operação da empresa não ocorra no Brasil, especifique o idioma correspondente.

**● Tipo de modelo**

○ Padrão (somente texto) ou modelo de mídia

![Imagem 11: ○ Padrão (somente texto) ou modelo de mídia](https://ajuda.sankhya.com.br/hc/article_attachments/42637495060759)![Imagem 12: ○ Padrão (somente texto) ou modelo de mídia](https://ajuda.sankhya.com.br/hc/article_attachments/42637468951959)

Os modelos de mensagem padrão têm apenas uma seção BODY, que é o único item obrigatório.
Para adicionar uma variável, insira **{{#}}** na posição desejada, onde # representa o índice da variável, iniciando em **{{1}}.**

Exemplo:

Olá, {{1}}, tudo bem?

Aqui é {{2}}, gostaria de confirmar seu agendamento do dia {{3}} e horário {{4}}.

Nesse exemplo, temos 4 variáveis, e será necessário preencher valores de exemplo para cada uma delas. Isso é importante para que a Meta reconheça quais informações serão dinâmicas durante o envio da mensagem.

![Imagem 13: Nesse exemplo, temos 4 variáveis, e será necessário preencher valores de exemplo para cada uma delas. Isso é importante…](https://ajuda.sankhya.com.br/hc/article_attachments/42637453633175)

### Criação de modelos de mídia

Os modelos de mídia têm mais blocos de construção e recursos. Consiste nos seguintes blocos de construção:

![Imagem 14: Os modelos de mídia têm mais blocos de construção e recursos. Consiste nos seguintes blocos de construção:](https://ajuda.sankhya.com.br/hc/article_attachments/42637464747415)

**CABEÇALHO**

O cabeçalho é opcional e serve como título ou cabeçalho do seu modelo. Suporta o seguinte:

● Texto

● Imagem ( É possível incluir imagem somente no cabeçalho)

● Documento (É possível incluir documento somente no cabeçalho)

● Vídeo (É possível incluir vídeo somente no cabeçalho)

ATENÇÃO: Ao adicionar imagem, documento e vídeo é necessário inserir a URL
(Caso não consiga gerar o link acesse o vídeo com o passo a passo GERAR LINK ARQUIVO .mkv).

![Imagem 15: ATENÇÃO: Ao adicionar imagem, documento e vídeo é necessário inserir a URL (Caso não consiga gerar o link acesse o…](https://ajuda.sankhya.com.br/hc/article_attachments/42637495623959)

**CORPO**

O corpo deve conter o texto mais importante do seu modelo. Apenas texto é compatível.

![Imagem 16: O corpo deve conter o texto mais importante do seu modelo. Apenas texto é compatível.](https://ajuda.sankhya.com.br/hc/article_attachments/42637469657367)

**RODAPÉ**

O rodapé suporta apenas texto e pode ser usado para fornecer informações menos relevantes em seu modelo de mensagem(Não terá variável).

**BOTÃO**

O botão adiciona interatividade aos seus modelos.

Você pode cadastrar até 10 botões por template no total.

Porém, existem limites específicos por tipo de botão:

• Resposta rápida: até 10 botões

• URL: até 2 botões

• Telefone: até 1 botão

Se o template tiver mais de 3 botões, apenas 2 aparecerão na mensagem e os demais ficarão em um botão "Ver todas as opções".

**● Botão de resposta rápida**

○ Usado para obter respostas rápidas de seu cliente
○ Ao selecionar o botão, o atendimento será aberto automaticamente para o cliente, e é possível configurar tratativas específicas de retorno com base no botão escolhido, essa configuração é opcional e pode ser utilizada conforme a estratégia do atendimento.

![Imagem 17: ○ Usado para obter respostas rápidas de seu cliente ○ Ao selecionar o botão, o atendimento será aberto automaticamente…](https://ajuda.sankhya.com.br/hc/article_attachments/42637495983383)

As informações contidas nos botões de resposta rápida não utilizam variáveis.

Ou seja, o conteúdo cadastrado previamente no 360 será enviado exatamente da mesma forma ao cliente, sem a necessidade de preenchimento de dados variáveis no momento do envio.

**● Botão de apelo à ação**

Usado para enviar seu cliente a um site ou ligar para um número de telefone

**● Botão de telefone:**
Para configurar esse botão, é necessário informar um nome e um número de telefone.

Ao clicar, o cliente será direcionado automaticamente para a área de discagem do celular, facilitando a realização da ligação.

![Imagem 18: Ao clicar, o cliente será direcionado automaticamente para a área de discagem do celular, facilitando a realização da…](https://ajuda.sankhya.com.br/hc/article_attachments/42637454533015)

As informações do botão de telefone **não utilizam variáveis**.

O conteúdo cadastrado previamente no 360 será enviado exatamente como registrado, sem necessidade de preenchimento dinâmico no momento do envio.

**Botão de URL:**
Neste botão, é necessário informar um nome e um link (URL).

O link pode ser fixo ou ter parte variável, dependendo da necessidade.

Caso deseje enviar sempre o mesmo link, basta cadastrá-lo normalmente.

**Exemplo:**
Envio do link do site da empresa <https://neppo.com.br> .

![Imagem 19: Caso deseje enviar sempre o mesmo link, basta cadastrá-lo normalmente. Exemplo: Envio do link do site da empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/42637454764951)

Caso seja necessário que parte do link varie a cada envio, clique em “Add variable” para tornar esse trecho editável.

**Exemplo:**

Envio de diferentes páginas do mesmo site:
<https://neppo.com.br/neppo-tecnologia/>
<https://neppo.com.br/programa-parcerias/>
<https://neppo.com.br/contato-neppo/>

Nesse caso, como o trecho após https://neppo.com.br/ muda em cada envio, é necessário utilizar uma variável.

A variável representará os caminhos "neppo-tecnologia/", "programa-parcerias/" e "contato-neppo/", que deverão ser preenchidos no momento da aprovação do template e do envio.

![Imagem 20: A variável representará os caminhos "neppo-tecnologia/", "programa-parcerias/" e "contato-neppo/", que deverão ser…](https://ajuda.sankhya.com.br/hc/article_attachments/42637499313687)

## Importante:

Antes de submeter o template, é necessário fornecer um exemplo da variável no link, caso ela exista.

Se o link for o mesmo em todos os envios, esse preenchimento não será necessário, pois o conteúdo será fixo.

Lembre-se: sempre que houver uma variável no link, o preenchimento dessa informação deve ser feito não só na aprovação, mas também no momento do envio.

![Imagem 21: Lembre-se: sempre que houver uma variável no link, o preenchimento dessa informação deve ser feito não só na aprovação,…](https://ajuda.sankhya.com.br/hc/article_attachments/42637470754455)

**Observação**: Todos os modelos requerem um corpo. Cabeçalhos, rodapés e botões são opcionais.

**Modelos de amostra**

Para todas as contas, o WhatsApp já registra uma série de modelos de amostra pré-aprovados. Esses modelos podem ser usados a qualquer momento e **não podem ser excluídos** . Os modelos de amostra sempre têm sample\_ no nome, conforme a imagem abaixo.

![Imagem 22: Para todas as contas, o WhatsApp já registra uma série de modelos de amostra pré-aprovados. Esses modelos podem ser…](https://ajuda.sankhya.com.br/hc/article_attachments/42637496881303)

**Cadastro de template**

No menu acesse o seguinte caminho: Configurações > Plataforma > Templates WhatsApp ou Buscar no campo de pesquisa “Templates WhatsApp”.

![Imagem 23: No menu acesse o seguinte caminho: Configurações > Plataforma > Templates WhatsApp ou Buscar no campo de pesquisa…](https://ajuda.sankhya.com.br/hc/article_attachments/42637455633431)

Quando clicar nessa opção, outra tela é aberta, com os locais de “Nome do Elemento”, “Nome do Espaço” e “Modelo”.

Na tela Templates WhatsApp estarão os templates utilizados pelo WhatsApp Enterprise para envio de mensagens ativas. É necessária a aprovação prévia desse template junto ao Whatsapp, para que esse possa ser utilizado na plataforma.

Eles existem como uma forma de garantir que as mensagens enviadas pelo canal estejam de acordo com as diretrizes de conteúdo permitidas. Após o template ser aprovado pelo WhatsApp, utilizar essa opção para cadastrá-lo na plataforma.

![Imagem 24: Eles existem como uma forma de garantir que as mensagens enviadas pelo canal estejam de acordo com as diretrizes de…](https://ajuda.sankhya.com.br/hc/article_attachments/42637455876375)

### Adicionar Template (Empresa)

Para adicionar novos templates na lista de Templates WhatsApp, basta clicar na opção localizado no canto direito e superior da tela ![Imagem 25: Para adicionar novos templates na lista de Templates WhatsApp, basta clicar na opção localizado no canto direito e…](https://ajuda.sankhya.com.br/hc/article_attachments/42637456075159) .

Após isto, outra tela será aberta, como mostra a Figura abaixo:

![Imagem 26: Após isto, outra tela será aberta, como mostra a Figura abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42637471909015)![Imagem 27: Após isto, outra tela será aberta, como mostra a Figura abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42637512415127)![Imagem 28: Após isto, outra tela será aberta, como mostra a Figura abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42637500797207)

Para adicionar novas listas, siga o passo a passo. É importante ressaltar que o administrador deve preencher corretamente de acordo com o template já aprovado pelo Whatsapp.

● Coloque o Nome do Elemento.

![Imagem 29: ● Coloque o Nome do Elemento.](https://ajuda.sankhya.com.br/hc/article_attachments/42637472538391)

Onde encontrar: Acessar o site do 360 > Mostrar detalhes > Templates. O nome do elemento é equivalente a parte a “name” conforme a imagem abaixo.

![Imagem 30: Onde encontrar: Acessar o site do 360 > Mostrar detalhes > Templates. O nome do elemento é equivalente a parte a “name”…](https://ajuda.sankhya.com.br/hc/article_attachments/42637484304791)

● Coloque o Nome do Espaço

![Imagem 31: ● Coloque o Nome do Espaço](https://ajuda.sankhya.com.br/hc/article_attachments/42637484495511)

Onde encontrar: Ao acessar o site do 360, você deve acessar a aba de Mostrar detalhes, e depois você encontrará um campo com a informação de Namespace.

![Imagem 32: Onde encontrar: Ao acessar o site do 360, você deve acessar a aba de Mostrar detalhes, e depois você encontrará um…](https://ajuda.sankhya.com.br/hc/article_attachments/42637513239447)

● Opção para ativar ou desativar um Template

![Imagem 33: ● Opção para ativar ou desativar um Template](https://ajuda.sankhya.com.br/hc/article_attachments/42637498849559)

● Coloque a Descrição. (Repetir o texto que está escrito no elemento)

![Imagem 34: ● Coloque a Descrição. (Repetir o texto que está escrito no elemento)](https://ajuda.sankhya.com.br/hc/article_attachments/42637525054871)

● Coloque o Modelo (Mensagem cadastrada dentro do template)

![Imagem 35: ● Para adicionar os tipos de parâmetros basta flegar as opções do template e depois conforme o modelo adicionar a…](https://ajuda.sankhya.com.br/hc/article_attachments/42637513837719)
● Para adicionar os tipos de parâmetros basta flegar as opções do template e depois conforme o modelo adicionar a quantidade de parâmetros através das setas.

![Imagem 36: ● Para adicionar os tipos de parâmetros basta flegar as opções do template e depois conforme o modelo adicionar a…](https://ajuda.sankhya.com.br/hc/article_attachments/42637514090519)

**Cabeçalho:**
Caso o envio seja de um vídeo, imagem ou documento clique em Mídia.

![Imagem 37: Cabeçalho: Caso o envio seja de um vídeo, imagem ou documento clique em Mídia.](https://ajuda.sankhya.com.br/hc/article_attachments/42637485621911)

**Corpo:**
Caso tenham parâmetros no corpo da mensagem informe a quantidade e mantenha como
Texto, não é necessário alterar.

![Imagem 38: Corpo: Caso tenham parâmetros no corpo da mensagem informe a quantidade e mantenha como Texto, não é necessário alterar.](https://ajuda.sankhya.com.br/hc/article_attachments/42637485750039)

**Botões:**
Essa opção deve ser selecionada apenas para botões do tipo URL com parte do link variável.

**Não selecione** essa opção para botões de telefone, resposta rápida ou URL com link fixo, pois esses casos não utilizam variáveis, o conteúdo já cadastrado no 360 será enviado exatamente como registrado, sem necessidade de preenchimento no momento do envio.

A definição sobre o uso de variáveis é feita durante o cadastro no 360. Portanto, no momento da configuração na Neppo, basta replicar o que já foi definido anteriormente.

![Imagem 39: A definição sobre o uso de variáveis é feita durante o cadastro no 360. Portanto, no momento da configuração na Neppo,…](https://ajuda.sankhya.com.br/hc/article_attachments/42637485949207)

Selecionar a operação correspondente que compartilhará o template no quadrado esquerdo, clicando na seta indicando o lado direito.

![Imagem 40: Selecionar a operação correspondente que compartilhará o template no quadrado esquerdo, clicando na seta indicando o…](https://ajuda.sankhya.com.br/hc/article_attachments/42637486115735)

Para finalizar, basta clicar na opção de **Salvar** e, caso contrário, clique na opção **Cancelar**.

### Editar Cadastro de Template

Para editar um Template, basta clicar sobre o cadastrado que deseja mudar. Após isto outra tela será aberta,

![Imagem 41: Para editar um Template, basta clicar sobre o cadastrado que deseja mudar. Após isto outra tela será aberta,](https://ajuda.sankhya.com.br/hc/article_attachments/42637503187479)

Note que a tela da edição de Template é muito semelhante à tela de cadastro. Os campos de edição são os mesmos e estão todos aptos à mudança, caso seja necessário.

●Vá para a opção com os grupos cadastrados que, no caso, é o quadrado da esquerda

![Imagem 42: ●Vá para a opção com os grupos cadastrados que, no caso, é o quadrado da esquerda](https://ajuda.sankhya.com.br/hc/article_attachments/42637486424599)

Quando quiser mudar um agente específico do campo direito para o esquerdo, basta selecionar o(s) cliente(s) selecionado e clicar nesta seta com sentido para a direita.

![Imagem 43: Quando quiser mudar um agente específico do campo direito para o esquerdo, basta selecionar o(s) cliente(s) selecionado…](https://ajuda.sankhya.com.br/hc/article_attachments/42637486623383)

●Caso queira fazer a mudança de todos os grupos do campo direito para o esquerdo, basta clicar na dupla seta com sentido para a direita e todos os grupos estarão aptos para o recebimento do template

![Imagem 44: ●Caso queira fazer a mudança de todos os grupos do campo direito para o esquerdo, basta clicar na dupla seta com…](https://ajuda.sankhya.com.br/hc/article_attachments/42637486819863)

●Quando quiser mudar alguns dos grupos do quadro direito para o esquerdo, basta clicar na seta com sentido para a esquerda.

![Imagem 45: ●Quando quiser mudar alguns dos grupos do quadro direito para o esquerdo, basta clicar na seta com sentido para a…](https://ajuda.sankhya.com.br/hc/article_attachments/42637527019671)

●Se quiser passar todos os agentes do lado direito para o esquerdo de uma só vez, basta clicar na dupla seta com sentido para a esquerda e, assim, todos os agentes deixam de estar selecionados para recebimento do aviso.

![Imagem 46: ●Se quiser passar todos os agentes do lado direito para o esquerdo de uma só vez, basta clicar na dupla seta com…](https://ajuda.sankhya.com.br/hc/article_attachments/42637504114711)

●Para finalizar, basta clicar na opção de **Salvar** e, caso contrário, clique na opção **Cancelar**.
