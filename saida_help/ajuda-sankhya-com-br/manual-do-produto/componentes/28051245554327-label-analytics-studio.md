---
id: "28051245554327"
titulo: "Label - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28051245554327-Label-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:10:44Z"
rotulos: ["Configuração", "Componentes", "Visualização de Dados", "Analytics Studio", "Interface do Usuário"]
---

# Label - Analytics Studio

O componente LABEL é utilizado para exibir textos, que podem ser fixos ou dinâmicos (provenientes do banco de dados). Este componente é ideal para adicionar descrições, títulos, totais, informações gerais de cadastros filtrados, ou qualquer outra informação textual. As interações incluem abrir modais, executar ações, manipular dados por SQL, abrir formulários, entre outras possibilidades.

![Imagem 1: O componente LABEL é utilizado para exibir textos, que podem ser fixos ou dinâmicos (provenientes do banco de dados).…](https://ajuda.sankhya.com.br/hc/article_attachments/28055619269271)

## Como configurar

Arraste o componente LABEL para a tela onde deseja exibir o texto.

### Dados

Configure a VIEW através de SQL, VIEW Análise de Dados ou VIEW de Cadastro caso queira alimentar os dados da label com informações provenientes do banco de dados. Ela deve retornar apenas uma linha e uma coluna. 

### Personalizar

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=QpXUO0HiKmo)

#### Configurações gerais

- **Texto:** insira o texto que será exibido pelo componente. Pode ser usado variáveis para exibir dados dinâmicos na label.
- **Scroll:** caso o conteúdo da label seja maior que o tamanho dela, ao ativar essa opção, será gerado um scroll interno.
- **Texto selecionável:** permite que o texto seja selecionado pelo usuário para ser possível copiá-lo usando o "Ctrl + C".
- **Tamanho:** permite definir o tamanho relativo da fonte, que altera conforme a resolução do usuário.
- **Tamanho Mínimo da Fonte (px):** defina o tamanho mínimo da fonte, para evitar que a fonte fique muito pequena em resoluções muito menores. Para entender melhor, acesse a documentação de [Responsividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio#Responsividade).
- **Fonte:** escolha a fonte do texto.
- **Formatação de Texto:** ajuste a formatação do texto, incluindo negrito, itálico, sublinhado, cor do texto, alinhamento e estilo.
- **Cor do Texto:** defina a cor do texto da label.
- **Cor de Fundo:** determine a cor de fundo da label.
- **Transparência:** defina a opacidade do label.
- **Configurar borda:** acesse para configurar o contorno, cor, espessura e arredondamento da borda.
- **Dica:** insira uma dica (tooltip) que será exibida ao passar o mouse sobre a label.
- **Incluir hiperlink:** permite incluir um link que abre em uma nova aba do navegador.

#### Animação

- **Transição:** ative para aplicar um efeito de transição que altera a cor de fundo do elemento ao passar o cursor sobre ele.
- **Cor da transição:** defina a cor do fundo quando o cursor passa sobre o label.
- **Elevação:** ative para adicionar um efeito de sombreamento que adiciona profundidade aos elementos.
- **Nível da elevação:** determine o nível da profundidade da elevação.

#### Visibilidade dinâmica

A funcionalidade de Visibilidade dinâmica permite que a label fique visível ou invisível conforme o valor retornado por uma View. O componente desaparecerá se o valor retornado for 0 ou null e aparecerá para qualquer outro número. Esta funcionalidade pode ser aplicada utilizando a View do próprio componente ou a View da tela, oferecendo flexibilidade na configuração e controle do comportamento dos componentes.

- **Referenciando a VIEW do próprio componente:** quando configurada para usar a View do próprio componente, a Visibilidade dinâmica baseia-se na primeira linha e coluna retornada pela View para determinar a visibilidade.
- **Referenciando a VIEW da tela:** caso a visibilidade seja configurada para referenciar a View da tela, o usuário pode especificar a interseção desejada utilizando comandos de variáveis. Por exemplo, o comando "$A1" pode ser usado para pegar o valor da primeira linha e coluna da View da tela.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=u6MRuhvlQGA)

#### Reatividade

Escolha manualmente os componentes que serão atualizados. Para mais detalhes sobre como utilizar essa funcionalidade, consulte a documentação [Reatividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/28080172417687-Reatividade-Analytics-Studio).

#### Interações

- **Nenhuma:** a label não terá interação.
- **Ação:** defina uma ação para ser executada ao interagir com a label.
- **Ação de Database:** permite realizar operações de manipulação de dados, como INSERT, UPDATE, DELETE, ou chamar PROCEDURES.
- **Formulário:** abra um formulário ao interagir com a label.
- **Modal:** abra um modal ao interagir com a label.

## Conjuntos de Labels

Os conjuntos de labels são agrupamentos de labels prontos que facilitam a montagem e a exibição de informações de forma organizada, que podem ser alterados para qualquer usabilidade. Nesses conjuntos, os componentes estão agrupados, de modo que ao arrastar, ampliar ou diminuir, todos os elementos do grupo são ajustados juntos. Caso queira modificar apenas uma label específica dentro do conjunto, será necessário desagrupar os componentes primeiro. Para mais informações sobre como desagrupar, acesse a documentação [Layout de Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/28055755050135-Layout-de-Componentes-Analytics-Studio).

### Cards

São conjuntos de labels mais simples. Eles podem incluir textos, ícones, valores e comparações, dependendo do modelo escolhido.

![Imagem 2: São conjuntos de labels mais simples. Eles podem incluir textos, ícones, valores e comparações, dependendo do modelo…](https://ajuda.sankhya.com.br/hc/article_attachments/28055633862295)

### Grupo de Cards

São conjuntos maiores que agrupam múltiplos cards para exibir informações detalhadas e comparativas.

![Imagem 3: São conjuntos maiores que agrupam múltiplos cards para exibir informações detalhadas e comparativas.](https://ajuda.sankhya.com.br/hc/article_attachments/28055633867031)

---

![Imagem 4: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157093559319) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
