---
id: "4417442682903"
titulo: "Divergências de Estoque WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:16:50Z"
rotulos: ["Configuração", "Inventário", "WMS", "Estoque", "Divergências", "Divergências de Estoque WMS", "Inconsistência de data de validade", "Inconsistência de estoque", "br.com.sankhya.wms.DivergenciasWMS", "Configurações e Ajustes", "Tipos de Divergência", "Análise de Divergências"]
---

# Divergências de Estoque WMS

| ``` ![Imagem 1: Módulo: WMS > Inventário Versão disponível: A partir da 4.11](https://ajuda.sankhya.com.br/hc/article_attachments/42311609914391) Módulo: WMS > Inventário                     ![Imagem 2: Módulo: WMS > Inventário Versão disponível: A partir da 4.11](https://ajuda.sankhya.com.br/hc/article_attachments/42311609915159) Versão disponível: A partir da 4.11 ``` |
| --- |

---

Esta tela possui acesso restrito a analistas de suporte, administradores do sistema, gestores de operação de estoque de armazém. Com o intuito de auxiliar no diagnóstico das divergências de estoque do WMS são apresentadas nesta tela, duas categorias de análise que podem ser ajustadas:

- Inconsistência de data de validade;
- Inconsistência de estoque.

Desse modo, trataremos os seguintes tópicos neste artigo:

| [![Imagem 3: Desse modo, trataremos os seguintes tópicos neste artigo:](https://ajuda.sankhya.com.br/hc/article_attachments/42311637430167)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#Configura%C3%A7%C3%B5esdatela) |  | [![Imagem 4: Desse modo, trataremos os seguintes tópicos neste artigo:](https://ajuda.sankhya.com.br/hc/article_attachments/42311637430551)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#tiposdediverg%C3%AAncia) |
| --- | --- | --- |

---

### Configurações da tela

Primeiramente no Painel de Filtros, informe a **"Empresa"** para que sejam apresentados os registros que possuem divergência. Para refinar a busca, você pode informar também o **"Produto"**, um **"Complemento"**, a **"Faixa de Endereços"**, o número **"Lote (Controle)** e o **"Parceiro"**.

![Imagem 5: Primeiramente no Painel de Filtros , informe a "Empresa" para que sejam apresentados os registros que possuem…](https://ajuda.sankhya.com.br/hc/article_attachments/4417459532823)

Depois, para os casos de inconsistência de data de validade, configure por meio do botão ![Imagem 6: Depois, para os casos de inconsistência de data de validade, configure por meio do botão as "Preferências de ajuste do…](https://ajuda.sankhya.com.br/hc/article_attachments/16841600447895) as **"Preferências de ajuste do WMS"**. Ao acioná-lo, será exibido um pop-up, onde você pode habilitar uma das seguintes opções:

- Seleciona a última data de validade conferida no Recebimento;
- Faz o cálculo da Data de Validade por meio do Shelf Life (Cadastro do Produto): Data Atual + Shelf Life = Data de Validade.

Neste pop-up, defina também a cor de fundo da fonte para cada tipo de divergência. Como neste exemplo, em que para as divergências de data de validade, os registros serão apresentados na cor **azul**.

[GIF animado: Imagem 7: Neste pop-up, defina também a cor de fundo da fonte para cada tipo de divergência. Como neste exemplo, em que para as…](https://ajuda.sankhya.com.br/hc/article_attachments/4420111095575)

Com as configurações acima realizadas, serão exibidos na grade superior os **"Dados de Estoque do WMS"**. Selecionando uma linha nesta grade, na aba **"Data de Validade"** serão apresentados os registros de estoque por data de validade.

![Imagem 8: Com as configurações acima realizadas, serão exibidos na grade superior os "Dados de Estoque do WMS" . Selecionando uma…](https://ajuda.sankhya.com.br/hc/article_attachments/4419745695895)

Se o produto do registro selecionado, estiver com alguma tarefa em aberta pendente, será exibido na aba **"Tarefas Pendentes"**.

Agora, clique em ![Imagem 9: Agora, clique em "Gerar ajustes" para que o sistema verifique qual cenário de divergência se encontra o registro e…](https://ajuda.sankhya.com.br/hc/article_attachments/16841523476887) **"Gerar ajustes"** para que o sistema verifique qual cenário de divergência se encontra o registro e realize o processamento de ajuste conforme definição e parâmetros selecionados em tempo de execução. Assim, será apresentada a mensagem:

**"Será feito o ajuste dos Registros apresentados/selecionados na Grid. Deseja confirmar?"**

Clicando em **"Sim"**, será exibida as informações dos ajustes:

![Imagem 10: Clicando em "Sim" , será exibida as informações dos ajustes:](https://ajuda.sankhya.com.br/hc/article_attachments/4417467839767)

Clicando em **"Não"**, o processo será cancelado.

Com os ajustes realizados, você pode verificar o histórico de execuções, por meio do botão ![Imagem 11: Com os ajustes realizados, você pode verificar o histórico de execuções, por meio do botão "Histórico de Ajustes" .](https://ajuda.sankhya.com.br/hc/article_attachments/16841907746583) **"Histórico de Ajustes"**.

![Imagem 12: Com os ajustes realizados, você pode verificar o histórico de execuções, por meio do botão "Histórico de Ajustes" .](https://ajuda.sankhya.com.br/hc/article_attachments/4417467879703)

| ``` Dica: Agende os ajustes por meio do botão  "Realizar agendamento". Ao  acioná-lo, você será direcionado a tela Agendador Divergências de Estoque WMS. ``` |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#top)

---

### Tipos de divergência

Conforme mencionado, essa tela vai identificar dois tipos de divergências: Divergência de Estoque e Divergências de Data de validade. Para um melhor entendimento do que o sistema trata como divergência, vamos mencionar abaixo todos os cenários.

| [![Imagem 13: Conforme mencionado, essa tela vai identificar dois tipos de divergências: Divergência de Estoque e Divergências de…](https://ajuda.sankhya.com.br/hc/article_attachments/42311637431575)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#Diverg%C3%AAnciadeestoque) |  | [![Imagem 14: Conforme mencionado, essa tela vai identificar dois tipos de divergências: Divergência de Estoque e Divergências de…](https://ajuda.sankhya.com.br/hc/article_attachments/42311609919383)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#Diverg%C3%AAnciadedatadevalidade) |
| --- | --- | --- |

---

#### Divergência de Estoque

O WMS faz uma "contabilização" de todas as tarefas geradas através das Entradas e Saídas pendentes no estoque, ou seja, para todas as tarefas com status em **"Aberto"**, o sistema tem que identificar a saída de um endereço e entrada em um endereço de destino. 

**Entradas e Saídas Pendentes**

| ``` Cenário 1 ``` |
| --- |

Caso o sistema identifique que existem tarefas Abertas, porém, no sistema não existem saídas pendentes no endereço da tarefa e entradas pendentes no destino da tarefa, o sistema irá identificar como divergências.

**Correção:** Para este cenário, o sistema realizará a auditoria analisando o total de tarefas abertas para a Empresa, Produto, Lote e Endereço, em seguida, será efetuada a correção deixando as Entradas e Saídas, conforme a quantidade de tarefas com a situação **"Aberta"** ou **"Em andamento"**. Considere o exemplo a seguir:

- Produto: Cerveja Skol
- Tarefas em Aberta/Em andamento: 1
- Endereço de Origem: 01.01
- Endereço de Destino: 01.02
- Estoque Endereço: 01.01 | Est: 10UN | Saídas Pend:0| Será Ajustado para 1UN
- Estoque Endereço: 01.02 | Est: 1UN | Entradas Pend:0| Será Ajustado para 1UN

Essa situação pode ocorrer somente nas saídas, ou somente nas entradas, sendo que, para os dois casos a correção será a mesma.

| ``` Cenário 2 ``` |
| --- |

No momento da auditoria se o sistema identificar que existe Saídas e Entradas pendentes para Endereços, porém, não exista tarefas com a situação **"Aberta"** ou **"Em andamento"**, neste caso o sistema também vai apresentar a divergência.

**Correção:** Como não existem tarefas que justifiquem a saída e a entrada nos endereços com divergência, o sistema vai zerar ou subtrair a quantidade no estoque, deixando de acordo com a contabilização feita de tarefas realmente em aberto/em andamento. Por exemplo:

- Produto: Cerveja Skol
- Tarefas em Aberta/Em andamento: 0
- Endereço de Origem: 01.01
- Endereço de Destino: 01.02
- Estoque Endereço: 01.01 | Est: 10UN | Saídas Pend:1| Será Ajustado para 0UN
- Estoque Endereço: 01.02 | Est: 1UN | Entradas Pend:1| Será Ajustado para 0UN

| ``` Cenário 3 ``` |
| --- |

Existem casos em que o usuário pode realizar intervenções via banco de dados (não recomendado), nesse cenário essa intervenção pode excluir alguma linha de estoque que contenha Saídas ou Entradas pendentes, deixando assim o estoque com inconsistente. Desse modo, o sistema identificará essa situação na auditoria e aplicará a correção. Considere o seguinte exemplo:

- Estoque: 20UN | End: 01.01| Saídas Pend: 10UN| (estoque excluído via banco de dados)
- Estoque: 10UN | End: 01.02| Entrada.Pend: 10UN|(estoque excluído via banco de dados)

**Correção:** O sistema vai retornar o estoque, deixando igual a saídas pendentes e em caso de entradas pendentes, o sistema vai retornar a linha deixando o estoque zerado.

- Estoque: 10UN | End: 01.01| Saídas Pend: 10UN| (estoque excluído via banco de dados)
- Estoque: 0UN | End: 01.02| Entrada.Pend:10UN|(estoque excluído via banco de dados)

| ``` ![Imagem 15: É recomendado neste caso que após a correção, os endereços envolvidos na divergência sejam inventariados devido ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16841529153687) É recomendado neste caso que após a correção, os endereços envolvidos na divergência  sejam inventariados devido ao estoque inserido para atender a demanda das saídas pendentes. ``` |
| --- |

**Saídas Pendente maior que o Estoque**

Quando o sistema identificar no estoque que existe quantidade de Saídas pendentes de um Endereço maior que o estoque, então o sistema vai apresentar como divergência, pois na execução das tarefas essa situação pode retornar no coletor a seguinte mensagem:

**"Essa operação deixará o estoque negativo do endereço:X Produto:Y controle:W."**

| ``` ![Imagem 16: Neste caso, não existem entradas pendentes para cobrir as saídas pendentes, assim, o estoque não vai atender a…](https://ajuda.sankhya.com.br/hc/article_attachments/16841529153687)  Neste caso, não existem entradas pendentes para cobrir as saídas pendentes, assim, o estoque não vai atender a quantidade de saídas, gerando a divergência. ``` |
| --- |

Considere o seguinte exemplo desta situação:

- Produto: 10 |Endereço: 01.01 |Estoque: 10UN| Saídas Pen: 30|

**Correção:** Quando identificada essa inconsistência, o sistema vai igualar o estoque para a mesma quantidade de saídas pendentes, desse modo, a demanda será atendida e a operação será continuada, evitando assim, que a tarefa fique parada ou aguardando outro tipo de intervenção.

- Produto: 10 |Endereço: 01.01 |Estoque: 30UN| Saídas Pen: 30|

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#tiposdediverg%C3%AAncia)

---

#### Divergência de Data de Validade

O controle de Data de validade no WMS é feito por meio de duas tabelas: TGWEST (estoque) e TGWESTVAL (Tabela de data de validade). O controle de Data de validade é um controle que exige mais atenção e critério por parte do setor de Planejamento de Controle de Estoque - PCE, pois deve ter coerência com a quantidade de estoque com a distribuição das datas para o Produto e Lote.

Geralmente esse controle é realizado com um lote tendo apenas uma data, porém existem operações que são registradas na Produção mais de uma Data de validade para o mesmo Lote. Mediante a este contexto, temos algumas situações que o WMS vai realizar a auditoria e identificar algumas inconsistências no estoque com Dt. de validade, conforme os cenários abaixo:

| ``` Cenário 1 ``` |
| --- |

Para os produtos com Shelf Life configurado (tela [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abawms)), que possui estoque, porém, sem registro de Data de validade em ambas as tabelas, temos a seguinte correção:

**Correção:** Nesta tela (Divergências de Estoque WMS) temos a opção **"Preferências de ajuste do WMS"**, que contém duas estratégias para correção do estoque sem data, são elas:

- Seleciona a última data de validade conferida no Recebimento;
- Faz o cálculo da Data de Validade por meio do Shelf Life (Cadastro do Produto): Data Atual + Shelf Life = Data de Validade.

Com a estratégia definida, clique na opção de ajuste, desse modo, será registrada a data de validade no estoque, conforme a opção selecionada.

| ``` Cenário 2 ``` |
| --- |

Estoque do produto com Data de validade em somente uma das tabelas de estoque.

**Correção:** O sistema vai inserir a mesma data de validade existente em uma das tabelas, na tabela que não contêm o registro.

| ``` Cenário 3 ``` |
| --- |

Caso tenha divergência de quantidade entre as tabelas, o sistema irá aplicar a seguinte regra:

![Imagem 17: Caso tenha divergência de quantidade entre as tabelas, o sistema irá aplicar a seguinte regra:](https://ajuda.sankhya.com.br/hc/article_attachments/4420120501271)

| ``` Cenário 4 ``` |
| --- |

Caso tenha divergência somente entre as Datas de validade entre as tabelas.

**Correção:** O sistema irá considerar a Data de validade da tabela de Dt. validade como correta, e utilizará para ambas as tabelas.

---

![Imagem 18: Todas as situações tratadas nesta tela é visando uma melhor gestão da operação, evitando que essas situações impactem…](https://ajuda.sankhya.com.br/hc/article_attachments/16841529153687) Todas as situações tratadas nesta tela é visando uma melhor gestão da operação, evitando que essas situações impactem na produtividade dos operadores e dos usuários do WMS. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#tiposdediverg%C3%AAncia) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4417442682903-Diverg%C3%AAncias-de-Estoque-WMS#top)
