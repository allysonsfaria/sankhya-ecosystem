---
id: "360045110453"
titulo: "Redimensionamento de Lote"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110453-Redimensionamento-de-Lote"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:22Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Ordem de Serviço", "Novo tamanho do Lote", "Redimensionamento de Lote", "Redimensionamento de Lote manual", "Estoque", "Produção", "Regras para aumento e diminuição do lote", "Acesso e alteração do tamanho do lote", "Consequências e ajustes no estoque e dependências"]
---

# Redimensionamento de Lote

O acesso à rotina de **"Redimensionamento de Lote"** é realizada através da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o), aba [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o#abaprodutos), botão **"Redimensionar Lote"**.

![Imagem 1: O acesso à rotina de "Redimensionamento de Lote" é realizada através da tela Ordens de Produção , aba Produtos , botão…](https://ajuda.sankhya.com.br/hc/article_attachments/8878118572951)

Através desta rotina, é possível alterar o tamanho do lote de uma determinada Ordem de Produção, sendo que este tamanho pode ser maior ou menor que o tamanho atual.

Ao acionar o botão **"Redimensionar Lote"** será aberto o pop-up **"Novo tamanho do Lote"**, você pode em seguida confirmar ou cancelar a alteração.

![Imagem 2: Ao acionar o botão "Redimensionar Lote" será aberto o pop-up "Novo tamanho do Lote" , você pode em seguida confirmar ou…](https://ajuda.sankhya.com.br/hc/article_attachments/8878154570391)

**Regras de um redimensionamento**

A seguir iremos tratar de algumas regras de um redimensionamento:

Quando o novo tamanho de lote é maior que o tamanho de lote atual:

- Todas as atividades iniciais (atividades que acontecem logo em sequência a um evento de inicio) devem estar em andamento;
- Caso exista dependência com Ordens de Produção de Produtos Intermediários, essas OP's devem suportar o novo tamanho de lote, ou seja, deve ser possível alocar uma maior quantidade dos PI's nas ordens em questão para representar o novo tamanho de lote do Produto Acabado.

Quando o novo tamanho de lote é menor que o tamanho de lote atual:

- Não será permitido o redimensionamento, caso exista apontamento com quantidade apontada (PA) maior que o novo tamanho de lote.

**Consequências**

As consequências de realização de um Redimensionamento de Lote são:

- Ajuste da quantidade atual no repositório de Produto Acabado de execução das atividades em execução (quando a atividade utiliza repositório de PA);
- As operações de estoque geradas pela ordem em questão que fazem reserva de estoque, terão sua quantidade recalculada de acordo com o novo tamanho de lote;
- Caso exista dependência de PI para a ordem em questão, o sistema irá tentar redefinir a dependência com a ordem em questão, ou com outra ordem para o PI que possua quantidade disponível.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110453-Redimensionamento-de-Lote#top)
