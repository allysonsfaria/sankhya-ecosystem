---
id: "44012034810775"
titulo: "Como realizar a devolução de um produto, gerar um vale-troca e emitir uma NFe de devolução?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012034810775-Como-realizar-a-devolu%C3%A7%C3%A3o-de-um-produto-gerar-um-vale-troca-e-emitir-uma-NFe-de-devolu%C3%A7%C3%A3o"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:17:00Z"
rotulos: ["sync_hc", "magis5", "magis5_204056240152", "sync_hash_8d149c28c6e4"]
---

# Como realizar a devolução de um produto, gerar um vale-troca e emitir uma NFe de devolução?

## Caso algum cliente opte por devolver um produto, é importante registrar essa devolução no Magis5 Hub para garantir um controle preciso do estoque e das transações.

Realizando a busca e localizando a venda desejada, você poderá prosseguir com o preenchimento dos detalhes da devolução, como o motivo, a data, o(s) produto(s) devolvido(s) e a quantidade. Essas informações são cruciais para rastrear a devolução e atualizar o estoque corretamente.

Após realizar este processo, será necessário emitir a nota fiscal de devolução, cujo objetivo é cancelar o processo de compra ou anular a própria nota fiscal. Isso é necessário quando a venda não é concluída ou quando é preciso cancelar uma nota fiscal que ultrapassou o prazo de cancelamento. Neste caso, a emissão da NFe de Devolução é obrigatória.

---

**REGISTRANDO UMA DEVOLUÇÃO**

Para registrar uma devolução, na barra de menus, clique em: Vendas → Devoluções de Vendas:

![Imagem 1: Para registrar uma devolução, na barra de menus, clique em: Vendas → Devoluções de Vendas:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-920-1024x195.png)

Clique em "Nova Devolução" para abrir os campos e iniciar o processo de devolução:

![Imagem 2: Clique em "Nova Devolução" para abrir os campos e iniciar o processo de devolução:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-23.png)

Para selecionar os produtos que deseja devolver, clique em "Pesquisa Avançada" e utilize os filtros fornecidos para localizar a venda específica:

![Imagem 3: Para selecionar os produtos que deseja devolver, clique em "Pesquisa Avançada" e utilize os filtros fornecidos para…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-20.png)

No exemplo abaixo, pesquisamos pelo cliente 'Marcio Tristão', e o sistema carregou suas vendas:

![Imagem 4: No exemplo abaixo, pesquisamos pelo cliente 'Marcio Tristão', e o sistema carregou suas vendas:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-21.png)

Clique em "Selecionar" para carregar os produtos da venda escolhida.

Caso possua o ID da venda, insira no campo apontado abaixo e clique em "buscar":

![Imagem 5: Caso possua o ID da venda, insira no campo apontado abaixo e clique em "buscar":](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-22.png)

Ao informar o ID da venda, o **Artemis5** carregará todos os itens da venda e você poderá informar quais itens poderá devolver. Caso vá devolver apenas um item, clique em “Remover Item” para remover os itens que não irá devolver.

![Imagem 6: Ao informar o ID da venda, o Artemis5 carregará todos os itens da venda e você poderá informar quais itens poderá…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-15.png)

Selecione o estoque ao qual o produto deverá ser retornado em "Estoque".

Importante lembrar que no momento da devolução é possível indicar o depósito para qual o produto será devolvido. Dessa forma, se o produto não estiver em condições para venda, selecione o depósito de avaria/erro, assim você não irá disponibilizar um produto sem qualidade para venda.

Em "Qtd. Dev." informe a quantidade de itens a serem devolvidos. É possível realizar várias devoluções para uma mesma venda até que todos os itens sejam devolvidos. Por exemplo:

Se um cliente comprou 5 unidades de um item, é possível registrar 5 devoluções, caso ele devolva um item por dia.

Em “Motivo da Devolução”, informe o motivo da devolução e clique em “Lançar Devolução”.

**Observação:** “Data de Validade” é opcional. Caso o seu empreendimento controle a data de validade dos produtos, informe-a no campo correspondente.

**EMITINDO UMA NOTA FISCAL DE DEVOLUÇÃO**

Se a venda devolvida ultrapassar o prazo de 24 horas, será necessário emitir uma Nota Fiscal de Devolução.

Para isso, após concluir o processo mencionado anteriormente, a devolução estará na "Lista de Devoluções".

![Imagem 7: Para isso, após concluir o processo mencionado anteriormente, a devolução estará na "Lista de Devoluções".](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-16.png)

Para emitir uma nota fiscal de devolução, clique no quadrado a direita, selecione a operação correspondente e clique em "Emitir NFe". Para saber qual a operação correta, valide o estado de origem e o estado de destino da devolução:

![Imagem 8: Para emitir uma nota fiscal de devolução, clique no quadrado a direita, selecione a operação correspondente e clique em…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-17.png)

A nota será processada automaticamente e ficará no status: "processando\_autorizacao". Para atualizar seu status, clique em "Atualizar status NFe" após alguns segundos:

![Imagem 9: A nota será processada automaticamente e ficará no status: "processando_autorizacao". Para atualizar seu status, clique…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-18.png)

A nota terá seu status atualizado e poderá ser baixada:

![Imagem 10: A nota terá seu status atualizado e poderá ser baixada:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-19.png)

Após registrar a devolução, o crédito referente à devolução ficará registrado na conta do usuário, podendo ser utilizado como "vale-troca" ao realizar um novo pedido.

Para utilizar um vale trocas, [clique aqui](https://ajuda.artemis5.com.br/como-utilizar-um-vale-trocas/)

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44012048706199)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
