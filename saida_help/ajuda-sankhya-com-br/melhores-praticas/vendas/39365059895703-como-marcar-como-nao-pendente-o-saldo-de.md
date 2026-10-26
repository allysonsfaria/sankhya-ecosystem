---
id: "39365059895703"
titulo: "Como marcar como não pendente o saldo de um pedido faturado parcialmente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39365059895703-Como-marcar-como-n%C3%A3o-pendente-o-saldo-de-um-pedido-faturado-parcialmente"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-08-14T01:32:05Z"
rotulos: ["Configuração", "Faturamento", "Portal de Vendas", "Estoque", "Artigo criado KCS", "CVE - KCS", "Pedidos de Venda"]
---

# Como marcar como não pendente o saldo de um pedido faturado parcialmente?

Quando um pedido de venda é faturado parcialmente, o sistema mantém a coluna **Pendente = Sim** para a quantidade que ainda não foi faturada. Se esse saldo não vai mais ser faturado, você pode encerrar o pedido usando a opção **"Marcar como não pendente"**.

### Quando usar?

- Cancelamento parcial solicitado pelo cliente
- Falta de estoque para completar o pedido
- Acordo comercial para fechar o pedido só com o que já foi faturado
- Pedidos antigos parados com saldo pendente

### Como fazer?

**(1)** Acesse **Comercial > Rotinas > Central de Vendas** (ou Portal de Vendas, dependendo da versão).

**(2)** Filtre pelo Pedido de Venda desejado.

**(3)** Clique em **"Outras Opções"** e selecione **"Marcar como não pendente"**.

**(4)** Confirme. A coluna Pendente do pedido passa de "Sim" para "Não" e ele deixa de aparecer como pendente de faturamento.

### Pontos de atenção

- **Reversão:** [confirmar em ambiente de teste antes de publicar] até onde a documentação indica, não há uma opção padrão de tela para voltar o pedido a "Pendente = Sim" depois de marcado. Confirme essa informação no sistema antes de repassar como regra definitiva.
- **Estoque:** verifique se existem reservas vinculadas ao saldo pendente que precisam ser liberadas.
- **Financeiro:** confirme se há provisões relacionadas ao saldo que não será faturado.
- **Comercial:** certifique-se de que há acordo com o cliente sobre o não faturamento do restante.
