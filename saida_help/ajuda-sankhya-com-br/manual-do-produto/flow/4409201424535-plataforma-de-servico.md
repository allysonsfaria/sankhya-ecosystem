---
id: "4409201424535"
titulo: "Plataforma de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:10:46Z"
rotulos: ["Configuração", "Central de Vendas", "Processo", "sankhyaflow", "Plataforma de Serviço", "Automatiza tarefas", "Confirma pedidos", "Diversos serviços ERP", "Tarefas de Serviço"]
---

# Plataforma de Serviço

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313325944215) Versão disponível: a partir da 4.7
```

---

A Plataforma de Serviço é um recurso que existe nas Tarefas de Serviço do SankhyaFlow. Ele permite utilizar uma série de serviços do ERP de uma forma simples e rápida, sem precisar de personalização.

**(2)** A lista de serviços é limitada e eventualmente eles podem aumentar, conforme as versões do Sankhya Om vão avançando.

Esse recurso também atende cenários no processo quando é necessário acessar uma outra tela, rotina do ERP e, ao invés de sair do SankhyaFlow, o modelador pode utilizar a Plataforma de Serviço para gerar essa automatização do processo e integração à outras rotinas do ERP.

Por exemplo, um modelador pode definir que uma lista de interessados no processo receba alertas dentro do ERP a cada tarefa concluída, sem que os usuários façam necessariamente parte do processo. Ele consegue fazer isso utilizando o **"Serviço para enviar avisos"** (Mensageiro do Sankhya Om).

Um processo de Pedido de Compra pode contemplar uma simulação de frete; então, através do Número da Nota, o modelador poderá definir uma Tarefa de Serviço do tipo Plataforma de Serviço que possua o serviço onde é feita a simulação de frete.

Nessa documentação trataremos sobre nosso [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#casodeuso), as [Configurações da Tarefa de Serviço "Confirmação de Pedido"](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#configura%C3%A7%C3%B5esdatarefadeservi%C3%A7oconfirma%C3%A7%C3%A3odepedido), os [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#resultados) e os [Demais serviços disponíveis em Plataforma de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#demaisservi%C3%A7osdispon%C3%ADveisemplataformadeservi%C3%A7o).

---

#### Caso de Uso

A empresa Alpha Ltda possui o módulo SankhyaFlow em seu ERP Sankhya. Com o intuito de evoluir na utilização dos processo ela adotou as melhores práticas, criando um processo a partir de um modelo. O modelo utilizado foi o de **"Pedido de venda simplificado"**:

![Imagem 2: A empresa Alpha Ltda possui o módulo SankhyaFlow em seu ERP Sankhya . Com o intuito de evoluir na utilização dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4409203294359)

| **Processo Pedido de venda simplificado** |
| --- |

O processo visa simplificar um lançamento de Pedido de Venda, reduzindo os campos que precisam ser preenchidos, simplificando as etapas e deixando esse processo mais ágil; por isso, o processo tem uma série de Tarefas de Serviço, pois elas deixam o processo inteligente, ágil e automatizado, diminuindo as interações com o usuário ao lançar o pedido.

A tarefa que utilizaremos aqui é a de **"Confirmação de pedido"**. Após o lançamento e registro do pedido, é gerado um Número do Pedido relacionado à [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas); para dar continuidade, esse pedido precisa ser confirmado e, nesse ponto, utilizaremos a Plataforma de Serviço para gerar essa confirmação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#top)

#### Configurações da Tarefa de Serviço "Confirmação de Pedido"

Para nosso caso de uso, utilizaremos um Processo Modelo de Pedido de venda simplificado. Para utilizá-lo, basta cadastrar um processo de negócio com base em um modelo. Feito isso, é necessário acessar a Tarefa de Serviço **"Atualização de dados do processo"** para que sejam ajustadas as configurações de ambiente, sendo elas: Tipo de Operação, Vendedor, Centro de Resultado, etc.

Com os ajustes no processo modelo feitos, podemos ir para o próximo passo. Iremos selecionar a Tarefa de Serviço **"Confirmação de pedido"** e seguir para o **"Tipo de serviço"** que, em nosso caso, será **"Plataforma de Serviço"**. Após essa definição, é necessário clicar no botão ![Imagem 3: Com os ajustes no processo modelo feitos, podemos ir para o próximo passo. Iremos selecionar a Tarefa de Serviço…](https://ajuda.sankhya.com.br/hc/article_attachments/4409213125399) **"Configuração"** para acessarmos os detalhes desse Tipo de serviço:

[GIF animado: Imagem 4: Com os ajustes no processo modelo feitos, podemos ir para o próximo passo. Iremos selecionar a Tarefa de Serviço…](https://ajuda.sankhya.com.br/hc/article_attachments/4409220899735)

| **Configuração em Plataforma de Serviço** |
| --- |

Ao clicar no botão Configuração, o pop-up Plataforma de Serviço será aberto; a primeira definição é sobre qual serviço utilizar e, em nosso caso, utilizaremos o **"Serviço para confirmação de notas/pedidos"**.

![Imagem 5: Ao clicar no botão Configuração , o pop-up Plataforma de Serviço será aberto; a primeira definição é sobre qual serviço…](https://ajuda.sankhya.com.br/hc/article_attachments/4409221016599)

| **Serviços disponíveis** |
| --- |

**Observação:** cada serviço possui uma proposta de utilização, nos tópicos seguintes abordaremos os outros serviços.

Os serviços precisam receber informações para serem utilizados, por exemplo, o Serviço para confirmação de notas/pedidos é necessário informar o Número de Nota/Pedido que o serviço irá confirmará e quem realizará essa confirmação. Isso irá variar de acordo com o serviço selecionado, sendo que nem todos os dados são obrigatórios.

Alguns serviços retornam informações e elas podem ser utilizadas no processo, bastando que o modelador atribua-as aos campos do processo. São exemplos de retorno: status da confirmação do Serviço para confirmação de notas/pedidos ou valores monetários quando trata-se do **"Serviço para simulação de frete"**.

Em nosso caso de uso utilizamos o retorno do Serviço para confirmação de notas/pedidos e trataremos apenas os dados necessários para utilização desse serviço.

![Imagem 6: Em nosso caso de uso utilizamos o retorno do Serviço para confirmação de notas/pedidos e trataremos apenas os dados…](https://ajuda.sankhya.com.br/hc/article_attachments/4409221278359)

| **Detalhes do Serviço para confirmação notas/pedidos** |
| --- |

Na imagem acima, na parte esquerda da tela, podemos ver os dados que o serviço demanda, sendo eles: o Número da Nota e o Código do Usuário de autenticação da nota. Já ao lado direito temos o campo que pegará o retorno desse serviço.

Tanto a utilização dos dados a serem passados, como o retorno do serviço, se dão por meio de scripts na linguagem JavaScript. Ao selecionar o **"Modo formulário"**, podemos escrever os scripts dos dados que serão passados no serviço:

![Imagem 7: Tanto a utilização dos dados a serem passados, como o retorno do serviço, se dão por meio de scripts na linguagem…](https://ajuda.sankhya.com.br/hc/article_attachments/4409221464855)

| **Campos no Modo formulário** |
| --- |

Para todo dado que o serviço pede, temos os seguintes detalhes:

- **Nome:** O nome do dado.
- **Descrição:** A descrição desse dado.
- **Tipo do Dado:** Qual é o tipo desse dado. Como nesse caso de uso estamos utilizando a confirmação de nota, nós precisamos do Número da Nota; por isso, seu tipo é BigDecimal. Essa informação é importante pois é isso que você vai retornar no script no campo **"Valor"**.
- **Valor:** O campo no qual o modelador escreve o script em JavaScript, que vai buscar a informação desejada e na última linha retornar ela. Nesse campo podemos utilizar todos os métodos de consulta de dados (buscarDados, buscarLinhas, getCampo, nativeSelect, etc…). Dessa forma, o modelador pode buscar por uma informação que esteja atrelada diretamente ao processo ou até fora dela em outras tabelas do ERP.

Na imagem abaixo, observe como ficou o nosso caso de uso para o dado **"NUNOTA"**:

![Imagem 8: Na imagem abaixo, observe como ficou o nosso caso de uso para o dado "NUNOTA" :](https://ajuda.sankhya.com.br/hc/article_attachments/4409221604503)

| **Nro. único nota** |
| --- |

| ``` var idinstprn = getIdInstanceProcesso(); var nota = buscarDado("MAX(NUMINT)", "TWFIVAR", "IDINSTPRN = :IDINSTPRN",idinstprn); return nota; ``` |
| --- |

Para o dado CODUSUAUTHINFO, que é o Código do Usuário para autenticação, o script ficou da seguinte forma:

![Imagem 9: Para o dado CODUSUAUTHINFO , que é o Código do Usuário para autenticação , o script ficou da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/4409221828759)

| **Cód. usuário para autenticação** |
| --- |

| ``` var usuario=getUsuarioLogado(); return usuario; ``` |
| --- |

Com esse script, o usuário de autenticação sempre será o que lançou o Pedido de Venda.

Após realizar essas definições, basta clicar em **"Salvar"** no canto inferior direito do pop-up e ele se fechará com as definições salvas, e como o processo foi alterado, lembre-se de publicá-lo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#top)

#### Resultados

Ao iniciar o processo de Pedido de venda simplificado, será necessário informar apenas alguns campos, como podemos ver na imagem abaixo:

![Imagem 10: Ao iniciar o processo de Pedido de venda simplificado , será necessário informar apenas alguns campos, como podemos ver…](https://ajuda.sankhya.com.br/hc/article_attachments/4409214255255)

| **Campos no Modo formulário** |
| --- |

Após isso, ao realizar uma consulta no Portal de Vendas, podemos verificar as informações do pedido lançado e já confirmado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#top)

#### Demais serviços disponíveis em Plataforma de Serviço

**Geração de arquivo de remessa (EDI Comercial):** Com esse serviço é possível gerar o arquivo de remessa e após o arquivo ser gerado, será possível enviá-lo por e-mail, como também para um diretório FTP ou ainda para uma pasta de repositório.

**Serviço para faturamento de pedidos:** Com esse serviço podemos faturar um pedido/nota já confirmado na base.

**Impressão de relatório formatado:** Com esse serviço é possível gerar a impressão de um Relatório Formatado e salvá-lo em uma pasta repositório ou também salvá-lo direto em um diretório FTP.

**Serviço para impressão de relatórios:** Com esse serviço é possível gerar a impressão de relatório direto para uma impressora local.

**Serviço de consulta ao serasa:** Com esse serviço podemos fazer uma consulta na base do Serasa.

**Serviço para simulação de frete:** Com esse serviço é possível solicitar a simulação para cálculo de frete para um parceiro que seja uma transportadora.

**Serviço para enviar avisos:** Com esse serviço é possível disparar mensagens para usuários, utilizando o Mensageiro do Sankhya Om.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409201424535-Plataforma-de-Servi%C3%A7o#top)
