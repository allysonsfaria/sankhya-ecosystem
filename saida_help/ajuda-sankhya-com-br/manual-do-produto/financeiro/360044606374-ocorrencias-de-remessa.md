---
id: "360044606374"
titulo: "Ocorrências de Remessa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:39:18Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Remessa", "Ocorrências", "Financeiro", "COMPDEVACERTO", "br.com.sankhya.config.alteracao.financeiro", "Ocorrências de Remessa manual", "Códigos de ocorrências bancárias", "Instruções de entrada baixa alteração", "Configuração e permissões", "EDI Bancário"]
---

# Ocorrências de Remessa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312301084311) Módulo: Financeiro > EDI Bancário
```

---

A tela Ocorrências de Remessa tem o objetivo de permitir a definição dos códigos de ocorrências de uma determinada [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas).

A Ocorrência é um número disponibilizado pela instituição financeira que representa cada uma das instruções enviada ao banco (Entrada do Título, Baixa de Título, Alteração de Vencimento).

Os códigos de ocorrências são disponibilizados pela Instituição Financeira (layout de cobrança); com isso, é necessário que a empresa consulte seu banco antes de realizar essa configuração. Assim, teremos o seguinte exemplo:

A empresa gera uma remessa para o título 01, solicitando a entrada do mesmo na carteira do banco. Essa instrução de entrada do título, recebe o código de ocorrência "01" que será utilizado pelo banco para identificar que essa instrução corresponde a uma entrada de título.

As ocorrências podem ser de: Entrada, Baixa ou Alteração.

É necessário que entendamos alguns conceitos:

(1)** Entrada:** Uma vez que a empresa gerou um boleto para o cliente, ela precisa comunicar ao banco a existência deste documento. Uma instrução de entrada de um título, se refere justamente a essa comunicação da empresa junto à instituição financeira.

(1)** Baixa:** A empresa pode solicitar a baixa dos títulos que se encontram em carteira para cobrança no banco. A baixa nesta ocasião, significa que a instituição financeira não deve mais realizar a cobrança deste documento. Um exemplo deste momento, é um cliente que ao invés de pagar o boleto, vai até o estabelecimento comercial e efetua seu pagamento diretamente no caixa.

(1)** Alteração:** Tratamos neste caso de títulos (boletos) que o banco tem conhecimento de sua existência, ou seja tiveram sua entrada no banco a partir do arquivo de remessa (pode ser utilizado o termo 'estar em carteira' no banco para cobrança), porém, sofreram algum tipo de modificação, como por exemplo, a sua data de vencimento. Essas alterações por sua vez, precisam ser comunicadas ao banco para que o mesmo mantenha os dados atualizados do documento para cobrança junto ao cliente.

Para facilitar sua navegação nas funcionalidades desta tela, acesse os links abaixo:

| [Inserindo uma Ocorrência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#inserindoumaocorrncia) |  | [Permissões por Ocorrência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#permiss%C3%B5esporocorr%C3%AAncia) |
| --- | --- | --- |
| [Duplicando um Cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#duplicandoumcadastro) |  | [Ocorrência de Entrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#ocorrnciadeentrada) |
| [Geração da Instrução de Entrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#gera%C3%A7%C3%A3odainstru%C3%A7%C3%A3odeentrada) |  | [Ocorrência de Baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#ocorrnciadebaixa) |
| [Geração de Instrução de Baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#geraodeinstruodebaixa) |  | [Ocorrências de Alterações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#ocorr%C3%AAnciasdealtera%C3%A7%C3%B5es) |
| [Geração da Instrução de Alteração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#geraodainstruodealterao) |  | [Estorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#estorno) |
| [Comp. de Devolução - Compensação Parcial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#compensaodedevoluo-compensaoparcial) |  | [Compensação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#compensaofinanceira) |
| [Comp. de Devolução - Compensação Total](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#compensaodedevoluo-compensaototal) |  | [Cancelamento de nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#cancelamentodenota) |
| [Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#renegociao) |  |  |

![Imagem 2: Renegociação](https://ajuda.sankhya.com.br/hc/article_attachments/4416149349399)

### Inserindo uma Ocorrência

Para inserir uma Ocorrência, clique no botão ![Imagem 3: Para inserir uma Ocorrência, clique no botão "Adicionar" e primeiramente selecione uma conta desejada no campo "Conta…](https://ajuda.sankhya.com.br/hc/article_attachments/16428446862615) **"Adicionar"** e primeiramente selecione uma conta desejada no campo **"Conta Bancária"**, posteriormente, você definirá qual será a ocorrência por meio dos campos **"Ocorrência de Entrada"**, **"Ocorrência de Baixa"** e **"Ocorrência de Exclusão"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Permissões por Ocorrência

Poderá ser necessário realizar a restrição das alterações de cada campo à determinados usuários. Você fará essa configuração na aba Permissões por Ocorrência. Nela é possível inserir os usuários que terão permissão de alteração em cada campo configurado na aba Ocorrências por Campo. Caso não especifique nenhum usuário, o sistema irá entender que qualquer um deles poderá alterar este campo e por consequência gerar uma instrução de alteração do título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Duplicando um Cadastro

A tela Ocorrências de Remessa possui um recurso especial que copia toda a configuração realizada, ou seja, Conta Bancária, Ocorrência de Entrada, Ocorrência de Baixa, Ocorrência de Exclusão e Permissões por Ocorrências. Para isso, utilize o botão  **"Duplicar"**.

Como os layout's dos bancos são baseados em um modelo disponibilizado pela [FEBRABAN](https://portal.febraban.org.br/), muitas das vezes os códigos de ocorrências são semelhantes, com isso, esse recurso visa otimizar a configuração inicial executada por você.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Ocorrência de Entrada

A próxima etapa é definir a Ocorrência de Entrada, que é utilizada automaticamente pelo sistema quando o título é incluído pela primeira vez em uma remessa, ou em uma renegociação onde o título de origem já esteja em carteira junto ao banco.

Como a renegociação exclui o título de origem e gera novos títulos referentes à ela, então pode-se entender que caso o título excluído pela renegociação esteja em carteira no banco, os novos títulos gerados a partir desta devem ser encaminhados ao banco de forma automática, ou seja, tem-se aqui uma Instrução de Entrada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Geração da Instrução de Entrada

A confirmação de uma nota e a consequente transformação de seu financeiro em título Real geram uma instrução de entrada para esse título (apenas títulos de Receita e do tipo Real), ou seja, financeiros que ainda são provisões não são monitorados. Títulos de despesa também não geram instruções de entrada.

As [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) bancárias monitoradas são aquelas que possuem definição de Ocorrências de Remessa. Uma vez lançado um título para uma conta bancária monitorada, este título se torna um título monitorado. A consequência do monitoramento é a geração de uma instrução do tipo entrada para este título com sua respectiva ocorrência. Essa instrução pode ser visualizada por meio da tela [Registro de Alteração Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834).

Na rotina de [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914), as linhas correspondentes a essas instruções são apresentadas sem alterações na sua coloração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Ocorrência de Baixa

Preencha em seguida, a Ocorrência de Baixa, que é utilizada automaticamente pelo sistema em dos seguintes casos:

- **Renegociação:** Quando os títulos de origem já se encontram em carteira junto ao banco. Então, para esses títulos, serão geradas instruções relacionadas a baixa junto à instituição bancária.
- **Baixa manual:** Na baixa manual que acontece pela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), quando um cliente ao invés de pagar o boleto vai até a loja e efetua o pagamento no caixa. Com isso, será gerada uma instrução referente a baixa junto à instituição bancária para o mesmo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Geração de Instrução de Baixa

A Instrução de Baixa corresponde ao pedido de baixa de um título da empresa junto ao banco, que esteja em carteira, porém não existe mais a necessidade de cobrança/recebimento por parte do banco.

Esta é gerada com a Ocorrência de Baixa definida nas Ocorrências de Remessa para a conta bancária. Assim que o título é baixado na Movimentação Financeira, a instrução de baixa é gerada. Estas características são visualizadas por meio da tela [Registro de Alteração Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834).

Na rotina de [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914), as linhas referentes a essas instruções são apresentadas na cor **vermelha**.

**Observação:** instruções do tipo Baixa também são geradas a partir da compensação total do título. 

**[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)**

### Ocorrências de Alterações

As Ocorrências de Alterações devem ser inseridas na aba Ocorrências por Campo, que como o próprio nome descreve, serão definidas por campos do Financeiro, ou seja, a partir do momento em que o título for monitorado, se determinado campo for alterado, será gerada uma Instrução de Alteração no título com o código de ocorrência definido nesta configuração.

Depois de acionar o botão ![Imagem 4: Depois de acionar o botão "Cadastrar Ocorrências por Campo" , selecione em "Nome Campo" , o campo do Financeiro que…](https://ajuda.sankhya.com.br/hc/article_attachments/16428446862615) **"Cadastrar Ocorrências por Campo"**, selecione em **"Nome Campo"**, o campo do Financeiro que será monitorado e que deve orientar a Instrução de Alteração. Para facilitar a utilização, as opções tem como padrão o formato <DESCRICAOCAMPO (NOMECAMPO)>.

**Nota:** os campos adicionais do Financeiro, também são apresentados na lista.

Feita a definição do Nome Campo, é necessário informar o código da "Ocorrência" corresponde à alteração.

**Importante:** vale mencionar que nem todos os campos do Financeiro devem gerar instruções de alteração junto ao banco. Por isso, configure apenas os campos necessários.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Geração da Instrução de Alteração

As instruções do tipo Alteração são consequências da modificação em um título monitorado que já foi enviado ao banco. Um título se enquadra nessa situação se existir uma instrução do tipo Entrada com o Número de Remessa preenchido. A visualização destas características pode ser feita por meio da tela Registro de Alteração Financeiro.

É importante citar que as instruções de alteração apenas serão geradas, caso o campo em que está sendo realizada a modificação esteja incluído na definição de Ocorrências de Remessa para a Conta bancária.

Na rotina de Geração Arquivo de Remessa, as linhas referentes a estas instruções são apresentadas na cor **amarela**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Estorno

A baixa de um título pertencente a uma conta de cobrança registrada monitorada pode ter acontecido indevidamente, de modo que ao proceder com o estorno do documento, é necessário executar ações com objetivo sincronizar a situação do título junto ao banco. Existem dois cenários para este caso:

**![Imagem 5: Instrução do tipo baixa já enviada ao banco](https://ajuda.sankhya.com.br/hc/article_attachments/16428506072727) Instrução do tipo baixa já enviada ao banco**

- Nesta situação, a instrução do tipo Baixa já foi remetida ao banco, e por esse motivo, o estorno será responsável por gerar uma nova Instrução de Entrada do título ao banco;
- A instrução do tipo Entrada é gerada seguindo a mesma lógica e contexto da instrução de entrada descrita no tópico Geração da Instrução de Entrada.

**![Imagem 6: Instrução do tipo baixa não enviada ao banco](https://ajuda.sankhya.com.br/hc/article_attachments/16428500733463) Instrução do tipo baixa não enviada ao banco**

- Neste caso a baixa do título aconteceu, porém a instrução do tipo Baixa gerada ainda não foi enviada ao banco; com isso, o estorno do documento exclui esta instrução, visto que não existe mais necessidade de comunicar a baixa ao banco. Deste modo, serão reabertas as instruções do tipo Alteração que podem ter existido antes da instrução de baixa e que ainda não foram comunicadas ao banco.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Compensação de Devolução - Compensação Parcial

A compensação parcial tem como característica, reduzir o valor de um título uma vez que este é compensado com outro título referente a um crédito do cliente gerado pela devolução. Caso o título que está tendo seu valor modificado já tenha sua instrução do tipo Entrada enviada ao banco, é gerada uma instrução de Abatimento com o valor específico do abatimento. Teremos um exemplo:

Uma venda no valor de R$100,00 gerou boleto de pagamento e foi enviado ao banco. Entretanto, por algum motivo o cliente não aceitou a mercadoria em sua totalidade, devolvendo R$20,00. Essa devolução se torna um crédito ao cliente, mas o mesmo deseja que seja refletido na venda, ou seja, ao invés de pagar R$100,00, ele almeja pagar R$80,00. A compensação de devolução altera o valor do título de R$100,00 para R$80,00; o sistema armazena a informação da alteração de valores no campo como Abatimento, de modo que uma instrução do tipo Alteração é gerada e será possível utilizar o valor de R$20,00 do Abatimento para encaminhamento ao banco.

O Estorno de uma Compensação Parcial é utilizado para desfazer uma compensação realizada de forma equivocada, em que poderá ter duas situações:

**1.Instrução de abatimento enviada:** Caso a instrução já tenha sido remetida ao banco, é necessário encaminhar uma segunda instrução correspondente ao cancelamento de abatimento. Essa instrução gera um estono que modifica o campo para Abatimento Cancelado, com isso, como existe Ocorrência de Remessa para este campo, a instrução do tipo Alteração será gerada.

**2.Instrução de abatimento não enviada:** Quando a instrução não foi encaminhada ao banco, o sistema realiza sua exclusão, uma vez que não existe mais a necessidade de comunicar ao banco sobre uma concessão de abatimento.

Poderá ter também o caso em que existe uma segunda compensação de devolução sobre um título que já sofreu compensação:

- Se a instrução existente já foi enviada ao banco:

Como o banco não aceita alterações no valor de Abatimento, é necessário gerar uma instrução de Cancelamento de Abatimento e em seguida uma nova instrução de Abatimento com o novo valor de abatimento;

A instrução de Cancelamento corresponde a uma instrução do tipo Alteração para o campo Abatimento Cancelado que recebeu o valor do abatimento antigo enviado ao banco anteriormente;

Uma nova instrução do tipo Alteração para o campo Abatimento é gerada por consequência da alteração do campo Abatimento que recebe o valor total do abatimento.

- Caso a instrução existente não tenha sido enviada ao banco:

Apenas o valor do campo Abatimento é modificado, de forma que o valor deste abatimento represente o valor total do abatimento que precisa ser direcionado ao banco pela instrução do tipo Alteração para o campo Abatimento.

Tem-se ainda, o estorno da Compensação Parcial realizado nos casos em que o cliente deseja que sua devolução fique como crédito para uma venda futura; nessa situação, o estorno da compensação consiste em retornar a situação anterior do título. Portanto, em casos que:

- **Instruções enviadas ao banco:** Será gerada uma instrução de cancelamento de abatimento para o valor inicial do abatimento. O campo Abatimento Cancelado recebe o valor do abatimento para ser utilizado na instrução encaminhada ao banco. Em consequência disso, temos a geração de uma instrução de abatimento para o novo valor do abatimento. O campo Abatimento recebe o novo valor de abatimento para ser utilizado na instrução enviada ao banco.
- **Instruções não enviadas ao banco:** Será feita a exclusão da instrução de Abatimento Cancelado e o valor do Abatimento será atualizado de forma que a instrução a ser enviada ao banco receba o valor correto de abatimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Compensação Financeira

A lógica da Compensação Financeira é a mesma da Compensação de Devolução, porém ao invés da compensação acontecer com base em uma nota de devolução (Central de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793)/[Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)), acontece na rotina de [Compensação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073).

- Caso seja necessário desfazer a compensação, se a instrução de Abatimento tiver sido enviada ao banco, o sistema irá gerar uma instrução de Cancelamento pertinente ao abatimento concedido anteriormente.
- Ao desfazer a compensação, se a instrução de Abatimento não tiver sido enviada ao banco, os títulos retornarão ao seu cenário inicial, ou seja, sem instrução de abatimento.

**[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)**

### Compensação de Devolução - Compensação Total

A compensação total tem como característica a baixa de um título correspondente a uma venda, pois o crédito gerado para o cliente consiste na devolução total de uma determinada venda. Por exemplo, uma venda no valor de R$100,00 gerou boleto de pagamento e foi enviado ao banco; entretanto, o cliente cancelou a compra, gerando uma devolução que por consequência gera um crédito a ser compensado na venda.

Como a compensação tem como particularidade baixar o título da venda, caso o título pertença a uma conta monitorada e já tenha sido remetido ao banco, a instrução do tipo Baixa será gerada. A geração da instrução do tipo Baixa ocorre assim como descrito no tópico Geração de Instrução de Baixa.

Assim como pode ocorrer na compensação parcial, a Compensação Total também pode ter sido realizada indevidamente (cliente deseja ficar com crédito para uma venda futura), sendo necessário a execução de um estorno da compensação, que baseia-se em retornar a situação anterior do título. Diante disso, tem-se duas possibilidades:

- Caso a instrução do tipo Baixa já tenha sido enviada ao banco, uma nova instrução do tipo Entrada será gerada para ser enviada ao banco;
- Se a instrução do tipo Baixa não tiver sido enviada ao banco, a mesma que foi gerada no momento da compensação é excluída, pois não existe mais a necessidade de ser direcionada ao banco, e as instruções do tipo Alteração que foram sinalizadas como baixadas no momento de geração da baixa, são reabertas de forma a permitir seu envio ao banco.

**Observação:** para que a compensação de devolução seja executada de uma forma compatível com o monitoramento de cobrança, o parâmetro **"Realizar compensação de devolução usando acerto - COMPDEVACERTO"** precisa estar ativado de forma a transformar o contexto da compensação de devolução no mesmo contexto da compensação financeira, entretanto com um tipo específico (devolução). Com estas configurações, torna-se possível gerar as instruções de abatimento conforme esperado (título original tem seu valor alterado e um novo título é criado para ser compensado).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Cancelamento de nota

O procedimento realizado no cancelamento de notas é semelhante ao da baixa manual, pois se o título já foi remetido ao banco é necessário que se encaminhe uma instrução ao banco solicitando a baixa do mesmo. A instrução do tipo Exclusão na realidade é a mesma ocorrência da instrução do tipo Baixa; para diferenciar os fatos e permitir que tal recurso seja ou não habilitado, temos a Ocorrência de Exclusão na configuração das Ocorrências de Remessa.

Deste modo, quando uma nota é cancelada e consequentemente seu respectivo título, se este pertencer a uma conta monitorada e já foi remetido ao banco, é gerada uma instrução do tipo Exclusão.

As linhas correspondentes às instruções do tipo Exclusão são apresentadas na rotina de [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914) na cor **cinza**.

Títulos excluídos não são apresentados na rotina de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), com isso, é possível acompanhar apenas a instrução gerada a partir da tela de consulta [Registro de Alteração Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

### Renegociação

A renegociação possui as seguintes características:

- Os títulos renegociados são baixados;
- Novos títulos são criados como resultado da renegociação.

Uma vez que os títulos renegociados são baixados, caso os títulos baixados pertençam a uma conta monitorada e já tenham sido remetidos ao banco, o sistema gera uma instrução do tipo Baixa para ser remetida ao banco; além disso, caso os títulos criados pertençam a uma conta monitorada, será gerada uma instrução do tipo Entrada para ser remetida ao banco.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374-Ocorr%C3%AAncias-de-Remessa#top)

---

![Imagem 7: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16512868551063) Acesse também:

[Controle/monitoramento de Cobranças Registradas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111753)

[Registro de Alteração Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834)
