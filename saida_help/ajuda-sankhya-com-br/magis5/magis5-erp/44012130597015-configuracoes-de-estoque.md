---
id: "44012130597015"
titulo: "Configurações de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012130597015-Configura%C3%A7%C3%B5es-de-Estoque"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:21:53Z"
rotulos: ["sync_hc", "magis5", "magis5_204048387417", "sync_hash_1ae757ee30a8"]
---

# Configurações de Estoque

## No Artemis5, o estoque dos produtos é organizado em depósitos, sendo o depósito principal considerado o depósito padrão.

No entanto, é possível utilizar mais de um depósito para armazenar os produtos, cada um deles identificado por um ID único.

Além disso, é possível criar depósitos adicionais para atender necessidades específicas, como depósitos por terminal de atendimento ou até mesmo depósitos virtuais para registrar ocorrências como quebra de estoque.

Para acessar as configurações de estoque dentro do Artemis5, clique em **Configurações > Configurações Gerais** na barra de menu na parte superior e depois clique na aba **Estoque**.

![Imagem 1: Para acessar as configurações de estoque dentro do Artemis5, clique em Configurações > Configurações Gerais na barra de…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-12.png)

Não há limites definidos para a quantidade de depósitos que podem ser criados no **Artemis5**, permitindo que você adapte o sistema de estoque às particularidades do seu empreendimento.

![Imagem 2: Não há limites definidos para a quantidade de depósitos que podem ser criados no Artemis5 , permitindo que você adapte…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-280.png)

- **Depósito Padrão**: É o estoque principal dos produtos no empreendimento. O depósito padrão pode ser configurado por terminal de atendimento, sendo o terminal 1 - depósito padrão A, terminal 2 - depósito padrão B, e assim sucessivamente. O depósito padrão não precisa ser o mesmo em todo o empreendimento;

- **Depósito Padrão para Tratativa de Erro de Separação**: É um depósito virtual utilizado quando há quebra de estoque. O item é removido do depósito padrão e, para não ficar perdido, é transferido para este depósito;

- **Telefone Reposição Estoque Padrão**: Utilizado para notificação de pedidos de reposição de lojas (utilizado em conjunto ao módulo de reposição de lojas);

- **ID do Empreendimento Padrão Fabricação**: Configurado nas lojas. É utilizado para informar às lojas e distribuidoras qual empreendimento é a fábrica (identificado pelo ID) e, com isso, bloquear o acesso e/ou edição da ficha técnica dos produtos;

- **ID do Empreendimento Padrão Distribuição**: Configurado na fábrica. É utilizado para identificar a distribuidora que irá receber a mercadoria após produção (identificado pelo ID).
  Após a produção dos produtos, é gerado um pedido de transferência e os produtos são enviados para a distribuidora. É gerado um alerta para a distribuidora informando que há uma remessa de produtos para recebimento. É possível bloquear o envio de produtos para a distribuidora caso seja necessário (neste caso, deve-se selecionar “Não” em “Bloquear Transf. Produção”).

![Imagem 3: ID do Empreendimento Padrão Distribuição : Configurado na fábrica. É utilizado para identificar a distribuidora que irá…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-281.png)

- **Plano de Contas Valorização de Estoque:** Utilizado no DRE. Caso esteja configurado um plano de contas, ao gerar o DRE, será exibido um plano de contas com valorização do estoque baseado no depósito padrão configurado.

- **Plano de Contas Padrão para Entrada de Notas** e **Conta Bancária Padrão para Entrada de Notas**: Utilizado na entrada de notas fiscais. Caso esses campos estejam preenchidos, ao receber uma nota fiscal com as parcelas discriminadas, não será necessário preencher este campo manualmente na entrada da nota fiscal;

- **Controlar validade nas Transferências entre Depósitos?** Caso o empreendimento faça o controle de produtos por validade na transferência, o usuário determina quais produtos serão transferidos entre as unidades por validade. 
  Se a empresa não controla os produtos por validade e o usuário não quer fazer a seleção de forma manual, é utilizado um método de controle de estoque chamado “FIFO” (First In, First Out - Primeiro a entrar, primeiro a sair) onde é enviado do produto mais antigo para o mais novo em estoque;

- **Ocultar produtos que não controlam o estoque?** Marque “Sim” caso o empreendimento controle o estoque de produtos de uso pessoal, por exemplo: produtos de limpeza, escritório, etc.

- **Finalizar Ordem de Produção no PDV?** Utilizado para controle de venda de produtos compostos no PDV. Ao realizar a venda de um produto composto, o sistema irá gerar uma Ordem de Produção para gerar o estoque do produto composto para posterior baixa no momento da venda;

- **Sempre gerar vendas a partir do envio de mercadoria?** Para qualquer tipo de operação fiscal, o **Artemis5** só conseguirá emitir Nota Fiscal se tiver uma venda atrelada, independente se o empreendimento é próprio ou compartilhado.
  - Caso selecione “Não”, a mercadoria será enviada e será realizada a baixa no estoque como uma “Transferência”, porém, como não irá gerar venda a partir do envio da mercadoria, não será possível emitir Nota Fiscal.
  - Caso selecione “Sim”,  o envio é realizado, é gerado a baixa no estoque dessa transferência e lançada uma venda. Na tela de transferência, haverá um botão de “Gerar Nota Fiscal”, onde o lojista poderá escolher o tipo de operação fiscal desejada: Venda ou transferência (cada um com uma tabela diferente). Optar pela transferência significa que está transferindo produtos da matriz para a filial. O optar pela venda significa que está enviando produtos da distribuidora para a loja.

- **Controlar estoque por endereço?** Utilizado em distribuidoras que controlam o estoque por endereços;

![Imagem 4: Controlar estoque por endereço? Utilizado em distribuidoras que controlam o estoque por endereços;](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-282.png)
![Imagem 5: Controlar estoque por endereço? Utilizado em distribuidoras que controlam o estoque por endereços;](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-283.png)

- **Tipo de Alerta para Produto Não Localizado**: Determina se o tipo do alerta ao conferir um produto será curto ou longo. Há duas situações em que esse alerta pode ocorrer: Quando o conferencista realiza a leitura de um produto que não está na lista de produtos em separação ou quando o conferencista realiza a leitura de mais itens, além do que está na lista de separação (Por exemplo: na lista há três produtos e ele tenta realizar a leitura de quatro produtos);

![Imagem 6: Tipo de Alerta para Produto Não Localizado : Determina se o tipo do alerta ao conferir um produto será curto ou longo.…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-285-1024x597.png)

- **Carregar produtos matéria prima automaticamente na contagem de estoque?** Utilizado no Inventário do Estoque. Quando sim, os produtos de matéria prima serão carregados automaticamente. Quando não, o lojista precisará selecionar item a item;

- **Realizar baixa do estoque ao enviar um pedido de transferência?** Utilizado na execução de um pedido de transferência. Se selecionar “Não”, a baixa do estoque só acontece quando o solicitante recebe a mercadoria. Quando sim, é dado baixa no estoque no momento do envio do pedido de transferência;

- **Gerar pedido de transferência após gerar Romaneio de Separação?** Utilizado em situações onde foi realizada a venda de um item e não tinha todas as unidades deste item no depósito padrão. Neste caso, ao gerar o romaneio de separação, é feito um pedido de transferência automaticamente para outro depósito para que seja realizada a entrega do produto.
  A ordem de saída do depósito é configurada no módulo Caixas → Depósito

![Imagem 7: Gerar pedido de transferência após gerar Romaneio de Separação? Utilizado em situações onde foi realizada a venda de um…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-284-1024x253.png)

- **Atualizar o depósito da venda para depósito padrão ao finalizar o Romaneio de Separação?** Utilizado em empreendimentos que mesclam depósitos para realizar uma venda. Para que conste que a venda foi realizada pelo depósito padrão, marque “Sim” (mesmo utilizando itens de outro depósito);

- **Bloquear envio de produtos excedentes no envio de mercadoria?** Utilizado para bloquear o envio de itens excedentes ao que realmente foi pedido na venda. Caso haja uma venda com 10 unidades e o lojista queira enviar 12, não é possível caso esteja marcado “Sim”;

- **Obrigatório preencher natureza dos itens na entrada de estoque?** Utilizado na entrada de produtos no estoque por nota fiscal. Caso tenha algum produto não cadastrado no **Artemis5,** será necessário realizar o cadastro dele. 
  Quando marcado “Sim” nesta configuração, no cadastro do produto será obrigatório o preenchimento do campo “Natureza de Operação”. Quando marcado “Não”, pode-se dar entrada no estoque sem preencher a “Natureza de Operação”.

- **Obrigatório valorizar estoque no inventário?** Utilizado no inventário. Caso sim, a valorização do estoque se torna obrigatória. 
  Neste caso, em “Itens Inventariados” abre-se uma coluna (R$) e os produtos precisam ter seu preço de custo inserido. A multiplicação é baseada em “R$ Custo” x “Qtd. Dif”.
  Quando não, a valorização é opcional. Abre-se um checkbox e o lojista pode optar por fazer ou não fazer a valorização do inventário:

![Imagem 8: Obrigatório valorizar estoque no inventário? Utilizado no inventário. Caso sim, a valorização do estoque se torna…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-286.png)

- **Conferir venda automaticamente no romaneio de separação:** Caso selecione “Sim”, o conferencista emite o romaneio de separação (que deve ser separado por vendas e não por produto), separa as vendas e as coloca na caixa para despacho, na qual os produtos serão conferidos automaticamente pela plataforma. 
  Caso selecione “Não”, a conferência dos produtos da venda será manual e deverá ser realizada após a separação dos itens através do Romaneio de Separação.

- **Permitir transferência de produtos zerados?** Caso sim, permite que produtos com estoque zerado possam ser transferidos para outros depósitos.

- **Depósito para visualização de estoque (Produtos)**: Utilizado para configurar quais serão os estoques que serão exibidos na tela de produtos. Caso não esteja configurado, irá exibir apenas os produtos do empreendimento logado.

**Imagem 1:**

![Imagem 9: Imagem 1:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-287.png)

**Imagem 2:**

![Imagem 10: Imagem 2:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-289-1024x237.png)

**Imagem 3:**

![Imagem 11: Imagem 3:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-288-1024x238.png)

**Imagem 4:**

![Imagem 12: Imagem 4:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-290-1024x234.png)

Na demonstração acima temos:

- Imagem 1: Depósitos selecionados na configuração “Depósito para visualização de estoque (Produtos)”;
- Imagem 2: Depósito Distribuidora e depósito Suplementos sendo exibidos e o estoque de ambos somados;
- Imagem 3: Apenas depósito Distribuidora selecionado e o estoque referente a ele;
- Imagem 4: Apenas depósito Suplementos selecionado e o estoque referente a ele.

Observação: Na tela de produtos, ao clicar na coluna estoque de um produto, será possível verificar quantas unidades do produtos consta em cada depósito:

![Imagem 13: Observação: Na tela de produtos, ao clicar na coluna estoque de um produto, será possível verificar quantas unidades do…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-292-1024x236.png)

- **Motivo para Baixa Manual de Estoque:** Utilizado para identificar quais os motivos para a retirada do produto do estoque. É possível a criação de um ou mais motivos para realização da baixa manual. Para isso, insira no campo abaixo identificado pelo retângulo e clique em salvar:

![Imagem 14: Motivo para Baixa Manual de Estoque: Utilizado para identificar quais os motivos para a retirada do produto do estoque.…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-291.png)

- **Configuração Grupo de Bloco K:** Utilizado, obrigatoriamente, por empresas Lucro Real. É um relatório com o estoque classificado e valorizado fiscalmente. Este relatório deve informar de onde será extraído o preço e de onde será extraído o estoque dos quatro grupos de produtos, sendo: Mercadoria para Revenda, Matéria Prima, Material de Embalagem e Produto  Acabado, item-a-Item. Após, é necessário inserir a quantidade e valor de cada item no relatório.

Segue um exemplo de configuração :

![Imagem 15: Segue um exemplo de configuração :](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-293.png)

Neste exemplo, a Mercadoria para Revenda, Matéria Prima e o Produto  Acabado tem sua base de preço na Fábrica e o Material de Embalagem, na distribuidora. Também estamos dizendo que a Mercadoria para Revenda e a Matéria Prima tem seu depósito base no Depósito da Fábrica e o Material de Embalagem e Produto Acabado, na distribuidora. 
Obs: O produto acabado tem seu preço de custo definido na fábrica, porém, o estoque, no depósito.

Vale lembrar que cada empreendimento terá uma configuração distinta e a representação acima foi apenas um exemplo.

- **Configuração Grupo de SPED:** Utilizado, obrigatoriamente, por empresas Lucro Real. É a apuração dos impostos baseado em tudo o que foi comprado e vendido dos principais impostos recolhidos na entrada e saída (IPI, ICMS, PIS e Cofins). Um relatório é gerado e enviado para a contabilidade informando quanto foi recolhido por produto;

**SEPARAÇÃO**

- **Preferência de Separação:** Utilizado para casos onde há um erro na separação de produtos (por exemplo: foram realizadas algumas vendas, porém, na hora de separar os produtos, foi identificado que um dos itens está em falta, não sendo possível completar o envio total de itens para todas as vendas).
  Neste caso, com base na opção selecionada é determinado qual será a preferência de envio.
  - Se “Qtd. de Produtos”: Prioriza por vendas que contém mais produtos;
  - Se “Qtd. de Pedidos”: Prioriza por clientes que possuem mais vendas na plataforma.
