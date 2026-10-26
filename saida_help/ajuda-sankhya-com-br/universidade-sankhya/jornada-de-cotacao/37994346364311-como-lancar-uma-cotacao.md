---
id: "37994346364311"
titulo: "Como lançar uma cotação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37994346364311-Como-lan%C3%A7ar-uma-cota%C3%A7%C3%A3o"
trilha: "Universidade Sankhya > Jornada de Cotação"
atualizado_em: "2026-07-22T14:03:10Z"
rotulos: ["Produtos", "Cotação", "Projeto", "Centro de Resultado", "Fornecedores", "ERP", "Compras"]
---

# Como lançar uma cotação

## Registro de cotação/orçamento manual

#### Qual é o objetivo do registro de uma cotação e por que esse procedimento é essencial para a tomada de decisões?

O registro manual de cotação consiste na inserção das informações obtidas junto aos fornecedores sobre preços, prazos e condições de compra. Esse procedimento permite à empresa comparar diferentes propostas e selecionar a opção com melhor custo-benefício. Ao centralizar esses dados no sistema, o processo de compras se torna mais estratégico e transparente, facilitando decisões baseadas em critérios objetivos e bem documentados. Essa prática contribui diretamente para a eficiência operacional, redução de custos e melhoria na negociação com fornecedores, garantindo que as aquisições atendam às necessidades da empresa da forma mais vantajosa possível.

#### Quais problemas este recurso resolve?

- **Decisões de compra pouco embasadas:** A centralização das informações dos fornecedores permite comparar critérios como preço, prazo e qualidade, evitando escolhas aleatórias ou mal fundamentadas.
- **Falta de histórico para análise:** Com os registros no sistema, é possível consultar cotações anteriores, identificar padrões e melhorar o planejamento futuro.
- **Desorganização nas negociações:** O controle estruturado evita perda de dados, falhas de comunicação e inconsistências nas informações de compra.

#### Quais os riscos de não utilizar?

Não utilizar esse recurso pode levar à perda de oportunidades de negociação e leva à escolha de fornecedores com condições desfavoráveis. A ausência de registro dificulta a rastreabilidade das decisões, aumenta a chance de erros e compromete a transparência nas compras. Além disso, sem uma base comparativa estruturada, a empresa pode realizar aquisições com preços acima do mercado, impactando diretamente o fluxo de caixa e a rentabilidade. A falta de controle também prejudica a relação com fornecedores e reduz a capacidade de resposta diante de auditorias ou revisões de processos.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP.

1. **Acesse a tela Cotação**
   Cotação >> Rotinas >> Cotação

- Clique no botão “+” (Cadastrar itens da cotação), o sistema abre a tela nova cotação para registro de uma nova cotação.

**Na aba “Geral” informe os dados básicos da cotação.**

- **Empresa**: informe aqui a empresa que está requisitando os produtos da cotação.
- **Centro de Resultado:** preencha aqui, o centro de resultados referente ao processo de cotação, para fins de controle gerencial.
- **Natureza:** informe neste campo a natureza referente ao processo de cotação.
- **Projeto:** é inserido aqui o projeto referente ao processo de cotação.
- **Usuário Responsável:** informe neste campo, o responsável pela cotação a ser realizada;
- **Usuário Comprador:** este campo é preenchido automaticamente com o usuário logado no sistema e não permite a edição.
- **Data inicial da cotação:** preencha este campo com a data e hora inicial da cotação, caso não seja informada, o sistema preenche este campo com a data e hora atuais ao concluir a inserção.
- **Data final da cotação:** informe neste campo, a data e hora final da cotação também para fins de filtro e controle.

**Feito isso, preencha na aba “Itens da Cotação", quais itens serão cotados neste momento.**

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

2. **O próximo passo é adicionar os fornecedores a serem cotados. Localize a cotação recém criada e dê um duplo clique.**

- Clique no botão **“...”** (**Outras opções**), e escolha a opção  **“Sugerir Fornecedores”**.
- Será aberto o popup de **“Sugestão de fornecedores”**.

**O campo "Fornecedores" é composto por opções que ajudam a filtrar a sugestão de fornecedores, ele possui as seguintes opções:**

- **“Que já forneceram”:** Busca todos os fornecedores que possuírem uma nota de compra confirmada para os produtos selecionados, considerando o filtro de periodicidade definido no campo **“Período por”**.
- **Que já cotaram:** Esta opção busca de todos os fornecedores que foram informados na cotação dos produtos selecionados, considerando o filtro de periodicidade definida no campo **“Período por”**.
- **Dos itens selecionados:** Esta opção busca os fornecedores que já se encontram inseridos nos itens selecionados anteriormente para cotação dos demais itens da nota. Essa opção é útil para comparar preços de todos os fornecedores para todos os produtos.
- **Do perfil de consumo x perfil principal do parceiro:** Esta opção realiza a busca dos fornecedores que possuem o perfil principal do cadastro, igual ao perfil de consumo dos produtos selecionados.
- **Do perfil de consumo x perfil do parceiro:** Esta opção busca os fornecedores que possum o perfil do cadastro igual ao perfil de consumo dos produtos selecionados.

Após definir o campo “**Fornecedores”** com uma das opções acima, clique no botão "**Buscar**" para efetuar o filtro escolhido.

- No botão “**+**” é possível adicionar outros fornecedores que não foram filtrados pelo critério da busca.
- Ao adicionar um novo fornecedor, informe para quais dos produtos selecionados o fornecedor será inserido.
- O botão **"Visualizar Produto"** permite visualizar para quais produtos o fornecedor sugerido será inserido, a partir dos critérios de busca.
- O botão **"Substituir"** é utilizado na substituição de um fornecedor sugerido pelo sistema por outro fornecedor, sendo possível escolher para quais produtos o fornecedor será substituído.
- Os botões **"Remove todas as linhas selecionadas"** e **"Remove todas as linhas não selecionadas"**, servem para retirada de fornecedores que não deseja-se inserir.
- Ao clicar no botão "**OK**", o sistema confirmará a operação ao inserir os devidos fornecedores para os itens selecionados.
- Os fornecedores selecionados são inseridos na aba **“Fornecedores e Coleta de Preços”.**
- Agora, a coleta de preços pode ser feita de forma **manual ou automática** a depender dos fornecedores escolhidos.
- Após todos os fornecedores serem cotados, a situação do produto se torna “Precificada”

#### Correção e repetição

- Lembre que não é possível gerar uma nova cotação para produtos que já possuem uma cotação em aberto.
- Confirme que todos os campos obrigatórios foram preenchidos de maneira correta e completa.
- Observação: o módulo de cotação não suporta o **Controle de Produtos por Grade**.
- Certifique-se de que os valores inseridos estão conforme as políticas e diretrizes da empresa, garantindo conformidade e precisão no pedido.
- Se os valores sugeridos não forem os esperados, revise o processo e corrija as informações necessárias antes de tentar novamente.
- Para reforçar sua habilidade no sistema, pratique criando um novo cenário, como um fornecedor, cliente ou produto diferente.
- Ao preencher o campo usuário responsável, o sistema verifica o parâmetro "**O responsável pela cotação tem que ser comprador? - RESPCOTCOMPR**".
