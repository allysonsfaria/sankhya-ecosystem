---
id: "28081059115287"
titulo: "Relatório Formatado - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28081059115287-Relat%C3%B3rio-Formatado-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:17:41Z"
rotulos: ["Configuração", "Relatórios Formatados", "Relatórios", "Financeiro", "Analytics Studio"]
---

# Relatório Formatado - Analytics Studio

A funcionalidade Relatório Formatado permite a criação de layouts personalizados para visualização de dados em formato de tabela, essa funcionalidade é amplamente aplicada na construção de relatórios financeiros como DREs (Demonstrações do Resultado do Exercício), DFCs (Demonstrações dos Fluxos de Caixa), Balanços Patrimoniais e outros.

Essa ferramenta oferece uma maneira única de adaptar o uso de tabelas nas telas, permitindo uma visualização clara e organizada de informações, essencial para análises detalhadas e tomadas de decisão.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=nlF-ikWHrGs)

### Localização e Requisitos

A funcionalidade Relatório Formatado está localizada dentro da VIEW de Análise no componente tabela, na seção **"Configurações"**, opção **"Relatório Formatado"**. Para habilitar essa opção, é necessário que haja apenas um cadastro marcado como agrupador na tabela. Este agrupador é essencial, pois os relatórios formatados são vinculados diretamente a um cadastro, e só aparecerão como opção caso este cadastro esteja como agrupador.

### Criando um novo relatório

Para criar um novo relatório formatado, é necessário ter um componente tabela onde a VIEW já esteja configurada e tenha apenas um cadastro na parte de agrupadores da VIEW. Após cumprir esses requisitos, vá para a seção Configurações na VIEW, e na opção Relatório formatado, selecione **"Adicionar"**. Ao clicar nesse botão, será aberto o modal de construção do relatório, que oferece diversas funcionalidades para auxiliar na criação.

**Adicionar Membro:** botão verde localizado ao lado do campo de busca. Clicando nele, será criado linhas para configuração do relatório. Cada linha do relatório possui as seguintes opções de configuração:

**Descrição:** nome que aparecerá na tabela. Se for uma linha do tipo agrupador, será utilizado como referência para ser usado na coluna **“Pai”** (explicada abaixo).

**Fórmula:** permite o uso de uma série de comandos, resultando em diferentes tipos de saída no relatório.

**Comandos:** os comandos **"%"** e **"\*"** devem obrigatoriamente estar entre aspas duplas. 

**%":** é utilizado para criar linhas do tipo agrupador. Estas linhas são responsáveis por apresentar o valor total disponível nas métricas, levando em consideração os filtros aplicados. Ele funciona da seguinte forma:

- **Criação de Agrupadores:** quando se usa **"%"** em uma linha, está dizendo ao sistema para agrupar contas que começam com um determinado número. Por exemplo, para agrupar todas as contas que começam com "1", utilize a fórmula "1%".
- **Posicionamento do "%":** o **"%"** pode ser colocado antes ou depois do número, como "1%" ou “%1”. Se o "%" é colocado após o número, como em "1%", o agrupador vai incluir todas as contas que começam com "1". Se o “%” é colocado antes do número, como em “%1”, o agrupador vai incluir todas as contas que terminam com “1”.
- **Agrupamento de Vários Agrupadores:** também pode criar um agrupador que some vários outros agrupadores. Por exemplo, a fórmula “1%”+”2%” agrupa todas as contas que começam com “1” e “2”.
- Em resumo, o comando “%” ajuda a organizar e resumir dados em sua tabela, mostrando totais para grupos específicos de contas baseados nos filtros e nos números com os quais elas começam. A interação drill está disponível para linhas do relatório que utilizam essa fórmula.

**\*:** é utilizado para criar linhas do tipo detalhamento na tabela. Estas linhas mostram os valores disponíveis nos cubos com base nos filtros aplicados, mas apresentam separadamente todas as linhas da dimensão original que são relevantes para a seleção. Aqui está uma explicação simples de como funciona:

- **Criação de Detalhamentos:** quando se usa “\*” em uma linha, está dizendo ao sistema para detalhar e mostrar individualmente todas as contas que correspondem ao filtro aplicado.
- **Vinculação com Agrupadores:** linhas de detalhamento estão geralmente ligadas a uma linha agrupadora através da coluna "Pai". Isso significa que, ao expandir um agrupador, será possível verificar os detalhes específicos de cada conta que compõe aquele agrupador.
- **Exemplo Prático:** considere as contas: "10 – Mensalidade" e "11 – EAD".
  Pode-se criar um agrupador "1%" chamado "Receitas".
  Depois, pode criar um detalhamento "1\*" vinculado a "Receitas" como pai, que apresentará as contas "10" e "11" quando "Receitas" for expandido.

**Somatória utilizando Ordem:** as linhas no DRE possuem um código único chamado de ordem. Para somar os valores dessas linhas, coloca-se a ordem da linha entre colchetes []. Não é possível utilizar esse recurso com linhas de detalhamento. Por exemplo, se a linha de ordem 0 tem a fórmula “1%” e a linha de ordem 2 tem a fórmula “2%”, para somar as contas iniciadas com 1 e 2, usa-se a fórmula [0]+[2]. A interação drill não está disponível para linhas do relatório que utilizam essa fórmula.

**Negrito:** define o texto da linha em negrito.

**Alinhamento:** altera o alinhamento da linha (esquerda, centro, direita).

**Cor de Fundo:** define a cor de fundo da linha. Para linhas do tipo agrupador, apenas o agrupador será colorido; para linhas de detalhamento, todas as cores de fundo do detalhamento serão alteradas.

**Cor do Texto:** define a cor do texto da linha. Para linhas do tipo agrupador, apenas o texto do agrupador será colorido; para linhas de detalhamento, todas as cores de texto do detalhamento serão alteradas.

**Elemento Pai:** permite associar uma linha a outra utilizando a descrição de outra coluna como referência. Muito utilizado para criar relatórios com múltiplos níveis de abertura e para associar linhas de detalhamento com seus respectivos agrupadores.

**Ordem:** define a ordem das linhas no relatório final e pode ser usada para criar linhas de somatória utilizando a ordem. Não é possível ter duas linhas com a mesma ordem.

**Esconder:** permite ocultar a linha no relatório final.

**Ações:**

- **Mover para cima:** altera a ordem da linha para -1 no valor da ordem, além de reordenar as demais linhas.
- **Mover para baixo:** altera a ordem da linha para +1 no valor da ordem, além de reordenar as demais linhas.
- **Adicionar acima:** cria uma nova linha imediatamente acima da linha selecionada, reordenando o restante das linhas.
- **Adicionar abaixo:** cria uma nova linha imediatamente abaixo da linha selecionada, reordenando o restante das linhas.
- **Duplicar:** cria uma linha idêntica à selecionada imediatamente abaixo dela.
- **Configurações da Linha:** permite definir prefixo, sufixo e quantidade de casas decimais para a linha.
- **Deletar item:** exclui permanentemente a linha selecionada.

**Filtros:** permite adicionar filtros adicionais para a linha, complementando ou especificando mais o filtro da fórmula.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=4uBinixDvkg)

Após fazer todas as configurações citadas acima, salve o relatório com as configurações desejadas e verifique na tela o resultado.

Para editar os relatórios, basta voltar na **"Configuração"** da View da tabela, ir em componentes e, em vez de adicionar um novo template, localizar o desejado e clicar no ícone de lápis. Isso abrirá a tela de configuração do template novamente para fazer as alterações pertinentes.

Para duplicar os relatórios, basta voltar na Configuração da View da tabela, ir em componentes e, em vez de adicionar um novo template, localizar o desejado e clicar no ícone de duplicar. Isso abrirá uma tela para nomear o novo template e em seguida, abrirá a tela de configuração do template para fazer as alterações pertinentes.

### Exemplos de Relatórios

#### Exemplo de Relatório utilizando apenas "%" e "\*"

**Nome do Template:** exemplo básico.

![Imagem 1: Nome do Template: exemplo básico.](https://ajuda.sankhya.com.br/hc/article_attachments/28081031144087)

Neste exemplo, as linhas de agrupadores **"Receitas"** e **"Despesas"** são representadas com **"%"**, e as linhas de detalhamento são representadas com **"\*"**.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=tHZjPIZRU_o)

#### Exemplo de Relatório utilizando outros tipos de linhas e seleções

**Nome do Template:** exemplo avançado.

![Imagem 2: Nome do Template: exemplo avançado.](https://ajuda.sankhya.com.br/hc/article_attachments/28081059110295)

Neste exemplo, além das linhas de agrupadores e detalhamento, foram utilizadas configurações adicionais como cores de fundo e texto, além de linhas de somatória utilizando a ordem, para criar um relatório mais detalhado e customizado.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=uhNenPcvjhk)

---

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157259225623) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
