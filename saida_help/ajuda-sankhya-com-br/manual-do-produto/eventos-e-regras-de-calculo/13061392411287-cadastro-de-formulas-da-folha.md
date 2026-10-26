---
id: "13061392411287"
titulo: "Cadastro de Fórmulas da Folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287-Cadastro-de-F%C3%B3rmulas-da-Folha"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Eventos e Regras de Cálculo"
atualizado_em: "2026-10-07T15:39:36Z"
rotulos: ["Configuração", "Eventos", "eSocial", "br.com.sankhya.rh.FormulaFolha", "Atualizar e reverter fórmulas padrão", "Adicionar e gerenciar fórmulas personalizadas", "Configurar eventos e fórmulas para RRA", "Pessoal+"]
---

# Cadastro de Fórmulas da Folha

```
 Módulo: Pessoal+ > Cadastros
```

---

Esta tela é destinada para a criação de fórmulas padrões e personalizadas para as diversas operações dentro do Pessoal+.

![Imagem 1: Esta tela é destinada para a criação de fórmulas padrões e personalizadas para as diversas operações dentro do Pessoal+…](https://ajuda.sankhya.com.br/hc/article_attachments/26805157888279)

### Aba Fórmulas Padrão

Nesta aba,  o sistema irá carregar um pacote geral de fórmulas padrão Sankhya.

Ao acionar o botão **"Atualizar"**, os [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) e as Fórmulas serão atualizados conforme a sua **"Característica"** ou **"Código"** cadastrados na base de dados do cliente, a fim de contemplar todas as personalizações existentes. Além disso, o sistema possui um **"Job"** noturno que atualizará de forma sincronizada as tabelas de Fórmulas (TFPNEWFORM), Eventos (TFPEVE) e Bases de Cálculo (TFPEBA) exatamente nessa ordem, de acordo com os dados do repositório Sankhya. Esta ação será apresentada na parte superior da tela. 

**Nota:** os Eventos vinculados a fórmulas padronizadas e que não possuírem características não serão atualizados.

Caso queira reverter a atualização dos eventos e fórmulas, basta acionar o botão **"Reverter última atualização"**, assim, o sistema irá realizar uma busca pela última sequência existente e irá retornar esses dados para as tabelas originais. Após essa reversão, a data e hora da atualização anterior poderão ser visualizadas nas telas [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767), Fórmulas e [Padronização de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/11467714112407).

Para criar uma fórmula personalizada, acione o botão ![Imagem 2: Para criar uma fórmula personalizada, acione o botão "Adicionar Fórmula" que abrirá o pop-up "Construa sua fórmula" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/18796310462871) **"Adicionar Fórmula"** que abrirá o pop-up **"Construa sua fórmula"**, assim,  preencha os seguintes dados:

![Imagem 3: Para criar uma fórmula personalizada, acione o botão "Adicionar Fórmula" que abrirá o pop-up "Construa sua fórmula" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/26805235389335)

Preencha a **"Característica"**, o **"Código"** e a **"Descrição"** da Fórmula que será criada. Em seguida, para construir a **"Fórmula do Valor"** e a **"Fórmula do Indice"** utilize  a **"Lista de Variáveis"** apresentada ao lado esquerdo da tela.

Logo após, clique no botão **"Compilar Fórmula"** e será exibida a seguinte mensagem:

**"Atenção! Fórmula compilada com** **sucesso!"**

Depois de compilada, basta clicar no botão ![Imagem 4: Depois de compilada, basta clicar no botão "Salvar" para que a Fórmula possa ser usada.](https://ajuda.sankhya.com.br/hc/article_attachments/26805214982423) **"Salvar"** para que a Fórmula possa ser usada.

### Aba Fórmulas Personalizadas

Esta aba apresenta as fórmulas e variáveis personalizadas, que foram criadas por meio do botão Adicionar Fórmula da aba Fórmulas Padrão. 

![Imagem 5: Esta aba apresenta as fórmulas e variáveis personalizadas, que foram criadas por meio do botão Adicionar Fórmula da aba…](https://ajuda.sankhya.com.br/hc/article_attachments/26805280648983)

---

Caso queira excluir ou duplicar uma fórmula específica, basta passar o mouse sobre a linha desejada e clicar nos botões **"Deletar fórmula"** ou **"Duplicar fórmula"** e confirmar a ação.

[GIF animado: Imagem 6: Caso queira excluir ou duplicar uma fórmula específica, basta passar o mouse sobre a linha desejada e clicar nos botões…](https://ajuda.sankhya.com.br/hc/article_attachments/26805293792407)

---

Nessa tela, tem-se disponível também as funções e variáveis para o cálculo dos [Rendimentos Recebidos Acumuladamente - RRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319), uma vez que estas serão consideradas nos cálculos de complementar de forma que, o resultado será enviado ao eSocial como RRA.

![Imagem 7: Nessa tela, tem-se disponível também as funções e variáveis para o cálculo dos Rendimentos Recebidos Acumuladamente -…](https://ajuda.sankhya.com.br/hc/article_attachments/18797358406807)

Esses eventos devem ser configurados na tela [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) ao configurar os campos **"IRRF"**, **"Evento de Diferença - RRA"** e a marcação **"Evento de RRA"** na aba [Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767-Eventos#AbaAvan%C3%A7ado). Depois é só criar a Fórmula nessa tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287-Cadastro-de-F%C3%B3rmulas-da-Folha#top)
