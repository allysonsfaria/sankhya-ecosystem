---
id: "39323368365975"
titulo: "Não é possível alterar ou excluir este item pois já existe nota fiscal de destino vinculada a ele."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39323368365975-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-ou-excluir-este-item-pois-j%C3%A1-existe-nota-fiscal-de-destino-vinculada-a-ele"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-31T02:17:43Z"
rotulos: ["Parceiro", "NF-e", "Faturamento", "Erro", "Artigo criado KCS", "CVE - KCS", "Documentos Eletrônicos"]
---

# Não é possível alterar ou excluir este item pois já existe nota fiscal de destino vinculada a ele.

### SITUAÇÃO

Esta mensagem aparece quando você tenta **"Alterar ou excluir um item"** em um pedido ou nota fiscal que já foi parcial ou totalmente faturado. O sistema impede a alteração porque já existe uma **"Nota fiscal de destino"** vinculada ao item.

### SOLUÇÃO

Para resolver o problema, siga os passos abaixo:

**(1)**  **Identifique o documento de destino:**

- Abra o lançamento (Portal de Vendas ou Compras) onde está tentando fazer a alteração;
- Selecione a nota que deseja alterar;
- Clique em **"Outras Opções"** > **"Documentos Relacionados"**;
- Na grade inferior, dê um duplo clique no **"Documento de Destino"** para visualizar o lançamento vinculado.

**(2)**  **Avalie as opções disponíveis:**

- Se precisar realmente alterar o item, será necessário primeiro cancelar, excluir ou desligar todas as notas de destino vinculadas a ele;
- Após remover os vínculos, realize as alterações necessárias.

**(3)**  **Alternativa para itens parcialmente faturados:**

- Em alguns casos, quando um item foi parcialmente faturado, o sistema permite a duplicação do item;
- O item original mantém a quantidade já faturada;
- Um novo item é criado com a quantidade pendente e as novas informações.

**Restrições importantes:**

- Não é possível alterar a **"Quantidade negociada"** para um valor menor que a quantidade já entregue;
- Itens totalmente faturados não podem ser alterados de forma alguma;
- Campos como **"Empresa"**, **"Tipo de Negociação"**, **"Tipo de Operação"** e **"Parceiro"** não podem ser alterados em pedidos já faturados.

### CAUSA

O erro acontece porque:

- O item que você está tentando modificar já foi faturado (possui quantidade entregue);
- Existe uma ligação entre o item do pedido original e um documento de destino;
- O sistema não permite alterações em itens já faturados para manter a integridade dos dados.
