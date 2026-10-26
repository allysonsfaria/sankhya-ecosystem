---
id: "360045110153"
titulo: "Impressões nos Portais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:29:50Z"
rotulos: ["AJUDA DO SKW", "AGRUPADANFEBOL", "Configuração", "Impressão", "Relatórios Formatados", "Adicional", "Impressora", "PARÂMETROS PNOMEUSULOGADO E PCODUSULOGADO", "Modelo", "IMPMODCTABAIX", "Impressões nos Portais", "Impressões nos Portais manual", "DIASVENCTFILE", "Portal de Vendas", "Nota", "TOP", "Parâmetros de Impressão", "Impressão de Nota Adicional", "Plugin Java"]
---

# Impressões nos Portais

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311995728023) Módulo: Comercial > Rotinas
```

---

É muito simples realizar impressões nos Portais de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603174-Portal-de-Compras-Atributos-da-Tela), [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela) e [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela). Abaixo, iremos demonstrar:

Através do botão ![Imagem 2: Através do botão " Imprimir" (localizado na grade "Resultado de Seleção" nos Portais e no alto da tela das Centrais )…](https://ajuda.sankhya.com.br/hc/article_attachments/16277612081815) **"Imprimir"** (localizado na grade **"Resultado de Seleção"** nos Portais e no alto da tela das Centrais) temos acesso às seguintes opções de impressão:

- [Imprimir Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#imprimirnota);
- [Imprimir Boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#imprimirboleto);
- [Imprimir Expedição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#imprimirexpedi%C3%A7%C3%A3o);
- [Imprimir Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#imprimirnotaadicional);
- [Desvincular Impressoras Substitutas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#desvincularimpressorassubstitutas);
- [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#relat%C3%B3riosformatados).

Temos outras duas formas de Impressão; para acessar as informações, clique nos links [Impressão de Recibo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#impress%C3%A3oderecibo) e [Impressão em Múltiplas Impressoras de Múltiplos Documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#impress%C3%A3oemm%C3%BAltiplasimpressorasdem%C3%BAltiplosdocumentos).

Quando o parâmetro **"Registrar Impressão de Pedido? - REGIMPPED"**estiver habilitado, o sistema registrará a impressão dos Pedidos de Venda e, a linha do pedido na grade do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), ficará na cor azul. Ao tentar reimprimir algum pedido já impresso anteriormente, o sistema perguntará se você deseja realmente reimprimir os pedidos já impressos; caso escolha **"Sim"**, todos os pedidos que foram selecionados serão impressos, inclusive os que já haviam sido impressos anteriormente. Optando por **"Não"**, o será feita a impressão apenas dos pedidos que não foram impressos e, por fim, caso você escolha **"Cancelar"**, o sistema cancelará a impressão e não imprimirá nada. Quando o parâmetro estiver desligado, o sistema irá agir normalmente, deixando a linha sem cor e não te questionará sobre reimpressões.

O Sankhya Om tem suporte à impressão de notas, utilizando modelo .txt e em modo gráfico. O modelo em modo gráfico deve ser configurado utilizando o iReport.

**Observação:** É feita uma validação nas rotinas de impressão de nota/pedido e envio de nota/pedido por e-mail, para que, ao utilizar modelos do iReport que não contenham o parâmetro NUNOTA, o sistema lance uma mensagem informando que o modelo de impressão está incorreto. Para utilizar um modelo criado através do iReport para impressão de notas/pedidos nos Portais é necessário:

- No select (query) utilizado no modelo, deverá ter o parâmetro $P{NUNOTA}, exemplo:

SELECT CAB.DTNEG AS Data\_Negoc, CAB.NUNOTA AS NroUniNota, ITE.CODPROD AS PRODUTO, ITE.QTDNEG AS QUANTIDADE FROM TGFCAB CAB, TGFITE ITE WHERE CAB.NUNOTA=ITE.NUNOTA AND CAB.NUNOTA = $P{NUNOTA}

**Nota:** Caso o Modelo não atenda à esta opção, será emitida a mensagem:

**"A query do modelo de impressão de notas/pedidos formatados pelo Ireport não usa o parâmetro $P{NUNOTA}. Corrija o modelo e tente novamente. (Modelo do Relatório Formatado = 1)".**

- No Modelo, também deverá ser criado o parâmetro (na opção de Parameters do iReport) com o nome NUNOTA.

**Observação:** Caso o Modelo não atenda a esta opção, será emitida a mensagem:

**"Documento xxxx: Modelo de impressão de notas/pedidos formatados pelo Ireport deve possuir parâmetro com nome NUNOTA do tipo numérico. Corrija o modelo e tente novamente. (Modelo do Relatório Formatado = xx)".**

Toda a impressão realizada nos Portais é feita utilizando um applet Java. Para utilizar o applet, é necessário que esteja instalado um Java Plugin no computador.

Ao acessar o Sankhya Om, o sistema verificará se o plugin para applets Java que está instalado no computador é da versão necessária para o funcionamento, sendo que a versão mínima é a Java Plugin 1.6.0\_15.

Caso o plugin não esteja instalado ou não seja da versão mínima necessária, será exibida uma mensagem alertando sobre o problema e um link para o download do recurso. Ao clicar nesse link, você será redirecionado para o site da Sun, para que seja feito o download do recurso.

Como é uma aplicação web que estará fazendo a impressão, o browser poderá solicitar a permissão de acesso à impressora através de uma janela de alerta:

![Imagem 3: Como é uma aplicação web que estará fazendo a impressão, o browser poderá solicitar a permissão de acesso à impressora…](https://ajuda.sankhya.com.br/hc/article_attachments/5675177030167)

![Imagem 4: Como é uma aplicação web que estará fazendo a impressão, o browser poderá solicitar a permissão de acesso à impressora…](https://ajuda.sankhya.com.br/hc/article_attachments/5675213740055)

Para permitir, basta clicar no botão **"OK"** ou **"Run"** da janela de alerta. Para evitar que essa mensagem seja disparada com frequência, basta selecionar a caixa **"Always allow this applet to access the printer"** ou **"Always trust content from this Publisher"**, antes de clicar em OK ou Run.

**Nota:** Quando ocorrer a mensagem: **"Não foi possível carregar a fonte de dados XML"** ao solicitar impressão de notas\pedidos, significa que o modelo configurado na TOP para impressão, possui um relatório formatado equivalente ao DANFE e o movimento do qual foi solicitado impressão não é NFE.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Imprimir Nota

Por esta opção, será possível imprimir as notas em modelos de .txt. Para imprimir uma ou mais notas em modelo .txt, você deve selecionar as notas e selecionar esta opção. Lembrando que, cada modelo pode ter sua particularidade.

Para utilizar essa funcionalidade, verifique o seguinte:

- Na TOP utilizada na nota, o campo **"Modelo de impressão de nota fiscal"** deve estar informado um modelo de .txt.

Esse modelo de .txt deve estar cadastrado, previamente, na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

**Importante:** o modelo utilizado na TOP, deve ser colocado na pasta do servidor de aplicação do Sankhya Om. Isso deverá ser feito manualmente por você.

Você pode verificar o caminho que está configurado, através do parâmetro **"Path dos modelos de impressão/e-mail (MGE Web) - SERVDIRMOD"**. O caminho está indicado no campo **"Texto"**. Você deve salvar os modelos de .txt na pasta informada nesse parâmetro. Observe um exemplo de caminho para a configuração deste parâmetro: /home/mgeweb/modelos/. Neste exemplo, os modelos estão dentro da pasta modelos.

![Imagem 5: Você pode verificar o caminho que está configurado, através do parâmetro "Path dos modelos de impressão/e-mail (MGE…](https://ajuda.sankhya.com.br/hc/article_attachments/360086068854)

É possível fazer impressões de notas obedecendo à ordem da tela de seleção. Para isso, configure o parâmetro **"Respeitar a ordem da grade em selec. várias Notas?’  - MULTSELORD"** que, uma vez habilitado, fará com que as notas sejam impressas de acordo com sua ordenação/apresentação na grade.

Temos um exemplo: As notas de número 5487, 6587, 5481 e 44 não estavam ordenadas por número de nota na grade, e estavam sendo apresentadas conforme a sequência informada. Ao solicitar a impressão das mesmas desta forma, o sistema obedecerá à sequência que está na grade, e a impressão ocorrerá na mesma ordem (5487, 6587, 5481 e 44).

Se o parâmetro MULTSELORD estiver desligado, as notas serão impressas sempre obedecendo a sequência número de nota e não a sua apresentação na grade.

Observe um exemplo com o parâmetro desligado: Se você solicitar a impressão das mesmas notas do exemplo anterior (5487, 6587, 5481 e 44), as mesmas serão impressas obedecendo ao número da nota na forma crescente, ou seja, primeiro será impresso a nota de número 44, depois a 5481, a 5487 e, por último a 6587, mesmo que as mesmas não estejam ordenadas por número da nota em forma crescente na seleção de notas.

**Observação:** para que as notas sejam impressas conforme ordenação da grade, o parâmetro **"Imprimir DANFE e depois boletos? - IMPDANFEBOL"** deve estar desligado, pois este quando ligado tem prioridade sobre o parâmetro MULTSELORD.

O parâmetro MULTSELORD vale só para o botão ![Imagem 6: O parâmetro MULTSELORD vale só para o botão "Imprimir" . Na rotina de faturar, mesmo que a TOP esteja configurada para…](https://ajuda.sankhya.com.br/hc/article_attachments/16277612081815) **"Imprimir"**. Na rotina de faturar, mesmo que a TOP esteja configurada para imprimir após o faturamento, o sistema seguirá a ordem do número único.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Imprimir Boleto

O Boleto é um Tipo de Título, um documento que pode ou não ser emitido pelo sistema no faturamento de uma Nota, como forma de pagamento ou recebimento. Você deverá ficar atento, pois, não é possível emitir boletos com data de vencimento anterior à sua emissão ou com Tipo de Negociação à vista.

O normal para impressão de boletos, é a existência de impressoras dedicadas à esta funcionalidade. O sistema imprimirá o **"Boleto"** para a **"Conta"** cadastrada no financeiro da nota ou do lançamento financeiro, baseando-se no modelo informado nesta Conta.

Para saber mais sobre as configurações para impressão de boletos, acesse [Impressão de Boletos nos Portais e Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599634-Impress%C3%A3o-de-boletos-nas-centrais-Compras-Vendas-Mov-Int-).

A impressão de boletos poderá ser realizada também, através da tela [Impressão de Boletos (gráfico)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-).

Relacionada à impressão de notas e boletos, temos o parâmetro **"Imprimir DANFE e boleto agrupados? - AGRUPADANFEBOL"** que, quando habilitado, faz com que o sistema agrupe o DANFE e o Boleto (se existirem), no momento da impressão, de acordo com cada nota. Com o parâmetro desabilitado, o sistema imprimirá todos os boletos e, em seguida, todos os DANFE's.

**Observação:** Esse parâmetro possui essa funcionalidade quando for utilizado o faturamento direto do sistema.

**Nota:** À medida que as impressões de boletos e notas vão sendo realizadas, arquivos de anexos de mensagens vão sendo gerados e armazenados internamente no sistema; estes arquivos são desnecessários a partir de um certo momento para o sistema, e consomem espaço significativo em disco. No parâmetro **"Dias p/ vencimento de arquivos temporários - DIASVENCTFILE"**, informe o tempo que o arquivo ficará armazenado internamente. Após este período, ele será excluído para não ocupar espaço desnecessariamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Imprimir Expedição

As notas de expedição são utilizadas para controle interno de estoque e separação do material vendido, normalmente é um espelho da Nota Fiscal.

Esta opção encontra-se disponível em:

**1)** Na seleção de Pedidos/Notas/Devolução nos Portais, pela opção **"Imprimir Expedição"**:

![Imagem 7: 1) Na seleção de Pedidos/Notas/Devolução nos Portais , pela opção " Imprimir Expedição" :](https://ajuda.sankhya.com.br/hc/article_attachments/360086072494)

**2)** Nas Centrais de Compras | Vendas | Mov. Internas, a opção Imprimir Expedição:

![Imagem 8: 2) Nas Centrais de Compras | Vendas | Mov. Internas , a opção Imprimir Expedição :](https://ajuda.sankhya.com.br/hc/article_attachments/360086072634)

Para configuração da impressão da expedição, é necessário:

- Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo), seção **"Expedição"**:

![Imagem 9: Na tela Preferências da Empresa , aba Estoque/Preço , seção "Expedição" :](https://ajuda.sankhya.com.br/hc/article_attachments/360087268373)

Informar o caminho da impressora no campo **"Impressora"**, ou seja, onde será impresso a expedição.

O **"Modelo"** deve ser previamente configurado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-). Para impressão de expedição, o modelo configurado pode ser arquivos com extensão em .txt ou relatório formatado.

Informe qual é o tipo de impressora no campo **"Tipo de Imp."**.

Observações: 

- Se o parâmetro "Pede senha p/imprimir Expedição p/Pedidos - EXPEDSENHA" estiver habilitado, o sistema solicitará usuário e senha para efetuar a impressão da expedição no tipo de movimento que for solicitado impressão.
- Se o parâmetro **"Imprimir expedição sem confirmar a nota? - IMPEXPSEMCONF"** for habilitado, o sistema permitirá a impressão de expedição para pedidos/notas/devoluções, sem estar confirmada. Se desligado, o sistema emite a mensagem:

**"Documento xxxx: Para imprimir expedição, confirme  a notas antes de imprimir".**

**Importante:** para os lançamentos de nota de compra que possuem a marcação **"Exige Conferência de Impostos"** no [Cadastro de Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) realizada, e for solicitada a impressão de expedição e esta conferência não for feita, o sistema emitirá uma mensagem avisando-o.

Na Central de Compras teremos a mensagem:

**"Documento X: Esta Nota exige conferência de Impostos pela TOP, mas eles não foram digitados ou a conferência não está Ok."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Imprimir Nota Adicional

O Sankhya Om dispõe, nos Portais de Compra, Vendas e Movimentações Internas, da opção **"Imprimir Nota Adicional"**.

A Nota Adicional é uma possibilidade que você tem de imprimir informações complementares em uma determinada nota, caso a empresa precise de controles adicionais. Pode ser uma nota adicional referente ao cupom fiscal, ou uma nota fiscal mesmo, tipo nota de transporte de mercadorias, ordem de separação ou um espelho da nota.

Esta opção encontra-se disponível em:

**1)** Na Seleção de Pedidos/Notas/Devolução nos Portais, pela opção Imprimir Nota Adicional.

**2)** Na Central de Compras | Vendas | Mov. Internas, opção Imprimir Nota Adicional.

Para configuração da impressão da Nota Adicional, é necessário configurar as telas descritas abaixo e o parâmetro **"Nota Adicional por Empresa?’ - NOTAADICEMP"**; se este parâmetro estiver habilitado, disponibilizará nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Estoque/Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquenotaadicional), as opções para configurar modelo e impressora para notas adicionais. O sistema passará a enxergar essa nova opção ao usar a opção Imprimir Nota Adicional, através do botão de Imprimir na Central - Compras | Vendas | Mov. Internas e Portais. Caso não seja habilitado, o sistema considerará a empresa 1 e buscará as informações através da tela [Modelo e Impressora Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597534-Modelo-e-Impressora-Nota-Adicional).

Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso):

- Se a marcação **"Imprimir Nota Adicional"**for selecionada, os dados da nota serão impressos em outra impressora e, para imprimir nos Portais, você deve selecionar o botão ![Imagem 10: Se a marcação "Imprimir Nota Adicional" for selecionada, os dados da nota serão impressos em outra impressora e, para…](https://ajuda.sankhya.com.br/hc/article_attachments/16277612081815) **"Imprimir"**, opção Imprimir Nota Adicional. As configurações no [Modelo e Impressora Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597534-Modelo-e-Impressora-Nota-Adicional) devem estar corretamente preenchidas e a marcação **"Numeração Automática"** nas Preferências da Nota Adicional tem que estar realizada.
- Se a marcação **"Imprimir nota adicional antes de confirmada?"** estiver selecionada, será impressa a nota adicional da nota selecionada que estiver não confirmada.

**Observações:**

Ao tentar imprimir uma nota adicional, as seguintes condições serão conferidas:

- Se você tem acesso à impressão na tela da central;
- Se o você é gerente do estoque;
- Se a marcação Imprimir nota adicional antes de confirmada? do Tipo de Operação  estiver realizada e a nota não estiver confirmada, será emitida a mensagem: **"Para imprimir nota Adicional, confirme a nota antes de imprimir."**

**Nota:** é possível imprimir nota adicional para mais de uma nota ao mesmo tempo, bastando, para isto, selecionar mais de uma na grade **"Resultado da Seleção"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Desvincular Impressoras Substitutas

Esta opção, desfaz a vinculação existente entre impressora e a impressora cadastrada no modelo de impressão.

**Observação:** ao realizar a impressão, o sistema realizará uma série de validações. Caso ocorra algum problema, o sistema exibirá uma mensagem através da janela **"Avisos"**.

Se ao enviar uma nova impressão, seja esta de notas ou boletos, e o pop-up para selecionar a impressora não for aberto, significa que, certamente, a última impressão foi feita efetuando-se a marcação **"Salvar Seleção?"**, o que impede a escolha de uma nova impressora. Neste caso, selecione a opção Desvincular Impressoras Substitutas que, assim, a impressora poderá ser novamente escolhida.

A opção **"Desvincular impressoras"** é apresentada também no menu de contexto:

![Imagem 11: A opção "Desvincular impressoras" é apresentada também no menu de contexto:](https://ajuda.sankhya.com.br/hc/article_attachments/360086200474)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Relatórios Formatados

Nos Portais e na Centrais - Compras | Vendas | Mov. Internas, no botão de impressão, a opção **"Relatórios Formatados"** mostrará os relatórios formatados vinculados à instância CentralNotas.

**Nota:** Os relatórios formatados só irão aparecer, caso a expressão definida no vínculo seja satisfeita.

Acesse como definir esse vínculo no help da tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025240174-Relat%C3%B3rios-Formatados).

Acesse como enviar notas/pedidos por e-mail, clicando no link [Conhecendo o Sankhya Om/Envio de Relatórios por Email](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238014-Conhecendo-o-Sankhya-W).

Acesse também: Relatórios Formatados/Recursos e Componentes/[Conhecendo o Sankhya Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238014-Conhecendo-o-Sankhya-W).  

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Impressão de Recibo

O recibo será impresso na confirmação da baixa, de acordo com a configuração dos parâmetros abaixo:

Através do parâmetro **"Imprimir Modelo da Conta na Hora da Baixa? - IMPMODCTABAIX"**, você poderá escolher se o sistema irá ou não emitir mensagem de confirmação para impressão de recibo:

- Se ligado, com configuração para tipo Inteiro, e valor maior ou igual a 1, emitirá mensagem questionando se você deseja ou não imprimir o recibo;
- Se ligado, com configuração para tipo Inteiro, e com o valor zero ou vazio, a impressão do recibo será automática;
- Se desligado, o sistema não emitirá o recibo.

Para que você consiga imprimir o recibo, é necessário configurar o parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"** e, na tela de [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boletas/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), configurar o caminho da impressora a ser utilizada e o modelo do recibo.

Para imprimir o recibo de um título pago com vários títulos, o modelo que o sistema utiliza e a impressora, são cadastrados na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Duplicata](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaduplicata).

**Observação:** Você pode escolher se a impressora a ser utilizada será ou não a padrão do Windows. Para escolher a impressora padrão do Windows, bastará preencher o caminho da impressora com a palavra **"PADRAO"**. Além disto, será possível direcionar a impressão de qualquer modelo .txt para um arquivo que deseja imprimir, bastando definir um caminho e arquivo no campo de impressora, através da tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).

**Nota:** No procedimento de **"baixa do financeiro"**, você pode realizar a impressão de modelos (Relatórios Formatados) apenas em formatos .txt ou HTML.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)

## Impressão em Múltiplas Impressoras de Múltiplos Documentos

Quando utilizado um modelo .txt para impressão de pedidos/notas/devoluções, o Sankhya Om conta com as tags:

- CAB GRUPO, TOT GRUPO, OUTRA IMPRESSORA e OUTRO MODELO.

É possível realizar agrupamentos no .txt, similar aos agrupamentos do formatador de relatórios. Para isto, é necessário criar uma sessão, delimitada por **\*\*\* INICIO CAB GRUPO \*\*\*** e

**\*\*\* FIM CAB GRUPO \*\*\***, estando disponível, também, uma sessão para rodapé, delimitada por **\*\*\* INICIO TOT GRUPO \*\*\*** e **\*\*\* FIM TOT GRUPO \*\*\***.

**\*\*\* INICIO CAB GRUPO \*\*\***

**\*\*\* FIM CAB GRUPO \*\*\***

**\*\*\* INICIO TOT GRUPO \*\*\***

**\*\*\* FIM TOT GRUPO \*\*\***

Exemplos:

\*\*\* INICIO TOT GRUPO \*\*\*

...................................................................

Documento: &numnot  Ini.Sep.: &datsis &horasis   Data: &datmov  

Cliente.: &nomcli  Ven.: copy(&apelid,1,13)

Separador: copy(&obser1,1,10)        Total Itens: &gcontad           Setor:   copy(&vloc01,1,2)

Vlr. Tot: &gvlrtot

\*\*\* FIM TOT GRUPO \*\*\*

\*\*\* INICIO CAB GRUPO \*\*\*

Existem algumas variáveis que são utilizadas para estes:

- &gqtdneg: Quantidade de Negociação
- &gqtdent: Quantidade de Entrega
- &gqtd: Quantidade de Negociação-Quantidade de Entrega
- &gvlrtot: Valor Total
- &gvlrtotdesc: (VLRTOT) – VLRDESC.
- &gvlrliq: Valor líquido do agrupamento.
- &gvlripi: IPI do agrupamento
- &gcontad: Contador

Há também a funcionalidade de indicar outro modelo de nota a ser impresso, viabilizando que mais relatórios possam ser feitos durante a impressão da nota. As diretivas para isto são:

- **\*\*\* OUTRO MODELO \*\*\* nome\_do\_arquivo**
- **\*\*\* OUTRA IMPRESSORA \*\*\* nome\_da\_impressora**

Se este último não for informado, será usada a mesma impressora. Se no primeiro for informado um nome repetido no encadeamento de modelos, o computador travará.

Exemplo:

\*\*\* OUTRO MODELO \*\*\* \\192.168.23.129\modelos\Exp\_06bema.txt

\*\*\* OUTRA IMPRESSORA \*\*\* \\192.168.23.129\BS5

**Importante:**

- O Sankhya Om não utiliza caminhos virtuais para ler os modelos, ele verificará qual o nome do .txt do caminho indicado e buscará o mesmo no diretório configurado no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**.
- Os documentos anexos na OS não são templates, por isso, acima foram mostrados exemplos de uso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110153-Impress%C3%B5es-nos-Portais#top)
