---
id: "360044611094"
titulo: "Apropriação de Custos Indiretos de Produção (CIP)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611094-Apropria%C3%A7%C3%A3o-de-Custos-Indiretos-de-Produ%C3%A7%C3%A3o-CIP"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:52:30Z"
rotulos: ["AJUDA DO SKW", "manual", "Custos", "CUSTODEC", "Configuração", "Requisições", "Financeiros", "Apropriação", "CIP", "Indiretos", "br.com.sankhya.caculo.de.custo.baseado.no.financeiro", "Apropriação de Custos Indiretos de Produção (CIP) manual", "Produção", "Financeiro", "Ajuste custos indiretos", "Atualização de custos", "Filtros financeiros"]
---

# Apropriação de Custos Indiretos de Produção (CIP)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312719201431) Módulo: Produção > Rotinas
```

---

Diretamente ligada à tela [Tarifas CIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025397373-Tarifas-CIP), esta tela realiza a adequação dos custos indiretos de produção. Os custos indiretos, são apropriados mediante o emprego de critérios pré-determinados (filtros financeiros, de requisições e lanç. contábeis) e vinculados a causas correlatas, como mão-de-obra e materiais indiretos, gastos com energia, entre outros.

![Imagem 2: Diretamente ligada à tela Tarifas CIP , esta tela realiza a adequação dos custos indiretos de produção. Os custos…](https://ajuda.sankhya.com.br/hc/article_attachments/360061281694)

Na parte superior esquerda da tela, estão disponíveis os campos para filtro, **"Empresa"**, **"Custo p/ base de cálculo"** (que pode ser definido como **"Gerencial"** ou **"Reposição"**), **"Período p/ atualização do custo"** (temos as opções **"Produção"** e **"Pós Produção"**) e **"Períodos para filtrar OPs"**.

O campo **"Data p/ atualização do custo"** é apenas informativo e demonstra em qual data o custo das tarifas será atualizado. Seu valor irá variar em função da configuração realizada nos campos Período para filtrar OPs e Período p/ atualização do custo, sendo que:

- Se o campo Período p/ atualização do custo estiver configurado como **"Produção"**, a data será igual à data inicial do Período para filtrar OPs;
- Estando ele configurado com a opção **"Pós Produção"**, a data será igual à data final do Período para filtrar OPs somando um dia.

Temos também os **"Filtros para Financeiros"**, **"Filtros para Requisições"** e **"Filtros para Lanç. Contábeis"**:

![Imagem 3: Temos também os "Filtros para Financeiros" , "Filtros para Requisições" e "Filtros para Lanç. Contábeis" :](https://ajuda.sankhya.com.br/hc/article_attachments/360061281754)

Nestes espaços, podemos utilizar dos filtros criados nas telas [Filtro para cálculo CIP (Financeiros)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025241694-Filtro-para-c%C3%A1lculo-CIP-Financeiros-), [Filtro para cálculo CIP (Requisições)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392773-Filtro-para-c%C3%A1lculo-CIP-Requisi%C3%A7%C3%B5es-) e [Filtro para cálculo CIP (Lanç. Contábeis)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025233654-Filtro-para-c%C3%A1lculo-CIP-Lan%C3%A7-Cont%C3%A1beis-), respectivamente.

Estes filtros possuem funcionalidades restritivas, ou seja, quando não forem configurados, serão exibidas todas as tarifas CIP's que estiverem utilizando os mesmos.

![Imagem 4: Estes filtros possuem funcionalidades restritivas, ou seja, quando não forem configurados, serão exibidas todas as…](https://ajuda.sankhya.com.br/hc/article_attachments/360062197253)

Além disto, ao configurar somente um dos filtros, o sistema apresentará as tarifas CIP's vinculadas ao mesmo, bem como, as tarifas que estiverem relacionadas aos demais filtros.

**Observação:** caso queira agregar os CIP's no produto será necessário realizar a criação de dois filtros com o mesmo Centro de Resultado por meio da tela Filtro para cálculo CIP (Financeiros), sendo um para cada empresa. Com isso, ao apropriar os custos, deve-se selecionar o filtro de acordo com a empresa que se deseja filtrar os financeiros.

A opção do menu **"Outros"**, apresenta a marcação **"Usar parâmetro CUSTODEC p/ arredondamento"** que, quando assinalada, definirá o número de casas decimais dos custos exibidos na tela.

Para isto, o parâmetro **"Decimais para custo - CUSTODEC"** deve ter sido previamente configurado com a quantidade de casas decimais desejadas na rotina. A quantidade de casas decimais definida neste parâmetro, influenciará também no arredondamento de valores.

O sistema buscará os produtos de acordo com os filtros definidos nos campos acima.

Os custos serão calculados pelo valor líquido dos títulos no financeiro.

Ao clicar em **"Calcular"**, o sistema exibirá na grade os produtos com os respectivos custos antigos e os novos custos apurados, baseados nos financeiros.

Por meio dos botões ![Imagem 5: Por meio dos botões "Remover selecionados" e "Remover selecionados" , você determina quais produtos terão ou não seus…](https://ajuda.sankhya.com.br/hc/article_attachments/360063804653) **"Remover selecionados"** e ![Imagem 6: Por meio dos botões "Remover selecionados" e "Remover selecionados" , você determina quais produtos terão ou não seus…](https://ajuda.sankhya.com.br/hc/article_attachments/360063804693) **"Remover selecionados"**, você determina quais produtos terão ou não seus custos atualizados, mantendo ou retirando estes da tela.

Clicando em **"Atualizar Custos"**, o sistema atualizará o último custo do produto para os novos custos calculados

Localizado abaixo da grade onde os produtos são apresentados, temos um painel totalizador de registros formado pelos seguintes campos:

**Total Qtd. x Custo Anterior:** É apresentado aqui, o custo de consumo das tarifas considerando o custo anterior, ou seja, o somatório da multiplicação entre quantidade consumida e custo anterior das tarifas (custo antes da atualização). Esse é considerado o custo previsto das tarifas para o período em questão.

**Total Valor Financeiro:** Este campo exibe o valor total dos financeiros (Vlr. do Desdobramento) que foram considerados para formação do novo custo das tarifas. Para as tarifa geradas a partir de requisições, será considerado o **"Vlr. Nota"**.

**Total Dif. Prev. x Real:** Temos neste campo, a diferença entre o valor valor previsto real das tarifas.

**Total Dif. em %:** Este campo traz o % (percentual) da diferenciação total (todas as tarifas) entre o custo previsto e custo real.

![Imagem 7: Total Dif. em %: Este campo traz o % (percentual) da diferenciação total (todas as tarifas) entre o custo previsto e…](https://ajuda.sankhya.com.br/hc/article_attachments/360062197773)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611094-Apropria%C3%A7%C3%A3o-de-Custos-Indiretos-de-Produ%C3%A7%C3%A3o-CIP#top)
