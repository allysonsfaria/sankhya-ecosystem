---
id: "42951391319319"
titulo: "Projeção de Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951391319319-Proje%C3%A7%C3%A3o-de-Pedidos"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T14:02:23Z"
rotulos: ["zydon", "sync_hc", "sync_hash_a411a7868c18", "zydon_219085737730"]
---

# Projeção de Pedidos

A tela **Projeção de Pedidos** ajuda sua equipe comercial a saber, dia a dia, quais clientes estão dentro do prazo esperado de recompra, quais já passaram do prazo e quando cada cliente deve fazer o próximo pedido, com base no histórico de frequência de compra.

Pré-requisitos

- Ter permissão de **Administrador** ou de um perfil com acesso ao módulo **Análises** na organização.
- Ter clientes com pelo menos um pedido registrado, para que o sistema consiga calcular um padrão de frequência de compra.

Onde encontrar

No menu lateral do Admin, clique em **Análises** e depois em **Projeção de pedidos**.

Resumo inteligente

No topo da tela, o card **Resumo inteligente** traz uma leitura automática (gerada por IA) do período selecionado - quantos pedidos foram realizados, quantos ainda estão previstos e a projeção de fechamento do período. Clique em **Ver mais** para expandir a análise completa.

Entendendo a grade de clientes

A grade principal mostra uma linha por cliente e uma coluna por dia, dentro do período selecionado. Cada célula indica o status da previsão de pedido daquele cliente naquele dia:

- **Pedido não realizado** - o cliente não fez o pedido dentro do prazo esperado de recompra.
- **Pedido previsto para hoje** - o cliente ainda não fez o pedido, mas ainda está dentro do prazo (previsto para o dia atual).
- **Pedido previsto** - data futura estimada para o próximo pedido, calculada conforme o padrão de frequência de compra do cliente. Passe o mouse sobre a célula para ver o detalhamento ("Próximo pedido estimado conforme padrão de frequência" + a data prevista).

![screenshot-1786363312831-26](https://ajuda.sankhya.com.br/hc/article_attachments/42951391706263)

No topo de cada coluna de dia, um contador mostra quantos pedidos estão previstos para aquela data. No cabeçalho da coluna "Clientes", o número total de clientes exibidos na grade é mostrado ao lado de um ícone de ordenação.

Navegando pelo período

- Use o seletor **Semana** para trocar a granularidade da visualização.
- Use as setas **‹ ›**, ao lado do intervalo de datas (ex.: "09 - 15 de ago de 2026"), para navegar entre períodos anteriores e seguintes.
- Clique em **Atualizar** para forçar um novo processamento dos dados. O horário da última atualização é exibido ao lado do botão.

Filtrando os dados

Clique em **Filtrar**, no canto superior direito da grade, para abrir o painel de filtros. Nele você pode refinar a visualização por:

- **Calendário** - selecione uma data específica no mês para navegar diretamente até ela.
- **Clientes** - busque e selecione um ou mais clientes específicos.
- **Segmentos** - filtre por segmento de cliente.
- **Status de eventos** - filtre por status da previsão (ex.: não realizado, previsto para hoje, previsto).
- **Classificações** - filtre por classificação do cliente.

> 💡 **Dica:** combine os filtros de **Status de eventos** com **Clientes não realizados** para montar rapidamente uma lista de contatos prioritários para a equipe de vendas acionar no dia.

Configurações

Clique em **Configurações**, no canto superior direito da tela, para acessar os parâmetros que definem como o sistema calcula o padrão de frequência de compra e as regras de "atraso" usadas para marcar um pedido como não realizado.

Perguntas frequentes

**Como o sistema calcula a data prevista do próximo pedido?** O cálculo é feito com base no histórico de pedidos do cliente, identificando um padrão médio de frequência de compra (por exemplo, a cada X dias) e projetando a próxima data esperada a partir do último pedido realizado.

**O que significa um cliente ficar marcado como "Pedido não realizado" por vários dias seguidos?** Significa que o cliente já passou da data prevista de recompra e ainda não fez um novo pedido. Vale a pena priorizar esse contato na régua de relacionamento comercial.

**Os clientes prospect (sem histórico de compra) aparecem na grade?** Sim, mas como ainda não há pedidos suficientes para calcular um padrão de frequência, a previsão pode ficar menos precisa até que o cliente registre seu primeiro pedido.

**Posso ver detalhes de um pedido específico direto na grade?** Sim. Ao clicar em uma célula da grade, é possível abrir os detalhes do relatório daquele dia, com a lista de pedidos, valores, status e clientes envolvidos.
