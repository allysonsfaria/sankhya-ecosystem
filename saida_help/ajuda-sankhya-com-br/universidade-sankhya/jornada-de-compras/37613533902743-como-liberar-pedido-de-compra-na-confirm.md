---
id: "37613533902743"
titulo: "Como liberar pedido de compra na confirmação da nota (Evento 18)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-08-21T11:04:53Z"
rotulos: ["Configuração", "Eventos", "Liberação de Limites", "Pedido de Compra", "TOP"]
---

# Como liberar pedido de compra na confirmação da nota (Evento 18)

| Categoria |
| --- |
| [Qual é a finalidade do Evento 18 - Liberação de Pedido/Confirmação de Nota no sistema?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18#h_01KESD1MM11DBKYYAA19BB9QGP) |
| [Quais problemas este recurso do sistema resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18#h_01KESD2GWQ0S11RD26G6WAANH4) |
| [Quais os riscos de não utilizar a liberação do evento 18?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18#h_01KESD386NP7QS0ZB2B04ET2NV) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18#h_01KESCY3YYSB4CKMY8F9REMW1G) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya.](https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18#h_01KESD4CDGVBC1X3HQK6ZJ5TP5) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37613533902743-Como-liberar-pedido-de-compra-na-confirma%C3%A7%C3%A3o-da-nota-Evento-18#h_01KESD6FJQAP00G9NE2G9XTWV5) |

## Liberação de pedido pela confirmação da nota (Evento 18)

#### Qual é a finalidade do Evento 18 - Liberação de Pedido/Confirmação de Nota no sistema?

O Evento 18 tem como finalidade reforçar o controle interno, exigindo uma validação formal antes da confirmação de Pedidos de Compra ou Notas, garantindo o alinhamento às políticas internas da empresa e promovendo maior segurança e transparência nos processos críticos. Este evento é utilizado exclusivamente para solicitar a liberação de confirmação, sem considerar valores ou limites financeiros, e não suporta a funcionalidade de "Liberação em Cascata", limitando-se ao primeiro usuário configurado para aprovação. Além disso, Notas de Complemento estão excluídas deste processo, não gerando qualquer solicitação de liberação.

#### Quais problemas este recurso do sistema resolve?

- Risco de fraudes e transações não autorizadas, por falta de controle nos processos de aprovação.
- Ausência de rastreabilidade nas decisões, dificultando auditorias e o acompanhamento das ações realizadas.
- Pedidos fora do orçamento, comprometendo o planejamento financeiro e causando gastos indevidos.
- Falta de dados confiáveis para decisões estratégicas, gerando compras desalinhadas com as reais necessidades da empresa.

#### Quais os riscos de não utilizar a liberação do evento 18?

Sem validação estruturada, as transações ficam sujeitas a compras desalinhadas às necessidades reais, resultando em estoques excessivos ou rupturas que impactam diretamente o fluxo operacional. A falta de controle sobre as alçadas de aprovação aumenta o risco de gastos desnecessários, fraudes e desvios financeiros, dificultando a identificação de irregularidades e comprometendo a transparência e governança interna.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052376852)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A colaboradora responsável pelas compras na empresa **Axis** iniciou a confirmação de um pedido de **200** unidades do **Produto 4**, essencial para as operações da empresa.

Durante o processo, o sistema solicita liberação vinculada ao Evento 18, exigindo validação do gestor para garantir conformidade com as políticas internas.

Somente após essa aprovação o pedido poderá ser confirmado e enviado ao fornecedor, assegurando o abastecimento adequado.

**Tarefa:** Dê continuidade ao fluxo de liberação para que o pedido de compra possa ser validado pelo gestor responsável. Após a aprovação, confirme o pedido no sistema para que ele seja formalizado e encaminhado ao fornecedor.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya.

1. **Configurações na TOP**

- Confira se a TOP Pedido de Compra está ativa e configurada corretamente para execução do **Evento 18**:
  Na Aba **Geral**, o campo **“Exigir Liberação antes da Confirmação”** deve estar marcado.
- Verifique-se foi determinado o responsável liberador na rotina **Usuários**.
  **Atenção!** Este evento acata somente a primeira opção informada na aba Liberações em Cascata dentro da tela Tipos de Operação - TOP

2. **Processo de Liberação de Limite**

**Pela Central de Compras**:

- Após acionar o botão **Confirmar**, para finalizar o pedido de compra, o pop-up **Liberações solicitadas** será apresentado.
- Selecione o usuário liberador no campo indicado.
- Clique em “**Salvar**”.
- Acesse o botão “**Liberações”**, que abrirá a tela **Liberações da Nota/Pedido**.
- Insira o **Usuário** e a **Senha**.
- Clique em “**Aplicar”**.
- Localize o pedido exibido, selecione e clique no botão “**Liberar”** ou dê um duplo clique para aprovação.

**Pela Tela de Liberação de Limites**:

- Acesse a tela **Liberação de Limites**.
  **Menu:** Configurações » Avançado » Liberação de Limites
- Insira os dados do liberador (usuário e senha) e clique em “**Aplicar**”.
- Todas as solicitações pendentes para o liberador serão exibidas.
- Localize o **Pedido de Compra**, selecione e clique em “**Liberar**”.

3. **Finalizar o Pedido de Compra**

- Após a liberação, volte à **Central de Compras** clicando no botão “**Voltar**” no canto superior direito.
- Revise todas as informações, como quantidades, valores e condições comerciais.
- Clique em “**Confirmar**” para concluir o pedido.

**Dica Final**: O sistema gerará o **Nro. da Nota**, que será o número do Pedido de Compra para controle e rastreamento.

#### Correção e Repetição

- Confira se a TOP Pedido de Compra está ativa e configurada corretamente.
- Verifique-se foi determinado o responsável pela liberação (**liberador**) na aba **Liberação em Cascata**.
- Na Aba Geral, deve estar marcado a opção Exigir Liberação antes da Confirmação.
- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Revise as configurações da TOP (Tipo de Operação).
- Lembre-se de que a TOP (Tipo de Operação) possui caráter histórico, o que significa que qualquer alteração realizada exigirá o cancelamento do pedido de compra atual e a criação de um novo para refletir as mudanças.
- Para praticar, experimente criar novamente com um cenário diferente, com outros produtos, com outros valores de pedido e fornecedor.
