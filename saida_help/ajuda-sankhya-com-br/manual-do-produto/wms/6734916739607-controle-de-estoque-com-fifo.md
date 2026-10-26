---
id: "6734916739607"
titulo: "Controle de Estoque com FIFO"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:17:09Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Preferências", "Controle de Estoque com FIFO", "FIFO", "WMSVALREGWMSPRO", "FIFO: Primeiro a entrar primeiro a sair", "Configurações prévias necessárias", "Controle eficiente de estoque"]
---

# Controle de Estoque com FIFO

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311613217303) Versão disponível: A partir da 4.11
```

---

O método FIFO é um sistema de armazenagem que trabalha conforme a sequência da entrada de mercadorias no estoque, sempre priorizando o despacho daqueles lotes que chegaram primeiro. Como diz o nome **"First In First Out"**, o primeiro que entra é o primeiro que sai; dessa forma, é possível ter um maior controle de armazenagem.

O FIFO estipula a rotação de mercadorias e faz movimentar e ordenar a saída dos produtos, para que aquele que está há mais tempo no estoque saia primeiro, seja qual for o produto: um insumo, uma matéria-prima, uma mercadoria ou produtos acabados.

Além disso, esse sistema determina a ordem de saída dos lotes, ou seja, o primeiro que chega ao estoque também será o primeiro a sair. Sendo assim, nas filas constituídas por essa categoria de sistema, os produtos serão comercializados por ordem de chegada.

Dessa forma é possível ter um controle de estoque mais assertivo, assegurando uma atualização constante do estoque, não deixando os produtos "envelhecerem" ou ultrapassarem a sua data de recebimento.

---

**Essa documentação aborda os seguintes tópicos:**

| [Configurações necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#configura%C3%A7%C3%B5esnecess%C3%A1rias) |
| --- |
| [Como realizar o Controle de Estoque com FIFO](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#comorealizarocontroledeestoquecomfifo) |

---

#### Configurações necessárias

Para usar a estratégia de FIFO, é necessário que você faça algumas configurações prévias, sendo elas:

Primeiramente, na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), habilite o parâmetro **"Validar 'REGRA DO WMS' do produto? - WMSVALREGWMSPRO"**.

Em seguida, no [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms), configure o campo **"Atualização Data Rec. no WMS"** da TOP de acordo com as opções abaixo:

- **Não Atualiza:** A data do recebimento fica igual à "vazio" quando for feito um recebimento no WMS.
- **Diário:** A data do recebimento fica igual à data do dia, possibilitando a armazenagem dos produtos em um mesmo endereço, desde que sejam recebidos na mesma data.
- **Semanal:** A data do recebimento fica igual à data do domingo, da semana do recebimento. Sendo possível a armazenagem dos produtos em um mesmo endereço, apenas os recebidos dentro da semana.
- **Mensal:** Com essa opção, a data do recebimento fica igual ao primeiro dia do mês do recebimento, possibilitando a armazenagem dos produtos recebidos dentro do mês em um mesmo endereço.

![Imagem 2: Mensal: Com essa opção, a data do recebimento fica igual ao primeiro dia do mês do recebimento, possibilitando a…](https://ajuda.sankhya.com.br/hc/article_attachments/6766621665943)

Após isso, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms), configure o campo **"Regra de WMS"** com a opção **"FIFO"**:

![Imagem 3: Após isso, no Cadastro de Produtos , aba WMS , configure o campo "Regra de WMS" com a opção "FIFO" :](https://ajuda.sankhya.com.br/hc/article_attachments/6766636261527)

Por fim, a [Configuração de Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234-Configura%C3%A7%C3%A3o-de-Armazenagem) deve ser definida de forma que a regra de picking não seja a primeira a ser executada pois, em endereços de picking não será registrada a **"Dt. Recebimento"**. Mantendo a regra de picking depois das demais, evitamos que a mercadoria de um novo recebimento seja armazenada nos pickings dos produtos recebidos e mantemos o estoque antigo nos endereços de pulmão:

![Imagem 4: Por fim, a Configuração de Armazenagem deve ser definida de forma que a regra de picking não seja a primeira a ser…](https://ajuda.sankhya.com.br/hc/article_attachments/6766692707351)

Feitas as configurações acima, o WMS passará a realizar as movimentações verticais respeitando a estratégia de FIFO, ou seja, nas operações em que forem movimentadas mercadorias do pulmão para o endereço de picking, sempre será movimentado o produto com a menor Dt. Recebimento. E nas movimentações entre endereços de pulmão, o sistema irá validar se a Dt. Recebimento entre os endereços permite realizar a operação para não misturar datas diferentes.

---

```
                                                                                               ![Imagem 5: Feitas as configurações acima, o WMS passará a realizar as movimentações verticais respeitando a estratégia de FIFO ,…](https://ajuda.sankhya.com.br/hc/article_attachments/42311613218071)

Os endereços de picking não irão registrar a Dt. Recebimento pois, nesses endereços ocorrerão
mistura de datas devido ao fluxo de movimentações (reabastecimento, armazenagem e etc)
ocorrido durante as operações.
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#top)

---

#### Como realizar o Controle de Estoque com FIFO

Agora que já foram realizadas as configurações necessárias, você já pode iniciar o Controle de Estoque com FIFO na prática. Abaixo demonstramos como é feito o processo para cada tipo de operação:

| ![Imagem 6: Agora que já foram realizadas as configurações necessárias, você já pode iniciar o Controle de Estoque com FIFO na…](https://ajuda.sankhya.com.br/hc/article_attachments/42311613219991) | ![Imagem 7: Agora que já foram realizadas as configurações necessárias, você já pode iniciar o Controle de Estoque com FIFO na…](https://ajuda.sankhya.com.br/hc/article_attachments/42311613220247) | ![Imagem 8: Agora que já foram realizadas as configurações necessárias, você já pode iniciar o Controle de Estoque com FIFO na…](https://ajuda.sankhya.com.br/hc/article_attachments/42311613221015) | ![Imagem 9: Agora que já foram realizadas as configurações necessárias, você já pode iniciar o Controle de Estoque com FIFO na…](https://ajuda.sankhya.com.br/hc/article_attachments/42311613221655) | ![Danificar grátis ícone](https://cdn-icons-png.flaticon.com/512/1739/1739833.png) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| [Recebimento e Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#recebimentoearmazenagem) | [Transferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#transfer%C3%AAncia) | [Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#invent%C3%A1rio) | [Expedição e Reabastecimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#expedi%C3%A7%C3%A3oereabastecimento) | [Endereços Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#endere%C3%A7osespeciais) |

|  |
| --- |

| ![Imagem 11: Endereços Especiais](https://ajuda.sankhya.com.br/hc/article_attachments/42311613223447) |
| --- |

---

**Recebimento e Armazenagem**

A entrada/registro da Dt. Recebimento no estoque do produto é realizado no [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias), sempre considerando a data para cálculo a **"Dt. Conferência"**. Considere o exemplo abaixo:

**Recebimento:** **10**

      **Dt. de Envio da NF p/ Recebimento:** **13/06/2022**

      **Dt. Conferência:** **14/06/2022**

Com as seguintes configurações da TOP de acordo com os dados acima:

- **Não atualiza: Dt. Recebimento vazia**
- **Diário: Dt. Recebimento 14/06/2022**
- **Semanal: Dt. Recebimento 12/06/2022 (domingo da semana)**
- **Mensal: Dt. Recebimento 01/06/2022 (primeiro dia do mês)**

Após ser realizada a conferência de todos os produtos e ser feito o envio da conferência no Coletor de Dados pelas tarefas **"Registro de Conferência"** ou **"Conferência de Entrada"**, o sistema registrará o estoque (tela [Estoque / Endereçamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS)) na Doca com a Dt. Recebimento para todos os itens conferidos:

![Imagem 12: Após ser realizada a conferência de todos os produtos e ser feito o envio da conferência no Coletor de Dados pelas…](https://ajuda.sankhya.com.br/hc/article_attachments/6789192983831)

A Dt. Recebimento irá acompanhar o produto em todas as movimentações realizadas no WMS, tendo seu fim somente quando o estoque do produto/endereço zerar.

Após registrar a Dt. Recebimento na conferência, o próximo passo é realizar a Armazenagem da mercadoria, lembrando de configurar as opções **"Completar Endereços"** ou **"Endereços vazios"** primeiro na hierarquia.

Caso seja configurado Endereços vazios primeiro, o WMS sempre priorizará a armazenagem dos produtos em endereços vazios, não sendo necessária a análise de mistura de Dt. Recebimento.

Se for configurada a regra Completar Endereços primeiro, o WMS buscará endereços que já possuam o produto porém, não estão com o percentual de completude em 100%. Sendo assim, quando for identificado um endereço para completar, o sistema avalia se já existe uma Dt. Recebimento diferente da atual; caso exista uma data no possível endereço, o produto será enviado para um endereço vazio.

No processo de Armazenagem, existem algumas ações manuais que possibilitam o operador escolher o endereço de armazenagem, portanto, caso ele tente realizar uma movimentação para endereços que já possua uma Dt. Recebimento diferente da data do endereço de destino, o sistema realizará a validação abaixo:

[GIF animado: Imagem 13: No processo de Armazenagem , existem algumas ações manuais que possibilitam o operador escolher o endereço de…](https://ajuda.sankhya.com.br/hc/article_attachments/6791384228119)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#comorealizarocontroledeestoquecomfifo)

---

**Transferência**

Nos Centros de Distribuição é comum que os gerentes de logística e operadores realizem transferências entre endereços, para otimizar espaço no armazém, tirando produtos que não estão ocupando um endereço em sua completude e enviando para endereços que já possuam estoque, aproveitando 100% de sua capacidade.

A transferência entre endereços também é utilizada para atender outros tipos de manutenção de estoque. Hoje, no WMS, temos algumas rotinas e tarefas que possibilitam que o operador/gestor realizem essas movimentações e agora, com o controle de estoque com FIFO. Observa abaixo as rotinas, tarefas e aplicações:

**Tarefa no Coletor - Movimentação Pró-Ativa**

A Movimentação Pró-Ativa é uma tarefa/recurso que permite realizar transferências entre endereços. Esse recurso do coletor não depende de outras rotinas para geração das tarefas, ficando a critério do operador a retirada da mercadoria de um endereço para transferir para um outro destino.

Com o Controle de Estoque com FIFO, as seguintes regras referente à Dt. Recebimento são observadas:

- Caso o Endereço de Origem possua registro de Dt. Recebimento porém o Destino não possui, será registrada no Destino a Dt. Recebimento do Endereço de Origem.
- Se o Endereço de Origem e Destino não tiverem registro da Dt. Recebimento, será registrada no Destino a menor Dt. Recebimento lançada (qualquer endereço com o produto/controle); se não for encontrada, será registrada a Dt. Recebimento com a data atual (dia da movimentação).
- Se o Endereço de Origem não possui Dt. Recebimento e o Destino possui registro, será mantida a Dt. Recebimento do Endereço de Destino.
- Caso o Endereço de Origem e Destino possuam Dt. Recebimento porém datas diferentes, o sistema realizará a validação, não deixando misturar estoque de Dt. Recebimento diferentes:

[GIF animado: Imagem 14: Caso o Endereço de Origem e Destino possuam Dt. Recebimento porém datas diferentes, o sistema realizará a validação,…](https://ajuda.sankhya.com.br/hc/article_attachments/6845742345239)

- Se o Endereço de Origem e Destino possuírem a mesma Dt. Recebimento, ou a data está dentro da semana ou mês de recebimento, o sistema irá permitir a movimentação e a validação será feita conforme a configuração da TOP.

---

**Transferência entre Endereços**

A movimentação entre endereços possibilita que a equipe de controle de estoque faça alterações no layout do armazém de maneira rápida e simples e agora com a estratégia de FIFO, serão aplicadas as mesmas regras que descrevemos acima.

Aqui também, caso o Endereço de Origem e Destino possuam Dt. Recebimento porém datas diferentes, o sistema realizará a validação, não deixando misturar estoque de Dt. Recebimento diferentes:

[GIF animado: Imagem 15: Aqui também, caso o Endereço de Origem e Destino possuam Dt. Recebimento porém datas diferentes, o sistema realizará a…](https://ajuda.sankhya.com.br/hc/article_attachments/6845745955479)

---

**Remanejamento de Estoque**

Para um melhor aproveitamento do espaço físico de um armazém, é necessário realizar um remanejamento de estoque nos endereços de pulmão, ou seja, fazer uma análise para identificar quais produtos não estão ocupando o espaço total do endereço. Com o Controle de Estoque com FIFO, o sistema valida as regras para manter em estoque os produtos mais novos e dar vazão aos mais antigos. Aqui serão observadas as mesmas regras descritas na [Tarefa Movimentação Pró-Ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#tarefanocoletor-movimenta%C3%A7%C3%A3opr%C3%B3-ativa).

Se o Endereço de Origem e Destino possuírem Dt. Recebimento porém datas diferentes, o sistema realizará a validação para não deixar misturar estoque de Dt. Recebimento diferentes:

[GIF animado: Imagem 16: Se o Endereço de Origem e Destino possuírem Dt. Recebimento porém datas diferentes, o sistema realizará a validação…](https://ajuda.sankhya.com.br/hc/article_attachments/6845747554967)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#comorealizarocontroledeestoquecomfifo)

---

**Inventário**

No processo de Inventário, o sistema verifica a regra de FIFO no momento do Ajuste de Estoque através da tela [Ajuste de Estoque por Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Ajuste-de-Estoque-por-Invent%C3%A1rio).

Nos endereços inventariados em que o estoque lógico for igual à 0 e a contagem de estoque for maior do que 0, o sistema registrará a menor data em estoque (será feita a busca da menor data em outros endereços para o produto/controle). Caso não tenha registro, o sistema registra a data atual para o endereço inventariado. Por exemplo:

- **Produto:** **10**
- **Endereço:** **01.01.01**
- **Estoque atual:** **0**
- **Quantidade contada:** **100 UN**

Com o seguinte estoque do produto em outros endereços de pulmão:

- **Endereço: 01.01.02  Estoque: 100  Dt. Recebimento: 01/05/2022**
- **Endereço:** **01.01.03Estoque:** **100Dt. Recebimento:** **05/05/2022**

Ajuste de estoque:

- **Endereço: 01.01.01  Estoque: 100  Dt. Recebimento: 01/05/2022 (menor data encontrada)**

O sistema irá manter a data já existente para os endereços que tiveram a contagem com sobra e que possuem estoque e registro de Dt. Recebimento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#comorealizarocontroledeestoquecomfifo)

---

**Expedição e Reabastecimento**

O processo de reabastecimento é o ato de transferir mercadorias de um endereço de pulmão para um endereço de coleta (picking). Esse processo é fundamental para o armazém pois é uma das funções que mais impacta diretamente na realização de outros processos, como exemplo, na separação de um pedido, na expedição, etc.

Com o FIFO, o WMS passa a reabastecer os endereços de picking com o produto mais antigo em estoque de pulmão, mantendo produtos novos em estoque, evitando avarias e perdas.

A estratégia de FIFO será aplicada nas operações abaixo:

- **Reabastecimento Corretivo:** Gerado no envio da onda e para recomposição de estoque após o registro de ocorrências na separação.
- **Reabastecimento Preventivo:** Gerado no momento em que o estoque do picking atinge o estoque mínimo ou menor que o mínimo.
- **Ressuprimento Preventivo:** É gerado de forma manual e o sistema sempre irá sugerir a menor Dt. Recebimento.

Em todas as operações citadas acima, o WMS pegará o endereço de pulmão com a menor Dt. Recebimento para abastecer o endereço de picking com a quantidade completa do pulmão; caso um endereço de pulmão não seja suficiente, o sistema diminui estoque do pulmão com a próxima "menor data" de recebimento.

**Operação de Separação**

Na operação de separação, o FIFO será aplicado apenas no tipo **"Separação Pulmão"**. Nessa operação, o sistema solicitará a separação no pulmão/palete com a menor Dt. Recebimento, mantendo produtos mais novos nos demais endereços de pulmão.

Durante as operações de separação, pode acontecer de algumas separações terem suas tarefas canceladas por motivos comerciais ou outros motivos em que a venda do pedido que está **"Em separação"** não será mais efetuada . Nesse processo, o WMS gera uma tarefa de retorno de estoque para os endereços de origem.

Quando separado no pulmão, o sistema gera a tarefa de retorno tendo o Endereço de Origem o configurado como **"Retorno de Expedição cancelada"** para o endereço de pulmão e, quando a separação for feita no endereço de picking, será utilizado o mesmo processo porém o Endereço de Destino é o endereço de picking.

Nesse cenário podemos ter o mesmo produto em mais de um pedido/separação cancelado. O retorno desse(s) produto(s) é para o pulmão (em caso de separação pulmão), registrando a menor Dt. Recebimento encontrada em estoque; caso não seja identificada, será registrada a data atual (data do retorno).

**Observação:** essa busca de data é feita devido os endereços de doca e retorno de expedição não registrarem a Dt. Recebimento.

Em caso de retorno para os endereços de picking, o sistema não registra Dt. Recebimento pois nesses endereços não tem o registro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#comorealizarocontroledeestoquecomfifo)

---

**Endereços Especiais**

Os Endereços Especiais são aqueles utilizados para controle de **"Avaria"**, **"Divergência"**, **"Perda"** e **"Sobra"**. Todos esses endereços passarão a ter Dt. Recebimento registrada nas movimentações durante as operações.

Esses endereços podem receber diferentes Dt. Recebimento para o mesmo produto, sendo assim, sempre será registrada no estoque a primeira Dt. Recebimento para o produto/controle.

Nos Endereços Especiais temos dois que permitem retorno do saldo de estoque, sendo a Divergência e a Avaria. O retorno pode ser feito para endereços de picking e pulmão e seguirá as regras do FIFO conforme descrito abaixo:

- Caso o Endereço de Origem possua registro de Dt. Recebimento porém o Destino não possui, será registrada no Destino a Dt. Recebimento do Endereço de Origem.
- Se o Endereço de Origem e Destino não tiverem registro da Dt. Recebimento, será registrada no Destino a menor Dt. Recebimento lançada (qualquer endereço com o produto/controle); se não for encontrada, será registrada a Dt. Recebimento com a data atual (dia da movimentação).
- Se o Endereço de Origem não possui Dt. Recebimento e o Destino possui registro, será mantida a Dt. Recebimento do Endereço de Destino.
- Caso o Endereço de Origem e Destino possuam Dt. Recebimento porém datas diferentes, o sistema realizará a validação, não deixando misturar estoque de Dt. Recebimento diferentes:

[GIF animado: Imagem 17: Caso o Endereço de Origem e Destino possuam Dt. Recebimento porém datas diferentes, o sistema realizará a validação,…](https://ajuda.sankhya.com.br/hc/article_attachments/6851947654039)

- Se o Endereço de Origem e Destino possuírem a mesma Dt. Recebimento, ou a data está dentro da semana ou mês de recebimento, o sistema irá permitir a movimentação e a validação será feita conforme a configuração da TOP.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#comorealizarocontroledeestoquecomfifo) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO#top)
