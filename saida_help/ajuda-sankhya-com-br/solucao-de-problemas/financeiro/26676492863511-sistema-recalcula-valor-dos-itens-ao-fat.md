---
id: "26676492863511"
titulo: "Sistema recalcula valor dos itens ao faturar um lançamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26676492863511-Sistema-recalcula-valor-dos-itens-ao-faturar-um-lan%C3%A7amento"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:40:50Z"
rotulos: ["Produtos", "Configuração", "TOP", "Vendas", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Sistema recalcula valor dos itens ao faturar um lançamento"]
---

# Sistema recalcula valor dos itens ao faturar um lançamento

**(1)**Ao realizar o faturamento de um lançamento, os valores do item são recalculados de acordo com a tabela de preço.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26676505222039)SOLUÇÃO:**

![Imagem 2: Caso trabalhe com o parâmetro RECPRECOTPV como "Nunca" , porém atenda a alguma dessas condições, ocorrerá o recalculo.](https://ajuda.sankhya.com.br/hc/article_attachments/26676492835095) Caso trabalhe com o parâmetro **RECPRECOTPV** como **"Nunca"**, porém atenda a alguma dessas condições, ocorrerá o recalculo.

**(1)**Se no cadastro do produto o campo **"Digitação na nota"** estiver como quantidade, permitirá o recalculo.

**(1)**Se for uma venda e trabalhar com um dos parâmetros abaixo **ligado** permitirá o recalculo:

- **DESCFOB** - Usa desconto FOB
- **PERCDESCFOB** - Usar % Desc.por região p/Frete FOB ?
- **USASIMFORMAPGTO** - Simula formas de pagamento na Central?
- **PERCDESCFOBCAB** - Usa Perc. Desc. FOB no rodap (Venda)?
- **USAPRECPELATOP** - Usa precificação de produtos/serviços pela TOP
- **USAPRECTOPPDV** - Usa precificação pela TOP no PDV Web

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26676505232791)CAUSA:**

Caso algum dos parâmetros acima estejam habilitados, resulta no recalculo do valor unitário do item ao faturar.
