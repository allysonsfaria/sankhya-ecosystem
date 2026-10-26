---
id: "43548085425047"
titulo: "Qual o impacto do \"% ajuste de demanda\" na demanda indireta do PI no MPS?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548085425047-Qual-o-impacto-do-ajuste-de-demanda-na-demanda-indireta-do-PI-no-MPS"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-10-09T21:27:56Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Qual o impacto do "% ajuste de demanda" na demanda indireta do PI no MPS?

A demanda indireta no **MPS (Plano Mestre de Produção)** refere-se à quantidade de um produto intermediário (PI) necessária para atender à produção de produtos acabados (PA) que o utilizam em sua composição. O ajuste dessa demanda é fundamental para garantir que todos os itens necessários estejam disponíveis no momento certo, evitando faltas ou excessos de estoque.

No Sankhya, a demanda indireta é automaticamente considerada no cálculo da necessidade de produção dos produtos intermediários, levando em consideração o **B.O.M**. 

O ajuste de demanda pode ser realizado por meio do campo **"% Ajuste Demanda" aba Geral** **no cabeçalho do plano**, tela **Planejamento de Produção (MRP I)**(Produção » Rotinas » Planejamento de Produção (MRP I))que aplica um percentual sobre a demanda bruta calculada do produto acabado, impactando os produtos intermediários.

### Como a demanda indireta é calculada

O cálculo da demanda indireta ocorre quando um produto intermediário é utilizado na composição de um produto acabado. O sistema verifica a quantidade de PI necessária para atender à produção dos PAs planejados no MPS. Assim, mesmo que não haja demanda direta para o PI, ele pode apresentar uma necessidade de produção devido à sua utilização em outros produtos.

Por exemplo, se um PA necessita de 10 unidades de um PI para cada unidade produzida, e a demanda ajustada do PA for de 100 unidades, a demanda indireta do PI será de 1.000 unidades. Essa quantidade será considerada no campo de demanda indireta do PI.

### Como o ajuste de demanda afeta o cálculo

O campo **"% Ajuste Demanda"** permite aumentar ou reduzir**(valores negativos)** a demanda bruta calculada para todos os itens do MPS, incluindo os produtos intermediários. O sistema aplica o percentual definido sobre a demanda bruta e, consequentemente afeta a demanda indireta. Dessa forma, qualquer alteração no percentual de ajuste impacta diretamente a quantidade a ser produzida dos PIs.
