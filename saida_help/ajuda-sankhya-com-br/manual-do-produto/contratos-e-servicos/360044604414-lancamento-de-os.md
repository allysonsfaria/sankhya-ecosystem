---
id: "360044604414"
titulo: "Lançamento de OS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:03:47Z"
rotulos: ["AJUDA DO SKW", "manual", "SERVDIRMOD", "Configuração", "Parceiro", "Contratos", "VALIDALINKANEXO", "Ordem de Serviço", "Serviços", "Lançamento de OS", "E-mail", "CHECHORAEXECOS", "Dados do contato", "EDITAPRECOORC", "EXIBPROJPENDOS", "MODORCASSITTEC", "MOSTRARNUMOS", "MOSTRARPRECOORC", "Orçamento", "PRODEXTRACONTR", "USATPAORCOS", "br.com.sankhya.os.cad.lancamentoos", "Lançamento de OS manual", "Lançamento Eficiente de Ordem de Serviço"]
---

# Lançamento de OS

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311173847191) Módulo: Contratos e Serviços > Ordem de Serviço
```

---

Para realizar o lançamento de uma nova OS, acesse esta rotina. O sistema cria uma OS através de um Wizard, informando os dados em sequência. 

[Salvando Alterações na OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#salvandoalteraesnaos)                             

[Salvando e Encaminhando uma Sub-OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#salvandoeencaminhandoumasub-os)

[Criando uma Sub-OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#criandoumasub-os)                                     

[Adicionando Anexos à OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#adicionandoanexosos)

[Regra para um Pedido ser apresentado para Lançamento de OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#regraparaumpedidoserapresentadoparalanamentodeos)

[Regra para os Produtos e Serviços serem apresentados para Lançamento da OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#regraparaosprodutoseserviosseremapresentadosparalanamentodaos)

[Origem de Atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#origemdeatendimento)

[Anexo I](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#anexoi)

[Orçamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#oramento)

[OS Web pelo Número de Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#oswebpelonmerodesrie)

[OS aberta no Sankhya Om e Portal do Cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#osabertanosankhyaomeportaldocliente)

[Gerar uma Requisição através de uma OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#gerarumarequisioatravsdeumaos)

Primeiramente, escolha o **"Nome do Parceiro"** no espaço **"Campo"** e digite, por exemplo, Sankhya no **"Início"** e clique no botão **"Pesquisar"**. O sistema apresentará na grade, os Parceiros encontrados, de acordo com o filtro informado. Caso seja encontrado apenas um Parceiro, o sistema passa automaticamente para o passo 2.

![Imagem 2: Em seguida, escolha o contato do Parceiro . Para isto, escolha "Nome do contato" no "Campo" , digite o nome no "Iní…](https://ajuda.sankhya.com.br/hc/article_attachments/360086626493)Em seguida, escolha o contato do Parceiro. Para isto, escolha **"Nome do contato"** no **"Campo"**, digite o nome no **"Início"** e clique no botão **"Pesquisar"** ou selecione um dos contatos apresentados na tela, clicando na linha correspondente.

[GIF animado: Imagem 3: Após, escolha o "Tipo de negociação" , sendo que as opções disponíveis são:](https://ajuda.sankhya.com.br/hc/article_attachments/360085451194)

Após, escolha o **"Tipo de negociação"**, sendo que as opções disponíveis são:

- **Pedido:** Serviços descritos no pedido.
- **Contrato:** Serviços descritos no contrato do Parceiro.
- **FAP:** Para lançar OS direto na FAP.

![Imagem 4: FAP: Para lançar OS direto na FAP .](https://ajuda.sankhya.com.br/hc/article_attachments/8523304345239)

**Observação:** apenas Ordens de Serviços de Contrato podem ser utilizadas como modelo, isto é, não é possível salvar como modelo as OS do tipo FAP e Pedido.

**Nota:** o parâmetro **"Mensagem para ser apresentada quando o cliente estiver em atraso - MSGCLIATRAS"** poderá ser utilizado para configurar a mensagem conforme você desejar; a mesma será apresentada no momento do lançamento de uma OS, para Parceiros que estão com títulos em atraso, ou seja, quando informado, o sistema trará a mensagem inserida no parâmetro. Por outro lado, caso nenhuma informação seja configurada neste parâmetro, o sistema irá apresentar a mensagem padrão. Por exemplo:

**"Cliente em atraso desde o dia 04/10/2015. Total atrasado: R$100,00"**

O sistema faz ainda a validação de atraso, caso o parâmetro **"Validação de Atraso - VALATRASOS"** esteja devidamente configurado. Assim, temos as opções **"Não Valida"**, **"Valida e Aceita"** ou **"Valida e Não Aceita"**, sendo que estas deverão estar configuradas da seguinte forma:

- Desejando que o sistema Valide e Aceite o atraso, insira o valor 1 no campo **"Inteiro"** da tela de configuração do parâmetro;
- Para Não validar e Não aceitar, configure o valor 2 no campo acima informado;
- Optando apenas por Não Validar registre o valor 0 neste campo.

**Observação:** se for Valida e Aceita, o sistema permitirá o lançamento da OS, mas exibirá a mensagem como alerta e, sendo Valida e Não Aceita, o sistema impedirá o lançamento da OS, exibindo a mensagem relacionada ao parâmetro Mensagem para ser apresentada quando o cliente estiver em atraso - MSGCLIATRAS.

**Nota:** a mensagem também será exibida no lançamento de OS Externa, respeitando os parâmetros da mesma forma como descrito acima.

Além da validação de atraso, temos também a opção de impedir o lançamento de uma OS para um Parceiro que possua as vendas à prazo para ele bloqueadas e, se o subtipo da negociação do contrato que está sendo utilizado não for à vista. Através da ativação do parâmetro **"Libera bloqueio a prazo na OS se negociar a vista? - LIBBLOQPRZOSAV"**, caso o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) possua na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacrdito), a marcação **"Bloquear venda a prazo"** efetuada, e o subtipo da negociação utilizada em seu contrato for **"à vista"**, nenhum impedimento será apresentado na conclusão do lançamento da OS.

**Observação:** você deve realizar as configurações acima mencionadas também para realizar o lançamento de uma OS a partir de um Pedido de Venda, ou seja, o parâmetro Libera bloqueio a prazo na OS se negociar a vista? - LIBBLOQPRZOSAV deverá estar habilitado, o Tipo de Negociação do pedido deverá ser à vista e a marcação Bloquear venda a prazo deverá estar efetuada.

Nesta próxima etapa, defina o **"Produto"** e o **"Serviço"** para abertura da OS. O serviço aqui selecionado é o serviço do primeiro item da OS. Vale ressaltar que cada OS é executada para apenas um Produto.

![Imagem 5: Nesta próxima etapa, defina o "Produto" e o "Serviço" para abertura da OS . O serviço aqui selecionado é o serviço do…](https://ajuda.sankhya.com.br/hc/article_attachments/360085452194)

Para que o Serviço Previsto seja apresentado para o Produto, existe uma diferenciação quando a negociação tratar-se de Contrato ou se tratar de Pedido. Trataremos sobre cada um deles:

- Tratando-se de Contrato, é necessário que no seu cadastro, aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774#abapropriedades), o campo **"Natureza"** esteja configurado e vinculado aos serviços autorizados pertinentes ao mesmo. Além disso, para que a série do imobilizado (código do bem) seja apresentada, o parâmetro **"Integrao com Mdulo de Imobilizado - SERVIMOBILI"** deverá está ligado. Com essa configuração, ao confirmar o lançamento, o sistema verifica se o produto do contrato é um bem imobilizado lançado anteriormente e com o devido vínculo na TCIBEM. Desse modo, caso você não queira que seja realizada essa verificação, o parâmetro SERVIMOBILI deverá estar desligado.
- Quando tratar-se de Pedido, o parâmetro **"Filtrar serviços pelo 'Uso produto' - SERVFILUSOPROD"** deverá está desligado, pois a diferenciação se dá pelo grupo de serviços informado no parâmetro **"Grupo de Serviços para Lançamento de OS p/ Pedido - GRUPOSERVSOFT"**.

Deste modo, todos os serviços que façam parte do Grupo de Produtos e Serviços apontado no parâmetro Grupo de Serviços para Lançamento de OS p/ Pedido - GRUPOSERVSOFT serão considerados Serviço no lançamento de OS por pedido. Todos os demais serão considerados Produtos. Portanto, o Produto do pedido será apresentado no campo Produto e os serviços do pedido como Serviços Previstos nesta etapa do lançamento de OS.

**Nota:** o parâmetro **"Descrição do produto no lançamento de OS - DESCPRODLCTOOS"** quando habilitado, formatará a descrição do Produto na tela de Ordem de Serviço de acordo com o valor digitado no parâmetro.

Ao digitar um valor no parâmetro acima com a seguinte nomenclatura: **"$CODPROD - $DESCRPROD [$REFFORN]"**, o sistema formata a descrição do Produto apenas na tela de OS da seguinte forma: **"001 – Refrigerante Mineiro [REF001FOO]"**.

As palavras denominadas com o identificador **"$"** deverão respeitar os campos existentes na tabela TGFPRO. Caso não exista o campo na TGFPRO, será retornada a palavra conforme digitado e, se o campo existir mas não tiver nenhum valor informado na tabela, o retorno será vazio.

**Observação:** o parâmetro será inativo quando não existir nenhuma informação digitada.

Após o preenchimento do parâmetro, os locais na Ordem de Serviço que apresentem a descrição do produto, respeitarão a descrição informada no mesmo.

**Nota:** no parâmetro **"Lista de Produtos extra contrato (Lanc. OS) - PRODEXTRACONTR"** você pode efetuar o cadastro de uma lista de Produtos "extra contrato", ou seja, Produtos que não estão vinculados à um contrato, de tal maneira que, ao realizar o Lançamento de Ordens de Serviço, na etapa correspondente à escolha do Produto, além dos produtos já associados aos contratos, será possível também selecionar/trabalhar com os produtos que foram listados no referido parâmetro.

Dando continuidade às etapas, após, informe o **"Executante"** da OS, ou seja, seu primeiro responsável. O sistema apresentará somente executantes que estejam ligados ao Produto e Serviço selecionados na etapa anterior.

![Imagem 6: Dando continuidade às etapas, após, informe o "Executante" da OS, ou seja, seu primeiro responsável. O sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/360085452514)

**Observação:** caso você não esteja vinculado ao Produto e Serviço da OS, é necessário cadastrá-lo aos mesmos; verifique qual o procedimento no tópico [ANEXO I](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#anexoi).

Nesta 6ª etapa, os campos sinalizados com um asterisco (\*) são de preenchimento obrigatório. Ao preenchê-los, juntamente com os demais campos necessários, a OS será criada:

![Imagem 7: Nesta 6ª etapa, os campos sinalizados com um asterisco (*) são de preenchimento obrigatório. Ao preenchê-los,…](https://ajuda.sankhya.com.br/hc/article_attachments/360086627993)

No campo **"Dt/Hr Limite"** informe a data máxima em que a OS deverá ser executada.

O campo **"Responsável"** é preenchido automaticamente no lançamento da OS.

O campo **"Solicitante"** também será preenchido automaticamente no lançamento da OS, porém, poderá ser modificado caso necessário.

O **"Status"** refere-se à como a OS se encontra (pendente, aguardando retorno do cliente etc).

A **"Dt.Chamada"** será preenchida automaticamente no lançamento da OS.

Temos também **"Tempo Previsto"** em que a OS deverá ser executada.

Descreva no campo **"Problema"**, com detalhes, qual o problema a ser solucionado pela OS.

Informe também a **"Previsão"** em que a OS deverá ser executada.

No campo **"Classificação"** temos as seguintes opções:

- **Conformidade:** Quer dizer que encontra-se dentro do previsto (em uma OS de FAP, execução dentro do escopo acordado para o projeto, irá abater o saldo do projeto);
- **Não Conformidade:** Foge do previsto, não está em acordo (um retrabalho, um erro do produto ou do banco de dados);
- **Serviços Complementares:** Serviço extra ao que está acordado (em uma OS de FAP, execução fora do escopo do projeto, não irá abater o saldo do projeto).

O campo **"Motivo"** deverá ser preenchido com a razão do envio da OS (se é bonificação, customização, previsto/conformidade etc).

Em relação ao campo **"Status Sub OS"**, informe como a sub-OS se encontra (pendente, aguardando retorno do cliente etc).

O campo **"Prioridade"** é de livre preenchimento, mas possui um comportamento significativo no sistema quando o lançamento da OS está dentro das regras do SLA.

Utilize o campo **"Relacionada à OS"** para estabelecer uma relação com outra OS.

Caso a OS esteja vinculada à um projeto pré-cadastrado, informe a mesma no campo **"Projeto"**.

Sendo necessário, você pode retornar a qualquer passo, clicando nos link's correspondentes ao passo desejado no alto da tela. Observe como executamos abaixo:

[GIF animado: Imagem 8: Sendo necessário, você pode retornar a qualquer passo, clicando nos link's correspondentes ao passo desejado no alto da…](https://ajuda.sankhya.com.br/hc/article_attachments/360085453174)

Depois de preenchidos os dados acima, clique no botão **"Salvar"** para finalizar a inclusão da nova OS.

**Nota:** quando finalizada a inclusão de uma OS, não será possível realizar sua exclusão.

Outro recurso oferecido pelo sistema é o bloqueio de envio de Ordens de Serviço à funcionários afastados ou de férias. Este recurso é acionado através do parâmetro **"Aceita enviar OS para executante indisponivel - SERVEXECINDSP"**.

Com este parâmetro desabilitado, o sistema verificará através da **"Data Início"** e **"Data Fim"** da **"Ocorrência"** se a pessoa está ou não indisponível ao trabalho, não permitindo o lançamento de OS's à funcionários indisponíveis, até que estes retornem às suas atividades. Quando o parâmetro estiver habilitado, não será realizada nenhuma verificação e, assim, será permitido o lançamento de OS para usuários que estejam indisponíveis.

**Observação:** para que o processo ocorra desta forma, é necessário que o funcionário esteja vinculado à um usuário do sistema pelo menu **"Arquivos/Controle de Acesso/Usuários"** do MGE Pessoal.

**Nota:** ao chegar ao passo 6, o sistema buscará o Centro de Resultado através da Negociação; se for contrato, o sistema trará o Centro de Resultado do Contrato. Se pedido, trará o Centro de Resultado do Pedido. Se FAP, trará o Centro de Resultado da FAP, porém, se a FAP não possuir Centro de Resultado, trará o Centro de Resultado do pedido ligado à FAP.

Na tela de Projeto, ao incluir uma nova FAP, será preenchido o campo Centro de Resultado com o valor do Centro de Resultado do pedido ligado à FAP, podendo-se modificar o valor do Centro de Resultado na tela de Projeto.

O sistema permitirá ainda a visualização dos perfis dos usuários **"Solicitantes"** e **"Executantes"** da Ordem de Serviço. Para visualizar os perfis do usuário Solicitante, é necessário prosseguir com os seguintes passos:

- Na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), selecione o **"Parceiro"** desejado; em seguida, na aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontatos), defina o **"Contato utilizado na Ordem de Serviço"** e efetue a inserção dos perfis para este, utilizando a sub-aba Perfil do Contato.

**Observação:** a sub-aba Perfil do Contato somente estará visível no modo de **"Edição"**; no modo **"Grade"** esta aba não poderá ser visualizada.

[GIF animado: Imagem 9: Observação: a sub-aba Perfil do Contato somente estará visível no modo de "Edição" ; no modo "Grade" esta aba não…](https://ajuda.sankhya.com.br/hc/article_attachments/360086632073)

- Na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), selecione o usuário que terá vínculo com o contato do Parceiro e, em seguida, preencha os campos **"Cód. Parceiro Perfil"** e **"Contato Perfil"** (localizados na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) da tela mencionada) de acordo com os respectivos Parceiro e Contato.
- Com as configurações acima efetuadas, ao lançar uma Ordem de Serviço utilizando o usuário ligado ao Contato do Parceiro, os campos Solicitante ou Responsável presentes na tela da Ordem de Serviço, serão link's de acesso à uma janela, que exibirá os dados cadastrados no Perfil do Contato do Parceiro.

Você pode enviar a OS por e-mail através do ícone **"E-mail"**, localizado no Cabeçalho da OS. Além disto, será possível editar o texto que é enviado no e-mail da OS; para isto, crie um arquivo com o nome **"email.txt"** e coloque-o no diretório informado no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"** (Exemplo: D\temp\teste\modelos\). O arquivo **".txt"** deve seguir uma estrutura, e informar tag's HTML dentro dele. Trouxemos um exemplo de estrutura:

text/html

Teste envio e-mail - (OS: ${numos}) \*\* esse trecho é o que vai no campo assunto do email \*\*

<HTML>

<b>Olá,</b>

<p>Este é um email de exemplo para demonstrar como o arquivo deve ser escrito.</p>

<p><font color=1100EE><b>Obrigado pela atenção!!!</b></font></p>

</HTML>

**Nota:** a informação entre '\*\*' (asteriscos), é um comentário para identificar que o texto que fica entre **"text/html"** e **"<HTML>"** é o assunto que será descrito nos e-mail's.

**Observação:** na tela **"Contratos e Serviços > Ordem de Serviço > Ordem de Serviço"**, caso o Parceiro possua projetos pendentes, se o parâmetro **"Exibe lista de projetos pendentes na OS - EXIBPROJPENDOS"** estiver habilitado, um alerta informando sobre estes projetos pendentes será apresentado; caso o parâmetro esteja desativado, o alerta não será exibido.

**Nota:** caso o parâmetro **"Mostrar Número da OS mesmo em Contrato Padrão -  MOSTRARNUMOS"** esteja desabilitado, ao visualizar a Ordem de Serviço aberta, sua respectiva numeração não será exibida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Salvando Alterações na OS

Caso seja necessário realizar alguma alteração na OS, faça as alterações e acione o botão **"Salvar OS"**, isto para a descrição do que será tratado na OS.

![Imagem 10: Caso seja necessário realizar alguma alteração na OS , faça as alterações e acione o botão "Salvar OS" , isto para a…](https://ajuda.sankhya.com.br/hc/article_attachments/360085457494)

Se a alteração ocorrer em um item da OS, clique no botão **"Salvar"** que encontra-se no cabeçalho do item.

![Imagem 11: Se a alteração ocorrer em um item da OS , clique no botão "Salvar" que encontra-se no cabeçalho do item.](https://ajuda.sankhya.com.br/hc/article_attachments/360085457814)

**Importante:** apenas o responsável da OS poderá salvar os dados alterados na descrição da OS e, apenas os executantes dos itens poderão realizar modificações nos itens da OS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Criando uma Sub-OS

Para criar uma nova Sub-OS, acione a opção **"Nova Sub-OS"** no Cabeçalho do Item, informando o **"Serviço Previsto"** e clique em **"Próximo"**.

![Imagem 12: Para criar uma nova Sub-OS , acione a opção "Nova Sub-OS" no Cabeçalho do Item , informando o "Serviço Previsto" e…](https://ajuda.sankhya.com.br/hc/article_attachments/360085458514)

**Importante:** em algum casos é exibida a mensagem: **"Natureza não encontrada para a negociação."**; nestes casos, é necessário que a Natureza seja informada no contrato para seguimento na criação da Sub-OS.

Selecione o novo executante do item e, em seguida, preencha os demais dados solicitados e obrigatórios.

![Imagem 13: Selecione o novo executante do item e, em seguida, preencha os demais dados solicitados e obrigatórios.](https://ajuda.sankhya.com.br/hc/article_attachments/360086633213)

Feito o devido preenchimento das informações obrigatórias da tela, clique em **"Salvar"** para que a Sub-OS seja criada.

**Observação:** caso o parâmetro **"Checar horário de execução? - CHECHORAEXECOS"** esteja habilitado, será realizada a validação de horários no lançamento dos itens da Ordem de Serviço, de modo que não será possível a inclusão de novos itens com horários conflitantes. Suponhamos o seguinte lançamento:

1º item com o seguinte horário: 15:00h---------16:00h

2º item com o seguinte horário: 15:10h---------15:50h

Com o referido parâmetro ativado, um lançamento de itens similar à este exemplo, não poderá ser salvo. Caso esteja desativado, o lançamento de itens na Ordem de Serviço, mesmo com conflito de horários, será permitido. Por padrão, este parâmetro é apresentado ativado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Salvando e Encaminhando uma Sub-OS

Depois que você executa seu item na OS, é necessário preencher o tempo gasto. Para isto, preencha no campo **"Solução"** o que foi feito no item da OS, além de informar os campos **"Data Execução"**, **"Hora Inicial"**, **"Hora Final"** e **"Intervalo"** (caso tenha) e, em seguida, clique no botão **"Salvar"** e, logo depois, em **"Encaminhar"** para que seja criado um novo item para outro executante.

**Nota:**quando um item é encaminhado, o item aberto será fechado. Já no processo de criar uma Sub-OS, o item aberto não sofre alteração.

**Observação:** o Parâmetro **"Valida horário de execução de serviço para o mesmo executante - VALIDADHEXECUSU"** quando habilitado, não permitirá que sejam lançados apontamentos com o mesmo horário para Parceiros iguais ou diferentes. Quando desabilitado, será permitido tal lançamento mas, com a condição do Parceiro ser diferente, ou seja, pode-se lançar apontamentos com o mesmo horário porém com Parceiros diferentes.

Informe o **"Serviço Previsto"** e clique no botão **"Próximo"**.

**Importante:** em alguns casos, aparece a mensagem **"Natureza não encontrada para a negociação."**; nestes casos, é necessário que a Natureza seja informada no contrato para seguimento no encaminhamento da Sub-OS.

Depois de adequadamente preenchidos os campos obrigatórios e necessários, clique em **"Salvar"** para que a Sub-OS seja encaminhada.

Ao preencher os campos **"Data execução"**, **"Hora Inicial"**, **"Hora Final"** e clicar no botão **"Salvar"**, caso seja o último item aberto da OS a ser fechada, serão apresentadas as opções a seguir no cabeçalho da OS:

[GIF animado: Imagem 14: Ao preencher os campos "Data execução" , "Hora Inicial" , "Hora Final" e clicar no botão "Salvar" , caso seja o último…](https://ajuda.sankhya.com.br/hc/article_attachments/360085458634)

- **Salvar e Fechar OS** **-** Esta opção irá salvar a alteração feita na Sub-OS e finalizar a OS.
- **Salvar e Abrir Sub-OS** **-** Quando escolhida esta opção, a alteração feita na Sub-OS será salva e abrirá uma nova Sub-OS para o próprio executante.
- **Salvar e Encaminhar** **-** Esta irá salvar a alteração feita na Sub-OS e abrirá a tela de encaminhamento de uma Sub-OS à outro executante.

**Nota:** a ordenação do histórico na OS é diferente da ordenação na tela de [Pendências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604254-Pend%C3%AAncias). No histórico dentro da OS, a ordenação é cronológica, ou seja, referente à ordenação da data de execução, com itens sem data listados no final do histórico; já nas Pendências, a ordenação é através do **"Nro do item da OS"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Adicionando Anexos à OS

Através do link disponibilizado no lado superior direito da tela, realize o adendo de um arquivo à Ordem de Serviço.

[GIF animado: Imagem 15: Através do link disponibilizado no lado superior direito da tela, realize o adendo de um arquivo à Ordem de Serviço .](https://ajuda.sankhya.com.br/hc/article_attachments/360085458734)

Será aberta uma tela onde você realiza a **"Seleção"** do arquivo, informa sua **"Descrição"**, e sua correspondente **"Data de Expiração"**. O parâmetro **"Politica de expiração de Anexos em OS - SERVANEPOL"** define os limites de tempo de expiração de acordo com o tamanho do arquivo em bytes. Por exemplo:

Através da configuração **"<2:0, <10:15, >10:3"**, arquivos menores que 2Mb possuem data de expiração livre. Arquivos menores que 10Mb podem expirar em no máximo 15 dias, e os maiores que 10Mb podem expirar em no máximo 3 dias.

Além disto, você também inserir um texto que descreva um link de um arquivo ou página. É possível trabalhar-se com os seguintes formatos de link:

- <http://dominio.com/arquivo.pdf>
- <ftp://servidor/arquivo.pdf>
- https://dominiossl.com/arquivo.pdf

**Observação:** o parâmetro **"Validar se o LINK incluido no anexo tem um formato - VALIDALINKANEXO"** quando habilitado, valida se o formato do link inserido corresponde ao formato padrão de URL; caso não esteja, será apresentada uma mensagem informando sobre tal incompatibilidade e o anexo não será salvo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Regra para um Pedido ser apresentado para Lançamento de OS

- O Tipo Movimento (TGFCAB.TIPMOV) deverá ser = **'P'** (Pedido de venda);
- O Pedido deverá estar **"Confirmado"**;
- O Parceiro do Pedido deverá ser o mesmo Parceiro selecionado para lançamento de OS;
- O Pedido não poderá estar envolvido em uma FAP, ou seja, se houver vínculo do pedido com uma FAP, ele não será apresentado para lançamento da OS por pedido.
- Caso o parâmetro **"Naturezas para Direito de Uso - SERVFATDUNAT"** possua algum valor, então a natureza do pedido (TGFCAB.CODNAT) deverá ser diferente dos valores previstos no parâmetro.

Por exemplo, considerando que o parâmetro possua o valor **"102030, 304050"** e o pedido tenha a Natureza (TGFCAB.CODNAT) igual a **"456030"**, então o pedido será apresentado. Se o pedido tiver a Natureza igual a **"102030"** ou a **"304050"**, então ele não será exibido.

**Nota:** caso a Natureza do pedido for igual a **"0"** (zero), então o parâmetro será ignorado.

- Se o parâmetro **"Grupos TOPs p/ lançamento de OS - SERVGTOPSOS"** possuir algum valor definido, então o grupo da TOP do pedido deverá estar na lista.
- Caso a TOP do pedido faça parte da configuração do parâmetro **"TOPs p/ faturamento de Serviços - SERVTOPSFAT"**, então:

1. A data de validade do pedido (TGFCAB.DTVAL) deverá estar vazia ou com uma data futura;
2. O total de horas de conformidade já realizadas do pedido (em outras OS's) deverá ser menor que o total negociado no pedido. O total negociado é a soma TGFITE.QTDNEG para os itens do pedido cuja unidade (TGFITE.CODVOL) seja igual ao parâmetro **"Unidade de referência para conversão hora/minuto - SERVUNIREFERENC"** (o padrão é H) e que o grupo de produtos seja igual ou da hierarquia do grupo constante no parâmetro **"Grupo de Serviços para Lançamento de OS p/ Pedido - GRUPOSERVSOFT"**.
   Com base no trecho acima, entende-se que o sistema faz a conversão hora/minuto na OS, de acordo com a informação do parâmetro SERVUNIREFERENC e a unidade do produto lançado no Pedido. Em outras palavras, caso o Produto tenha sido lançado no Pedido com a Unidade UN, o parâmetro SERVUNIREFERENC deverá ser preenchido com a mesma Unidade UN para que o sistema calcule o Saldo do Pedido.

- Caso a TOP do pedido não faça parte da configuração do parâmetro **"TOPs p/ faturamento de Serviços - SERVTOPSFAT"**, então, o pedido deverá estar pendente (TGFCAB.PENDENTE = 'S').

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Regra para os Produtos e Serviços serem apresentados para Lançamento da OS

- Os serviços serão aqueles presentes no pedido que façam parte do grupo de produtos informados no parâmetro **"Grupo de Serviços para Lançamento de OS p/ Pedido - GRUPOSERVSOFT"** e, cuja unidade seja igual ao parâmetro **"Unidade de referência para conversão hora/minuto - SERVUNIREFERENC"** (padrão é H).
- O valor do parâmetro Grupo de Serviços para Lançamento de OS p/ Pedido - GRUPOSERVSOFT pode ser um grupo sintético; neste caso, todos os grupos filhos serão utilizados.
- Os produtos serão aqueles presentes no pedido e que não fazem parte da configuração realizada no parâmetro Grupo de Serviços para Lançamento de OS p/ Pedido - GRUPOSERVSOFT.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Origem de Atendimento

Esta configuração permite um maior controle e acompanhamento interno das Ordens de Serviço; ela é feita informando o campo **"Origem"**, na abertura da OS (etapa 6 de seu lançamento, campo Origem), ou mesmo depois que esta já encontra-se aberta.

![Imagem 16: Esta configuração permite um maior controle e acompanhamento interno das Ordens de Serviço ; ela é feita informando o…](https://ajuda.sankhya.com.br/hc/article_attachments/360085459074)

A Origem do Atendimento está diretamente ligada à configuração realizada no parâmetro **"Máscara para origem da chamada - MASCORIGATEND"**, onde você cria a máscara a ser utilizada no cadastro da origem do atendimento. Observe como cadastrar uma nova origem de atendimento:

- Primeiramente, no parâmetro MASCORIGATEND, defina a máscara para a origem. A configuração da máscara deverá ocorrer da seguinte forma:
- Acesse a tela Preferências: e, no campo **"Tipo"**, selecione a opção **"Texto"** para que se possa então digitar a máscara na caixa de texto.

**Importante:** a máscara deverá ser definida com **"\" (barra)** e **"."(ponto)**, como por exemplo, **"99\.99\.99"**.

A configuração será feita de acordo com a necessidade de sua empresa, sendo que a máscara poderá ter no máximo 4 níveis que somados, não deverão ultrapassar 9 dígitos. De acordo com esta máscara serão cadastradas as origens.

O tamanho dos graus (pai, filho, neto e bisneto) definirão o número de dígitos que devem conter cada grau, a barra **"\"** separará os níveis. Com isso, no exemplo anterior **"99\.99\.99"**, a máscara apresenta três níveis (pai, filho e neto), sendo que foi definido no nível 1 (pai) dois dígitos (99), no nível 2 (filho) dois dígitos fora o ponto **"."** (99) e no nível três (neto), mais dois dígitos fora o ponto **"."** (99). Feita a definição da máscara, o segundo passo é o cadastro da origem:

- Acesse a tela [Origem de Atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604294):

![Imagem 17: Acesse a tela Origem de Atendimento :](https://ajuda.sankhya.com.br/hc/article_attachments/360086633993)

A máscara configurada no parâmetro MASCORIGATEND definirá a forma de inserção dos níveis e graus da nova origem, no campo **"Código"** desta tela. A tela segue o padrão de cadastro **"Analítico"** e **"Sintético"** existente no sistema, permitindo a inclusão, exclusão e alteração dos cadastros.

O campo **"Descrição"** é de livre digitação e, juntamente com o código, identificará na Ordem de Serviço a origem do atendimento. Por exemplo, Telefone, Chat, Whats App Empresa, E-mail etc.

A Origem de Atendimento, também pode ser utilizada na Pré-Venda. Esta definição é realizada através do campo **"Tipo"**, que definirá se a nova origem poderá ser empregada na **"Pré-Venda"**, no **"Atendimento"** ou em **"Ambos"**.

Este cadastro respeitará a hierarquia **"pai/filho"**, ou seja, o sistema verificará o Tipo definido para o pai e não permitirá que o filho seja cadastrado com outro Tipo senão o do pai. Se isso ocorrer, será emitida a mensagem:

**"O Tipo do registro filho não pode ser diferente do Tipo do registro pai"**

Contudo, se o Tipo definido para o pai for igual a Ambos, será possível cadastrar os filhos tanto como Atendimento, quanto como Pré-Venda.

Uma vez cadastrado o pai, não será possível mudar o seu Tipo e, neste caso, o sistema emitirá a mensagem:

**"O Tipo do registro pai não pode ser alterado"**

Uma vez cadastrada a **"Origem"** você pode, no lançamento de uma OS, classificá-la quanto à sua origem, seguindo as configurações realizadas.

Como já mencionamos, no passo 6 do lançamento de OS, você pode preencher o campo Origem, selecionando a origem desejada através da pesquisa. Nela serão apresentadas as origens de atendimento que estão **"Ativas"**, Sintéticas e Analíticas, e que possuam o Tipo igual a Atendimento ou Ambos. As origens de Tipo Pré-Venda, poderão ser visualizadas apenas na tela de **"Negociação"** (Pré-Venda).

Se depois de incluir uma origem for necessário alterá-la para outra, antes de salvar a OS, bastará clicar novamente sobre o campo **"Origem"** para selecionar outra origem na tela **"Pesquisar Origem do Atendimento"**. Logo à frente do campo **"Origem"**, encontra-se um ícone com o formato de **"borracha"**, através da qual será possível **"limpar"** o conteúdo do campo, nos casos em que não desejar-se mais informar a origem da OS.

A informação no campo Origem do cabeçalho não poderá ser apagada; somente o **"Responsável pela OS"** poderá alterá-lo através do botão de **"Pesquisa"** (lupa), que abrirá novamente a tela Pesquisar Origem do Atendimento, para escolha de nova origem.

**Observação:** localizado à frente do campo **"Contato"**, tem-se o link **"Dados do contato"** que, ao ser acionado, apresentam o **"Nome"**, **"Cidade"** e **"Telefone"** do referido contato. Para que estes campos sejam alimentados, os mesmos deverão ser preenchidos no lançamento de uma OS de Atendimento (são campos do cabeçalho da OS), onde os dados são gravados na tabela TCSOSE e poderão ser visualizados no link mencionado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Anexo I

Para realizar a inserção de um **"Produto"** e um **"Serviço"** à um **"Executante"**, é necessário acessar a tela [Serviços por Executante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113153).

No lado esquerdo da tela, selecione diretamente o **"Executante"**, ou ainda o **"Grupo"** ao qual o executante pertence.

![Imagem 18: No lado esquerdo da tela, selecione diretamente o "Executante" , ou ainda o "Grupo" ao qual o executante pertence.](https://ajuda.sankhya.com.br/hc/article_attachments/8527072304279)

Uma vez selecionado o executante, do lado direito da tela, podemos visualizar os **"Produtos"** e **"Serviços"** que já estão vinculados aos executantes, ou que poderão ser vinculados através do botão de inclusão ![Imagem 19: Uma vez selecionado o executante, do lado direito da tela, podemos visualizar os "Produtos" e "Serviços" que já estão…](https://ajuda.sankhya.com.br/hc/article_attachments/8526892328599), e salvos através do botão ![Imagem 20: Uma vez selecionado o executante, do lado direito da tela, podemos visualizar os "Produtos" e "Serviços" que já estão…](https://ajuda.sankhya.com.br/hc/article_attachments/8526858507543).

![Imagem 21: Uma vez selecionado o executante, do lado direito da tela, podemos visualizar os "Produtos" e "Serviços" que já estão…](https://ajuda.sankhya.com.br/hc/article_attachments/8527057336215)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Orçamento

No cabeçalho da OS, podemos trabalhar com Orçamento. Para utilização de tal funcionalidade, é necessário realizar a configuração dos parâmetros abaixo:

- **"Utiliza o parceiro atendido no módulo OS-USAPARCATEND"** deve estar ligado para que a opção Orçamento seja apresentada na tela.
- **"Edição de preço em orçamento de OS - EDITAPRECOORC"** marcado como **"Editável"**;
- **"Mostrar preço em orçamento de OS? - MOSTRARPRECOORC"** habilitado;
- **"Nota modelo de orçamento para assistência técnica - MODORCASSITTEC"** preenchido com o Número Único do Modelo de Nota, configurado previamente na tela **"Comercial > Consulta > Modelo de Notas e Pedidos"** que servirá de referência para geração do orçamento;
- **"Utilizar Tipo de Atendimento em orçamentos de OS? - USATPAORCOS"** habilitado.

**Importante:** vale salientar que, quando o parâmetro USATPAORCOS estiver ligado, será gerada apenas uma Nota na criação e aprovação do Orçamento. Porém, quando estiver desligado, o sistema terá uma tratativa para gerar requisições de produto com e/ou sem garantia, conforme a marcação **"Garantia cobre?"** de cada produto do orçamento e as notas modelos informadas nos parâmetros MODREQCOMGAR e MODREQSEMGAR.

[GIF animado: Imagem 22: Importante: vale salientar que, quando o parâmetro USATPAORCOS estiver ligado, será gerada apenas uma Nota na criação e…](https://ajuda.sankhya.com.br/hc/article_attachments/360085459694)

Ao acionar a opção **"Orçamento"**, será aberta uma tela, contendo as abas **"Dados Orçamento"** e **"Dados Parceiro"**.

O botão **"Aprovar"** é apresentado quando você possuir um vendedor vinculado em seu cadastro; caso o vendedor não esteja vinculado, este botão não será apresentado.

**Aba Dados Orçamento**

Os dois campos iniciais, são de preenchimento obrigatório; os demais serão informados de acordo com a necessidade do orçamento.

Informe o **"Tipo de Atendimento"** para o produto a ser inserido no orçamento.

Preencha o campo **"Produto"** com o produto a ser acrescentado no orçamento.

**Aba Dados Parceiro**

Nesta aba serão apresentados os Dados do Parceiro para o qual está sendo realizado o orçamento.

Ambas as abas desta tela (Dados Orçamento e Dados Parceiro), possuem em seu rodapé o botão **"Totais Por Tipo de Atendimento"**; este, quando acionado, abrirá  uma tela com este mesmo nome apresentando os Tipos de Atendimento realizados para este Parceiro e seu somatório.

**Nota:** quando o parâmetro **"Orçamento pendente conforme configuração TOP? - ORCPENDENTETOP"** estiver habilitado, fará com que o Orçamento siga a marcação **"A nota fica como pendente"** da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) , aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)); caso esta marcação esteja efetuada, o lançamento gerado pelo Orçamento, será apresentado como **"Pendente"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## OS Web pelo número de Série

É possível ainda, realizar a abertura de Ordens de Serviço Web por meio do Número de Série dos Produtos (produtos estes, utilizados nos Contratos).

Para que este procedimento seja possível, efetue a ativação dos seguintes parâmetros:

- **Abertura de OS Web pelo Nro de série. - OSWEBPESQSERIE:** Quando ativado, habilitará a pesquisa por Contrato e Produto a partir do número de série.
- **Descrição para o campo Contrato na OS Web. - DESCAMPCONTRATO:** Configure o campo que será visualizado na descrição do Contrato (campos da tabela TCSCON, incluindo Campos Adicionais).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## OS aberta no Sankhya Om e Portal do Cliente

Uma vez que a Ordem de Serviço esteja aberta no Sankhya Om, temos o link Imprimir que, quando acionado, terá a geração da Ordem de Serviço no formato PDF.

Através do Portal do Cliente, acessado por meio do [Sankhya Place](http://place.sankhya.com.br/#login), desde que você possua os devidos acessos, é possível realizar a consulta da situação das Ordens de Serviço, o lançamento das mesmas, bem como a verificação do histórico dos atendimentos efetuados.

![Imagem 23: Através do Portal do Cliente , acessado por meio do Sankhya Place , desde que você possua os devidos acessos, é…](https://ajuda.sankhya.com.br/hc/article_attachments/8980512799767)

**Importante:** tanto no lançamento de Ordens de Serviço realizado no Sankhya Om ou na consulta feita por meio do Portal do Cliente, existe a possibilidade de visualizar/imprimir o documento em formato PDF; para que seja possível realizar tal procedimento, é necessário que os arquivos **"osPortal.jrxml"** e **"osPortal\_itens\_ossub.jrxml"** sejam copiados para o diretório de modelos definidos no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**. Estes arquivos são obtidos através da [Central de downloads Sankhya](http://downloads.sankhya.com.br/) na seção Ferramentas. É essencial mencionar que os dois arquivos citados são disponibilizados pela baixa de um único arquivo denominado **"modelos\_osportal.zip"**. Além disto, você pode modificar estes documentos por meio do iReport; o relatório principal osPortal.jrxml contém uma referência para a imagem logo-sk.gif a ser modificada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)

## Gerar uma Requisição através de uma OS

Você pode criar uma requisição por meio de uma OS, para tanto, é necessário realizar as seguintes configurações:

- O parâmetro **"Usa número da O.S. na requisição - SERVNUMOSREC"** deverá estar habilitado;
- Informe no parâmetro **"TOP usada p/ Requisições em OS - SERVTOPREQ"** o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) a ser utilizado para o lançamento da requisição, sendo que este necessita conter o tipo de movimento **"Requisição"**.

Referente ao parâmetro **"Exibe estoque prod na Resuisição pela tela de OS - EXIBEESTQPRODOS"**, ao habilitá-lo, o sistema exibirá um pop-up em HTML5 após clicar na lupa de pesquisa dos Produtos da Requisição.

Assim, no campo de pesquisa, você pode procurar pelos produtos da requisição.

Após isto, será aberto o pop-up **"Procurar por"** para que os produtos possam ser carregados.

**Observação:** para inserir o Produto, basta selecioná-lo, definir a quantidade desejada e, em seguida, clicar em **"OK"** ou dar um duplo clique na linha do mesmo.

**Nota:** ao acionar o botão **"Cancelar"** o pop-up será fechado e nenhum produto será selecionado para a requisição.

Com o parâmetro **"Apresentar produtos do contrato da OS na requisição - REQPRODCONT"** habilitado, o sistema exibirá na tela de Requisição de Ordem de Serviço apenas os produtos pertencentes ao contrato da Requisição.

**Observação:** crie um Modelo de Nota (tela **"Comercial > Consulta > Modelo de Notas e Pedidos"**) configurado com a Empresa que está realizando a solicitação da requisição e o Tipo de Operação - TOP mencionado anteriormente. Vincule o número único do Modelo de Nota criado ao parâmetro **"Modelo p/ Requisições em OS's - SERVMODREQ"**:

![Imagem 24: Observação: crie um Modelo de Nota (tela "Comercial > Consulta > Modelo de Notas e Pedidos" ) configurado com a Empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/360085460034)

Tendo sido realizada a criação do Modelo de Nota, efetue o registro da OS de modelo através dos passos abordados na rotina [Lançamento de OS por Modelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604714). Deste modo, ao realizar o lançamento da OS de modelo tem-se a exibição da tela Ordem de Serviço posicionada no referido registro.

Localizado no lado inferior esquerdo da tela, está o botão **"Lançar Requisição"** que, ao ser acionado, permite informar os dados pertinentes ao registro da requisição:

[GIF animado: Imagem 25: Localizado no lado inferior esquerdo da tela, está o botão "Lançar Requisição" que, ao ser acionado, permite informar…](https://ajuda.sankhya.com.br/hc/article_attachments/360085460254)

Ao finalizar o preenchimento dos referidos dados, utilize o botão **"Salvar"** para confirmar o registro da requisição:

Através do [Portal de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025394173-Portal-de-Mov-Internas) pode-se localizar a requisição criada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS#top)
