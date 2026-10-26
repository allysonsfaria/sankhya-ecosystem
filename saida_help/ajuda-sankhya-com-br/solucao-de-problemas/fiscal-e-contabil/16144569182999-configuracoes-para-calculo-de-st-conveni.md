---
id: "16144569182999"
titulo: "Configurações para Cálculo de ST - Convênio 142/2018"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16144569182999-Configura%C3%A7%C3%B5es-para-C%C3%A1lculo-de-ST-Conv%C3%AAnio-142-2018"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:55:30Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "Alíquotas de ICMS", "Configuração de ST", "Cálculo conforme Convênio 142/2018", "Convênio 142/2018"]
---

# Configurações para Cálculo de ST - Convênio 142/2018

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18970352093207)**SOLUÇÃO:**

Configuração necessária para que o sistema calcule o valor do ST em nota de venda conforme a resolução do Convênio 142/2018.

Comercial > Arquivo > Cadastros > Alíquotas > Alíquotas de ICMS
 
**Aba:** Geral
Tributação = 10 - Tributada e c/ Cobrança por Substituição
Alíquota = Preenchido com o percentual correspondente
Tipo de Cálculo DIFAL e do FCP = 5 - Cálculo do DIFAL Convênio 142/2018: Vlr. Operação / (1 - Alíq. Interna Destino - Alíq. Interestadual)
Alíq. Interna Destino = Preenchido com o percentual correspondente
 
**Aba:** Substituição Tributária
MVA = Preenchido com a devida margem de valor agregado (caso a operação não tenha MVA, o valor informado deve ser “0,01”, pois assim, essa informação será gerada nas TAGs de XML e os valores do impostos serão calculados conforme necessidade do cliente).
Alíq.Subst. Tributária = Preenchido com o percentual correspondente
Tipo de Cálculo de ST Específico = 7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC)

Cálculo efetuado pelo sistema:
(Vlr da Operação / (1 - (Aliq. Interna - Aliq. Interestadual))) \* (Aliq. Interna - Aliq. Interestadual)
