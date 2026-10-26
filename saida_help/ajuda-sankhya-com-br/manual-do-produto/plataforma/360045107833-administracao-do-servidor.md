---
id: "360045107833"
titulo: "Administração do Servidor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor"
trilha: "Manual do Produto > Plataforma e Integrações > Plataforma"
atualizado_em: "2026-07-29T16:13:54Z"
rotulos: ["Configuração", "Relatórios", "Cache", "Segurança", "Atualização", "Log", "Administração do Servidor", "Aprimoramento do Sistema", "Autorização de Acesso", "Autorização para Applets", "Avançado", "Extensões Instaladas", "Google Analytics", "Integração SankhyaW com o Google Analytics", "Licença", "Notificações", "Relatório de Diagnóstico", "Telemetria", "WPM", "br.com.sankhya.core.cfg.administracaoservidor", "Administração do Servidor manual", "Erro de comunicação com o servidor de acessos", "IPSERVACESS", "OCULQTDLICSAS", "Monitoramento do Servidor", "Personalização", "Configurações do Sistema"]
---

# Administração do Servidor

```
 Módulo: Configurações > Avançado
```

---

Nesta tela são disponibilizados recursos de monitoramento do servidor de aplicações, juntamente com informações da instalação do sistema, atualização da licença, entre outros. Abaixo, observe as abas disponibilizadas na tela.

| Funcionalidades da tela | |
| --- | --- |
| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abageral) | [Aba Personalização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abapersonaliza%C3%A7%C3%A3o) |
| [Aba Notificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abanotifica%C3%A7%C3%B5es) | [Aba Google Analytics](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abagoogleanalytics) |
| [Aba Relatório de Diagnóstico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abarelat%C3%B3riodediagn%C3%B3stico) | [Aba Add-ons Instalados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#AbaAdd-onsInstalados) |
| [Aba Extensões Instaladas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abaextens%C3%B5esinstaladas) | [Aba Eventos Programáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abaeventosprogram%C3%A1veis) |
| [Aba Licença](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abalicen%C3%A7a) | [Aba Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abaavan%C3%A7ado) |
| [Aba Autorização de Acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abaautoriza%C3%A7%C3%A3odeacesso) | [Configurações de Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#configura%C3%A7%C3%B5esdeseguran%C3%A7a) |

### Aba Geral

Nesta aba são apresentadas as facilidades que permitirão a Manutenção do Servidor, bem como as informações referentes ao sistema.

| [Seção Manutenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#manuten%C3%A7%C3%A3o) | [Seção Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#informa%C3%A7%C3%B5es) |
| --- | --- |

---

#### Seção Manutenção

**Download do Log:** esta opção permite efetuar o download do log do sistema. O log possui informações detalhadas do funcionamento do sistema e é um meio indispensável para reportar erro ou um comportamento fora do padrão por parte do sistema.

**Descartar Cache:** cache é o armazenamento de informações que tem o objetivo de melhorar a performance. O recurso de descarte do cache é útil, quando uma tarefa é executada em rotinas externas ao sistema, tais como: alteração de informações de banco de dados, parâmetros, entre outras. Esta não é uma opção de uso comum e seu propósito é bastante específico.

**Observação:** acionando esta opção, será realizada a limpeza do cache do timezone, não sendo necessário reiniciar o jboss/wildfly.

**Reinicializar Sistema:** esta opção irá reinicializar o sistema; ela é utilizada em situações específicas e em casos em que o descarte de cache não é suficiente.

**Observação:** para impedir que o usuário utilize a opção Reinicializar Sistema é necessário configurar o parâmetro **"-Denviroment.restart.blocked=true"** no servidor da aplicação. Além disso, ao efetuar essa configuração é possível definir uma mensagem de aviso utilizando o parâmetro **"definição realizada pelo usuário - MSGRBLQREST"**, como, por exemplo:

**"Não é permitida a reinicialização do sistema. Favor entrar em contato com o responsável pela aplicação"**. 

O parâmetro MSGRBLQREST deve ser criado de acordo com as seguintes regras: 

- **Chave:** MSGRBLQREST;
- **Descrição:** definição realizada pelo usuário;
- **Módulos do Sistema:** configurações;
- **Aba:** diversas;
- **Tipo:** texto;
- **Texto:** mensagem de aviso, conforme exemplificado anteriormente.

**Atualização do Sistema:**para saber mais sobre a atualização do sistema acesse o artigo [Atualização do sistema Sankhya Om via WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM). 

**Gerenciar Sessões:** através dessa opção, é possível ver as sessões dos usuários logados ou não no sistema. Ao clicar nela, será aberta a tela **"Gerenciador de Sessões"**, exibindo os usuários logados no sistema. Nessa tela, caso o campo **"Nome usuário"** seja exibido em branco, representa que uma pessoa acessou a tela de login do sistema mas ainda não o acessou de fato, ou também pessoas que fizeram logout (saíram do sistema) e foram redirecionados automaticamente para a tela de login.

**Nota:** o objetivo deste recurso não é gerenciar o uso de licenças. Para isso, utilize do SASConsole.

![Imagem 1: Nota: o objetivo deste recurso não é gerenciar o uso de licenças. Para isso, utilize do SASConsole .](https://ajuda.sankhya.com.br/hc/article_attachments/1500002028621)

**Observação:** para maiores informações a respeito deste recurso, clique no botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15993080035991) localizado na parte inferior da tela.

**Nota:** quando o parâmetro **"Ocultar a coluna Qtd. Licença no Geren. de Sessões na Administração do Servidor? - OCULQTDLICSAS"** estiver ligado, fará com que a coluna **"Qtd. Licenças"** não seja apresentada no pop-up Gerenciador de Sessões.

**Central de Ajuda:** esta opção permite a realização da baixa/atualização da documentação relacionada à Central de Ajuda, caso não esteja sendo utilizado o [Help Online](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599294-Help-Online). Esta ferramenta valida a data de modificação do arquivo referente a Central de Ajuda e seu nome em um arquivo de registro que utiliza como chave o nome do arquivo; arquivos cuja a data foi atualizada ou arquivos que não existem no registro, serão enviados para o repositório de clientes na próxima execução da rotina. Ao utilizar esta opção, será aberto um pequeno pop-up, que pode assumir os seguintes status:

![clip2378](https://ajuda.sankhya.com.br/hc/article_attachments/360061912493)

![clip2376](https://ajuda.sankhya.com.br/hc/article_attachments/360060983254)

![clip2379](https://ajuda.sankhya.com.br/hc/article_attachments/360060983274)

![clip2380](https://ajuda.sankhya.com.br/hc/article_attachments/360060983294)

![clip2381](https://ajuda.sankhya.com.br/hc/article_attachments/360060983314)

![clip2383](https://ajuda.sankhya.com.br/hc/article_attachments/360061912513)

![clip2384](https://ajuda.sankhya.com.br/hc/article_attachments/360060983354)

**Observação:** tem-se uma configuração que permitirá que o seu sistema **Sankhya Om** seja ou não exibido nos resultados de ferramentas de pesquisa ao procurar por **"Sankhya"**. Para realizar uma restrição desses resultados, basta configurar o parâmetro -**Dsankhyaw.app.indexing.enabled=false**. Porém, ao configurar o parâmetro como **true**, não haverá restrição para indexação, ou seja, a página será mostrada nos resultados da pesquisa. Destaca-se ainda que, esse parâmetro será configurado no arquivo standalone.conf.bat, em rem JAPE, localizado no diretório de instalação do **Sankhya Om** da sua máquina. Dessa forma, depois que esse parâmetro for configurado de acordo com sua preferência, o servidor deve ser reiniciado para constar as modificações realizadas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abageral)

#### Seção Informações

No espaço destinado às informações, existem os dados relacionados ao servidor de aplicações; dados como **"Versão do Sistema"**, **"Arquitetura da JVM"**, **"Banco de Dados"**, entre outros.

![Imagem 10: No espaço destinado às informações, existem os dados relacionados ao servidor de aplicações; dados como "Versão do…](https://ajuda.sankhya.com.br/hc/article_attachments/23781531796503)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abageral) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Personalização

Esta aba permite que todas as pessoas que possuam acesso a tela, adicionem ou alterem a logomarca que será exibida na tela de login, ou ainda, alterem os papéis de parede do sistema, removendo-os e/ou adicionando-os.

| [Logomarca da página de login](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#logomarca) | [Papéis de parede](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#papeisdeparede) |
| --- | --- |

---

**Importante:** ao gerar imagens para planos de fundo utilize a dimensão de 1920x1200 e o padrão de cores RGB.

![Imagem 11: Importante: ao gerar imagens para planos de fundo utilize a dimensão de 1920x1200 e o padrão de cores RGB.](https://ajuda.sankhya.com.br/hc/article_attachments/1500002028701)

#### Logomarca da página de login

Quando não há uma imagem de logomarca no sistema, o botão **"+ Logo"** será exibido e, ao ser acionado, será aberta a janela de **"Seleção de logomarca"**, para que seja escolhida uma logomarca em sua máquina.

[GIF animado: Imagem 12: Quando não há uma imagem de logomarca no sistema, o botão "+ Logo" será exibido e, ao ser acionado, será aberta a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001973522)

Quando existe uma imagem salva como logomarca, ela é exibida juntamente ao botão **"Alterar"** que, ao ser acionado, abrirá a janela de **"Seleção de logomarca"**, para que a imagem seja modificada, caso necessário. Além disso, será apresentado o botão **"Remover"**, que deverá ser utilizado caso queira excluir alguma logomarca permanentemente do sistema.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abapersonaliza%C3%A7%C3%A3o)

#### Papéis de parede

Alguns papéis de parede são disponibilizados por padrão no sistema, mas existe a possibilidade de acrescentar alguma imagem desejada. Essa inclusão é feita clicando sobre o botão **"+ Imagem"**, onde será aberta a tela para **"Adição de um papel de parede"**.

![Imagem 13: Alguns papéis de parede são disponibilizados por padrão no sistema, mas existe a possibilidade de acrescentar alguma…](https://ajuda.sankhya.com.br/hc/article_attachments/360100868954)

Caso queira excluir uma imagem, posicione o mouse sobre a imagem para que seja exibido um ícone de lixeira no canto superior direito da imagem, conforme demonstrado abaixo:

[GIF animado: Imagem 14: Caso queira excluir uma imagem, posicione o mouse sobre a imagem para que seja exibido um ícone de lixeira no canto…](https://ajuda.sankhya.com.br/hc/article_attachments/360103033053)

Assim como na exclusão de uma logomarca, ao clicar sobre este ícone, será a apresentada uma mensagem de confirmação de exclusão. Os papéis de parede padrão do sistema não podem ser removidos.

Tanto as imagens de papéis de parede, quanto a imagem da logomarca, são salvas no repositório de arquivos, na estrutura de pastas **"System > Imagens > Papéis de Parede"**. As imagens das logomarcas se localizam na raiz da pasta **"Imagens"**; já as imagens referentes aos papéis de parede inseridas manualmente, se encontram na pasta **"Papéis de Parede"**.

É disponibilizada também no sistema, uma outra forma de adicionar papéis de parede e logomarcas, colocando ambos em uma pasta chamada **"Wallpaper"**, dentro do diretório de modelos do servidor, definido no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**. Assim, as imagens que estiverem na pasta Wallpaper continuarão funcionando como papéis de parede e poderão ser visualizadas e removidas na aba **"Personalização"**, sendo que, quando uma nova imagem for inserida, o destino dela será a pasta **"Papeis de Parede"**, criada automaticamente no repositório.

A logomarca funciona da mesma forma, caso já exista o arquivo **"logo-cliente.jpg"** na pasta do parâmetro SERVDIRMOD, ela será exibida na aba de Personalização, para que possa ser alterada. Porém, quando uma nova logomarca for inserida, o destino dela será a pasta **"Imagens"** do repositório.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abapersonaliza%C3%A7%C3%A3o) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Notificações

Através desta aba, será possível enviar mensagens para todos as pessoas que usam o sistema. Os tipos de mensagens definem o ícone que será exibido na lista de mensagens (opção disponível através do ícone numérico no canto superior direito). O tipo de mensagem **"Urgente"**, além de ser registrada na lista de mensagens, exibe imediatamente um pop-up para cada pessoa logado.

![Imagem 15: Através desta aba, será possível enviar mensagens para todos as pessoas que usam o sistema. Os tipos de mensagens…](https://ajuda.sankhya.com.br/hc/article_attachments/23781521177879)

No lado esquerdo da tela, são definidos os tipos de notificação que poderão ser encaminhadas. Elas podem ser do tipo:

**Informação:** a pessoa será notificada com uma mensagem informativa.

**Atenção:** será enviada uma notificação de alerta.

**Erro:** a pessoa será notificada com uma mensagem de erro.

**Urgente:** através deste tipo de notificação, a pessoa será notificada instantaneamente com uma janela no centro da tela, independente da atividade que ele esteja desenvolvendo.

**Atualização do sistema:** será notificada instantaneamente com uma mensagem de atualização do sistema.

Os tipos de notificação **"Informação"**, **"Atenção"** e **"Erro"**, serão exibidos através do botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15993119979671) **"Notificações"** presente no canto superior direito da tela.

**Observação:** a cada 60 segundos um job é executado, recuperando os novos avisos de notificações. 

Feita a definição do Tipo de Notificação que será enviada, defina para quais pessoas será encaminhada a notificação. Esta escolha é feita através da opção **"Enviar para"**, que possui três opções:

- **Todos:** Através dessa opção, todas as pessoas irão receber a notificação.
- **Grupo:** Ao definir o campo com essa opção, a notificação será encaminhada apenas a um grupo de usuários. Se escolher esta opção, o filtro para escolha do grupo é imediatamente apresentado.
- **Usuário:** Definindo o campo com esta marcação, a notificação será encaminhada a uma ou mais pessoas específicas. De forma semelhante a opção anterior, ao escolher esta opção, o filtro para escolha da pessoa é imediatamente apresentado.

---

| **Comportamento automático em caso de erros no sistema:**  Quando ocorrem falhas internas geradas pela própria aplicação, como erros de envio de e-mail, triggers, procedures ou outras rotinas, o próprio sistema cria a notificação automaticamente na tabela de **Aviso do sistema (**`TSIAVI`**)**. Nesses cenários de erro, a aplicação não vincula a mensagem a um destinatário específico, deixando os campos de **Usuário (**`CODUSU`**)** e **Grupo (**`CODGRUPO`**)** vazios (`null`). Como o preenchimento dessas informações é feito de forma automática pelo sistema e **não há como o usuário alterá-las**, o comportamento padrão do Sankhya será disparar a notificação desse erro para **todos os usuários**. |
| --- |

---

Após ser feita a escolha dos destinatários da notificação, no lado direito da tela, é feita a formulação da notificação propriamente dita, onde devem ser inseridos seu **"Título"** e sua **"Descrição"**.

Por fim, é possível realizar o direcionamento da notificação às pessoas através dos botão **"Enviar"**. Caso o texto da notificação esteja incorreto, utilize o botão **"Limpar"** para excluir as informações inseridas, podendo dar início à criação de uma nova notificação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Google Analytics

O Google Analytics é um analisador gratuito de aplicações Web de nível empresarial. Ele fornece uma ótima visibilidade do tráfego da aplicação, disponibilizando indicadores importantes do uso do sistema. Quando a integração do **"Sistema + Google Analytics"** está ativa, algumas informações referentes à navegação dos usuários são enviadas para sua conta no Google Analytics. Os dados enviados dizem respeito apenas às pessoas vinculadas à sua conta, não podendo ser visualizados por terceiros. Com essas informações, será possível saber quais telas estão sendo mais utilizadas, qual fluxo as pessoas utilizam para executar uma determinada tarefa, qual o tempo de permanência delas no sistema, que região geográfica acessa-se mais o sistema, entre outras informações.

![Imagem 17: O Google Analytics é um analisador gratuito de aplicações Web de nível empresarial. Ele fornece uma ótima visibilidade…](https://ajuda.sankhya.com.br/hc/article_attachments/23034987654935)

O Google Analytics é um recurso de estatística de acesso à páginas da web, que é utilizado para se obter informações de acesso ao sistema. Estas informações limitam-se apenas aos acessos feitas às telas (cliques).

| [Seção Integrar com Google Analytics](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#integrar) | [Seção Aprimorando o sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#aprimorar) |
| --- | --- |

---

#### Seção Integrar com Google Analytics

Para realizar a configuração da integração do **Sankhya Om** com o Google Analytics é necessário criar uma conta no Google Analytics e, em seguida, preencher nessa aba, o campo **"ID da propriedade da web"** com o **"ID da métrica"** da conta criada. Por exemplo: **G-XXXXXXXXX**.

**Observação:** para encontrar o ID da conta criada, siga os seguintes passos:

**1.** Faça login na conta do Google Analytcs 4.

**2.** Clique em **"Administrador (Admin)"** na barra lateral de navegação.

**3.** Selecione a **"Propriedade (Property)"** para a qual deseja obter o ID da métrica. 

**4.** Clique em **"Fluxos de dados (Data Streams)"** na segunda coluna.

**5.** Escolha seu fluxo de dados na lista e copie o ID.

![Imagem 18: 5. Escolha seu fluxo de dados na lista e copie o ID.](https://ajuda.sankhya.com.br/hc/article_attachments/23034719435031)

Ao ser inserido o código, o botão **"Salvar"** será habilitado e, uma vez salva a configuração, o botão **"Desativar integração"** também será habilitado.

O botão Salvar utiliza o valor inserido no campo ID da propriedade da web para inseri-lo na integração com o Google Analytics. Isso funciona de forma interna e transparente, ou seja, é necessário apenas inserir o devido código no campo mencionado, Salvar, e a integração já está realizada.

A desvinculação do **Sankhya Om** com essa ferramenta também ocorre de maneira simples. Caso essa seja a necessidade, basta utilizar o botão Desativar integração. Automaticamente o campo ID da propriedade da web receberá o valor padrão do **Sankhya Om** e os dados não mais serão enviados para o Google Analytics.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abagoogleanalytics)

#### Seção Aprimorando o sistema

É possível optar pelo aprimoramento da captura de informações do sistema para disponibilização para o **Sankhya Om**, a fim de verificar o desempenho do sistema e os processos para melhorias na qualidade do software.

Não existe necessidade de criação ou configuração de usuário da Google para utilização desta opção. apenas marque ou desmarque a opção **"Permitir que o sistema aprimore minha navegação"**.

O Google Analytics pode ser acessado através do endereço **"http://www.google.com/analytics/"**. No entanto, para usufruir desta solução, é necessário possuir um cadastro ou conta na Google. Esse cadastro também é gratuito e possibilita acesso não só a funcionalidade citada, como também todas as demais soluções disponibilizadas pela Google.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abagoogleanalytics) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Relatório de Diagnóstico

Nesta aba são apresentadas as estatísticas do sistema.

| [Sub-aba Informações de Diagnóstico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#informa%C3%A7%C3%B5esdediagn%C3%B3stico) | [Sub-aba Parâmetros de Performance](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#Par%C3%A2metrosdePerformance) |
| --- | --- |

---

![Imagem 19: Sub-aba Parâmetros de Performance](https://ajuda.sankhya.com.br/hc/article_attachments/360103033213)

#### Sub-aba Informações de Diagnóstico

**Diretório temporário:** é o diretório onde são armazenados arquivos temporários do sistema. Para saber qual é o diretório temporário, basta acessar a aba Geral do menu de Administração do Sistema e verificar o campo **"Diretório Temporário"**. Para este quesito, o acesso é permitido para leitura e escrita do diretório.

**Memória Física:** é o total de memória física do servidor, ou seja, é a memória RAM da máquina.

**Memória alocada para o sistema:** se refere à quantidade de memória reservada para o sistema. Através do WPM na aba Configurações, opção Configurações de memória do JBoss é possível aumentar ou diminuir a quantidade de memória.

**Tempo de CPU utilizado:** tempo de processamento do sistema em relação ao tempo total de execução do servidor de aplicações. Esta informação é obtida internamente pelo sistema.

**Tempo gasto com GC:** porcentagem do tempo gasto com Garbage Collector em relação ao tempo total execução do servidor de aplicações. Esta informação é obtida internamente pelo sistema.

**Acesso de usuários:** média de acessos únicos de pessoas que utilizaram o **Sankhya Om** nos últimos 90 dias.

**Conexões concorrentes:** são as estatísticas com base em conexões simultâneas; quantas conexões estão ativas em um mesmo período de tempo. Estas conexões referem-se ao banco de dados.

**Espera por conexão:** estatísticas com base no tempo de espera por uma conexão. Quanto tempo o banco de dados leva para atender a solicitação de uma abertura de conexão.

As opções **"Conexões concorrentes"** e **"Espera por conexão"** são auxiliadores para o DBA verificar sobre o Banco de Dados e se referem ao **Sankhya Om**, ou seja, não analisam outras aplicações que estejam utilizando também a mesma base de dados.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abarelat%C3%B3riodediagn%C3%B3stico)

#### Sub-aba Parâmetros de Performance

Nesta sub-aba são listados os principais parâmetros que possuem influência no desempenho do sistema; possuem um sinalizador para verificar se estão ligados, desligados ou ainda a forma que foram configurados não seja aconselhável.

![Imagem 20: Nesta sub-aba são listados os principais parâmetros que possuem influência no desempenho do sistema; possuem um…](https://ajuda.sankhya.com.br/hc/article_attachments/360103033253)

**Importante:** em base de dados SQL Server, existe os parâmetros ALLOW\_SNAPSHOT\_ISOLATION e READ\_COMMITED\_SNAPSHOT; com ambos ativados, será notada uma mudança no comportamento do banco de dados com relação a lock, de modo a obter um melhor desempenho no sistema. Caso um dos dois parâmetros esteja desligados, seu status será apresentado como **Não Recomendado**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abarelat%C3%B3riodediagn%C3%B3stico) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Add-ons Instalados

Por meio dessa aba, será possível realizar a desinstalação de add-on's quando necessário.

![Imagem 21: Por meio dessa aba, será possível realizar a desinstalação de add-on's quando necessário.](https://ajuda.sankhya.com.br/hc/article_attachments/18395757546519)

Os add-on's instalados são exibidos na aba e quando um ou mais estiverem selecionados, ao clicar no botão ![Imagem 22: Os add-on's instalados são exibidos na aba e quando um ou mais estiverem selecionados, ao clicar no botão "Desinstalar"…](https://ajuda.sankhya.com.br/hc/article_attachments/18395757549975) **"Desinstalar"** será apresentado o pop-up **"Desinstalar add-on"** para confirmar a exclusão.

**Observação:** lembre-se que não é possível desinstalar add-on's baixados pelo diretório do servidor.

Então, após a exclusão, ao pesquisar pelo add-on deletado e clicar neste, o sistema irá exibir o pop-up **"Detalhes do Pacote"** que irá apresentar os dados do add-on excluído anteriormente para, caso queira, ser instalado novamente.

Além disso, tem-se também o botão ![Imagem 23: Além disso, tem-se também o botão "Ver add-on no Place" , em que, ao clicar neste ocorrerá o direcionamento para o…](https://ajuda.sankhya.com.br/hc/article_attachments/18395757558295) **"Ver add-on no Place"**, em que, ao clicar neste ocorrerá o direcionamento para o add-on no [Sankhya Place](https://ajuda.sankhya.com.br/hc/pt-br/articles/4422517129623).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Extensões Instaladas

Extensões são aplicações web que podem utilizar o framework do sistema e são incorporadas por ele de maneira transparente. Este recurso permite que terceiros, mediante aquisição de chave de desenvolvimento, possam desenvolver rotinas para o sistema. Através desta aba, é possível visualizar as extensões que se encontram instaladas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Eventos Programáveis

Ao utilizar esta aba, é possível controlar eventos programáveis considerando as entidades do sistema; estes eventos são mecanismos que podem ser programados para executar ações em Java ou Stored Procedure atuando como regra de negócio para lançamentos nas respectivas entidades (telas nativas ou adicionais).

Assim, é possível realizar as configurações dos eventos:

- Antes de inserir um registro (Before Insert);
- Após inserir um registro (After Insert);
- Antes de remover um registro (Before Delete);
- Depois de remover um registro (After Delete);
- Antes de atualizar um registro (Before Update);
- Depois de atualizar um registro (After Update);
- Antes de finalizar uma transação (Before Commit).

Por meio destas configurações é possível mensurar os valores que serão apresentados no banco de dados.

![Imagem 24: Por meio destas configurações é possível mensurar os valores que serão apresentados no banco de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/360100869014)

No lado superior esquerdo, realize a configuração do botão **"ligar/desligar"** considerando o seguinte:

| ![Imagem 25: No lado superior esquerdo, realize a configuração do botão "ligar/desligar" considerando o seguinte:](https://ajuda.sankhya.com.br/hc/article_attachments/42315398799767) | Ao clicar neste botão, será possível visualizar os status dos eventos programáveis em massa. |
| --- | --- |
| ![Imagem 26: Ao clicar neste botão, será possível visualizar os status dos eventos programáveis em massa.](https://ajuda.sankhya.com.br/hc/article_attachments/42315398800535) | Quando acionado este botão, o sistema desabilitará provisoriamente o serviço utilizado, habilitando-o novamente ao reiniciar o servidor. |

![Imagem 27: Quando acionado este botão, o sistema desabilitará provisoriamente o serviço utilizado, habilitando-o novamente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/23781531810455)

As colunas destacadas na imagem acima possuem as seguintes funcionalidades:

**Ativo:** utilizando esta opção, é possível ligar/desligar um evento específico. Assim, é necessário considerar que as configurações originais dos status dos eventos serão reabilitadas ao reiniciar o servidor.

**Descrição:** através desta opção, registre o nome do evento.

**Instância:** por meio desta opção, insira o nome da instância a qual o evento está vinculado.

**Filtro de telas:** esta opção permite analisar os ID's das telas relacionados aos eventos, sendo necessário separá-los por vírgula ao proceder com sua inserção; dessa maneira, considere:

1. Quando o evento estiver configurado para ser executado nas telas registradas, deverá seguir o padrão abaixo:

```
br.com.sankhya.menu.adicional.Finanlote
```

2. Quando o evento estiver configurado para não ser executado nas telas registradas, deverá constar o caractere (!), conforme abaixo:

```
!br.com.sankhya.menu.adicional.Finanlote
```

**Tipo:** ao utilizar esta opção, insira o tipo do evento, a rotina de banco de dados (Stored Procedure) ou a ação (Java).

![Imagem 28: Acesse também as informações contidas nas telas Dicionário de Dados e Construtor de Telas .](https://ajuda.sankhya.com.br/hc/article_attachments/16023294536983) Acesse também as informações contidas nas telas [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) e [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas).

**Observação:** ao informar o valor "0" (zero) no parâmetro **"Tamanho batchUpdateSize p/ Evento Programável-BATSIZEEVTPROG"**, os registros serão inseridos um de cada vez, permitindo dessa forma, que seja identificado o campo que esta causando erro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Licença

Serão apresentados nesta aba todos os dados relacionados à licença do sistema. Caso haja conexão com o SAS, a aba apresentará os dados do licenciado (código e nome), as empresas registradas (CNPJ's liberados), as empresas que estão com problemas de CNPJ e suas respectivas datas de bloqueio (caso exista) e a lista de produtos, módulos e opcionais licenciados agrupados por grupo e data de expiração.

![Imagem 29: Serão apresentados nesta aba todos os dados relacionados à licença do sistema. Caso haja conexão com o SAS, a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002029181)

Independente da existência ou não da conexão com o SAS, a aba Licença irá informar o IP, a porta do SAS configurado e o status da conexão, **"Conectado"** ou **"Desconectado"**.

Os dados somente serão apresentados se o sistema possuir uma conexão ativa com o SAS. Se a conexão não estiver estabelecida, os dados não serão exibidos e a aba somente fornecerá o status da conexão com o SAS como Desconectado.

Desde Janeiro de 2017 o sistema trabalha com a Licença Online. A Licença Online é útil pois permite que todos os produtos, módulos e opcionais sejam definidos de forma online sem a necessidade de substituição da licença. Além disso, a renovação da licença que anteriormente ocorria de 3 a 6 meses, não será mais necessária, ou seja, não é mais necessário que a empresa entre em contato com a equipe de suporte da Sankhya para geração da licença de uso.

A utilização da Licença Online se da por meio da observância a três passos:

- **SAS 3**

A versão do SAS 3, possui como pré-requisito o acesso a internet; o servidor onde o SAS será instalado, deve acessar a internet e deve possuir acesso irrestrito às url's <https://grupo.sankhya.com.br> e <https://contgrupo.sankhya.com.br>, ou seja, nenhum Firewall ou outra limitação do servidor, pode bloquear o acesso a estas url's.

O instalador do SAS 3 pode ser baixado por meio do acesso ao site [downloads.sankhya.com.br](https://ajuda.sankhya.com.br/hc/pt-br/articles/downloads.sankhya.com.br), onde tem-se acesso ao manual do SAS e ao instalador correspondente ao sistema operacional utilizado.

- **Atualização do sistema**

Uma vez instalado o SAS, realize a atualização do sistema da maneira convencional como já é realizada, ou seja, por meio do acesso ao site [downloads.sankhya.com.br](https://ajuda.sankhya.com.br/hc/pt-br/articles/downloads.sankhya.com.br) ou através do WPM.

É importante mencionar que, o **Sankhya Om** para ser compatível com o SAS 3, deve estar na versão 3.16 ou superior; o SAS deve ser instalado primeiramente, em seguida o sistema.

- **Informar a chave de cliente**

Depois de atualizar o SAS e o **Sankhya Om**, é necessário informar a chave. Para realização deste procedimento, acesse o Sankhya Place (<https://place.sankhya.com.br>), opção Portal do Cliente, opção Chave de Cliente; será apresentado um campo com este mesmo nome contendo a chave gerada; em seguida, por meio do botão localizado à frente do referido campo, copie a chave para a área de transferência do computador.

Feito isso, no **Sankhya Om**, acesse esta tela, Administração do Servidor, aba Licença e, no campo Chave do Cliente, cole a chave obtida. Ao clicar em **"Aplicar"**, é possível usar o sistema normalmente.

**Importante:** a seguir, tem alguns possíveis erros do SAS, bem como seus significados e suas soluções:

| **Mensagem apresentada** | **Significado** | **Solução** |
| --- | --- | --- |
| Não foi possível conectar ao servidor de acessos (SAS), isso pode limitar telas e funcionalidades. Por favor, comunique o administrador do sistema para serem verificados os parâmetros e configurações de acesso. | O parâmetro **"IP do servidor de acessos - IPSERVACESS"** encontra-se com o IP que não tem o SAS ou o SAS não está inicializado. | Verificar se o parâmetro IPSERVACESS encontra-se configurado da forma correta ou se o serviço SAS está em execução. |
| **LU0101**: falha na validação da licença de uso do sistema. Algumas telas e recursos do sistema podem ficar indisponíveis daqui a X dias e Y horas. Entre em contato com sua unidade Sankhya para evitar a indisponibilidade do sistema! | Significa que o cliente encontra-se inadimplente, mas continua dentro do período de carência. | Orientar que o cliente entre em contato com a unidade Sankhya para evitar o bloqueio das telas e recursos |
| **LU0102**: falha na validação da licença de uso do sistema. Algumas telas e recursos do sistema estão indisponíveis no momento. Para mais informações, entre em contato com sua unidade Sankhya! | O cliente encontra-se inadimplente e o período de carência se esgotou. | Solicitar que o cliente entre em contato com a unidade Sankhya para que a pendência seja negociada e as telas e recursos sejam desbloqueados. |
| **LU0103**: o servidor de acesso (SAS) não possui uma "Chave de cliente" ou a chave informada é inválida!  É necessário informar esta chave para que a licença seja validada.  A chave deve ser inserida na tela Administrador do Servidor, aba Licença.  Para obter a chave: Acesse [http://place.sankhya.com.br](http://place.sankhya.com.br;);  Efetue login;  Clique na opção **"Chave de Cliente"**. | Através desta mensagem indica-se que o sistema não possui a chave de cliente informada. | Orientar que o cliente acesse o Portal do Cliente no Sankhya Place, acesse a opção de chave de cliente, copie-a e, depois, acesse a Administração do Servidor, aba Licença e cole a chave copiada. |
| **LU0104**: a licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação.  Por favor, comunique o administrador do sistema para ser verificada a conexão do servidor (SAS) com a internet e possíveis bloqueios nos endereços de acesso.  Permanecendo a falha na conexão, algumas telas e recursos do sistema poderão ficar indisponíveis daqui a X horas e Y minutos. | O SAS não conseguiu conexão com o SankhyaHub e o cliente tem X horas e Y minutos para resolver, caso contrário, as telas e recursos ficarão indisponíveis para utilização. | Verificar se o servidor em que o SAS encontra-se instalado possui a conexão com a internet liberada e acesso às duas URLs seguintes:   - <https://grupo.sankhya.com.br> - <https://contgrupo.sankhya.com.br> |
| **LU0106**: a versão do sistema é superior à versão liberada na licença de uso! | A versão do **Sankhya Om** que o cliente atualizou é superior à versão permitida para sua atualização. | Encaminhar o cliente para o Departamento Financeiro da Sankhya, para poder ser explicado o motivo da limitação da versão. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

#### Critérios para consumo de licenças

Para o uso de produtos do sistema, é necessário possuir licenças para utilizá-las. Referente à licença do produto **"30616 - Editor de Dashboard"**, com o uso apenas desta, será possível lançar um DashBoard, além de conseguir visualizá-los depois de lançados, porém utilizando apenas uma licença, sendo esta a do Produto 30616 - Editor de Dashboard.

Caso tenha apenas a licença do produto **"30647 - DashVieWer"**, este poderá somente visualizar os Dashboards que já foram criados, consumindo apenas esta licença.

Se possuir as duas licenças, sendo estas dos produtos 30616 - Editor de Dashboard e 30647 - DashVieWer, ao utilizar a tela [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI) o sistema fará o uso da licença 30616 - Editor de DashBoards; se usar a tela [Construtor de DashBoards](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605574-Construtor-de-Dashboards), o sistema usará a licença 30616 - Editor de Dashboards. Tem-se assim, o exemplo:

Se a pessoa "A" acessar a tela Construtor de Componentes de BI e/ou a tela de Construtor de Dashboards, o sistema utilizará a licença 30616 - Editor de Dashboard, e ainda utilizará a opção **"Adicionar Lançador"**. Quando este Lançador for visualizado, a licença 30647 - DashVieWer que será consumida.

**Nota:** caso possua uma licença para cada produto, a pessoa "A" esteja usando-as e a pessoa "B" tente utilizar uma destas telas, este não conseguirá o acesso, pois estas licenças já estarão em uso por outra pessoa.

#### Aquisições de licença

Caso o usuário seja administrador ou possua permissão para realizar aquisições, nesta tela aparecerá o botão **“Aquisições de licenças”** um microsserviço disponibilizado por uma plataforma de compra e venda de Licenças ou de compra de CNPJ adicional.

![Imagem 30: Para saber mais acesse o artigo Aquisições de licenças .](https://ajuda.sankhya.com.br/hc/article_attachments/16023294536983) Para saber mais acesse o artigo [Aquisições de licenças](https://ajuda.sankhya.com.br/hc/pt-br/articles/16805141839511-Aquisi%C3%A7%C3%A3o-de-licen%C3%A7as-).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Avançado

Nesta aba é possível alterar o tempo de timeout tanto do jape session quanto do tempo de transação do jboss. O tempo de transação do jboss será o valor informado no campo timeout + 30 segundos o tempo de sessão do jape será o tempo informado no campo timeout.

Caso o campo timeout esteja com o valor **"-1"**, significa que o timeout não sofreu alterações e segue seu comportamento normal. Se o servidor estiver configurado com o atributo de VM jape.session.timeout, será feito um MAX entre este e o tempo de timeout definido. O Jape.session.timeout por default é configurado com **"5 minutos"**.

Se for feita a tentativa de informar um timeout menor que o setado no jape.session.timeout, será apresentada uma mensagem de erro.

![Imagem 31: Se for feita a tentativa de informar um timeout menor que o setado no jape.session.timeout , será apresentada uma…](https://ajuda.sankhya.com.br/hc/article_attachments/360103033393)

1. O campo **"Valor"** tem o número -1 como valor inicial. Se esse campo estiver preenchido com -1 significa que o tempo de timeout ainda não foi alterado.
2. **Timeout menor que o padrão:** Quando é informado um tempo menor que o tempo do atributo **"jape.session.timeout"**, que nesse caso é 180000 ms = 3 min, o sistema apresenta a seguinte mensagem:

**"Tempo mínimo para sessão nesse servidor é de 3mins"**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Aba Autorização de Acesso

Nesta aba, são realizadas as configurações da Agenda do Google.

![Imagem 32: Nesta aba, são realizadas as configurações da Agenda do Google .](https://ajuda.sankhya.com.br/hc/article_attachments/1500002029241)

As devidas informações e orientações para utilização desta aba encontram-se descritas na mesma.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

### Configurações de Segurança

A fim de defendê-lo contra ataques de força bruta em tentativas de login no sistema, a Sankhya desenvolveu parâmetros contra esses tipos de ameaças.

Estão disponíveis links referenciais mais detalhados sobre as funcionalidades e o valor dos parâmetros. Os parâmetros deverão seguir as especificações dentro destes. A seguir, eles habilitarão o início da proteção dos headers via HTTP:

**sankhyaw.httpsecurity.enabled=true**

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options>

sw.xframe.options="SAMEORIGIN"

<https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP> 
<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>

**sw.csp.options="default-src 'self'"**

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection
sw.x.xss.protection="1; mode=block"

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie> 
sw.set.cookie="HttpOnly"
sw.set.cookie.path="; HttpOnly"

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options>

**sw.content.type.options=nosniff**

Portanto, existem os parâmetros:

- **login.security.active:** esse parâmetro irá ativar o protocolo de segurança de tentativa de ataque de força bruta. Todos os demais parâmetros que serão informados a seguir, serão efetivos apenas se este estiver ligado. O valor dele é false mas, para ativá-lo, acrescente-o no servidor como true; desta forma, tem-se -Dlogin.security.active=true.
- **login.security.header:** será utilizado na definição do header usado pela aquisição a fim de recuperar o IP de origem. Seu valor padrão é **"X-Forwarded-For"**. Se as informações requeridas aqui não forem recuperadas, o sistema procurará o endereço de IP do cliente ou do ultimo proxy em cabeçalhos mais comuns.
- **login.security.time.attempt:** nesse parâmetro define-se o tempo máximo de minutos que a requisição poderá tentar na verificação para bloqueio, visando que um contador de tempo é utilizado. A partir do momento que a penalidade aplicada for igual ou maior que o valor aqui informado, a requisição para aquele determinado IP será bloqueada. Destaca-se ainda que seu valor padrão é de 10 minutos.
- **login.security.time.penalty:** este parâmetro será utilizado para a definição do tempo máximo entre a última e a nova requisição. As requisições de ataque de força bruta são praticamente simultâneas ou extremamente rápidas, além disso, para esses ataques, serão utilizados um dicionário de senhas e um software. O valor padrão deste é de 1 segundo.

**Importante:** este valor poderá ser alterado, mas é importante que permaneça com o valor padrão para que não ocorra um falso positivo ao tentar logar no sistema.

- **login.security.time.unblock:** aqui, será definido o tempo em que a requisição ficará bloqueada. A partir do momento em que houver o bloqueio desta, o valor aqui definido será fundamental para que esta requisição/IP possa ser retirado da lista de bloqueio. O seu valor padrão será de 60 minutos.

Para a utilização dos parâmetros descritos acima, se atente a alguns pontos:

- Após alteração de algum destes, reinicie o servidor;
- Caso informe o parâmetro e não atribua nada a ele, ele será definido com um nome padrão;
- O bloqueio não ocorrerá em mobile;
- O bloqueio ocorrerá por endereço de IP, ou seja, caso utilize outro valor de endereço, é possível fazer a tentativa de login novamente.
- Não existe uma tela para que um desbloqueio seja efetuado, uma vez que um endereço de IP é bloqueado, ele só será desbloqueado quando o tempo de desbloqueio definido terminar ou quando o servidor for reiniciado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16023294536983) Acesse também:

[Cache do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048212114)
