---
id: "360044600574"
titulo: "Programação da TV Corporativa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600574-Programa%C3%A7%C3%A3o-da-TV-Corporativa"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-07T15:34:55Z"
rotulos: ["manual", "Configuração", "Componentes de BI", "Dashboards", "Feed", "Feed RSS", "Gadget", "HTML5", "javascript", "página externa", "página interna", "Programação da TV Corporativa", "RSS", "Sankhya-W TV Corporativa", "script", "slides", "SmartTV", "Tipo de slide", "TV Corporativa Sankhya", "URL", "URL da Página", "Usuários", "Youtube", "Controle de Acessos", "onload", "onShowing", "tag body", "tag head", "br.com.sankhya.mge.cfg.tvcorporativa", "Programação da TV Corporativa manual", "Indicadores", "BI", "Gestão Eficiente da TV Corporativa", "TV Corporativa", "Módulo"]
---

# Programação da TV Corporativa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310742253207) Módulo: Configurações > Avançado
```

---

A mobilidade da informação nos dias de hoje ultrapassou diversas fronteiras, inclusive a da disponibilidade. O SankhyaOm TV Corporativa surgiu para atender essa necessidade. Com ele, você conseguirá levar a informação onde seus colaboradores ou clientes estão indo direto ao ponto.

A TV Corporativa é totalmente integrada com os Componentes de BI, permitindo que o você mostre em diversos pontos de sua empresa, indicadores importantes, que facilitará o alcance de grandes resultados, aprimorando sua gestão. Além disso, com a TV Corporativa a empresa conseguirá apresentar indicadores externos ao sistema, como páginas da internet e agregadores de notícias.

Ou seja, este produto possibilitará a execução de alguns Dashboards em forma de slides e páginas externas ao sistema, desde que estas páginas externas estejam disponíveis ao servidor de aplicações.

![Imagem 2: Ou seja, este produto possibilitará a execução de alguns Dashboards em forma de slides e páginas externas ao sistema,…](https://ajuda.sankhya.com.br/hc/article_attachments/8577968714519)

Para acessar a TV Corporativa informe o endereço do **"Servidor"**, barra (/) **"mge"**, barra (/) **"tv"**, como por exemplo 192.168.0.248:8080/mge/tv.

Na tela de login serão preenchidos o **"Usuário"** e **"Senha"**, que já devem ter sido configurados no sistema.

A configuração por usuário possibilita acessar esta ferramenta da seguinte forma:

**1º -** Para que em uma mesma empresa possam existir várias TVs espalhadas em locais diferentes e apresentando informações diferentes, de acordo com o local e usuário logado pois, para cada usuário, pode-se configurar um tipo de apresentação de slides.

**2º -** Por questão de segurança, permitindo por exemplo que seja apresentado em uma Matriz dados diferentes dos apresentados na Filial.

Através da divisão de usuários, é possível fazer uma divisão de conteúdo, ou seja, de dados que serão apresentados em cada TV Corporativa.

Ao clicar em **"Entrar"**, o sistema carregará os slides.

#### Página de Abertura

A página pode ser por exemplo uma página externa com informações de um RSS de Notícias:

![Imagem 3: A página pode ser por exemplo uma página externa com informações de um RSS de Notícias:](https://ajuda.sankhya.com.br/hc/article_attachments/8577967751191)

Bem como, uma interna apresentando um Componente de BI, cujos dados foram retirados do sistema.

#### Configurações Necessárias

Abaixo, temos os passos para cadastrar um usuário com acessos para a TV Corporativa:

- No [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), efetue o cadastro do novo usuário e a sua senha de acesso.

#### Aba Programação da TV Corporativa

Ainda no Cadastro de Usuários, esta aba permite configurar os tipos de slides que serão apresentados na TV Corporativa. Vejamos cada configuração:

O **"Tipo de slide"** é utilizado para selecionar o tipo de slide que deseja adicionar. As opções de seleção são:

- Gadget;
- Site;
- RSS;
- Vídeo.

Ao selecionar uma das opções acima, os campos exibidos nesta aba serão apenas os necessários para a configuração da opção selecionada.

**Nota:** para realizar a configuração através da aba Programação da TV Corporativa é necessário ter acesso a esta tela como um todo e, em casos onde isso não é viável, libera-se o acesso apenas à essa tela.

A primeira opção de tipo de slide disponível é o Gadget, que consiste em um Componente de BI, ou seja, esta informação virá da tela [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI). Portanto, bastará informar neste campo o código do componente que se deseja apresentar na TV Corporativa.

**Observação:** é importante que não haja parametrização configurada para o Gadget selecionado, pois o mesmo será exibido em uma TV. Além disto, o Gadget selecionado como slide não poderá ter mais do que um nível, uma vez que se houvessem níveis seria necessária a intervenção de um usuário, o que não ocorrerá na TV.

O **"URL da Página"** é usado para apresentação de um slide que é na verdade uma página externa ao sistema; informe neste campo a URL da página, que será então exibida como slide externo.

Ao informar um Gadget no campo superior, automaticamente o sistema apagará a URL informada neste campo, e vice-versa, pois slides internos são excludentes de slides externos e cada slide deve ser configurado separadamente.

Defina no campo **"Tempo de apresentação (em segundos)"**, quanto tempo o slide ficará em apresentação na TV. Assim que este tempo for esgotado, o sistema passará para o próximo slide de acordo com a ordenação dos mesmos.

**Leitor de RSS:** É possível adicionar um slide do tipo RSS no qual você insere a URL de um feed RSS e o leitor RSS exibirá a última notícia do Feed.

**Vídeo:** Tem-se também um leitor de vídeos do Youtube. Neste tipo de slide, você insere a URL do vídeo e o tempo de apresentação, após isso no momento em que o slide estiver sendo visualizado, o vídeo começará a tocar automaticamente.

Após a adição dos slides, retornando ao modo grade, você poderá alterar a ordem de apresentação através das setas laterais à direita.

![Imagem 4: Após a adição dos slides, retornando ao modo grade, você poderá alterar a ordem de apresentação através das setas…](https://ajuda.sankhya.com.br/hc/article_attachments/8577966708631)

Finalizada a configuração do Usuário e dos Gadgets que serão apresentados, bastará acessar o browser com o endereço do servidor para dar início à apresentação dos mesmos. Mesmo com o player em execução (TV Corporativa em apresentação) será possível alterar a ordem, adicionar ou remover slides nesta aba.

#### Executando a Apresentação dos Slides

Há duas formas possíveis para execução dos slides:

1. Através de uma SmartTV com acesso à internet e que possua um dos seguintes browsers instalados Chrome, Firefox ou Safari. Além disto, a SmartTV deverá ter hardware suficiente para rodar HTML5, sem travar;
2. Por meio de uma TV convencional na qual será conectado um PC (computador), com os mesmos requisitos de browser e hardware apresentados na forma anterior.

**Nota:** a Sankhya recomenda a utilização do Chrome para execução da TV Corporativa, como se trata de HTML5 poderá ocorrer algum tipo de problema de processamento com os outros dois browsers que possuem um desempenho um pouco menor que o Chrome.

Para executar a TV Corporativa, bastará abrir o browser e informar o endereço do servidor.

![Imagem 5: Para executar a TV Corporativa , bastará abrir o browser e informar o endereço do servidor.](https://ajuda.sankhya.com.br/hc/article_attachments/8577955792919)

Para que o browser mostre a página em tela cheira bastará teclar **"F11"**.

Após o primeiro login, será possível a realizar a execução automática, ou seja, sem a necessidade de passar novamente pela tela inicial de login para informar Usuário e Senha. Isso ocorre da seguinte forma:

Realizado o primeiro login, o sistema irá gerar uma URL criptografada que caso seja copiada permitirá um novo acesso sem a necessidade de novo login.

Uma terceira forma de execução possível ao player, será a abertura do browser em modo "full screen" (tela cheia) automaticamente, na informação da URL de acesso. Para isto deve-se:

**No Windows:** Executar o Chrome (browser) e o comando **"- -kiosk"**, seguido da URL criptografada, gerada no primeiro login. Como por exemplo:

C:\Users\USUARIO\AppData\Local\Google\Chrome\Application\chrome.exe –kiosk http://endereco.sankhyaw/mge/tv?s=bGVhbmRybzoxMjMoNTY=

**No Linux:** Bastará acessar o endereço de execução do Chrome (browser) adicionar "%U --kiosk" e em seguida a URL criptografada com usuário e senha de acesso. Como por exemplo:

\usr\bin\chromium-browser %U -- kiosk http://endereco.sankhyaw/mge/tv?s=bGVhbmRybzoxMjMoNTY=

**Observação:** nos dois sistemas operacionais quando o computador estiver conectado à TV, o Sistema Operacional do PC poderá ser configurado para que ao iniciar o browser seja aberto automaticamente no modo **"kiosk"**, com o endereço, usuário e senha da URL criptografada, dispensando assim a intervenção do usuário.

Ao chegar ao final da apresentação o player será novamente carregado de forma automática, sem necessidade de uma nova intervenção na TV ou no PC, apresentando neste momento qualquer alteração que tiver sido feita em relação à apresentação dos slides.

#### Executar Efeito na Apresentação de uma Página

**Nota:** a configuração a seguir, destina-se a usuários técnicos, que são capacitados a criar uma página personalizada na internet.

Quando a TV Corporativa é iniciada, ela carrega automaticamente todos os slides que foram configurados para o usuário informado na URL criptografada, não importando se este slide é um componente de BI ou uma página externa, por isso se houver na apresentação algum slide que possua algum efeito especial, no momento do carregamento da página poderá acontecer de o mesmo não ser apresentado.

Para que slides com efeitos especiais sejam apresentados corretamente, será necessário realizar em sua página na internet (nos fontes de criação) a configuração de um javascript como o descrito no código abaixo.

**1 –** Adicione como atributo tag body do documento o onload=”setupShowingEvent()”, ficará como no código abaixo:

<body onload=”setupShowingEvent()”>

</body>

2 – Dentro da tag head da página adicione o seguinte código:

<head>

 <script type=”text/javascript”>

         function setupShowingEvent(){

                         if ("onhashchange" in window) {

                                 window.onhashchange = function() {

                                         if(window.location.hash && window.location.hash.indexOf("showing") > -1){

                                                 onShowing();

                                         }

                                 }

                         }

                         if(window.location.hash && window.location.hash.indexOf("showing") > -1){

                                 onShowing();

                         }

                 }                        

                 function onShowing(){

                         //Código do que tem que ser executado quando a página for exibida

                 }        

</script>

</head>

**3 –** Dentro da função onShowing() adicione o código que deve ser executado, quando a página for exibida, como:

 function onShowing(){
         window.alet(“Teste”);

 }

Para exibir um alerta de texto na tela.

#### Utilização da TV Corporativa em Android

Após as configurações realizadas no Sankhya Om, para utilização em android, é necessário baixar o aplicativo através do site <http://downloads.sankhya.com.br/>. Deste modo, o sistema abrirá a seguinte tela:

![Imagem 6: Após as configurações realizadas no Sankhya Om , para utilização em android, é necessário baixar o aplicativo através…](https://ajuda.sankhya.com.br/hc/article_attachments/8577965123607)

Endereço (Servidor): Informe o endereço do servidor de aplicações, sempre informando o ip e não o dns. Como por exemplo http://192.168.0.96:8480/mge.

**Usuário:** Usuário configurado no sistema para ser o usuário da TV Corporativa.

**Senha:** Senha do usuário informado no campo Usuário.

**Botão Testar:** Serve para verificar se as informações da configuração conseguem comunicar com o servidor de aplicações.

**Botão Salvar:** Salva as configurações e já começa a carregar as configurações efetuadas da TV Coorporativa.

**Voltar:** Volta ao estado anterior. Se não informada nenhuma configuração, aparece na tela que o servidor não foi encontrado.

Caso as configurações não estejam corretas, o sistema irá alertar por meio de uma mensagem que o usuário e senha são inválidos.

Após a inserção dos dados de configuração serão apresentados os sites, gadgets e vídeos conforme configurado anteriormente no Sankhya Om no menu de TV Coorporativa. Caso seja necessário voltar as configurações ou sair do aplicativo basta ir ao menu de contexto.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600574-Programa%C3%A7%C3%A3o-da-TV-Corporativa#top)
