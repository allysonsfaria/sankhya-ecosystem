---
id: "25680346898967"
titulo: "Estoque do produto apresenta como bloqueado no WMS na rotina de consulta de produto, porem não apresenta na tela de Estoque/Endereçamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25680346898967-Estoque-do-produto-apresenta-como-bloqueado-no-WMS-na-rotina-de-consulta-de-produto-porem-n%C3%A3o-apresenta-na-tela-de-Estoque-Endere%C3%A7amento"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:44:46Z"
rotulos: ["Produtos", "Configuração", "Consulta", "WMS", "Estoque", "não é exibido na tela de endereçamento de estoque", "estoque do produto aparece como bloqueado no WMS", "rotina de consulta de produto"]
---

# Estoque do produto apresenta como bloqueado no WMS na rotina de consulta de produto, porem não apresenta na tela de Estoque/Endereçamento

Realize uma consulta via DBEXPLORE para identificar quais são os endereços em que o estoque é apresentado e que não apresenta na tela "Estoque/Endereçamento". Acesse a tela Endereço de Armazenamento e busque o endereço identificado na consulta, valide se a opção **"Analítico"** está desmarcada no endereço. Todo endereço com essa opção desmarcada não é exibido na tela de estoque do WMS. Caso seja necessário usar essa marcação no endereço, lembre-se de que antes é preciso transferir o estoque para outro endereço analítico, a fim de realizar a tratativa devida do produto.
