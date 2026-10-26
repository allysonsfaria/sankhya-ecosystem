---
id: "24229997150359"
titulo: "Nenhuma Nota de compra/produção foi localizada associada ao lote informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24229997150359-Nenhuma-Nota-de-compra-produ%C3%A7%C3%A3o-foi-localizada-associada-ao-lote-informado"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-24T12:42:34Z"
rotulos: ["Produtos", "Configuração", "Requisições", "Estoque", "Parâmetro", "CORE_E03584", "Produto deve ter estoque; ajuste \"MODREQAMOSTRAS\"", "Amostra manual sem estoque disponível", "Nenhuma nota associada ao lote", "Erro"]
---

# Nenhuma Nota de compra/produção foi localizada associada ao lote informado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24230000900503) **MENSAGEM:**

[CORE\_E03584] Nenhuma Nota de compra/produção foi localizada associada ao lote informado

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24230000901783) **SOLUÇÃO:**

**Observação:** Não é possível fazer um lançamento avulso de amostra, pois o sistema exige que o produto tenha estoque disponível da amostra para fazer a baixa na requisição configurada no parâmetro **"MODREQAMOSTRAS"**. O processo de Controle de Qualidade de materiais inicia-se com a um movimento que faça a entrada do produto no estoque.

Caso o produto já tenha dado entrada com uma nota antiga, verifique como está a configuração do parâmetro: **"DIASBUSCALOTE - Qtde.Dias"** para busca de lotes em amostras. Esse parâmetro define a quantidade de dias entre os quais acontecerá a busca dos lotes nas notas, se a nota for anterior ao dias configurados ele não localiza o lote.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24229997148055)**CAUSA:**

A mensagem é apresentada ao tentar gerar uma amostra manual de um produto que não tem estoque disponível.
