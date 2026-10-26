---
id: "44012216084119"
titulo: "[Routing] - Release Notes 2.7.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012216084119--Routing-Release-Notes-2-7-0"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:22:06Z"
rotulos: ["sync_hc", "lincros", "lincros_13434207", "sync_hash_f9aa041e8b79"]
---

# [Routing] - Release Notes 2.7.0

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012216221591)

## Correções

## Integração de Pré-nota entre o TMS Lincros e o Routing utilizando data de agendamento - Chamado 240764.

Com a correção é possível criar uma sessão utilizando pré-notas com data de agendamento.

Para as integrações de documentos utilizando marcadores está sendo validado se há cadastrado o marcador enviado.

---

## Funcionalidade de Recarga.

Com a correção as rotas estão sendo criadas respeitando os parâmetros estabelecidas para gerar uma recarga.

---

## Funcionalidade para criar embarque no TMS Lincros utilizando endereço de entrega diferente ao cadastrado no cliente.

Com a correção o embarque criado está considerando o CEP do pedido e não mais do cliente.

---

## Integração de pedidos entre o TMS Lincros e o Routing.

Realizada melhoria no retorno de um possível erro de integração quando não há o cliente cadastrado. Com a correção deve ser apresentada na tela **Log de Erros de importação** a mensagem **“Não há cliente com o CNPJ XXXXXXXX, para o documento de número XXXXX”**.

---

## Importação de coordenadas.

Com a correção é possível realizar uma importação de uma coordenada para atualizar um cadastro de cliente.

---

## Emissão do relatório do romaneio - Chamado 250869.

Com a correção o relatório de romaneio está sendo gerado obedecendo os dados da sessão.

---

## Funcionalidade de exibir filtros na tela da sessão.

Com a correção é possível filtrar os marcadores dos pedidos quando enviados.

---

## Adicionar pedidos manual dentro de uma sessão -Chamado 121574.

Com a correção é possível realizar a adição de um pedido manual dentro de uma sessão.

---

## Parâmetro de depósito, funcionalidade para gerar recarga -Chamado 122699.

Com a correção as rotas criadas estão obedecendo os parâmetros de **tempo mínimo recarga.**

---

## Funcionalidade de sequenciamento de rota utilizando a tecla ALT -Chamado 124514.

Foi realizado melhorias de performance ao realizar um sequenciamento com a tecla ALT.

---

## Relatório de integrações automáticas.

Após a correção está sendo registrado os arquivos JSON de integração de clientes na tela Relatórios>Integrações automáticas.

---

## Relatório de integrações automáticas.

Após a correção está sendo registrado os arquivos JSON de integração de clientes.

---

## Importação de pedidos entre o Routing e o TMS Lincros.

Após a correção está sendo possível importar os pedidos do TMS Lincros utilizando o filtro de data de agendamento, quando há pedidos com data de agendamento cadastrado.

---

## Pedidos dentro de uma sessão -Chamado 125797.

Após a correção ao realizar uma exclusão de uma rota a quantidade de pedidos não está sendo alterada.

---

## Integração de rotas com o TMS Lincros -Chamado 125258.

Após a correção está considerando para criar o embarque o parâmetro **volta ao Depósito após o término das Entregas**, enviado o KM total da rota.

---

## Integração de pedidos entre o Routing e o TMS Lincros -Chamado 128393.

Após a correção todos os pedidos estão sendo importados do TMS Lincros, obedecendo os parâmetros estabelecidos.

---

## Integração de clientes entre o TMS Lincros e o Routing -Chamado 128424.

Após a correção as coordenadas dos clientes estão sendo geradas.

---

## Cadeado otimização automática -Chamado 133289.

Realizadas as correções no **cadeado de otimização** quando selecionado.

---

## Tecla de atalho CTRL + F -Chamado 133290.

Realizadas as correções nas consultas de pedidos e clientes quando selecionado a tecla de atalho CTRL+F.

---

## Rotas com parâmetros de volta para o depósito -Chamado 129590.

Realizadas as correções nas linhas de rotas criadas com veículos parametrizados com volta para o depósito.

---

## Melhorias

## Alterada a orientação da funcionalidade de ajudar “?”.

Alterado a mensagem da tecla de atalho CTRL + Z para “**Desfaz operações realizadas em apenas uma rota”.**

---

## Importação de pedidos entre Routing e o TMS Lincros -Chamado 111878.

Com a melhoria se torna obrigatório informar pelo menos uma unidade de negócio antes de confirmar uma importação de pedido do TMS Lincros**.**

---

## Cadastro de veículo.

No cadastro do veículo os cadastros de motorista agora estão sendo disponibilizados em ordem alfabética**.**

---

## Novas funcionalidade de integração utilizando WebAPI.

Com os novos WebServices é possível realizar as seguintes funções:

1. ## Exclusão de pedidos.
2. ## Cadastro de veículo
3. ## Cadastro de tipo de veículo
4. ## Cadastro de motorista

## OBS: Para os clientes que tem interesse em realizar as integrações acima, pedimos que entrem em contato com o nosso setor de Help Desk solicitando às documentações.

---

## Adequação a nova Lei Geral de proteção de dados (LGPD).

A partir desta nova versão, será exibido após efetuar o 1º login o termo de uso de Software, voltando a aparecer apenas quando ocorrer alguma alteração do termo.

---

## Layout de exportação para o ERP.

Foi inserido o campo **Custo total da rota** no layout de exportação para o ERP. Para o uso desta funcionalidade no layout é necessário solicitar para equipe de

---

## Informações da sessão.

Agora é possível visualizar o **Custo por quilo** no campo **informações da sessão,** e em uma rota selecionada. O Custo por quilo, é o valor calculado pelas configurações inseridas no Tipo do Veículo dentro do Cadastro de Transportadora. O cálculo utilizado para exibir o valor nesse campo é, Custo / Peso

---

## Tela de sequenciamento de rota.

Foi inserido um novo campo com as informações de observações do cliente na tela de sequenciamento de rota, quando informada no cadastro do cliente.

---

## Relatório do Romaneio.

Ao gerar o **relatório de Romaneio** com pedidos sem a informação do campo **Observação**, será apresentado a **Observação** informada no cadastro do cliente, será disponibilizado o **tipo de cliente** e a quantidade de itens.

---

## Renderização do mapa.

Realizadas melhorias na renderização do mapa dentro de uma sessão.

---

## Exportação de sessão para ERP -Chamado 132117.

Realizadas melhorias no tempo de exportação de uma sessão para o ERP.

---

## Filtro de pedidos.

Realizadas melhorias de performance para consultas na tela de **pedido**.

---

## Adicionar pedidos dentro de uma sessão.

Foi adicionado na tela **Adicionar atividades na sessão**, o filtro de **Pesquisa avançada,** possibilitando consultar os pedidos por tipo de cliente, tipo de produto e por um determinado peso ou cubagem.

---

## Nova funcionalidade para entregas entre clientes em um determinado raio.

Criada nova parametrização para roteirizar (**entregas a pé),** para clientes dentro de um determinado raio de atendimento cadastrado.

OBS: Para maiores informações entre em contato com a equipe de Help-Desk.

---

## Otimização de rota -Chamado 129378.

A otimização de rota irá verificar qual é o melhor KM e custo para a rota, na primeira otimização. Caso tente otimizar a rota novamente será apresentado em tela a seguinte mensagem “**Rotas já Otimizadas**“.

---

![Imagem 2: A otimização de rota irá verificar qual é o melhor KM e custo para a rota, na primeira otimização. Caso tente otimizar…](https://ajuda.sankhya.com.br/hc/article_attachments/44012179940503)
