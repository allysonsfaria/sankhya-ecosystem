---
id: "360044604294"
titulo: "Origem de Atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604294-Origem-de-Atendimento"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:53:42Z"
rotulos: ["manual", "Configuração", "Ordem de Serviço", "Preferências", "Consulta de OS", "OS", "atendimento", "Origem de Atendimento", "Responsável pela OS", "br.com.sankhya.cad.origemdeatendimento", "Origem de Atendimento manual", "Cadastro", "Parâmetro", "Configuração da Origem do Atendimento nas Ordens de Serviço"]
---

# Origem de Atendimento

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310827847319)Módulo: Configurações > Cadastros
```

---

Esta configuração permite um maior controle e acompanhamento interno das ordens de serviços e é feita através do campo **"Origem"**, na abertura da OS.

Essa opção pode ser utilizada no [Lançamento de OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414) e em **"OS Pré-Venda"**.

A Origem do Atendimento esta diretamente ligada ao parâmetro **"Máscara para origem da chamada - MASCORIGATEND"**, onde você criará a máscara que será utilizada no cadastro da origem do atendimento

Como cadastrar uma nova origem de atendimento:

Primeiramente, no parâmetro MASCORIGATEND, você define a máscara para a origem. A configuração da máscara deve se dar da seguinte forma:

- Acesse a tela Preferências.
- No campo **"Tipo"**, selecione **"Texto"** para que se possa então digitar a máscara na caixa de texto.

**Importante:** a máscara deve ser definida com **"\" (barra)** e **"."(ponto)**, como por exemplo, **"99\.999\.99"**.

A configuração será feita de acordo com a sua necessidade, sendo que a máscara poderá ter no máximo 4 níveis, que somados não deverão ultrapassar 9 dígitos. De acordo com esta máscara serão cadastradas as origens.

O tamanho dos graus (pai, filho, neto e bisneto) definirá o número de dígitos que deverá conter cada grau, a barra **"\"** separará os níveis. Então, no exemplo anterior **"99\.999\.99"**, a máscara apresenta três níveis (pai, filho e neto), sendo que foi definido no nível 1 (pai) dois dígitos (99), no nível 2 (filho) três dígitos fora o ponto **"."** (999) e no nível três (neto) mais dois dígitos fora o ponto **"."** (99).

Definida a máscara, o segundo passo será cadastrar a origem na tela Origem de Atendimento.

![Imagem 2: Definida a máscara, o segundo passo será cadastrar a origem na tela Origem de Atendimento .](https://ajuda.sankhya.com.br/hc/article_attachments/360085477274)

A máscara configurada no parâmetro MASCORIGATEND definirá a forma de inserção dos níveis e graus da nova origem, no campo **"Código"** desta tela.

A tela segue o padrão de cadastro **"Analítico"** e **"Sintético"** existente no sistema, permitindo a inclusão, exclusão e alteração dos cadastros.

O campo **"Descrição"** é de livre digitação e, juntamente com o código, identificará na Ordem de Serviço a origem do atendimento.

**Exemplo de Descrição:** Chamada de Service Desk ou Chamada telefônica por parte do Cliente...

O campo **"Tipo"** definirá se a nova origem de atendimento será de **"Pré-Venda"**, de **"Atendimento"** ou **"Ambos".**

Este cadastro respeitará a hierarquia **"pai/filho"**, ou seja, o sistema verificará o **"Tipo"** definido para o pai e não permitirá que o filho seja cadastrado com outro Tipo senão o do pai. Se isto ocorrer, o sistema emitirá a mensagem:

**"O Tipo do registro filho não pode ser diferente do Tipo do registro pai".**

Contudo, se o Tipo definido para o pai for igual a **"Ambos"**, será possível cadastrar os filhos tanto como **"Atendimento"**, quanto como **"Pré-Venda"**.

Uma vez cadastrado o pai, não será possível mudar o seu tipo e, neste caso, o sistema emitirá a mensagem:

**"O Tipo do registro pai não pode ser alterado."**

Uma vez cadastrada a **"Origem"**, você poderá, no lançamento de uma OS, classificá-la de acordo com a origem cadastrada:

![Imagem 3: Uma vez cadastrada a " Origem " , você poderá, no lançamento de uma OS , classificá-la de acordo com a origem…](https://ajuda.sankhya.com.br/hc/article_attachments/360085498474)

No passo 6 do lançamento de OS, você visualizará o campo **"Origem"**, onde selecionará através da pesquisa, a origem de atendimento desejada.

Para pesquisar uma origem de atendimento, você deve clicar sobre o nome do campo, Origem, para que o sistema abra a tela **"Pesquisar Origem do Atendimento"**, que apresentará, por sua vez, todas as origens cadastradas na rotina Origem de Atendimento.

Na grade, serão apresentadas as origens de atendimento que estão **"Ativas"**, **"Sintéticas"** e **"Analíticas"** e de Tipo igual a **"Atendimento"** ou **"Ambos"**. As origens de Tipo igual a Pré-Venda, só poderão ser visualizadas na tela de **"Negociação"(Pré-Venda)**.

O sistema só aceitará a inclusão de origens Analíticas.

Se depois de incluir uma origem, você desejar trocá-la por outra, antes de salvar a OS, bastará clicar novamente sobre o nome do campo Origem para selecionar outra origem na tela **"Pesquisar Origem do Atendimento"**. Logo à frente do campo Origem encontra-se uma **"borracha"**, através da qual será possível **"limpar"** o conteúdo do campo, quando o usuário não desejar mais informar a origem da OS.

Ao informar a origem e salvar a OS, pode-se ver no campo Origem do cabeçalho da OS, a informação que foi inserida no passo 6.

A informação no campo **"Origem"** do cabeçalho não poderá ser apagada e, somente o **"Responsável pela OS"** poderá alterá-lo através do botão de **"Pesquisa"** (lupa), que abrirá novamente a tela **"Pesquisar Origem do Atendimento"**, para escolha de nova origem.

**Nota:** a grade das telas **"Consulta de OS"** e **"Pendências"**, apresentam a coluna **"Origem do Atendimento"** que traz a origem de atendimento da OS, para consulta dos usuários.
