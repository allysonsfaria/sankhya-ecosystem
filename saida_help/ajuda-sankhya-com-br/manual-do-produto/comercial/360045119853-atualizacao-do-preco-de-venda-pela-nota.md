---
id: "360045119853"
titulo: "Atualização do Preço de Venda pela Nota de Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:33:24Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Fórmulas", "Compra", "Custo", "Nota Fiscal de Compra", "Atualização de Preço de Venda", "Atualização de Preço de Venda manual", "Preço", "Venda", "Atualização do Preço de Venda pela Nota de Compra", "Precificação", "br.com.sankhya.com.mov.atualizaprecvendapelacompra", "Atualização do Preço de Venda pela Nota de Compra manual", "Fórmula de precificação", "Nota fiscal de compra", "Comercial", "Preço de Venda"]
---

# Atualização do Preço de Venda pela Nota de Compra

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312131446679) Módulo: Comercial > Avançado
```

---

Esta tela permite aplicar um percentual de acréscimo no valor de venda do produto. Sua principal funcionalidade é atualizar o preço de venda de itens de uma Nota Fiscal de Compra através de uma fórmula de precificação. Sendo possível também, acrescentar um percentual sobre o valor sugerido.

**Observação:** a fórmula de custo/preço informada no [Cadastros do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), aba [Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo), não irá influenciar nessa rotina; a única fórmula que influenciará é a informada no campo **"Fórmula de precificação"** desta tela.

Para mais informações sobre as funcionalidades desta tela, basta acessar os links abaixo:

| Funcionalidades da Tela | |
| --- | --- |
| [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#h_df7fcf67-b6cd-4421-9246-07b1bdb1665d) | [Painel de Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#h_db3e4e40-d02a-4567-9d83-e9d3066e47b4) |
| [Grade de Apresentação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#h_97a76098-c1c9-4124-961e-f465cdf1a088) | [Como Proceder](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#h_30775461-c4b3-4067-a415-d66f766be8e6) |
| [Custo do Produto na Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#h_ac7b6b3c-8517-42a8-a5ec-b6f384d60e48) |  |

![Imagem 2: Custo do Produto na Nota](https://ajuda.sankhya.com.br/hc/article_attachments/21711419246871)

### Painel de Filtros

Esse painel dispõe de alguns campos do tipo pesquisa para filtrar as notas, sendo eles: **"Período"**, **"Empresa"**, **"Fornecedor"**, **"Produto"**, **"Grupo de produto"** e **"Nro. Único da nota de compra"**.

Ao clicar no ícone de pesquisa do campo Nro. Único da nota de compra, a tela de pesquisa apresentará somente as notas com TOP's de compra.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#top)

### Painel de Opções

Informe no campo **"Fórmula de precificação"**, a fórmula de precificação a ser considerada como base dos cálculos. Essa fórmula deverá estar previamente cadastrada na tela [Fórmulas de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874).

Ao informar uma fórmula, o sistema preencherá a coluna **"Vlr. Sugerido"** da grade de produtos da nota com o valor calculado pela fórmula.

Preencha o campo **"% sobre o valor sugerido"** com o percentual que se deseja acrescentar sobre o valor sugerido.

Pode-se também escolher uma **"Tabela"** de preço a ser atualizada na rotina de Atualização do Preço de Venda pela Nota de Compra, bem como sua **"Data de vigor"**.

**Observação:** ao utilizar uma fórmula personalizada, o cálculo da fórmula padrão do sistema será substituído, sendo aplicado apenas o cálculo definido pela nova fórmula. Caso necessário, é importante incluir na fórmula personalizada os componentes da fórmula padrão do sistema. Observe a fórmula padrão abaixo:

```
![Imagem 3: Observação: ao utilizar uma fórmula personalizada, o cálculo da fórmula padrão do sistema será substituído, sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/42312131448727) VlrSug = (cusGer / (1 - ((percCusFixo + icmsSaida + Produto.MARGLUCRO) /
 100))) * (1 + (taxaFinCpa / 100));
```

![Imagem 4: Os campos "PercCusFixo" , "ICMSSaida" e "TaxaFinCpa" devem ser considerados na fórmula personalizada.](https://ajuda.sankhya.com.br/hc/article_attachments/27633372763159) Os campos **"PercCusFixo"**, **"ICMSSaida"** e **"TaxaFinCpa"** devem ser considerados na fórmula personalizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#top)

### Grade de Apresentação

Essa grade exibirá os dados dos produtos da nota filtrada. Nela, o sistema preenche o campo **"Margem Gerencial"** de acordo com a fórmula

```
![Imagem 5: Essa grade exibirá os dados dos produtos da nota filtrada. Nela , o sistema preenche o campo "Margem Gerencial" de…](https://ajuda.sankhya.com.br/hc/article_attachments/42312131448727) ((1-(Custo Gerencial/Vlr. Calculado))*100)
```

Sobre a grade dessa tela tem-se, além dos botões de configuração e impressão da grade padrões do sistema, os botões:

**![Imagem 6: Confirmar cálculo: a o aplicar o percentual sobre o valor sugerido, confirme os valores apresentados através deste…](https://ajuda.sankhya.com.br/hc/article_attachments/21713149618199) Confirmar cálculo:** ao aplicar o percentual sobre o valor sugerido, confirme os valores apresentados através deste botão;

**![Imagem 7: Rejeitar cálculo: depois de aplicar o percentual sobre o valor sugerido, caso estes não estejam satisfatórios, cancele…](https://ajuda.sankhya.com.br/hc/article_attachments/21713140732823) Rejeitar cálculo:** depois de aplicar o percentual sobre o valor sugerido, caso estes não estejam satisfatórios, cancele a modificação através deste botão;

**![Imagem 8: Calcular: logo após a aplicação do percentual sobre o valor sugerido, acione este botão para que o cálculo sobre o…](https://ajuda.sankhya.com.br/hc/article_attachments/21713143661975) Calcular:** logo após a aplicação do percentual sobre o valor sugerido, acione este botão para que o cálculo sobre o percentual informado seja realizado;

**![Imagem 9: Remover selecionados: a o filtrar por uma nota que possua vários produtos, caso queira atualizar os percentuais apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/21713182308119) Remover selecionados:** ao filtrar por uma nota que possua vários produtos, caso queira atualizar os percentuais apenas de alguns deles, selecione os itens indesejados, mantendo a tecla **"Ctrl"** do teclado pressionada clique sobre os mesmos, e por fim acione este botão para que os produtos sejam excluídos da tela;

![Imagem 10: Remover NÃO selecionados: ao contrário do botão acima, ao filtrar por uma nota que possua vários produtos, caso queira…](https://ajuda.sankhya.com.br/hc/article_attachments/21713208065943) **Remover NÃO selecionados:** ao contrário do botão acima, ao filtrar por uma nota que possua vários produtos, caso queira atualizar os percentuais apenas de alguns deles, deve-se selecionar os itens indesejados, manter a tecla **"Ctrl"** do teclado pressionada e clicar sobre os mesmos, e por fim acionar este botão para que os produtos sejam excluídos da tela.

![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028199852439) **Outras Opções...:** neste botão, tem-se a opção **"Componentes de BI"** para que seja inserido algum componente de BI para esta rotina.

![Imagem 12: Análises: este botão apenas será habilitado quando a rotina possuir pelo menos um componente de BI.](https://ajuda.sankhya.com.br/hc/article_attachments/21713187690647) **Análises:** este botão apenas será habilitado quando a rotina possuir pelo menos um componente de BI.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#top)

### Como Proceder

Depois de informar os filtros desejados, acione o botão ![Imagem 13: Depois de informar os filtros desejados, acione o botão "Aplicar" para que a nota seja apresentada; estando esta na…](https://ajuda.sankhya.com.br/hc/article_attachments/21713306928791) **"Aplicar"** para que a nota seja apresentada; estando esta na tela, na parte de **"Opções"**, informe a Fórmula de Precificação que será considerada e o percentual sobre o valor sugerido que será aplicado; feito isso clique no botão ![Imagem 14: Depois de informar os filtros desejados, acione o botão "Aplicar" para que a nota seja apresentada; estando esta na…](https://ajuda.sankhya.com.br/hc/article_attachments/21713359479447) **"Aplicar%"**.

Quando a fórmula indicada for zero, o sistema utilizará a seguinte fórmula interna:

```
![Imagem 15: Quando a fórmula indicada for zero, o sistema utilizará a seguinte fórmula interna:](https://ajuda.sankhya.com.br/hc/article_attachments/42312131448727) (CusGer / (1-((PercCusFixo + ICMSSaida + MARGLUCRO)/100)))*(1 +
(TaxaFinCpa/100))
```

Onde:

- **CusGer:** busca na tela [Variação de Custo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos), na última data atualizada, o **"Custo Gerencial"** para preenchimento na fórmula;
- **PercCusFixo:** busca nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line) do Gerente On-line (GOL), configurações de [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abamargemdecontribuio), o campo **"%  de Custo Fixo"** para preenchimento na fórmula;
- **ICMSSaida:** busca na tela [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), o campo **"Alíquota"** da Alíquota Interna do Estado do [Cadastro de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas) para preenchimento na fórmula;
- **MARGLUCRO:** busca no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo), o campo **"%  Margem de Lucro"** para preenchimento na fórmula;
- **TaxaFinCpa:** busca o parâmetro **"Taxa Financeira para Cálculo do preço de Venda - TAXAFINCPA"** para preenchimento na fórmula.

Ao clicar no botão Aplicar%, o sistema preencherá na grade de produtos a coluna **"Percentual"** com o valor indicado no campo **"% sobre o valor sugerido"**.

Clicando no botão Calcular, será calculado o percentual sobre o valor sugerido.

Após confirmar o cálculo, o sistema irá alterar os preços de venda dos produtos que foram selecionados na grade de produtos da nota de compra informada. O sistema criará uma nova Tabela de Preço (Código 0), com as atualizações de preço dos produtos que estiverem na grade da tela.

Ao atualizar o preço dos produtos que fazem parte da Tabela derivada, o sistema alimentará a **"Tabela"** de preço com origem **"0"** se o parâmetro **"Utiliza Cod.Tipo Tabela como origem - USACODTIPTAB"** estiver desligado. Porém, com o parâmetro ligado, o sistema criará uma Tabela de preço com origem própria, ou seja, com o código informado.

Se algum produto já foi atualizado no dia, o sistema permitirá que se selecione e confirme a nova atualização de preço dos produtos.

**Observações:**

- Quando o item da nota possuir Valor de Substituição maior que 0, o sistema obrigatoriamente utilizará a fórmula padrão para calcular o Vlr. Sugerido e irá desconsiderar a fórmula informada pelo usuário.
- A coluna **"Vlr. Sugerido"** da grade será atualizada com valor 0 quando o produto não possuir Custo Gerencial. Ou seja, se na rotina [Atualização de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594174-Atualiza%C3%A7%C3%A3o-de-Custos) o campo **"Custo Gerencial"** do produto estiver zerado não será sugerido nenhum valor para o campo **"Valor Sugerido"** desta rotina.
- Os Registros com valores de percentual ou valor sugerido igual a zero não serão calculados.
- Quando o valor sugerido retornar zero, o sistema emitirá o aviso: **"Existem produtos com valor sugerido igual a zero"**. Neste caso o cálculo não poderá ser feito, pois não há como adicionar um Percentual sobre o valor zero.
- A coluna **"Última DT. Vigor"** possui ligação com o campo **"Data de Vigor"** da tela [Atualização de Preço de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612094-Atualiza%C3%A7%C3%A3o-de-Pre%C3%A7o-de-Venda). Caso este esteja informado com uma data maior que a data atual, não será possível realizar a atualização do preço de venda pela nota de compra conforme orientado nesta documentação.

**Importante:** se o produto foi atualizado numa determinada data em questão e ele já existir nas tabelas que estão sendo atualizadas, o pop-up **"produtos Atualizados Hoje"** será exibido na tela.

Para exemplificar, segue os cenários abaixo:

- **Cenário 1**
  Produto 1050
  Dt atualização = 09/12/2022
  Tabela 10

Produto 1050
Dt atualização = 01/10/2022
Tabela 20

Nesse cenário, mesmo que produto o 1050 não tenha sido atualizado na tabela 20, o sistema vai apresentar a mensagem porque existe o produto nesta tabela.

- **Cenário 2**
  Produto 1050
  Dt atualização = 09/12/2022
  Tabela 10

Produto 1050 não existe nesta tabela
Dt atualização = 09/12/2022
Tabela 30

No cenário acima o sistema não irá emitir o pop-up porque não existe o produto na tabela 30.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#top)

### Custo do Produto na Nota

Para buscar o custo do produto da nota são considerados os seguintes parâmetros:

- **Custo por empresa? - CUSTOPOREMP:** se este parâmetro estiver desabilitado, o sistema irá buscar os custos da empresa 1;
- **Custo por local? - CUSTOPORLOC:** com este parâmetro habilitado, o sistema irá buscar o custo do produto no local da nota de compra.
- **Custo por controle? - CUSTOPORCONT:** quando este parâmetro estiver habilitado, o sistema irá buscar o custo do produto no controle da nota de compra.

Além de considerar os parâmetros acima citados, o sistema buscará o último custo do produto considerando a data da nota conforme configuração do parâmetro **"Data para atualização de custo - DTPATUCUST"**.

Exemplo: o parâmetro DTPATUCUST está configurado com a **"Data de Negociação"**. Então o sistema buscará o último custo existente para a data de negociação da nota de compra.

**Importante:** o sistema não atualiza preço de produto configurado na aba [Família](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abafamlia) do [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos).

Ao abrir a tela [Recálculo de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214-Rec%C3%A1lculo-de-Custos) e confirmar uma nota que gere cálculo de custos (apresentada no painel de avisos) serão apresentadas as seguintes mensagens de aviso:

- Quando o parâmetro DTPATUCUST estiver configurado como **"Negociação"**:

**"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos Dt. Negociação. Foi identificado que você está usando configuração diferente do que é atualmente permitido, entre em contato com a Sankhya para se informar sobre as consequências de usar esta configuração."**

- Quando o parâmetro DTPATUCUST estiver configurado como **"Movimentação ou Faturamento"**:

**"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos Dt. Entrada/Saída e caso ela não esteja preenchida usaremos Dt. Negociação. Foi identificado que você possui configuração diferente de Dt. Entrada/Saída, para não ver esta mensagem novamente, basta ajustar o parâmetro "Data para atualização de custo" (DTPATUCUST) colocando a opção "Entrada/Saída", quando o parâmetro DTPATUCUST está igual a "Negociação".**

Para estas mensagens não serem apresentadas, basta configurar o parâmetro DTPATUCUST para Entrada/Saída.

O sistema apresenta a variação de preço de venda, ao confirmar uma nota de compra em que a TOP esteja configurada para precificar, e o parâmetro **"Apresentar variação de preço na NF de compra? - APRVARPNFCOMPRA"** esteja habilitado; o sistema irá apresentar a mensagem:

**"Houve variação no preço de venda. Deseja visualizar os produtos com variação?", clicando-se em "Sim", é apresentada a variação de preço em relação à última data de vigor da tabela de preços, ignorando o dia da confirmação da nota de compra.**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119853-Atualiza%C3%A7%C3%A3o-do-Pre%C3%A7o-de-Venda-pela-Nota-de-Compra#top)
