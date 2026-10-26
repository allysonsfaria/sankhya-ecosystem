---
id: "28076589636631"
titulo: "Modal de Detalhes - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28076589636631-Modal-de-Detalhes-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Interações"
atualizado_em: "2026-09-23T17:24:17Z"
rotulos: ["Configuração", "Relatórios", "Componentes", "Analytics Studio", "Interação"]
---

# Modal de Detalhes - Analytics Studio

A funcionalidade Modal de Detalhes é uma interação projetada para oferecer uma visão detalhada de itens selecionados pelos usuários, sempre ligado a uma única tabela de cadastro. Essa interação é particularmente útil para exibir informações completas e detalhadas sobre um item específico, permitindo uma análise mais aprofundada.

![Imagem 1: A funcionalidade Modal de Detalhes é uma interação projetada para oferecer uma visão detalhada de itens selecionados…](https://ajuda.sankhya.com.br/hc/article_attachments/28076662886423)

### Como criar um Modal de detalhes

- Acesse a seção de **"Interações"** do componente que deseja e crie um novo modal de detalhes.
- Selecione o cadastro ao qual o modal de detalhes será vinculado. Isso definirá a fonte de dados que será utilizada, permitindo que os detalhes sejam filtrados para cada registro específico desse cadastro.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=573wmAXiKvY)

### Estrutura do componente

- **Informações Cadastrais (lado esquerdo):** exibe detalhes cadastrais do item selecionado. Esses detalhes podem ser configurados para serem editáveis ou somente leitura, conforme as necessidades da aplicação.
- **Área de Conteúdo (lado direito):** esta área permite a criação de múltiplas abas, cada uma podendo exibir diferentes tipos de conteúdos relacionados ao item. Abaixo, são detalhados os tipos de abas que podem ser configurados:

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=CYlx9PUowJs)

#### TimeLine

Essa aba é ideal para exibir atualizações, históricos ou para aprofundar o nível de detalhes da aplicação. O comportamento é semelhante ao do componente **"TimeLine"**. A aba TimeLine só estará disponível se houver uma tabela ligada com o cadastro do **"Modal de Detalhes"** como **"FK"**. Por exemplo, um modal de Negociação pode ter a entidade **"Item de Negociação"** como parte da TimeLine, permitindo um acompanhamento detalhado das interações e eventos.

#### Formulário

Essa aba permite adicionar um formulário relacionado ao cadastro específico ligado ao modal de detalhes. É utilizada principalmente para facilitar a edição dos dados de cadastro, oferecendo uma interface direta e intuitiva para alterações de informações.

#### Tela

Essa aba possibilita a escolha de uma das telas já construídas utilizando o Page Builder. 

### Botões de Interação

Na área superior do componente Modal de Detalhes, é possível criar botões de interação, cada um configurável com as seguintes opções:

- **Dica:** texto apresentado como hover do botão, exibido quando o cursor do mouse passa sobre o botão.
- **Critério de Bloqueio:** permite definir um atributo para bloquear o botão dinamicamente, baseado nas seleções do modal de detalhes. O botão ficará ativo se o atributo utilizado para bloquear retornar 0 ou null, e será bloqueado para outros valores.
- **Tipo de Execução:** define a interação do botão, com opções de executar uma ação, com a possibilidade de configurar uma mensagem de confirmação, ou abrir uma tela, que funciona como um modal, abrindo uma tela configurada no Page Builder.
- **Personalizar:** configurações de layout padrão do botão, incluindo ícone, cor de fundo, e cor de texto/ícone.

### Configurações gerais do Modal de detalhes

No canto superior direito da tela, por meio do botão **"Configurações"**, estão disponíveis algumas configurações gerais, como critério de bloqueio que define um atributo para bloquear todo o modal de detalhes quando o valor for diferente de null ou 0.

Quando bloqueado, a área de informação cadastral e a área de conteúdo ficam acinzentadas, com uma mensagem centralizada no header do detail, configurada no campo **"Mensagem do Bloqueio"**.

---

![Imagem 2: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157115423255) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
