---
id: "4404421872151"
titulo: "Histórico de Processo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:25Z"
rotulos: ["Configuração", "Eventos", "Tarefas", "Processo", "Histórico", "sankhyaflow", "histórico de processo", "Visualize histórico de processos", "Consulte eventos tarefas gateways", "Configure e personalize exibição"]
---

# Histórico de Processo

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313305406487) Módulo: Flow                    ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42313305408151) Versão disponível: a partir da 4.8
```

---

O Histórico de Processo do SankhyaFlow é um recurso que possibilita ao executor de tarefas consultar dados do histórico de um processo em uma linha do tempo (cronológica), em que são apresentados diferentes tipos de eventos (início, intermediários, fim), gateways e tarefas do processo.

Assim, o executor da tarefa do SankhyaFlow utilizará o histórico de processo para verificar informações sobre a origem do processo como os executores (donos de tarefas anteriores) dados preenchidos em tarefas, tempo de execução e etc, para que esses dados possam auxiliá-lo na execução de sua tarefa ou acompanhamento do processo.

Para cada elemento, são apresentadas as datas de criação, aceite, conclusão, status (em andamento ou concluído) e tempo gasto de execução.

Nesse artigo, você terá acesso aos seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#casodeuso)
2. [Configurando a apresentação do Histórico de Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#configurandoaapresenta%C3%A7%C3%A3odohist%C3%B3ricodeprocesso)
3. [Consultando o Histórico de Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#consultandoohist%C3%B3ricodeprocesso)
4. [Tipos de elementos do Histórico de Processo utilizados no Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#tiposdeelementosdohist%C3%B3ricodeprocessoutilizadosnocasodeuso)
5. [Apresentação de outros Tipos de Elementos no Histórico](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#apresenta%C3%A7%C3%A3odeoutrostiposdeelementosnohist%C3%B3rico)
6. [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#resultados)

---

#### Caso de Uso

O processo de **"Solicitação de compras"** que apresentamos abaixo, tem o objetivo de permitir a realização de uma solicitação de compras no Flow, contemplando etapas de solicitação, aprovação, cotação, geração de pedidos e comunicação por e-mail aos envolvidos no processo.

![Imagem 3: O processo de "Solicitação de compras" que apresentamos abaixo, tem o objetivo de permitir a realização de uma…](https://ajuda.sankhya.com.br/hc/article_attachments/4404417210007)

| **Processo de Solicitação de Compras** |
| --- |

Em determinados momentos, os executores de processos têm a necessidade de consultar o histórico de processos para identificar, por exemplo, donos de tarefas anteriores, data de abertura do processo ou de tarefas, dados preenchidos em formulários, tempo gasto para execução e etc, para acompanhamento e realização de sua atividade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

#### Configurando a apresentação do Histórico de Processos

Os dados que são apresentados no histórico na lista de tarefas podem ser configurados no ambiente de modelagem no contexto de processo (inicialização) e tarefas de usuário, na aba **"Resumo do Histórico"**, conforme as imagens abaixo:

![Imagem 4: Os dados que são apresentados no histórico na lista de tarefas podem ser configurados no ambiente de modelagem no…](https://ajuda.sankhya.com.br/hc/article_attachments/4404417593751)

| **Configuração do Resumo do Histórico no contexto de Processo (inicialização)** |
| --- |

![Imagem 5: Configuração do Resumo do Histórico no contexto de Processo (inicialização)](https://ajuda.sankhya.com.br/hc/article_attachments/4404417985943)

| **Configuração do Resumo do Histórico no contexto de Tarefa do Usuário** |
| --- |

Por padrão, caso o modelador não realize nenhuma configuração no resumo do histórico, serão apresentados no Histórico de Processo um título com a descrição informada para o formulário e todos os respectivos campos disponíveis nesse formulário de inicialização ou tarefa de usuário.

Para personalizar o histórico que será exibido para a tarefa de usuário **"Analisar solicitação de compra"**, basta selecionar essa tarefa, acessar a aba Resumo do Histórico e clicar em **"Editar resumo do Histórico"**. Assim, na sequência, será aberta a tela para configuração. Abaixo demonstramos o procedimento, observe:

[GIF animado: Imagem 6: Para personalizar o histórico que será exibido para a tarefa de usuário "Analisar solicitação de compra" , basta…](https://ajuda.sankhya.com.br/hc/article_attachments/4404435542807)

| **Configuração do Resumo do Histórico** |
| --- |

**Observação:** o modelador poderá definir um título geral para todos os formulários contidos em uma tarefa. Para isso, basta clicar em **"Título do formulário"** para que seja apresentada a variável para inserção de um título geral do(s) formulário(s) da tarefa:

[GIF animado: Imagem 7: Observação: o modelador poderá definir um título geral para todos os formulários contidos em uma tarefa. Para isso,…](https://ajuda.sankhya.com.br/hc/article_attachments/4404435615639)

| **Configurando a variável do título** |
| --- |

Para configurar a apresentação dos dados preenchidos em um formulário, é necessário selecioná-lo na opção **"Variáveis"**. No caso da tarefa **"Analisar solicitação de compra"**, temos os formulários **"AD\_SOLICITACAOCOMPRA"** e **"AD\_APROVACAO"**.

![Imagem 8: Para configurar a apresentação dos dados preenchidos em um formulário, é necessário selecioná-lo na opção "Variáveis" .…](https://ajuda.sankhya.com.br/hc/article_attachments/4404427391255)

| **Configurando a variável do título** |
| --- |

Como essa tarefa possui campos editáveis que estão no formulário AD\_APROVACAO, iremos clicar nessa opção para que sejam apresentadas as variáveis conforme a imagem abaixo:

![Imagem 9: Como essa tarefa possui campos editáveis que estão no formulário AD_APROVACAO , iremos clicar nessa opção para que…](https://ajuda.sankhya.com.br/hc/article_attachments/4404435728023)

| **Configuração do Resumo do Histórico (variáveis)** |
| --- |

Na imagem acima podemos identificar na primeira linha a variável **'$FormTitle{AD\_APROVACAO}'**, que irá retornar o título no histórico obtendo o dado da descrição informada no formulário.

Na linha seguinte, temos o nome do formulário e, na sequência, temos os campos disponíveis nele. Caso o modelador queira ocultar a apresentação de algum campo no histórico, basta retirar a linha que corresponda a ele.

Em nosso exemplo, mantemos todos os campos para apresentação no Histórico de Processo dessa tarefa e modificamos apenas o título para **"Aprovação da Solicitação"** e o formatamos em negrito e itálico:

![Imagem 10: Em nosso exemplo, mantemos todos os campos para apresentação no Histórico de Processo dessa tarefa e modificamos apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/4404435772055)

| **Configuração do Resumo do Histórico (variáveis)** |
| --- |

**![Imagem 11: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16110001315863) Informações adicionais:**

- Não é suportada a apresentação de dados no histórico de formulário quando for utilizado o recurso de ligação entre formulários na modelagem;
- Quando o formulário for do tipo múltiplos registros, os dados serão apresentados no histórico na lista de tarefas em uma sequência com os dados de cada registro;
- O modelador pode digitar no Resumo do Histórico qualquer mensagem para ser apresentada no Histórico de Processo.

Dando continuidade, iremos salvar e publicar o processo:

[GIF animado: Imagem 12: Dando continuidade, iremos salvar e publicar o processo:](https://ajuda.sankhya.com.br/hc/article_attachments/4404435864727)

| **Configuração do Resumo do Histórico (variáveis configuradas)** |
| --- |

Note que, após clicar em salvar, as variáveis que definimos anteriormente foram apresentadas na aba Resumo do Histórico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

#### Consultando o Histórico de Processo

Maria é dona da tarefa **"Realizar cotação"** e identificou a necessidade de consultar dados de tarefas anteriores como a justificativa para aprovação da compra, o responsável pela aprovação e o tempo gasto até o processo chegar ao setor de Compras para cotação.

Para consultar esse histórico, basta que Maria posicione essa tarefa, clique no botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15499970261527) **"Outras Opções..."** e escolha a opção **"Histórico do Processo"**. Observe abaixo como fazemos:

[GIF animado: Imagem 14: Para consultar esse histórico, basta que Maria posicione essa tarefa, clique no botão "Outras Opções..." e escolha a…](https://ajuda.sankhya.com.br/hc/article_attachments/4404427812887)

| **Consulta ao Histórico do Processo** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

#### Tipos de elementos do Histórico de Processo utilizados no Caso de Uso

O Histórico de Processo é apresentado em uma linha do tempo (cronológica) em que cada elemento do fluxo do processo é apresentado em uma sequência na vertical, ordenada pela sua data de criação.

Abaixo iremos tratar sobre os [Eventos de início](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#eventosdein%C3%ADcio), [Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#tarefas) e [Gateways](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#gateways).

**Eventos de início**

Todos os tipos de Eventos de início disponibilizados na modelagem podem ser apresentados no histórico. Quando o processo for iniciado por uma pessoa e houver foto dela no seu usuário, ela será apresentada no card de início; caso contrário, será exibido apenas o símbolo do Evento de início, acompanhado do nome do evento dado pelo modelador e a data de abertura da solicitação (processo).

![Imagem 15: Todos os tipos de Eventos de início disponibilizados na modelagem podem ser apresentados no histórico. Quando o…](https://ajuda.sankhya.com.br/hc/article_attachments/4404624938903)

| **Evento de início do Processo** |
| --- |

Assim, ao clicar sobre o card de abertura do processo, podemos visualizar os dados preenchidos no formulário de inicialização, conforme demonstramos abaixo:

[GIF animado: Imagem 16: Assim, ao clicar sobre o card de abertura do processo, podemos visualizar os dados preenchidos no formulário de…](https://ajuda.sankhya.com.br/hc/article_attachments/4404624950807)

| **Dados preenchidos em Tarefas de Usuário** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#tiposdeelementosdohist%C3%B3ricodeprocessoutilizadosnocasodeuso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

**Tarefas**

Os tipos de tarefas (serviço, usuário e e-mail) utilizados na modelagem do processo e executados, são representados no histórico com o respectivo símbolo de cada tipo de tarefa, sendo possível, especificamente, para Tarefa do tipo Usuário, visualizar os dados preenchidos em formulários.

Podemos visualizar no card, fotos de usuários que concluíram tarefas (quando possuírem em seu cadastro de usuário) e, caso não possua foto, será exibido apenas o símbolo do tipo usuário e o nome nome do dono da tarefa também será apresentado no card.

Em todos os cards de Tarefas de Usuário temos a data de aceite da tarefa (momento em que a tarefa foi atribuída a uma determinada pessoa), a data de conclusão (quando houver) e o tempo gasto.

**Nota:** quando a tarefa ainda não tiver data de aceite ou conclusão, o tempo gasto será calculado do momento da criação da tarefa até o momento da geração (visualização) do histórico do processo.

Abaixo trouxemos um exemplo de card de uma Tarefa de Usuário:

![Imagem 17: Abaixo trouxemos um exemplo de card de uma Tarefa de Usuário :](https://ajuda.sankhya.com.br/hc/article_attachments/4404624966935)

| **Card Tarefa de Usuário** |
| --- |

Clicando sobre esse card, podemos visualizar os dados que foram preenchidos em formulários da tarefa.

Abaixo, temos o exemplo de uma tarefa de serviço que foi executada pelo processo de Solicitação de compras:

![Imagem 18: Abaixo, temos o exemplo de uma tarefa de serviço que foi executada pelo processo de Solicitação de compras :](https://ajuda.sankhya.com.br/hc/article_attachments/4404625005847)

| **Card Tarefa de Serviço** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#tiposdeelementosdohist%C3%B3ricodeprocessoutilizadosnocasodeuso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

**Gateways**

Também é possível visualizar todos os tipos de Gateways que foram inseridos no processo pelo modelador (paralelo, exclusivo e inclusivo) e executados até o momento da consulta.

**Observação:** o nome apresentado no Gateway é o mesmo que foi definido pelo modelador no ambiente de modelagem. Caso não tenha nome, não será exibido nenhum nome no card:

![Imagem 19: Observação: o nome apresentado no Gateway é o mesmo que foi definido pelo modelador no ambiente de modelagem. Caso não…](https://ajuda.sankhya.com.br/hc/article_attachments/4404625047191)

| **Card Gateway Exclusivo** |
| --- |

Observe na imagem acima que o modelador definiu o nome **"Solicitante é o responsável pelo CR?"** para o Gateway.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#tiposdeelementosdohist%C3%B3ricodeprocessoutilizadosnocasodeuso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

#### Apresentação de outros Tipos de Elementos no Histórico

Todos os tipos de elementos utilizados na modelagem e executados no processo serão exibidos no Histórico de Processo. Abaixo, apresentamos alguns exemplos de outros elementos que poderão ser exibidos no histórico:

---

**Tarefas**

![Imagem 20: Tarefas](https://ajuda.sankhya.com.br/hc/article_attachments/4404618241431)

| **Card Tarefa de Serviço** |
| --- |

![Imagem 21: Card Tarefa de Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/4404625375639)

| **Card Tarefa de E-mail** |
| --- |

---

**Eventos Intermediários**

Quando executados no processo, os Eventos Intermediários também serão apresentados na linha do tempo do Histórico de Processo:

![Imagem 22: Quando executados no processo, os Eventos Intermediários também serão apresentados na linha do tempo do Histórico de…](https://ajuda.sankhya.com.br/hc/article_attachments/4404625401111)

| **Card Evento Intermediário de Tempo** |
| --- |

Observe no exemplo da imagem acima, que o modelador definiu para o Evento Intermediário de tempo o nome **"Aguarda pagamento"** e seu símbolo é apresentado no card.

---

**Eventos de Fim**

Os diferentes tipos de Eventos de Fim são representados (após execução) no histórico com o nome dado pelo modelador, data de fim e o símbolo do evento, conforme consta nas imagens abaixo:

![Imagem 23: Os diferentes tipos de Eventos de Fim são representados (após execução) no histórico com o nome dado pelo modelador,…](https://ajuda.sankhya.com.br/hc/article_attachments/4404625422999)

| **Card Evento de Fim** |
| --- |

![Imagem 24: Card Evento de Fim](https://ajuda.sankhya.com.br/hc/article_attachments/4404618293271)

| **Card Evento de Fim do Tipo Término** |
| --- |

---

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#apresenta%C3%A7%C3%A3odeoutrostiposdeelementosnohist%C3%B3rico) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)

#### Resultados

Abaixo temos a representação do histórico de um processo de Solicitação de compras que foi consultado pela Maria na tarefa **"Realizar cotação"**. Observe que cada elemento é apresentado cronologicamente pela sua data de criação:

![Imagem 25: Abaixo temos a representação do histórico de um processo de Solicitação de compras que foi consultado pela Maria na…](https://ajuda.sankhya.com.br/hc/article_attachments/4404568597399)

| **Histórico do Processo de Solicitação de compras** |
| --- |

Também podemos visualizar a legenda, com o status de execução de cada elemento (em andamento ou concluída), onde a bola **verde** significa conclusão e a **azul** em andamento.

**Nota:** quando o card estiver todo preenchido de **cinza**, como na tarefa Realizar cotação, significa que essa é a tarefa que o usuário (em nosso caso a Maria), acessou na lista de tarefas para visualizar o histórico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404421872151-Hist%C3%B3rico-de-Processo#top)
