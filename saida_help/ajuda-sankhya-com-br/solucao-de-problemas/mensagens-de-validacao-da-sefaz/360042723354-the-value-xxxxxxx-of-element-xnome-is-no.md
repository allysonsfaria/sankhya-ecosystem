---
id: "360042723354"
titulo: "The value 'XXXXXXX' of element 'xNome' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723354-The-value-XXXXXXX-of-element-xNome-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:54Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoBraga", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "Valor Inválido para Nome", "Erro"]
---

# The value 'XXXXXXX' of element 'xNome' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16511664278039) MENSAGEM:**

cvc-pattern-valid: Value 'XXXX' is not facet-valid with respect to pattern '[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}' for type '#AnonType\_xNomeTLocal'.
cvc-type.3.1.3: The value 'XXXXXXX' of element '**xNome**' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16511664282903) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Para correção, siga os passos abaixo: Identifique na mensagem/rejeição retornada a qual cadastro refere-se a descrição…](https://ajuda.sankhya.com.br/hc/article_attachments/16511676909463) Identifique na mensagem/rejeição retornada a qual cadastro refere-se a descrição do nome mencionado.

- No exemplo: The value **'XXXXXXX'** of element **'xNome**' is not valid, a descrição rejeitada trata-se do 'XXXXXXX'.

![Imagem 4: Acesse a tela " Parceiros " (Caminho de acesso: Configurações » Cadastros ).](https://ajuda.sankhya.com.br/hc/article_attachments/16511676912919)Acesse a tela **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso: Configurações » Cadastros).

![Imagem 5: Busque pelo cadastro mencionado na rejeição, conforme identificado no item 1.](https://ajuda.sankhya.com.br/hc/article_attachments/16511676919063) Busque pelo cadastro mencionado na rejeição, conforme identificado no item 1.

![Imagem 6: Para os campos " Nome Parceiro" e 'Razão Social" apague toda a informação digitada e digite novamente. Certifique-se…](https://ajuda.sankhya.com.br/hc/article_attachments/16511676925719) Para os campos "**Nome Parceiro"** e **'Razão Social"** apague toda a informação digitada e digite novamente. Certifique-se que não existe espaço em branco no início da descrição e evite ctrl+c, ctrl+v, para não copiar espaços ou caracteres indevidos:

![Imagem 7: Para os campos " Nome Parceiro" e 'Razão Social" apague toda a informação digitada e digite novamente. Certifique-se…](https://ajuda.sankhya.com.br/hc/article_attachments/14610996920343)

![Imagem 8: Realizado o ajuste, busque autorização para que a NF-e fique 'Aguardando Correção', posteriormente, redigite a…](https://ajuda.sankhya.com.br/hc/article_attachments/16511676927383) Realizado o ajuste, busque autorização para que a NF-e fique 'Aguardando Correção', posteriormente, redigite a informação 'Parceiro' no cabeçalho da nota e gere um novo lote.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16511664301591) CAUSA:**

Rejeição apresentada quando a descrição de determinado 'Nome' enviado nas tag's do XML possuem espaço em branco, duplicidade de informações e/ou caracteres especiais.

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16511676934295) OBSERVAÇÃO:**

Verificar o parâmetro **"RAZDESTINADANFE-Razão Social do destinatário p/impressão no DANFE"**, caso esteja com a opção 'Razão Social e Nome', levará as duas informações no DANFE e caso seja extenso demais o nome e razão social, irá extrapolar o limite do campo no XML.
