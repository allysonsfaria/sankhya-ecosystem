---
id: "44010706275351"
titulo: "[Routing] - Release Notes 2.8.2"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010706275351--Routing-Release-Notes-2-8-2"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T18:43:14Z"
rotulos: ["sync_hc", "lincros", "lincros_13434220", "sync_hash_6de56fbcc1f6"]
---

# [Routing] - Release Notes 2.8.2

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44010661008023)

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

Com a correção a informação do cálculo do total do km será considerado a distância percorrida ate o pernoite e do ponto de pernoite até o depósito.

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

## Melhorias

## Nova funcionalidade de desagrupar pedidos agrupados de um mesmo pedido.

Foi incluído nova funcionalidade nos parâmetros do roteirizador (**Permitir agrupar/desagrupar todos os pedidos do mesmo cliente em todas as entregas dentro da sessão**), ao selecionar esta opção será adicionado botão na tela da sessão.

![Imagem 2: Foi incluído nova funcionalidade nos parâmetros do roteirizador ( Permitir agrupar/desagrupar todos os pedidos do mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/44010638061079)

Ao acionar o botão, os pedidos são desagrupados;

![Imagem 3: Ao acionar o botão, os pedidos são desagrupados;](https://ajuda.sankhya.com.br/hc/article_attachments/44010706695831)

![Imagem 4: Ao acionar o botão, os pedidos são desagrupados;](https://ajuda.sankhya.com.br/hc/article_attachments/44010706812823)

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

![Imagem 5: Com a melhoria será possível informar uma data de inicio e de fim para a validade da disponibilidade.](https://ajuda.sankhya.com.br/hc/article_attachments/44010665404567)

---

## Melhoria na tela de importação de pedidos.

Com a melhoria será possível identificar o total de pedidos importados, pedidos com erros e o total de linhas do arquivo.

![Imagem 6: Com a melhoria será possível identificar o total de pedidos importados, pedidos com erros e o total de linhas do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010661600791)

![Imagem 7: Com a melhoria será possível identificar o total de pedidos importados, pedidos com erros e o total de linhas do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010665631383)
