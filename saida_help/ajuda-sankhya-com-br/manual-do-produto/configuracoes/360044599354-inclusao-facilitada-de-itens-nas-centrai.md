---
id: "360044599354"
titulo: "Inclusão Facilitada de Itens nas Centrais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599354-Inclus%C3%A3o-Facilitada-de-Itens-nas-Centrais"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:48Z"
rotulos: ["Produtos", "Configuração", "Inclusão Facilitada de Itens nas Centrais", "Inclusão Facilitada de Itens nas Centrais manual", "Central de Vendas", "Movimentação Financeira", "Estoque"]
---

# Inclusão Facilitada de Itens nas Centrais

Quando o parâmetro **"Inclusão facilitada de produtos controlados por lista - INCFACPROLIS"** estiver Ligado o sistema habilitará na [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), na grade Itens, uma nova aba para inserção de itens na nota, de nomenclatura **"Facilitado"**.

A aba Facilitado tem como objetivo dinamizar a inclusão de produtos com Controle Adicional do tipo Lista; nela será apresentada apenas uma linha para cada produto, independente do controle. Os campos Quantidade e Controle não são apresentados em modo grade ou em modo de edição; todos os controles e suas quantidades são exibidos ao lado direito do painel da Central de Notas. Vejamos a imagem abaixo:

![Imagem 1: A aba Facilitado tem como objetivo dinamizar a inclusão de produtos com Controle Adicional do tipo Lista ; nela será…](https://ajuda.sankhya.com.br/hc/article_attachments/9005146211223)

Na imagem acima, tem-se o painel com as quantidades dos controles do produto; pode-se observar à direita o Título do controle (informado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-) - aba Medidas e Estoque - sub-aba Controle Adicional), bem como as Quantidades de cada Controle do produto.

Caso não seja informada nenhuma quantidade para o controle, ele não será incluído na nota. Para cada quantidade informada nos controles, uma linha será incluída nos itens da nota; as informações incluídas podem ser vistas pela aba Padrão. Caso o controle possua quantidade e for alterado para o valor zero, a linha será removida dos itens. Caso alguma informação seja alterada por esse painel, todos os itens da aba Padrão terão seus valores alterados, por exemplo, caso seja alterado o valor unitário, todos os itens da nota desse produto terão seus valores unitários modificados para um novo valor.

A aba Facilitado permite inserção apenas de produtos que tenham Controle Adicional de Estoque do tipo Lista; os demais deverão ser adicionados pela aba Padrão. Os produtos adicionados pela aba Padrão e que não possuem Controle Adicional de Estoque do tipo Lista não irão aparecer na grade da aba Facilitado.

**Observação:** esta funcionalidade não se aplica a produtos com tabela de preço que tenham preços diferentes para cada controle. Além disso, caso seja necessário realizar modificações nas linhas da aba Padrão, ou seja, alterar algum campo para algum controle em específico, pode-se proceder com as modificações, porém deve-se ajustar algo somente depois de finalizadas todas as alterações no item na aba Facilitado; caso contrário, as informações alteradas na aba Padrão serão perdidas; uma simples alteração na quantidade de algum controle pela aba Facilitado fará com que todas as linhas daquele produto na aba Padrão sejam atualizadas conforme a modificação realizada.

## Inclusão Facilitada por Referência

Além da forma de inserção de itens relatada acima, com a ativação do parâmetro **"Lançamento por referência (Inclusão facilitada) - USAINCFACLANREF"**, será possível realizar a inclusão de itens na aba Facilitado informando-se a referência dos mesmos. Pode-se pesquisar um produto informando sua referência diretamente no campo de pesquisa e teclando-se Enter ou ainda clicando-se no botão de pesquisa e localizando o item desejado.

![Imagem 2: Além da forma de inserção de itens relatada acima, com a ativação do parâmetro "Lançamento por referência (Inclusão…](https://ajuda.sankhya.com.br/hc/article_attachments/9005169036951)

Ao digitar a referência do item, e pressionando-se Enter, o sistema carrega o produto localizado na primeira grade posicionada abaixo do campo Referência; selecionando o produto desejado nesta primeira grade e pressionando Enter uma segunda vez, este produto é apresentado na segunda grade, onde à direita, tem-se os controles correspondentes ao item, bem como suas respectivas quantidades a serem informadas. Em suma, a grade superior é alimentada a medida que a referência dos itens é informada; teclando-se Enter, este produto é carregado na grade inferior, onde preenche-se suas devidas quantidades.

Uma vez inseridas as quantidades de itens necessárias, pode-se proceder normalmente com a confirmação do documento.

## Controles na Inclusão Facilitada

É possível que os controles utilizados nos Produtos sejam exibidos na grade de inclusão facilitada; para tal, é necessário que o parâmetro **"Controles apresentados na Inclusão facilitada - ITELSTGRADE"** seja alimentado com os controles desejados; os mesmos devem ser incluídos separados por vírgula.

![Imagem 3: É possível que os controles utilizados nos Produtos sejam exibidos na grade de inclusão facilitada; para tal, é…](https://ajuda.sankhya.com.br/hc/article_attachments/9005227609751)

Após serem configurados no parâmetro, esses controles serão apresentados na grade de inclusão facilitada; a medida que as quantidades forem informadas, as respectivas colunas serão preenchidas.

![Imagem 4: Após serem configurados no parâmetro, esses controles serão apresentados na grade de inclusão facilitada; a medida que…](https://ajuda.sankhya.com.br/hc/article_attachments/9005264847127)

Caso não seja informada quantidade para o produto, sua coluna correspondente será exibida com valor "0" (zero).

**Importante:** para que as colunas correspondentes aos controles seja apresentadas na grade, é necessário que o layout de documento utilizado, não seja o layout padrão; esta definição é realizada na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), onde a marcação **"Usar como padrão para este tipo de movimento?"** não pode estar efetuada.

Se outros produtos forem adicionados, e possuírem estes mesmos controles, serão adicionadas em novas linhas da grade normalmente.

![Imagem 5: Se outros produtos forem adicionados, e possuírem estes mesmos controles, serão adicionadas em novas linhas da grade…](https://ajuda.sankhya.com.br/hc/article_attachments/9005251215767)
