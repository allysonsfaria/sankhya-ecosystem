---
id: "39282533338519"
titulo: "Influência dos parâmetros DISTJDCONF, NVALIDARDESCMAX e DISTDESCPRODSM no desconto máximo do pedido de vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39282533338519-Influ%C3%AAncia-dos-par%C3%A2metros-DISTJDCONF-NVALIDARDESCMAX-e-DISTDESCPRODSM-no-desconto-m%C3%A1ximo-do-pedido-de-vendas"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-04T14:38:32Z"
rotulos: ["Produtos", "Configuração", "Liberação de Limites", "Venda Mais", "Artigo criado KCS", "CVE - KCS", "NVALIDARDESCMAX"]
---

# Influência dos parâmetros DISTJDCONF, NVALIDARDESCMAX e DISTDESCPRODSM no desconto máximo do pedido de vendas

### SITUAÇÃO

Ao lançar um pedido de vendas com desconto aplicado no campo **"Percentual de Desconto"** do rodapé, com valor superior ao desconto máximo cadastrado nos produtos, o sistema dispara os eventos de liberação **2 (Desconto Produto)** e **25 (Desconto por Item da Nota)**, que são aprovados normalmente.

Apesar da aprovação, ao **confirmar** o pedido o sistema recalcula o desconto de cada item, respeitando o desconto máximo do cadastro do produto (ou do Tipo de Negociação), e o valor do desconto no rodapé é reduzido ou zerado.

### SOLUÇÃO

**Confirme que o DISTJDCONF está ativo.** Ele é o parâmetro que ativa a distribuição automática do desconto do rodapé entre os itens. Se ele estiver desligado, essa distribuição não ocorre na confirmação e o problema descrito não se aplica.

**Escolha o parâmetro de acordo com o cenário:**

| **Parâmetro** | **O que faz** | **Quando usar** |
| --- | --- | --- |
| **NVALIDARDESCMAX** | Ignora completamente o desconto máximo (do produto e do Tipo de Negociação) na distribuição, permitindo até 100% de desconto por item | Quando o desconto aprovado na liberação deve prevalecer em qualquer produto, mesmo os que já têm desconto máximo cadastrado |
| **DISTDESCPRODSM** | Só afeta produtos **sem** desconto máximo cadastrado (0 ou nulo): nesse caso, usa o desconto máximo do Tipo de Negociação em vez de bloquear em 0 | Quando produtos com desconto máximo cadastrado devem continuar respeitando esse limite, e o ajuste é necessário só para produtos sem limite próprio |

**(1)** Acesse **Configurações > Avançado > Parâmetros do Sistema**.
**(2)** Localize o parâmetro desejado (**NVALIDARDESCMAX** ou **DISTDESCPRODSM**).
**(3)** Ative o parâmetro.
**(4)** Salve as alterações realizadas.

**Resultado:** com NVALIDARDESCMAX ativo, o desconto aprovado na liberação, inclusive acima do limite do Tipo de Negociação, é aplicado integralmente na distribuição. Com DISTDESCPRODSM ativo (e NVALIDARDESCMAX desligado), apenas produtos sem desconto máximo cadastrado passam a aceitar desconto até o limite do Tipo de Negociação; produtos com limite próprio continuam sendo respeitados.

### CAUSA

Esse comportamento só ocorre quando o parâmetro **DISTJDCONF** ("Distribuir desconto na confirmação da nota") está ativo. Com ele ligado, o sistema trata desconto lançado direto no item e desconto lançado no rodapé de formas diferentes:

- **Desconto lançado no item**: passa pela validação normal de liberação de limites (eventos 2 e 25). Uma vez aprovada, a liberação é respeitada.
- **Desconto lançado no rodapé**: na confirmação, esse valor precisa ser distribuído proporcionalmente entre os itens, porque a NF-e não aceita desconto só no total da nota, ele tem que estar detalhado por item. Essa distribuição é feita por uma rotina própria que recalcula o desconto de cada item com base no desconto máximo cadastrado, **sem considerar se já existe uma liberação aprovada para a nota**.

É por isso que o desconto aprovado é perdido: a liberação de limites aprova o desconto lançado, mas a rotina de distribuição do rodapé ignora essa aprovação e aplica o limite do cadastro de qualquer forma.
