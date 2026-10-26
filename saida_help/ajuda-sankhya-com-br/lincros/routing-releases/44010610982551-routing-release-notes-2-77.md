---
id: "44010610982551"
titulo: "[Routing] - Release Notes 2.77"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010610982551--Routing-Release-Notes-2-77"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T18:41:40Z"
rotulos: ["sync_hc", "lincros", "lincros_14971002", "sync_hash_06552da3e688"]
---

# [Routing] - Release Notes 2.77

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44010584132503)

## Melhorias:

## Tema visual Sankhya disponível no Roteirizador com ativação por usuário

O Roteirizador agora conta com o tema visual Sankhya, habilitado por padrão para todos os usuários, incluindo os já existentes. Quem preferir manter a aparência anterior pode desativar a opção "Layout Sankhya" em Meus Dados, acessível pelo menu superior. A preferência é individual, salva automaticamente e aplicada a cada login, sem necessidade de suporte ou intervenção de administradores.

![Imagem 2: O Roteirizador agora conta com o tema visual Sankhya, habilitado por padrão para todos os usuários, incluindo os já…](https://ajuda.sankhya.com.br/hc/article_attachments/44010584347927)

## Tela de sessão do Routing disponível em modo embed no ERP SankhyaOM (Beta)

A partir desta versão, usuários do ERP SankhyaOM podem visualizar e acompanhar sessões de roteirização diretamente no ERP, sem precisar alternar para o Routing em separado. Nesta versão beta, o componente embedado disponibiliza o mapa com as rotas da sessão, o painel de detalhes da rota selecionada e os botões de ação da sessão, incluindo Exportar, Polígono e demais ações existentes. O menu de contexto (botão direito sobre a rota) também está disponível com todas as opções de edição já conhecidas da versão standalone.

## API ConsultaSessao v6 passa a expor dados de pedágio SemParar por rota

O endpoint `GET /consultasessao/v6/{idSessao}` passa a incluir, em cada rota, os dados de pedágio da integração SemParar quando disponíveis: código da viagem no integrador, IDVPOs ANTT, valor total de pedágios, protocolo do vale pedágio, data de compra, vigência, status da transação, centro de custo, nome do usuário responsável pela compra, praças percorridas com localização e praças do retorno à base. Rotas sem integração SemParar ou sem compra realizada retornam o bloco com campos nulos, seguindo o padrão já existente da API.

## Nova funcionalidade identifica automaticamente os estados percorridos em uma rota a partir do CEP de origem e destino

Agora é possível saber automaticamente quais estados brasileiros uma rota de entrega vai cruzar. Basta informar o CEP de origem e o CEP de destino: o sistema calcula o trajeto rodoviário e retorna a sequência de UFs em ordem de passagem, a distância estimada em km e a indicação se a rota é interestadual ou não, facilitando cálculos de frete, apuração de ICMS e planejamento logístico.

## Tipo de Conhecimento de pedidos de reentrega agora é preenchido automaticamente na exportação para o TMS

Pedidos identificados como reentrega agora têm o Tipo de Conhecimento preenchido automaticamente como "Reentrega" no momento do recebimento, seja via integração com o Tracking ou por importação. Ao exportar o embarque para o TMS, o sistema já envia o valor correto, eliminando a necessidade de alteração manual.

## Exportação ao TMS agora valida CEP do cliente e exibe mensagem de erro detalhada quando ausente

Para depósitos com integração TMS habilitada, o CEP do cliente de destino passou a ser obrigatório na exportação. Quando o CEP estiver ausente, o sistema bloqueia o envio e exibe uma mensagem identificando o pedido e o cliente afetado, com um hyperlink direto para o cadastro do cliente para facilitar a correção. Clientes que já possuem CEP cadastrado não são impactados por essa alteração.

![Imagem 3: Para depósitos com integração TMS habilitada, o CEP do cliente de destino passou a ser obrigatório na exportação.…](https://ajuda.sankhya.com.br/hc/article_attachments/44010584507543)
