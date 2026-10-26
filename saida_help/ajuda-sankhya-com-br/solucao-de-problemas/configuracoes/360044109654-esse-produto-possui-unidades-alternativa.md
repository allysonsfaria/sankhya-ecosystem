---
id: "360044109654"
titulo: "Esse produto possui unidades alternativas cadastradas e o controle adicional não pode ser alterado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109654-Esse-produto-possui-unidades-alternativas-cadastradas-e-o-controle-adicional-n%C3%A3o-pode-ser-alterado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:46Z"
rotulos: ["#PUBLIFER", "#SINTONIAWILKER", "CORE_E03864", "O.S 1288144", "Produtos", "Configuração", "Estoque", "Restrição na Alteração do Controle Adicional de Produto", "Erro", "Unidades Alternativas"]
---

# Esse produto possui unidades alternativas cadastradas e o controle adicional não pode ser alterado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16784254052887) MENSAGEM:**

[CORE\_E03864]: Esse produto possui unidades alternativas cadastradas e o controle adicional não pode ser alterado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16784254058519) SOLUÇÃO:**

- O sistema valida a alteração de controle adicional caso o controle anterior ou novo seja do tipo "Lista" ou "Livre" e exista alguma unidade alternativa cadastrada para o produto.
- Essa validação ocorre visto que para os dois casos tratam-se de controles que normalmente ficam registrados em cadastros e não apenas nas movimentações. Dessa forma, a liberação de alterações de controle poderão gerar inconsistências caso existam unidades alternativas com controle informado.
- Por exemplo, em um controle por lista, seria possível registrar uma unidade alternativa sendo "Caixa Azul" e outra "Caixa Vermelha", e uma mudança no tipo do controle deixaria estes cadastros de unidade alternativa inconsistentes.

Suponhamos que a empresa sempre trabalhou com "Canetas" controladas por Lista (Azul/Vermelha), e a partir de agora esse controle não irá mais existir. Para esse cenário é necessário compreender os detalhes que geram essa validação e avaliar junto ao implantador da empresa a aplicação das **práticas recomendadas** abaixo:

![Imagem 3: Caso não existam movimentações para as unidades alternativas cadastradas, será permitido a exclusão de seus cadastros,…](https://ajuda.sankhya.com.br/hc/article_attachments/16784254065303) Caso não existam movimentações para as unidades alternativas cadastradas, será permitido a exclusão de seus cadastros, e consequentemente a alteração do controle adicional. Para os demais casos, avaliar os próximos tópicos;

![Imagem 4: Inventariar os produtos que sofrerão a alteração, zerando seu estoque e finalizando todos os movimentos em aberto para…](https://ajuda.sankhya.com.br/hc/article_attachments/16784246605975) Inventariar os produtos que sofrerão a alteração, zerando seu estoque e finalizando todos os movimentos em aberto para evitar inconsistências;

![Imagem 5: Inative os respectivos produtos e realize novos cadastros desses, informando o controle adicional correto e desejado;](https://ajuda.sankhya.com.br/hc/article_attachments/16784246610071) Inative os respectivos produtos e realize novos cadastros desses, informando o controle adicional correto e desejado;

![Imagem 6: Realize os ajustes de estoque de entrada para os novos produtos, conforme controle adicional atual cadastrado para os…](https://ajuda.sankhya.com.br/hc/article_attachments/16784246612503) Realize os ajustes de estoque de entrada para os novos produtos, conforme controle adicional atual cadastrado para os mesmos;

![Imagem 7: Para relatórios ou análises de períodos anteriores, é importante considerar que os produtos foram alterados.](https://ajuda.sankhya.com.br/hc/article_attachments/16784246618775) Para relatórios ou análises de períodos anteriores, é importante considerar que os produtos foram alterados.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16784246625815) CAUSA:**

Ao tentar alterar o controle adicional de um produto, caso o controle anterior ou novo seja do tipo "Lista" ou "Livre" e exista alguma unidade alternativa cadastrada, essa alteração não será permitida.
