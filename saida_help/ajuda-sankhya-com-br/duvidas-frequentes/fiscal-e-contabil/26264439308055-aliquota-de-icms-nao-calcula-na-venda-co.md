---
id: "26264439308055"
titulo: "Alíquota de ICMS NÃO calcula na VENDA. \"Cód. Alíq. ICMS\" vazio ou zerado ( IDALIQICMS )"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26264439308055-Al%C3%ADquota-de-ICMS-N%C3%83O-calcula-na-VENDA-C%C3%B3d-Al%C3%ADq-ICMS-vazio-ou-zerado-IDALIQICMS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:42:55Z"
rotulos: ["Produtos", "Configuração", "ICMS", "Impostos", "TOP", "Venda Mais"]
---

# Alíquota de ICMS NÃO calcula na VENDA. "Cód. Alíq. ICMS" vazio ou zerado ( IDALIQICMS )

Durante o lançamento de algum documento no Portal de Venda e ao lançar o item na grade de itens, nota-se que o campo "Cód. Alíq. ICMS" fica vazio, ou até zerado, e não chega em nenhum cálculo de ICMS, ou apresenta situações não previstas no lançamento, sobre isso falaremos a seguir.

#### **(1)** Cenário 1:

Se ao lançar o item nas centrais a CST ficar como **41 - Não tributada** e o campo **"Cód. Alíq. ICMS"** ficar vazio, analise na configuração do produto a marcação **"Tem ICMS"** (Aba Impostos, Ou, Impostos / Informações por empresa). Provavelmente a marcação está desativada, pois esse é o cenário no qual todas as marcações estão realizadas. Nesse caso, só falta essa marcação para o cálculo acontecer.

#### **(1)** Cenário 2:

Se ao salvar o item na grade de itens, o sistema chegar a algum **"Cód. Alíq. ICMS"** porém os campos: "**Base, alíquota e valor" ficarem zerados**, mesmo havendo configurações na regra encontrada pelo sistema, pode ser que a TOP está ou estava com a marcação **"Tem ICMS"** desativada. Desse modo,  é necessário ativar, E/OU relançar a nota, pois esse é o cenário em que todas as marcações estão realizadas, e só falta essa marcação para o cálculo acontecer.

#### **(1)** Cenário 3:

Se ao salvar o item na nota, tanto o campo **"Cód. Alíq. ICMS"** quanto o campo **"Tributação" (CST do ICMS) ficarem vazios,** é sinal que a marcação **"Calcula ICMS?:"** (nas preferências da empresa - comercial) está desativada. Pois esse é o cenário em que todas as marcações estão realizadas e só falta essa marcação para o cálculo acontecer.

#### **(1)** Cenário 4:

 Se ao incluir o item na nota, o campo **"Tributação"** (CST do ICMS) fica **diferente** da informação que está na configuração do **"Cód. Alíq. ICMS"** encontrado pelo sistema, normalmente é sinal que no cadastro do Parceiro, o campo **"Classificação ICMS"** está marcado como **"Isento de ICMS".**

#### **(1)** Cenário 5:

Quando a operação for **dentro do estado** e o **"Cód. Alíq. ICMS"** encontrado pelo sistema tem configurações para cálculo do **ICMS-ST,** como:

1. CST = 10-Tributada e c/cobrança por substituição
2. Alíquotas de ICMS, ICMS-ST, MVA, etc.

Ou seja, tudo para haver o cálculo do ST na operação, mas, o sistema lança na grade de itens o campo **"Tributação" (CST do ICMS)** como **"60-ICMS cobrado anteriormente por substituição"** e **zera** todos os campos de: Base ICMS, alíquota ICMS, valor ICMS, base substituição e valor de substituição… tem-se o comportamento da marcação no cadastro de **"Produtos"**, campo **"Tipo de substituição:"** igual a **"Revenda com subst. Tributária (cálculo de Subst. Na compra)".** Isso porque uma vez que há o cálculo do ST, apenas na entrada, automaticamente na saída o sistema não deve proceder com o cálculo, se de fato há a necessidade de se fazer esse cálculo, altere essa configuração para **"subst. Na compra e na venda"**

#### **(1)** Cenário 6:

Se ao salvar o item na grade de itens, o sistema grava o campo **"Cód. Alíq. ICMS"** igual a **ZERO** e o campo **"Tributação" (CST do ICMS)** igual a **"00-Tributada integralmente",** pode ser que o código da UF vinculada à cidade do parceiro ou da empresa não seja o mesmo código de UF que há cadastrado na tela Alíquotas de ICMS. Situação comum acontece quando, de forma errada, são criados **Estados** e **Cidades** repetidos na base e estes cadastros são vinculados ao parceiro ou a empresa da nota.
