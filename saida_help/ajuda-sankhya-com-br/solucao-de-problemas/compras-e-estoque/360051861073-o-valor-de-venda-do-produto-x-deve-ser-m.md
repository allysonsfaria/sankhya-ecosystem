---
id: "360051861073"
titulo: "O valor de venda do produto 'X' deve ser maior que ZERO"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051861073-O-valor-de-venda-do-produto-X-deve-ser-maior-que-ZERO"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:30:12Z"
rotulos: ["CORE_E01699", "Produtos", "Configuração", "TOP", "Preferências", "Valor de Venda Inválido para o Produto 'X'"]
---

# O valor de venda do produto 'X' deve ser maior que ZERO

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15936103722647) MENSAGEM:**

[CORE\_E01699] O valor de venda do produto 'X' deve ser maior que ZERO.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15936125748887) CAUSA:**

Ao tentar confirmar uma nota de compra com Tipo de Operação que atualize 'preço de venda', e o preço "calculado" seja menor que o preço de tabela atual, a mensagem poderá ser apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15936103724695) SOLUÇÃO:**

![Imagem 4: Sintonize com os usuários certificados da sua empresa, que possuam detalhes dos processos internos, se de fato o Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/15936103725719) Sintonize com os usuários certificados da sua empresa, que possuam detalhes dos processos internos, se de fato o Tipo de Operação utilizado deverá ter o campo 'Precifica' definido com a opção para atualização de preço de venda:

**Tela:**Tipos de Operação - TOP >> **Aba**: Geral >> **Campo:** Precifica:

![Imagem 5: Tela: Tipos de Operação - TOP >> Aba : Geral >> Campo: Precifica:](https://ajuda.sankhya.com.br/hc/article_attachments/15936116499991)

 Caso a configuração acima esteja incorreta, realize os devidos ajustes e refaça o lançamento.

![Imagem 6: Caso a atualização de preço de venda deva ocorrer, possivelmente a mensagem está sendo apresentada pois considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/15936103727255) Caso a atualização de preço de venda deva ocorrer, possivelmente a mensagem está sendo apresentada pois considerando sua Fórmula de precificação atual, diante valor informado para o item, o preço que está sendo calculado é MENOR que o preço de tabela atual.

![Imagem 7: Caso em sua empresa, esse cenário seja permitido, o parâmetro DIMINUIPRECO (Tela Preferências/Configurações/Avançado)…](https://ajuda.sankhya.com.br/hc/article_attachments/15936125754007) Caso em sua empresa, esse cenário seja permitido, o parâmetro **DIMINUIPRECO**(Tela Preferências/Configurações/Avançado) deve ser ajustado para **LIGADO**.

![Imagem 8: Caso em sua empresa, esse cenário seja permitido, o parâmetro DIMINUIPRECO (Tela Preferências/Configurações/Avançado)…](https://ajuda.sankhya.com.br/hc/article_attachments/15936103493271)

![Imagem 9: Realizado o ajuste, teste a confirmação da nota. Valide a atualização de preço gerada através da tela 'Variação de…](https://ajuda.sankhya.com.br/hc/article_attachments/15936103729431) Realizado o ajuste, teste a confirmação da nota. Valide a atualização de preço gerada através da tela 'Variação de Preços de Produtos' e alinhe sobre a permanência do parâmetro ligado para situações futuras.
