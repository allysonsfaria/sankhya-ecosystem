---
id: "27010884310807"
titulo: "ORA-12899: valor muito grande para a coluna \"SANKHYA\".\"TGFEDFDC170\".\"CST_IPI\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27010884310807-ORA-12899-valor-muito-grande-para-a-coluna-SANKHYA-TGFEDFDC170-CST-IPI"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:40:18Z"
rotulos: ["Configuração", "Financeiro", "ORA-12899", "Valor muito grande para a coluna", "valor muito grande para a coluna \"SANKHYA\".\"TGFEDFDC170\".\"CST_IPI\" (real: 3 máximo: 2)", "Erro", "CST_IPI"]
---

# ORA-12899: valor muito grande para a coluna "SANKHYA"."TGFEDFDC170"."CST_IPI"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27119161292951) MENSAGEM:**

ORA-12899: valor muito grande para a coluna "SANKHYA"."TGFEDFDC170"."CST\_IPI" (real: 3, máximo: 2)

Esse é um erro do Oracle que indica que o valor que está sendo inserido "CST\_IPI da tabela ultrapassa o tamanho permitido. A coluna foi modelada para aceitar no máximo 2 caracteres, mas o valor que está sendo fornecido tem 3 caracteres.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27119161298839) SOLUÇÃO:**

**Verifique o valor de CST\_IPI:** o valor que está sendo inserido na coluna CST\_IPI tem que ter no máximo 2 caracteres.

É preciso avaliar o valor nos dados de origem para que ele respeite o limite de 2 caracteres.

Conforme o Guia prático, **o caractere \*(Asterisco)** aposto ao lado do tamanho do campo **indica que o campo deve ser informado com aquela quantidade exata de caracteres.**

![Imagem 3: Conforme o Guia prático, o caractere *(Asterisco) aposto ao lado do tamanho do campo indica que o campo deve ser…](https://ajuda.sankhya.com.br/hc/article_attachments/27119297112471)

Na tabela no banco de dados o campo aceita 2 caracteres.

![Imagem 4: Na tabela no banco de dados o campo aceita 2 caracteres.](https://ajuda.sankhya.com.br/hc/article_attachments/27119297115031)

É necessário pegar um monitor de consultas para identificar o número da nota que está acontecendo o problema e corrigir na raiz.
