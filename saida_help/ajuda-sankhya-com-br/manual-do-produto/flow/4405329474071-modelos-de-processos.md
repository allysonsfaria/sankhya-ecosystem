---
id: "4405329474071"
titulo: "Modelos de Processos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:57Z"
rotulos: ["Configuração", "Processos", "Modelos", "sankhyaflow", "modelos de processos", "Cadastro", "Modelos de Processos: Utilizados como base", "Exemplos de Modelos: Compras produto cliente", "Cadastro e Importação: Baseada em modelo"]
---

# Modelos de Processos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313320007191) Versão disponível: a partir da 4.6
```

---

Os Modelos de Processos são processos prontos que o modelador pode utilizar como base para construção de um determinado processo da empresa; por exemplo, a empresa MS Agro utilizou o modelo de **"Solicitação de Compras"** para implantar; dessa forma, adaptou o processo conforme a sua necessidade, inserindo uma nova tarefa para os casos onde é necessário refazer a Solicitação de Compras.

Esses modelos também são utilizados como exemplos didáticos no contexto de configurações avançadas, para tarefas de serviços, expressões de gateways, tarefas de e-mail e etc, além de serem modelos das melhores práticas em alguns contextos de processos.

Em nosso caso de uso, temos o Paulo. Ele é o analista responsável pela implantação de processos em uma empresa do segmento de vendas de materiais de construção. Paulo precisa implantar o processo de compras na sua empresa e, para isso, utilizou o recurso de cadastrar um processo com base no modelo Solicitação de Compras.

No decorrer dessa documentação, trataremos sobre o [Cadastro de Processos com base em um Modelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#cadastrodeprocessoscombaseemummodelo) e os [Modelos de Processos Disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#modelosdeprocessosdispon%C3%ADveis).

---

#### Cadastro de Processos com base em um Modelo

Para fazer o cadastro de processo com base em um modelo, Paulo deve acessar a tela [Processos de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio), clicar na seta do botão ![Imagem 2: Para fazer o cadastro de processo com base em um modelo, Paulo deve acessar a tela Processos de Negócios , clicar na…](https://ajuda.sankhya.com.br/hc/article_attachments/4405318724247) **"Cadastrar Processo de Negócio"** e escolher a opção **"Com base em modelo"**. Assim, serão apresentados os modelos de processos disponíveis:

[GIF animado: Imagem 3: Para fazer o cadastro de processo com base em um modelo, Paulo deve acessar a tela Processos de Negócios , clicar na…](https://ajuda.sankhya.com.br/hc/article_attachments/4405329768727)

| **Cadastro de Processo com base em um Modelo** |
| --- |

Ao clicar em um modelo de processo, serão apresentadas as informações que caracterizam o processo:

- **Contextualização:** Nesse tópico é exibida uma descrição sobre o que vem a ser o processo.
- **Detalhes do processo:** Aqui serão detalhadas todas as tarefas de usuário/serviço que contemplam o processo e a função de cada uma delas.
- **Conteúdo:** Nessa seção será apresentado o conteúdo a ser importado (diagrama, formulários, eventos, etc).
- **Informações adicionais:** Essa seção traz informações que o modelador deve atualizar no processo para que o mesmo funcione conforme os dados de sua empresa, como por exemplo, scripts, eventos, etc, além de outras informações relevantes sobre o processo.

[GIF animado: Imagem 4: Informações adicionais: Essa seção traz informações que o modelador deve atualizar no processo para que o mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/4405319078039)

| **Informações do Modelo de Processos** |
| --- |

![Imagem 5: A data de publicação refere-se à última atualização do processo.](https://ajuda.sankhya.com.br/hc/article_attachments/16110928232087) A data de publicação refere-se à última atualização do processo.

Após clicar no modelo de processo de Solicitação de compras, para importá-lo na base, basta clicar no botão ![Imagem 6: Após clicar no modelo de processo de Solicitação de compras, para importá-lo na base, basta clicar no botão "Utilizar" :](https://ajuda.sankhya.com.br/hc/article_attachments/4405319154967) **"Utilizar"**:

[GIF animado: Imagem 7: Após clicar no modelo de processo de Solicitação de compras, para importá-lo na base, basta clicar no botão "Utilizar" :](https://ajuda.sankhya.com.br/hc/article_attachments/4405319206807)

| **Importação do Modelo de Processo** |
| --- |

Ao importar um Processo de Negócio, o sistema verifica os dados inseridos nesse processo com o cadastro do ERP (base Sankhya). Dessa forma, caso não exista uma equivalência com algum dos dados abaixo, deve ser selecionado um dado disponível na base:

- Grupo Processo;
- Contas SMTP;
- Artefatos (Módulo Java, Procedures, Triggers, Entidades adicionais, Relatórios Formatados).

Dando continuidade, após clicar no botão Utilizar, o sistema verificou que a conta SMTP utilizada no processo modelo não existe na base que está sendo importada; sendo assim, Paulo deverá selecionar uma conta SMTP substituta:

![Imagem 8: Dando continuidade, após clicar no botão Utilizar , o sistema verificou que a conta SMTP utilizada no processo modelo…](https://ajuda.sankhya.com.br/hc/article_attachments/4405336289687)

| **Análise de conflito Conta SMTP** |
| --- |

Como esse processo está sendo importado pela segunda vez nessa base, o módulo Java utilizado já havia sido cadastrado no banco de dados; dessa forma, Paulo deverá resolver se irá manter ou substituir esse módulo Java:

![Imagem 9: Como esse processo está sendo importado pela segunda vez nessa base, o módulo Java utilizado já havia sido cadastrado…](https://ajuda.sankhya.com.br/hc/article_attachments/4405330291991)

| **Análise de conflito Módulo Java** |
| --- |

Após resolver os conflitos e clicar em **"Concluir"**, o processo será importado na base:

[GIF animado: Imagem 10: Após resolver os conflitos e clicar em "Concluir" , o processo será importado na base:](https://ajuda.sankhya.com.br/hc/article_attachments/4405336475927)

| **Importação do Modelo de Processo** |
| --- |

Agora, deverão ser realizados os ajustes no processo conforme consta na seção de **"Informações Adicionais"**, além de inserir o Usuário/Grupo de usuário/Equipe (compartilhamento e candidatos), caso seja necessário.

![Imagem 11: Agora, deverão ser realizados os ajustes no processo conforme consta na seção de "Informações Adicionais" , além de…](https://ajuda.sankhya.com.br/hc/article_attachments/4405330424599)

| **Informações Adicionais do Processo** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#top)

#### Modelos de Processos Disponíveis

Nesse tópico trataremos sobre cada um dos processos disponíveis, sendo eles: [Solicitação de compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#solicita%C3%A7%C3%A3odecompras), [Cadastro de produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#cadastrodeproduto), [Cadastro de cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#cadastrodecliente), [Pedido de venda simplificado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#pedidodevendasimplificado) e [Adiantamento de viagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#adiantamentodeviagem).

---

**Solicitação de compras**

Esse modelo de processo realiza a solicitação e a geração do pedido de compras através do SankhyaFlow:

![Imagem 12: Esse modelo de processo realiza a solicitação e a geração do pedido de compras através do SankhyaFlow :](https://ajuda.sankhya.com.br/hc/article_attachments/4408101874583)

| **Processo Solicitação de compras** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#modelosdeprocessosdispon%C3%ADveis) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#top)

---

**Cadastro de produto**

Esse modelo permite realizarmos o cadastro de um novo produto a partir de um fluxo estruturado padronizado. A principal diferença entre esse modelo de cadastro e modelo tradicional já existente no ERP, é a quebra do trabalho em fases (tarefas), representando as contribuições que cada departamento da empresa possui para se chegar ao resultado final, que seria o produto cadastrado e disponível para uso pelas diversas áreas.

![Imagem 13: Esse modelo permite realizarmos o cadastro de um novo produto a partir de um fluxo estruturado padronizado. A principal…](https://ajuda.sankhya.com.br/hc/article_attachments/4408101841687)

| **Processo Cadastro de produto** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#modelosdeprocessosdispon%C3%ADveis) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#top)

---

**Cadastro de cliente**

O processo Cadastro de cliente permite realizar o cadastro de novos clientes a partir de um fluxo estruturado padronizado. A principal diferença entre esse modelo de cadastro e o modelo tradicional já existente no ERP é a quebra do trabalho em fases (tarefas), representando as contribuições que cada departamento da empresa possui para se chegar ao resultado final, que seria o cliente cadastrado e disponível para uso pelas diversas áreas.

![Imagem 14: O processo Cadastro de cliente permite realizar o cadastro de novos clientes a partir de um fluxo estruturado…](https://ajuda.sankhya.com.br/hc/article_attachments/4408090598039)

| **Processo Cadastro de cliente** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#modelosdeprocessosdispon%C3%ADveis) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#top)

---

**Pedido de venda simplificado**

Esse modelo de processo permite realizar o lançamento de pedidos de vendas a partir de uma abordagem simplificada, visto que o volume de dados que o vendedor (solicitante do processo) precisa informar durante a abertura do processo é mínima, tornando sua execução mais rápida que a abordagem tradicional (Central de Vendas).

![Imagem 15: Esse modelo de processo permite realizar o lançamento de pedidos de vendas a partir de uma abordagem simplificada,…](https://ajuda.sankhya.com.br/hc/article_attachments/4408090615319)

| **Processo Pedido de venda simplificado** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#modelosdeprocessosdispon%C3%ADveis) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#top)

---

**Adiantamento de viagem**

O processo de Adiantamento de viagem permite que um colaborador solicite um adiantamento em R$ de viagem ao seu líder imediato. Após as solicitações serem aprovadas, elas são direcionadas ao solicitante (colaborador) para que ele detalhe as despesas geradas durante sua viagem.

Na sequência, a solicitação é remetida ao departamento financeiro para serem analisadas as despesas apontadas e, em seguida, são executadas tarefas de serviço de lançamento e compensação de títulos. Por fim, é enviado um e-mail para o solicitante do processo informando que o acerto de viagem foi finalizado e se existirá reembolso ou devolução do adiantamento.

![Imagem 16: Na sequência, a solicitação é remetida ao departamento financeiro para serem analisadas as despesas apontadas e, em…](https://ajuda.sankhya.com.br/hc/article_attachments/4408101962007)

| **Processo Adiantamento de viagem** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#modelosdeprocessosdispon%C3%ADveis) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405329474071-Modelos-de-Processos#top)
