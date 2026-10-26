---
id: "27960389702423"
titulo: "Caso de uso: ST (substituição tributária) para frete extra-nota, proporcional aos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27960389702423-Caso-de-uso-ST-substitui%C3%A7%C3%A3o-tribut%C3%A1ria-para-frete-extra-nota-proporcional-aos-itens"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:05Z"
rotulos: ["Configuração", "Fiscal", "ICMS", "Impostos", "TOP", "ST", "Caso de uso", "ST (substituição tributária) para frete extra-nota proporcional aos itens"]
---

# Caso de uso: ST (substituição tributária) para frete extra-nota, proporcional aos itens

Confira neste artigo a funcionalidade da marcação **"Calc. ICMS/ST extra nota p/ frete extra nota proporcional aos itens**", presente na TOP - Tipos de Operação e sua sistemática de cálculo ao lançarmos algum documento nos portais.

No artigo [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) há algumas informações sobre a marcação citada, mas não demonstra de forma detalhada o cálculo realizado pelo sistema, quando estamos utilizando essa rotina nos portais. Pois, existem particularidades na memória de cálculo dessa rotina, que serão abordadas a seguir:

Neste documento, há dois itens:

**![Imagem 1: Primeiro tem IPI (R$ 3,50) e também FCP Interno (R$ 3,11) para o ST , além do ST normal do item, com MVA de 50%;](https://ajuda.sankhya.com.br/hc/article_attachments/28000376915991) Primeiro tem IPI** (R$ 3,50) e também **FCP** Interno (R$ 3,11) para o **ST**, além do ST normal do item, com **MVA** de 50%;

**![Imagem 2: Segundo tem apenas o próprio ST do item, com MVA de 70%;](https://ajuda.sankhya.com.br/hc/article_attachments/28000341739159) Segundo tem apenas o próprio ST** do item, com MVA de 70%;

Valores dos itens na tabela de impostos da nota:

- Ambos os itens têm o total de produto na grade de itens igual a R$ 100,00;
- Valor do Frete da nota R$ 100,00;

(1)** Sequência 1**

![Imagem 3: (1) Sequência 1](https://ajuda.sankhya.com.br/hc/article_attachments/27988312821143)

(1)** Sequência 2**

![Imagem 4: (1) Sequência 2](https://ajuda.sankhya.com.br/hc/article_attachments/27988327663767)

![Imagem 5: (1) Sequência 2](https://ajuda.sankhya.com.br/hc/article_attachments/27988449368727)

Para o cálculo dos campos **"Base do ICMS/ST do Frete"** e **"Vlr. ICMS/ST sobre o frete",** o sistema vai seguir a seguinte memória de cálculo:

**(SOMA TOTAL DAS BASES REDUZIDAS DE ST) / (TOTAL DOS ITENS + IPI) \* VALOR DO FRETE**

Aplicando a fórmula aos valores apresentados dos itens, no qual ao somar as bases reduzidas de ST e dividir pela soma total dos itens mais IPI, cria-se um índice de majoração para aplicar ao frete, buscando proporcionalizar nele tudo aquilo que foi aplicado aos itens, no qual se tem:

(325,25) / (203,50) \* 100,00 =  159,83

Este valor de R$ 159,83 será o valor usando no campo Base do ICMS/ST do Frete**.**

Já para encontrarmos o valor do campo Vlr. ICMS/ST sobre o frete, se usa a seguinte memória de cálculo:

**(TOTAL DO VALOR DE ST) / (TOTAL DA BASE REDUZIDA ST) \* BASE DO ICMS/ST DO FRETE**

(19,06 + 18,60) / (325,25) \* 159,83 = 18,51

**Observação:** o valor de R$ 19,06, que é o total de ST do primeiro item, está composto pelo valor do ST do item e também pelo valor do FCP Interno ST do item. Ou seja, de forma indireta, se o item tem FCP ST Interno, o valor do ICMS/ST sobre o frete será cálculo com este tributo também.
