---
id: "360043577354"
titulo: "Código de produto ou Código da unidade não encontrados para alguns itens do XML ou o XML contém produtos que utilizam controle adicional de estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577354-C%C3%B3digo-de-produto-ou-C%C3%B3digo-da-unidade-n%C3%A3o-encontrados-para-alguns-itens-do-XML-ou-o-XML-cont%C3%A9m-produtos-que-utilizam-controle-adicional-de-estoque"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:57Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "NF-e", "XML", "Estoque", "Código de Produto", "Importação de XML", "Unidade de Medida"]
---

# Código de produto ou Código da unidade não encontrados para alguns itens do XML ou o XML contém produtos que utilizam controle adicional de estoque

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16192773291927) MENSAGEM**:

Código de produto ou Código da unidade não encontrados para alguns itens do XML ou o XML contém produtos que utilizam controle adicional de estoque.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16192780000407) SOLUÇÃO**:

Identifique no DANFE/XML da nota de compra quais são as unidades dos produtos (Ex.: UN, CX, PC, TN, etc.). 

![Imagem 3: Acesse o cadastro dos "Produtos" (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), identifique o…](https://ajuda.sankhya.com.br/hc/article_attachments/16192780003991) Acesse o cadastro dos **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), identifique o campo: **"Unid. Compra"** e verifique se a Unidade de Compra corresponde com a Unidade dos produtos no XML da Nota de Compra.

![Imagem 4: Acesse o cadastro dos "Produtos" (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), identifique o…](https://ajuda.sankhya.com.br/hc/article_attachments/14679401935255)

![Imagem 5: Caso a compra foi em Unidade Alternativa, acesse a aba: Unidades Alternativas do cadastro de produtos e verifique se a…](https://ajuda.sankhya.com.br/hc/article_attachments/16192780006039) Caso a compra foi em Unidade Alternativa, acesse a aba: **Unidades Alternativas** do cadastro de produtos e verifique se a unidade alternativa está cadastrada e ativa.

![Imagem 6: Caso a compra foi em Unidade Alternativa, acesse a aba: Unidades Alternativas do cadastro de produtos e verifique se a…](https://ajuda.sankhya.com.br/hc/article_attachments/14679389606679)

![Imagem 7: Após os ajustes, volte na Importação de XML e vincule o código do produto juntamente com a unidade cadastrada no…](https://ajuda.sankhya.com.br/hc/article_attachments/16192780008343) Após os ajustes, volte na Importação de XML e vincule o código do produto juntamente com a unidade cadastrada no sistema e que seja igual à unidade do XML.

**![Imagem 8: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16192806855063) CAUSA**:

Ocorre quando a Unidade do XML da Compra não é igual à Unidade de Compra dos Produtos ou Unidade Alternativa.
