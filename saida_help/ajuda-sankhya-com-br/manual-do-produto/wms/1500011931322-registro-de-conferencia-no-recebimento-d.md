---
id: "1500011931322"
titulo: "Registro de Conferência no Recebimento de Mercadorias - WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:12:53Z"
rotulos: ["Conferência", "Configuração", "WMS", "Recebimento", "Recebimento de Mercadorias", "registro de conferência", "UMA", "Registro de Conferência no Recebimento de Mercadorias - WMS", "Armazenagem"]
---

# Registro de Conferência no Recebimento de Mercadorias - WMS

O Registro de Conferência trata-se de uma tarefa de conferência que torna o processo de armazenagem mais ágil e é indicado para operações onde há pouco espaço para recebimento, assim, à medida que a conferência for realizada, os produtos já serão direcionados para a armazenagem. Também é utilizado nessa tarefa, o conceito de U.M.A (Unidade de Movimentação de Armazenagem).

Utilizando a geração de tarefas automáticas através de um job, esse mecanismo faz com que os produtos recebidos não fiquem parados na doca, otimizando o espaço de recebimento da mesma.

Para que você consiga fazer o processo de Registro de Conferência no Recebimento com sucesso, realize primeiramente as configurações abaixo:

1. Efetue a marcação **"Utiliza recebimento parcial?"** localizada nas telas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) e [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms);
2. Configure o parâmetro **"Código do modelo do mapa de recontagem. - CODRELRECONTA"** com o código do mapa de recontagem. Esse mapa é responsável por, na hora de confirmar a recontagem, registrar os produtos em um dashboard que é impresso nesse mesmo momento automaticamente, para que possa ser direcionado ao responsável pela conferência, os endereços que contém o produto a ser recontado. O mapa não é nativo e deverá ser personalizado. **Observação:** para a impressão do mapa de recontagem, informe a impressora padrão no parâmetro **"Impressora padrão para o mapa de recontagem. - IMPMAPARECONTA"**.
3. Realize a marcação **"Múltiplos usuários na conferência de entrada"** na tela Preferências da Empresa, aba WMS, para que mais de uma pessoa possa conferir a mesma nota (ou mais de uma) no mesmo Recebimento;
4. Por fim, é necessário que seja concedida permissão de acesso à tarefa do Coletor para o(s) conferente(s) através da tela [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354-Configura%C3%A7%C3%B5es-por-Usu%C3%A1rio).

Realizadas as configurações acima, você já pode iniciar o processo de Registro de Conferência.

---

[GIF animado: Imagem 1: Realizadas as configurações acima, você já pode iniciar o processo de Registro de Conferência .](https://ajuda.sankhya.com.br/hc/article_attachments/1500019824541)

---

Primeiramente, é necessário que uma Nota de Compra seja lançada e enviada para o Recebimento de Mercadorias, através do botão ![Imagem 2: Primeiramente, é necessário que uma Nota de Compra seja lançada e enviada para o Recebimento de Mercadorias , através…](https://ajuda.sankhya.com.br/hc/article_attachments/16978070446359) **"Outras Opções..."**, opção **"Enviar para o WMS (Recebimento)"**:

[GIF animado: Imagem 3: Primeiramente, é necessário que uma Nota de Compra seja lançada e enviada para o Recebimento de Mercadorias , através…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019722761)

Após o envio, o conferente apto a utilizar a tarefa Registro de Conferência, irá iniciá-la no Coletor e informar a **"Doca"** em que ocorrerá essa conferência. Então, depois de informar a Doca, o próximo passo é inserir a **"U.M.A"** na qual aquele produto será conferido:

[GIF animado: Imagem 4: Após o envio, o conferente apto a utilizar a tarefa Registro de Conferência , irá iniciá-la no Coletor e informar a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019470762)

**(1)** A U.M.A pode ser uma etiqueta de identificação do palete, tratando-se de um número sequencial para o controle de Conferência e Armazenagem do Produto.

Informada a U.M.A, você deve inserir a **"Quantidade"** e o **"Produto"** que está naquela Unidade de Movimentação de Armazenagem, no nosso caso, o palete com a etiqueta **"0002"**:

[GIF animado: Imagem 5: Informada a U.M.A , você deve inserir a "Quantidade" e o "Produto" que está naquela Unidade de Movimentação de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019736481)

![Imagem 6: Depois de informar a Quantidade e o Produto, caso existam somente esses Produtos no palete, você pode informar que eles…](https://ajuda.sankhya.com.br/hc/article_attachments/16978070453527) Depois de informar a Quantidade e o Produto, caso existam somente esses Produtos no palete, você pode informar que eles estão prontos para a Armazenagem clicando no botão **"Fechar U.M.A"**.

**Observação:**com o parâmetro **"Registro de conferência completa endereço? - REGCONCOMPLEND"** ligado não será possível utilizar a função de completar endereço para armazenamento. Quando desligado, essa função só poderá ser utilizada se o recebimento não estiver associado a um Registro de Conferência.

**(1)** Se o parâmetro **"Registro de conferência c/ armazenagem automática - REGCONFARMAUTO"** estiver ligado, o sistema irá gerar as tarefas de armazenagem de forma automática para os produtos registrados na U.M.A após clicar em Fechar U.M.A, atualizando a situação do Recebimento para **"Enviado para Armazenagem"** (com exceção de produtos [avariados](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-WMS-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia#registrodeavaria)):

[GIF animado: Imagem 7: (1) Se o parâmetro "Registro de conferência c/ armazenagem automática - REGCONFARMAUTO" estiver ligado, o sistema irá…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019777941)

Porém, se o parâmetro estiver desligado, o responsável pela Geração das Tarefas de Armazenagem deve acessar a tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento) e realizar a geração.

---

**![Imagem 8: Observações importantes:](https://ajuda.sankhya.com.br/hc/article_attachments/16978070452119) Observações importantes:**

- Quando a U.M.A for fechada, ela não poderá mais ser utilizada por nenhum outro produto ou Registro de Conferência, caso contrário, teremos a mensagem abaixo:

  [GIF animado: Imagem 9: Quando a U.M.A for fechada, ela não poderá mais ser utilizada por nenhum outro produto ou Registro de Conferência ,…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019513962)

- Você pode registrar vários produtos para uma U.M.A, mas depois de fechá-la, não poderá utilizá-la novamente.
- Após a geração das tarefas, o sistema bloqueia os endereços de Destino (endereços de armazenagem); assim, se houverem divergências, elas serão tratadas sem correr o risco do produto ser movimentado. Esse processo pode ser alterado através da marcação **"Inibe bloqueio do endereço no registro de conferência"**, localizada na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms).

![Imagem 10: Caso nas operações de entrada do sistema, sendo elas, Compras e Devoluções de Vendas, a empresa utilizada no processo…](https://ajuda.sankhya.com.br/hc/article_attachments/16978070452119) Caso nas operações de entrada do sistema, sendo elas, Compras e Devoluções de Vendas, a empresa utilizada no processo esteja com a marcação **"Utiliza explosão de lote no recebimento"** da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) habilitada, o sistema realizará a explosão de lote em determinados momentos da operação. Observe:

- Quando não houverem divergências, o sistema realizará a inserção ou atualização no controle de lote dos itens da nota ao processar o recebimento;
- Se houver um mesmo produto que se encontra em UMA's diferentes, o sistema irá somá-los, o que atualizará os itens da grade;
- Porém, caso esse mesmo produto possuir controles de lotes diferentes, estes serão inseridos na grade de itens com uma sequência para cada controle cadastrado ou quantidade menor que a inicial, de forma que, o sistema irá realizar o recálculo dos valores da grade e de seus impostos.

---

Depois de todos os produtos da nota passarem pelo Registro de Conferência, finaliza-se a conferência clicando no botão **"Finalizar conferência"**, sendo apresentado o número de Produtos na Nota e o número de Produtos Conferidos. No caso abaixo, realizamos a conferência de dois produtos, logo, o sistema gerou as tarefas para os dois:

[GIF animado: Imagem 11: Depois de todos os produtos da nota passarem pelo Registro de Conferência , finaliza-se a conferência clicando no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019778181)

**(1)** O botão Finalizar Conferência deve ser acionado para indicar que todos os produtos existentes naquele Recebimento foram conferidos. Após finalizar a conferência, ao processar o recebimento na tela de [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias) as notas serão confirmadas.

Agora, após a conferência ser validada, podemos executar as tarefas de Armazenagem no Coletor. Aqui, você pode optar pelo Armazenamento Seletivo, Armazenamento Expresso ou Armazenagem. Observe abaixo como fazemos o processo:

[GIF animado: Imagem 12: Agora, após a conferência ser validada, podemos executar as tarefas de Armazenagem no Coletor . Aqui, você pode optar…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019813741)

Ao concluir o processo de Armazenagem, na tela Recebimento de Mercadorias, a situação do recebimento será alterada para **"Armazenado"**.

Por fim, a etapa de Processar o Recebimento e Liberar a Doca já pode ser feita, através da tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias), botão **"Outras Opções..."**, opções **"Processar recebimento"** e **"Liberação da Doca"**:

[GIF animado: Imagem 13: Por fim, a etapa de Processar o Recebimento e Liberar a Doca já pode ser feita, através da tela Recebimento de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019814881)

![Imagem 14: Caso o parâmetro "Liberação Automática de doca de entrada no WMS - LIBAUTDOCENTWMS" esteja ligado, após Processar o…](https://ajuda.sankhya.com.br/hc/article_attachments/16978070453527) Caso o parâmetro **"Liberação Automática de doca de entrada no WMS - LIBAUTDOCENTWMS"** esteja ligado, após Processar o Recebimento a doca de entrada será liberada automaticamente.

No processo de Registro de Conferência, temos a flexibilidade de [armazenar](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias-WMS#armazenagem) os produtos após a [geração das tarefas de armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias-WMS#gera%C3%A7%C3%A3odetarefasdearmazenagemautom%C3%A1tica) ou então, aguardar o [processamento do recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias-WMS#processarrecebimentoeliberardoca) para já tratar as divergências. Essa execução fica a critério do que melhor atende sua operação.

No exemplo do gif acima, quando Processamos o Recebimento, é exibida a mensagem de que as conferências foram concluídas com sucesso, porém, em alguns casos, pode ser que hajam divergências durante o processo de conferência, como, por exemplo a Avaria, Falta ou Sobra.

---

**![Imagem 15: Saiba mais sobre cada uma das divergências nesse processo acessando a documentação Divergências no Registro de…](https://ajuda.sankhya.com.br/hc/article_attachments/16978175096215) Saiba mais sobre cada uma das divergências nesse processo acessando a documentação [Divergências no Registro de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-WMS-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia).**

---

![Imagem 16: O Registro de Conferência no Recebimento de Mercadorias está apto para realizar Explosão de Lotes .](https://ajuda.sankhya.com.br/hc/article_attachments/16978070452119) O Registro de Conferência no Recebimento de Mercadorias está apto para realizar [Explosão de Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes).
