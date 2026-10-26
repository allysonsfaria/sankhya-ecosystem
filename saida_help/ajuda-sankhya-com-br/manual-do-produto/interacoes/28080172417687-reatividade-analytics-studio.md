---
id: "28080172417687"
titulo: "Reatividade - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28080172417687-Reatividade-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Interações"
atualizado_em: "2026-09-23T17:28:13Z"
rotulos: ["Configuração", "Analytics Studio", "Desempenho", "Reatividade", "Interface do Usuário"]
---

# Reatividade - Analytics Studio

A funcionalidade de Reatividade permite o controle dos componentes que serão atualizados em resposta a interações do usuário. Isso é fundamental para manter a interface sincronizada com o estado atual dos dados, mas ao mesmo tempo não atualizar componentes que não são necessários na interação.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=3O_DE-eMGTw)

### Reatividade manual desativada

Por padrão, se a Reatividade manual estiver desativada, a plataforma atualiza todos os componentes da tela quando ocorre uma alteração de dados ou interação do usuário. Este processo inclui um "piscar" da tela, onde todos os elementos são atualizados de uma vez, o que pode ser visualmente disruptivo, mas garante que toda a interface esteja sempre atualizada.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=aXy7vj7npdw)

### Configuração de reatividade

- **Selecionar o Componente:** navegue até o componente que deseja configurar a reatividade.
- **Ativar Reatividade Manual:** no menu de configurações, em **"Personalizar"**, acesse a seção **"Reatividade"** e ative a marcação **"Escolher manualmente componentes que serão atualizados"** em resposta a mudanças nos dados ou interações do usuário. Isso proporciona maior controle sobre o comportamento da interface e pode otimizar o desempenho da aplicação. É particularmente útil em cenários onde a atualização constante de todos os componentes não é necessária ou poderia impactar negativamente na experiência do usuário.
- **Selecionar Telas:** selecione as telas onde estão os componentes que deseja reativar.
- **Componentes:** após selecionar uma tela, escolha os componentes dentro dela que devem ser atualizados automaticamente. Os componentes são selecionados pelos seus IDs. Por exemplo, pode-se selecionar a Tela 1 e escolher atualizar os componentes com ID 3 e 4. Em seguida, selecionar a Tela 2 e escolher os componentes com ID 2 e 9. Isso significa que os componentes com o ID 3 e 4 da Tela 1, e os componentes com o ID 2 e 9 da Tela 2 serão reativos às mudanças.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=4__YkVp8Fuc)

### Como encontrar o ID dos componentes

Para configurar a reatividade manualmente, é necessário conhecer o ID dos componentes que deseja tornar reativos. Cada componente, ao ser adicionado à tela, recebe automaticamente um ID único. Para descobrir o ID de um componente:

- **Clique com o botão direito no componente:** ao clicar com o botão direito sobre o componente, abrirá um menu drop-down de opções.
- **Ver o ID no header do menu:** o ID do componente estará exibido no header deste menu. Este é o ID que deve ser selecionado ao configurar a reatividade para garantir que o componente correto seja atualizado.

![Imagem 1: Ver o ID no header do menu: o ID do componente estará exibido no header deste menu. Este é o ID que deve ser…](https://ajuda.sankhya.com.br/hc/article_attachments/28080172412823)

### Não atualizar nenhum outro componente

Caso queira que nenhum componente seja atualizado, basta ativar a marcação **"Escolher manualmente componentes que serão atualizados"** e não selecionar nenhum componente. Isso desativa as atualizações automáticas para todos os componentes, garantindo que a interface permaneça estática mesmo com alterações de dados ou interações do usuário.

### Entrada de dados automática e reatividade

A funcionalidade de Entrada de dados automática é projetada para salvar automaticamente todas as alterações de dados feitas pelos usuários. Essa funcionalidade é frequentemente usada em conjunto com a marcação Escolher manualmente componentes que serão atualizados para otimizar o desempenho da aplicação e melhorar a experiência do usuário.

O uso conjunto dessas funcionalidades garante que as atualizações sejam feitas de forma suave, sem "piscadas" de tela ou interrupções visuais, proporcionando uma experiência de usuário mais fluida e contínua. Para mais informações sobre entrada de dados automática, acesse o artigo [Entrada de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/28000829892119-Entrada-de-Dados).

### Vantagens da reatividade

- **Controle Preciso:** permite selecionar exatamente quais componentes devem ser atualizados, evitando atualizações desnecessárias de toda a interface.
- **Otimização de Desempenho:** reduz a carga de processamento ao evitar a atualização de componentes que não mudaram, melhorando a eficiência da aplicação.
- **Melhoria da Experiência do Usuário:** com menos "piscadas" na tela, a interface se torna mais estável e agradável para o usuário final.

---

![Imagem 2: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157258760983) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
