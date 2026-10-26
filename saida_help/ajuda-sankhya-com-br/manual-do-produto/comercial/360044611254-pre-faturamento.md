---
id: "360044611254"
titulo: "Pré-faturamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:25:54Z"
rotulos: ["AJUDA DO SKW", "manual", "Impressão", "NF-e", "Faturamento", "Pré-faturamento", "RECALVENCAPROV", "RECALVENCFAT", "Romaneio", "br.com.sankhya.prod.prefaturamento", "Pré-faturamento manual", "Transporte", "Painel de Filtros", "Refaturar Notas", "Impressão de DANFE", "Documentos Eletrônicos", "Comercial"]
---

# Pré-faturamento

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311939787543) Módulo: Comercial > Rotinas > Produção
```

---

Nesta tela é feita a confirmação dos romaneios gerados na tela [Montagem de Romaneio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611574). Na grade principal serão listadas as [Ordens de carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713) da empresa. Ao modificar a tela para o modo formulário, teremos na parte superior, os dados da Ordem de Carga (Empresa, Total da Carga, Veículo etc.) e na parte inferior uma segunda grade contendo os romaneios.

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#paineldefiltros)                                                                         [Tela Pré- Faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#telapr%C3%A9faturamento)     

[Botão Faturas...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#bot%C3%A3ofaturas)                                                                           [Botão Impressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#bot%C3%A3oimpress%C3%B5es)     

![Imagem 2: Botão Faturas... Botão Impressões](https://ajuda.sankhya.com.br/hc/article_attachments/4416520784407)

## Painel de Filtros

Os romaneios podem ser filtrados por meio do painel de filtros, localizado no lado esquerdo da tela. Ele é composto pelos seguintes campos:

O campo **"Cód. Barras da O.C."**, se refere ao Código de barras da Ordem de Carga;

Por meio do campo **"Empresa"**, busque pela empresa utilizada na geração do romaneio;

Informe no campo **"Transportadora"** a empresa transportadora correspondente ao romaneio;

Você poderá buscar o romaneio por meio do **"Motorista"** responsável pelo transporte da carga;

É possível identificar o romaneio pela **"Placa"** do veículo utilizado no transporte;

Localize os romaneios por meio de sua **"Situação"**, que pode ser:

- Pendente de confirmação;
- Confirmadas;
- Todas.

Pode-se localizar também os romaneios por meio do campo **"Nro. Ordem de Carga"**, onde deve-se informar a numeração da ordem de carga a ele vinculada;

Você poderá também identificar os romaneios por meio do número do **"Pedido/Nota"** a ele relacionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#top)

## Tela Pré-Faturamento

Por meio da tela Pré-faturamento, de acordo com o processo de cada empresa, trabalha-se também com pedidos de venda que serão faturados e darão origem a Notas Fiscais Eletrônicas. Ao clicar no botão **"Confirmar"** o sistema efetua o processo de faturamento do pedido de venda e gera a NF-e junto a SEFAZ. Além disso, realiza a confirmação dos romaneios referentes a Ordem de carga; são confirmadas as Ordens de Produção e as faturas de cada romaneio.

**Nota:** Sobre o processo de faturamento, caso o parâmetro **"Recalcular vencimento dos títulos no faturamento? - RECALVENCFAT"** esteja ativado, o vencimento dos financeiros dos títulos poderá ser recalculado; este comportamento ocorrerá nos seguintes casos:

- Se o título possuir apenas uma parcela e a data de vencimento desta for menor que a data atual (data do faturamento), seu vencimento será recalculado;
- Caso o título possua duas ou mais parcelas e a data destas parcelas seja menor que a data atual (data do faturamento), será feito a agrupamento em uma única parcela e seu correspondente vencimento recalculado.

Se a data de vencimento calculada, coincidir com a data de alguma parcela já existente, estas parcelas serão agrupadas. Além disso, os impostos da nota serão recalculados, exceto os que foram digitados, estes serão excluídos.

**Observação:** Caso o parâmetro **"Recalcular venc. títulos na aprovação (Sefaz)? - RECALVENCAPROV"** esteja ativado, será possível recalcular o vencimento dos financeiros de títulos que possuam o Tipo de Movimento Venda, antes que estes tenham seu lote enviado para aprovação na SEFAZ. O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) utilizado no lançamento do título em questão, deve estar com opção **"Vencimento pré-fixado no pedido"** localizada na  aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), desmarcada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#top)

## Botão Faturas

O botão **"Faturas..."** possui duas alternativas de utilização:

- **Ver faturas:** O acionamento desta opção, apresenta um pop-up denominado **"Notas faturadas"**, na qual você poderá visualizar as notas faturadas correspondentes ao romaneio em questão. Além disso, caso necessário, você pode acessar a nota (fatura) no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454), por meio do botão correspondente localizado no alto do pop-up;
- **Refaturar notas canceladas:** Por meio desta opção, será aberto um pop-up com esta mesma nomenclatura; informe a TOP e a Série de Faturamento, além de determinar pelo agrupamento de pedido quando possível. Poderão ser refaturadas, notas que por algum motivo particular de cada empresa, foram canceladas através do Portal de Vendas.

**Observação**: Ao realizar o cancelamento de uma nota, esta é desvinculada do romaneio antes de ser removida do mesmo. Por esse motivo, ao proceder com o cancelamento de uma nota, utilize a opção Refaturar notas canceladas, para que seja "refeita" a última etapa da montagem do romaneio, ou seja, será criada uma nota não confirmada, de modo que toda a Ordem de Carga ficará com o status de não confirmada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#top)

## Botão Impressões

Neste botão, você poderá escolher entre os seguintes tipos de impressão:

- **Impressão de etiquetas:** Por meio desta opção, o sistema imprime para cada embalagem que o produto possuir uma etiqueta, considerando a quantidade para produzir.
- **Reimpressão de etiquetas...:** Caso seja necessário, realize a reimpressão de etiquetas através desta opção.
- **Imprimir DANFE das faturas:** Por meio desta opção, você poderá utilizar o serviço de impressão dos DANFES correspondentes às faturas.
- **Imprimir Boletos das faturas:** Realize por meio desta opção, a impressão dos boletos pertinentes às faturas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611254-Pr%C3%A9-faturamento#top)
