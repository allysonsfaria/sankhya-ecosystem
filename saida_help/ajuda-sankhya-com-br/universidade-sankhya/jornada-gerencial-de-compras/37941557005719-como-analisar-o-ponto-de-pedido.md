---
id: "37941557005719"
titulo: "Como analisar o ponto de pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido"
trilha: "Universidade Sankhya > Jornada de Compras > Jornada Gerencial de Compras "
atualizado_em: "2026-07-22T14:04:21Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "Estoque", "Financeiro"]
---

# Como analisar o ponto de pedido

| Categoria |
| --- |
| [O que é o ponto de pedido?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKW6XK7XRY8RZBR9B3MV6J) |
| [Quais os problemas que este recurso resolve para empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKWHZTZ9NJD6M8HBJ8YND8) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKWR01QMA5ZNT8Y49D7W69) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKZD93R20FJ2CJCSND9KNG) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKX84V23S5XQ5ZAC50S42N) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKXEJ1C8JC6DXXJEKXRPZK) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941557005719-Como-analisar-o-ponto-de-pedido#h_01KFXKXPG00Y4KDEGPAKP0TPQZ) |

## Ponto de pedido

#### O que é o ponto de pedido?

Ponto de Pedido é o momento ideal para realizar um novo pedido de compra, garantindo que a empresa tenha tempo suficiente para repor o estoque antes que ocorra uma ruptura. Esse cálculo considera três fatores principais: o estoque atual disponível, o Lead Time (tempo necessário para o fornecedor entregar o produto) e o estoque de segurança, que funciona como uma reserva estratégica para evitar falta de mercadoria em caso de atrasos ou aumento inesperado na demanda. Assim, o sistema exibe a data prevista em que o pedido deve ser lançado para assegurar que os produtos estejam disponíveis no momento certo, mantendo a operação fluida e evitando perdas por falta de estoque.

#### Quais os problemas que este recurso resolve para empresa?

O recurso de ponto de pedido resolve problemas como a ruptura de estoque, o atraso no atendimento de pedidos, a perda de vendas por falta de produtos e a reposição desorganizada. Ele garante que os pedidos de compra sejam realizados no momento certo, evitando tanto faltas quanto excessos, e promovendo uma gestão de estoque mais eficiente e alinhada à demanda real.

#### Quais os riscos de não utilizar?

Não utilizar o ponto de pedido aumenta o risco de compras reativas e emergenciais, que costumam ter custos mais altos e menor poder de negociação com fornecedores. Além disso, compromete o planejamento da cadeia de suprimentos, gera instabilidade no fluxo operacional e dificulta a previsibilidade financeira da empresa.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1104585682)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

Carlos é o responsável pelo setor de compras da empresa Axis Ltda. Durante uma análise semanal de estoque, ele percebe que alguns itens com alta saída estão se aproximando de níveis críticos. Sabendo que o prazo médio de entrega dos fornecedores é de 7 dias e que há uma demanda constante desses produtos, Carlos acessa o sistema ERP para consultar o ponto de pedido de cada item.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela de **Análise de Giro**
2. Nos campos da matriz, localize o “Ponto de pedido”
3. Esse campo é calculado seguindo as seguintes regras:

- Quando o parâmetro "Somar o Lead Time aos dias úteis de estocagem - SOMALEADTIME" estiver ligado, a fórmula utilizada no cálculo do campo Ponto de Pedido será: **Ponto de Pedido = Data atual - 1 + (Duração de Estoque  - Duração do Estoque de Segurança - Lead Time - Dias Úteis de Estocagem)**.
- Se o parâmetro for desligado, e se tiver informações do Lead Time para o Produto selecionado, teremos: **Ponto de Pedido = Data Atual - 1 + (Duração de Estoque  - Duração do Estoque de Segurança - Lead Time)**.
- E se for desligado o parâmetro Somar o Lead Time aos dias úteis de estocagem - SOMALEADTIME, e não tiver informações referente ao Lead Time para o produto selecionado: **Ponto de Pedido = Data Atual - 1 + (Duração de Estoque  - Duração do Estoque de Segurança - Dias Úteis de Estocagem)**.

4. Faça a análise aplicando a fórmula de acordo com a configuração de sua base de testes e valide se a data informada como ponto de pedido esta correta

#### Correção e Repetição

- Analise diferentes itens
- Retorne no vídeo demonstrativo caso tenha dificuldades
