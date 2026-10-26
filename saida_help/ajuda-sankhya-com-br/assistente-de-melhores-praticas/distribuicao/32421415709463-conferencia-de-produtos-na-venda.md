---
id: "32421415709463"
titulo: "Conferência de Produtos na Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32421415709463-Confer%C3%AAncia-de-Produtos-na-Venda"
trilha: "Assistente de Melhores Práticas > Distribuição"
atualizado_em: "2026-07-22T14:31:23Z"
rotulos: ["Produtos", "Configuração", "WMS", "Vendas", "Estoque"]
---

# Conferência de Produtos na Venda

### Descrição

A funcionalidade **Conferência de Produtos na Venda** permite configurar as preferências e liberar os acessos necessários para que os usuários realizem a conferência dos produtos antes da expedição dos pedidos ou notas.

Ela garante maior segurança e controle no processo de entrega, ao permitir que os itens sejam verificados via código de barras ou código do produto, antes de seguir para faturamento ou confirmação da nota.

Além disso, a solução possibilita:

- Configuração do momento da conferência (antes do faturamento ou antes da confirmação da nota).
- Definição do tipo de identificação dos produtos (por código de barras ou código do produto).
- Controle sobre cortes e divergências através de liberação de limites.
- Cadastro de usuários liberadores para autorizar os cortes quando necessário.

### Como instalar

1. Clique em **"Iniciar"**.

2. Selecione os **grupos e/ou usuários** responsáveis pela conferência de produtos na venda.

3. Clique em **"Avançar"**.

4. Defina o **momento da conferência**:

4.1 Antes do faturamento do pedido de venda (padrão).

4.2 Antes da confirmação da nota de venda.

5. Escolha o tipo de **identificação do produto**:

5.1 Código de barras (padrão).

5.2 Código do produto.

6. Configure a política de **liberação de limites** para cortes apontados:

6.1 Não exigir liberação (padrão).

6.2 Exigir liberação por pedido/nota.

6.3 Exigir liberação por produto.

7. Cadastre os **usuários liberadores**, caso tenha optado por exigir liberação de limites.
8. Clique em **"Avançar"**.
9. Revise o resumo com os dados selecionados.
10. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- Fila de Conferência

**Tabelas atualizadas**

**TGFCCO (Configuração de Conferência)**

- Inserção de nova configuração com regras de conferência
- Parâmetros como momento da conferência, modo de identificação do produto, tipo de liberação de corte, entre outros

**TGFTOP (Tipos de Operação)**

- Atualização do campo Configuração p/ Conferência (NUCCO) em tipos de operação de Pedido ou Venda, conforme o momento da conferência escolhido

**TSILIM (Limites de Liberação)**

- Caso exigida liberação de cortes, cadastro dos usuários liberadores para o evento 64 – Corte/divergência de pedido (Conferência)
