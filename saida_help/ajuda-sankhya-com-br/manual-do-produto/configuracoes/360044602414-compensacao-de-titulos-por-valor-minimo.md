---
id: "360044602414"
titulo: "Compensação de Títulos por Valor Mínimo do Imposto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602414-Compensa%C3%A7%C3%A3o-de-T%C3%ADtulos-por-Valor-M%C3%ADnimo-do-Imposto"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:52:34Z"
rotulos: ["Alíquotas", "Configuração", "Empresa", "Parceiro", "Impostos", "Compensação", "Financeiro", "Imposto", "Mínimo", "RETOUTROSIMP", "Valor", "Compensação de Títulos por Valor Mínimo do Imposto manual", "Títulos", "Compensação de Títulos por Valor Mínimo do Imposto"]
---

# Compensação de Títulos por Valor Mínimo do Imposto

As configurações realizadas na tela [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos), por meio das abas [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaparceiro), [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abatop) e [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaempresa), permitem o destaque dos impostos na nota, bem como a configuração das devidas retenções. As informações abaixo, demonstram como acontece a compensação de títulos que contenham retenções a serem calculadas na baixa. O sistema calculará automática e internamente, o valor dos impostos a serem retidos, fazendo que o valor da compensação seja o valor líquido a ser baixado com o outro título (que não tenha retenção).

**1°:** Caso as configurações realizadas na tela Impostos tenham sido definidas para que se tenha retenção no Financeiro, não haverá retenção na nota. A cada valor a ser pago (valor de desdobramento), o sistema calcula o valor do imposto a ser retido, e verifica se este é igual ou maior que o mínimo exigido; se sim, haverá a retenção na compensação; se não, não haverá retenção.

A retenção parcial será aceita se o parâmetro **"Retem outros impostos - RETOUTROSIMP"** estiver ativado.

Na compensação, o **"Valor Acerto"** definido pelo usuário, será acrescentado pelo sistema, do imposto a ser retido. Assim, o cálculo será feito internamente da seguinte forma:

Valor Acerto / ((100-X)/100) à Valor Acerto / Resultado;

onde:

X = alíquota do imposto a ser retido.

Assim, suponhamos que o Valor do Acerto seja R$ 228,90 e para este, deve haver uma retenção de COFINS de 3%, com valor mínimo do imposto de R$ 6,46:

= 228,90 / ((100-3)/100)

= 228,90 / 0,97

= 235,98

Ocorrerá a compensação mesmo que os valores a serem reparados sejam maiores que R$ 235,98.

R$ 235,98 x 3% = R$ 7,08 (maior que o mínimo R$ 6,46 - haverá retenção)

**2°:** Se existir mais de um imposto configurado por valor mínimo, será feito este mesmo cálculo somando o percentual de todos eles, para obter-se a base de cálculo. Após a obtenção da base de cálculo, o sistema irá calcular cada imposto e verificar quais deles sofrerão retenção e quais não, conforme comparação entre o valor obtido e o valor mínimo configurado.

Na compensação, o **"Valor Acerto"** definido pelo usuário, deverá ser acrescentado pelo sistema, dos impostos a serem retidos. Assim, o cálculo - por grupo do valor mínimo - será feito internamente, da seguinte maneira:

Valor Acerto / ((100-X)/100) à Valor Acerto / Resultado;

onde:

X = alíquota do imposto a ser retido.

Dessa forma, suponhamos que o Valor do Acerto seja R$ 228,90 e para este tenha-se uma retenção de 0,65% de PIS e valor mínimo de R$ 1,40; 3% de COFINS e valor mínimo de R$ 6,46; e 1% de CSLL e valor mínimo de R$ 2,15; todos compondo o grupo PCC; assim, o grupo PCC terá alíquota de 4,65% e valor mínimo do imposto de R$ 10,01:

= 228,90 / ((100-4,65)/100))

= 228,90 / 0,9535

= 240,06

Haverá a compensação, mesmo se os valores a serem compensados forem maiores que R$ 240,06. Haverá retenção, apenas se o valor dos impostos do grupo por valor mínimo calculado pelo sistema, for maior que aquele definido na configuração para o grupo do valor mínimo do imposto, conforme abaixo:

R$ 240,06 x 4,65% = R$ 11,16 (maior que o mínimo R$ 10,01 - haverá retenção)

**3°:** Se houver mais de um imposto, alguns compondo o grupo e outros não, o grupo será considerado como um único imposto e os demais, também com um imposto independente.

Sendo assim, o sistema irá somar internamente todos os percentuais para obter a base de cálculo com os impostos. Depois de calculada esta base de cálculo, ele irá calcular cada um destes impostos e comparar com seu mínimo exigido. Sendo maior ou igual, o sistema armazenará o mesmo para compor a base de cálculo e a retenção; se não, não irá armazenar, pois ele não irá ser objeto de retenção.

O sistema irá armazenar os impostos, verificar se são maiores que o valor mínimo e se possuem valor maior que a base de cálculo (valor do acerto com os impostos a serem retidos internamente); somente se estas duas situações acontecerem, a compensação ocorrerá para valores com impostos a serem retidos no Financeiro.

Assim, considere que determinado serviço possui um Financeiro no valor de R$ 228,90 e está em um grupo de valor mínimo do imposto PCC com alíquota de 4,65% e Vr. Mínimo de R$ 10,01 - onde há retenção de 0,65% de PIS e valor mínimo de R$ 1,40; 3% de COFINS e valor mínimo de R$ 6,46; e 1% de CSLL e valor mínimo de R$ 2,15; este mesmo produto, possui um imposto por valor mínimo IR, com percentual de 1,5% e valor mínimo igual a R$ 10,01.

Assim, o sistema efetuará o seguinte cálculo:

Valor Acerto / ((100-X)/100) à Valor Acerto / Resultado;

onde:

X = alíquota do(s) imposto(s) a ser retido.

= R$ 228,90 / ((100-6,15)/100)

= R$ 228,90 / 0,9385

= R$ 243,90

R$ 243,90 x 4,65% = R$ 11,34 - é maior que R$ 10,01 - Retém (Grupo por valor mínimo do imposto – todos do grupo somados como se fossem um único imposto);

R$ 243,90 x 1,50% = R$ 3,66 - é menor que R$ 10,01 - Não Retém (Imposto por valor mínimo do imposto).

Neste caso, o sistema irá desprezar um dos impostos (o que não deu retenção) para compor novamente a base, e verificar se há imposto:

= R$ 228,90 / ((100-4,65)/100)

= R$ 228,90 / 0,9535

= R$ 240,06

R$ 240,06 x 4,65% = R$ 11,16 - é maior que R$ 10,01 - Retém (Grupo por valor mínimo do imposto).

Assim, o crédito deve ser maior ou igual a R$ 240,06 para que se tenha a compensação. Sendo que esta compensação terá R$ 11,16 de valor retido devidamente.

**Observação:** ao proceder com a compensação, as regras de tal procedimento serão modificadas apenas em relação ao recálculo dos outros impostos no financeiro de origem de despesa, a recomposição do valor de desdobramento dos novos financeiros que foram gerados, sendo incluso a retenção dos outros impostos.

O sistema conta com uma regra para chegar ao valor de desdobramento e não perder no arredondamento de valores para obtenção do valor líquido e valor de desdobramento correto, ou seja, no momento da compensação, os títulos que compõem o acerto, somados devem ter o valor de desdobramento igual ao título original.

Considere, por exemplo, que para uma Despesa com valor de desdobramento de R$1.000,00 e Receita de R$ 600,00, serão gerados dois títulos de despesas, um de R$ 600,00 e outro de R$ 400,00, que somados possuem o mesmo valor de desdobramento do título original; e devem também ter o mesmo valor líquido.
