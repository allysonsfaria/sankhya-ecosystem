---
id: "360045117633"
titulo: "Ajuste de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-10-06T14:19:06Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Inventário", "WMS", "TOP", "Estoque", "Ajuste de Estoque", "br.com.sankhya.mgeinvent.ajuste.estoque", "Ajuste de Estoque  manual", "Ajuste de estoque necessário", "Criação de notas/pedidos", "Regras e filtros aplicáveis"]
---

# Ajuste de Estoque

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312604079127) Módulo: Inventário > Arquivo
```

---

![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/360081680814)

Feita a Cópia e Contagem, alguns produtos podem apresentar diferenças, sendo necessário ajustar o estoque no sistema. Estas diferenças demandam recontagens.

Dependendo do volume, pode ser necessária uma sindicância à fim de descobrir as causas das diferenças, que poderão ser:

- Notas sem registro no sistema;
- Falha no processo de entrega onde produtos parecidos estão sendo "trocados" na hora da entrega (por exemplo, a marca A de extrato, no lugar da marca B);
- Algum local sem contagem;
- Erro de digitação;
- Erro de anotação;
- Erro na inadimplência de produto;
- Roubo;

**Importante:** é necessário acessar a tela **"Comercial > Consulta > Modelo de Notas e Pedidos"** e criar dois Modelos de Notas/Pedidos, um para as notas/pedidos de Entrada e outro de Saída, utilizando um [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) especial de Ajuste de Estoque com as corretas configurações:

- A TOP para Entrada precisa atualizar o estoque (Entrar).
- A TOP para Saída precisa atualizar o estoque (Baixar).
- A TOP não pode atualizar o financeiro.
- O **"Tipo do Movimento"** da TOP precisa ser igual a Venda, Compra, Pedido de Venda, Pedido de Compra.

A nota usada como modelo pode ser configurada de duas maneiras:

Se for utilizar um modelo para cada empresa, é necessário que você preencha os campos **"Modelo Ajuste de Entrada de Estoque"** ou **"Modelo Ajuste de Saída de Estoque"** da aba **"Estoque/Preço"** da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa); estes campos devem ser preenchidos com o **"Número Único"** que é gerado por estes modelos de nota/pedido.

![Imagem 3: Se for utilizar um modelo para cada empresa, é necessário que você preencha os campos "Modelo Ajuste de Entrada de…](https://ajuda.sankhya.com.br/hc/article_attachments/360082824413)

Sendo utilizado um modelo para notas para qualquer empresa, é necessário que você configure o Número Único que é gerado por este modelo de nota/pedido através dos parâmetros abaixo:

- Nota Modelo Ajuste Estoque (Entrada) - NOTAENTAJUSTEST;
- Nota Modelo Ajuste Estoque (Saída) - NOTASAIAJUSTEST.

O sistema irá, primeiramente, tentar pegar o modelo da empresa; caso não encontre configurado na empresa, ele buscará o modelo do parâmetro; não localizando o modelo em nenhum lugar, será exibida uma mensagem informando que é necessário configurar o modelo.

No **"Ajuste de Estoque"** serão geradas notas de ajuste de forma automática. Serão geradas, conforme a necessidade, notas separadas para os Ajustes de Entrada e Saída.

**Nota:** na alteração de um modelo já configurado, o sistema fará validação, impedindo a utilização de uma TOP mais recente que a TOP do modelo já existente, isto só ocorre nas alterações de modelo; no cadastro de um novo modelo, esta validação não ocorre, uma vez que o modelo também é novo. Da seguinte forma:

No parâmetro NOTAENTAJUSTEST, você deve informar o numero único do modelo de nota/pedido configuradas com uma TOP de Entrada e, no parâmetro NOTASAIAJUSTEST, informe o número único do modelo de nota/pedido configuradas com uma TOP de Saída.

**Importante:** as TOP's deverão ser configuradas sem geração de financeiro e com movimentação de estoque.

**Observação:** ao realizar um lançamento de notas de Ajuste de Estoque, caso seja necessário determinar a quantidade máxima de itens presentes em cada nota (tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), botão **"Outras Opções"**, opção **"Controle de Numeração"**, campo **"Quantidade de itens na nota"**), a configuração da base de numeração da TOP utilizada, deverá ser através da opção **"TOP"** localizada na tela Tipos de Operação - TOP, aba **"Impressão"**, campo **"Base numeração"**. Desta forma, considere que esta será uma configuração a ser efetuada de forma ordenada, ou seja, primeiramente, defina a Base numeração igual a TOP e, logo em seguida, informe a Quantidade de itens na nota e as demais características do Controle de Numeração.

## Regras

- Quando a quantidade contada for maior que a cópia, o item será inserido em uma nota de Entrada;
- Quando a quantidade contada for menor que a cópia, o item será inserido em uma nota de Saída;
- Se ocorrer os dois casos, serão geradas duas notas, uma para entrada e uma para saída.

Existe um **"Filtro"** geral no topo da tela, este filtro permite definir um filtro personalizado que será usado para a filtragem de quais produtos serão ajustados.

A **"Empresa"** em que será feito o Ajuste de Estoque, é a mesma empresa utilizada na Cópia e na Contagem de Estoque. Este campo é obrigatório para gerar zeros, ajustar e para pesquisar as datas de contagem e cópia.

Os campos **"Produto"**, **"Local"** e **"Controle"**, assim como o filtro geral, são utilizados para filtragem do ajuste, por exemplo, se informarmos um produto específico no campo Produto, será feito o ajuste somente para este produto, ou se, por exemplo, informarmos um Local, será feito o reajuste somente para os produtos com estoque naquele Local; da mesma forma funciona para o controle.

**Observação:** os itens das notas de ajustes serão preenchidos com a opção de Venda (fabricação própria) no campo **"Uso do Produto"**.

**Nota:** o campo Controle, somente é apresentado, se o parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"** estiver habilitado. O campo Local somente será exibido se o parâmetro **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** estiver habilitado e se o parâmetro **"Descrição para Local - DESCRLOCAL"** estiver diferente de vazio o campo Local será de acordo com o conteúdo desse parâmetro.

O campo **"Inventário no WMS"** tem a finalidade de filtrar as contagens por inventário no WMS no momento de fazer o Ajuste de Estoque. Ao realizar um Inventário do WMS, seja implantação ou rotativo, nesta tela o sistema pedirá o número do inventário para filtrar o ajuste de estoque por inventário.

Caso o código do inventário não seja digitado, será exibida a seguinte mensagem:

**"Informe o número do Inventário no WMS."**

O **"Preço Unitário"** serve para informar como será calculado o preço dos Produtos incluídos nas notas geradas através do ajuste; se for informado, neste campo, o valor **"Usar o preço informado na TOP"**, o preço será calculado através do campo **"Usar como Preço"** do Cadastro da TOP. A TOP utilizada para pegar o valor deste campo é a TOP configurada na nota usada como modelo. Defina qual o valor será lançado para os produtos na nota de Ajuste.

**Seção Datas**

Informe no campo **"Cópia"** a Data da Cópia do Estoque.

Informe no campo **"Contagem"** a Data da Contagem.

Se não houver Cópia ou Contagem nas datas informadas, o sistema exibirá uma mensagem; ao clicar na lupa  é possível visualizar quais são as datas em que foram feitas copias/contagens.

Através do botão ![gerar](https://ajuda.sankhya.com.br/hc/article_attachments/15507325915031), será gerado na Contagem, um registro com quantidade igual a zero, para os produtos que existirem apenas na Cópia, ou seja, para os produtos que não foram contados. O sistema só gerará Ajuste para os produtos da Cópia que estiverem presentes na Contagem. Por isto, é necessário utilizar este botão sempre que a ausência de Contagem seja em função da inexistência de estoques.

Quando o inverso acontece (produtos que existem na Contagem, mas não existem na Cópia), o sistema considera, automaticamente, que o estoque lógico do sistema seja igual à zero.

Exemplo: copiamos o estoque dos produtos A e B.

Cópia:

Produto A

Produto B

Ao contar, registramos os produtos B e C.

Contagem:

#### Produto B

#### Produto C

Observe que o **"Produto A"**, não foi encontrado no estoque, contudo, não foi digitado "zero" na contagem. Já o **"Produto C"** foi encontrado no estoque, mas não existe registro no sistema, não apareceu na cópia.

Como o Produto A não foi contado, o sistema não ajustará o estoque do mesmo se o botão **"Gerar Zero"** não for acionado.

Já o Produto C, que não possui Cópia, será ajustado automaticamente, independente do acionamento deste botão.

O botão ![Imagem 5: O botão realiza o ajuste do estoque, gerando notas de entrada ou saída, ao terminar o ajuste será mostrado um pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/15507325916055) realiza o ajuste do estoque, gerando notas de entrada ou saída, ao terminar o ajuste será mostrado um pop-up com as notas geradas, ao dar duplo clique no número único da nota gerada, será aberta a [Central - Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414).

Confirmar as notas na tela da Central - Compras | Vendas, para que seja atualizado o estoque, com a baixa ou entrada, conforme a nota ser de Entrada ou Saída.

**Observação:** pode haver no estoque da empresa, produtos que não estejam disponíveis para venda, mas para os quais é necessário fazer contagem e ajuste de estoque. Por isto, o sistema permite ajuste de estoque de **"Produtos Inativos"**.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque#top)

![Imagem 6: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16251327863319) Acesse também:

[Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609654)

[Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514)
