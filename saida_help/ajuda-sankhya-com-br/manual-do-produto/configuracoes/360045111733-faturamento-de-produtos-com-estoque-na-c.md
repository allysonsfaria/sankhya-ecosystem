---
id: "360045111733"
titulo: "Faturamento de Produtos com Estoque na Confirmação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111733-Faturamento-de-Produtos-com-Estoque-na-Confirma%C3%A7%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:58:14Z"
rotulos: ["Configuração", "Faturamento", "Faturamento de Produtos com Estoque na Confirmação", "SERIEVNDPADRAO", "Faturamento de Produtos com Estoque na Confirmação manual", "TOP", "Vendas", "Estoque", "Confirmação de Notas"]
---

# Faturamento de Produtos com Estoque na Confirmação

É possível executar o faturamento de produtos com estoque na confirmação do pedido/requisição, ou seja, na Central - Vendas | Mov. Internas do Sankhya Om, quando você Confirmar o Pedido de Venda ou de Requisição, o sistema abrirá uma janela para você digitar algumas informações e já faturar o pedido diretamente daí.

A marcação **"Fatura Produtos com Estoque na Confirmação"**, do [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba **"Estoque"**, só será habilitada para os Tipos de movimentos Pedido de Venda ou Pedido de Requisição e, deve estar realizada, para a funcionalidade ser habilitada.

Após fazer as marcações necessárias na TOP, ao lançar um Pedido de Venda ou de Requisição e confirmá-lo, o sistema exibirá uma janela, onde deve ser informada a **"TOP"**, a **"Série"** e a **"Data Saída/Hora Saída"** para o faturamento.

[GIF animado: Imagem 1: Após fazer as marcações necessárias na TOP , ao lançar um Pedido de Venda ou de Requisição e confirmá-lo, o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/360086258694)

O campo Hora Saída só ficará visível se o parâmetro **"Imprimir hora entrada/saída no DANFE? - IMPHRSAIDADANFE"** estiver habilitado. Caso seja informado um neste campo e não tenha sido informado nada no campo Data Saída, o sistema utilizará a data atual como Data Saída.

Caso tenha informado no Cadastro da TOP, algum valor para o campo **"TOP p/Faturamento"** (no caso de Pedido de Venda) ou **"TOP p/Devolução"** (no caso de Pedido de Requisição), o campo TOP ficará desabilitado para edição e virá preenchido com o valor informado no respectivo campo do Cadastro da TOP:

[GIF animado: Imagem 2: Caso tenha informado no Cadastro da TOP , algum valor para o campo " TOP p/Faturamento" (no caso de Pedido de Venda )…](https://ajuda.sankhya.com.br/hc/article_attachments/360086259034)

O texto que é exibido abaixo do campo TOP, é derivado dos campos **"Tipo de Numeração"** e **"Base numeração"**.

Na tela [L](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites)[iberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites), existe a opção **"Confirmar notas selecionadas"** no botão **"Outras Opções..."** que, se a nota não estiver confirmada, ela poderá ser confirmada clicando nesse item; nesse caso, se a TOP do Pedido estiver configurada para **"Fatura Produtos com Estoque na Confirmação"** e os campos TOP p/Faturamento ou TOP p/Devolução estiverem preenchidos, o sistema fará o faturamento e não mostrará a tela de Preparação da Nota.

Se concluído, será apresentada a tela **"Resultados da confirmação das notas"**.

Existe também, a marcação **"Tentar confirmar a nota automaticamente"** ao clicar em **"Outras Opções..."**; neste caso, ao fazer a liberação, o sistema já tenta realizar a confirmação da nota; se a TOP estiver com a configuração acima, o sistema também irá tentar realizar o faturamento e exibirá a tela Resultados da confirmação das notas, caso tenha sucesso.
