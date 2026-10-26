---
id: "360045108813"
titulo: "Alíquotas de COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:28:44Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Porporcionalização de PIS/COFINS", "Fiscal", "NF-e", "COFINS", "Alíquotas de COFINS", "br.com.sankhya.com.cad.aliquota.cofins", "Alíquotas de COFINS manual", "Impostos", "UTILCFOPPC", "INCLUIALIPISCOF", "UTILORIGPRODPCC", "Cadastro Alíquotas COFINS", "UTILGRUPPF"]
---

# Alíquotas de COFINS

| ```  Módulo: Comercial > Arquivo > Cadastros > Alíquotas ``` |
| --- |

---

COFINS é a sigla para Contribuição para o Financiamento da Seguridade Social. Trata-se de uma contribuição a nível federal, calculada sobre a receita bruta de empresas. Sua arrecadação é destinada aos fundos de previdência e assistência social e da saúde pública.

No **Sankhya Om**, o cadastro das alíquotas relacionadas a esse imposto são cadastradas nessa tela.

![Imagem 1: No Sankhya Om , o cadastro das alíquotas relacionadas a esse imposto são cadastradas nessa tela.](https://ajuda.sankhya.com.br/hc/article_attachments/21131423692567)

Por meio do campo **"Código Alíquota"** será possível identificar qual alíquota é utilizada nos documentos fiscais. 

Os campos **"Grupo"**, **"Empresa"**, **"Parceiros"**, **"TOP"**, **"Tipo"** e **"Tipo alíquota"** são de preenchimento obrigatório e possibilitam a criação de regras de exceção para cálculo. O campo Grupo está ligado diretamente ao [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), assim, por exemplo, pode-se ter um grupo chamado **"Plástico"** e associá-lo ao cadastro de vários produtos. Sendo assim, todos os produtos que tiverem o grupo **"Plástico"** estarão nessa exceção.

**Nota:** a prioridade para determinação de alíquota será: TOP, Parceiro e Empresa.

Se não for encontrada nenhuma exceção, poderá ser utilizada uma configuração com valor padrão como:

Empresa 0; Parceiro 0; TOP 0; Alíquota 3,0.

Deve-se observar que, a TOP será a exceção mais analítica, ou seja, caso exista uma seguinte situação de exceção: Empresa 1, Parceiro 10 e TOP 100, apenas as vendas dos produtos daquele Grupo pela Empresa 1, para o Parceiro 10 e utilizando a TOP 100 serão tributadas, obedecendo as regras definidas. Uma venda para Empresa 1, Parceiro 10 e TOP 99, por exemplo, deverá obedecer a regra geral, desde que também não exista outra regra específica para a TOP 99.

O campo **"Tipo"** indica se o cálculo do COFINS será realizado nas movimentações de Entrada, Saída ou em Ambas.

No campo **"Alíquota"**, informa-se o percentual ou valor referente à alíquota do imposto, conforme a definição realizada anteriormente no campo **"Tipo da Alíquota"** que pode ser determinado como Percentual ou Valor.

Preencha o campo **"Alíquota Suframa"** para efetuar a emissão de NF-e referente à venda para a Zona Franca de Manaus e Área de Livre Comércio, onde do valor total da nota fiscal será subtraído o valor de PIS e COFINS desonerado pela operação.

**Importante:** com o campo acima preenchido, a marcação **"Possui Suframa para PIS/COFINS"** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) habilitada, a nota sendo de venda e o CST do PIS e COFINS igual à **"06 - Alíquota Zero"**, o cálculo desses dois impostos será feito preenchendo os campos de Alíquota e Valor de PIS/COFINS desonerados, sendo que, isso vale tanto para incidência no produto quanto para despesas acessórias.

**Observação:** a soma dos valores de PIS/COFINS desonerados dos impostos do item será incluída no campo **"Valor PIS/COFINS Desonerados"** do [Rodapé da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) e, no XML, teremos os valores desonerados adicionados à tag **<vDesc>**.

Nos campos **"% Red. Base"** e **"IVA"**, informe os percentuais correspondentes, se necessário. O campo **"Alíq. p/ crédito"** é utilizado na movimentação de COFINS.

**Observação:** caso utilize o crédito de COFINS em suas operações, realize a marcação **"Tem Créd.COFINS?"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa). Desse modo, o sistema irá aplicar a alíquota de crédito informada no campo acima.

O campo **"Retém no financeiro"** será utilizado assim que a NF-e passar a tratar movimentações de serviço.

Preencha o campo **"Tabela c/ base p/ ST"** com o código da tabela correspondente, se o imposto for por pauta.

Ao marcar a opção **Habilitar geração simultânea dos grupos PIS/COFINS e PISST/COFINSST**, o sistema gera as tags de contribuição própria (PIS/COFINS) e as tags de Substituição Tributária (PISST/COFINSST) ao mesmo tempo dentro do XML da NF-e para um mesmo item. Ative esta marcação quando a sua operação fiscal exigir a incidência conjunta dessas contribuições. Com ela ativada, se o item da nota tiver valores calculados para as duas incidências, o sistema constrói os dois grupos tributários no XML. Nessa estrutura simultânea, o grupo de ST utiliza a mesma alíquota definida para a operação normal e o sistema força o envio do CST 05 para o grupo ST, independentemente do CST configurado para o grupo normal.

> **Atenção:** se você deixar esta opção desligada, o sistema mantém o comportamento padrão, gerando apenas o grupo tributário da regra principal da operação. Alterações nesta marcação impactam apenas as notas geradas após a mudança.

Logo abaixo, a marcação **Indica se o valor do PIS/COFINS ST compõe o valor total da NF-e** soma o valor calculado da Substituição Tributária ao Valor Total da nota.

Para evitar erros de estruturação no XML, o sistema controla automaticamente a liberação destes dois campos de acordo com a opção que você selecionar no campo **Cód. sit. tributária (CST)**:

- Se você selecionar os CSTs **01** ou **02** (Alíquota Normal ou Diferenciada), o sistema libera a marcação de geração simultânea e bloqueia a opção que compõe o valor total da NF-e.
- Se você selecionar o CST **05** (Operação Tributável por ST), o sistema libera a opção que compõe o valor total e bloqueia o campo de geração simultânea, uma vez que o CST 05 já é exclusivamente de ST e não exige a regra de simultaneidade.

No campo **"Código sit. tributária"**, determine dentre as opções da lista, a regra tributária do produto/empresa.

**Importante:** a tabela de CST de COFINS possui situações tributárias específicas para **"Entrada"** ou para **"Saída"**, sendo que essa definição deve ser respeitada, para evitar posteriores erros de validação da **"EFD Contribuições"**. O sistema fará então, a seguinte validação na inclusão de CST, evitando configurações inconsistentes de Alíquotas de COFINS:

- Se informada uma CST na faixa de 50 a 98, o **"Tipo"** deverá ser igual à **"Entrada"**.
- Se informada uma CST na faixa de 1 a 49, o Tipo deverá ser igual à **"Saída"**.

Ao ativar a marcação **"IPI incide na base de cálculo"**, o IPI será integrado a base de cálculo de PIS, COFINS e CSSL.

Se a marcação **"Produto sem tributação"** estiver efetuada, fará com que os campos Alíquota, %Red. base, IVA e Alíq. p/ crédito sejam zerados e desabilitados. Sendo assim,  poderá se emitir notas não tributadas pelo imposto em questão.

**Nota:** o botão  **"Edição múltipla"** permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com as alíquotas em modo grade na tela Alíquotas de COFINS selecione-as e em seguida clique no botão Edição múltipla, assim os campos poderão ser editados simultaneamente para todas as selecionadas.

O campo **“Indica se o valor do COFINSST compõe o valor total da NF-e”** deve ser ativado para indicar se o valor do COFINS Substituição Tributária (COFINSST) deve ser incluído no total da Nota Fiscal Eletrônica (NF-e).

Se esse campo estiver desmarcado, significa que o valor do COFINSST não será somado ao valor total da NF-e. Ele será apenas informado separadamente.

Se estiver marcado, o valor do COFINSST será somado ao total da NF-e, ou seja, fará parte do cálculo final da nota.

Essa configuração também afeta a forma como as informações do COFINSST aparecem no XML da NF-e, garantindo que os dados sejam gerados corretamente.

Se no campo **"Cód. sit. tributária"**, também na tela **Alíquota de COFINS**, você selecionar a opção **“05 - Operação Tributável por Substituição Tributária”** e a alíquota for diferente de zero, o sistema exibirá um aviso ao salvar os dados na tela de Alíquotas de COFINS:

**“Sempre que a CST for igual a 05 e houver cálculo de COFINS, o campo Indica se o valor do COFINSST compõe o valor total da NF-e deverá estar marcado”.**

---

### Proporcionalização de PIS e COFINS

O cálculo da proporcionalização dos campos do pé da nota é muito parecido em relação às marcações na aba **"Despesas Acessórias"** do cadastro de TOP's.

Para todos os impostos, a regra segue a mesma. Só possui algumas diferenciações como: alguns impostos têm redução de base de cálculo. Mas a lógica é a mesma para todos. Tem-se o exemplo:

- Item 1 - Total (qtd x vlrunit): 8,00 - 8/16 = 0,50 = 50%
- Item 2 - Total (qtd x vlrunit): 4,00 - 4/16 = 0,25 = 25%
- Item 3 - Total (qtd x vlrunit): 4,00 - 4/16 = 0,25 = 25%
- Total dos Itens: 16,00
- Vlr do Frete Total: 10,00
- Vlr do Frete Proporcional:
- Item 1 - Total:5,00
- Item 2 - Total:2,50
- Item 3 - Total:2,50

No caso de PIS e COFINS, o cálculo segue o seguinte roteiro a cada nota:

**Observação:** o que for escrito abaixo para PIS, vale também para o COFINS.

O sistema irá buscar na TGFDIN todas as linhas que possuem o imposto PIS e com incidência igual à Geral, Produto ou Serviço, ou seja, o valor do PIS normal que cada item da nota calculou (PIS normal está sempre na incidência igual à Geral).

Para haver a proporcionalização do PIS/COFINS, é necessário que os itens possuam o cálculo de PIS/COFINS.

---

Para saber sobre a segregação de PIS/COFINS retido e apuração própria de origem na NT 007/2026 acesse o seguinte artigo: [NFS-e: Segregação de PIS/COFINS Retido e Apuração Própria (NT 007/2026)](https://ajuda.sankhya.com.br/hc/pt-br/articles/38956082590487-NFS-e-Segrega%C3%A7%C3%A3o-de-PIS-COFINS-Retido-e-Apura%C3%A7%C3%A3o-Pr%C3%B3pria-NT-007-2026).

---

### Parâmetros que influenciam a rotina

Ao habilitar o parâmetro **"Incluir impostos simultâneos (PIS/COFINS)? - INCLUIALIPISCOF"**, é possível cadastrar as alíquotas de PIS e COFINS simultaneamente, agilizando o processo de cadastro. Observe:

[GIF animado: Imagem 2: Ao habilitar o parâmetro "Incluir impostos simultâneos (PIS/COFINS)? - INCLUIALIPISCOF" , é possível cadastrar as…](https://ajuda.sankhya.com.br/hc/article_attachments/21220037122967)

Após a inclusão, para validar o cadastro da alíquota de PIS, acesse a tela [Alíquota de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS).

#### ![Imagem 3: Aplicação do cálculo de PIS e COFINS por exceção:](https://ajuda.sankhya.com.br/hc/article_attachments/42312007369495)Aplicação do cálculo de PIS e COFINS por exceção:

Existem várias possibilidades para configurar exceções no cálculo de PIS e COFINS, que podem ser baseadas na Finalidade da Operação, na origem do produto, no CFOP e/ou no grupo de PIS/COFINS do Parceiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS#top)

#### ![Imagem 4: Finalidade da Operação](https://ajuda.sankhya.com.br/hc/article_attachments/42311990237591) Finalidade da Operação

Através da tela [Finalidade da Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599434-Finalidade-da-Opera%C3%A7%C3%A3o), é possível realizar cadastros para serem utilizados na rotina de exceção para o cálculo do PIS, COFINS e CSLL em pedidos e/ou notas fiscais.

Para isso, ao cadastrar a Finalidade da Operação, deve-se definir no campo **"Sigla"** a variável que será usada como parâmetro para definir a exceção. Esta sigla pode ser, por exemplo, a primeira letra que melhor identifique a finalidade.

Na prática, pode-se ter o seguinte cadastro: na **"Descrição"**, define-se a Finalidade da Operação como **"Imobilizado"** e, na sigla, a variável **"I"**.

Uma vez definida a variável de exceção, é necessário criar as alíquotas correspondentes de PIS, COFINS e CSLL para que, no lançamento do pedido e/ou nota, o sistema possa buscar a informação correta. A **"Descrição"** do grupo das alíquotas de PIS, COFINS e CSLL deve indicar a descrição da regra padrão seguida pela sigla definida anteriormente, separadas por dois pontos (:). Considere o seguinte exemplo:

Suponha que no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) o campo **"Grupo PIS"** esteja definido com a opção **"TODOS"**. As Finalidades de Operação são: **"Imobilizado: I"** e **"Consumo: C"**, e para cada situação se aplicam alíquotas diferentes, como descrito abaixo:

- Alíquota de PIS para Revenda (padrão): 3%
- Alíquota de PIS para Consumo: 9%
- Alíquota de PIS para Imobilizado: 6%

Neste caso, a alíquota de PIS deverá ser cadastrada três vezes, da seguinte forma:

- Grupo: TODOS à Alíquota: 3%
- Grupo: TODOS:I à Alíquota: 6%
- Grupo: TODOS:C à Alíquota: 9%

No contexto do pedido e/ou nota, ao informar o código da Finalidade da Operação cadastrada anteriormente no lançamento do item, o sistema verificará se existe alguma alíquota de PIS, COFINS e CSLL registrada nos moldes indicados acima. Caso exista, esta será considerada na aplicação do cálculo dos impostos citados. Caso contrário, será utilizada a alíquota padrão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS#top)

#### ![Imagem 5: Por origem do produto](https://ajuda.sankhya.com.br/hc/article_attachments/42312007372439) Por origem do produto

Quando o parâmetro **"Utiliza Orig. Prod para localizar aliq. PisCofins - UTILORIGPRODPCC"** estiver habilitado, o sistema irá considerar a origem do produto informado no campo **"Origem do Produto"** (do lançamento do item) para determinar a alíquota de PIS e COFINS a ser utilizada na nota.

**Observação:** para que o sistema identifique a alíquota correta, no cadastro das alíquotas de PIS e COFINS, é necessário inserir a um novo cadastro indicando no campo **"Grupo"** a descrição da alíquota padrão, seguida por dois pontos (":") e o código da origem do produto.  

Exemplo: TODOS:0

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS#top)

#### ![Imagem 6: Por CFOP](https://ajuda.sankhya.com.br/hc/article_attachments/42312007376663) Por CFOP

Se o parâmetro **"Utiliza CFOP para localizar alíq. PIS/COFINS - UTILCFOPPC"** estiver habilitado, ao emitir uma nota fiscal de venda contendo um item bonificado, por exemplo, o sistema considerará as alíquotas de exceção de PIS e COFINS para os grupos com suas respectivas CFOPs mencionadas na descrição do Grupo.

Exemplo: TODOS:5910.

**Importante:** se for informado algum valor após os dois pontos (":") que não seja um CFOP válido, essa exceção não será considerada.

**Observação:** essa rotina se aplica a operações classificadas com outros CFOPs.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS#top)

#### ![Imagem 7: Por grupo de PIS/COFINS do parceiro](https://ajuda.sankhya.com.br/hc/article_attachments/42311990244503) Por grupo de PIS/COFINS do parceiro

Com o parâmetro **"Utiliza Grupo PIS/COFINS do Parceiro para localizar Aliq. PisCofins - UTILGRUPPF"** habilitado, é possível configurar uma exceção de PIS e COFINS indicando uma variável ou número no campo **"Grupo PIS/COFINS"** da aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros).

Para que o sistema identifique a exceção, deve-se cadastrar as alíquotas de PIS e COFINS, inserindo no campo Grupo a descrição da alíquota padrão seguida por dois pontos (":") e o código definido no campo Grupo PIS/COFINS.

Exemplo: TODOS:número da exceção.

**Nota:** ao trabalhar com mais de uma variável, o sistema seguirá uma lógica hierárquica para determinar a alíquota adequada de PIS e COFINS para a operação, percorrendo a seguinte ordem: CFOP, Finalidade da Operação, Origem do Produto, e Grupo de PIS/COFINS do Parceiro.

**Importante:** o sistema não atende a casos de exceções com múltiplas variáveis simultaneamente. Portanto, para obter a alíquota de PIS e COFINS por meio das exceções possíveis, é necessário configurar cada exceção separadamente. Lembre-se de que o sistema seguirá a hierarquia definida anteriormente: CFOP, Finalidade da Operação, Origem do Produto e Grupo de PIS/COFINS do Parceiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS#top)
