---
id: "31030523915031"
titulo: "ORA-12899: valor muito grande para a coluna “SANKHYA\"TSIUSU\" *NOMEUSUALTER\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31030523915031-ORA-12899-valor-muito-grande-para-a-coluna-SANKHYA-TSIUSU-NOMEUSUALTER"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:13Z"
rotulos: ["Configuração", "Financeiro", "ORA-12899", "TSIUSU", "valor muito grande para a coluna", "SANKHYA\"TSIUSU\" *NOMEUSUALTER", "Erro", "NOMEUSUALTER", "NOMEUSU"]
---

# ORA-12899: valor muito grande para a coluna “SANKHYA"TSIUSU" *NOMEUSUALTER"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31108825448855) **MENSAGEM:**

ORA-12899: valor muito grande para a coluna “SANKHYA"TSIUSU" \*NOMEUSUALTER"

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31108793574167)**SOLUÇÃO:**

Será necessário que o DBA faça a correção, ajustando o tamanho dos campos para torná-los compatíveis. Caso a empresa não tenha um DBA, a Unidade poderá disponibilizar um profissional para realizar esse ajuste.

![Imagem 3: Será necessário que o DBA faça a correção, ajustando o tamanho dos campos para torná-los compatíveis. Caso a empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/31030523912599)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31030523912983) CAUSA:**

Esse erro ocorre quando a quantidade de caracteres dos campos NOMEUSU e NOMEUSUALTER da tabela TSIUSU são diferentes.

Para verificar a quantidade de caracteres cadastrada em cada campo, acesse a tela **"DBExplorer"**, busque pela tabela TSIUSU e localize os campos NOMEUSU e NOMEUSUALTER. Se os tamanhos forem diferentes, o erro será apresentado.

![Imagem 5: Para verificar a quantidade de caracteres cadastrada em cada campo, acesse a tela "DBExplorer" , busque pela tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/31030498355863)

![Imagem 6: Para verificar a quantidade de caracteres cadastrada em cada campo, acesse a tela "DBExplorer" , busque pela tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/31030523913495)
