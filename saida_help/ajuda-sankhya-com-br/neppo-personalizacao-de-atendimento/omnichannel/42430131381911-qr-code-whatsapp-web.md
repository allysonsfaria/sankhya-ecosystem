---
id: "42430131381911"
titulo: "QR Code - WhatsApp Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T16:58:53Z"
rotulos: ["sync_hc", "neppo", "neppo_413270023", "sync_hash_5939e2db9bf0"]
---

# QR Code - WhatsApp Web

A funcionalidade **WhatsApp Web** está disponível no **painel lateral direito do atendimento**, dentro do conjunto de ações relacionadas ao cliente e à sessão de atendimento.

Ela fica acessível mesmo quando **nenhum cliente está selecionado**, indicando que a conexão do WhatsApp é uma **ação do agente**, não do atendimento em si.

[GIF animado: Imagem 1: Ela fica acessível mesmo quando nenhum cliente está selecionado , indicando que a conexão do WhatsApp é uma ação do…](https://ajuda.sankhya.com.br/hc/article_attachments/42639482261271)

Esta é uma solução não oficial do WhatsApp.

- [Tela inicial — Nenhum cliente selecionado](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Tela-inicial--Nenhum-cliente-selecionado)
- [Tela de boas-vindas do WhatsApp Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Tela-de-boas-vindas-do-WhatsApp-Web)
- [Tela de consentimento informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Tela-de-consentimento-informado)
- [Tela de configuração da conexão](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Tela-de-configuracao-da-conexao)
- [Tela do QR Code](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Tela-do-QR-Code)
- [Tela de seleção de contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Tela-de-selecao-de-contatos)
- [WhatsApp Web conectado (estado ativo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#WhatsApp-Web-conectado-estado-ativo)
- [Menu do WhatsApp Web (⋮)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Menu-do-WhatsApp-Web-)
- [Estados possíveis do WhatsApp Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430131381911-QR-Code-WhatsApp-Web#Estados-possiveis-do-WhatsApp-Web)

---

## Tela inicial — Nenhum cliente selecionado

![Imagem 2: Tela inicial — Nenhum cliente selecionado](https://ajuda.sankhya.com.br/hc/article_attachments/42639493633175)

### O que você está vendo

Uma mensagem central informando:

> **Nenhum cliente selecionado**
> Escolha um atendimento ou realize ações abaixo

No painel lateral, você vê algumas ações disponíveis, mesmo sem um cliente aberto:

- Abrir ticket
- **WhatsApp Web — Desconectado**
- Frase Padrão
- Novo Cliente

### O que isso significa

Você ainda não iniciou um atendimento.
A Neppo permite que algumas ações sejam feitas **antes** de escolher um cliente — uma delas é conectar o WhatsApp Web.

### O que fazer agora

Para conectar seu WhatsApp:

- Clique em **WhatsApp Web (Desconectado)**

---

## Tela de boas-vindas do WhatsApp Web

![Imagem 3: Tela de boas-vindas do WhatsApp Web](https://ajuda.sankhya.com.br/hc/article_attachments/42639466425751)

### O que você está vendo

Uma tela introdutória com:

- Título: **WhatsApp Web**
- Texto: Conecte o WhatsApp ao Neppo
- Mensagem explicativa dizendo que a conexão ajuda a simplificar sua operação
- Dois botões:

  - **Cancelar**
  - **Avançar**

### O que isso significa

Esta é uma tela de orientação.
Ela explica **o que você está prestes a fazer**, antes de qualquer ação definitiva.

Nada foi conectado ainda.

### O que fazer agora

- Se quiser continuar, clique em **Avançar**
- Se não quiser seguir agora, clique em **Cancelar**

---

## Tela de consentimento informado

![Imagem 4: Tela de consentimento informado](https://ajuda.sankhya.com.br/hc/article_attachments/42639482880279)

### O que você está vendo

Um texto explicando que, ao usar o WhatsApp Web na Neppo:

- Seus contatos e mensagens serão utilizados para o atendimento
- Os dados serão processados dentro da plataforma
- Você pode revogar esse consentimento a qualquer momento

Ao final, há uma opção de aceite (checkbox).

### O que isso significa

Antes de conectar o WhatsApp, a Neppo precisa da sua **confirmação explícita**.
Nada acontece automaticamente.

Sem esse aceite, a conexão não pode continuar.

### O que fazer agora

- Leia o conteúdo
- Marque a opção de aceite
- Clique em **Avançar**

---

## Tela de configuração da conexão

![Imagem 5: Tela de configuração da conexão](https://ajuda.sankhya.com.br/hc/article_attachments/42639494221079)

### O que você está vendo

#### Campo: Telefone

- Um seletor de país
- Um campo para informar o número do WhatsApp que será conectado

#### Campo: Grupo de Atendimento

- Um seletor onde você escolhe em qual grupo esse WhatsApp será utilizado

É recomendado que o grupo individual do agente esteja criado

### O que acontece ao selecionar o grupo

Quando o agente seleciona um **Grupo de Atendimento** durante a conexão do WhatsApp:

- O grupo selecionado recebe **automaticamente a flag de Canal Multitenant**
- Essa flag identifica que o grupo está vinculado a um **WhatsApp conectado via infraestrutura multitenant**

![Imagem 6: Essa flag identifica que o grupo está vinculado a um WhatsApp conectado via infraestrutura multitenant](https://ajuda.sankhya.com.br/hc/article_attachments/42639494403863)

- Nenhuma ação manual adicional é necessária por parte do agente ou administrador

Esse vínculo garante que:

- As mensagens sejam corretamente roteadas pelo gateway multitenant
- O grupo esteja preparado para operar dentro das regras de isolamento e escalabilidade do multitenant

### Comportamento em caso de desconexão do WhatsApp

Se o usuário **desconectar o WhatsApp** posteriormente:

- A flag de **Canal Multitenant é removida automaticamente do grupo**
- O grupo retorna ao estado padrão, sem vínculo ativo com o multitenant
- Não há risco de o grupo permanecer marcado de forma incorreta

Na parte inferior:

- **Cancelar**
- **Gerar QR Code**

### O que isso significa

Aqui você está dizendo à Neppo:

- Qual número do WhatsApp será conectado
- Onde esse WhatsApp será usado dentro da plataforma

Essas informações organizam seu atendimento desde o início.

### O que fazer agora

- Confira o número de telefone
- Escolha o grupo de atendimento
- Clique em **Gerar QR Code**

---

## Tela do QR Code

![Imagem 7: Tela do QR Code](https://ajuda.sankhya.com.br/hc/article_attachments/42639514491799)

### O que você está vendo

- Um QR Code centralizado
- A instrução:

  Aponte seu celular para esta tela para escanear o QR code
- Botões:

  - Cancelar
  - Gerar QR Code

### O que isso significa

Este QR Code é o que conecta seu WhatsApp à Neppo.

Nada acontece sozinho:
a conexão só ocorre quando você escanear o código com seu celular.

### O que fazer agora

1. Abra o WhatsApp no seu celular
2. Vá em **Dispositivos conectados**
3. Escaneie o QR Code exibido na tela

---

## Tela de seleção de contatos

![Imagem 8: Tela de seleção de contatos](https://ajuda.sankhya.com.br/hc/article_attachments/42639483557911)

### O que você está vendo

- Um campo de busca:

  Pesquise ou selecione os contatos
- Uma lista de contatos do seu WhatsApp
- Cada contato tem uma caixa de seleção
- Botões:

  - Cancelar
  - Sincronizar

### O que isso significa

Você escolhe **quais contatos** ficarão disponíveis na Neppo.

Nem todos precisam ser sincronizados.
Você tem controle total sobre isso.

### O que fazer agora

- Marque os contatos que deseja usar. Você pode voltar a selecionar posteriormente
- Clique em **Sincronizar**

---

## WhatsApp Web conectado (estado ativo)

![Imagem 9: WhatsApp Web conectado (estado ativo)](https://ajuda.sankhya.com.br/hc/article_attachments/42639497254935)

### O que você está vendo

- A opção **WhatsApp Web** agora aparece com o status:
  **Ativo**
- Um indicador visual verde
- Um menu de opções (⋮)

### O que isso significa

Seu WhatsApp está conectado e pronto para uso.

A partir daqui:

- Mensagens podem ser enviadas e recebidas
- Atendimentos podem ser iniciados normalmente

---

## Menu do WhatsApp Web (⋮)

![Imagem 10: Menu do WhatsApp Web (⋮)](https://ajuda.sankhya.com.br/hc/article_attachments/42639467680535)

Ao clicar no menu, você verá duas opções.

---

### Selecionar contatos

**O que faz**
Permite revisar ou alterar os contatos sincronizados.

**Quando usar**
Quando quiser incluir ou remover contatos da lista.

---

### Desconectar

**O que faz**
Encerra a conexão do WhatsApp com a Neppo.

**Quando usar**

- Fim do expediente
- Troca de computador
- Quando não quiser mais usar o WhatsApp Web

---

## Estados possíveis do WhatsApp Web

- **Desconectado**
  Ainda não há conexão ativa

![Imagem 11: Desconectado Ainda não há conexão ativa](https://ajuda.sankhya.com.br/hc/article_attachments/42639484042263)

- **Autenticação**
  O sistema está aguardando a confirmação da conexão

![Imagem 12: Autenticação O sistema está aguardando a confirmação da conexão](https://ajuda.sankhya.com.br/hc/article_attachments/42639484170263)

- **Ativo**
  WhatsApp conectado e funcionando

![Imagem 13: Ativo WhatsApp conectado e funcionando](https://ajuda.sankhya.com.br/hc/article_attachments/42639497254935)
