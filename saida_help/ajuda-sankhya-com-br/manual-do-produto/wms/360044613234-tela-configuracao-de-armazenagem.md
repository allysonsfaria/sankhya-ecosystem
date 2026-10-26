---
id: "360044613234"
titulo: "Tela Configuração de Armazenagem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:28Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "WMS", "Estoque", "WMSINCEXPAUTO", "Armazenagem Seletiva", "Configuração de Armazenagem", "Indefinido", "WMSDIGLOTARMEXP", "br.com.sankhya.configuracao.armazenagem", "Configuração de Armazenagem manual", "Configuração de estratégias de armazenagem", "Geração de tarefas para endereço indefinido", "Mensagens personalizadas no coletor de dados", "Squad WMS", "Armazenagem"]
---

# Tela Configuração de Armazenagem

**Módulo:** WMS › Rotinas
**Caminho de acesso:**  WMS › Rotinas › Configuração de Armazenagem

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#oque) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#antes) [Regras de armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#regras)    ↳ [Consolidação de paletes no mesmo endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#consolidacao)    ↳ [Endereços Vazios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#enderecosvazios)    ↳ [Completar Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#completarenderecos)    ↳ [Picking](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#picking) | [Armazenagem Seletiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#seletiva) [Geração de Tarefas para Endereço Indefinido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#indefinido) [Mensagens personalizadas no coletor de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#mensagens) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#pontosdeatencao) |
| --- | --- |

## O que é e para que serve

A **Tela Configuração de Armazenagem** permite configurar as regras (algoritmos) usadas na geração automática das tarefas de armazenagem do WMS. Você cadastra quantas regras forem necessárias e pode vincular cada uma a um produto ou a um grupo de produtos. Ela não executa a armazenagem em si — apenas define a estratégia que o motor de geração de tarefas vai seguir quando as tarefas forem geradas em outras rotinas (recebimento, armazenagem expressa, reprocessamento).

Quando o **Produto** ou o **Grupo do Produto** não tiver regra configurada, o sistema usa a regra marcada como **Padrão**. O sistema também respeita a ordem em que as regras estão configuradas: segue tentando a próxima regra da lista até que todo o estoque da doca tenha sido armazenado.

![Tela Configuração de Armazenagem, lista de Regras de armazenagem à esquerda e detalhe da regra selecionada à direita](https://ajuda.sankhya.com.br/hc/article_attachments/360099670954)

## Antes de começar

Para que uma regra tenha efeito prático na geração das tarefas, os produtos envolvidos precisam ter os seguintes cadastros preenchidos antes de configurar a regra:

- **Lastro × camadas** — sem esse cadastro no produto, os comportamentos que dependem de "palete completo" (descritos em [Endereços Vazios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#enderecosvazios) e [Completar Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#completarenderecos)) não são aplicados, mesmo com a regra corretamente configurada.
- **Peso** e/ou **cubagem** do produto — sem esses dados, o mecanismo de consolidação de paletes no mesmo endereço não é aplicado.

**⚠️ Atenção**

Se algum desses cadastros estiver ausente no produto, o sistema não exibe aviso — ele volta silenciosamente ao comportamento anterior (um palete por endereço). Veja mais em [Consolidação de paletes no mesmo endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#consolidacao).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

## Regras de armazenagem

As regras de armazenagem são complementares: seguindo a ordem em que estão configuradas, o sistema gera o máximo de tarefas possível em uma regra e, se ainda sobrar estoque do produto na doca, passa para a próxima, até que todo o estoque tenha sido armazenado. Ao selecionar uma regra na lista **Regras de armazenagem**, o detalhe correspondente é exibido à direita, com os campos daquele algoritmo específico.

As regras disponíveis são: [Endereços vazios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#enderecosvazios), [Completar Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#completarenderecos) e [Picking](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#picking).

### Consolidação de paletes no mesmo endereço

A consolidação de paletes no mesmo endereço se aplica exclusivamente às regras **Completar Endereços** e **Endereços Vazios**. Para que o comportamento seja aplicado, a regra correspondente precisa estar configurada com a marcação **Usar lastro x camada** habilitada e com a marcação **Múltiplas tarefas no mesmo endereço** habilitada. Caso essa configuração não esteja habilitada, o sistema não realiza a consolidação e mantém o comportamento anterior, tratando cada palete isoladamente.

Quando ativa, ao gerar as tarefas de armazenagem o sistema avalia a ocupação do endereço de forma consolidada, em vez de avaliar cada palete isoladamente. Com isso, múltiplos paletes compatíveis podem ser direcionados para o mesmo endereço dentro de um único processamento, sempre que houver capacidade disponível. Essa lógica não altera o cadastro do endereço.

Para decidir se um palete pode ser direcionado a um endereço que já recebeu outros paletes no mesmo processamento, o sistema aplica o seguinte cálculo:

`Capacidade disponível = Capacidade total − Estoque físico − Tarefas futuras válidas − Ocupação simulada atual`

| Componente | O que representa |
| --- | --- |
| Capacidade total | Limite configurado para o endereço. |
| Estoque físico | Paletes já confirmados no endereço. |
| Tarefas futuras válidas | Tarefas de armazenagem pendentes ou em andamento para aquele endereço. |
| Ocupação simulada atual | Paletes já direcionados para o mesmo endereço dentro do processamento atual, mas ainda não gravados ou concluídos. Esse controle é reiniciado a cada endereço avaliado — ele não acompanha a ocupação de outros endereços do mesmo lote. A cada palete direcionado a um endereço, essa ocupação simulada é atualizada antes de avaliar o próximo palete para aquele mesmo endereço. |

**ℹ️ Nota**

Tarefas canceladas, finalizadas ou estornadas não são contabilizadas nesse cálculo — elas não consomem capacidade lógica futura do endereço.

Essa consolidação ocorre nos seguintes fluxos:

- **Geração automática pós-recebimento** — após a conferência de recebimento, as tarefas de armazenagem são geradas considerando a ocupação física e lógica futura dos endereços.
- **Geração manual** — ao gerar tarefas manualmente, as mesmas regras de capacidade e compatibilidade são aplicadas.
- **Reprocessamento** — paletes sem tarefa podem ser reprocessados, recalculando a ocupação atualizada dos endereços.
- **Consolidação de armazenagem** — paletes compatíveis são agrupados no mesmo endereço sempre que houver capacidade disponível.
- **Concorrência** — em processamentos simultâneos, o sistema impede que dois processos ultrapassem juntos a capacidade do mesmo endereço.

Pontos de atenção sobre a consolidação:

- Se o endereço já estiver parcialmente ocupado por estoque físico ou por tarefas futuras, apenas a capacidade restante é utilizada para os novos paletes.
- Um palete incompatível com o endereço, conforme as regras de armazenagem vigentes, continua sendo direcionado para outro endereço elegível — a consolidação só ocorre entre paletes compatíveis.
- A consolidação acontece durante a geração da tarefa; depois que uma tarefa é concluída, ela não é reaberta para receber novos paletes.

**⚠️ Atenção**

Essa regra não altera o cadastro do Endereço de Armazenamento. Ela não cria novo tipo de endereço, nova regra de armazenagem ou nova regra de compatibilidade, e não muda a capacidade física já cadastrada para o endereço — apenas o cálculo de ocupação feito pelo motor de geração de tarefas.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

### Endereços Vazios

Mesmo sendo um endereço multi-produto, o sistema pode armazenar produtos em **Endereços Vazios** até o limite físico do endereço, potencializando o processo de armazenagem. Endereços que estavam vazios no início da geração de tarefas recebem mais produtos, respeitando as regras de limite configuradas para eles.

#### Proibir Un. menor que a padrão

**O que faz**

Bloqueia a geração de tarefas de armazenagem com Unidades Alternativas menores que a Unidade Padrão do produto.

**Quando usar**

Use quando não quiser que o sistema direcione o produto para o endereço em unidades menores que a padrão. Esta marcação vem **desmarcada** por padrão.

**Como funciona**

Marcada: o sistema não aceita, durante a geração de tarefas, unidades alternativas menores que a padrão — dá preferência às maiores unidades alternativas ou, se só houver uma alternativa e ela for menor que a padrão, usa a própria unidade padrão. Desmarcada: o sistema pode usar qualquer unidade alternativa disponível, inclusive as menores que a padrão.

![Campo Proibir Un. menor que a padrão na regra Endereços Vazios](https://ajuda.sankhya.com.br/hc/article_attachments/360085119294)

#### Unidade de armazenamento

**O que faz**

Define qual unidade será usada para armazenar o produto no endereço vazio.

**Quando usar**

Use para controlar se o sistema deve priorizar a maior unidade alternativa livre, a menor, a que melhor aproveita o espaço do endereço, ou sempre a unidade padrão.

**Como funciona**

- **Maior Un. Alternativa disponível** — armazena de acordo com a maior unidade alternativa livre.
- **Menor Un. Alternativa disponível** — armazena pela menor Unidade Alternativa acessível.
- **Com melhor aproveitamento do endereço** — o sistema analisa e armazena o produto de acordo com a melhor utilização do endereço.
- **Unidade Padrão** — armazena sempre na Unidade Padrão, sem converter as tarefas para Unidade Alternativa. Você pode receber o produto em uma Unidade Alternativa e armazená-lo na Unidade Padrão.

#### Desconsiderar endereço multi-produto / Permitir múltiplos produtos por endereços

**O que faz**

Controla se a armazenagem pode direcionar mais de um produto para o mesmo endereço.

**Como funciona**

Quando **Desconsiderar endereço multi-produto** está marcada, a marcação **Permitir múltiplos produtos por endereços** fica bloqueada, e a armazenagem é gerada com cada produto em um endereço separado. Quando **Desconsiderar endereço multi-produto** está desmarcada e **Permitir múltiplos produtos por endereços** está selecionada, a armazenagem é feita para endereços multi-produto, mantendo o primeiro endereço vazio encontrado, se ele tiver espaço.

**ℹ️ Nota**

Se **Permitir múltiplos produtos por endereços** não for selecionada, o comportamento é o mesmo do primeiro caso (cada produto em um endereço separado).

#### Prioriza pulmões vinculados ao produto

**O que faz**

Prioriza, na geração das tarefas de armazenagem, os endereços vinculados ao produto.

**Como funciona**

Com a marcação habilitada, ao gerar as [tarefas de armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento#bot%C3%A3ogerartarefas), o sistema prioriza os endereços vinculados ao produto. Se não houver vínculo, seleciona um endereço indefinido.

**💡 Dica**

Para usar somente endereços específicos, selecione **Exclusivo** no campo **Produtos Relacionados** da aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto) do [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

### Completar Endereços

O sistema tenta armazenar o produto em endereços que já possuem o mesmo produto e o mesmo controle. Exemplo: ao gerar uma tarefa de armazenagem para o produto A, o sistema localiza o endereço 1051, que já tem 5 unidades desse produto. Se o endereço não estiver na ocupação máxima, ele é usado para armazenar uma quantidade do produto A que complete o endereço até a ocupação máxima, ou até completar a norma de paletização configurada para a unidade armazenada, quando houver.

![Exemplo de armazenagem no endereço 1051 completando com o produto A](https://ajuda.sankhya.com.br/hc/article_attachments/360086297853)

**⚠️ Atenção**

Quando a quantidade restante a armazenar for menor que um palete completo (a quantidade de **lastro × camada** configurada para o produto), essa quantidade residual **não é armazenada** nesse endereço — a capacidade que sobrar fica sem uso nessa execução. Exemplo: restam 50 unidades para armazenar, o palete completo do produto equivale a 20 unidades e o endereço tem folga para 80; o sistema gera 2 tarefas de 20 unidades (40 no total) e as 10 unidades restantes não são direcionadas para esse endereço. Esse comportamento é diferente do que ocorre em [Endereços Vazios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#enderecosvazios), onde a quantidade residual pode ser aproveitada no mesmo endereço.

#### Preferir Endereços

**O que faz**

Determina a ordem em que o sistema apresenta os endereços disponíveis para armazenagem.

**Como funciona**

- **Maior proximidade ao picking** — usa a ordem de picking para apresentar os endereços; os mais próximos aos pickings dos produtos são preferidos.
- **Com maior disponibilidade** — ordena pela capacidade do endereço, considerando peso máximo, cubagem e a quantidade do produto já armazenada nele.

#### Usar lastro x camada

**O que faz**

Determina se a armazenagem respeitará as regras de lastro × camada configuradas para o produto.

**Como funciona**

Junto com a marcação **Múltiplas tarefas no mesmo endereço**, habilita a consolidação de paletes no mesmo endereço descrita em [Consolidação de paletes no mesmo endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#consolidacao). Sem o cadastro de lastro × camada no produto, essa marcação não tem efeito.

#### Desconsiderar endereço multi-produto / Tipo de ocupação

**O que faz**

Controla se um endereço multi-produto pode ser completado com um produto diferente do que já está armazenado nele.

**Como funciona**

Quando **Desconsiderar endereço multi-produto** está selecionada, ao gerar as tarefas de recebimento o sistema verifica se o endereço é multi-produto; se for, não gera as tarefas para ele. Quando não está selecionada, o campo **Tipo de ocupação** define o comportamento:

- **Endereços ocupados com o mesmo produto (padrão)** — completa apenas os endereços onde já existe estoque do mesmo produto.
- **Endereços ocupados com qualquer produto** — completa endereços que possuem estoque de qualquer produto, desde que multi-produto.

**ℹ️ Nota**

A opção **Endereços ocupados com qualquer produto** só é usada quando a regra não estiver com **Desconsiderar endereço multi-produto** marcada — essa marcação, quando ativa, anula a opção. Quando o endereço é completado com um produto diferente e ainda não possui estoque do produto do recebimento, o sistema busca a maior unidade alternativa configurada para o produto e gera o armazenamento com essa unidade. Se, durante a geração, for encontrado um endereço que já tem estoque do próprio produto do recebimento entre os endereços de outros produtos, esse endereço é priorizado para ser completado.

#### Prioriza pulmões vinculados ao produto

Com a marcação habilitada, ao gerar as [tarefas de armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento#bot%C3%A3ogerartarefas), o sistema prioriza os endereços vinculados ao produto. Se não houver vínculo, seleciona um endereço indefinido. (Mesmo comportamento descrito em [Endereços Vazios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#enderecosvazios).)

**💡 Dica**

Para usar somente endereços específicos, selecione **Exclusivo** no campo **Produtos Relacionados** da aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto) do [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

### Picking

O sistema tenta armazenar os produtos em endereços de Picking.

- **Ordenação** — o sistema apresenta os endereços ordenados com base na quantidade de estoque que eles podem receber.

#### Perc. máximo de ocupação atual

**O que faz**

Determina o percentual de ocupação atual do Picking para que ele se torne elegível para receber mais estoque.

**Como funciona**

O Picking só recebe estoque adicional se dispuser de um espaço mínimo, evitando o envio de quantidades pequenas, até atingir o estoque máximo configurado para ele. Exemplo: um endereço tem 200 unidades em estoque e o estoque máximo configurado para o produto é 400 — ou seja, o endereço está 50% ocupado. Se o percentual máximo estiver configurado em 40%, esse endereço não é utilizado; se estiver configurado em 60%, o endereço é utilizado com uma tarefa de 200 unidades, atingindo o estoque máximo de 400.

![Exemplo de cálculo do percentual máximo de ocupação atual no Picking](https://ajuda.sankhya.com.br/hc/article_attachments/360086285733)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

## Armazenagem Seletiva

A **Armazenagem Seletiva** permite escolher qual tarefa será armazenada primeiro, de acordo com a Doca e com o Produto bipado, para que sejam levados do local de origem para seus respectivos endereços.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

## Geração de Tarefas para Endereço Indefinido

O WMS conta com um recurso para auxiliar o processo de armazenagem: quando nenhuma regra de armazenagem consegue gerar as tarefas, o sistema gera tarefas para um endereço curinga e, ao executar a tarefa, é possível trocar o endereço destino. A troca de endereço destino também se aplica a tarefas em que o sistema já conseguiu gerar o endereço final.

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), preencha o campo **Cód. End. Armazenamento Indefinido** com um endereço de armazenamento indefinido, usado quando nenhuma regra de armazenagem for satisfeita. Com isso, é gerada a tarefa com a quantidade restante a ser armazenada, para o endereço definido nesse campo.

Durante a armazenagem expressa, na fase de entrega de um produto cuja tarefa está com destino ao armazenamento indefinido, é solicitada a definição do endereço de destino:

![Tela de armazenamento expresso solicitando definição do endereço de destino](https://ajuda.sankhya.com.br/hc/article_attachments/8900369444631)

**ℹ️ Nota**

O parâmetro `MOSTRAQTDARMEXP` ("Mostrar quantidade no armazenamento expresso"), quando ligado, preenche o campo **Quantidade** na tela de Armazenamento Expresso com a quantidade do produto a armazenar; desligado, o campo fica zerado. Também exibe os campos **Total disp. nas tarefas**, **Qtd. Origem**, **Qtd. Destino** e **Proporção de volume origem destino**.

O botão **Endereço** é usado para definir o endereço de armazenagem. Ao acioná-lo, a tela de definição de endereço é aberta, permitindo também definir a quantidade a ser entregue do produto. Por exemplo, se a tarefa solicitava 10 unidades e, ao definir o endereço, você informar 4 unidades, ao salvar o sistema divide a tarefa em uma de 4 unidades (selecionada imediatamente para entrega) e uma de 6 unidades, que volta para a fila de tarefas a entregar com o endereço ainda a definir.

![Tela de definição de endereço acessada pelo botão Endereço](https://ajuda.sankhya.com.br/hc/article_attachments/8900430819735)

Essa definição de endereço também pode ser usada para trocar o endereço de entrega de uma tarefa cujo destino final foi gerado pela regra de algoritmo. Nesse caso, o botão **Endereço** só fica habilitado quando o parâmetro `WMSDEFENDARMEXP` ("Permite definir endereço armazenamento expresso?") estiver ativado — por padrão, ele vem desativado.

**ℹ️ Nota**

O parâmetro `WMSDEFENDARMEXP` não tem influência quando a tarefa foi gerada para o endereço curinga — nesse caso, o endereço destino sempre precisa ser alterado.

O botão **Pegar Tudo** aparece quando o produto informado é controlado por lote e há mais de um lote, e quando, nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), a marcação **Armazenar o total coletado no recebimento expresso** estiver habilitada. Ao acionar **Pegar Tudo**, o sistema coleta todos os lotes do produto informado inicialmente.

![Botão Pegar Tudo na tela de armazenamento expresso](https://ajuda.sankhya.com.br/hc/article_attachments/8900795149975)

O botão **Cons.Produto** consulta as informações do produto que está sendo entregue, mostrando seus dados e os endereços em que ele possui estoque, para facilitar a escolha do endereço.

![Consulta de produto pelo botão Cons.Produto](https://ajuda.sankhya.com.br/hc/article_attachments/8900770567447)

Durante uma entrega para um endereço de Picking definido por você, caso o produto não tenha vínculo com esse endereço, o sistema pode criar o vínculo automaticamente, com as mesmas regras da movimentação proativa — desde que o parâmetro `WMSINCEXPAUTO` ("Inclui relação produto x endereço automaticamente?") esteja ativado.

Na Armazenagem Expressa, o coletor de dados não guarda os dados localmente — o processamento fica a cargo do servidor. Há paginação de dados nas telas **Produtos Coletados** e **Produtos Disponíveis do Armazenamento Expresso**. Na tela de informação do lote, use uma marcação para selecioná-lo; quando há muitos lotes, o parâmetro `WMSDIGLOTARMEXP` ("Informar lote manualmente no armazenam. expresso?"), quando ativado, substitui a seleção por marcação por um campo de digitação.

**ℹ️ Nota**

O parâmetro `PROIBEDIGCOLWMS` ("Proibir digitação no coletor do WMS?") influencia as seguintes tarefas: Armazenamento Expresso, Armazenagem Seletiva e Movimentação Pro-ativa.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

## Mensagens personalizadas no coletor de Dados

**ℹ️ Nota**

Esta é uma rotina idealizada para ser configurada por um profissional que domine a linguagem de programação PL/SQL.

No Sankhya Om, você pode configurar mensagens para serem exibidas no coletor de dados do WMS — tanto quando a tarefa é mostrada no coletor quanto ao informar o endereço — para que informações relevantes ao processo apareçam no momento da execução da tarefa.

Para exibir uma mensagem quando a tarefa aparece na tela do coletor, crie uma trigger personalizada inserindo uma mensagem de até 99 caracteres no campo `AD_MSGCOLETOR` da tabela `TGWTEC` do [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294), conforme a regra de negócio — esse comportamento também pode ser configurado em um evento Java. Exemplo de trigger:

```
create or replace TRIGGER TRG_INC_UPD_TGWTEC BEFORE INSERT OR
        UPDATE ON TGWTEC FOR EACH ROW
            BEGIN
                :NEW.AD_MSGCOLETOR := 'Necessário um envelope plástico (Venda
                do tipo E Commerce), colete-o antes de executar a separação';
            END;
```

![Mensagem exibida no coletor após configuração da trigger](https://ajuda.sankhya.com.br/hc/article_attachments/4408236840343)

Outros exemplos de mensagens configuráveis:

- Processo de separação: "Para esta separação é necessário um envelope plástico (Venda do tipo E Commerce), colete-o antes de executar a separação."
- Processo de separação por esteira: "Esta é uma separação especial. Disponibilize caixa personalizada junto às mercadorias separadas."
- Processo de armazenagem: "Verifique se o palete físico não possui datas diferentes. Recebimento com mais de uma data para este produto."

Essas mensagens também podem ser exibidas quando o endereço da tarefa é lido: insira o caractere `#` antes da mensagem no campo `AD_MSGCOLETOR` da tabela `TGWTEC`. Exemplo:

```
create or replace TRIGGER TRG_INC_UPD_TGWTEC BEFORE INSERT OR
UPDATE ON TGWTEC FOR EACH ROW
    BEGIN
    :NEW.AD_MSGCOLETOR := '#Produto com alto índice de avarias, cuidado ao movimentá-lo.';
END;
```

![Mensagem exibida na leitura do endereço da tarefa](https://ajuda.sankhya.com.br/hc/article_attachments/4408237289751)

Outro exemplo de uso, no processo de reabastecimento: "Atenção! Produto com mais de uma data no endereço, colete a de menor disponibilidade."

Esse serviço de mensagens pode ser aplicado nos seguintes processos:

- Tarefas de Armazenagem
- Transferência
- Reabastecimento
- Tarefas de Separação (Convencional, balcão, por área e por esteira)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Tela-Configura%C3%A7%C3%A3o-de-Armazenagem#sumario)

---

## Pontos de atenção

- **Completar Endereços** e **Endereços Vazios** tratam o resíduo (quantidade menor que um palete completo) de forma diferente: em Endereços Vazios o resíduo pode ser aproveitado no mesmo endereço; em Completar Endereços, não — a capacidade restante fica ociosa nessa execução. Os dois nomes sugerem "completar ao máximo", mas o comportamento real de Completar Endereços é mais conservador do que o nome indica.
- A consolidação de paletes no mesmo endereço depende de três condições simultâneas: cadastro de peso e/ou cubagem no produto, cadastro de lastro × camada no produto, e as marcações de regra habilitadas. A ausência de qualquer uma delas desativa a consolidação silenciosamente, sem aviso na interface.
