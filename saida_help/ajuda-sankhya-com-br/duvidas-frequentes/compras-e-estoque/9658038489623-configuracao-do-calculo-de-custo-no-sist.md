---
id: "9658038489623"
titulo: "Configuração do cálculo de custo no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9658038489623-Configura%C3%A7%C3%A3o-do-c%C3%A1lculo-de-custo-no-sistema"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:06:54Z"
rotulos: ["Produtos", "Custos", "Configuração", "Fórmulas", "TOP", "Estoque", "Configuração do Cálculo de Custo no Sistema", "Cálculo de custo"]
---

# Configuração do cálculo de custo no sistema

Os custos são calculados/atualizados de acordo com a expressão utilizada na Fórmula de precificação. 
Esta fórmula é criada e validada pelo cliente, utilizando seus critérios para o custeio dos produtos (frete, impostos, descontos etc.).
Para que os custos sejam atualizados de forma correta é necessário que você verifique os seguintes pontos:

![Imagem 1: A configuração do campo "Precifica", da aba Geral , para os Tipo de Operação-TOP de Compra:](https://ajuda.sankhya.com.br/hc/article_attachments/16413619036055) A configuração do campo **"Precifica",** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), para os [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de Compra:

![Imagem 2: A configuração do campo "Precifica", da aba Geral , para os Tipo de Operação-TOP de Compra:](https://ajuda.sankhya.com.br/hc/article_attachments/15476371383191)

Por meio do campo Precifica defina pela atualização ou não dos custos e preço de venda dos produtos, ao realizar a confirmação de uma nota compra. As opções são:

- **Não atualizar custo nem preço de venda:** por esta opção, custo e preço não serão atualizados;
- **Atualizar custo e preço de venda:** tanto custo, quanto preço de venda serão atualizados na confirmação da nota de compra;
- **Atualizar somente custo:** apenas o custo será atualizado ao confirmar-se a nota de compra;
- **Atualizar custo pelo agendador:** esta opção será utilizada para realização do cálculo de custos do produto apenas na rotina [Agendador de Recálculo de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594294-Agendador-para-Rec%C3%A1lculo-de-Custos).

**![Imagem 3: IMPORTANTE: Para operações de Devolução de Venda e Requisição , o custo aplicado será sempre aquele em vigor na data…](https://ajuda.sankhya.com.br/hc/article_attachments/16413632057111) IMPORTANTE:** Para operações de Devolução de Venda e Requisição, o custo aplicado será sempre aquele em vigor na data do(s) lançamento(s) dessas operações.

![Imagem 4: Se os campos "Fórmula de Custo/Preço" e " % Margem de Lucro" , aba Formação de Custo/Preço , da tela Cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/16413632057623) Se os campos **"Fórmula de Custo/Preço"** e **"% Margem de Lucro"**, aba [Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo), da tela [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) ,estão devidamente preenchidos;

**![Imagem 5: IMPORTANTE: q uando o produto não possui fórmulas de custo/preço, o sistema utiliza a fórmula interna para calcular os…](https://ajuda.sankhya.com.br/hc/article_attachments/16413632057111) IMPORTANTE:** quando o produto não possui fórmulas de custo/preço, o sistema utiliza a fórmula interna para calcular os custos e preços do produto. Para entender tais fórmulas, acesse o artigo [Cálculo de Custos sem Fórmula de Precificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597894)

**Parâmetros que influenciam :**

| **CHAVE** | **DESCRIÇÃO** | **FUNCIONALIDADE** |
| --- | --- | --- |
| DIASLIMALTCUSTO | Dias limite para excluir custos | Não poderão ser excluídos custos com data de atualização anterior ao período digitado no parâmetro. |
| EXCLUIRCUSTODIG | Excluir custo digitado quando houver mov. De entrada? | A atualização dos 'Custos Digitados' dependerá do parâmetro "EXCLUIRCUSTODIG". - Se há custo digitado ele será excluído se o parâmetro EXCLUIRCUSTODIG estiver ligado. Isso ocorrerá apenas em dias que houver movimento que atualizem custos. - Se o parâmetro EXCLUIRCUSTODIG estiver desligado, o custo digitado será mantido e não será feito cálculo de custo para a data, preservando assim o que foi digitado.  Custos Médios: - Caso exista no dia, custos digitados, que não foram excluídos, tendo sido digitado qualquer dos custos médios (Médio Com ICMS, Médio Sem ICMS, Médio Gerencial), estes custos médios não serão recalculados. Caso contrário, serão recalculados com base nos custos digitados para o dia |
| CALCCUSTOMEDCAF | Calcula Custo Médio na C.A.Fornecedor na Confirmação? | O parâmetro "Calcula Custo Médio na C.A.Fornecedor na Confirmação? - CALCCUSTOMEDCAF", quando acionado, e for utilizada a opção de Recalcular Custos, além de calcular o custo de entrada, também vai calcular o custo médio. Se desativado, o processo de confirmação ficará mais ágil, pois ao não calcular o custo médio, não é feita uma leitura de estoque, entradas e saídas, na confirmação da nota, processo este feito na realização do referido cálculo. |
| CUSTOPORCONT | Controla Custos por Controle? | Habilita o campo "Controle" na Rotina de Atualização de Custos, para atualização de custos por controle.  quando habilitado, **não é recomendado realizar transferências entre controles**, pois o controle é uma característica fixa do produto, e pode impactar o cálculo de custo. |
| CUSTOPORLOC | Controla Custos por Local? | Habilita o campo "Local" na Rotina de Atualização de Custos |
| CUSTOPOREMP | Custo por Empresa | Se estiver "Sim", na tela de recálculo de custos aparece o campo "Empresa", para o usuário poder escolher para qual empresa os custos serão recalculados. Se estiver "Não", não será possível escolher a empresa para recalcular custos. |
| DTPATUCUST | Data para atualização de custo | Defina neste parâmetro qual a data da nota de entrada que o sistema irá utilizar para o cálculo do custo dos produtos: Data de Negociação, Entrada e Saída, Movimentação e Faturamento. |
| CUSTODEC | Decimais para custo | Utilizado para informar quantidade de casas decimais que serão apresentadas nas notas de compras; |
| CUSTOFORMEMP | Usar fórmula da empresa? | Definirá o local onde o sistema buscará a Fórmula Custo/Preço para atualização de custos. Quando ligado, será utilizada a fórmula informada na aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), permitindo uma atualização diferente para cada Empresa, de acordo com as fórmulas informadas. Quando desligado, o sistema buscará a fórmula informada na aba [Formação de Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaformaodecustopreo) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-). |
