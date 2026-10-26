---
id: "44012283219351"
titulo: "[Routing] - Release Notes 2.23"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012283219351--Routing-Release-Notes-2-23"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:24:39Z"
rotulos: ["sync_hc", "lincros", "lincros_13433966", "sync_hash_a3dc154b92ec"]
---

# [Routing] - Release Notes 2.23

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012248187927)

## Melhorias:

- ## Remover bloqueio por capacidade de veículos na criação de rota de transferência:

  - Atualmente no Routing, existe bloqueio para criação da rota de **transferência(first mile)** (manual e automática), caso o veículo selecionado não suporte o peso e cubagem para transporte dos pedidos.

![Imagem 2: Atualmente no Routing, existe bloqueio para criação da rota de transferência( first mile ) (manual e automática), caso…](https://ajuda.sankhya.com.br/hc/article_attachments/44012283689751)

- Foi implementada uma melhoria que, no momento de criar uma rota de transferência manual, caso o veículo selecionado não suporte o peso e cubagem para transporte dos pedidos, o sistema seguirá a mesma regra da rota de **distribuição (last mile) manual**, permitindo que o usuário selecione o veículo e crie a rota, apresentando apenas um alerta quando a cubagem ou peso do veículo é menor que o total dos pedidos.

  ![Imagem 3: Foi implementada uma melhoria que, no momento de criar uma rota de transferência manual, caso o veículo selecionado não…](https://ajuda.sankhya.com.br/hc/article_attachments/44012248586903)

- ## Atualizar dados dos clientes para todas as integrações (TMS, TXT, API)

  - Hoje no Routing, ao receber uma nova integração de pedidos, a ferramenta não atualiza os dados do endereço dos clientes.
  - Portanto, foi criada uma verificação nas importações de pedidos via WebService, via arquivo TXT e importação via TMS das notas.

    - Essa verificação checa o cadastro atual no Routing do cliente em questão, e caso o dado presente no Routing for diferente do recebido, o endereço é alterado conforme o registro recebido.
  - Portanto, quando realizada uma ação de importação de pedidos, o endereço dos clientes será equivalente a ultima versão dos dados integrados.

![Imagem 4: Portanto, quando realizada uma ação de importação de pedidos, o endereço dos clientes será equivalente a ultima versão…](https://ajuda.sankhya.com.br/hc/article_attachments/44012309157527)
