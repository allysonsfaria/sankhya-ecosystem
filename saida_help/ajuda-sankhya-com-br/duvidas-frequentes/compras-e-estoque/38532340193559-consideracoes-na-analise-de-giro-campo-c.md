---
id: "38532340193559"
titulo: "Considerações na Análise de Giro – Campo Compra Pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38532340193559-Considera%C3%A7%C3%B5es-na-An%C3%A1lise-de-Giro-Campo-Compra-Pendente"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:01:28Z"
rotulos: ["Produtos", "Configuração", "Movimentação Financeira", "Análise de Giro", "Estoque", "Compra Pendente", "Entradas Pendentes", "TGFEST"]
---

# Considerações na Análise de Giro – Campo Compra Pendente

A apresentação das informações referentes ao campo ''**Compra Pendente''** depende da configuração do campo **“Apresentar por”** na Matriz utilizada.

**Quando “Apresentar por” = Vazio**

- O sistema apresentará as **Entradas Pendentes**, independentemente de existir ou não registros na tabela **TGFEST** para o produto.

**Quando “Apresentar por” = Empresa, Local ou Controle**

- Se o produto **não possuir registros na TGFEST para a empresa**, o sistema não apresentará as **Entradas Pendentes**, mesmo que existam notas ou pedidos pendentes.
- Se o produto **possuir registros na TGFEST**, o sistema apresentará as **Entradas Pendentes** conforme cada Empresa, considerando as movimentações provenientes de nota ou pedido.
