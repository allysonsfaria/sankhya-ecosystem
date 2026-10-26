---
id: "37042081840407"
titulo: "Item vinculado a uma Ordem de Produção. Sua alteração ou exclusão deve ser realizada na própria OP."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37042081840407-Item-vinculado-a-uma-Ordem-de-Produ%C3%A7%C3%A3o-Sua-altera%C3%A7%C3%A3o-ou-exclus%C3%A3o-deve-ser-realizada-na-pr%C3%B3pria-OP"
trilha: "Melhores Práticas > Produção"
atualizado_em: "2026-07-22T14:21:55Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Ordem de Produção", "Vendas", "Artigo atualizado KCS", "Item vinculado a uma Ordem de Produção", "Alteração ou exclusão deve ser realizada na própria OP", "integridade entre o pedido de venda e a OP", "Ordem de Produção (OP)", "OP vinculada", "Produção - KCS"]
---

# Item vinculado a uma Ordem de Produção. Sua alteração ou exclusão deve ser realizada na própria OP.

**SITUAÇÃO**

A mensagem será exibida quando:

- Um item vinculado a uma **"Ordem de Produção"** (OP) for alterado ou excluído na **"Central de Vendas"** (Comercial >> Consulta >> Central de Vendas).
- O sistema detecta que a alteração pode comprometer a integridade entre o pedido de venda e a OP, perdendo sua rastreabilidade.
- Qualquer operação que tente modificar a quantidade, unidade e produto ou exclusão do item sem passar pela OP correspondente.

**SOLUÇÃO**

Para realizar alterações em itens vinculados a uma Ordem de Produção, siga uma das opções abaixo:

**Opção 1: Cancelar a Ordem de Produção**

**(1)** Acesse a tela de [**"Ordens de Produção - NOVA"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova) (Produção >> Rotinas >> Ordens de Produção - NOVA) e localize a OP vinculada ao pedido.

**(2)** Cancele a Ordem de Produção através da opção **"Cancelar"**.

**(3)** Retorne ao pedido de venda e realize as alterações necessárias nos itens.

**(4)** Gere uma nova Ordem de Produção com as informações atualizadas do pedido.

**Opção 2: Criar um Novo Pedido**

**(1)** Acesse a tela de **"Central de Vendas"** (Comercial >> Consulta >> Central de Vendas).

**(2)** Lance um novo pedido com as informações corretas e atualizadas.

**(3)** Gere a Ordem de Produção a partir do novo pedido criado.

**Opção 3: Realizar Alterações Diretamente na OP**

**(1)** Acesse a tela de [**"Ordens de Produção - NOVA"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova) (Produção >> Rotinas >> Ordens de Produção - NOVA).

**(2)** Localize a OP vinculada ao pedido e realize as alterações necessárias, ajustando a quantidade ou substituindo o produto diretamente na própria Ordem de Produção.

**OBSERVAÇÕES**: Não altere nem exclua o item pela Central de Vendas. Todas as modificações relacionadas ao item devem ser realizadas por meio da Ordem de Produção (OP).

Pela Central de Vendas, alterações permitidas, como valor unitário, observação, entre outros campos poderão ser realizadas.

**CAUSA**

Este aviso é exibido apenas quando há vínculo entre o pedido e a Ordem de Produção. O procedimento garante a integridade dos dados e evita inconsistências no sistema. Caso necessite de maior flexibilidade, considere sugerir uma melhoria através do [**"Sankhya Comunidade"**](https://community.sankhya.com.br/) ou solicitar uma personalização via OS.
