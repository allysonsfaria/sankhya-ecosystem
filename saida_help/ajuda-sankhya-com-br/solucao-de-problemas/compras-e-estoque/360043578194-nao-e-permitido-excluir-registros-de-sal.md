---
id: "360043578194"
titulo: "Não é permitido excluir registros de saldo de entrada que tenham movimentações associadas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578194-N%C3%A3o-%C3%A9-permitido-excluir-registros-de-saldo-de-entrada-que-tenham-movimenta%C3%A7%C3%B5es-associadas"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:48Z"
rotulos: ["Movimentação Financeira", "Impostos", "Estoque", "ORA-20101", "Restrição na Exclusão de Registros de Saldo de Entrada", "Registro de Saldo", "Rastreamento de Estoque", "Erro"]
---

# Não é permitido excluir registros de saldo de entrada que tenham movimentações associadas

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16172211099799) MENSAGEM:**

ORA-20101: Não é permitido excluir registros de saldo de entrada que tenham movimentações associadas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16172194727063) SOLUÇÃO:**

![Imagem 3: Compreender que a mensagem acima é apresentada, visto que a nota a ser excluída/cancelada gerou registros de entrada…](https://ajuda.sankhya.com.br/hc/article_attachments/16172211111575) Compreender que a mensagem acima é apresentada, visto que a nota a ser excluída/cancelada gerou registros de entrada para 'Rastreamento de Estoque (ST)'. 

A implementação do rastreamento do Estoque necessita de **integridade das informações**. Ao atribuir uma saída tomando como rastreamento determinada entrada **não é possível excluir nem cancelar** este lançamento, pois todas as informações da saída foram geradas com base nesta entrada, como valores de impostos e controle do estoque.

![Imagem 4: Dessa forma, será necessário sintonias com o Contador da Empresa para avaliar a melhor solução para o respectivo…](https://ajuda.sankhya.com.br/hc/article_attachments/16172194736535) Dessa forma, será necessário sintonias com o Contador da Empresa para avaliar a melhor solução para o respectivo problema/incidente. Visto que essa exclusão/cancelamento não será permitido.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16172211123351) CAUSA:**

Quando existe o rastreamento de estoque (ST), ao atribuir uma saída tomando como rastreamento determinada entrada, não é possível excluir nem cancelar este lançamento, pois todas as informações da saída foram geradas com base nesta entrada, como valores de impostos e controle do estoque.
