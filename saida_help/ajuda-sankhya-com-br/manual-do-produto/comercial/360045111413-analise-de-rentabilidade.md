---
id: "360045111413"
titulo: "Análise de Rentabilidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111413-An%C3%A1lise-de-Rentabilidade"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-25T15:35:51Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Rentabilidade", "Análise de Rentabilidade", "br.com.sankhya.com.cad.analiserentabilidade", "Análise de Rentabilidade manual", "Portal de Vendas", "Impostos", "Preferências", "Análise de rentabilidade", "Preferências de apresentação", "Configuração de dados", "Comercial"]
---

# Análise de Rentabilidade

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312036109975) Módulo: Comercial > Preferências 
```

---

Nesta tela são definas as preferências para a apresentação dos dados na Análise de Rentabilidade.

![Imagem 2: Nesta tela são definas as preferências para a apresentação dos dados na Análise de Rentabilidade .](https://ajuda.sankhya.com.br/hc/article_attachments/21463561846295)

Através do campo **"Intervalo de % (<)"** será possível adicionar o percentual de intervalo em que serão utilizadas as cores.

No campo **"Cor da Fonte"** selecione a cor da fonte que se deseja utilizar.

Indique no campo **"Cor de Fundo"** a cor de fundo a ser utilizada.

Por meio do campo **"Legenda"** informe uma legenda, se julgar necessário.

No campo **"Tipo"** selecione o tipo de preferência, dentre as opções:

- Lucro
- Margem de Contribuição

![Imagem 3: Margem de Contribuição](https://ajuda.sankhya.com.br/hc/article_attachments/21464022832279)

Em seguida, acione o botão ![Imagem 4: Em seguida, acione o botão "Salvar" para finalizar a configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/22235332214935) **"Salvar"** para finalizar a configuração.

### Utilização

As configurações aqui efetuadas irão surtir efeito na Análise da Rentabilidade das notas presentes no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454) através do botão  **"Mostrar Rentabilidade"**. Esta configuração será a **"legenda"** empregada em cada nota no Portal de Vendas.

Tem-se como exemplo, a criação de uma legenda com três intervalos diferentes do tipo **"Margem de Contribuição"** com a mesma cor de fonte e cores de fundo distintas:

![Imagem 5: Tem-se como exemplo, a criação de uma legenda com três intervalos diferentes do tipo "Margem de Contribuição" com a…](https://ajuda.sankhya.com.br/hc/article_attachments/21464244930967)

Acessando uma nota no Portal de Vendas e clicando no botão acima mencionado, será aberta a tela Análise de Rentabilidade referente à nota selecionada.

![Imagem 6: Acessando uma nota no Portal de Vendas e clicando no botão acima mencionado, será aberta a tela Análise de…](https://ajuda.sankhya.com.br/hc/article_attachments/21547643697559)

Observe abaixo o resumo acerca dos pontos da rentabilidade da nota:

- **Faturamento:** é o valor de faturamento do produto.
- **Custo da Mercadoria Vendida (CMV):** é baseado nas regras de cálculo de custo conforme a opção escolhida nas [Preferências do Gerente On-Line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line) (aba [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abamargemdecontribuio), campo **"Custo a ser considerado"**)
- **Gasto Variável (GV):** é todo gasto ou despesa que altera em proporção às vendas. É calculado da seguinte forma:

| ``` ![Imagem 7: Gasto Variável = Impostos - ST A Recuperar + OutrosGastos + Comissão](https://ajuda.sankhya.com.br/hc/article_attachments/42312052395287) Gasto Variável = Impostos - ST A Recuperar + OutrosGastos + Comissão ``` |
| --- |

Em que:

**Impostos** = abrange todos os impostos incidentes sobre a venda, como IPI, ICMS, PIS, COFINS, entre outros. Também inclui a tributação pertinente a contribuintes do Simples Nacional, quando aplicável.

**ST a recuperar** = este valor é customizável pela função no banco de dados SNK\_GET\_ST\_RECUPERAR(), seu valor padrão é 0 (zero);

**Outros gastos** = Embalagem + Frete + Juro + Destaque.

**Nota:** o cálculo de Gasto Variável pode ser ajustado com base nas opções de personalização.

**Importante:** o campo **"Considerar débito ICMS nas consultas gerenciais"**, presente no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), influencia na composição dos Gastos Variáveis. Quando a opção está marcada, o sistema irá considerar como débito o ICMS sobre o produto, refletindo no resultado da rentabilidade do item e da nota.

| ![informações](https://ajuda.sankhya.com.br/hc/article_attachments/42312052396183) | Verifique os parâmetros que influenciam nos Gastos Variáveis, no tópico [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111413-An%C3%A1lise-de-Rentabilidade#Par%C3%A2metrosqueinfluenciamnestarotina). |
| --- | --- |

- **Margem de Contribuição (MC):** representa o valor que sobra do preço de venda após a dedução dos custos e despesas variáveis, como custos de produção, matéria-prima e tributos. Esse montante é essencial para cobrir os custos fixos e, após essa cobertura, se transformar em lucro.

- **Participação no Gasto Fixo:** é baseado nas regras de cálculo da participação no gasto fixo.
- **Lucro:** o lucro é analisado através da seguinte fórmula:

```
![Imagem 9: Lucro: o lucro é analisado através da seguinte fórmula:](https://ajuda.sankhya.com.br/hc/article_attachments/42312052395287) Faturamento - (Gastos Variáveis + Gastos Fixos + CMV).
```

Pode-se notar no rodapé da tela, a legenda anteriormente mencionada, representada pelo campo **"Margem de Contribuição da Nota"**; é notório também a coluna **"Margem de Contribuição"** apresentando também esta informação por item da nota.

**Nota:** esta configuração é realizada por usuário, porém, caso esta não tenha sido feita para algum utilizador do sistema, serão consideradas para ele, a disposição criada por e para o usuário SUP do sistema.

Esta análise permite ao gerente e/ou vendedor decidirem sobre a concessão ou não de um desconto especial em determinado Pedido ou Nota, apresentando qual será a sua rentabilidade final, considerando o desconto.

**Observações:**

- O gráfico de rentabilidade não irá exibir informações, caso os dados básicos para montagem do gráfico não sejam satisfatórios. Exemplo disso é o faturamento, se ele for "zero", o sistema não irá apresentar o gráfico, pois ele depende do valor do faturamento.
- Os itens satisfatórios, conforme acima, serão agrupados pelas informações Produto, Código, Descrição, Marca, Uso do Produto e Item Vlr. custos.
- No cadastro de [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#top), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana), o campo **"Exibir valores na Análise de Rentabilidade?"** se estiver desmarcado na Análise de Rentabilidade, o sistema mostrará apenas o valor de Faturamento e a grade de Produtos.

---

### Parâmetros que influenciam nesta rotina

**Controla custos por Controle? - CUSTOPORCONT:** com este parâmetro habilitado, o controle será considerado no cálculo do Lucro, Margem de Contribuição e Custo da Mercadoria/Produto Vendido.

**Controla custos por Local? - CUSTOPORLOC:** quando este parâmetro estiver habilitado, o local será considerado no cálculo do Lucro, Margem de Contribuição e Custo da Mercadoria/Produto Vendido.

**Controla custos por Empresa? - CUSTOPOREMP:** com este parâmetro habilitado, o custo por Empresa será considerado no cálculo do Lucro, Margem de Contribuição e Custo da Mercadoria/Produto Vendido.

**Considerar ST a Recuperar em análise de rentab? - CONSIDSTRECUP:** se este parâmetro estiver habilitado, o ST a recuperar será considerado no cálculo do Gasto Variável.

**Usar % e Vlr Custo Variável do cad.de Tip.Títulos? - GOL-CVTIT:** o sistema irá disponibilizar na tela [Tipos de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral), os campos **"% Custo variável"** e **"Valor Custo Variável"**, e estes permitirão a análise futura dos Gastos Variáveis na Análise de Rentabilidade.

**Atualizar Comissão por item? - ATUALCOMITE:** caso este parâmetro esteja ativado, o sistema considera a comissão registrada na grade de itens para compor o Gasto Variável. Se estiver desativado, será considerada a comissão inserida no cabeçalho da nota para estruturar o gasto. Para as notas antigas (lançadas antes da ativação do parâmetro), o sistema não considera a comissão na formação do Gasto Variável. Além disso, como a ativação do parâmetro não dispara o recálculo de comissão, a rentabilidade do item só observará o percentual do item para as notas com comissão calculada ou recalculada após a ativação do mesmo.

**Considerar débito de PIS/COFINS/CSLL na M.C.? - GOL-PISCOFINS:** os dados referentes aos Gastos Variáveis apresentados no [Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), sofrem influência deste parâmetro. Quando ativado, faz com que o sistema deixe de buscar os percentuais de PIS, COFINS e CSLL das configurações do Gerente On-Line que são aplicados no gasto variável, passa a buscar os valores dos impostos da nota (TGFDIN) e soma estes valores ao gasto variável. Além dos três impostos já mencionados, são somados também ISS, INSS e IRF.

**Calcular impostos para Análise de Rentabilidade? - CALCDINRENT:** quando estiver habilitado, o cálculo de **"PIS/COFINS/CSLL"** (quando existir) na nota, será considerado na análise de rentabilidade. O parâmetro habilitado/desabilitado não define o cálculo dos impostos, mas define a participação destes na Análise de Rentabilidade.

**Função p/ Calculo Gasto Variavel Central/Portal - CALGAVARCENPORT:** em relação ao cálculo do Gasto Variável na Análise de Rentabilidade do [Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), será possível realizar a personalização do mesmo por meio de uma função criada no banco de dados (que retorne o valor do Gasto Variável), conforme a necessidade de cada empresa. Assim, para que o cálculo seja efetuado conforme a personalização, deve-se configurar o parâmetro Função p/ Calculo Gasto Variável Central/Portal - CALGAVARCENPORT inserindo no campo **"Texto"** tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), necessariamente, o nome desta função.

Para o correto funcionamento desta função, deve-se informar os parâmetros **"P\_NUNOTA"** e **"P\_SEQUENCIA"** na mesma.

Caso o parâmetro acima mencionado não esteja configurado com o nome da função personalizada, será utilizada a fórmula de cálculo nativa do sistema na Análise de Rentabilidade.

**Função p/ Ativar o Cálculo do Gasto Variavel Centr - CALGACENPORGOL:** pode-se definir neste parâmetro se deseja utilizar a personalização do cálculo do Gasto Variável no Gerente On-line - GOL e/ou no Portal/Central de Vendas, conforme as seguintes opções:

- Ambos;
- Apenas Central/Portal;
- Apenas GOL.

O sistema lerá a opção definida no parâmetro Função p/ Ativar o Cálculo do Gasto Variável Centr - CALGACENPORGOL e, conforme a opção marcada, ele executará o valor definido no parâmetro de chave Função p/ Calculo Gasto Variável Central/Portal - CALGAVARCENPORT, caso possua.

**Usar % Custo Variável do cad.de Vendedores? - GOL-CVVEND:** com esse parâmetro ligado, o sistema irá considerar o campo **"% Custo Variável"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral) do cadastro de [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores) ao realizar a análise de rentabilidade da nota conforme o resultado das vendas de cada vendedor.

**Observações:**

- Para o controle do parâmetro Função p/ Ativar o Cálculo do Gasto Variavel Centr - CALGACENPORGOL, tem-se nas [Preferências do Gerente On-line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line), aba [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abamargemdecontribuio), o campo **"Gasto variável personalizado"** onde será possível escolher a opção para exibição no Gerente On-line - GOL e/ou no Portal/Central de Vendas.
- O sistema sempre irá considerar o **"Vlr. Outros"** no momento de compor a base a ser utilizada para calcular a comissão. Para ser desconsiderado o Vlr. Outros nesse momento, podem ser utilizadas as funcionalidades dos parâmetros CALGACENPORGOL e CALGAVARCENPORT. Ou seja, será possível criar uma função responsável por calcular o gasto variável da nota e informada nos parâmetros mencionados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111413-An%C3%A1lise-de-Rentabilidade#top)
