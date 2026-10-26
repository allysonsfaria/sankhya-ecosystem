---
id: "360044611534"
titulo: "Programação de Carga"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:26:03Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Planejamento", "Central de Vendas", "Previsto", "TOP", "Produção", "Programação de Carga", "br.com.sankhya.prod.mov.planejamento.producao", "Programação de Carga manual", "Demanda", "Distribuição"]
---

# Programação de Carga

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311900908823) Módulo: Comercial > Rotinas > Produção
```

---

![Imagem 2: Esta tela foi criada de forma personalizada para atender demandas exclusivas de um parceiro Sankhya .](https://ajuda.sankhya.com.br/hc/article_attachments/18201183057303) Esta tela foi criada de forma personalizada para atender demandas exclusivas de um parceiro **Sankhya**.

Ela exibe a demanda de produção em função de um período, permitindo também a distribuição dessa demanda conforme os compromissos junto aos clientes e a capacidade produtiva. Dessa forma, você pode ter uma visão apurada sobre a situação da indústria no momento atual e em um futuro próximo.

Assim, trataremos neste artigo sobre os seguintes tópicos:

[Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#configura%C3%A7%C3%B5esiniciais)                                            [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#paineldefiltros)

[Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#bot%C3%B5esnotopodatela)                                          [Totalizadores do rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#totalizadoresdorodap%C3%A9) 

## Configurações Iniciais

Antes da utilização desta tela, na tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), a partir de um pedido de venda, provisiona-se a entrega item a item, podendo ainda dividir a entrega de um item, seguindo a necessidade do cliente. Para lançar esta previsão, será utilizado a opção [Provisionar Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#provisionarentrega), da tela Central de Vendas , [Grade Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), menu [Outras opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es).

Ao clicar no sinal (+), e inserir as informações de **"quantidade"** e **"data prevista"**, estas serão gravadas após pressionar o botão **"Gravar Provisão"**. Para que este botão fique disponível, toda a quantidade do item deve ser atendida, e um totalizador mostrará o saldo do item no rodapé para facilitar a distribuição.

![clip0383](https://ajuda.sankhya.com.br/hc/article_attachments/360061021914)

Uma vez confirmado o pedido, o sistema gera planejamentos de produção (conforme configuração da TOP), que são os registros visualizados na tela de Programação de Carga e serão a base do Romaneio de carga (etapa seguinte a esse processo). Cada item da previsão será convertido em um planejamento, e nesse momento a matéria-prima necessária para elaborar o produto será empenhada para o mesmo. Isso servirá para determinar quanto de matéria-prima estará comprometida em determinado período (o empenho não é sinônimo de reserva de estoque).

**Observação:** para que o registro de Planejamento de Produção seja gerado nessa tela, é preciso que a marcação **"Gerar plano de produção"** da aba [Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaproduo) localizada na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) seja acionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#top)

## Painel de Filtros

Na tela de Programação de Carga, inicialmente informe os dois filtros de preenchimento obrigatório, que são, **"Empresa"** e o **"Período Previsto de Entrega"**. A empresa é a mesma informada no cabeçalho do pedido na Central de Vendas; já o período, é o período no qual foi feita a provisão de entrega do item na Central de Vendas.

![clip0384](https://ajuda.sankhya.com.br/hc/article_attachments/360061940793)

Além dos dois campos de preenchimento obrigatório, você pode informar os demais campos, afim de restringir e/ou refinar a pesquisa.

Na seção **"Situação"**, temos as seguintes alternativas:

- **Todas:** Retorna todas as notas que estão provisionadas para entrega;
- **Com ordem de Produção:** Retorna todas as notas que estão provisionadas para entrega com ordem de produção;
- **Sem ordem de Produção:** Retorna todas as notas que estão provisionadas para entrega sem ordem de produção.

**Período de planejamento:** Informe aqui, a data que abrange o planejamento de entrega.

**Incluir não planejados:**Com esta marcação efetuada, serão incluídas as notas provisionadas que não estão planejadas para entrega.

Na seção **"Pedido"**, são apresentados quatro campos que possibilitam a busca direta por um determinado pedido, que são:

- **Número:** Número do pedido de venda;
- **Cliente:** Busque pelo parceiro para o qual o pedido foi lançado;
- **Cidade:** Cidade que está sendo programado a entrega;
- **UF:** Unidade Federativa para a qual está sendo programado a entrega.

Você pode também realizar as seguintes marcações na seção **"Outros filtros"**:

**Previsões atrasadas ainda não planejadas:** quando efetuada, esta marcação irá trazer as previsões realizadas que ainda não estão planejadas para a produção da mesma.

**Apenas com planejamento atrasado:** Quando assinalada esta marcação, incluirá apenas as cargas com produção em atraso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#top)

## Botões no topo da tela

Preenchidos os filtros desejados, informe na parte superior da grade, os campos **"Dt. carregamento"** e **"Capacidade Produtiva"**; estas duas informações não estão rigidamente vinculadas a programação, servindo apenas para fortalecer as informações sobre a programação e sugerir a data de planejamento no momento da edição. Em seguida, clique no botão **"Aplicar"**; serão apresentados na grade, os planejamentos que obedecem aos filtros criados.

Você pode agrupar as cargas por pedido, através do botão **"Agrupar por pedido"**, localizado na parte superior da grade.

Dê dois cliques sobre um dos planejamentos, assim será aberta uma pequena tela, onde são informadas a **"Quantidade planejada"**, a **"Data do planejamento"**, a **"Transportadora"**, a **"Ordem"** (sequencia de produção), a **"Fórmula"** de composição do produto e alguma **"Observação"** desejada.

![clip0386](https://ajuda.sankhya.com.br/hc/article_attachments/360061021934)

A quantidade a ser planejada, é apresentada no topo dessa janela, seguida do saldo remanescente (Qtd. Original - Vlr informado no campo Qtd. Plan). Ao informar a quantidade planejada, se o campo Dt Plan. ainda não estiver informado, o sistema automaticamente o preenche com a data do carregamento. O processo inverso também acontece, ou seja, ao informar a Dt Plan., se estiver vazio o campo Qtd. Plan, o sistema preenche automaticamente com a quantidade total.

**Importante:** na edição de um registro, se existir uma **"Qtd. Remanescente"** no momento da finalização (botão **"Salvar alteração"**) a quantidade será alterada para o valor planejado e uma cópia do registro será criada instantaneamente levando a quantidade restante, que deverá ser planejada posteriormente.

Quando o registro estiver corretamente editado, o botão Salvar alteração, que será habilitado, deve ser pressionado. Neste momento, a edição ainda não foi gravada no banco de dados, e o botão **"Confirmar"** que ficará habilitado, é o responsável por realizar esta gravação de fato. Portanto, até que este botão seja acionado, os dados podem ser alterados e a reaplicação do filtro refeita.

O próximo passo será utilizar o botão **"Liberar..."**. que apresenta quatro alternativas de escolha:

- **Lib. Logística (item selecionado):** Faz a liberação para a Logística, apenas do item selecionado;
- **Lib. Logística (todos c/ planej.):** Realiza a liberação para a Logística de todos os itens com planejamento;
- **Lib. Produção (item selecionado):** Efetua a liberação para a Produção, apenas do item selecionado;
- **Lib. Produção (todos c/ planej.):** Realiza a liberação para a Produção de todos os itens com planejamento.

![clip0387](https://ajuda.sankhya.com.br/hc/article_attachments/360061021954)

---

![Imagem 7: Informações adicionais referentes à geração da Programação de Carga:](https://ajuda.sankhya.com.br/hc/article_attachments/18848946443031)**Informações adicionais referentes à geração da Programação de Carga:**

- Se o item da nota na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) possuir o campo **"Variação da Fórmula"** da grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414#gradedeitens) vazio junto ao parâmetro **"Seleciona variação de fórmula no portal de vendas? - SELVARFOR"** desativado, é preciso cadastrar a fórmula utilizada na tela [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154) do item da nota com o **"Produto"**, junto às informações do seu **"Local Padrão"** e Controle, ambos localizados no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), para os itens que possuem provisionamento de entrega para que, assim, na confirmação da nota, seja gerada a programação de carga. Porém, caso a fórmula não seja devidamente cadastrada, ao gerar a programação o sistema exibirá a mensagem:

**"A variação da fórmula deve ser informada para o produto [DESCRICAOPRODUTO, CONTROLE, LOCAL]."**

- Entretanto, se o campo Variação da Fórmula estiver vazio e o parâmetro SELVARFOR ligado, será exibida a mensagem:

**"A variação da fórmula deve ser informada para o produto xxx."**

- Por fim, com o campo Variação da Fórmula preenchido e o parâmetro SELVARFOR ligado ou desligado, é necessário que o cadastro da fórmula referente ao item da nota seja realizado nos campos **"Produto"**, **"Local"**, **"Controle"** e **"Variação"** da tela [Fórmula de Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414) conforme o Produto, **"Local origem"**, Controle do produto e Variação da Fórmula da Central de Vendas para aqueles itens que possuírem o provisionamento de entrega. Desse modo, ao confirmar a nota será gerada a programação de carga.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#top)

## Totalizadores do rodapé

Os valores exibidos nos itens abaixo, são obtidos a partir das linhas da grade, representando, portanto, a situação vista na tela e não valores absolutos. Assim, você poderá obter as seguintes informações:

- **Atrasado:** Itens com data prevista antes da data atual e sem planejamento definido;
- **Previsto para a data:** Itens cuja data de planejamento está prevista para a data carregamento;
- **Planejado atrasado:** Itens planejados antes da data atual que ainda não foram produzidos;
- **Planejado na data:** Soma dos itens planejados para a data de carregamento;
- **Planejado futuro:** Soma dos itens planejados para depois da data de carregamento;
- **Atrasado + Data:** Somatório entre Planej. atrasado e Planej. na data;
- **A Planejar:** Total dos itens que ainda não foram planejados;
- **Saldo Capacidade Produtiva:** Apresenta a informação preenchida no campo "Capacidade produtiva" apresentado na parte superior da tela.

#### Campos adicionais

Se necessário, o consultor Sankhya pode incluir campos de outras tabelas para fornecer informações extras nesse processo (desde que estes campos sejam de tabelas que já estejam envolvidas neste processo). Para definir novos campos o parâmetro **"Campos adicionais visíveis no planej. de produção - CAMPOSADPLPROD"** deve ser utilizado, onde o nome dos campos são separados por virgula, por exemplo, NotaOrigem.CODREG, NotaOrigem.Regiao.NOMEREGIAO.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611534-Programa%C3%A7%C3%A3o-de-Carga#top)
