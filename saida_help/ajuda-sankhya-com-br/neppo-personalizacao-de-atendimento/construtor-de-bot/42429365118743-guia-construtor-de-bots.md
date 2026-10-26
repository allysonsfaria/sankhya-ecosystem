---
id: "42429365118743"
titulo: "Guia Construtor de Bots"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T15:46:37Z"
rotulos: ["sync_hc", "neppo", "neppo_101154818", "sync_hash_d879efd60a35"]
---

# Guia Construtor de Bots

Este manual detalha o **Construtor de Bots** da Neppo, uma ferramenta visual e modular projetada para criar e gerenciar fluxos de atendimento automatizado. O objetivo é capacitar o administrador a construir desde chatbots simples de resposta direta até árvores de decisão complexas com integrações a sistemas externos e inteligência artificial.

- [O QUE É O CONSTRUTOR DE BOTS](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#O-QUE-E-O-CONSTRUTOR-DE-BOTS)
  - [Criar novo chatbot em branco](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Criar-novo-chatbot-em-branco)
- [TEMPLATE PADRÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#TEMPLATE-PADRAO)
- [VARIÁVEIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#VARIAVEIS)
  - [Variáveis Globais da Sessão](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Variaveis-Globais-da-Sessao)
  - [Variável contact – Dados do Contato Atual](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Variavel-contact--Dados-do-Contato-Atual)
  - [Variável config – Gerenciamento de Credenciais (Neppo Vault)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Variavel-config--Gerenciamento-de-Credenciais-Neppo-Vault)
- [ORDEM DE EXECUÇÃO DOS FLUXOS](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#ORDEM-DE-EXECUCAO-DOS-FLUXOS)
- [TEXTO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#TEXTO)
- [ENTRADA DE DADOS](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#ENTRADA-DE-DADOS)
- [ANEXO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#ANEXO)
- [MENU DE OPÇÕES](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#MENU-DE-OPCOES)
  - [Menu Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Menu-Padrao)
  - [MENSAGEM INTERATIVA (WHATSAPP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#MENSAGEM-INTERATIVA-WHATSAPP)
  - [Menu em Botão](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Menu-em-Botao)
  - [Menu Lista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Menu-Lista)
- [REDIRECIONAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#REDIRECIONAR)
- [TIMEOUT](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#TIMEOUT)
- [EXPRESSÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#EXPRESSAO)
- [CONDIÇÕES](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#CONDICOES)
- [VALIDAÇÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#VALIDACAO)
- [EXECUTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#EXECUTAR)
- [SAIR](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#SAIR)
- [ITERAÇÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#ITERACAO)
- [COMPONENTE PERSONALIZADO](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#COMPONENTE-PERSONALIZADO)
- [REQUISIÇÕES REST](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#REQUISICOES-REST)
  - [Requisição CHAT API](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Requisicao-CHAT-API)
- [CONVERTER PARA JSON](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#CONVERTER-PARA-JSON)
- [COMPONENTE OpenAI](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#COMPONENTE-OpenAI)
  - [Visão Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Visao-Geral)
  - [Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Usabilidade)
    - [Transcrição de Voz](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Transcricao-de-Voz)
    - [Sintetização de Voz](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Sintetizacao-de-Voz)
    - [Configuração do Token](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429365118743-Guia-Construtor-de-Bots#Configuracao-do-Token)

## O QUE É O CONSTRUTOR DE BOTS

O Construtor de Bots é uma ferramenta avançada da Neppo, desenvolvida para facilitar a criação e gestão de fluxos de atendimento automatizado. Esta ferramenta intuitiva permite a construção de fluxos baseados em componentes modulares, onde cada fluxo segue uma sequência lógica de ações e respostas.

Com o Construtor de Bots, é possível:

**Criar Fluxos Simples:** Ideal para atendimentos diretos e de baixa complexidade, onde as interações seguem uma linha reta de perguntas e respostas.

**Desenvolver Fluxos Complexos:** Projetado para atender a necessidades mais sofisticadas, permitindo a criação de árvores de atendimento. Dependendo das escolhas do usuário, diferentes fluxos podem ser acionados, proporcionando uma experiência personalizada e dinâmica.

**Integrar com Outros Sistemas:** Para soluções mais robustas, a ferramenta oferece a possibilidade de integração com sistemas externos por meio de APIs REST, garantindo que os bots possam acessar e manipular dados de diversas fontes, melhorando a eficiência e a eficácia do atendimento.

### Criar novo chatbot em branco

Para criar um novo chatbot em branco, siga os passos abaixo:

1. **Selecionar a Opção Novo Chatbot**: Inicie o processo clicando na opção **"Novo Chatbot"**.
2. **Escolher o Template**: Selecione o template **"Em Branco"** para iniciar a construção do seu chatbot do zero.
3. **Preencher Informações**:

   - **Nome do Chatbot**: Insira um nome que identifique claramente o seu chatbot.
   - **Descrição**: Adicione uma breve descrição que resuma a finalidade e as funcionalidades do chatbot.
   - **Categoria (Opcional)**: Se desejar, atribua o chatbot a uma categoria específica para melhor organização.
4. **Cadastrar**: Após preencher todas as informações, clique em **"Cadastrar"** para finalizar a criação do seu novo chatbot.

Com esses passos, você terá um chatbot em branco pronto para ser configurado conforme suas necessidades.

![Imagem 1: Com esses passos, você terá um chatbot em branco pronto para ser configurado conforme suas necessidades.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdsmJ8VZfIMBiGoE18e4FLbo0_TPIYQVMah5AKBLPlaRAuI7ZskR8n9HjQ2lffZVjzXYZ8LyO5MJ99x1FDoT6uJgXJzggjUC-GCjbKJYUT1NBQcIgfN1NVj9Bk5aK8ZV1Ce_ce6mML8hgT1_3En9KVEf-SU?key=dl2TjX0aZ4RksGhHZJaPAw)

Após criar o chatbot, você verá a tela inicial, onde os componentes disponíveis são exibidos em círculos azul-escuro. Nesta interface, é possível visualizar os fluxos configurados, incluindo:

1. **Fluxo Principal**: Este fluxo serve como o ponto de partida inicial ao executar o bot. Nele, você pode definir as interações e ações que ocorrerão assim que o usuário iniciar a conversa.

![Imagem 2: Fluxo Principal : Este fluxo serve como o ponto de partida inicial ao executar o bot. Nele, você pode definir as…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdE5VVm7-JJSP6A_gDS81g54K28ogseSeyLtMco7pUm2B1SmWwddbto61KO4_LkFjwwHjq2y2t2GC8WLNwXfC92GGlmanWnpITTHcXmJKvGfCPw4yQUYLEut5kiixi2eXjpDOc7m0NhymZUTENch4ETEMsJ?key=dl2TjX0aZ4RksGhHZJaPAw)

2. **Fluxo "Erro"**: Este fluxo é projetado para gerenciar situações em que ocorra um erro global. No campo "Sequência", você pode selecionar um fluxo que será executado automaticamente caso um erro seja detectado, garantindo que o atendimento continue de forma eficiente e controlada.

![Imagem 3: Fluxo "Erro" : Este fluxo é projetado para gerenciar situações em que ocorra um erro global. No campo "Sequência", você…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXccFH0fI_6Y24tjJuGyI0xd5CCkgjkrVD6f0WTS8PyD42xtF_4fYWHzk8u6pF48AG4zUHgmX9NEX8Pnwx_DfmaGJfVASoAaoOzr10QKPUZl8f-Oi7EOhQJZH0-kgLF90Piwv62WWhrdOy2ZFMEfeslHbY9Q?key=dl2TjX0aZ4RksGhHZJaPAw)

Essa estrutura facilita a criação e o gerenciamento do chatbot, permitindo que você organize componentes e fluxos de maneira intuitiva.

## TEMPLATE PADRÃO

É recomendada a utilização do template padrão disponível na aba **Construtor de Bots**, em vez de criar um modelo em branco. O fluxo padrão pode ser mantido desativado e utilizado apenas como referência para clonagem, facilitando a criação de novas versões.

**Vantagens do Template Padrão:**

1. **Funcionalidades Configuradas**: O fluxo já vem com algumas funcionalidades pré-configuradas e regras padrão, como o direcionamento de respostas de disparos ativos para os atendentes que os realizaram ou para grupos específicos.
2. **Facilidade de Início**: Basta iniciar a construção do fluxo a partir do ponto **“Início do Bot”**, permitindo que você aproveite as configurações já existentes e otimize o processo de desenvolvimento.

Utilizar o template padrão não apenas economiza tempo, mas também garante que você siga as melhores práticas ao criar seu chatbot.

![Imagem 4: Utilizar o template padrão não apenas economiza tempo, mas também garante que você siga as melhores práticas ao criar…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeT1hQpFrkDVcYQz6FBYUinyFzbqg_6yKfdN5cQJwprugTt6SJ7Jcib6MMbP9GCiyrZdMMv2qVw8LjV98NjfIS7XMXQUJGvSQysS-eJjx6qdbJRJuKkMCDqnCW0zX8xRy7unBudXQb_uZ3sOn-qJHBP9vY?key=dl2TjX0aZ4RksGhHZJaPAw)![Imagem 5: Utilizar o template padrão não apenas economiza tempo, mas também garante que você siga as melhores práticas ao criar…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcNhbUINmoG5eOG0zs18dKpdg_ux6U3xBfulviLCtUk_W4R1CtTV29WN7jdXIY6Ld9-eCIWf7mf6IZffqjFEvgESm3oG2jGNI0nplfDzR1RP1Hs6Lkhw-d7FRmCJe4pUAjYlE8ub5ZQS-6CySlkVZ6TWFA?key=dl2TjX0aZ4RksGhHZJaPAw)

## VARIÁVEIS

No Construtor de Bots, as variáveis são utilizadas para armazenar valores primários, como números e strings. Estas variáveis são locais a cada fluxo, mas podem ser passadas para os fluxos seguintes como argumentos ou parâmetros, permitindo a continuidade e a personalização do atendimento.

Os valores das variáveis podem ser utilizados em qualquer parte do fluxo no formato `{{Variavel}}`, utilizando duas chaves para indicar a referência à variável. Isso facilita a inserção de dados dinâmicos, garantindo que as respostas e interações do bot sejam contextuais e personalizadas com base nas informações previamente coletadas.

Por exemplo, se uma variável `{{Nome}}` armazenar o nome do cliente, o bot pode utilizá-la para saudar o cliente pelo nome em diferentes pontos do atendimento, proporcionando uma experiência mais humanizada e eficiente.

### Variáveis Globais da Sessão

Além das variáveis locais, também estão disponíveis algumas variáveis globais com informações sobre a sessão atual. Estas podem ser acessadas diretamente em qualquer parte do fluxo, oferecendo dados importantes do contexto da conversa:

- `firstMessage.message`: conteúdo da primeira mensagem recebida na sessão.
- `firstMessage.group`: identificador do grupo de atendimento atual.
- `firstMessage.externalProtocol`: protocolo externo da conversa.
- `firstMessage.originUser`: origem do usuário que iniciou a conversa.
- `firstMessage.sessionId`: identificador único da sessão.

Essas variáveis permitem adaptar o fluxo com base no contexto inicial da conversa, como protocolos específicos ou canais de entrada.

### Variável `contact` – Dados do Contato Atual

Foi disponibilizada também a variável especial `contact`, que carrega os dados do contato atual conforme exibido na tela de **Clientes**. Essa variável está disponível em todo o fluxo do bot e permite o acesso direto a diversas informações do usuário.

Abaixo estão os atributos disponíveis em `contact`:

| Atributo | Tipo | Descrição |
| --- | --- | --- |
| `id` | int | Identificador do usuário na plataforma Neppo |
| `userName` | string | Nome do usuário na plataforma Neppo |
| `displayName` | string | Nome do usuário exibido no WhatsApp |
| `cpf` | string | CPF do usuário |
| `email` | string | E-mail do usuário |
| `birthDate` | date | Data de nascimento |
| `phone` | string | Número de telefone |
| `country` | string | Abreviação do país do usuário (ex.: `br`) |
| `active` | bool | Indica se o usuário está ativo na plataforma Neppo |
| `agent` | objeto | Objeto com os dados do agente associado ao contato |

Atributos do Objeto `agent`

| Atributo | Tipo | Descrição |
| --- | --- | --- |
| `id` | int | Identificador do agente na plataforma Neppo |
| `userName` | string | Nome do agente na plataforma Neppo |
| `displayName` | string | Nome do agente |
| `email` | string | E-mail do agente |
| `phone` | string | Número de telefone do agente |
| `active` | bool | Indica se o agente está ativo na plataforma Neppo |

**Exemplos de uso no fluxo do bot:**

```
{{contact.userName}} — para exibir o nome do usuário
{{contact.cpf}} — para acessar o CPF
{{contact.agent.userName}} — para obter o nome do agente responsável
```

### Variável `config` – Gerenciamento de Credenciais (Neppo Vault)

A variável `config` é utilizada para acessar credenciais armazenadas no **Neppo Vault**, uma funcionalidade que permite centralizar e proteger informações sensíveis como **tokens, chaves de API, URLs, logins e senhas**.

**Como configurar:**

1. Acesse a tela **Neppo Vault** no painel da plataforma.
2. Crie um novo diretório (por exemplo: `sankhya`).
3. Dentro do diretório, adicione credenciais com os nomes desejados (por exemplo: `token`).
4. Opcionalmente, você pode organizar as credenciais em subpastas para melhor estruturação e segurança.

**Como utilizar no bot:**

Para acessar uma credencial armazenada, utilize o seguinte formato:

```
{{config.<diretório>.<nome_da_credencial>}}
```

**Exemplo:** Se foi criado um diretório chamado `sankhya` e dentro dele uma credencial chamada `token`, o acesso via bot deve ser feito assim:

```
{{config.sankhya.token}}
```

Isso permite ao bot acessar dinamicamente informações sensíveis sem a necessidade de armazená-las diretamente nos fluxos, garantindo mais segurança, escalabilidade e facilidade na manutenção de dados de integração.

Benefícios do uso do `config`:

- **Segurança:** As credenciais ficam protegidas e acessíveis apenas em tempo de execução.
- **Organização:** Diretórios e subpastas permitem agrupar credenciais por sistema ou finalidade.
- **Facilidade de atualização:** Atualizações nas credenciais não exigem alteração dos fluxos do bot.
- **Controle centralizado:** Ideal para equipes técnicas que precisam gerenciar acessos de múltiplas integrações.

## ORDEM DE EXECUÇÃO DOS FLUXOS

 Os atendimentos se iniciam a partir do fluxo principal, onde podem ser incluídos os componentes disponíveis. Novos fluxos podem ser criados clicando no símbolo "+" na lateral esquerda. De acordo com determinadas ações dentro de cada fluxo, é possível direcionar para outros fluxos, permitindo uma navegação dinâmica e condicional.

Os fluxos podem ser reordenados para melhor organização visual, mas a ordem de apresentação não influencia a execução. Um fluxo só será executado se uma ação em outro fluxo direcionar para ele, garantindo que o atendimento siga uma lógica coerente baseada nas interações do usuário.

Além disso, os fluxos podem ser reaproveitados e chamados de vários pontos diferentes, aumentando a eficiência na construção do atendimento e permitindo a reutilização de processos comuns. Isso facilita a manutenção e a atualização dos fluxos, garantindo consistência e economia de tempo no desenvolvimento.

## TEXTO

O componente de texto é utilizado para exibir mensagens ao cliente, garantindo que informações importantes, instruções ou qualquer outro tipo de conteúdo textual sejam apresentados de forma clara e direta durante o atendimento. Além disso, o componente suporta o envio de arquivos nos formatos JSON, texto, documento, imagem, áudio e vídeo, sendo necessário selecionar o tipo de mensagem e fornecer a URL para o envio do arquivo.

![Imagem 6: O componente de texto é utilizado para exibir mensagens ao cliente, garantindo que informações importantes, instruções…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdk1MatOLyfjDuEpC5ajInDF-RhCuIpS2JcrnIlLPdvZpGa6SfbLuPrKBM_KWkiZzXMTr995XU0PgNYudSOgoiX1dDu3dum-a43VMCLJfFJY-XpLGPjsUuMK9dORS4ac63NKvlCKvJYTQzz42rhF-EA7gYP?key=dl2TjX0aZ4RksGhHZJaPAw)

## ENTRADA DE DADOS

Assim como o componente de envio de mensagem, o componente de entrada de dados exibe uma mensagem ou arquivo para o cliente e aguarda sua resposta. A resposta fornecida é armazenada na variável especificada, para uso posterior no fluxo de atendimento. É necessário selecionar o tipo de mensagem a ser exibida e, no campo "variável", identificar a variável que será utilizada para armazenar a resposta.

Além disso, é possível configurar a flag de inatividade para definir qual fluxo será executado caso o cliente não responda dentro de um período de tempo específico. Isso permite a execução automática de um fluxo alternativo ou a realização de outras ações pré-definidas, garantindo uma experiência de atendimento contínua e eficiente.

![Imagem 7: Além disso, é possível configurar a flag de inatividade para definir qual fluxo será executado caso o cliente não…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXea7t-cNW9L8F1BYHGiO4kqi5VLx46Mgwmaqqb12AZtHxeiRpfptR0ivHyg_Ek9ZqC4wOnfXl76_ZV1_YIo7op34U8mizWI7nOpZE4uJt6mfmZFHin_Rm-K_9yCAtIa28yOaLRGUZxmIGGxD5_nBQnTWOzh?key=dl2TjX0aZ4RksGhHZJaPAw)

## ANEXO

O componente de Anexo é utilizado para exibir diversos tipos de anexos, como documentos, imagens, fotos e áudios, com um limite de até 15 MB por arquivo anexado diretamente do diretório local do usuário. Além de exibir os anexos, é possível adicionar uma legenda para fornecer contexto ou informações adicionais sobre cada arquivo apresentado.

![Imagem 8: O componente de Anexo é utilizado para exibir diversos tipos de anexos, como documentos, imagens, fotos e áudios, com…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeyVjZMJEBiC-JWYlvzCQRK8WooRiusScVxguVdOhhrfFsK-zM24fYB4D3cZHPcrE5k5XOwwms8t514CKufX3TXt_NzpmkOsUEfPG9shWN71RXJvgc-QkGnzwg7d6RqwOFptzVevgIFySpHBKTLobIw-iM?key=dl2TjX0aZ4RksGhHZJaPAw)

## MENU DE OPÇÕES

O componente Menu de Opções é utilizado para oferecer menus interativos ao cliente durante o atendimento. Existem duas configurações principais, Mensagem padrão e Mensagem Interativa.

### Menu Padrão

O texto inserido no campo de mensagem será exibido ao cliente no canal de atendimento.

É necessário definir uma variável para armazenar o menu. Em seguida, são configuradas opções numéricas, onde cada número direciona para um fluxo específico.

A opção padrão serve para tratar respostas inválidas, ou seja, quando o cliente fornecer uma informação não reconhecida, o fluxo definido na opção padrão será executado. Além disso, é possível adicionar palavras semelhantes para cada opção. Por exemplo, "opção 1" poderá reconhecer termos como "um", "venda", entre outros.

Também é possível ativar a flag de inatividade, que define um fluxo a ser executado caso o cliente não responda dentro de um período de tempo determinado.

![Imagem 9: Também é possível ativar a flag de inatividade, que define um fluxo a ser executado caso o cliente não responda dentro…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdAMViBCfxri71vP3urm4AO8smgI9-dbStnEm9aDdLKNCAh8pPDIQ1Wm01XWVIEEjz9kZ2sfo3j3dc5hvvk1k2VInjYFqSTl47Ib7nU-qJXvB7zi3A-YVNAs2iUY-Fc1GzabULNfTjodA2JKzsG8oobhds?key=dl2TjX0aZ4RksGhHZJaPAw)

### MENSAGEM INTERATIVA (WHATSAPP)

Este componente funciona exclusivamente no canal de atendimento do WhatsApp, respeitando as limitações da plataforma oficial. Primeiro, é necessário selecionar o tipo de mensagem, que pode ser uma lista ou um botão.

### Menu em Botão

Este componente apresenta opções como botões interativos que o cliente pode selecionar diretamente. Cada menu pode conter até 3 opções, com no máximo 20 caracteres por opção.

Inicialmente, é possível ativar a flag de cabeçalho, que é opcional. Caso ativada, você pode incluir um texto no cabeçalho que será exibido ao cliente. No conteúdo, é obrigatório preencher um texto que será mostrado na mensagem principal. Além disso, é possível adicionar um rodapé, também opcional.

Para as ações, é possível configurar até 3 botões. Para cada botão, deve-se inserir um texto para a opção, selecionar o item do fluxo que será executado com base na resposta, e também é possível incluir argumentos ou parâmetros que serão passados como variáveis para o próximo fluxo.

Após preencher todas as opções, é necessário selecionar uma variável para armazenar o menu. A opção padrão será acionada em caso de respostas inválidas, executando um fluxo definido.

Também é possível ativar a flag de inatividade, que define um fluxo a ser executado caso o cliente não responda dentro de um período de tempo determinado.

![Imagem 10: Também é possível ativar a flag de inatividade, que define um fluxo a ser executado caso o cliente não responda dentro…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdwZ-2BTACtwUC_OvEQ7h2Z3WGdTxj3fUEX_89ALAuwFMa0YeaNBrkfwjRACeBAvpXRRcYy1k3xj_166BqMQ5XRVjhDGCLi9fTvsnWjWCEs_hMJDyH_AxnW6u--jbotVV3WOEJzfARfR56p_3ILWkwxpOEh?key=dl2TjX0aZ4RksGhHZJaPAw)

### Menu Lista

 Este componente apresenta opções como lista interativa, que o cliente pode selecionar diretamente. Cada menu pode conter até 10 opções, com no máximo 20 caracteres por opção.

Inicialmente, é possível ativar a flag de cabeçalho, que é opcional. Se ativada, você pode incluir um texto no cabeçalho que será exibido ao cliente. No campo de conteúdo, é obrigatório preencher um texto que será a mensagem principal da lista. Também é possível adicionar um rodapé, que é opcional.

Na aba de ações, deve-se configurar um único botão, preenchendo o conteúdo do botão, por exemplo, com "Clique aqui". Ao clicar, será exibida a lista, que pode ser dividida em sessões. Pelo menos uma sessão é obrigatória, e para cada sessão é necessário preencher o título no campo "Título da sessão".

Para as ações, é possível configurar até 10 opções na lista. Para cada opção, deve-se inserir o texto da opção, selecionar o fluxo que será executado com base na resposta do cliente, e, se necessário, incluir argumentos ou parâmetros que serão passados como variáveis para o próximo fluxo.

Após configurar todas as opções, é necessário selecionar uma variável para armazenar o menu. A opção padrão será acionada em caso de respostas inválidas, executando um fluxo definido.

Além disso, é possível ativar a flag de inatividade, que define um fluxo a ser executado caso o cliente não responda dentro de um período de tempo determinado.

![Imagem 11: Além disso, é possível ativar a flag de inatividade, que define um fluxo a ser executado caso o cliente não responda…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd4gDD8A43hNPXbAaFe1pitwe00sZp6ml2TF967KFoXQ8HUEdvjWKSoWhFLwapTzwh8-fiXjAh7kzpP4cBJ_1Ck4pEQrG5kw4Ogn2qjFfpltGviyGN2hFdXTxURtycf0PcJvwCJ1fLp1H2Wp3Gh8TphNIk6?key=dl2TjX0aZ4RksGhHZJaPAw)

## REDIRECIONAR

O componente "Redirecionar" é utilizado para encaminhar o fluxo de atendimento para diferentes destinos, como grupos de atendimento especificados por nome, transferência para um agente específico (onde é necessário informar o usuário do agente), transferência para outro fluxo de atendimento, direcionamento para uma pesquisa de satisfação ou inserção na fila de espera.

![Imagem 12: O componente "Redirecionar" é utilizado para encaminhar o fluxo de atendimento para diferentes destinos, como grupos de…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfWoUdcT6dnavenpqRqt63uvRJYczE225aVCNxBd7ndJoK22CCNPyyg9n0phh5XxpS4Q0DcS0aCIBJY7Taa8txDCo66a-PtwbkBCgU_hwb0Q2piIRZpLgkN3y1a1skxR_6HRuayJv35-kZkFvyRMS7kt7Au?key=dl2TjX0aZ4RksGhHZJaPAw)![Imagem 13: O componente "Redirecionar" é utilizado para encaminhar o fluxo de atendimento para diferentes destinos, como grupos de…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdl_AHqop3SziDZ6gtPFRw_M8wB8xbfJszNxXlk3tswVNuowuyMzAlVMj4j6hyMCZt2I3TeNSL6qWYRQ9L3Yli57j_Ng0Yg2YNgfFJX2V4xmvcscHP8SWVPriEXlC94VUSBHqM7Lub2146bXzx7xlmQmOc?key=dl2TjX0aZ4RksGhHZJaPAw)

## TIMEOUT

O componente "Timeout" é configurado para aguardar um determinado período de tempo antes de executar o próximo componente no fluxo de atendimento. Isso permite definir intervalos de espera para garantir que determinadas ações ocorram dentro de prazos específicos. Deve ser preenchido o campo variável para armazenar o timer.

![Imagem 14: O componente "Timeout" é configurado para aguardar um determinado período de tempo antes de executar o próximo…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZLMTlCMPrnT4WQ0vT_bXLZoZScE7q54FJudcNF0rPLtRkycnvQ4ql0Z1U5orwoUBTApDS7gWCCH0BiDfq6GZyx-t5yAh0f6J-x5fNwAhOqnbO1qxSz4F-Tiu1DPnwaGsv-4kvoET68N1kLr0MouLS2z5n?key=dl2TjX0aZ4RksGhHZJaPAw)

## EXPRESSÃO

O componente "Expressão" permite a execução de expressões condicionais dentro do fluxo de atendimento. Você pode definir uma expressão para verificar condições específicas e, com base no resultado, realizar ações correspondentes. Por exemplo:

**Expressão:**
**“**{{Setor}}” == "Vendas"

Nesse caso, uma ação será selecionada para quando a expressão for verdadeira, e outra para quando for falsa, direcionando o fluxo de atendimento de acordo. Também é possível carregar variáveis como argumentos para uso em outras partes do fluxo.

Além disso, o componente oferece a funcionalidade de "Avaliar Expressão", onde expressões JavaScript podem ser utilizadas, permitindo operações avançadas, como concatenações, cálculos e manipulação de dados, cujo resultado é atribuído a uma variável. Exemplo:

**Expressão JavaScript:**
New Date().toDateString().split(" ")[0]

**Variável:**
Esse resultado pode ser armazenado em uma variável, como "Dia", para ser utilizado em componentes posteriores no fluxo.

![Imagem 15: Variável: Esse resultado pode ser armazenado em uma variável, como "Dia", para ser utilizado em componentes posteriores…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdCCYKidSHeuhNd8I9dnJo9Zur3BFC4cy5SEFYkmi0xWUJVUAyQxw1M84F8eFJCPLigmLNqSL-nmxSfO34LcSS3WrMcAkF50QnueqCaK3eECeLFhhDYdRYhxqExeEV_B_lVcHPHVHe3_p095s_IsumLxIVk?key=dl2TjX0aZ4RksGhHZJaPAw)![Imagem 16: Variável: Esse resultado pode ser armazenado em uma variável, como "Dia", para ser utilizado em componentes posteriores…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUF6EJFY_-c6gJ7HIa8t-IKwzw9IOh2KSW3tRafJSKzXYTWUHoKrzRFsuwm99r2k2e2hDmBnidixJswmtG9r2Y3xlCZtTu4BrKuWx9ikDFdPI9PhSdpINdG4ijJ0GWVlDuwvniOtfo7wV13e6Ddzoz5y-F?key=dl2TjX0aZ4RksGhHZJaPAw)

## CONDIÇÕES

O componente "Condições" permite a criação de múltiplas condições. No campo "Se", deve ser informada uma variável como entrada. No campo "Condição", você seleciona o tipo de operação, como "igual", "maior", "contém", entre outras, que será comparada com os dados inseridos no campo "Valores", verificando se a variável atende a uma condição específica. Também é possível adicionar a opção "e" para combinar mais de uma condição.

Se a variável atender à condição, o fluxo será direcionado para o caminho informado na opção "Ir para", e é possível passar valores como parâmetros para o próximo fluxo. Caso nenhuma condição seja atendida, a opção padrão pode ser configurada para redirecionar o fluxo para uma ação específica.

Além disso, há a possibilidade de ativar a flag de inatividade, definindo um fluxo a ser executado caso o cliente não responda dentro de um período de tempo determinado.

![Imagem 17: Além disso, há a possibilidade de ativar a flag de inatividade, definindo um fluxo a ser executado caso o cliente não…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdbKdzTo-8qaV16ru_PPKxZ9z9qyT6Gek9jdbl359TI_QyBpdmQV3HoO220V6-D2piwnTpv7fdcp2n5678KXmrDcOSajFS30ddNyz92X8UHJodE3GElNMw_Re6H-sn3SE2Xy8536x3kxHeG8sumuPJSP2MS?key=dl2TjX0aZ4RksGhHZJaPAw)

## VALIDAÇÃO

 O componente "Validação" é utilizado para verificar a precisão dos dados inseridos, como CPF, CNPJ, números, entre outros formatos, garantindo que as informações fornecidas pelos clientes estejam corretas antes de prosseguir com o atendimento ou executar outras ações.

No campo "Texto", deve ser informada a variável que contém os dados a serem validados, por exemplo, {{CPF}}. Em seguida, no campo "Tipo de validação", você escolhe o tipo de dado que deseja validar, como "Validar CPF".

Os campos "Quando for válido" e "Quando não for válido" devem ser preenchidos com os fluxos que serão executados caso a validação seja bem-sucedida ou falhe, respectivamente.

![Imagem 18: Os campos "Quando for válido" e "Quando não for válido" devem ser preenchidos com os fluxos que serão executados caso a…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeLM0uKdhn1awnO1dYnWnWjQIMEN69QsxCMoSFA7BVz-Rw8wYOt8elD2rsJVUm4TZ9_8SxiGtDiA4jIafBRLntSVTUg8zBNahXDPC-u9DBDyLyWI-Nit2_TWlmxgPwWW0eiMQWsnI8xgD8JAV8Mp9NxvgI?key=dl2TjX0aZ4RksGhHZJaPAw)

## EXECUTAR

O componente "Executar" recebe um campo "Sequência", onde deve ser informado o fluxo que será executado em um momento específico. O campo "Argumento" serve para passar valores como parâmetros para o fluxo em questão.

Esse componente é especialmente útil em situações onde nenhuma ação foi selecionada anteriormente no fluxo, permitindo a continuidade do atendimento ou a execução de processos adicionais conforme necessário.

![Imagem 19: Esse componente é especialmente útil em situações onde nenhuma ação foi selecionada anteriormente no fluxo, permitindo…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcKjpUYWwE0Lg0kitv33IVHKfUtUYOB_ekwBDFRa2AQAIp6_XpQ1EgnBtXya41Z4UDcMyYeN_hmoVViJ9tysrEHnxSFAilgKJ7a6Z8yVLvNSvt6nuPs-Ddv76mEAm1qNZhlqdl7uKkIOum8EKBwGScZTe4?key=dl2TjX0aZ4RksGhHZJaPAw)

## SAIR

O componente "Sair" encerra o atendimento a sessão atual de forma definitiva.

![Imagem 20: O componente "Sair" encerra o atendimento a sessão atual de forma definitiva.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc2TiDpauDcoGLriGX_hAjPME7neReXlC-fsWWHHpCPi1N13FzRqW1stadPuKD9D8kAJhvxsLJb588pUYnVOKfHi5APWXfBRYhBSWjgeHYZDLDPcqu9g6HemggtPDCG8groRPchVSpc4UG1kt2puILYlZaB?key=dl2TjX0aZ4RksGhHZJaPAw)

## ITERAÇÃO

O componente "Iteração" recebe um array como entrada e executa um fluxo de atendimento repetidamente com base no número de elementos presentes no array. Este componente é útil para lidar com listas de dados dinâmicas, permitindo realizar ações específicas para cada item contido no array.

No campo "Iteração sobre", deve-se passar a variável que contém o array. Neste caso, não utilize chaves duplas; por exemplo, em vez de {{retornoApi.produtos}}, utilize apenas retornoApi.produtos.

É necessário preencher o campo "Variável de cada item", que pode ser nomeado como "elemento\_lista". Em seguida, na opção de "Fluxo", selecione o fluxo que será executado em cada iteração.

Além disso, deve-se preencher o campo "Variável" com o nome da variável que armazenará o componente (embora essa variável não seja utilizada diretamente). Você também pode adicionar argumentos para serem utilizados dentro do fluxo do loop.

Dentro do fluxo que será executado em loop, você poderá acessar as variáveis do array no formato {{elemento\_lista.nomeProduto}}. Isso permite manipular os dados de cada item conforme necessário durante a execução do fluxo.

![Imagem 21: Dentro do fluxo que será executado em loop, você poderá acessar as variáveis do array no formato…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf5bbdu12CyxBR-U62RSXVwSHY61m2rsY4Xs_0qVn3T2uwNx3eWhvYELM4sGaW6XFco_djGFVH7EQ7LWhqkD4nLYlJsmPULZirPAfuHjJV4p7VDs48OOW4PbI7Fu_TZa4KbMFp1bF6P3cQqzlLjNShLbUxT?key=dl2TjX0aZ4RksGhHZJaPAw)

## COMPONENTE PERSONALIZADO

Ainda não disponível. O componente "Personalizado" permitirá a integração de funcionalidades específicas ou personalizadas dentro do fluxo de atendimento. Sendo possível desenvolver lógicas de negócio complexas ou integrar com sistemas externos de acordo com requisitos específicos.

## REQUISIÇÕES REST

O componente "Requisição REST" permite executar chamadas a APIs REST externas. Para configurá-lo, siga os passos abaixo:

**Tipo de Requisição**: Selecione o tipo de requisição que deseja realizar (GET, POST, etc.).

**Endpoint**: No campo "URL", insira o endpoint da requisição.

**Corpo da Requisição (Body)**: Para o corpo da requisição, você pode utilizar um JSON simples, por exemplo:

{

  "nome": "João",

  "idade": 30

}

**Cabeçalhos (Headers)**: Caso haja cabeçalhos a serem incluídos, preencha o campo "Chave" e "Valor". Um exemplo de cabeçalho seria:

- Chave: Authorization
- Valor: Bearer {{token}}

**Armazenamento da Resposta**: Atribua uma variável para armazenar a resposta da API, permitindo que você utilize esses dados em etapas posteriores do fluxo.

Além disso, é possível ativar a flag de inatividade para que, caso a requisição não seja executada dentro de um período de tempo determinado, um fluxo alternativo possa ser acionado.

![Imagem 22: Além disso, é possível ativar a flag de inatividade para que, caso a requisição não seja executada dentro de um período…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdJXJev-uOLmkV2bqkzx5w2fXGg3LbhZjYz8Gu_1VIW-29ew9tOEbWu_5MWlAvoMaQWPQCGUyymcqP4_HozWT-BtmQUeROa67xEseu_sZU2aFCnAu2x4sJIM7XIUpYM2CgudFKL_bCle6jKl5z6nEIz4kqO?key=dl2TjX0aZ4RksGhHZJaPAw)

### Requisição CHAT API

O componente "Requisição CHAT API" permite interações diretas com a API da Neppo, facilitando consultas a diversas entidades da plataforma, como usuários, agentes, contatos, horários de atendimento e grupos. Este componente é semelhante ao de requisições REST, mas otimiza o processo ao receber diretamente as credenciais de autenticação na API, eliminando a necessidade de chamadas individuais para autenticação.

**Configuração do Componente:**

**Campo URL de Autenticação**: Preencha com a URL de autenticação da API da Neppo.

**Credenciais**:

- **Usuário**: Insira seu nome de usuário para autenticação.
- **Senha**: Forneça a senha correspondente.
- **Authorization**: Inclua qualquer cabeçalho de autorização necessário.

Novos acessos à API podem ser criados na tela **Integrações**, na opção **Neppo Token API**.

**Dados da API**:

- **Tipo de Requisição**: Selecione o tipo de requisição que deseja realizar (GET, POST, etc.).
- **Endpoint**: No campo "URL", insira o endpoint da requisição.

**Corpo da Requisição (Body)**: Para o corpo da requisição, você pode utilizar um JSON simples. Por exemplo:

{

  "nome": "João",

  "idade": 30

}

Ao configurar o componente dessa forma, você facilitará a comunicação com a API da Neppo, tornando as interações mais rápidas e eficientes.

![Imagem 23: Ao configurar o componente dessa forma, você facilitará a comunicação com a API da Neppo, tornando as interações mais…](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAQlTf_O0mpq2lLX9YX_F4XU9QZ4m-giO3NNaVs7-CZ69gGz-0Z0Tx9_BwFHeLSGh5v1FxaAmZknqi2IWkPVrC39Z2WCXjZNO-dEIkIp-w0ga5nqm5w5E703dIWYu3KnaSMHARyGbvmi6yAbsdryPx1t-3?key=dl2TjX0aZ4RksGhHZJaPAw)

## CONVERTER PARA JSON

O componente "Converter para JSON" realiza a conversão de uma string JSON retornada por uma API externa em um objeto JavaScript. Essa conversão facilita o processamento e a manipulação de dados estruturados dentro do fluxo de atendimento automatizado.

**Configuração do Componente:**

**Campo Texto**: Neste campo, deve-se passar o corpo da resposta da API. Por exemplo, se a variável que armazenou a resposta de uma Requisição REST ou Requisição CHAT API for chamada BuscarUsuarios, você pode preencher o campo texto com:

{{BuscarUsuarios.body}}

**Campo Variável**: Preencha com o nome da variável que irá receber o objeto JSON convertido. Por exemplo:

BuscarUsuarios\_obj

Após a conversão, em fluxos posteriores, você poderá acessar os valores do objeto utilizando a nova variável. Por exemplo:

{{BuscarUsuarios\_obj.nome}}

Essa abordagem permite manipular os dados de forma mais eficiente, otimizando o fluxo de atendimento automatizado.

![Imagem 24: Essa abordagem permite manipular os dados de forma mais eficiente, otimizando o fluxo de atendimento automatizado.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcDP9vtvnsCqpvoC1nxf2KySPlmCE4P11L545GpoMO1i9TI60-KLZf8Bu4v6cQniPG05jWnSoC0gDmO3U3EL1baz9oGZ_Q4AgkAJKA9R9T2-M81Dx6V_CL12HhIOfaTzIpN9ifIVmJw23cFHMdYzY1rdkw?key=dl2TjX0aZ4RksGhHZJaPAw)

## COMPONENTE OpenAI

### Visão Geral

Este documento descreve o componente da OpenAI do Construtor de Bot, oferecendo uma solução avançada para criação de fluxos inteligentes e interações naturais com usuários. O componente permite personalizar completamente o comportamento da IA por meio de parâmetros configuráveis, garantindo respostas dinâmicas e contextualizadas dentro dos fluxos do bot.

Para utilizar o Componente da Openai deverá ser informado na funcionalidade NEPPO Vault as informações do Token através do caminho "openai/token”

### Usabilidade

**Geração de Respostas**

![Imagem 25: Geração de Respostas](https://ajuda.sankhya.com.br/hc/article_attachments/42637142410007)![Imagem 26: Geração de Respostas](https://ajuda.sankhya.com.br/hc/article_attachments/42637158713239)

A aba de geração de respostas permitirá ao usuário definir o modelo de IA a ser utilizado, instruir comportamento da IA através do prompt, definir quantas mensagens anteriores do chat serão consideradas como contexto da resposta, limitar a quantidade de tokens gerados para controle de custo, controlar a criatividade da IA(mais objetivo, mais simpatico…) e definir o nome da variável para utilização dentro do fluxo. Além disso, poderão ser criadas funções específicas para interações definindo o identificador, descrição e os parâmetros da função para retorno.

Retorno da variável:

```
{
    "status": 200,
    "body": {
            "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
            "object": "text_completion",
            "created": 1589478378,
            "model": "gpt-3.5-turbo-instruct",
            "service_tier": "default",
            "system_fingerprint": "fp_101a39fff3",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "text",
                        "tool_calls": [],
                        "refusal": null,
                        "annotations": []
                    },
                    "logprobs": null,
                    "finish_reason": "tool_calls"
                }
            ],
            "usage": {
                "prompt_tokens": 48,
                "completion_tokens": 11,
                "total_tokens": 59,
                "prompt_tokens_details": {
                    "cached_tokens": 0,
                    "audio_tokens": 0
                },
                "completion_tokens_details": {
                    "reasoning_tokens": 0,
                    "audio_tokens": 0,
                    "accepted_prediction_tokens": 0,
                    "rejected_prediction_tokens": 0
                }
            }
        }
}
```

Em caso de dúvidas consulte a documentação da OpenAI. <https://platform.openai.com/docs/api-reference/chat/create>

**Embeddings**

![Imagem 27: Embeddings](https://ajuda.sankhya.com.br/hc/article_attachments/42637119102359)

A aba de embeddings permitirá ao usuário definir o modelo de embeddings e os textos de entrada, tanto por meio de input manual quanto de variável e definir o nome da variável para utilização dentro do fluxo

Retorno da variável:

```
{
   "status": 200,
   "body": {
        "object": "list",
        "data": [
            {
                "object": "embedding",
                "embedding": [
                    0.0023064255,
                    -0.009327292,
                    .... (1536 floats total for ada-002)
                    -0.0028842222,
                ],
                "index": 0
            }
        ],
        "model": "text-embedding-ada-002",
        "usage": {
            "prompt_tokens": 8,
            "total_tokens": 8
        }
    }
}
```

Em caso de dúvidas consulte a documentação da OpenAI: <https://platform.openai.com/docs/api-reference/embeddings>

#### Transcrição de Voz

![Imagem 28: Transcrição de Voz](https://ajuda.sankhya.com.br/hc/article_attachments/42637159251991)

A aba de transcrição de voz permitirá ao usuário definir o modelo de IA, informar a variável de voz onde se encontra o áudio para realizar a transcrição para texto e definir o nome da variável para utilização dentro do fluxo.

Retorno da variável:

```
{
  "status": 200,
  "body": {
   "text": "Texto da transcrição",
  }
}
```

Em caso de dúvidas consulte a documentação da OpenAI: <https://platform.openai.com/docs/guides/speech-to-text?lang=curl#transcriptions>

#### Sintetização de Voz

![Imagem 29: Sintetização de Voz](https://ajuda.sankhya.com.br/hc/article_attachments/42637173134103)

A aba de sintetização de voz permitirá ao usuário definir o modelo de IA, informar a variável de texto, selecionar o modelo de voz desejado (permite demonstração) e definir o nome da variável para utilização dentro do fluxo.

Retorno da variável:

```
{
  "status": 200,
   "body": {
  "url": "https://seu_audio.wav",
  "error": ""
  }
}
```

Em caso de dúvidas consulte a documentação da OpenAI: <https://platform.openai.com/docs/api-reference/audio>

#### Configuração do Token

Para utilizar o componente da Openai, o usuário deverá realizar o cadastro do token na funcionalidade do Neppo Vault. Para isso, basta acessar a funcionalidade, expandir o diretório da Openai e clicar em “Editar Item”.

![Imagem 30: Para utilizar o componente da Openai, o usuário deverá realizar o cadastro do token na funcionalidade do Neppo Vault.…](https://ajuda.sankhya.com.br/hc/article_attachments/42637131143319)

Ao clicar em “Editar Item” , exibirá uma interface para informar os dados do token no campo “Valor”. Após informar os dados e clicar no botão “Salvar”, caso os dados sejam válidos, o componente da Openai já poderá ser utilizado.

![Imagem 31: Ao clicar em “Editar Item” , exibirá uma interface para informar os dados do token no campo “Valor”. Após informar os…](https://ajuda.sankhya.com.br/hc/article_attachments/42637159878679)
