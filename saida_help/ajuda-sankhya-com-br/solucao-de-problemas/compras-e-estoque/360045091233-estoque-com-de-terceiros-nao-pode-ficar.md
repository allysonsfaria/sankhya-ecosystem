---
id: "360045091233"
titulo: " Estoque com/de Terceiros não pode ficar negativo. Produto: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045091233--Estoque-com-de-Terceiros-n%C3%A3o-pode-ficar-negativo-Produto-X"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-10-02T15:53:39Z"
rotulos: ["#PUBLIFER", "#revisadosilvio", "Produtos", "Configuração", "Parceiro", "estoque", "Terceiros", "ORA-20101", "Gerenciamento de Estoque com Terceiros", "Solução", "Erro"]
---

#  Estoque com/de Terceiros não pode ficar negativo. Produto: 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18588656376855) MENSAGEM:**

ORA-20101: Estoque com/de Terceiros não pode ficar negativo. Produto: 'X'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588656389527) SITUAÇÃO:**

Mensagem apresentada ao realizar movimentações no sistema configuradas para 'Subtrair do Estoque próprio em poder de terceiros'.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588656407191) CAUSA:**

Mensagem apresentada ao realizar movimentações configuradas para 'Subtrair do Estoque próprio em poder de terceiros', quando não há estoque suficiente em poder do respectivo parceiro para o produto informado.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588656420759) SOLUÇÃO:**

Estoque COM Terceiros: Estoques pertencentes à empresa (propriedade), porém se encontram nas mãos de outra empresa (posse). Dessa forma a mensagem será apresentada quando não houver estoque suficiente registrado para o respectivo parceiro na tabela de estoques do produto. Para essa análise, siga as orientações abaixo:

![Imagem 5: Acessar a tela 'Consulta de Produtos', buscar pelo produto mencionado na mensagem de erro e avaliar o estoque atual…](https://ajuda.sankhya.com.br/hc/article_attachments/18588656438423) Acessar a tela 'Consulta de Produtos', buscar pelo produto mencionado na mensagem de erro e avaliar o estoque atual desse produto.

![Imagem 6: Verificar se para o parceiro que está sendo baixado o respectivo estoque, existe saldo 'Disponível' suficiente.…](https://ajuda.sankhya.com.br/hc/article_attachments/18588687371415) Verificar se para o parceiro que está sendo baixado o respectivo estoque, existe saldo 'Disponível' suficiente. Atente-se as informações de 'Local' e 'Controle' caso o produto trabalhe com essas.

![Imagem 7: Caso não exista estoque suficiente para essa operação, sintonize com o setor responsável, afim de avaliar se a…](https://ajuda.sankhya.com.br/hc/article_attachments/18588687374615) Caso não exista estoque suficiente para essa operação, sintonize com o setor responsável, afim de avaliar se a quantidade a ser registrada nessa movimentação de baixa encontra-se correta. Em caso positivo, avalie junto ao contador da empresa qual operação será registrada para entrada de estoque em poder de terceiros, para esse parceiro, que atualize o saldo e assim exista estoque suficiente.

**Importante:**

Caso tenha dúvidas sobre as configurações atuais do processo de estoque de terceiros realizado, verifique detalhes no artigo: [Melhores práticas para Configuração e Movimentação de Estoque com/de Terceiros.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579854)
