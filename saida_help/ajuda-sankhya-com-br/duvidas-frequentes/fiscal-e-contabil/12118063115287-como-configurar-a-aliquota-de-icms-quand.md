---
id: "12118063115287"
titulo: "Como configurar a alíquota de ICMS quando o CST for \"51 - Diferimento\" e o valor do imposto for repassado como desconto para o parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12118063115287-Como-configurar-a-al%C3%ADquota-de-ICMS-quando-o-CST-for-51-Diferimento-e-o-valor-do-imposto-for-repassado-como-desconto-para-o-parceiro"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:01:18Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "ICMS", "Impostos", "Alíquota de ICMS CST 51", "Cadastro regra", "Desconto <vProd> diferimento <vICMSDif>."]
---

# Como configurar a alíquota de ICMS quando o CST for "51 - Diferimento" e o valor do imposto for repassado como desconto para o parceiro

Caso a Tributação seja "51 - Diferimento" e o parceiro possua benefício fiscal, no qual o valor do ICMS será repassado como desconto, indique o percentual diferido no campo "% de Outorga/Diferimento" no cadastro da regra de alíquota. E na aba **"Repassar para o Cliente",** marque a opção **"Redução do Imposto"** para que o sistema desconte o valor do ICMS nos produtos da nota.

[GIF animado: Imagem 1: Caso a Tributação seja "51 - Diferimento" e o parceiro possua benefício fiscal, no qual o valor do ICMS será repassado…](https://ajuda.sankhya.com.br/hc/article_attachments/12118055332119)

Na geração do XML, o sistema aplica o desconto no valor do ICMS diretamente na tag <vProd> dos itens e na tag <vICMSDif> irá constar o valor do diferimento. Caso o diferimento seja de 100%, no total dos impostos a tag <vICMS> deverá estar zerada.

![Imagem 2: Na geração do XML, o sistema aplica o desconto no valor do ICMS diretamente na tag <vProd> dos itens e na tag…](https://ajuda.sankhya.com.br/hc/article_attachments/12118056595223)

![Imagem 3: Na geração do XML, o sistema aplica o desconto no valor do ICMS diretamente na tag <vProd> dos itens e na tag…](https://ajuda.sankhya.com.br/hc/article_attachments/12118057187863)
