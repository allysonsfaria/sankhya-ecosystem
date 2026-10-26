---
id: "360044612274"
titulo: "Formação de Carga"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-10T01:05:05Z"
rotulos: ["AJUDA DO SKW", "manual", "Ordem de Carga", "WMS", "Parceiro", "AGRAREASEPPROD", "APRVAMOFORCARGA", "Formação de Carga", "MODNOTACN48", "br.com.sankhya.mgecom.cad.formacaocarga", "Formação de Carga manual", "Transporte", "Filtros", "USENDENTREGA", "CALCPESOCUMUOC", "Ferramenta de Formação de Cargas", "Mapa Marcadores", "Logística"]
---

# Formação de Carga

```
 Módulo: Comercial > Rotinas > Ordem de Carga
```

---

**Versão 4.35**: Otimização da tela de Formação de Carga com a inclusão do filtro rápido de **'Situação'** e da coluna **'Situação OC'** na grade de resultados.

---

Depois de criada a **"Ordem de Carga"**, você utilizará esta rotina para selecionar as notas que farão parte da Carga, que foi criada para realizar a entrega da mercadoria.

Assim, trataremos neste artigo sobre os seguintes tópicos:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#paineldefiltros)                                                     [Como formar uma Carga?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#comoformarumacarga?)

[Resumo por Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#resumoporordemdecarga)                             [Totalizadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#totalizadores)   

[Botão Mapa na Formação de Cargas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#bot%C3%A3omapanaforma%C3%A7%C3%A3odecargas)                [Funcionamento - Mapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#funcionamentomapa)

[Botão Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#bot%C3%A3oordemdecarga)                                         [Botão Sequência de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#bot%C3%A3osequ%C3%AAnciadecarga)   

[Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#bot%C3%A3ooutrasop%C3%A7%C3%B5es)                                            [Botão Expedição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#Bot%C3%A3oExpedi%C3%A7%C3%A3o)

[Parâmetros que influenciam nessa rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#par%C3%A2metrosqueinfluenciamnessarotina)

---

### Painel de filtros

Esta tela apresenta várias opções de filtros rápidos para apresentação das notas, que poderão ser incluídas na formação da carga, tais como: **"Período de Negociação"**, **"Período de Validade"**, data de **"Início da O.C"**, **"Tipo de Movimento"**, **"Empresa"**, **"Transportadora"**, **"Tipo de Operação"**, **"Região"**, **"Cidade"**, **"Vendedor", "Situação"** e **"Perfil"**, serão usados como opção de filtros rápidos. Além disso, você pode alimentar a grade buscando os dados através da **"Rota"** a ser utilizada.

**Nota:** O filtro **Situação** permite que o usuário filtre os pedidos e notas de acordo com o status atual da Ordem de Carga (OC) vinculada, facilitando a localização de documentos que estejam em estágios específicos do processo logístico.

**Observação:** No campo Tipo de Movimento, temos as seguintes opções:

- Pedido de Venda;
- Venda;
- Pedido de Compra;
- Compra;
- Transferência;
- Pedido de Requisição;
- Requisição;
- Devolução de Venda;
- Devolução de Compra.

Você pode também optar por **"Exibir pedidos não confirmados"** ou **"Exibir somente pedidos pendentes"**.

Formulados os filtros desejados, clique em **"Aplicar"**; assim o sistema irá carregar, na grade superior à direita da tela, todos os Pedidos/Notas que poderão ser incluídos na Formação da Carga.

**Nota:** Existem algumas informações adicionais para as quais o usuário da formação de carga precisa estar alerta. Quando houver alguma carga para o parceiro cujo campo, **"Logística"**, ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), aba [Endereço de Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereodeentrega)), a linha do pedido ficará na cor **vermelha** e as informações adicionais deste campo estarão disponíveis para visualização do usuário, através do campo Logística, nesta rotina.

Após aplicar os filtros, a grade de resultados ao lado direito será carregada. A coluna **"Qtd. Prod. Distintos"** apresentará a soma da quantidade de produtos da nota (que forem distintos) dentro da mesma Formação de Carga.

Além das colunas de agrupamento, a grade de resultados conta com a coluna '**Situação OC'**. Esta coluna exibe o status em tempo real da Ordem de Carga associada a cada nota ou pedido, permitindo ao gestor visualizar rapidamente o andamento e a situação operacional (ex: Aberta, Fechada, Em Processo) de cada documento listado.

Com o filtro de **'Situação'** e a coluna **'Situação OC'**, a filtragem e a visualização do andamento das OCs tornam-se muito mais eficientes, permitindo uma gestão direta sem a necessidade de alternar entre telas para verificar o status operacional.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Como formar uma Carga?

Selecionadas as notas que farão parte da carga, através dos botões ![clip3043](https://ajuda.sankhya.com.br/hc/article_attachments/360061942793) e ![clip3044](https://ajuda.sankhya.com.br/hc/article_attachments/360061942813) localizados no alto da tela, você realiza a validação dos dados da formação da carga, ou desiste da formação iniciada, respectivamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Painel Resumo por Ordem de Carga

O painel Resumo por Ordem de Carga permiti avaliar se a quantidade de volume pode ser acomodada no veículo e também se, pela quantidade de entregas, o motorista conseguirá cumprir o roteiro naquele período.

![Imagem 3: O painel Resumo por Ordem de Carga permiti avaliar se a quantidade de volume pode ser acomodada no veículo e também se,…](https://ajuda.sankhya.com.br/hc/article_attachments/28687550307991)

![Imagem 4: Dica: com o parâmetro "Calcula Peso Cumulativo na OC? - CALCPESOCUMUOC" habilitado, conforme os Pedidos/Notas são…](https://ajuda.sankhya.com.br/hc/article_attachments/16608249401367) **Dica:** com o parâmetro **"Calcula Peso Cumulativo na OC? - CALCPESOCUMUOC"** habilitado, conforme os Pedidos/Notas são vinculados a uma Ordem de Carga, os valores apresentados neste painel são recalculadas. Assim, é possível visualizar os valores atualizados durante a vinculação. 

Através deste painel, você poderá verificar as seguintes informações:

**Cód. Empresa:** Código da empresa da [Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713) vinculada aos Pedidos e/ou Notas selecionados na grade superior.

**Nome Fantasia:** Nome fantasia da empresa da Ordem de Carga vinculada aos Pedidos/Notas selecionados na grade superior.

**Ordem Carga:** Número da Ordem de Carga que foi vinculada à Empresa das Notas e/ou Pedidos selecionados na grade. Caso você queira visualizar as OC's de outras empresas, utilize as opções disponíveis no botão [Ordem de carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#bot%C3%A3oordemdecarga).

**Qtd. Parc. Dest:** Totaliza o número de parceiros destinatários distintos (usando o **"Cód. Parceiro"** quando não preenchido) da Empresa/Ordens de carga selecionadas na grade.

**Peso Máx:** É o peso máximo informado no cadastro da Ordem de Carga, aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#h_01ECQYS6QH937X57WSMH9GSH58), campo **"Peso Máximo"**.

**Peso:** Será o **"Peso Bruto"** do cadastro do produto multiplicado pela quantidade negociada do item.

**Dif. Peso:** Será a diferença entre o Peso Máximo e o Peso.

**M3 Máx.:** É o Metro Cúbico Máximo informado no cadastro da Ordem de Carga, aba Propriedades, campo**"Metro Cúbico Máximo"**.

**M3:** Tem-se aqui, o Metro Cúbico presente na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), aba [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), campo **"Metro Cúbico"**. O M3 se refere ao volume a entregar de cada pedido/nota. Esta informação é obtida somando-se o volume disponível dos itens do pedido/nota. Para se obter o volume disponível, é feita a proporcionalização do volume total do item pela quantidade disponível para entrega, ou seja, quantidade negociada menos a quantidade cortada subtraindo-se a quantidade já faturada/devolvida.

**Dif. M3:** Será a diferença entre o Metro Cúbico Máximo e o Metro Cúbico.

**Qtd. Volumes:** Somatório da quantidade de volumes das Notas/Pedidos escolhidos na grade da empresa/ordens de carga selecionadas para a formação de ordem de carga.

**Valor Frete:** Tem-se aqui, o somatório do Valor do Frete das notas/pedidos selecionados na grade da empresa/ordem de carga para a formação de ordem de carga.

**Qtd. Notas:** Aqui é apresentado, a somatória da quantidade das notas/pedidos selecionadas na grade da empresa/ordem de carga escolhidas para a formação de ordem de carga.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Totalizadores

Na parte inferior da tela, você pode observar os **"Totais"** referentes a alguns dados da tela. Abaixo trataremos sobre cada um deles.

![Imagem 5: Na parte inferior da tela, você pode observar os "Totais" referentes a alguns dados da tela. Abaixo trataremos sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/28687550310167)

**Valor Total:** Temos aqui o somatório da coluna **"Vlr. Nota"** apresentada na grade superior da tela, ou seja, a soma dos valores totais dos pedidos/notas.

**Valor do Frete:** Este totalizador exibe o total do frete relacionado às notas/pedidos envolvidos na carga.

**Peso Bruto:** É apresentado neste totalizador, o somatório da coluna **"Peso bruto dos Itens"** exibida na grade dos pedidos e/ou notas.

**Peso a Entregar:** Aqui temos, a soma da coluna **"Peso a Entregar"** também exibida na grade dos pedidos e/ou notas.

**Metro Cúbico:** Este totalizador apresenta o somatório da coluna **"Metro Cúbico"** apresentada na grade dos pedidos/notas.

**M3 a Entregar:** Temos neste totalizador, a soma da coluna **"M3 a Entregar"** presente na grade onde os pedidos e/ou notas são apresentadas.

**Qtd. Volumes:** Somatório da quantidade de volumes das notas/pedidos selecionadas na grade para a formação de ordem de carga.

**Qtd. Parc. Dest.:** Totaliza o número de parceiros destinatários distintos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Botão Mapa na Formação de Cargas

Através do botão ![Imagem 6: Através do botão "Mapa" localizado no lado superior direito da tela, temos um recurso visual para realizar a formação…](https://ajuda.sankhya.com.br/hc/article_attachments/28687559498007) **"Mapa"** localizado no lado superior direito da tela, temos um recurso visual para realizar a formação de carga. Isso é possível devido à integração do Sankhya-Om com o recurso de mapas disponibilizado pelo Google.

Algumas recomendações devem ser seguidas para que se tenha um melhor desempenho desta opção. Primeiramente, é extremamente realizar o devido cadastro dos componentes que formam os endereços:

- [País](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600894);
- [Estado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294);
- [Região](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074);
- [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913);
- [Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602274-Endere%C3%A7os).

Também é recomendado que seja feito o devido preenchimento do endereço do cliente ( Tela cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), abas [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo) ou **"Endereço de entrega"**) informando, além dos componentes citados acima, o **"CEP"** e o **"Número"**. Ainda no cadastro de Parceiros, você pode observar os campos **"Latitude"** e **"Longitude"** presentes na aba Endereço. Estes campos são preenchidos, quando são utilizados as opções **"Mapas/Endereço"** e **"Mapas/Endereço de entrega"**.

Sendo assim, ao solicitar estas opções, será aberta no Sankhya-Om uma nova janela contendo a mesma ferramenta Mapa da Formação de Carga. Dessa forma, o usuário verificará se o endereço é válido para ser utilizado por essa ferramenta. E ainda, utilizando estas opções, o Sankhya-Om preenche os campos Latitude e Longitude, facilitando o funcionamento do mapa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Funcionamento - Mapa

Para que o botão Mapa seja habilitado, você deve configurar e aplicar o filtro da Formação de Carga. Assim que o resultado da consulta é apresentado na grade, o botão fica habilitado. Dessa forma, ao solicitar esta opção, o sistema lança em uma nova tela o mapa correspondente da integração com a ferramenta da Google.

Similar ao Google Maps é possível ampliar o zoom rolando scroll do mouse para cima, ou reduzir o zoom, fazendo o movimento contrário. Ao clicar e segurar, é possível arrastar a imagem para qualquer direção desejada. Para um melhor entrosamento com essa ferramenta, a Google disponibiliza um suporte com todas as informações necessárias, clique no link para obter mais informações <http://maps.google.com/support/>.

As informações necessárias para se efetuar as configurações de integração do botão Mapa com a ferramenta Google Maps, podem ser visualizadas através do link [Como configurar o botão Mapas Integrado ao Google Maps](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#comoconfigurarobotomapasaogooglemaps).

![clip3052](https://ajuda.sankhya.com.br/hc/article_attachments/360061025594)

Quando o mapa é inicializado, o sistema busca os valores contidos nos campos **"Latitude"** e **"Longitude"** (contidos no endereço) dos parceiros das notas. Sendo que, primeiramente o sistema tenta a busca pelo **"Endereço de Entrega"** (Tela [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), aba [Endereço de Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereodeentrega)). Caso as coordenadas geográficas não sejam encontradas para o endereço de entrega desses parceiros, serão buscadas então no endereço padrão.

**Nota:** A rota é traçada de acordo com a própria sequência de carga contando com uma integração com o Google Maps. Sendo que, é necessário que a empresa verifique o seu contrato com a Google pois essa integração é um recurso pago.

![Imagem 8: Nota: A rota é traçada de acordo com a própria sequência de carga contando com uma integração com o Google Maps . Sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/28687550317207)

Ao acionar o botão Mapa, e sendo aberta a tela **"Mapa p/ Formação de Carga"**, caso seja apresentada a mensagem abaixo, a causa do problema é uma inconsistência no cadastro do Endereço de Entrega, uma vez que a busca é feita pelos servidores do Google.

**"Não foi possível gerar coordenadas do(s) marcadore(s)"**

Por exemplo, o endereço de entrega Rua Engenheiro Diniz não é encontrado nos registros do Google, logo, um parceiro com este endereço em seu cadastro, não será marcado no mapa.

Se o parceiro não possuir Endereço de entrega cadastrado, o sistema buscará o endereço padrão, entretanto se este estiver inconsistente, com erro ou em branco, da mesma forma não será marcado no mapa.

Apesar destes parceiros não estarem marcados, estes serão relacionados no painel esquerdo Ordens de Carga. Este painel pode ser expandido ou retraído na tela. Se expandido, apresenta uma lista das ordens de carga que estão sendo empregadas na formação da carga, separando-as por empresa.

A partir disso, você pode então verificar quais apresentaram o problema e corrigir os endereços nos respectivos cadastros. Do contrário, se o marcador continuar a não aparecer no mapa, a principal funcionalidade da tela será impactada, ou seja, não será possível efetuar, conforme necessidade, eventuais alterações na Ordem de Carga.

Caso sejam filtradas notas já relacionadas à Ordem de Carga, serão apresentados os itens no painel **"Ordens de carga"**. Nestes itens estarão contidos os nomes das Empresas, o número das respectivas Ordens de Carga, além da quantidade de notas relacionadas a cada OC, o Peso total, quantidade total em Metros Cúbicos, e a Previsão de Saída.

Ao acionar o botão **"Ver Notas"**, você pode visualizar as notas relacionadas ao item:

![Imagem 9: Ao acionar o botão "Ver Notas" , você pode visualizar as notas relacionadas ao item:](https://ajuda.sankhya.com.br/hc/article_attachments/28687550318615)

No painel direito é apresentado o mapa inicialmente do Brasil; para visualização de mais detalhes, pode-se dar um zoom pelos botões localizados no canto inferior direito da tela, ou dar um duplo clique com o mouse posicionando na área desejada.

Um **"Marcador"** corresponde ao parceiro é representado pelo símbolo de um pequeno balão ![clip3058](https://ajuda.sankhya.com.br/hc/article_attachments/360061025634) que recebe cores e valores ao longo da configuração. Se nenhum dos endereços for encontrado, ele não será exibido no mapa e não será possível alterar notas daquele parceiro.

Ordem de Carga é uma forma de agrupamento, onde diversas notas são reunidas em uma carga. É possível que se exista um mesmo número de Ordem de Carga em parceiros diferentes, pois este agrupamento é realizado por **"Parceiro"**. É importante ressaltar que os marcadores do mapa representam os Parceiros, e não as notas. Ou seja, as notas são agrupadas por Parceiro.

Por exemplo, tendo o Parceiro X com notas 1001 (sequência 5), 1010 (sequência 2) e 1101 (sequência 7) filtradas na tela de formação de carga, teremos apenas um marcador o representando no mapa e dentro do balão marcador será mostrado um número **"2"**, oriundo da nota 1010 (sequência 2) e que é a menor sequência entre as filtradas.

Estes marcadores são os "pinos" posicionados no mapa representando os locais de origem e destinos (pontos de parada) envolvidos nas Ordens de Carga.

Os marcadores de destino (pontos de parada) são os próprios parceiros das notas, estes poderão ser o contato do parceiro. Para isso é necessário que o campo **"Utiliza endereço de entrega do contato"** presente na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), esteja marcado; desta forma, o endereço indicado no mapa será o cadastrado como contato (para que esta marcação esteja disponível para ser utilizada, é necessário que o parâmetro **"Usa endereço de entrega dos contatos - USENDENTREGA"** esteja ativado).

Clicando em um marcador, uma pequena janela é aberta descrevendo detalhes das notas, informações de origem e informações de pontos de parada.

Os marcadores possuem determinados esquemas de cores, podendo ser brancos, vermelhos ou coloridos.

**1.** Dos marcadores:

- **Branco:** O marcador assume esta coloração, quando o parceiro não possui nenhuma nota com alguma ordem de carga definida. Todas as notas do parceiro estão sem ordem de carga.
- **Vermelho:** Neste caso, o parceiro possui notas com diferentes empresas entre si (Por exemplo, notas A e B com empresas 1 e 10, respectivamente) ou parceiro possui notas com ordens de carga diferentes entre si (Por exemplo, notas A e B, ambas com empresa 1, porém com ordem de carga 10 e 20, respectivamente). É importante ressaltar que, caso o parceiro possua empresas diferentes, obrigatoriamente ele terá ordens de cargas diferentes (Por exemplo, notas A e B, com empresas 1 e 10, respectivamente, e ambas com ordem de carga 30. As ordens de carga das notas A e B são diferentes).
- **Outras cores:** Os marcadores com outras cores, tem-se que o parceiro possui notas com uma mesma ordem de carga definida para todas elas, o marcador terá a cor que aquela ordem de carga possuir no painel Ordens de carga. É importante ressaltar que caso o parceiro possua 3 notas, o marcador do parceiro será da cor do item "Empresa 1 – OC 10", apesar de possuir notas sem ordem de carga definida.

A, com Empresa 1 – OC 10;

B, com Empresa 1 – OC <Sem OC>;

C, com Empresa 1 – OC <Sem OC>.

**2.**Dos itens do painel **"Ordens de carga"**, que representam uma ordem de carga:

Cada cor é gerada randomicamente para cada item. O número dentro do marcador corresponde a menor sequência de carga dentre todas as notas daquele Parceiro.

Quando o mapa é inicializado e nenhuma Ordem de Carga consta no painel, tem-se que nenhum parceiro/nota foi ainda relacionado à sua respectiva Ordem de Carga. Em alguns casos, quando o filtro já traz "Ordens de Cargas" ligadas as notas, assim que o mapa é inicializado, podem ser observadas as Ordens de Carga contidas no painel.

Na parte inferior do painel Ordens de Carga podemos observar a quantidade de notas sem ordem de carga, o peso total, e quantidade total de metros cúbicos.

![Imagem 11: Na parte inferior do painel Ordens de Carga podemos observar a quantidade de notas sem ordem de carga, o peso total, e…](https://ajuda.sankhya.com.br/hc/article_attachments/28687559507607)

Neste quadro, temos o ícone ![clip3061](https://ajuda.sankhya.com.br/hc/article_attachments/360061025654) que acompanha a informação **"Qtd. de notas sem OC definida"**. Ao clicar neste ícone, a opção **"Notas sem ordem de carga definida"** será aberta, na qual será possível visualizar em detalhes as notas sem Ordem de Carga.

**Observação:** Todas as configurações aplicadas a cada marcador sejam preenchendo os campos **"OC"** ou **"Sequência"**, implicarão diretamente na tela Formação de Carga. Ao acessar essa tela, configurar e aplicar o filtro com os mesmos parâmetros utilizados para iniciar o mapa, poderá ser observado que as notas receberam os valores de OC e Sequência, conforme as configurações realizadas no mapa.

**Nota:** Nos casos em que, já foi definido para um parceiro a sua OC e Sequência, ao solicitar outro marcador e esse se referir a um segundo parceiro que possua notas referentes a mesma empresa daquele primeiro parceiro, automaticamente será preenchido o campo OC e o sistema irá sugerir o próximo número para o campo Sequência.

Considere o seguinte exemplo:

São 10 notas referentes a uma única empresa, a qual foi criada a Ordem de Carga código 100, sendo estas notas distribuídas entre 3 parceiros. Ao iniciar o mapa e selecionar o primeiro marcador, que corresponderá ao primeiro parceiro, informe no campo OC o valor 100, e preencha a Sequência com o valor 1. Assim que o segundo marcador for selecionado, o campo OC já possuirá o valor 100 e a Sequência será 2. Assim da mesma forma com o terceiro marcador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Botão Ordem de Carga

Ao selecionar o botão Ordem de Carga, na parte superior da tela, temos as seguintes opções:

**Zerar Ordem de Carga:** Esta opção desmarca o campo Ordem de Carga das notas selecionadas na tela, ou seja, desvincula a(s) nota (s) da Ordem de Carga.

**Atualizar Ordem de Carga de todas:** Através desta opção, será marcado todas as notas com um número de Ordem de Carga que será definido pelo usuário. Para isso, o sistema disponibilizará o pop-up de pesquisa de Ordens de Carga na tela.

**Atualizar Ordem de Carga de todas (Sem Atualizar a Transportadora):** Esta opção terá o mesmo comportamento e finalidade da opção anterior, contudo, quando selecionada, não atualizará a Transportadora.

**Atualizar Ordem de Carga das linhas selecionadas:** Através desta opção, será feita a atualização das Ordens de Cargas apenas para as Notas que tiverem sido selecionadas na grade.

**Atualizar Ordem de Carga das linhas selecionadas (Sem Atualizar a Transportadora):** Esta opção possui o mesmo comportamento e finalidade da opção anterior, porém, quando selecionada, não atualizará a transportadora das notas que foram selecionadas na grade, apenas as Ordens de Carga.

**Zerar OC CN48:** Esta opção zera a informação presente na coluna **"Ordem de carga CN48"** para todas as Ordens de Carga existentes na grade.

**Atualizar Ordem de carga CN48:** Esta opção copia a informação existente na coluna Ordem de carga CN48 da linha selecionada, para todas as ordens de carga existentes na grade.

**Importante:** Para que as duas últimas opções citadas sejam habilitadas, é necessário a configuração do parâmetro **"Modelo padrão para nota de saída de caixas CN48 - MODNOTACN48"**, que deve possuir um valor maior que "0" (zero), porém, este é integrante da rotina "Controle para unitizadores" que se encontra em processo de implementação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Botão Sequência de Carga

Temos as seguintes alternativas ao selecionar o botão Sequência de Carga: 

**Zerar Sequência:** Esta opção desmarca o campo sequência das notas selecionadas na grade.

**Atualizar Sequência:** Através desta opção, será marcado a sequência para a entrega da carga, em ordem crescente.

**Usar Sequência do parceiro:** Por esta opção, você irá registrar para a Ordem de Carga que estiver selecionada, a **"Sequência de Entrega"** de cada parceiro. A sequência de entrega do parceiro pode ser definida a partir do cadastro de regiões do parceiro na tela [Regiões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074), aba [Rota de Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074-Regi%C3%B5es#abarotadeentrega).

**Usar Sequência de entrega dos Vendedores:** Esta opção define a sequência de entregas de acordo com as sequências de cada vendedor, no Cadastro de cidades. Para essa opção será necessária a ativação do parâmetro **"Sequência Entrega por cidade? - SEQENTCID"** e definir a sequência no cadastro de cidades do parceiro na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913) na aba [Rota de Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abarotadeentrega).

**Importante:** A sequência é definida vendedor a vendedor, portanto, para que esta opção seja válida na prática, cada vendedor deve ser responsável por um bairro, ou região próxima.

**Usar Sequência de Entrega do Parceiro Destinatário:** Esta opção quando marcada, a sequência de entrega será preenchida levando em consideração o destinatário informado no painel **"Transporte"** no rodapé do pedido/nota de venda.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Botão Outras Opções

O botão **Outras Opções**, localizado na parte superior da tela de Formação de Carga, agrupa funcionalidades avançadas para organização, cálculos e visualização de dados. Abaixo, detalhamos cada grupo de opções:

#### Reordenar

Estas opções permitem organizar a sequência de atendimento das notas na grade:

- **Reordenar Vendedores:** Organiza a grade com base no cadastro de vendedores.
- **Reordenar Vendedores (Seq. da Carga):** Reordena os vendedores respeitando a sequência já definida para a carga.
- **Reordenar Cidades:** Agrupa as notas por cidade.
- **Reordenar Cidades (Seq. da Carga):** Agrupa por cidade respeitando a sequência de entrega da carga.

#### Usar Transp./Data da O.C.

- **Usar Transportadora da O.C.:** Atualiza as notas selecionadas com a transportadora definida na Ordem de Carga.
- **Usar Data da O.C.:** Alinha a data de saída das notas com a data prevista na Ordem de Carga.

#### Imprimir/Confirmar Notas | Ver Obs.

- **Imprimir/Confirmar notas sem número:** Permite a confirmação em lote de pedidos que ainda não possuem numeração de nota fiscal.
- **Ver observação:** Abre um pop-up para visualização rápida das observações inseridas no cabeçalho da nota/pedido selecionado.

#### Calcular Frete/Valor por Fórmula ou por Rota

Permite realizar o rateio dos custos de frete entre as notas da carga utilizando diferentes critérios:

- **Rateio por Peso:** Distribui o valor proporcionalmente ao peso bruto de cada nota.
- **Rateio por Valor:** Distribui o valor proporcionalmente ao valor total de cada nota.
- **Ganho Logístico:** Realiza o cálculo baseado na eficiência logística configurada no sistema.

#### Visualizar parceiro destinatário? | Endereços

Este grupo gerencia quais informações de endereço serão exibidas nas colunas da grade de resultados:

- **Visualizar parceiro endereço:** Quando marcado, alterna a exibição para os dados do parceiro destinatário.
- **Endereços:** Permite escolher qual tipo de endereço será carregado nas colunas de logradouro da grade. As opções disponíveis são:

  - **Principal:** Endereço padrão do cadastro do parceiro.
  - **Entrega:** Endereço específico para entrega de mercadorias.
  - **Recebimento:** Endereço definido para recebimento de notas/mercadorias.
  - **Contato:** Endereço vinculado ao contato selecionado na nota.
  - **Contato Entrega:** Endereço de entrega específico do contato.

> **Nota:** Para que a visualização dos endereços funcione corretamente, as colunas correspondentes (como Bairro, CEP, Logradouro) devem estar previamente configuradas e visíveis na grade da tela.

![Imagem 13: Nota: Para que a visualização dos endereços funcione corretamente, as colunas correspondentes (como Bairro, CEP,…](https://ajuda.sankhya.com.br/hc/article_attachments/38781422571543)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Botão Expedição

O envio para expedição é realizado por meio das seguintes opções:

**(1)** **Encerrar OC:** selecione esta opção para encerrar a Ordem de Carga manualmente. Para que essa funcionalidade esteja disponível, é necessário ativar o parâmetro **"Encerrar ordem de carga manualmente? - ENCERRAOCMANUAL"**.

(1)** Enviar para expedição:** através desta opção, serão enviadas todas as separações feitas por pedido;

(1)** Enviar para expedição por OC:** esta opção encaminhará todas as separações executadas por produto e por pedido e efetuará o fechamento da Ordem de Carga.

Nas duas opções, ao executar o envio para expedição não possuindo a quantidade total do(s) produto(s) no estoque para atender à necessidade, tem-se a exibição do pop-up **"Detalhes Corte de Pedido"** que possibilita realizar as tratativas de corte necessárias.

![clip7963](https://ajuda.sankhya.com.br/hc/article_attachments/360061025694)

Na parte superior do pop-up, temos dois marcadores que exibem o percentual do corte baseando na quantidade que será cortada na Ordem de Carga e o percentual do corte no valor.

São apresentados alguns botões que desempenham funcionalidades de suma importância para o processo na parte superior do pop-up, são eles:

- **Gerar Pedido:** Será gerado um novo pedido contendo os itens cortados, mantendo o cabeçalho do pedido original e a mesma TOP.
- **Corte Total:** Através deste botão, você pode cortar a quantidade total do produto, enviando apenas os demais produtos do pedido.
- **Retirar da O.C:** Ao acionar este botão, será retirado o pedido em questão da Ordem de Carga.
- **Sem corte:** Não será efetuado nenhum corte no pedido.

Em ambas as grades posteriores, são apresentados os dados que norteiam os pedidos enviados para expedição e seus produtos, detalhando sobre cada um deles dados como a Quantidade disponível no estoque, Percentual de corte no produtos, entre outros.

Ressaltamos que na segunda grade, você pode indicar manualmente a quantidade a ser cortada, bem como, o motivo pelo qual esta sendo realizado o corte. Essas indicações serão realizadas através das colunas **"Qtd. Corte"** e **"Motivo do Corte"**. Sendo que, o motivo do corte deve estar previamente cadastrado na tela [Motivos de Corte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120413).

**Observação:** ao utilizar a opção Enviar para expedição em um Pedido de Transferência com uma Ordem de Carga vinculada, e a TOP utilizada na operação estiver com a marcação **"Separação em Balcão"** selecionada, o sistema exibirá a seguinte mensagem:

**"Pedido/Nota de Venda Balcão não pode estar com a Ordem de Carga preenchida. Verifique a nota/Pedido nro único: xxx."**

**Nota:** quando o endereço de picking for configurado em unidade maior do que a padrão, se a quantidade negociada no Pedido/OC não for múltipla da unidade do estoque, ao tentar enviar o pedido para expedição o sistema apresentará a mensagem abaixo:

**"Produto: X armazenado no endereço Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade.**

**O Envio não foi concluído para não fracionar o Estoque.**
**Pedido: Z, seq: null**

**Verifique a configuração de endereços.**

**Pickings disponíveis:**

**Endereço: XX**
**Estoque: YY**

**Pulmões Disponíveis:**

**Pegas registradas:**

**Código: WMS\_E00770"**

**Observação:** no envio da Ordem de Carga, caso um produto esteja sem vínculo com um endereço de picking, o sistema apresentará a imagem abaixo:

**"O Produto X não possui endereço de Picking configurado. Verifique com o Gerente do WMS**
**Pedido: Y**

**O produto deve estar vinculado em um endereço do Tipo: Picking e que 'Permite Expedição'. Esse cadastro é feito na Rotina:**

**WMS >> Cadastros >> Endereço de Armazenamento**

**Código: WMS\_E00770"**

Caso mais de um produto não tenha a configuração, a mensagem apresentará todos os produtos, pedido e sequência do produto no Pedido de Venda/Nota.

(1)** Análise de envio da Expedição**

Através dessa opção, será apresentada a tela **"Análise de Envio de Expedição"** que permite validar as configurações e parametrizações que impactam no envio de pedido de venda para expedição do [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602114-WMS).

![Imagem 15: Através dessa opção, será apresentada a tela "Análise de Envio de Expedição" que permite validar as configurações e…](https://ajuda.sankhya.com.br/hc/article_attachments/28687717835799)

Assim, inicialmente informe a **"Ordem de Carga"** e/ou **"Pedido/Nota"**. Sendo que, se for informado somente a Ordem de Carga, serão exibidos todos os pedidos relacionados a essa ordem. Caso seja informado apenas Pedido/Nota serão validados os itens associados a essa nota. Em seguida, clique no botão ![Imagem 16: Assim, inicialmente informe a "Ordem de Carga" e/ou "Pedido/Nota" . Sendo que, se for informado somente a Ordem de…](https://ajuda.sankhya.com.br/hc/article_attachments/28730432318615) **"Gerar Análise"**.

Na grade superior será exibido o **"Resultado da Análise"**, destacando os itens que contenham os erros de configuração, cadastro e parâmetros que possam impedir o envio para a expedição. As informações serão exibidas nas seguintes colunas:

- Produto;
- Descrição Produto;
- Qtd. Negociada;
- Controle;
- Referência;
- Unidade - unidade negociada no pedido;
- Situação da Análise - detalhamento do problema identificado;
- Solução - orientação para correção do problema;
- Rotina da Solução - caminho da rotina onde deverá ser realizada a correção.

Na grade inferior, denominada **"Notas/Pedidos"**, são apresentados os dados dos pedidos relacionados aos itens com erros. Essas informações serão exibidas nas colunas:

- Nro. Único;
- Nro. Nota;
- Empresa;
- Nome Fantasia;
- Ordem de carga;
- Cod. Veículo;
- Região;
- Nome do Parceiro;
- Cód. Parceiro transportadora;
- Parceiro.

Após revisar os resultados, clique em **"Concluir"** para retornar a tela Formação de Carga.

#### Divergências e Soluções mapeadas na tela de Análise de Expedição

Confira a seguir as principais divergências que podem ser identificadas na tela de Análise de envio da Expedição suas respectivas soluções e as rotinas necessárias para realizar os ajustes:

![Imagem 17: Confira a seguir as principais divergências que podem ser identificadas na tela de Análise de envio da Expedição suas…](https://ajuda.sankhya.com.br/hc/article_attachments/28730997330839)

(3)** Produto sem endereço de Picking vinculado**

Quando o produtor for controlado pelo WMS, mas não estiver vinculado a um endereço de picking para expedição, deve-se acessar a tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) e vincular o produto em um endereço que esteja com as marcações **"Picking"** e **"Permite Expedição"** acionadas na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral).

**Nota:**se o parâmetro **"separação no picking sem vínculo do produto- SEPPICKSEMEXP"** estiver ligado, o sistema permitirá o envio para a expedição sem o vínculo com o produto.

(3)** Produto em endereço sem área de separação configurado**

Caso o produto esteja associado a um endereço que não possui uma área de separação vinculada, será necessário realizar o vinculo do endereço a uma área de separação por meio da tela [Área de Separação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o).

(3)** Separação Pulmão sem área de separação configurada**

Se na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), a marcação **"Utiliza separação pulmão"** estiver habilitada, e o produto estiver alocado em um endereço do tipo pulmão sem um local de separação vinculado, será necessário acessar a tela Área de Separação e realizar o vínculo desse endereço a uma área de separação.

(3)** Produto com endereço de Picking ou Pulmão bloqueado e/ou não permite expedição**

Caso o produto esteja em um endereço bloqueado e/ou não permite expedição, será necessário atualizar o cadastro do endereço na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral), habilitando a marcação **"Permite Expedição"**. Além disso, no campo **"Situação do Estoque"**, deve ser selecionada a opção **"Disponível"**.

(3)** Sem configurações de Explosão de Lote**

Quando o produto é controlado por lote, mas não foram realizadas as configurações necessárias para a explosão de lote durante o processo de expedição, deve-se realizar os seguintes ajustes:

- Ative o parâmetro **"Lote automático no envio para o WMS?- LOTEENVIOWMS"**;
- Na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), sub-aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) > [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional), defina o campo **"Controlar Por"** com a opção **"Número do Lote"**.
- Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), habilite a marcação **"Utiliza explosão de lote na separação"**.

(3)** Produto sem fragmentação de lote**

Quando o produto é controlado por lote e possui saldo em estoque, é necessário acionar a marcação **"Fragmenta lote no envio para separação"**, na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abawms) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos).

(3)** Parâmetros de explosão de lote**

Quando o parâmetro **"Lote automático no envio para o WMS?-LOTEENVIOWMS"** estiver ativado na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) e a marcação **"Utiliza explosão de lote na separação"**, localizada na seção **"Expedição de Mercadoria"** da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) em [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), também estiver ativada, o envio para expedição não será permitido. Isso ocorre porque a explosão de lote deve acontecer em momentos distintos.

(3)** Produto está armazenado com Unidade diferente da quantidade negociada (Und. Est. Picking X Und. Venda)**

Quando a unidade informada no pedido de venda não for múltipla da unidade armazenada ou vinculada ao endereço, o envio para expedição será impactado. Por exemplo:

- O produto **"Arroz"** está configurado com a unidade padrão = Unidade.
- Possui uma unidade alternativa configurada = Caixa.
- O endereço de picking vinculado a este produto está configurado com Unidade (Estoque Mín/Máx) = Caixa.

Se a quantidade informada no Pedido de Venda não for múltipla da unidade armazenada (exemplo: Caixa com 30 unidades, enquanto o Pedido de Venda possui 20 unidades), ocorrerá uma inconsistência.

Nesse caso, o produto deve ser enviado utilizando a unidade alternativa configurada ou um valor múltiplo da unidade padrão. A correção pode ser feita por meio da tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento).

(3)** Unidade armazenada não encontrada no Cadastro do Produto**

Esse erro ocorre quando o pedido de venda utiliza a unidade padrão do produto, mas não há uma unidade alternativa configurada para atender ao endereço de armazenamento. Por exemplo:

- O produto **"Arroz"** está configurado com a unidade padrão = Unidade.
- Não possui a unidade alternativa Caixa configurada.
- O endereço de picking vinculado a este produto está configurado com Unidade (Estoque Mín/Máx) = PC.

Desse modo, deve-se revisar as configurações de unidade do produto na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) para garantir a compatibilidade entre o pedido de venda e o endereço de armazenamento.

(3)** O produto possui divergências de entradas/saídas no estoque WMS.**

Essa situação ocorre quando o parâmetro **"Validar entradas e saídas do estoque das tarefas? - WMSVALENTSAIPEN"** está ativado e há tarefas em aberto com pendências de registro de entrada ou saída no estoque.

Assim, realize os ajustes necessários no estoque do produto por meio da tela [Divergências de Estoque WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS).

(3)** Produto Sem Código de Barras Válido**

A ausência de um código de barras cadastrado para o produto não impede o envio para expedição, mas impossibilita a execução da tarefa no coletor de dados.

Para resolver essa situação, cadastre um código de barras em um dos seguintes locais no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos):

- Campo **"Referência"** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral);
- Aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas);
- Aba [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abacdigodebarras).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)

### Parâmetros que influenciam nessa rotina

**Apresentar valores monetários na formação de carga? - APRVAMOFORCARGA:**  por padrão é apresentado ligado. Ao desativá-lo, os valores monetários presentes na grade superior através dos campos **"Vlr. Nota"** e **"Vlr. Frete"**, na grade **"Resumo por Ordem de Carga"**, o campo **"Vlr. Frete"** e no rodapé da tela, os dados **"Valor Total"** e **"Valor do Frete"**, deixarão de serem exibidos.

**Usa endereço de entrega dos contatos - USENDENTREGA:** para se utilizar outros endereços de entrega além do endereço de entrega do parceiro, tem-se o parâmetro USENDENTREGA, que quando habilitado mostrará na aba Endereço da tela de Cadastro de Parceiros o campo **"Utiliza endereço de entrega do contato"**.

Ao lançar um Pedido ou Nota de Venda e informar um Parceiro que esteja com o campo Utiliza endereço de entrega do contato marcado, o sistema irá fazer a validação de modo que seja informado um **"Contato"** com endereço preenchido no Cabeçalho da Nota.

- Se o parceiro possuir um Contato cadastrado, mas o mesmo não estiver com o endereço preenchido, o sistema irá barrar emitindo a seguinte mensagem:

**"Contato não tem endereço preenchido".**

- Se o campo Utiliza endereço de entrega do contato estiver marcado, mas o Parceiro não possuir um Contato cadastrado, o sistema não aceitará o salvamento do Pedido/Nota e emitirá a seguinte mensagem:

**"É obrigatório informar o contato do parceiro para entrega".**

Para que os campos de endereço de contato possam ser utilizados, é necessário informar as variáveis descritas abaixo, no modelo TXT do campo **"Observação"** da NF-e, que é o local onde o endereço do contato será impresso.

- **enderecont:** retorna o endereço do contato;
- **baicont:** retorna o bairro do contato;
- **cidadecont:** retorna a cidade do contato;
- **estadocont:** retorna o estado do contato;
- **cepcont:** retorna o CEP do contato.

Na tela de Formação de Carga, o botão Outras Opções apresenta a opção **"Visualizar endereços/Endereços/Contato"**, que se habilitado, exibirá o endereço do contato das notas (da mesma forma que ocorre para as outras opções deste mesmo menu).

Sendo assim, será impresso na Nota (campo Observação) o endereço de entrega do Contato e na tela de Formação de Carga, você poderá montar as cargas com base no endereço do contato.

**Importante:** Não é permitido alterar o endereço principal na Nota, uma vez que não é legalmente possível, que um Parceiro tenha mais de um endereço. Por isso, o endereço do "Contato" será apresentado nos dados adicionais da Nota.

**Qtd máxima dias sem filtro na Ordem Carga - MAXDIASORDCARGA:** Este parâmetro tem como funcionalidade evitar uma queda/lentidão no desempenho da rotina ao filtrar um curto ou longo período contendo um número excessivo de ordens de carga. Considere o exemplo:

Quando o parâmetro estiver configurado com 30 dias, o usuário poderá filtrar pela data de negociação com até 30 dias retroativos. Caso o resultado da diferença de dias entre a data inicial e final (período) for maior do que 30, será apresentada a seguinte mensagem:

**"Informe um período de até 30 dia(s) para "Data da negociação", ou ainda informe um filtro para "OC"."**

**Calcular frete por Cidade - FRETEPORCID:** quando estiver ligado e o campo **"Ordem de carga"** localizado nesta tela constar um registro diferente de zero, tem-se que será habilitado no botão **"Outras Opções"**, a opção **"Gerar Fretes por Cidade"**. Além disto, se o parâmetro **"Misturar cid. empresa c/ outras cid. na Form.Carga? - FCCIDMIST"** também estiver acionado, ao clicar na opção Gerar Fretes por Cidade, surgirá um pop-up dispondo dos seguintes campos:

- Frete Mínimo (considerando as opções **"Por Nota"**, **"Ordem Carga"** ou **"Por Fórmula"**);
- TOP de Venda de CTRC;
- TOP de Venda de Série A;
- Serviço de Frete;
- Serviço de Taxa de Entrega;
- Tipo de Negociação;
- Valor da Taxa de Entrega.

**Importante:** Para que a opção Gerar Fretes por Cidade com seu respectivo pop-up seja liberado, é necessário que a opção **"Visualizar endereços/Endereços/Principal"** esteja selecionada.

**Utilizar nova estratégia de corte no faturamento? - CONTSLDCORTEFAT:** esse parâmetro foi criado para cenários onde se realiza o corte em itens de um pedido por meio dos Portais. Posteriormente, ao faturar este pedido ocorre a explosão de lote e caso o parâmetro esteja desligado o corte será realizado em cada item daquele produto que sofreu a explosão de lote. Para melhor compreensão, considere o seguinte exemplo:

- O produto CODPROD 1 dispõe de um estoque válido nos lotes A e B, onde o lote A possui quantidade 30 e o lote B possui 70;
- Foi gerado um pedido de venda deste produto, com quantidade igual a 100, mas sem informar o lote;
- No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) foi realizado o corte de 10 produtos;
- Ao faturar este pedido, na nota será apresentada a quantidade final igual a 80, sendo 30 unidades para o lote A e 50 para o lote B, pois em cada uma das linhas do item (lote A e lote B) sofreram o corte de 10, ou seja, o corte foi replicado para cada linha daquele produto na nota.

Assim, para que o corte não seja replicado, ligue o parâmetro CONTSLDCORTEFAT. Dessa forma, o corte ocorrerá em apenas uma linha da nota faturada.

Vale ressaltar que, essa regra ocorre quando se utiliza o WMS e o faturamento é realizado pelo Portal.

Se for utilizado o WMS e o corte for efetuado por meio da tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274) e, ainda, o parâmetro CONTSLDCORTEFAT esteja ligado, o item cortado será enviado para a nota faturada. Desse modo, para que não seja levado em consideração na nota o item cortado, o parâmetro deve estar desligado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga#top)
