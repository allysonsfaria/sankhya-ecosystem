---
id: "44011939889687"
titulo: "Importação do XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011939889687-Importa%C3%A7%C3%A3o-do-XML"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:15:14Z"
rotulos: ["sync_hc", "magis5", "sync_hash_9d597a3c2962", "magis5_204048557106"]
---

# Importação do XML

Para acessar o módulo de entrada de Notas Fiscais, acesse: Suprimentos → Notas Fiscais de Entrada / Controle de Estoque:

![Imagem 1: Para acessar o módulo de entrada de Notas Fiscais, acesse: Suprimentos → Notas Fiscais de Entrada / Controle de Estoque:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-116-1024x143.png)

É possível realizar a entrada da NF através de um XML enviado pelo fornecedor. Para isso, clique em “Nova Entrada”:

![Imagem 2: É possível realizar a entrada da NF através de um XML enviado pelo fornecedor. Para isso, clique em “Nova Entrada”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-626-1024x158.png)

Será exibida a tela para inserir o XML referente a Nota Fiscal:

![Imagem 3: Será exibida a tela para inserir o XML referente a Nota Fiscal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-628-1024x284.png)

Para inserir o XML, basta clicar em “Selecione” no campo “XML da NF-e” e, após selecionar o XML, clicar em “Carregar dados do XML (NF-e)”:

![Imagem 4: Para inserir o XML, basta clicar em “Selecione” no campo “XML da NF-e” e, após selecionar o XML, clicar em “Carregar…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-629-1024x330.png)

Para realizar a entrada de uma Nota Fiscal, é necessário que o fornecedor esteja cadastrado. Caso contrário, será exibida uma mensagem pedindo que o cadastro seja realizado, para então, prosseguir com a entrada da Nota Fiscal:

![Imagem 5: Para realizar a entrada de uma Nota Fiscal, é necessário que o fornecedor esteja cadastrado. Caso contrário, será…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-630-1024x165.png)

Confirme os dados do fornecedor e clique em “Salvar e recarregar dados do XML”:

![Imagem 6: Confirme os dados do fornecedor e clique em “Salvar e recarregar dados do XML”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-631-1024x331.png)

Ao carregar os dados, todas as informações referente à Nota Fiscal serão exibidas, inclusive os produtos que compõem a Nota:

![Imagem 7: Ao carregar os dados, todas as informações referente à Nota Fiscal serão exibidas, inclusive os produtos que compõem a…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-632-1024x415.png)

Ao carregar os produtos, o **Artemis5** diferencia produtos que estão cadastrados e produtos não cadastrados.

No exemplo acima, o produto da primeira linha (em vermelho) não está cadastrado na plataforma enquanto o outro produto (com a linha em branco) está.

Neste caso, é preciso fazer o vínculo dele à algum produto cadastrado ou então cadastrá-lo.

Para isso, clique no botão “De↔Para” e realize um dos procedimentos acima mencionados:

![Imagem 8: Para isso, clique no botão “De↔Para” e realize um dos procedimentos acima mencionados:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-633-1024x221.png)

Após realizar o vínculo do produto ou cadastrá-lo, confira se as outras informações estão corretas. Para auxiliar, segue o significado de cada item:

- **XML da NF-e:** É o campo utilizado para realizar a entrada da Nota Fiscal por XML;

- **Fornecedor:** Informe o fornecedor do pedido (é obrigatório informar o fornecedor para então, informar o número do pedido. Caso o fornecedor não seja cadastrado, clique em “Cadastrar” para inserir as informações básicas do cadastro);

- **Pedido:** Informe o número do pedido (vinculado ao fornecedor informado). Ao informar o número do pedido, ele carregará todos os itens vinculados ao pedido;

- **Depósito:** Informe qual depósito será abastecido ao realizar a entrada da Nota Fiscal;

- **Data do Recebimento:** Informe a data do recebimento do pedido;

- **Data Emissão NF-e:** Informe a data de emissão da Nota Fiscal;

- **Número NF-e:** Informe o número da Nota Fiscal;

- **Total Frete:** Informe o valor do frete do pedido;

- **Valor NF-e:** Campo não editável. É a soma do “Total Frete” + “Itens do Pedido”;

- **Desconto:** Caso essa nota fiscal possua algum desconto, informar neste campo;

- **Total NF-e:** Campo não editável. É o “Valor NF-e” menos o “Desconto”

- **Especificar natureza dos itens:** Informe a classificação do plano de contas para o lançamento financeiro (ao selecionar este checkbox, a coluna do preço de custo abre automaticamente) - caso esteja preenchido no cadastro do fornecedor, este campo virá preenchido;

- **Alterar valor de custo:** Utilizada para alterar o valor de custo atual dos produtos em sistema

- **Especificar endereço:** Utilizado em empreendimentos que controlam estoques por endereços. Neste campo é possível identificar qual o endereço do produto em questão.

Após revisar todos os campos é hora de inserir as duplicatas referente à Nota Fiscal, caso não venha preenchido ao realizar a leitura do XML. Para isso, no campo “Duplicatas”, clique em (+), insira o número da duplicata, o vencimento, o valor e clique em “Incluir”:

![Imagem 9: Após revisar todos os campos é hora de inserir as duplicatas referente à Nota Fiscal, caso não venha preenchido ao…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-635-1024x463.png)

Feito isso, será necessário informar uma Conta Bancária e um Plano de Contas para o lançamento das duplicatas:

![Imagem 10: Feito isso, será necessário informar uma Conta Bancária e um Plano de Contas para o lançamento das duplicatas:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-634-1024x180.png)

Após finalizar os lançamentos, clique em “Salvar”:

![Imagem 11: Após finalizar os lançamentos, clique em “Salvar”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-636-1024x432.png)
