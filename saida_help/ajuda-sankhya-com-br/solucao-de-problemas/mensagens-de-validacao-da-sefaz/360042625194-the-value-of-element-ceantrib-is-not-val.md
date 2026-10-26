---
id: "360042625194"
titulo: "The value ' ' of element 'cEANTrib' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625194-The-value-of-element-cEANTrib-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:33Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "Impostos", "Estoque", "Valor Inválido de 'cEANTrib'", "Erro"]
---

# The value ' ' of element 'cEANTrib' is not valid

**![Imagem 1: MENSAGEM: cvc-pattern-valid: Value ' ' is not facet-valid with respect to pattern '(0-9){0}|(0-9){8}|(0-9){12,14}' for…](https://ajuda.sankhya.com.br/hc/article_attachments/16509856804631) MENSAGEM:**
cvc-pattern-valid: Value ' ' is not facet-valid with respect to pattern '[0-9]{0}|[0-9]{8}|[0-9]{12,14}' for type '#AnonType\_cEANTribproddetinfNFeTNFe'.
cvc-type.3.1.3: The value ' ' of element 'cEANTrib' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16509880454551) SOLUÇÃO:**

![Imagem 3: Acesse o cadastro do respectivo produto : Tela "Produtos" (Caminho de acesso: Configurações » Cadastros » Produtos )](https://ajuda.sankhya.com.br/hc/article_attachments/16509856814487) Acesse o cadastro do respectivo produto : Tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos)

- Aba: **"Impostos"**
- Campo **"EAN/GTIN produto p/ NF-e"**

![Imagem 4: Campo "EAN/GTIN produto p/ NF-e"](https://ajuda.sankhya.com.br/hc/article_attachments/14606199117079)

![Imagem 5: Avalie juntos aos responsáveis na sua empresa, se esse produto possui um controle efetivo de Código EAN/GTIN. Em caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16509880463511) Avalie juntos aos responsáveis na sua empresa, **se esse produto possui um controle efetivo de Código EAN/GTIN.** Em caso negativo, o campo "EAN/GTIN Produto p/ NF-e" deve ser alterado para "**Não Informar**". Realizado esse ajuste, inutilize a numeração da respectiva NF-e, realize sua exclusão e uma nova emissão.

![Imagem 6: Caso esse controle seja necessário, avalie as opções abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16509880465687) Caso esse controle seja necessário, avalie as opções abaixo:

- **Código de Barras Estoque:** Caso esteja esta opção, informe um EAN/GTIN válido no campo "**Cód. de Barras"** da aba: "**ESTOQUE"**
- **Cód. Barras da Unid.Alternativa ou a Referencia:** Caso esteja esta opção, informe um EAN/GTIN válido no campo Código de Barras da aba: "**Unidades Alternativa"**
- **Referência:** Caso esteja esta opção, informe um EAN/GTIN válido no campo 'Referencia da aba: Geral'
- **Código do Produto:** Caso esteja esta opção, nada a fazer.

Realizado os devidos ajustes, inutilize a numeração da respectiva NF-e, realize sua exclusão e uma nova emissão.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16509856823575) CAUSA:**

Quando for emitida uma NF-e e dentre os teus itens for informado na tag <cEANTrib> um código GTIN ( identificador para itens comerciais) inválido, a rejeição será apresentada. Visto que o Código de Barras (GTIN ou EAN) somente deve ser informado se tratar-se de um código válido e aceito.
