---
id: "39340762286743"
titulo: "Portal de Vendas não apresenta Metros Cúbicos do Pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39340762286743-Portal-de-Vendas-n%C3%A3o-apresenta-Metros-C%C3%BAbicos-do-Pedido"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-14T01:14:35Z"
rotulos: ["Produtos", "Configuração", "Portal de Vendas", "Venda Mais", "Artigo criado KCS", "CVE - KCS", "Customização"]
---

# Portal de Vendas não apresenta Metros Cúbicos do Pedido

**Situação**

No "Portal de Vendas" (Comercial > Consulta > Portal de Vendas), o campo "Metros Cúbicos" (M3) não aparece na grade do cabeçalho do pedido, mesmo quando os itens já possuem esse valor cadastrado.

**Solução**

Não é necessário criar um novo campo, pois o M3 já existe no cabeçalho do pedido. Primeiro defina o que é realmente necessário:

**(1)** **Só exibir o valor** (quando ele já estiver preenchido, por ter passado pela Formação de Carga): adicione a coluna M3 ao layout da grade do Portal de Vendas.

**(2)** **Calcular automaticamente em qualquer pedido**, sem depender de passar pela Formação de Carga: será necessária uma customização que, ao incluir ou alterar itens, some os valores de M3 (TGFITE) e atualize o cabeçalho (TGFCAB).mente os valores de metros cúbicos de todos os itens do pedido e apresentar o total no cabeçalho.

**Causa**

O campo "Metro Cúbico" da nota (TGFCAB) é preenchido automaticamente com o valor do campo "M3" da tela Formação de Carga. Sendo assim, ao salvar itens em um Pedido de Venda, por exemplo, o sistema não calcula automaticamente o metro cúbico total da nota. Esse cálculo é feito apenas na Formação de Carga.

Além disso, o Portal de Vendas não traz esse campo como coluna padrão da grade principal, ele hoje só é usado no popup de rateio de frete entre notas.
