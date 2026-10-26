---
id: "360044605354"
titulo: "Construtor de Componentes de BI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-30T18:20:01Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Dashboards", "XML", "Parceiros", "Estatísticas", "ORDENARACOES", "Acumular Valores", "Construtor de Componentes de BI", "LIMITLINHASDASH", "Totalizadores", "USADASHANT", "br.com.sankhya.core.cfg.gadgetbuilder", "Construtor de Componentes de BI manual", "BI", "Componentes essenciais para construção de dashboards", "Personalização avançada das visualizações de tabela", "Ferramentas para filtrar e editar dados nos componentes do BI", "JIVA"]
---

# Construtor de Componentes de BI

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311302549527) Módulo: Configurações > Avançado > Construtor de Componentes de BI
```

---

**Importante:** caso a empresa possua o produto **20495 – JIVA–ANÁLISES PARA DASHBOARDS /W (Jiva Om)**, as telas Construtor de Componentes de BI e Configurações > Avançado > Construtor de Dashboards serão disponibilizadas no menu do Jiva Om. Porém, o sistema valida a quantidade total de análises em dashboards personalizados e adquiridos no Jiva Place presentes na licença de uso referentes ao produto mencionado pela empresa, de modo que se esta quantidade for ultrapassada e for feita a tentativa de visualização de um dashboard, será apresentada a seguinte mensagem:

**"A quantidade de licenças disponíveis em sua base não é suficiente para visualização desse dashboard. Por favor, entre em contato com o seu Gerente de Contas para obter mais análises."**

Um comportamento semelhante poderá ser observado, caso seja feita a tentativa de instalação via Jiva Place de dashboards que extrapolem a quantidade de análises adquiridas pela empresa. Será exibido o seguinte alerta:

**"O dashboard não será instalado pois ele extrapola a quantidade de licenças adquiridas. Por favor, entre em contato com o seu Gerente de Contas para obter mais análises."**

**Importante:** se a licença de uso do cliente possuir o visualizador de Dashboards (**20482 - JIVA - DASHBOARD VIEWER/W**), o sistema não irá consumir licenças do Construtor de Componentes de BI (**20495 – JIVA–ANÁLISES PARA DASHBOARDS /W**) para visualização de Dashboards, deste modo, quando esgotam-se as licenças de visualização de Dashboards, não será possível abrir mais nenhuma visualização de Dashboards.

| [Introdução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#introduo) |  | [Design | XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#designxml) |
| --- | --- | --- |
| [Área de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#readetrabalho) |  | [Cartões Inteligentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#cartesinteligentes) |
| [Controles > Valor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controlesvalor) |  | [Controles > Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controlestabela) |
| [Alterando cores das linhas da Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#alterandoseletivamenteascoresdaslinhasemcomponentesdotipotabela) |  | [Controle > Tabela ...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#criandoumaformataocondicionalporclulaemcomponentesdotipotabela) |
| [Controles > Tabela Dinâmica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controlestabeladinmica) |  | [Controles > Geomapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controlesgeomapa) |
| [Controles > HTML5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controleshtml5) |  | [Controles > IReport](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controlesireport) |
| [Gráficos > Linha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficoslinha) |  | [Gráficos > Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosbarras) |
| [Gráficos > Colunas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficoscolunas) |  | [Gráficos > Pizza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficospizza) |
| [Gráficos > Análise de Rentabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosanlisederentabilidade) |  | [Gráficos > Velocímetro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosvelocmetro) |
| [Gráficos > Geográfico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosgeogrfico) |  | [Gráficos > Área](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosrea) |
| [Gráficos > Donut](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosdonut) |  | [Gráficos > Bolha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosbolha) |
| [Gráficos > TreeMap](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficostreemap) |  | [Gráficos > Dispersão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosdisperso) |
| [Gráficos > Radar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosradar) |  | [Gráficos > Funil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosfunil) |
| [Gráficos > Intervalo de Área](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#grficosintervaloderea) |  | [Acumular Valores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#acumularvalores) |
| [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#parmetros) |  | [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#configuraes) |
| [Variáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#variveis) |  | [Argumentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#argumentos) |
| [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos) |  | [Eventos - Controles/Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-controlestabela) |
| [Eventos - Controles/Valor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-controlesvalor) |  | [Quadrante Expressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#quadranteexpresso) |
| [Pré-Visualização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#pr-visualizao) |  | [Impressão/Exportação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#impressoexportao) |
| [Ações nos Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#aesnoscomponentesdebi) |  | [Central de Certificações...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#centraldecertificaesparadashboards) |
| [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#botooutrasopes) |  |  |

## Introdução

O primeiro passo para criação de um **"Dashboard"** será a construção dos "gadgets" (componentes) que farão parte de sua composição. A criação destes componentes será feita por meio desta tela.

Quando a tela é aberta em modo **"Grade"** os componentes que já foram cadastrados serão exibidos.

![EVO01](https://ajuda.sankhya.com.br/hc/article_attachments/360061932153)

#### Painel de Filtros

Localizado no lado esquerdo da tela, teremos o painel com as seguintes funcionalidades:

- O **"Botão de Filtros"** permitirá a criação de filtros personalizados.
- No campo **"Código"** pode-se pesquisar o código dos gadgets criados para o filtro.
- Ao informar um texto no campo **"Título Contendo"**, o sistema fará a busca baseado no texto que foi inserido.
- Da mesma forma como o campo Título Contendo, o campo **"Descrição Contendo"** fará a busca com base na Descrição inserida neste.
- Em **"Categoria"** você poderá filtrar os gadgets criados por meio da categoria atribuída a cada um deles.

Teremos ainda no canto direito da tela, o ícone ![clip8773](https://ajuda.sankhya.com.br/hc/article_attachments/360061932173) que quando acionado, permitirá a visualização e edição da posição dos níveis contidos no dashboard. Sendo que, esta funcionalidade também estará disponível no momento da edição do dashboard.

O primeiro passo para criação de um **"Dashboard"** será a construção dos **"gadgets"** que farão parte de sua composição. A criação de **"gadgets"** é feita através desta tela.

**Nota:** pode-se visualizar mais detalhes sobre a criação de Dashboards por meio do link [Construtor de Dashboards](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605574).

**Importante:** se a licença de uso do cliente possuir o visualizador de Dashboards (**30647 - DASHVIEWER/W**), o sistema não irá consumir licenças do Construtor de Componentes de BI (**30616 - EDITOR DE DASHBOARD/W**) para visualização de Dashboards. Deste modo, quando as licenças de visualização de Dashboards esgotarem não será possível abrir nenhuma visualização de Dashboards.

Acionando-se o sinal de inclusão de um novo componente (gadget), informa-se um **"Título"** para o mesmo. O campo **"Categoria"** serve para que os gadgets sejam agrupados por categoria; é um campo de livre digitação onde pode-se criar a categoria desejada, ou simplesmente pesquisar uma já existente.

**Nota:** não existe um cadastro prévio de Categorias, as mesmas são criadas diretamente neste campo a medida em que são digitadas.

No campo **"Ativo"** podemos ativa e desativar o componente conforme sua marcação.

Em **"Descrição"** o sistema permite que você faça breves comentários sobre o novo gadget de modo que sua identificação fique mais fácil.

![EVO02](https://ajuda.sankhya.com.br/hc/article_attachments/360061009454)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Design | XML

Temos duas formas de montar o gadget; uma pelo **"Design"**, que é um assistente que auxiliará na sua montagem:

![EVO03](https://ajuda.sankhya.com.br/hc/article_attachments/360061932213)

Pelo Design selecionam-se os **"Componentes"** propriamente ditos, sendo estes divididos em **"Controles"** e **"Gráficos"**.

#### Controles

- Valor;
- Tabela;
- Tabela Dinâmica;
- Geomapa.

#### Gráficos

- Linha;
- Barras;
- Colunas;
- Pizza;
- Análise de Rentabilidade;
- Velocímetro;
- Geográfico;
- Área;
- Donut;
- Bolha;
- TreeMap;
- Dispersão
- Intervalo de Área.

A segunda maneira de construção de um componente é por meio do **"XML"** caso você conhecer a sintaxe (por esse motivo, não detalharemos aqui a construção de gadgets por meio de XML).

![EVO04](https://ajuda.sankhya.com.br/hc/article_attachments/360061009474)

Caso o componente seja construído pelo **"Design"**, à medida que é montado, o sistema irá compor o **"XML"**; contudo, caso você conheça a sintaxe, poderá montar o gadget diretamente pelo XML. Este será gravado no banco de dados na tabela **"TSIGDG"**, que possui que possibilitam gravar todas as informações do cabeçalho do Construtor de Componentes de BI, além do campo **"CONFIG"** que irá arquivar todo o conteúdo do XML. 

Hoje no sistema é possível na criação de dashboards utilizar bancos de dados que não é o banco do Sankhya Om como fonte de dados; consideremos para estas situações, bancos de dados externos ao sistema. Para mais informações sobre este procedimento, acesse o link [Banco de Dados - Dashboards no Sankhya-Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733).

**Nota:** quando você comprar uma solução pelo Place e esta for protegida, os botões **"Design"** e **"XML"** ficarão desabilitados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Área de Trabalho

Cada componente que pode ser utilizado é selecionado da mesma maneira; ao selecionar o gadget desejado e arrastá-lo para a **"área de trabalho [principal]"**. Temos como exemplo, a inserção do componente **"Gráfico de Linhas"**:

![EVO05](https://ajuda.sankhya.com.br/hc/article_attachments/360061932253)

Quando inserido, cada componente possui as seguintes ferramentas:

![clip3337](https://ajuda.sankhya.com.br/hc/article_attachments/360061009494) **Alterar tipo:** Esta opção é apresentada apenas para os componentes do tipo "Gráfico" e ao ser acionada tem-se a apresentação de uma pequena tela para seleção do novo componente a ser empregado.

![clip3338](https://ajuda.sankhya.com.br/hc/article_attachments/360061009534) **Mover para cima e Mover para baixo:** Nos casos em que se está realizando uma análise que conte com mais de um componente, através destes botões pode-se posicioná-los para cima ou para baixo, respectivamente, conforme a necessidade da análise.

![clip3339](https://ajuda.sankhya.com.br/hc/article_attachments/360061009554) **Editar:** Esta opção quando acionada, abre a tela própria de edição de cada componente; através dela, realiza-se toda a configuração do gadget. Através de um duplo clique do mouse sobre o componente na área de trabalho, também é aberto o seu modo de edição.

![clip3340](https://ajuda.sankhya.com.br/hc/article_attachments/360061932273) **Remover:** Por meio desta opção você poderá remover um componente que não será utilizado; que quando acionado, o sistema apresentará um questionamento de confirmação do procedimento de exclusão. Quando um componente da área de trabalho for selecionado, ao pressionar a tecla **"Delete"** do teclado,a remoção também será efetuada.

#### Disposição dos componentes

Em casos que há a necessidade de utilização de mais de um gadgets de uma vez para aprimoramento de análise, o sistema contará com uma estrutura que possibilita a construção do layout mais flexível.

O quadro **"Ferramentas"** posicionado no canto superior esquerdo da tela possibilita a divisão (aba **"Dividir"**) na quantidade de colunas desejadas, da área selecionada; esta pode ser a área principal ainda sem nenhum componente inserido, ou a área já preenchida com algum gadget. Notemos na imagem abaixo, que optou-se por uma divisão em quatro colunas, onde a primeiro e a terceira coluna também foram divididas.

Pode-se também por meio da aba **"Inserir"**, acrescentar a quantidade de colunas desejadas e necessárias para a construção do layout.

![EVO06](https://ajuda.sankhya.com.br/hc/article_attachments/360061932293)

No alto do quadro Ferramentas, tem-se as seguintes opções:

![clip3463](https://ajuda.sankhya.com.br/hc/article_attachments/360061932313) **Desfazer a última ação:** Esta opção irá desfazer a última atividade realizada na construção do layout.

![clip3464](https://ajuda.sankhya.com.br/hc/article_attachments/360061932333) **Excluir a coluna selecionada:** Por meio desta, será feita a exclusão da coluna que estiver selecionada.

![clip3465](https://ajuda.sankhya.com.br/hc/article_attachments/360061009594) **Limpar a coluna selecionada:** Diferentemente da opção anterior, esta realiza apenas a limpeza da coluna selecionada; não é feita sua exclusão.

![clip6164](https://ajuda.sankhya.com.br/hc/article_attachments/360061009614) **Mesclar a coluna selecionada:** Este recurso pode ser utilizado nos casos em que incluiu-se alguns componentes no painel principal, e optou-se por manter apenas um componente; ao acionar este botão, os componentes presentes na tela são mesclados ao painel principal, obtendo-se assim somente uma camada de componentes a serem configurados.

![clip6163](https://ajuda.sankhya.com.br/hc/article_attachments/360061932353) **Layout:** Este botão apresenta as opções **"Top-Down"** e **"Personalizado"**; a primeira permite a configuração da direção dos componentes, apenas na vertical; a segunda opção, possibilita que os componentes sejam divididos/posicionados vertical e horizontalmente. Por padrão, a opção Personalizado é apresentada assinalada.

**Importante:** a disposição aqui definida para os componentes será mantida na geração/visualização dos componentes, depois que estes forem devidamente configurados (sequência desta documentação).Trabalhando-se com Dashboards que possuem mais de um nível de navegação, ou seja, clicando-se em um trecho da análise tem-se a abertura de outros níveis, ao utilizar estes botões, será possível retornar para o primeiro nível, retornar ao nível anterior e avançar para o nível seguinte, respectivamente.

![clip6385](https://ajuda.sankhya.com.br/hc/article_attachments/360061932373): Trabalhando-se com Dashboards que possuem mais de um nível de navegação, ou seja, clicando-se em um trecho da análise tem-se a abertura de outros níveis, ao utilizar estes botões, será possível retornar para o primeiro nível, retornar ao nível anterior e avançar para o nível seguinte, respectivamente.

**Observação:** durante a apresentação de um dashboard na tela, caso seu carregamento seja demorado em consequência da grande quantidade de dados, pode-se interromper sua construção através do **"x"** localizado no lado superior esquerdo da tela junto à barra de carregamento.

**Nota:** caso o parâmetro **"Usa dashboard antigo - USADASHANT"** esteja ativado, o quadro **"Ferramentas"** deixará de ser exibido e consequentemente esta forma de visualização dos gadgets não poderá ser utilizada.

![Imagem 19: Não é viável deixar os containers do segundo nível vazios no BI, pois mesmo com relatórios de diferentes tipos além do…](https://ajuda.sankhya.com.br/hc/article_attachments/23392901443351) Não é viável deixar os containers do segundo nível vazios no BI, pois mesmo com relatórios de diferentes tipos além do I-report, o sistema tentará interpretá-los como contendo um gadget, resultando em erros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Cartões Inteligentes

No Construtor de Componentes de BI tem-se a opção **"Cartão Inteligente"** que irá configurar a exibição dos componentes como Cartões Inteligentes. Tem-se que esta opção estará disponível caso a base do usuário esteja atualizada com o Sankhya Om. 

![EVO08](https://ajuda.sankhya.com.br/hc/article_attachments/360061009634)

Para utilizar este recurso, o componente deve atender aos seguintes requisitos:

- Estar ativo;
- Possuir informações;
- Não conter filtros (parâmetros);
- Nenhum de seus níveis possuir mais de um gadget (com exceção dos gadgets do tipo Valor, pois estes não possuem limite de quantidade por nível).

Deste modo, outra opção será habilitada para que o usuário possa configurar qual será o tamanho de exibição do cartão.

![EVO09](https://ajuda.sankhya.com.br/hc/article_attachments/360061932393)

Uma vez configurado, o componente passa a ser exibido na tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) para que o administrador configure quais usuários poderão visualizá-lo na área de trabalho.

![EVO10](https://ajuda.sankhya.com.br/hc/article_attachments/360061932413)

**Observação:** o componente só deixará de ser exibido na tela de Acessos quando for excluído do Construtor de Componentes de BI. Desta forma, você poderá habilitar ou desabilitar o mesmo sem perder as configurações de acesso salvas.

Ao acessar o sistema com o usuário configurado, o cartão será exibido na área de trabalho:

![EVO11](https://ajuda.sankhya.com.br/hc/article_attachments/360061009654)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Controles > Valor

![EVO12](https://ajuda.sankhya.com.br/hc/article_attachments/360061932433)

Acionando-se o botão de **"Edição"** será feito o direcionamento para a seguinte tela:

![EVO13](https://ajuda.sankhya.com.br/hc/article_attachments/360061932453)

A imagem acima mostra a edição de um componente de **"Valor"** que retornará um **"valor pontual"** ou **"texto"** após a renderização.

#### Aba Geral

Na utilização do componente **"Controle/Valor"** pode-se trabalhar com uma barra de ferramentas para formatação de textos, transcrevendo estes em formato HTML. Para utilização desta funcionalidade, efetua-se a **"seleção do texto"** desejado, e aciona-se o botão referente a formatação que será empregada no texto em questão.

Os botões apresentados para utilização, possuem as seguintes funcionalidades:

![clip2112](https://ajuda.sankhya.com.br/hc/article_attachments/360061009674) O texto será adaptado para a exibição em **"Negrito"**;

![clip2113](https://ajuda.sankhya.com.br/hc/article_attachments/360061009694) O texto selecionado, será apresentado no modo **"Sublinhado"**;

![clip2114](https://ajuda.sankhya.com.br/hc/article_attachments/360061009714) O texto será apresentado no modo **"Itálico"**;

![clip2115](https://ajuda.sankhya.com.br/hc/article_attachments/360061932473) Através desta opção, será adicionada uma **"Quebra de linha"** ao texto selecionado;

![clip2116](https://ajuda.sankhya.com.br/hc/article_attachments/360061009734) O texto selecionado, será alinhado à **"Esquerda"**;

![clip2117](https://ajuda.sankhya.com.br/hc/article_attachments/360061009754) Este botão irá alinhar o texto selecionado ao **"Centro"**;

![clip2118](https://ajuda.sankhya.com.br/hc/article_attachments/360061009794) O texto selecionado, será alinhado à **"Direita"**;

![clip2122](https://ajuda.sankhya.com.br/hc/article_attachments/360061009814) Através deste botão, pode-se definir os **"Tipos de Fonte"** que serão utilizados no texto selecionado;

![clip2120](https://ajuda.sankhya.com.br/hc/article_attachments/360061932513) Por este botão, pode-se determinar o **"Tamanho da Fonte"** do texto;

![clip2121](https://ajuda.sankhya.com.br/hc/article_attachments/360061009834) As cores definidas nestas duas caixas, irão determinar a **"Cor da Fonte"** e a **"Cor do Realce"**, respectivamente.

**Nota:** vale ressaltar que para empregar ao texto alguma das formatações mencionadas acima é necessário que primeiramente este texto seja selecionado (através do mouse), e em seguida aciona-se o botão desejado.

Caso um **"Título"** seja informado, este será renderizado como um label. No painel à direita, o sistema disponibilizará todos o **"Parâmetros/Variáveis disponíveis"** para que estes possam ser utilizados no componente.

Estes parâmetros e variáveis poderão ser utilizados tanto no **"Texto"** quanto no **"Título"** do componente. Basta arrastar o parâmetro ou variável para o campo do Título ou do Texto.

Contudo, pode-se digitar diretamente no texto os parâmetros, desde que estes estejam disponíveis para o componente caso contrário o sistema acusará erro.

Além disso, este componente permite por meio de expressões a criação de links que se direcionam para os sites desejados. Para tanto, é necessário atentar-se para alguns detalhes na referida expressão, como por exemplo na criação de um link direcionado para o site www.google.com a expressão ficará da seguinte forma:

```
<a href="http://www.google.com"  target="_blank"> Nome do link</a>
```

**Importante:** na constituição da expressão deve-se sempre utilizar o **target**=**"**\_**blank"** no final do link para que o mesmo funcione de forma correta.

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO14](https://ajuda.sankhya.com.br/hc/article_attachments/360061932533)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Controles > Tabela

![EVO15](https://ajuda.sankhya.com.br/hc/article_attachments/360061009854)

Quando o componente for do tipo **"Tabela"** o painel de "Edição" não apresentará o campo **"Texto"**, apenas o **"Título"**. Contudo, a edição da **"Descrição"** será muito importante neste tipo de componente, pois ela aparecerá no header (cabeçalho) da Tabela, após a renderização.

#### Aba Geral

![EVO16](https://ajuda.sankhya.com.br/hc/article_attachments/360061009874)

No campo **"Entidade"** poderemos definir uma Entidade/Tabela de modo que será possível executar ações vinculadas à estas entidades. Teremos o exemplo, onde informou-se neste campo a entidade **"Parceiro"**, e na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) definiu-se duas ações para ela, denominadas neste exemplo, **"Script"** e **"Lançador"**, como pode-se notar na imagem abaixo:

![EVO17](https://ajuda.sankhya.com.br/hc/article_attachments/360061932553)

No componente gerado tem-se um botão de ações que traz para utilização as duas ações configuradas para a entidade Parceiro:

![EVO18](https://ajuda.sankhya.com.br/hc/article_attachments/360061009894)

Na edição do componente Tabela temos a marcação **"Permite seleção de múltiplas linhas?"** que quando selecionada, faz com que no componente gerado, possa ser selecionado várias linhas da tabela, e ao pressionar a tecla **"Ctrl"** no teclado, você poderá selecionar as linhas de sua preferência pelo clique do mouse.

Ao acionar a marcação **"Utilizar a nova versão da grade"** são disponibilizados novos recursos na grade do componente. Inicialmente, o botão ![clip9834](https://ajuda.sankhya.com.br/hc/article_attachments/360061009914) **"Configuração da Grade"** e o seu pop-up são exibidos em um novo formato:

![EVO19](https://ajuda.sankhya.com.br/hc/article_attachments/360061932593)

Além disso, é disponibilizado o acesso ao **"Menu da Grade"** que propicia uma maior agilidade e conforto na visualização e pesquisa das informações contidas na grade.

![EVO20](https://ajuda.sankhya.com.br/hc/article_attachments/360061009934)

Todas as informações a respeito das funcionalidades contidas no Menu da Grade podem ser acessadas através da opção ![clip9831](https://ajuda.sankhya.com.br/hc/article_attachments/360061932613) **"Iniciar Tour"**.

Na utilização do componente Tabela, ao definir um campo como **"Farol"** na criação de sua expressão, configura-se para que seu retorno seja uma cor, isso fará com que as análises realizadas no dashboard sejam efetuadas com rapidez e proporcionem melhor entendimento dos resultados. Por meio da aba Expressão na configuração deste recurso, pode-se optar por um farol grande **"Farol(G)"** ou farol **"Farol(P)"**:

![EVO21](https://ajuda.sankhya.com.br/hc/article_attachments/360061009954)

Observe um exemplo de configuração de retorno para o campo:

```
SELECT

        CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#86C154' ELSE '#C3C3C3' END AS FAROL,
        CASE WHEN Financeiro.VLRDESDOB < 100 THEN 'RED' ELSE 'GREEN' END AS FAROL2,
        Financeiro.NUFIN,
        Financeiro.VLRDESDOB,
        CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FF0000' ELSE '' END AS FGCOLOR,
        CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FFFF00' ELSE '' END AS BKCOLOR

FROM

        TGFFIN Financeiro
```

Observe o exemplo de um Componente que contêm um campo onde utilizou-se o tipo **"Farol"**:

![EVO22](https://ajuda.sankhya.com.br/hc/article_attachments/360061932633)

Na utilização dos componentes **"Tabela"** e **"Tabela Dinâmica"** (apresentada no tópico abaixo), quando há geração de dados, o título de cada coluna terá a possibilidade de filtragem e/ou ordenação das informações da tabela, e para sua configuração você deve apenas posicionar o mouse sobre a coluna que é desejável empregar para filtro/ordenação; será apresentado o botão ![clip3222](https://ajuda.sankhya.com.br/hc/article_attachments/360061932653), que ao ser acionado, exibirá a seguintes opções:

- Ordenar crescente;
- Ordenar decrescente;
- Remover ordenação;
- Filtrar;
- Remover filtro.

Observe a referida opção em uma tabela construída para exemplificação:

![EVO23](https://ajuda.sankhya.com.br/hc/article_attachments/360061932673)

Na utilização deste componente, tendo-se a tabela gerada, pode-se caso necessário, **"Copiar"** as informações de uma célula ou de uma linha para algum outro documento desejado; pode-se fazê-lo selecionado o trecho a ser copiado com o mouse, e pressionando as teclas **"Ctrl + C"** no teclado, ou mesmo pela opção do botão direito do mouse.

Relacionada à apresentação dos dados na grade tem-se a configuração decorrente do parâmetro **"Limite de linhas nas grades do dashboard - LIMITLINHASDASH"**; informa-se nesta parametrização, a quantidade máxima de linhas a serem apresentadas quando na geração do gadget.

Ao realizar a geração do gadget através do ícone ![clip7346](https://ajuda.sankhya.com.br/hc/article_attachments/360061009974) localizado no canto superior direito da tela, pode-se realizar a exportação de todos os dados gerados pelo componente em questão, independente do limite de linhas definido no parâmetro de chave LIMITLINHASDASH; a quantidade de linhas estabelecidas neste parâmetro, serão exibidas no ícone. Este é um comportamento disponível apenas para gadget's do tipo Tabela. É importante mencionar que este ícone será apresentado, apenas se o parâmetro citado for configurado com algum valor diferente e maior que "0" (zero).

**Aba BIA**

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO24](https://ajuda.sankhya.com.br/hc/article_attachments/360061010014)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

**Alterando seletivamente as cores das linhas em componentes do tipo Tabela**

É possível que o usuário customize sua tabela com cores, podendo assim criar uma interface mais gerencial. Para isso, a expressão SQL (query) do componente tipo Tabela deve retornar duas novas colunas: BKCOLOR, e FGCOLOR. O conteúdo destas colunas são valores hexadecimais, os quais correspondem ao código da cor desejada. A coluna BKCOLOR corresponde a cor do fundo da linha na tabela. Já a coluna FGCOLOR faz referência à cor das letras do texto.

Exemplo:

```
SELECT

 Financeiro.NUFIN,
 Financeiro.VLRDESDOB,
 Financeiro.DHBAIXA,
 Financeiro.CODPARC,
 CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FF0000' ELSE '' END AS FGCOLOR,
 CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FFFF00' ELSE '' END AS BKCOLOR

FROM

 TGFFIN Financeiro
```

Na edição do componente aciona-se o botão **"Editar"** presente na grade **"Expressão"**:

![EVO25](https://ajuda.sankhya.com.br/hc/article_attachments/360061932693)

Será aberta a tela para edição da consulta/expressão:

![EVO26](https://ajuda.sankhya.com.br/hc/article_attachments/360061010074)

**Criando uma Formatação Condicional por célula em componentes do tipo Tabela**

O recurso de ![clip6626](https://ajuda.sankhya.com.br/hc/article_attachments/360061010094) **"Formatação Condicional"** está localizado na extremidade direita da grade **"Expressão"**, este método possibilita que o usuário crie a definição de uma ou mais Regras de formatação, sendo que quando a regra for verdadeira será aplicada na célula respectiva ao campo selecionado. Pode-se personalizar a cor de fundo, o estilo da fonte entre negrito e/ou itálico de células especificas. A referida formatação só está disponível para o componente **"Tabela"**, nos campos do tipo **"Inteiro"**, **"Moeda"**, **"Decimal"**, **"Data"** e **"Data e Hora"**. Ao clicar no recurso será aberto um pop-up para edição da formatação condicional:

![EVO27](https://ajuda.sankhya.com.br/hc/article_attachments/360061010114)

Primeiramente, neste pop-up deve-se selecionar no campo Tipo, o tipo de layout a ser utilizado no assistente; tem-se as opções Formatação ou Escala de Cores; a primeira delas permite a adição e edição de todas as demais regras; já a segunda, é exclusiva para uso de escala de cores.

Tratando sobre o tipo **"Escala de Cores"**, estas podem ser do estilo Bicolor ou Tricolor, ou seja:

- **Bicolor:** Determina-se duas colorações, bem como, duas parametrizações possíveis e correspondentes às cores; trabalha-se com pontos Mínimos e Máximos de modo que estes podem ser do tipo Menor valor, Valor e Percentil, e Maior valor, Valor e Percentil, respectivamente.

Na escala de cores Bicolor, o ponto mínimo não pode ter valor maior do que o máximo se os dois forem do mesmo tipo (percentual ou valor).

- **Tricolor:** Neste estilo de escala, determina-se três parametrizações e suas respectivas colorações; além dos pontos Mínimos e Máximos (que podem ser do tipo Menor valor, Valor e Percentil, e Maior valor, Valor e Percentil, respectivamente), define-se também o ponto Médio e sua correspondente coloração; um ponto Médio pode ser apenas do tipo Valor ou Percentil.

Na escala de cores Tricolor, o ponto mínimo não pode ter valor maior que o médio se os dois forem do mesmo tipo, além disso, o ponto médio não pode ser maior que o máximo seguindo a mesma regra.

**Importante:** não são permitidos valores menores que "0" (zero) e maiores que "100" (cem) no campo Valor se o tipo do ponto for Percentil.

![EVO28](https://ajuda.sankhya.com.br/hc/article_attachments/360061010134)

Definindo-se o Tipo como **"Formatação"**, tem-se as seguintes possibilidades de Regra:

- **Maior (>):** O valor informado for maior que o resultado obtido na consulta;
- **Maior igual (>=):** O valor informado for maior ou igual ao resultado obtido na consulta;
- **Menor (<):** O valor informado for menor que o resultado obtido na consulta;
- **Menor igual (<=):** O valor informado for menor ou igual ao resultado obtido na consulta;
- **Igual (=):** O valor informado for igual ao resultado obtido na consulta;
- **Diferente (<>):** O valor informado for diferente do resultado obtido na consulta;
- **Entre (Between):** Os valores informados estiverem entre o resultado obtido na consulta;
- **Não entre (not Between):** Os valores informados não estiverem entre o resultado obtido na consulta;
- **Vazia (NULL):** Quando não houver valor no resultado obtido na consulta;
- **Não vazia (NOT NULL):** Quando houver valor no resultado obtido na consulta.
- **Fórmula Personalizada:** Esse tipo de formatação permite a criação e aplicação de uma fórmula personalizada em uma célula especifica, com base no valor de outros campos. A referida fórmula só pode utilizar os campos do mesmo componente de tabela em questão, sendo possível a utilização de todos os outros tipos de regras na mesma fórmula, como por exemplo 'CODCR>=100'.

**Ícone:** Esta opção é composta por uma listagem de ícones a serem apresentados juntamente com a regra de formatação condicional; estes ícones tem como objetivo salientar as divergências que podem ocorrer nos resultados, bem como aprimorar a apuração dos mesmos, em casos de grandes volumes de informação.

**Mostrar somente ícone:** Esta marcação se realizada, o texto correspondente ao campo será ocultado e apenas o ícone será exibido. Por padrão, esta marcação não é apresentada assinalada.

![EVO29](https://ajuda.sankhya.com.br/hc/article_attachments/360061010154)

**Observação:** caso já exista uma regra do tipo Escala de Cores não será permitido incluir outras regras de qualquer tipo. Além disso, várias regras do tipo Formatação podem ser adicionadas em um mesmo campo, porém, se ao menos uma for adicionada, a opção de Escala de Cores ficará indisponível.

Os botões apresentados para utilização, possuem as seguintes funcionalidades:

![clip6664](https://ajuda.sankhya.com.br/hc/article_attachments/360061932713) Este botão exibe alguns exemplos de expressão.

![clip6665](https://ajuda.sankhya.com.br/hc/article_attachments/360061932733) Através deste botão, será adicionada a variável que foi selecionada.

![clip6666](https://ajuda.sankhya.com.br/hc/article_attachments/360061010174) Por este botão, pode-se selecionar a variável desejada.

![clip6667](https://ajuda.sankhya.com.br/hc/article_attachments/360061010194) A célula específica será exibida no modo Negrito.

![clip6668](https://ajuda.sankhya.com.br/hc/article_attachments/360061932753) A célula específica será exibida no modo Itálico.

![clip6669](https://ajuda.sankhya.com.br/hc/article_attachments/360061010214) Este botão permite a alteração da cor da fonte.

![clip6670](https://ajuda.sankhya.com.br/hc/article_attachments/360061010234) Através deste botão, pode-se alterar a cor de fundo do texto.

O campo **"Valor"** deverá ser usado como referência para que o sistema verifique se a regra configurada é verdadeira ou falsa. Apresentando-se de acordo com seu tipo, ou seja:

**Inteiro:** Não deve possuir casas decimais.

**Moeda:** Deve apresentar casas decimais.

**Data:** Deve apresentar a máscara de data.

**Nota:** nas regras **"Célula vazia"** e **"Célula não vazia"**, o campo Valor estará inativo.

**Observação:** na criação de várias regras de formatação condicional para o mesmo campo, o sistema irá verificar a ordem de acordo com a grade, caso o sistema verifique que a primeira é verdadeira irá desconsiderar as demais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Controles > Tabela Dinâmica

![EVO30](https://ajuda.sankhya.com.br/hc/article_attachments/360061932773)

Este componente é uma poderosa ferramenta para análise das mais variadas informações. Este pode ser configurado e utilizado da mesma forma que a tabela acima mencionada. Para configurá-la, deve-se editar e inserir uma expressão contendo a query desejada.

Pode-se arrastar os campos da consulta a fim de se criar a visualização padrão. Esta configuração é válida para a primeira vez que o componente for executado. Se for feita alguma alteração, o sistema irá manter o último estado da tabela dinâmica.

Acionando a edição da Tabela Dinâmica, determina-se seu **"Título"**, o **"Tamanho do texto"**, além da forma de **"Visualização padrão"** dos campos que irão compor a tabela. Dentre as configurações pertinentes a forma de visualização padrão, tem-se a marcação **"Sempre usar visualização padrão"** que quando acionada estabelecerá que as últimas alterações (linhas e colunas) efetuadas pelo usuário não serão salvas e assim o gadget será iniciado com a visualização padrão que foi configurada.

Simultaneamente a estas configurações, define-se os **"Parâmetros/variáveis disponíveis"**, bem como, a **"Expressão"** do componente (grades no lado direito da tela)

![EVO31](https://ajuda.sankhya.com.br/hc/article_attachments/360061932793)

Caso seja necessário, na utilização deste componente e a tabela dinâmica gerada, você poderá **"Copiar"** as informações de uma célula ou de uma linha para algum outro documento desejado, para executar essa ação pode-se selecionar o trecho a ser copiado com o mouse, e pressionar as teclas **"Ctrl + C"** no teclado, ou pela opção do botão direito do mouse. 

**Nota:** ao configurar-se um filtro utilizando-se de um dos campos, este ficará na cor **"vermelha"** para que identificar que ele está em uso como filtro.

**Importante:** relacionada à apresentação dos dados na grade tem-se a configuração decorrente do parâmetro **"Limite de linhas nas grades do dashboard - LIMITLINHASDASH"**; informa-se nesta parametrização, a quantidade máxima de linhas a serem apresentadas quando na geração do gadget. Vale salientar que esta configuração influencia apenas os componentes que geram grade (Tabela e Tabela Dinâmica); os demais não são afetados por este parâmetro.

**Observação:** quando um parâmetro vazio for utilizado, os valores na tabela dinâmica serão exibidos em branco ou zerados, dependendo do formato do campo. Desta forma, a configuração realizada no layout não será perdida.

**Nota:** ao realizar uma consulta a descrição desta não poderá conter caracteres, como '**.**', por exemplo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Controles > Geomapa

![EVO32](https://ajuda.sankhya.com.br/hc/article_attachments/360061932813)

Assim como os demais componentes, para início da utilização do Geomapa, basta arrastá-lo para o centro da tela, onde através do ícone ![clip3091](https://ajuda.sankhya.com.br/hc/article_attachments/360061932833) dá-se início a sua configuração.

![EVO33](https://ajuda.sankhya.com.br/hc/article_attachments/360061010254)

Os dados inseridos na seção **"Configurações do mapa"** serão utilizados para centralizar o mapa quando carregado; não sendo informado nenhum pondo de referência, o mapa será centralizado no Brasil. Além disso, por meio do campo **"Raio"** é possível inserir um raio em KM ao redor do ponto central (inserido no campo **"Endereço"**). Deste modo, viabilizando a verificação da volumetria e o grau de proximidade, como por exemplo, de clientes que se encontrem próximos a um endereço informado.

Na seção **"Marcadores"** tem-se a configuração das informações que irão representar os dados retornados pela expressão SQL. Assinalando-se a opção **"Apenas marcar"**, um pino vermelho será a representação de cada aspecto do analisado no mapa. Já a opção **"Marcar com uma bolha"** se refere à representatividade da marcação, ou seja, serão apresentadas bolhas no mapa com diferentes tamanhos e cores, onde quanto maior a bolha, maior a representatividade da marcação.

Vale ressaltar que ao definir um evento de clique através do botão **"Evento"**, e juntamente definir detalhes para o marcador, o evento de clique é redirecionado para um link chamado **"Mais detalhes"**, dentro do balão de informações.

Na última seção **"Detalhe do marcador (opcional)"** pode-se adicionar detalhes ao marcador. Realizando esta configuração, ao clicar- em um marcador será apresentada uma pequena janela contendo as informações definidas em cada campo de detalhe. No campo de Título, define-se um resumo da informação. Pode-se adicionar nesse campo, textos fixos em conjunto com variáveis de níveis, parâmetros de usuário e campos da expressão SQL. Já no campo de Texto, determina-se o restante da informação. A forma de utilizar é a mesma do campo de título, com a diferença que pode-se adicionar tag's HTML.

**Observação:** no gadget Geomapa, visando a manutenção de sua performance são apresentados pelo sistema os primeiros 400 (quatrocentos) marcadores retornados na consulta por visualização.

![EVO34](https://ajuda.sankhya.com.br/hc/article_attachments/360061010274)

**Observação:** quando a query que realiza as buscas dos parâmetros que foram enviados posteriormente ao GEOMAPA possuir campos vazios ou valores nulos, a API do Maps não irá considerar o registro, mesmo que o campo com os valores nulos não estejam sendo utilizados, ou seja, para que a localização seja precisa, é necessário que os campos **"Latitude"** e **"Longitude"** dos Parceiros na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), estejam preenchidos com seus respectivos valores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Controles > HTML5

Para utilização deste componente, pode-se inicialmente seguir os seguintes passos:

- Através das opções **"Download Modelo Simples HTML5"** ou **"Download Modelo Completo HTML5"** (botão Outras Opções...) realiza-se a baixa do modelo desejado;
- Realiza-se a abertura do arquivo baixado, onde tem-se dois modelos no formato XML, correspondentes ao banco de dados da empresa, SqlServer ou Oracle; deve-se abrir o arquivo XML correspondente ao seu banco de dados e copiar o seu conteúdo;
- O conteúdo copiado deve ser colado no espaço apresentado com o acionamento do botão ![clip6383](https://ajuda.sankhya.com.br/hc/article_attachments/360061010294) **"XML"** referente ao componente que está sendo criado; informa-se o Título adequado ao gadget, e a partir disso, o componente começa a possuir um formato definido;
- Feito isso, por meio do botão ![clip6382](https://ajuda.sankhya.com.br/hc/article_attachments/360061010314) **"Upload do Pacote HTML"** realiza-se o total carregamento do pacote inicialmente baixado. Finalizado o upload, será exibida a seguinte mensagem:

**"Pacote HTML5 atualizado com sucesso."**

Vale mencionar que os modelos disponibilizados pelas opções **"Download Modelo Simples HTML5"** e **"Download Modelo Completo HTML5"** são apenas embasamentos para utilização do componente HTML5.

![EVO35](https://ajuda.sankhya.com.br/hc/article_attachments/360061932853)

Da mesma forma que os demais componentes, para início da utilização do HTML5, basta arrastá-lo para o centro da tela, onde através do ícone ![clip3091](https://ajuda.sankhya.com.br/hc/article_attachments/360061932833) dá-se início a sua configuração.

![EVO36](https://ajuda.sankhya.com.br/hc/article_attachments/360061932893)

Na seção **"Configurar Componente HTML5"** tem-se as seguintes informações:

Ponto de Entrada: Neste campo especifica-se o nome completo (com extensão) do arquivo JSP a ser compilado.

Logo à frente do campo Ponto de Entrada tem-se o botão ![clip5927](https://ajuda.sankhya.com.br/hc/article_attachments/360061932913), que ao ser acionado será exibido um pop-up contendo os arquivos **.JSP** e **.HTML** do pacote zip anexado ao gadget.

No alto da aba, tem-se o link **"Editando {Nome\_Componente} [{Nome\_Nível}]"**, que ao ter o cursor sobre este label posicionado, será exibido um tooltip com o Id do componente em questão; clicando-se sobre o mesmo, este será copiado para a área de transferência.

**Importante:** o Componente HTML5 pode receber query's nos formatos de parâmetros padrão, além de manter também o formato antigo. Nele pode-se inserir as consultas da query no formato padrão, como descrito nos exemplos abaixo:

Exemplo 1:

```
SELECT * FROM TGFPAR WHERE CODPARC = :CODPARC_PARAM ORDER BY CODPARC ASC
```

Exemplo 2:

```
SELECT CAB.CODPARC, CAB.NOMEPARC

FROM TGFCAB CAB WHERE CODPARC IN

(SELECT PAR.CORPARC

FROM TGFPAR PAR INNER JOIN TGFCTT CTT ON (PAR.CODPARC = CTT.CODPARC)

WHERE PAR.ATIVO IN (:P_ATIVOLIST)

AND PAR.CODPARC IN (:P_CODPARCLIST)

AND CTT.ATIVO IN (:P_ATIVOLIST))

AND (:P_DTNEG.INI IS NULL OR CAB.DTNEG >= :P_DTNEG.INI)

AND (:P_DTNEG.FIN IS NULL OR CAB.DTNEG <= :P_DTNEG.FIN)

AND (:P_SERIENOTA IS NULL OR CAB.SERIENOTA LIKE '%' || :P_SERIENOTA || '%')
```

**Observação:** no caso do banco de dados em SQL Server deve-se alterar a última linha para:

```
AND (:P_SERIENOTA IS NULL OR CAB.SERIENOTA LIKE '%' + :P_SERIENOTA + '%')
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Controles > IReport

Este componente permite a exibição de relatórios formatados nos dashboards.

![EVO37](https://ajuda.sankhya.com.br/hc/article_attachments/360061010354)

Para utilização deste componente é necessário realizar a criação de um relatório na tela de [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados), adicionar no mesmo os arquivos do Jasper Reports (extensão JRXML) e apontar o seu código no componente que está sendo criado.

![EVO38](https://ajuda.sankhya.com.br/hc/article_attachments/360061010374)

Deste modo, será possível **"Importar Parâmetros do Relatório"** e abrir a tela de Relatórios Formatados já posicionada no relatório configurado. Ao importar os parâmetros do relatório, caso existam parâmetros com o mesmo nome estes não serão importados.

Ao acionar a marcação **"Ignorar paginação"** os relatórios que possuem quebra de página serão apresentados em paginação contínua.

**Observação:** alguns cuidados devem ser tomados ao configurar os parâmetros do componente, são eles:

- Para utilizar os parâmetros do tipo Multi List no dashboard, deve-se configurar o relatório para receber o parâmetro como String.
- Para usar os parâmetros do tipo Período, é necessário configurar dois parâmetros do tipo Data (Date ou Timestamp) no relatório com o mesmo nome, porém um com sufixo .ini e o outro com sufixo .fin. Vejamos um exemplo:

No dashboard o parâmetro do tipo Período é nomeado como ENTRADA e no relatório são configurados dois parâmetros do tipo Timestamp nomeados como "ENTRADA.INI" e "ENTRADA.FIN".

É possível também utilizar eventos de click no componente iReport, mas é necessário criá-los no editor do Jasper Report (iReport Design ou outro). As informações a cerca da criação destes eventos, podem ser acessadas por meio do tutorial [Como criar eventos de click no IReport](http://code.sankhya.com.br/como-criar-eventos-de-click-no-ireport/).

![EVO39](https://ajuda.sankhya.com.br/hc/article_attachments/360061932933)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Linha

![EVO40](https://ajuda.sankhya.com.br/hc/article_attachments/360061932953)

Ao acionar o modo de edição do gráfico, define-se seu **"Título"**, o **"Tamanho do texto"** a ser utilizado para apresentação do gráfico e se sua **"Legenda"** será ou não apresentada; caso afirmativo, deve-se estabelecer também sua **"Posição"** e **"Direção"** no gráfico.

#### Aba Eixos

No componente gráfico do tipo **"Linha"** deve-se definir uma **"Descrição"** pro eixo, tanto **"Horizontal"** quanto **"Vertical"** e definir se este será do tipo **"Valor"** ou do tipo **"Categoria"**.

- **Categoria:** Este tipo será por grupo; exemplo: Receitas e Despesas.
- **Valor:** Este tipo será contínuo, quantitativo; exemplo: Volume de Receitas e Volume de Despesas.

Através do campo **"Visão Parcial"** pode-se definir dentre as opções Primeiros Registros e Últimos Registros, quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise.

**Observação:** as configurações feitas no eixo horizontal influenciam nas configurações do eixo vertical. Por exemplo: Quando o campo Visão Parcial está desativado, ele ignora as configurações do mínimo e máximo do quadrante vertical.

Na edição dos gráficos cartesianos (Linhas, Barras e Colunas) o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; pode-se posicioná-los de "-90º" a "90º"; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico.

A opção **"Redimensionamento Vertical"** quando acionada, efetivará a configuração realizada para os valores mínimo e máximo do redimensionamento vertical condizentes ao gráfico. Além disso, o redimensionamento poderá ser apontado de forma automática ou fixa. Sendo que, optando pela forma Fixa o mesmo permitirá a fixação do seu posicionamento em um valor decimal de 4 casas.

A marcação **"Omitir valores nulos"** quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget.

#### Aba Séries

Série é um conjunto de dados que irão compor o gráfico. Nesta aba poderão ser definidas várias **"Séries"** sendo que cada uma representará uma linha no gráfico.

![EVO41](https://ajuda.sankhya.com.br/hc/article_attachments/360061932973)

No gráfico de Linha a **"Série"** poderá ser apenas do tipo **"Linha"**. Informa-se também a **"Descrição"** da Série. O **"Campo na Horizontal"** e o "Campo na Vertical" virão das variáveis disponíveis, e apresentarão os valores para a Série na vertical e na horizontal.

Quando a opção **"Destacar pontos"** é assinalada, irá fazer com que os pontos onde ocorreram mudança nos valores do gráfico, sejam enfatizados; esta opção marca automaticamente o campo **"Mostrar placa de valor"** (localizado logo abaixo), que no gráfico irá apresentar a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo. Vejamos um exemplo de um gráfico gerado:

![EVO42](https://ajuda.sankhya.com.br/hc/article_attachments/360061932993)

Na aba **"Série"**, tanto em modo grade, como em formulário, para os gráficos cartesianos (Linha, Barras e Colunas), o sistema disponibiliza o campo **"Cor"** para que seja informada a cor de apresentação da Série, possibilitando a personalização desta. Da mesma forma, os demais campos também são apresentados nas duas formas de visualização (grade e formulário) para serem analisados e editados se necessário.

Se o campo de marcação **"Usar cor padrão"** não estiver assinalado, a paleta de cores será habilitada e a Série receberá cores definidas na paleta; caso contrário, serão utilizadas cores padrão do sistema.

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

**Observação:** este tipo de gadget ao ser visualizado conta com o recurso de **"Zoom"** que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão **"Resetar Zoom"**, que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela.

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO43](https://ajuda.sankhya.com.br/hc/article_attachments/360061010394)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Barras

![EVO44](https://ajuda.sankhya.com.br/hc/article_attachments/360061933013)

#### Aba Eixos

![EVO45](https://ajuda.sankhya.com.br/hc/article_attachments/360061010414)

Na edição dos gráficos cartesianos (**Linhas**, **Barras** e **Colunas**) o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que eles serão apresentados nos gráficos; você poderá posicioná-los de **"-90º"** a **"90º"**; a palavra **"Exemplo"** posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico.

Ainda na aba **"Eixos"**, a única diferença entre a configuração do gráfico de Barras para o gráfico de Linhas será no campo **"Tipo"**, que apresentará um valor fixo, tanto para o eixo horizontal quanto para o eixo vertical. Como no gráfico de Barras somente o eixo horizontal poderá apresentar valores quantitativos, o Tipo virá fixado como **"Valor"**, já para o eixo vertical que apresentará os agrupamentos, o Tipo virá fixado como **"Categoria"**.

Por meio do campo **"Visão Parcial"** pode-se definir dentre as opções Primeiros Registros e Últimos Registros, quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise.

A marcação **"Omitir valores nulos"** quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget.

#### Aba Séries

![EVO46](https://ajuda.sankhya.com.br/hc/article_attachments/360061933033)

O gráfico de Barras permite a associação de Série de **"Barras"** com **"Linhas"**. Pode-se definir "n" séries para um gráfico. Exemplo: 

Pode-se criar uma Série com vendas por parceiro e outra por compras, sendo as duas por **"Barras"** e criar sobre estas, uma **"Linha"** trazendo o somatório mostrando o volume de negociações.

O campo **"Mostrar placa de valor"** no gráfico irá apresentar a informação de cada barra quando o mouse for posicionado sobre a mesma.

**Observação:** para que seja exibida uma placa de valor que está sobrepondo outra placa, é necessário que o parâmetro **"Permite sobreposição de placas de valor em gráfico - SOBREVALORGRAF"** esteja ligado. Do contrário, o sistema irá ocultar as placas de valor quando identificar que a mesma irá sobrepor outra.

![EVO47](https://ajuda.sankhya.com.br/hc/article_attachments/360061010434)

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

**Observação:** este tipo de gadget ao ser visualizado, conta com o recurso de **"Zoom"** que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão **"Resetar Zoom"**, que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela.

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO48](https://ajuda.sankhya.com.br/hc/article_attachments/360061010454)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Colunas

![EVO49](https://ajuda.sankhya.com.br/hc/article_attachments/360061933053)

Na utilização do Gráfico de Colunas, ao realizar sua edição, nota-se o campo **"Colunas"** que é utilizado para determinar-se a quantidade de colunas que se deseja visualizar no momento em que o Dashboard em construção será aberto. Este campo possui **"6"** (seis) como valor padrão, não podendo este valor ser diminuído, apenas acrescido.

#### Aba Eixos

![EVO50](https://ajuda.sankhya.com.br/hc/article_attachments/360061010474)

Na edição dos gráficos cartesianos (Linhas, Barras e Colunas) o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; você poderá posicioná-los de **"-90º"** a **"90º"**; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico.

A única discrepância em relação à configuração do gráfico de barras para este, será a inversão dos valores do campo **"Tipo"** nesta aba. Pois, num gráfico de **"Colunas"** o eixo horizontal apresentará os agrupamentos e o Tipo virá fixado como **"Categoria"**, já o eixo vertical apresentará valores quantitativos e o Tipo virá fixado como **"Valor"**.

Por meio do campo **"Visão Parcial"** pode-se definir dentre as opções Primeiros Registros e Últimos Registros, quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise.

**Observação:** as configurações feitas no eixo horizontal influenciam nas configurações do eixo vertical. Por exemplo: Quando o campo Visão Parcial está desativado, ele ignora as configurações do mínimo e máximo do quadrante vertical.

A opção **"Redimensionamento Vertical"** quando acionada, irá efetivar a configuração realizada para os valores mínimo e máximo do redimensionamento vertical condizentes ao gráfico. Além disso, o redimensionamento poderá ser apontado de forma automática ou fixa. Sendo que, optando pela forma Fixa o mesmo permitirá a fixação do seu posicionamento em um valor decimal de 4 casas.

**Nota:** o Redimensionamento Vertical não será aplicado, caso exista dois ou mais cadastros de série e um deles estiver com a marcação **"Escala Secundária"** acionada.

A marcação **"Omitir valores nulos"** quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget.

Ao ativar a opção **"Rotacionar Resultados"**, pode-se redefinir novos intervalos no gráfico, referentes ao seu eixo **"Y"**, ou seja, dependendo do dimensionamento do gráfico, pode-se visualizar valores de 0 a 10, ou de 2 a 8, por exemplo, bastando para isso, movimentar a barra vertical que será apresentada no lado superior direito da tela.

#### Aba Série

Assim com o gráfico de Barras, o de Colunas também permite a associação de Série de **"Linhas"** com **"Colunas"**. Pode-se definir **"n"** séries para um gráfico.

![EVO51](https://ajuda.sankhya.com.br/hc/article_attachments/360061933073)

**Importante:** a ordenação das séries (controlada pelos botões ![clip3795](https://ajuda.sankhya.com.br/hc/article_attachments/360061010494)) influencia na apresentação do gráfico, pois se for criado um dashboard que contenha uma linha de totalização, esta é exibida por detrás das barras.

O campo **"Mostrar placa de valor"** no gráfico irá apresentar a informação pertinente a cada coluna, quando posicionar-se o mouse sobre a mesma.

**Observação:** pode-se através da expressão SQL buscar a informação desejada para ser colocada no balão de informações do gráfico e adicioná-la ao campo Descrição, sempre prefixado pelo símbolo $.

O botão ![clip6776](https://ajuda.sankhya.com.br/hc/article_attachments/360061933093) localizado no lado superior direito da tela, quando acionado, apresenta as opções **"Mostrar Título"** (quando marcada, exibe o título do gráfico), **"Mostrar Legenda"** (apresenta a legenda do gráfico, quando assinalada; quando marcada, esta opção assume a nomenclatura **"Ocultar Legenda"** para a necessidade de se esconder a legenda novamente) e **"Imprimir Gráfico"** (da início ao processo de impressão do gráfico em questão).

Ainda sobre a aba Série na configuração do gráfico de colunas, definindo-se o campo Série com a opção **"Linha"**, tem-se a aba com as seguintes informações:

![EVO53](https://ajuda.sankhya.com.br/hc/article_attachments/360061933113)

Deve-se preencher os campos **"Descrição"**, **"Campo na Horizontal"** e **"Campo na Vertical"**; o link [Acumular valores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#acumularvalores), irá apresentar os detalhes a respeito da referida marcação.

A marcação **"Escala Secundária"** ao ser assinalada, será possível no gráfico gerado, realizar a criação de uma escala vertical secundária para que seja feito o destaque dos valores da respectiva série de dados. Efetuando-se esta marcação, será apresentado logo abaixo da mesma, o campo **"Sufixo da Escala"**, para inclusão de uma breve denominação para a escala secundária. Caso a série possua escala secundária (marcação realizada), o recurso de Visão Parcial Vertical do Gráfico não será apresentado. A Escala Secundária poderá ser utilizada se o campo Série for definido com ambas as opções disponíveis, Linha e Colunas.

A opção **"Destacar pontos"** quando assinalada, irá fazer com que os pontos onde ocorreram mudança nos valores do gráfico, sejam enfatizados; esta opção exibe e assinala automaticamente a marcação **"Mostrar placa de valor"** (localizado logo abaixo), que no gráfico irá apresentar a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo.

A marcação **"Cor"** é utilizada para informar-se a cor de apresentação da Série, possibilitando a personalização desta, de modo que pode-se utilizar a cor desejada ou ainda, a cor padrão.

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

**Observação:** este tipo de gadget ao ser visualizado, conta com o recurso de **"Zoom"** que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão **"Resetar Zoom"**, que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela.

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO54](https://ajuda.sankhya.com.br/hc/article_attachments/360061010514)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Pizza

![EVO55](https://ajuda.sankhya.com.br/hc/article_attachments/360061933133)

Em relação à configuração dos gráficos apresentados anteriormente, este tipo de gráfico apresenta uma maior variação, uma vez que para ele não configura-se as abas **"Eixos"** e **"Série"**.

![EVO56](https://ajuda.sankhya.com.br/hc/article_attachments/360061010534)

#### Aba Geral

Como teoricamente em um gráfico de Pizza será apresenta uma única **"Série"**, além do **"Título"**, configura-se aqui os campos **"Valor"** e **"Agrupamento"**.

As funcionalidades do botão **"Evento"** podem ser visualizadas clicando-se no link [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos).

O **"Campo Valor"** trará o percentual de determinado setor circular. O **"Campo Agrupamento"**definirá o campo que fará o agrupamento no gráfico.

Por meio do campo **"Tamanho dos Títulos"**, você definirá a quantidade de caracteres que serão utilizados na legenda de cada região do gráfico de pizza. Por exemplo, em um gráfico onde uma das legendas é **"Nota de Compra"**, ao definir o campo **"Tamanho dos Títulos"** com "3" caracteres, será apresentada no gráfico a descrição **"Not..."**; em outras palavras, o sistema irá limitar a descrição à quantidade de caracteres definidos no campo. Vejamos um exemplo de um gráfico de pizza:

![EVO57](https://ajuda.sankhya.com.br/hc/article_attachments/360061933153)

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO58](https://ajuda.sankhya.com.br/hc/article_attachments/360061010554)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Análise de Rentabilidade

![EVO59](https://ajuda.sankhya.com.br/hc/article_attachments/360061010574)

Neste gráfico além do seu **"Título"**, define-se o **"Tamanho do texto"** a ser nele utilizado.

**Apresentação:** Determina-se como será a apresentação (label) do gráfico; se por **"Produto"** ou **"Serviço"**.

Na **"Apresentação"** será determinado como se a apresentação (label) do gráfico será por **"Produto"** ou por **"Serviço"**.

A **"Posição da legenda"** será definido a posição que a legenda se encontrará.

No campo **"Apresentações dos Valores"** deve-se indicar se os valores a serem exibidos será por **"Percentual"** ou **"Valores"**.

Em **"Colunas na legenda"** determina-se a quantidade de divisões de colunas das legendas de cada região do gráfico.

Por meio da marcação **"Abreviar legenda"** você poderá abreviar a legenda gerada para cada região do gráfico. Como por exemplo, se tivermos a "Faturamento" será apresentada no gráfico como **"FAT"**.

O botão **"Evento"** possui algumas opções que irão possibilitar a exploração das informações pertinentes à Análise de Rentabilidade em diferentes níveis de detalhamento, exibindo-as de maneira hierárquica. Tem-se as seguintes alternativas:

- Faturamento;
- CMV/PV:
- Gasto Variável;
- Gasto Fixo;
- M. Contribuição;
- Resultado.

Depois de definido o ponto a ser considerado para configuração do Evento, o pop-up Editar Evento será exibido, os detalhes deste poderão consultados por meio do link [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos).

**Observação:** a Margem de Contribuição não pode ser configurada por meio de evento, pois é um resultado obtido através do seguinte cálculo:

```
MC = Faturamento - Custo Mercadoria Vendida - Gasto Variável
```

![EVO60](https://ajuda.sankhya.com.br/hc/article_attachments/360061933173)

Além da expressão principal, definida na aba **"Expressão"**, este tipo de gráfico permitirá que sejam criadas expressões independentes para cada uma de suas partes. Para isto, basta apenas dar um duplo clique sobre qualquer uma das partes para que o construtor de expressões seja aberto. Na expressão independente que esta sendo definida para uma determinada parte, pode-se utilizar variáveis ou campos que vieram da expressão principal.

**Nota:** a expressão principal é a que foi definida na aba Expressão, trata-se da query básica que trará informações para o componente. Cada componente possui uma expressão principal.

**Importante:** se não for informada uma expressão para a Margem de Contribuição, seu valor será calculado com base nos outros dados informados.

Observe o exemplo de um gráfico de Análise de Rentabilidade:

![EVO61](https://ajuda.sankhya.com.br/hc/article_attachments/360061933193)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Velocímetro

![EVO62](https://ajuda.sankhya.com.br/hc/article_attachments/360061010594)

O funcionamento do gráfico de Gauge (Velocímetro) segue o mesmo princípio dos demais componentes.

![EVO63](https://ajuda.sankhya.com.br/hc/article_attachments/360061933213)

#### Aba Geral

Aqui, teremos os seguintes dados:

Será determinado no **"Campo de Valor"**, a qual campo será atribuído o valor do gráfico (lembrando-se que se trata de um gráfico de valor pontual).

Definiremos nos campos **"Valor Mínimo"** e **"Valor Máximo"**, os valores mínimo e máximo a serem considerados no gráfico.

Serão estabelecidas em **"Faixa de alerta"**, as cores dos intervalos de valores a serem empregados no gráfico.

**Nota:** na grade dos intervalos são feitas algumas validações para auxiliar o usuário. Caso seja encontrado algum problema será exibida uma mensagem em vermelho acima da grade com a listagem de problemas encontrados.

As funcionalidades do botão **"Evento"** podem ser visualizadas clicando-se no link [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos).

![EVO64](https://ajuda.sankhya.com.br/hc/article_attachments/360061010614)

O botão ![clip6777](https://ajuda.sankhya.com.br/hc/article_attachments/360061010634) localizado no lado superior direito da tela, quando acionado, apresenta as opções **"Mostrar Título"** (quando marcada, exibe o título do gráfico), **"Mostrar Legenda"** (apresenta a legenda do gráfico, quando assinalada; quando marcada, esta opção assume a nomenclatura **"Ocultar Legenda"** para a necessidade de se esconder a legenda novamente) e **"Imprimir Gráfico"** (da início ao processo de impressão do gráfico em questão).

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![evo65](https://ajuda.sankhya.com.br/hc/article_attachments/360061933233)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Geográfico

![EVO66](https://ajuda.sankhya.com.br/hc/article_attachments/360061933253)

Uma vez adicionado o gráfico no nível, configura-se as informações que serão representadas.

![EVO67](https://ajuda.sankhya.com.br/hc/article_attachments/360061933273)

Define-se o **"Modo de apresentação do mapa"**; se as informações serão geradas por **"Países"** ou **"Estados"**.

Tem-se também a configuração da **"Legenda"**, onde determina-se qual e a quantidade das faixas de cores a serem utilizadas no mapa.

Além disso, faz-se a definição dos **"Marcadores"** e **"Nomenclaturas"** a serem empregadas no mapa quando este for visualizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Área

![EVO68](https://ajuda.sankhya.com.br/hc/article_attachments/360061933293)

Ao acionar-se a edição deste gadget, as configurações a serem realizadas, são semelhantes às efetuadas no uso do gadget de Colunas. Na aba **"Eixos"**, tem-se:

Na edição do gráfico, o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; pode-se posicioná-los de **"-90º"** a **"90º"**; a palavra **"Exemplo"** posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico.

A marcação **"Redimensionamento Vertical"** quando acionada, efetivará a configuração realizada para os valores mínimo e máximo do redimensionamento vertical condizentes ao gráfico. Além disso, o redimensionamento poderá ser apontado de forma automática ou fixa. Sendo que, optando pela forma Fixa o mesmo permitirá a fixação do seu posicionamento em um valor decimal de 4 casas.

A única diferença entre a configuração do gráfico de barras para este, será a inversão dos valores do campo **"Tipo"** nesta aba. Pois, num gráfico de **"Colunas"** o eixo horizontal apresentará os agrupamentos e o Tipo virá fixado como **"Categoria"**, já o eixo vertical apresentará valores quantitativos e o Tipo virá fixado como **"Valor"**.

Através do campo **"Visão Parcial"** pode-se definir dentre as opções Primeiros Registros e Últimos Registros, quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise.

A marcação **"Omitir valores nulos"** quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget.

Na construção deste gadget, também é essencial a configuração da aba **"Série"**.

![EVO69](https://ajuda.sankhya.com.br/hc/article_attachments/360061933313)

**Observação:** este tipo de gadget ao ser visualizado, conta com o recurso de **"Zoom"** que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão **"Resetar Zoom"**, que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela.

As informações pertinentes a aba **"BIA"** podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO70](https://ajuda.sankhya.com.br/hc/article_attachments/360061010654)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Donut

![EVO71](https://ajuda.sankhya.com.br/hc/article_attachments/360061933333)

Primeiramente na configuração do gráfico de Donut, define-se seu **"Título"**, o **"Tamanho do texto"** a ser utilizado para apresentação do gráfico e se sua **"Legenda"** será ou não apresentada; caso afirmativo, deve-se estabelecer também sua **"Posição"** e **"Direção"** no gráfico.

As funcionalidades do botão **"Evento"** podem ser visualizadas clicando-se no link [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos).

Esta configuração é semelhante a que é realizada no uso do gráfico de Pizza, se diferenciando pela definição do **"Tipo de Donut"**, que traz as opções **"Completo - 360º"** e **"Semicírculo - 180º"**; a escolha feita neste campo, irá determinar o formato em que o gráfico Donut será apresentado, ou seja, se irá formar um círculo completo ou um semicírculo.

![EVO72](https://ajuda.sankhya.com.br/hc/article_attachments/360061933353)

As informações pertinentes a aba **"BIA"** podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO73](https://ajuda.sankhya.com.br/hc/article_attachments/360061010674)

Observe abaixo o exemplo de um gráfico Donut gerado no formato completo:

![EVO74](https://ajuda.sankhya.com.br/hc/article_attachments/360061010694)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Bolha

![EVO75](https://ajuda.sankhya.com.br/hc/article_attachments/360061933373)

Aqui, teremos mais  uma alternativa para geração de gráficos nos Componentes de BI. Suas configurações básicas e funcionalidades, seguem o padrão dos demais componentes.

A diferença principal para os outros componentes é a necessidade de definição de um diâmetro para as bolhas, a saber; para construção de um gráfico de bolha, são necessários três valores, **"X"**, **"Y"** e **"Z"**, que se referem aos campos do eixo X, eixo Y e diâmetro da bolha, respectivamente.

**Observação:** vale ressaltar que o dashboard de Bolha não utiliza campo de "Categoria", somente campo de **"Valor"**.

Primeiramente na configuração do gráfico de Bolhas, define-se seu **"Título"**, o **"Tamanho do texto"** a ser utilizado para apresentação do gráfico e se sua **"Legenda"** será ou não apresentada; caso afirmativo, deve-se estabelecer também sua **"Posição"** e **"Direção"** no gráfico.

Na aba **"Eixos"** configura-se a nomenclatura a ser atribuída aos eixos **"Horizontal"** e **"Vertical"** do gráfico que será construído.

Na aba **"Séries"** configura-se os dados para cada agrupamento de bolhas. Cada série configurada será referente a uma coloração de bolhas, portanto, pode-se ter mais de uma série em cada gráfico gerado.

![EVO76](https://ajuda.sankhya.com.br/hc/article_attachments/360061933393)

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

**Observação:** este tipo de gadget ao ser visualizado, conta com o recurso de **"Zoom"** que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão **"Resetar Zoom"**, que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela.

As informações pertinentes a aba **"BIA"** podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO77](https://ajuda.sankhya.com.br/hc/article_attachments/360061010714)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > TreeMap

![EVO78](https://ajuda.sankhya.com.br/hc/article_attachments/360061010734)

Ao acionar a tela para configuração deste componente, tem-se as abas **"Geral"**, **"Categorias"** e **"BIA"**.

![EVO79](https://ajuda.sankhya.com.br/hc/article_attachments/360061010754)

Depois de informado o Título e definido o Tamanho do texto, na aba Geral tem-se a marcação **"Exibir valor no item"**, que quando efetuada, no gráfico gerado, será apresentado juntamente a cada item, o valor que este representa.

As funcionalidades do botão **"Evento"** podem ser visualizadas clicando-se no link [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos).

Na seção **"Layout de Apresentação"** tem-se a possibilidade de personalização da apresentação do gráfico; faz-se esta personalização por meio de duas opções, **"Categoria"** e **"Item"**. A opção de layout para Categoria determina como as categorias serão exibidas; a opção Item, como os itens dentro de um categoria serão apresentados.

Tem-se quatro layout's disponibilizados para Categoria e Item. A saber:

- **Simples e rápido:** Layout simples e rápido para apresentar, porém, pode dificultar a comparação das informações.
- **Listra:** Layout simples que apresenta as informações na mesma direção.
- **Proporcional alternado:** Layout que tenta apresentar as informações para facilitar a comparação, porém, pode alterar a direção das mesmas.
- **Proporcional:** Comportamento semelhante ao "Proporcional alternado", porém, não altera a direção das informações.

Na aba **"Categorias"**, configura-se exatamente as categorias que serão utilizadas na apresentação do gráfico.

![EVO80](https://ajuda.sankhya.com.br/hc/article_attachments/360061010774)

No **"Id"**, ou Identificador de categoria, Todos os itens (resultados retornados na expressão) que pertencem a ela, deverão ter obrigatoriamente o valor idêntico ao identificador na coluna configurada no **"Campo de Categoria"**. 

Na **"Descrição"**, informaremos a descrição da categoria que será exibida no Treemap.

Você definirá no campo **"Cor"**, a cor de fundo para os itens desta categoria.

Na seção **"Configurações das colunas"** configura-se os campos de acordo com a query utilizada para gerar os dados do gráfico.

No **"Campo de Nome"** será inserido o nome da coluna com o valor da descrição do item que será exibido no Gráfico Treemap.

Informaremos em **"Campo de Categoria"** o nome da coluna  com o valor que representa a categoria "pai" do item; essa opção é quem define em qual quadrante o resultado será encaixado no momento de renderização do Gadget.   

Teremos no **"Campo de Valor"**, uma coluna com o valor que o item possui. Deverá ser uma coluna que retorna um valor numérico.

As informações pertinentes a aba **"BIA"** podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO81](https://ajuda.sankhya.com.br/hc/article_attachments/360061933413)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Dispersão

![EVO82](https://ajuda.sankhya.com.br/hc/article_attachments/360061010794)

O gráfico de Dispersão permite a verificação da existência ou não de relação entre duas variáveis de natureza quantitativa, ou seja, analisando dois aspectos, será possível com este tipo de gráfico, identificar se um elemento melhora, piora ou se mantém, quando relacionado com o segundo fator.

Depois de determinar-se o **"Título"** do Componente, bem como o **Tamanho do texto** e suas respectivas **Posições** e **Direções**, tem-se para sua configuração, as abas **"Eixos"**, **"Série"** e **"BIA"**:

![EVO83](https://ajuda.sankhya.com.br/hc/article_attachments/360061933433)

Na aba Eixos, determinam-se as descrições dos eixos **Horizontal** e **Vertical**. Além disso, o campo **"Tipo de apresentação"** define se o gráfico gerado será composto por Pontos e linhas, ou Somente pontos.

Já na aba Série, determinam-se as particularidades de cada conjunto de pontos e/ou linhas a serem apresentados no gráfico, tais como sua **Descrição**, as variáveis na **Horizontal** e na **Vertical**, as **Cores** de cada um e se serão exibidas **Placas de valor** (ao passar o mouse sobre os pontos, tem-se o valor correspondente à cada um deles).

![EVO84](https://ajuda.sankhya.com.br/hc/article_attachments/360061010814)

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

As informações pertinentes a aba BIA podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO85](https://ajuda.sankhya.com.br/hc/article_attachments/360061933453)

Vejamos abaixo o exemplo de um gráfico gerado por este componente:

![EVO86](https://ajuda.sankhya.com.br/hc/article_attachments/360061933473)

**Observação:** este tipo de gadget ao ser visualizado, conta com o recurso de **"Zoom"** que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão **"Resetar Zoom"**, que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Radar

![EVO87](https://ajuda.sankhya.com.br/hc/article_attachments/360061010834)

Ao acionar o modo de edição do gráfico, define-se seu **"Título"**, o **"Tamanho do texto"** a ser utilizado para apresentação do gráfico e se sua **"Legenda"** será ou não apresentada; caso afirmativo, deve-se estabelecer também sua **"Posição"** e **"Direção"** no gráfico.

#### Aba Eixos

![EVO88](https://ajuda.sankhya.com.br/hc/article_attachments/360061010854)

No componente gráfico do tipo Radar, deve-se definir uma **"Descrição"** pro eixo, tanto Horizontal quanto Vertical e definir se este será do tipo **"Valor"** ou do tipo **"Categoria"**.

- **Categoria:** Este tipo será por grupo; exemplo: Receitas e Despesas.
- **Valor:** Este tipo será contínuo, quantitativo; exemplo: Volume de Receitas e Volume de Despesas.

É possível também informar uma **"Máscara"** para formatar os valores dos eixos. O campo para informar a máscara só estará disponível para eixos do tipo **"Valor"**. É possível digitar a máscara diretamente no campo ou editá-la através do **"Assistente de edição de máscara"** (ícone localizado ao lado do campo).

A marcação **"Omitir valores nulos"** quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget.

De forma similar à marcação anterior, assinalando a opção **"Omitir títulos"**, alguns títulos serão automaticamente ocultados, para que se tenha uma visualização mais clara.

Na edição do gráfico, na seção Vertical, o sistema possibilita a rotação do Título, ou seja, o ângulo em que este será apresentado nos gráficos; pode-se posicioná-lo de **"-90º"** a **"90º"**; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título será exibido no gráfico.

#### Aba Série

![EVO89](https://ajuda.sankhya.com.br/hc/article_attachments/360061010874)

Série é um conjunto de dados que irão compor o gráfico. Nesta aba poderão ser definidas várias "Séries" sendo que cada uma representará uma linha ou área no gráfico.

No gráfico de Radar a **"Série"** poderá ser do tipo Linha ou Área, ou seja, o gráfico gerado terá seu resultado delimitado por linhas que se ligam ponto a ponto, ou toda a área que abrange o resultado será preenchida com a coloração desejada. Informa-se também a **"Descrição"** da Série. As informações referentes ao **"Campo na Horizontal"** e o **"Campo na Vertical"** virão das variáveis disponíveis, e apresentarão os valores para a "Série" na vertical e na horizontal.

O campo **"Mostrar placa de valor"** quando assinalado, no gráfico tendo-se a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo.

Ainda na aba **"Série"**, tanto em modo grade como em formulário, o sistema disponibiliza o campo **"Cor"** para que seja informada a cor de apresentação da "Série", possibilitando a personalização desta. Da mesma forma, os demais campos também são apresentados nas duas formas de visualização (grade e formulário) para serem analisados e editados se necessário.

Se o campo de marcação **"Usar cor padrão"** não estiver assinalado, a paleta de cores será habilitada e a Série receberá cores definidas na paleta; caso contrário, serão utilizadas cores padrão do sistema. Vejamos o exemplo de um gráfico gerado:

![EVO90](https://ajuda.sankhya.com.br/hc/article_attachments/360061010894)

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO91](https://ajuda.sankhya.com.br/hc/article_attachments/360061010914)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Funil

![EVO92](https://ajuda.sankhya.com.br/hc/article_attachments/360061933493)

Os gráficos de Funil permitem a visualização de valores em vários estágios de um processo. Pode-se por exemplo, exibir o número de clientes em potencial em cada etapa de um cronograma de vendas.

![EVO93](https://ajuda.sankhya.com.br/hc/article_attachments/360061010934)

Primeiramente na configuração do gráfico de Funil, define-se seu **"Título"**, o **"Tamanho do texto"** a ser utilizado para apresentação do gráfico e se sua **"Legenda"** será ou não apresentada; caso afirmativo, deve-se estabelecer também sua **"Posição"** e **"Direção"** no gráfico.

#### Aba Geral

As funcionalidades do botão **"Evento"** podem ser visualizadas clicando-se no link [Eventos - Gráficos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#eventos-grficos).

Por meio do **"Campo Valor"** você determinará o campo que irá representar os valores em cada setor no funil. O **"Campo Etapa"** define qual informação será tomada como base para apresentação das etapas no gráfico.

Através do campo **"Exibição dos Títulos"**, define-se como se dará a apresentação dos resultados no gráfico, dentre as opções Valor e % da etapa anterior; a primeira exibe os valores exatos correspondentes a cada "fatia" do gráfico; já o % da etapa anterior, apresenta o quanto em percentual uma etapa representa em relação ao seu estágio precedente. Vejamos um exemplo de um gráfico de funil:

![EVO94](https://ajuda.sankhya.com.br/hc/article_attachments/360061933513)

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO95](https://ajuda.sankhya.com.br/hc/article_attachments/360061933533)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Gráficos > Intervalo de Área

Os gráficos de Intervalo de Área permitem a criação de ranges de valores, possibilitando assim destacar comparações de valores em um determinado período. Como por exemplo, uma empresa pode visualizar o dia que o preço praticado ficou acima, na média ou abaixo do preço adotado pelo mercado.

![EVO96](https://ajuda.sankhya.com.br/hc/article_attachments/360061010954)

Ao acionar-se a edição deste gadget, as configurações a serem realizadas, são semelhantes às efetuadas no uso do gadget de Colunas. Na aba **"Eixos"**, tem-se:

Na edição do gráfico, o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; pode-se posicioná-los de **"-90º"** a **"90º"**; a palavra **"Exemplo"** posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico.

Através do campo **"Visão Parcial"** pode-se definir dentre as opções Primeiros Registros e Últimos Registros, quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise.

Em um gráfico de **"Intervalo de Área"** o eixo horizontal apresentará os agrupamentos e o **"Tipo"** virá fixado como **"Categoria"**, já o eixo vertical apresentará valores quantitativos e o "Tipo" virá fixado como **"Valor"**.

A opção **"Omitir títulos"** quando acionada, alguns títulos serão automaticamente ocultados, para que se tenha uma visualização mais clara.

#### Aba Série

![EVO97](https://ajuda.sankhya.com.br/hc/article_attachments/360061933553)

A Série poderá ser do tipo **"Intervalo de Área"** ou **"Linha"**. Informa-se também a **"Descrição"** da Série. O **"Campo na Horizontal"** virá das variáveis disponíveis, e apresentará os valores para a Série na horizontal.

Os valores informados nos campos **"Campo Mín."** e **"Campo Máx."** serviram como pontos limitadores onde o gráfico irá oscilar mostrando as elevações e quedas atingidas durante um certo período. Como por exemplo, em uma analise semanal dos valores máximo e mínimo praticados no mercado; o gráfico apresentará o valor que foi praticado pela empresa em relação à estes valores.

O campo **"Mostrar placa de valor"** quando acionado, irá apresentar no gráfico a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo.

Ainda na aba Série, o sistema disponibiliza o campo **"Cor"** para que seja informada a cor de apresentação da Série, possibilitando a personalização desta. Se o campo de marcação **"Usar cor padrão"** não estiver assinalado, a paleta de cores será habilitada e a Série receberá cores definidas na paleta; caso contrário, serão utilizadas cores padrão do sistema.

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão **"Ctrl"** do seu teclado, marque as séries e clique no botão **"Agrupar séries"**.

#### Aba BIA

As informações pertinentes a esta aba podem ser acessadas no link [B.I.A - Business Intelligence Analyst](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047266793).

![EVO98](https://ajuda.sankhya.com.br/hc/article_attachments/360061933593)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Acumular Valores

A opção **"Acumular valores"**, está disponível para os gráficos dos tipos **"Linha"**, **"Barras"** e **"Colunas"**, está localizada na aba **"Série"**, logo abaixo dos campos **"Campo na Horizontal"** e **"Campo na Vertical"**.

Porém esta opção estará disponível de forma diferente de acordo com o tipo do gráfico.

- Para os gráficos do tipo **"Linha"**, a opção estará ligada aos dois campos **"Campo na Horizontal"**, e **"Campo na Vertical"**;
- Já para os gráficos do tipo **"Barras"**, a opção se relaciona ao campo **"Campo na Horizontal"**;
- Nos de tipo **"Colunas"**, ela é relacionada ao campo **"Campo na Vertical"**.

Esta opção permite a configuração de indicadores (barras, colunas, linhas) nos gráficos de modo a somar seus próprios valores conforme o progresso. Para exemplificar o seu uso, considere um gráfico válido (em barras, colunas, ou em linhas) que mostre o andamento das vendas conforme determinado período (o período pode ser configurado em forma de parâmetro).

Para isso, o gadget deve ser configurado para realizar uma busca no banco de dados que possibilite o gráfico ser alimentado com os valores necessários. Dessa forma, uma expressão SQL deve ser especificada para isso. Para os gráficos do tipo **"Barras"**, configurar uma **"Série"** onde o eixo vertical corresponda ao período e o eixo horizontal, aos valores das vendas.

Marcando-se a opção **"Acumular valores"**, as barras que partem do eixo referente ao período, somarão seus valores conforme a evolução do período. Ou seja, a primeira barra, correspondente ao primeiro dia/mês do período, possuirá o valor total das vendas realizadas até então. A segunda barra, que corresponderá ao segundo dia/mês do período, somará/acumulará o seu próprio valor, ao valor da barra anterior, e assim por diante.

O mesmo ocorre nos demais tipos de gráfico, porém, com seus comportamentos particulares. É importante observar que a opção Acumular valores é utilizada apenas para campos numéricos.

![EVO99](https://ajuda.sankhya.com.br/hc/article_attachments/360061010974)

Na edição desses tipos de gráficos (linhas, barras e colunas) é possível informar uma máscara para formatar os valores dos eixos. O campo para informar a máscara só estará disponível para eixos do tipo **"Valor"**. É possível digitar a máscara diretamente no campo ou editá-la através do **"Assistente de edição de máscara"** (ícone localizado ao lado do campo):

![EVO100](https://ajuda.sankhya.com.br/hc/article_attachments/360061010994)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Parâmetros

No construtor de componentes pelo **"Design"**, o painel a direita da tela apresenta abas para que sejam informados os **"Parâmetros"**, **"Configurações"**, **"Variáveis"** e **"Argumentos"**; estes dados serão manipulados no novo "gadget". Vejamos cada uma delas a seguir:

Inicialmente, na aba **"Parâmetros"** informam-se os parâmetros que serão utilizados como filtros para o "gadget" na tela de visualização de Dashboard.

![EVO101](https://ajuda.sankhya.com.br/hc/article_attachments/360061011014)

**Observação:**  na criação de uma consulta, o sistema realiza sua validação verificando se existem erros em sua estrutura ao clicar-se no botão **"OK"**. Caso exista algum erro, este será apresentado na tela, de modo a orientar o usuário para sua correção.

Deve-se informar um **"Id"** único e uma **"Descrição"** para ele. Discriminar pelo campo **"Requerido"** se este será um parâmetro obrigatório ou não. E pelo campo **"Salvar último valor"** definir se o último parâmetro informado será ou não salvo.

Já quando a marcação **"Mostrar inativas"** for habilitada será possível pesquisar registros inativos nos filtros de pesquisa dos dashboards.

No campo **"Tipo"**, seleciona-se como será o "gadget". Tem-se as seguintes opções:

- Entidade/Tabela;
- Período;
- Data;
- Texto;
- Data/Hora;
- Número Inteiro;
- Número Decimal;
- Verdadeiro/Falso;
- Single List;
- Multi List.

![EVO102](https://ajuda.sankhya.com.br/hc/article_attachments/360061011034)

De acordo com o **"Tipo"** definido, abaixo dele serão apresentados campos que irão consumar o tipo determinado. Vejamos abaixo alguns exemplos:

- Utilizando-se os tipos **"Texto"**, **"Número Inteiro"** e **"Número Decimal"** pode-se configurar o campo **"Limite de caracteres"** e estabelecer-se um limite para os caracteres a serem utilizados.
- Na escolha dos tipos **"Data"**, **"Data/Hora"** ou **"Período"**, será habilitado para possível marcação, o campo **"Considerar data atual?"**; ao realizá-la e construindo posteriormente um Dashboard, em sua abertura, o parâmetro será apresentado preenchido automaticamente com a data atual.

**Observações:** se o tipo utilizado for Data o campo **"Salvar último valor"** não poderá ser marcado simultaneamente ao campo **"Considerar data atual?"**. Caso seja feita a utilização do tipo Período, os campos **"Salvar último valor"** e **"Considerar data atual?"** podem ser marcados em paralelo, porém a **"data atual"** será apresentada apenas para o período final.

- O campo **"Range"** é empregado para os tipos **"Número Inteiro"** e **"Número Decimal"**, onde pode-se estabelecer que sejam informados os valores dentro do intervalo determinado.
- Os tipos **"Single List"** e **"Multi List"**, devem ser combinados com o campo **"Tipo de dado"**, que apresenta as opções **"Texto"**, **"SQL"** ou **"Entidade/Campo"**. Utilizando-se o tipo de dado **"SQL"** por exemplo, pode-se realizar a criação de uma lista por meio de uma query personalizada; no tipo de dado **"Texto"**, a criação de uma lista por meio do fornecimento manual de valores, e assim sucessivamente.

#### Utilização de Parâmetros

Para utilizar um parâmetro criado, você deve se referir a ele com **:ID\_do\_parâmetro**. Sendo que, **":"** é o aviso para buscar o conteúdo do parâmetro identificado pelo ID. Vejamos o exemplo a seguir:

Suponha que criamos um parâmetro **(P\_PARCEIRO)** para escolher de qual parceiro queremos ver as OS de 01/01/2021 em diante. Para se referir a esse parâmetro numa consulta SQL, utilizamos:

```
SELECT          *
FROM            TCSOSE
WHERE          CODPARC IN :P_PARCEIRO
AND               DHCHAMADA >= '01/01/2021'
ORDER BY      NUMOS
```

Quando utilizamos o **":"**, o Construtor de Componentes de BI, traduz isso da seguinte forma **"(“, conteúdo do parâmetro, ")"**. Suponha que o valor 2135 esteja no **P\_PARCEIRO**. Logo, a tradução da query SQL ficaria:

```
SELECT          *
FROM            TCSOSE
WHERE          CODPARC IN IN (2135)
AND               DHCHAMADA >= '01/01/2021'
ORDER BY      NUMOS
```

Se o tipo do parâmetro for texto, o tradutor acrescentará um apóstrofo (‘) antes e depois do conteúdo. Se o parâmetro contiver a palavra SANKHYA, a tradução seria **(‘SANKHYA’)**.

Existem algumas variantes do **":"**, que são:

![Imagem 144: Existem algumas variantes do ":" , que são:](https://ajuda.sankhya.com.br/hc/article_attachments/4985233560599)

#### Parâmetros Internos

Existem parâmetros internos do sistema que podem ser utilizados nas consultas e expressões. São eles:

**CODUSU\_LOG** = cód. usuário logado

**CODGRU\_LOG** = cód. grupo usuário logado

**CODPARC\_B2B** = cód. parceiro B2B

**CODVEN\_LOG** = cód. vendedor logado

Todos estes parâmetros são do tipo Número Inteiro.

**Nota:** o tipo **"Entidade/Tabela"** irá gerar nos filtros do Dashboard campos com opção de pesquisa, como mostra a imagem a seguir:

É possível definir um tempo de atualização automática do gadget.

**Nota:** ao utilizar o parâmetro Multi list, o tipo de expressão for SQL, e este retornar um resultado com mais de mil valores, deve-se editar o Tipo no Editar Consulta/Expressão e adicionar o delimitador **"/\*Incolletion\*/"**. Desta forma, observa-se o exemplo em que antes da inclusão do delimitador tem-se a expressão:

```
SELECT CODPARC, NOMEPARC, TIPPESSOA, CODCID FROM TGFPAR WHERE CODCID
 in :P_CODCID
```

Depois da edição deste, nota-se:

```
SELECT CODPARC, NOMEPARC, TIPPESSOA, CODCID FROM TGFPAR WHERE /*inCollection*/
CODCID in :P_CODCID/*inCollection*/
```

**Importante:** quando o parâmetro retornar um resultado com mais de mil valores, a inserção do delimitador será obrigatória.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Configurações

Nesta aba serão informadas as configurações mais rígidas do componente; uma vez que estas sejam salvas gadget, sempre que este for executado estas configurações serão apresentadas, não sendo necessário informá-las novamente.

![EVO103](https://ajuda.sankhya.com.br/hc/article_attachments/360061011054)

Os campos desta aba são similares aos apresentados na aba **"Parâmetros"**, diferenciando-se pela possibilidade de informar um **"Valor Padrão"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Variáveis

Aqui são informadas as Variáveis locais que serão utilizadas no gadget. As variáveis poderão ser de dois tipos, **"SQL"** ou **"Java BeanShell"**.

#### SQL

Esta opção conta com o **"Assistente"** de query do sistema, que visa auxiliar aos usuários na construção da query.

![EVO104](https://ajuda.sankhya.com.br/hc/article_attachments/360061011074)

#### Assistente

Através da uma pesquisa e seleção, o usuário compõe a query nesta aba, como pode-se visualizar no exemplo abaixo. Inicialmente, seleciona-se a **"Tabela"**:

![EVO105](https://ajuda.sankhya.com.br/hc/article_attachments/360061011094)

Ao selecionar uma Tabela, todas as outras tabelas ligadas a esta tabela principal serão apresentadas no painel. Observe a imagem a seguir:

![EVO106](https://ajuda.sankhya.com.br/hc/article_attachments/360061011114)

Depois de selecionada a Tabela, os **"Campos"** pertencentes à esta tabela serão apresentados no painel ao lado. Podem-se selecionar todos os campos da tabela para compor a query ou apenas os desejados; além disso, pode-se depois de selecionar os campos, criar **"Filtros"** específicos para alguns deles.

![EVO107](https://ajuda.sankhya.com.br/hc/article_attachments/360061011134)

O **"Parâmetro"** utilizado na aba Filtros pode ser associado, pelo nome, a outro parâmetro já criado pelo usuário, ou seja, bastará informar o nome de um parâmetro criado anteriormente para que o sistema faça a ligação entre eles. Se o usuário desejar colocar vários gadgets em um mesmo Dashboard e todos eles precisarem de um mesmo **"Parâmetro"**, por exemplo, **"CODUSU"**, é interessante colocar todos com o mesmo nome, pois quando o Dashboard for renderizado, será renderizado apenas um parâmetro que será utilizado em todas os gadgets.

Na criação de uma query (consulta SQL) cujo objetivo final é a geração de dados para montagem do Gadget, pode-se informar o parâmetro variável da seguinte maneira:

```
:#PARAMETRO
```

Esta maneira é a mais recomendada, por ela realizar o auto preenchimento das ' ' (aspas) corretas de acordo com o tipo do valor do parâmetro.

Pode-se também utilizar ':@' para representar um parâmetro, onde este possui também as seguintes funcionalidades:

- Autopreenchimento correto do SQL quando os valores forem NULOS;
- Autopreenchimento das aspas corretas quando os valores forem DATA;

Vale salientar que na utilização desta forma quando se trata de string, deve-se informar ' ' (aspas) antes e depois do parametro - **':@PARAMETRO'**.

A utilização do :@ ou :# visa melhorar a performance da query, pois elas realizam a substituição direta dos valores na query. Para utilizar a nova forma de parâmetro :#, vejamos o seguinte exemplo:

```
SELECT * FROM TSICID WHERE DTALTER > :#DTALTER
```

As outras formas de criação da query, com **":"** ou **":@"**, funcionam da seguinte maneira:

```
SELECT * FROM TSICID WHERE DTALTER > :DTALTER

SELECT * FROM TSICID WHERE NOMECID = ':@DTALTER'
```

#### Avançado

![EVO108](https://ajuda.sankhya.com.br/hc/article_attachments/360061011154)

Pode-se construir a query diretamente nesta aba sem nenhuma assistência ou mesmo visualizá-la já montada com a ajuda do assistente.

**Importante:** caso o usuário informe uma query diretamente nesta aba, o assistente para criação de query será desativado e o usuário ficará por sua conta. Neste caso, o sistema irá reconhecer a query informada nesta aba e todas as manipulações necessárias nesta query serão feitas sob responsabilidade exclusiva do usuário, que fará os ajustes diretamente na query. Ou seja, o sistema não mais auxiliará o usuário na edição da query, contudo o funcionamento permanecerá o mesmo.

Na configuração de expressão dos componentes do dashboard, pode-se utilizar variáveis como parâmetros da query configurada. Vejamos abaixo um exemplo da utilização da variável CODEMP:

```
SELECT CODUSU, NOMEUSU, CODEMP FROM TSIUSU WHERE CODEMP = :COD OR CODEMP =
 :CODEMP
```

#### Resultado

Esta aba possibilita ao usuário testar a query criada antes de utilizá-la no novo gadget. Como se trata apenas de um teste, o resultado é limitado a 20 linhas para que não haja sobrecarga no banco de dados.

![EVO109](https://ajuda.sankhya.com.br/hc/article_attachments/360061011174)

#### Java BeanShell

![EVO110](https://ajuda.sankhya.com.br/hc/article_attachments/360061933613)

O **"Java BenShell"** representa outra forma de criação de uma expressão variável, que constitui um trecho de código Java mais simplificado, digitado diretamente nesta área. Esta forma de criação de variáveis dispensa o auxílio do assistente.

Trouxemos dois exemplos:

**1.**

```
void addColumn(String name, String type, String description){
ui = uiElement();
meta = ui.getChild("metadata");
if( meta == null){
meta = new org.jdom.Element("metadata");
ui.addContent( meta );
}

f = new org.jdom.Element("field");
f.setAttribute("name",name);
f.setAttribute("label",description);
f.setAttribute("type",type);
f.setAttribute("visible","true");
f.setAttribute("useFooter","false");

meta.addContent(f);
}

void initMetadata(){
addColumn("CODPROJ","I","Cód.Projeto");
addColumn("NOMEPROJ","S","Nome Prj");
addColumn("TAMANHO","I","Tam");
addColumn("KANBAN","S","Kanban");
addColumn("DHENTRADA","T","Dh.Entrada");
addColumn("DHENTREGA","T","Dh.Entrega");
addColumn("DIAS","I","Dias");
addColumn("ANALISTA","S","Analista");
addColumn("DHINIANALISE","T","Ini.Análise");
addColumn("DHFIMANALISE","T","Fim.Análise");
addColumn("DEV","S","Dev");
addColumn("DHINIDEV","T","Ini.Dev");
addColumn("DHFIMDEV","T","Fim.Dev");
addColumn("QA","S","QA");
addColumn("DHINIQA","T","Ini.QA");
addColumn("DHFIMQA","T","Fim.QA");
addColumn("VALIDADOR","S","Validação");
addColumn("DHINIVAL","T","Ini.Val");
addColumn("DHFIMVAL","T","Fim.Val");
}

initMetadata();

return var("_vprojects");
```

**2.**

```
import java.math.BigDecimal;

int qtdSaidas = ((BigDecimal) var("QTD_SAIDAS")).intValue();

Collection linhas = new ArrayList();
linhas.add(new Object[]{ "Qtde. Saídas", qtdSaidas, qtdSaidas });
return linhas;
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Argumentos

![EVO111](https://ajuda.sankhya.com.br/hc/article_attachments/360061011194)

Os Argumentos são compostos por um **"Id"** e um **"Tipo"**; estes são parâmetros de entrada de um nível para outro, ou seja, parâmetros de passagem. Deste modo, pode-se criar um gadget que no primeiro nível exiba, por exemplo, "Vendas por Vendedor", sendo que ao dar um duplo clique sobre algum vendedor apresentado no gráfico, sejam apresentadas as vendas deste vendedor em outra grade, logo, o código deste vendedor que permitiu passar do primeiro pro segundo nível seria um exemplo de **"Argumento"**.

Ao contrário das demais abas da opção **"Design"** que são definidas por "gadgets", os Argumentos são definidos por **"nível"**, ou seja, o Argumento será válido apenas para o nível que foi definido.

O botão **"Nível"** permite ao usuário tanto editar o nome do nível, quanto navegar pelos diversos níveis de um gadget.

![EVO112](https://ajuda.sankhya.com.br/hc/article_attachments/360061011214)

Os botões ![clip4290](https://ajuda.sankhya.com.br/hc/article_attachments/360061011234) permitem a inserção e exclusão dos níveis, respectivamente.

Podemos ainda, lançar o Argumento na tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354) no registro que você desejar. Para tal ação, selecione o argumento NUARQUIVO na tela Construtor de Componentes de BI e, ao clicar na linha desejada o Dahsboard será direcionado especificamente ao registro desejado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Eventos - Gráficos

Nos gráficos, os eventos são definidos por **"Séries"**, cada uma das séries apresentará o botão **"Evento"**, que acionará a tela de edição de eventos, através da qual o usuário definirá o comportamento de cada componente quando este for acionado no Dashboard, como por exemplo, quando sob a ação de um duplo clique.

![EVO113](https://ajuda.sankhya.com.br/hc/article_attachments/360061011254)

Ao acionar o botão **"Evento"** é aberta a tela de edição de eventos que conta com duas possibilidades, **"Abrir um novo nível"** ou **"Lançar uma tela do sistema"**.

Optando por **"Abrir um novo nível"**, serão apresentados os níveis já criados para o componente. Selecionando-se um destes níveis, se houver um **"Argumento"** vinculado a ele, este também será apresentado e o usuário associará a variável ou campo ao argumento, pela coluna **"Valor"**.

Sendo que, se tratando de um gadget com por exemplo 3 (três) níveis, o terceiro nível já herda todas as variáveis que foram passadas como argumento do primeiro para o segundo nível. Deste modo, torna-se mais adequado a utilização das variáveis herdadas evitando assim a criação de novas variáveis com os mesmos valores.

Por meio da opção **"Lançar uma tela do sistema"**, configura-se o componente para que este abra a partir do Dashboard, qualquer tela ou Dashboard do Sankhya Om através de um duplo clique. Isto poderá ser feito tanto em valores, quanto em uma linha na grade, uma coluna ou barra ou ainda um campo, a configuração é livre.

![EVO114](https://ajuda.sankhya.com.br/hc/article_attachments/360061011274)

No editor de eventos seleciona-se a tela ou Dashboard que se deseja vincular ao componente. A **"PK"** da tabela principal da tela selecionada será apresentada no **"Argumento"**, permitindo ao usuário associar a esta através do **"Valor"**, uma variável local do "gadget"; deste modo, a tela será aberta posicionada no registro que está sendo analisado.

**Observações:**

1. **"PK"** é o mesmo que chave primária. Resumidamente chave primária é o conjunto de campos da tabela que identificam unicamente uma linha, ou seja, nenhuma outra linha da tabela terá valores repetidos para esta coluna. Um exemplo, é o cadastro de parceiros que terá como chave primária o campo Código do Parceiro, pois não existirão outros iguais.
2. No momento da visualização do Dashboard, uma tela só será efetivamente aberta, se o usuário logado possuir pelo menos permissão de visualização para a tela.

Na Aba **"Atualizar detalhes"** é possível configurar para que o controle corrente force a atualização de um outro controle vinculado a ele.

![EVO115](https://ajuda.sankhya.com.br/hc/article_attachments/360061933633)

Nesta aba serão listados os controles que estão no mesmo nível do controle selecionado. Para fazer o vínculo, basta marcar um ou mais componentes que serão atualizados. Existe a possibilidade de passar grandezas do componente mestre como argumentos para a atualização. Os argumentos são informados na grade localizada logo abaixo da lista de componentes. Nesse caso, esses argumentos serão inseridos diretamente no ambiente dos componentes selecionados, podendo esses argumentos serem utilizados na query/expressão do componente detalhe. Vejamos um exemplo:

Suponhamos um componente com dois elementos em um nível, uma tabela de parceiros e um gráfico em pizza agrupado por segmento de atuação. Ao clicar em uma das "fatias da pizza", a tabela é atualizada, buscando os parceiros correspondentes àquele segmento em que o clique aconteceu. Neste exemplo, o componente mestre é o Gráfico de Pizza, e é nele que o Evento deve ser configurado, marcando-se na aba **"Atualizar detalhes"** a opção correspondente a tabela e passando os argumentos necessários para atualização do componente detalhe; neste caso esse argumento seria o "Segmento de atuação".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Eventos - Controles/Tabela

Nos componentes do tipo **"Tabela"** o evento é único e será acionado também pelo botão **"Evento"**. Neste caso, o evento será definido de acordo com a linha da tabela que será acionada.

![EVO116](https://ajuda.sankhya.com.br/hc/article_attachments/360061011294)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Eventos - Controles/Valor

No caso dos componentes do tipo **"Valor"** pontual, o evento será reenderizado como um **"link"**.

![EVO117](https://ajuda.sankhya.com.br/hc/article_attachments/360061011314)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Quadrante Expressão

No quadrante Expressão, são realizadas definições essenciais para a geração dos dados no Dashboard. Inicialmente determina-se o Tipo a ser trabalhado; as explicações a respeito deste aspecto, bem como dados a respeito do assistente de montagem de query aberto com o acionamento do botão **"Editar"**, podem ser visualizadas por meio do link [Variáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#variveis).

Ao salvar a expressão o sistema irá reconhecer os campos da query ou código que aquela expressão retorna e informar todos eles na grade, permitindo a redefinição dos **"Tipos"** ou edição da **"Descrição"**.

![EVO119](https://ajuda.sankhya.com.br/hc/article_attachments/360061011334)

**Nota:** o Controle do tipo **"Valor"** suporta HTML do tipo simplificado (tamanho, cor, fonte e imagem).

Em seguida tem-se os seguintes botões:

![clip7480](https://ajuda.sankhya.com.br/hc/article_attachments/360061011354) **Assistente de edição de campos calculados** - Será aberto o pop-up denominado **"Editar Campos Calculados"**, onde tem-se a possibilidade de configurar-se cálculos personalizados com valores de outros campos, além de concatenar informações como o nome de uma cidade e seu respectivo estado;

![clip7481](https://ajuda.sankhya.com.br/hc/article_attachments/360061933653) **Assistente de edição de máscara** - Ao utilizar análises do tipo Linhas, Barras e Colunas, poderemos utilizar máscaras para formatação dos valores do eixos. O campo para informar a máscara estará disponível para eixos do tipo Valor. A máscara pode ser digitada diretamente no campo, ou pode ser editada clicando-se neste botão, onde será aberto o pop-up **"Editar Máscara"**;

![clip7482](https://ajuda.sankhya.com.br/hc/article_attachments/360061933693) **Formatação condicional** - O recurso de Formatação Condicional possibilita a definição de uma ou mais Regras de formatação, sendo que quando a regra for verdadeira será aplicada na célula respectiva ao campo selecionado. Pode-se personalizar a cor de fundo, o estilo da fonte entre negrito e/ou itálico de células específicas. A referida formatação só está disponível para o componente **"Tabela"**, nos campos do tipo **"Inteiro"**, **"Moeda"**, **"Decimal"**, **"Data"** e **"Data e Hora"**. Ao clicar no recurso será aberto o pop-up **"Editar Formatação Condicional"** para ajustes na formatação condicional.

![clip7483](https://ajuda.sankhya.com.br/hc/article_attachments/360061011374) **Assistente de Formatação e Agregação** - Ao editar e/ou inserir uma Expressão SQL, nos campos do tipo Inteiro, Decimal ou Moeda, pode-se efetuar a configuração de agregação de valores através da coluna **"Agregador"**, que irá apresentar tais informações no rodapé da grade do componente gerado. A coluna Agregador, é utilizada em substituição a coluna Totalizar. Pode-se escolher as seguintes funções de agregação:

- Maior;
- Menor;
- Média;
- Somar;
- Personalizada.

Optando-se pela opção Personalizada, pode-se criar várias particularidades de agregadores para a coluna selecionada. Por meio desta opção, será habilitado o ícone ?, que ao ser acionado, será aberto o pop-up **"Editar Agregadores Personalizados"**, onde será possível informar uma expressão e utilizar valores dos outros campos com funções de agregação dos cálculos retornados.

**Observação:** em componentes de [Tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#controlestabela), na utilização de campos do tipo **"Hora"** também pode-se empregar o uso de funções de agregação para os mesmos (somar, média, mínimo, máximo, personalizado). Esta configuração visa auxiliar nas análises em que tem-se tempo gasto, horas produtivas, orçamento de horas, entre outras possibilidades.

**Importante:** a Formatação de Agregação Personalizada não permite a realização de cálculos matemáticos que fujam das possibilidades disponibilizadas pela Fórmula Personalizada; pode-se trabalhar apenas com a utilização de cálculos com base nos campos pertencentes à consulta. No pop-up Editar Agregadores Personalizados, nas fórmulas utilizadas na expressão, somente são aceitas as variáveis existentes na Seleção de Variáveis; pode-se configurar quantos agregadores forem necessários. O campo Título é utilizado para informar-se uma descrição para o resultado da fórmula do agregador personalizado. O resultado da agregação configurada, é sempre apresentado no Rodapé da Grade. Vejamos um exemplo:

```
SUM(VALOR_VENDA) / SUM(VALOR_CUSTO)
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Pré-Visualização

Outro recurso que favorece a criação do gadget é o botão **"Pré-visualizar"** localizado no canto direito da barra de ferramentas e ao lado do botão **"Outras Opções"** no topo da tela, tanto para a opção **"Design"** quanto para opção **"XML"**.

![EVO120](https://ajuda.sankhya.com.br/hc/article_attachments/360061011394)

Este recurso abrirá o gadget assim como em um Dashboard, possibilitando a visualização do resultado final, permitindo uma noção de como funcionará o Dashboard. Através do botão **"Editar"** localizado no canto superior direito da tela, o usuário que tiver acesso para alterações nesta tela, poderá retornar para edição do Dashboard. Caso o usuário não tenha acesso para alteração nesta tela, este botão não estará disponível.

![EVO121](https://ajuda.sankhya.com.br/hc/article_attachments/360061011414)

Deste modo, o gadget irá rodar sozinho em um Dashboard de visualização, onde pode-se analisar se ele realmente está retornando o resultado esperado.

No ambiente móbile os gráficos são apresentados maximizados automaticamente permitindo a navegação entre gráficos, assim como na versão desktop.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Impressão/Exportação

Componentes do tipo **"Gráfico"** permitem sua impressão através do ícone em forma de engrenagem, onde tem-se a opção **"Imprimir Gráfico"**:

![EVO122](https://ajuda.sankhya.com.br/hc/article_attachments/360061933713)

Componentes do tipo **"Tabela"** possibilitam tanto a exportação como **"PDF"** quanto em **"Planilha Excel"** ou **"Visualizar em Cubo"**.

![EVO123](https://ajuda.sankhya.com.br/hc/article_attachments/360061011434)

Nas tabelas dos Componentes de BI que forem criados, é disponibilizado um botão para apresentação dos dados estatísticos referentes aos campos numéricos exibidos na grade. Para maiores detalhes sobre esta funcionalidade, clique no link [Estatísticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110473).

**Observações:**

1.No editor de dashboard, para que expressões sejam interpretadas como HTML, é necessário que as infomações estejam em um blocoo CDATA no XML, como pode-se notar no exemplo abaixo:

```
<title><![CDATA[Mês negociado<br><br>Junho</br></br>]]></title>
```

2.Nos editores de fonte do Dashboard agora é possível utilizar o CTRL+Z para desfazer uma edição no texto.

3.Ao visualizar o dashboard, no menu lateral de filtros agora é possível aplicar um filtro pressionando a tecla **"Enter"** no teclado.

4.Na edição do XML principal e na configuração das query's dos componentes, pode-se utilizar o botão scroll do mouse (botão de rolagem localizado entre os botões direito e esquerdo), de modo a facilitar a navegação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Ações nos Componentes de BI

Ao realizar a construção de um componente de BI, é possível utilizar as ações vinculadas a uma entidade nos componentes de grid's do construtor e lançar ações através da visualização do dashboard; em poucas palavras, pode-se executar uma ação partindo de um Componente de BI. Para isso realiza-se as seguintes configurações:

- Ao cadastrar um novo componente de BI, preenche-se os campos **"Título"**, **"Categoria"**, **"Ativo"** e **"Descrição"**. Neste caso, o componente deve ser do tipo **"Tabela"**.
- Depois de selecionado o tipo Tabela, clica-se no botão ![clip2024](https://ajuda.sankhya.com.br/hc/article_attachments/360061011454) **"Editar"**, onde define-se um **"Título"** e uma entidade a ser trabalhada.
- Clicando-se na aba **"Expressão"** presente no lado direito da tela, e em seguida no botão **"Editar"**, tem-se a tela **"Editar Consulta/Expressão"**, onde na aba **"Avançado"** informa-se uma query que irá proporcionar um resultado para alimentar a tabela. Além disso nesta aba, pode-se pesquisar dentro do editor de consulta/expressão, por trechos do texto existentes na consulta/expressão criada; para isso, informa-se a palavra desejada no campo de busca localizado na parte superior da tela. Sendo feita alguma modificação, o sistema irá apresentar um pequeno lembrete para possível salvamento das alterações realizadas.
- Na tela **"Configurações > Avançado > Dicionário de Dados"**, pesquisando pelo **"Nome da Instância"**, identifica-se a entidade a ser trabalhada e na aba **"Ações"**, efetua-se a inclusão de uma ação que pode ser do tipo **"Rotina no Banco de Dados"**, **"Script (JavaScript)"**, **"Lançador"** ou **"Rotina Java"**.

Ao visualizar o Componente de BI criado através do botão ![clip2025](https://ajuda.sankhya.com.br/hc/article_attachments/360061933733), pode-se visualizar a ação criada.

**Observação:** na configuração de ações pelo usuário, tem-se a opção de utilizar o parâmetro **"Ordenar ações por ordem alfabética? - ORDENARACOES"** que quando ativado, ordena a visualização das ações por ele criadas em seu correspondente botão de ações de forma alfabética.

**Importante:** ao utilizar a ação de uma entidade vinculada a tabela, os dados que podem ser utilizados são os que estão presentes na entidade relacionada. Não é possível utilizar em um botão de ação, um campo que não esteja nessa entidade relacionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Central de Certificações para Dashboards

Para acessar as informações sobre o processo de inserção das regras pertinentes à [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053) na construção do Dasboard, acesse [Restrição por Dashboard](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#restriopordashboard).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)

## Botão Outras Opções

![EVO124](https://ajuda.sankhya.com.br/hc/article_attachments/360061933753)

A opção **"Dashboards que usam esse componente"** quando acionada, permite visualizar a listagem de todos os dashboards que utilizam determinado componente de BI.

![EVO125](https://ajuda.sankhya.com.br/hc/article_attachments/360061011474)

Ao efetuar um duplo clique em algum item da lista, será aberta a tela de **"Construtor de Dashboard"** posicionando a navegação de registro, no dashboard correspondente ao item clicado.

**Nota:** caso seja necessário, é possível realizar a construção de um componente de BI para ser executado a partir da tela **"Configurações > Consulta > Ficha de Parceiros"** considerando a marcação **"Exibir por Matriz ou Convênio"**. Na criação do Componente de BI, pode ser utilizado o parâmetro EXIBIRMATRIZ correspondente a marcação mencionada na tela Ficha de Parceiros.

Através da opção **"Download Modelo JavaScript Simples HTML5"**, pode-se baixar o modelo de documento html que possui a estrutura de referência que permite a execução de queries em tempo de execução via JavaScript. Os seguintes pontos devem ser observados:

- Este modelo está configurado para receber parâmetros do tipo Data/Hora, Data, MultiList:Text, Periodo, Entidade/Tabela, Texto e SingleList:Text.
- Para o parâmetro do tipo MultiList:Text, se nenhum item é selecionado são retornados todos os registros, então para utilização fixa na query este parâmetro deve ser configurado como obrigatório.
- A consulta pode usar tanto um parâmetro quanto uma combinação de vários parâmetros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI#top)
