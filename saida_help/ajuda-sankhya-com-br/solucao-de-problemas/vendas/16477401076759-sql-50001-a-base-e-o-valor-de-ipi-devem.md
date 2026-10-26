---
id: "16477401076759"
titulo: "SQL-50001 - A base e o valor de IPI devem ser zero (0) para o produto: XXXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16477401076759-SQL-50001-A-base-e-o-valor-de-IPI-devem-ser-zero-0-para-o-produto-XXXXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:55:09Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "Valor de IPI deve ser zero para o produto", "IPI não está marcado no cadastro do produto", "Ajuste o campo \"Tem IPI\" no cadastro do produto e reimporte o XML"]
---

# SQL-50001 - A base e o valor de IPI devem ser zero (0) para o produto: XXXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16477401056023)  MENSAGEM:**

SQL-50001 - A base e o valor de IPI devem ser zero (0) para o produto: XXXXXX.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16477354888471) CAUSA:**

Ocorre devido ao cadastro do Produto a opção do **IPI** estar desmarcada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16477371917463) SOLUÇÃO:**

-  Verifique se no XML o produto possui IPI;

![Imagem 4: No cadastro do Produto pode ser que o produto tenha informações do valor de IPI, porém no cadastro do produto não está…](https://ajuda.sankhya.com.br/hc/article_attachments/16481289986583)  No cadastro do Produto pode ser que o produto tenha informações do valor de IPI, porém no cadastro do produto não está marcado para **"Calcular IPI"**. Esse processo vale para ambos (compra e venda). Então acesse:

**(2)** Configurações » Cadastros » Produtos » Produtos:

**(3)**Aba **"Imposto"**, campo **"Tem IPI"**

![Imagem 5: (3) Aba "Imposto" , campo "Tem IPI"](https://ajuda.sankhya.com.br/hc/article_attachments/16480663297815)

![Imagem 6: Verifique se na aba Impostos / Informações por empresa possui cadastro para empresa que está sendo importado XML.](https://ajuda.sankhya.com.br/hc/article_attachments/16481281863063)  Verifique se na aba **Impostos / Informações por empresa** possui cadastro para empresa que está sendo importado XML.

Se essa aba estiver preenchida deverá ser preenchido também as configurações dos impostos pois a mesma sobrepõe as informações da aba **Impostos**.

**(2)** Configurações » Cadastros » Produtos » Produtos:

**(3)**Aba **Impostos / Informações por empresa** campo**: "**IPI na Entrada" "IPI na Saída"

![Imagem 7: (3) Aba Impostos / Informações por empresa campo : " IPI na Entrada" "IPI na Saída"](https://ajuda.sankhya.com.br/hc/article_attachments/16481012874647)

![Imagem 8: (3) Aba Impostos / Informações por empresa campo : " IPI na Entrada" "IPI na Saída"](https://ajuda.sankhya.com.br/hc/article_attachments/16481290015895) Após realizar os ajustes deverá importar o XML novamente e Processar Arquivo.
