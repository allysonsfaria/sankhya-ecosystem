---
id: "4403065244439"
titulo: "Parâmetros do sistema que influenciam na rotina de WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403065244439-Par%C3%A2metros-do-sistema-que-influenciam-na-rotina-de-WMS"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-07-22T15:24:02Z"
rotulos: ["Configuração", "WMS", "TOP", "Parâmetros", "Estoque", "#validadoRonald", "Configuração de TOPs para entrada e devolução no WMS", "Parâmetros para movimentação e separação no WMS", "Reabastecimento ajustes e cortes automáticos no WMS", "Squad WMS"]
---

# Parâmetros do sistema que influenciam na rotina de WMS

| **![Imagem 1: ATENÇÃO: Antes de alguma alteração de parâmetros, avalie em sua base de teste se realmente o parâmetro irá influenciar…](https://ajuda.sankhya.com.br/hc/article_attachments/16343584543255) ATENÇÃO:** Antes de alguma alteração de parâmetros, avalie em sua base de teste se realmente o parâmetro  irá influenciar em outras rotinas e se vai atenderá a suas necessidades. |
| --- |

(1)** "TOP de entrada de mercadorias no WMS - TOPENTRADAWMS"**:  informe neste parâmetro a TOP que será utilizada para a criação de uma " Nota de Entrada" criada automaticamente pelo servidor.

**![Imagem 2: OBSERVAÇÃO: configure esta TOP para dar entrada no estoque e não atualizar o financeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/16343570775447) OBSERVAÇÃO:** configure esta TOP para dar entrada no estoque e não atualizar o financeiro.

**(1)** **"TOP para a  devolução de Mercadorias no WMS (TOPDEVOLUCAOWMS)":** informe neste parâmetro a TOP que será utilizada para criação de uma ‘Nota de Devolução’ automaticamente pelo servidor.

**Exemplo:** ao se fazer uma compra de 250 itens e conferir apenas 200, será gerada automaticamente uma nota de devolução de 50 itens, utilizando as mesmas informações da ‘Nota Original’.

**![Imagem 3: OBSERVAÇÃO: quando as notas de ‘Devolução’ e ‘Compra’ forem criadas automaticamente pelo sistema, no campo "Observação"…](https://ajuda.sankhya.com.br/hc/article_attachments/16343570775447) OBSERVAÇÃO:** quando as notas de ‘Devolução’ e ‘Compra’ forem criadas automaticamente pelo sistema, no campo **"Observação"** o sistema adicionará a seguinte informação: "Nota criada automaticamente pelo WMS por divergência de contagem".

As notas geradas no processo de conferência com divergência para mais ou para menos irá respeitar a marcação 'Nunca incluir confirmada' existente no Cadastro da TOP.

**(1)** **"Série p/ Devolução de Mercadorias no WMS - SERIEDEVWMS":** informe neste parâmetro qual será a série da nota gerada no processo de conferência de entrada. Trabalha juntamente com o parâmetro **'TOPDEVOLUCAOWMS**’, da seguinte forma:

Ao finalizar a conferência, se houver divergência na conferência de entrada, caso o usuário aceite a divergência, ao gerar a ‘Nota de Devolução’ o sistema utilizará este parâmetro para buscar a ‘Série’ a ser utilizada na ‘Nota Fiscal’. As notas geradas no processo de conferência com divergência para mais ou para menos irá respeitar a marcação 'Nunca incluir confirmada' existente no Cadastro da TOP.

(1)** "Unidade Alternativa para Palete no WMS - UNALTPAWMS":** Este parâmetro é utilizado no processo da produção. Informe a sigla da unidade que é considerada como Palete. Apresentar complemento do produto? (APRCOMPLPROD): Quando habilitado, apresentará no coletor o campo “Complemento do produto” concatenando com a “Descrição do Produto”.

**![Imagem 4: OBSERVAÇÃO: ao alterar este parâmetro, limpe o cache do servidor para que o sistema reconheça a nova alteração.](https://ajuda.sankhya.com.br/hc/article_attachments/16343570775447) OBSERVAÇÃO:** ao alterar este parâmetro, limpe o cache do servidor para que o sistema reconheça a nova alteração.

**(1)** **"Valida Estoque no WMS antes do envio? - VALIDAESTWMS":** desativado a partir da versão 4.0

Até a versão 4.0 este parâmetro era utilizado para validação do Estoque no WMS antes do envio para ‘Expedição’. Este parâmetro atendia a existência de algumas exceções quando o estoque no MGE Comercial não estava coerente com o WMS, impedindo, desta forma, que uma nota fosse para o WMS sem que existisse estoque para sua separação. A partir da versão 4.0 sistema passou a verificar o estoque de forma padrão e este parâmetro foi desativado.

(1)** "Armazenar Produtos Vol. Alternativo no WMS?' - ARMPROUNALTWMS":** quando estiver ligado e não existir endereços disponíveis na ‘Unidade de Agrupamento’ do produto, o sistema buscará os endereços da maior unidade para menor unidade, até encontrar um local onde seja possível armazená-lo.

(1)** Notas:**
Os parâmetros **“Exige agendamento para carga e descarga no WMS? EXIGEAGENDAWMS”** e “**Exibe Tarefas Geradas ao Enviar para o WMS? - EXIBETAREFASWMS”** foram substituídos por marcação na TOP.

(1)** "Permite Reabastecimento p/ Estoq. Min zero no WMS? - REABESTZEROWMS":** se ligado, fará o reabastecimento quando o endereço estiver configurado com o estoque mínimo igual a zero. Se estiver desligado, o reabastecimento só será gerado se o estoque mínimo do endereço for maior que zero.

(1)** "Unidade com Prioridade para Separação no WMS - UNPRIORSEPWMS":** este parâmetro altera a ordem de prioridade de separação. O padrão deste parâmetro é vazio, caso o usuário necessite alterar a ordem de separação deverá informar no parâmetro a unidade que terá priorização.

(1)** "Utiliza a movimentação vertical no WMS - USAMOVVERTWMS":** este parâmetro possibilitará ao WMS trabalhar com movimentações horizontais executadas por paleteira e verticais executadas por empilhadeiras evitando, assim, que um tipo de equipamento venha a fazer o movimento de outro. Por exemplo, que a empilhadeira faça movimentos horizontais que na verdade é a função da paleteira e assim sucessivamente. Quando este parâmetro estiver ligado será apresentado no cadastro de endereços o campo de marcação "Endereço auxiliar para Movimentação Vertical". Deve-se criar um endereço Pai e marcá-lo com esta opção. Em seguida, devem-se criar os endereços filhos deste endereço. Além disto, será habilitada neste mesmo cadastro a aba **"Movimentação Vertical"**, onde será necessário informar para o endereço atual qual será o endereço “Preferencial” e “Secundário”.

(1)**"Separação por área de conferência no WMS - SEPAREACONFWMS":** este parâmetro liga a funcionalidade de separação por área. Assim que enviar um pedido para separação no WMS, o sistema gera separações diferentes por área de separação. Este parâmetro liga as telas descritas abaixo:

1. Arquivos/Cadastros/Área de Conferência.

2. Arquivos/Cadastros/Área de Separação.

3. Cadastro de produtos, aba WMS os campo: "Cód. Área Separação"

4. No Cadastro de endereçamento o Campo "Exclusivo para Conferência".

5. Opção "Conferência por Pedido", no cadastro “Definir Tarefa e Volume por usuário”.

6. Rotinas/Registro de Volume.

7. Botão direito da tela de Rotinas/Formação de carga, a opção: "Enviar para Expedição por OC".

Altera a forma de envio da opção o "Enviar para expedição" no botão direito da seleção de pedidos, fazendo o envio dos pedidos apenas para os locais que tem a definição "por pedido", no cadastro de área de separação.

8. Formatador de Relatórios/Registro de volumes.

(1)**"Gerar reabastecimento corretivo no WMS? - REABCORRECAOWMS":** quando este parâmetro estiver ligado, ao mandar gerar uma separação e o estoque do picking não for suficiente, o sistema comandará um reabastecimento que extrapolará o estoque máximo do picking. Somente após a execução do reabastecimento é que poderá ser feito a tarefa de separação, fazendo com que o separador vá ao picking apenas uma vez.

(1)** "Imprimir etiquetas na separação por OC no WMS - IMPETIQSEPOC":** para Separação Por Ordem de Carga será necessária a ativação do parâmetro IMPETIQSEPOC. Desta forma, a Conferência de Volumes para as separações que foram feitas na área de separação "Por Produto" estará habilitada no 'Coletor'.

A conferência por volume na separação por produto é similar à conferência por volume na separação por pedido. Contudo, no processo de separação POR PRODUTO, ao enviar pelo "Coletor" a Conferência, a "Quantidade de Volume" gerada não será questionada, mas será gerada uma linha na TGWREV para cada unidade de cada item conferido, por consequência, uma etiqueta com IDREV diferente para cada linha gerada.

(1)** "Impressão de etiqueta de volumes com as seguintes opções - IMPETQVOL":**

"Ao fim da conferência"

"Ao colocar o produto na doca"

Determina o momento em que as etiquetas de volumes serão geradas. Este parâmetro está subordinado ao parâmetro Imprime etiquetas de Separação por OC no WMS, que determina se haverá geração de etiquetas. O parâmetro IMPETQVOL é utilizado apenas para os produtos cuja área de separação está configurada como separação por produto.

Uma vez configurado como “Ao colocar o produto na doca”, ao colocar primeiro produto na doca, o sistema irá gerar as etiquetas para todos os produtos do pedido cujos produtos sejam da área de separação por OC. Caso o contrário, só irá gerar as etiquetas assim que terminar toda a separação.

**Restrição:** o campo sequência da etiqueta não será mais gerado para os produtos da área de separação por produto. Se houver corte no momento da separação, a inutilização das etiquetas será manual.

(1)** "Nota modelo perda estoque WMS (Saída) - NOTASAIPERDAWMS" e "Nota modelo sobra estoque WMS (Entrada) - NOTAENTSOBRAWMS":** configure nesses parâmetros modelos de nota para perda e entrada de estoque no WMS que é gerado através da tela Consulta/Consulta Estoque com Ocorrências (Avaria, Perda, Sobra, Divergência)

(1)** "Priorizar picking na separação no WMS - PRIORPICKINGWMS":** quando ligado, no momento da geração de tarefas, será priorizada a separação para os endereços de picking.

(1)** "Local para ajuste de estoque WMS - WMSLOCALAJEST":** será utilizado para definir o local padrão que será considerado no momento do ajuste de estoque entre MGE Comercial\Mitra x WMS. Ao executar a rotina de ajuste pelo SankhyaW, o sistema criará as ‘Notas de Ajuste’ no MGE WMS, considerando neste o local definido no parâmetro WMSLOCALAJEST.

(1)** "Cortar no MGE itens em falta no WMS? - CORTEFALTAWMS":** quando desligado, no envio de um pedido para o WMS, se não existir estoque no WMS, o sistema emitirá uma mensagem informando que não tem estoque.

**Exemplo:** "Não existe estoque suficiente para Separação (WMS) dos produtos:" e o processo será abortado. Quando ligado, o sistema continuará mostrando a mensagem: "Não existe estoque suficiente para  separação (WMS) dos produtos:" e logo em seguida irá mostrar: 'Cortar itens em falta no WMS?', se responder não o envio é abortado, se responder sim o sistema envia os produtos que tem estoque e os que não têm estoque são cortados. O corte pode ser visto no campo **"Qtde. Corte"**, na tela de seleção de pedidos.

(1)** "Tipo de Corte na separação do WMS? - TIPOCORTEWMS":** este parâmetro é utilizado na rotina de corte, nos casos em que a separação é feita para pedidos agrupados. Se o parâmetro estiver configurado com a opção **"Maior Quantidade"**, o sistema tentará fazer o corte no pedido que tenha a maior quantidade dos produtos. Se não conseguir fazer o corte total em apenas um pedido, pegará o próximo pedido da lista.

Se o parâmetro estiver configurado com a opção "Menor Quantidade", o sistema tentará fazer o corte no pedido que tenha a menor quantidade dos produtos. Se não conseguir fazer o corte total em apenas um pedido, pegará o próximo pedido da lista Se o parâmetro estiver configurado com a opção "Proporcionalizado", o sistema tentará fazer o corte proporcionalizando nos pedidos encontrados, onde a lógica de ordenação é em ordem crescente pelo número único do pedido e data de negociação.

(1)** "TOP p/ Venda Balcão no WMS - TOPVDBALCAOWMS":** quando o pedido estiver configurado com esta TOP, a separação deverá ser feita enviada pela opção do botão direito na tela de seleção de pedidos de venda, sem a necessidade de informar Ordem de carga. Este pedido terá prioridade na ordem de separação em relação aos pedidos da Ordem de Carga.

(1)** "Utiliza Registro de volumes no faturamento? - WMSUSAREGVOLFAT":** quando **desligado**, no faturamento de um pedido não exige que o produto tenha o campo **"Unidade p/Resumo de entrega"** preenchido e nem efetue o registro de volumes na tabela TGFVOR. No cadastro de produto, esconde os campos Unidade p/Resumo de entrega e Conversão de Volume.

Este parâmetro trabalha em conjunto com o parâmetro **“Separação por área de conferência no WMS? - SEPAREACONFWMS”**.

(1)** "Valid.Estoq p/envio WMS considera Entr.pendentes? - CONSENTRPENDWMS":** quando ligado irá considerar um estoque a receber como estoque real. **Exemplo:** ao fazer o envio para expedição se existir produtos na doca de entrada, onde foram geradas as tarefas, mas não executadas. Neste caso, o sistema entenderá como estoque, colocando a tarefa de separação dependente da tarefa de armazenagem.

(1)** "WMS aceita APENAS PDS pendentes p/ expedição? - WMSPDPENDENTE":** quando o parâmetro WMSAGRUPAPDPARC estiver ligado, no envio ao WMS, pedidos com mesmo parceiro e tipo de negociação serão agrupados e um só por uma TOP informada no parâmetro TOPENVWMSAGRUP.

(1)**"WMS agrupa PDs por parceiro na expedição? - WMSAGRUPAPDPARC":** possibilitará o agrupamento de pedidos por "Parceiro" e "Tipo de Negociação" no envio ao WMS, tanto pela opção **"Enviar para o WMS (Expedição)... "** do botão direito do mouse na tela de **"Seleção de Pedidos\Notas"** da Central, quanto nas opções **"Enviar para Expedição..."** e **"Enviar para Expedição por OC..."** do botão direito do mouse na tela de **"Formação de Carga"**.

Os pedidos selecionados nestas opções serão agrupados em um só com a TOP que será informada no parâmetro TOP Pedido Agrupado p/ Enviar ao WMS (Expedição). Contudo, os pedidos de mesmo "Parceiro" e "Tipo de Negociação", enviados ao WMS, que foram lançados com alguma TOP indicada no parâmetro TOP p/ Venda Balcão no WMS, serão todos agrupados em um só, por esta mesma TOP e não pela que estiver indicada no parâmetro TOPENVWMSAGRUP.

Os pedidos que forem agrupados ficarão como não pendentes e os criados estarão confirmados e pendentes. As TOPs dos pedidos usados no agrupamento não poderão ter os campos **"TOP p/ Faturamento:"** e **"TOP p/ Separação:"** da aba **"Propriedades do Cadastro de TOP"** preenchidos, apenas a TOP que será usada para agrupá-los poderá ter estes campos preenchidos.

Após o agrupamento o "Pedido Gerado" é enviado ao WMS contendo todos os itens dos “Pedidos Origem” e a partir daí o processo continua normalmente para a Expedição do WMS

(1)** "TOP pedido agrupado p/ enviar ao WMS (Expedição) - TOPENVWMSAGRUP":** trabalha em conjunto com o parâmetro WMSPDPENDENTE. Configure a TOP que será utilizada para agrupar os pedidos em um novo pedido.

(1)** "Lote automático no envio para o WMS - LOTEENVIOWMS":** esta rotina foi criada para produtos que são controlados pelo WMS, tem controle por lote e possuem a opção **"Usar controle adicional no WMS?"** marcada na aba **"WMS"** do Cadastro de Produtos. Assim, em um Pedido no qual haja um produto com lote armazenado no WMS, este item não deverá ter seu campo **"Controle (lote)"** preenchido e o Pedido deve ser confirmado, podendo ser enviado pelos processos normais de envio ao WMS.

No envio para o WMS, o sistema irá explodir o item no Pedido, gravando os lotes encontrados, buscando o de menor validade e assim por diante, até atender a quantidade do pedido. Para funcionamento correto desta customização o parâmetro Controle Automático por Data de Validade de Lote? deve estar desabilitado.

(1)** "Utiliza Integração da Produção x WMS - INTEGRAWMSPROD":** este parâmetro ativa as funcionalidades de integração entre WMS e Produção. Processo específico de cliente e não deve ser utilizado para outros clientes.

(1)**"Endereço de checkout indefinido - ENDECKTINDEF":** entre no cadastro de endereços e crie um novo endereço identificado como Endereços Exclusivos de Conferência. O código reduzido deste endereço deve ser informado neste parâmetro. No coletor, assim que ele encontrar uma tarefa de separação em que o endereço de destino é o endereço definido no parâmetro ENDECKTINDEF, ele chama um serviço que verificará se existe algum endereço de checkout disponível. Se o endereço existir, ele fará a troca para todos os itens de tarefa da tarefa em questão para esse endereço encontrado. Além disso, o serviço já trata os estoques, transferindo do endereço de checkout indefinido para o endereço encontrado.

Na segunda fase da tarefa, no coletor, já aparecerá o endereço encontrado. Se o usuário rejeitar a tarefa na segunda fase, o endereço destino não irá retornar para o endereço definido no parâmetro. No MGEWMS, ao fazer o envio para o WMS e a separação por área de separação, o endereço de destino sempre será gerado para o endereço definido no parâmetro.

(1)** "Endereço de checkout indefinido atribuído de forma - CKTINDEFAUTOM":** quando estiver desligado, ao cumprir as separações de uma tarefa e clicar para bipar o destino, o sistema aceitará que seja qualquer endereço de checkout, desde que esteja configurado na área de separação da respectiva tarefa e que não esteja ocupado. Mas, se o parâmetro estiver ligado, o sistema ao buscar o destino irá indicar o endereço daquela área de separação exigindo que o checkout seja aquele definido pelo sistema. Para as duas situações o parâmetro **"Endereço de checkout indefinido - ENDCKTINDEF"** deve estar habilitado.

(1)** "Proibir digitação no coletor do WMS? - PROIBEDIGCOLWMS":** o padrão deste parâmetro é ligado. Quando ligado, nas tarefas de armazenagem e separação, caso o usuário tente digitar o código do endereço, o sistema irá emitir a seguinte informação: "Utilize o leitor de cód. barras para realizar a leitura".

(1)** "Tempo em ms para permitir digitação no coletor - WMSTMINDIG":** informe neste parâmetro o tempo mínimo de espera para bloquear a entrada de caracteres manualmente nos campos de endereço e produto das tarefas do coletor. O padrão é 300 milissegundos. Quanto menor esse valor, mais rapidamente o coletor é bloqueado para digitação. Depende do parâmetro PROIBEDIGCOLWMS para funcionamento.

(1)** "Utiliza reabastecimento em transferência no WMS - REABTRANSFWMS":** se estiver ligado, o reabastecimento em transferências será feito normalmente, se estiver desligado não será feito. Lembrando que esta funcionalidade deixou de ser passiva do parâmetro **"LIGAREABESTWMS".** Ou seja, se o parâmetro LIGAREABESTWMS estiver ligado, mas o REABTRANSFWMS não estiver, o reabastecimento não será feito em transferências e, por consequência, o parâmetro REABTRANSFWMS passa a ser passivo do parâmetro LIGAREABESTWMS, funcionando apenas quando o último estiver ligado.

(1)** "Priorizar endereços de pulmão vazio na armazenagem? - WMSPIOENDVZARM":** quando este parâmetro estiver ligado, no processo de armazenagem, altera o algoritmo de armazenagem obrigando o sistema a procurar os endereços de pulmão vazio em primeiro lugar, para depois encontrar os endereços de pulmão que tenha estoque. Com este parâmetro ligado, poderá acontecer de ter um endereço de pulmão com 1 caixa do produto x e, na hora do novo armazenamento, o sistema vai colocar este mesmo produto em um outro endereço. Mesmo com este parâmetro ligado, o sistema ainda continua priorizando os endereços de picking para depois para os endereços de pulmão.

(1)** "% de completude para completar endereço - PERCOMPTENDWMS":** este parâmetro determinará o percentual para completar o endereço de picking apenas na rotina de armazenamento.

(1)** "Endereço indefinido para movimentações - ENDEMOVINDEF":** este parâmetro determinará qual é o endereço que será usado para endereço indefinido nas movimentações pró-ativa.

(1)** "Validar prod. no end. na cont. de estoque do WMS - VALENDCONTWMS":** quando este parâmetro estiver ligado, ao fazer a contagem de inventário e existir um produto fisicamente diferente do que foi configurado no sistema, será emitida uma mensagem imediatamente, solicitando ao usuário chamar o gerente do WMS. Neste caso, não será registrado a contagem e o gerente deverá rever o cadastro de endereços ou alocar fisicamente o produto no endereço correto.

(1)** "Permitir separadores fazerem conferência? - WMSPERMCONFSEP":** parâmetro do Sankhya-W que é ativo por padrão. Quando está ligado permite que o separador faça conferência das separações que ele realizou. Mas quando está desligado, ao buscar uma conferência por pedido ou doca, o sistema filtra as separações em que o usuário logado no coletor já participou nas tarefas de separação e não deixa fazer a conferência. Portanto, com o parâmetro desligado o usuário logado no coletor só conseguirá conferir as separações que ele **não** participou das tarefas.

(1)** "Tratamento para falta de estoque no envio da OC para WMS - TRATOCWMS":** quando o estoque necessário para atender a O.C não é suficiente no WMS, este parâmetro apresenta a tela produtos com falta de estoque no WMS, onde são tomadas as decisões de corte: corte total, retirar pedido da O.C ou gerar novo pedido. Esta tela é apresentada ao fazer o envio da ordem de carga pela tela de rotinas/formação de ordem de carga. O usuário poderá tomar as seguintes ações:

**“Corte Total”:** o sistema envia todos os itens menos a quantidade cortada.

**“Retirar da O.C”:** o sistema vai tirar este pedido da OC limpando o campo Ordem de Carga na TGFCAB.

**“Gerar novo Pedido”:** o sistema gera um novo pedido com o(s) item(s) cortado(s), mantendo os dados do cabeçalho do pedido original.

Parâmetro que influencia a tela **"Produtos"** com falta de estoque no WMS’: **"Motivo de corte Obrigatório MOTCORTEOBRIG":** Na tela de Produtos com falta de estoque no WMS" os campos **"Cód. Motivo Corte"** e **"Motivo Corte"** serão de preenchimento obrigatório quando o parâmetro MOTCORTEOBRIG estiver habilitado. Caso contrário o usuário poderá informar nesta tela apenas o corte.

**Nota:** Os 'Motivos' de corte poderão ser cadastrados através da tela **"Motivos de Corte"**, disponível no menu Arquivos/Cadastros/Motivos de Corte (Consulte o Help on line deste cadastro).

(1)** "Permitir estoque fragmentado no WMS - FRAGMENTAESTWMS":** se na implantação for definido que o estoque poderá ser separado de forma fragmentada, este parâmetro deverá estar ligado, caso contrário este parâmetro deverá permanecer desligado.

(1)** "Permite bipar qualquer cod.barras em tarefas WMS? - WMSBIPQQCODBARS":** (Default ligado) O parâmetro é alterável pelo Sankhya-W. Quando ligado, pode-se bipar qualquer código de barras ativo vinculado ao produto. Caso desligado, somente será possível bipar os códigos de barra ligados ao volume da tarefa.

(1)** "Campo utilizado para ordenação, no momento do split das tarefas - CAMPOORDSPLIT":** a ordem da execução das tarefas de separação é determinada pela ordem que o usuário definir neste parâmetro. Os campos disponíveis são Todos os campos das seguintes tabelas:

TGWITT(ITT), TGFPRO(PRO), TGWEND(EN), TGWSEP(SEP). Ou seja, se o usuário quiser ordenar pelo 'Código do Produto', por exemplo, deverá informar o parâmetro da seguinte forma: CAMPOORDSPLIT= ITT.CODPROD. O interessante dessa ordenação é que se o usuário precisar criar qualquer 'campo adicional' e quiser utilizar como base da ordenação, bastará informar o mesmo no parâmetro, mais se o usuário não informar nada no parâmetro, o sistema utilizará o campo **"Sequência"** do item, para ordenar.

Exemplo - SPLIT considerando apenas PESO: Se área de separação "A" estiver configurada para 200KG e na O.C tiver 800KG para aquela área, então serão geradas 4 separações, obviamente, se o produto tiver cubagem configurada e a área de separação também, será levado em consideração a 'cubagem', no momento da geração das tarefas. A geração das separações através do split será feita apenas uma vez e para ‘Ordens de Carga’ que ainda não foram liberadas.

(1)** "Percentual máximo de ocupação das áreas de separação - PERCMAXOCUPSEP":** para fazer a quebra das separações, o sistema também leva em consideração o parâmetro PERCMAXOCUPSEP, que determina um ‘percentual base’ de ocupação de um palete, definindo a quebra do item da tarefa de separação em outro palete ou completando o mesmo até o limite de peso/m3, configurado para a área de separação. Isso só serve como base de comparação, para verificar se o palete já ultrapassou ou não o percentual máximo, pois se ele não ultrapassou o percentual máximo, o usuário poderá completa-lo até seu limite de peso/m3 máximo, indo o restante para outra separação.

(1)** "Utiliza liberação de separação - UTILLIBSEPARA":** o parâmetro tem por finalidade habilitar a utilização de liberação das áreas de separação. Quando ligado, ao descer a OC para a expedição no WMS, o sistema irá gerar as tarefas de reabastecimento e separação, porém, estas não poderão ser executadas antes da liberação das áreas de separação.

(1)** "Envio ped.Balcão WMS - ENTPENBALCAOWMS":** considera Entr.pendentes. Considera ou não entradas pendentes no envio de pedidos venda balcão para o WMS,

(1)** "Dias anteriores à dt atual p/ mostrar notas no WMS - NRODIASNOTASWMS":**  - Criado o parâmetro NRODIASNOTASWMS, na tela de Gerência de WMS, no filtro rápido para 'Nota/Pedido', o sistema irá apresentar as notas/pedidos na pesquisa, considerando a quantidade de dias informado no parâmetro.

(1)** "Exige picking quando separação prioriza picking - EXIGEPICKINGWMS":** criado o parâmetro EXIGEPICKINGWMS Default **sim**. Ao enviar uma Ordem de Carga para o WMS se o produto não tiver um endereço de picking configurado o sistema não permitirá que seja gerada a separação.

(1)** "Gerar reabastecimento corretivo sem dependente - RESCORSEMDEPWMS":** assim será gerado as tarefas de reabastecimentos porem não ira gerar a dependência a tarefa de separação.

(1)** "Priorizar volume fracionado WMS - WMSPRIORVOLFRAC":** alterada a rotina que gera a separação do WMS para pegar as unidades que tenham estoques fragmentados, em seguida, a gerar tarefas para os endereços que tem estoque completo.

Para que esta funcionalidade seja executada, foi criado o parâmetro WMSPRIORVOLFRAC, este deve estar ligado.

(1)** "Ativa nova estratégia lig. TGFVAR explosão lotes - WMSSTRATVARLOTE":** quando ligado o parâmetro ativa uma nova estratégia para restauração da TGFVAR após a distribuição dos lotes de acordo com o estoque. Neste caso, em vez de apagar a TGFVAR e recriar para um único pedido, mantemos as ligações originais, fazendo os ajustes nas quantidades conforme necessário e incluindo os novos itens ligando com os pedidos originais de acordo com os itens que sofreram alteração.

(1)** "Busca manual de tarefas de separação - BUSCAMANTARSEP":** quando ligado, o sistema ao executar a tarefa de separação não busca a próxima tarefa automaticamente, para executar a próxima tarefa é necessário clicar no botão Tarefa. No entanto, caso o referido parâmetro esteja desligado, o botão **“Tarefas”** não ficará visível.

(1)** "Configuração de registro de ocorrências do WMS - WMSREGOCOR":** o parâmetro, do tipo lista, tem as opções: "Nunca", "Sempre" e "Em caso de Corte".

**Nunca:** o sistema funcionará da mesma forma que hoje, permitindo lançar ocorrência de estoque durante as tarefas sem restrições não gerando liberação de ocorrência.

**Sempre:** antes de processar a ocorrência de estoque, o sistema irá gerar uma solicitação de ocorrência em estado "Pendente" que deverá ser liberada antes de continuar com a execução da tarefa. Quando uma tarefa está com uma solicitação de liberação em estado pendente ela não será mais buscada pelo coletor enquanto não for liberada.

**Em caso de Corte:** o sistema só gerará solicitação de liberação caso a ocorrência lançada for gerar corte na nota.

**![Imagem 5: OBSERVAÇÃO: essas solicitações só são geradas quando relacionadas a uma tarefa, ou seja, não é possível lançá-las por…](https://ajuda.sankhya.com.br/hc/article_attachments/16343570775447) OBSERVAÇÃO:** essas solicitações só são geradas quando relacionadas a uma tarefa, ou seja, não é possível lançá-las por uma ocorrência de avaria lançada pela função "Avaria" do menu principal do coletor do WMS.

Para liberar ou cancelar uma solicitação de liberação de ocorrência, foi criada a tela "Liberação de Ocorrências". Na grade são apresentadas as solicitações de acordo com o filtro. É obrigatório o uso de pelo menos um dos filtros, isso se faz necessário para evitar o carregamento de um número muito grande de solicitações. Para realizar a liberação da ocorrência clique no botão **"Liberar"** ou execute um duplo clique no registro.

(1)** "Confirma Nota no Registro de Conferência de Entrada - WMSCONFNOTARCE":** quando ligado, ao realizar a conferência pela tela **"Registro de Conferência de Entrada",** o sistema tenta confirmar as notas envolvidas no recebimento.

(1)** "Desconsiderar Est.bloq. no WMS no Est. disponível - WMSDESCONESTBLQ"**: criado o parâmetro, ao ser habilitado o sistema desconsidera o estoque bloqueado WMS no momento de criar os pedidos nas centrais.

(1)** "Detalhar volumes em conferências p/pedido no WMS - DETALHAVOLWMS:** em empresas nas quais os pedidos possuem diversos itens de tamanhos variados, é comum que um mesmo volume contenha diversos produtos diferentes. Se os pedidos possuírem diversos itens, e com isto forem gerados diversos volumes, pode haver a necessidade de se identificar o conteúdo de uma determinada caixa.

Para facilitar esta conferência do conteúdo, o WMS oferece a possibilidade de se imprimir nas etiquetas informações sobre o conteúdo de um determinado volume, listando os itens que compõe uma determinada caixa.

Para isto, é necessário ligar o parâmetro Detalhar volumes em conferências p/pedido no WMS ?.

O parâmetro modifica a tela de **"Conferência por pedido"**, possibilitando que a formação de volumes aconteça ao longo do processo de conferência. Este processo é necessário para que seja possível a impressão posterior de etiquetas listando os produtos do volume.

(1)** "Endereço de checkout indefinido - ENDECKTINDEF":** entre no cadastro de endereços e crie um novo endereço identificado como Endereços Exclusivos de Conferência. O código reduzido deste endereço deve ser informado no parâmetro ENDECKTINDEF.

Assim, no coletor, logo que ele encontrar uma tarefa de separação onde o endereço de destino é o endereço definido no parâmetro ENDECKTINDEF, ele chame um serviço que irá verificar se existe algum endereço de checkout disponível.

Se o endereço existir, ele fará a troca para em todos os itens de tarefa da tarefa em questão para esse endereço encontrado.

Além disso, o serviço já trata os estoques, transferindo do endereço de checkout indefinido para o endereço encontrado.

Na segunda fase da tarefa, no coletor, já aparecerá o endereço encontrado. Se o usuário rejeitar a tarefa na segunda fase, o endereço destino não irá retornar para o endereço definido no parâmetro.

No MGEWMS, ao fazer o envio para o WMS e a separação por área de separação, o endereço de destino sempre será gerado para o endereço definido no parâmetro.

(1)** "Endereço de checkout indefinido atribuído de forma - CKTINDEFAUTOM":** habilita a busca de endereço de checkout disponível automática na separação por pedido.

(1)** "Exigir Norma de Paletinização no WMS - WMSEXIGENORMPAL":** quando ligado o sistema vai realizar as validações abaixo de Lastro de Camadas no cadastro do produto.

(1)** "Formação de Volumes após a conferência por pedido - FORMVOLPOSCONF":** na formação de volumes, caso a empresa queira minimizar a quantidade de volumes a serem gerados, o momento de se gerar os volumes pode ser transferido para a Doca de Saída, reunindo "conferências" de diferentes áreas correspondentes ao mesmo pedido. Para isto, é necessário ligar o parâmetro FORMVOLPOSCONF.

Esta configuração é conflitante com a impressão de etiquetas. Portanto, os parâmetros Imprimir etiquetas de volume na conferência? e Detalhar volumes em conferências p/pedido no WMS? devem estar desligados.

Quando este último parâmetro estiver desligado o sistema irá verificar se a marcação **"Imprimir etiquetas de volume na conferência"** nas preferências da Empresa está marcada. Sendo assim, é necessário desmarcar também esta opção para uso da Formação de Volumes após a Conferência.

Após realizar a conferência por pedido, a situação das separações do pedido ficará como "Aguardando Formação por Volumes".  Quando todas as separações de um mesmo pedido estiverem com esta situação, o operador pode iniciar a Função "Formação de Volumes" no coletor.

Essa função "Formação de Volumes" só aparece quando o parâmetro FORMVOLPOSCONF está ligado e o usuário tem permissão para executar essa tarefa.

Ao escolher a função, o botão **"Volumes"** ficará habilitado na tela de identificação de funções do coletor. Ao clicá-lo, o sistema irá direcionar para uma tela onde deverá ser bipada a doca que receberá o pedido, Em seguida, será necessário bipar cada um dos checkouts relacionados ao pedido.

O sistema obrigará o usuário a digitar todos os checkouts, que serão exibidos na lista de Checkouts já bipados. O sistema permite bipar o mesmo mais de uma vez, mas no final, todos deverão estar bipados.

Após ter bipado todos os Checkouts com a lista completa, é só clicar em "próximo". Então, o usuário chegará na etapa em que informará a quantidade de volumes que serão geradas.  Depois de informada a quantidade, o sistema envia os itens do checkout para a DOCA, ficando a separação na situação "Conferência Validada" e libera a impressão da etiqueta.

(1)** "Impressora Padrão Imp. de Etiqueta de Armazenagem - WMSIMPETIQPAL":** este parâmetro foi criado para inserir o nome local de impressora mapeada no Print Service.

(1)** "Impressão de Etiqueta por Agrupamento Mínimo - USAIMPRAGRUPMIN":** este parâmetro foi criado para que o sistema considere o agrupamento mínimo na impressão das etiquetas de volumes, que é habilitada pelo parâmetro IMPETIQVOLCONF.

Ao habilitar o parâmetro USAIMPRAGRUPMIN é apresentado na tela de cadastro de produtos aba WMS o campo **"Imprimir Etiqueta de Volume por Agrupamento Mínimo"**.  Por padrão o campo do cadastro de produtos já estará marcado, isso por que a maior parte dos produtos do cliente usa a impressão por agrupamento mínimo. Atualmente, quando o cliente vai imprimir as etiquetas através do MGE, o sistema  imprime uma etiqueta para cada produto e isso causa um grade desperdício já que os produtos são embalados em agrupamentos e é necessário somente uma etiqueta para essa embalagem.

(1)** "Informar número do palete em separações agrupadas - WMSEXIGENROPL":** para separações agrupadas (por produto) ao enviar para o destino (doca) o sistema solicita a identificação do palete. Esse identificador será uma etiqueta pré-impressa com código de barras sequencial que será usada mais tarde para iniciar o processo de conferência e recontagens. Ao bipar o identificador, o sistema grava o NROPALETE na separação. Basicamente, o separador vai andar com um rolo de etiquetas que será impresso todos os dias e a perda de números ou etiquetas não causa prejuízos para o processo.

(1)** "Lote automático no envio para o WMS - LOTEENVIOWMS":** esta rotina foi criada para produtos que são controlados pelo WMS, tem controle por lote e possuem a opção **"Usar controle adicional no WMS?"** marcada na aba **"WMS"** do Cadastro de Produtos. Assim, em um Pedido no qual haja um produto com lote armazenado no WMS, este item não deverá ter seu campo **"Controle (lote)"** preenchido e o pedido deve ser confirmado, podendo ser enviado pelos processos normais de envio ao WMS.

No envio para o WMS o sistema irá explodir o item no pedido gravando os lotes encontrados, buscando o de menor validade e assim por diante, até atender a quantidade do pedido.

(1)** "Modelo de Etiqueta de Palete - WMSMODETIQPAL":** deverá ser inerido o modelo do relatório formatado no qual será configurado o modelo jrxml com informações a ser fixado no palete.

**(1)** **"Mostrar a ref. do produto em telas do coletor WMS - MOSTRAREFWMS":** Quando ligado no coletor onde é apresentada a descrição do produto será exibida também a composição "Referência (Código de Barras) + Descrição do Produto + Complemento do Produto".

(1)** "Motivo de corte no WMS é obrigatório - MOTCORTEOBRIG":** na grade inferior da tela de "Produtos com falta de estoque no WMS", foram adicionados os campos: Cód. Motivo Corte e Motivo Corte, para que o usuário informe o motivo pelo qual está realizando o corte. Esses novos campos são de preenchimento obrigatório, quando o parâmetro  Motivo de corte Obrigatório estiver habilitado. Caso  o parâmetro esteja desligado, o usuário poderá informar  apenas o corte.

(1)** "Percentual máximo de ocupação das áreas de separação - PERCMAXOCUPSEP":** para fazer a quebra das separações, o sistema também leva em consideração o parâmetro PERCMAXOCUPSEP, que determina um percentual base de ocupação de um palete, definindo a quebra do item da tarefa de separação em outro palete ou completando até o limite de peso/m3, configurado para a área de separação. </b>

Isso só serve como base de comparação, para verificar se o palete já ultrapassou ou não o percentual máximo, pois se ele não ultrapassou o percentual máximo, o usuário poderá completá-lo até seu limite de peso/m3 máximo, indo o restante para uma outra separação.

(1)** "Permite bipar qualquer cod.barras em tarefas WMS - WMSBIPQQCODBARS":** o padrão deste parâmetro é ligado e ele é alterável pelo Sankhya-W. Caso ligado, pode-se bipar qualquer código de barras ativo vinculado ao produto. Caso desligado, somente podemos bipar os códigos de barra ligados ao volume da tarefa.

(1)** "Proibir digitação de qtd. na conferência por pedido - PROIBDIGCONFPED":** este inibe a edição do campo **"Quantidade"** e funciona em conjunto com o parâmetro WMSQTDCONFDOCA, caso o mesmo não tenha quantidade padrão então o campo não será desabilitado.

(1)** "Proibir digitação no coletor do WMS - PROIBEDIGCOLWMS":** o padrão deste parâmetro é ligado. Quando ligado, nas tarefas de armazenagem e separação, caso o usuário tente digitar o código do endereço, o sistema irá emitir a seguinte informação : "Utilize o leitor de cód.barras para realizar a leitura". Esta função **não funciona** no emulador de micro computador, apenas no coletor de dados. O parâmetro PROIBEDIGCOLWMS passa a ter efeito nas tarefas de 'Armazenagem Expressa', 'Armazenagem Seletiva' e 'Movimentação Pro-ativa'

(1)** "Tipo de estratégia de reabastecimento corretivo - WMSTIPOREABAS:** quando informado "Menor saldo de estoque", ao gerar um reabastecimento, o sistema prioriza endereços que tenham menos estoque, quando informado "FIFO" mantem o comportamento atual, priorizando reabastecimento aos endereços com produtos mais antigos.

(1)** "Usa endereço de checkout adicional na separação - WMSUSACKADIC":** quando utilizado permite que na separação o usuário utilize checkouts adicionais. Os seguintes parâmetros interferem na rotina: ENDECKTINDEF, [CODEND] e CKTINDEFAUTOM Desligado.

(1)** "Utiliza conferência parcial de volumes - CONFPARCIALVOL":** esse parâmetro possibilitará realizar a conferência parcial de volumes de Pedidos em uma Doca.

Assim não será obrigatório o usuário conferir todos os Pedidos presentes na Doca, mas apenas os volumes de um determinado Pedido e concluir apenas este.

**Exemplo:**

**Pedido 1:** Separação 1 e 2  Doca 1

Volumes 1, 2 e 3.

**Pedido 2:** Separação 3 Doca 1

Volumes 4 e 5

Com o parâmetro desligado, o usuário deverá obrigatoriamente conferir os volumes de 1 a 5 (todos os volumes presentes na Doca) para só assim o sistema confirmar a conferência de ambos os pedidos, de uma vez só.

Ao ligar o parâmetro, o usuário poderá conferir os volumes 1, 2 e 3.

Assim, como o Pedido 1 foi conferido por completo, sua separação será marcada como Conferida, e poderá seguir seu processo. Enquanto o Pedido 2 ainda ficará pendente de Conferência, já que o volume 4 e 5 não foi conferido.

No caso do usuário cancelar a conferência de volumes neste momento, o sistema não invalidará o Pedido 1, que já foi completamente conferido, cancelando apenas a conferência do Pedido 2, que ainda está em aberto.

(1)** "Validar M3 na Movimentação Pró-Ativa - WMSVALM3MOVPRO":** valida a transferência de produtos na Movimentação Pró-Ativa, caso ligado o sistema verifica o M3 do produto em relação ao endereço de destino.

(1)** "Validar peso na Movimentação Pró-Ativa - WMSVALPESMOVPRO":** valida a transferência de produtos na Movimentação Pró-Ativa, caso ligado o sistema verifica o peso do produto em relação ao endereço de destino.

(1)** "Validar prod. no end. na cont. de estoque do WMS - VALENDCONTWMS":** criado parâmetro VALENDCONTWMS, quando estiver ligado, ao fazer a contagem de inventário e existir um produto fisicamente diferente do que foi configurado no sistema, será emitida uma mensagem imediatamente, solicitando ao usuário chamar o gerente do WMS. Neste caso, não será registrado a contagem e o gerente deverá rever o cadastro de endereços ou alocar fisicamente o produto no endereço correto.

(1)** "Validar produtos/endereço em pulmão ao contar - VALCONTPULMWMS":** quando ligado, nas tarefas de contagem do estoque, será feito a validação do produto contado com o produto que está registrado no sistema, se houver divergência será emitido um alerta para o usuário, solicitando refazer a contagem.

(1)** "Validar unidade na Movimentação Pró-Ativa - WMSVALUNMOVPRO":** este parâmetro quando ligado valida se o volume que está no destino é igual ao volume do produto. Ou seja, caso o volume do produto seja UM e no pulmão seja CX, o sistema não vai permitir a transferência do produto.

(1)** "Confirmação NF de Entrada Manual WMS - CONFENTRMANWMS":** quando top de compra der entrada no WMS  e parâmetro igual a sim, o usuário poderá confirmar a nota antes de enviar para o WMS.

(1)** "Desconsidera estoque em doca do WMS - SUBESTDOCAWMS":** quando ligado subtrai do estoque a quantidade que está na DOCA. Esta implementação se fez necessária para quando for realizar uma venda não considerar os produtos que não foram armazenados ainda. Na consulta de produtos o sistema verifica a quantidade que está na doca e subtrai do campo **"Estoque"** e **"Disponível"** no **"Detalhes de Estoque".**

(1)** "Gerar reabastecimento corretivo no WMS - REABCORRECAOWMS":** Criado o parâmetro, quando ele estiver ligado, ao mandar gerar uma separação e o estoque do picking não for suficiente, o sistema comandará um reabastecimento ao qual extrapolará o estoque máximo do picking. Somente após a execução do reabastecimento é que poderá ser realizada a tarefa de separação, fazendo com que o separador vá ao picking apenas uma vez.

(1)** "Imprimir etiquetas de volume na conferência - IMPETIQVOLCONF"** Para  separação por pedidos será necessário a ativação do parâmetro Imprimir etiquetas de volume na conferência?, com ele a conferência de volumes, para separações que foram feitas nas áreas de separação "Por Pedido", estará habilitada no 'Coletor'.

Ou seja, ao enviar a conferência de uma expedição que foi feita em uma área de separação "Por Pedido" o sistema abrirá no "Coletor" uma janela na qual o usuário informará a quantidade de "Volume" gerada. Ao clicar em "Enviar", para cada volume será criada uma linha na tabela de "Registro de Etiquetas de Volume" (TGWREV) com chave no campo **"Identificação do Registro de Etiquetas de Volumes"** (IDREV) que será a identificação (Código de Barras) de cada etiqueta.

(1)** "Permite Reabastecimento p/ Estoq.Min zero no WMS - REABESTZEROWMS":** quando ligado, irá fazer o reabastecimento quando o endereço estiver configurado com o estoque mínimo igual a zero. Se estiver desligado, o reabastecimento só será gerado se o estoque mínimo do endereço for maior que zero.

(1)** "Priorizar picking na Separação no WMS - PRIORPICKINGWMS":** quando ligado, no momento da geração de tarefas, será priorizado a separação para os endereços de picking.

(1)** "Regra de armazenagem para devoluções de venda - WMSREGRARMDEV":** Usa Regras de armazenagem. O sistema usa as regras de armazenagem, conforme o comportamento atual. Prefere Picking respeitando limite máximo. O sistema respeita a o máximo do piking, contudo caso o máximo do piking seja atingido e ainda tiver produtos a ser armazenados o mesmo respeita a "Configuração de Armazenagem". Prefere Picking extrapolando limite máximo. O sistema armazena todos os produtos no piking mesmo que a quantidade máxima do piking seja atingida.

**![Imagem 6: OBSERVAÇÃO: O referido parâmetro não é soberano a Configuração de Armazenagem. Caso o produto não tenha nenhuma regra…](https://ajuda.sankhya.com.br/hc/article_attachments/16343570775447) OBSERVAÇÃO:** O referido parâmetro não é soberano a Configuração de Armazenagem. Caso o produto não tenha nenhuma regra vinculada ou a regra vinculada não tenha nenhuma opção ativa, o sistema não conseguirá gerar as tarefas. Não importa a posição que o Picking esteja e se o mesmo esteja ativo, o sistema sempre irá gerar tarefas para o picking.

(1)** "Separação por área de conferência. Este parâmetro liga as telas descritas abaixo - SEPAREACONFWMS"**:

1. Arquivos/Cadastros/Área de Conferência.

2. Arquivos/Cadastros/Área de Separação.

3. Cadastro de produtos, aba WMS os campo: "Cód. Área Separação" e "Unidade p/ Resumo de Entrega".

4. No Cadastro de endereçamento o Campo "Exclusivo para Conferência".

5. Opção "Conferência por Pedido", no cadastro "Definir Tarefa e Volume por usuário".

6. Rotinas/Registro de Volume.

7. Botão direito da tela de Rotinas/Formação de carga, a opção: "Enviar para Expedição por OC". Altera a forma de envio da opção o "Enviar para expedição" no botão direito da seleção de pedidos, fazendo o envio dos pedidos apenas para os locais que tem a definição "por pedido", no cadastro de área de separação.

8. Formatador de Relatórios/Registro de volumes.

(1)** "Tipo de Corte na separação do WMS - TIPOCORTEWMS":** Este parâmetro é utilizado na rotina de corte, nos casos em que a separação é feita para pedidos agrupados.

Se o parâmetro estiver configurado com a opção "Maior Quantidade", o sistema tentará fazer o corte no pedido que tem a maior quantidade dos produtos. Se não conseguir fazer o corte total em apenas um pedido, pegará o próximo pedido da lista.

Se o parâmetro estiver configurado com a opção "Menor Quantidade", o sistema tentará fazer o corte no pedido que tem a menor quantidade dos produtos. Se não conseguir fazer o corte total em apenas um pedido, pegará o próximo pedido da lista.

Se o parâmetro estiver configurado com a opção **"Proporcionalizado"**, o sistema tentará fazer o corte proporcionalizando nos pedidos encontrados, no qual a lógica de ordenação é em ordem crescente pelo número único do pedido e data de negociação.

(1)** "Utiliza liberação de separação - UTILLIBSEPARA":** quando ligado aparecerá na tela Arquivos/Cadastros/Área de Separação os campos M3 e peso máximo no MGEWMS.

No SankhyaW exigirá que seja feita liberação pela tela Liberação de Ordens de carga para que sejam executadas as tarefas de separação ou reabastecimento, ou seja, o parâmetro tem por finalidade habilitar a utilização de liberação das áreas de separação. Quando ligado, ao descer a OC para a expedição no WMS, o sistema irá gerar as tarefas de reabastecimento e separação, porém, estas não poderão ser executadas antes da liberação das áreas de separação.
