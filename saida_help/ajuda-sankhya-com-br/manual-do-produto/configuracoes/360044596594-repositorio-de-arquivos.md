---
id: "360044596594"
titulo: "Repositório de Arquivos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:45:30Z"
rotulos: ["manual", "Configuração", "FREPBASEFOLDER", "Pesquisa", "Repositório de Arquivos", "br.com.sankhya.sistema.arquivos", "Repositório de Arquivos manual", "Acesso Remoto", "Gerenciamento de Arquivos com Sankhya Om", "Organização de Arquivos", "Gerenciamento de Documentos", "Permissões de Pasta"]
---

# Repositório de Arquivos

| ``` ![Imagem 1: Módulo: Configurações > Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/42310605547671) Módulo: Configurações > Avançado ``` |
| --- |

---

Esta tela possui funcionamento semelhante ao Explorer do Windows, que posiciona pastas em uma árvore hierárquica para que o usuário possa organizar arquivos. O objetivo principal é disponibilizar ao usuário um repositório, área lógica semelhante a um depósito de arquivos, no qual é possível alocar arquivos.

![Imagem 2: Esta tela possui funcionamento semelhante ao Explorer do Windows, que posiciona pastas em uma árvore hierárquica para…](https://ajuda.sankhya.com.br/hc/article_attachments/4961209121943)

Com os arquivos inseridos no **"Repositório de Arquivos"**, o usuário estará possibilitado a ter acesso a estes documentos mesmo não estando presente em seu local de trabalho. Isso devido ao fato de que o Sankhya Om pode ser acessado via internet de qualquer lugar do mundo, possibilitando ao usuário acessar os arquivos no servidor que roda o sistema. Sendo assim, o usuário poderá inserir no Repositório de Arquivos, qualquer tipo de arquivo que desejar, e poderá permitir acesso a outros usuários, possibilitando assim, fácil acesso a estes arquivos.

Considere o seguinte exemplo:

O gerente de um estabelecimento comercial que utiliza o Sankhya Om, cria uma pasta e a disponibiliza para o "Grupo de Usuário", "Consultores de Vendas". Nesta pasta, ele insere tabelas de preços, materiais de publicidade, tabelas diversas, documentos de texto, documentos .pdf, imagens, etc.

Dessa forma, consultores externos, que possivelmente estarão fora da empresa atendendo clientes em diversas localidades, poderão acessar o Sankhya Om através da internet, e visualizar, ou até mesmo baixar, os arquivos que foram disponibilizados no Repositório de Arquivos. Este acesso pode ser feito de qualquer tipo de computador, desktop ou portátil, celular, tablet, com acesso à internet.

O parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"** é utilizado para definir o caminho para a pasta base do repositório. A saber:

- Se o parâmetro for preenchido com um diretório inexistente, por exemplo, **"D:\Teste"**, ao abrir a tela Repositório de Arquivos será criado um diretório "Teste" no caminho especificado que nesse caso é D:\Teste.
- Caso o parâmetro seja preenchido com um caminho inexistente, por exemplo, **"teste"**, ao abrir a tela Repositório de Arquivos será criado um diretório "teste" dentro da pasta bin do Jboss. Se o diretório já existir serão apresentados os diretórios e arquivos.
- Já se o parâmetro estiver em branco (sem nenhum caminho), ao abrir a tela Repositório de Arquivos, serão apresentados os arquivos da pasta **".sw\_file\_repository"** que estão localizados dentro da pasta do usuário no C:\.

No painel **"Pastas"**, localizado à esquerda da tela, pode-se criar novos diretórios para a alocação dos arquivos do sistema, sendo possível excluir, renomear e configurar o acesso às pastas.

![Imagem 3: No painel "Pastas" , localizado à esquerda da tela, pode-se criar novos diretórios para a alocação dos arquivos do…](https://ajuda.sankhya.com.br/hc/article_attachments/9756637271575)

Utilizando o botão ![Imagem 4: Utilizando o botão "Criar nova pasta" , o sistema insere um novo diretório no repositório de arquivos. Para inserir uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16746844192535) **"Criar nova pasta"**, o sistema insere um novo diretório no repositório de arquivos. Para inserir uma pasta dentro de outra, basta selecionar (clicar) a pasta desejada, e, em seguida, solicitar a inclusão através do botão Criar nova pasta.

Com uma pasta selecionada, estarão disponíveis para os usuários duas outras opções:  ![Imagem 5: Com uma pasta selecionada, estarão disponíveis para os usuários duas outras opções: "Deletar pasta" e "Renomear pasta"…](https://ajuda.sankhya.com.br/hc/article_attachments/4961238955671) **"Deletar pasta"** e ![Imagem 6: Com uma pasta selecionada, estarão disponíveis para os usuários duas outras opções: "Deletar pasta" e "Renomear pasta"…](https://ajuda.sankhya.com.br/hc/article_attachments/16746937745943) **"Renomear pasta"**. A primeira opção exclui a pasta que foi selecionada do repositório de arquivos, apresentando uma mensagem informando que esta ação também excluirá os arquivos e sub-pastas que possam estar contidas nesta. Já a segunda opção apresenta uma janela contendo um campo onde é inserido o novo nome que se deseja dar à pasta.

O campo **"Localizar arquivo"** e o botão de **"Pesquisa"** localizado ao lado, permitem realizar a pesquisa dos arquivos armazenados no repositório. Pode ser observado no gif abaixo um campo onde você insere o nome do arquivo desejado. A pesquisa pode ser acionada pelo botão "Enter", ou clicando no botão de Pesquisa.

[GIF animado: Imagem 7: O campo "Localizar arquivo" e o botão de "Pesquisa" localizado ao lado, permitem realizar a pesquisa dos arquivos…](https://ajuda.sankhya.com.br/hc/article_attachments/9757015516567)

Serão listados, como critério da pesquisa, todos os arquivos que contenham (em qualquer parte) a palavra informada na pesquisa não considerando maiúsculo/minúsculo. Por exemplo, considerando "Rel" como valor buscado, os seguintes arquivos seriam válidos, como resultado: Relatório.doc, RELATÓRIO.doc, MEU-relatório, etc.. O mesmo seria válido se o critério de busca fosse "REL", "rel", "rEL".

O painel Pastas conta ainda com a opção ![Imagem 8: O painel Pastas conta ainda com a opção "Configurar acessos da pasta" que será detalhado no final deste documento.](https://ajuda.sankhya.com.br/hc/article_attachments/4961319289111) **"Configurar acessos da pasta"** que será detalhado no final deste documento.

## Inserindo arquivos

Quando a pasta selecionada não possui nenhum arquivo inicial, o sistema apresenta a seguinte mensagem:

**"Esta página não contém arquivos, clique aqui para adicionar!"**

Sendo assim, ao clicar em **"clique aqui"** o sistema apresenta uma janela que é utilizada para buscar o arquivo e inseri-lo no repositório de arquivos.

![Imagem 9: Sendo assim, ao clicar em " clique aqui " o sistema apresenta uma janela que é utilizada para buscar o arquivo e…](https://ajuda.sankhya.com.br/hc/article_attachments/4961372644759)

É possível copiar ou mover os arquivos de uma pasta para outra, bastando para isso selecionar os arquivos a serem copiados ou movidos e arrastar com o mouse para a pasta destino.

**Nota:** para selecionar mais de um arquivo pressione **"Ctrl"** e clique com o mouse sobre a linha de cada arquivo ou pressione **"Shift"** e com as setas direcionais do teclado selecione os arquivos que serão incluídos na seleção.

Após a inserção do arquivo, a tela passa a apresentar um novo modo de visualização e habilita os botões presentes em sua parte superior.

![Imagem 10: Após a inserção do arquivo, a tela passa a apresentar um novo modo de visualização e habilita os botões presentes em…](https://ajuda.sankhya.com.br/hc/article_attachments/4961468932759)

A opção **"Adicionar Arquivos"** é utilizada para inserir novos itens na pasta. Os arquivos são posicionados na grade, como pode ser observado na imagem acima.

Após selecionar o arquivo desejado na grade, caso necessário, pode-se utilizar a opção **"Remover Selecionados"** para excluí-los da pasta. Através da opção **"Visualizar/Baixar"**, realiza-se o download de um arquivo na máquina.

Já a opção **"Renomear"** possibilita dar um novo nome ao arquivo. Com a opção **"Atualizar"** é possível substituir o arquivo selecionado por outro, para isso, o sistema apresentará a mesma janela utilizada para buscar e inserir os arquivos no repositório.

A opção **"Propriedades"** apresenta uma pequena janela com informações sobre o arquivo selecionado.

![Imagem 11: A opção "Propriedades" apresenta uma pequena janela com informações sobre o arquivo selecionado.](https://ajuda.sankhya.com.br/hc/article_attachments/4961614666391)

## Configurando Acessos da Pasta

No painel Pastas temos o botão Configurar acessos da pasta. Ao acioná-lo, será apresentada uma janela utilizada para especificar quais os demais usuários do sistema possuem acesso para visualizar e alterar as pastas que forem criadas. Somente o usuário que criou a pasta, possui autorização para realizar esta configuração.

As autorizações podem ser concedidas para os **"Usuários"** como também para os **"Grupos de Usuários"**. Nestes painéis encontram-se os campos para pesquisa, úteis para realizar buscas em listas de usuários, ou grupos. Ao digitar o nome que deseja pesquisar, clique no botão **"Localizar"**.

![Imagem 12: As autorizações podem ser concedidas para os "Usuários" como também para os "Grupos de Usuários" . Nestes painéis…](https://ajuda.sankhya.com.br/hc/article_attachments/4961823963799)

Para inserir o **"Usuário"**, ou **"Grupo"**, no painel da direita, basta selecionar o registro desejado e clicar no botão**![Imagem 13: Para inserir o "Usuário" , ou "Grupo" , no painel da direita, basta selecionar o registro desejado e clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/4961849494423) "Mover para direita"**, podendo também utilizar o duplo clique, ou ainda pode-se clicar no registro e arrastar para este painel direito.

Os mesmos procedimentos podem ser utilizados para fazer o caminho contrário, ou seja, retirar o **"Usuário"** ou **"Grupo"** do painel direito e voltá-lo para o painel esquerdo, porém o botão que deve ser utilizado é o**![Imagem 14: Os mesmos procedimentos podem ser utilizados para fazer o caminho contrário, ou seja, retirar o "Usuário" ou "Grupo" do…](https://ajuda.sankhya.com.br/hc/article_attachments/4961842284567) "Remover selecionado"**.

![Imagem 15: Os mesmos procedimentos podem ser utilizados para fazer o caminho contrário, ou seja, retirar o "Usuário" ou "Grupo" do…](https://ajuda.sankhya.com.br/hc/article_attachments/4961739253143)

Com os devidos **"Usuários"**, ou **"Grupos"**, inseridos no painel da direita, o administrador deve especificar quais rotinas que estes poderão executar no uso das pastas, sub-pastas e arquivos contidos neste repositório.

A coluna **"L"** corresponde ao direito de **"Ler"**, já a coluna **"A"** concede o direito de **"Alterar"**.

**Nota:** caso esta segunda coluna esteja marcada, o usuário terá automaticamente o direito de **"Ler"**. E não necessariamente terá o direito de **"Alterar"**, aquele usuário que está autorizado a **"Ler"**.

A coluna **"D"** representa que o usuário é o **"Dono"** do arquivo e somente é atribuído ao usuário que criou a pasta.

![Imagem 16: A coluna "D" representa que o usuário é o "Dono" do arquivo e somente é atribuído ao usuário que criou a pasta.](https://ajuda.sankhya.com.br/hc/article_attachments/4961877243287)

Com relação às permissões da tela **"Repositório de Arquivos"**, elas são as seguintes:

- **Adicionar:** um usuário pode adicionar um registro se a coluna **"A"** (alteração) estiver marcada para aquele usuário;
- **Remoção:** um usuário pode remover um registro se o mesmo puder adicionar um arquivo e se existir algum registro selecionado na grade;
- **Edição:** um usuário pode editar um arquivo, se ele puder adicionar um arquivo e se existir somente um registro selecionado na grade.

Dessa forma, não é possível que um usuário tenha permissão de adicionar e não tenha permissão de remover.

É importante salientar que no Repositório de Arquivos, as permissões de acesso às pastas são liberadas "pasta a pasta" independente de sua hierarquia. Considere o seguinte exemplo:

Criando-se uma pasta com o nome PAI, outras duas de nomes Filho1 e Filho2; caso o usuário SUP conceda permissão apenas para a pasta PAI para algum usuário qualquer, este mesmo usuário não terá permissão para acessar as pastas Filho1 e Filho2, apenas a pasta PAI.

Ao concluir toda essa configuração, o usuário deverá utilizar o botão **"Salvar"** para confirmar as alterações que foram feitas e fechar a janela. Ou poderá descartar clicando na opção **"Cancelar"**.

**Observação:** a tabela de anexos é a TSIANX, assim, quando for inserido um anexo no sistema, ele será salvo primeiro na tabela e depois no repositório; caso dê algum erro pra salvar no repositório, o sistema fará rollback na tabela. Da mesma forma acontece na exclusão, ou seja, quando você exclui o anexo, primeiro será excluído do repositório e depois do sistema. 

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos#top)
