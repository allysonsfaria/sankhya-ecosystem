---
id: "360045111933"
titulo: "Baixa Parcial com Retenções"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111933-Baixa-Parcial-com-Reten%C3%A7%C3%B5es"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-10T12:15:49Z"
rotulos: ["Configuração", "Movimentação Financeira", "Baixa Parcial com Retenções", "Baixa Parcial com Retenções manual", "Impostos", "Estoque", "Financeiro", "Processo de Baixa Parcial com Retenções", "Impostos retidos"]
---

# Baixa Parcial com Retenções

As informações abaixo, descrevem sobre a baixa parcial de títulos oriundos do estoque ([Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)) e que possuem impostos retidos. Ao proceder com a baixa parcial, os impostos a serem retidos, serão embutidos por dentro, de modo que o valor líquido da baixa parcial seja o digitado pelo usuário na execução do processo. Em outras palavras, internamente, o sistema realizará o cálculo da base do imposto, já ciente do valor total que este deve possuir, para em seguida chegar ao valor do imposto e verificar se deverá ou não ocorrer sua retenção na baixa parcial.

Diante disso, temos:

No [Cadastro de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos), caso você efetue a configuração do campo **"Vlr. Mínimo do Imposto"**, o sistema irá proceder com o cálculo do imposto retido por dentro.

![Imagem 1: No Cadastro de Impostos , caso você efetue a configuração do campo "Vlr. Mínimo do Imposto" , o sistema irá proceder…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003039221)

Na realização da baixa de um título de forma parcial, na tela de [Baixa de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos) aberta por meio da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), caso este título possua impostos retidos, o sistema verifica inicialmente se o imposto em questão possui origem na configuração efetuada no Cadastro de Impostos. Caso afirmativo, baixando um título parcialmente, informe o valor a ser baixado de forma manual, o sistema irá calcular o imposto sobre este valor digitado, considerando este imposto por dentro para se chegar à base de cálculo.

Uma vez que se chegou à base de cálculo, será realizado o cálculo do imposto e seu valor será comparado ao valor inserido no campo **"Vlr. Mínimo do Imposto"** no Cadastro de Impostos. Com isso, temos duas possibilidades:

- Se este imposto calculado é igual ou maior que o valor mínimo configurado, o sistema irá deixar o imposto calculado para ser retido na baixa parcial, e o valor a ser baixado será o valor calculado para base de cálculo deste imposto;
- Se o valor do imposto calculado for menor que o mínimo configurado, será feita a baixa do título, sem retenção do imposto, e o valor da baixa parcial será aquele indicado pelo usuário.

O cálculo por dentro obedece a seguinte fórmula:

**BC = Valor da Baixa Parcial / ((100 - Y) /100)**

Onde:

Y = alíquota do imposto a ser retido; com isso:

**Imposto a ser retido = BC \* Y**

Considere alguns exemplos:

**Exemplo 1** - Suponhamos no Cadastro de Impostos, o imposto COFINS a uma alíquota de 3% e configurado com Vlr. Mínimo do Imposto de R$6,46.

Em uma nota cuja base do imposto é R$235,98, aplicando uma alíquota de 3%, chegamos a um valor de COFINS de R$7,08.

Ao proceder com a baixa parcial, informando um valor de R$228,90, temos sobre este a aplicação de 3% do imposto, o sistema efetua de forma interna o seguinte cálculo:

BC = BASE / ((100 – Alíquota) / 100)

BC = 228,90 / ((100-3) / 100)

BC = 228,90 / 0,97

BC = 235,98

Em seguida será feito o seguinte cálculo, para verificar se haverá ou não a retenção do imposto:

I = BC \* Alíquota

I = 235,98 \* 3%

I = R$7,08

**Conclusão:** Como o valor do imposto foi R$7,08, ou seja, maior que o Vlr. Mínimo de Imposto informado no Cadastro de Impostos, na execução da baixa parcial, ocorrerá a retenção do imposto. Ou seja, na tela de Baixa Parcial, na coluna Baixa Corrente, o campo Outros Impostos será alimentado.

**Exemplo 2** - Suponhamos ainda no Cadastro de Impostos, o imposto COFINS a uma alíquota de 3% e configurado com Vlr. Mínimo do Imposto de R$6,46.

Em uma nota cuja base do imposto é R$206,19, aplicando uma alíquota de 3%, chegamos a um valor de COFINS de R$7,08.

Ao proceder com a baixa parcial, informando um valor de R$200,00, temos sobre este a aplicação de 3% do imposto, o sistema efetua de forma interna o seguinte cálculo:

BC = BASE / ((100 – Alíquota) / 100)

BC = 200,00 / ((100-3) / 100)

BC = 200,00 / 0,97

BC = 206,19

Em seguida será efetuado o seguinte cálculo, para verificar se haverá ou não a retenção do imposto:

I = BC \* Alíquota

I = 206,19 \* 3%

I = R$6,18

**Conclusão:** Como o valor do imposto foi R$6,18, ou seja, menor que o Vlr. Mínimo de Imposto informado no Cadastro de Impostos, na execução da baixa parcial, ocorrerá a retenção do imposto. Ou seja, na tela de Baixa Parcial, na coluna Baixa Corrente, o campo Outros Impostos será apresentado zerado.

**Exemplo 3** **-** Suponhamos agora um valor de acerto de R$250,00; na qual foi configurado um Grupo do Valor Mínimo com três impostos, PIS 0,65%, COFINS 3%, e CSLL 1%; além disso, o valor mínimo do grupo de impostos é de R$10,01. Assim, temos:

BC = 250,00 / ((100 - 4,65)/100)

BC = 250,00 / 0,9535

BC = 262,19

I = 262,19 \* 4,65%

I = R$12,19

**Conclusão:** Chegamos no valor de R$12,19, ou seja, maior que o mínimo de R$10,01, assim, haverá retenção. De forma contrária, se este valor fosse menor que R$10,01, não haveria retenção.

**Exemplo 4** **-** Supondo agora que o valor do acerto seja R$300,00; na qual foi configurado  um Grupo Vlr Mínimo dos Impostos PIS - COFINS - CSSL no Valor mínimo de R$10,01 e percentuais de PIS 0,65%, COFINS 3%, e CSSL 1%; além disso, tem-se também o IRRF de 1,5%, com Valor Mínimo de R$10,00.

Deste modo, o sistema irá calcular os impostos separadamente; porém, para achar a Base de Cálculo, em um primeiro momento, soma-se os dois percentuais (4,65% + 1,5%), para chegar na base. Assim, temos:

BC = 300,00 / ((100 - 6,15)/100)

BC = 300,00 / 0,9385

BC = 319,66

I = 319,66 \* 4,65%

I = R$14,86

Chegamos no valor de R$14,86, ou seja, maior que o mínimo de R$10,01, portanto, haverá retenção. De forma contrária, se este valor fosse menor que R$10,01, não haveria retenção.

I = R$ 319,66 \* 1,5%

I = R$ 4,79

Como o valor foi de R$4,79, ou seja, menor que o valor mínimo de R$10,01, portanto, não haverá retenção.

Nesta situação, o sistema irá refazer o cálculo da Base de Cálculo para retenção, pois terá que ignorar a retenção do segundo imposto configurado (IRRF) nesta baixa parcial. Assim, tem-se o cálculo somente considerando o primeiro imposto (grupo PIS - COFINS - CSSL), com alíquota de 4,65%, ou seja:

BC = 300,00 / ((100 - 4,65)/100)

BC = 300,00 / 0,9535

BC = 314,63

I = R$314,63 \* 4,65%

I = R$14,63

**Conclusão:**Chegamos no valor de R$14,63, ou seja, maior que o mínimo de R$10,01, assim, haverá retenção. De forma contrária, se este valor fosse menor que R$10,01, não haveria retenção.

Mesmo sendo configurados dois impostos, somente um superou o valor mínimo. Neste caso, o valor da baixa parcial será de R$314,63 com a retenção do grupo PIS - COFINS - CSSL de R$ 14,63.

#### Preservação da alíquota original nas baixas parciais

Por padrão, ao realizar a baixa parcial de um título com imposto retido, o sistema recalcula o imposto utilizando a alíquota vigente no Cadastro de Impostos. Dessa forma, se a alíquota for alterada após a escrituração do documento, a baixa passa a considerar a nova alíquota, e não aquela usada na geração da movimentação financeira.

Para manter a tributação originalmente calculada, habilite a marcação "Preservar alíquota original da movimentação financeira" no Cadastro de Impostos. Com ela habilitada, a baixa parcial, o título de pendência e o estorno da baixa utilizarão a alíquota gravada na movimentação financeira, independentemente de alterações posteriores no cadastro.

**Nota:** a configuração é aplicada individualmente para cada imposto e não altera o comportamento dos impostos que não a possuírem habilitada.

Para saber mais, acesse o artigo [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834), nas Configurações Iniciais.
