---
id: "27958110669719"
titulo: "Board - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27958110669719-Board-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:15:50Z"
rotulos: ["Configuração", "Visualização de Dados", "Analytics Studio", "Gestão de Projetos", "Kanban", "CRM"]
---

# Board - Analytics Studio

O componente Board é uma ferramenta projetada para organizar e visualizar fluxos de trabalho no estilo Kanban, permitindo o movimento de cards entre diferentes etapas. Esse componente é especialmente útil para gestão de tarefas, gestão de projetos, fluxo de processos ou até mesmo CRM, proporcionando uma visão clara e organizada do status dos itens em cada fase do processo.

![Imagem 1: O componente Board é uma ferramenta projetada para organizar e visualizar fluxos de trabalho no estilo Kanban,…](https://ajuda.sankhya.com.br/hc/article_attachments/27958114993047)

---

### Como Configurar

Arraste o componente board para a tela onde deseja exibir o Kanban. Depois, configure a VIEW utilizando SQL ou VIEW de Cadastro para alimentar os cards e etapas do Board.

### Personalizar VIEW de SQL

Na configuração de **"Personalizar"**, ao optar pelo uso de uma VIEW de SQL, é necessário seguir os passos abaixo:

1. **Cadastro de Cards:** informe qual é o cadastro que está sendo utilizado para gerar os cards, como, por exemplo, **"Negociações"** em um CRM.
2. **Coluna de ID:** selecione a coluna da VIEW que contém o ID dos cards, essencial para identificar cada card de forma única dentro do Board.
3. **Coluna de Descrição:** defina qual coluna da VIEW trará a descrição do card. Esta descrição será o texto principal exibido no componente.
4. **Cadastro de Etapas:** especifique o cadastro que define as etapas do Kanban. No caso de um CRM, as etapas podem incluir **"Lead"**, **"Demonstração"**, **"Prova de Conceito"**, **"Negociação"**, **"Forecast"**, **"Positivado"**. Para uma gestão de tarefas, as etapas podem ser **"Pendente"**, **"A Fazer"**, **"Concluído"**, entre outras.
5. **Coluna de Etapa:** selecione a coluna da VIEW que contém o ID da FK que representa as etapas. Sua VIEW deve retornar pelo menos o ID do cadastro gerador de cards, a descrição do card e o ID da FK que define as etapas.
6. **Etapas Visíveis:**

- **Fixo:** selecione manualmente as etapas que deseja visualizar no Board.
- **SQL:** utilize SQL para retornar o ID e a descrição das etapas, permitindo que as fases do card sejam montadas dinamicamente.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=4np3SI4faMk)

### Personalizar VIEW de Cadastro

Ao configurar o board utilizando uma VIEW de Cadastro, o [Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231) reconhece automaticamente o cadastro e sua relação com a coluna que armazena as etapas. Nesse caso, basta definir:

1. **Cadastro de Etapas:** selecione o cadastro que definirá as etapas do Kanban, assim como na configuração via SQL.
2. **Etapas Visíveis:**
   - **Fixo:** selecione manualmente as etapas que deseja visualizar no Board.
   - **SQL:** utilize SQL para determinar quais etapas serão visíveis, permitindo que as fases do card sejam definidas dinamicamente.
3. **Utilizar Primeiro Dado como Título:** caso o título do card deva ser baseado em uma coluna da VIEW em vez da descrição do eixo, ative essa opção. Por exemplo, em um CRM, é possível usar o nome do prospect como título, em vez do número da negociação.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=IUKXDmsnkQ0)

#### Configurações Gerais Adicionais:

- **Movimentação de Cards:** ative ou desative a movimentação dos cards entre as etapas.
- **Busca:** ative a opção de busca, permitindo que os usuários localizem rapidamente cards específicos.
- **Design:** personalize o design do Board, ajustando a cor e o tamanho da fonte, a largura das colunas e outras opções estéticas.

### Tags

É possível adicionar tags aos cards para categorizá-los ou destacá-los visualmente. Para isso, concatene o nome do atributo com o código hexadecimal da cor (por exemplo, "Quente#FF5733" para representar "Quente" em vermelho). As tags aparecerão coloridas, facilitando a identificação visual dos cards.

Para mais detalhes, assista ao vídeo demonstrativo ou, em caso de dúvidas sobre os algoritmos ou a configuração da VIEW, consulte a **documentação "View de Cadastro"**, que aborda o processo de construção e personalização de views de cadastros.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=IOszXQo6f7c)

### Controle de Movimentação

As movimentações de cards entre etapas podem ser controladas de forma personalizada. Essa configuração é realizada diretamente nas configurações de cada etapa. Ao clicar nos três pontos localizados na etapa, é possível definir as regras de movimentações.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=K_YYb7agoKg)

### Interações

O Board aceita várias interações, incluindo:

- **Ação:** permite configurar uma ação específica para ser executada ao interagir com um card.
- **Ação de Database:** possibilita a realização de operações de manipulação de dados, como INSERT, UPDATE, DELETE, ou chamar PROCEDURES.
- **Formulário:** abre um formulário ao interagir com um card.
- **Modal de Detalhes:** exibe um modal de detalhes ao interagir com um card.

#### Modal de Detalhes Diferentes por Fase

Entre na configuração de cada fase para definir um modal de detalhes específico para aquela fase. Por exemplo, a Fase 1 pode ter o Modal de Detalhes 1, enquanto a Fase 2 pode ter o Modal de Detalhes 2.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=hfpcQSJi_p0)

---

![Imagem 2: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157115148567) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
