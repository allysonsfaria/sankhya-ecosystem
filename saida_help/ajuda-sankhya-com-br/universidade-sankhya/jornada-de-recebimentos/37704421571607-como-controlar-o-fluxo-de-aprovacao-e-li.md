---
id: "37704421571607"
titulo: "Como controlar o fluxo de aprovação e liberar limite de crédito no pedido de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37704421571607-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-no-pedido-de-venda"
trilha: "Universidade Sankhya > Jornada de Recebimentos"
atualizado_em: "2026-08-01T02:53:32Z"
rotulos: ["Configuração", "Parceiro", "Portal de Vendas", "Liberação de Limites", "Crédito", "Financeiro", "Artigo atualizado KCS", "CVE - KCS"]
---

# Como controlar o fluxo de aprovação e liberar limite de crédito no pedido de venda

### Como funciona e qual a importância dessa prática?

O controle de liberação de crédito no Sankhya gerencia os limites financeiros concedidos aos clientes com precisão. Ele opera com dois tipos de limites: o global, que define o valor máximo acumulado em compromissos financeiros, e o mensal, que restringe o uso em um único mês. Quando um pedido excede esses limites, o sistema bloqueia a transação e a encaminha para aprovação, garantindo alinhamento às políticas financeiras da empresa.

Esse controle reduz riscos como inadimplência, fortalece a governança ao centralizar decisões e registra transações com transparência. Além disso, oferece flexibilidade para ajustar limites conforme o perfil dos clientes, promovendo uma gestão financeira mais segura e eficiente.

### Pedido liberado direto sem fluxo de aprovação

Quando um vendedor cria um pedido no sistema, é esperado que este pedido passe por um **fluxo de liberação** antes de ser confirmado. No entanto, em algumas situações, os pedidos são liberados automaticamente no momento da confirmação, sem passar pela tela de **"Liberação de Limites"**, gerando problemas no processo interno de aprovação.

Este comportamento pode ocorrer devido à configuração da **"Tipo de Operação"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) utilizada no pedido, ou pela ausência de configurações específicas que forcem a solicitação de liberação.

### Configuração da TOP para exigir liberação

Para que o sistema solicite liberação antes da confirmação do pedido, configure a **"Tipo de Operação"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) utilizada no processo de vendas.

Acesse a **"Tipo de Operação"** utilizada nos pedidos de venda.
 Localize e marque a opção **"Exigir liberação antes da confirmação"**.
 Salve as alterações realizadas na TOP.

Ao marcar esta opção, o sistema passará a solicitar liberação independentemente do tipo de negociação utilizado. Todos os pedidos criados com esta TOP precisarão ser liberados antes de serem confirmados.

### Liberação por tipo de negociação específico

Caso seja necessário que a solicitação de liberação ocorra apenas para um tipo de negociação específico, como por exemplo apenas para pedidos com pagamento em boleto, a configuração padrão da TOP não será suficiente.

Neste cenário, será necessário o desenvolvimento de um evento personalizado que valide o tipo de negociação e force a liberação apenas quando a condição específica for atendida. Para implementar esta customização, abra uma **"Ordem de Serviço"** para que a equipe técnica desenvolva a solução adequada.

### Duração da liberação de limite

Quando um pedido é liberado, existe um período de validade para esta liberação. Caso o faturamento ocorra após este período, o sistema solicitará uma nova liberação. Este comportamento é controlado pelo parâmetro **"Duração da liberação de Atraso/Limite crédito"** (DIASTOLCREATR).

### Eventos de liberação

**Evento 18 – Confirmação:** quando a liberação ocorre por este evento, o gatilho acontece no momento da confirmação. Após confirmado, o pedido não solicita nova liberação.
**Evento 41 – Análise de Itens:** quando o pedido está liberado por este evento, não é possível alterar ou excluir o pedido. Este comportamento é padrão do sistema.

### Quais problemas essa prática resolve?

**Descontrole financeiro:** evita que clientes acumulem dívidas insustentáveis, protegendo o fluxo de caixa.
**Governança frágil:** padroniza e documenta aprovações, evitando decisões inconsistentes.
**Erros manuais:** automatiza processos, minimizando falhas e otimizando o trabalho da equipe.

### Quais os riscos de não a utilizar?

Sem um controle estruturado de crédito, a empresa corre riscos que comprometem a saúde financeira. A inadimplência aumenta, impactando negativamente o fluxo de caixa e dificultando o planejamento. A ausência de rastreabilidade nas decisões compromete a governança e as auditorias, tornando o processo menos confiável e transparente.

### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa está enfrentando desafios para controlar a concessão de crédito a seus clientes. Para resolver esse problema, implemente o controle de liberação de crédito com limites por alçada no ERP Sankhya.

### Como aplicar o conhecimento adquirido

Acesse a tela **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas) e selecione o **"Tipo de Movimento"** como Pedido de Venda.
 Ao exibir o pop-up **"Liberações Solicitadas"**, informe o **"Usuário liberador"** e clique no botão **"Definir liberador"**.
 Na **"Central de Vendas"**, clique no botão **"Liberações"**.
 Insira o **"Usuário"** e a **"Senha"** do liberador, selecione o pedido e clique em **"Liberar"**.
 Retorne à **"Central de Vendas"** e clique em **"Confirmar"** para concluir o pedido.

### Correção e repetição

Experimente simular cenários alternativos, utilizando outros clientes e valores para observar diferentes reações do sistema.
