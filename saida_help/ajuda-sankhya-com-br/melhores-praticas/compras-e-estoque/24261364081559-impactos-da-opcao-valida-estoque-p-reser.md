---
id: "24261364081559"
titulo: "Impactos da opção ‘Valida Estoque p/ Reservar’ desmarcada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24261364081559-Impactos-da-op%C3%A7%C3%A3o-Valida-Estoque-p-Reservar-desmarcada"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-07-22T14:47:07Z"
rotulos: ["Produtos", "Configuração", "Faturamento", "Estoque", "‘Valida Estoque p/ Reservar’", "Reserva"]
---

# Impactos da opção ‘Valida Estoque p/ Reservar’ desmarcada

Com esta opção desmarcada a reserva passa a ser tratada como demanda, o que pode fazer com que o pedido só seja faturado usando a opção **"Faturar pelo estoque"**, pois como dois pedidos podem reservar a mesma mercadoria, não há como determinar de quem é a reserva.

**Exemplo:** Digamos que há 5 unidades de um produto. O pedido X reserva 3 e o pedido Y reserva 3 também.

No momento do faturamento não haverá estoque suficiente, pois não há estoque para atender a toda a reserva. Contudo no faturamento pelo estoque, o primeiro pedido a ser faturado irá consumir o estoque. Mesmo que não exista o pedido Y, o sistema não considera que a reserva é do pedido A, pois de fato não se trata de uma reserva nesse caso.

Mesmo que exista 5 no estoque, e apenas um pedido reserve as 5 quantidades, ao faturar de modo convencional será apresentado o erro de estoque insuficiente, sendo necessário o faturamento pelo estoque.

**Observação:** Com a opção desmarcada, não só o saldo do estoque será desconsiderado, porém todas as outras informações de estoque também (Empresa, Local, controle). Segue abaixo um exemplo.

Se tenho um produto que trabalha com controle por lote que não tenha saldo, ao lançar um pedido que reserva estoque sem informar controle, o sistema criará uma linha no estoque sem controle, para reservar o mesmo, deixando o saldo ‘Disponível’ negativo, até que seja faturado para que o lote em questão seja baixado, ou seja, o sistema não te exige lote mesmo marcando para usar.
