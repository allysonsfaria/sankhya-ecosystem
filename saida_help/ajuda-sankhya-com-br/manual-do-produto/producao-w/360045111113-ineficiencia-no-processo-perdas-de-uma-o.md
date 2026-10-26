---
id: "360045111113"
titulo: "Ineficiência no Processo (perdas de uma Ordem de Produção)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:28Z"
rotulos: ["AJUDA DO SKW", "Custos", "Configuração", "Último", "Ineficiência no Processo (perdas de uma Ordem de Produção) manual", "Apontamento", "Ordem de Produção", "Estoque", "Produção", "Quebras desregulagens erros", "Cálculo perdas estoque", "Consumo refugo subproduto", "Refugo"]
---

# Ineficiência no Processo (perdas de uma Ordem de Produção)

Durante a execução das atividades de uma OP podem acontecer falhas operacionais, como a quebra de uma máquina, um equipamento desregulado, um erro do operador, entre outras. Grande parte das vezes as falhas reduzem a quantidade de Produto Acabado que será gerado ao final da produção. Em algumas indústrias principalmente devido à natureza do produto fabricado, as falhas operacionais dão origem a um produto defeituoso, classificado como perda/refugo podendo este consumir matérias-primas.

O fato da perda/refugo consumir materiais, está diretamente relacionado à necessidade deste item entrar no estoque recebendo sua parte do custo da produção que lhe originou.

Apresentaremos a seguir o caso de uso de uma indústria Têxtil (segmento de vestuário), responsável pela fabricação do produto "Blusa" com geração de refugos ao longo do processo.

Assim, abordaremos neste artigo, os seguintes tópicos:

| [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#casodeuso) |  | [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#configura%C3%A7%C3%B5es) |
| --- | --- | --- |
| [Execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#execu%C3%A7%C3%A3o) |  | [Cálculo para consumo dos materiais por refugo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#c%C3%A1lculoparaconsumodosmateriaisporrefugo) |
| [Último apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#%C3%BAltimoapontamento) |  |  |

### Caso de Uso

O processo produtivo deste produto é realizado por meio de duas atividades, sendo elas o Corte e a Costura.

![Imagem 1: O processo produtivo deste produto é realizado por meio de duas atividades, sendo elas o Corte e a Costura .](https://ajuda.sankhya.com.br/hc/article_attachments/4416570961943)

Em função de alguma ineficiência na operação, sabemos que ao longo dessa produção pode acontecer do produto sair fora do padrão aceitável pela indústria, ocasionando assim perdas/refugo na produção. No caso dessa indústria que estamos utilizando como exemplo, todas as atividades estão sujeitas a geração desses refugos.

Na atividade de Corte, em função de uma desregulagem da máquina é possível que ocorra um corte indesejado do tecido, resultando assim em um tecido fora dos padrões aceitos pela equipe de qualidade. Esses tecidos que fogem do padrão de qualidade são refugados e vendidos como "Retalho".

Como esses subprodutos (refugos) gerados por esse processo são vendidos, se faz necessário que seja apropriado o custo dos materiais gastos nesta produção. Além disso, como a comercialização desses itens refugados não se dará da mesma forma que o produto principal, os estoques desses refugos são direcionados para um local especial utilizado pela indústria, para que os estoques dos produtos principais não se misture com os produtos secundários.

Já na atividade de Costura, a blusa em seu formato ideal/desejado é onde acontece de fato a costura do tecido. Aqui, por um descuido também é possível que o tecido sofra uma alteração na costura, resultando em uma blusa fora dos padrões aceitos pela equipe de qualidade. Essas blusas que fogem do padrão de qualidade, são vendidas no outlet da indústria, para isto se faz necessário que seja apropriado o custo dos materiais gastos nessa produção.

A seguir apresentaremos, as configurações necessárias para atender o processo descrito desta indústria na geração destes refugos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#top)

### Configurações

Nas atividades Corte e Costura ([Botão Roteiro - Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades), aba [Produtos (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa), sub-aba [Lista de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistademps), sub-aba **"Material"**) foram inseridas as matérias-primas necessárias para fabricação do produto "Blusa" e como estas precisam ser consumidas pelo custo aos refugos gerados, a marcação **"Material consumido por refugo"** deverá ser acionada.

- Material consumido por refugo da atividade Corte:

![Imagem 2: Material consumido por refugo da atividade Corte:](https://ajuda.sankhya.com.br/hc/article_attachments/4416675279639)

- Material consumido por refugo da atividade Costura:

![Imagem 3: Material consumido por refugo da atividade Costura:](https://ajuda.sankhya.com.br/hc/article_attachments/4416675392535)

Conforme o cenário descrito, as perdas geradas na atividade de Corte serão representadas por um produto diferente do PA (Retalho), já na atividade de Costura será gerado o próprio PA como refugo (Blusa).

Para que o refugo seja considerado por um produto diferente do PA, é necessário cadastrar um subproduto na sub-aba [Lista de Subprodutos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistadesubprodutos) da atividade, com a opção **"Subproduto por Perda/Refugo"** acionada. Deste modo, evidencia-se que o subproduto em questão irá representar os refugos gerados nesta atividade.

![Imagem 4: Para que o refugo seja considerado por um produto diferente do PA, é necessário cadastrar um subproduto na sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4416675443351)

Defina no campo **"Subproduto"**, o produto que será gerado ao apontar a perda.

Indique no campo **"Quantidade"**, a quantidade que será gerada do subproduto (refugo) em relação à quantidade (unidade) apontada de perda. Sendo assim, a quantidade gerada do refugo será igual à "Qtd. Perda" multiplicada pela "Quantidade" definida neste campo.

Informe no campo **"Unidade"**, a unidade de medida a ser utilizada para o subproduto (refugo).

Ao acionar a marcação **"Subproduto por Perda/Refugo"**, indicará que o subproduto se trata de perda/refugo, onde os subprodutos serão consequências das perdas geradas. É importante lembrar que os subprodutos marcados com essa opção não devem ser apontados na atividade, pois sua origem é reflexo do apontamento de perda.

Na atividade de Corte, o campo Quantidade foi preenchido com 1 unidade, ou seja, para cada unidade do PA apontada como perda, será gerada 1 unidade do subproduto "Retalho".

Para dar entrada no estoque de refugo, é necessário configurar uma operação de estoque específica em cada atividade que pode gerar refugo. O [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado nesta operação de estoque deverá ser do tipo de movimento **"F - Produção"**.

Neste exemplo, foi cadastrado nas atividades de Corte e Costura (no caso da atividade Costura foi cadastrada duas operações de estoque, sendo uma para gerar a nota de refugo e outra para gerar a nota de produção, visto que se trata da última etapa do processo).

![Imagem 5: Neste exemplo, foi cadastrado nas atividades de Corte e Costura (no caso da atividade Costura foi cadastrada duas…](https://ajuda.sankhya.com.br/hc/article_attachments/4416675469591)

Determine no campo **"Quando"** o momento em que a operação de estoque será gerada, no caso da nota de refugo deve ser **"Ao apontar PA"**. Isso significa que o documento será gerado ao confirmar o apontamento com perda.

No campo **"Modelo de nota"** informe um modelo de nota a ser utilizado na operação de estoque.

Indique no campo **"Tipo de Operação para Perda"** a TOP que será utilizada na operação de estoque, caso não seja informado o sistema irá utilizar a TOP do modelo de nota. Sendo que, apenas TOP's do tipo de movimento **"F - Produção"** podem ser utilizadas.

Informe no campo **"Local de destino para Perda"**, o local de destino para as perdas geradas na atividade.

**Observação:** os campos Tipo de Operação para Perda e Local de destino para Perda somente serão habilitados quando o campo **"Tipo dos Itens"** estiver definido com a opção **"Subproduto da Atividade"**.

Aponte em **"Local para baixa de MPs"**, o local para baixa das matérias-primas consumidas pelo refugo.

Determine no campo **"Tipo dos Itens"**, os itens que serão movimentados, no caso da nota de refugo é necessário que este campo esteja definido com a opção **"Subproduto da Atividade"**.

| **Atenção aos detalhes de implementação:**   - **Lançamento da OP:** Se o tipo de lote for "Manual", o sistema apresentará um passo adicional chamado **"Subprodutos"** durante o lançamento da OP para que o usuário informe o lote manualmente. - **Geração de Datas:** Caso a base de cálculo seja a "Data da Primeira nota de produção", as datas de validade/fabricação só serão visíveis no Resumo PA após o primeiro apontamento realizado na tela **Operações de Produção**. |
| --- |

### Rastreabilidade e controle de lote para Subprodutos

Para que o sistema realize o controle de rastreabilidade dos subprodutos (como o "Retalho" ou a "Blusa" de outlet), gerando corretamente o **Número do Lote**, **Data de Fabricação** e **Data de Validade**, é indispensável realizar as configurações abaixo na tela **Processo Produtivo**:

- **Utilizar essa configuração para Subproduto:** Esta marcação é **obrigatória**. Quando acionada, ela garante que o subproduto tenha sua própria inteligência de lote e validade, desvinculando-o do produto principal.
- **Tipo de Nro. de Lote:** Define se a numeração será "Automática" ou "Manual".
- **Base para cálculo para Dt. Validade:** Configuração realizada na tela **Composição do Produto** para determinar se as datas serão calculadas a partir da "Data de Inicialização da OP" ou da "Data da Primeira nota de produção do lote".

> **Importante:** se a opção **"Utilizar essa configuração para Subproduto"** não estiver marcada, o sistema não preencherá as datas de fabricação e validade. Nesses casos, qualquer número de lote que venha a aparecer no subproduto é apenas uma herança do lote do Produto Acabado (PA) principal, o que não caracteriza um controle de estoque correto para o subproduto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#top)

### Execução

Neste exemplo, tem-se o lançamento de uma OP para produzir 100 UN do produto Blusa. Durante a atividade de Corte ocorreu uma desregulagem na máquina de corte, ocasionando uma perda de 30 unidades. Sendo assim, foi apontada uma **"Qtd Perda"** igual à 30.

![Imagem 6: Neste exemplo, tem-se o lançamento de uma OP para produzir 100 UN do produto Blusa. Durante a atividade de Corte…](https://ajuda.sankhya.com.br/hc/article_attachments/4416679040535)

Ao confirmar o apontamento com perda, o sistema gera a nota de refugo contendo os subprodutos por Perda/Refugo e as matérias-primas consumidas por refugo. Esta nota pode ser visualizada na tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o), aba [Notas de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o#abanotasdeproduo).

> Os dados de rastreabilidade (Lote e Validade) configurados anteriormente podem ser conferidos na tela Ordens de Produção, através do popup "Resumo PA", clicando no botão "Visualizar Subprodutos". Ali, será exibido um grid com o número do lote, data de validade e data de fabricação de cada subproduto gerado.

![Imagem 7: Os dados de rastreabilidade (Lote e Validade) configurados anteriormente podem ser conferidos na tela Ordens de…](https://ajuda.sankhya.com.br/hc/article_attachments/4416668984855)

De acordo com o resultado da atividade Corte, está previsto para serem processadas 70 UN de "Blusa" na atividade Costura. Entretanto, durante a execução desta tarefa (Costura) o operador (costureira) cometeu alguns erros que ocasionaram a perda de 5 UN do produto. Logo, esta perda foi apontada no sistema (tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274)) pelo operador na atividade.

![Imagem 8: De acordo com o resultado da atividade Corte, está previsto para serem processadas 70 UN de "Blusa" na atividade…](https://ajuda.sankhya.com.br/hc/article_attachments/4416675899543)

Ao confirmar o apontamento com perda, o sistema gera a nota de refugo contendo os subprodutos por Perda/Refugo e as matérias-primas consumidas por refugo.

![Imagem 9: Ao confirmar o apontamento com perda, o sistema gera a nota de refugo contendo os subprodutos por Perda/Refugo e as…](https://ajuda.sankhya.com.br/hc/article_attachments/4416679590295)

Ao confirmar o apontamento com perda, o sistema também gera a nota de produção contendo o produto acabado Blusa e os materiais gastos na produção.

![Imagem 10: Ao confirmar o apontamento com perda, o sistema também gera a nota de produção contendo o produto acabado Blusa e os…](https://ajuda.sankhya.com.br/hc/article_attachments/4416676016535)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#top)

### Cálculo para consumo dos materiais por refugo

O sistema executa regra de três para dividir a quantidade apontada dos materiais consumidos por refugo, entre o produto acabado e a perda gerada na atividade. Analisemos abaixo:

**Atividade Corte**

Qtd. Apontada = 70 UN (70% da quantidade total apontada)

Qtd. Perda = 30 UN (30% da quantidade total apontada)

Qtd. Apontada "Seda" = 200 MT

Nota de refugo - Atividade Corte:

Qtd. Refugo ("Retalho") = 30UN

Qtd. Matéria-prima ("Seda") = 60 MT (30% de 200 MT apontados em Corte)

**Atividade Costura**

Qtd. Apontada = 65 UN (92,85% da quantidade total apontada)

Qtd. Perda = 5 UN (7,15% da quantidade total apontada na atividade Costura e 5% da quantidade total apontada na atividade Corte)

Qtd. Apontada "Linha" = 350 MT

**Nota de refugo - Atividade Costura**

Qtd. Refugo ("Blusas") = 5UN

Qtd. Matéria-prima ("Linha") =  25 MT (7,15 % de 350 MT apontados em Costura)

Qtd. Matéria-prima ("Seda") = 10 MT (5% de 200 MT apontados em Corte)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#top)

## Último apontamento

Ao confirmar um apontamento com a quantidade menor que o saldo restante em atividades geradoras de nota de produção, o sistema questionará se este será o último apontamento. Caso seja o último apontamento, é necessário executar os seguintes processos:

1. Lançar como perda no apontamento a diferença entre o saldo restante da atividade e quantidade apontada (automaticamente);
2. Baixar na nota de produção a quantidade restante de materiais (saldo restante) apontadas nas atividades anteriores.

Com base no processo de fabricação do produto Blusa apresentado anteriormente, na atividade de Costura está previsto costurar 70 blusas (esta gera nota de produção), nesta atividade é utilizada a MP "Linha", o qual é consumida por refugo. Ao apontar 65 unidades, o sistema verifica que a quantidade apontada é menor que o saldo restante:

![Imagem 11: Com base no processo de fabricação do produto Blusa apresentado anteriormente, na atividade de Costura está previsto…](https://ajuda.sankhya.com.br/hc/article_attachments/4416686362263)

Desta forma, ao clicar em confirmar, será apresentada a seguinte mensagem:

**"Este será o último apontamento? Caso este seja o último apontamento, diferença de quantidade será considerada com perda para estes produtos/controles."**

Neste cenário, ao confirmar que a diferença será tratada como perda, o sistema proporcionaliza a quantidade de MP (linha) apontada para o total de PAs bons e ruins. O consumo da matéria-prima "Linha" sairá na nota de refugo e produção por ser um material consumido por refugo, caso esta matéria-prima não fosse consumida por refugo sairia apenas na nota de produção com a quantidade total consumida.

Então para este caso, o sistema realiza os seguintes cálculos (utilizando regra de três):

- Quantidade prevista de PA: 70 unidades;
- Quantidade apontada de PA: 65 unidades;
- Quantidade apontada da MP (Linha): 325 Metros;
- Quantidade de perda de PA (lançada automaticamente pelo sistema): 5 unidades.

Desta forma, 325 metros da MP foi utilizado para realizar o total de 70 PAs, então para produzir os 65 PAs em bom estado foram consumidos 302 metros de MP (nota de produção) e para fazer os 5 PAs ruins foram gastos 23 metros da MP (nota de refugo).

**Importante:** ao confirmar o último apontamento, se os materiais apontados nas atividades anteriores não forem consumidos por refugos, o sistema contemplará na nota de produção a quantidade prevista a ser produzida. Segue o exemplo:

Em uma Ordem de Produção prevendo a produção de 100 unidades de blusas, foram realizados os seguintes apontamentos:

![Imagem 12: Em uma Ordem de Produção prevendo a produção de 100 unidades de blusas, foram realizados os seguintes apontamentos:](https://ajuda.sankhya.com.br/hc/article_attachments/4416581289495)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111113-Inefici%C3%AAncia-no-Processo-perdas-de-uma-Ordem-de-Produ%C3%A7%C3%A3o#top)
