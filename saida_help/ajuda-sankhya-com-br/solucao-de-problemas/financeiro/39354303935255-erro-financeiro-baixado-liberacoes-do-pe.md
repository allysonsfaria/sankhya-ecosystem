---
id: "39354303935255"
titulo: "Erro \"Financeiro baixado, Liberações do Pedido/Nota não podem ser eliminadas\" ao alterar pedido com Metas e Orçamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354303935255-Erro-Financeiro-baixado-Libera%C3%A7%C3%B5es-do-Pedido-Nota-n%C3%A3o-podem-ser-eliminadas-ao-alterar-pedido-com-Metas-e-Or%C3%A7amentos"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-22T12:58:40Z"
rotulos: ["Configuração", "Pedido de Compra", "TOP", "Financeiro", "TGMTRA", "Artigo criado KCS", "Financeiro - KCS", "Metas e Orçamento"]
---

# Erro "Financeiro baixado, Liberações do Pedido/Nota não podem ser eliminadas" ao alterar pedido com Metas e Orçamentos

### SITUAÇÃO

Ao tentar alterar um pedido de compra (por exemplo, mudar a quantidade, o valor ou excluir um item), o sistema mostra a mensagem:

![Imagem 1: Ao tentar alterar um pedido de compra (por exemplo, mudar a quantidade, o valor ou excluir um item), o sistema mostra a…](https://ajuda.sankhya.com.br/hc/article_attachments/44428347109783)

Isso ocorre em pedidos controlados por **Metas e Orçamentos** (Metas e Orçamentos >> Planejamento de metas/orçamentos), em geral quando o pedido já tem entrega parcial ou financeiro parcialmente liquidado.

### SOLUÇÃO

**(1)**  **Antes de qualquer ação, verifique:**

- na aba **Financeiro** do pedido, ou na tela de **Movimentação Financeira**, confira se algum título do pedido já foi baixado;
- confira se o pedido já gerou notas, como a nota de entrada de uma entrega parcial.

(2)** Se o pedido já tiver gerado notas,** a alteração direta não é permitida Escolha conforme o processo da sua empresa:

- exclua ou cancele a nota vinculada e depois altere o pedido;
- ou trate a diferença em um novo pedido.

(3)** Se o pedido não deveria ter controle orçamentário**, revise o cadastro de Metas e Orçamentos e confira a TOP, o Centro de Resultado e a Natureza vinculados à meta. Assim os próximos pedidos não entram no controle por engano. Para corrigir um pedido que já foi lançado, procure o suporte.

> **Atenção:** não faça exclusões direto no banco de dados para liberar a alteração. Isso deixa os saldos de Metas e Orçamentos inconsistentes e afeta relatórios e validações.

###

### CAUSA

Quando um pedido é confirmado e a TOP, o Centro de Resultado ou a Natureza têm uma Meta Orçamentária ativa, o sistema registra o valor do pedido como compromisso no orçamento.

Ao alterar o pedido, o sistema precisa recalcular esse compromisso. Ele não deixa fazer isso quando a liberação orçamentária do pedido já foi analisada e o pedido está em uma destas situações:

- **Tem títulos baixados no financeiro:** aparece a mensagem "Financeiro baixado...".
- **Já gerou notas** (faturamento, entrega ou devolução): aparece a mensagem "Pedido ou Nota já foram faturados/devolvidos...".

Esse comportamento é esperado. Ele evita que o valor comprometido no orçamento mude depois que o pedido já teve efeito financeiro ou fiscal. Um pedido com controle orçamentário, mas sem títulos baixados e sem notas geradas, pode ser alterado normalmente.
