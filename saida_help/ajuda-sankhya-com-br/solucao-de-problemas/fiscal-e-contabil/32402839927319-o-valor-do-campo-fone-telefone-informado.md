---
id: "32402839927319"
titulo: "O valor do campo fone (Telefone) informado não é valido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32402839927319-O-valor-do-campo-fone-Telefone-informado-n%C3%A3o-%C3%A9-valido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:31:27Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "Parceiro", "XML", "Parceiros", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Fone", "Telefone informando não é válido", "Squad Docs"]
---

# O valor do campo fone (Telefone) informado não é valido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32402824245655) **MENSAGEM:**

O valor do campo fone (Telefone) informado não é valido

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32402824247831)SOLUÇÃO:**

**(1)** Gere o ''**XML''** do ''**MDF-e''**, e verifique se a tag **''Fone''** está sendo gerada corretamente.

**(2)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(3)** Verifique o cadastro correto de telefone e também no cadastro da Empresa.

**(4)** Caso o telefone não esteja informado, inclua o número de contato corretamente para que a tag seja gerada:

![Imagem 3: (4) Caso o telefone não esteja informado, inclua o número de contato corretamente para que a tag seja gerada:](https://ajuda.sankhya.com.br/hc/article_attachments/38803026770583)

**OBSERVAÇÃO:** Não utilize caracteres especiais, espaços ou traços no número de telefone.

**(5)** Após corrigir e/ou incluir o telefone, gere novamente o lote da nota.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32402824253335)CAUSA:**

O erro acontece quando o número de telefone do parceiro ou da empresa **não está cadastrado** ou **contém caracteres especiais**, como espaços, traços ou símbolos.
