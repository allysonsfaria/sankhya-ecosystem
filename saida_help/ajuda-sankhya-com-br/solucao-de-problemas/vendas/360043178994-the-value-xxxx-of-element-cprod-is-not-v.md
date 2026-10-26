---
id: "360043178994"
titulo: "The value 'XXXX 'of element 'cProd' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178994-The-value-XXXX-of-element-cProd-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:52Z"
rotulos: ["#PUBLIFER", "Produtos", "Configuração", "NF-e", "XML", "SEFAZ", "Valor 'XXXX ' inválido para 'cProd'.", "NF-e com erro na tela", "Corrija o campo \"Cód. Produto\" remova espaços e gere novo lote", "Erro"]
---

# The value 'XXXX 'of element 'cProd' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16148080083735) MENSAGEM:**

cvc-pattern-valid: Value 'XXXX ' is not facet-valid with respect to pattern '[!-y]{1}[ -y]{0,}[!-y]{1}|[!-y]{1}' for type '#AnonType\_cProdproddetinfNFeTNFe. cvc-type.3.1.3: The value 'XXXX 'of element 'cProd' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16148066056343) SITUAÇÃO:**

Ao realizar  emissão de NF-e pela tela Central de Vendas no SankhyaW, a nota ficará com Status: 'Aguardando Correção'. Acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da rejeição a seguir.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16148080091543) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: tela "Produtos" ( Caminho de acesso: Configurações » Cadastros » Produtos )](https://ajuda.sankhya.com.br/hc/article_attachments/16148080092567) Acesse: tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos)

- Aba **Impostos** » Campo **"Cód. Produto p/ NF-e/NFC-e/CF-e":**

![Imagem 5: Aba Impostos » Campo " Cód. Produto p/ NF-e/NFC-e/CF-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/14633770550935)

Caso esse esteja definido como "Referência", busque pelo campo **"Referência"** na aba **Geral** e certifique-se que essa informação foi inserida corretamente. Verifique possíveis espaços em branco antes ou após a informação inserida, e existindo apague os mesmos e salve as alterações.

![Imagem 6: Realizado ajuste, conforme item anterior, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16148080097687) Realizado ajuste, conforme item anterior, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16148066075031) CAUSA:**

Mensagem apresentada quando enviado na tag <cProd> informações incoerentes com o esperado pela SEFAZ.
