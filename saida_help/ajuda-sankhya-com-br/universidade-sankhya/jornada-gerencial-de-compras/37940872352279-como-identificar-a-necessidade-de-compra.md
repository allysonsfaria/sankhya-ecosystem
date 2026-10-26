---
id: "37940872352279"
titulo: "Como identificar a necessidade de compras em função do estoque mínimo e máximo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo"
trilha: "Universidade Sankhya > Jornada de Compras > Jornada Gerencial de Compras "
atualizado_em: "2026-07-22T14:04:25Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "Estoque", "Sankhya"]
---

# Como identificar a necessidade de compras em função do estoque mínimo e máximo

| Categoria |
| --- |
| [Qual a importância da reposição do estoque em função do mínimo e máximo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFXJMPEKS6CN3M0Y5FEE3JNK) |
| [Quais os problemas que este recurso resolve para empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFXJN0NZ6QC5JGVEN63WCPHC) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFXJN7P0ANB9FC4YQG8ZQY2Q) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFXJNJAEZRJ3TZK38N7NNXP0) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFXJNQZQ1J4DN0R6NST78WMF) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37940872352279-Como-identificar-a-necessidade-de-compras-em-fun%C3%A7%C3%A3o-do-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFXJNXYB3S6Y0J7XNQV91MQ7) |

## Reposição do estoque em função do estoque mínimo

#### Qual a importância da reposição do estoque em função do mínimo e máximo?

A reposição de estoque baseada em níveis mínimos e máximos é essencial para evitar rupturas de estoque e excesso de produtos, garantindo disponibilidade sem imobilizar capital desnecessariamente. Ao definir um nível mínimo, evita-se a falta de produtos, enquanto o nível máximo previne compras excessivas, reduzindo custos de armazenamento e desperdício. Esse método otimiza o capital de giro, facilita o planejamento de compras, melhora a previsibilidade e permite a automação do processo, proporcionando eficiência operacional e melhor atendimento ao cliente.

#### Quais os problemas que este recurso resolve para empresa?

- **Falta de produtos em estoque (rupturas):** Leva à perda de vendas e insatisfação dos clientes devido à indisponibilidade de produtos.
- **Excesso de estoque:** Gera custos elevados de armazenamento e risco de perdas por obsolescência ou deterioração.
- **Planejamento de compras ineficiente:** Resulta em compras desorganizadas, falta de previsibilidade e dificuldades nas negociações com fornecedores.
- **Imobilização de capital desnecessária:** Compromete o capital de giro da empresa, limitando recursos para outras operações importantes.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052296315)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na **Axis**, parte do portfólio é composto por produtos de alto giro. A falta recorrente de alguns itens tem afetado a produtividade da equipe e gerado atrasos nas operações, evidenciando a necessidade de um controle mais eficiente. 
Para apoiar esse processo, o sistema ERP Sankhya disponibiliza à compradora uma ferramenta que permite acompanhar o consumo, definir os níveis de estoque mínimo e máximo e evitar rupturas no estoque.

**Tarefa:** Identifique a necessidade de compra de produtos com base nos dados gerados pelo processamento da matriz na Análise de Giro.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Na tela de **Análise de Giro**
2. Acesse a aba Detalhes da sugestão de compra

- Veja que a matriz de giro calcula 03 sugestões de compra (sugestão de compra, sugestão de compra giro e sugestão de compra giro ajustada)
- Na Sugestão de compra, analise o valor trazido nos campos Estoque mínimo, Estoque, Pedido de compra pendente e pedido de venda pendente
- Para trazer o valor do campo Total encontrado na Sugestão de compra, o sistema processa o seguinte cálculo: Sug. Compra = (Estoque mínimo + percentual de acréscimo na sugestão de compras) - Estoque - Compra pendente + Venda pendente)
- O campo % de acréscimo da sugestão de compra podemos validar nas configurações da matriz de giro
- O campo estoque é alimentado com a quantidade disponível do produto naquela data, onde podemos validar pelo pelo cadastro do Produto na aba Estoque, no campo Estoque ou também através da tela Gerência de produtos
- O campo compra pendente irá trazer as quantidades negociadas nos pedidos de compra que ainda estão pendentes de faturamento, ou seja que ainda não deram entrada no estoque da empresa
- O campo venda pendente irá trazer as quantidades negociadas nos pedidos de venda onde as TOP’s utilizadas não façam reservas de estoque, e podemos validar caso exista algum valor alimentado neste campo, na própria tela da análise de giro, na coluna Compra/Venda pendente, ou até mesmo acessando os portais e fazendo a consulta pelo tipo de  movimento Pedido
- Então podemos entender que essa sugestão de compra observa os níveis cadastrados no produto para estoque mínimo, caso, seu estoque atual considerando os pedidos pendentes esteja abaixo do mínimo definido, será gerada uma sugestão de compra que será exibida no campo Total ao final da linha denominada Sug. Compra presente na aba Detalhes da sugestão de compra

#### Correção e Repetição

- Se os valores sugeridos não forem os esperados, revise o processo e corrija as informações necessárias antes de tentar novamente.
- Assegure-se de seguir todos os passos repassados no vídeo demonstrativo para evitar erros recorrentes.
- Para reforçar sua habilidade no sistema, pratique criando um novo cenário, como um fornecedor, cliente ou produto diferente.
