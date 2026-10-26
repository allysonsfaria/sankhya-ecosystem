---
id: "28000829892119"
titulo: "Entrada de Dados - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28000829892119-Entrada-de-Dados-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Interações"
atualizado_em: "2026-09-23T17:30:23Z"
rotulos: ["Configuração", "Ações", "Analytics Studio", "Entrada de Dados", "Reatividade"]
---

# Entrada de Dados - Analytics Studio

A funcionalidade de Entrada de Dados possibilita a edição direta de informações em componentes de tabelas. Esta opção está disponível exclusivamente em telas Web ou Mobile, não sendo compatível com dashboards.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=FKklPBGoktU)

### Configuração

Para habilitar a entrada de dados na tabela, acesse o menu de configurações do componente. Na View, navegue até a coluna que deseja habilitar a entrada de dados, clique nos três pontos ao lado do dado e ative a opção de entrada de dados. Assim, essa coluna permitirá ao usuário, a inserção de dados.

Indicação visual:

- **Sem Entrada de Dados:** quando a entrada de dados não está ativada, as células da tabela são exibidas com uma aparência padrão.
- **Entrada de Dados Ativada, Sem Salvamento:** quando a entrada de dados é ativada e os dados são editados, mas ainda não salvos, as células são destacadas com uma cor diferente (um **rosa** mais forte), indicando que há alterações pendentes de salvamento.
- **Entrada de Dados Ativada, Dados Salvos:** após os dados serem salvos, as células retornam a uma aparência de dados salvos (**rosa** claro), indicando que as informações foram persistidas no banco de dados.

![Imagem 1: Entrada de Dados Ativada, Dados Salvos: após os dados serem salvos, as células retornam a uma aparência de dados salvos…](https://ajuda.sankhya.com.br/hc/article_attachments/28042536708119)

#### Critério de uso para a funcionalidade de entrada de dados

Essa funcionalidade é regulada por um critério essencial: o nível de detalhamento da tabela. A entrada de dados é automaticamente bloqueada se a tabela não estiver no nível de detalhamento mais específico, para garantir a precisão e a integridade das informações.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=AJyAb1ganG8)

#### Nível de detalhamento

**Mais Específico:** a entrada de dados é permitida quando a tabela exibe dados no seu nível raiz, como registros individuais de transações ou eventos. Neste caso, o sistema pode identificar a qual registro específico as alterações devem ser aplicadas. Por exemplo:

Em uma tabela que detalha vendas por mês e vendedor, é possível editar os dados de vendas e metas porque cada registro é único e específico para cada mês e cada vendedor.

#### Nível de agregação

**Menos Específico:** quando a tabela é configurada para um nível de agregação mais alto, como resumir dados anuais ou por categoria, a entrada de dados é desabilitada. Isso ocorre porque o sistema não pode determinar com precisão como distribuir as alterações feitas pelos usuários em registros específicos. Por exemplo:

Ao visualizar dados de vendas agregados por ano, o sistema não sabe a qual mês uma nova meta de vendas deveria ser aplicada.

#### Uso de filtros para especificação

**Seletor de Detalhes:** para permitir a entrada de dados em tabelas agregadas, os usuários podem utilizar filtros ou seletores para especificar o nível de detalhe desejado. Por exemplo, um seletor de mês pode ser usado para definir um mês específico. Isso permite que o sistema saiba exatamente onde aplicar as alterações, desbloqueando a funcionalidade de entrada de dados. Este método ajuda a manter a integridade dos dados enquanto permite a edição em níveis de detalhamento adequados. Para mais detalhes, acesse o artigo [Seletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/28043220122647-Seletor-Analytics-Studio).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=PbCb4WqBU7c)

Este critério de bloqueio para entrada de dados em níveis de agregação mais altos é uma precaução importante para proteger a precisão dos dados. Ele assegura que qualquer modificação seja feita de forma consciente e precisa, correspondendo aos registros específicos onde essas alterações são aplicáveis.

---

### Entrada de dados automática

A entrada de dados automática é uma funcionalidade que salva automaticamente as alterações feitas pelos usuários sem a necessidade de ações manuais. Isso garante que todas as mudanças sejam persistidas no banco de dados instantaneamente, mantendo os dados sempre atualizados.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=xOxIod0JBk0)

#### Configuração

Para ativar a entrada de dados automática, acesse as configurações do componente, em **"Personalizar"**, habilite a marcação **"Entrada de dados automática"**.

#### Integração com reatividade

A entrada de dados automática pode ser usada em conjunto com a funcionalidade de **"Reatividade"**. Quando ambas estão habilitadas, a plataforma não só salva as alterações automaticamente, mas também atualiza os componentes relacionados de forma automática, sem a necessidade de recarregar todos os componentes da tela. Isso é especialmente útil para garantir que a interface do usuário reflita sempre os dados mais recentes sem interrupções visuais, como "piscadas" na tela. Para mais informações, acesse o artigo [Reatividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/28080172417687-Reatividade-Analytics-AI).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=GpEq4DUp9tI)

### Ações personalizadas para salvar dados

Além da entrada de dados automática, os desenvolvedores podem configurar ações personalizadas para salvar dados manualmente, por meio de um botão ou label. Isso é útil em cenários onde o salvamento automático não é desejável, proporcionando maior controle sobre o momento e as condições em que os dados são salvos.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=N4IU7Vn2hSE)

#### Configuração

Para a criação da ação:

![Imagem 2: Acesse a seção de interações do componente que deseja, crie e vincule uma nova ação.](https://ajuda.sankhya.com.br/hc/article_attachments/28042792762263) Acesse a seção de interações do componente que deseja, crie e vincule uma nova ação.

![Imagem 3: No primeiro passo da ação, adicione o passo "Salvar Entrada de Dados" .](https://ajuda.sankhya.com.br/hc/article_attachments/28042776849559) No primeiro passo da ação, adicione o passo **"Salvar Entrada de Dados"**.

![Imagem 4: No segundo passo, adicione a funcionalidade "Recarregar" , que garante que a interface do usuário seja atualizada para…](https://ajuda.sankhya.com.br/hc/article_attachments/28042776862999) No segundo passo, adicione a funcionalidade **"Recarregar"**, que garante que a interface do usuário seja atualizada para refletir os dados salvos recentemente. Para mais detalhes sobre a configuração dessas ações, consulte o artigo [Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/27883754211863-A%C3%A7%C3%B5es-Analytics-AI).

Atribuição da ação:

A ação personalizada pode ser atribuída a vários tipos de componentes, como botões e labels, por exemplo, ao clicar em um botão configurado com a ação de salvamento, o sistema irá salvar os dados e recarregar a interface conforme configurado.

Essa abordagem de salvamento manual é útil em casos onde é necessário validar os dados antes de salvá-los ou quando o usuário precisa confirmar o salvamento.
