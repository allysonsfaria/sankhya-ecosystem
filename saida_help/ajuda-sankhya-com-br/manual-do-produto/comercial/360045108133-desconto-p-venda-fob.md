---
id: "360045108133"
titulo: "Desconto p/ Venda FOB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108133-Desconto-p-Venda-FOB"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:28:12Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Desconto para Venda FOB", "br.com.sankhya.com.avancado.descontoparavendafob", "Desconto p/ Venda FOB manual", "Desconto", "Tabelas de Preços", "Tratamento Especial", " DESCFOB", "FOB", "Comercial"]
---

# Desconto p/ Venda FOB

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311986246423) Módulo: Comercial > Avançado
```

---

Na tela de Desconto p / Venda FOB será possível criar tratamento especial de preço FOB/CIF nas Tabelas de Preços.

**Importante:** essa tela pode ser acessada somente se o parâmetro **"Usa desconto FOB - DESCFOB"** estiver ligado.

![Imagem 2: Importante: essa tela pode ser acessada somente se o parâmetro " Usa desconto FOB - DESCFOB" estiver ligado .](https://ajuda.sankhya.com.br/hc/article_attachments/23790105418647)

Nesta tela, deve-se informar o valor do desconto por tonelada, relativo ao frete, a ser repassado para o cliente. Os dados registrados nesta tela serão gravados na tabela TGFDFO. Os descontos podem ser por grupo de produto ou por produto FOB.

Nas Centrais de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas) dependendo da configuração do layout do cabeçalho, é exibido o campo **"CIF/FOB"**.

Para utilizar este desconto no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), deve-se informar na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), no campo **"Peso Bruto"**, o peso do produto em quilogramas. Como no exemplo abaixo:

**Produto A:** Unidade Principal = KG / Peso Bruto = 1,2

**Produto B:** Unidade Principal = Fardo / Peso Bruto = 60

**Nota:** independente da Unidade Principal, o Peso Bruto deve ser em quilogramas.

Ao lançar a nota, o sistema calculará o valor do desconto FOB da seguinte forma:

Desconto FOB = Valor do desconto FOB / 1000 \* Peso bruto do item.

Se no Cabeçalho da Nota o campo CIF/FOB for FOB, ao lançar o item, o preço será o de tabela da [Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos) [de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos). Ao alterar o cabeçalho para CIF ou Empresa da Nota, o preço será recalculado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108133-Desconto-p-Venda-FOB#top)
