---
id: "360043127333"
titulo: "The value 'NOME DO PRODUTO' of element 'xProd' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043127333-The-value-NOME-DO-PRODUTO-of-element-xProd-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:15Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "XML", "SEFAZ", "Valor Inválido na Descrição do Produto", "Erro"]
---

# The value 'NOME DO PRODUTO' of element 'xProd' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482676255127) MENSAGEM:**

The value 'NOME DO PRODUTO

NOME DO PRODUTO

NOME DO PRODUTO' of element '**xProd**' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482676263191) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16482652624023) Acesse: Configurações » Cadastros » Produtos » Produtos

Campo **"Descrição":** Limpe totalmente o campo e digite novamente a descrição do item, sem espaço no início/fim e sem dar 'Enter' para não criar 'quebras de linhas'].

- **Exemplo** de como o XML é montado quando há quebra de linha na descrição:

![Imagem 4: Exemplo de como o XML é montado quando há quebra de linha na descrição:](https://ajuda.sankhya.com.br/hc/article_attachments/360060882593)

- **Exemplo** aceito pela SEFAZ

![Imagem 5: Exemplo aceito pela SEFAZ](https://ajuda.sankhya.com.br/hc/article_attachments/360060882613)

![Imagem 6: Após o ajuste, redigite o cabeçalho da nota e gere um novo lote ou fature novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16482676285975) Após o ajuste, redigite o cabeçalho da nota e gere um novo lote ou fature novamente.

![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482676291223) **CAUSA:**

Ocorre quando a Descrição do cadastro do Produto possui Enter na sua descrição, caracteres especiais ou espaço em branco no início e fim da descrição também são causadores da rejeição.
