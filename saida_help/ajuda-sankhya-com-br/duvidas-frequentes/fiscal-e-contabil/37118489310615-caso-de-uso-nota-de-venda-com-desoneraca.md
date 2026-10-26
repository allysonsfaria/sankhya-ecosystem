---
id: "37118489310615"
titulo: "Caso de Uso: Nota de Venda com Desoneração/SUFRAMA e Desconto no Total da Nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37118489310615-Caso-de-Uso-Nota-de-Venda-com-Desonera%C3%A7%C3%A3o-SUFRAMA-e-Desconto-no-Total-da-Nota"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:19:40Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SUFRAMA", "Impostos", "Desconto", "Rebalanceamento do desconto aplicado", "ICMS desonerado", "Nota de venda com desoneração", "Desoneração/suframa", "Desconto no total da nota", "Não possui desoneraçãp/SUFRAMA", "Nova aliquota de desconto", "Novo valor de desconto"]
---

# Caso de Uso: Nota de Venda com Desoneração/SUFRAMA e Desconto no Total da Nota

Este artigo apresenta um caso de uso de Nota de Venda com desoneração/SUFRAMA e desconto no total da nota. Ele descreve os principais pontos de configuração e o comportamento do sistema, com o objetivo de esclarecer como a desoneração impacta os impostos e como o desconto é corretamente aplicado no valor total da nota, garantindo conformidade fiscal e consistência nos cálculos.

**Cálculo do total do pedido:**

Quando o pedido de venda **não possui desoneração/SUFRAMA** e contém apenas **descontos nos itens**, o total do pedido é calculado da seguinte forma:

| `Total do pedido = Valor total dos produtos - Descontos nos itens + Despesas acessórias - Desconto no rodapé do lançamento` |
| --- |

![Imagem 1: Total do pedido = Valor total dos produtos - Descontos nos itens + Despesas acessórias - Desconto no rodapé do…](https://ajuda.sankhya.com.br/hc/article_attachments/37192082373783)

Quando faturamos o pedido para uma nota de venda, o sistema realiza o **rebalanceamento do desconto aplicado no total da nota**, considerando agora também o **desconto da desoneração/SUFRAMA**.

Para isso, o sistema calcula a **nova alíquota de desconto** da seguinte forma:

| `Nova alíquota de desconto (%) = (Valor do desconto no rodapé do pedido / Valor total líquido dos itens do pedido) * 100` |
| --- |

![Imagem 2: Nova alíquota de desconto (%) = (Valor do desconto no rodapé do pedido / Valor total líquido dos itens do pedido) * 100](https://ajuda.sankhya.com.br/hc/article_attachments/37192082373911)

Essa nova alíquota de desconto no rodapé da nota é aplicada sobre os seguintes valores da nota de venda, para encontrar o **novo valor de desconto**:

| `Valor total líquido dos itens - valor de desoneração do ICMS (incluindo despesas acessórias) + despesas acessórias * nova alíquota de desconto`  `Exemplo: (3.133,20 - 221,35 + 97,22) * 3,69% = 111,07` |
| --- |

Nesse ponto, devemos nos atentar à seguinte situação:

Como foi dado desconto no total da nota, o sistema precisa **distribuir esse desconto entre os itens**, para seguir as normas da NF-e 2.0. Existem duas formas de fazer isso, que podem ser consultadas na [Central de Ajuda NF-e 2.0](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043155074-NF-e-2-0-exige-que-o-desconto-do-p%C3%A9-da-nota-seja-distribu%C3%ADdo-entre-os-itens).

A NF-e 2.0 exige que o desconto do **pé da nota seja distribuído entre os itens**, e essa distribuição altera o valor total da nota, que havia sido calculado pelo faturamento.

Na etapa seguinte, haverá uma alteração no total da nota durante a confirmação. Ao ratear o desconto nos itens, o **total dos itens diminui** e, consequentemente, ocorre a **diluição do valor da base de ICMS**, reduzindo o valor de ICMS desonerado. Com isso, **menos desconto é aplicado no total da nota**, aumentando o valor final da nota, e os valores de "desconto no total da nota" são zerados pelo sistema.

![Imagem 3: Na etapa seguinte, haverá uma alteração no total da nota durante a confirmação. Ao ratear o desconto nos itens, o total…](https://ajuda.sankhya.com.br/hc/article_attachments/37192118320151)
