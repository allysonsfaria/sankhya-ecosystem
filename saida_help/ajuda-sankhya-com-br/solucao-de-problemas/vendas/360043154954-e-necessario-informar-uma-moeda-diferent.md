---
id: "360043154954"
titulo: "É necessário informar uma moeda diferente da moeda 0 neste cabeçalho ou a TOP não deve ser uma operação em moeda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043154954-%C3%89-necess%C3%A1rio-informar-uma-moeda-diferente-da-moeda-0-neste-cabe%C3%A7alho-ou-a-TOP-n%C3%A3o-deve-ser-uma-opera%C3%A7%C3%A3o-em-moeda"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:52Z"
rotulos: ["Configuração", "NF-e", "Moeda", "TOP", "Financeiro", "CORE_E04179", "Moeda incoerente na TOP", "Ajustar moeda na TOP ou na Tabela de Preços", "Divergência entre a moeda da nota e a tabela de preços"]
---

# É necessário informar uma moeda diferente da moeda 0 neste cabeçalho ou a TOP não deve ser uma operação em moeda

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16136689879959) MENSAGEM:**

[CORE\_E04179] Configurações incoerentes: A TOP XX possui a marcação 'Operação em Moeda' mas fora encontrada a moeda YY neste cabeçalho. É necessário informar uma moeda diferente da moeda 0 neste cabeçalho ou a TOP não deve ser uma operação em moeda.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16136689883031) SOLUÇÃO:**

A mensagem é apresentada caso o pedido/nota esteja lançado com uma TOP configurada para trabalhar com moedas estrangeiras (aba **"Financeiro"** » "**Operação em Moeda**"), o campo **"Usar como Preço"** também na TOP, está definido como **"Preço de Venda"**, porém a Tabela de Preços do item está configurada para a moeda corrente.

Dessa forma, identifique:

![Imagem 3: A marcação da TOP para trabalhar com Operação em Moeda é coerente com essa movimentação?](https://ajuda.sankhya.com.br/hc/article_attachments/16136689885719) A marcação da TOP para trabalhar com Operação em Moeda é coerente com essa movimentação?

Em caso negativo, desmarque essa opção e refaça o faturamento.

![Imagem 4: Em caso negativo, desmarque essa opção e refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/14661132259351)

![Imagem 5: Caso a marcação da TOP encontre-se correta, localize a " Tabela de Preço " (Caminho de acesso: Comercial » Arquivo »…](https://ajuda.sankhya.com.br/hc/article_attachments/16136674290327) Caso a marcação da TOP encontre-se correta, localize a **"[Tabela de Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os)"** (Caminho de acesso: Comercial » Arquivo » Tabelas de Preços) utilizada para esse lançamento e informe no campo **"Moeda"** o código Moeda a ser utilizado na respectiva operação/tabela. Realizado esse ajuste, refaça o faturamento.

![Imagem 6: Caso a marcação da TOP encontre-se correta, localize a " Tabela de Preço " (Caminho de acesso: Comercial » Arquivo »…](https://ajuda.sankhya.com.br/hc/article_attachments/14661132291223)

(1)** IMPORTANTE:**

Para identificar a tabela de preço que está sendo utilizada, verifique o parâmetro **"TIPTABPRECO"** (Caminho de acesso: Configurações » Avançado » Preferências) e a partir do mesmo localize os devidos cadastros.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16136674295831) CAUSA:**

Ocorre quando a moeda informada no cabeçalho da nota for diferente da moeda informada na tabela de preços do item que está sendo inserido, o sistema irá exibir esse alerta, informando que as configurações estão incoerentes.
