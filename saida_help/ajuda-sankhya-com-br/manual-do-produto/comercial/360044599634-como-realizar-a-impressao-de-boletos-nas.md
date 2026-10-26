---
id: "360044599634"
titulo: "Como realizar a impressão de boletos nas centrais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599634-Como-realizar-a-impress%C3%A3o-de-boletos-nas-centrais"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:22:19Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Impressão", "Relatórios Formatados", "Contas", "Boletos", "TOP", "Impressão de boletos pelas centrais (Compras", "Vendas", "Mov. Internas e Notas)", "JUROOBRIG", "Modelos de Nota Fiscal/Duplicatas/Boletas", "RESOLVEUNC", "VLRLIQBOL", "Impressão de boletos nas centrais (Compras", "Mov. Int) manual", "Boleto", "Financeiro", "Impressão de Boletos: Configurações e Procedimentos"]
---

# Como realizar a impressão de boletos nas centrais

Nos Portais e nas Centrais de Compras, Vendas e Mov. Internas temos o botão ![Imagem 1: Nos Portais e nas Centrais de Compras , Vendas e Mov. Internas temos o botão "Imprimir" com a opção de "Imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/16947098483991)**"Imprimir"** com a opção de **"Imprimir Boleto"**. Porém, antes de efetuarmos a impressão do boleto do financeiro de uma nota pelos Portais/Centrais, é importante verificarmos se determinadas telas foram configuradas, conforme apresentado no fluxograma. 

![Imagem 2: Nos Portais e nas Centrais de Compras , Vendas e Mov. Internas temos o botão "Imprimir" com a opção de "Imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/4406907569303)

| ``` Leia a seguir os detalhes sobre as configurações que devem ser realizadas em cada tela. ``` |
| --- |

---

#### Configurações Gerais

Primeiramente, verifique se a nota está confirmada. Depois, confira se o [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), utilizada na nota possui as seguintes configurações:

- Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) o campo **"Financeiro"** deve estar atualizando **"Despesas"** ou **"Receitas"**.
- Na aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso) o campo **“Imprimir Pix/Boleto/Duplicata"** deve estar indicando **"Na confirmação"** ou **"Manual"**. Caso esteja indicando Na confirmação, ao confirmar a nota o boleto será impresso automaticamente.

[GIF animado: Imagem 3: Na aba Impressão o campo “Imprimir Pix/Boleto/Duplicata" deve estar indicando "Na confirmação" ou "Manual" . Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/4406900481431)

Feito isso, certifique se o [Tipo de negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) utilizado na nota, está com o campo **"Imprimir Pix/Boleto/Duplicata"** da aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173#abacaractersticas), configurado como **"Na confirmação"** ou **"Manual"**.

![Imagem 4: Feito isso, certifique se o Tipo de negociação utilizado na nota, está com o campo "Imprimir Pix/Boleto/Duplicata" da…](https://ajuda.sankhya.com.br/hc/article_attachments/4406900482199)

| ``` ![Imagem 5: Dica: após configurar a TOP e o Tipo de Negociação para emitir boleto "Na confirmação" , basta confirmar a nota e o…](https://ajuda.sankhya.com.br/hc/article_attachments/42311798515607) Dica: após configurar a TOP e o Tipo de Negociação para emitir boleto "Na confirmação", basta confirmar a nota e o boleto será impresso. ``` |
| --- |

Além das configurações acima, no financeiro da nota deve haver uma conta indicada, pois dessa forma, o sistema imprimirá o **"Boleto"** para a **"Conta"** cadastrada no financeiro da nota ou do lançamento financeiro, baseando-se no modelo informado nesta Conta.

Assim, no cadastro da [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113) vinculada à nota, verifique se na aba [Boletos/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113#ababoletosduplicatas) a marcação **"Emite"** esta habilitada, e se o campo **"Impressora"** possui uma impressora associada. Além disso, o campo **"Modelo"** deve ser informado com um modelo de boleto. Caso você não tenha realizado o cadastro do modelo de boleto para inserir no campo Modelo, leia o tópico a seguir [Cadastro de Modelos de Boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599634-Como-realizar-a-impress%C3%A3o-de-boletos-nas-centrais#Cadastrodemodelosdeboleto).

[GIF animado: Imagem 6: Assim, no cadastro da Conta vinculada à nota, verifique se na aba Boletos/Duplicatas a marcação "Emite" esta…](https://ajuda.sankhya.com.br/hc/article_attachments/4406900485399)

| ![Imagem 7: GIF animado: Imagem 6: Assim, no cadastro da Conta vinculada à nota, verifique se na aba Boletos/Duplicatas a marcação…](https://ajuda.sankhya.com.br/hc/article_attachments/42311798517527) | **Deve haver harmonia entre essas configurações, pois elas estão interligadas. Por exemplo, ao tentar emitir um boleto com uma TOP ou um Tipo de Negociação que não foi configurada para a emissão de boletos, você não terá êxito com a impressão.** |
| --- | --- |

**Observações:** 

- Caso o parâmetro **"Controla boleto por fila? - FILABOLETA"** esteja ligado e exista uma **"Fila"** de impressão cadastrada, o sistema usará a impressora da Fila para imprimir os mesmos. Caso contrário, o sistema buscará a impressora da **"Conta"** registrada no financeiro da nota.
- Se os títulos da nota não possuírem **"Nosso Número"** ou o parâmetro **"Renumera nosso número sempre? - RENNOSSONUM"** estiver ligado juntamente com o parâmetro FILABOLETA, no momento da impressão do boleto a **"Conta"** e o **"Banco"** registrados no financeiro serão substituídos pela **"Conta"** e **"Banco"** cadastrados na **"Fila"**. Neste caso o modelo utilizado para impressão do boleto será o da conta da fila.

---

#### Cadastro de Modelos de Boleto

O sistema possui um modelo padrão de boleto que pode ser baixado por meio da tela [Modelos de Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134). Assim, ao clicar no botão **"Baixar modelo padrão"**, opção **"Boleto"**, o sistema automaticamente irá realizar o download do modelo. 

![Imagem 8: O sistema possui um modelo padrão de boleto que pode ser baixado por meio da tela Modelos de Boletos . Assim, ao clicar…](https://ajuda.sankhya.com.br/hc/article_attachments/4406907594647)

Com o arquivo do modelo do boleto baixado, acesse a tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) para cadastrar o novo modelo. Inicialmente, preencha uma **"Descrição"** e salve o cadastro.

![Imagem 9: Com o arquivo do modelo do boleto baixado, acesse a tela Relatórios Formatados para cadastrar o novo modelo.…](https://ajuda.sankhya.com.br/hc/article_attachments/4406900508183)

Em seguida, para adicionar o arquivo do modelo, clique em **"Adicionar Arquivo..."**, dessa forma, o sistema abrirá uma janela para que, ao clicar em **"Escolher arquivo..."**, seja feita a procura pelo modelo previamente salvo no computador. Depois de escolher o arquivo, clique em **"Abrir"**, assim o modelo estará cadastrado na tela Relatórios Formatados.

[GIF animado: Imagem 10: Em seguida, p ara adicionar o arquivo do modelo, clique em "Adicionar Arquivo..." , dessa forma, o sistema abrirá uma…](https://ajuda.sankhya.com.br/hc/article_attachments/4406900514199)

![Imagem 11: O sistema permitirá apenas adicionar arquivos com extensão ".jrxml" . Caso seja feita a tentativa de adicionar um…](https://ajuda.sankhya.com.br/hc/article_attachments/16948213515415) O sistema permitirá apenas adicionar arquivos com extensão **".jrxml"**. Caso seja feita a tentativa de adicionar um arquivo com outra extensão, será emitido o aviso:

**"Somente arquivos no formato ".jrxml" são aceitos"**.

Para vincular o **"Relatório Formatado"** cadastrado anteriormente a um modelo de impressão, acesse a tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913).

![Imagem 12: Para vincular o "Relatório Formatado" cadastrado anteriormente a um modelo de impressão, acesse a tela Modelos de Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/4406907608471)

Após preencher os campos obrigatórios da tela, o vínculo entre o modelo e relatório formatado, será realizado por meio do preenchimento do campo **"Número do relatório modelo"**, onde você deverá informar o código do relatório cadastrado anteriormente na tela Relatórios Formatados.

Ao salvar a inclusão, o modelo estará vinculado ao Relatório Formatado informado.

Com o cadastro do modelo de boleto efetuado, o código do modelo que você preencherá na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113#ababoletosduplicatas), campo **"Modelo"**, e que será apresentado no financeiro da nota, é a informação do campo **"Modelo"**.

![Imagem 13: Com o cadastro do modelo de boleto efetuado, o código do modelo que você preencherá na tela Contas , aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4406900530967)

Realizadas as configurações, para efetuar a impressão e geração de numeração bancária, com a nota selecionada na grade ou na Central com a nota aberta, você deverá clicar na seta ao lado do botão de impressão ![Imagem 14: Realizadas as configurações, para efetuar a impressão e geração de numeração bancária, com a nota selecionada na grade…](https://ajuda.sankhya.com.br/hc/article_attachments/16947098483991) e selecionar a opção **"Imprimir Pix/ Boleto"**.

![Imagem 15: Não é possível realizar a impressão de um boleto Cobrança Pix nas Centrais, para imprimi-lo, utilize a opção "Imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/16948213515415) Não é possível realizar a impressão de um boleto Cobrança Pix nas Centrais, para imprimi-lo, utilize a opção **"Imprimir Pix"** do botão [Outras Opções..](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es). da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

---

## Parâmetros que influenciam neste processo

**Cálculo de Juro obrigatório - JUROOBRIG:** Se estiver ligado, manterá o valor dos juros quando um título for estornado. Se estiver desligado, o valores de juros serão limpos ao estornar. Este parâmetro deve estar ligado para que seja feita a impressão do **"Valor Líquido"** na linha digitável do boleto.

**Calcula valor líquido boleta? - VLRLIQBOL:** Este parâmetro gera o valor total da duplicata líquida. O valor líquido é o valor do desdobramento, aplicando sobre ele tudo que afeta o valor a ser pago, como juros, multa, descontos, impostos retidos (do próprio financeiro e outros impostos). Este parâmetro influência apenas na emissão de boletos e assim como o parâmetro JUROOBRIG, também deve estar ligado para que seja possível a impressão do Valor Líquido na linha digitável do boleto.

**Resolução de nome de impressora via UNC - RESOLVEUNC:** Visando agilizar o procedimento de impressão de boletos, caso a impressora informada não exista na rede, pode-se fazer uso deste parâmetro, que quando desativado, o sistema irá ignorar a resolução de nomes UNC, acelerando assim o ganho no tempo de resposta e informando quase instantaneamente que a impressora não existe. Quando o parâmetro estiver ligado, o sistema irá demorar alguns minutos para imprimir notas/boletos, pois o tempo para informar que a impressora não existe na rede, será maior.

**Imprimir DANFE e boleto agrupados? - AGRUPADANFEBOL:** Este parâmetro quando habilitado, faz com que o sistema agrupe o DANFE e o Boleto se existirem, no momento da impressão, de acordo com cada nota. Com o parâmetro desabilitado, o sistema irá imprimir todos os boletos e em seguida todos os DANFE's. Este parâmetro possui essa funcionalidade quando é utilizado o faturamento direto do sistema.
