---
id: "44012238569495"
titulo: "[Routing] - Release Notes 2.19"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012238569495--Routing-Release-Notes-2-19"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:23:42Z"
rotulos: ["sync_hc", "lincros", "sync_hash_808362ee2be7", "lincros_13434017"]
---

# [Routing] - Release Notes 2.19

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012267962391)

## Melhorias

---

## Relatório de Ações Sessão

Acrescentamos no relatório novas informações como Usuário, Placa, Rota, Pedidos e Clientes.

![Imagem 2: Acrescentamos no relatório novas informações como Usuário, Placa, Rota, Pedidos e Clientes.](https://ajuda.sankhya.com.br/hc/article_attachments/44012241635223)

---

## Cadastro de Checkpoint

Agora não será obrigatório definir região de início da rota, considerando o depósito como ponto inicial. Foi implementado a opção de utilizar um polígono, depósito ou setores como áreas de destino em que utilizaremos o checkpoint para definir a melhor porta de entrada para região.

![Imagem 3: Agora não será obrigatório definir região de início da rota, considerando o depósito como ponto inicial. Foi…](https://ajuda.sankhya.com.br/hc/article_attachments/44012206603287)

---

## Relatório Integrações Automáticas

Adicionamos a melhoria no relatório de integrações pedidos para buscar as integrações realizadas pela API /importacaoPedidos.

---

## Agrupamento de Pedidos

Foi implementado uma melhoria para agrupar a visualização dos pedidos não roteirizados no mapa de roteirização (conforme imagem abaixo), possibilitando em remover os pedidos desejados da rota. Para funcionar, é necessário habilitar o parâmetro "Agrupar todas atividades não roteirizadas de um mesmo cliente em uma única atividade" no cadastro do depósito.

![Imagem 4: Foi implementado uma melhoria para agrupar a visualização dos pedidos não roteirizados no mapa de roteirização…](https://ajuda.sankhya.com.br/hc/article_attachments/44012226839703)

---

## Painel Geocode

Na tela inicial do sistema foi adicionado o painel de confiabilidade de geolocalização.

![Imagem 5: Na tela inicial do sistema foi adicionado o painel de confiabilidade de geolocalização.](https://ajuda.sankhya.com.br/hc/article_attachments/44012268767895)

---

## Filtro Grupo Setor

Foi adicionado a melhoria na tela iniciar uma nova sessão de roteirização, que permite realizar o filtro setor pelo nome do grupo vinculado ao setor.

![Imagem 6: Foi adicionado a melhoria na tela iniciar uma nova sessão de roteirização, que permite realizar o filtro setor pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/44012206988311)

---

## Validação de Restrição de Veículos Perfil OSRM

Implementamos a validação do sistema em que restringe o percurso de um determinado tipo de veículo de vias com bloqueios, quando configurado com o perfil OSRM.

Como exemplo, caminhões, não podem transitar na Rua São Paulo em Blumenau. Assim, quando o tipo de veículo configurado ao perfil OSRM igual a Truck ou Toco, não será criado uma rota automática nesta via para o mesmo.

![Imagem 7: Como exemplo, caminhões, não podem transitar na Rua São Paulo em Blumenau. Assim, quando o tipo de veículo configurado…](https://ajuda.sankhya.com.br/hc/article_attachments/44012207059735)

---

## Layout de Importação de Pedidos

Foi incluído o novo campo tipo de cliente no layout importação de pedidos. Para adicioná-lo em um novo layout de importação de pedidos é necessário solicitar a análise do suporte.

---

## Prioridade de Entrega do Grupo de Setor

Adicionamos a melhoria para ser possível atribuir prioridade de entrega ao grupo do setor. Assim, é possível determinar áreas de riscos, para que o sistema entenda quais as atividades devem ser entregues por primeiro/último.
Para funcionar, é preciso vincular o grupo ao cadastro do setor, por fim, determinar a prioridade de entrega.

Prioridade de entrega (Cadastro Setor vinculado ao Grupo):

- Muito alta: serão entregues primeiro;
- Alta: serão entregues logo após a prioridade muito alta;
- Normal: ficarão como últimas atividades da rota;

  ![Imagem 8: Normal: ficarão como últimas atividades da rota;](https://ajuda.sankhya.com.br/hc/article_attachments/44012239892887)

---

## Usuário Manager

Foi adicionado a melhoria para permitir o usuário Manager (key user) atribuir a permissão de Manager a outros usuários.

![Imagem 9: Foi adicionado a melhoria para permitir o usuário Manager (key user) atribuir a permissão de Manager a outros usuários.](https://ajuda.sankhya.com.br/hc/article_attachments/44012207328535)
