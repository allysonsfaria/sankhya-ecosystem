---
id: "1500012384422"
titulo: "Divergências no Registro de Conferência - WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:12:57Z"
rotulos: ["Conferência", "Configuração", "WMS", "Estoque", "Recebimento de Mercadorias", "registro de conferência", "divergências", "divergências no registro de conferência", "VERAVAFEUMARC", "Registro de Avaria", "Registro com Sobra", "Registro de Falta"]
---

# Divergências no Registro de Conferência - WMS

Conforme mencionamos no artigo sobre o processo de [Registo de Conferência no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias), pode ser que em algum momento hajam divergências durante a conferência. Aqui nesse artigo trataremos sobre elas.

---

| [![Imagem 1: Conforme mencionamos no artigo sobre o processo de Registo de Conferência no Recebimento de Mercadorias , pode ser que…](https://ajuda.sankhya.com.br/hc/article_attachments/42311489515927)](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrodeavaria) |  | [![Imagem 2: Conforme mencionamos no artigo sobre o processo de Registo de Conferência no Recebimento de Mercadorias , pode ser que…](https://ajuda.sankhya.com.br/hc/article_attachments/42311489516567)](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrocomsobra) |  | [![Imagem 3: Conforme mencionamos no artigo sobre o processo de Registo de Conferência no Recebimento de Mercadorias , pode ser que…](https://ajuda.sankhya.com.br/hc/article_attachments/42311483541527)](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrodefalta) |
| --- | --- | --- | --- | --- |
**Clique nas imagens abaixo para verificar sobre cada uma das divergências:**

---

### Registro de Avaria

No Registro de Conferência é possível evitar que na mesma U.M.A sejam alocados produtos em bom estado com produtos avariados, fazendo com que sejam geradas as tarefas de Armazenagem somente da quantidade **"não avariada"**.

Essa configuração é feita através do parâmetro **"Verificar avaria no fechamento da UMA no registro. - VERAVAFEUMARC"**.

Para registrar uma Avaria, você deve informar no Coletor, no momento do [registro de conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#tarefaregistrodeconfer%C3%AAncia), a quantidade total daquele produto e informar o quanto daquele total está avariado, diferente da conferência convencional, onde é informada a quantidade + avaria = quantidade total do produto. Observe abaixo:

[GIF animado: Imagem 4: Para registrar uma Avaria , você deve informar no Coletor , no momento do registro de conferência , a quantidade total…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019868981)

Após ser feito o registro da Avaria, é possível visualizar através do botão ![Imagem 5: Após ser feito o registro da Avaria , é possível visualizar através do botão da tela Recebimento de Mercadorias , que o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019856101) da tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias), que o sistema gerou a tarefa apenas para a quantidade não avariada **(25)**:

[GIF animado: Imagem 6: Após ser feito o registro da Avaria , é possível visualizar através do botão da tela Recebimento de Mercadorias , que o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019600902)

Para fazer a tratativa dessa Avaria, devemos [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca) pelo botão ![Imagem 7: Para fazer a tratativa dessa Avaria , devemos Processar o Recebimento pelo botão "Outras Opções..." da tela Recebimento…](https://ajuda.sankhya.com.br/hc/article_attachments/16978228252311) **"Outras Opções..."** da tela Recebimento de Mercadorias, conforme demonstramos abaixo:

[GIF animado: Imagem 8: Para fazer a tratativa dessa Avaria , devemos Processar o Recebimento pelo botão "Outras Opções..." da tela Recebimento…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019601282)

---

**(1)** Você poderá **"Devolver Avaria"** através do botão ![Imagem 9: (1) Você poderá "Devolver Avaria" através do botão , onde será gerada a Nota de Devolução com a quantidade avariada, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019601342), onde será gerada a Nota de Devolução com a quantidade avariada, ou pode **"Aceitar Avaria"**, clicando no botão ![Imagem 10: (1) Você poderá "Devolver Avaria" através do botão , onde será gerada a Nota de Devolução com a quantidade avariada, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019601422). No nosso caso acima, aceitamos a Avaria.

---

Ao finalizar a tratativa de divergência aceitando a avaria, o próximo passo é gerar a tarefa de armazenagem para o endereço de avaria na tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento).

**Observação:** para que a tarefa de armazenagem seja gerada é necessário que no cadastro do [Endereço de Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) o campo **"Situação do Estoque"** esteja com a opção **"Bloqueado"** selecionada.

[GIF animado: Imagem 11: Observação: para que a tarefa de armazenagem seja gerada é necessário que no cadastro do Endereço de Avaria o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019876741)

Agora que as tarefas foram geradas, o produto está pronto para ser armazenado, tanto a quantidade avariada quanto a que não está:

[GIF animado: Imagem 12: Agora que as tarefas foram geradas, o produto está pronto para ser armazenado, tanto a quantidade avariada quanto a que…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019607982)

Após finalizar a tarefa de [armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem), processe novamente o recebimento para validar a conferência e, posteriormente libere a doca, da mesma forma como demonstramos no artigo [Processar Recebimento e Liberar a Doca](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrodeavaria) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#top)

### Registro com Sobra

O Registo de Conferência tem uma particularidade de alertar o conferente quando a quantidade conferida do produto está maior do que a quantidade negociada na Nota. Para isso ocorrer, basta desligar o parâmetro **"Permitir contar a maior no Registro de Conferência - PERMCONTREGCON"**.

No nosso exemplo, a quantidade negociada na Nota foi de 50 unidades e, no momento da conferência informamos 60 unidades. Assim, com o parâmetro acima desligado, quando for identificada a sobra na conferência, será gerada a mensagem abaixo:

[GIF animado: Imagem 13: No nosso exemplo, a quantidade negociada na Nota foi de 50 unidades e, no momento da conferência informamos 60 unidades…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019884641)

---

**(1)** No pop-up da mensagem acima, se optarmos por **"Sim"**, o sistema aceitará a quantidade informada, mesmo com divergência e, caso clicarmos em **"Não"**, o cursor voltará para o campo **"Quantidade"** para iniciar a conferência de outro produto ou já resolver a divergência do primeiro e assim, seguir com a conferência.

---

Após ser feito o registro da Sobra, você consegue visualizar através do botão ![Imagem 14: Após ser feito o registro da Sobra , você consegue visualizar através do botão da tela Recebimento de Mercadorias , a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019856101) da tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias), a tarefa gerada para o produto após a conferência:

[GIF animado: Imagem 15: Após ser feito o registro da Sobra , você consegue visualizar através do botão da tela Recebimento de Mercadorias , a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019885241)

Para realizar a tratativa dessa Sobra, devemos [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca) pelo botão **"Outras Opções..."** da tela Recebimento de Mercadorias, assim como demonstramos abaixo:

[GIF animado: Imagem 16: Para realizar a tratativa dessa Sobra , devemos Processar o Recebimento pelo botão "Outras Opções..." da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019980741)

---

**(1)** Você poderá **"Devolver Tudo"**, ou seja, todos os itens da nota, onde será gerada a Nota de Devolução com a quantidade total da nota de compra, **"Devolver Item"** através do botão ![Imagem 17: (1) Você poderá "Devolver Tudo" , ou seja, todos os itens da nota, onde será gerada a Nota de Devolução com a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019711202) para devolver apenas a quantidade do item selecionado, ou poderá **"Aceitar Diferença"**, clicando no botão ![Imagem 18: (1) Você poderá "Devolver Tudo" , ou seja, todos os itens da nota, onde será gerada a Nota de Devolução com a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019614622), para que seja lançada uma nota de compra para alimentar o estoque fiscal, armazenando a quantidade a mais. No nosso caso acima, aceitamos a Sobra.

---

Finalizado o registro de conferência com sobra, já podemos executar as tarefas de [Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem) no Coletor. Observe abaixo como fazemos o processo:

[GIF animado: Imagem 19: Finalizado o registro de conferência com sobra, já podemos executar as tarefas de Armazenagem no Coletor . Observe…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019981321)

Ao concluir o processo de Armazenagem, na tela Recebimento de Mercadorias, a situação do recebimento será alterada para **"Armazenado"**.

Por fim, basta que você faça a Liberação da Doca:

[GIF animado: Imagem 20: Por fim, basta que você faça a Liberação da Doca :](https://ajuda.sankhya.com.br/hc/article_attachments/1500019981721)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrocomsobra) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#top)

### Registro de Falta

No Registro de Conferência com Falta, podem ocorrer 2 situações: a [Falta Parcial](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#faltaparcial) e a [Falta Total](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#faltatotal). Nesse tópico, trataremos sobre elas.

---

**Falta Parcial**

A Falta Parcial de um produto é identificada no momento do Registro de Conferência e segue os mesmos procedimentos que o registro de [Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrodeavaria) e com [Sobra](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrocomsobra) para sua tratativa.

No exemplo abaixo, a quantidade da nota é de 100 unidades e, no momento da conferência, fizemos a contagem de apenas 50 unidades:

[GIF animado: Imagem 21: No exemplo abaixo, a quantidade da nota é de 100 unidades e, no momento da conferência, fizemos a contagem de apenas 50…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019983761)

Agora, o próximo passo é [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca). Quando ocorrer a falta parcial, caso a tratativa seja **"Recontar"**, essa recontagem deve ser feita informando a própria U.M.A,. Observe abaixo como fazer:

[GIF animado: Imagem 22: Agora, o próximo passo é Processar o Recebimento . Quando ocorrer a falta parcial, caso a tratativa seja "Recontar" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019983921)

Após ser executada a recontagem, podemos finalizá-la clicando no botão **"Fechar U.M.A"**; assim, o sistema irá sobrepor a primeira tarefa de Armazenagem gerada com 50 unidades, enviando 100 unidades para armazenagem:

[GIF animado: Imagem 23: Após ser executada a recontagem, podemos finalizá-la clicando no botão "Fechar U.M.A" ; assim, o sistema irá sobrepor a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019713502)

Ao invés de fazer a Recontagem, você poderá **"Devolver Falta"** através do botão ![Imagem 24: Ao invés de fazer a Recontagem , você poderá "Devolver Falta" através do botão . Quando for acionado, será gerada uma…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019988521). Quando for acionado, será gerada uma nota de Devolução de Compra com a quantidade apresentada com falta.

Finalizada a tratativa da divergência de falta parcial, os produtos já podem ser [armazenados](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem) e a [doca liberada](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca):

[GIF animado: Imagem 25: Finalizada a tratativa da divergência de falta parcial, os produtos já podem ser armazenados e a doca liberada :](https://ajuda.sankhya.com.br/hc/article_attachments/1500019713942)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrodefalta)

---

**Falta Total**

Demonstraremos agora a Falta Total no processo de Registro de Conferência. No nosso exemplo, lançamos uma nota com dois produtos e enviamos para o WMS. Após isso, ao executar a tarefa de [registro de conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#tarefaregistrodeconfer%C3%AAncia), registramos a entrada apenas de um dos produtos da nota:

[GIF animado: Imagem 26: Demonstraremos agora a Falta Total no processo de Registro de Conferência . No nosso exemplo, lançamos uma nota com…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019986021)

---

**(1)** Ao final da conferência, são apresentadas as **"Qtde itens recebimento: 2"** e **"Qtde. Itens conferidos: 1"** e a mensagem **"Este recebimento possui 1item(s) pendente(s) de conferência. Ao acionar o Finalizar este(s) produto(s) será(ão) tratado(s) com divergência de falta"**.

---

Após registrar os produtos, iremos [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca) para tratar as divergências. Em nosso exemplo, iremos realizar a Recontagem do produto:

[GIF animado: Imagem 27: Após registrar os produtos, iremos Processar o Recebimento para tratar as divergências. Em nosso exemplo, iremos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019987041)

**(1)** Diferente da [Falta Parcial](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#faltaparcial), quando se tem a Falta Total de um produto, o sistema gera uma Unidade de Movimentação de Armazenagem - U.M.A interna (que pode ser consultada na tabela TGWRCON) para realizar a recontagem; então, essa U.M.A deve ser bipada para o início da tarefa de recontagem.

No nosso caso, a U.M.A criada foi a **"REC718150"** (onde REC=Recebimento, 718=Número do Recebimento e 150=Código do Produto):

[GIF animado: Imagem 28: No nosso caso, a U.M.A criada foi a "REC718150" (onde REC=Recebimento , 718=Número do Recebimento e 150=Código do…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019737542)

---

**(1)** A U.M.A é criada devido o produto não ter sido alocado à uma U.M.A durante a conferência e, caso esse recebimento tivesse mais produtos não conferidos, seriam criadas U.M.A's internas para cada produto.

---

No caso que demonstramos acima, realizamos a Recontagem e informamos a quantidade correta, ou seja, de 100 unidades; porém, poderíamos ter optado por **"Devolver Falta"**, através do botão ![Imagem 29: No caso que demonstramos acima, realizamos a Recontagem e informamos a quantidade correta, ou seja, de 100 unidades ;…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019988521).

Concluída a tratativa de divergência de falta total, os produtos já estão prontos para serem armazenados e a doca liberada:

[GIF animado: Imagem 30: Concluída a tratativa de divergência de falta total, os produtos já estão prontos para serem armazenados e a doca…](https://ajuda.sankhya.com.br/hc/article_attachments/1500020008921)

**Observação:** Quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar o botão [Recontar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#recontar), será criada uma tarefa de recontagem da(s) UMA(s) na doca e no endereço de destino. Desse modo, ao acessar o coletor TotalCross você pode conferir o **"Endereço"**, a **"UMA"** e o **"Produto"** que será recontado. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#registrodefalta) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS#top)

---

**![Imagem 31: Saiba mais sobre as configurações e etapas do Registro de Conferência acessando a documentação Registro de Conferência…](https://ajuda.sankhya.com.br/hc/article_attachments/16977727344023) Saiba mais sobre as configurações e etapas do Registro de Conferência acessando a documentação [Registro de Conferência no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias).**

---
