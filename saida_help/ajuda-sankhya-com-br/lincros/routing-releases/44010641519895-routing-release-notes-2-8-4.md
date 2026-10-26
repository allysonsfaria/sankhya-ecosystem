---
id: "44010641519895"
titulo: "[Routing] - Release Notes 2.8.4"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010641519895--Routing-Release-Notes-2-8-4"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T18:42:47Z"
rotulos: ["sync_hc", "lincros", "sync_hash_dce6044a7636", "lincros_13434180"]
---

# [Routing] - Release Notes 2.8.4

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44010672791319)

## Correções

## Correção no histórico da informação do usuário na tela de importação de pedidos via WS - Chamado 137709

Com a correção será apresentada a informação do usuário encaminhado na requisição do arquivo JSON;

---

## Correção na informação de prioridade de pedidos na tela da sessão - Chamado 137711

Após a correção será apresentado no mapa da sessão o identificador da prioridade ao lado do pedido, quando configurado e informado na importação do pedido.

---

## Correção no cadastro manual de clientes - Chamado 134217

Com a correção os clientes cadastrados manualmente, será realizado automaticamente o vínculo do setor.

---

## Informação do cálculo total do KM da rota - Chamado 135521

Com a correção a informação do cálculo do total do km será considerado a distância percorrida até o pernoite e do ponto de pernoite até o depósito.

---

## Correção na ação para visualizar o endereço do cliente após o clique duplo - Chamado 136167

Com a correção ao realizar a ação de clique duplo do mouse em cima de um pedido ou rota, serão apresentadas as informações de endereço do cliente.

---

## Correção de Latitude e Longitude na tela de cadastro de cliente - Chamado 138492

Corrigido a mensagem de erro ao atualizar as coordenadas com informação zerada.

---

## Correção no relatório de indicadores da Roteirização - Chamado 138254

Após a correção as informações apresentadas estão de acordo com as informações da sessão.

---

## Correção no relatório de Romaneio - Chamado 137275

Após a correção as informações de Km estão de acordo com o apresentado na rota.

---

## Correção na ação do Botão Otimizar

Após a correção o botão Otimizar está sendo disponibilizado para as rotas criadas manualmente.

---

## Correção na ação do Botão ocultar deslocamento - Chamado 136701

Com a correção a ação do botão ocultar deslocamento está ocultando o deslocamento até a primeiras entrega e a volta para o depósito.

---

## Integração de cliente entre TMS Lincros com o Routing - Chamado 136396

Realizada a correção na integração de clientes entre o TMS Lincros com o Routing.

---

## Clientes com mais de um pedido em rotas diferentes - Chamado 139802

Realizada a remoção do parâmetro **(Em clientes com mais de um pedido, marcar os pedidos como não roteirizados caso haja algum que não possa ser entregue no mesmo veículo)** da tela de início de sessão. Permanecendo nas configurações do depósito com a nomenclatura **(Agrupar todos os pedidos do mesmo cliente em uma única entrega.)**.

---

## Melhorias

## Nova funcionalidade de desagrupar pedidos agrupados de um mesmo pedido.

Foi incluído nova funcionalidade nos parâmetros do roteirizador (**Permitir agrupar/desagrupar todos os pedidos do mesmo cliente em todas as entregas dentro da sessão**), ao selecionar esta opção será adicionado botão na tela da sessão.

![Imagem 2: Foi incluído nova funcionalidade nos parâmetros do roteirizador ( Permitir agrupar/desagrupar todos os pedidos do mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/44010652929687)

Ao acionar o botão, os pedidos são desagrupados;

![Imagem 3: Ao acionar o botão, os pedidos são desagrupados;](https://ajuda.sankhya.com.br/hc/article_attachments/44010673074327)

![Imagem 4: Ao acionar o botão, os pedidos são desagrupados;](https://ajuda.sankhya.com.br/hc/article_attachments/44010657944087)

---

## Nova funcionalidade para inserir pedidos dentro da tela de iniciar uma sessão. [Link da Documentação](https://intercom.help/ajudalincros/pt-BR/articles/13439472-routing-busca-de-pedidos-pelo-numero-para-iniciar-uma-roteirizacao)

Foi incluído um novo campo na tela de iniciar uma sessão para buscar os pedidos, sendo possível informar vários números de pedidos no filtro com separador "Vírgula" ou "Enter".

---

## Nova funcionalidade para iniciar uma sessão sem rodar o algoritmo. [Link da Documentação](https://intercom.help/ajudalincros/pt-BR/articles/13439446-routing-iniciar-uma-nova-sessao-de-roteirizacao)

Com a nova funcionalidade quando não informado nenhum veículo para iniciar uma sessão, todos os pedidos serão incluídos como **não roteirizados**.

---

## Adicionado novas mensagens para o botão CRTL+Z na tela da sessão.

Adicionado novas mensagens para auxiliar na execução do botão CRTL+Z.

---

## Alteração da nomenclatura "Valor Máximo Rota" para "Valor Alvo" e melhoria nas informações da sessão. [Link da Documentação](https://intercom.help/ajudalincros/pt-BR/articles/13438690-routing-valor-alvo-para-as-rotas)

Com a nova melhoria será apresentado nas informações da rota o valor total nas cores: Amarelo (valor inferior ao Valor Alvo), Verde (igual ao Valor Alvo), Vermelho (superior ao Valor Alvo).

---

## Melhoria na ação de reimportar pedidos - chamado 136354

Foi realizado melhoria na ação de reimportar pedidos com erros, unificando em um único arquivo os pedidos com e sem erros.

---

## Melhoria no cadastro de disponibilidade de veículo

Com a melhoria será possível informar uma data de inicio e de fim para a validade da disponibilidade.

![Imagem 5: Com a melhoria será possível informar uma data de inicio e de fim para a validade da disponibilidade.](https://ajuda.sankhya.com.br/hc/article_attachments/44010635629591)

---

## Melhoria na tela de importação de pedidos.

Com a melhoria será possível identificar o total de pedidos importados, pedidos com erros e o total de linhas do arquivo.

![Imagem 6: Com a melhoria será possível identificar o total de pedidos importados, pedidos com erros e o total de linhas do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010642708247)

![Imagem 7: Com a melhoria será possível identificar o total de pedidos importados, pedidos com erros e o total de linhas do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010673615895)
