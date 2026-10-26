---
id: "44012254630935"
titulo: "[Routing] - Release Notes 2.21"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012254630935--Routing-Release-Notes-2-21"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:23:56Z"
rotulos: ["sync_hc", "lincros", "sync_hash_290fae9e9f1a", "lincros_13433985"]
---

# [Routing] - Release Notes 2.21

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012244036119)

## Melhorias

## Criar parâmetro novo para combinar utilização da API do Google com o Nominatim

Hoje no routing é realizado uma consulta nas ferramentas do Google para realizar georeferenciamento, para melhor asseRoutingividade foi implementado novo parâmetro"Priorizar Google-API" em Cadastros>>Depósitos>>Parâmetros de Geolocalização(ADMIN).
Quando ativo este realizará dupla busca no georreferenciamento do endereço, quando qualidade do dado de retorno da API do Google for inferior a 80%, buscará também na API do Nominatim para assegurar a qualidade do tratamento de dados de endereço.

---

## Parâmetro nas estratégias de roteirização para desabilitar o grupo de setores

Criado parâmetro “Desabilitar regras para grupos de setores“ em: Cadastros >> Estratégias de roteirização >> (Parâmetros Gerais), quando estiver marcado desabilita o(s) grupo(s) de setor(es) existente(s) que restringem ou não os veículos dentro do setor, assim, aumenta a flexibilização de roteirização conforme demanda do cliente.
Resultado esperado: A roteirização será impactada como se não existissem grupos de setor cadastrados.
Cenário de utilização: para dias em que demandas onde temos durante alguns períodos, aumento ou baixa nos pedidos que devem ser roteirizados, precisamos que as regras da roteirização sejam flexíveis e adaptativas.
Quando o parâmetro não for marcado, a regra de setorização não será afetada.

---

**Melhoria na retroalimentação de pedidos do Tracking (Reentrega)**
Realizado um ajuste na integração de Tracking x Routing, para pedidos como reentrega, agora clonará todas as informações do pedido informado, alterando apenas a data inserção para data atual, a Data cadastro, que deverá assumir a data informada no campo "DataReentrega" e terá o campo reentrega marcado.
Ao informar um pedido não existente (número, data ou série incorreto), retornará a mensagem de pedido não encontrado e ao informar uma data igual na reentrega, retornará a mensagem de que já existe um pedido na data informada.

---

## Estouro de janela - Horário de atendimento na otimização

No Routing possuímos a opção de otimização de rotas que facilita a pessoa que realiza as funções de roteirização diariamente, foi implementado uma melhoria no algoritmo para respeitar o horário de atendimento na roteirização de rotas montadas manualmente.
Ao executar o processo de “Otimização” é disponibilizado o melhor sequenciamento possível e que as janelas de atendimento sejam respeitadas, caso não seja possível evitar que as janelas de atendimento sejam estouradas, o sequenciamento sugere a rota que tenha o menor número de estouro possível.
Em Cadastros >> Estratégias de Roteirização >> Parâmetros Fitness, aumentar o parâmetro "Peso do horário de atendimento excedido", recomenda-se que seja menor que o parâmetro "Peso da atividade NR".

---

## Criação de Rotas com múltiplos clientes no GE

Hoje o Routing envia a rota para o Tracking como se fosse uma única entrega, e atribuída a uma única parada, mas com os pedidos agrupados.
Realizado uma melhoria para quando for utilizado o parâmetro: Cadastros >> Depósitos >> Parâmetros do Depósito Smub >> "Raio em metros", juntar os pedidos da mesma posição geográfica e ao expoRoutingar a sessão para o Tracking, o Routing deve enviar a mesma sequencia de entrega para cada cliente.
Alterado retorno na API do Routing para que no envio das entregas ao Tracking, pedidos agrupados serão enviados com todos os clientes na mesma sequência de entrega.
Resultado esperado:
1-No caso de múltiplos clientes: Será gerada uma entrega para cada cliente mesmo que a sequência seja a mesma, ou seja, haverá a sequência 1 repetida duas vezes no tracking, sendo uma para cada cliente.
2-No caso de um cliente por atividade: Deve ser enviado como é hoje, uma entrega por atividade.

---

## Identificação de atividades com endereço de entrega ou pedido / Botão para editar o endereço do pedido

Melhoria realizada para exibir, se o cliente utiliza o endereço do pedido ou da entrega e possibilitar editar o endereço ao clicar no ícone que caracteriza o tipo de endereço dele.

---

![Imagem 2: Melhoria realizada para exibir, se o cliente utiliza o endereço do pedido ou da entrega e possibilitar editar o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012275018775)
