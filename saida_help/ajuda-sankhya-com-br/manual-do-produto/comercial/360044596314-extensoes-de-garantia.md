---
id: "360044596314"
titulo: "Extensões de Garantia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596314-Extens%C3%B5es-de-Garantia"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:20:39Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Portal de Vendas", "Extensões de Garantia", "Planos", "Garantias", "Plano de Garantia", "Garantia Obrigatória", "EXTGARANTOBRIG", "br.com.sankhya.cad.exetensoesgarantia", "Extensões de Garantia manual", "TOP", "Vendas", "Serviços Pré-cadastrados", "Planos de Garantia"]
---

# Extensões de Garantia

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311714711319) Módulo: Comercial > Arquivo > Cadastros
```

---

Nesta tela serão cadastrados os Planos com suas respectivas garantias, que são serviços pré-cadastrados para tal.

**Nota:** As Extensões de Garantia de um produto são incluídas apenas nos Pedidos de Venda.

![Imagem 2: Nota: As Extensões de Garantia de um produto são incluídas apenas nos Pedidos de Venda .](https://ajuda.sankhya.com.br/hc/article_attachments/360093849753)

Esta tela possui os seguintes campos:

O campo **"Plano"** é de preenchimento obrigatório e manual, que deve ser informado um código para ele.

Referente ao campo **"Descrição"**, este também será de preenchimento obrigatório e manual, definindo um nome  para o plano; como por exemplo, **"Extensão de 1 ano"**, **"Plano de garantia"**, **"Copa de 2014"** e etc.

Abaixo desses campos, você pode cadastrar as **"Garantias por Serviços"**:

O campo de pesquisa **"Serviço"** é de preenchimento obrigatório e você deve preencher com o serviço que fará parte do plano.

Por meio dos campos **"Valor Mínimo"** e **"Valor Máximo"**, informe a faixa de preço de produtos para qual a garantia será usada. O sistema fará uma validação para estes campos e, caso uma divergência de valores seja verificada, a seguinte mensagem será apresentada:

**"Valor Máximo" deve ser maior ou igual ao "Valor Mínimo".**

Se apenas um desses campos for preenchido, a mensagem não será exibida.

No campo **"Preço"**, informe o preço da garantia. Este preço será acrescentado ao valor do produto.

Na parte superior da tela, existe o botão ![Imagem 3: Na parte superior da tela, existe o botão "Outras Opções..." que apresenta a opção "Copiar Garantias de outro Plano" .…](https://ajuda.sankhya.com.br/hc/article_attachments/16242023744791) **"Outras Opções..."** que apresenta a opção **"Copiar Garantias de outro Plano"**. Essa opção agiliza o cadastro das garantias nos diversos planos, permitindo copiar serviços de garantias de um plano para outro.

![Imagem 4: Na parte superior da tela, existe o botão "Outras Opções..." que apresenta a opção "Copiar Garantias de outro Plano" .…](https://ajuda.sankhya.com.br/hc/article_attachments/360091689414)

No campo Plano, informe de qual plano você deseja copiar a garantia e, na opção **"Para"**, indique para qual plano está sendo copiada a garantia.

**Importante:** Através do campo **"Extensão de Garantia"** localizado na aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abavenda), do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), você vincula uma garantia ao produto. Assim, quando este produto for inserido no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), havendo somente um plano para a faixa de preços da mercadoria, o serviço vinculado (garantia) será incluído automaticamente nos itens da nota.

**Observação:** Alterando a quantidade do produto, a quantidade e o valor do serviço de extensão de garantia também serão alterados, proporcionalmente.

Se houver mais de um plano para a faixa de preços da mercadoria, o sistema exibirá um pop-up para que se efetue a escolha do plano de garantia, incluindo-o nos itens da nota depois da confirmação.

O Serviço de Garantia lançado no pedido só poderá ser excluído se o parâmetro **"Extensão de Garantia Obrigatória? - EXTGARANTOBRIG"** estiver desligado. Caso se encontre habilitado, o usuário e senha do gerente da Central deverão ser informados no momento da exclusão.

**Nota:** Se você desejar excluir o produto e não apenas as garantias, mesmo que este parâmetro esteja ligado, as garantias serão excluídas juntamente com o produto.

A tela de [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) apresenta o painel **"Extensões de Garantia"** que contém as informações sobre os Planos de Garantia Estendida que o produto selecionado possui. Porém, para que ocorra a exibição da extensão de garantia, é necessário que o preço do produto esteja entre o valor mínimo e valor máximo, que são definidos nesta rotina.

**Observação:** Para que esta funcionalidade seja executada corretamente, o parâmetro **"Tem Extensão de Garantias? - TEMEXTGAR"** deve estar habilitado e, no [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes), a marcação **"Exige Garantia?"** habilitada.

Ainda, tem-se o botão  ![Imagem 5: Ainda, tem-se o botão "Edição múltipla" que permite a edição simultânea de vários registros a partir do modo grade. Ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16242023745943) **"Edição múltipla"** que permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com os planos em modo grade na tela Extensões de Garantia selecione-os e em seguida clique no botão Edição múltipla, assim os campos poderão ser editados simultaneamente para os planos selecionados.
