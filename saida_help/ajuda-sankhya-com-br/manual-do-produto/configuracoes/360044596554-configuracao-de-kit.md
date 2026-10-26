---
id: "360044596554"
titulo: "Configuração de Kit"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-20T17:55:51Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Componente", "CONFKITIND", "Kit", "PRECOKIT", "br.com.sankhya.mge.configuracao.kit", "Configuração de Kit manual", "Central de Vendas", "Portal de Vendas", "UTILPLANCESTAS", "Estoque", "Configuração de Kit: Uma Nova Abordagem na Gestão de Produtos"]
---

# Configuração de Kit

```
 Módulo: Configurações > Produtos
```

---

Através desta tela, tem-se início a realização de configurações que irão levar a uma nova forma de utilização de Kit; será possível efetuar o cadastro de produtos Kit e seu respectivo produto substituto; pode-se também realizar configurações e vincular tais configurações ao produto que deverá segui-la na inclusão do Kit na grade de matérias-primas na Central - Compras | Vendas | Mov. Internas.

---

**![Imagem 1: Importante: Incompatibilidade com o Módulo de Produção](https://ajuda.sankhya.com.br/hc/article_attachments/26753765824407) Importante:** **Incompatibilidade com o Módulo de Produção**

É crucial entender que o modelo de **venda de kits**, configurado por esta tela, **não é compatível com itens fabricados por meio do módulo de Produção**. Ambos os processos (Produção e Venda de Kits) realizam a baixa de componentes, o que pode levar a:

- **Inconsistências de estoque:** Componentes sendo baixados em duplicidade.
- **Erros de restrição de integridade (ORA−00001:restric\ca~oexclusiva(SANKHYA.TGFITE\_I08)violada):** Impedindo o apontamento da produção ou o faturamento.
- **Problemas operacionais:** Dificultando o controle e a gestão dos seus produtos.

**Recomendamos fortemente que você utilize apenas uma das abordagens (Produção OU Venda de Kit) por produto para garantir a integridade dos seus dados e evitar problemas futuros.** Para mais detalhes sobre o motivo do conflito e orientações sobre qual abordagem escolher, consulte o tópico **"Conflito entre Kits e Produção"** neste artigo.

---

### Configuração do parâmetro CONFKITIND

Esta tela será apresentada para utilização, apenas se o parâmetro **"Configuração para Kit Independente - CONFKITIND"** estiver ligado. Com essa configuração realizada, a forma de utilização de Kit habitual já conhecida no sistema, deixará de funcionar; por este motivo, se faz necessária uma análise detalhada desta nova configuração e seus impactos na empresa. Com o parâmetro ativado, outras parametrizações deixarão de ser consideradas pelo sistema, sendo elas:

- Habilitar o suporte a kit no Sankhya-W - HABSUPORTEKITSW;
- Tem matéria prima na central atendimento ao Cliente - TEMMPVENDA;
- Editar MP ligadas - EDITMP;
- Soma dos custos das MPs no produto principal - EDITMPSOMCUSTO;
- Soma preço das MPs Extras ao produto principal - EDITMPSOMAEXT;
- Soma preço das MPs ao produto principal - EDITMPSOMPRECO;
- Explode Componentes na aba de MP - EDITMPEXPLOD;
- Apresentar apenas MP da aba Componentes - EDITMPVALCOMP;
- Soma ICMS das MPs (Art. 42 do RICMS/2002-MG) - EDITMPSOMAICMS;
- Calcular Impostos para Matéria Prima - CALCIMPMP.

---

### Configuração para um novo Kit

Para iniciar a configuração de um novo Kit, acione o botão de inclusão, e efetue o preenchimento do campo **"Código"**; este preenchimento poderá ser realizado automaticamente, ou de forma manual. Esta definição é feita através do botão ![Imagem 2: Para iniciar a configuração de um novo Kit, acione o botão de inclusão, e efetue o preenchimento do campo "Código" ;…](https://ajuda.sankhya.com.br/hc/article_attachments/360067164474), opção **"Numeração"**, localizado no lado superior direito da tela.

Depois, informe no campo **"Descrição"**, a nomenclatura do Kit que está sendo configurado, para facilitar sua identificação.

![Imagem 3: Depois, informe no campo "Descrição" , a nomenclatura do Kit que está sendo configurado, para facilitar sua…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007685601)

Feito isso, na aba Geral são apresentadas algumas marcações que irão definir o comportamento do Kit no sistema. São elas:

**Calcula imposto do componente:** Realiza o cálculo de impostos nos componentes do kit aos quais esta configuração está ligada.

**Soma custo do componente ao kit:** Refere-se à soma do campo **"Custo"** dos itens (componentes) da **"Central - Vendas | Mov. Internas"**. Tem-se que este valor não será calculado para notas de entrada, pois o Custo corresponde ao valor unitário do componente.

**Nota:** o campo Custo será calculado apenas para os Tipos de Movimento:

- **J:** Pedido de requisição;
- **Q:** Requisição;
- **L:** Devolução de requisição;
- **P:** Pedido de Venda;
- **V:** Venda;
- **D:** Devolução de Venda;
- **T:** Transferência.

**Soma preço do componente ao kit:** com essa marcação efetuada, o valor total do kit passará a ser a soma do valor total dos componentes, e o valor unitário kit será o valor total dividido pela quantidade.

**Distribuir preço do kit nos componentes:** essa marcação distribui (rateia) o preço do kit aos seus componentes.

**Observação**: esta marcação não pode ser usada junto com a configuração de 'Soma preço do componente ao Kit'. Sempre somente uma das duas opções deve estar marcada.

**Distribuir desconto do kit nos componentes:** através dessa marcação, será efetuada a distribuição (rateio) do desconto do kit nos componentes.

**Utiliza preço sugerido na aba 'Componentes':** com essa marcação habilitada, será usado o "Preço" sugerido na aba Componentes do Cadastro de Produtos como preço unitário do componente. Lembrando que, este Preço será utilizado somente quando o parâmetro "Informar Preço p/Componente no cad.Produto?- PRECOKIT" estiver habilitado. Quando a opção "Distribuir preço do kit nos componentes" estiver marcada esse preço será a base para o rateio do valor do kit para os componentes.

**Explodir componentes na grade de matéria prima da central:** Por meio dessa marcação, será feita a explosão dos componentes que foram inseridos na aba Componentes do Cadastro de Produtos.

**Observação:** o parâmetro **"Soma IPI das MPs ao valor total da nota. - EDITMPSOMAIPI"** quando habilitado, calcula o valor total do IPI dos componentes do Kit, e os soma diretamente ao valor total da nota.

**Nota:** somente irá acontecer a explosão na inserção de um kit.

**Observação:** quando o parâmetro **"Soma preço das MPs Extras ao produto principal? - EDITMPSOMAEXT"** estiver habilitado, ao faturar o pedido de venda, os componentes do Kit serão incluídos juntos aos produtos na aba [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#configuraescadastrosprodutosprodutos). Além disso, é importante destacar que, com este parâmetro ativado, o sistema não calculará o desconto automático dos componentes ao explodi-los.

**Faturar apenas KIT com estoque de todos os componentes:** Quando essa marcação for utilizada, ao tentar faturar pedidos em que houverem componentes do kit faltantes ou com estoque abaixo do requerido, o faturamento será realizado apenas com a quantidade de itens existentes no estoque. Dessa forma, você poderá utilizar duas opções do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) para realizar essa validação, sendo elas, [Faturar pelo Estoque deixando pendente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#faturarpeloestoquedeixandopendente) e [Faturar pelo Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#faturarpeloestoque). Assim, considere que iremos montar um Kit Escolar contendo uma mochila, um estojo e uma lancheira, em que:

Montaremos um pedido com 10 kits, porém, o estoque contém o suficiente para montar apenas 9 kit's completos. Ao utilizar a opção Faturar pelo Estoque deixando pendente, o sistema irá faturar a quantidade existente no estoque e deixará o restante pendente de faturamento, assim, quando houver uma nova entrada de estoque para finalizar esse pedido, ele será faturado e finalizado.

Agora, considere que temos um pedido de 12 kit's escolares:

Dado que no estoque há quantidade suficiente para a montagem de apenas 9 kit's, ao utilizar a opção Faturar pelo estoque, o sistema irá faturar apenas a quantidade utilizada para a montagem dos kit's completos, finalizando assim o pedido sem quantidades pendentes.

---

### Conflito entre Kits e Produção

Este tópico visa esclarecer o motivo pelo qual a configuração de Kits e o uso do módulo de Produção podem gerar inconsistências quando aplicados ao mesmo produto.
**Entendendo o conflito:**
No SankhyaOM, o **módulo de Produção** é projetado para gerenciar a fabricação de um produto. Quando você produz um item:

**1.** As **matérias-primas (MPs)** são baixadas do estoque.
**2.** O **produto acabado (PA)** é gerado e tem sua entrada registrada no estoque.
Por outro lado, a funcionalidade de **Venda de Kits** opera de forma diferente. Quando um "kit" é vendido (mesmo que ele seja composto pelos mesmos itens de um PA) o sistema tenta realizar a **baixa dos componentes individuais (MPs)** que formam o kit diretamente do estoque no momento da venda.
**A inconsistência surge quando um produto é configurado para ser fabricado (via Produção) E, simultaneamente, tem seus componentes gerenciados para venda como Kit.**

Por exemplo, se uma "Cesta Básica" é produzida, o "Arroz" e o "Feijão" (componentes) já foram baixados. Se essa mesma "Cesta Básica" for vendida como um Kit, o sistema tentará baixar o "Arroz" e o "Feijão" novamente, levando a:
• **Baixa duplicada**: gerando estoque negativo ou incorreto dos componentes.
• **Erro ORA−00001**: violação de restrição de unicidade ao tentar registrar a baixa de um componente que já foi baixado ou processado de uma forma diferente pela produção.

**Exemplo Prático (Cesta Básica):**
Considere uma "Cesta Básica" que contém "Arroz" e "Feijão":
• Se você **fabrica** a Cesta Básica: as quantidades de Arroz e Feijão são baixadas quando a Cesta Básica é produzida. Na venda, você baixa do estoque a Cesta Básica (o produto acabado).
• Se você **vende** a Cesta Básica como KIT: você agrupa Arroz e Feijão. Na venda, o sistema baixa as quantidades de Arroz e Feijão diretamente.
Não é possível fazer ambos com o mesmo item de forma integrada no sistema, pois as lógicas de baixa de estoque se conflitam.

**![Imagem 4: Quando utilizar Produção vs. Venda de Kits Para evitar problemas e garantir a integridade do seu estoque, escolha a…](https://ajuda.sankhya.com.br/hc/article_attachments/26753765824407) Quando utilizar Produção vs. Venda de Kits**
Para evitar problemas e garantir a integridade do seu estoque, escolha a abordagem correta para cada produto:
**• Utilize o Módulo de Produção quando:**
◦ Seu produto final é o resultado de um processo de fabricação que consome matérias-primas e requer controle de etapas, recursos e custos.
◦ Você precisa ter o produto acabado (PA) em estoque antes da venda.
◦ Exemplo: Fabricação de alimentos processados, móveis, componentes eletrônicos.
**• Utilize a Configuração de Venda de Kits quando:**
◦ Seu "kit" é uma combinação de produtos já existentes em estoque que são agrupados apenas para fins de venda, sem um processo de fabricação formal do "kit" em si.
◦ A baixa dos componentes individuais ocorre apenas no momento da venda do kit.
◦ Você não precisa de um "estoque" do kit pronto, apenas de seus componentes.
◦ Exemplo: Um "kit de higiene" que agrupa sabonete, shampoo e condicionador que já estão individualmente em estoque.
Ao configurar seus produtos, certifique-se de que a escolha entre Produção e Venda de Kit esteja alinhada ao seu fluxo de trabalho e à forma como o estoque dos componentes deve ser gerenciado.

---

### Como as configurações de Kits afetam o comportamento das telas

Ao utilizar as novas formas de trabalho com Kit's, algumas telas podem ter o seu comportamento afetado. Vejamos quais são elas:

[Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#central-comprasvendasmov.internas)                 [Cadastros de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#configuraescadastrosprodutosprodutos)   

[Cadastros de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#configuraescadastrosparceiros)                                           [Cadastros de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#configuraescadastrosprodutosservio) 

[Observações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#observaes)

---

### Central - Compras | Vendas | Mov. Internas

Na inserção de um Kit, de acordo com o arranjo estabelecido na tela Configuração de Kit, os valores de preço, custo, desconto, ICMS e impostos dos Kit's e componentes sofrerão alterações.

Na Central de Compras | Vendas | Mov. Internas, você também pode realizar a substituição de componentes, por exemplo:

Na venda de uma cesta (Kit padrão) que contenha um pacote do produto "A - Marca X" e outro do produto "B - Marca X"; percebe-se que não há mais do produto "A - Marca X", pode-se realizar a substituição dos componentes de uma cesta Kit de composição padrão, para uma cesta Kit de composição personalizada, onde pode-se incluir outros produtos, como neste caso, um produto "A - Marca Z".

Esta substituição é feita através da opção **"Substituir Componentes do Kit"** localizada no botão **"Outras Opções..."** presente na grade de itens, que será apresentada se o parâmetro **"Substituição de kit Independente- HABSUBSKITIND"** estiver ativado.

![Imagem 5: Esta substituição é feita através da opção "Substituir Componentes do Kit" localizada no botão "Outras Opções..."…](https://ajuda.sankhya.com.br/hc/article_attachments/360068244293)

**Nota:** neste procedimento de substituição, não é permitido substituir para uma quantidade menor ou igual a zero, ou maior que a quantidade do kit de origem.

**Observação:** se o parâmetro **"Valida alteração quantidade componente ao faturar? - VALALTCOMPONFAT"** estiver ligado, o sistema só permitirá o faturamento do Kit se, os itens que o compõe, apresentarem estoque suficiente. Caso contrário, será emitida uma mensagem informando que não há estoque suficiente para esse componente.

Na grade de itens das Centrais, o painel **"Matéria-Prima"** será apresentado quando o produto que compor os itens tratar-se de um kit. Dessa forma, quando o produto selecionado na grade tiver componentes, você poderá observar o painel Matéria-Prima. Por outro lado, caso o produto indicado não seja um kit, esse painel não será visualizado.

**Observação:** este painel apenas será observado após o produto kit ser salvo na grade Itens das Centrais de Notas.

Destaca-se ainda que, para que esse painel seja apresentado nas Centrais de Notas, grade **"Itens"**, deve-se habilitar os parâmetros:

- "Tem aba Mat.Prima na Transferência? - TEMMPTRAN";
- "Tem aba Mat.Prima na requisição? - TEMMPREQ";
- "Tem aba mat.prima na central atend. ao Cliente? - TEMMPVENDA";
- "Tem aba mat.prima na central atendimento ao Forn.? - TEMMPCOMPRA";
- "Mostrar grid de mat. prima somente quando existir - SHOWGRIDMATPRI".

**Observação:** ao realizar operações de vendas, caso queira que os produtos componentes (matérias-primas de um produto KIT) não sejam exibidos no lançamento de um pedido/nota, habilite o parâmetro **"Inibir exibição de MP nos movimentos de vendas? - INIBESELECUSOPD"**; desse modo, não serão exibidas as MPs explodidas se o campo **"Usado como"**, estiver configurado com a opção **"Revenda (por fórmula)**" [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-). Assim, considere o exemplo abaixo:

- Produto A = Produto KIT
- Produtos B e C = Matérias-primas do produto A.

Quando o pedido/nota for lançado com o Produto A, os Produtos B e C não serão exibidos se o parâmetro estiver habilitado. Logo, se o pedido de venda for faturado as matérias-primas (produtos componentes) deste pedido não serão levadas para a nota de venda.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#top)

### Cadastro de Parceiros

Participando dessa nova forma de utilização de Kit's, a tela de [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) (aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontatos), sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#sub-abageral)) conta com dois campos que serão apresentados para utilização, apenas se o parâmetro **"Utiliza planejamento produção de cestas. - UTILPLANCESTAS"** estiver ativado. São eles:

**Participa plan. entrega cesta:** Quando você realizar essa marcação, fará com que o Contato do Parceiro em questão, possa ser inserido na rotina de [Planejamento de Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612594) (grade Contatos).

**Quantidade Cestas:** Informe nesse campo, a quantidade de cestas que serão atribuídas a cada um.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#top)

### Cadastro de Produtos

A tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Componentes, conta com quatro campos que irão influenciar no comportamento do Kit. São eles:

**Tipo de Kit:** Selecione nesse campo a composição do Kit, de acordo com as seguintes opções:

- Composição Padrão;
- Composição Personalizada.

**Configuração p/ Kit:** Determine nesse campo, a configuração que será respeitada quando um produto for lançado na Central - Compras | Vendas | Mov. Internas. A informação aqui apresentada para escolha, é previamente cadastrada na tela [Configuração de Kit](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit).

**Código do Produto Substituto do Kit:** Informe nesse campo, o produto que será utilizado para substituir um kit padrão no lançamento na Central - Compras | Vendas | Mov. Internas.

**Preço:** Esse campo será apresentado para preenchimento, apenas se o parâmetro **"Informar Preço p/Componente no cad.Produto?- PRECOKIT"** estiver ativado. Nele informe o preço referente ao componente do Kit.

**Observação:** ao ligar o parâmetro **"Valida Local da MP no KIT? - VALLOCKITMP"**, o sistema não permitirá o lançamento de Kit's com produtos que estejam com Local **"0"** quando a marcação **"Usa local"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba **"Medidas e estoque"**, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque) for habilitada.

**Nota:** para trabalhar com local padrão definido nos componentes do kit, é necessário habilitar o parâmetro **"Mostrar o controle na aba de componentes - CONTROLECOMPON"**. Assim, quando ligado, será apresentado no Cadastro de Produtos, aba [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacomponentes), o campo **"Controle"** (que engloba o local).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#top)

### Cadastro de Serviço

Quando o parâmetro Configuração para Kit Independente - CONFKITIND estiver ligado, na tela de [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), a aba Componentes deixa de ser apresentada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#top)

### Observações

Na explosão do Kit (parâmetro Configuração para Kit Independente - CONFKITIND habilitado), para que o local nos componentes seja obtido, tem-se o seguinte comportamento:

- Se a opção do Cadastro de Produto, **"Usa local"** (aba **"Medidas e Estoque"**, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque)) não estiver marcada, o local definido será zero (0);
- Caso a opção anterior não seja atendida, e tenha sido definido um local para o componente no cadastro do produto Kit, este local será utilizado;
- Caso as opções anteriores não sejam atendidas e o parâmetro **"Local Padrão para Pedidos e Notas - LOCALPADRAO"** esteja definido, o seu valor será utilizado;
- Caso nenhuma das opções anteriores sejam atendidas, o valor utilizado será zero (0).

**Nota:** É fundamental lembrar que a explosão de kits se aplica principalmente ao fluxo de vendas para baixa de componentes. Para produtos que passam por processo de fabricação e geram um produto acabado, o módulo de Produção deve ser utilizado para o controle da baixa de matérias-primas e entrada do item final.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596554-Configura%C3%A7%C3%A3o-de-Kit#top)
