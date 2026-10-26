---
id: "360044611574"
titulo: "Montagem de Romaneio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611574-Montagem-de-Romaneio"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-20T15:46:55Z"
rotulos: ["AJUDA DO SKW", "manual", "Ordem de Carga", "Faturamento", "Romaneio", "Transporte", "TOP", "Produção", "br.com.sankhya.producao.montagem.romaneio", "Montagem de Romaneio manual", "Planejamento de Produção", "Quantidade a Produzir", "Gerar Romaneio"]
---

# Montagem de Romaneio

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311910116503) Módulo: Comercial > Rotinas > Produção
```

---

Nesta tela, você visualiza os planejamentos feitos na tela de Planejamento de Produção, que respeitam o painel de filtro na parte esquerda da tela e que foram liberadas na tela de Planejamento de Produção.

![Tela](https://ajuda.sankhya.com.br/hc/article_attachments/15620160189335)

A **"Data do Carregamento"** será preenchida automaticamente ao abrir a tela, com a data do dia.

O campo **"Transportadora"** é de preenchimento obrigatório e deve ser preenchida pelo usuário.

Você também deve informar a **"Empresa"**, porém, ela será salva sempre que você realizar um filtro e, ao abrir a tela novamente, a Empresa virá preenchida com a última que foi utilizada.

O campo **"Pedido/Nota"** e o campo **"Produto"** são filtros rápidos.

A marcação **"Apresentar Atrasadas"** faz com que o sistema ignore a data inicial de carregamento para planejamentos que não foram entregues totalmente.

A marcação **"Apenas c/ qtd a produzir"** sempre estará habilitada ao abrir a tela, e faz uma filtragem mostrando somente os planejamentos que não foram entregues totalmente.

O botão ![clip4831](https://ajuda.sankhya.com.br/hc/article_attachments/360061022014) **"Gerar Romaneio"** somente estará habilitado caso haja linhas na grade.

Ao clicar no botão Gerar Romaneio, na parte superior da tela, o sistema irá exibir um pop-up. Assim, você preenche as informações que serão usadas para a geração da Ordem de Carga e para faturar os pedidos.

![Imagem 4: Ao clicar no botão Gerar Romaneio , na parte superior da tela, o sistema irá exibir um pop-up. Assim, você preenche as…](https://ajuda.sankhya.com.br/hc/article_attachments/15620125560471)

Caso a coluna **"Qtd. a gerar"** das linhas da grade esteja em branco ou com valor zero, o sistema irá mostrar uma mensagem informando que é necessário preencher essa coluna com valores maiores do que zero.

Se a marcação **"Agrupar Pedidos quando possível"** estiver realizada no momento do faturamento dos pedidos e houver pedidos para o mesmo parceiro, o sistema irá juntar os produtos desses pedidos em apenas uma nota.

Ao término da Geração do Romaneio, o sistema irá exibir um pop-up informando o número da Ordem de Carga que foi gerado e perguntará se você deseja abrir a tela de Pré-Faturamento, que será utilizada para imprimir as Etiquetas e o Romaneio.

Durante a Geração do Romaneio, o sistema cria também algumas Ordens de Produção.

Para a geração dessas Ordens de Produção, é necessário informar no parâmetro **"TOP para produção - TOPPRODUCAO"** um Tipo de Operação (TOP) que seja do tipo **"F – Produção"**. Caso não seja informado essa TOP, ela não exista, ou não seja de Produção, o sistema irá parar a Geração do Romaneio e exibirá uma mensagem te informando sobre o preenchimento do parâmetro.
