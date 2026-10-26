---
id: "4556268538903"
titulo: "Como configurar a baixa automática de um título ao confirmar o lançamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4556268538903-Como-configurar-a-baixa-autom%C3%A1tica-de-um-t%C3%ADtulo-ao-confirmar-o-lan%C3%A7amento"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:18:55Z"
rotulos: ["Configuração", "NF-e", "Central de Vendas", "Movimentação Financeira", "Financeiro", "#validadoHugo", "#causaraiz", "Configurar baixa automática", "Baixa na confirmação", "NF-e não autorizada sem impressão"]
---

# Como configurar a baixa automática de um título ao confirmar o lançamento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16334976328471) MENSAGEM:**

Como configurar a baixa automática de um título ao confirmar o lançamento?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334976329367) SOLUÇÃO:**

![Imagem 3: Marcando a opção "Baixa na Confirmação" (Tela "Tipo de Negociação" ) será aberta a tela de Baixa no ato da confirmação…](https://ajuda.sankhya.com.br/hc/article_attachments/16334976329879) Marcando a opção **"Baixa na Confirmação"** (Tela **"Tipo de Negociação"**) será aberta a tela de Baixa no ato da confirmação da nota;

**(1)**Essa é uma configuração utilizada para Tipo de Negociação A Vista e que desejem que seu financeiro entre com status baixado evitando assim retrabalho de efetuar a baixa manual.

![Imagem 4: (1) Essa é uma configuração utilizada para Tipo de Negociação A Vista e que desejem que seu financeiro entre com status…](https://ajuda.sankhya.com.br/hc/article_attachments/15775522038935)

![Imagem 5: Tem-se a opção de na realização da baixa, na confirmação da nota, configurar o sistema de modo que o questionamento…](https://ajuda.sankhya.com.br/hc/article_attachments/16334976333079) Tem-se a opção de na realização da baixa, na confirmação da nota, configurar o sistema de modo que o questionamento sobre o desejo de realizar ou não a baixa não seja realizado. Para isso, existe o parâmetro**"Baixar título na central sem perguntar? - BXARTITSEMPERG"**, que ao ser ativado, e a marcação Baixa na Confirmação estiver realizada, nenhuma tela para confirmação da baixa será apresentada, a baixa do título é diretamente realizada na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

![Imagem 6: Tem-se a opção de na realização da baixa, na confirmação da nota, configurar o sistema de modo que o questionamento…](https://ajuda.sankhya.com.br/hc/article_attachments/15775536495255)

**Nota:** para que a tela de baixa seja apresentada, se faz necessário configurar na rotina de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) a liberação das opção de **"Baixa"** para a tela de Movimentação Financeira.

**Importante:** a baixa realizada pelo sistema quando efetuada a marcação Baixa na Confirmação acontece apenas quando é feita a confirmação manual dos documentos, ou seja, através do botão [Confirmar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#confirmar) presente na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

**Observações:**

**(1)** Ao utilizar esta forma de baixa, não será solicitado nenhum tipo de impressão pelo sistema;

**(1)** Caso na tentativa de aprovação de uma NF-e (com baixa automática do respectivo título), ocorram falhas de comunicação por questões de timeout ou mesmo de configurações equivocadas, será exibida a seguinte mensagem e não ocorrerá a baixa do título:

"Ocorreu um erro na baixa automática: O financeiro está vinculado a uma NF-e não autorizada pela Sefaz, portanto não é possível baixá-lo. Aprove a nota e realize a baixa manualmente."
