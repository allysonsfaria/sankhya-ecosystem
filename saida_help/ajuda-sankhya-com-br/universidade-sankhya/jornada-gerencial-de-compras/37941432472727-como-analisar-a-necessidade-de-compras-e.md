---
id: "37941432472727"
titulo: "Como analisar a necessidade de compras em função do giro ajustado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado"
trilha: "Universidade Sankhya > Jornada de Compras > Jornada Gerencial de Compras "
atualizado_em: "2026-07-22T14:04:22Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "Estoque", "Financeiro"]
---

# Como analisar a necessidade de compras em função do giro ajustado

| Categoria |
| --- |
| [Para que serve a sugestão de compra por giro ajustado na matriz de análise e quais seus benefícios?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKMY4WH97GJ20797RX0380) |
| [Quais os problemas que este recurso resolve para empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKN99JKKK3ZB2SDSNX3BJ4) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKNFV3FZNQ6VBXK7FFM6FW) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKNNMEM2515EJGQZYETTJZ) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKP09SM3XXNA2MM15R774N) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKP66MJ9CAKEPVTE498R5Q) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37941432472727-Como-analisar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-giro-ajustado#h_01KFXKPKB4M9A2FFG4E9QA8M5D) |

## Reposição do estoque em função do giro ajustado

#### Para que serve a sugestão de compra por giro ajustado na matriz de análise e quais seus benefícios?

A Sugestão de Compra Giro Ajustado é um cálculo que o sistema realiza para garantir que o estoque final fique dentro dos limites estabelecidos (entre o estoque mínimo e máximo). Este cálculo ajustado ajuda a manter os níveis de estoque adequados, evitando tanto a falta quanto o excesso de produtos em estoque, tornando o processo de compras mais eficiente e preciso.

#### Quais os problemas que este recurso resolve para empresa?

A Sugestão de Compra por Giro Ajustado resolve problemas relacionados à má gestão de estoques, como rupturas por falta de produtos e custos elevados por excesso de mercadorias paradas. Ao considerar os limites de estoque mínimo e máximo, esse recurso evita compras desnecessárias ou insuficientes, promovendo um equilíbrio entre disponibilidade e capital investido. Isso contribui para melhorar o giro dos produtos, reduzir perdas financeiras com vencimentos ou obsolescência e garantir que a empresa esteja sempre preparada para atender à demanda do mercado com agilidade e eficiência.

#### Quais os riscos de não utilizar?

Não utilizar a Sugestão de Compra por Giro Ajustado expõe a empresa a riscos como falta de produtos, excesso de estoque, compras mal planejadas e desperdício de recursos. Isso compromete a eficiência do processo de compras, afeta o fluxo de caixa e pode gerar insatisfação dos clientes, impactando diretamente os resultados do negócio.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/897256312)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

A Axis Ltda fazia pedidos de compra com base em previsões mensais e feeling da equipe. Durante uma campanha, o Produto 1, de alta demanda, esgotou rapidamente, gerando perda de vendas. Ao mesmo tempo, havia excesso de itens parados no estoque, ocupando espaço e imobilizando capital.

Diante desse desequilíbrio, a empresa percebeu a necessidade de utilizar a Sugestão de Compra por Giro Ajustado para alinhar reposições ao giro real dos produtos, evitando faltas e excessos.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela de **Análise de Giro**
2. Acesse a aba Detalhes da sugestão de compra

- A sugestão de compra giro ajustado, além de observar o giro médio diário tem o cuidado de avaliar os níveis de estoque mínimo e máximo definidos no cadastro do produto, pois caso ao comprar a sugestão de compra baseada no giro, se o estoque ficar abaixo do mínimo ou acima do máximo o sistema irá gerar um ajuste garantindo que não compre acima da capacidade do seu depósito e nem compre abaixo do nível mínimo defiindo no cadastro
- Para compreender as quantidades trazidas referente a compra giro ajustado, primeiramente deve encontrar o estoque final, ele é calculado da seguinte forma:

**Estoque final =** **Estoque atual + pedido de compra pendente - pedido de venda pendente + sugestão de compra giro**

- Caso o estoque final seja menor que o valor definido no campo estoque mínimo, será feito um ajuste utilizando para sugestão de compra o valor do estoque mínimo, então o cálculo ficaria desta forma:

**Sug. Compra Giro Ajustado = Sugestão de compra giro + (estoque mínimo - estoque final)**

- Caso o estoque final seja maior que o valor definido no campo estoque máximo, será feito um ajuste utilizando para sugestão de compra o valor do estoque máximo, então ficaria da seguinte forma:

**Sug. Compra Giro Ajustado = Sugestão de compra giro - (estoque final - estoque máximo) se negativo zerar**

#### Correção e Repetição

- Crie cenários diferentes, com períodos diferentes e analise também outros itens
- Verifique se o documento de preparação foi devidamente executado
