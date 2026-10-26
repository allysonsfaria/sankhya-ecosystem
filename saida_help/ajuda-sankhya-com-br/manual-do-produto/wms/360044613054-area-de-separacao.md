---
id: "360044613054"
titulo: "Área de Separação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-09-26T06:33:51Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Coletor", "Etiquetas", "WMSEXIGENROPL", "Endereços", "Área", "SEPAREACONFWMS", "Separação", "Separadores", "br.com.sankhya.wms.cad.areadeseparacao", "Área de Separação manual", "Cadastro e Gerenciamento de Áreas de Separação no WMS"]
---

# Área de Separação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311555309591) Módulo: WMS > Cadastros
```

---

**Importante:** esta tela será apresentada para utilização, apenas se o parâmetro **"Separação por Área de Conferência no WMS? - SEPAREACONFWMS"** estiver ativado.

Nesta tela, devem ser realizados os cadastros das Áreas de Separação a serem utilizadas na rotina WMS.

| [Preenchimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#preenchimentosiniciais) | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#abageral) |
| --- | --- |
| [Aba Impressão de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#abaimpressodeetiquetas) | [Aba Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#abaendereos) |
| [Aba Separadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#abaseparadores) | [Separação agrupada por produto - Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#separaoagrupadaporproduto-coletor) |
| [Mensagens personalizadas...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#mensagenspersonalizadas) |  |

---

## Preenchimentos iniciais

Primeiramente, para realização do cadastro de uma nova área de separação, informe ou tenha de forma automática, o preenchimento do campo **"Cód. Área Separação"**; esta definição é realizada no botão **"Configuração da tela"**, acessado pelo ícone ![Imagem 2: Primeiramente, para realização do cadastro de uma nova área de separação, informe ou tenha de forma automática, o…](https://ajuda.sankhya.com.br/hc/article_attachments/16837709969687).

No campo **"Descrição"**, informe o nome destinado a área de separação.

O campo **"Cód. Área Conferência"**, está destinado a definir a Área de Conferência relacionada à Área de Separação que está sendo cadastrada.

No campo **"Tipo Separação"**, determine o tipo de separação que será realizado na referida Área de Separação, dentre duas possibilidades:

- Por Produto;
- Por Pedido.

## Aba Geral

![Imagem 3: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/360086265973)

Defina no campo **"Posição na esteira de separação"**, o local correspondente à Área de Separação em questão, na esteira de separação; esta configuração é válida em separações Flow Rack. Temos as seguintes opções:

- **Nenhuma:** Esta opção não corresponde à separação Flow Rack;
- **Inicial:** Por esta opção, a Área de Separação em questão está localizada na parte inicial da esteira;
- **Intermediária:** Temos aqui que a Área de Separação está localizada na parte mediana da esteira;
- **Terminal:** Por esta opção, a Área de Separação em questão está localizada na parte final da esteira.

Os produtos pertencentes à uma área de separação por esteira, sendo ela com posição inicial, intermediaria ou final os quais sejam relacionados a mesma área de conferência, irão para uma mesma separação.

No coletor de dados, a função **"Separação por Esteira"** executará tais separações, da seguinte forma:

![Imagem 4: No coletor de dados, a função "Separação por Esteira" executará tais separações, da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/360086266233)

Ao se iniciar a separação por esteira serão exibidas quais posições você tem permissão para realizar as separações.

![Imagem 5: Ao se iniciar a separação por esteira serão exibidas quais posições você tem permissão para realizar as separações.](https://ajuda.sankhya.com.br/hc/article_attachments/8895999033367)

Caso o executante efetue a tentativa de puxar uma tarefa na posição intermediária ou final de uma separação, que ainda não tenha sido iniciada na posição inicial, a rotina não apresentará nenhuma tarefa. Quando iniciada a separação, será exibida a tela com o resumo da referida separação.

![Imagem 6: Caso o executante efetue a tentativa de puxar uma tarefa na posição intermediária ou final de uma separação, que ainda…](https://ajuda.sankhya.com.br/hc/article_attachments/8896003943831)

Para se iniciar uma tarefa, é necessário que seja aberto um UMA (Unidade de Movimentação e Armazenagem) através do botão **"U.M.A"**.

![Imagem 7: Para se iniciar uma tarefa, é necessário que seja aberto um UMA (Unidade de Movimentação e Armazenagem) através do…](https://ajuda.sankhya.com.br/hc/article_attachments/8896003342359)

Após o procedimento de abertura, volte e acione o botão **"Tarefa"** para buscar as tarefas disponíveis para essa posição na esteira. Iniciando a separação a partir de qualquer outra posição que não seja a inicial, será necessário informar o(s) UMA(s) que foi(foram) iniciado(s) na separação:

![Imagem 8: Após o procedimento de abertura, volte e acione o botão "Tarefa" para buscar as tarefas disponíveis para essa posição…](https://ajuda.sankhya.com.br/hc/article_attachments/8895995393559)

Caso as tarefas da posição anterior da esteira correspondentes a esse checkout não tenham sido iniciadas ou concluídas, a seguinte mensagem será exibida:

**"O U.M.A "xxxxxx" ainda possui tarefas em uma área anterior da esteira."**

**Observação:** na separação do pedido, pode-se também verificar os detalhes adicionais do produto a ser separado. Para essa ação, basta clicar no botão ![Imagem 9: Observação: na separação do pedido, pode-se também verificar os detalhes adicionais do produto a ser separado. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/14030566667671) (SuperWaba) e ao iniciar a tarefa de separação (TotalCross).

A marcação **"Agrupar pedidos"** permite que os produtos que pertencem à uma referida Área de Separação e se encontram em pedidos que possuem a mesma ordem de carga, sejam agrupados em uma única separação **"Mãe"**. Essa ligação de separações filhas e mães acontece por meio da tabela TGWSVAR.

Nesse processo de agrupamento, as informações da separação mãe não são exibidas na rotina de [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias), apenas as informações das filhas serão exibidas. Abaixo, temos um exemplo do procedimento desta marcação:

O produto 1 está nos pedidos 30 e 31; esses pedidos irão gerar duas separações por pedido, durante o envio da onda ocorrerá o agrupamento destes na separação mãe. Caso o pedido 30 solicite 10 unidades deste produto e o pedido 31 solicite 5 unidades, o item de tarefa da separação mãe deverá então conter a solicitação de 15 unidades desse produto.

**Nota:** nas tarefas de separação, você pode realizar a personalização de mensagens aos usuários que realizarem essas tarefas. Para tal ação, na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) digite a trigger de sua preferência na tabela TGWTEC com sua mensagem, uma vez que, se esta for inserida com o caractere **#** em seu início, será exibida no momento em que a tela de separação do coletor é aberta, caso contrário, a mensagem será apresentada somente quando a tarefa de separação for selecionada.

**Seção Separação agrupada por produto**

Efetuando a marcação **"Utiliza separação agrupada por produto"**, você estará determinando que nesta Área de Separação será feito o uso da separação agrupada por produto. Esta marcação aumenta a eficiência e produtividade ao possibilitar que operadores separem múltiplos pedidos em um único deslocamento, minimizando o tempo percorrido sem demanda. O sistema guia o usuário para a separação solicitando os endereços de checkouts necessários, que na verdade são representados pelo equipamento físico (caixa, carrinho, gaiola com divisórias ou contêineres de separação). Na ilustração abaixo, você poderá observar o equipamento e as configurações exemplares para este caso:

![Imagem 10: Efetuando a marcação "Utiliza separação agrupada por produto" , você estará determinando que nesta Área de Separação…](https://ajuda.sankhya.com.br/hc/article_attachments/360096942414)

Informe no campo **"Quantidade máx. de checkouts por separação"**a quantidade máxima de checkouts a serem utilizados por separação.

A informação do campo **"Peso máx. do checkout por separação"** se refere ao peso máximo permitido que o operador pode separar por vez.

Insira no campo **"Volumetria máx. do checkout por separação (M3)"**, a volumetria máxima das caixas utilizadas na separação. A volumetria será calculada através das seguintes informações da caixa:

A - Altura da caixa

L - Largura da Caixa

P - Profundida da caixa

Fórmula: A x L x P = X m³

Informe no campo **"Quantidade de Checkouts por Pedido"** a quantidade de checkouts que poderão ser realizados por pedido em uma separação agrupada.

Preencha o campo **"Quantidade de pedidos por separação"** com a quantidade de pedidos que poderão ser agrupados por vez.

Quando selecionada a marcação **"Volume Contínuo?"**, fará com que, que a cada item lido, o volume seja fechado e, da mesma forma, seja aberto o próximo volume de forma automática.

**Observação:** para que você consiga editar volumes de produtos recontados de áreas de separação de volume contínuo, realize a marcação Volume Contínuo? dessa tela e habilite os parâmetros **"Detalha volumes com volume contínuo na recontagem? - DTVOLCOMVCREC"** e **"Detalhar volumes em conferências p/pedido no WMS? - DETALHAVOLWMS"**. Dessa forma, durante a recontagem, você poderá editar os volumes gerados durante a contagem inicial, independente se a opção **"V.C"** do coletor está ou não realizada.

Na tela **"Conferência por Pedido"** do Emulador **"SuperWaba"**, esta mesma marcação estará habilitada, de acordo com a configuração realizada na tela Área de Separação. Caso você opte por desmarcá-la, o sistema trabalhará no modo padrão, ou seja, realizará a conferência manualmente e não de forma automática.

**Nota:** esta rotina só poderá ser realizada após a habilitação do parâmetro **"Detalhar volumes em conferências p/pedido no WMS? - DETALHAVOLWMS"**.

**Importante:** este cadastro é dependente também da marcação **"Utiliza separação agrupada por produto"** localizada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) em sua aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), seção **"Utiliza separação agrupada por produto"**. Veja abaixo como funcionam as opções contidas nesta marcação:

- **Sim, conforme área de separação:** Esta opção irá realizar o agrupamento conforme marcação na área de separação.
- **Sim, conforme empresa:**  Esta opção irá realizar o agrupamento para todas as áreas de separação igualmente, conforme marcação para a empresa, na própria tela com os campos disponibilizados na sequência da tela.
- **Não usa:** Esta opção irá desligar o mecanismo de agrupamento, inclusive por área de separação se houver marcação já estabelecida.

Para verificar as separações agrupadas, consulte a tela [Gerência WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS) onde haverá a tarefa considerada mãe e as tarefas filhas. A tarefa que será executada no coletor serão as filhas e a tarefa mãe é apenas um controle deste agrupamento, sendo posteriormente cancelada.

Na imagem a seguir você poderá visualizar um exemplo contendo a separação mãe 693, e as filhas 689, 690 e 691 em processo de separação:

![Imagem 11: Na imagem a seguir você poderá visualizar um exemplo contendo a separação mãe 693, e as filhas 689, 690 e 691 em…](https://ajuda.sankhya.com.br/hc/article_attachments/360099283633)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)

**Seção Subdivisão tarefas de separação**

![Imagem 12: As configurações de "Separação agrupada por produto" e "Subdivisão de tarefas de separação" são incompatíveis e não…](https://ajuda.sankhya.com.br/hc/article_attachments/34508278453015) As configurações de **"Separação agrupada por produto"** e **"Subdivisão de tarefas de separação"** são incompatíveis e não podem ser utilizadas em conjunto.

![Imagem 13: As configurações de "Separação agrupada por produto" e "Subdivisão de tarefas de separação" são incompatíveis e não…](https://ajuda.sankhya.com.br/hc/article_attachments/34508278453911)

Quando tratar-se de uma área por produto será possível realizar a quebra de tarefas, considerando a norma palete quando a soma de quantidades entre os pedidos atinjam a quantidade suficiente para um palete para que que mais de um usuário possa realizar a tarefa de separação simultaneamente cada qual com seu palete fechado.

Isso poderá ser feito na sub-aba **“Subdivisão tarefas de separação”**, nele existe o campo **“Quebra por Norma/Palete”** do tipo liga/desliga, ao utilizar a opção ligado, terá a função de quebrar as tarefas de expedição em áreas por produto em um mesmo endereço, de acordo com a norma palete, permitindo que mais de um usuário possa realizar a separação do mesmo item.

**Observação:** a regra de Quebra por Norma/Palete não está contemplada na separação por área, separação esteira e separação balcão.

Se o **“Tipo de Separação”** estiver selecionado com o tipo **“Por pedido”** o campo Quebra por Norma/Palete ficará ofuscado, no entanto, caso esteja selecionado com o tipo **“Por produto”** o campo ficará aberto para o usuário selecioná-lo.

No campo **"Quantidade de SKU's por separação"**, defina a quantidade máxima de SKU's que cada separação terá.

Insira no campo **"Quantidade Tolerância de SKU's por separação"**, a quantidade máxima de SKU's que poderá ser somada à quantidade do item anterior, seguindo as regras abaixo:

- Sempre fragmentar as separações pela quantidade definida no campo Quantidade de SKU's por separação;
- Caso a quantidade de SKU's do pedido seja maior do que a definida no campo Quantidade de SKU's por separação, o sistema verificará se essa quantidade está dentro do valor do campo Quantidade Tolerância de SKU's por separação; se sim, então será gerada apenas uma separação.

Trouxemos um exemplo:

Quantidade de SKU's por separação = 1;
Quantidade Tolerância de SKU's por separação = 1;
Quantidade pedido = 4;
O sistema deverá gerar duas separações com 2 pedidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)

## Aba Impressão de Etiquetas

![Imagem 14: Aba Impressão de Etiquetas](https://ajuda.sankhya.com.br/hc/article_attachments/360086266473)

Nesta aba, temos os campos **"Impressora da Etiqueta de Volume"** e **"Modelo de Etiqueta de Volume"**, onde devem ser informadas a impressora a ser utilizada na impressão e o modelo de etiqueta, respectivamente. O modelo de etiqueta deve ser anteriormente inserido na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

O campo **"Imprimir etiqueta no fechamento do volume"** está diretamente ligado à marcação **"Usa impressão de etiqueta ao fechar volume"**([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms)) e temos as seguintes opções para seleção neste campo:

- **Sim, conforme área de separação:** Com esta opção selecionada e a marcação habilitada, fará com que o sistema imprima a etiqueta a cada volume conferido fechado.
- **Sim, conforme empresa:** Estando esta opção desligada e a marcação habilitada, fará com que o sistema somente imprima as etiquetas de volume ao final da conferência, ou seja, esta opção inibirá a ação da marcação.
- **Não usa:** Caso a marcação esteja desabilitada, esta opção não terá nenhuma ação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)

## Aba Endereços

![Imagem 15: Aba Endereços](https://ajuda.sankhya.com.br/hc/article_attachments/360085090334)

Nesta aba, informe nos campos **"Cód. End. Ini."** e **"Cód. End. Final"**, o intervalo dos endereços que compreendem a Área de Separação em questão. Os endereços aqui apresentados, são os cadastrados na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313), cuja a marcação **"Exclusivo p/ Conferência"** não esteja realizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)

## Aba Separadores

![Imagem 16: Aba Separadores](https://ajuda.sankhya.com.br/hc/article_attachments/360085090414)

Nesta aba, através do campo **"Cód. Separador"**, informe o separador responsável que atuará na área de separação. Você pode cadastrar mais de um separador, dependendo das funções que serão desempenhadas. Poderão ser inseridos neste campo, as pessoas vinculadas às tarefas desejadas; este vínculo é previamente realizado na tela [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354), na aba **"Tarefas Permitidas"**, onde a pessoa para ser apresentada para escolha, deve ter a tarefa **"Separação"** à ela vinculada.

**Observação:** se o separador responsável não estiver cadastrado em nenhuma área de separação, ele conseguirá visualizar tarefas de todas as áreas existentes, no entanto, caso este usuário já esteja definido para uma área especifica, ele somente visualizará as tarefas vinculadas a essa área.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)

## Separação agrupada por produto - Coletor

Ao iniciar uma tarefa de separação agrupada, teremos no coletor a seguinte tela:

![Imagem 17: Ao iniciar uma tarefa de separação agrupada, teremos no coletor a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/8895993534743)

Esta tela é exibida pois, a rotina de agrupamento da separação, já calcula a quantidade de checkouts (caixas) necessários para essa separação agrupada; basta informar aqui os chekouts que serão utilizados na separação.

Ao informar o endereço de origem e o produto, será exibida a seguinte tela:

![Imagem 18: Ao informar o endereço de origem e o produto, será exibida a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/8895965943063)       ![Imagem 19: Ao informar o endereço de origem e o produto, será exibida a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/8895965156247)

Como tratamos aqui de uma separação agrupada, você deve separar os produtos apenas com as quantidades e checkouts que pertencem aquele pedido.

**Observação:** em relação à data de validade, a rotina de Separação considerará a menor data de validade no estoque do endereço.

**Nota:** para realizar o agrupamento da separação de forma automática, habilite o parâmetro **"Agrupamento de separação automático - WMSSEPAGRUAUTO"**.

**Observação:** ao realizar o agrupamento no momento da separação por pedidos, para que o sistema não utilize produtos vinculados a uma Área de Separação quando a marcação Agrupar pedidos (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#abageral)) estiver desabilitada, ligue o parâmetro **"Permitir separação flowrack parcial? - SEPFLOWRACKPARC"**.

---

![Imagem 20: Influência do parâmetro WMSEXIGENROPL nesta rotina.](https://ajuda.sankhya.com.br/hc/article_attachments/26809641128599)**Influência do parâmetro WMSEXIGENROPL nesta rotina.**

Com o parâmetro **"Informar número do palete em separações agrupadas - WMSEXIGENROPL"** ativado, ao executar uma tarefa de separação pelo **"Coletor WMS Android"** em cenários de grandes volumes e várias sequências de endereços, será possível rejeitar a próxima tarefa e destinar o que já foi separado diretamente para a doca. Nesse momento, o coletor solicitará o código do Container, e a tarefa executada será remanejada para uma nova separação, mantendo o restante de tarefas pendentes na separação original.

[GIF animado: Imagem 21: Com o parâmetro "Informar número do palete em separações agrupadas - WMSEXIGENROPL" ativado, ao executar uma tarefa de…](https://ajuda.sankhya.com.br/hc/article_attachments/26809667714071)

Assim, cada separação terá seu próprio Container, garantindo que cada uma possa ser conferida de forma individual posteriormente na doca de expedição.

Informações complementares sobre o parâmetro WMSEXIGENROPL: 

- Funciona apenas para o tipo de separação Por Produto. Separações Por Pedido não estão contempladas nesse fluxo.
- Se a área estiver configurada para separação por produto, o recurso Separação Pulmão funciona. Se configurada para separação por pedido, o parâmetro não será aplicado.
- Este parâmetro não suporta Separação Balcão.
- A conferência será realizada exclusivamente com base no container. Para cada container, será esperado que contenha exatamente o que foi separado e alocado para ele.
- Cancelamentos de expedição, como a retirada de notas já enviadas para expedição, só podem ser realizados se a separação ainda não tiver sido iniciada.
- A criação da etiqueta do container deverá seguir a necessidade do cliente, podendo utilizar código bidimensional ou código de barras. É importante que os códigos não se repitam em nenhuma circunstância. Vale destacar que o processo não é fornecido nativamente.
- Um container não pode ser conferido por mais de um conferente ao mesmo tempo.
- Diversas validações serão realizadas para verificar se um container já existe, está em uso, foi utilizado anteriormente, já foi conferido ou está em processo de recontagem.
- O uso do parâmetro WMSEXIGENROPL ligado, concede acesso exclusivo e compatível apenas com o Coletor WMS Android. Este parâmetro não é compatível com o produto Super Waba.
- Além disso, esse parâmetro não é suportado em conjunto com os parâmetros:

  - Busca manual de tarefas de separação? - BUSCAMANTARSEP;
  - Habilita controle de produtos com peso variável - PESOVARWMS;
  - Campos para informações adicionais da tarefa. - WMSINFOADTAREFA.
- Também não é aplicável com as seguintes marcações da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa):

  - Permite outro usuário continuar separação;
  - Utiliza explosão de lote na separação;
  - Utiliza cód. de barras concatenado.
- Esse é um recurso novo e ainda está em fase de testes. Assim, pode haver casos de uso não compreendidos em suas totalidades.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)

## Mensagens personalizadas no coletor de Dados

**Nota:** esta é uma rotina idealizada para ser configurada por um profissional que domine as linguagens de programação PL/SQL.

No **Sankhya Om**, você pode configurar determinadas mensagens para que estas sejam exibidas no coletor de dados do WMS, de forma que, sejam apresentadas quando a tarefa é mostrada no coletor e também, ao informar o endereço, pois, assim, informações relevantes ou inerentes ao processo no ato da execução da tarefa sejam exibidas.

Portanto, você poderá configurá-las da seguinte maneira:

Quando a tarefa for apresentada na tela do seu coletor, para que a mensagem de sua preferência seja exibida, pode-se realizar a criação de uma trigger personalizada inserindo uma mensagem de até 99 caracteres no campo **"AD\_MSGCOLETOR"** da tabela **"TGWTEC"** do [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294), conforme a regra de negócio, sendo que, este também pode ser configurado em um evento Java.

Essa rotina pode ser definida com inúmeras regras de negócio. Desse modo, considere o exemplo de uma trigger abaixo:

**create or replace TRIGGER TRG\_INC\_UPD\_TGWTEC BEFORE INSERT OR**
            UPDATE ON TGWTEC FOR EACH ROW
                      BEGIN
                      :NEW.AD\_MSGCOLETOR := **'Necessário um envelope plástico (Venda**

**do tipo E Commerce), colete-o antes de executar a separação';**

**END;**

Em seguida, observe a mensagem a ser exibida:

[GIF animado: Imagem 22: Em seguida, observe a mensagem a ser exibida:](https://ajuda.sankhya.com.br/hc/article_attachments/4408237518871)

Após a configuração, temos também, alguns exemplos de mensagens:

**Processo de separação**
**"Para esta separação é necessário um envelope plástico (Venda do tipo E Commerce), colete-o antes de executar a separação."**

**Processo de separação por esteira**
**"Esta é uma separação especial. Disponibilize caixa personalizada junto às mercadorias separadas."**

**Processo de armazenagem**
**"Verifique se o palete físico não possui datas diferentes. Recebimento com mais de uma data para este produto."**

Além disso, essas mensagens também podem ser exibidas quando a leitura do endereço da tarefa for efetuada; para essa ação, basta inserir o caractere '**#**' antes da mensagem no campo AD\_MSGCOLETOR da tabela TGWTEC da tela Dicionário de Dados. Abaixo, observe um exemplo de trigger na especificação aqui exposta:

**create or replace TRIGGER TRG\_INC\_UPD\_TGWTEC BEFORE INSERT OR**

UPDATE ON TGWTEC FOR EACH ROW

         BEGIN

         :NEW.AD\_MSGCOLETOR := **'#Produto com alto índice de avarias, cuidado ao movimentá-lo.';**

END;

Após a configuração acima, você poderá visualizar a seguinte mensagem:

[GIF animado: Imagem 23: Após a configuração acima, você poderá visualizar a seguinte mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/4408248941847)

Conforme a regra de negócio na trigger, pode-se personalizar inúmeras mensagens para diversas aplicações, como, por exemplo, no processo de reabastecimento. Observe:

**"Atenção! Produto com mais de uma data no endereço, colete a de menor disponibilidade."**

Lembre-se que este serviço de mensagens, pode ser aplicado nos seguintes processos:

- Tarefas de Armazenagem;
- Transferência;
- Reabastecimento e;
- Tarefas de Separação (Convencional, balcão, por área e por esteira).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#top)
