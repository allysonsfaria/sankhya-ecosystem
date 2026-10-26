---
id: "42430176210327"
titulo: "Área do Construtor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430176210327-%C3%81rea-do-Construtor"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:59:51Z"
rotulos: ["sync_hc", "neppo", "neppo_477462530", "sync_hash_99005532bc74"]
---

# Área do Construtor

Esta tela é o ambiente de trabalho principal onde a lógica, as respostas e o comportamento do chatbot são construídos. A interface é dividida em quatro áreas principais para facilitar a navegação e construção.

![Imagem 1: Esta tela é o ambiente de trabalho principal onde a lógica, as respostas e o comportamento do chatbot são construídos.…](https://ajuda.sankhya.com.br/hc/article_attachments/42639486248983)

## 1. Barra Superior (Gestão e publicação)

Localizada no topo da tela, esta barra contém os controles administrativos do bot que está sendo editado.

[GIF animado: Imagem 2: Localizada no topo da tela, esta barra contém os controles administrativos do bot que está sendo editado.](https://ajuda.sankhya.com.br/hc/article_attachments/42639547235735)

- **Identificação:** Exibe o nome do bot (ex: "Valdson teste") e um ícone de lápis para edição do nome.
- **Controle de Versão:** Mostra a versão atual (ex: "Versão 1.0 • Editando bot existente") e permite alternar entre versões anteriores através de um menu suspenso.
- **Ações Principais:**

  - **Salvar:** Grava as alterações realizadas no rascunho sem disponibilizá-las para os usuários finais.
  - **Download (Ícone):** Permite baixar/exportar o fluxo atual.
  - **Publicar:** Torna a versão atual ativa e disponível para interação real.

## 2. Menu Lateral Esquerdo (Estrutura do Fluxo)

Esta área, intitulada "Visão dos fluxos", organiza a hierarquia de navegação do bot.

[GIF animado: Imagem 3: Esta área, intitulada "Visão dos fluxos", organiza a hierarquia de navegação do bot.](https://ajuda.sankhya.com.br/hc/article_attachments/42639518281751)

- **Adicionar Fluxo:** Botão para criar novos caminhos de conversa independentes.
- **Ações após adição de componentes:** Renomear, Duplicar e Excluir.

  - Renomear ação:

    ![Imagem 4: Renomear ação:](https://ajuda.sankhya.com.br/hc/article_attachments/42639500572695)
  - Duplicar ação:

    [GIF animado: Imagem 5: Duplicar ação:](https://ajuda.sankhya.com.br/hc/article_attachments/42639531962391)
  - Excluir ação:

    [GIF animado: Imagem 6: Excluir ação:](https://ajuda.sankhya.com.br/hc/article_attachments/42639537987223)
- **Ações do fluxo:**

  - Renomear fluxo:

    ![Imagem 7: Renomear fluxo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639522022295)
  - Duplicar fluxo:

    [GIF animado: Imagem 8: Duplicar fluxo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639548848535)
  - Excluir fluxo:

    [GIF animado: Imagem 9: Excluir fluxo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639532929815)
- **Árvore de Navegação:**

  - **Fluxo principal:** O ponto de partida da interação do bot. Contém a opção "+ Adicionar ação" para inserir novos passos.
  - **Fluxo de erro:** Define o comportamento do bot quando algo inesperado ocorre ou o sistema falha.

## 3. Área Central (Canvas de Trabalho)

É o espaço onde o fluxo é visualizado e construído. Ao iniciar um bot novo, esta área exibe instruções de boas-vindas:

![Imagem 10: É o espaço onde o fluxo é visualizado e construído. Ao iniciar um bot novo, esta área exibe instruções de boas-vindas:](https://ajuda.sankhya.com.br/hc/article_attachments/42639549283223)

1. **Inserção:** Clique no ícone do componente desejado no menu à direita para inseri-lo.
2. **Configuração:** Preencha os dados do componente e salve.
3. **Publicação:** Após finalizar a montagem, clique em publicar.

## 4. Menu Lateral Direito (Biblioteca de componentes)

Este menu contém todas as ferramentas disponíveis para construir a interação. Os componentes são divididos por categorias e podem ser encontrados via barra de busca ("Buscar componentes...").

[GIF animado: Imagem 11: Este menu contém todas as ferramentas disponíveis para construir a interação. Os componentes são divididos por…](https://ajuda.sankhya.com.br/hc/article_attachments/42639502288535)

### Categorias disponíveis:

- **IA (Inteligência Artificial):**

  - OpenAI, Assistente, Fala para texto, Texto para fala, Base de Conhecimento.
- **Elementos (Interação Básica):**

  - Texto, Entrada de Dados, Anexo, Menu de Opções.
- **Lógica (Processamento e Regras):**

  - Requisitar API, Neppo API, Redirecionar, Executar Script.
  - Esperar, Condicionar, Para JSON, Iteração.
  - Expressão, Validar, Executar, Sair.
- **Outras Integrações:**

  - Voz, Whatsapp, Google Agenda (visíveis nas tags de filtro).
