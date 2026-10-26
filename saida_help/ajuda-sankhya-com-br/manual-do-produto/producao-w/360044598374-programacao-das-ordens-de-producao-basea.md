---
id: "360044598374"
titulo: "Programação das Ordens de Produção baseadas no Plano Mestre de Produção (MPS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-10-22T14:32:26Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Planejamento", "Programação Plano Mestre de Produção manual", "Ordens de Produção", "Produção", "Priorização capacidade finita geração e cancelamento de ordens", "Automática ou manual no gráfico de Gantt", "Centros de Trabalho carga horária e tempo de processamento", "MPS", "Gantt"]
---

# Programação das Ordens de Produção baseadas no Plano Mestre de Produção (MPS)

A rotina Programação Plano Mestre de Produção (MPS) visa alocar ou sequenciar as Ordens de Produção de maneira automática no gráfico de Gantt conforme a capacidade de cada Centro de Trabalho e quantidade de produtos a serem fabricados conforme o MPS.

Além disso, essa rotina possui 2 processos de alocação, sendo elas automática e manual. Observe:

**(1)** **Alocação automática:** esta ação é realizada conforme a carga horária disponível do centro de Trabalho (CT) e o tempo de fabricação do produto acabado (PA) na Ordem de Produção (OP). Sabendo disso, considere o exemplo abaixo:

Após o sistema calcular que uma atividade de uma OP demora 50 horas para ser executada, o sistema verificará o CT que irá executar a atividade e a carga horária disponível do CT.

Se o CT possuir uma carga horária disponível de 10 horas úteis por dia, a OP será programada para ser executada em 5 dias.

A data de início da programação será a data de início do planejamento.

**(1)** **Alocação manual:** para alterar a alocação para manual, basta utilizar o recurso clica e arrasta para movimentar as OP's para outra data e/ou Centro de Trabalho (CT), ou ao clicar na atividade no gráfico de gantt e informar uma nova data e horário manualmente.

A rotina possui as seguintes características: 

- Priorização na execução das OP's de Produtos Intermediários (PI) necessários para a fabricação dos Produtos Acabados (PA);
- O gráfico de Gantt atua com capacidade finita, ou seja, ele é gerado com base no período de planejamento definido no MPS;
- Ao confirmar a programação de produção é possível gerar automaticamente as ordens de produção;
- Caso as execuções das ordens de produção não ocorram conforme a programação, pode-se efetuar o cancelamento e gerar uma nova programação.

![Imagem 1: Lembre-se ainda que a rotina não contempla os processos, regras ou integrações com APS (Advanced Planning and…](https://ajuda.sankhya.com.br/hc/article_attachments/18496182392727) Lembre-se ainda que a rotina não contempla os processos, regras ou integrações com APS (Advanced Planning and Scheduling), criação de cenários ou planejamento de recursos, sendo este a mão de obra, além de não considerar saldos de outros MPS.

**Importante:** essa tela será apresentada somente se existir na licença o opcional **"30.426 - Programação de O.P/W"**.

| [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#configuraes) | [Utilizando a Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#utilizandoarotina) |
| --- | --- |
| [Falta de Capacidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#faltadecapacidade) | [Centro de Trabalho Indisponível](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#centrodetrabalhoindisponvel) |
| [Conflitos de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#conflitosdeatividades) | [Outras Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#outrasaes) |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#Par%C3%A2metrosqueinfluenciamestarotina) |  |

## Configurações

Será necessário realizar algumas configurações antes de se iniciar o uso deste rotina. Trataremos abaixo a descrição de cada uma delas:

#### Centro de Trabalho

O Centro de Trabalho é uma estrutura capaz de executar as atividades de um processo produtivo. A estrutura pode ser composta por máquinas, pessoas e equipamentos. Logo, se torna necessário cadastrar na tela [Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793) todos os centros de trabalho da planta que se deseja executar a programação de produção.

![Imagem 2: O Centro de Trabalho é uma estrutura capaz de executar as atividades de um processo produtivo. A estrutura pode ser…](https://ajuda.sankhya.com.br/hc/article_attachments/6952286160919)

---

#### Carga Horária

A Carga Horária determina os dias e horários que um Centro de Trabalho se encontra disponível para uso, assim como os dias e horários de funcionamento de uma Planta de Manufatura. Deste modo, as diversas cargas horárias devem ser definidas na tela [Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118133) e associadas aos Centros de Trabalhos e plantas de manufatura.

**Importante:** ao configurar um dia da semana, caso os campos **"Entrada turno"** e **"Saída turno"** não sejam preenchidos, na geração da programação da produção o sistema irá considerar esse dia e preencherá automaticamente a Entrada turno como 00:00 e a Saída turno como 23:59.

**Observação:** é possível configurar a carga horária com uma **"Saída turno"** menor que a **"Entrada turno"**. Nessas situações a carga horária excedente será considerada como carga horária do próximo dia da semana. Como por exemplo, se a carga horária de segunda-feira for definida das 21:00 às 02:23, será considerado que segunda-feira será das 21:00 às 23:59 e terça-feira das 00:00 às 02:23.

![Imagem 3: Observação: é possível configurar a carga horária com uma "Saída turno" menor que a "Entrada turno" . Nessas situações…](https://ajuda.sankhya.com.br/hc/article_attachments/6952275381655)

---

#### Alocação Centro de Trabalho

Temos por Alocações de Centros de Trabalho de um Processo Produtivo, a maneira de se definir a necessidade de uso de Centros de Trabalho por atividades de um Processo Produtivo. Por meio destas alocações, é possível tornar a seleção do Centro de Trabalho o mais tarde possível, pois a definição pode acontecer por Categoria de Centros de Trabalho, e no momento da programação um Centro disponível pertencente a referida categoria será selecionado.

Após a definição das diversas alocações na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo), aba [Alocações de Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#abaalocaodecentrosdetrabalho), é necessário vincular as mesmas nas atividades através do campo **"Alocação de C. Trabalho"** localizado na tela Processo Produtivo, [Configurações de Atividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674), aba Geral.

---

#### Tempo de processamento

O tempo de processamento corresponde ao tempo gasto para processar o produto na Atividade. Este tempo deve ser definido levando em consideração o lote padrão, podendo possuir "quebra" por quantidade (para quantidade diferente do lote padrão é feita uma regra de três para encontrar o tempo da quantidade desejada) ou por lote (para quantidades diferente do lote padrão utiliza-se uma vez o tempo para cada fração menor ou igual ao lote padrão). A definição de tempo poderá ocorrer de forma genérica ou especifica por Produto Acabado e Centro de Trabalho. Elas são configuradas nos seguintes lugares:

- Genérica:

![Imagem 4: Genérica:](https://ajuda.sankhya.com.br/hc/article_attachments/6952375841815)

- Específica:

![Imagem 5: Específica:](https://ajuda.sankhya.com.br/hc/article_attachments/6955383560343)

---

#### Sequência de execução

O valor definido no campo **"Sequência de execução"** (Configuração da Atividade, aba Geral) determina a ordem de execução das atividades, ou seja, determina o fluxo do processo.

---

#### Tamanho de Lote OP igual ao Lote Padrão

A opção **"Tamanho de Lote OP igual ao Lote Padrão"** localizada na tela Planejamento de Produção (MRP I), permite definir se as OPs geradas pela programação de produção terão seu tamanho igual ao saldo à produzir ou igual ao lote padrão do produto.

![Imagem 6: A opção "Tamanho de Lote OP igual ao Lote Padrão" localizada na tela Planejamento de Produção (MRP I) , permite definir…](https://ajuda.sankhya.com.br/hc/article_attachments/6954463015831)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)

## Utilizando a Rotina

Tendo sido realizadas todas as configurações elencadas acima, você pode utilizar a rotina Programação Plano Mestre de Produção. O acesso à respectiva rotina é realizado através da tela [Planejamento de Produção (MPR I)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I-), basta que você se posicione em um MPS e selecione no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I-#outrasopes...) a opção **"Programação"**.

![Imagem 7: Tendo sido realizadas todas as configurações elencadas acima, você pode utilizar a rotina Programação Plano Mestre de…](https://ajuda.sankhya.com.br/hc/article_attachments/6954539431191)

Um pop-up será aberto solicitando que seja selecionada uma opção de programação, sendo que, cada uma delas executará as seguintes funcionalidades:

- **Carregar programação:** essa opção carrega a programação já existente e caso seja necessário gera novas OPs considerando apenas o saldo pendente dos produtos (saldo a produzir);
- **Excluir e iniciar nova programação:** quando selecionada essa opção, ocorre a exclusão das OPs em programação (Aguardando programação e Em programação), e em seguida são geradas novamente OPs a serem programadas considerando o novo saldo pendente dos produtos (saldo a produzir).

![Imagem 8: Excluir e iniciar nova programação: quando selecionada essa opção, ocorre a exclusão das OPs em programação (Aguardando…](https://ajuda.sankhya.com.br/hc/article_attachments/6954576446615)

Note que ambas as opções lidam com Ordens de Produção, ou seja, neste momento os itens do MPS são transformados em OPs que serão utilizadas na programação da produção. As OPs criadas recebem um status específico (Aguardando Programação) visível e utilizável apenas por esta rotina. A prioridade dos itens do MPS é utilizada como ordem para a geração das OPs.

Ao selecionar a opção desejada, o sistema irá abrir a tela Programação Plano Mestre de Produção, sendo composta por uma grade em sua parte superior onde são apresentadas todas as OPs a programar e um gráfico de Gantt na parte inferior. O gráfico de Gantt é dividido em recursos a esquerda (Centros de Trabalho da Planta de Manufatura do MPS) e um calendário à esquerda.

![Imagem 9: Ao selecionar a opção desejada, o sistema irá abrir a tela Programação Plano Mestre de Produção , sendo composta por…](https://ajuda.sankhya.com.br/hc/article_attachments/6954620152599)

Para iniciar a programação, selecione uma ou mais OPs na grade e acione o botão Programar.

A ação programar quebra a Ordem de Produção em Atividades e aloca cada uma em um Centro de Trabalho compatível e disponível. Cada OP programada recebe uma cor que facilita sua identificação tanto no calendário quanto na grade de OPs. Por fim, as ordens recebem status igual à **"Em programação"**.

[GIF animado: Imagem 10: A ação programar quebra a Ordem de Produção em Atividades e aloca cada uma em um Centro de Trabalho compatível e…](https://ajuda.sankhya.com.br/hc/article_attachments/6954659944343)

A seleção do Centro de Trabalho da Atividade, respeita sua definição de Alocações de Centro de Trabalho da seguinte forma:

- **Sugere CT Padrão (+OP no MPS):** sugere utilizar o Centro de Trabalho configurado como **"Padrão"**, priorizando o Centro de Trabalho padrão da **"Composição do Produto"**. Caso esse não esteja disponível, deve-se recorrer ao Centro de Trabalho padrão da **"Categoria de CT"** da alocação. Além disso, será permitido a edição de qualquer Centro de Trabalho pertencente à categoria.
- **Usar CT Padrão:** utiliza o Centro de Trabalho padrão da categoria associada à alocação, sendo que o usuário não pode alterar o Centro de Trabalho utilizado.
- **Na inclusão manual da O.P:** indique o Centro de Trabalho disponível da categoria vinculada à alocação. A edição é permitida para qualquer Centro de Trabalho dentro dessa categoria.
- **Especificar CT:** utilize o Centro de Trabalho relacionado à alocação. O usuário não poderá alterar o Centro de Trabalho em uso.

É valido ressaltar que o sistema utiliza a sequência de execução das Atividades para definir a ordem de execução de cada atividade da OP.

As atividades pertencentes a Ordens de Produção Em programação podem ter seu Centro de Trabalho alterado. Para isso basta clicar e segurar sobre a atividade, arrastar até a linha referente ao Centro de Trabalho desejado e soltar. Sendo que, a atividade poderá mudar de tamanho, pelo fato de que os novos equipamentos podem possuir eficiência diferente do anterior.

Outra alteração possível sobre as atividades Em programação, é a data/hora de execução da mesma. Essa mudança pode ser realizada arrastando a atividade na linha correspondente ao Centro de Trabalho ou a partir do botão **"Alterar data da atividade"**.

[GIF animado: Imagem 11: Outra alteração possível sobre as atividades Em programação , é a data/hora de execução da mesma. Essa mudança pode ser…](https://ajuda.sankhya.com.br/hc/article_attachments/6954727636503)

Após confirmar a edição na data/hora da atividade, é apresentado o pop-up **"Confirmação"** para indicar se serão movimentadas outras atividades da OP proporcionalmente à movimentação executada na Atividade. As opções disponíveis são:

- **Todas:** todas as atividades serão movimentadas proporcionalmente na direção em que a atividade foi movimentada;
- **Apenas posteriores:** apenas as atividades sucessoras à Atividade serão movimentadas proporcionalmente na direção em que a Atividade foi movimentada;
- **Nenhuma:** nenhuma atividade será movimentada além da atividade movimentada por você.

![Imagem 12: Nenhuma: nenhuma atividade será movimentada além da atividade movimentada por você.](https://ajuda.sankhya.com.br/hc/article_attachments/6954750388887)

Ao finalizar a programação do MPS, ou seja, após alocação das atividades das Ordens de Produção do MPS em seus respectivos Centros de Trabalho e horário de execução, é necessário confirmar a programação. A confirmação da programação é uma forma de firmar o arranjo realizado que bloqueia a edição futura e que disponibiliza as OPs por consequência ao chão de fábrica.

As Ordens de Produção que tiveram sua programação confirmada, recebem o status Programado e são apresentadas na tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) podendo assim serem inicializadas pelo líder de produção. Uma vez iniciada, a OP deixa de ser apresentada na grade de OPs a serem programadas, recebe uma coloração **cinza** no gráfico e se torna bloqueada para reprogramação, ou seja, não volta ao status Em programação.

O resultado da programação das atividades de um MPS servirá de base para os operadores e poderá ser visualizado na [Fila de Operações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119253) por cada Centro de Trabalho. Uma vez confirmada a programação de uma ordem, a sua reprogramação poderá ser realizada somente na referida tela por meio da edição de prioridades.

**Nota:** para realizar o caso em que duas atividades estejam no mesmo centro de trabalho sendo realizadas na mesma data/hora, deve-se alterar as suas datas iniciais manualmente.

É possível também gerar uma programação Plano Mestre de Produção para produtos configurados em processos produtivos com [Gateways](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793-Bot%C3%A3o-Roteiro#gateways) do tipo **"Exclusivo"** em ordens de produção nos Centros de Trabalho e, ter uma estimativa da conclusão desta produção. Para isso, ao realizar a Programação para os produtos com Gateways Exclusivo que tiverem fluxos prioritários definidos, o sistema apresentará uma mensagem informando que a programação de produção poderá não refletir a realidade da produção e questionará se a programação deverá ser ou não gerada:

- Clicando em **"SIM"**, a OP será programada de acordo com o fluxo definido como Prioritário, desconsiderando os demais fluxos;
- Ao optar por **"NÃO"**, a programação não será realizada.

![Imagem 13: Ao optar por "NÃO" , a programação não será realizada.](https://ajuda.sankhya.com.br/hc/article_attachments/13237521106583)

Contudo, ao realizar esta Programação para produtos com Gateways do tipo Exclusivo, mas, que não tenha nenhum fluxo posterior definido como Prioritário, será exibida a seguinte mensagem:

**"O Processo Produtivo XXXX, Versão X, está configurado com gateway do tipo "Exclusivo" e nenhum fluxo após o gateway foi definido como "Prioritário". É necessário que um fluxo seja definido como prioritário para realizar a programação."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)

## Falta de Capacidade

A falta de capacidade da Planta de Manufatura dado o MPS em questão, pode ser percebida ao efetuar a programação de uma Ordem de Produção. Sendo que, caso não exista disponibilidade de recurso (Centro de Trabalho) para alocação de alguma das atividades da OP a seguinte mensagem é apresentada:

**"Não foi possível programar a Atividade <nome da atividade> do Processo produtivo <nome do processo> versão X na Ordem Y no Centro de Trabalho <nome do centro de trabalho> com o tempo de Z minutos porque não existe mais data disponível para programação."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)

## Centro de Trabalho Indisponível

A indisponibilidade do Centro de Trabalho é apresentada no gráfico de Gantt como se fosse uma atividade na data e hora programada contendo a coloração **amarela**. Apenas os registros de indisponibilidade cuja situação seja igual à Pendentes, são considerados pela Programação do Plano Mestre de Produção.

![Imagem 14: A indisponibilidade do Centro de Trabalho é apresentada no gráfico de Gantt como se fosse uma atividade na data e hora…](https://ajuda.sankhya.com.br/hc/article_attachments/6954905546775)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)

## Conflitos de Atividades

Os conflitos entre atividades são apresentados no gráfico de Gantt como um contorno na cor **vermelha** nas atividades conflitantes e podem acontecer em dois tipos situações:

- **Execução simultânea de Atividades:** uma atividade sucessora da atividade está sendo executada antes de sua finalização. Como as atividades são sequenciais, faz sentido uma segunda atividade ser iniciada somente após a finalização da atividade antecessora.
- **Execução simultânea no Centro de Trabalho:** duas ou mais atividades estão sendo executadas ao mesmo tempo em um Centro de Trabalho cujo tipo de operação seja Exclusivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)

## Outras Ações

Existem outras ações além das descritas até aqui, que você será capaz de realizar. Algumas destas ações, se aplicam sobre as Ordens de Produção da grade de Ordens a serem programadas, são elas:

- **Modificar prioridade:** cada OP gerada a partir do MPS possui sua prioridade, que é utilizada para determinar a ordem de programação quando esta ação é comandada para mais de uma ordem ao mesmo tempo. O sistema utiliza a ordem crescente, ou seja, as OPs de menor valor em prioridade são programadas antes daquelas de maior valor. Deste modo, você pode modificar a prioridade de uma OP para baixo ou para cima e salvar a mesma.

![Imagem 15: Modificar prioridade: cada OP gerada a partir do MPS possui sua prioridade, que é utilizada para determinar a ordem de…](https://ajuda.sankhya.com.br/hc/article_attachments/6955088624407)

- **Refazer programação:** é possível solicitar que o sistema refaça a programação de todas as OPs selecionadas na grade de ordens a programar. Esta ação consiste em excluir a programação existente para as OPs e gera-las novamente levando em consideração o mesmo princípio da ação programar. A reprogramação pode ser executada clicando sobre o botão **"Refazer Programação"**.

![Imagem 16: Refazer programação: é possível solicitar que o sistema refaça a programação de todas as OPs selecionadas na grade de…](https://ajuda.sankhya.com.br/hc/article_attachments/6955116291735)

Outras ações podem ser executadas por meio de botões e filtros presentes na barra superior de ações do gráfico de Gantt. Estas ações têm por objetivo modificar o resultado da programação ou melhorar a usabilidade do gráfico:

- **Remover todos:** possibilita desfazer a programação de todas as OPs Em programação do MPS, ou seja, remover estas OPs do gráfico.
- **Mostrar dependências:** todas as atividades de uma Ordem de Produção possuem vínculo de dependência entre si (predecessora x sucessora). Essas dependências também existem entre OP de PA e PI. Elas são representadas no gráfico por setas de ligação entre as atividades que podem ou não ser apresentadas conforme definição do filtro Mostrar dependências.
- **Apresentação de OPs:** é possível apresentar todas as OPs programadas para serem executadas nos Centros de Trabalhos no período do MPS ou apenas as OPs do MPS. Deste modo é possível evitar programações conflitantes no Centro. A ação é realizada por meio do filtro Ordens de produção.
- **Desfazer movimentação:** essa ação permite realizar o estorno de edições indevidas ou erradas.
- **Maximizar gráfico:** maximiza o gráfico de modo a melhorar a usabilidade do mesmo para edições manuais.

![Imagem 17: Maximizar gráfico: maximiza o gráfico de modo a melhorar a usabilidade do mesmo para edições manuais.](https://ajuda.sankhya.com.br/hc/article_attachments/6955190277015)

Por fim, mas não menos importantes, existem as ações que podem ser comandadas a partir de uma atividade pertencente a uma ordem Em programação ou Programado. Estas ações podem ser comandadas por meio de botões presentes no quadro Informações da Atividade apresentado ao posicionar o cursor sobre a atividade. As possíveis ações são:

- **Excluir a Ordem de Programação de Produção:** ao clicar sobre este botão, a OP será removida da programação da produção e volta a ser uma ordem Aguardando programação.
- **Enviar para o fundo:** em situações onde várias Atividades/OPs são executadas ao mesmo tempo no Centro de Trabalho, essa ação permite mover graficamente a Atividade/OP selecionada para o fundo.
- **Enviar para a frente:** quando várias Atividades/OPs são executadas ao mesmo tempo no Centro de Trabalho, essa ação possibilitará a movimentação gráfica da Atividade/OP selecionada para a frente.
- **Alterar o status da Ordem para Em Programação:** esta ação é possível apenas sob uma atividade de OPs cuja programação esteja confirmada, permite também voltar uma ordem Programada para a situação de Em programação de modo a permitir sua edição.

[GIF animado: Imagem 18: Alterar o status da Ordem para Em Programação: esta ação é possível apenas sob uma atividade de OPs cuja programação…](https://ajuda.sankhya.com.br/hc/article_attachments/6955237799319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)

## Parâmetros que influenciam esta rotina

**Considera OPs pendentes no lançamento de OP pelo MPS - CONSQTDOPMPS:** no processo de planejamento, o usuário escolhe um dos produtos e cria uma Ordem de Produção (OP) para esse produto e seu Produto Intermediário (PI). Posteriormente, ao gerar uma OP para o segundo produto, se o parâmetro estiver desativado, o sistema criará a OP apenas para o Produto acabado (PA) e não para o PI. Por outro lado, se o parâmetro estiver ativado, o sistema gerará a OP tanto para o PA quanto para o seu PI, pois nesse caso o sistema não identifica para qual PA a ordem de produção do PI foi gerada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598374-Programa%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-baseadas-no-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS#top)
