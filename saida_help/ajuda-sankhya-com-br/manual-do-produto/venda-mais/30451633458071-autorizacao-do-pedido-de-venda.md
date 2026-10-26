---
id: "30451633458071"
titulo: "Autorização do pedido de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30451633458071-Autoriza%C3%A7%C3%A3o-do-pedido-de-venda"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Venda Mais"
atualizado_em: "2026-07-29T13:12:55Z"
rotulos: ["Configuração", "Central de Vendas", "Portal de Vendas", "Crédito", "TOP", "Venda Mais"]
---

# Autorização do pedido de venda

Com os limites de crédito aprovados, o processo de vendas utilizando a condição de pagamento **Venda Mais** pode ser iniciado.

A primeira etapa desse processo é garantir a autorização de crédito. Para as empresas que operam com a emissão de pedidos de venda, é necessário garantir que os [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) e [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) **estejam configurados para uso no Venda Mais**. Assim, ao confirmar o pedido, será solicitada a autorização de crédito ao parceiro responsável. Caso seja aprovada, a reserva do valor solicitado será garantida até a conclusão do processo de faturamento.

### Requisitos para um pedido usar o Venda Mais

Para que um pedido use o crédito do Venda Mais, é necessário configurar:

![Imagem 1: O Tipo de Negociação como Exclusivo Venda Mais (aba Características).](https://ajuda.sankhya.com.br/hc/article_attachments/30451633442071) O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) como **Exclusivo Venda Mais** (aba Características).

![Imagem 2: O Tipo de Negociação como Exclusivo Venda Mais (aba Características).](https://ajuda.sankhya.com.br/hc/article_attachments/30451633443095)

![Imagem 3: A TOP (Tipo de Operação) para Utilizar o Sankhya Venda Mais .](https://ajuda.sankhya.com.br/hc/article_attachments/30451679045015) A [TOP (Tipo de Operação)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) para **Utilizar o Sankhya Venda Mais**.

![Imagem 4: A TOP (Tipo de Operação) para Utilizar o Sankhya Venda Mais .](https://ajuda.sankhya.com.br/hc/article_attachments/30451633444375)

### Confirmação do pedido e autorização de crédito

Ao confirmar o pedido, o sistema verifica se o cliente tem limite suficiente para a compra.

#### **(1)** Com limite suficiente

Se o cliente tiver limite suficiente para a autorização, ao confirmar o pedido, o sistema solicita a autorização ao parceiro de crédito somente para a garantia desse crédito. Se aprovado, será apresentado no rodapé da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) o aviso: **Crédito Venda Mais autorizado com sucesso**.

![Imagem 5: Se o cliente tiver limite suficiente para a autorização, ao confirmar o pedido, o sistema solicita a autorização ao…](https://ajuda.sankhya.com.br/hc/article_attachments/30451633450007)

#### **(1)** Caso não haja limite suficiente

Se o cliente não tiver limite suficiente, o que acontece depende da configuração do parâmetro **Usar liberação de limites por alçada? - USALIBLIM**:

1. **Se a liberação de limites por alçada estiver ativada:**

- será solicitada a liberação do evento 3 - limite de crédito;

![Imagem 6: será solicitada a liberação do evento 3 - limite de crédito;](https://ajuda.sankhya.com.br/hc/article_attachments/30456731577367)

- a solicitação de liberação do evento chegará ao usuário responsável, que ao tentar liberar o evento será notificado sobre a ausência de limite junto ao parceiro de crédito;

![Imagem 7: a solicitação de liberação do evento chegará ao usuário responsável, que ao tentar liberar o evento será notificado…](https://ajuda.sankhya.com.br/hc/article_attachments/30456802805271)

- ao clicar para Solicitar análise de crédito poderá informar ao parceiro de crédito o limite desejado para essa venda, aguardando o retorno sobre essa solicitação;

![Imagem 8: ao clicar para Solicitar análise de crédito poderá informar ao parceiro de crédito o limite desejado para essa venda,…](https://ajuda.sankhya.com.br/hc/article_attachments/30457074851735)

- se o crédito for aprovado, basta liberar a venda e confirmar o pedido;
- se o crédito for negado, é necessário escolher outra forma de pagamento, ajustar o Tipo de Negociação para não ser Exclusivo Venda Mais e seguir com a confirmação do pedido.

2. **Se a liberação de limites por alçada estiver desativada:**

- o sistema informa que o cliente não tem crédito suficiente;
- um usuário responsável pela análise de crédito precisa acessar o cadastro do cliente e solicitar um novo limite por meio da aba Venda Mais;
- se o crédito for aprovado, o pedido pode ser confirmado normalmente;
- se o crédito for rejeitado, é necessário escolher outra forma de pagamento, ajustar o Tipo de Negociação para não ser Exclusivo Venda Mais e seguir com a confirmação do pedido.

### Conferência da reserva de limite e autorização do pedido

Depois da confirmação, a reserva do limite é atualizada no cadastro do cliente, na aba **Venda Mais**. 

No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), a autorização pode ser conferida das colunas:

- **código de autorização Venda Mais** (ID da autorização no parceiro de crédito);
- **status da autorização Venda Mais**.

![Imagem 9: status da autorização Venda Mais .](https://ajuda.sankhya.com.br/hc/article_attachments/30475322270999)

### Cancelamento da autorização de crédito

Se a autorização de crédito foi concedida, mas ainda não foi utilizada, é possível solicitar o seu cancelamento junto ao parceiro de crédito. Para isso, acesse o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), botão **Outras Opções >** **Venda Mais** > **Cancelar autorização de crédito**. Assim, o limite de crédito do cliente será liberado novamente.

![Imagem 10: Se a autorização de crédito foi concedida, mas ainda não foi utilizada, é possível solicitar o seu cancelamento junto…](https://ajuda.sankhya.com.br/hc/article_attachments/30475419336087)

### Expiração da autorização de crédito

O parceiro de crédito determinará em contrato o prazo para expiração da autorização de crédito, quando essa não for utilizada. Esse prazo deverá ser configurado na tela Configurações Venda Mais > Processos > Configurar rotinas > Pedidos de Venda > **Prazo para expiração da pré-autorização conforme contrato**.

![Imagem 11: O parceiro de crédito determinará em contrato o prazo para expiração da autorização de crédito, quando essa não for…](https://ajuda.sankhya.com.br/hc/article_attachments/30529957505303)

Após essa configuração, ao selecionar um **Pedido de Venda** (Venda Mais), o campo **Dt. Validade Crédito** será preenchido no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654). Quando a data de validade do crédito for atingida, caso a autorização não tenha sido **Utilizada** ou **Cancelada**, o campo **Status Autorização Venda Mais** será atualizado para **Expirado**.

![Imagem 12: Após essa configuração, ao selecionar um Pedido de Venda (Venda Mais), o campo Dt. Validade Crédito será preenchido no…](https://ajuda.sankhya.com.br/hc/article_attachments/30530435520919)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30451633458071-Autoriza%C3%A7%C3%A3o-do-pedido-de-venda#top)
