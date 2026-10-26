---
id: "37995002697239"
titulo: "Como lançar o pedido de cotação através de requisições internas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37995002697239-Como-lan%C3%A7ar-o-pedido-de-cota%C3%A7%C3%A3o-atrav%C3%A9s-de-requisi%C3%A7%C3%B5es-internas"
trilha: "Universidade Sankhya > Jornada de Cotação"
atualizado_em: "2026-07-22T14:03:03Z"
rotulos: ["Configuração", "Cotação", "Requisições", "Centro de Resultado", "ERP", "Compras"]
---

# Como lançar o pedido de cotação através de requisições internas

## Compra em função de solicitações ou requisições internas

#### Qual é o objetivo de realizar compras em função de solicitações ou requisições internas e por que esse procedimento é essencial para a tomada de decisões?

Realizar compras com base em solicitações internas garante que os produtos ou serviços adquiridos atendam às demandas específicas da empresa, promovendo clareza e priorização. Esse procedimento centraliza as necessidades dos setores, evita compras desnecessárias, melhora o uso de recursos e assegura controle e rastreabilidade, permitindo decisões mais estratégicas e alinhadas aos objetivos organizacionais.

#### Quais problemas o procedimento resolve?

- **Falta de organização e clareza nas demandas internas:** O procedimento evita compras desnecessárias ou desalinhadas às necessidades dos setores.
- **Retrabalho e  inconsistências no atendimento de requisições:**  Essa melhor prática elimina retrabalho e inconsistências no atendimento de requisições, melhora o uso eficiente de recursos e reduz atrasos na aquisição de itens críticos.
- **Falta de controle e rastreabilidade:** assegurando que as compras estejam alinhadas aos objetivos estratégicos da empresa.

#### Quais os riscos de não utilizar?

Não utilizar esse procedimento traz riscos como **desorganização nas demandas internas**, resultando em compras desnecessárias, duplicadas ou desalinhadas às prioridades da empresa. A falta de controle pode gerar atrasos no atendimento de itens críticos, uso ineficiente de recursos e aumento de custos. Além disso, dificulta a rastreabilidade e o planejamento, comprometendo a eficiência operacional e a capacidade de tomar decisões estratégicas baseadas em dados confiáveis.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP.

É possível incluir uma cotação a partir do lançamento de **“Pedidos de Vendas", “Pedidos de Requisição", “Vendas"** e **“Requisições"**. 

1. Acesse a tela “**Portal de Mov. Interna”**
   Comercial » Consulta

- Selecione o “**Tipo de Movimento - Pedido de requisição”**
- Clique na opção “**Novo Registro”**
- Preencha as informações do “**Cabeçalho”** e clique em “**Salvar”**
- Na grade “**Itens”**, preencha as informações do produto
- Clique em “**Confirmar”**
- Agora, localize o Pedido de requisição lançado
- Clique no botão **“...”** (**Outras opções**) no menu.
- Para iniciar o processo de Cotação, escolha a opção **“Gerar Solicitação de Compra"** ou **"Gerar Solicitação de Compra para produto sem estoque"**, conforme a necessidade da empresa.

2. **Acesse a tela Cotação**
   Cotação >> Rotinas >> Cotação

- Utilize os **“Filtros Rápidos”** para localizar a solicitação, e acesse a opção **“Alterar Cabeçalho da Cotação"** para complementar os dados da cotação.

**Na aba “Geral” informe os dados básicos da cotação que podem não ter sido preenchidos na requisição.**

- **Empresa**: informe aqui a empresa que está requisitando os produtos da cotação.
- **Centro de Resultado:** preencha aqui, o centro de resultados referente ao processo de cotação, para fins de controle gerencial.
- **Natureza:** informe neste campo a natureza referente ao processo de cotação.
- **Projeto:** é inserido aqui o projeto referente ao processo de cotação.
- **Usuário Responsável:** informe neste campo, o responsável pela cotação a ser realizada;
- **Usuário Comprador:** este campo é preenchido automaticamente com o usuário logado no sistema e não permite a edição.
- **Data inicial da cotação:** preencha este campo com a data e hora inicial da cotação, caso não seja informada, o sistema preenche este campo com a data e hora atuais ao concluir a inserção.
- **Data final da cotação:** informe neste campo, a data e hora final da cotação também para fins de filtro e controle.

#### Feito isso, preencha na aba “Itens da Cotação", quais itens serão cotados neste momento.

- **Produto:** informe quais itens deverão ser cotados.
- **Volume:** defina o volume (unidade) em que o produto deverá ser cotado.
- **Quantidade:** determine qual a quantidade deste produto a ser cotada.
- **Local:** caso o produto possua local de estoque, informe-o neste campo.
- **Dt. Limite:** neste campo é necessário informar até que data a empresa precisa desse produto.
- Se julgar necessário, utilize o campo “**Observação**” para informações complementares.

**Na aba “Pesos e Critérios", defina quais quesitos serão considerados na classificação dos fornecedores, e o peso de cada um.**

- Caso não seja definido peso para os critérios,  o sistema assume o valor padrão **“1”** para  o critério “**Preço**" e **“0”** para os demais critérios.
- Utilize o botão “**Critérios**” para filtrar um critério previamente determinado, substituindo os valores dos campos pelos definidos no cadastro.
- Ao clicar em “**Confirmar**” a Cotação é incluída, retornando para a tela inicial.
- Clique no botão ‘Modo Formulário’ ou dê um duplo clique sobre o produto para visualizar a aba ‘Fornecedores e Coleta de Preços’.
- Essa aba contém as informações das cotações de cada fornecedor, que serão utilizadas no apoio à decisão do comprador no momento de escolher a melhor oferta.

**Para a coleta de fornecedores, acesse a aba “Itens da Cotação", na sub aba “Fornecedores e Coleta de Preços”.**

- Os fornecedores podem ser adicionados manualmente nesta aba ou através da cotação online no botão **“...”** (**Outras opções**), através da opção  **“Sugerir Fornecedores”**.
- Será aberto o popup de **“Sugestão de fornecedores”**.

**O campo "Fornecedores" é composto por opções que ajudam a filtrar a sugestão de fornecedores:**

- A opção **“Que já forneceram”:** Busca todos os fornecedores que possuírem uma nota de compra confirmada para os produtos selecionados, considerando o filtro de periodicidade definida no campo “Período por”.
- **Que já cotaram:** Esta opção busca de todos os fornecedores que foram informados na cotação dos produtos selecionados, considerando o filtro de periodicidade definida no campo “Período por”.
- **Dos itens selecionados:** Esta opção busca os fornecedores que já se encontram inseridos nos itens selecionados anteriormente para cotação dos demais itens da nota. Essa opção é útil para comparar preços de todos os fornecedores para todos os produtos.
- **Do perfil de consumo x perfil principal do parceiro:** Esta opção realiza a busca dos fornecedores que possuem o perfil principal do cadastro, igual ao perfil de consumo dos produtos selecionados.
- **Do perfil de consumo x perfil do parceiro:** Esta opção busca os fornecedores que possum o perfil do cadastro igual ao perfil de consumo dos produtos selecionados.

Após definir o campo **Fornecedores** clique no botão "**Buscar**" para efetuar o filtro escolhido na grade da tela dos fornecedores obtidos.

- No botão “**+**” é possível adicionar outros fornecedores que não foram filtrados pelo critério da busca. Ao adicionar um novo fornecedor, informe para quais produtos, dos selecionados, o fornecedor será inserido.
- O botão **"Visualizar Produto"** permite visualizar para quais produtos o fornecedor sugerido será inserido, a partir dos critérios de busca.
- O botão **"Substituir"** é utilizado na substituição de um fornecedor sugerido pelo sistema por outro fornecedor, sendo possível escolher para quais produtos o fornecedor será substituído.
- Os botões **"Remove todas as linhas selecionadas"** e **"Remove todas as linhas não selecionadas"**, servem para retirada de fornecedores que não deseja-se inserir.
- No pop-up de **"Sugestão de fornecedores"**, informe se os fornecedores obtidos pelo critério acessam ou não o **Portal de Cotação Online**, qual foi a data da última compra realizada junto a este fornecedor e qual a quantidade de notas de compra confirmadas feitas com o mesmo.
- Ao clicar no botão "**OK**", o sistema confirmará a operação ao inserir os devidos fornecedores para os itens selecionados.
- Agora, a coleta de preços pode ser feita de forma **manual ou automática**.

#### Correção e repetição

- Confirme que todos os campos obrigatórios foram preenchidos de maneira correta e completa.
