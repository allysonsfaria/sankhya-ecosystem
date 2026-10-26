---
id: "360044602854"
titulo: "Suporte Produção por Terceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:52:57Z"
rotulos: ["Configuração", "Parceiro", "Ordem de Produção", "Terceiros", "Estoque", "Produção", "Suporte Produção por Terceiros", "Suporte Produção por Terceiros manual", "Implementação de Produção por Terceiros"]
---

# Suporte Produção por Terceiros

Existem cenários produtivos, onde terceiriza-se o processo de produção como um todo ou simplesmente algumas operações (atividades) dentro do processo produtivo. A execução por terceiros também é conhecida como beneficiamento, ou seja, um parceiro terceiro irá executar determinada operação de transformação, agregando valor ao produto e posteriormente, retorna este à indústria para que sejam executadas as operações de produção restantes.

Para esse tipo de execução de atividades do processo, é necessário a geração de documentos que formalizem tal execução e/ou acompanhamento no transporte dos materiais remetidos e retornados para transformação pelo parceiro terceiro.

Nesse artigo trataremos dos seguintes tópicos:

| [Configuração do Processo em Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#configura%C3%A7%C3%A3odoprocessoemterceiros) |  | [Lista de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#listadeterceiros) |
| --- | --- | --- |
| [Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#opera%C3%A7%C3%B5esdeestoque) |  | [Lançamento de Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#lan%C3%A7amentodeordemdeprodu%C3%A7%C3%A3o) |

## Configuração do Processo em Terceiros

Na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050884074-Processo-Produtivo), você pode especificar se as Ordens de Produção do processo em questão, utilizam ou não um parceiro terceiro. O campo **"Produção terceirizada"** é empregado nessa definição. As opções disponíveis são:

- **Sempre:** O Processo Produtivo sempre será executado por terceiros, ou seja, todas as Ordens de Produção criadas por esse processo contarão com a participação de terceiros.
- **Nunca:** As Ordens de Produção criadas para esse Processo Produtivo, nunca contarão a participação de terceiros.
- **Opcional:** As Ordens de Produção criadas por esse Processo Produtivo, podem ser terceirizadas eventualmente, ou seja, podem tanto ser realizadas internamente ou por terceiros. Essa definição irá ocorrer no momento do lançamento da ordem de produção.

Uma vez determinado que o Processo Produtivo pode ser executado por terceiros, será necessário definir como as Ordens de Produção serão terceirizadas; isso será feito por meio do campo **"Definição de Terceiro"**, de acordo com as seguintes opções:

- **Por OP:** Neste caso, o vínculo com o parceiro terceiro será feito com a Ordem de Produção, então todas as operações (atividades) marcadas como terceirizadas serão realizadas pelo mesmo parceiro naquela Ordem de Produção.
- **Por Operação:** Nesta situação, pode ter operações (atividades) sendo realizadas por parceiros diferentes na mesma Ordem de Produção, pois cada operação terceirizada possui vínculo com um parceiro terceiro diferente. Quando o processo possui essa opção selecionada, deverá existir ao menos uma atividade que seja executada em terceiros.

![Imagem 1: Por Operação: Nesta situação, pode ter operações (atividades) sendo realizadas por parceiros diferentes na mesma Ordem…](https://ajuda.sankhya.com.br/hc/article_attachments/4409523795479)

Quando o Processo Produtivo for terceirizado, será necessário definir se as operações (atividades) serão ou não executadas por parceiro terceiro. Esta configuração é feita por meio do botão **"Roteiro"**, clicando duas vezes sobre uma atividade, na aba **"Geral"**, onde você pode definir a **"Execução Terceirizada"** dentre as seguintes opções:

- **Nunca:** Escolhendo esta opção, a atividade nunca será executada por um terceiro, mesmo que a OP esteja com alguma forma de terceirização.
- **Sempre:** Por meio desta opção, a atividade sempre será executada por um terceiro. Apenas em Processos Produtivos que estejam configurados para utilizar terceiros, suportarão atividades com esse tipo de execução.
- **Opcional:** Selecionando esta opção, a atividade pode ou não ser executada por um terceiro. A escolha de fato acontecerá posteriormente; no momento do lançamento de uma OP para o processo em questão.

![Imagem 2: Opcional: Selecionando esta opção, a atividade pode ou não ser executada por um terceiro. A escolha de fato acontecerá…](https://ajuda.sankhya.com.br/hc/article_attachments/4409531622167)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#top)

## Lista de Terceiros

Realizada as configurações acima, é necessário definir uma lista dos parceiros aptos a realizarem Ordens de Produção do processo em questão. Esta definição dos parceiros terceiros, acontece por produto e é impactada pelo tipo de Definição de Terceiro, ou seja:

- **Por OP:** Será necessário criar uma lista dos parceiros aptos por processo produtivo, pois todas as operações do processo serão executadas pelo mesmo parceiro. Sendo assim, você define a lista de parceiros por processo por meio da aba **"Produtos(PA)"**, sub-aba **"Terceiros"**.
- **Por Operação:** Da mesma forma que a opção anterior, é necessário criar uma lista dos parceiros aptos por operação, pois cada operação terceirizada possui vínculo com um parceiro terceiro diferente. Sendo assim, defina a lista de parceiros por operação na aba Produtos(PA), sub-aba Terceiros na configuração da atividade.

**Observação:** a aba Terceiros na configuração da atividade, somente será habilitada caso a atividade selecionada seja executada por terceiro (campo Execução Terceirizada diferente de Nunca).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#top)

## Operações de Estoque

Quando existir atividades que são executadas internamente e outras por terceiros, é necessário definir quando as operações de estoque devem ser executadas. Para isso, configure por meio do botão Roteiro, clicando duas vezes sobre a atividade, na aba **"Operações de Estoque"**, campo **"Execução da Atividade"**.

- **Terceiros:** Por esta opção, a operação de estoque será executada sempre por um parceiro terceiro.
- **Todos:** Por meio desta opção, a operação de estoque será executada sempre, independente do tipo de execução da atividade (seja por um parceiro terceiro ou execução própria).
- **Própria:** Escolhendo esta opção, a operação de estoque será executada sempre pela fábrica própria.

![Imagem 3: Própria: Escolhendo esta opção, a operação de estoque será executada sempre pela fábrica própria.](https://ajuda.sankhya.com.br/hc/article_attachments/4409525174295)

Além de definir o executante da operação de estoque, é possível especificar que o parceiro do documento gerado por essa operação seja o parceiro terceiro da OP (atividade). Para utilizar esta funcionalidade, basta marcar o campo **"Usar o Parceiro Terceiro da OP"** 

Com essas configurações, será possível comandar a geração de notas para o terceiro, que de fato irá operacionalizar determinada atividade realizando controle de estoque com terceiros (remessa para industrialização e retorno de industrialização). Lembrando que os [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) utilizadas em atualizações de estoque de terceiro, devem estar configuradas para realizar tal atualização por meio da aba [Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114#abaestoquedeterceiros).

![Imagem 4: Com essas configurações, será possível comandar a geração de notas para o terceiro, que de fato irá operacionalizar…](https://ajuda.sankhya.com.br/hc/article_attachments/20264114346263)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#top)

## Lançamento de Ordem de Produção

Na tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) ao clicar no botão ![Imagem 5: Na tela Ordens de Produção ao clicar no botão "+ Nova OP" você será direcionado para a tela de "Lançamento de Ordem de…](https://ajuda.sankhya.com.br/hc/article_attachments/16749912004503) **"+ Nova OP"** você será direcionado para a tela de **"Lançamento de Ordem de Produção"**. Sendo que, a aba **"Terceiros"** será habilitada sempre que for selecionado um Processo Produtivo que utilize terceiros.

Quando a definição de parceiro for **"por OP"**, existirá um único registro na grade com a descrição da atividade igual a **"Todas Terceirizáveis"** para que seja especificado o parceiro terceiro da Ordem de Produção dentre os parceiros aptos para a execução.

Se a definição de parceiro for **"por Operação"**, existirá um registro para cada atividade terceirizada na grade, para que seja especificado o parceiro terceiro da Ordem de Produção dentre os parceiros aptos para a execução.

![Imagem 6: Se a definição de parceiro for "por Operação" , existirá um registro para cada atividade terceirizada na grade, para…](https://ajuda.sankhya.com.br/hc/article_attachments/4409532984855)

A partir das configurações citadas até aqui, temos a definição dos parceiros que de fato irão executar a terceirização das OP's/Operações; o sistema irá seguir o fluxo de processo definido no roteiro e executar as Operações de Estoque considerando os parceiros em questão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602854-Suporte-Produ%C3%A7%C3%A3o-por-Terceiros#top)
