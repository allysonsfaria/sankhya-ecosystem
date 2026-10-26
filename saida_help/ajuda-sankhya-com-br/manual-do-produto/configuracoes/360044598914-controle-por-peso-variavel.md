---
id: "360044598914"
titulo: "Controle por peso variável"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:22Z"
rotulos: ["Produtos", "Configuração", "WMS", "Controle", "Recebimento", "Peso", "CHECKMAPAWMS", "ENDMANUAUTOWMS", "PESOVARWMS", "Reabastecimento", "Variável", "Controle por peso variável manual", "TOP", "Estoque", "Controle Eficiente por Peso Variável", "Peso Variável", "Tolerância"]
---

# Controle por peso variável

Algumas empresas podem trabalhar com a compra e venda de produtos onde seus pesos podem sofrer variações, dependendo do fornecedor e/ou cliente.

Pode existir casos onde, a separação dos produtos é feita por pedido, mas sua baixa, é realizada por quilo. Assim, o sistema conta com um recurso que possibilita o controle desta situação.

Acesse os links abaixo para navegar nas funcionalidades desta rotina:

[Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#configura%C3%A7%C3%B5esiniciais)                                      [Reabastecimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#Reabastecimento)

[Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#Recebimento)                                                      [Expedição de produtos com peso variável](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#Expedi%C3%A7%C3%A3odeprodutoscompesovari%C3%A1vel)

[Tolerância por quantidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#Toler%C3%A2nciaporquantidade)

## Configurações Iniciais

Inicialmente, habilite os parâmetros:

- Habilita controle de produtos com peso variável. - PESOVARWMS;
- Associar checkout na geração do mapa de separação do WMS. - CHECKMAPAWMS;
- Usa endereçamento manual automático. - ENDMANUAUTOWMS.

Feito isso, serão disponibilizados alguns campos para configuração, nas telas apresentadas a seguir.

![Imagem 1: Feito isso, serão disponibilizados alguns campos para configuração, nas telas apresentadas a seguir.](https://ajuda.sankhya.com.br/hc/article_attachments/1500012285182)

Em [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms), configure os campos abaixo:

A marcação **"Produto controlado por peso variável"**, se assinalada indica que o produto será controlado por peso.

Informe no campo  **"% de tolerância de peso a maior no recebimento"**, o percentual de tolerância para um peso maior que o solicitado no recebimento.

Indique no campo **"% de tolerância de peso a menor no recebimento"**, o percentual de tolerância para um peso menor que o solicitado no recebimento.

Na utilização de produtos controlados por peso variável, utilize o campo **"% de tolerância de peso a maior na separação"** para informar o percentual de tolerância de peso a mais na conclusão de tarefas de separação por código de barras.

De forma inversa ao campo anterior, informe no campo **"% de tolerância de peso a menor na separação"** o percentual de tolerância de peso a menos na conclusão de tarefas de separação por código de barras.

Defina no campo **"Unidade de separação para produtos com peso variável"**, a unidade utilizada na conferência no mapa de separação.

![Imagem 2: Defina no campo " Unidade de separação para produtos com peso variável" , a unidade utilizada na conferência no mapa de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012636221)

Realizado os procedimentos acima, na tela de [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), efetue as seguintes configurações nos campos:

Informe no campo **"Série TOP diferença a maior (peso variável)"**, a série da nota para venda, que será utilizada na TOP configurada no campo a seguir.

Indique no campo **"TOP diferença a maior (peso variável)"**, a TOP para nota de compra que será gerada, quando a quantidade for maior que a solicitada, e estiver fora do percentual de tolerância configurado no cadastro dos produtos.

Preencha o campo **"Série TOP diferença a menor (peso variável)"**, com a série da nota de compra que será utilizada na TOP configurada no campo a seguir.

No campo **"TOP diferença a menor (peso variável)"** informe a TOP para nota de venda que será gerada, quando a quantidade for menor que a solicitada, e estiver fora do percentual de tolerância configurado no cadastro dos produtos.

Ao realizar a separação que contenha produtos cujo controle é feito por peso variável, através do modelo de relatório configurado e informado no parâmetro **"Relatório p/ mapa de separação manual por pedido - RELMAPSEPMANPED"**, será apresentado o mapa de separação.

**Observação:** caso o parâmetro **"Associar checkout na geração do mapa de separação - CHECKMAPAWMS"** esteja ativado, será feita a busca por um endereço de checkout disponível, e será realizada a alteração do endereço de destino na tarefa.

Feita a geração do mapa de separação, acesse a rotina [Conclusão de Tarefas por Cód. de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613414), se existirem produtos com peso variável, será apresentado um pop-up, onde devem ser informados os dados de quantidade da separação e o peso do que foi separado; ao confirmar a quantidade solicitada é confrontada com os dados que foi indicado, levando em consideração os percentuais inseridos na aba WMS no Cadastro de Produtos, campos % de tolerância de peso a maior na separação e % de tolerância de peso a menor na separação:

[GIF animado: Imagem 3: Feita a geração do mapa de separação, acesse a rotina Conclusão de Tarefas por Cód. de Barras , se existirem produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012285222)

Caso as quantidades informadas sejam divergentes, será feita a validação do percentual configurado no campo % de tolerância de peso a maior na separação; se a quantidade exceder o limite de tolerância tanto para menor quanto para maior, será lançado um evento de liberação **"72 - Tolerância na variação de peso do pedido excedida (WMS)"** e exibida a tela de liberação na tela.

Se a quantidade estiver no limite tolerável, serão realizados todos os ajustes nas quantidades dos campos de origem, destino, estoque e quantidades negociadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#top)

## Reabastecimento

Na função de reabastecimento do coletor, caso o parâmetro **"Habilita controle de produtos com peso variável. - PESOVARWMS"** esteja habilitado e o produto a ser reabastecido encontre-se configurado com peso variável, será exibido o campo quantidade na segunda fase da tarefa.

Ao informar este campo, serão feitas as devidas validações conforme o campo **"% de tolerância de peso a maior no recebimento"**.

Caso a quantidade indicada seja menor que a quantidade do reabastecimento solicitado, será feita uma verificação, analisando se a quantidade informada no coletor é maior ou igual que a quantidade mencionada inicialmente; sendo esta quantidade menor, o reabastecimento não será concluído.

Se todas as validações forem concluídas sem nenhum erro, as quantidades serão atualizadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#top)

## Recebimento

Quando se está realizando o recebimento de itens que disponibilizam o controle por peso variável e outros que não possuam, e a partir de alguns desses itens é gerada uma divergência (controlados por peso que extrapolem a tolerância ou itens sem controles com divergência), as notas de ajuste serão geradas ao final do processo de recontagem do coletor, onde estes produtos que possuíam limite tolerável serão reprocessados e as notas geradas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#top)

## Expedição de produtos com peso variável

Esta configuração de peso variável, também é válida no processo de separação dos produtos por meio do coletor de dados. No coletor, ao bipar o endereço e produto na separação, será exibida uma tela para informar o peso real do produto separado e para que seja realizado um ajuste na quantidade solicitada no pedido:

![Imagem 4: Esta configuração de peso variável, também é válida no processo de separação dos produtos por meio do coletor de dados.…](https://ajuda.sankhya.com.br/hc/article_attachments/13005311597847)

Ao acionar o botão **"OK"** a quantidade informada no campo **"Peso Real"** é adicionada ao **"Peso Total"**.

![Imagem 5: Ao acionar o botão "OK" a quantidade informada no campo "Peso Real" é adicionada ao "Peso Total" .](https://ajuda.sankhya.com.br/hc/article_attachments/13005366303767)

O botão **"Limpar"** apaga o conteúdo do campo Peso Real e zera o Peso Total.

Na tela é apresentado um alerta sobre os excessos quanto ao peso real informado e ao peso da tarefa solicitada; para isso, tem-se um percentual de tolerância pré-fixado de **"15%"** tanto para maior quanto para menor.

Quando o peso informado excede essa tolerância, o valor no Peso Total é marcado na cor **vermelha**:

![Imagem 6: Quando o peso informado excede essa tolerância, o valor no Peso Total é marcado na cor vermelha :](https://ajuda.sankhya.com.br/hc/article_attachments/13005454702487)

Mesmo extrapolando tal quantidade, será possível confirmar a pesagem, sendo apresentado apenas o alerta com relação à quantidade informada:

Clicando em **"Não"**, retorna-se para a tela de pesagem para que se possa corrigir a quantidade; clicando em **"Sim"**, a operação de ajuste é executada.

Ao confirmar, a rotina ajusta as quantidades solicitadas no pedido, onde nas diferenças para maior, a quantidade solicitada é modificada para o peso real informado, nas diferenças para menor, é gerado um corte no pedido.

Também são realizados ajustes nos endereços de armazenagem (TGWEST) e nos itens de tarefa de separação (TGWITT).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#top)

## Tolerância por quantidade

Ao realizar as pegas da separação (produtos com metragem variável), as peças podem estar com uma quantidade acima ou abaixo da solicitada no pedido e/ou tolerância do produto. Deste modo, o sistema irá analisar a margem de tolerância por quantidade de acordo com os seguintes pontos:

- Quantidade acima, porém dentro da tolerância;
- Quantidade acima, porém fora da tolerância;
- Quantidade abaixo, porém dentro da tolerância;
- Quantidade abaixo, porém fora da tolerância.

Assim, você poderá efetuar a separação novamente ou continuar o processo.

![Imagem 7: Assim, você poderá efetuar a separação novamente ou continuar o processo.](https://ajuda.sankhya.com.br/hc/article_attachments/13005620380567)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598914-Controle-por-peso-vari%C3%A1vel#top)
