---
id: "28269505969815"
titulo: "Filtrar outros componentes - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28269505969815-Filtrar-outros-componentes-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Interações"
atualizado_em: "2026-09-23T17:19:28Z"
rotulos: ["Configuração", "Analytics Studio", "Mobile", "Page Builder", "Interações"]
---

# Filtrar outros componentes - Analytics Studio

Na seção **"Interações"** se define entre os componentes, como, navegação entre telas, abertura de modais de detalhes ou formulários. 

A funcionalidade Filtrar outros componentes permite selecionar, através do ID, quais componentes serão atualizados ao interagir com um componente específico. Essa interação dinâmica entre diversos componentes em uma tela é semelhante ao funcionamento de dashboards e está disponível tanto em telas do tipo Page Builder (desktop) quanto em telas mobile.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=31izbTqvg7I)

Para configurar a interação Filtrar outros componentes em sua plataforma, siga os passos abaixo:

1. Acesse as Configurações do componente, selecione o componente desejado na tela e acesse a seção Interações.
2. Escolha a opção **"Filtrar outros componentes"** para configurar a filtragem.
3. Indique os **"Componentes"** para receber o filtro. Cada componente pode ser identificado pelo formato 'tipo de componente: ID'. Para obter o ID do componente, clique com o botão direito sobre o componente desejado, e o ID será exibido no topo do pop-up.
4. Clique no segmento do componente que será usado como base para a filtragem. Este segmento ficará em destaque.
5. Nos componentes de destino, um alerta será exibido indicando as seleções recebidas. Em componentes como cards ou views da tela, o alerta de seleção passada não é visível, mas é possível configurá-los para receberem as seleções de outros componentes.

![Imagem 1: Nos componentes de destino, um alerta será exibido indicando as seleções recebidas. Em componentes como cards ou views…](https://ajuda.sankhya.com.br/hc/article_attachments/28269498991255)

Exemplo:

Uma empresa deseja analisar o desempenho de negociações por executivo, utilizando um gráfico com a quantidade de negociações por executivo e uma tabela listando todas as negociações. Com a funcionalidade Filtrar outros componentes é possível conectar o gráfico com a tabela para que interajam entre si.

**Configuração:**

- **Gráfico:** negociações por Executivos: ID do componente: 240.
- **Tabela:** negociações: ID do componente: 241.

**Uso:** ao clicar em um executivo específico no gráfico, a tabela é atualizada para listar somente as negociações deste executivo. Caso, clique novamente no mesmo executivo, a filtragem é removida e a tabela volta a mostrar todas as negociações.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=L-ivvd5f7S0)
