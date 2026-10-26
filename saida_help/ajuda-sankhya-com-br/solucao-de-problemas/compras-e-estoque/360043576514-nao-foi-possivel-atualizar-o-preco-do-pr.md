---
id: "360043576514"
titulo: "Não foi possível atualizar o preço do produto \"X\" pois o seu novo preço \"R$\" é menor que o preço \"R$\" da regra da tabela \"0\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576514-N%C3%A3o-foi-poss%C3%ADvel-atualizar-o-pre%C3%A7o-do-produto-X-pois-o-seu-novo-pre%C3%A7o-R-%C3%A9-menor-que-o-pre%C3%A7o-R-da-regra-da-tabela-0"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:08Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "Produtos", "Configuração", "Atualização", "TOP", "Preferências", "Problema de Atualização de Preço do Produto: Preço Calculado Menor que o Preço de Tabela", "Erro"]
---

# Não foi possível atualizar o preço do produto "X" pois o seu novo preço "R$" é menor que o preço "R$" da regra da tabela "0"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16192155820183) MENSAGEM:**

Não foi possível atualizar o preço do produto "X" pois o seu novo preço "R$" é menor que o preço "R$" da regra da tabela "0". Verifique as configurações do item "X" na nota "Y".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16192155824407) SOLUÇÃO:**

![Imagem 3: Sintonize com os usuários certificados da sua empresa, que possuam detalhes dos processos internos, se de fato o Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/16192164840855) Sintonize com os usuários certificados da sua empresa, que possuam detalhes dos processos internos, se de fato o Tipo de Operação utilizado deverá ter o campo **"Precifica"** definido com a opção para atualização de preço de venda:

Tela: **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** » Aba: **Geral** » Campo: Precifica:

![Imagem 4: Tela: " Tipos de Operação - TOP " » Aba: Geral » Campo: Precifica :](https://ajuda.sankhya.com.br/hc/article_attachments/14684309671959)

Caso a configuração acima esteja incorreta, realize os devidos ajustes e refaça o lançamento.

![Imagem 5: Caso a atualização de preço de venda deva ocorrer, possivelmente a mensagem está sendo apresentada pois considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/16192164842007) Caso a atualização de preço de venda deva ocorrer, possivelmente a mensagem está sendo apresentada pois considerando sua fórmula de precificação atual, diante do valor informado para o item, o preço que está sendo calculado é MENOR que o preço de tabela atual.

![Imagem 6: Caso em sua empresa, esse cenário seja permitido, o parâmetro " DIMINUIPRECO" na tela " Preferências " (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/16192164843031) Caso em sua empresa, esse cenário seja permitido, o parâmetro "**DIMINUIPRECO"** na tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso: Configurações » Avançado » Preferências) deve ser ajustado para ligado.

![Imagem 7: Caso em sua empresa, esse cenário seja permitido, o parâmetro " DIMINUIPRECO" na tela " Preferências " (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/14684265627927)

![Imagem 8: Realizado o ajuste, teste a confirmação da nota. Valide a atualização de preço gerada através da tela " Variação de…](https://ajuda.sankhya.com.br/hc/article_attachments/16192164847767) Realizado o ajuste, teste a confirmação da nota. Valide a atualização de preço gerada através da tela **"[Variação de Preços de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753)"** e alinhe sobre a permanência do parâmetro ligado para situações futuras.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16192155830167) CAUSA:**

Ao tentar confirmar uma nota de compra com Tipo de Operação que atualize 'preço de venda', e o preço 'calculado' seja menor que o preço de tabela atual, a mensagem poderá ser apresentada.
