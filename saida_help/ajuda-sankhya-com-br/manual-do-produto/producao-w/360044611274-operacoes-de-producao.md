---
id: "360044611274"
titulo: "Operações de Produção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:53:00Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Materiais", "Amostras", "Centro de Trabalho", "Ciclos de Controle de Qualidade", "Finalizar", "Laudo", "Operações de Produção", "Rejeitar", "Tipo de Atividade", "br.com.sankhya.producao.cad.operacaoproducao", "Operações de Produção manual", "Planta", "Apontamento", "Controle de Qualidade", "Ordem de Produção", "Apontamentos", "Iniciar", "Produtos (PA)", "APOTARIFAMAT", "Grupo de Produto", "Subprodutos", "Produção", "Filtros para busca por OP produto centro de trabalho", "Atividades de Ordens de Produção iniciadas", "Ações: aceitar iniciar parar atividades", "Operações"]
---

# Operações de Produção

```
 Módulo: Produção > Rotinas
```

---

Nesta tela, temos as atividades que exigem interação com os usuários executantes, quer seja para apontamento, ou controle de fila de execução.

Apenas atividades oriundas de Ordens de Produção já iniciadas serão exibidas aqui, ou seja, esta tela não trabalha com ordens planejadas, mas sim, ordens que foram de fato criadas e inicializadas pela gerência da produção. 

![Imagem 1: Apenas atividades oriundas de Ordens de Produçã o já iniciadas serão exibidas aqui, ou seja, esta tela não trabalha com…](https://ajuda.sankhya.com.br/hc/article_attachments/360099689334)

Esta tela é composta por diversas informações, sendo esta visualizada em modo grade, ou em modo formulário. A seguir será detalhado seu comportamento e as configurações envolvidas.

| [Painel de filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#paineldefiltros) |  | [Tela - Modo Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modograde) |
| --- | --- | --- |
| [Tela - Modo Formulário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio) |  | [Botão Nova Movimentação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#bot%C3%A3onovamovimenta%C3%A7%C3%A3o) |

## Painel de Filtros

Depois de algumas Atividades criadas e inicializadas, você pode através dos filtros disponibilizados do lado esquerdo da tela, filtrar os dados desejados.

![Imagem 2: Depois de algumas Atividades criadas e inicializadas, você pode através dos filtros disponibilizados do lado esquerdo…](https://ajuda.sankhya.com.br/hc/article_attachments/360101894593)

**Seção Geral**

Esta seleção de informações, pode ser realizada por meio da criação de um filtro personalizado, ou através das seguintes opções de filtro:

**Nro. OP:** informe neste campo, o número da Ordem de Produção, de modo a obtê-la em específico na tela.

**Nro. Lote:** este campo, recebe o número dos lotes relacionados às Ordens de Produção lançadas.

**Tipo do Período:** defina o período a ser considerado para apresentação das atividades. Temos, as seguintes opções:

- Inclusão;
- Aceite;
- Início;
- Final;
- Início Prev;
- Final Prev.

**Período:** determine neste campo, um período em que ocorreram lançamentos de Ordens de Produção.

**Centro de Trabalho:** as Ordens de Produção podem também ser apresentadas pelo Centro de Trabalho ao qual pertencem, assim insira esta informação neste campo.

**Cód. Produto:** informe aqui, o produto ligado a Ordem de Produção.

**Referência do Produto:** preencha neste campo, a referência do produto ligado a Ordem de Produção.

**Grupo de Produto (PA):** através deste campo, defina o grupo de produtos relacionado ao Produto Acabado.

**Planta:** você pode filtrar as informações, buscando também pela planta das Ordens de Produção.

**Executante:** neste campo, busque pelas atividades através do executor das mesmas.

**Tipo de Atividade:** a tela pode ser também alimentada, através das informações pelos tipos possíveis de atividade. São eles:

- Todas;
- Operação;
- Setup de Centro de Trabalho;
- Cleanup de Centro de Trabalho;
- Controle de Qualidade.

**Seção Situação**

É possível buscar as atividades ligadas às Ordens de Produção, através da Situação em que elas se encontram. São elas:

- Todas;
- Aceitas;
- Iniciadas;
- Finalizadas;
- Aguardando Aceite;
- Paradas.

De forma semelhante, você pode rastrear as atividades, de acordo com seu **"Status"**. Temos as seguintes opções:

- Todos;
- Operação Normal;
- Reprocesso.

Por fim, é possível localizar as atividades através de seu **"Status Ciclo de Qualidade"**. Você pode definir dentre as seguintes alternativas:

- Todos;
- Não Iniciado;
- Em Andamento;
- Aprovado;
- Reprovado;
- Aprovada com ressalvas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#top)

## Tela - Modo Grade

A partir da visualização da tela em modo grade, você obtém as principais informações das atividades (operações de produção) resultantes do filtro aplicado; é possível efetuar a múltipla seleção de registros, mantendo pressionada a tecla "Ctrl" do teclado, e selecionando as linhas desejadas.

Por padrão, as atividades serão ordenadas pela coluna **"Prioridade"**. Esta grade não suporta configuração específica de ordenação, ou seja, mesmo que seja feita ordenação por algum critério, a ordenação padrão é retomada quando a tela é reiniciada.

As ações que podem ser comandadas sobre as atividades, são aquelas geradas a partir da seleção de um registro e ao acionar algum dos botões disponíveis na barra superior. São eles:

**![Imagem 3: Anexos processos produtivo: Ao acionar este botão, temos a exibição do pop-up "Documentos" , que contém os anexos ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16703287447959) Anexos processos produtivo:** Ao acionar este botão, temos a exibição do pop-up  **"Documentos"**, que contém os anexos ou link's configurados no processo produtivo/atividade, sendo possível efetuar o download dos arquivos anexados.

![Imagem 4: Aceitar: Temos aqui, um botão cuja função é marcar como aceitas as atividades selecionadas na grade pelo usuário,…](https://ajuda.sankhya.com.br/hc/article_attachments/16703287456663) **Aceitar:** Temos aqui, um botão cuja função é marcar como aceitas as atividades selecionadas na grade pelo usuário, colocando este como responsável por elas no fluxo de trabalho. Caso existam operações de estoque configuradas para serem executadas nesse momento, serão executadas de forma automática. Uma vez aceita a atividade em questão, ela passa a fazer parte da lista de tarefas do usuário e apenas este terá a possibilidade de executá-la.

![Imagem 5: Iniciar: Este botão assinala as atividades selecionadas como iniciadas, inserindo d ata e hora no campo "Dh. Início…](https://ajuda.sankhya.com.br/hc/article_attachments/16703287459991) **Iniciar:** Este botão assinala as atividades selecionadas como iniciadas, inserindo data e hora no campo **"Dh. Início Atividade"**. Em outras palavras, será apontado ao sistema pelo usuário o inicio da atividade (operação) em questão.

![Imagem 6: Parar: Por meio deste botão, é possível efetuar a pausa d a(s) atividade(s) selecionada(s) na grade. Sendo que, ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283373079) **Parar:** Por meio deste botão, é possível efetuar a pausa da(s) atividade(s) selecionada(s) na grade. Sendo que, ao solicitar a parada de uma ou várias atividades será solicitado no pop-up **"Parada da atividade"**, o tipo de parada, um motivo para este procedimento e as observações a cerca do mesmo.

![Imagem 7: Parar: Por meio deste botão, é possível efetuar a pausa d a(s) atividade(s) selecionada(s) na grade. Sendo que, ao…](https://ajuda.sankhya.com.br/hc/article_attachments/7788152959127)

Temos assim, os seguintes pontos:

- Tratando-se do campo **"Tipo"** de parada, a opção **"Fim de turno"** só estará disponível se a atividade selecionada estiver configurada para suportar Multi-turnos ([Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674) do Processo Produtivo, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abageral), marcação **"Multi-turno"**);
- Além disso, ao optar pela opção Fim de turno o campo **"Motivo Parada"** será preenchido automaticamente com o motivo configurado na Configuração de Atividades do Processo Produtivo, aba Geral, campo **"Motivo de parada (fim de turno)"**;
- Os motivos de parada deverão estar previamente cadastrados na tela [Motivos de Parada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611614).

**Observação:** o parâmetro **"É obrigatório selecionar um motivo para parada - OBRIGMOTIVPARAD"** quando ligado, será obrigatório informar o motivo pela qual ocorreu a(s) parada(s) na(s) atividade(s) do tipo **"Normal"**.

**Nota:** quando a atividade estiver pausada, as abas [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abageral), [Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaapontamentos) e [Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abacontroledequalidade) serão desabilitadas.

**Observação:** ao parar uma atividade que utiliza Centro de Trabalho, o usuário executante poderá liberá-lo, caso seja necessário.

Em casos em que a atividade já se encontra como parada, o usuário poderá realizar a liberação do Centro de Trabalho, porém para executar esta ação, a atividade deve estar configurada para liberar o C.T manualmente.

![Imagem 8: Continuar: Acione este botão para reiniciar a(s) atividade(s) que estão pausadas. Sendo que, o mesmo só será…](https://ajuda.sankhya.com.br/hc/article_attachments/16703287469079) **Continuar:** Acione este botão para reiniciar a(s) atividade(s) que estão pausadas. Sendo que, o mesmo só será apresentado quando a atividade selecionada estiver parada.

**Nota:** ao continuar uma atividade que utiliza Centro de Trabalho o sistema irá realocar automaticamente o C.T da atividade, desde que este não esteja em uso por outra atividade.

Se a alocação da atividade utilizar um Centro de Trabalho específico ou por categoria que utiliza o padrão da categoria e ambos forem de uso exclusivo, caso estes estiverem alocados em outra atividade não será possível dar continuidade, sendo assim, o sistema exibirá a mensagem:

**"Não será possível continuar a atividade, pois o Centro de Trabalho não é exclusivo e está sendo utilizado por outra atividade."**

Quando o Centro de Trabalho é por categoria que utiliza o **"Tipo de Alocação"**, **"Inclusão de ordem"** ou **"Antecipado (no planejamento)"** e este for de uso exclusivo, caso o C.T esteja alocado em outra atividade, será apresentado um pop-up para o usuário selecionar outro Centro de Trabalho da mesma categoria que esteja disponível para uso.

![Imagem 9: Finalizar: Através deste botão, as atividades são marcadas como finalizadas, o campo "Dh. Fim Atividade" é alimentado,…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283381527) **Finalizar:** Através deste botão, as atividades são marcadas como finalizadas, o campo **"Dh. Fim Atividade"** é alimentado, além de ser disparada uma transição do processo para a próxima atividade caso haja, ou será concluído o processo. Portanto, o usuário aponta ao sistema o fim da atividade em questão.

![Imagem 10: Rejeitar: Este botão possui a função inversa do botão Aceitar , ou seja, o usuário não traz a atividade para sua lista…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283386647) **Rejeitar:** Este botão possui a função inversa do botão Aceitar, ou seja, o usuário não traz a atividade para sua lista de tarefas e sinaliza ao sistema a não possibilidade de execução da mesma.

![Imagem 11: Liberar C.T: Caso esteja operando uma atividade configurada apenas para liberar o Centro de Trabalho manualmente,…](https://ajuda.sankhya.com.br/hc/article_attachments/16703287478295) **Liberar C.T:** Caso esteja operando uma atividade configurada apenas para liberar o Centro de Trabalho manualmente, efetua-se esta liberação por meio deste botão; o sistema verifica se o Centro de Trabalho vinculado à atividade foi liberado; caso negativo, não será permitida a finalização da atividade.

![Imagem 12: Alterar C.T: Por meio deste botão, realiza-se a modificação do Centro de Trabalho em questão. Para que cada usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/16703287481367) **Alterar C.T:** Por meio deste botão, realiza-se a modificação do Centro de Trabalho em questão. Para que cada usuário possa fazer uso desta funcionalidade, é necessário que na tela [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854) (módulo Produção > Rotinas > Operações de Produção), a opção **"Altera Centro de Trabalho"** esteja assinalada. A alteração de Centro de Trabalho possui algumas particularidades:

- Ao modificar um C.T., serão disponibilizados para seleção, os centros pertencentes à Planta da Operação de Produção e que pertencem à mesma [Categoria do Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119033) atual;
- Se o CT estiver em uso pela atividade, será realizada a liberação do mesmo e o consequente registro no sistema do usuário que comandou a ação;
- Caso a atividade já esteja iniciada, será realizada a alocação do novo Centro de Trabalho registrando no sistema o usuário que comandou a ação. Além disso, o sistema verifica se o Centro de Trabalho não está em uso por outra atividade;
- Se a atividade já estiver iniciada, as indisponibilidades de Centro de Trabalho também serão consideradas, ou seja, se existir uma indisponibilidade para o Centro de Trabalho pendente naquele momento, não será permitido seu uso.
- Caso a atividade já esteja iniciada, e a indisponibilidade for em um momento posterior ao início do uso, o sistema apresenta um alerta quanto a este fato.

![Imagem 13: Ações: Este botão terá suas opções apresentadas apenas se uma ação for cadastrada na tela Dicionário de dados .](https://ajuda.sankhya.com.br/hc/article_attachments/16703287484439) **Ações:** Este botão terá suas opções apresentadas apenas se uma ação for cadastrada na tela [Dicionário de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

**Importante:** o usuário "dono" da atividade (seu candidato Executante), é aquele que realizou seu aceite ou a inicializou. Considerando um único usuário ou mesmo um grupo de usuários, uma atividade poderá ser visualizada apenas pelo usuário que fez sua aceitação ou inicialização. O usuário configurado como Gerente de Manufatura, poderá visualizar todas as atividades, tendo elas passado ou não pelo aceite ou inicialização. Além disso, a finalização das atividades poderá ser realizada apenas pelo usuário dono da atividade, ou ainda pelo seu Gerente de Manufatura.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#top)

## Tela - Modo Formulário

No modo formulário inicialmente, você poderá visualizar um cabeçalho da atividade selecionada, contendo as principais informações da mesma, tais como, Nro. OP, Nro. Lote, Dh. OP, Qtd. (quantidade do PA), Produto PA da OP, Descrição da Atividade e Data de criação da Atividade.

Os detalhes e demais ações da atividade são distribuídos nas abas **"Geral"**, **"Apontamentos"**, **"Produtos (PA)"** e **"Controle de Qualidade"**. Trataremos de cada aba a seguir.

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abageral) |  | [Aba Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaapontamentos) |
| --- | --- | --- |
| [Aba Produtos (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaprodutospa) |  | [Aba Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abacontroledequalidade) |
| [Aba Execuções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaexecues) |  | [Aba Mov. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abamov.acessrias) |

## Aba Geral

O objetivo dessa aba é exibir as informações gerais referentes a Ordem de Produção selecionada. É uma aba apenas informativa, e por isso todos os campos são atualizados automaticamente pelo sistema e encontram-se desabilitados para realização de modificações.

![Imagem 14: O objetivo dessa aba é exibir as informações gerais referentes a Ordem de Produção selecionada. É uma aba apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/7788208402711)

Esta aba é composta pelas seguintes informações: 

**Controle:** temos aqui o tipo de controle do produto, caso exista.

**Complemento do Produto:** este campo exibe o conteúdo do campo **"Complemento"** do Cadastro de Produtos.

**Un. Lote:** visualize aqui a unidade de lote padrão do produto. Exemplo: Unidade, Caixa etc.

**Dt./Hr. Início Prev.:** este campo, exibe a data/hora prevista para início da atividade.

**Dt./Hr. Final Prev.:** complementando o campo anterior, temos aqui a data/hora prevista para o fim da atividade.

**Dh. Início Atividade:** neste campo será registrada efetivamente a data/hora em que a atividade começou.

**Dh. Fim Atividade:** semelhante ao campo anterior, temos aqui a data/hora em que a atividade terminou.

**Grupo do Produto:** visualize aqui o grupo de produtos ao qual pertence o Produto Acabado. Exemplo: Descartáveis, Comestíveis etc.

**Executante:** Este campo exibe o usuário que aceitou a atividade.

**Centro de Trabalho:** temos neste campo, o Centro de Trabalho ao qual a atividade está vinculada.

**Nro. Processo:** este campo, apresenta o processo ao qual a atividade está inserida.

**Prioridade:** a prioridade desta atividade é visualizada neste campo.

**Tempo Gasto em Minutos:** através deste campo, será exibida a duração em minutos do tempo gasto para realização da atividade.

**Multi-produto:** este campo, quando apresentado marcado, tem-se que a operação permite Multi-Produtos.

**Repositório da operação:** o repositório relacionado a operação, será exibido neste campo.

**Repositório de destino:** de forma semelhante ao campo anterior, temos aqui o repositório de destino relacionado a atividade.

**Nro. OP Principal:** este campo irá exibir o número da Ordem de Produção principal, a qual a atividade está ligada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio)

## Aba Apontamentos

Esta aba e a aba seguinte (aba Produtos (PA)), são apresentadas quando na [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674) do Processo Produtivo, na aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento), estiver selecionado no campo **"Tipo de Apontamento"**, a opção **"Apontamento de PA / MP"**.

Esta aba é responsável por receber os apontamentos do produto acabado (ou componente) produzido na atividade, assim como suas respectivas matérias-primas consumidas e subprodutos gerados.

**Observação:** com o parâmetro **"Aponta Tarifa junto com Materiais. - APOTARIFAMAT"** ligado, a configuração das [Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611074) poderão ser realizadas através da tela [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto), aba [Matérias-Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abamat%C3%A9rias-primas), e o apontamento de Tarifas CIP feito juntamente com o apontamento de materiais.

Podemos observar no alto da aba, o botão **"Confirmar"**, que deve ser acionado, após a inclusão de um apontamento e/ou realização de suas respectivas edições. Caso a atividade possua algum apontamento pendente, não será possível finalizá-la.

Além disso, caso seja feita a tentativa de exclusão de um apontamento, o sistema valida se este apontamento gerou registros de operações de estoque; caso afirmativo, a exclusão não acontecerá e o usuário será avisado deste fato.

Logo abaixo, temos o **"Nro. Único"**, que é preenchido automaticamente pelo sistema no ato da inserção de um novo apontamento.

**Importante:** o sistema conta com  uma validação, de modo que não será permitida a inserção de um novo apontamento para a mesma atividade, caso exista algum pendente para aquele **"Produto + Controle"**. Na inclusão de um novo apontamento, onde é alterada a quantidade apontada e realizada sua confirmação, o sistema realizará as seguintes validações:

**1.** Verifica se a atividade em questão possui operações de estoque que geram nota de produção; caso exista, o sistema valida se a quantidade apontada é menor que a quantidade a produzir; caso seja, o sistema questiona ao usuário:

**"Quantidade apontada menor que o saldo restante da OP. Este será o último apontamento para estes produtos/controle?"**

Ao clicar em **"Sim"**, será executada a baixa de materiais (MP) considerando a quantidade total pendente de faturamento, ou seja, não será executado o cálculo de proporcionalização de MP's de acordo com a quantidade apontada de Produto Acabado na nota de produção a ser gerada. Se optar por **"Não"**, o processo seguirá normalmente.

**2.** Quando se cria um novo item de apontamento, o sistema abre um pop-up contendo **"Produto + Controle"** para que seja selecionado e criado o item; com o comportamento descrito acima, o sistema não apresentará o Produto + Controle que estiver com sua produção já concluída.

Você pode visualizar maiores detalhes sobre este comportamento, por meio do link [Ineficiência do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-).

**Importante:** ao tentar finalizar uma atividade, existindo Apontamentos Divergentes, ou seja, apontamentos que fujam dos desvios inferior ou superior ([Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#abaapontamento)), no pop-up denominado Apontamentos Divergentes, será apresentada a seguinte mensagem:

**"Qtd. Apontada é menor/maior que a qtd. em operação para: <Descrição do Produto (PA)>. Deseja continuar a confirmação?"**

**Observação:** se a mensagem abaixo for exibida, verifique se há uma divergência entre o horário da máquina onde o sistema está instalado e o horário da máquina onde as ordens de produção estão sendo executadas:

**"A 'Dh. Início da Atividade' 'Atividade X' não pode ser anterior à 'Dh. Fim da Atividade' na atividade 'Atividade Y'."**

**Nota:** os nomes das atividades mudarão conforme a base utilizada pelo usuário.

A aba Apontamentos é composta por outras duas sub-abas. A saber:

[Sub-aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#sub-abageral)                                                      [Sub-aba Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#sub-abaitens)  

---

#### Sub-aba Geral

Esta aba tem o objetivo de apresentar as informações gerais referentes ao apontamento.

![Imagem 15: Esta aba tem o objetivo de apresentar as informações gerais referentes ao apontamento.](https://ajuda.sankhya.com.br/hc/article_attachments/7788214142487)

Ressaltamos que a data e a hora informada no campo **"Dh. Apontamento"** não pode ser menor que a data/hora estabelecida no início da atividade, pois toda atividade é precedente do apontamento. Assim, verifique se o horário do servidor está igual ao horário do computador.

Além disso, nessa aba o usuário pode inserir uma **"Observação"** referente ao apontamento. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaapontamentos)

#### Sub-aba Itens

Essa aba exibe em sua parte superior, uma grade com os Produtos Acabados (PA) ou Componentes que estão sendo apontados na atividade, com suas respectivas quantidades.

![Imagem 16: Essa aba exibe em sua parte superior, uma grade com os Produtos Acabados (PA) ou Componentes que estão sendo apontados…](https://ajuda.sankhya.com.br/hc/article_attachments/7788219840535)

Esses produtos são carregados automaticamente pelo sistema na inserção de um novo apontamento, de acordo com a configuração de Apontamento da atividade.

Quando o campo **"Quantidade base para apontamento"** da aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova#abaapontamento) estiver configurado com a opção **"Não sugere"**, a coluna **"Qtd. apontada"** do PA será exibida com o valor igual a zero, dessa forma, o apontamento só será confirmado após a alteração desse valor. Caso o referido campo esteja com a opção **"Qtd. apontada de PA"** selecionada, o apontamento poderá ser confirmado sem a necessidade de editar o valor apresentado na coluna. 

Na coluna **"Qtd. Total de Perda"** informe a quantidade correspondente à perda total do apontamento para posterior finalização da atividade.

Informe na coluna **"Qtd. de Motivos de Perda"** a quantidade total de motivos de perda. Se for inserida uma quantidade de motivos de perda maior do que 1, será aberto o pop-up de detalhamento de perda automaticamente: 

[GIF animado: Imagem 17: Informe na coluna "Qtd. de Motivos de Perda" a quantidade total de motivos de perda. Se for inserida uma quantidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/6375434578711)

**Nota:** conforme exibido no gif acima, com uma quantidade de motivos de perda maior do que 1, também é habilitado o botão ![Imagem 18: Nota: conforme exibido no gif acima, com uma quantidade de motivos de perda maior do que 1, também é habilitado o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283405335) **"Detalhar Perdas"**. Através dele você informa o volume de perda por cada motivo durante o apontamento e, após salvá-lo, o botão seguirá habilitado para consultas:

[GIF animado: Imagem 19: Nota: conforme exibido no gif acima, com uma quantidade de motivos de perda maior do que 1, também é habilitado o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/6375425365655)

**Observações:**

- Se a Qtd. de Motivos de Perda informada no pop-up Detalhamento de Perdas for diferente do valor informado no campo, será exibida a mensagem abaixo:

**"Total de motivos de perda detalhado é diferente do valor X informado no campo Qtd. de Motivos de Perda. Por favor revisar os motivos informados e salvar novamente."**

- Quando for informada uma Qtd. Perda no pop-up Detalhamento de Perdas diferente da inserida no campo Qtd. Total de Perda, será apresentada a seguinte mensagem:

**"Total de perda confirmado é diferente do valor X informado no campo Qtd. Total de perda. Por favor revisar os volumes informados e salvar novamente."**

Após confirmar os apontamentos com os motivos de perdas, a aba [Detalhamento de Perdas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova#abadetalhamentodeperdas) na tela [Ordens de Produção - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova) será preenchida automaticamente. Também será gerada uma Nota de Produção para o Subproduto e Produto Acabado e os resultados apresentados na tela [Dashboard OEE](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405006529047-Dashboard-OEE). 

**Importante:** caso o parâmetro **"É obrigatório selecionar um motivo para perda - OBRIGMOTIVPERDA"** esteja ativado, ao iniciar a atividade e efetuar os apontamentos das unidades e suas respectivas perdas, torna-se obrigatório o preenchimento do Motivo da Perda; caso contrário, ao confirmar o procedimento, será apresentada a seguinte mensagem:

**"É obrigatório o usuário selecionar um motivo para perda sempre que apontar 'qdt. perda'"**

Por meio do botão **"Nro. Série"** será aberto o pop-up **"Número de série"** onde serão apresentados os números de série do Produto Acabado. Neste pop-up, se a série foi configurada para ser gerada automaticamente, tem-se apenas a visualização dos dados e estes não poderão ser editados. Caso a geração da série seja manual, será possível inserir e/ou excluir informações no pop-up.

Também no pop-up Número de série, tem-se a marcação **"Perda"** que se assinalada, a série em questão corresponde a uma determinada quantidade apontada como perda do PA. Nestas situações, a quantidade de séries sinalizadas como perdas deve ser igual a quantidade definida como perda no apontamento.

A parte inferior da sub-aba Itens, é composta por outras três abas, sendo elas:

[Aba Materiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abamateriais)                              [Aba Subprodutos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abasubprodutos)                    [Aba Recursos CT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abarecursosct)  

---

#### Aba Materiais

A primeira delas, exibe os produtos que são matérias-primas do Produto Acabado, ou seja, todos os produtos que são utilizados para gerá-lo. Esta aba será habilitada apenas quando a atividade em questão estiver configurada para **"Apontar matéria-prima"**. As matérias-primas da atividade podem ser carregadas de forma automática, conforme configuração e vinculação com o **"PA x Processo Produtivo"**. Caso a quantidade do Produto Acabado seja modificada, os registros dessa sub-aba são alterados proporcionalmente.

**Nota:** caso aconteçam situações em que na realização dos apontamentos, as matérias-primas reservadas não sejam suficientes para supri-los (inclusão de PAs com MPs insuficientes para atenderem a fórmula de produção), será exibida na tela uma mensagem alertando sobre tal ocorrência.

**Importante:** o parâmetro **"Permitir definir produto como MP de si próprio. - PRODMPPROP"** quando habilitado, possibilitará que um produto seja apontado como Matéria-prima de um apontamento, quando este produto for o próprio Produto Acabado do referido apontamento.

**Observação:** tratando-se de um processo de reprocessamento/reparo, é possível que um produto seja utilizado como matéria-prima de si mesmo.

Quando houver a perda de matérias-primas durante a execução da atividade, você poderá ligar o parâmetro **"Habilita perda de Matéria Prima na produção - HABPERDAMPPROD"**, assim, será possível especificar uma ou mais perdas nessa sub-aba. Dessa forma, o sistema exibirá as colunas **"Qtd. Total de Perda"**, **"Qtd. de Motivos de Perda"** e **"Motivo(s) de Perda"**, onde serão apontadas as quantidades das perdas.

Considere ainda que, quando houver mais de um motivo de perda para a mesma matéria-prima, o botão ![Imagem 20: Considere ainda que, quando houver mais de um motivo de perda para a mesma matéria-prima, o botão Detalhar Perdas será…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283405335) Detalhar Perdas será habilitado para que você informe os detalhes.

Então, após realizar esse apontamento, você poderá conferi-lo na aba [Detalhamento de Perdas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova#abadetalhamentodeperdas) da tela [Ordens de Produção - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova).

**Observação:** ao habilitar o parâmetro **"É obrigatório selecionar um motivo para perda de Matéria Prima - OBRIGMOTPERDAMP"**, você deverá, obrigatoriamente, informar na coluna **"Qtd. Perda"**, o motivo da perda de Matéria Prima quando houverem apontamentos com essa perda.

**Nota:** as especificações de perdas de matérias-primas estarão disponíveis a partir da versão **4.16** do sistema.

No campo **"Local de Baixa"** será exibido o local da baixa da MP, este local deve estar previamente definido no campo **"Local para baixa de MPs"** da aba **"Atividades"** das [Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova#opera%C3%A7%C3%B5esdeestoque), tela [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova). Além disso, esse campo poderá ser editado quando a marcação **"Permitir alterar local da baixa da MP"** da aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento) das [configurações das atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento), for habilitada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#sub-abaitens) 

**![Imagem 21: Cenários Específicos de Apontamento de Matérias-primas: Pré-ordem de Transferência e o Erro "PROD_E00075"](https://ajuda.sankhya.com.br/hc/article_attachments/33773697751575) Cenários Específicos de Apontamento de Matérias-primas: Pré-ordem de Transferência e o Erro "PROD\_E00075"**

Ao realizar apontamentos em **pré-ordens de transferência**\*, especialmente quando a quantidade apontada é maior do que a prevista, o sistema pode criar uma linha adicional para o material. Ao tentar confirmar, pode ser exibida a mensagem de erro **"Não foi possível obter o estoque necessário da Matéria-Prima XXX - MP PADRÃO COM LOTE YYYYY no Local ZZZ. Código: PROD\_E00075**".

Essa mensagem geralmente indica que:

- Existem matérias-primas (MPs) apontadas sem o lote informado, e o sistema tenta realizar a **"explosão de lotes"** sem encontrar estoque suficiente.
- Os lotes no estoque podem estar diferentes dos lotes apontados, o que faz com que o sistema os ignore na explosão.
- A data de validade do item pode ser anterior à data atual.
- A quantidade apontada de material é maior que a quantidade transferida.

É importante notar que o comportamento do sistema nesse cenário pode variar dependendo da configuração da nota de produção e do contexto da transferência (seja dentro de uma atividade específica ou fora dela, e também em comparação com reservas).

**Solução e Recomendação:**
Para prosseguir, é fundamental **ajustar a quantidade da matéria-prima (MP)** na movimentação interna para que o sistema consiga localizar e alocar o estoque corretamente.

Se você estiver enfrentando esse erro, a orientação é:
1. **Verifique os lotes e datas de validade** dos itens no estoque e compare com os lotes apontados. Se houver MPs sem lote informado, ou lotes inconsistentes, ajuste conforme o estoque disponível.
2. **Ajuste a quantidade apontada das MPs** para as quais os lotes foram informados, ou **exclua a matéria-prima "sem lote"** do apontamento.
3. Utilize a aba **"Mov. Acessórias"** e o botão **"+ Nova Movimentação"** para realizar os ajustes manuais necessários no estoque da matéria-prima. Esta funcionalidade permite que você controle manualmente as movimentações de estoque, garantindo que a quantidade correta seja baixada.

#### Aba Subprodutos

Já a aba Subprodutos exibe os subprodutos que foram gerados a partir do processamento do Produto Acabado na atividade em questão. Essa aba será habilitada apenas quando a atividade selecionada estiver configurada para **"Apontar subprodutos"**. Os subprodutos da atividade, podem ser carregados de forma automática conforme configuração e vinculação com o PA x Processo Produtivo. Caso a quantidade do Produto Acabado seja alterada os registros dessa sub-aba são ajustados proporcionalmente.

**Nota:** você poderá realizar o apontamento de Subprodutos não previstos em fórmula.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#sub-abaitens) 

#### Aba Recursos CT

Por fim, a aba Recursos CT tem como objetivo, permitir a realização do apontamento dos recursos de Centros de Trabalho da Atividade ou da OP, de acordo com a respectiva configuração (atividade em execução). Como o apontamento de recursos de Centro de Trabalho depende da quantidade apontada de PA na atividade em questão, as colunas serão apresentadas em colorações distintas, ou seja, em **vermelho**, se a quantidade apontada for igual a **"0"** (zero) e **amarelo**, se o apontamento de itens de recursos não for o esperado.

**Observação:** o campo **"Qtd. apontada (Total)"** apresentará a multiplicação da **"Qtd. Apontada"** pela **"Qtd. Alocada"** definida para o Recurso em Recursos PA ou Recurso por Centro de Trabalho conforme combinação de Centro de Trabalho e Categoria de Recurso selecionados.

Tem-se ainda que você poderá realizar uma transferência parcial no sistema,  em que ao confirmar o mesmo a mensagem será apresentada:

**"Este será o último apontamento? Caso seja o último apontamento, este receberá o saldo das matérias-primas do tipo fixa."**

Ao clicar em **"Sim"**, a diferença de quantidade restante para apontar MP será considerada neste apontamento. Se não, o último apontamento será confirmado conforme a proporção da MP referente á quantidade do PA.

Em casos em que a quantidade apontada do PA for superior ao tamanho do lote, a quantidade da MP tipo fixa não passará da quantidade fixa configurada no processo.

Quando já houver uma nota de produção em determinada atividade, e nesta for realizada apontamentos parciais, o sistema exibirá o pop-up já existente, assim você verá a mensagem:

**"Este será o último apontamento? Caso seja o último apontamento, este receberá o saldo das matérias-primas do tipo fixa e a diferença de quantidade será considerada com perda para este produtos/controles."**

Se você clicar no botão **"Não"**, será informado ao sistema que o apontamento em questão não será o último apontamento e a quantidade de MP será proporcional à quantidade apontada do PA. E quando for indicado que é o último apontamento, o mesmo receberá o saldo da MP do tipo fixo.

Você também poderá realizar este comportamento na tela [Apontamento de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o).

**Nota:** para realizar o apontamento com o valor **"0"**, marque a opção **"Permitir apontamento de 100% de perda"** na tela **"Processo Produtivo"**, aba **"Apontamento"** dos itens do roteiro. Para saber mais sobre esta funcionalidade acesse a tela [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio)

## Aba Produtos (PA)

Esta aba e a aba anterior (aba Apontamentos), são apresentadas quando na Configuração de Atividades do Processo Produtivo, na aba Apontamento estiver selecionado no campo  Tipo de Apontamento a opção Apontamento de PA / MP.

![Imagem 22: Esta aba e a aba anterior (aba Apontamentos), são apresentadas quando na Configuração de Atividades do Processo…](https://ajuda.sankhya.com.br/hc/article_attachments/7788221855511)

Serão exibidos na grade Produtos (PA) os Produtos Acabados da Ordem de Produção a qual a atividade pertence, com suas principais informações. Nos casos em que existirem Ordens de Produção com multiprodutos, ou seja, o mesmo produto com controles distintos, serão apresentados vários registros nesta grade.

Na grade Matérias Primas você pode visualizar os materiais consumidos na atividade em questão, a quantidade de cada um e se utilizam uma matéria prima alternativa, entre outras informações.

Ao final, temos a grade Materiais Alternativos que comporta os materiais utilizados como alternativa às matérias primas apresentadas na grade anterior, a quantidade aplicada, entre outros dados.

**Observação:** as informações dessa aba são referentes as configurações feitas no lançamento da ordem e não serão alteradas, ou seja, caso o apontamento feito pelo usuário seja diferente do lançamento, as informações contidas nessa aba não são impactadas.

> **Importante:** para casos em que o Operador de Produção não pode visualizar as matérias primas devido ao sigilo na composição do produto final, é possível configurar o sistema para inibir a visualização das MPs através da configuração **"Inibe acesso à matéria prima"** da aba **Segurança** do cadastro de **Usuários**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio)

## Aba Controle de Qualidade

Através desta aba, o operador realiza as operações de comando pertinentes aos Ciclos de Controle de Qualidade da Ordem de Produção, correspondente a Atividade.

![Imagem 23: Através desta aba, o operador realiza as operações de comando pertinentes aos Ciclos de Controle de Qualidade da Ordem…](https://ajuda.sankhya.com.br/hc/article_attachments/7788269993495)

Esta aba é dividida em três espaços. Trataremos a seguir sobre cada uma delas:

[Grade Ciclos de Controle de Qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#gradeciclosdecontroledequalidade)                                   [Grade Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#gradeamostras)

[Grade Laudos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#gradelaudos)

---

#### Grade Ciclos de Controle de Qualidade

Nessa primeira grade da tela, são apresentadas todas as instâncias de Ciclos de Controle de Qualidade da Ordem de Produção referente a Atividade.

Caso a atividade em questão possua um evento de Controle de Qualidade anexada a ela, será possível então, inicializar um novo ciclo através do botão **"Iniciar Ciclo"** que ficará habilitado.

**Importante:** o ciclo de controle de qualidade foi implementado apenas para os produtos que possuem controle adicional do tipo **"Número do Lote"**. Essa configuração é realizada na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), no campo **"Controlar por"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abacontroledequalidade) 

#### Grade Amostras

Na segunda grade visualizada na tela, você pode comandar as ações pertinentes a uma amostra. Apenas as atividades configuradas com **"Operações"** de **"Amostragem"** ou **"Amostragem + Laudo"** serão capazes de executar ações de amostras.

![Imagem 24: Esse botão tem a finalidade de gerar amostras do Produto Acabado para os ensaios (análises). Ao ser acionado, caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283408279) Esse botão tem a finalidade de gerar amostras do Produto Acabado para os ensaios (análises). Ao ser acionado, caso tenha mais de um tipo de amostra, o pop-up **"Tipo Amostra"** será aberto para que seja selecionado o tipo de amostra que se deseja coletar; existindo apenas um tipo de amostra, esta já será diretamente inserida na grade.

![Imagem 25: Através deste botão, você pode realizar a exclusão de amostras já inseridas na grade. Sendo que, somente as amostras…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283412375) Através deste botão, você pode realizar a exclusão de amostras já inseridas na grade. Sendo que, somente as amostras que apresentarem seu status como Pendente poderão ser excluídas.

![Imagem 26: Esse botão tem como função aprovar uma amostra coletada, ou seja, confirma que a amostra em questão está apta para o…](https://ajuda.sankhya.com.br/hc/article_attachments/16703283417111) Esse botão tem como função aprovar uma amostra coletada, ou seja, confirma que a amostra em questão está apta para o ensaio (análise).

![Imagem 27: Utilizando este botão, é possível reprovar uma amostra coletada, ou seja, a amostra em questão não está própria para o…](https://ajuda.sankhya.com.br/hc/article_attachments/16703562637335) Utilizando este botão, é possível reprovar uma amostra coletada, ou seja, a amostra em questão não está própria para o ensaio (análise); deste modo, não será possível lançar laudo de análise para a amostra.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abacontroledequalidade) 

#### Grade Laudos

Por fim, nesta terceira grade, são registrados os ensaios (análises) sobre uma determinada amostra (selecionada na grade acima). Aqui serão registrados o resultado do ensaio a partir do documento chamado de **"Laudo"**. Apenas as atividades configuradas com Operações de Laudo ou Amostragem + Laudo terão a capacidade de executar ações sobre laudo. Alterando o modo de visualização desta grade para o modo formulário, temos três partes:

- **Cabeçalho:** No cabeçalho do laudo visualiza-se o número do laudo em questão, assim como seu **"Padrão de Classificação"** (teste ao qual o laudo representa).
- **Aba Geral:** Nessa aba é possível visualizar as demais informações relacionadas ao laudo, além de editar a **"Data e hora"** da análise.
- **Aba Item de laudo:** Por esta aba, você pode efetuar o apontamento do resultado de cada uma das características analisáveis, além de especificar uma observação no caso de rejeição da mesma para uma possível correção. Os registros dessa aba têm sua coloração modificada de acordo com seu resultado, sendo elas, **azul** caso esteja dentro dos valores aceitáveis, e **vermelho** caso esteja fora dos valores aceitáveis.

**Observação:** é possível remover uma característica analisável do laudo, desde que ela seja uma característica não obrigatória para o padrão de classificação do mesmo.

Além das subdivisões mencionadas, a grade destinada aos laudos possui alguns botões para ação pertinentes ao operador responsável pelo ensaio (análise), são eles:

**Novo:** Esse botão permite o lançamento de um novo laudo para a amostra selecionada. Deve-se selecionar um Padrão de Classificação para o novo laudo. Os itens de laudos são carregados de forma automática de acordo com o padrão selecionado.

**Concluir Laudo:** A finalidade deste botão é a conclusão do laudo selecionado representando a finalização do ensaio (análise) a qual o laudo representa. Será considerado o resultado apontado em cada um dos itens de laudo para se chegar ao resultado do laudo e o último laudo de cada amostra do lote de produto para se chegar ao resultado da Instância do Ciclo de Controle de Qualidade.

**Importante:** pode-se efetuar o lançamento de diversos laudos para uma mesma amostra, porém apenas o último laudo será considerado válido para a conclusão do ciclo de controle de qualidade. Ou seja, o último laudo da amostra torna inválidos os laudos anteriores.

Defina no campo **"Resultado"** se o laudo será aprovado ou reprovado de acordo com as opções **"Conforme"** ou **"Não Conforme"**, respectivamente. Uma vez que, deve ser configurado quando a marcação **"Característica Conforme/Não Conforme"** da tela [Características Analisáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600194-Caracter%C3%ADsticas-Analis%C3%A1veis) for habilitada. Assim, caso a opção Não conforme for selecionada, ficará vermelha quando esta for visualizada em modo grade.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio)

## Aba Execuções

Tem-se nesta aba os registros de execuções da atividade em questão.

![Imagem 28: Tem-se nesta aba os registros de execuções da atividade em questão.](https://ajuda.sankhya.com.br/hc/article_attachments/7788325870359)

**Nota:** tendo-se a continuidade da atividade e a execução do tipo **"Parada - Fim de turno"** possua uma observação, será apresentado um painel na parte inferior da tela contendo informações como o Usuário e a Observação.

**Observação:** se a mensagem abaixo for exibida, verifique se há uma divergência entre o horário da máquina onde o sistema está instalado e o horário da máquina onde as ordens de produção estão sendo executadas:

**"A 'Dh. Início da Atividade' 'Atividade X' não pode ser anterior à 'Dh. Fim da Atividade' na atividade 'Atividade Y'."**

**Nota:** os nomes das atividades mudarão conforme a base utilizada pelo usuário.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio)

## Aba Mov. Acessórias

Esta aba visa apresentar todas as notas vinculadas a Operação de Produção selecionada (documentos de qualquer tipo de movimento, com exceção da nota de produção). Note que a aba é dividida em duas grades, sendo a primeira referente as **"Notas"** e a segunda aos **"Itens"** da nota selecionada na primeira grade.

As notas aqui exibidas, são as geradas por movimentações de estoque conforme configuração do processo produtivo (movimentações de estoque de atividades e transições).

**Observação:** o sistema sempre irá acatar na explosão de lote, o lote que possuir a menor data de validade. Caso queira utilizar o lote gerado encadeado deverá inserí-lo manualmente.

![Imagem 29: Observação: o sistema sempre irá acatar na explosão de lote, o lote que possuir a menor data de validade. Caso queira…](https://ajuda.sankhya.com.br/hc/article_attachments/7788344855703)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#tela-modoformulrio)

## Botão Nova Movimentação

O botão ![Imagem 30: O botão apenas será habilitado caso existam Operações de Estoque com o "Tipo de Execução da Operação" igual a "Ambas"…](https://ajuda.sankhya.com.br/hc/article_attachments/16703603050135) apenas será habilitado caso existam Operações de Estoque com o **"Tipo de Execução da Operação"** igual a **"Ambas"** ou **"Manual**" (tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), [botão Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793), [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674), aba **"Operações de Estoque"**). Desta forma, ao utilizar este botão, as operações poderão ser realizadas manualmente pelo operador da atividade no andamento desta.

Acionando o botão **"Nova Movimentação"** será aberto um pop-up com o registro das operações definidas com o Tipo de Execução da Operação igual a Manual e/ou Ambas para a atividade em questão:

![Imagem 31: Acionando o botão "Nova Movimentação" será aberto um pop-up com o registro das operações definidas com o Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/7788301117719)

Clicando no botão **"Próximo"** será apresentada a grade de matérias-primas da atividade; nesta grade, considere o campo Tipo Material configurado na aba Operações de Estoque. Desta forma, as matérias primas serão apresentadas de acordo com a atividade e suas quantidades:

![Imagem 32: Clicando no botão "Próximo" será apresentada a grade de matérias-primas da atividade; nesta grade, considere o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/7788302246551)

**Nota:** será possível executar uma operação de estoque manual quantas vezes forem necessárias e, da mesma maneira, o usuário poderá editar, inserir e/ou excluir os registros de matérias-primas e seus valores editáveis.

**Observação:** o campo **"Local de Origem"** não será disponibilizado para edição caso a marcação **"Sempre utilizar Local de Origem da Operação"** (tela Processo Produtivo, botão Roteiro, Configuração de Atividades, aba Operações de Estoque) enconteja selecionada.

Ao confirmar a Operação de Estoque Manual, o sistema apresentará a mensagem de confirmação e, após, será gerada a movimentação conforme a operação selecionada e matérias-primas da grade.

**Nota:** ao tentar finalizar uma atividade que possua uma operação de estoque com o Tipo de Execução da Operação igual a Manual e a marcação Obrigatória habilitada, porém que não tenha nenhuma movimentação de estoque manual realizada para esta atividade, o sistema apresentará a seguinte mensagem:

**"Não é possível finalizar atividade, pois existe operação de estoque manual pendente".**

Neste mesmo contexto, finalizando uma atividade do roteiro que possua uma operação de estoque do tipo Manual e Obrigatória porém, que não tenha nenhuma movimentação de estoque manual para a Ordem de Produção realizada, será exibida a mensagem a seguir:

**"Não é possível finalizar atividade, pois existe operação de estoque manual pendente para a Ordem de Produção".**

---

#### Execução da Operação Encadeada

Na tela Operações de Produção, aba [Mov.Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abamov.acessrias), temos o botão [+ Nova Movimentação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#bot%C3%A3onovamovimenta%C3%A7%C3%A3o) que, ao ser acionado, exibirá a operação de estoque de acordo com as configurações da operação de estoque encadeada.

O botão será apresentado quando o **"Tipo de Execução"** da operação de estoque encadeada for **"Manual"**.

No cabeçalho da Nota, temos o campo **"Empresa de Origem"**, que representa a empresa da nota de produção.

O campo **"Empresa de Destino"** receberá o valor da operação encadeada.

**Observação:** este campo será habilitado somente se a TOP for de Transferência.

Ao clicar no botão **"Próximo"**, o pop-up seguirá para a próxima página de configurações, na qual são exibidos os seguintes campos:

O **"saldo"** será o saldo do produto disponível para movimentação a partir da operação Encadeada. Sendo que, o valor deste campo é calculado como o total do produto em notas de produção subtraindo o valor movimentado por operação encadeada.

No campo **"Qtd. a Movimentar"**, será informado a quantidade do produto que será movimentado na operação encadeada em questão.

**Nota:** a quantidade a ser inserida no neste campo não poderá ser superior ao Saldo, e não aceitará valores negativos.

O **"Local de Destino"** será o local de destino da Operação Encadeada.

**Observação:** este campo será habilitado para edição somente se a TOP for do tipo T-Transferência.

**Nota:** a finalização da atividade não será permitida caso a Operação Encadeada não for sido executada e estiver marcada como Obrigatória.

![Imagem 33: Para saber mais sobre esta operação, acesse o artigo Configurações de Atividades do Processo Produtivo .](https://ajuda.sankhya.com.br/hc/article_attachments/16703733439255) Para saber mais sobre esta operação, acesse o artigo [Configurações de Atividades do Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#top)
