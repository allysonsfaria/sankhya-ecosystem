---
id: "44012080658839"
titulo: "Como cadastrar um serviço?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012080658839-Como-cadastrar-um-servi%C3%A7o"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:19:35Z"
rotulos: ["sync_hc", "magis5", "magis5_204048557325", "sync_hash_7ab291158e8d"]
---

# Como cadastrar um serviço?

## O cadastro de serviços é utilizado no registro e gerenciamento de trabalhos contratados por terceiros, sejam eles indivíduos ou empresas.

Essa funcionalidade é especialmente útil para registrar uma ampla variedade de serviços, como assessorias, consultorias, limpeza de estabelecimentos, manutenção de equipamentos, segurança de bens, taxas de serviços, taxas de entrega, garantias estendidas, assinaturas e até mesmo serviços prestados por pessoas.

Por meio do cadastro de serviços, é possível registrar as informações relevantes para cada tipo de serviço, como descrição, preço, prazo de entrega, especificações técnicas, condições de pagamento e outros detalhes pertinentes.

Com o cadastro de serviços no **Artemis5**, é possível ter um controle detalhado sobre os trabalhos contratados, facilitando a gestão financeira, o acompanhamento de prazos e a emissão de documentos fiscais, como notas fiscais de serviços eletrônicas (NFS-e).

---

Para criar um produto do tipo “Serviço”, siga os passos abaixo:

Na barra de menus, clique em: Serviços → Cadastro - Serviços:

![Imagem 1: Na barra de menus, clique em: Serviços → Cadastro - Serviços:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-132-1024x135.png)

No módulo de produtos, clique em “Novo Produto”.

Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e automática, cujo código é único e não editável.

![Imagem 2: Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-341-1024x208.png)

O módulo de produtos é separado por abas, sendo cada uma delas responsável por uma área específica.

Para cadastrar um produto Serviço siga os seguintes passos:

**INFORMAÇÕES BÁSICAS**

- **Tipo de Produto:** Selecione “Serviço”;

- **Descrição do Produto:** É o nome do produto utilizado para identificação interna. Este campo é obrigatório;

- **Tamanho:** Caso o produto tenha um tamanho, clique em “Select an Option” e selecione-o. Se não localizar a opção desejada, é porque ainda não foi cadastrada no **Artemis5**, então, será necessário cadastrá-la. Para isso, clique em (+) ao lado de “Tamanho”, preencha o campo “**Tamanho”** e clique em “Salvar”;

Observação: Antes de cadastrar um novo tamanho, verifique se já não consta o tamanho cadastrado, por exemplo: 60 Caps é diferente de 60Caps.

![Imagem 3: Observação: Antes de cadastrar um novo tamanho, verifique se já não consta o tamanho cadastrado, por exemplo: 60 Caps é…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-342-1024x282.png)

- **Sabor/Cor:** Caso o produto tenha um sabor ou uma cor, clique em “Select an Option” e selecione-o. Se não localizar a opção desejada, é porque ainda não foi cadastrada no **Artemis5**, então, será necessário cadastrá-la. Para isso, clique em (+) ao lado de “Tamanho”, preencha o campo “**Tamanho”** e clique em “Salvar”;

Observação: Antes de cadastrar um novo tamanho, verifique se já não consta o tamanho cadastrado, por exemplo: 60 Caps é diferente de 60Caps.

![Imagem 4: Observação: Antes de cadastrar um novo tamanho, verifique se já não consta o tamanho cadastrado, por exemplo: 60 Caps é…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-344-1024x247.png)

- **Nome de Exibição (PDV):** É o nome do produto que será exibido no módulo de frente de caixa (PDV) ao cliente;

**EMPREENDIMENTOS**

O empreendimento que o usuário está logado vem selecionado por padrão, caso o lojista possua mais de um empreendimento, é possível compartilhar o cadastro do produto entre eles, evitando ter que refazer o cadastro e agilizando o processo.

Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em “(+) Incluir” e selecione os empreendimentos desejados:

![Imagem 5: Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em “(+) Incluir” e…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-345-1024x274.png)

- **Categoria:** Cada produto poderá ser inserido em apenas uma categoria por empreendimento. Porém, é possível inserir esse produto em categorias diferentes em cada empreendimento;

- **Ativo:** Informa se este produto estará habilitado ou não no empreendimento. O produto pode estar ativo em um empreendimento e desativado em outro.

**PREÇO**

Cada empreendimento pode ter sua tabela de preços, sendo possível que cada empreendimento tenha até quatro tabelas de preços diferentes, sendo elas: “Atacado”, “Intermediário 1”, ”Intermediário 2” e “Varejo”. A definição de quais tabelas o empreendimento irá utilizar é definida na implantação do **Artemis5**, podendo ser alterado nas configurações de cada empreendimento.

A aplicação do preço final ao cliente é definida no cadastro do cliente ou pelo vendedor na hora da venda (caso o vendedor possua a permissão necessária);

- **%:** É a porcentagem de lucro sobre o preço de custo do produto. O preenchimento deste campo calcula automaticamente o valor de venda do produto com base na porcentagem informada e preenche a coluna (R$);

- **R$**: É o valor de venda do produto que será cobrado do cliente final. O preenchimento deste campo calcula automaticamente a porcentagem de lucro que este produto terá com base no preço informado e preenche a coluna (%);

- **% Desc. Máx:** Sobrepõe qualquer outro desconto que o produto possa ter. É a porcentagem de desconto máximo a ser disponibilizado para o produto. O valor inserido neste campo implica na liberação de desconto para o produto no ato da compra. Por exemplo:
  - Situação 1: O produto tem um desconto máximo de 20%, porém, um vendedor deseja aplicar um desconto superior.  A venda é travada e o desconto só é aplicado após alteração no cadastro do produto ou a correção do desconto.
  - Situação 2: O campo “Desc. Máx” não está preenchido, consequentemente o produto não possui um limite de desconto. Porém, o vendedor que está realizando a venda só tem permissão para aplicar uma porcentagem fixa de desconto. Caso  ele queira aplicar um desconto maior, será necessário que alguém com uma permissão superior libere o desconto.

**INFORMAÇÕES COMPLEMENTARES**

- **Natureza:** Informe a classificação do produto dentro do plano de contas (Para saber mais sobre o plano de contas, clique aqui)

- **Garantia (Meses):** Caso seja oferecida uma garantia pelo produto, informe o tempo de cobertura (em meses);

- **Descrição:** É a descrição do produto. Neste campo é possível estilizar a fonte utilizada (seja a cor, tamanho, etc). Limite de 4.000 caracteres;

- **Descrição Curta:** É a descrição curta do produto. Diferente da “Descrição”, neste campo não é possível estilizar a fonte. Limite de 4.000 caracteres;

- **Miniatura do Produto:** É a foto do produto otimizada, utilizada no PDV, App 's, sites, etc. O **Artemis5** é compatível com os formatos .png e .jpg;

- **Vetor do Produto:** É a foto do produto vetorizada. Neste campo, pode-se enviar fotos nos formatos .svg, .png ou .jpg;

**IMAGENS**

Utilizado para inserir mais imagens no cadastro do produto para serem usadas em integrações, vitrines e marketplaces. É possível inserir imagens por plataforma, como no exemplo abaixo:

![Imagem 6: Utilizado para inserir mais imagens no cadastro do produto para serem usadas em integrações, vitrines e marketplaces. É…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-346-1024x558.png)
