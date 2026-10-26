---
id: "43548566032535"
titulo: "Por que a OP não aparece na tela de Operações de Produção?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548566032535-Por-que-a-OP-n%C3%A3o-aparece-na-tela-de-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-10-06T12:36:40Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Por que a OP não aparece na tela de Operações de Produção?

Ao lançar uma ordem de produção no sistema, é esperado que ela seja exibida na tela de **"Operações de Produção"** (Produção » Rotinas » Operações de Produção) para apontamento das atividades. No entanto, em algumas situações, a ordem de produção pode não aparecer nesta tela, gerando dúvidas sobre o motivo e como proceder para que a ordem seja corretamente exibida.

A ausência da ordem de produção na tela de operações pode estar relacionada a diferentes fatores, como o **status da ordem e permissões de usuário.** É importante verificar cada um desses pontos para garantir o correto funcionamento do processo produtivo e o registro das operações realizadas.

### Verificação do status da ordem de produção

Para que uma ordem de produção seja exibida na tela de **"Operações de Produção"** (Produção » Rotinas » Operações de Produção), ela precisa estar devidamente inicializada. Ordens apenas planejadas ou ainda não liberadas para execução não aparecem nesta tela, pois o sistema exibe apenas ordens em andamento, ou seja, aquelas que já foram criadas e inicializadas pela gerência da produção.

Verifique o status da ordem na tela de **"Ordens de Produção"** (Produção » Rotinas » Ordens de Produção - Nova). Caso a ordem esteja como planejada/criada, realize a **inicialização** para que ela passe a ser exibida nas operações.

### Permissões de usuário e filtros aplicados

Em alguns casos, a ordem de produção pode não aparecer devido a restrições de acesso do usuário ou filtros aplicados na tela de **"Operações de Produção"**.

**Obs.:** Uma atividade já iniciada é apresentada somente para o **usuário executante** daquela operação, caso o processo tenha configuração de **usuários executantes dentro do roteiro.**

Certifique-se de que o usuário possui permissão para visualizar e operar as ordens desejadas e revise os filtros ativos na tela, como empresa, centro de trabalho, status da atividade, entre outros. E, se preciso, revise as permissões de acesso no cadastro de **"Usuários"** (Configurações » Controle de Acesso » Usuários) ou **"Acessos"** (Configurações » Controle de Acesso » Acessos), garantindo que o usuário tenha acesso ao módulo de produção e às operações relacionadas.

**Obs.:** Na aba Segurança da tela **"Usuários"** (Configurações » Controle de Acesso » Usuários), temos a opção **"Gerente de Manufatura"**, quando marcada essa opção, o usuário consegue visualizar e realizar qualquer ação em todas as atividades daquela OP, mesmo estando atribuída à algum usuário executante.
