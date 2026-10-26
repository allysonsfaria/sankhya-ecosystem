---
id: "42430296847511"
titulo: "Google Calendário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430296847511-Google-Calend%C3%A1rio"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:01:14Z"
rotulos: ["sync_hc", "neppo", "neppo_857998268", "sync_hash_252697cc2f00"]
---

# Google Calendário

- [Visão Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430296847511-Google-Calend%C3%A1rio#Visao-Geral)
- [Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430296847511-Google-Calend%C3%A1rio#Usabilidade)
- [Criar Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430296847511-Google-Calend%C3%A1rio#Criar-Eventos)
- [Buscar Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430296847511-Google-Calend%C3%A1rio#Buscar-Eventos)
- [Excluir Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430296847511-Google-Calend%C3%A1rio#Excluir-Eventos)

## Visão Geral

Este documento tem como finalidade orientar a utilização do componente Google Calendário para fins de criação de bot na funcionalidade Construtor de bot.

## Usabilidade

Para utilizar o componente Google Calendário é necessário primeiramente criar uma conexão via funcionalidade de integrações para permitir ao google o acesso a sua agenda. Siga os passos:

### 1. Acessando a interface de Integrações

1. No menu principal da plataforma, digite no campo de busca por “Integrações” e acesse a funcionalidade de **Integrações**.
2. A página exibirá todos os serviços integráveis com a plataforma.
3. Localize o card **Google** entre as opções disponíveis.

![Imagem 1: Localize o card Google entre as opções disponíveis.](https://ajuda.sankhya.com.br/hc/article_attachments/42639575954327)

### 2. Selecionando o card do Google

1. No card **Google**, clique no botão **Acessar**.
2. Você será direcionado para a tela de **Listagem de Conexões Google**.

![Imagem 2: Você será direcionado para a tela de Listagem de Conexões Google .](https://ajuda.sankhya.com.br/hc/article_attachments/42639590687895)

**3. Visualizando suas conexões com o Google**

Nesta página você verá todas as conexões já criadas, contendo:

- **Nome da conexão**
- **E-mail da conta vinculada**
- **Permissões concedidas (acessos)**
- **Data de criação**
- **Ações disponíveis** (Reconectar / Desconectar)

Esta é a central onde você gerencia todas as suas integrações com o Google.

**4. Criando uma nova conexão**

1. No canto superior direito da tela, clique no botão **+ Criar Conexão**.
2. Será aberto um **drawer** do lado direito da tela.

![Imagem 3: Será aberto um drawer do lado direito da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/42639561312919)

### 5. Preenchendo as informações da conexão

Dentro do drawer “Criar Conexão”:

1. No campo **Nome da conexão**, informe um nome que identifique facilmente a integração.
2. Após preencher, clique no botão **Iniciar com Google**, localizado no canto inferior direito.

### 6. Autorizando o acesso ao Google

Ao clicar em **Iniciar com Google**, será aberta a janela de autenticação do Google:

1. Selecione o **e-mail** da conta Google que será integrada.
2. O Google exibirá uma solicitação de permissões.
3. Você deve **permitir o acesso** para que a plataforma possa:

   - Gerenciar agendas,
   - Visualizar eventos,
   - Criar e editar compromissos no Google Calendar.

É obrigatório conceder estas permissões para que o componente de Calendário funcione corretamente.

Agora sua conta Google está vinculada e pronta para ser utilizada nos componentes de Google Calendário dentro dos fluxos e funcionalidades da plataforma. Para utilizar o componente:

## Criar Eventos

### 1. Selecionando a conexão e agenda

Ao inserir o componente “**Criar Evento**” no fluxo, será exibida uma interface semelhante à imagem abaixo:

![Imagem 4: Ao inserir o componente “ Criar Evento ” no fluxo, será exibida uma interface semelhante à imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639564243095)

### 1.1 Conexão

- No campo **Conexão**, selecione a conexão Google criada anteriormente.
- Todas as conexões válidas aparecerão no dropdown.
- Esta conexão define **em qual conta Google** o evento será criado.

### 1.2 Agenda

- Após selecionar a conexão, selecione a **Agenda** desejada.
- Na maioria dos casos, a agenda padrão será a **Agenda Principal** da conta Google.
- Se a conta possuir agendas adicionais, elas serão listadas.

### 2. Detalhamento do evento

Aqui você define todas as informações que irão compor o evento dentro do Google Calendar.

### 2.1 Nome do evento (obrigatório)

- É o título que será exibido no Google Agenda.
- Exemplo: Atendimento ao Cliente – Consulta, Reunião Semanal, Retorno do Suporte, etc.

### 2.2 Data de início (obrigatório)

- Define quando o evento começa.
- Formato aceito: **data + horário**
- Exemplo: 25/11/2025 14:00

### 2.3 Data de fim (obrigatório)

- Define quando o evento termina.
- Deve ser maior que a data de início.

### 2.4 Descrição do evento

- Campo para inserir um texto explicativo ou informações adicionais.
- Será exibido dentro da agenda do Google.

### 2.5 Localização

- Pode ser:

  - Endereço físico
  - Sala de reunião
  - Ou um **link de videoconferência**
- Caso utilize o Meet automaticamente, o link também pode ser exibido aqui.

### 3. Convidados

O componente permite adicionar participantes ao evento.

- Insira os **e-mails** das pessoas que devem ser convidadas.
- Cada convidado receberá (opcionalmente) um **e-mail de notificação** do Google informando sobre o evento.

### Enviar notificação

- Quando ativado, envia um e-mail automático do Google Calendar com o convite.
- Recomendado para garantir que o convidado seja informado.

### 4. Reunir com Google Meet

Ao ativar esta opção:

- A plataforma gera automaticamente um **link de reunião do Google Meet**.
- O link é anexado ao evento.
- Pode ser utilizado tanto pelo sistema quanto pelos convidados.

### 5. Variável de armazenamento

No final da configuração, é possível escolher uma variável para armazenar o retorno da ação.

### Variável de escopo global (opcional)

- Caso marcado, essa variável poderá ser usada em qualquer parte do fluxo.
- Se não marcado, estará disponível apenas no trecho local.

## Buscar Eventos

![Imagem 5: Buscar Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/42639564526103)

### 1. Selecionando a conexão e a agenda

Assim como na criação de eventos:

- No campo **Conexão**, selecione a conexão Google previamente criada.
- No campo **Agenda**, escolha a agenda onde os eventos estão registrados, normalmente, a **Agenda Principal**.

### 2. Parâmetros de busca

O componente permite filtrar eventos de forma flexível, utilizando:

#### Nome do evento

- Permite buscar eventos que contenham o texto informado no título.

#### Data de início

- Define o período a partir do qual deseja buscar eventos.

#### Data de fim

- Define até qual data os eventos devem ser buscados.

#### Quantidade máxima de eventos

- Limita quantos eventos serão retornados na busca.

### 3. Variável de armazenamento

No final da configuração, é possível escolher uma variável para armazenar o retorno da ação.

**Variável de escopo global (opcional)**
Caso marcado, essa variável poderá ser usada em qualquer parte do fluxo.
Se não marcado, estará disponível apenas no trecho local.

## Excluir Eventos

![Imagem 6: Excluir Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/42639581144855)

### 1 . Selecionando a conexão e a agenda

Assim como na criação e busca de eventos:

- No campo **Conexão**, selecione a conexão Google previamente criada.
- No campo **Agenda**, escolha a agenda onde os eventos estão registrados, normalmente, a **Agenda Principal**.

### 2 . Identificador do Evento

Informe uma variável ou informação que identifique o evento salvo a ser excluído.
