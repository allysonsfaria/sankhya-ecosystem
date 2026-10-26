---
id: "42427428121879"
titulo: "Gerador de Modelos de Documento com IA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427428121879-Gerador-de-Modelos-de-Documento-com-IA"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-11T16:14:56Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14433769", "sync_hash_1433fb9cd12f"]
---

# Gerador de Modelos de Documento com IA

## 1) Sobre o Gerador de Modelos de Documento com IA

O **Gerador de Modelos de Documento com IA** é uma funcionalidade que permite criar e editar o layout HTML de modelos de documento diretamente a partir de uma conversa com inteligência artificial. Em vez de construir o HTML do zero, você pode enviar um arquivo de referência (como um PDF ou word da sua proposta atual), descrever o que deseja, ou combinar os dois e a IA gera o layout pronto para uso no Ploomes.

Você envia suas instruções e/ou arquivos, visualiza o resultado, solicita ajustes e, quando estiver satisfeito, aplica o layout no modelo de documento. Além disso, a IA também é capaz de identificar campos da conta e de criar campos dinâmicos automaticamente a partir do conteúdo do seu arquivo, agilizando a montagem completa do modelo.

**Tipos de modelo compatíveis:** Proposta, Venda, Documento de Cliente e Documento de Negócio.

---

## 2) Pré-requisitos

- Ter o **módulo de Automação de Propostas e Documentos** contratado.
- Ser **administrador** da conta Ploomes.
- Acessar a área de **Administração → Modelos de Documento**.

---

## 3) Utilizando o Gerador de Modelos de Documento com IA

## 3.1) Criando um modelo com IA

Para iniciar a criação de um modelo com IA, siga os passos abaixo:

**a) Acesse o editor de modelos**

Vá até **Administração → Modelos de Documento** e crie um novo modelo (Proposta, Venda, Documento de Cliente ou Documento de Negócio). A tela do editor será aberta em branco.

[GIF animado: Imagem 1: Vá até Administração → Modelos de Documento e crie um novo modelo (Proposta, Venda, Documento de Cliente ou Documento…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231019818/82e48d15239d7ec4a3e7236e843b/1.gif?expires=1786536000&signature=f04e2426e3a5279797795c0186a01a5d3327a1523336abc33eef773833fb6d33&req=diIkF8l%2FlIleUfMW3nq%2BgTvq632okrScfkLVogYrds9OXt5VPqRKHvUUYm7S%0AQw2HkMXFw4bM3wMCbaAfCQtAfXo%3D%0A)

**b) Abra o chat com IA**

Clique na ação de geração com IA disponível na tela do editor. Um modal no formato de chat será aberto.

![Imagem 2: Clique na ação de geração com IA disponível na tela do editor. Um modal no formato de chat será aberto.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231021516/b0911dff7075b1cb077dabc95906/image+%2846%29.png?expires=1786536000&signature=ef1cc1c20f77ed0b13daf379d8f8aed96d2da2957cd93fd9dd11a6e823c905c9&req=diIkF8l8nIReX%2FMW3nq%2BgayrjKgNtHgVGE3TEf9CjxU3kGiy8mh87PlJnvim%0Aq0U5w96OcnpRdDlV%2ByTVWJ6kAQc%3D%0A)

**c) Envie sua solicitação**

Dentro do chat, você tem três formas de iniciar a geração:

- **Apenas anexo(s):** Anexe um ou mais arquivos de referência sem escrever nenhuma instrução. A IA vai gerar o layout buscando reproduzir o visual e a estrutura do(s) arquivo(s) com a maior fidelidade possível.
- **Apenas descrição textual:** Descreva o layout que deseja (ex.: "Crie uma proposta comercial com cabeçalho azul, logo à esquerda, tabela de produtos e rodapé com dados da empresa"). A IA gera o HTML com base na sua descrição.
- **Anexo(s) + descrição:** Combine os dois. Envie arquivos de referência e adicione instruções específicas para orientar a geração.

**Importante:** Não é possível enviar uma solicitação vazia. É obrigatório incluir pelo menos um anexo ou uma descrição textual.

**Formatos de anexo suportados:** PDF, PowerPoint (.pptx), Word (.docx), Excel (.xlsm), Texto (.txt), CSV (.csv), PNG e JPEG.

**Formatos não suportados:** Vídeo, áudio e GIF.

![Imagem 3: Formatos não suportados: Vídeo, áudio e GIF.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231045348/d5fd9dc809617f01d0f8b307fa83/image.png?expires=1786536000&signature=11f6fe2242c54967631bf63e4b2b33320cc360d31fffa893196d41ff7943d995&req=diIkF8l6mIJbUfMW3nq%2Bgexvn0jWA5lCz2HxcMYVTbmC5ISptRZprXd%2FcX9u%0AyCipbyxn4iYIPWUFxKPbLtoHo2I%3D%0A)

**d) Aguarde o processamento**

Após enviar a solicitação, a IA iniciará a geração do layout. Um indicador de carregamento será exibido enquanto o processamento estiver em andamento.

![Imagem 4: Após enviar a solicitação, a IA iniciará a geração do layout. Um indicador de carregamento será exibido enquanto o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231111050/aca3e688c07e35f9e65195782684/image.png?expires=1786536000&signature=9dd9786b3c6c2882858acff1f34f5d298615ceebf6c542c9291f6569851d3121&req=diIkF8h%2FnIFaWfMW3nq%2BgVph87tGd8hks7wksyqUylppQjTtMZ5zEGEmmGO8%0AzQHw6TzTZjOjO5likz0hoREX%2FYM%3D%0A)

**e) Visualize o resultado**

Quando a geração for concluída, você poderá visualizar o resultado de duas formas, alternando entre elas:

- **Preview visual:** Mostra como o documento ficará visualmente.
- **Código HTML:** Exibe o código HTML gerado pela IA.

Nessa etapa, o resultado é apenas uma visualização. Nenhuma alteração é aplicada ao modelo até que você confirme.

[GIF animado: Imagem 5: Nessa etapa, o resultado é apenas uma visualização. Nenhuma alteração é aplicada ao modelo até que você confirme.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231165767/985e36230c9bc30fda75a50520ad/4.gif?expires=1786536000&signature=af4c52192ce58ddfc0bd67a8e571d50aad3414aef3d2c0facad9266f94bc517d&req=diIkF8h4mIZZXvMW3nq%2BgZ%2FMuOxCGq4hh0YTrv5m5e8sdkzMvvC8eAUXyiBX%0AozD7eMrBAhXXaEsZNlfOKbuI%2BI8%3D%0A)

**f) Aplique o resultado**

Se estiver satisfeito com o resultado, clique em **"Confirmar visual do documento"**. O HTML gerado será inserido no editor do modelo de documento como uma seção.

**Observação:** Cada geração cria uma única seção no modelo. Se você precisar de múltiplas seções, será necessário gerar cada uma separadamente.

![Imagem 6: Observação: Cada geração cria uma única seção no modelo. Se você precisar de múltiplas seções, será necessário gerar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231244531/9a40300726abeb23d2163fd50d4d/image.png?expires=1786536000&signature=9fdb94b975c27eeb95e3be6ab5f5ea30bf05d8968768e59b191dc3384b9f77ce&req=diIkF8t6mYRcWPMW3nq%2BgfTToPNDRXzm1MA3mgZAW3n7ieCBNzz%2FXAi2HHWv%0ATfTjU1FB2ICgX%2F%2FWt%2FC591G9Z9w%3D%0A)

---

## 3.2) Solicitando alterações e navegando entre versões

Se o resultado da geração não atender às suas expectativas, você pode solicitar ajustes sem precisar começar do zero.

**a) Solicitar alterações**

Na tela de preview, escolha a opção **"Solicitar alterações"** e envie uma nova instrução descrevendo o que deseja mudar. Você pode incluir novos anexos, se necessário.

A IA vai gerar uma nova versão do layout aplicando as alterações solicitadas sobre o HTML atual. É importante destacar que a IA **não mantém um histórico da conversa**, ou seja, cada solicitação de alteração considera apenas o HTML da versão atual e a nova instrução enviada.

**Dica de boas práticas:** Seja específico na sua solicitação de alteração. Em vez de "melhore o layout", prefira instruções como "aumente o espaçamento entre o cabeçalho e o corpo do texto" ou "mude a cor do fundo do cabeçalho para azul escuro".

[GIF animado: Imagem 7: Dica de boas práticas: Seja específico na sua solicitação de alteração. Em vez de "melhore o layout", prefira…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231257213/490033a4da74ea99a8fe545871d9/6.gif?expires=1786536000&signature=dc5eeaa88e2b756cd0a65cd87f491cea7b560b38ee6a10fa4fba159990d7a4c1&req=diIkF8t7moNeWvMW3nq%2BgWOIM1qiurZMJIy%2BA2AOvL%2BjFoq7%2F8AKBgBDbCeP%0AR%2F8VTP4LRuJ7cDtzie%2B4tYp7uHo%3D%0A)

**b) Navegar entre versões**

Quando houver múltiplas versões geradas, você pode navegar entre elas (voltar para a anterior ou avançar para a mais recente) e comparar os resultados. Ao decidir, escolha a versão desejada e clique em **"Confirmar identidade visual do documento"** para aplicá-la.

[GIF animado: Imagem 8: Quando houver múltiplas versões geradas, você pode navegar entre elas (voltar para a anterior ou avançar para a mais…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231267560/d151b93225f1fbb5ab83a2e1f995/7.gif?expires=1786536000&signature=a3bf572a08edc7f537736cac8492b80e068eed2c7fa6e16aceef52848dd1daef&req=diIkF8t4moRZWfMW3nq%2BgSfjG7bjQt2zxEnEaZQLC3v%2FT0ATEXFyag%2B62YqC%0AH7V9AnlQSuA9neKqLAGdslALEmI%3D%0A)

---

## 3.3) Editando uma seção existente com IA

A IA não serve apenas para criar modelos do zero. Você também pode utilizá-la para editar seções já existentes em qualquer modelo de documento, **inclusive seções que não foram criadas originalmente por IA**.

**Como editar:**

1. Abra o modelo de documento que contém a seção que deseja editar.
2. Selecione a opção de editar a seção com IA.
3. No modal de chat, envie sua solicitação descrevendo as alterações desejadas (com ou sem anexos de apoio).
4. A IA vai gerar uma nova versão da seção, alterando **apenas o que foi solicitado** e preservando todo o restante do layout e conteúdo.

**Princípio de mínima alteração:** a orientação para a IA é tratar o HTML existente como base e modificar somente os pontos que indicados pelo usuário. O direcionamento é não "melhorar", "modernizar" ou reinterpretar partes que não foram mencionadas na solicitação.

[GIF animado: Imagem 9: Princípio de mínima alteração: a orientação para a IA é tratar o HTML existente como base e modificar somente os pontos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231283999/632284ad279226540af9f5859479/8.gif?expires=1786536000&signature=a0a81ccd113b82aeb9403d7417bcab927be647e2b208467712877ded789015f6&req=diIkF8t2nohWUPMW3nq%2Bge0RBwLzemPUpVgO3v2ukDh57QIBjINeGQvfPRvw%0Av9GwF5heazAhUPhJPwfvy6Bw35k%3D%0A)

---

## 3.4) Identificação e criação de campos com IA

Além de gerar o layout, a IA pode identificar e criar campos dinâmicos automaticamente no seu modelo de documento. A IA analisa o conteúdo do arquivo enviado, interpreta o contexto de cada trecho e sugere quais campos devem ser criados, a qual entidade pertencem e qual o tipo de dado adequado. Isso é feito de forma automática, sem necessidade de marcações prévias no arquivo.

**Importante:** A identificação de campos acontece durante a **primeira geração** (no envio inicial do arquivo e/ou descrição). Ao solicitar alterações posteriormente, o fluxo é voltado exclusivamente para ajustes de layout. Ou seja, não é possível solicitar a identificação de campos nessa etapa pelo comando para a IA.

## Como funciona o fluxo de campos

**a)** Ao enviar o arquivo de referência no chat com IA (na criação do modelo), a IA analisa automaticamente o conteúdo e identifica valores dinâmicos com base no contexto (ex.: nomes, datas, valores monetários, CPF, CNPJ). Além de propor novos campos, a IA também busca associar os valores encontrados a **campos já existentes na sua conta**, aumentando o reaproveitamento e evitando duplicidades.

Para cada campo identificado, a IA propõe:

- **Nome do campo** (ex.: "Nome do Cliente")
- **Entidade** a qual o campo pertence (ex.: Cliente, Negócio, Proposta)
- **Tipo do campo** (ex.: Texto simples, Moeda, Data, CPF, CNPJ)
- **Associação com campo existente**, quando houver correspondência com um campo já cadastrado na conta

Se a IA encontrar um campo existente compatível, ela sugere a associação automaticamente. Caso contrário, o campo será proposto como novo para pré-criação. Você pode revisar e ajustar todas as sugestões na tela de confirmação.

![Imagem 10: Se a IA encontrar um campo existente compatível, ela sugere a associação automaticamente. Caso contrário, o campo será…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231463090/ae7b3bae564a630616f11e2a93a1/image.png?expires=1786536000&signature=c7b085b498547332dd5834963cc037247adbbc78a7983bf7347a0239f7720303&req=diIkF814noFWWfMW3nq%2BgYmiIXJrCBaNgg7PaCnODMb2Uq5bXksOtczZhVjH%0Amu%2BzVAcItACKZ9L60UtLAnG4T2I%3D%0A)

**Como aumentar a taxa de acerto da IA:** A identificação automática já possui uma alta taxa de acerto, mas você pode aumentar ainda mais a precisão direcionando a IA. Algumas formas de fazer isso:

- **Grifo no documento:** Destaque (grife) os valores que deseja que sejam campos dinâmicos no arquivo antes de enviá-lo.
- **Instruções no chat:** Escreva no campo de texto quais campos você espera que sejam criados (ex.: "Identifique os campos de nome do cliente, CNPJ, valor total e data de vencimento").
- **Marcações no arquivo:** Se preferir, insira marcações no próprio documento (ex.: usando `#NomeDoCliente` ou formatação em negrito) para sinalizar os pontos desejados.

Essas orientações devem ser fornecidas no **primeiro envio** (na criação), pois a etapa de solicitação de alterações é exclusiva para ajustes de layout.

**b) Revise e ajuste os campos**

Na tela de confirmação, você pode:

- **Alterar a entidade** do campo (ex.: mudar de "Cliente" para "Negócio").
- **Alterar o tipo** do campo (ex.: mudar de "Texto simples" para "Moeda").
- **Excluir** um campo da lista (caso não deseje criá-lo).
- **Alterar o campo por algum existente na conta**
- **Alterar o campo por um novo campo** (criação rápida de campos)

[GIF animado: Imagem 11: Alterar o campo por um novo campo (criação rápida de campos)](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2231466387/e716235931d475f1ab9cf6ae2e34/9.gif?expires=1786536000&signature=29aa03364ab71ab3b5816fc46dae008d8aab07feb0d8c5cb3fddb4368571ea0a&req=diIkF814m4JXXvMW3nq%2BgacKsN0t5opwRKoqdE6q63wVrq6IoiEeC8UUSwyR%0AdHB91SPhRC9RrwYUZOlNlPJd%2BBQ%3D%0A)

**c) Confirme a criação**

Após revisar a lista, confirme a criação dos campos. O sistema exibirá um indicador de carregamento enquanto os campos são criados e carregados no contexto do modelo.

Ao concluir:

- O HTML escolhido será inserido no modelo.
- Os campos identificados e criados serão posicionados automaticamente nos locais definidos pela IA no documento.
- Você receberá um aviso de sucesso confirmando que o modelo está pronto.

**Observação:** Os campos são criados apenas como pré-cadastro (vazios). A configuração completa de cada campo (como opções de preenchimento, obrigatoriedade e outras propriedades) deve ser feita posteriormente nas configurações de campos do Ploomes.

## Entidades disponíveis para campos

Os campos criados pela IA podem pertencer às seguintes entidades:

| **Entidade** |
| --- |
| Cliente |
| Negócio |
| Proposta |
| Bloco |
| Produto da Proposta |
| Vínculo de Produto da Proposta |
| Sua Empresa |
| Venda |
| Produto da Venda |
| Vínculo de Produto da Venda |
| Documento |
| Produto do Documento |
| Vínculo de Produto do Documento |

---

## 3.5) Tabelas e Tabela de Produtos

A IA é capaz de gerar tabelas dentro do layout HTML, tanto tabelas convencionais (com dados estáticos) quanto a **Tabela de Produtos**, que é um dos elementos mais importantes dos modelos de documento no Ploomes.

**Tabelas convencionais**

Se o seu arquivo de referência contém tabelas (ex.: tabela de condições de pagamento, cronograma, escopo de serviços), a IA vai reproduzi-las no HTML mantendo a estrutura original — colunas, linhas, bordas e alinhamentos.

**Tabela de Produtos**

Quando o documento envolve uma lista de produtos ou serviços, a IA gera automaticamente uma **tabela dinâmica de produtos**. Diferente das tabelas convencionais, a tabela de produtos utiliza um **conjunto fixo de campos dinâmicos definidos pelo Ploomes**, que são preenchidos automaticamente no momento da geração do documento final.

Os campos dinâmicos disponíveis para a tabela de produtos são:

| Coluna | Campo dinâmico | Descrição |
| --- | --- | --- |
| Item | Índice do produto | Número sequencial do item na lista |
| Nome | Nome do produto | Nome do produto vinculado à proposta |
| Quantidade | Quantidade | Quantidade do produto naquela linha |
| Valor Unitário | Valor unitário | Preço por unidade do produto |
| Total | Total do item | Valor total da linha (quantidade × valor unitário) |

Ao final da tabela, é exibida uma linha de **Total geral** que soma automaticamente os valores de todos os itens do bloco.

**Como a IA monta essa tabela:** A IA identifica que o documento contém uma tabela de produtos e aplica os campos dinâmicos do padrão Ploomes listados acima. A **ordem das colunas segue o documento original** enviado como referência, ou seja, a IA é direcionada para usar a disposição que você já utiliza, sem forçar uma sequência fixa. O visual da tabela (cores, bordas, alinhamentos) também é adaptado ao layout do seu arquivo.

Se o documento original tiver menos colunas do que o padrão, a IA remove as colunas ausentes. Se tiver colunas a mais (ex.: uma coluna de "Desconto" ou "Observação"), a IA adiciona essas colunas extras com texto estático, pois somente os campos listados acima possuem preenchimento automático.

---

## 4) Boas práticas para usar o Gerador de Modelos com IA

Para obter os melhores resultados com a IA, siga estas recomendações:

## 4.1) Seja claro e direcionado nas suas instruções

Quanto mais específico for o seu pedido, melhor será o resultado. Em vez de simplesmente anexar um arquivo sem nenhuma descrição, aproveite o campo de texto para direcionar a IA.

**Exemplos de boas instruções:**

- "Crie uma proposta comercial com cabeçalho contendo logo à esquerda, nome da empresa à direita, tabela de produtos no corpo e rodapé com dados de contato."
- "Reproduza o layout desse PDF, mas troque a cor do cabeçalho para azul escuro e aumente o espaçamento entre as seções."
- "Use este documento como referência, mas remova a segunda tabela e mantenha apenas a tabela de produtos."

**Exemplos de instruções pouco eficientes:**

- "Faça uma proposta bonita." (muito vago)
- "Melhore isso." (sem direcionamento)

## 4.2) Atenção à complexidade do documento

O Gerador de Modelos com IA é projetado para documentos cujos layouts possam ser reproduzidos em HTML — como propostas comerciais, contratos, ordens de serviço e documentos corporativos. Documentos com layouts extremamente complexos (ex.: materiais gráficos com sobreposições de elementos, diagramas elaborados ou formatações muito específicas de softwares de design) podem não ser fielmente reproduzidos pela IA.

**Recomendações:**

- Prefira enviar documentos com estrutura clara: cabeçalho, corpo de texto, tabelas e rodapé.
- Se o seu documento original é muito complexo, considere simplificá-lo antes de enviar ou divida-o em partes menores, gerando uma seção por vez.
- Lembre-se de que o HTML gerado precisa ser compatível com a conversão para PDF do Ploomes, o que impõe algumas restrições visuais (sem sombras, bordas arredondadas, animações ou fontes externas).

## 4.3) Envie arquivos enxutos e objetivos

A qualidade e a velocidade da geração estão diretamente ligadas à quantidade de conteúdo que a IA precisa interpretar. Cada geração com IA cria uma única seção do modelo, então o ideal é que o arquivo de referência reflita exatamente isso. Envie apenas a parte do documento que corresponde à seção que você quer gerar.

Na prática, isso significa que um arquivo PDF de uma ou duas páginas é o cenário ideal. Enviar um documento de dez páginas, por exemplo, além de não trazer benefício (já que o resultado será uma única seção), tende a piorar a qualidade do layout gerado, aumentar significativamente o tempo de processamento e consumir mais tokens da conta.

**A mesma lógica vale para múltiplos arquivos:** quanto mais arquivos e mais pesados eles forem, mais lenta será a resposta da IA. Se o seu modelo final terá várias seções, a melhor abordagem é separar o material por seção e gerar cada uma individualmente, com um arquivo de referência enxuto por vez.

## 4.4) Direcione a identificação de campos

Embora a IA identifique campos dinâmicos automaticamente com alta taxa de acerto, você pode aumentar a precisão fornecendo orientações no primeiro envio:

- **Grife os valores** no documento antes de enviá-lo.
- **Escreva no chat** quais campos espera encontrar (ex.: "Os campos desse documento são: nome do cliente, CNPJ, valor total e prazo de entrega").
- **Insira marcações no arquivo** (ex.: `#NomeDoCliente`) para facilitar a identificação.

Lembre-se: essas orientações devem ser enviadas junto com o primeiro prompt de criação. A etapa de "solicitar alterações" é exclusiva para ajustes de layout.

## 4.5) Use arquivos menores para cada seção

Como cada geração com IA cria uma única seção, o ideal é enviar um arquivo de referência que represente apenas aquela parte do modelo. Na prática, arquivos de **uma a duas páginas são o cenário recomendado**.

Essa abordagem traz vários benefícios: a IA entrega resultados com maior qualidade quando trabalha com arquivos enxutos, o tempo de processamento é menor e o consumo de tokens é mais eficiente.

Além disso, ao acertar o resultado logo nas primeiras tentativas, você evita múltiplas rodadas de ajuste, o que economiza ainda mais tokens.

De quebra, o seu modelo de documento fica mais organizado dentro do Ploomes, com seções bem definidas e leves.

---

## 5) Limitações do Gerador de Modelos de Documento com IA

- **Uma seção por geração:** Cada uso do gerador cria uma única seção. Para modelos com múltiplas seções, é necessário gerar cada seção separadamente.
- **Imagens como placeholders:** Imagens presentes no arquivo de entrada são inseridas no HTML como uma estrutura padrão (placeholder) para que você substitua posteriormente pela imagem definitiva. A IA não importa as imagens originais como assets finais.
- **Sem histórico de conversa:** Ao solicitar alterações, a IA não armazena as mensagens anteriores. Ela considera apenas o HTML atual e a nova instrução. Por isso, seja claro e completo em cada solicitação de ajuste.
- **Formatos não suportados:** Vídeo, áudio e GIF não são aceitos como anexo.
- **Campos na tela de confirmação:** Não é possível adicionar campos novos na tela de confirmação da IA. Caso a IA não identifique algum campo marcado, ele deverá ser inserido manualmente no editor do modelo. É possível criar campos pela criação rápida de campos, mas apenas onde a IA marcar e definir que existe um campo.
- **Tamanho dos arquivos e consumo de tokens:** Não há um limite rígido de tamanho de arquivo, porém, quanto maior o arquivo enviado, mais tempo a IA levará para processar e mais tokens da conta serão consumidos. Arquivos muito grandes podem esgotar os tokens disponíveis.
- **Compatibilidade visual:** O HTML gerado segue as regras de compatibilidade do Ploomes, o que significa que alguns recursos visuais avançados (como sombras, bordas arredondadas, animações e fontes externas) não são suportados. Isso garante que o documento seja convertido corretamente para PDF.
- **Sem regras de exibição condicional:** O Gerador de Modelos com IA não suporta a criação de regras de exibição condicional (ex.: mostrar ou ocultar um bloco dependendo de um valor de campo). Caso precise dessa lógica, ela deve ser configurada manualmente após a geração.
- **Fórmulas não são aplicadas aos campos:** Os campos criados pela IA não possuem fórmulas ou cálculos automáticos. Se o seu modelo depende de campos calculados, as fórmulas devem ser configuradas manualmente nas propriedades do campo após a criação.
- **Campos são criados vazios (pré-cadastro):** A IA cria os campos apenas como pré-cadastro, posicionando-os nos locais corretos do documento. A configuração completa de cada campo (como opções de preenchimento, obrigatoriedade, valores padrão e outras propriedades) deve ser feita posteriormente nas configurações de campos do Ploomes.

---

## 6) F.A.Q.

1. **Posso editar um modelo que não foi criado por IA?**

   1. Sim. A edição com IA funciona em qualquer seção existente do modelo, independentemente de ter sido criada manualmente ou pela IA.
2. **O que acontece se a IA não identificar um campo no meu documento?**

   1. A identificação é automática e baseada em contexto, mas pode não captar todos os campos. Se algum campo não foi reconhecido, você poderá inseri-lo manualmente no editor do modelo de documento após a criação. Para aumentar o acerto, direcione a IA no primeiro envio: grife os valores no arquivo, escreva quais campos espera ou insira marcações no documento.
3. **Posso gerar várias seções de uma vez?**

   1. Não. Cada geração com IA cria uma única seção. Se o seu modelo precisa de múltiplas seções, gere cada uma separadamente.
4. **A IA mantém o histórico das minhas mensagens anteriores?**

   1. Não. A cada solicitação de alteração, a IA considera apenas o HTML da versão atual e a nova instrução. Mensagens anteriores não são enviadas. Por isso, sempre inclua todas as informações relevantes na sua solicitação.
5. **Posso usar a IA apenas para gerar o layout, sem criar campos?**

   1. Sim. A etapa de identificação e criação de campos é parte do fluxo, mas você pode utilizar a IA apenas para gerar ou editar o layout HTML e gerenciar os campos de forma manual posteriormente.
6. **As imagens do meu arquivo serão reproduzidas automaticamente no modelo?**

   1. Não. A IA insere placeholders nos locais onde havia imagens no arquivo original. Você deve substituir esses placeholders pelas imagens definitivas diretamente no editor do modelo.
7. **E se ocorrer um erro durante a geração ou criação de campos?**

   1. O sistema exibirá uma mensagem de erro explícita. Nenhuma alteração será aplicada automaticamente ao modelo em caso de falha, garantindo que nada seja perdido ou sobrescrito indevidamente.
8. **Quais tipos de modelo posso criar com a IA?**

   1. A feature está disponível para os quatro tipos de modelo de documento: Proposta, Venda, Documento de Cliente e Documento de Negócio.
9. **Arquivos muito grandes podem causar problemas?**

   1. Embora não haja um limite rígido, arquivos grandes consomem mais tokens da conta e exigem mais tempo de processamento. É recomendável utilizar arquivos objetivos e bem estruturados para obter resultados mais rápidos e eficientes.
10. **Os campos criados pela IA já vêm configurados?**

    1. Não. Os campos são criados apenas como pré-cadastro (vazios e posicionados no documento). A configuração completa — como opções de preenchimento, obrigatoriedade, valores padrão e fórmulas — deve ser feita manualmente nas configurações de campos do Ploomes.
11. **Posso usar regras de exibição condicional com o Gerador de Modelos com IA?**

    1. Não. A IA não cria regras de exibição condicional. Caso precise de lógica condicional (ex.: mostrar ou ocultar blocos dependendo de um valor), essa configuração deve ser feita manualmente após a geração.
12. **Consigo pedir para a IA identificar campos ao solicitar alterações de layout?**

    1. Não. A identificação de campos acontece exclusivamente no primeiro envio (criação). A etapa de "solicitar alterações" é dedicada apenas a ajustes de layout.

---

## Glossário

| Termo | Definição |
| --- | --- |
| **Modelo de Documento** | Template configurável na Administração do Ploomes usado para gerar propostas, contratos e outros documentos com dados dinâmicos. |
| **Seção** | Bloco de conteúdo dentro de um modelo de documento. Cada geração com IA cria uma única seção. |
| **Campo dinâmico** | Elemento dentro do modelo que é preenchido automaticamente pelo Ploomes com dados reais no momento da geração do documento (ex.: nome do cliente, valor total). |
| **Entidade** | Categoria de dados à qual um campo pertence (ex.: Cliente, Negócio, Proposta). Define de onde o Ploomes vai buscar o valor do campo. |
| **Preview** | Visualização prévia do layout gerado pela IA, antes de ser aplicado ao modelo de documento. |
| **Tabela de Produtos** | Tabela dinâmica especial que lista automaticamente os produtos ou serviços vinculados a uma proposta, venda ou documento, com campos como nome, quantidade, valor unitário e total. |
| **Tokens** | Unidades de processamento consumidas pela IA a cada interação. Arquivos maiores e solicitações mais complexas consomem mais tokens. |
| **HTML** | Linguagem de marcação usada para estruturar o layout dos modelos de documento no Ploomes. |
| **Placeholder** | Elemento temporário inserido no lugar de uma imagem ou conteúdo que deve ser substituído manualmente pelo usuário. |
| **Seção** | Bloco independente de conteúdo dentro de um modelo de documento. Cada seção abarca uma parte do modelo e pode conter mais de uma página. A quebra de página acontece automaticamente. É recomendável manter poucas páginas por seção para que o modelo fique mais leve e organizado. Cada geração com IA cria uma única seção. |

---

## Artigos relacionados

- [https://suporte.ploomes.com/pt-BR/collections/3067337-propostas-e-documentos](https://sankhya.zendesk.com/hc/pt-br/sections/42427433105687)
