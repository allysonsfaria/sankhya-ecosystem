---
id: "16443701402391"
titulo: "Ao gerar o Livro ICMS/IPI de nota de nacionalização, o sistema não está somando o valor do ICMS ao valor contábil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16443701402391-Ao-gerar-o-Livro-ICMS-IPI-de-nota-de-nacionaliza%C3%A7%C3%A3o-o-sistema-n%C3%A3o-est%C3%A1-somando-o-valor-do-ICMS-ao-valor-cont%C3%A1bil"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:55:13Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "ICMS", "Impostos", "CST 00 e Outros CSTs", "Valor do ICMS", "Empresas do Simples"]
---

# Ao gerar o Livro ICMS/IPI de nota de nacionalização, o sistema não está somando o valor do ICMS ao valor contábil

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912686588311) SITUAÇÃO:**

Após cadastrar uma nota de compra de nacionalização e gerar o Livro ICMS/IPI, o valor contábil não condiz com o valor total da nota. A diferença em questão se refere ao valor do imposto ICMS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912674024855) SOLUÇÃO:**

Para que o valor do ICMS seja considerado no valor contábil nas notas cujo CST é diferente de 00, é necessário que a empresa seja optante do Simples Nacional.
 Do contrário, caso a empresa não seja optante do regime, o sistema só irá somar os valores do imposto nas notas que possuem o CST 00.
