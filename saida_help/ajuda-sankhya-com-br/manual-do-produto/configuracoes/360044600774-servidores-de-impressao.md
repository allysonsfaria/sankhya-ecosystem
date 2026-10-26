---
id: "360044600774"
titulo: "Servidores de Impressão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:50:36Z"
rotulos: ["manual", "Configuração", "Impressão", "Servidores de Impressão", "Sankhya Print Service", "br.com.sankhya.servidoresdeimpressao", "Servidores de Impressão manual", "Servidores", "Configuração e Gerenciamento de Servidores de Impressão no Sankhya", "Jiva Print Service"]
---

# Servidores de Impressão

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310728159511) Módulo: Configurações > Avançado > Impressão
```

---

Para configurar o componente [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service)/Jiva Print Service você deve utilizar a tela de servidores de impressão. Esta rotina permite que você cadastre um servidor de impressão e suas impressoras. Ao acionar esta tela, teremos a lista de servidores cadastrados.

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#abageral) |  | [Aba Controle de Acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#abacontroledeacesso) |
| --- | --- | --- |
| [Aba Impressoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#abaimpressoras) |  | [Cadastrando um Servidor de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#cadastrandoumservidordeimpresso) |

![Imagem 2: Cadastrando um Servidor de Impressão](https://ajuda.sankhya.com.br/hc/article_attachments/1500002191842)

## Aba Geral

O campo **"Código"** é preenchido automaticamente ao ser criado o servidor.

Os campos **"Nome ou IP"** e **"Porta"** são preenchidos pelo sistema com os dados que foram informados na criação do servidor.

Informe um nome para o servidor de impressão no campo **"Descrição"**.

Através da marcação **"Ativo"** você define se o servidor de impressão está disponível ou não.

O campo **"Usuário"** exibe o código de usuário do responsável pela inclusão do servidor.

No campo **"Dt. Alteração"** é apresentada a data e horário de criação do servidor ou de sua última alteração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#top)

## Aba Controle de Acesso

Através desta aba, configure o acesso de um grupo ou usuário ao servidor de impressão selecionado. Configurando por meio do campo **"Tipo"** um grupo, qualquer pessoa do grupo poderá imprimir em qualquer impressora do servidor. Quando configurado apenas um usuário, apenas ele terá permissão para imprimir em qualquer impressora do servidor.

![Imagem 3: Através desta aba, configure o acesso de um grupo ou usuário ao servidor de impressão selecionado. Configurando por…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002253101)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#top)

## Aba Impressoras

O primeiro passo para efetuar o cadastro de uma nova impressora é através dessa aba. Quando você acionar o botão ![Imagem 4: O primeiro passo para efetuar o cadastro de uma nova impressora é através dessa aba. Quando você acionar o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16749069615127) **"Cadastrar Impressoras"**, será aberto o pop-up **"Cadastrando de um servidor de** **impressão"**, exibindo a lista de impressoras disponíveis. Selecionando a(s) impressora(s) desejada(s), clique no botão **"Concluir"** para finalizar o procedimento.

O campo **"Código"** é preenchido automaticamente ao ser cadastrada a impressora.

Através do campo **"Endereço"** você visualiza o IP da máquina, a porta do servidor de impressão e o nome da impressora cadastrada; clicando sobre o campo, é exibido o pop-up **"Editando campo Endereço"**, que possibilita a edição desses dados.

O botão **"Imprimir teste"** permite a impressão de uma página de teste para verificação do funcionamento da impressora selecionada.

![Imagem 5: O botão "Imprimir teste" permite a impressão de uma página de teste para verificação do funcionamento da impressora…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002191882)

**Sub-aba Geral**

Nessa sub-aba são exibidas as informações pertinentes à cada impressora configurada, como por exemplo, seu nome, status ou a data e hora de seu cadastro e sua última modificação.

**Sub-aba Controle de Acesso**

Nessa aba você configura o acesso de uma pessoa específica ou de um grupo à impressora indicada. A configuração de acesso ocorre da seguinte forma:

- Quando configurado apenas um usuário, apenas ele terá permissão para imprimir nessa impressora;
- Configurando um grupo, qualquer pessoa desse grupo poderá imprimir na referida impressora.

![Imagem 6: Configurando um grupo, qualquer pessoa desse grupo poderá imprimir na referida impressora.](https://ajuda.sankhya.com.br/hc/article_attachments/1500002253121)

O campo **"Tipo"** define entre as alternativas **"Usuário"** ou **"Grupo"**, o acesso à impressora. Após sua definição, o campo abaixo irá segui-lo, tendo sua nomenclatura apresentada como **"Usuário"** ou **"Grupo"**.

**Verificando o status da impressora**

Ao cadastrar uma impressora, a localização dessa impressora é armazenada no banco de dados do Sankhya Om. O processo de atualização automática de status visa manter o status dessa localização de impressora, sincronizado com o status da impressora no servidor SPS apropriado.

Essa atualização ocorre a cada 1 minuto e pode ser visualizada na sub-aba **"Geral"**, através do campo **"Status"**. Essa rotina não é atualizada automaticamente. O Sankhya Om atualiza o status da impressora na tabela e você precisa atualizar a tela para ver o novo status.

Uma impressora pode ter os seguintes estados:

- **Pronta:** Indica que a impressora está pronta para receber novas impressões, sem espera;
- **Processando:** Aponta que a impressora está processando um documento e que novos trabalhos serão colocados na fila. A atualização para esse estado depende de que a impressora notifique o sistema operacional de seu status e de que esse notifique a JPS. Em muitos casos, uma impressora que está imprimindo um documento pode aparecer como Pronta. Este estado foi incluído para manter a compatibilidade com a JPS.
- **Parada:** Assinala que a impressora está parada por algum motivo e uma intervenção direta na impressora é requisitada. A atualização para esse estado depende de que a impressora notifique o sistema operacional de seu status e de que esse notifique a JPS. Em muitos casos, uma impressora que está parada pode aparecer como Pronta. Este estado foi incluído para manter a compatibilidade com a JPS.
- **Desconhecido:** Mostra que o componente SPS não foi capaz de determinar o estado da impressora.

O processo de atualização de impressoras pode ser executado manualmente, clicando no botão **"Atualizar status"**. Esse processo, contudo, atualiza as impressoras de todos os servidores de impressão cadastrados no sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#top)

## Cadastrando um Servidor de Impressão

Para cadastrar um novo servidor de impressão, clique no botão ![Imagem 7: Para cadastrar um novo servidor de impressão, clique no botão "Cadastrar Servidores de Impressão" . Ao acioná-lo, será…](https://ajuda.sankhya.com.br/hc/article_attachments/16749069615127) **"Cadastrar Servidores de Impressão"**. Ao acioná-lo, será aberto o pop-up **"Cadastrando um servidor de impressão"**, para que você configure os dados iniciais do servidor.

[GIF animado: Imagem 8: Para cadastrar um novo servidor de impressão, clique no botão "Cadastrar Servidores de Impressão" . Ao acioná-lo, será…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002191902)

No primeiro passo, é necessário informar o nome ou IP e a porta do servidor de impressão. O preenchimento do campo **"Descrição"** é opcional. O botão **"Próximo"** será habilitado após os campos obrigatórios estarem devidamente preenchidos. Com as informações preenchidas, será solicitado ao servidor informado a sua lista de impressoras.

**Observação:** se algum problema ocorrer durante a busca por informações, será exibido um pop-up com uma mensagem informando o problema específico. Se o servidor informado for encontrado e a lista for retornada com sucesso, ela será exibida na tela de escolha de impressoras.

Feita a escolha, o servidor de impressão e as impressoras escolhidas são salvos. Após esses passos, o botão **"Concluir"** é habilitado e, ao acioná-lo, o procedimento de cadastro é finalizado.

Conheça o [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service) acessando o link.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#top)
