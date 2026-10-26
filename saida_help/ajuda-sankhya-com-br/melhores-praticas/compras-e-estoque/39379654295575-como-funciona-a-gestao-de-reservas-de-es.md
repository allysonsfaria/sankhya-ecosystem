---
id: "39379654295575"
titulo: "Como funciona a gestão de reservas de estoque em pedidos de venda?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39379654295575-Como-funciona-a-gest%C3%A3o-de-reservas-de-estoque-em-pedidos-de-venda"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-08-01T02:42:26Z"
rotulos: ["Configuração", "Central de Vendas", "Portal de Vendas", "TOP", "Estoque", "Artigo criado KCS", "CVE - KCS", "Pedidos de Venda"]
---

# Como funciona a gestão de reservas de estoque em pedidos de venda?

No ERP Sankhya, a **"Reserva de Estoque"** é realizada automaticamente no momento em que um pedido de venda é inserido na **"Central de Vendas"** (Comercial Consulta Central de Vendas), mesmo que o pedido ainda não tenha sido confirmado ou aprovado. Este comportamento é padrão do sistema e funciona como uma **"Garantia de Venda"** para o parceiro comercial.

### Funcionamento da reserva de estoque

Quando um pedido de venda é criado, o sistema reserva automaticamente os itens no estoque, independentemente do status do pedido (Pendente, Aprovado ou Reprovado). Esta reserva garante que os produtos fiquem separados para aquele pedido específico, evitando que sejam vendidos para outros clientes.

A configuração que controla esse comportamento está localizada no **"Tipo de Operação (TOP)"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) do pedido de venda, através do campo **"Atualização do Estoque > Reservar"**. Quando este campo está marcado, o sistema realiza a reserva automaticamente.

### Impactos da reserva automática

Esta funcionalidade pode gerar algumas situações operacionais importantes:

**Estoque reservado em pedidos não confirmados:** Produtos ficam reservados mesmo quando o pedido está com status **"Pendente"**, reduzindo o saldo disponível para novos pedidos.

**Saldo disponível zerado:** Mesmo havendo estoque físico, o saldo disponível pode estar zerado devido às reservas de pedidos não finalizados.

### Remoção de reserva de estoque

A única forma de remover a reserva de estoque é acessar o **"Tipo de Operação (TOP)"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) do pedido e desmarcar o campo  **"Reservar"**. No entanto, esta ação pode gerar outros problemas operacionais:

• Permite a criação de vários pedidos sem validação de estoque
• No momento do faturamento, pode ocorrer a mensagem de **"Estoque Insuficiente"**
• Perde-se o controle sobre a disponibilidade real dos produtos

### Diferença entre faturamento pelo estoque e pelo portal

É importante compreender a diferença entre as duas formas de faturamento:

**Faturamento direto pelo estoque:** O sistema verifica exclusivamente a quantidade disponível em estoque, desconsiderando as reservas vinculadas ao pedido.

**Faturamento pelo portal (botão "Faturar"):** O sistema considera a reserva gerada pelo próprio pedido que está sendo faturado, permitindo o faturamento mesmo com saldo disponível zerado.

### Recomendações e melhores práticas

Para uma gestão eficiente de estoque e reservas, recomenda-se:

**(1)** Mantenha o campo **"Reservar"** marcado no **"Tipo de Operação (TOP)"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) para garantir o controle adequado do estoque.

**(2)** Considere os produtos como reservados sempre que estiverem vinculados a um pedido de venda, mesmo que não confirmado.

**(3)** Realize o faturamento através do **"Portal de Vendas"** utilizando o botão **"Faturar"**, que considera as reservas do pedido.

**(4)** Monitore regularmente os pedidos com status **"Pendente"**  para liberar reservas desnecessárias.

**(5)** Configure adequadamente a **"Validação de Estoque"** no **"Grupo de Produtos/Serviços"** (Comercial Arquivo Cadastros Produtos Grupos de Produtos) conforme a necessidade operacional da empresa.
