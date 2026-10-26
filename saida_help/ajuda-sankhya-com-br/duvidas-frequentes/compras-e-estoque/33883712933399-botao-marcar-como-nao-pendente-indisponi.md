---
id: "33883712933399"
titulo: "Botão “Marcar como não pendente” indisponível do cabeçalho dos portais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33883712933399-Bot%C3%A3o-Marcar-como-n%C3%A3o-pendente-indispon%C3%ADvel-do-cabe%C3%A7alho-dos-portais"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:28:08Z"
rotulos: ["Pedidos", "Configuração", "Segurança", "Agendador", "Integração", "Portal", "Botão", "Marcar como não pendente", "TGFCAB.CODUSUINC", "Status do pedido", "Usuário de inclusão", "“Marcar como não pendente”", "indisponível do cabeçalho dos portais"]
---

# Botão “Marcar como não pendente” indisponível do cabeçalho dos portais

Pedidos incluídos por meio de integração apresentam uma limitação no uso do botão **"Outras Opções >> Marcar como não pendente"** nos portais.
Esse botão fica indisponível quando o usuário logado não é o mesmo que realizou a inclusão do pedido. Situação comum em operações automatizadas, como integrações via API ou robôs, nas quais os pedidos são inseridos com um usuário genérico (por exemplo, integração ou ERP).
Nesses casos, os demais usuários não conseguem marcar o pedido como “não pendente” diretamente pelo portal, o que pode gerar dúvidas sobre o funcionamento do sistema.

**SOLUÇÃO:**

**Siga as alternativas abaixo para contornar a indisponibilidade do botão:**

- **Usuário de inclusão:** apenas o usuário responsável pela inclusão, identificado pelo campo **"TGFCAB.CODUSUINC"**, poderá visualizar e utilizar o botão **"Marcar como Não Pendente"** nos portais.
  **Exemplo:** se o pedido foi criado pelo usuário 10, ao logar com o usuário 1 o botão ficará indisponível. Se o usuário 1 duplicar o pedido, ele se torna o novo usuário de inclusão, habilitando a opção para ele.
- **Status do pedido:** quando o pedido estiver com o status **"Confirmado"** ou **"Liberação Reprovada"**, **qualquer usuário** poderá utilizar o botão para marcar o pedido como não pendente, independentemente do usuário de inclusão.
- **Alternativa - botão no quadrante de itens:** utilize o botão **"Marcar como Não Pendente"** disponível no **quadrante de itens** do portal. Esse botão costuma estar acessível mesmo quando o botão do cabeçalho está desabilitado. Quando todos os itens do pedido estiverem marcados como não pendentes, o sistema considera automaticamente o pedido como não pendente no cabeçalho.
- **Agendador para marcar pedidos como não pendentes:** utilize a tela do Agendador para marcar pedidos como não pendentes. Por meio dela, configure regras automáticas para que pedidos sejam atualizados periodicamente conforme critérios definidos (exemplo: pedidos sem itens pendentes há mais de X dias). Essa prática automatiza o processo e evita dependência de ações manuais, especialmente em ambientes com integração.

**CAUSA:**

A indisponibilidade do botão **"Marcar como Não Pendente"** está diretamente ligada à lógica de controle por usuário de inclusão implementada no sistema. Essa regra garante que apenas o responsável pela criação do pedido, identificado no campo TGFCAB.CODUSUINC, tenha permissão para alterar determinados estados do pedido.

Pedidos criados via integração costumam ser inseridos com um usuário padrão (normalmente técnico ou de sistema), o que impede que usuários operacionais realizem certas ações sem duplicar o pedido ou recorrer a alternativas, como o botão disponível nos itens ou o uso do agendador.

Essa limitação não é um erro do sistema, mas sim uma medida de controle voltada à segurança e à rastreabilidade. Em ambientes integrados ou com múltiplas equipes, pode impactar a operação se não for bem compreendida e tratada com as alternativas mencionadas.
