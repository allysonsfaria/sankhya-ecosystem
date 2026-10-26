---
id: "360060958194"
titulo: "Controle de Estoque de Terceiros - WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > Compras e Estoque"
atualizado_em: "2026-09-15T12:47:31Z"
rotulos: ["Configuração", "WMS", "Parceiro", "Expedição", "Recebimento", "Estoque", "estoque de terceiros", "Ressuprimento e Abastecimento", "Recebimento e Expedição", "AJUSTEPARCZERO"]
---

# Controle de Estoque de Terceiros - WMS

Nesse artigo, abordaremos os diversos modos de controle de estoque de terceiros no WMS. Para conferir as funcionalidades dessa tela, basta acessar os links abaixo:

| Funcionalidades da Tela | |
| --- | --- |
| [Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#recebimento) | [Expedição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#expedi%C3%A7%C3%A3o) |
| [Ressuprimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#ressuprimento) | [Movimentação Pró-Ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#movimenta%C3%A7%C3%A3opr%C3%B3-ativa) |
| [Transferência entre Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#transfer%C3%AAnciaentreendere%C3%A7os) | [Inventários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1rios) |
| [Inventário de Implantação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1riodeimplanta%C3%A7%C3%A3o) | [Inventário Rotativo e Global](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1riorotativoeglobal) |
| [Contagem com sobra e perda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#contagemcomsobraeperda) | [Troca de depositante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#trocadedepositante) |
| [Contagem com depositantes diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#contagemcomdepositantesdiferentes) | [Contagem em endereço vazio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#contagememendere%C3%A7ovazio) |

                                                                           

### Recebimento

O processo de recebimento de estoque de terceiro é semelhante ao que é praticado pela maioria dos clientes atuais em relação ao recebimento de estoque próprio, sendo que, sua particularidade se dá no estoque que é recebido, pois este estará em poder próprio, mas pertencente a um parceiro terceiro.

Assim, no sistema, na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) crie uma TOP de Nota de Compra exclusiva para o recebimento de estoque de terceiro com o preenchimento dos seguintes campos:

- Na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms), efetue a marcação **"Atualiza Estoque de Terceiros WMS"**;
- E na aba [Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros), defina o campo **"Estoque com/de terceiros"** como **"Somar ao estoque de terceiros em poder da empresa"**.

[GIF animado: Imagem 1: E na aba Estoque de Terceiros , defina o campo "Estoque com/de terceiros" como "Somar ao estoque de terceiros em poder…](https://ajuda.sankhya.com.br/hc/article_attachments/22404828212375)

Em seguida, defina no [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313) qual endereço estará vinculado à qual produto. Essa medida irá associar o parceiro informado na nota de compra ao produto e, assim, o vinculará ao endereço cadastrado.

Após o envio das notas, na tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034), pode-se utilizar o campo **"Parceiro"** no Painel de Filtros para identificar o parceiro para o qual está sendo feito o recebimento. Essa informação poderá ser usada na consulta de recebimentos daqueles que foram ou não realizados ao parceiro utilizado na pesquisa que estiver relacionado ao processo. 

**Observação:** será possível enviar mais de uma nota para o recebimento, desde que elas sejam do mesmo parceiro, e as TOP's estejam configuradas para o recebimento de estoque de terceiro. Se alguma das TOP's não possuírem as configurações previamente descritas, a atualização de estoque de terceiro não será registrada nas tabelas do sistema.

Após a finalização da conferência, o estoque deverá ser gerado na tabela de estoque do WMS (TGWEST) com o nome do Parceiro depositante incluído, ou seja, esse estoque terá um proprietário.

As tarefas de armazenagem devem ser geradas conforme a estratégia utilizada por cada empresa. O sistema não permitirá que o mesmo endereço seja ocupado por dois depositantes diferentes, mas se o endereço utilizado estiver com a marcação **"Multi Produto"** habilitada na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) poderá ser registrado em mais de um produto armazenado no endereço do mesmo depositante.

![Imagem 2: As tarefas de armazenagem devem ser geradas conforme a estratégia utilizada por cada empresa. O sistema não permitirá…](https://ajuda.sankhya.com.br/hc/article_attachments/22405265635863)

**Importante:** ao realizar um recebimento de terceiro, é essencial que o vínculo entre endereço e produto tenha sido realizado. Assim, ao proceder com o recebimento, o sistema irá vincular o parceiro ao endereço nas tabelas de estoque do WMS (TGWEST) e Estoque Validade WMS (TGWESTVAL). Dessa forma, para que vários produtos sejam vinculados a um parceiro, insira os produtos desejados no cadastro do endereço de picking, a tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto), bem como, o recebimento por parceiros distintos.

Para que seja feito o recebimento dos itens relativos à estoque de terceiro contemplando o código do parceiro nas movimentações internas sem que haja dependência do estoque contábil, podendo a cobertura fiscal ser efetivada no período de até dias após o armazenamento inicial, é necessário realizar as configurações abaixo na TOP: 

- Na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms), a marcação **"Atualiza Estoque de Terceiros WMS?"** deve estar ligada. Essa ação levará o campo **"CODPARC"** nos controles de WMS;
- Na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), o campo **"Atualização do Estoque"** deve estar configurado com a opção **"Nenhuma"**;
- Por fim, na aba [Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros), o campo **"Estoque com/de Terceiros"** deve estar com uma das opções abaixo para atualizar o estoque comercial:

1. **Somar ao Estoque de terceiros em poder da empresa:**
2. **Somar ao estoque próprio em poder de terceiros**

**Observação:** caso esteja com a opção **"Não controla"**, será mantido o comportamento atual do sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)

### Expedição

Para a utilização da Expedição no Estoque de Terceiros, utilize as mesmas configurações da TOP realizadas no recebimento.

O sistema está habilitado para que o processo de separação do estoque de terceiro seja feito por pedido e produto, além da separação do pulmão.

No envio da onda, as tarefas de separação e ressuprimentos necessários são geradas de acordo com o depositante, uma vez que as docas de saída suportam mais de um parceiro. Caso haja a necessidade de corte, a ferramenta considera o depositante, sendo que a primeira grade do pop-up **"Detalhes Corte de Pedidos"** da tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274) apresentará o corte por parceiro. Assim, a seguir, tem-se as peculiaridades de cada tipo de separação, onde pode-se efetua-las através do coletor de dados e poderá consultar os status das tarefas na tela [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474):

- A separação por Pulmão ocorrerá diretamente em um endereço de pulmão, onde a separação é feita pela quantidade total do endereço. Assim, não haverá entrega em quantidades fragmentadas.
- Na separação por pedido, o sistema irá gerar as separações respeitando o estoque do parceiro por pedido.
- Referente à separação por produto, haverá o agrupamento de parceiros na tarefa de separação considerando que este pode ter mais de um depositante do mesmo produto, e constará em um pedido de venda e parceiros diferentes, porém estarão juntos em uma Ordem de Carga. Logo, essa Ordem estará preparada para que haja mais de um parceiro depositante vinculado à ela.

Uma vez que o controle poderá ser feito pela data de validade e lote, se o produto em separação for controlado por lote, o coletor conseguirá indicar ao separador qual lote e endereço será separado, e qual será o depositante proprietário. 

**Observação Técnica**: Diferente do fluxo de estoque próprio, na expedição de Estoque de Terceiros, o sistema **não suporta a Explosão Automática de Lotes**. Mesmo que os parâmetros globais de automação de lote estejam ligados, para mercadorias de terceiros, o controle deve ser indicado manualmente ou via coletor, conforme a disponibilidade física do depositante.

Ao finalizar a separação, a conferência ocorrerá normalmente, sendo que as conferências por pedido são realizadas no checkout, efetuando a geração de volumes e envio dos mesmos para a doca para conferência e carregamento. 

**Nota:** mesmo quando o produto estiver no checkout, será possível visualizá-lo no estoque do WMS (TGWEST).

Caso haja a necessidade de realizar o estorno da separação, o sistema irá considerar os endereços que tenham o produto, e que sejam do mesmo depositante para que, dessa forma, as tarefas de armazenagem possam ser geradas. 

**Observação:** se não houver endereço que possua estoque do parceiro, a tarefa será gerada para um endereço vazio.

Além de estornos, ainda pode-se realizar o registro de ocorrências, pois em alguns casos, o sistema pode gerar um ressuprimento ou solicitar que a pega dos produtos seja feita em outro endereço (separação pulmão). Essas ocorrências podem ser criadas na tela [Tipos de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120213) e consultadas na tela [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094), sendo que, a liberação delas é feita na tela [Liberação de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613294).

**Nota:** os endereços especiais estão habilitados para o armazenamento de produtos com mais de um parceiro depositante, assim como os endereços de estorno.

Durante todo o processo de expedição, pode-se consultar o nome do destinatário por meio da tela [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)

### Ressuprimento

Referente ao ressuprimento ou abastecimento, tem-se três tipos diferentes, sendo eles: 

O Ressuprimento Corretivo, que pode ser gerado pelo envio da onda por meio do lançamento de ocorrência, e ocorre para tornar suficiente a quantidade disponível no picking, de forma que atenda à separação do pedido.

Quando o estoque atingir uma quantidade mínima para realizar o picking, o sistema poderá fazer um ressuprimento automático, ou reabastecimento agendado.

Em relação ao [Ressuprimento Preventivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120193), ele ocorrerá apenas se o estoque em questão for do mesmo parceiro depositante. Assim, o sistema irá considerar o depositante do endereço de picking, juntamente com o do pulmão para efetuar o ressuprimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)

### Movimentação Pró-Ativa

Na Movimentação Pró-Ativa, o sistema irá validar os produtos e o depositante no momento em que eles forem buscados no endereço de origem e entregues ao endereço de destino, para que assim, não se misture produtos de depositantes diferentes entre endereços.

No coletor, ao realizar uma movimentação e houverem mais produtos a serem movimentados, pode-se ir para a próxima tarefa e realizá-la, caso não haja, retorne ao menu inicial de movimentações.

Dessa forma, a Movimentação Pró-Ativa tratará de uma transferência de mercadorias entre endereços e é realizada diretamente no Coletor de dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)

### Remanejamento de Estoque

No remanejamento de estoque, os produtos serão alocados de forma que o máximo de espaço seja aproveitado para que assim, novos espaços sejam disponibilizados para outros produtos.

No armazenamento de Estoque de Terceiros, o sistema irá considerar o produto, a compatibilidade e demais acessos, assim como o parceiro depositante.

Ao gerar o remanejamento, além de efetuar todas as validações já existentes, o sistema também validará o parceiro do endereço, ou seja, não será possível enviar produtos de parceiros distintos para o mesmo endereço.

Na tela [Remanejamento de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008361662-Remanejamento-de-estoque), por meio do filtro **"Parceiro"**, pode-se realizar uma busca por todos os Parceiros quando julgar necessário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)

### Transferências entre endereços

Na tela [Transferência entre Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107213), pode-se realizar uma busca por Parceiros visto que, esta rotina está apta para suportar Estoque de Terceiros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)

### Inventários

Os processos de inventário de implantação, global e rotativo, poderão realizar a contagem de estoque de terceiros. pode-se filtrar os endereços para a geração das tarefas de contagem, podendo gerar o inventário para um parceiro específico ou não. Abaixo, falaremos sobre cada processo:                                     

### Inventário de Implantação

Na tela [Geração de Tarefas de Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Gera%C3%A7%C3%A3o-de-Tarefas-de-Contagem), faça a geração dessas tarefas que poderão ser visualizadas na tela [Gerência do WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453).

Logo depois, será possível realizar a contagem dos endereços requeridos no Coletor de Dados.

Ao clicar no botão **"Implantar estoque"** da tela Ajuste de Estoque por Inventário, o pop-up **"Escolha o depositante do estoque"** será aberto.

Dessa forma, a solicitação do ajuste será realizada, e a tabela Contagem para Inventário (TGWIVR) será atualizada com o(s) Depositante(s) informados(s) no pop-up.

**Observação:** esse pop-up será aberto somente se for habilitado o parâmetro **"Aviso de ajuste feito com parceiro zerado. - AJUSTEPARCZERO"**.

Na tela [Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633) as notas de ajuste serão geradas. Assim a tabela de estoque (TGFEST) também é atualizada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1rios)

### Inventário Rotativo e Global

Os Inventários Rotativo e Global são processos de recontagem contínua de estoque, sendo que o Inventário Global irá deferir-se apenas no momento de realizar o ajuste, em que, será exibido uma tela de filtro onde tem-se a possibilidade de escolher o ajuste apenas para endereços que tiverem no mínimo uma determinada quantidade de contagens iguais consecutivas. Para maiores detalhes sobre esses processos, clique nos links abaixo:                                                               

### Contagem com sobra e perda

**Nota:** habilite o parâmetro Aviso de ajuste feito com parceiro zerado. - AJUSTEPARCZERO.

Para realizar a Contagem a maior, ou uma contagem em que há sobra de produtos, primeiramente, acesse a tela [Geração de Tarefas de Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Gera%C3%A7%C3%A3o-de-Tarefas-de-Contagem) e faça as tarefas de contagem.

No coletor, efetue a contagem do endereço e, com uma divergência de sobra, realize o lançamento de ajuste na tela [Ajuste de Estoque por Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Ajuste-de-Estoque-por-Invent%C3%A1rio) utilizando o **"Gerar ajuste"**.

Após isso, na tela [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094), lance a nota de ajuste.

O mesmo processo ocorrerá caso haja uma divergência na contagem em que ela seja a menor, ou seja, em que há falta de produtos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1riorotativo)

### Troca de depositante

Ainda sobre o Inventário Rotativo, existem alguns casos em que o parceiro depositante efetua uma transferência de estoque para outro parceiro. Quando a troca de proprietário é feita na quantidade total do estoque ou total do endereço, é gerada apenas uma mudança sistêmica de depositante (movimentação atômica), ou seja, é realizada a troca de depositante.

Nesse caso, considere como exemplo, que o estoque deixou de ser da Empresa A e foi transferida para a Empresa B. Tal ação será realizada na rotina de inventário, quando se confirmar o pedido, assim, o sistema irá gerar a nota de saída para baixar estoque vinculado ao Parceiro A e, em seguida, gerará a nota de entrada para o destinatário, sendo este o Parceiro B.

Ao realizar o lançamento de uma nota de compra, uma vez que esta irá desencadear um recebimento envolvendo um Parceiro Depositante, a TOP utilizada nesse lançamento deve estar com a marcação Atualiza Estoque de Terceiro WMS habilitada. Assim, ao concluir o recebimento, o sistema interpretará que o estoque do(s) produto(s) em questão, pertencem ao Parceiro da nota. Consequentemente, as demais operações, como Expedição e Transferências, poderão ser realizadas para este parceiro, utilizando o estoque que ele possui no armazém.

Para realizar

Para realizar a contagem com mudança de depositante, depois de gerar a tarefa de contagem, e ao realizar a contagem no coletor, e fazer o ajuste na tela Ajuste de Estoque por Inventário, no botão Gerar Ajuste habilite a marcação **"Apenas endereços deste ajuste"** e atribua o novo endereço de sua preferência no campo **"Depositante"** do pop-up **"Escolha o depositante do estoque"**.

**Observação:** não será possível lançar um ajuste com um Depositante 0.

Na tela Consulta Estoque com Ocorrências, pode-se observar que a solicitação da nota de ajuste será gerada com a nova quantidade pertencente ao novo parceiro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1riorotativo)

### Contagem com depositantes diferentes

No WMS, também pode-se realizar a contagem de perda e/ou sobra com parceiros e endereços diferentes no mesmo inventário. Para essa ação, ao gerar as tarefas de ajuste de contagem e clicar no botão Gerar ajuste da tela Ajuste de Estoque por Inventário, na solicitação de geração das notas de ajuste na tela Consulta Estoque de Ocorrências, a validação das notas será realizada para cada parceiro de forma individual. Considerando esse comportamento, trouxemos o exemplo a seguir:

Caso a Empresa A for filtrada na tela, o sistema exibirá todas as notas de ajuste referente àquela Empresa, e ao gerar as notas com todas elas selecionadas, o sistema não permitirá essa geração se o Parceiro/Endereço delas forem diferentes. Assim, utilize o filtro rápido Parceiro para selecionar as notas pertencentes a ele e, posteriormente, lance as notas.

**Observação:** esse comportamento também poderá ocorrer quando a contagem pertencer a depositantes e tiver uma contagem de Sobra ou ou Falta.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#invent%C3%A1riorotativo)

### Contagem em endereço vazio

Depois de gerar as tarefas de ajuste, e conferi-las na tela Gerência de WMS, ao informar o endereço no coletor, clique no botão **"End. vazio"** no coletor para indicar a ausência de produtos no endereço em questão. Depois de realizar a geração do Ajuste, pode-se conferir as notas de ajuste geradas na tela Consulta Estoque com ocorrências.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros-WMS#top)
