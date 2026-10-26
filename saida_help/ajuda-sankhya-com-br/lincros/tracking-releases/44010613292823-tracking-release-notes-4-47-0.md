---
id: "44010613292823"
titulo: "[Tracking] - Release Notes 4.47.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010613292823--Tracking-Release-Notes-4-47-0"
trilha: "Lincros > Releases (Atualizações) > Tracking (Releases)"
atualizado_em: "2026-10-05T18:41:56Z"
rotulos: ["sync_hc", "lincros", "lincros_13434535", "sync_hash_e0ad542487e5"]
---

# [Tracking] - Release Notes 4.47.0

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44010596788375)

## Melhorias:

## Relatório Detalhes da Rota com novos campos

Nova atualização para os relatórios Detalhes da Rota. Esta atualização traz a inclusão de novas colunas nos relatórios sintéticos e analíticos, oferecendo uma visão mais abrangente dos dados.

## Novidades:

Nos relatórios Detalhes da Rota (sintético), adicionamos as colunas:

- Documento (CNPJ/CPF) Transportadora
- Rota origem
- Rota destino
- Data execução baldeio destino
- CPF Motorista

No relatório Detalhes da Rota (analítico - entrega), incluímos as seguintes colunas:

- Documento (CNPJ/CPF Cliente)
- Número NF (Número da nota fiscal)
- Motivo Apontamento pelo Motorista
- Motivo Apontamento pela Central
- Comprovante
- Data/Hora Devolução
- Motivo Devolução
- Descrição Motivo
- Agente do Tratamento
- Data/Hora inicial do Tratamento
- Data/Hora final do Tratamento
- Origem apontamento (Apontamento via App ou manual)
- Possui Foto
- Possui Assinatura

Todas as novas colunas são exibidas no relatório Detalhes da Rota ao exportá-lo pela opção Exportar consolidado (sintético e analítico).

As novas colunas são exibidas em tela e nos arquivos importados (CSV e Excel) conforme os layouts especificados.

## Envio da Data Prevista da entrega ao TMS na criação da rota de CrossDocking no TRK

Agora, ao criar rotas no CrossDocking, o Tracking atualiza automaticamente o TMS com as datas previstas de entrega. Garantindo informações atualizadas para um planejamento mais eficiente.

## Campo Série da Nota Fiscal ajustado

O tamanho do campo Série da Nota Fiscal foi ajustado para aceitar até 10 caracteres, padronizando-o com o TMS.

## Envio de mensagens via WhatsApp no Chat

Agora é possível utilizar o WhatsApp diretamente pelo Chat para se comunicar com os motoristas. Com essa melhoria, além de mensagens de texto, os motoristas também podem enviar áudios e imagens para a central de monitoramento, tornando a comunicação mais prática, rápida.

## Nova tecnologia para integração de posições e temperatura

Adicionamos a tecnologia Total Trac em nosso lista de integrações de posições e temperatura.

## Múltiplas Janela de atendimento

Agora é possível cadastrar múltiplas janelas de atendimento para os clientes, permitindo uma maior flexibilidade na gestão das agendas de atendimento.

## Vinculo automático de transportadoras à usuários do perfil Manager

Agora, quando o módulo Tracking recebe uma nova transportadora através da integração de rotas, essa transportadora é automaticamente associada aos usuários com perfil "Manager".

## Serviço de Sincronização entre TMS e Tracking

Foi criado um novo serviço que sincroniza dados de clientes e ativos entre TMS e Tracking. Com essa integração, garantimos que os dados entre os produtos estejam sempre atualizados de forma automatizada.

## Validação de Canhoto com IA

Agora é possível ativar no App Lincros a validação automática de canhotos usando Inteligência Artificial. Com isso, o sistema verifica se a imagem enviada pelo motorista é, de fato, um canhoto válido, trazendo mais agilidade e segurança ao processo.

## Novidades na opção 'Reproduzir Rota'

 Agora, o botão "Reproduzir Rota" na tela de monitoramento do mapa sinótico estará habilitado mesmo para viagens ainda não iniciadas.

![Imagem 2: Agora, o botão "Reproduzir Rota" na tela de monitoramento do mapa sinótico estará habilitado mesmo para viagens ainda…](https://ajuda.sankhya.com.br/hc/article_attachments/44010618616599)
