---
id: "360043696853"
titulo: "Este produto já foi faturado, veja 'Qtde Entregue'. Não pode ser alterado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696853-Este-produto-j%C3%A1-foi-faturado-veja-Qtde-Entregue-N%C3%A3o-pode-ser-alterado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-13T20:31:25Z"
rotulos: ["CORE_E02001", "CORE_E03231", "Produtos", "NF-e", "Central de Vendas", "Produto faturado não pode ser alterado", "Verificar e cancelar nota destino", "Tentativa de alteração em item já faturado", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# Este produto já foi faturado, veja 'Qtde Entregue'. Não pode ser alterado

**Mensagem**

[CORE\_E02001] Este produto já foi faturado, veja "Qtde Entregue". Não pode ser alterado.

[CORE\_E03231] Este produto já foi faturado, veja "Qtde Entregue". Não pode ser alterado.

**Situação**

Ao tentar alterar excluir um item em um pedido/nota, a mensagem é apresentada. A situação ocorre quando existe faturamento vinculado (parcial ou total).

**Causa**

Essa mensagem é apresentada, quando o item que está sendo alterado e/ou excluído já foi faturado, ou seja, já existe uma nota destino para esse item/lançamento.

O erro ocorre porque o sistema identifica que o item do pedido possui **"Quantidade Entregue"** (QTDENTREGUE) registrada, indicando uma ligação entre o item original e um documento de destino (nota fiscal). Esta proteção evita inconsistências no estoque, no financeiro e nos registros fiscais, garantindo que alterações não comprometam documentos já emitidos.

**Solução**

Para resolver este problema, siga os passos abaixo:

**(1)Identificação do vínculo:**

- Abra o lançamento onde está tentando fazer a alteração.
- Selecione o item específico.
- Clique em **"Outras Opções"** > **"Documentos Relacionados"**.
- Na grade inferior, identifique e, se necessário, dê um duplo clique no **"Documento de Destino"** para visualizar o lançamento vinculado.

  Para esse cenário, devido tal ligação, de fato a alteração não será permitida, até que todas as notas destino desse item seja excluídas/canceladas/desligadas.

  Detectado esse lançamento, **analise-o para entender qual será a tratativa mais viável**. Essa tratativa precisa ser bem alinhada internamente, para não impactar negativamente o processo da empresa.

(2)** Seguem os procedimentos viáveis:**

- **Nota destino  não confirmada ou NF-e de 'Terceiros':** exclua o lançamento e  assim poderá ajustar o documento de origem.
- **Nota fiscal eletrônica dentro do prazo de cancelamento:** Após proceder com o cancelamento dessa, o documento origem poderá ser alterado.
- **Central de Vendas » Outras Opções » 'Desligar a Nota dos Pedidos':** Quando os itens estão relacionados a uma outra transação, esta opção retira essa ligação. Ou seja, caso seja realizado o faturamento de um Pedido de Venda, a Nota que será gerada possuirá ligação de seus itens com os itens do Pedido; por meio da opção Desligar a Nota dos Pedidos pode-se desvincular a Nota desse Pedido
- Cancele o faturamento parcial ou duplique o item, mantendo a quantidade já faturada no original e criando um novo para a quantidade pendente, caso o item tenha sido parcialmente faturado.

**(3)Cenários de exceção (Sem nota vinculada):**

- Verifique o campo **"Quantidade Entregue"** (QTDENTREGUE) do item. Se este campo estiver preenchido indevidamente, o sistema impedirá a exclusão.
- Caso a **"Quantidade Entregue"** esteja preenchida sem documento de destino, pode ser necessária correção via banco de dados pelo suporte técnico ou consultoria. Realize o procedimento inicialmente em ambiente de testes.

**Restrições importantes:**

- Não altere a **"Quantidade Negociada"** para um valor menor que a quantidade já entregue.
- Itens totalmente faturados não podem ser alterados ou excluídos sem que o vínculo de faturamento seja desfeito.
- Campos como **"Empresa"**, **"Tipo de Negociação"**, **"Tipo de Operação"** e **"Parceiro"** não podem ser alterados em pedidos já faturados (parcial ou totalmente) sem o desvinculo prévio.
