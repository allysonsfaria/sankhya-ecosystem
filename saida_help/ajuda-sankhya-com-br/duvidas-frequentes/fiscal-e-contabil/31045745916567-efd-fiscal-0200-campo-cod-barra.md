---
id: "31045745916567"
titulo: "EFD Fiscal - 0200 | Campo COD_BARRA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31045745916567-EFD-Fiscal-0200-Campo-COD-BARRA"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:33:49Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "EFD", "0200", "Campo COD_BARRA", "EAN/GTIN Produto p/ NF-e", "EFD Fiscal"]
---

# EFD Fiscal - 0200 | Campo COD_BARRA

Confira nesse artigo, as regras sistêmicas de construção do campo COD\_BARRA do registro 0200 do EFD Fiscal (ICMS/IPI)

O principal cadastro, no qual o sistema aplica as regras de validações, é feito na tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos), aba **"Impostos",**campo **"EAN/GTIN Produto p/ NF-e"**

![Imagem 1: O principal cadastro, no qual o sistema aplica as regras de validações, é feito na tela "Produtos" (Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/31045745914775)

![Imagem 2: O sistema inicia a validação, verificando se no campo EAN/GTIN Produto p/ NF-e foi escolhida a opção "Código do…](https://ajuda.sankhya.com.br/hc/article_attachments/31281274812439) O sistema inicia a validação, verificando se no campo EAN/GTIN Produto p/ NF-e foi escolhida a opção **"Código do Produto"**, se sim, será utilizado o código do produto, e nenhuma outra validação será realizada;

![Imagem 3: Por outro lado, se e a opção selecionada for "Referência" OU "Cód.Barras da Unid.Alternativa ou a Referência" o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/31281274813463) Por outro lado, se e a opção selecionada for **"Referência" OU "Cód.Barras da Unid.Alternativa ou a Referência"** o sistema validará:

**(2)**Se a versão do layout do txt é 15 ou superior;

**(2)**Se o item em questão está presente em algum documento do C100 e C170, pois nessa situação algum código de barras deve ter sido lançado na nota, onde no campo TGFITE.GTINNFE deve ter alguma informação;

**(2)**Deve estar marcado para gerar o registro 0220 e ter alguma unidade alternativa no cadastro do produto. Então, se essas três sub-validações forem satisfeitas, o sistema verificará qual unidade alternativa foi gerada no 0220 e no cadastro de Unidades Alternativas, qual opção está marcada para busca do GTIN e vai comparar se é igual ao que foi utilizado no documento C100/C170:

![Imagem 4: (2) Deve estar marcado para gerar o registro 0220 e ter alguma unidade alternativa no cadastro do produto. Então, se…](https://ajuda.sankhya.com.br/hc/article_attachments/31045768924695)

Se essa validação de "igualdade" entre o que está atualmente no cadastro de unidades alternativas e o que foi lançado na nota baterem, o sistema verificará se o parâmetro **"LIVUSACODBARALT"** está ligado. Caso esteja, aplicará no campo de código de barras do 0200 a informação que estiver atualmente no campo **"Código de barras"** da unidade alternativa. No entanto, se o parâmetro estiver desligado, o sistema vai pegar o que está no campo **"Referência"** do cadastro de Produto.

**(1)** **Se as validações do tópico 2 não forem satisfeitas**, o sistema valida se algum GTIN foi usado nas notas (TGFITE.GTINNFE) do produto. Também, se na tela Produtos, aba Impostos, campo EAN/GTIN Produto p/ NF-e está selecionada a opção **"Código de Barras Estoque" OU "Cód.Barras da Unid.Alternativa ou a Referência".** Sendo satisfeitas essas últimas validações, será usado como código de barras do 0200 o que foi usado nos documentos presentes no C100/C170.

**(1)** Em contrapartida, se nenhuma das validações acima forem satisfeitas, o sistema deixará o campo vazio.
