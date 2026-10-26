---
id: "37943400554263"
titulo: "Como realizar o ajuste de estoque de produtos controlados por série"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie"
trilha: "Universidade Sankhya > Jornada de Inventário"
atualizado_em: "2026-07-22T14:04:13Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "Sankhya"]
---

# Como realizar o ajuste de estoque de produtos controlados por série

| Categoria |
| --- |
| [Qual é o objetivo de se realizar o ajuste de estoque por série?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ0MF37FXBJP5YC24V1DBD) |
| [Quais problemas esse recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ43TA8SFC3BX92GDPBWDJ) |
| [Quais os riscos de não se fazer o ajuste de estoque por série?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ4A7DV52RDNW5652645S2) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ4FWJXHZMHAABW4261P0D) |
| [Cenário prático e passo a passo para realizar a atividade no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ50932GEMCDB3G3KH3194) |
| [Agora, efetue as movimentações no sistema conforme o contexto fornecido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ5H7SQPFDSDGKEMTJWJ59) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943400554263-Como-realizar-o-ajuste-de-estoque-de-produtos-controlados-por-s%C3%A9rie#h_01KFXQ63E13G1T661QV5J2TADC) |

## Ajuste de estoque por Série

#### Qual é o objetivo de se realizar o ajuste de estoque por série?

O objetivo do ajuste por número de série é alinhar os registros do sistema com o estoque físico, garantindo que cada item com identificação individual esteja corretamente posicionado e controlado. Essa prática reforça a integridade do controle de produtos sensíveis, permite rastrear individualmente cada item e fortalece a segurança nas movimentações. É um recurso essencial para manter a confiabilidade do inventário e sustentar uma gestão orientada por dados reais.

#### Quais problemas esse recurso resolve?

- Inversão de produtos ou registros duplicados por erro operacional.
- Falta de controle sobre itens com rastreabilidade obrigatória.
- Dificuldade em localizar produtos específicos dentro do estoque.
- Falhas no processo de separação de pedidos com controle por série.
- Barreiras no atendimento de solicitações de troca ou garantia por falta de vínculo com o número de série.

#### Quais os riscos de não se fazer o ajuste de estoque por série?

Negligenciar esse processo compromete a rastreabilidade individual dos produtos, aumenta a chance de envio incorreto de itens e reduz a segurança no atendimento a trocas, devoluções e recalls. A ausência de ajustes por série pode gerar desconformidade com normas fiscais e regulatórias, prejudicar auditorias e resultar em perdas financeiras por extravios não detectados. Além disso, decisões baseadas em dados imprecisos enfraquecem o planejamento e a eficiência operacional da empresa.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052364171)

#### Cenário prático e passo a passo para realizar a atividade no sistema

**Contexto:** Após a realização de um inventário físico no setor de notebooks, a equipe de estoque da TechTools identificou divergências entre o estoque físico e os registros no sistema ERP Sankhya para o grupo de produtos notebooks. Alguns números de série estavam ausentes fisicamente, enquanto outros constavam no local sem estarem registrados no sistema. Isso indica possíveis falhas em processos de movimentação, expedição ou recebimento.

**Tarefa:** Realize os ajustes de estoque no ERP Sankhya, corrigindo as discrepâncias entre o estoque físico e o sistema, com base na conferência por número de série. Garanta que todos os itens estejam corretamente registrados e reflitam a situação real do estoque, assegurando rastreabilidade e confiabilidade nos dados.

#### Agora, efetue as movimentações no sistema conforme o contexto fornecido

1. Acesse a tela **Ajuste de Estoque Por Série**
   Menu: Inventário » Arquivo » Ajuste de Estoque Por Série

- Informe a **Empresa** no campo indicado.
- Caso tenha realizado a cópia e a contagem por **Local**, informe no campo indicado.
- No campo **Preço unitário** selecione a opção **Usar o preço informado na TOP.**
- Informe as datas de **Cópia** e **Contagem** nos campos indicados.
- Clique no botão “**Ajustar**”.
- No pop-up Notas geradas as notas de saída e entrada para ajuste do estoque serão apresentadas.
- Dê um duplo clique no registro para ser direcionado à tela Central de Compras/Vendas.
- Clique em “**Confirmar**” para aprovar a nota gerada.

**Observação:** As operações de correção utilizam as TOPs de Ajuste de Estoque e não geram lançamentos no financeiro. Elas servem exclusivamente para realizar entradas e saídas no estoque, com o objetivo de alinhar os saldos físicos aos registros do sistema.

#### Correção e Repetição

- Revise os registros para confirmar se as operações foram concluídas.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo, retorne no vídeo demonstrativo novamente caso necessário.
