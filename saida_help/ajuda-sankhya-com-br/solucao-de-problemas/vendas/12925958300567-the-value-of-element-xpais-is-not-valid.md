---
id: "12925958300567"
titulo: "The value \" of element 'xPais' is not valid "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12925958300567-The-value-of-element-xPais-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:00:37Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Erro de validação XML; valor inválido para 'xPais'", "Verifique estado e código do país; edite e salve informações", "Código do país não informado na tela de cadastro de estados", "Erro", "País"]
---

# The value " of element 'xPais' is not valid 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17147654686231) MENSAGEM:**

Erro durante validacao do XML do lote: cvc-pattern-valid: Value " is not facet-valid with respect to pattern I-Mill -MO.} p-yll111[!-A{1}' for type 1#AnonType\_xPaisTEnderecol. cvc type.3.1.3: The value " of element 'xPais' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17147654688791) SOLUÇÃO:**

![Imagem 3: Identifique qual o estado referente a nota apresentada na rejeição na tela de cadastro de estados;](https://ajuda.sankhya.com.br/hc/article_attachments/17147642330647) Identifique qual o estado referente a nota apresentada na rejeição na tela de cadastro de estados;

![Imagem 4: Informe o código do país em questão;](https://ajuda.sankhya.com.br/hc/article_attachments/17147654696983) Informe o código do país em questão;

![Imagem 5: Redigite alguma informação no cabeçalho da nota (por exemplo código do parceiro);](https://ajuda.sankhya.com.br/hc/article_attachments/17147642335383) Redigite alguma informação no cabeçalho da nota (por exemplo código do parceiro);

![Imagem 6: Salve;](https://ajuda.sankhya.com.br/hc/article_attachments/17147642337815) Salve;

![Imagem 7: Gere lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/17147654705047) Gere lote novamente.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17147654709399) CAUSA:**

O erro ocorre quando o código do País informado na tela de cadastro de estado não está informado, assim não levando o conteúdo para o xml da nota.
