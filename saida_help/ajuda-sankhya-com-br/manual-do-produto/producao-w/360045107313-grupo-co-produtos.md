---
id: "360045107313"
titulo: "Grupo Co-produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107313-Grupo-Co-produtos"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:53:51Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "br.com.sankhya.mgeprod.cad.grupo.coprodutos", "Grupo Co-produtos manual", "Ordem de Produção", "Produção", "Cadastro", "Processamento e OPs: Gerar OPs ajustar quantidades e remover se necessário", "Cadastro de Grupos de Co-Produtos: Informar código descrição e ativação", "Campos Importantes: MP Compartilhada Qtd. de processamento e Unidade"]
---

# Grupo Co-produtos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312725907735) Módulo: Produção > Cadastros
```

---

Entende-se como Grupos de Co-Produtos, um agrupamento de vários coprodutos gerados em função de um tipo de processamento de uma determinada matéria-prima compartilhada. Esta tela é responsável pelo cadastro de cada um destes grupos.

![Imagem 2: Entende-se como Grupos de Co-Produtos , um agrupamento de vários coprodutos gerados em função de um tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/8838654022167)

O campo **"Código"** irá facilitar na identificação do grupo.

Em **"Descrição"** informe um nome para o grupo.

Se a marcação **"Ativo"** for habilitada, será informado ao sistema que o grupo pode ser utilizado no lançamento de OP.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107313-Grupo-Co-produtos#abageral)                                                                 [Aba Co-Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107313-Grupo-Co-produtos#abacoprodutos) 

## Aba Geral

No campo **"MP Compartilhada"** você informa uma matéria-prima principal de consumo compartilhada entre todos os Coprodutos pertencentes ao grupo.

Referente ao campo **"Qtd. de processamento (padrão)"**, informe a quantidade padrão para o processamento da matéria-prima em uma produção conjunta. O valor preenchido no campo, será processado de forma automática ao ser lançado uma nova OP conjunta para o Grupo.

No campo **"Unidade"**, informe a unidade da quantidade informada no campo Qtd. de processamento (padrão).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107313-Grupo-Co-produtos#top)

## Aba Co-Produtos

Nesta aba, temos uma lista de produtos que serão gerados por meio do processamento da matéria-prima compartilhada.

![Imagem 3: Nesta aba, temos uma lista de produtos que serão gerados por meio do processamento da matéria-prima compartilhada.](https://ajuda.sankhya.com.br/hc/article_attachments/8838710079383)

Cada produto inserido nesta, possuirá um **"Rendimento Previsto (em %)"** que será considerado no lançamento de OP para definição do tamanho do lote da OP do produto em função da quantidade da Matéria-Prima principal processada.

**Observação:** caso a Unidade da MP Compartilhada seja diferente da Unidade padrão dos itens de coprodutos, ao salvar, o sistema mostrará uma mensagem de erro:

**" 'Unidade' diferente da Un. padrão dos co-produtos."**

**Facilitador do lançamento de OPs de uma operação conjunta**

Na tela [Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP-), referente ao campo **"Tipo de Ordem"**, temos a opção **"Produção Conjunta"**; ao selecionar esta, será apresentado o campo **"Grupo Co-Produtos"**.

Quando o botão Incluir OP for clicado, será apresentado o pop-up **"Produção Conjunta"**:

Logo, os campos MP Compartilhada, Qtd. de processamento, Unidade, Qtd de processamento (padrão)  e Un. Padrão serão apresentados.

**Nota:** a quantidade que será proporcionada para os PAs do coproduto será a Qtd. de processamento (Un. padrão).

Ao clicar no botão Incluir OP e o rendimento total previsto dos itens do grupo de coproduto selecionado for diferente de 100%, será apresentada a seguinte mensagem:

**"O rendimento total previsto dos itens do grupo de co-produto selecionado é diferente de 100%."**

Se na MP Compartilhada existir unidade alternativa e o campo Unidade for alterado, a quantidade que será apresentada no campo Qtd. de processamento (Un. padrão) também será alterada.

Quando você confirmar a inclusão das OPs conforme o campo Qtd. de processamento (Un. padrão), serão incluídas OPs para os itens do grupo de coprodutos, sendo assim, será realizada a quantidade equivalente conforme for exibido na tabela Rendimento Previsto (%).

Quando o coproduto for salvo, você poderá alterar a Qtd. de processamento Co-produto por meio do botão ![Imagem 4: Quando o coproduto for salvo, você poderá alterar a Qtd. de processamento Co-produto por meio do botão "Alterar Qtd.…](https://ajuda.sankhya.com.br/hc/article_attachments/16674190124823) **"Alterar Qtd. Processamento Co-produto"**, porém, este só aparecerá quando o item da OP for Produção Conjunta; ao acioná-lo, o pop-up surgirá novamente para edição. Porém, na edição deste, irá constar a marcação **"Seq. Produção Conjunta e Reproporcionar qtd. entre Co-produções"**; quando marcada, fará com que as OPs de lançamento sejam ajustadas de acordo com a qtd. de processamento (Un. padrão). Quando não for habilitada, somente a qtd. processamento (Un. padrão) será alterada, sendo que, irá como sugestão para a qtd. da MP na tela [Apontamento de Produções Conjuntas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118753-Apontamento-de-Produ%C3%A7%C3%B5es-Conjuntas) e não será ajustado para as OPs do lançamento.

Se você clicar no botão **"Remover"**, o sistema mostrará a mensagem de confirmação:

**"Deseja remover todas as OPs que fazem parte desta produção conjunta?"**

O botão **"Sim"** irá remover todas as OPs com a seq. produção conjunta;

Caso você opte por **"Não"**, o sistema excluirá somente a que foi selecionada;

O botão **"Cancelar"** não irá remover nenhuma OP.

Para você lançar as OPs finalizadas, basta clicar no botão **"Lançar Ordens"** e, assim que lançadas, essas OPs serão exibidas na tela Ordens de Produção no modo grade.

Se houver lançamento de OP específico que você queira filtrar, busque pelo seu Número Único no campo **"Nro. OP Conjunta"**.

Na tela Apontamento de Produções Conjuntas, você pode incluir OPs de Produção Conjunta por meio do botão ![Imagem 5: Na tela Apontamento de Produções Conjuntas , você pode incluir OPs de Produção Conjunta por meio do botão "Incluir OP"…](https://ajuda.sankhya.com.br/hc/article_attachments/16674212402071) **"Incluir OP"**. Ao clicar neste botão, o sistema exibirá o seguinte pop-up:

![Imagem 6: Na tela Apontamento de Produções Conjuntas , você pode incluir OPs de Produção Conjunta por meio do botão "Incluir OP"…](https://ajuda.sankhya.com.br/hc/article_attachments/8839051192215)

No campo **"Tipo"** temos as opções **"Produção Conjunta"** ou **"Ordem Produção"**. De acordo com o que for selecionado neste campo, o nome do campo abaixo irá variar entre **"Nro. Produção Conjunta"** e **"Ordem de Produção (OP)"**.

Desta forma, as OPs lançadas ficarão da seguinte maneira:

![Imagem 7: Desta forma, as OPs lançadas ficarão da seguinte maneira:](https://ajuda.sankhya.com.br/hc/article_attachments/8839059144215)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107313-Grupo-Co-produtos#top)
