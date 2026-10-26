---
id: "360045108573"
titulo: "Relatórios Formatados "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-15T13:30:34Z"
rotulos: ["SQL", "Configuração", "Relatórios Formatados", "Relatórios", "MGE", "relatório", "relatórios", "Formatador de Relatórios", "MGE\\Mitra", "Mitra", "Visualização de Relatórios Formatados no MGE/MITRA", "Relatórios Formatados  manual", "Estoque", "Financeiro", "Gerando Relatórios Personalizados: Uma Abordagem Detalhada", "Banco de Dados"]
---

# Relatórios Formatados 

Um dos principais objetivos de um ERP é fornecer informações detalhadas sobre a situação da empresa, de forma rápida e acessível. Para isso, é necessário organizar os dados obtidos durante o exercício das atividades, agrupando-os de forma conveniente a extrair informações relevantes, aos processos da organização.

A forma tradicional de se obter essas informações é a geração de relatórios. Por exemplo, para saber quantas unidades de um determinado produto foram vendidas no mês passado, será necessário somar a quantidade desse produto, em cada Nota de Venda onde ele apareça, desde que a Data da Venda esteja entre o início e o final do mês passado. Se além do total de vendas desse produto, desejarmos saber o total de cada vendedor, será preciso buscar as vendas de cada um dos vendedores separadamente, criando subtotais.

Existem vários relatórios que são comuns entre empresas, que vão desde relatórios operacionais (relatórios de comissões, relatórios de estoques, relatórios de movimentação financeira etc), até relatórios gerenciais (Margem de contribuição, Análise de giro, Projeção de Faturamento etc). Praticamente todas as empresas, quase sem exceção, utilizam esses relatórios cotidianamente; mas existem alguns relatórios que são mais específicos, a um determinado segmento de mercado, ou até mesmo a uma empresa em particular. Para criar seus próprios relatórios, de forma a atender suas necessidades específicas, as empresas poderão recorrer ao **"Formatador de Relatórios"**.

#### Como funciona o Formatador de Relatórios?

Como os relatórios agrupam os dados, a base desse mecanismo é uma consulta ao Banco de Dados, construída através da linguagem SQL. Essa poderosa linguagem fornece ferramentas, que possibilitam todo tipo de cruzamento entre dados, agrupando-os, comparando-os, executando operações aritméticas, manipulando esses dados, de acordo com as informações a se obter.

#### Quem utiliza?

Existem dois (ou três) perfis de usuários para essa ferramenta. Os usuários que apenas geram os relatórios a fim de extrair informações, e os usuários com habilidades técnicas e conhecimento sobre o Banco de Dados, capazes que cruzar os dados para criar relatórios.

**Nota:** embora em geral este segundo usuário seja capaz de montar qualquer tipo de relatório, pode existir a demanda por um consultor, que consegue enxergar de forma mais clara os relacionamentos entre os dados, criando novas formas de acesso a estes. Veremos isso de forma mais detalhada na sessão **"Manutenção de campos"**.

#### Visão prática da ferramenta

O banco de dados do sistema está organizado de forma tabular, ou seja, estruturado em campos, pertencentes a tabelas. Sempre que você deseja obter informações junto ao banco de dados, monte uma consulta SQL, que partirá de uma dessas tabelas, eventualmente juntando informações de outras tabelas através de ligações. Assim, para o exemplo citado acima, partimos da tabela onde as vendas estão armazenadas (TGFCAB), e ligamos à tabela onde cada item da nota está gravado (TGFITE). O resultado dessa consulta é fornecido pelo Banco de Dados como uma coleção de registros, onde cada registro irá conter as colunas de ambas as tabelas. Para reduzir a quantidade de registros é necessário fornecer critérios de consulta, que filtram o resultado. Deve-se então, criar um filtro para que sejam retornadas apenas notas do tipo venda (TGFCAB.TIPMOV = 'V') e que tivessem sido confeccionadas no mês passado (consideremos março de 2015, então, TGFCAB.DTMOV >= '01/03/2015' AND TGFCAB.DTMOV <= '31/03/2015').  Esta é a forma de interação do sistema com o Banco de Dados.

Para facilitar a construção dessas consultas e viabilizar a organização dos resultados, o **"Formatador de Relatórios"** usa estruturas básicas pré-cadastradas, que mapeiam os relacionamentos entre as tabelas, rotulando essas estruturas como **"Campos de relatório"**. Esses campos fornecem as informações necessárias para montar a consulta SQL de forma automática, além da forma de exibir os resultados. Existem vários formatadores de relatórios e cada formatador possui um cadastro de campos. Na prática, esses campos podem (e devem) ser usados em mais de um relatório. Quando o Sankhya-Om é instalado, já existe um conjunto básico de campos cadastrados e na sessão **"Manutenção de Campos"** veremos como alterá-los ou criar novos campos.

A tela do formatador é semelhante em todos os módulos em que é acionada, diferenciando-se pelos campos que são apresentados para cada tela, ou seja, no relatório de Parceiros, são apresentados os campos relacionados aos Parceiros, no relatório de Produtos, os campos ligados aos Produtos, e assim sucessivamente; a tela possui três modos de operação: **"Visualizador de relatórios"**, **"Edição de relatórios"** e **"Grade de dados"**. Tomemos como exemplo para entendimento, a tela **"Comercial > Relatórios > Entradas e Saídas"**.

**1 -Visualizador de relatórios**

À medida que os relatórios são criados, estes precisam ser disponibilizados aos usuários, isso é feito no modo padrão do formatador. Cada relatório está listado de forma hierárquica, permitindo que sejam agrupados por afinidade.

![Imagem 1: À medida que os relatórios são criados, estes precisam ser disponibilizados aos usuários, isso é feito no modo padrão…](https://ajuda.sankhya.com.br/hc/article_attachments/4835458171287)

Com um relatório selecionado, clicando nos botões disponíveis pode-se:

- **Visualizar Relatório –** É o momento em que o sistema organiza os dados do relatório em um arquivo em formato **"pdf"**, podendo  ser visualizado, enviado por e-mail, salvo ou impresso. Além deste botão, o relatório também poderá ser visualizado por meio de um duplo clique no item da árvore.

**Observação:** você poderá verificar maiores informações sobre o envio de e-mails acessando o tópico [Conhecendo o Sankhya-W/Envio de Relatórios por E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934).

Sempre que um relatório é executado, para assegurar mais agilidade na próxima execução, o sistema guarda em memória uma espécie de "gabarito" do relatório, tornando essa segunda execução mais rápida. Contudo, os relatórios disponíveis nessa ferramenta são compartilhados com outros sistemas (MGE, Mitra e Jiva G1) e eventualmente (se o relatório foi editado em algum desses outros sistemas) esse "gabarito" poderá estar desatualizado. Assim, existe a opção **"Descartar Cache"**, sendo que na maioria dos casos não é necessária.

- **Visualizar Grade** **–** Trata-se de uma forma alternativa de se obter os dados da consulta. Ao invés de emitir o relatório, o modo **"Grade de dados"** é acionado.

![Imagem 2: Visualizar Grade – Trata-se de uma forma alternativa de se obter os dados da consulta. Ao invés de emitir o relatório,…](https://ajuda.sankhya.com.br/hc/article_attachments/4835681282071)

Nesse modo, como em quase todas as grades do sistema pode-se exportar os dados da grade através do botão ![Imagem 3: Nesse modo, como em quase todas as grades do sistema pode-se exportar os dados da grade através do botão para um "Cubo"…](https://ajuda.sankhya.com.br/hc/article_attachments/16746763626775) para um **"Cubo"**, uma planilha em Excel ou em arquivo **"PDF"**. O botão **"Voltar"** retornará ao modo **"Visualizador de relatórios"**.

**2 -Estrutura de organização (Grupos de relatórios)**

Pode-se entender que os relatórios estão agrupados por um critério (afinidade, processo, nível etc). Para permitir que cada empresa defina esse critério de agrupamento, existe um cadastro de grupos de relatório, responsável por criar as "pastas" onde os relatórios serão anexados.

O cadastro de grupos **"(Configurações > Cadastros > Grupo de relatórios)"** é compartilhado entre todos os formatadores e funcionará, exatamente, como outros cadastros hierárquicos do sistema. 

**3 -Edição/Criação de relatórios**

No modo **"Edição de relatórios"**, a tela permite que sejam montados relatórios de forma simples e rápida. Isso é feito informando-se o nome do relatório, o grupo (pasta) ao qual ele deve ser anexado na visualização e um conjunto de campos, além de outras informações adicionais como filtros e outros detalhes, que serão vistos adiante. As informações estão dispostas em abas, para facilitar a montagem do relatório. Vejamos:

#### 3.1 -Seleção de campos

Na área, **"Disponíveis"**, localizada na lateral esquerda da tela, é apresentada uma listagem de todos os campos ligados àquela tela do formatador (no nosso exemplo, Entradas e Saídas). Os campos, assim como os relatórios também poderão ser agrupados, mas a forma de agrupá-los é ligeiramente mais simples e será discutida no tópico **"Manutenção de campos"**. As tarefas básicas da aba **"Campos"** são selecionar os campos, definir a ordem das colunas no relatório, definir quebras (entendamos as quebras como agrupadores de informações), definir a ordem dos registros e adicionalmente é onde edita-se os campos (também discutido em "Manutenção de campos").

#### 3.1.1 -Selecionados

Você poderá adicionar campos a esta lista, arrastando os itens da árvore de **"Disponíveis"** ou através do botão  localizado entre as duas listas. Para removê-los, utilize do mesmo procedimento de arrastar (dessa vez da lista para a árvore) ou através dos botões  ou . Além disso, a ordem definida por essa lista será empregada para organizar os campos no relatório/grade. Neste trecho, a ordem também pode ser definida arrastando os itens ou utilizando os botões  e  disponíveis no topo da lista.

#### 3.1.2 -Ordenação e Agrupamento

Qualquer campo que esteja presente na lista de **"Selecionados"**, pode ser usado para definir a ordem em que os registros serão apresentados (pensemos nisso como o "ORDER BY" da consulta SQL). Da mesma forma que a lista de **"Selecionados"**, pode-se arrastar os campos ou utilizar os botões para adicionar/remover, mas a ordenação desta lista só pode ser feita pelos botões  e .

Os quatro primeiros campos da lista de ordenação podem ser definidos como **"Quebra"** do relatório. Para isso, cada um deles possui um "checkBox" na coluna **"Agrupar"**. Funciona da seguinte forma:

Digamos que exista um relatório de **"Comissão de Vendedores"** e os campos desse relatório sejam, **"Código do Vendedor"**, **"Apelido do Vendedor"**, **"Total de Vendas"**, **"Percentual de Comissão"** e **"Valor da Comissão"**; se você quiser organizar os registros **"por vendedor"**, deve-se então colocar na lista de ordenação o **"código"** ou o **"apelido do vendedor"** (o que for mais conveniente). Assim, todos os registros referentes àquele vendedor serão exibidos sequencialmente. Marcando o campo como quebra, instruímos o mecanismo de relatórios a criar uma **"sessão"** nova sempre que o valor daquele campo mudar. Quando um campo é marcado como quebra, outro checkBox na coluna **"Saltar página"** será habilitado e quando marcado, sempre que uma nova sessão ocorrer, a impressão dela será no topo de uma nova página.

Além disso, no topo da lista quando marcada a opção **"Reimprimir quebra após salto de página?"**, sempre que uma sessão não couber dentro da página, que começou a ser impressa, os detalhes da sessão serão reimpressos no começo da página seguinte. Essa marcação serve para todas as quebras.

Ainda sobre quebras, usando o botão ![Imagem 4: Ainda sobre quebras, usando o botão , disponível em cada um dos campos onde é possível marcar quebra, será possível…](https://ajuda.sankhya.com.br/hc/article_attachments/4847335350935), disponível em cada um dos campos onde é possível marcar quebra, será possível imprimir outros campos, no cabeçalho de cada grupo.

#### 3.2 -Expressão de filtro

Nesta sessão defina quais entre todos os registros existentes no Banco de Dados, devem ser utilizados como filtros no relatório. Isso é um requisito crítico de qualquer relatório, pois é assim que identifica-se, por exemplo, se um registro da tabela TGFCAB é uma "Nota de Venda". Além disso, o volume de informações exibidas deve ser adequado, ao consumo dessas informações. Uma quantidade muito grande de registros pode degradar o desempenho do servidor de banco de dados e/ou do servidor de aplicação.

A forma de definir o filtro é simples. Do lado esquerdo, está disponível a árvore com todos os campos do formatador. Na prática, mesmo um campo que não esteja selecionado em um relatório, poderá pertencer ao filtro (isso quase sempre acontece).

Selecionando-se e arrastando um campo para o painel **"Expressão de Filtro"**, escolha um tipo de comparação para ser utilizado neste, isto é, um critério.

[GIF animado: Imagem 5: Selecionando-se e arrastando um campo para o painel "Expressão de Filtro" , escolha um tipo de comparação para ser…](https://ajuda.sankhya.com.br/hc/article_attachments/4847463285143)

São eles:

- > **maior que:** Compara o valor do campo com algum valor e retorna verdadeiro quando maior.
- < **menor que:** Compara o valor do campo com algum valor e retorna verdadeiro quando menor.
- = **igual a:** Verdadeiro se for o mesmo valor.
- >= **maior igual a:** Verdadeiro se maior ou igual.
- <= **menor igual a:** Verdadeiro se menor ou igual.
- <> **diferente de:** Verdadeiro se não for igual.
- LIKE '%abc%' **contendo:** O argumento fornecido deve estar contido no valor do campo (usado em campos do tipo Texto).
- LIKE 'abc%' **começando com:** Verdadeiro caso o início do campo seja igual ao argumento passado.
- LIKE '%abc' **terminando com:** Verdadeiro se o final do campo for igual ao argumento passado.
- IS NULL **vazio:** Verdadeiro se o campo não estiver preenchido.

Existem duas formas de definir o valor de referência, para comparação com os campos. A primeira é usando um argumento literal, explicitamente digitado no campo de texto disponível na aba. Outra forma, é deixar que sejam informados esses valores no momento da execução do relatório. Para isso, marque a opção **"Variável"**; assim, quando o relatório for executado, uma pequena janela será apresentada, solicitando que sejam informados os valores de cada parâmetro variável.

Caso exista mais de um critério, será necessário definir um "elo" de ligação, entre eles. Por exemplo, **"deseja-se que o "Tipo de Movimento" da nota seja venda ou pedido de venda"**; neste caso, a ligação "ou" faz com que a expressão seja verdadeira quando qualquer uma das duas perguntas for positiva. Mas poderia ser também, "eu desejo que a data de movimento seja maior que 01/12/2015 e menor que 31/12/2015"; nesse caso o registro só será usado caso sua data atenda aos dois requisitos.

Com todos os campos preenchidos, ao clicar em **"Adicionar"**, o critério é incorporado à expressão e mostrado no campo de texto amplo que está logo abaixo. Aliás, esse campo permite que usuários, que estejam mais familiarizados com essa estrutura, editem a expressão de forma direta, sem auxílio dos recursos descritos anteriormente.

#### 3.3 -Aba Configurações

Nessa aba todos os detalhes do relatório serão definidos. São eles:

**Imprimir detalhes:** Quando desmarcado, omite a impressão dos registros, imprimindo somente o cabeçalho, as quebras e rodapés.

**Imprimir totais:** Se marcado, no rodapé de cada quebra serão impressos os totais de cada coluna numérica, e no rodapé do relatório, o total de todos os registros.

**Imprimir contador de registros:** Permite imprimir a quantidade de registros que existem em cada quebra. Também ao final do relatório, a quantidade total.

**Eliminar duplicidades:** Impede que dois registros iguais sejam impressos.

**Orientação do relatório:** Esta opção define se o relatório será impresso em modo "Retrato" (forma vertical), ou "Paisagem" (forma horizontal).

**Imprimir Logomarca:** Possibilita a impressão de uma imagem no cabeçalho do relatório. Quando marcado, habilita todos os campos relativos a essa imagem. São eles:

- **Arquivo:** Trata-se do nome do arquivo que deve ser usado. O arquivo pode ser escolhido através do botão ![Imagem 6: Arquivo : Trata-se do nome do arquivo que deve ser usado. O arquivo pode ser escolhido através do botão , que abrirá…](https://ajuda.sankhya.com.br/hc/article_attachments/4847618153495), que abrirá uma lista com todos os arquivos do tipo de imagem disponível, no diretório de modelos ou pelo caminho do repositório de dados. Exemplo: **"Repo://Relatorios/1355\_logo.png"**.

**Nota:** os relatórios são compatíveis entre os sistemas Sankhya-Om, Jiva-W, MGE, Mitra e G1. Esse tópico é incompatível entre sistemas que rodam em ambiente de servidor (Sankhya-Om e Jiva-Om) e sistemas que rodam na máquina do usuário (MGE, Mitra e G1), pois os arquivos que estão na máquina do usuário, não são acessíveis pelo servidor. Assim, para permitir que relatórios feitos em um dos sistemas "Desktop" rodem em ambiente "Servidor", é necessário manter uma cópia do arquivo na pasta de modelos (vide documentação específica), bastando usar o mesmo nome do arquivo local.

Exemplo: **"C:\Meus documentos\imagens\logo\_empresa.bmp"** ou **"\\algum\_lugar\_na\_rede\imagens\logo\_empresa.bmp"**; para os dois casos, se houver um arquivo no diretório de modelos chamado **"logo\_empresa.bmp"**, este será automaticamente usado. No caso de não existir, uma logo padrão será colocada no lugar da imagem. Também é importante mencionar que quando esse campo é alterado por um sistema **"Servidor"**, a propriedade é mantida inalterada no ambiente **"Desktop"**.

- **Ajustar tamanho da imagem para largura e altura:** Se marcado, altera o aspecto da imagem, para ajustá-la de acordo com o tamanho definido nos campos altura e largura. Caso contrário, assume a dimensão que melhor se ajuste ao tamanho real da imagem e calcula proporcionalmente a segunda dimensão.
- **Altura:** Determina o tamanho que a imagem deve ter na vertical.
- **Largura:** Determina quanto espaço deve ocupar na horizontal.
- **Distância:** Responsável pelo espaço entre a imagem e os textos impressos no cabeçalho do relatório.

**4 -Manutenção de campos**

Os campos de relatórios são estruturas básicas pré-cadastradas, que mapeiam os relacionamentos entre as tabelas. As tarefas de definir e alterar os campos são reservadas a usuários que têm habilidades de "Banco de Dados" e uma ampla visão das tabelas, que o sistema utiliza para gravar as informações (normalmente consultores).

Na aba **"Campos"**, acima da árvore de campos disponíveis, existe um botão que dá acesso ao modo ![Imagem 7: Na aba "Campos" , acima da árvore de campos disponíveis, existe um botão que dá acesso ao modo "Manutenção de campos" .…](https://ajuda.sankhya.com.br/hc/article_attachments/16746763628567) **"Manutenção de campos"**. Quando esse modo está ativo, as listas **"Selecionados"** e **"Ordenação e Agrupamento"** darão lugar ao seguinte formulário:

[GIF animado: Imagem 8: Na aba "Campos" , acima da árvore de campos disponíveis, existe um botão que dá acesso ao modo "Manutenção de campos" .…](https://ajuda.sankhya.com.br/hc/article_attachments/4847661043479)

Pode-se alterar qualquer um dos campos do formatador, excluí-los ou incluir novos.

**Nota:** devemos ter muita cautela ao remover campos, pois por questões técnicas não é possível determinar de forma rápida em quais relatórios ele é utilizado. A remoção de um campo compromete o funcionamento de todos os relatórios que o utilizam.

Existem dois tipos de campos, os campos comuns, usados para montar o relatório e outros campos, que têm finalidade de organizá-los de forma hierárquica. Campos usados com esse propósito são marcados como **"Só Hierarquia"**. Assim, ao criar um campo, pode-se dizer em que parte da árvore, deseja-se que ele apareça, através do campo **"Cód.Campo Pai"**. Os campos que não tem valor informado nesse campo aparecerão no primeiro nível da árvore, sendo possível criar quantos níveis forem necessários. Os demais atributos do campo são:

**Cód. Único:** Campo do sistema, gerado automaticamente.

**Cód. Campo:** Campo do sistema, gerado automaticamente.

**Descrição:** Identificação do campo. Deve-se utilizar um nome sugestivo e que evite ambiguidades, pois em muitos casos é a forma mais rápida de saber do que se trata.

**Tipo:** É apresentada uma listagem com os tipos de dados que representam o campo. Teremos os seguintes tipos:

- Letras;
- Data;
- Data/Hora;
- Dinheiro;
- Imagem;
- Inteiro;
- Lista;
- Memo;
- Número;
- Rich Text.

**Alinhamento:** Determina como o texto deve ser alinhado, no espaço reservado para o campo no relatório.

**Tamanho:** Utilizado para calcular o tamanho reservado no relatório, para este campo.

**Máscara:** Permite determinar a forma como os dados serão impressos no relatório.

**Zerar na quebra:** Campos numéricos podem ter **"totalizadores nas quebras"**. Um campo que tenha esse atributo marcado, irá começar um novo total a cada quebra.

Existem outros três campos que são os responsáveis por determinar como o gerador de relatórios deve obter os dados. Imaginemos que você gostaria de obter o Tipo de Movimento de uma nota. A consulta necessária para obter essa informação é a seguinte: **SELECT CAB.TIPMOV FROM TGFCAB CAB**

**Expressão:** Parte da consulta que corresponde à coluna na tabela de origem. No exemplo acima, seria preenchido com: **CAB.TIPMOV**.

**Tabelas:** Trata-se da parte da expressão correspondente ao "FROM" da consulta. Determina qual tabela contém os dados desejados.

**Ligação:** Eventualmente, podem existir (normalmente existem) campos de tabelas distintas; nesses casos, o conteúdo destes determina como o relacionamento entre as tabelas será resolvido. Nosso campo pertence à tabela TGFCAB e no módulo comercial, podemos considerar essa tabela como o coração do módulo, afinal nela são guardadas as informações de compras, vendas, transferências etc. Ela serve de "base" para os relatórios do módulo comercial e portanto, é por ela que o mecanismo de relatórios começa a montagem da consulta. Os campos mapeados para ela não devem ter valor para a ligação. Se o campo estivesse em outra tabela, por exemplo, na **TGFITE**, o valor seria **ITE.NUNOTA = CAB.NUNOTA**, de modo que ao montar a consulta, o "WHERE" contivesse a ligação entre a tabela base e a tabela a qual o campo pertence.

#### 5 -Relatórios personalizados

Com base no que foi descrito até aqui, o gerador de relatórios é capaz de montar um relatório em um formato "padronizado", onde os registros serão impressos em forma de colunas, o que atende à grande maioria dos casos. Contudo, algumas vezes precisa-se interferir na distribuição da informação, na área onde ela deve ser impressa. Para isso, o layout (chamemos assim o formato em que o relatório é impresso) pode ser convenientemente definido, de duas formas:

#### 5.1 -Personalizados no MGE / Mitra / Jiva G1

Os relatórios são compatíveis entre os sistemas **"Desktop"** (MGE / Mitra / Jiva G1) e os sistemas de "Servidor de aplicação" (Sankhya-Om / Jiva-Om). Mas a aba de "layout" que existe nos sistemas **"Desktop"** não existe no formatador do Sankhya-Om/Jiva-Om. Portanto embora esses relatórios, sejam compatíveis para visualização, não será possível editar o layout personalizado.

#### 5.2 -Personalizados no IReport

A opção apropriada para os relatórios, que precisam ter um layout específico é usar essa ferramenta. Isso eleva as possibilidades de personalização e flexibiliza bastante a aplicação dos recursos do formatador de relatórios.

Na verdade, o mecanismo de relatórios do Sankhya-Om/Jiva-Om utiliza arquivos **"JRXML"**, o mesmo arquivo usado pelo IReport. Com o botão **"Baixar JRXML"** é possível usar o relatório criado pelo sistema como base e então proceder às modificações. Finalizada a alteração do JRXML utiliza-se o botão **"Selecionar JRXML"**, para salvar o arquivo no relatório. A partir desse momento, o sistema irá usar esse modelo ao invés do modelo padrão.

Depois de personalizado o layout, o relatório não deve mais ser alterado, sob pena de perder compatibilidade com o layout, já que este não evolui automaticamente junto com as alterações. Por isso, sempre que há uma tentativa de alteração no relatório, o seguinte aviso será exibido:

**"Atenção: Este relatório possui um layout personalizado.**
**Qualquer alteração fará com que o layout seja DEFINITIVAMENTE DESCARTADO, tornando-o não personalizado.**
**Caso seja necessário personalizar o layout baixe o JRXML e modifique-o usando a ferramenta IReport.**
**Deseja realmente alterar o relatório?"**

Se a resposta for afirmativa o relatório será alterado, porém o layout personalizado será automaticamente descartado e o layout padrão voltará a ser utilizado.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados#top)
