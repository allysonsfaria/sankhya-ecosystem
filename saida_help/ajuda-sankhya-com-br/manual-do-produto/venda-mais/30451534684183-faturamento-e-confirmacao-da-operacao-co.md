---
id: "30451534684183"
titulo: "Faturamento e confirmação da operação com NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30451534684183-Faturamento-e-confirma%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-com-NF-e"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Venda Mais"
atualizado_em: "2026-07-29T13:12:53Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "Crédito", "TOP", "Tipos de Negociação", "Configurações Venda Mais", "Venda Mais", "Aprovação de crédito"]
---

# Faturamento e confirmação da operação com NF-e

No processo de venda usando a linha de crédito Venda Mais, deve-se emitir a Nota Fiscal Eletrônica (NF-e) normalmente. O parceiro de crédito contratado será o responsável por emitir os boletos para pagamento.

**Importante:**

- somente serão aceitas Notas Fiscais Eletrônicas no modelo **55**;
- notas de contingência **não** são aceitas no Venda Mais.

### Requisitos para que uma NF-e entre no fluxo do Venda Mais

1. A marcação **Exclusivo Venda Mais** deve estar ativada na aba **Características** da tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173).
2. Na tela [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba **Geral**, a marcação **Utilizar no Sankhya Venda Mais** deve estar habilitada e, na aba **NF-e/NFC-e/CF-e** o **Modelo do Documento** deve ser **55 (Nota Fiscal Eletrônica)**.

### Confirmação da NF-e e aprovação do crédito

A aprovação da operação de crédito pode ocorrer em dois cenários:

**![Imagem 1: Faturamento vinculado a um pedido já autorizado pelo Venda Mais](https://ajuda.sankhya.com.br/hc/article_attachments/30451580551447) Faturamento vinculado a um pedido já autorizado pelo Venda Mais**

Se a NF-e for gerada a partir de um pedido de venda que **já tenha um Código de Autorização**, após a aprovação da NF-e na SEFAZ (Status NF-e = Aprovada), a operação será automaticamente enviada ao parceiro de crédito para confirmação.

Neste cenário, o valor da NF-e **não pode ser maior** que o valor autorizado no pedido.

**![Imagem 2: Nota de venda avulsa ou não faturada através de um pedido autorizado pelo Venda Mais](https://ajuda.sankhya.com.br/hc/article_attachments/30451580552471) Nota de venda avulsa ou não faturada através de um pedido autorizado pelo Venda Mais**

Se a NF-e emitida atender aos requisitos do Venda Mais, mas **não** estiver vinculada a um pedido previamente autorizado (Código de autorização Venda Mais recebido), a autorização será solicitada no momento da confirmação da nota.

**Se existir limite disponível**, a NF-e será confirmada e, após a aprovação junto à SEFAZ (Status NF-e = Aprovada), será solicitado ao parceiro de crédito a aprovação desta operação no Venda Mais.

Caso **não haja limite disponível**, a confirmação será bloqueada e uma mensagem de alerta será exibida. Nesse caso, o usuário responsável pela análise de crédito deve acessar o cadastro do cliente e solicitar um novo limite de crédito informando o limite desejado para essa venda. 

Ainda assim, se o retorno do parceiro de crédito for negativo, é necessário escolher outra forma de pagamento, ajustar o [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) para **não** ser **Exclusivo Venda Mais** e seguir com a confirmação da nota.

### Operação de venda aprovada pelo parceiro de crédito

Após a aprovação da NF-e junto à SEFAZ, os dados serão enviados ao parceiro de crédito para aprovação da operação. Se aprovada, será exibida a seguinte mensagem:

**"Operações aprovadas**
**Foi aprovada 1 nota junto ao parceiro de crédito. O boleto já está disponível na rotina de impressão de boleto."**

A operação pode ser conferida em:

- **aba Venda Mais** do [cadastro do cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494): onde o **Limite utilizado** estará atualizado;
- no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), a coluna **Status Venda Mais** exibirá a opção **Crédito Aprovado**.

### Falhas na aprovação

Se houver erro na aprovação do crédito, uma mensagem de erro será exibida.

Para entender o motivo do erro, selecione a NF-e no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) > botão **Outras Opções** > **Ver acompanhamento**.

[GIF animado: Imagem 3: Para entender o motivo do erro, selecione a NF-e no Portal de Vendas > botão Outras Opções > Ver acompanhamento .](https://ajuda.sankhya.com.br/hc/article_attachments/30451580552983)

Detectado o erro, este precisa ser tratado imediatamente:

- **se for uma falha que possa ser corrigida**, faça os ajustes necessários e utilize a opção **Solicitar aprovação de crédito Venda Mais** para que uma nova tentativa de aprovação da operação de crédito seja realizada;
- **caso o erro não possa ser corrigido**, a NF-e deve ser cancelada e refaturada utilizando outro [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) que seja compatível com essa venda.

### Solicitar aprovação de crédito manualmente

Se houver instabilidade ou falhas no envio automático da NF-e para confirmação da operação Venda Mais, é possível solicitar a aprovação manualmente pelo [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) > botão **Outras Opções** > **Venda Mais** > **Solicitar aprovação de crédito Venda Mais**.

![Imagem 4: Se houver instabilidade ou falhas no envio automático da NF-e para confirmação da operação Venda Mais, é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/30483321502743)

![Imagem 5: Essa opção só estará disponível se:](https://ajuda.sankhya.com.br/hc/article_attachments/30451534681239) Essa opção só estará disponível se:

- a NF-e estiver aprovada na SEFAZ;
- o Código de Autorização estiver preenchido;
- o Status Venda Mais **não** for Crédito Aprovado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30451534684183-Faturamento-e-confirma%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-com-NF-e#top)
