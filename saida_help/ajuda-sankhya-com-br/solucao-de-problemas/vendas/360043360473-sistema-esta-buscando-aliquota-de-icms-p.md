---
id: "360043360473"
titulo: "Sistema está buscando alíquota de ICMS para dentro do Estado, mesmo sendo uma operação para fora do Estado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043360473-Sistema-est%C3%A1-buscando-al%C3%ADquota-de-ICMS-para-dentro-do-Estado-mesmo-sendo-uma-opera%C3%A7%C3%A3o-para-fora-do-Estado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:31Z"
rotulos: ["DUVIDANF", "#PUBLIFER", "#Revisadoclaudio", "Configuração", "Fiscal", "Parceiro", "Impostos", "TOP", "difal", "consumidor", "alíquota", "icms", "contribuinte", "ICMS errado entre UFs", "Configuração incorreta de exceções fiscais", "Ajustar exceções por tipo de consumidor"]
---

# Sistema está buscando alíquota de ICMS para dentro do Estado, mesmo sendo uma operação para fora do Estado

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16115076783255) SITUAÇÃO:**

Lançamentos no sistema onde UF de origem difere da UF de destino, espera-se que o sistema busque a respectiva exceção de ICMS, considerando uma operação para fora do Estado. Porém, essa exceção é ignorada e o lançamento busca informações de exceções para dentro do Estado.

Essa situação, em sua maioria, ocorre quando a Classificação de ICMS do parceiro (Aba **"Fiscal"**) é **Consumidor Final Não Contribuinte**, **Consumidor Contribuinte** ou **Produtor Rural**.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16115061020439) SOLUÇÃO:**

Para analisar e solucionar a situação mencionada acima, compreenda as seguintes regras:

![Imagem 3: Regra Consumidor Contribuinte :](https://ajuda.sankhya.com.br/hc/article_attachments/16115061022359) Regra **Consumidor Contribuinte**:

Primeiro verifica se existe exceção de ICMS para Consumidor Contribuinte fora do estado, se não tiver então verifica se tem exceção para eles dentro do Estado.

Dessa forma, é recomendado que exista a **exceção = Consumidor Contribuinte** para a Origem/Destino desejados, conforme exemplo abaixo:

![Imagem 4: Dessa forma, é recomendado que exista a exceção = Consumidor Contribuinte para a Origem/Destino desejados, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/14598362375575)

![Imagem 5: Regra Consumidor Final :](https://ajuda.sankhya.com.br/hc/article_attachments/16115076788631) Regra **Consumidor Final**:

Caso o Tipo de Operação - TOP utilizado na operação não esteja com a opção **"Calcular DIFAL Partilhado"** localizada na aba **"Impostos"** marcada, ou uma das configurações para cálculo do DIFAL não esteja realizada (Partilhas DIFAL, % de alíquota interna de destino) o sistema irá considerar a alíquota de ICMS de dentro do estado.

De acordo com as marcações citadas acima, utilizará a alíquota interestadual priorizando a exceção para Consumidor independente da hierarquia. Caso não encontre essa exceção, irá considerar a exceção de dentro do estado mais próximo do processo que está sendo negociado.

Dessa forma, é recomendado que exista a **exceção = Consumidor** para a Origem/Destino desejados, conforme exemplo abaixo:

![Imagem 6: Dessa forma, é recomendado que exista a exceção = Consumidor para a Origem/Destino desejados, conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/14598387415959)

![Imagem 7: Regra Produtor Rural :](https://ajuda.sankhya.com.br/hc/article_attachments/16115061026583) Regra **Produtor Rural**:

Verifica-se a exceção de produtor rural de acordo com as UF´s envolvidas, se não encontrar exceção de produtor rural então considera a exceção mais próxima do processo que está sendo negociado dentro ou fora do estado.

Dessa forma, é recomendado que exista a **exceção = Produtor Rural** para a Origem/Destino desejados, conforme exemplo abaixo:

![Imagem 8: Dessa forma, é recomendado que exista a exceção = Produtor Rural para a Origem/Destino desejados, conforme exemplo…](https://ajuda.sankhya.com.br/hc/article_attachments/14598362432407)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16115061027735) CAUSA:**

Situação causada, em sua maioria, pela não configuração específica de exceções de acordo com as classificações fiscais: **Consumidor Final Não Contribuinte**, **Consumidor Contribuinte** ou **Produtor Rural**.
