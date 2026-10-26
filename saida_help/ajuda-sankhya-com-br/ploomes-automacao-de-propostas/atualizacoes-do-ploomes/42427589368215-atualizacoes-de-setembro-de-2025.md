---
id: "42427589368215"
titulo: "Atualizações de Setembro de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427589368215-Atualiza%C3%A7%C3%B5es-de-Setembro-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:25Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_7141e0702491", "ploomes_12166451"]
---

# Atualizações de Setembro de 2025

## [01/09/2025] [Correção]

- Correção no Skeleton dos Checklists: Ajustada a lógica de renderização para evitar loops infinitos, garantindo o carregamento correto dos dados sem necessidade de atualizar a página.

## [02/09/2025] [Correção]

- Fizemos uma melhoria na query que faz a contagem de oportunidades, por funis, que o usuário tem acesso. É esperado que o tempo de resposta para requisições desse tipo caiam pela metade.

## [03/09/2025] [Correção]

- Na integração com o Neppo, identificamos que, quando a integração buscava o usuário na Ploomes pelo AgentId enviado pela Neppo e não encontrava o registro, ocorria um erro e o registro de interação não era criado. Para corrigir isso, implementamos uma validação que utiliza o campo session DisplayName. Assim, caso o usuário não seja localizado na Ploomes, o sistema passa a registrar o nome do agente a partir desse campo, evitando falhas na criação do registro de interação.
- Corrigido o comportamento do CPQ Beta em que as opções dos produtos eram mantidas quando o produto era alterado. Agora, assim como era no CPQ Legado, as opções são todas apagadas quando o produto é alterado.

## [04/09/2025] [Correção]

- [Aplicativo] Foi corrigido um problema no aplicativo em que, ao selecionar um produto opcional, os campos opcionais que dependiam de fórmulas de exibição não eram exibidos, pois o aplicativo não estava recuperando corretamente os valores do produto necessários para o cálculo dessas fórmulas.

## [05/09/2025] [Correção]

- Corrigida falha que impossibilitava a edição do nome da Moeda nas configurações do sistema.

## [09/09/2025] [Correção]

- Corrige o problema que ocorria quando um documento qualquer sem vínculo com nenhum cliente era compartilhado para assinatura com a integração ClickSign, que agora é possível normalmente.

## [10/09/2025] [Correção]

- Campos de data no CPQ Beta não estavam sendo atualizados após ficarem com datas válidas, o que fazia com que zerassem após inserir um 0. Esse comportamento foi corrigindo, estabilizando o funcionamento desse tipo de campo.
- Corrigido o problema em que exportações de gráficos do tipo barra, linha e área eram exportados sem incluir os valores vazios/nulos.

## [24/09/2025] [Correção]

- Corrigido problema em que o botão com o logo da Neppo impedia que o botão de "Salvar" em Relatórios 3.0. Foi adicionado um observador para identificar os momentos corretos de remover o snippet, evitando conflitos com os botões de confirmação.

## [25/09/2025] [Correção]

- App: adicionado um scroll em mensagens de erro, que agora poderão ser lidas em sua completude.
- App: corrigido o problema em que campos obrigatórios de opcionais eram requeridos mesmo que nenhum opcional tenha sido incluído ao produto.
