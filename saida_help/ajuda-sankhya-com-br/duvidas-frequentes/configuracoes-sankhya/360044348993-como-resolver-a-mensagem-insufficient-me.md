---
id: "360044348993"
titulo: "Como resolver a mensagem Insufficient memory for this operation"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044348993-Como-resolver-a-mensagem-Insufficient-memory-for-this-operation"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:10Z"
rotulos: ["Configuração", "MGE", "Mitra", "Resolução de Erro de Memória", "Erro", "BDE"]
---

# Como resolver a mensagem Insufficient memory for this operation

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17145518733463) SITUAÇÃO:**

Ao tentar acessar o sistema MGE/Mitra, apresenta a mensagem: Insufficient memory for this operation e ocorre quando o Alias do BDE não está com memoria suficiente para processar operação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17145489440023) SOLUÇÃO:**

Acesse o Menu Iniciar do computador e busque por BDE. Clique no mesmo com botão direito >> Executar como administrador.

Aberto o BDE, ajuste os campos conforme abaixo:

**(1)**Aba **"Databases"**:

**BLOB SIZE**: 999 (máximo)

**BLOBS TO CACHE**: 1000

Pode aumentar de 1000 em 1000 até não mais apresentar o erro. O mesmo vale caso o valor neste campo esteja muito alto, ir abaixando ate que o erro não ocorra mais.

**(1)** Aba **"Configuration > System > Init"**:

**SHAREDMEMSIZE** = 4096

Salve as alterações e teste o acesso novamente.
