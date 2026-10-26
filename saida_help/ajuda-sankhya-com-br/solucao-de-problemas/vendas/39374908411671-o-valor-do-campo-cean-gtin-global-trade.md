---
id: "39374908411671"
titulo: "O valor do campo cEAN (GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras) informado não é válido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39374908411671-O-valor-do-campo-cEAN-GTIN-Global-Trade-Item-Number-do-produto-antigo-c%C3%B3digo-EAN-ou-c%C3%B3digo-de-barras-informado-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-27T13:54:50Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "Erro", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# O valor do campo cEAN (GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras) informado não é válido.

O valor do campo cEAN (GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras) informado não é válido.

O valor do campo cEANTrib (GTIN (Global Trade Item Number) da unidade tributável, antigo código EAN ou código de barras) informado não é válido.

![Imagem 1: O valor do campo cEANTrib (GTIN (Global Trade Item Number) da unidade tributável, antigo código EAN ou código de…](https://ajuda.sankhya.com.br/hc/article_attachments/41985338494615)

### SITUAÇÃO

Esta mensagem é apresentada quando o sistema identifica problemas com o código GTIN cadastrado no produto. O erro pode ocorrer em diferentes cenários.

### SOLUÇÃO

A solução depende da situação do produto. Siga os passos adequados ao seu cenário:

**Cenário 1: Produto NÃO possui código GTIN/EAN**

**(1)** Acesse a tela **"Produtos(Configurações » Cadastros » Produtos » Produtos)"**.
**(2)** Localize e abra o cadastro do produto que está apresentando o erro.
**(3)** Acesse a aba **"Impostos"**.
**(4)** No campo **"EAN/GTIN Produto p/ NF-e"**, selecione a opção **"Não informar"**.
**(5)** Caso o produto tenha Unidade Alternativa, acesse a aba "Unidades Alternativas". No campo **"EAN/GTIN Unid.Tributação"**, selecione também **"Não informar"**.
**(6)** Salve as alterações no cadastro do produto.
**(7)** Retorne à nota fiscal, exclua e inutilize a numeração (se necessário).
**(8)** Gere uma nova nota fiscal com o produto corrigido.

**Cenário 2: Produto POSSUI código GTIN/EAN válido**

**(1)** Acesse a tela **"Produtos(Configurações » Cadastros » Produtos » Produtos)"**.
**(2)** Localize o produto e acesse a aba **"Impostos"**.
**(3)** Verifique qual opção está selecionada no campo **"EAN/GTIN Produto p/ NF-e"**.

- **Código de Barras Estoque:** Caso esteja esta opção, informe um EAN/GTIN válido no campo "**Cód. de Barras"** da aba: "**ESTOQUE"**
- **Cód. Barras da Unid.Alternativa ou a Referencia:** Caso esteja esta opção, informe um EAN/GTIN válido no campo Código de Barras da aba: "**Unidades Alternativa"**
- **Referência:** Caso esteja esta opção, informe um EAN/GTIN válido no campo 'Referencia da aba: Geral'
- **Código do Produto:** Caso esteja esta opção, nada a fazer.

  **Obs:** verifique se o código do produto utilizado atende ao padrão GTIN. Caso o código interno da empresa não seja um GTIN válido, altere a configuração para utilizar o campo correto ou selecione Não informar, quando aplicável.

**(4)** Acesse o campo correspondente à opção selecionada e corrija o código GTIN.

**Observações importantes:**

• Quando o campo estiver configurado como Não informar, o sistema enviará automaticamente o valor "SEM GTIN" nos campos cEAN e cEANTrib do XML, conforme previsto na Nota Técnica 2017.001.
• Em caso de dúvidas sobre a obrigatoriedade ou validade do GTIN do produto, consulte seu contador ou o responsável fiscal da empresa.

### CAUSA

O erro ocorre por uma das seguintes razões:

1 - Produto sem GTIN configurado, mas com envio indevido do código.
2 - GTIN inexistente, inválido ou com dígito verificador incorreto.
3 - Quantidade de dígitos incompatível com o padrão GTIN.
4 - Configuração incorreta do campo EAN/GTIN Produto p/ NF-e, fazendo com que o sistema envie uma informação inválida no XML.
