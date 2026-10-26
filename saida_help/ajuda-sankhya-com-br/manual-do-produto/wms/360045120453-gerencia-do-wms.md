---
id: "360045120453"
titulo: "Gerência do WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:16:14Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "WMS", "Parceiro", "Estoque", "Gerência do WMS", "br.com.sankhya.wms.gerenciadowms", "Gerência do WMS manual", "Tipos Empresa Produto", "Tarefas Itens", "Aplicar Configurar Exportar"]
---

# Gerência do WMS

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311621715863) Módulo: WMS > Gerência
```

---

Através da tela Gerência de WMS, você pode realizar o acompanhamento de todos os processos executados no WMS que se encontram pendentes ou em execução, permitindo a alocação de recursos, bem como sua priorização. Todos os procedimentos concretizados no WMS poderão ser visualizados e monitorados por meio desta tela.

Abaixo temos suas características:

[Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#filtros)                                   [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#gradeprincipal)                                   [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#botesdotopodatela)

## Filtros

O lado esquerdo da tela, conta com alguns campos destinados à filtragem dos processos trabalhados no WMS.

![Imagem 2: O lado esquerdo da tela, conta com alguns campos destinados à filtragem dos processos trabalhados no WMS .](https://ajuda.sankhya.com.br/hc/article_attachments/360102435094)

Para apresentação das informações na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#gradeprincipal), algumas definições se fazem obrigatórias. São elas:

Especifique no campo **"Tipos de Tarefa"**, qual tarefa em particular você deseja visualizar na grade, dentre as seguintes opções:

- Todas;
- Recebimento;
- Recebimento Cancelado;
- Expedição;
- Expedição Balcão;
- Expedição Cancelada;
- Reabastecimento;
- Reabastecimento Corretivo;
- Reabastecimento (Todos);
- Transferência;
- Inventário;
- Recontagem;
- Todas.

**Nota:** para o Tipo de Tarefa Expedição Cancelada, temos a coluna **"Situação Cancelamento da Sep"** onde será apresentada a situação em que a separação parou antes de ser cancelada. Caso o pedido seja separado normalmente e não tenha cancelamento, essa coluna terá a situação **"Não cancelado"**.

Determine a **"Empresa"** que você deseja acompanhar os processos do WMS.

O campo **"Produto"** do filtro, apresentará todas as tarefas que contém o produto informado, não limitando apenas ao item especificado.

**Observação:** ao escolher um Produto no filtro, a grade retornará o produto filtrado e os demais envolvidos na tarefa do produto em questão, ou seja, serão apresentadas as informações da tarefa que possua o produto informado, sem a necessidade de ocultar os dados dos demais produtos.

**Nota:** você poderá utilizar o filtro de Produto juntamente com os demais filtros e também, poderá consultar apenas as tarefas já concluídas e com dependências desse produto, através das marcações **"Apresentar Tarefas Concluídas"** e **"Apenas Tarefas com Dependências"**, respectivamente.

No **"Cód. Parceiro"** você poderá inserir um Parceiro, sendo que este será o destinatário que poderá ou não utilizar [Controle de Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros).

É essencial que seja informado o intervalo de tempo em que as tarefas foram iniciadas, no caso de tarefas já concluídas, o **"Período"** em que foram executadas.

Os demais campos são de preenchimento opcional; caso você queira refinar ainda mais a busca:

- Cód. Parceiro;
- Transportadora;
- Nro. Único;
- Nota/Pedido;
- Ordem de Carga.

A marcação **"Apresentar Tarefas Concluídas"** quando realizada, fará com que na Grade Principal sejam apresentadas apenas as tarefas que já foram consumadas.

Ao selecionar a marcação **"Apenas Tarefas com Dependências"**, serão exibidas na grade as tarefas que dependem de outras para serem executadas. Por exemplo, para atendimento à um pedido, pode ser que o Picking não possua o total da quantidade de itens solicitada, sendo necessário um Reabastecimento para concretização da tarefa, ou seja, a tarefa dependente de reabastecimento será apresentada na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#top)

## Grade Principal

Uma vez determinados os filtros desejados, clicando em **"Aplicar"**, serão apresentados na grade os dados correspondentes ao Tipo de Tarefa definido. Optando por visualizar Todos os Tipos de Tarefa, será exibida apenas uma grade contendo todas as tarefas:

![Imagem 3: Uma vez determinados os filtros desejados, clicando em "Aplicar" , serão apresentados na grade os dados correspondentes…](https://ajuda.sankhya.com.br/hc/article_attachments/360102434474)

Através de um duplo clique na tarefa desejada, ou mesmo especificando o Tipo de Tarefa nos Filtros, a grade será dividida em dois, onde na segunda grade, teremos os Itens da Tarefa em questão:

![Imagem 4: Através de um duplo clique na tarefa desejada, ou mesmo especificando o Tipo de Tarefa nos Filtros , a grade será…](https://ajuda.sankhya.com.br/hc/article_attachments/360102434594)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#top)

## Botões do topo da tela

O topo da tela conta com alguns botões que visam auxiliar e dinamizar o uso da Gerência do WMS. São eles:

![Imagem 5: Filtros: além das opções apresentadas no tópico Filtros , por meio deste botão, você pode construir filtros…](https://ajuda.sankhya.com.br/hc/article_attachments/16921391206295) **Filtros:** além das opções apresentadas no tópico [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#filtros), por meio deste botão, você pode construir filtros personalizados de modo a detalhar ainda mais a busca pelo processo desejado.

![Imagem 6: Aplicar: este botão sintetiza os filtros fixos e/ou personalizados que foram criados, e exibe na Grade Principal o seu…](https://ajuda.sankhya.com.br/hc/article_attachments/16921361525527) **Aplicar:** este botão sintetiza os filtros fixos e/ou personalizados que foram criados, e exibe na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#gradeprincipal) o seu resultado.

![Imagem 7: Configurar grade: o acionamento deste botão apresenta na tela o pop-up Configuração da grade , onde você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/16921391213079) **Configurar grade:** o acionamento deste botão apresenta na tela o pop-up Configuração da grade, onde você pode selecionar as colunas que serão exibidas na tela, bem como determinar a ordenação destas colunas.

![Imagem 8: Exportar grade: este botão está presente na Grade Principal e na grade inferior (quando apresentada); ele permite a…](https://ajuda.sankhya.com.br/hc/article_attachments/16921441354135) **Exportar grade:** este botão está presente na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#gradeprincipal) e na grade inferior (quando apresentada); ele permite a exportação dos dados presentes nas grades para PDF, para Planilha (Excel) ou para Cubo.

![Imagem 9: Atualização Automática: através deste botão, você determina o Tempo de atualização da tela (em segundos), ou seja, com…](https://ajuda.sankhya.com.br/hc/article_attachments/16921435713687) **Atualização Automática:** através deste botão, você determina o Tempo de atualização da tela (em segundos), ou seja, com base nos filtros definidos, é possível estabelecer um período para que a tela seja automaticamente carregada.

![Imagem 10: Cancelar: trabalhando com tarefas do tipo Transferência , por meio deste botão, você realiza seu cancelamento. Para que…](https://ajuda.sankhya.com.br/hc/article_attachments/16921454031255) **Cancelar:** trabalhando com tarefas do tipo Transferência, por meio deste botão, você realiza seu cancelamento. Para que uma tarefa de Transferência possa ser cancelada, é necessário que ela esteja na situação **"Aberta"** e se encontre **"Sem tarefas pendentes"**. Como este é um botão trabalhado nas tarefas do tipo Transferência, o botão Cancelar é apresentado apenas quando esta tarefa for filtrada.

![Imagem 11: Executantes: por meio deste botão, caso a tarefa não tenha sido concluída, é possível Alterar , Adicionar ou Remover…](https://ajuda.sankhya.com.br/hc/article_attachments/16921521034519) **Executantes:** por meio deste botão, caso a tarefa não tenha sido concluída, é possível Alterar, Adicionar ou Remover executantes da tarefa em questão.

![Imagem 12: Nro. Único: ao acionar este botão, será aberto o pop-up Nota/Pedido contendo o Pedido/Nota correspondente à tarefa.](https://ajuda.sankhya.com.br/hc/article_attachments/16921491530135) **Nro. Único:** ao acionar este botão, será aberto o pop-up Nota/Pedido contendo o Pedido/Nota correspondente à tarefa.

![Imagem 13: Dependentes: este botão é apresentado apenas na grade Itens da Tarefa ; seu acionamento exibe na tela o pop-up Tarefas…](https://ajuda.sankhya.com.br/hc/article_attachments/16921556589591) **Dependentes:** este botão é apresentado apenas na grade Itens da Tarefa; seu acionamento exibe na tela o pop-up Tarefas Dependentes, onde serão exibidas em relação a cada item da tarefa separadamente, suas Tarefas Dependentes e suas Tarefas Predecessoras.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS#top)
