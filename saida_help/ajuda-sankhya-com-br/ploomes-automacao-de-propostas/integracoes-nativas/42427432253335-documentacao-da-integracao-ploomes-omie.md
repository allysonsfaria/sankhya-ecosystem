---
id: "42427432253335"
titulo: "Documentação da Integração Ploomes - Omie"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427432253335-Documenta%C3%A7%C3%A3o-da-Integra%C3%A7%C3%A3o-Ploomes-Omie"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:57Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452457", "sync_hash_1fa6d0c0f953"]
---

# Documentação da Integração Ploomes - Omie

## Introdução

Omie é um ERP (Enterprise Resource Planning), que integramos com o nosso CRM da Ploomes por meio de uma integração Plug-and-Play. Por meio dessa integração é possivel unir os dois sistemas através das entidades: Cliente, Produto, Venda, Produto da Venda, Serviço e Ordem de Serviço, e também os usuários no ploomes que são os vendedores no Omie. Esta aplicação permite a integração rápida, fácil e sem custos adicionais de desenvolvimento para os clientes da parceria.

Este documento apresenta o escopo e as explicações da integração. O documento começa com o resumo do escopo geral da integração. Em seguida, é explicado como funciona o mapeamento de campos entre as duas ferramentas e as instruções de ativação. Por fim, são demonstrados os detalhes técnicos de implementação para os desenvolvedores que precisarem de algum tipo de guia.

## Escopo geral

A integração do Ploomes com o Omie liga as informações de clientes, produtos e vendas do Ploomes com as entidades de Clientes/Fornecedores, Produtos, Serviços, Venda e Ordem de Serviços no Omie.

Conforme a imagem abaixo, a comunicação da integração se comporta unilateral ou bilateralmente, a depender das entidades envolvidas. A entidade de Clientes no Ploomes, se comunica bilateralmente com a entidade de Clientes/Fornecedores do Omie. Isso quer dizer que a criação, edição e exclusão de um cliente em um dos sistemas afetará o outro também. Entenda mais sobre quais são os campos que fazem parte da integração e às exceções de integração na seção sobre clientes.

A base de Produtos do Ploomes será preenchida pelo Omie, já que esta integração é feita unilateralmente. Qualquer criação, edição e exclusão no Omie será refletida no Ploomes. Por outro lado, nenhuma modificação no Ploomes é enviada ao Omie. O Omie possui duas entradas separadas: uma para produtos e outra para serviços. Essas duas tabelas serão enviadas ao Ploomes como produtos. Dito isso, recomenda-se que o cliente que optar por ativar a integração use somente o Omie para gerenciar os seus produtos.

A entidade de Proposta do Ploomes não é integrada ao Omie. Os cálculos de preços serão configurados no Ploomes, já que não foi possível integrar as tabelas de preços do Omie. A contribuição do Omie na criação de propostas será com o campo de consulta de estoque. Ao ativar a integração, o campo de tabela de estoque estará disponível para o usuário. Este campo dinâmico em produtos no Ploomes que contém uma tabela de informações sobre estoque de produto obtidas do Omie, obedece às regras de negócio do Omie como permissão de acesso da tabela para vendas e inativação da tabela.

Por fim, Vendas no Ploomes estão integradas ao módulo de Venda de Produto do Omie. Portanto, é imprescindível que o módulo esteja habilitado na conta Ploomes daqueles que querem usufruir da integração. A integração se comporta bilateralmente, então criação, edição e exclusão são transferidas entre os dois lados. Vale destacar que, por mais que os serviços do Omie sejam enviados ao Ploomes, a entidade de Vendas não está integrada à entidade de Ordens de Serviços do Omie. Qualquer venda, contendo produtos ou serviços, será enviada ao módulo de Venda de Produto do Omie.

![Imagem 1: Por fim, Vendas no Ploomes estão integradas ao módulo de Venda de Produto do Omie. Portanto, é imprescindível que o…](https://downloads.intercomcdn.com/i/o/754452697/e065db0944e06e3a55b7197c/image.png?expires=1786536000&signature=ca4c509440d33bcbba47df13703907aea69174a0e45db5cf36725ffc21521e4d&req=cyUjEsx8m4hYFb4V1XW4gXUNLPV6JQ5hZnyT%2FMnIPrgBQYbVaUZHX7OS6IV2%0AZReVUlAn2aeD3LR%2FOxKyYeuHUg%3D%3D%0A)

De forma implícita, foi necessário sincronizar também usuários Ploomes com vendedores Omie, mas de forma passiva, não são criados novos usuários em nenhum dos dois lados já que o número de usuários define o preço de licença do software Ploomes, e também do Omie. É feita uma busca com base no e-mail, que é esperado existir em ambos os lados, como usuário Ploomes e vendedor Omie, após essa busca é preenchido o campo de Usuário ‘Id Vendedor (Omie)’ no Ploomes, com isso o vínculo está feito.

A próxima seção explica o comportamento fixo entre os dois sistemas. Alguns campos de clientes, produtos e vendas se comportam da mesma forma durante a integração para todos os usuários. A seção de mapeamento de campos explica melhor como o usuário pode customizar a integração usando campos personalizados do Ploomes para enviar impostos, dados dos clientes e especificidades das vendas entre os dois sistemas.

## Escopo: Detalhamento das entidades

Cada entidade integrada apresenta suas próprias particularidades e comportamentos. A seguir, cada entidade é detalhada com a informação de quais campos têm protagonismo na comunicação entre os dois sistemas e quais ações dos usuários podem prejudicar a sincronização das informações.

## Contatos

As entidades de Clientes/Fornecedor (Omie) e Contatos (Ploomes) estão sincronizadas simultaneamente com seus campos mais importantes.

Mapeamento fixo de campos:

- Nome;
- Razão Social;
- Email;
- CNPJ;
- CPF;
- Telefone;
- Telefone 2;
- Fax;
- Website;
- Endereço;
- Complemento;
- Numero;
- Bairro;
- CEP;
- Cidade;
- Estado;
- País;
- Tags (Omie) ⇔ Marcadores (Ploomes);
- Código CNAE;
- Vendedor Padrão (Omie) ⇔ Responsável (Ploomes);
- Inativo (Omie) => Status (Ploomes);

**Observações:**

- É possível colocar mais de um endereço no Omie, mas não no Ploomes (precisa criar novos campos). Então, por enquanto, o Ploomes conseguiria integrar apenas um endereço. O endereço integrado será o primeiro inserido no Omie.
- O Omie possui um limite de três telefones por cadastro, diferente do Ploomes que permite a inclusão de vários números em um só contato. Por isso, os números de telefones cadastrados no Ploomes são enviados para os seguintes campos do Omie: Telefone 1, Telefone 2 e Fax. Para o campo Fax ser preenchido no Omie, o Telefone tem que ser do tipo Fax no Ploomes. Se mais de três números de telefones forem cadastrados, apenas os três primeiros números serão enviados ao Omie.
- O Omie possui uma funcionalidade de ativar/inativar clientes cadastrados. Clientes inativados continuam na base mas não podem ser selecionados para vendas. As informações de ativo/inativo serão enviadas ao Ploomes como opções do campo de Status do cliente. No entanto, a edição do campo no Ploomes não afetará a ativação/inativação no Omie via API. Portanto, ao ativar a integração, é **recomendável bloquear o campo** status **da entidade Cliente no Ploomes** (por segurança, ele já força manter o valor).
- O campo responsável representa um usuário no Ploomes, e para integrar com o Omie, é preciso que haja um vendedor **com o mesmo e-mail** cadastrado no Omie.
- O Omie exige preenchimento dos campos Razão Social e também do Nome Fantasia e no Ploomes só é exigido o campo Nome. Caso a razão social não seja preenchida no Ploomes, é tomado o que foi digitado no campo Nome para maior flexibilidade ao usuário.

- O Ploomes não permite que um contato seja trocado de tipo pessoa física para jurídica (pessoa ou empresa) ou vice e versa, já o Omie sim. Por isso, trocar o tipo de pessoa no Omie não irá refletir no Ploomes.
- A validação de duplicidade é feita através do CPF/CNPJ ou pelo ID do Omie, caso o mesmo já esteja preenchido.
- Ao criar um cliente no Ploomes, se o campo "responsável" estiver preenchido e o mesmo estiver inativo no Omie, o cliente não será criado no Omie. No entanto, o inverso ocorre: se o usuário estiver inativo no Ploomes e a criação for realizada no Omie com esse usuário, ele será criado no Ploomes sem erros.
- Ao cadastrar um cliente no Ploomes e atribuir um responsável (vendedor) que não está cadastrado no Omie, é importante destacar que a integração entre os dois sistemas não realiza a criação de usuários no Omie, portanto o campo ficara vazio. Isso ocorre também para na criação entre Omie x Ploomes.
- **No Omie é possivel configurar se o cadastro exigira algum preenchimento, como o de CPF/CNPJ por exemplo**, caso o usuário tente criar sem esse preenchimento no Ploomes, o Omie ira criar um registro de interação informando o erro na inserção do cliente e não ocorrera a integração até que a informação seja preenchida.

![Imagem 2: No Omie é possivel configurar se o cadastro exigira algum preenchimento, como o de CPF/CNPJ por exemplo , caso o…](https://downloads.intercomcdn.com/i/o/754495146/835854e3c7e328c1a022b5ca/image.png?expires=1786536000&signature=be89f596d811282b8c64747e60b7f70f220d2a180368acd4f751986338a90fa2&req=cyUjEsB7nIVZFb4V1XW4ga%2FrDMGQJH4GzsFDQ5nTNUUhMmLY0sgcNvoMjF%2Fi%0AJkNfRwQ1boQS%2Fie%2BfnD1IgUP3w%3D%3D%0A)

![Imagem 3: No Omie é possivel configurar se o cadastro exigira algum preenchimento, como o de CPF/CNPJ por exemplo , caso o…](https://downloads.intercomcdn.com/i/o/754495393/8cdb9afd74f9c63cfd72bb64/image.png?expires=1786536000&signature=9a934bf2fa08129cec474357f02551b4c7d63d89d496466ae266ab53288da593&req=cyUjEsB7nohcFb4V1XW4gU%2Ft%2B3P4HGw79td%2BRnF3DaVBTBHKMmdnqxJswLgg%0Ae%2BjnfezXDbEridZijKhNe9RA9w%3D%3D%0A)

## Produtos

Diferente de outras entidades, **produtos e serviços seguem apenas o fluxo Omie → Ploomes**.

- Não é possível criar produtos no Ploomes e enviá-los para o Omie;
- Qualquer criação ou edição estrutural de produtos deve ser feita diretamente no Omie;
- O Ploomes apenas consome as informações enviadas pelo ERP.

### Famílias e grupos de produtos no Ploomes

Ao ativar a integração com o Omie, o Ploomes cria automaticamente duas famílias padrão:

- **Produtos**
- **Serviços**

Essas famílias são utilizadas para diferenciar, no Omie, **pedidos de venda** e **pedidos de serviço** gerados a partir do Ploomes.

Regras de alocação:

1. Produtos do Omie **sem família informada** são alocados no grupo **“Produtos”**, dentro da família **“Produtos”** no Ploomes;
2. Como o Omie não possui campo de família para serviços, todos os serviços são cadastrados no grupo **“Serviços”**, dentro da família **“Serviços”** no Ploomes.

![Imagem 4: Como o Omie não possui campo de família para serviços, todos os serviços são cadastrados no grupo “Serviços” , dentro…](https://downloads.intercomcdn.com/i/o/754500723/5cbed40c42a51b926c07d42f/image.png?expires=1786536000&signature=91adf7b4ff5bbec51da447adfd173d81579e0e9d759819e4bcb454eca530aaa1&req=cyUjE8l%2BmoNcFb4V1XW4gdyGg6dzrrZPGdzHfd3%2FqMAsF1G%2FdSVmpP3YYaYH%0A6VZhMRRTBiH3JycdfRg4mis7Dg%3D%3D%0A)

⚠️ **Atenção**: os produtos **devem obrigatoriamente pertencer às famílias “Produtos” ou “Serviços”** no Ploomes. A remoção ou alteração dessas famílias pode causar falhas na integração de vendas.

### Campos obrigatórios para criação de produtos no omie

Para um produto ser criado corretamente no Omie (e consequentemente integrado ao Ploomes), é obrigatório preencher:

- **Descrição**;
- **Unidade**;
- **Código NCM**;
- **Código do Produto** (gerado automaticamente pelo Omie).

### Mapeamento fixo de campos na integração

Os campos abaixo possuem **mapeamento fixo** na integração entre Omie e Ploomes.

**Produtos:**

| **Omie** | **Ploomes** |
| --- | --- |
| Descrição | Nome |
| Código | Código |
| Unidade de Medida | Unidade de medida |
| Preço unitário | Valor unitário |
| Família | Grupo |
| Inativo | Marcadores |

**Serviços:**

| **Omie** | **Ploomes** |
| --- | --- |
| Descrição | Nome |
| Código | Código |
| Preço unitário | Valor unitário |
| Inativo | Marcadores |

O campo **Marcadores** dos produtos no Ploomes segue o mesmo comportamento do campo de **status**, conforme descrito nas observações da [integração de clientes](https://sankhya.zendesk.com/hc/pt-br/articles/42427413400855).

### Consulta de estoque no Ploomes

O estoque dos produtos integrados é exibido no Ploomes por meio de um **campo dinâmico de texto multilinha**, que armazena uma **tabela em HTML**.

#### Regras de exibição:

- A tabela respeita as permissões definidas no Omie;
- Apenas locais de estoque **habilitados para venda** são exibidos;
- Essa configuração é controlada no painel de **Locais de Estoque** do Omie.

![Imagem 5: Essa configuração é controlada no painel de Locais de Estoque do Omie.](https://downloads.intercomcdn.com/i/o/754512291/66aa9d655ebb4f53b7635ec9/image.png?expires=1786536000&signature=5a1d4377f812986ebee725ce3d371c813e3645118d2b871c1a696651749b465e&req=cyUjE8h8n4heFb4V1XW4gYdwjVaLfYQ88tONOzoOxxng8O50cdH6pVb6PpZS%0AxOvVVgR%2B550rdRDSCgDaKlsCTA%3D%3D%0A)

#### Exemplo da tabela no Ploomes:

![Imagem 6: Exemplo da tabela no Ploomes:](https://downloads.intercomcdn.com/i/o/754512864/faac76d2cf4d30864bd4cbb4/image.png?expires=1786536000&signature=f616a14d4789758881ea291f3710b073318fd111b45c483ed96be6914a21ffeb&req=cyUjE8h8lYdbFb4V1XW4gVTOJXlWQ1v7SqJCfq0M3jDF%2BqfSflw0HHWmTUc1%0Ah2V5Fv55XKxfh3ndADm9utjWWg%3D%3D%0A)

#### Informações exibidas na tabela:

- Status do Estoque;
- Local de Estoque;
- Estoque Disponível;
- Estoque Mínimo;
- Previsão de Saída;
- Tipo de Local de Estoque;

#### Atualização dos dados

A tabela é atualizada quando:

- Ocorre uma movimentação no estoque do produto;
  ou
- Um administrador clica manualmente em **Atualizar**, o que força a atualização de todos os produtos.

Ao final da tabela, é exibida a **data e hora da última atualização**, garantindo mais transparência.

## Vendas

A integração de vendas entre o Ploomes e o Omie funciona de forma bilateral. Isso significa que uma venda criada no Ploomes será enviada para o Omie, e vice-versa. Dessa forma, quando uma venda é criada no Omie, ela também é automaticamente criada no Ploomes.

Para uma venda ser integrada ao Omie, algumas informações importantes, tem que estar preenchidas, a falta dessas informações pode gerar problemas na integração:

- O cliente e o produto precisam existir no Omie, e, estejam corretamente integrados e ativos.
- Na venda tem que estar preenchido os campos [Produto da venda.Quantidade] e [Produto da venda. Valor unitário].
- Produto tem que pertencer ou a família produtos, ou a família serviços no Ploomes.
- O cliente tem que ter CPF ou CNPJ preenchidos. (Caso obrigatoriedade esteja ativa).
- O cliente obrigatoriamente tem que possuir o campo Cidade/Estado preenchido no Ploomes.
- Caso queira responsável na venda/serviço, o mesmo deverá ser integrado com E-mail idêntico ao do vendedor do Omie.
- Os campos [Produto da Venda.Desconto] e/ou [Produto.Desconto] não podem ser preenchidos com valores menores que 0.
- Id Omie não pode estar preenchido com “” (string vazia), precisa estar ou preenchida com o Id Omie ou com 0 (Apenas caso já exista dentro da entidade) e isso serve para as outras entidades também.

**Mapeamento fixo de campos:**

- Cliente;
- Vendedor;
- Itens do pedido
- Produto do item;
- Quantidade;
- Preço definido;

#### Campos Criados pela Integração

Ao habilitar a integração com o Omie, novos campos dinâmicos são adicionados ao Ploomes para armazenar informações sincronizadas. Esses campos não substituem os campos nativos do Ploomes, mas são utilizados para registrar os dados vindos do Omie.

#### Campos de Venda:

- **Número da Venda de Produto (Omie)** → Campo criado pela integração, recebe o número da venda conforme registrado no Omie.

**Número da Ordem de Serviço (Omie)** → Campo criado pela integração, armazena o número da ordem de serviço conforme registrado no Omie.

**Observações:**

As vendas do Ploomes e os pedidos do Omie sincronizam automaticamente ao ligar a integração de acordo com a configuração do usuário. Se as opções estiverem habilitadas, quer dizer que vendas e pedidos criados antes da ativação vão ser sincronizados entre os dois sistemas assim que a integração for ativada. Se as opções estiverem desativadas, somente pedidos e vendas criados APÓS a ativação serão sincronizados.

![Imagem 7: As vendas do Ploomes e os pedidos do Omie sincronizam automaticamente ao ligar a integração de acordo com a…](https://downloads.intercomcdn.com/i/o/754519430/b7d45b03a1ffedad3d26f6cd/image.png?expires=1786536000&signature=3ee84da0a688613b1e82352663774f746da09b955bfc4cd37226fe2112e9aa2d&req=cyUjE8h3mYJfFb4V1XW4gRpWZLAfeNj0M02WK3Te1174NIFeHhCt1zYzvAqv%0AIeUU4djVjAL6%2B9T9vdue8XySdw%3D%3D%0A)

Os serviços do Omie também são incluídos no cadastro de produtos do Ploomes da forma explicada acima.

Caso o campo 'Método de Pagamento (Omie)' não esteja mapeado ou não preenchido, será enviado para o Omie com a opção 'À Vista'. É importante lembrar que esse campo deve ser mapeado com o campo 'Método de Pagamento' em 'VendaProduto', pois assim será possível preencher o campo 'Número de Parcelas' no Omie. Como esse campo é criado pela própria integração, não é recomendado adicionar opções a ele no Ploomes, pois isso pode ocasionar problemas na integração da venda.

Todas as vendas são inseridas no Omie usando a informação de conta-corrente configurada no modal da integração.

![Imagem 8: Todas as vendas são inseridas no Omie usando a informação de conta-corrente configurada no modal da integração.](https://downloads.intercomcdn.com/i/o/754520742/4c1502397edaccc8264e95b8/image.png?expires=1786536000&signature=a01f81c77f28f03158808d99889e3178b239121218f683439bc139278e696218&req=cyUjE8t%2BmoVdFb4V1XW4gbnk8ncqw6O5OyLGa4HZ0JtLzcfCNTl5SwqyhmDT%0ARDm7ROx%2FgnpDWD0Dux5TYURSZA%3D%3D%0A)

Ao marcar a opção 'As vendas nunca serão sincronizadas' no modal de integração, as vendas do Ploomes deixarão de ser sincronizadas. No entanto, o Omie ainda poderá criar/editar vendas no Ploomes. Para impedir essa sincronização também por parte do Omie, basta desativar os webhooks.

![Imagem 9: Ao marcar a opção 'As vendas nunca serão sincronizadas' no modal de integração, as vendas do Ploomes deixarão de ser…](https://downloads.intercomcdn.com/i/o/754521499/b2ec0f28386261c4969b8296/image.png?expires=1786536000&signature=d7c0d2255a07af91e418828dcb7d5a8e2a4f8f0ba33fa83acdf2ff28f3c26368&req=cyUjE8t%2FmYhWFb4V1XW4gXgfXASJjGww%2FX3W3R8Z12yFz04N5Te%2B%2FP%2FEPpsg%0As76LVLSJP0N7lm3txPPSWAO2pA%3D%3D%0A)

Os itens não seguem a mesma sequência de número do pedido unilateralmente. Caso seja desejável sincronizar os números do pedido em ambos os lados, Ploomes e Omie, é possível configurar o próximo número a ser usado no Ploomes. No módulo de Administração, entre na opção Módulos do sistema e selecione Vendas.

![Imagem 10: Os itens não seguem a mesma sequência de número do pedido unilateralmente. Caso seja desejável sincronizar os números…](https://downloads.intercomcdn.com/i/o/754521931/c4f043f3cd0831065fe5d5c1/image.png?expires=1786536000&signature=471674d46debcd3a3e514903bed7be91fcee741066887fcfc510417819c5124d&req=cyUjE8t%2FlIJeFb4V1XW4gXlIcTijRxShId9nzw25wny%2BnX7ug7US4m4P2RLY%0AgzeDmtJS1uTpogH%2FvdXXVvgDhg%3D%3D%0A)

![Imagem 11: Os itens não seguem a mesma sequência de número do pedido unilateralmente. Caso seja desejável sincronizar os números…](https://downloads.intercomcdn.com/i/o/754522166/58b27aafea2aca577d73a12c/image.png?expires=1786536000&signature=69491475585655d86c9dfcf72298c79e11411eb6564330fa1bed5fdea7627598&req=cyUjE8t8nIdZFb4V1XW4gZ1lUvbKp985Gqj3eGb9ievW4EtprFt5L%2FtOcDm6%0AxBuQLZvhzB2%2FYyRnn63iyo5ZQA%3D%3D%0A)

O pedido ao ser enviado para o Omie, é inserido com as configurações tributáveis alteradas automaticamente pelo Omie.

No Omie é possível alterar o Cliente da venda, no Ploomes não. Alterações no Cliente da venda no Omie não são aplicadas no Ploomes.

Quando excluímos uma venda no Ploomes, essa exclusão é automaticamente sincronizada e a venda é cancelada no Omie. Da mesma forma, quando excluímos uma venda no Omie, ela também é automaticamente excluída no Ploomes.

Quando uma venda é registrada no Ploomes contendo apenas produtos e posteriormente é editada para incluir algum serviço, resulta na criação de uma Ordem de Serviço no Omie.

## Mapeamento de campos

Durante a ativação da integração, o cliente vai conseguir mapear campos do Ploomes com campos do Omie. Com isso, os usuários poderão usufruir da integração através das regras fixas entre campos (como mencionado na seção de Escopo), e de regras customizadas de acordo com as necessidades deles.

Tendo em vista que os campos do Omie e do Ploomes apresentam comportamentos diferentes, é importante destacar os seguintes pontos cruciais:

Toda mudança no mapeamento de campos é salva ao clicar em “Atualizar integração”. Quando a opção é ativada, a uma nova varredura é feita entre os dois sistemas. Esse processo pode demorar alguns minutos e é bastante pesado, então evite atualizações constantes a todo momento. Atualize a integração quando terminar todas as modificações ao invés de salvar a cada campo mapeado. A integração só executa caso houver alguma diferença nas configurações (para evitar abuso dessa função que sobrecarrega a API do Omie).

**Os campos do tipo “opções pré-cadastradas” sincronizam suas opções com o Omie toda vez que a integração é atualizada. Ou seja, uma sincronização é disparada quando o usuário clica em “Atualizar integração” no painel de configuração de plug & play no Ploomes. Portanto, evite a alteração das opções quando o campo for usado na integração. Uma dica para evitar falhas é restringir a edição e inclusão de opções do campo para apenas o administrador da conta.**

Toda vez que um campo de imposto do Omie é mapeado, o sistema do Omie automaticamente interpreta que as informações de imposto serão enviadas do Ploomes ao Omie. Então, o usuário deve escolher entre fazer as regras de impostos do Ploomes e enviar para o Omie ou deixar que o Omie se encarregue dos impostos. Cuidado com esta decisão. Se ao menos um campo de imposto do Omie for mapeado, ele deixa de calcular os impostos.

Alguns campos são apenas para leitura. O Omie recebe a informação mas não a utiliza para inserção ou atualização. Esses campos são:

**Venda:**

- Valor do Desconto (apenas leitura)
- Total de Mercadorias (apenas leitura)
- Valor Total do Pedido (apenas leitura)
- Total de ICMS ST (apenas leitura)
- Total de IPI (apenas leitura)
- Nº pedido do cliente (apenas leitura)
- Etapa (apenas leitura)

**Ordem de Serviço:**

- Valor Total do Pedido (apenas leitura)
- Nº ordem do serviço (apenas leitura)
- Etapa (apenas leitura)

Os campos a serem mapeados devem ter tipos compatíveis. Se qualquer campo estiver mapeado com tipos errados, a integração alerta sobre esse erro e não executa a sincronização.

Abaixo está a relação de campos do Omie e o tipo de campo esperado no Ploomes:

| **Campo do Omie** | **Tipo de campo do Ploomes** |
| --- | --- |
| ClienteFornecedor.Inscrição Estadual | Texto Simples |
| ClienteFornecedor.Inscrição Municipal | Texto Simples |
| ClienteFornecedor.Inscrição SUFRAMA | Texto Simples |
| ClienteFornecedor.Tipo de Atividade | Opções pré-cadastradas |
| ClienteFornecedor.Optante do Simples Nacional | Checkbox |
| ClienteFornecedor.É um produtor rural | Checkbox |
| ClienteFornecedor.Limite de Crédito Total | Moeda |
| ClienteFornecedor.Observações | Texto Multilinha |
| ClienteFornecedor.Observações Detalhadas | Texto Multilinha |
| Produto.Código NCM | Texto Simples |
| Produto.Código EAN | Texto Simples |
| Produto.Marca | Texto Simples |
| Produto.Altura | Número com casas decimais ilimitadas |
| Produto.Largura | Número com casas decimais ilimitadas |
| Produto.Profundidade | Número com casas decimais ilimitadas |
| Produto.Dias de Garantia | Número inteiro |
| Produto.Dias de Crossdocking | Número inteiro |
| Produto.Peso Líquido | Número com casas decimais ilimitadas |
| Produto.Peso Bruto | Número com casas decimais ilimitadas |
| Produto.Indicador de Produção em Escala Relevante | Checkbox |
| Produto.Descrição Detalhada do Produto | Texto Multilinha |
| Produto.Observações Internas | Texto Multilinha |
| VendaProduto.Previsão de Faturamento | Data |
| VendaProduto.Valor do Desconto **(apenas leitura)** | Moeda |
| VendaProduto.Total de Mercadorias **(apenas leitura)** | Moeda |
| VendaProduto.Valor Total do Pedido **(apenas leitura)** | Moeda |
| VendaProduto.Total de ICMS ST **(apenas leitura)** | Moeda |
| VendaProduto.Total de IPI **(apenas leitura)** | Moeda |
| VendaProduto.Tipo do frete | Opções pré-cadastradas |
| VendaProduto.Valor do Frete | Moeda |
| VendaProduto.Transportadora | Opções pré-cadastradas (Campo do tipo Cliente) |
| VendaProduto.Observações | Texto Multilinha |
| VendaProduto.Nº pedido do cliente **(apenas leitura)** | Texto Simples |
| VendaProduto.Etapa **(apenas leitura)** | Texto Simples |
| VendaProduto.Método de Pagamento | Opções pré-cadastradas |
| VendaProduto.Número de Parcelas | Número inteiro |
| VendaProduto.Contato | Texto Simples |
| VendaProduto.Utilizar os seguintes endereços de e-mail | Texto Multilinha |
| VendaProduto.Nº do Pedido do Cliente | Texto Simples |
| VendaProduto.Nº do Contrato de Venda | Texto Simples |
| VendaProduto.Item.Alíquota ICMS | Porcentagem |
| VendaProduto.Item.Base ICMS | Moeda |
| VendaProduto.Item.Situação Tributária ICMS | Opções pré-cadastradas |
| VendaProduto.Item.Modalidade ICMS | Opções pré-cadastradas |
| VendaProduto.Item.Origem ICMS | Opções pré-cadastradas |
| VendaProduto.Item.Percentual de redução da base de cálculo do ICMS | Porcentagem |
| VendaProduto.Item.Valor ICMS | Moeda |
| VendaProduto.Item.Alíquota ICMS ST Operação Própria | Porcentagem |
| VendaProduto.Item.Alíquota ICMS ST | Porcentagem |
| VendaProduto.Item.Valor Base ICMS ST | Moeda |
| VendaProduto.Item.Margem ICMS ST | Porcentagem |
| VendaProduto.Item.Modalidade ICMS ST | Opções pré-cadastradas |
| VendaProduto.Item.Percentual de redução da base de cálculo do ICMS ST | Porcentagem |
| VendaProduto.Item.Valor ICMS ST | Moeda |
| VendaProduto.Item.Alíquota IPI | Número com casas decimais ilimitadas |
| VendaProduto.Item.Valor Base IPI | Moeda |
| VendaProduto.Item.Situação Tributária IPI | Opções pré-cadastradas |
| VendaProduto.Item.Enquadramento IPI | Opções pré-cadastradas |
| VendaProduto.Item.Quantidade de Unidades Tributáveis do IPI | Número com casas decimais ilimitadas |
| VendaProduto.Item.Tipo de cálculo do IPI | Opções pré-cadastradas |
| VendaProduto.Item.Valor IPI | Moeda |
| VendaProduto.Item.Valor do IPI por Unidade Tributável | Moeda |

**Novos campos de Serviço e de Ordem de Serviço**

| **Campo do Omie** | **Tipo de campo do Ploomes** |
| --- | --- |
| Serviço.Tributação do Serviço | Texto Simples |
| Serviço.Código NBS - Nomenclatura Brasileira de Serviços | Texto Simples |
| Serviço.Código do Serviço LC 116 | Texto Simples |
| Serviço.Código do Serviço ou CNAE | Texto Simples |
| Serviço.% Alíquota do COFINS | Porcentagem |
| Serviço.% Alíquota do CSLL | Porcentagem |
| Serviço.% Alíquota do INSS | Porcentagem |
| Serviço.% Alíquota do IR | Porcentagem |
| Serviço.% Alíquota do ISS | Porcentagem |
| Serviço.% Alíquota do PIS | Porcentagem |
| Serviço.COFINS RetidoCheckbox | Checkbox |
| Serviço.CSLL Retido | Checkbox |
| Serviço.INSS Retido | Checkbox |
| Serviço.IR Retido | Checkbox |
| Serviço.ISS Retido | Checkbox |
| Serviço.PIS Retido | Checkbox |
| OrdemServiço.Valor Total do Pedido **(apenas leitura)** | Moeda |
| OrdemServiço.N° ordem do Serviço **(apenas leitura)** | Texto Simples |
| OrdemServiço.Etapa **(apenas leitura)** | Texto Simples |
| OrdemServiço.N° de parcelas | Número inteiro |
| OrdemServiço.Previsão de Faturamento | Data |
| OrdemServiço.Método de Pagamento | Opções pré-cadastradas |
| OrdemServiço.Observações | Texto Multilinha |
| OrdemServiço.N° Pedido do Cliente | Texto Simples |
| OrdemServiço.N° Contrato de Venda | Texto Simples |
| OrdemServiço.Dados Adicionais para a Nota Fiscal | Texto Multilinha |
| OrdemServiço.Código da Obra | Texto Simples |
| OrdemServiço.Código ART | Texto Simples |
| OrdemServiço.Contato | Texto Simples |
| OrdemServiço.Item.Acréscimos | Moeda |
| OrdemServiço.Item.Descontos | Moeda |
| OrdemServiço.Item.Outras Retenções | Moeda |
| OrdemServiço.Item.Não gerar Contas a receber | Moeda |
| OrdemServiço.Item.COFINS Retido | Checkbox |
| OrdemServiço.Item.CSLL Retido | Checkbox |
| OrdemServiço.Item.INSS Retido | Checkbox |
| OrdemServiço.Item.IRRF Retido | Checkbox |
| OrdemServiço.Item.ISS Retido | Checkbox |
| OrdemServiço.Item.PIS Retido | Checkbox |
| OrdemServiço.Item.% Alíquota do COFINS | Porcentagem |
| OrdemServiço.Item.% Alíquota do CSLL | Porcentagem |
| OrdemServiço.Item.% Alíquota do INSS | Porcentagem |
| OrdemServiço.Item.% Alíquota do IRRF | Porcentagem |
| OrdemServiço.Item.% Alíquota do ISS | Porcentagem |
| OrdemServiço.Item.% Alíquota do PIS | Porcentagem |

As Ordens de Serviço no Omie têm um comportamento peculiar. Quando é criado um novo serviço em uma Ordem de Serviço, é possível escolher um serviço da base de serviços cadastrados, ou criar um no momento da edição da Ordem, sendo que neste último caso, este serviço só existirá naquela ordem (chamaremos esse de serviço único).

No Ploomes não existe essa funcionalidade, então para que a integração aconteça, por recomendação da equipe de desenvolvimento da Omie, nós criamos um único serviço no Ploomes com nome “Serviços Prestados (NÃO APAGAR) (Integração Omie)” e com valor unitário 1,00 , e apontamos quaisquer serviços únicos do Omie para este serviço. O valor do item da venda é um valor exclusivo do item da venda, e não do produto, então continuará com o valor que veio da integração pelo Omie; Já o nome do produto, o Ploomes acessa diretamente do cadastro do produto. Portanto, a integração cria um campo com nome “Produto/Serviço (Omie)” que pega o nome do serviço único usado na Ordem de Serviço de lá, para ser usado no documento de venda no lugar do campo padrão [Produto.Nome].

## O que não é contemplado na integração Ploomes <> Omie?

### 1. Integração com Múltiplos CNPJ:

- Não há suporte para a integração simultânea com vários CNPJs.

### 2. Consulta em Tempo Real de Impostos:

- A capacidade de consulta em tempo real de impostos não está disponível.

### 3. Integração com Contas a Pagar e Contas a Receber:

- A integração não abrange as funcionalidades de contas a pagar e contas a receber.

### 4. Integração com o Módulo de "Vendas de Contratos":

- A integração não inclui o módulo de "Vendas de Contratos".

### 5. Integração com Todos os Campos Dinâmicos:

- Nem todos os campos customizados estão integrados. Consulte a tela de mapeamento da integração para verificar a disponibilidade

### 6. Integração com Cadastro de Materiais:

- O cadastro de materiais não é integrado ao Ploomes.

### 7. Integração com Ficha Técnica do Produto:

- A ficha técnica do produto não é integrada.

### 8. Cancelamento de Vendas no Omie e seu Impacto no Ploomes:

- Quando uma venda é cancelada no Omie, não há reflexo automático no Ploomes. Existe uma melhoria em desenvolvimento para alterar este comportamento.

### 9. Envio de Todos os Produtos do Omie para o Ploomes:

- Todos os produtos do Omie são enviados ao Ploomes, incluindo produtos de uso pessoal não destinados à comercialização. Não é possível realizar filtragem.

### 10. Restrição na Escolha da Conta para Envio de Pedidos:

- No Ploomes, apenas uma conta pode ser escolhida para enviar pedidos, enquanto no Omie, para faturar, é possível alterar a conta, havendo mais de uma disponível.

### 11. Atualização de Dados no Omie ao Ativar a Integração:

- Ao ativar a integração, se um cliente existente na Ploomes também estiver no Omie, os dados serão atualizados no Omie, considerando a Ploomes como o primeiro proprietário da informação.

### 12. Impacto da Retirada de Produtos da Família Produtos ou Serviços na Integração da Venda:

- Se os produtos forem retirados da família produtos ou serviços, a integração da venda pode ser afetada.

### 13. Limitação no Mapeamento de Campos de Data:

- Atualmente, o mapeamento de campos de data se limita à 'previsão de faturamento'.

### 14. Restrição na Mapeamento de Campos de Opção Pré-Cadastrada Customizados:

- Campos de opção pré-cadastrada customizados não podem ser mapeados por valor padrão da proposta para a venda.

### 15. Validade de links de imagens de produtos

Os links de imagens de produtos gerados pelo sistema Omie possuem um **prazo de validade de 7 dias**. Após esse período, o link expira automaticamente e a imagem deixa de ser exibida, sendo necessário renovar o link no Omie.

Esse comportamento é uma limitação do Omie e, por consequência, impacta a integração com o Ploomes, que apenas consome o link disponibilizado pelo ERP.

**Formas de contorno:**

- **Editar manualmente o produto no Omie**, salvando novamente o cadastro para renovar o link da imagem (solução temporária, válida por mais 7 dias);
- **Criar uma rotina semanal de [edição em lote de produtos no Omie](https://ajuda.omie.com.br/pt-BR/articles/5391514-atualizando-em-lote-as-fotos-do-seus-produtos)**, para renovação periódica dos links;
- **Hospedar as imagens em uma plataforma pública de armazenamento** (como Google Drive, por exemplo) e substituir, no Ploomes, o link da imagem pelo link público dessa plataforma (manualmente ou via importação);
- **Adicionar a imagem diretamente no Ploomes**, fazendo upload do arquivo pelo botão **“Selecionar”** no campo de imagem e, em seguida, **“Adicionar imagem”** (processo manual).

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
