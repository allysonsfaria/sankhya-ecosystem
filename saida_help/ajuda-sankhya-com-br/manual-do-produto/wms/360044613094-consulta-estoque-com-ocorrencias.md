---
id: "360044613094"
titulo: "Consulta Estoque com Ocorrências"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:16Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Consulta", "WMS", "Retorno", "Ocorrências", "Perda", "Divergência", "Estoque", "Ajuste de Estoque", "Transferência", "Avaria", "Sobra", "br.com.sankhya.wms.con.consultaestoqueocorrencias", "Consulta Estoque com Ocorrências manual", "Reimpressão de etiquetas", "Opções de ajuste", "Consulta de estoque"]
---

# Consulta Estoque com Ocorrências

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311514255127) Módulo: WMS > Consultas
```

---

Por meio dessa tela, você pode realizar a consulta de estoque dos endereços destinados a avarias, perdas, sobras e divergências.

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias#filtros) |  | [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias#botooutrasopes...) |
| --- | --- | --- |
| [Botão Gerar Nota de Ajuste](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias#botogerarnotadeajuste) |  |  |

![Imagem 2: Botão Gerar Nota de Ajuste](https://ajuda.sankhya.com.br/hc/article_attachments/4410177470231)

## Filtros

No lado esquerdo da tela, você poderá utilizar alguns filtros rápidos, de modo a agilizar a busca pelos endereços desejados. São eles:

O campo **"Empresa"** é de preenchimento obrigatório. Assim, informe aqui a empresa a qual o endereço desejado está vinculado.

Efetue a busca pelos endereços por meio do campo **"Produto"**, através de um produto em específico. Caso o produto neste campo informado possua algum tipo de Controle, o campo **"Controle"** logo abaixo é habilitado e o controle do produto poderá ser também informado (a nomenclatura desse campo pode ser modificada conforme o tipo de controle do produto escolhido).

No filtro **"Parceiro"**, você poderá buscar os Parceiros vinculados às ocorrências lançadas nessa tela, sendo que, por meio dele, você filtra os Parceiros que utilizam o [Controle de Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros).

Além dos campos citados, através das marcações **"Avaria"**, **"Perda"**, **"Sobra"**, **"Divergência"** e **"Garantia"** você poderá selecionar um ou mais tipos de endereço desejados.

Definidos os filtros, clique em **"Aplicar"**, assim os endereços com seus respectivos estoques serão exibidos na grade posicionada à direita na tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias#top)

## Botão Outras Opções...

Ao acionar o referido botão por meio do ícone ![Imagem 3: Ao acionar o referido botão por meio do ícone , teremos as seguintes opções:](https://ajuda.sankhya.com.br/hc/article_attachments/4410170227095), teremos as seguintes opções:

![Imagem 4: Ao acionar o referido botão por meio do ícone , teremos as seguintes opções:](https://ajuda.sankhya.com.br/hc/article_attachments/4410177697559)

#### Retorno de Estoque

Ao selecionar uma **"Avaria"** ou **"Divergência"** na grade, e acionar esta opção, será aberto o seguinte pop-up:

![Imagem 5: Ao selecionar uma "Avaria" ou "Divergência" na grade, e acionar esta opção, será aberto o seguinte pop-up:](https://ajuda.sankhya.com.br/hc/article_attachments/4410177719575)

Os campos **"Endereço Especial de Origem"**, **"Unidade"** e **"Estoque atual na origem"** são apresentados preenchidos e bloqueados para edição, pois, estes correspondem ao endereço selecionado, a unidade da avaria/divergência e a quantidade atual no estoque, respectivamente.

O campo **"Endereço para Retorno de Estoque"**, refere-se ao endereço para onde a quantidade informada do produto deve retornar.

**Nota:** a unidade do endereço selecionado para a transferência, precisar conter as quantidades múltiplas adequadas para realização da operação.

Além disso, insira a quantidade que retornará para o endereço, no campo **"Quantidade do estoque a retornar"**.

**Nota:** se o endereço selecionado como destino possuir configurações específicas, como **"Multi-Produto"** e/ou **"Lote Único"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) da tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), o sistema irá validar se a transação poderá ou não ser realizada, conforme seu status, quando o botão **"Confirmar"** do pop-up Retorno de Estoque for acionado. Ainda se o endereço possuir regras de permissão na aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto) na tela de Endereços de armazenamento e estiver com a opção **"Permitir",** obrigatoriamente o item deverá ter sido adicionado para que seja aceito no endereço. Da mesma forma deve ocorrer na aba [Grupo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abagrupodeprodutos) da tela Endereços de Armazenamento, ou seja, a transferência será permitida apenas se o produto for vinculado na aba Grupo de Produtos. Quando a opção **"Proibir"** estiver selecionada em ambas as configurações citadas anteriormente, e o produto não for adicionado à aba, o sistema aceitará qualquer produto no endereço de destino informado.

---

#### Transferência de avaria p/ perda

Essa opção realiza uma transferência de forma atômica de um ou mais produtos que estejam no endereço de avaria direto para perda. Nessa opção existe a necessidade de se informar a quantidade a ir para o endereço, preenchendo na grade a coluna **"Qtd. envio p/ Perda"**. Caso a linha seja selecionada para transferência, mas não tenha sido informada qualquer quantidade, a seguinte mensagem será exibida:

**"Não existem itens selecionados para transferência de avaria para perda ou não foi informada a quantidade para envio."**

---

#### Transferência de avaria p/ garantia

Por meio dessa opção, realize o envio de um ou mais produtos que estejam no endereço de avaria para a garantia. Esta funcionalidade quando utilizada gera uma tarefa a ser executada pelo [Coletor de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112173). Dado que, exista um endereço específico para Garantia, a geração de uma tarefa irá conduzir o operador a retirar o produto fisicamente da avaria e enviá-lo para o endereço de garantia.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias#top)

## Botão Gerar Nota de Ajuste

Através dessa opção, você efetuará a geração de notas de ajuste para perda e para sobra (notas de venda e compra). Quando houver um mesmo produto com **"Perda"** e **"Sobra"**, ao selecionar duas linhas para geração das notas de ajuste, o sistema questionará se é desejada a compensação do ajuste que está sendo feito, a seguinte mensagem será apresentada:

**"Na compensação, quando houver registro de perda e de sobra para o mesmo produto, será gerada apenas uma nota de acordo com a diferença entre eles. Nos casos em que a perda e a sobra forem iguais, não será gerada nenhuma nota e os registros de perda e sobra serão excluídos, uma vez que um anula o outro. Deseja gerar compensação quando houver perda e sobra para o mesmo produto?"**

Na apresentação desta mensagem, clicando em **"Sim"** o sistema irá gerar a **"Nota de Ajuste"** de acordo com a diferença entre perda e sobra. Se a Sobra for maior, será gerada uma nota de entrada; sendo a Perda maior, será gerada uma nota de venda; porém, se os dois se anularem não será gerada nenhuma nota de ajuste e as linhas de Perda e Sobra serão excluídas.

Ao clicar em **"Não"** o sistema gerará duas notas distintas, uma para Perda e outra para Sobra. Assim, quando o ajuste for finalizado você poderá visualizar no pop-up **"Nota de Perda/Sobra geradas"** as notas de sobra e perda geradas.

Ao clicar no ícone representado por **"Setas"** localizado a frente do número único da nota, será aberta a [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), onde você poderá visualizar as notas geradas.

**Observação:** a quantidade precisar ser maior que zero quando o botão Gerar Nota de Ajuste for acionado. 

**Nota:** caso tenha alguma divergência ao realizar a contagem de estoque, esta deve ser tratada na tela [Ajuste de Estoque por Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Ajuste-de-Estoque-por-Invent%C3%A1rio) no primeiro momento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias#top)
