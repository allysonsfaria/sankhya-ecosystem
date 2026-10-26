---
id: "360043723754"
titulo: "Nenhum processo produtivo que permita vínculo com pedido de venda encontrado para o pedido [XXXXX]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043723754-Nenhum-processo-produtivo-que-permita-v%C3%ADnculo-com-pedido-de-venda-encontrado-para-o-pedido-XXXXX"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-08-25T16:45:26Z"
rotulos: ["#criadoRoger", "#revisadohugo", "PROD_E00135", "Produtos", "Configuração", "Produção", "Pedido de Venda", "Sem processo produtivo para o pedido [52765]", "Cheque configuração \"Exige pedido de venda\"", "Falta de processo configurado corretamente", "Erro", "Artigo atualizado KCS", "Produção - KCS"]
---

# Nenhum processo produtivo que permita vínculo com pedido de venda encontrado para o pedido [XXXXX]

**MENSAGEM**

Não é permitido especificar Pedido para OP sequência 1, pois o Processo Produtivo está configurado como "Nunca" exige pedido de venda.

[PROD\_E00135] Nenhum processo produtivo que permita vínculo com pedido de venda encontrado para o pedido.

**SITUAÇÃO**

Este erro ocorre ao tentar lançar uma Ordem de Produção (OP) vinculada a um pedido de venda ou ao gerar a OP pelo Portal de Vendas, por meio da opção **Outras Opções » "Gerar Produção"**.

O problema ocorre quando o Processo Produtivo associado ao produto está configurado com a opção "**Exigir pedido de venda"** definida como "**Nunca"**. Nesse cenário, o sistema identifica uma incompatibilidade entre a configuração do processo produtivo e a tentativa de vincular a OP a um pedido de venda, ocasionando o bloqueio da operação.

**SOLUÇÃO**

Para solucionar o problema, siga os passos abaixo:

**(1)** Acesse a tela **"Processo Produtivo - NOVA"** **(Produção » Cadastros » Processo Produtivo - Nova)** e localize o processo produtivo utilizado pelo produto que está apresentando o erro.

**(2)** Clique no botão **"Outras Opções".**

**(3)** Localize o campo **"Exigir pedido de venda"** e verifique a configuração atual.

**(4)** Altere a configuração para **"Opcional"** ou **"Sempre"**, conforme a necessidade do seu processo produtivo:

    • **"Opcional"**: permite lançar OPs com ou sem vínculo ao pedido de venda. Com esta opção na produção de múltiplos produtos, caso algum necessite do pedido, o sistema irá gerar os devidos pedidos conforme a necessidade.

    • **"Sempre"**: exige obrigatoriamente o vínculo da OP a um pedido de venda.

**(5)** Salve as alterações realizadas no **Processo Produtivo.**

**(6)** Refaça o processo de lançamento das OPs.

![Imagem 1: (1) Acesse a tela "Processo Produtivo - NOVA" (Produção » Cadastros » Processo Produtivo - Nova) e localize o processo…](https://ajuda.sankhya.com.br/hc/article_attachments/42985880830487)

**CAUSA**

O erro ocorre devido a uma divergência na configuração do campo **"Exigir pedido de venda"** entre os diferentes processos produtivos utilizados nos itens do pedido.

O bloqueio pode ocorrer, por exemplo, quando o produto que aparece na primeira posição da ordenação possui um processo produtivo configurado como **"Nunca"**. Também pode ocorrer quando há pedidos com necessidade de produção e nenhum dos processos produtivos da planta está configurado com **"Exigir pedido de venda"** como **"Opcional"**.

Recomenda-se padronizar a configuração do campo “Exigir pedido de venda” entre todos os processos produtivos.
