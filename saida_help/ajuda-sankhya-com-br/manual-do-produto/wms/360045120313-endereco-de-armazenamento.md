---
id: "360045120313"
titulo: "Endereço de Armazenamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-10-19T21:18:09Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "WMS", "Estoque Mínimo", "Estoque", "WMSINCEXPAUTO", "Endereço de Armazenamento", "Altura", "CONFCEGTARARM", "ENDPRODNOVO", "Estoque Máximo", "Largura", "LIGAREABESTWMS", "Metro Cúbico Max.", "Peso Máximo", "Picking", "Profundidade", "REABPICKUNIDMUL", "RESPESTMAXPICK", "UTIMULPROENDCON", "VALESTMAXMEDIDA", "Validar estoque máximo versus peso e volume do endereço", "WMSENDERPERMVAZ", "WMSREGRARMDEV", "Endereço de Armazenamento manual", "br.com.sankhya.wms.EnderecoArmazenamento", "Cadastro", "Código identificador facilita rotinas", "Informação visível no Coletor", "Marcadores e propriedades específicas", "Squad WMS"]
---

# Endereço de Armazenamento

```
 Módulo: WMS > Cadastros
```

---

Antes de dar início ao Cadastro de Endereços de Armazenamento, é necessário definir sua Máscara, ou seja, o embasamento numérico em que serão realizados os cadastros. O **"Endereço"** é formado em níveis pré-configurados através do parâmetro **"Máscara para Endereços WMS** **-** **MASCENDWMS"**.

**Observação:** se a máscara for informada na tela [Máscara para endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120513) antes de configurá-la no parâmetro Máscara para Endereços WMS - MASCENDWMS, este será automaticamente preenchido com o que foi configurado na tela dita anteriormente.

Caso nenhuma máscara seja definida e a tela de Cadastro de Endereço de Armazenamento seja aberta, o sistema emitirá a seguinte mensagem:

**"Parâmetro para máscara de hierarquia 'MASCENDWMS', não encontrado".**

Nesta rotina cadastre/configure os Endereços, para que estes aceitem ou não, o armazenamento de um Produto ou Grupo de Produtos. Trataremos a seguir, sobre os seguintes tópicos referentes a tela:

|  |  |  |
| --- | --- | --- |
| [Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#preenchimentosiniciais) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) |
| [Aba Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abamedidas) |  | [Aba Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto) |
| [Aba Grupo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abagrupodeprodutos) |  | [A](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abamovimentaovertical)[ba Movimentação Vertical](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abamovimentaovertical) |
| [Aba Unidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaunidade) |  | [Aba Reabastecimento Picking](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abareabastecimentopicking) |
| [Aba Unitizador (UMA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#AbaUnitizador(UMA)) |  | [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#botooutrasopes...) |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#parmetrosqueinfluenciamestarotina) |  | [Movimentação Vertical - Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#movimentaovertical-processo) |
| [Configurações recomendadas por tipo de endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#configura%C3%A7%C3%B5es-recomendadas-por-tipo-de-endere%C3%A7o) |  |  |

## Preenchimentos Iniciais

![Imagem 1: Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/article_attachments/9811061950487)

O **"Endereço reduzido"** é o código correspondente ao endereço, que irá facilitar sua posterior identificação nas rotinas em que for utilizado. É uma numeração gerada manual ou automaticamente; esta definição é feita através do botão ![Imagem 2: O "Endereço reduzido" é o código correspondente ao endereço, que irá facilitar sua posterior identificação nas rotinas…](https://ajuda.sankhya.com.br/hc/article_attachments/16844534287767) **"Configuração da Tela"**.

Informe a **"Descrição"** pertinente ao endereço; esta descrição, será apresentada para o usuário do [Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112173).

O **"Endereço"** é informado de acordo com a definição realizada no parâmetro Máscara para Endereços WMS - MASCENDWMS citado inicialmente; se trata do código dos endereços.

A marcação **"Ativo"** determina se o endereço poderá ser utilizado (quando marcado), ou não (quando desmarcado) nas rotinas do sistema.

O endereço marcado como **"Analítico"** representa o último nível na hierarquia dos cadastros, pois não poderá ter endereços filhos.

A marcação **"Exclusivo p/ Conferência"** é habilitada pela ativação do parâmetro **"Separação por Área de Conferência no WMS? - SEPAREACONFWMS"** e faz parte do Processo de Separação e Conferência por Área no WMS. Os endereços que possuírem esta marcação, serão identificados como endereços para Checkouts (balcões de conferência).

Através da marcação **"Movimentação Vertical?"** determine o comportamento do endereço em questão, quanto a este tipo de movimentação; maiores detalhes, podem ser visualizados neste tópico, pelo link [Movimentação Vertical - Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#movimentaovertical-processo).

Por meio da marcação **"Tipo"** indique a característica principal do endereço que está sendo cadastrado. Um Endereço de Armazenamento, pode ser do tipo:

- Apartamento;
- Bloco;
- Depósito;
- Nível;
- Prédio;
- Rua.

O campo **"Lado"** determina o flanco correspondente ao endereço na rua; pode ser Ímpar ou Par.

**Observação:** caso seja feita feita a tentativa de modificação das marcações Exclusivo p/ Conferência ou Movimentação Vertical?de um endereço que já possua estoque, as seguintes mensagens serão apresentadas, respectivamente:

**"O campo "Exclusivo p/ Conferência" não pode ser modificado pois o endereço possui estoque."**

**"O campo "Movimentação Vertical" não pode ser modificado pois o endereço possui estoque."**

Nos casos em que o endereço não possuir estoque, e alguma destas marcações for efetuada, os campos da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) (exceto o campo **"Ordem"**) serão desmarcados e o campo **"Situação do Estoque"** será alterado para **"Disponível"**.

O campo **"Empresa"** corresponde a organização à qual o endereço de armazenamento está vinculado.

As abas que serão apresentadas abaixo, ficarão desabilitadas para preenchimento com as seguintes combinações de marcação:

- Somente Exclusivo p/ Conferência marcado;
- Se Analítico não estiver marcado, independentemente de como estejam as outras marcações;
- Somente Movimentação Vertical? estiver marcado ou não;
- Exclusivo p/ Conferência, Movimentação Vertical? e Analítico marcados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Geral

Deverão ser configuradas nesta aba as propriedades do endereço, ficando habilitada somente se o endereço for analítico.

A marcação **"Multi Produto"** quando assinalada, informa ao sistema que este endereço poderá receber mais de um produto diferente ao mesmo tempo.

Por meio da marcação **"Permite Expedição"** tem-se que neste endereço é possível fazer coleta de mercadorias. Utilizado para todos os endereços, exceto Docas.

Realizando a marcação **"Picking"** será informado ao sistema que este endereço é um Picking, ou seja, lugar em que os produtos são armazenados fracionados.

**Observação:** ao marcar o endereço como Picking, as abas [Grupo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abagrupodeprodutos) e [Unidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaunidade) serão **desabilitadas**, pois uma vez que o endereço é Picking, a configuração deverá se feita pela aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto).

A marcação **"Permite Fragmentar Estoque"** deve ser realizada em endereços onde é permitido pegar partes do estoque existente, como por exemplo, Picking. Endereços onde não é permitido apanhar partes do estoque, não deverão ter esta opção marcada, como por exemplo, no armazenamento de Paletes que não podem ser fragmentados. Saiba mais informações sobre esta marcação, clicando no link [Processo de Garantias no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598634).

A Separação respeitará a marcação Permite Fragmentar Estoque do endereço. Quando o sistema não conseguir separar na unidade em que foi agrupado, ele verificará se existe estoque nas unidades menores (continua a verificação nas unidades maiores).

**Observação:** este caso só irá acontecer, quando o fator de conversão for igual a 1 (um).

Por exemplo:

Produto que tem 1 Palete = 1 Milheiro, pois neste caso sendo o mesmo fator, ele não poderá identificar se o Palete ou o Milheiro é a maior unidade.

Através do campo **"Ordem"** defina a ordenação para alguns processos. No caso de armazenamento, este campo pode ser utilizado para definir a proximidade entre endereços de pulmão e picking.

**Observação:** deve ser analisado a melhor estrutura de criação do ordenamento, para obter melhores aproveitamentos para esta finalidade. Por exemplo, usar a própria estrutura de números correspondente ao endereço é uma das estratégias, ou números simples e sequenciais que refletem esta necessidade.

Em caso de expedição, este campo será responsável por definir a sequência de apresentação das tarefas de separação do coletor de dados. Este campo não influencia majoritariamente na escolha dos endereços de separação durante o envio da onda. Ou seja, não define de forma prioritária se um endereço será utilizado ou não na criação das tarefas, isso porque o sistema conta com várias outras regras anteriores e importantes, tais como FIFO, FEFO, menor esforço (Disponibilidade para atender a pedidos) e entre outros. Este é um dos últimos critérios de ordenação.

O campo **"Situação do estoque"** determinará se os produtos correspondentes ao endereço, estão Disponíveis ou Bloqueados.

\*\*Observação:\*\*para que seja possível realizar movimentações de produtos bloqueados no WMS (localizados em endereços Bloqueados), é necessário que o parâmetro **"Desconsiderar Est.bloq. no WMS no Est. disponível - WMSDESCONESTBLQ"** esteja desativado. A ativação deste parâmetro impede a confirmação de notas que contenham itens bloqueados no WMS, pois o estoque nessa situação será ignorado; o sistema não irá considerá-lo como disponível.

A marcação **"Permitir apenas contagem por produto"** deverá ser utilizada em endereços que só aceitam contagem de inventário por produto. É uma marcação que evita a geração acidental de inventário por endereço em endereços que possuem muitos produtos e que por esta razão teriam contagem zero para os produtos não contados.

Quando um endereço estiver com a marcação Permite contagem apenas por produto realizada, o sistema não permitirá gerar inventário para este endereço sem informar o produto. Em endereços que possuem múltiplos produtos, mas que estejam com esta opção desmarcada o sistema permitirá gerar contagem por endereço (sem informar produto), e neste caso o sistema gerará contagem zero para todos os produtos não contados que estejam em estoque.

Ao realizar a marcação **"Usa picking intermediário"** será indicado que este é um endereço cujas tarefas devem levar a um picking intermediário.

A marcação **"Picking Intermediário"** indica que o endereço em questão, é um picking intermediário.

**Importante:** as duas marcações anteriores visam sistematizar o processo de separação de itens controlados da empresa. Fazendo com que o sistema utilize pickings intermediários, ligando uma área de separação à outra, através de Reabastecimento por **"Ordem Carga"** dos produtos a serem separados, sendo este reabastecimento restrito apenas a usuários configurados para área dos endereços de origem, ou seja, para a área controlada.

Os endereços da área controlada devem participar das demais áreas de separação, ou seja, esta não será uma área de separação específica. Contudo, a área controlada deverá possuir um grupo de endereço diferente das áreas não controladas. Desta forma, o MGE gerará as tarefas de separação, normalmente Por Pedido, pegando dos pickings existentes na área controlada e como destino um checkout indefinido (ou definido). Durante o processo de liberação de Ordem de Carga para separação, as tarefas geradas serão reprocessadas de forma a atender o processo da área controlada, ou seja:

- Todos os itens de tarefa cujo endereço de origem estejam marcados como Utiliza picking intermediário serão agrupados por grupo de endereços e então para cada um desses grupos será gerada uma tarefa de reabastecimento corretivo;
- O reabastecimento liga a origem da tarefa original a um picking intermediário. O picking intermediário deverá estar inicialmente livre de tarefas ou estoque provenientes de outras ordens de carga;
- A continuação da tarefa fica sendo do picking intermediário ao endereço de checkout;
- A tarefa que leva do picking intermediário ao checkout é dependente da tarefa que leva da área controlada ao picking intermediário;
- Se for feita alguma ocorrência na tarefa de reabastecimento do picking intermediário, somente outras áreas controladas (que possuem cadastro de grupo de endereços) poderão reabastecer o picking intermediário;
- No parâmetro **"Tipo de estratégia de reabastecimento corretivo - WMSTIPOREABAS"** quando definido pela opção Menor saldo de estoque, ao gerar um reabastecimento, o sistema prioriza endereços que tenham menos estoque; se definido como FIFO será priorizado o reabastecimento aos endereços com produtos mais antigos.

Determine no campo \*\*"\*\***Nro. máximo de produtos"**, o limite máximo de produtos que serão aceitos no endereço em questão. Quando o endereço se tratar de um picking, o campo estará desabilitado para preenchimento, pois um picking possui sua configuração própria. A definição realizada neste campo, é similar a realizada no campo Nro. máximo de produtos no endereço localizado na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) das **"Preferências da Empresa"**, sendo que a informação deste último é prioritária sobre o valor inserido no primeiro campo citado. Além disso, esta configuração está ligada aos cadastros realizados na tela [Produtos Compatíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613434), de modo que poderão ser armazenados no endereço o máximo de produtos aqui definidos.

A marcação \*\*"\*\***Reabastecido por Picking"**, determina se o endereço em questão é reabastecido por um outro endereço de picking; neste caso, ambos os endereços (o que irá reabastecer e o que será reabastecido) precisam ser Picking's. Além disso, esta marcação irá habilitar a aba [Reabastecimento Picking](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abareabastecimentopicking).

\*\*Observação:\*\*no parâmetro **"Endereço WMS para produtos novos** **-** **ENDPRODNOVOWMS"** informe o código do \*\*"\*\***Endereço Reduzido"** do endereço curinga. Assim, ao realizar um recebimento na geração das tarefas de armazenagem o sistema irá ignorar a marcação Permitir Expedição definido como Não para o endereço curinga, que está configurado no parâmetro de chave ENDPRODNOVOWMS e gerará as tarefas para este endereço.

Depois do sistema armazenar o produto no endereço curinga, por meio da Movimentação Pró-Ativa, você pode realizar a transferência deste produto para o endereço de destino. Quando o sistema realiza essa transferência, desvincula o produto do endereço curinga.

**Nota:** o endereço curinga deve ter as seguintes configurações:

- Ativo - Sim
- Multi Produto - Sim
- Permitir Expedição - Não
- Picking - Sim
- Permitir Fragmentar Estoque - Sim
- Permitir Apenas Produtos Relacionados - Sim

Ao selecionar a marcação **"Lote Único"** nos endereços, não será permitida a inserção de mais de um lote por produto no endereço correspondente, porém você poderá inserir mais de um produto desde que o endereço esteja com a configuração Multi Produto feita. Assim, destacamos:

- Se você tentar realizar a marcação, mas o endereço já tiver Lotes distintos cadastrados, o sistema o informará que a ação não será concluída, pois há mais de um lote por produto armazenado no endereço em questão;
- Nas tarefas de recebimento e armazenagem, se o endereço utilizado possuir a marcação habilitada, ao realizar a tarefa o sistema irá validar se já existe produto no endereço e se ele é controlado por lote, assim, o recebimento irá para um endereço que possua o mesmo lote ou para um endereço vazio. Os produtos também serão enviados aos endereços, dessa forma caso sejam lançados em uma mesma nota, e estejam com lotes diferentes;
- Ao tentar realizar uma Transferência entre Endereços, Movimentação Pró-Ativa ou Remanejameno de Estoques, o sistema validará se os endereços de destino utilizados estão com a marcação Lote Único realizada. Se sim, a transferência será feita caso os endereços de destino possuírem apenas um lote por produto após a conclusão da operação, caso contrário, a movimentação/transferência não poderá ser concluída;
- Quando uma contagem for realizada em um endereço de Lote Único, não será possível informar mais de um lote para o mesmo produto. Porém, no endereço poderá ser informado mais de um produto, caso o mesmo esteja configurado como Multi Produto, uma vez que a regra do campo Lote Único é exclusiva de lote, não de produto;
- Nas movimentações pró-ativas realizadas pelo coletor, só será possível realizar movimentações de endereços de Lote Único se o endereço de destino possuir o mesmo lote do endereço que está sendo movimentado, ou caso o endereço do Lote Único estiver vazio.

**Observação:** a marcação Lote Único será exibida apenas se o parâmetro \*\*"Utiliza lote único por endereço? - LOTEUNICOXEND"\*\*estiver ligado e poderá ser habilitado se a marcação Permite expedição for selecionada.

**Nota:** os produtos cadastrados nos endereços que possuírem o Lote Único, devem ser controlados por lote.

**Observação:** atualmente, o Lote Único não trabalha com separação por esteiras.

Além disso, para a realização dos tipos de Ressuprimentos Corretivo, Automático e Preventivo com Lote Único, os endereços de picking devem estar com estoque zerado ou o produto do pulmão com o mesmo lote de picking.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Configurações recomendadas por tipo de endereço

As marcações do endereço mudam conforme o papel dele no WMS. O quadro abaixo resume o que marcar em cada caso. As marcações que não aparecem no quadro ficam desmarcadas, salvo necessidade específica.

**ℹ️ Nota**

As marcações da aba **Geral** só ficam editáveis se o endereço estiver marcado como **Ativo** e **Analítico**.

| **Marcação** | **Picking** | **Pulmão** | **Doca** | **Checkout** | **Especiais (avaria, divergência, perda e sobra)** |
| --- | --- | --- | --- | --- | --- |
| **Picking** | Marcar | Não marcar | Não marcar | Não marcar | Não marcar |
| **Permite Expedição** | Marcar | Marcar | Não marcar | Não marcar | Não marcar |
| **Permite Fragmentar Estoque** | Marcar, se usa fragmentação | Marcar, se usa fragmentação | Marcar | Não marcar | Não marcar |
| **Multi Produto** | Opcional | Opcional | Marcar | Não marcar | Marcar |
| **Lote Único** | Opcional ¹ | Opcional ¹ | — | — | — |
| **Exclusivo p/ Conferência** | Não marcar | Não marcar | Não marcar | Marcar ² | Não marcar |
| **Situação do estoque** | Disponível | Disponível | Disponível | — | Bloqueado ³ |

¹ **Lote Único** só aparece com o parâmetro **"Utiliza lote único por endereço? - LOTEUNICOXEND"** ligado e só pode ser marcado se **Permite Expedição** estiver marcado. A regra é de lote, não de produto: com **Multi Produto** marcado, o endereço continua aceitando mais de um produto diferente, só não aceita mais de um lote por produto.

² **Exclusivo p/ Conferência** depende do parâmetro **"Separação por Área de Conferência no WMS? - SEPAREACONFWMS"**. Ao marcá-la, as demais abas do endereço são desabilitadas: o checkout é apenas balcão de conferência.

³ **Bloqueado** não é uma marcação própria: é o campo **Situação do estoque** = **Bloqueado**, na aba **Geral**. Para movimentar estoque bloqueado no WMS, o parâmetro **"Desconsiderar Est.bloq. no WMS no Est. disponível - WMSDESCONESTBLQ"** deve estar desativado.

Na Doca, **Permite Expedição** não é usado, porque a marcação vale para todos os endereços, exceto Docas. **Multi Produto** é necessária porque a doca recebe produtos sortidos: sem ela, o sistema recusa um segundo produto no mesmo endereço. Para saber mais, acesse [Configurações para validar endereço de DOCA](https://ajuda.sankhya.com.br/hc/pt-br/articles/20648185367191-Configura%C3%A7%C3%B5es-para-validar-endere%C3%A7o-de-DOCA).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Medidas

Configure obrigatoriamente nesta aba as dimensões do endereço, não permitindo o armazenamento de produtos que ultrapassem essas definições.

![Imagem 3: Configure obrigatoriamente nesta aba as dimensões do endereço, não permitindo o armazenamento de produtos que…](https://ajuda.sankhya.com.br/hc/article_attachments/9811124300823)

Determine o **"Nível"** do endereço em relação aos demais.

Informe a **"Altura"** do endereço em questão.

Defina a **"Largura"** do endereço que está sendo cadastrado.

Indique a **"Profundidade"** do endereço de armazenamento.

No campo **"Metro Cúbico Máx."** informe o metro cúbico máximo permitido para este endereço. Este campo é o resultante do cálculo dos campos Altura x Largura x Profundidade. Você pode indicar um valor superior ao resultado deste cálculo, porém não será aceito um valor inferior. Caso seja informado um valor menor que o calculado, será apresentada a seguinte mensagem:

**"Valor do Campo "Metro Cúbico Max." não pode ser menor do que "Altura x Largura x Profundidade"."**

**Observação:** para que a comparação do volume seja realizada, é preciso que o cadastro da Altura, Largura e Profundidade do endereço sejam realizados em metros.

Informe no campo **"Peso Máximo"** a carga extrema suportada por este endereço. Caso o produto que está sendo recebido tenha um peso superior ao informado neste campo, o sistema não será capaz de armazená-lo, deixando-o na doca de entrada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Produto

Adicione nesta aba, os [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) que poderão ser proibidos, exclusivos ou permitidos para este endereço.

![Imagem 4: Adicione nesta aba, os Produtos que poderão ser proibidos, exclusivos ou permitidos para este endereço.](https://ajuda.sankhya.com.br/hc/article_attachments/9811128095767)

Inicialmente no campo **"Produtos Relacionados"**, você pode definir três vínculos para os produtos. A saber:

- **Proibir:** Selecionando esta opção, os produtos posteriormente inseridos na grade abaixo, não poderão ser armazenados no endereço selecionado.
- **Exclusivo:** Por esta marcação, será representado que os produtos incluídos na grade, poderão ser armazenados apenas no endereço selecionado, ou em outros endereços também exclusivos.
- **Permitir:** Através desta marcação, tem-se que apenas os produtos informados na grade poderão ser armazenados no endereço em questão.

Quando o parâmetro **"Endereçar produtos em endereços com permissão vazia. - WMSENDERPERMVAZ"** estiver habilitado (comportamento padrão) durante a geração das tarefas de armazenagem na tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334), serão considerados todos os endereços que estiverem com este campo definido com a opção **"Permitir"**, porém que não possuam qualquer produto vinculado a este e quando utilizada a regra de armazenagem para endereços vazios. Caso o parâmetro citado esteja desativado, não serão considerados os endereços que não possuem tal vinculo.

\*\*Observação:\*\*a informação correspondente aos produtos inseridos na grade (proibir, exclusivo ou permitir), poderão ser visualizadas em cada produto, em seu respectivo cadastro na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms) ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)), seção **"Diversos"**, campo **"Vínculo Produto"**.

---

#### Grade - Aba Produto

Informe o código do **"Produto"** que será proibido, exclusivo ou permitido no endereço.

A marcação **"Ativo"** determinará se o produto permanecerá ou não nesta regra.

Determine no campo **"Estoque Mínimo"** qual o mínimo de produto que deverá permanecer neste endereço. É uma configuração utilizada apenas para endereços de Picking.

O campo **"Estoque Máximo"** deve ser alimentado com a capacidade máxima que será permitida para o armazenamento. Sempre que houver uma tarefa de armazenagem o sistema considerará o valor informado neste campo.

No campo **"Data Início"** informe a partir de qual data este endereço considerará a permissão, exclusividade ou proibição para este produto.

De forma inversa ao campo anterior, no campo **"Data Fim"** determine a partir da qual data este endereço não irá considerar a permissão, exclusividade ou proibição para este produto.

O campo **"Est. Mínimo Un. Padrão"** é apenas informativo; caso o estoque mínimo esteja configurado com uma unidade alternativa, esse campo apresentará o estoque mínimo na unidade padrão.

Equivalente à informação anterior, o campo **"Est. Máximo Un. Padrão"** é apenas informativo; caso o estoque máximo esteja configurado com uma unidade alternativa, esse campo irá apresentar o estoque máximo na unidade padrão.

No campo **"Unidade Padrão"** temos a unidade que será considerada para este endereço. Ao inserir um produto, o sistema preenche neste campo a Unidade padrão informada no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-). Também poderá ser informada uma Unidade alternativa.

**Nota:** ao configurar diversos produtos nesta aba, você deve deixar a aba [Unidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaunidade) sem preenchimento; você pode também adicionar na aba Unidade todas as Unidades dos produtos que foram inseridos na aba Produto.

**Observação:** ao tentar salvar uma alteração da Unidade de um Produto que possua saldo em estoque e esteja vinculado ao picking, o sistema emitirá a seguinte mensagem:

**"Não é permitido alterar a unidade do produto. O mesmo possui estoque em uma unidade distinta da solicitada".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Grupo de Produtos

Indique nesta aba, os [Grupos de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os) que poderão ser proibidos ou permitidos para este endereço.

![Imagem 5: Indique nesta aba, os Grupos de Produtos que poderão ser proibidos ou permitidos para este endereço.](https://ajuda.sankhya.com.br/hc/article_attachments/9811167504151)

Inicialmente no campo **"Grupos Relacionados"**, defina dois vínculos para os Grupos de Produtos. A saber:

- **Proibir:** Por esta definição, o(s) grupo(s) não poderá(ão) ser armazenado(s) neste endereço.
- **Permitir:** Definindo por esta opção, será obrigatório informar nesta aba, pelo menos um grupo de produto. Informando um ou mais grupos de produto o sistema permitirá que sejam armazenados neste endereço, produtos que pertençam ao grupo de produto informado.

**Observação:** quando marcada a opção Permitir apenas grupos selecionados, o sistema apresentará uma mensagem informando que você deve inserir algum produto ou grupo de produto. Não será necessário configurar produtos e grupos de produtos ao mesmo tempo, esta decisão deverá ser tomada antes da implantação.

---

#### Grade - Aba Grupo de Produtos

Informe o código do **"Grupo"** que será proibido ou permitido no endereço.

A marcação **"Ativo"** determinará se o Grupo de Produtos permanecerá ou não nesta regra.

No campo **"Data Início"** informe a partir de qual data este endereço considerará a permissão ou proibição para este Grupo de Produtos.

De forma reversa ao campo anterior, no campo **"Data Fim"** determine a partir da qual data este endereço não irá considerar a permissão ou proibição para este Grupo de Produtos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Movimentação Vertical

As informações correspondentes ao processo em que esta aba está envolvida, poderão ser visualizadas por meio do link [Movimentação Vertical - Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#movimentaovertical-processo).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Unidade

Adicione nesta aba, quais serão as unidades permitidas para este endereço. A regra consiste em que cada endereço armazene apenas uma unidade por vez, quando o endereço não for Multi produto (marcação presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral)). Para endereços Multi produto, esta aba deverá ficar vazia.

Se nenhuma unidade for configurada no endereço, o sistema aceitará qualquer unidade.

**Importante:** se não houver Unidade configurada para um endereço de Picking, o sistema irá considerar a Unidade Padrão do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Para os outros endereços o sistema permitirá a entrada de qualquer unidade.

Informe a **"Unidade"** permitida no endereço.

A marcação **"Ativo"** determina se o uso da Unidade em questão, é ou não permitido no endereço.

No campo **"Data Início"** informe a partir de qual data este endereço considerará a Unidade cadastrada.

De forma reversa ao campo anterior, no campo **"Data Fim"** indique a partir da qual data este endereço não irá considerar a Unidade.

\*\*Observação:\*\*a exceção do Picking, quando não for adicionada Unidade no endereço, o sistema aceitará qualquer unidade, mesmo sendo Unidade Fracionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Reabastecimento Picking

Esta aba é habilitada para uso, caso a marcação **"Reabastecido por Picking"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) esteja efetuada.

Nela informe o **"Cód. End. Cedente"**, ou seja, o endereço do picking que irá reabastecer o picking que está sendo configurado.

![Imagem 6: Nela informe o "Cód. End. Cedente" , ou seja, o endereço do picking que irá reabastecer o picking que está sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/9811384149655)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Aba Unitizador (UMA)

Esta aba será habilitada somente para endereços analíticos, aqui você deve configurar o uso do Unitizador (UMA) por endereço, de forma unitária.

![Imagem 7: Esta aba será habilitada somente para endereços analíticos, aqui você deve configurar o uso do Unitizador (UMA) por…](https://ajuda.sankhya.com.br/hc/article_attachments/9811834551447)

Ative a marcação \*\*"\*\***Utiliza UMA"** para permitir o uso de UMA no endereço. Lembrando que, caso tente desativar essa marcação enquanto houver registro de UMA no endereço ou saldo de estoque em pelo menos uma UMA, será emitida a mensagem abaixo:

**"O campo Utiliza U.M.A no cadastro de endereço não pode ser alterado pois existe estoque registrado. Para alterá-lo é necessário que não haja estoque no endereço."**

Informe no campo **"Qtd. máxima de UMAs permitidas no endereço"** quantas UMAs serão armazenadas simultaneamente no endereço, que por padrão, inicialmente deverá ser 1 (uma).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Botão Outras Opções...

O botão Outras Opções... é composto por apenas uma funcionalidade. A saber:

O acionamento da opção \*\*"\*\***Copiar Personalizações"**, abre um pop-up de nomenclatura **"Copiar Personalizações para Endereços Analíticos"**, ou seja, serão copiados dados de um endereço para outro.

Selecione a Origem e o Destino das Informações, preenchendo:

- Propriedades Gerais;
- Medidas;
- Grupo de Produtos;
- Produtos;
- Unidade;
- Local.

![Imagem 8: Local.](https://ajuda.sankhya.com.br/hc/article_attachments/9811690614423)

Informe no **"Destino das Informações"** os campos De e Até, pertinentes a quais endereços de destino serão copiadas as informações.

**Importante:** a opção **"Copiar Personalizações"** atualizará apenas os campos ligados diretamente ao endereço, ou seja, os campos contidos na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) e na aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abamedidas). Nas demais abas, somente ocorrerá a cópia quando os campos de destino não possuírem informações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Parâmetros que influenciam esta rotina

A validação feita através do parâmetro **"VALESTMAXMEDIDA - Validar estoque máximo versus peso e volume do endereço"**, tem o objetivo de evitar informações divergentes, ou seja, se o peso e volume dos produtos não estão excedendo o peso e volume máximo suportado pelo endereço de armazenagem.

O parâmetro de chave VALESTMAXMEDIDA, uma vez habilitado, fará com que o sistema valide o peso e o volume, ao cadastrar um Produto na tela de Endereço de Armazenamento.

**Nota:** esta validação somente é feita quando o endereço é de Picking (com o parâmetro ligado ou não).

Os parâmetros **"Validar M3 na Movimentação Pró-Ativa? - WMSVALM3MOVPRO"** e **"Validar peso na Movimentação Pró-Ativa? - WMSVALPESMOVPRO"** validam a transferência de produtos na Movimentação Pró-Ativa, caso ligados o sistema verifica o M3 (metro cúbico) e o Peso do produto em relação ao endereço de destino. O sistema realiza o seguinte cálculo: É multiplicado o M3 pela quantidade de produtos que estão sendo transferidos e verifica se é menor que o M3 máximo do endereço e subtrai o somatório dos produtos que estão no endereço; este cálculo também é realizado para o Peso Bruto.

O parâmetro **"Validar unidade na Movimentação Pró-Ativa? - WMSVALUNMOVPRO"** quando ativado, valida se o volume que está no destino é igual ao volume do produto, ou seja, caso o volume do produto seja UN (unidade) e no pulmão seja CX (caixa) o sistema não permitirá a transferência do produto.

Quando o parâmetro **"Inclui relação produto x endereço automaticamente? - WMSINCEXPAUTO"** for ativado, em movimentações pró-ativas do WMS, caso o produto que está sendo movimentado seja colocado em um endereço em que não possui vínculo, o sistema automaticamente cria o vínculo do produto no endereço. Caso o parâmetro esteja desativado, este procedimento só é feito se o produto for colocado no endereço de produto novo, definido através do parâmetro **"Endereço WMS para produtos novos - ENDPRODNOVOWMS"**. Ativando o parâmetro primeiramente citado, a funcionalidade se estende a qualquer endereço.

O parâmetro **"Regra de armazenagem para devoluções de venda - WMSREGRARMDEV"** possui três definições possíveis, que são:

- **Usa Regras de armazenagem:** O sistema usa as regras de armazenagem, conforme o comportamento atual.
- **Prefere Picking respeitando limite máximo:** O sistema respeita a o máximo do picking, contudo caso o máximo do picking seja atingido e ainda tiver produtos a ser armazenados o mesmo respeita a Configuração de Armazenagem.
- **Prefere Picking extrapolando limite máximo:** O sistema armazena todos os produtos no picking mesmo que a quantidade máxima do picking seja atingida.

**Nota:** o referido parâmetro não é soberano a [Configuração de Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234), caso o produto não tenha nenhuma regra vinculada ou a regra vinculada não tenha nenhuma opção ativa, o sistema não conseguirá gerar as tarefas. Não será analisada pelo sistema, a posição em que o Picking está, ou se o mesmo está ativo; sempre serão geradas tarefas para ele.

**Observação:** ainda que seja definida alguma das opções de Picking no parâmetro, o WMS evitará de levar para este os produtos com data de validade maior que a existente nos pulmões, aplicando desta forma, o controle por FIFO (First in/First out), ou seja, o primeiro produto a entrar no armazém deverá ser também o primeiro a sair, com a finalidade de evitar a perda por vencimento da mercadoria. Deste modo, caso existam pulmões com a data de validade menor do que a que está para ser armazenada, as tarefas não serão geradas para Picking.

O parâmetro **"Separação no picking sem vínculo do produto - SEPPICKSEMEXP"** quando habilitado, permite que sejam geradas as tarefas de separação para produto com estoque no picking onde o mesmo não possui vínculo, e também realiza a validação das capacidades do endereço selecionado como destino na armazenagem expressa.

Quando o parâmetro **"Respeita estoque máximo do picking - RESPESTMAXPICK"** estiver ativado, faz com que o sistema respeite o estoque máximo no reabastecimento, não deixando exceder o picking quando o mesmo não está dimensionado para o tamanho correto da caixa.

Através do parâmetro **"Reabastecer picking com unidade múltipla do produto - REABPICKUNIDMUL"** só será gerado a armazenagem/reabastecimento com a quantidade fechada da maior unidade de volume alternativo ou maior unidade de volume conferida para os casos de recebimento. Por exemplo, suponhamos que o endereço tenha espaço para armazenar 14 unidades (UN) de um determinado produto, porém este produto foi conferido na unidade caixa (CX) com a quantidade 2, o que corresponde a 24 unidades (UN) do produto (cada 12 unidades (UN) do produto equivale a 1 CX). Neste exemplo, com o parâmetro de chave REABPICKUNIDMUL ativado, será gerado apenas o recebimento com 12 unidades (1 CX) e a outra caixa será armazenada fechada no pulmão, já que esta não será aberta para ressuprir mais 2 unidades no picking. As rotinas que sofrem influência desta configuração, são:

**Tarefas de Recebimento**

Na compra ao gerar as tarefas de recebimento, estas serão geradas no picking apenas com unidades fechadas, desde que durante o processo de conferência no coletor tenha ocorrido a conferência com a unidade alternativa do produto. Caso a conferência tenha sido realizada na unidade padrão, não ocorrerá qualquer validação na geração do recebimento com relação a unidade fechada.

O WMS não possui, nativamente, uma regra ou parâmetro para garantir que a geração das tarefas de armazenagem respeite a ordem dos lotes lidos durante a conferência. A sequência das tarefas segue a lógica interna do sistema, sem opção de parametrização por lote.

**Ressuprimento Preventivo**

A regra aqui é a mesma do recebimento, atentando apenas para o fato que, as informações necessárias para saber qual a maior unidade a ser utilizada para o ressuprimento, virá das unidades alternativas do produto. Será buscado a maior unidade do produto e verificado se esta unidade atende a necessidade do picking.

Caso o estoque identificado no endereço do produto já esteja com a unidade fragmentada, por exemplo, já possui uma caixa "aberta" utilizamos essa quantidade para gerar o ressuprimento, para assim "limpar" o estoque.

**Reabastecimento agendado (JOB)**

Quando o parâmetro **"Utiliza reabastecimento no WMS? - LIGAREABESTWMS"** estiver ativado, durante o processo de separação após a efetivação da primeira fase de execução da tarefa e envio da mesma, é gerado o registro de um JOB na tabela TGWRAG que verifica se o endereço de picking está abaixo de sua capacidade máxima e assim gera um reabastecimento corretivo de forma automática; esse reabastecimento é gerado utilizando as mesmas regras do ressuprimento preventivo e de acordo com o parâmetro citado, também não permite que sejam geradas tarefas de ressuprimento com unidades que não estejam fechadas.

**Separação (Geração de ocorrência de avaria)**

Na separação existe uma opção para que seja gerada uma ocorrência para o produto, quando selecionado a opção de avaria e informado uma quantidade para o produto aonde a quantidade no picking se torne insuficiente para esta separação; tenta-se então gerar uma tarefa de reabastecimento corretivo para esta separação, seguindo as mesmas regras do ressuprimento preventivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)

## Movimentação Vertical - Processo

Trataremos nesta seção, os seguintes tópicos:

[Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#configura%C3%A7%C3%B5es)                                       [Execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#execu%C3%A7%C3%A3o)                                    [Considerações Finais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#considera%C3%A7%C3%B5esfinais)

---

#### Configurações:

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), selecione a marcação **"Utiliza Movimentação Vertical"**:

![Imagem 9: Nas Preferências da Empresa , aba WMS , selecione a marcação "Utiliza Movimentação Vertical" :](https://ajuda.sankhya.com.br/hc/article_attachments/360061944833)

Nos [Tipos de Equipamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612954), configure os \*\*"\*\***Níveis Máximo"** e \*\*"\*\***Mínimo"** da empilhadeira e da paleteira:

![Imagem 10: Nos Tipos de Equipamento , configure os **"** Níveis Máximo" e **"** Mínimo" da empilhadeira e da paleteira:](https://ajuda.sankhya.com.br/hc/article_attachments/360061028374)

No Cadastro de Endereços de Armazenamento, você deve criar os endereços de conexão, cadastrando um nível chamado por exemplo, de Conexão e dentro deste, criar as diversas Ruas. O cadastro que possuir a marcação **"Movimentação Vertical?"** presente nos [Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#preenchimentosiniciais) realizada, será o endereço de conexão, e por isso, as demais abas não serão habilitadas. Deve-se ter apenas 1 (um) endereço de conexão para cada prédio.

![Imagem 11: No Cadastro de Endereços de Armazenamento, você deve criar os endereços de conexão, cadastrando um nível chamado por…](https://ajuda.sankhya.com.br/hc/article_attachments/360061028394)

Em cada endereço de armazenagem que será vinculado ao endereço de conexão anteriormente configurado, você deve preencher a aba Movimentação Vertical informando no campo **"Endereço Preferencial"** o endereço de conexão ligado diretamente ao prédio. No campo **"Endereço Secundário"** informe o endereço pai do endereço de conexão; isso porque, se o endereço de conexão que está ligado diretamente com o prédio estiver ocupado, o sistema tentará colocar em qualquer endereço de conexão dentro do endereço pai.

Marque a opção **"Utiliza endereço de conexão para Entrada"** caso queira que apenas os movimentos de entrada utilizem movimentação vertical.

Você deve marcar a opção **"Utiliza endereço de conexão para Saída"** caso os movimentos de saída utilizem movimentação vertical.

Se a configuração for feita apenas para entrada, o reabastecimento de picking não irá gerar tarefas de movimentação vertical e horizontal.

Sugerimos que as etiquetas de conexão sejam impressas com uma etiqueta colorida, para destacar que é o endereço de conexão, evitando confusões na hora de ler o endereço propriamente dito.

**Nota:** endereços de picking de nível zero não devem ter a aba Movimentação Vertical configurada, pois não gastará um endereço de conexão.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#movimentaovertical-processo)

#### Execução:

Lance a nota de entrada e a envie para o WMS. Realize em seguida a conferência de entrada.

Na tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334), será apresentado apenas o endereço final que será armazenado, ou seja, os endereços de conexão não serão vistos nesta tela. Se for necessário, você pode verificar as tarefas que foram geradas para os endereços de conexão pela tela de [Gerência do WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453).

![Imagem 12: Na tela Tarefas de Recebimento , será apresentado apenas o endereço final que será armazenado, ou seja, os endereços de…](https://ajuda.sankhya.com.br/hc/article_attachments/360061944853)

No [Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112173), realize o login utilizando a paleteira e efetue as tarefas de pegar o produto na doca e colocar no endereço de conexão:

![clip7339](https://ajuda.sankhya.com.br/hc/article_attachments/360061028414) ![clip7341](https://ajuda.sankhya.com.br/hc/article_attachments/360061028434)

Em seguida, efetue o login utilizando a empilhadeira e realize as tarefas de pegar no endereço de conexão e colocar no endereço de armazenagem:

![clip7342](https://ajuda.sankhya.com.br/hc/article_attachments/360061028454) ![clip7343](https://ajuda.sankhya.com.br/hc/article_attachments/360061028474)

**Observação:** durante a conferência de entrada, sempre serão registradas todas as datas de validade informadas pelo conferente, ou seja, o sistema sempre registrará todas as datas inseridas desde o início do processo de conferência de entrada.

**Importante:**

- Caso o parâmetro **"Utiliza multiprodutos nos endereços de conexão? - UTIMULPROENDCON"** seja ativado, será permitido que um endereço de conexão suporte mais de um produto, ou seja, ao realizar um armazenamento e/ou ressuprimento (recebimento e expedição, respectivamente), serão utilizados todos os endereços da rua e logo em seguida, estes endereços serão preenchidos com outros produtos (produtos distintos), se existir mais de um endereço cadastrado; caso contrário, será utilizado apenas o endereço disponível. Em outras palavras, com todos os endereços ocupados, o próximo processo de armazenagem/ressuprimento irá selecionar um endereço que contenha a menor quantidade distinta de produtos para realização do procedimento. Nos processos seguintes, serão pegos outros endereços utilizando a mesma regra ocupando todos os endereços com dois, três, quatro produtos e assim sucessivamente.
- Nas tarefas cujo endereço de origem seja uma conexão e o destino seja um picking, caso o parâmetro **"Realiza conferência cega nas tarefas do WMS? - CONFCEGTARARM"** esteja ativado, será exigida a digitação da quantidade do produto que está sendo armazenado. Com este parâmetro ativado, internamente o sistema irá confrontar a quantidade da tarefa com a quantidade digitada, e em caso de divergência, exibe uma mensagem no coletor sobre tal fato. Este comportamento irá ocorrer em tarefas do tipo Ressuprimento Preventivo e Ressuprimento Corretivo e tem por objetivo evitar o armazenamento nos endereços de picking de quantidades incorretas de produtos, gerando maior seguridade no controle de estoque.
- No parâmetro **"Limite de recontagem na conf. do reabastecimento - LIMRECCONFCEG"** configure a quantidade de contagens que poderão ser efetuadas na conferência cega no abastecimento de picking. Caso a quantidade seja ultrapassada, será gerada a movimentação para dos produtos correspondentes ao endereço picking efetuando os demais acertos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#movimentaovertical-processo)

#### Considerações Finais:

No equipamento é possível configurar o nível mínimo e máximo que o mesmo pode trabalhar; o sistema verifica o nível do equipamento com relação ao nível do endereço contido na tarefa, conforme descrito abaixo:

- Se o destino possui conexão e a origem também possui, o sistema valida se os níveis da origem e do destino estão entre o mínimo e máximo do equipamento utilizado;
- Se apenas o destino possuir conexão, o sistema valida se o nível da origem está entre o mínimo e máximo do equipamento;
- Se apenas a origem possuir conexão, o sistema valida se o nível do destino está entre o mínimo e máximo do equipamento;
- Caso não haja conexão envolvida na movimentação e a origem for um picking com nível maior que zero, o nível do destino deve estar entre o mínimo e máximo do equipamento;
- Caso não exista conexão envolvida na movimentação, e a origem possuir um nível maior que zero, mas não for um picking, os níveis da origem e do destino devem ser menores ou iguais ao nível do equipamento;
- Em qualquer outro caso, os níveis da origem e do destino devem estar entre o mínimo e máximo do equipamento;
- Quando o endereço destino da tarefa de armazenagem está marcado como **"Utiliza endereço de conexão para Entrada ou Saída"**, é obrigatório informar tanto o Endereço Preferencial quanto o Endereço Secundário. Caso um deles não esteja informado, o sistema exibe uma mensagem alertando tal fato e o endereço deve ser configurado antes de gerar as tarefas de armazenagem;
- Quando o endereço utiliza movimentação na entrada ou saída e o endereço preferencial está inativo, o sistema tentará verificar em todos os filhos do endereço secundário por algum endereço disponível. Caso não encontre, o algoritmo de armazenamento tentará achar outro endereço e o endereço atual será descartado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#movimentaovertical-processo) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#top)
