---
id: "360044597254"
titulo: "Controle de Produtos com Número de Série Global"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597254-Controle-de-Produtos-com-N%C3%BAmero-de-S%C3%A9rie-Global"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:12Z"
rotulos: ["Produtos", "Configuração", "Controle de Produtos com Número de Série Global", "Controle de Produtos com Número de Série Global manual", "Segurança", "Ocorrências", "Estoque", "USACBGLOBAL", "TIPCALCNSGLOBAL", "DIGOCORBLOQSER", "LOCALCURINGAFAT", "USANSFABRIC", "TEMMPCOMPRA", "TEMMPREQ", "TOPVENCOMPINDIV", "HABSUPORTEKITSW", "TEMMPVENDA", "TEMMPTRAN"]
---

# Controle de Produtos com Número de Série Global

Esse controle é utilizado para rastrear e fazer o controle dos produtos da empresa, onde cada produto é localizado por um número de série único e global, que é gerado para todos os produtos que entram na empresa, além de controlar o produto por série também é possível fazer o controle de série do fabricante e de locais para alguns produtos pois, em alguns casos, o número de série do fabricante é controlado pelo governo.

O número de série do fabricante indica o número de série de um determinado produto, tais como "Impressoras Fiscais", "Freezer" etc. Sendo obrigatório em alguns itens que, por exigência fiscal, deve inclusive constar na nota de venda.

---

![Imagem 1: Esse controle é habilitado pelo parâmetro "Usa Número de Série Global - USACBGLOBAL" .](https://ajuda.sankhya.com.br/hc/article_attachments/16202571799191) Esse controle é habilitado pelo parâmetro **"Usa Número de Série Global - USACBGLOBAL"**.

**Importante:** o módulo [Produção/W](https://ajuda.sankhya.com.br/hc/pt-br/sections/360007784253-Produ%C3%A7%C3%A3o-W) não suporta a utilização da série global.

O controle de série global do Sankhya Om apresenta os campos contidos no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional).

Os produtos que fazem parte do processo de série global devem estar configurados com Controle Adicional de Estoque = Série e devem ter a marcação **"Valida Cód. Barra de Nro Série Global"** realizada. Essa marcação indica que o produto utiliza série Global. 

O campo **"Notificação para conferência"** é  utilizado na tela de conferência de série global. Ao fazer a conferência de uma série desse produto o sistema irá exibir uma mensagem com o texto informado nesse campo.

A marcação **"Exige Número de série do Fabricante"** é exibida somente quando o parâmetro **"Usa nro de série do fabricante - USANSFABRIC"** estiver habilitado, e é utilizada para indicar que, ao fazer a conferência de uma nota de compra de uma série desse produto, você deverá informar também o número de série do fabricante.

![Imagem 2: A marcação "Exige Número de série do Fabricante" é exibida somente quando o parâmetro " Usa nro de série do fabricante…](https://ajuda.sankhya.com.br/hc/article_attachments/4407442370839)

Nos itens da nota, para o produto controlado, o sistema apresenta o botão **"Números de Série"**. Na tela aberta através desse botão, é possível verificar a coluna **"Série do Fabricante"**, a qual estará preenchida com a série informada no campo "Nro. De série do Fabricante", presente na tela de conferência de séries. As séries não serão apresentadas para pedidos porque as mesmas são geradas somente em notas.

![Imagem 3: Nos itens da nota, para o produto controlado , o sistema apresenta o botão "Números de Série" . Na tela aberta através…](https://ajuda.sankhya.com.br/hc/article_attachments/4407442419223)

O campo **"Tipo de série para NF-e"** indica qual a série que será apresentada junto com a descrição do item na impressão da nota. Se você escolher fabricante, será impresso o Nro. de série do fabricante; se deixar vazio ou escolher a opção padrão, o sistema irá imprimir o número de série global.

Para que as séries sejam impressas, independente de ser padrão ou fabricante, é necessário que nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) utilizada no lançamento, na opção **"Complemento p/ Itens da Nota (Web)"** localizada no botão **"Outras Opções"**, você inclua a variável Série nos campos em uso.

A ativação do parâmetro de chave USACBGLOBAL apresenta a marcação **"Número de Série Global - Transferência"** na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque) das TOPs de compra, venda e devoluções. Serão utilizados quatro tipos de notas para movimentar as séries, **"Nota de Compra"**, **"Nota de Venda"**, **"Devolução de Compra"** e por fim **"Devolução de venda"**. Se marcada, as ocorrências geradas serão relacionadas à transferência de produtos entre filiais, sendo assim, por exemplo, para transferências entre filiais, a empresa de origem deve fazer uma nota de venda com uma TOP de venda com essa marcação, e a empresa de destino deve fazer uma nota de compra com uma TOP de compra com a mesma marcação.

![Imagem 4: A ativação do parâmetro de chave USACBGLOBAL apresenta a marcação "Número de Série Global - Transferência" na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4407442614935)

Além dos menus **"Abrir Conferência"** e **"Abrir Conferência p/ Exclusão"** do botão Outras Opções da Central, mostra os menus Abrir Conferência p/ Exclusão e **"Abrir Conferência p/ Cancelamento ou Exclusão"** nas telas de Seleção de Documentos.

Caso seja lançada uma nota que contenha itens que utilizem validação por série global e a TOP não esteja marcada para baixar ou reservar estoque, o sistema não irá solicitar a conferência dos itens.

No intuito de rastrear os produtos da empresa, será feito um histórico com uma ocorrência para cada ação (alteração de Status) que a série está sujeita a sofrer, por exemplo: ao ser gerada uma nova série, ela já ganha sua primeira ocorrência **"Geração do número"** e ao vender essa série, o sistema gera um histórico com a ocorrência **"Expedição"**. Existem várias outras ocorrências e status para as séries dos produtos que poderão ser mais bem visualizadas no Diagrama de Fluxo de Status que, por sua vez, detalha quais ocorrências e quais status são lançados e alterados para cada ação tomada dentro do sistema.

Para garantir que as séries sejam movimentadas corretamente e com segurança, será necessário conferir essas séries constantemente, antes da confirmação da nota, antes de cancelar ou excluir uma nota, antes de remover itens que já estão conferidos, atualizando o Status da série e gerando um novo histórico para que, dessa forma, saibamos se uma série está disponível para movimentar ou não.

A marcação **"Inibe consulta de séries"** na aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana) do [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) definirá se o mesmo poderá visualizar as séries sugeridas no lançamento das Notas de Venda; caso o usuário não possa ter acesso às séries, o campo **"Controle"** não será visualizado na grade de itens.

Ao lançar uma nota de compra, quando forem incluídos produtos que tenham a marcação **"Valida Cód. Barra de Nro Série Global"** realizada, o sistema irá gerar os números de série de acordo com o padrão **"AANNNNNNNNDD"**, onde AA é o ano da nota (Data de negociação), NNNNNNNN é uma sequência e DD um dígito verificador de módulo 10 sobre AANNNNNNNN. A cada novo ano a sequência é reiniciada.

Caso o cliente deseje que os números de séries globais sejam gerados sem o dígito verificador, exemplo: AANNNNNNNN (onde A=Ano, N=Número Sequencial), é necessário que o parâmetro **"Tipo de cálculo para Nro. Série Global em notas de entrada - TIPCALCNSGLOBAL"** esteja com valor igual a **"Sem dígito Verificador"**.

Após a nota lançada, devemos imprimir as etiquetas (não poderá ser feito pelo Sankhya Om), fixar as etiquetas aos produtos e fazer a conferência dos produtos, para que assim consiga confirmar a nota. Se você tentar fazer a confirmação da nota sem conferir os produtos, o sistema mostra uma mensagem informando que é preciso fazer a conferência de todos os itens para realizar a confirmação.

**Observação:** com a marcação Valida Cód. Barra de Nro Série Global efetuada, ao emitir uma Nota de Requisição, o sistema não permitirá consultar as Séries disponíveis, sendo necessário digitar o Nro. Série manualmente.

Além do campo **"Números de séries"** dos itens da nota, as séries podem ser visualizadas na tela [Consulta de Séries](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119233-Consulta-de-S%C3%A9ries), localizada no menu **"Comercial > Rotinas > Série Global > Consulta de Séries"**.

Essa tela serve para consultar informações referentes à série. As mesmas podem ser buscadas através dos filtros da tela, como Nro. Série, Nro. Série Fabricante, Produto, Nro. Nota ou através do Status da série, caso você saiba.

**Nota:** ao clicar no botão Números de séries dos itens da nota, serão apresentadas as séries vinculadas à nota.  As séries não serão apresentadas no **"Número de série"** de **"Pedido"** porque elas são geradas somente em **"Notas"**.

Existe a possibilidade de trocar o número de série do fabricante através do botão **"Trocar Série Fabricante"** presente nessa tela. Basta filtrar a linha correspondente à série que deseja trocar, clicar no botão, informar a nova série e confirmar a operação.

![Imagem 5: Existe a possibilidade de trocar o número de série do fabricante através do botão " Trocar Série Fabricante" presente…](https://ajuda.sankhya.com.br/hc/article_attachments/4407442743191)

Para que esse botão seja apresentado na tela e seja possível trocar a série do fabricante, é necessário que o mesmo tenha o acesso especial **"Troca Num. de Série do Fabricante"** liberado. Além disso, a troca de número de série do fabricante somente poderá ser realizada se a série estiver com status em estoque.

A tela de conferência possui duas grades, uma superior mostrando as conferências que estão sendo feitas e uma grade inferior mostrando as conferências já confirmadas.

Na grade superior existem botões para remover item da grade, **"Confirmar conferência"** que confirma a conferência dos itens da grade superior (caso você não clique nesse botão após fazer a conferência e feche a tela ou o navegador, a conferência deverá ser refeita).

Se houver algum problema com o produto da série sugerida e for preciso utilizar outro, você poderá acionar o botão **"Trocar Num. Série Sugerido"**; assim, o sistema irá bloquear a série e pegará outra série disponível; caso não haja outra série, o sistema irá lançar mensagem de erro informando que não existem mais séries disponíveis.

Se o produto utilizar local e o local da nova série for diferente da anterior, o sistema irá lançar um novo item com as mesmas informações do item atual, porém com local e série diferente e quantidade negociada igual a 1.

Exemplo:

Há no local X 2 produtos. Porém, ao efetuar a venda desses dois produtos você deseja alterar uma dessas séries. Ao realizar essa operação, o sistema identifica que não há mais desse produto no local X e sim no local Y (para a mesma empresa). Então, ele usará essa série e acrescentará nos itens da nota uma linha, sendo uma referente à série BB do local X com quantidade negociada igual a 1 e a outra referente a série CC do local Y com quantidade negociada também igual a 1. O sistema só irá fazer desta forma caso não tenha séries disponíveis no mesmo local.

A troca do número de série global só ocorrerá com números de séries do fabricante que estão ligados com o mesmo código de empresa, ou seja, produtos que estão no estoque da mesma empresa.

Caso a série a ser trocada esteja cadastrada na tela de [Registro de Avarias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120333-Registro-de-Avarias), a mesma não pode ser trocada, pois ela pode possuir um valor de desconto devido à avaria.

Você pode fazer a conferência de alguns itens e clicar em confirmar conferencia e continuar a conferencia em outro momento.

As telas de Conferência de Série e Conferência de Série p/ Exclusão ou Cancelamento aparecem no menu de acessos **"Comercial > Rotinas > Série Global"**, mas não aparecem no menu do sistema, isso por que elas somente poderão ser abertas através do botão **"Outras Opções..."** das Centrais de Notas ou das telas de Seleção de Documentos.

Na grade inferior, quando a quantidade negociada de algum item ficar igual à quantidade conferida, a linha ficará com a cor **azul**.

Na grade inferior, também tem uma opção para **"Remover item conferido"**, o sistema irá mostrar uma tela para informar a série que será feito o cancelamento da conferência.

**Observação:** os campos de texto para inserção de números de séries nas telas de conferência foram projetados para serem usados com Leitor de Código de Barras, ou seja, suas funções são realizadas ao pressionar a tecla enter.

Quando o parâmetro **"Usa nro de série do fabricante -** **USANSFABRIC"** estiver habilitado, também será apresentada na tela de Conferência de Série Global (aberta pelo botão Outras Opções/Abrir Conferência) a coluna **"Série do Fabricante"**.

A tela Conferência de Série p/ Exclusão ou Cancelamento será usada sempre que for preciso excluir ou cancelar uma nota que já esteja com seus itens conferidos pela tela de Conferencia, a conferência para exclusão dura apenas 24hrs, ou seja, se um produto for conferido para cancelamento, mas não tiver sua nota cancelada nas próximas 24 horas, será necessário conferir novamente o item para cancelamento da nota.

A tela [Bloqueio de Números de Série Global](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108693) é específica para bloqueio e desbloqueio de números de série.

![Imagem 6: A tela Bloqueio de Números de Série Global é específica para bloqueio e desbloqueio de números de série .](https://ajuda.sankhya.com.br/hc/article_attachments/4407439318423)

Nessa tela será lido pelo leitor do código de barras ou digitado por você um número de série.  Ao preencher o campo número de série, o sistema trará o último status do número de série e apresentará na tela. Essa informação é apenas para consulta e não pode ser alterada. Aqui existe um botão de Bloqueio e um botão de Desbloqueio.

Para o Bloqueio, esee número de série obrigatoriamente deverá estar com status **"Em Estoque"** e para o Desbloqueio com status **"Bloqueado"**.

Ao bloquear, será gerado um histórico com ocorrência Bloqueio e status Bloqueado. Ao desbloquear, será gerado um histórico com ocorrência Desbloqueio e status Em Estoque. Ao bloquear ou desbloquear, o sistema atualizará a tela com o novo status da série.

**Observação:** se o parâmetro **"Digitar no campo ocorrência quando bloquear série - DIGOCORBLOQSER"** estiver habilitado e você solicitar o bloqueio de uma série, será apresentado um pop-up para que seja informada a ocorrência do bloqueio.

Para permitir ao vendedor informar a série do produto que deseja vender, estando o produto avariado ou não, existe na Central de Vendas, o campo **"Nro. Série"** na grade de itens. Esse campo é utilizado para efetuar transações com uma série específica e é liberado para digitação somente se o parâmetro USACBGLOBAL estiver habilitado, a nota/pedido for de venda e se o produto utilizar série global

Só será possível vender a série específica (preenchendo-a no campo Nro série da grade de itens), se a quantidade negociada não for diferente de 1 e se esta série não estiver pendente para outra nota. Ao confirmá-la, o sistema pegará automaticamente o código do local em que a série informada está e não permitirá alterar o local. Se a TOP estiver reservando ou atualizando estoque essa série será reservada.

Quando o produto está configurado para trabalhar com local, o sistema exige que o mesmo seja digitado durante o lançamento do item mas, ao fazer a venda, não sabemos informar em qual local está esse produto para retirada. Por isso, ao invés de digitar o local correspondente a cada série, devemos informar um local curinga. Esse local deverá estar informado no parâmetro **"Local curinga para lançamento de pedidos/notas - LOCALCURINGAFAT"**. Ao preencher o item com ele e salvar, o sistema irá preencher a série e irá alterar o campo **"Local origem"** para o local das séries. Se não tiver todas as séries no mesmo local, ele irá quebrar o item e irá lançar outro item com as outras séries dos demais locais e atualizar a quantidade negociada de acordo com as séries disponíveis nos locais.

Se no faturamento o Local de Origem for igual ao indicado no parâmetro LOCALCURINGAFAT o sistema também irá quebrar o item de acordo com a quantidade de séries disponíveis nos locais. Além disso, se no pedido estiver sendo utilizada uma série específica, na nota de venda gerada não será apresentado à série específica no campo Nro série. Nesse caso, a série poderá ser visualizada na tela aberta através do botão Números de séries da grade de itens.

**Observação:** o sistema não permite vender séries que estão bloqueadas.

Ainda em relação ao parâmetro LOCALCURINGAFAT, se as seguintes configurações estiverem efetuadas:

- O parâmetro LOCALCURINGAFAT estiver definido com o valor 196000000;
- O parâmetro **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** estiver ligado;
- O [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) for de Baixa;
- Se o CODLOCALORG (do pedido de venda) estiver definido no item e for igual ao CODLOCAL do parâmetro LOCALCURINGAFAT no item do pedido.

O sistema realizará uma verificação por meio da query denominada **"CentralFaturamento\_queLocaisComEstoque.sql"**. Essa consulta buscará o CODLOCALORG com o menor estoque, desde que o estoque naquele local seja maior ou igual à QTDNEG do item no Pedido.

Se o valor presente no parâmetro LOCALCURINGAFAT for igual ao definido no item do pedido, o sistema executará essa consulta e selecionará o local com o menor estoque, desde que esse estoque seja maior ou igual à QTDNEG.

---

**Alteração do título do painel de Matéria prima presente nos Itens da Nota**

Na tela de [Configuração de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota) será possível mudar o **"Título do painel matéria prima"** que aparece junto com a grade de itens da Central. Para isso, é necessário abrir a janela de edição da grade dos itens e informar o novo título no campo.

![Imagem 7: Na tela de Configuração de Layout da Nota será possível mudar o "Título do painel matéria prima" que aparece junto com…](https://ajuda.sankhya.com.br/hc/article_attachments/4407442899735)

O campo somente será apresentado durante a edição da grade do item caso o parâmetro **"Habilitar o suporte a kit no SankhyaW? -** **HABSUPORTEKITSW"** esteja ligado. Outros parâmetros também deverão estar habilitados, variando de acordo com o tipo de movimento do layout:

- Para Compra é necessário habilitar o parâmetro **"Tem aba mat.prima na central atendimento ao Forn.? -** **TEMMPCOMPRA"**;
- Para Venda, Pedido de Venda ou Devolução de Venda é necessário habilitar o parâmetro **"Tem aba mat.prima na central atend. ao Cliente.? -** **TEMMPVENDA"**;
- Para Transferência é necessário habilitar o parâmetro **"Tem aba Mat.Prima na Transferência -** **TEMMPTRAN"**;
- Para Requisição é necessário habilitar o parâmetro **"Tem aba Mat.Prima na requisição? -** **TEMMPREQ"**;

Se o parâmetro USACBGLOBAL estiver habilitado, o Painel de séries da tela de [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtoshttps://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos) mostrará a coluna **"Avariado"** e o botão **"Ver detalhes da avaria"**.

A coluna **"Nro. Pedido Reserva"** somente será preenchida caso a série em questão esteja reservada para algum Pedido. Se a série não estiver em nenhum Pedido, a coluna aparecerá vazia.

Caso a série relacionada esteja avariada, será apresentada a linha em **vermelho** e o botão Ver detalhes da avaria ficará habilitado. Além disso, o mesmo será identificado como Avariado = Sim na coluna Avariado.

Ao clicar no botão Ver detalhes da Avaria, será apresentado na janela os detalhes dessa série avariada, como o número de cadastro da mesma, o % de desconto que será aplicado sobre a venda, um campo para observações e imagens do produto.

Se você clicar no botão **"Enviar série p/ pedido/nota"**, será enviado o produto, a série específica, o percentual de desconto e o local (caso o produto utilize local).

As avarias, como já informamos, são cadastradas na tela de Registro de Avarias.

![Imagem 8: As avarias, como já informamos, são cadastradas na tela de Registro de Avarias .](https://ajuda.sankhya.com.br/hc/article_attachments/4407428521111)

Na aba Geral deverão ser informados dados referentes à série que será avariada, como o código do produto, o número da série, o % de desconto que será aplicado caso essa avaria seja vendida e alguma observação sobre o produto, caso seja necessário.

Os campos **"Cód. Usuário"** e **"Data"** estarão desabilitados e serão preenchidos automaticamente pelo sistema quando o mesmo confirmar o registro. O campo Cód. Usuário será preenchido com o código e o nome do usuário que cadastrou a avaria e o campo Data mostrará a data e a hora dessa criação.

Na aba **"Fotos de Avaria"** poderão ser adicionadas fotos da avaria.

![Imagem 9: Na aba "Fotos de Avaria" poderão ser adicionadas fotos da avaria.](https://ajuda.sankhya.com.br/hc/article_attachments/4407428527127)

Na tela de [Consulta de Séries](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119233-Consulta-de-S%C3%A9ries), a coluna **"Nro. Pedido Reserva"** somente será preenchida caso a série em questão esteja reservada para algum Pedido.

![Imagem 10: Na tela de Consulta de Séries , a coluna " Nro. Pedido Reserva" somente será preenchida caso a série em questão esteja…](https://ajuda.sankhya.com.br/hc/article_attachments/4407428588951)

---

**Venda de componentes fora do Kit**

A empresa poderá vir a configurar o sistema de forma que consiga vender um componente separado do Kit.

Para isso, na aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda) da tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) efetue a marcação **"Aceitar venda fora do KIT"**.

![Imagem 11: Para isso, na aba Venda da tela de Cadastro de Produtos efetue a marcação " Aceitar venda fora do KIT" .](https://ajuda.sankhya.com.br/hc/article_attachments/4407435168407)

Se a marcação estiver realizada e for lançado um Pedido ou uma Nota de Venda com um produto que seja componente de outro e ele estiver sendo vendido separadamente o sistema permitirá.

Caso a marcação não esteja feita e você tente realizar um procedimento conforme descrito anteriormente, o sistema irá verificar se no parâmetro **"Tops para venda individual de componentes -** **TOPVENCOMPINDIV"**, a TOP desse Tipo de Movimento está relacionada. Se sim, ele também conseguirá vender separadamente um produto que seja componente de outro. Se não estiver nem marcada e nem relacionado na TOP, essa venda não será permitida e a seguinte mensagem será lançada:

**"Componente não pode ser vendido separadamente".**

Nesse processo também poderá ser vendida uma série avariada, e o sistema irá preencher o campo % desconto (conforme configuração do mesmo na tela de Registro de Avarias). Se o produto utilizar Local, o sistema carregará o local correto e bloqueará o campo **"Local origem"**.

Produtos avariados não respeitam a marcação do cadastro de produtos e podem ser vendidos separadamente, independentemente da configuração do produto ou do parâmetro.

---

**Venda de uma série específica seja ela avariada ou não e "Local Curinga"**

O sistema permitirá ao vendedor informar a série do produto que deseja vender, estando ele avariado ou não.

Para isso, na Central de Vendas, o campo **"Nro. Série"** na grade de itens será utilizado para efetuar transações com uma série específica e será liberado para digitação somente se o parâmetro USACBGLOBAL estiver habilitado, a Nota/Pedido for de Venda e se o produto utilizar **"Série Global"**.

Só será possível vender a série específica (preenchendo-a no campo Nro série da grade de itens), se a quantidade negociada não for diferente de 1 e se essa série não estiver pendente para outra nota. Ao confirmá-la, o sistema pegará automaticamente o código do local em que a série informada está e não permitirá alterar o local. Se a TOP estiver reservando ou atualizando estoque essa série será reservada.

Quando o produto estiver configurado para trabalhar com local, o sistema exigirá que o mesmo seja digitado durante o lançamento do item mas, ao fazer a venda, não saberemos informar em qual local esse produto está, para retirada. Por isso, ao invés de digitar o local correspondente a cada série, ele informará um local curinga. Este local deverá estar informado no parâmetro LOCALCURINGAFAT. Ao preencher o item com ele e salvar, o sistema irá preencher a série e irá alterar o campo Local origem para o local das séries. Se todas as séries não estiverem no mesmo local, ele irá quebrar o item e irá lançar outro item com as outras séries dos demais locais e atualizar a quantidade negociada de acordo com as séries disponíveis nos locais.

Se no faturamento o Local de Origem for igual ao do parâmetro LOCALCURINGAFAT, o sistema também irá quebrar o item de acordo com a quantidade de séries disponíveis nos locais. Além disso, se no Pedido estiver sendo utilizada uma série específica, na nota de venda gerada não será apresentado à série específica no campo Nro série. Nesse caso a série poderá ser visualizada na janela aberta através do botão **"Números de séries"** da grade de itens.

**Observação:** o sistema não permite vender séries que estejam bloqueadas.

---

**Conferência de Série**

Na tela de Conferência de Série o botão **"Visualizar conferidos"** irá mostrar as séries que já foram anteriormente conferidas. Mostrará a série, e o produto. Exemplo: Você entra na tela e confere 5 séries; confirma essa conferência mesmo que falte conferir algumas séries. Ao entrar na tela novamente, a informação de que 5 séries já foram conferidas estará lá, mas as séries que já foram conferidas não ficarão visíveis, então você poderá acessar esse botão para ver quais são as séries já conferidas.

Lista de parâmetros:

- Usa Número de Série Global? - USACBGLOBA;
- Usa nro de série do fabricante? - USANSFABRIC;
- Digitar no campo ocorrência quando bloquear série - DIGOCORBLOQSER;
- Habilitar o suporte a kit no SankhyaW? - HABSUPORTEKITSW;
- Tem mat.prima na central atendimento ao Cliente? - TEMMPVENDA;
- Tem mat.prima na central atendimento ao Fornec.? - TEMMPCOMPRA;
- Tem Mat.Prima na Transferência? - TEMMPTRAN;
- Tem Mat.Prima na requisição? - TEMMPREQ;
- Tipo de cálculo para Nro. Série Global em notas de entrada - TIPCALCNSGLOBAL;
- Tops para venda individual de componentes - TOPVENCOMPINDIV;
- Local curinga para lançamento de pedidos/notas - LOCALCURINGAFAT.

---

**Processo de Conferência de produtos com controle adicional por série global**

Para os produtos que têm controle adicional por série, o sistema permite efetuar conferência de compra/venda utilizando séries com letras e números.

- **Regra 1: Leitura de códigos de barras com letras na série**

Exemplo:

Lançada uma Nota de Compra para o produto 120 – Produto com série e com letras.

| Produto | Quantidade | Local | Série |
| --- | --- | --- | --- |
| 120 | 1 | 2100 | ACIMAQ123 |
| 120 | 1 | 2100 | ACIMAQ456 |
| 120 | 1 | 3000 | ACIMAQ |
| 120 | 1 | 3000 | ACIMAQA |

Conferência de Séries que possui letras e números.

- **Regra 2: Busca de locais no faturamento**

Na tela [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abaestoque), realizar as marcações **"Pela Empresa"** e **"Agrupar local na validação de estoque"**.

E configurar o parâmetro **"Local curinga para lançamento de pedidos/notas - LOCALCURINGAFAT"**;

- **Regra 2.1: Processo de Faturamento de um Pedido de Venda com o local curinga para um produto controlado por série:**

Ao faturar, se tem o produto em 10 locais, qual deles o sistema considera primeiro?

Primeiro, o sistema busca um local que tenha a mesma quantidade que está sendo faturada em estoque disponível para obter as series; caso não encontre, ele busca o menor código local para consumir as series destes, depois o próximo em ordem crescente.

**Estoque do Produto: 120**

| Produto | Quantidade | Local | Série |
| --- | --- | --- | --- |
| 120 | 1 | 2100 | ACIMAQ123 |
| 120 | 1 | 2100 | ACIMAQ456 |
| 120 | 1 | 3000 | ACIMAQ |
| 120 | 1 | 3000 | ACIMAQA |

- **Regra 2.2: Processo de Faturamento de um Pedido de Venda com o local curinga, para um produto sem controle adicional por estoque.**

Lançada uma Nota de Compra para o produto 116, sem controle adicional por estoque:

| Produto | Quantidade | Local |
| --- | --- | --- |
| 116 | 100 | 2100 |
| 116 | 100 | 3000 |

- **Regra 2.3: Locais marcados como Independentes**

Na tela [Cadastro de Locais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602894-Locais), efetue a marcação **"Val. Est. independente"**.

| Produto | Quantidade | Local | Série |
| --- | --- | --- | --- |
| 118 | 10 | 2100 |  |
| 118 | 20 | 300 |  |
| 119 | 10 | 1000 | 1300000045 a 1300000051 e restante das séries com letras |

Como o produto 119 só possui estoque para locais que têm a validação independente, ao tentar lançar um Pedido de Venda com esse produto, mesmo que seja informado o Local Curinga, o sistema fará a validação.

Foi lançado um Pedido de Venda para o produto 118 na quantidade 9 e ao tentar faturar, um dos locais que tem estoque foi marcado para validar estoque independente, nisso, ao faturar o Pedido o sistema valida o estoque.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597254-Controle-de-Produtos-com-N%C3%BAmero-de-S%C3%A9rie-Global#top)
