---
id: "360052062993"
titulo: "Troca de Tipos de Título"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052062993-Troca-de-Tipos-de-T%C3%ADtulo"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:46:00Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "Parâmetro impede troca no caixa.", "Troca de tipos de título restrita.", "Configuração de restrição por tipo."]
---

# Troca de Tipos de Título

No ato do recebimento de um título no caixa, podem ocorrer casos em que este será diferente do previsto no pedido de venda. Nestas situações, deve-se bloquear, por exemplo, a troca do tipo "Dinheiro" por "Cheque", pois este último requer consulta junto ao SPC, por exemplo. Já o processo contrário é permitido, pois qualquer tipo de título pode ser substituído por "Dinheiro".

O sistema faz a permissão de troca ou não do tipo de título, por meio do parâmetro **"Usa restrição de troca de título no recebimento? - USARESROTITREC"** que quando habilitado, não permite que a troca de tipos de título seja realizada no recebimento deste no caixa. Vejamos as configurações envolvidas neste processo:

![Imagem 1: Habilita-se o parâmetro de chave USARESROTITREC ;](https://ajuda.sankhya.com.br/hc/article_attachments/16585613287959) Habilita-se o parâmetro de chave USARESROTITREC;

![Imagem 2: Tela Tipos de Título ;](https://ajuda.sankhya.com.br/hc/article_attachments/16585613290903) Tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo);

- Com a ativação do parâmetro mencionado, nesta tela, será habilitada a aba **"Restrição para troca no caixa"**.
- Nela informa-se os tipos de título que não poderão ser utilizados para substituição no momento do recebimento no caixa. No exemplo retratado na imagem abaixo, o tipo de título **"Dinheiro"** não poderá ser modificado para os tipos de título **"Cheque"** e **"Cheque pré-datado"**.

![Imagem 3: Tela Cadastro de Usuários ;](https://ajuda.sankhya.com.br/hc/article_attachments/16585613293719) Tela [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios);

- Configura-se nesta tela, as particularidades de cada usuário e dentre elas, na aba **"Identificação"**, efetua-se a marcação **"Caixa"**.

![Imagem 4: No Portal de Vendas , efetua-se o lançamento de uma nota de venda, utilizando um tipo de título que possua em seu…](https://ajuda.sankhya.com.br/hc/article_attachments/16585628862359) No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela), efetua-se o lançamento de uma nota de venda, utilizando um tipo de título que possua em seu cadastro, uma restrição de tipos de título;

![Imagem 5: Na tela Movimentação Financeira ;](https://ajuda.sankhya.com.br/hc/article_attachments/16585613301015) Na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874);

- Acessando esta tela, localiza-se a nota lançada e ao tentar alterar o tipo de título, tem-se a validação realizada pelo parâmetro de chave USARESROTITREC sendo concretizada. No exemplo, tentou-se alterar o tipo de título Dinheiro para Cheque:
- Ainda na tela de Movimentação Financeira, ao realizar a baixa com vários títulos, não serão apresentados na pesquisa para utilização na baixa, os tipos de título restritos, ou seja, no exemplo utilizado neste tópico, os tipos de título **"3 - Cheque"** e **"5 - Cheque pré datado"**. Vejamos a imagem abaixo:

**Importante:** vale salientar que, caso não seja desejado que o sistema impeça a troca de tipos de título no recebimento, tem-se a opção de desativar o parâmetro de chave USARESROTITREC, ou caso o mesmo esteja ativado, não realiza-se a configuração da aba **"Restrição para troca no caixa"** na tela Tipos de Título.
