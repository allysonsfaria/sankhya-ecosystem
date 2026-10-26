---
id: "42427469505431"
titulo: "Integração com o ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427469505431-Integra%C3%A7%C3%A3o-com-o-ERP-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:47Z"
rotulos: ["sync_hc", "ploomes", "ploomes_10022499", "sync_hash_9d2c9865ff30"]
---

# Integração com o ERP Sankhya

## 1 Introdução

**O que é a integração?**

A integração com o ERP Sankhya é uma plataforma desenvolvida pela Ploomes para realizar operações de comunicação entre Ploomes e Sankhya.

**O que a integração faz?**

A integração realiza importação e exportação de dados das entidades principais integradas e também realiza consultas em tempo real no Sankhya em algumas entidades de apoio.

**Como funciona a integração?**

A integração é composta por serviços de API que são acionados sob demanda para criar e editar as regras de integração e realizar a comunicação de dados através dos serviços de API’s do Sankhya e API’s do Ploomes.

---

## 2 Escopo Geral

A integração realiza importação e exportação de cadastros básicos de operação e também dos documentos comerciais gerados entre as plataformas. No entanto, existem entidades específicas do Sankhya que são integradas e outras que são apenas consultadas como apoio para as operações no Ploomes.

## 2.1 Entidades integradas e vias de integração possíveis

Abaixo estão listadas as **entidades integradas** e suas vias de integração possíveis (exportação e/ou importação).

| **Entidade Sankhya** | **Tabela** | **Vias de integração possíveis** | **Entidade Ploomes** |
| --- | --- | --- | --- |
| Parceiro Pessoa Jurídica | TGFPAR | Sankhya ⇄ Ploomes | Empresa |
| Parceiro Pessoa Física | TGFPAR | Sankhya ⇄ Ploomes | Pessoa |
| Contato de Cliente | TGFCTT | Sankhya ⇄ Ploomes | Pessoa |
| Vendedor | TGFVEN | Sankhya → Ploomes | Usuário |
| Produto / Serviço | TGFPRO | Sankhya → Ploomes | Produto |
| Grupo de Produto | TGFGRU | Sankhya → Ploomes | Grupo de Produto |
| Orçamento | TGFCAB/TGFITE | Sankhya ⇄ Ploomes | Proposta |
| Pedido de Venda | TGFCAB/TGFITE | Sankhya ⇄ Ploomes | Venda |
| Nota de Venda | TGFCAB/TGFITE | Sankhya → Ploomes | Venda (leitura) |

## 2.2 Entidades Sankhya de Apoio

As entidades a seguir não estão diretamente integradas ao Ploomes, gerando cadastros no Ploomes como as entidades integradas detalhadas acima, mas são utilizadas para consultas ao Sankhya que trazem informações para o Ploomes.

| **Entidade** | **Comportamento no Ploomes** |
| --- | --- |
| Cidade | Cidades do Ploomes poderão gerar novas cidades no Sankhya e cidades do Sankhya poderão gerar novas cidades no Ploomes. |
| Endereço | Endereços do Ploomes poderão gerar novos endereços no Sankhya e endereços do Sankhya serão recebidos em campos de endereço do Ploomes. |
| Bairro | Bairros do Ploomes poderão gerar novos bairros no Sankhya e bairros do Sankhya serão recebidos em campos de endereço do Ploomes. |
| Região | Regiões do Sankhya não geraram regiões no Ploomes e não é possível gerar regiões no Sankhya pelo Ploomes. |
| Unidade de medida | As unidades de medida de produto virão para o Ploomes nos produtos e como opções nos produtos da proposta / venda. |
| Unidades de medida alternativas | As unidades de medida alternativas de produtos virão para o Ploomes como opções nos produtos da proposta / venda. |
| Estoque | Os estoques disponíveis poderão ser consultados para os produtos da proposta / venda durante a geração da proposta / venda. |
| Tabela de preço | Os preços de produtos nas tabelas de preço poderão ser consultadas para os produtos da proposta / venda durante a geração da proposta / venda. |
| Tipo de Operação | As TOPs do Sankhya ficarão disponíveis para configuração da integração de orçamentos (propostas) e pedidos de vendas (vendas). |
| Tipo de Negociação | Os Tipos de Negociação ficarão disponíveis como opções nos campos de proposta e venda. |
| Empresa | As Empresas ficarão disponíveis como opções nos campos de proposta e venda. |
| Local Financeiro | Os Locais Financeiros ficarão disponíveis como opções nos campos de proposta e venda. |
| Natureza | As Naturezas ficarão disponíveis como opções nos campos de proposta e venda. |
| Centro de Resultado | Os Centros de Resultado ficarão disponíveis como opções nos campos de proposta e venda. |

---

## 3 Configuração

## 3.1 Primeira configuração

### 3.1.1 Habilitação da integração

Para conseguir habilitar a integração, é necessário que o módulo da Integração Sankhya esteja ativo na conta Ploomes. Com o módulo ativo, é possível visualizar nas configurações do Ploomes, na tela de Integrações Plug & Play, a integração Sankhya.

![Imagem 1: Para conseguir habilitar a integração, é necessário que o módulo da Integração Sankhya esteja ativo na conta Ploomes.…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434589/2019b81ceaa9ff8d04d54d93027d/AD_4nXdx0KsRlSm1LEmu6OHxgbJDwCxzrQPNWPzZHp04uyfwXI1LUoGBTlujpVQz_PbYp8kCu1OUEXRhMFgGs8heeIHEKDuGTIfLdXNRyPfftibn3cIr2O4w8xKzd-9jEftKZ9tKpTRDGA?expires=1786536000&signature=d3809148810ad5346389bc05ac8b548a2747d266bdf20e341041a041db2ed740&req=dSUlEs19mYRXUPMW3nq%2BgT4wdSG3klLdLJOhK481e9syXNiBeBqJtzj4bb3X%0Aa4k0OTHFNOwdSURRw1qCnK8b%2Bg8%3D%0A)

Ao abrir a tela de Integrações Plug & Play vão ser listadas diversas integrações possíveis, inclusive a integração Sankhya.

![Imagem 2: Ao abrir a tela de Integrações Plug & Play vão ser listadas diversas integrações possíveis, inclusive a integração…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434592/aee139ab90712c798decec0a85fe/AD_4nXcVuGo6CRTsc1UNgDYU5tKbjZ2OUXgLUZOuYLKmHuTrZO-4It2EMVOtO41Ym2qZNJPv2T3WhH-2kM6a85Kt5ESjjt_-TF3ImSDRmLjv8h5cU9pStpeaO5IfUwF4b5ZH9TB-moKsCQ?expires=1786536000&signature=23a32141b3d9f79d49921bdc9696d1c1686b52aac237ffe411bd254b256a5281&req=dSUlEs19mYRWW%2FMW3nq%2BgZvmudxD9jb6hvvxulGE6%2FFLi%2BQom%2FZNDrAkyuaa%0A0Q9pUBbZYfa4cFPAyv%2F0A6t1xsc%3D%0A)

Na tela de “Integrações plug and play”, se o módulo da Integração Sankhya estiver ativo para a conta Ploomes, é possível iniciar a habilitação da integração Sankhya.

Ao abrir a tela de configuração da integração Sankhya, é aberta a tela de autorização da integração. Nessa tela, é necessário inserir o Token de integração - este token é gerado no ambiente de produção do Sankhya - e realizar a validação do Token. Nessa validação, a integração faz uma consulta simples ao Sankhya para garantir que será possível logar no Sankhya e que será possível trazer os dados do Sankhya para o Ploomes.

![Imagem 3: Ao abrir a tela de configuração da integração Sankhya, é aberta a tela de autorização da integração. Nessa tela, é…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434593/4ed8743987c8ee7c8fc126a22c54/AD_4nXesgnyaMqCyerQ_0VuzVKwGKRe0wCn0FnTY7BgI5l_faeWKokDmpXg0dgRevK4HcBSe-SMp9DFrSXTars6uDnXikjZm0Pho1c1pQ23M1XkBQSLL6uUDb1RnOyzxtOeNTRBB3DWQPQ?expires=1786536000&signature=ec0d51df27a830909d12bad95b7ccdba089632c98d7ef57636412fc54f28fd9a&req=dSUlEs19mYRWWvMW3nq%2Bganv%2FMuGLgNcdxz0ha4M%2Fc1Sooq0LVLJzmTfmpJs%0AZiUfpmpb%2F8CxuAkJL3g9fBVnTHc%3D%0A)

Na tela inicial de habilitação da integração é necessário inserir um Token do ambiente Sankhya de produção gerado para a aplicação CRM Ploomes. Após inserir o Token, é necessário realizar uma Validação e posteriormente, caso a validação seja bem sucedida, a Habilitação da integração. Se o Token for válido, ficará disponível o botão “Habilitar integração” que deve ser acionado para prosseguir com a configuração.

E então, com a **habilitação da integração concluída**, o usuário administrador é direcionado para a tela de configuração da integração.

### 3.1.2 Autenticação e acesso ao Sankhya

Após a validação do token e habilitação da integração, a integração passa a ter acesso ao Sankhya para as entidades configuradas para o usuário de integração. A autenticação do usuário de integração é feita através de um serviço de login via API: [Serviço de Autenticação via Json](https://developer.sankhya.com.br/reference/post_login).

Ao realizar o login no Sankhya integrado, é possível realizar as ações necessárias de consulta, edição e envio de dados entre Ploomes e Sankhya. O usuário de integração fica com sessão ativa no Sankhya, mas consome não compete com as sessões de usuários normais.

Os usuários de integração tem suas sessões expiradas no Sankhya assim como qualquer outro usuário. Portanto, a integração inicia novas seções a cada vez que tem sua sessão interrompida, mantendo sempre um BearerToken principal e outro reserva válido.

---

**# Observações importantes sobre a autenticação da integração no Sankhya**

- Quanto menor for o tempo de inatividade configurado para o sistema, maior será o impacto no tempo de processamento da integração, pois há necessidade de realizar novos logins de forma recorrente. Recomenda-se que o tempo mínimo de inatividade esteja configurado em 5 minutos. No entanto, quanto maior este intervalo, melhor para a integração. Artigo Sankhya: [Como definir o tempo de inatividade no sistema – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044351353-Como-definir-o-tempo-de-inatividade-no-sistema)
- As permissões dadas ao usuário de integração do Ploomes no Sankhya são importantes, pois caso alguma entidade não esteja liberada para o usuário da integração, não será possível utilizar a integração.

  - Exemplo: usuário de integração não possui acesso a TGFPRO, logo não será possível consultar os produtos via API, devido a restrição do Sankhya. Portanto é preciso liberar o acesso para o usuário de integração.
- A data de expiração de acesso ao Sankhya do usuário de integração deve estar válida, caso contrário a integração não terá acesso para realizar login no Sankhya e portanto não será possível realizar as ações da integração.
- Qualquer interrupção na sessão do usuário de integração interrompe a operação da integração, pois sem estar logado no Sankhya não é possível realizar ações de exportação, importação nem consultas em tempo real.

---

### 3.1.3 Gatilhos de ação

Os gatilhos de ação são parâmetros True/False configurados na integração para determinar o acionamento ou não de determinados padrões de comportamentos.

Os gatilhos são a forma do usuário administrador determinar se determinadas ações devem ocorrer pela integração ou não.

De forma geral, os gatilhos de ação vão determinar se cadastros serão importados e/ou exportados, e se essas importações e/ou exportações serão realizadas para qualquer criação de cadastro e/ou para qualquer edição de cadastro.

Abaixo, exemplo de gatilho para importação de Parceiros Cliente PJ ativo na configuração.

![Imagem 4: Abaixo, exemplo de gatilho para importação de Parceiros Cliente PJ ativo na configuração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434582/c08601a5180ce977ec3dfe2ec32b/AD_4nXe4nA0ldhXsCxPy6anS-Dd5pIpVqNAn_wMByWcD4otzwHTY9aFZRGdMu0a7sOT11LwCOHsl5dLZBkJXnuXcDLhe-93bH9z2c244gB-oqD3uLA3eaEgX3r2Uo1bChAT_q9MLUOie?expires=1786536000&signature=5099556c552b2c9721df20f5da81c3e934f40a73feca3254ef8a0d0120c545cf&req=dSUlEs19mYRXW%2FMW3nq%2BgSpGE%2B0w%2Bk7o6vxciObC9uPSY9Mbnnaz793zwkGf%0AYf3tPmX%2FmobjKBvEWfEqtXP%2BNJQ%3D%0A)

### 3.1.4 Filtros de integração

Os filtros de integração são regras pré-definidas na integração para aplicar filtros na importação e exportação de cadastros, selecionando melhor os dados que serão integrados.

Os filtros de integração são uma ferramenta fundamental para que a integração se adapte à necessidade de uso da integração na conta Ploomes, pois permite a criação de regras de filtros totalmente dinâmicas.

Os filtros de integração podem ser de dois tipos:

- **Filtros de recebimento (ou Filtros de importação):** esses filtros são configurados a cada seção de entidade integrada para criar filtros dinâmicos com base nos campos filtráveis da entidade de origem no Sankhya. Então, com base em campos da entidade no Sankhya, é possível definir regras de filtragem para restringir ou selecionar quais dados serão recebidos do Sankhya no Ploomes.
- **Filtros de envio (ou Filtros de exportação):** esses filtros são configurados a cada seção de entidade integrada para criar filtros dinâmicos com base nos campos filtráveis da entidade de origem no Ploomes. Então, com base nos campos da entidade no Ploomes, é possível definir regras de filtragem para restringir ou selecionar quais dados serão enviados do Ploomes para o Sankhya.

Os filtros de integração são aplicados tanto na carga de dados inicial da integração quanto durante a operação normal durante o uso da integração e também afetam todos os cadastros do Ploomes e do Sankhya, mesmo os cadastros que já estão integrados.

Os filtros de integração são customizáveis e permitem diversas condições de filtro com base no tipo de campo que podem ser combinadas em múltiplas seções de regras de “E” e “OU”. Não é possível realizar fieldpath nos filtros de recebimento, isto é, não é possível utilizar campos de entidades relacionadas a entidade integrada na criação do filtro de integração.

### 3.1.5 Mapeamento de campos

O mapeamento de campos é o processo de definir a correspondência entre os campos de duas bases de dados ou sistemas diferentes, garantindo que as informações sejam transferidas corretamente entre eles.

No contexto da integração entre o Ploomes e o Sankhya, esse mapeamento determina quais campos do Ploomes serão sincronizados com os respectivos campos do Sankhya, respeitando os formatos e regras de cada sistema. Por exemplo, um campo de "Nome do Cliente" no Ploomes pode ser vinculado ao campo "Nome Parceiro" no Sankhya, garantindo que os dados sejam corretamente replicados e atualizados entre as plataformas.

Na configuração do mapeamento de campos da integração temos os tipos de mapeamento e as vias de integração dos campos.

#### Tipos de Mapeamento

Os tipos de mapeamento existentes determinam como é o comportamento de mapeamento específico de alguns campos. Os tipos são definidos abaixo:

**Mapeamento fixo**

Os mapeamento fixos são aqueles em que os pares de campos (Sankhya e Ploomes) são definidos por padrão na integração. Esses mapeamentos incluem campos obrigatórios do Sankhya que já possuem campos equivalentes nativos no Ploomes.

Os mapeamentos fixos são obrigatórios e não podem ser removidos da integração.

**Mapeamento de escolha**

Os mapeamentos fixos são aqueles em que o campo de origem no Sankhya é obrigatório mas não necessariamente já exista um campo nativo no Ploomes equivalente. Portanto, nesses mapeamentos é possível escolher qual o campo do Ploomes será mapeado com o campo do Sankhya.

Por padrão, esses campos do Ploomes terão um campo sugerido pela integração. Mas é possível alterá-los na configuração do mapeamento.

Os mapeamentos de escolha são obrigatórios e não podem ser removidos da integração.

**Mapeamento customizado**

Os mapeamentos customizados são aqueles em que o usuário administrador pode adicionar novas relações de campos para mapeamento conforme a necessidade de uso da integração. Portanto, é possível mapear os campos de origem da entidade Sankhya com qualquer campo do Ploomes (nativos ou dinâmicos).

Por padrão, ao adicionar uma nova relação de campos, o Ploomes não irá sugerir um campo de mapeamento. No entanto, é possível selecionar um campo existente no Ploomes para mapeamento ou criar um campo dinâmico para mapeamento.

É possível mapear campos adicionais criados na entidade principal do Sankhya.

No mapeamento customizado, só é possível mapear os campos do Sankhya que existem na entidade principal integrada. Ou seja, campos existentes em entidades relacionadas não podem ser mapeados, bem como campos virtuais do Sankhya que não existem na entidade Sankhya também não podem ser mapeados.

Os mapeamentos customizados são opcionais e podem ser removidos da integração.

![Imagem 5: Os mapeamentos customizados são opcionais e podem ser removidos da integração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434587/23ae59d655c92b3b99d8c987b9a1/AD_4nXc3Z4HmcA_JPsSxDEdhQcB9NTcTha0eoAbagsptQBj92GH2XSBYbPzGhZVRlu7PnqEr6sRKkafD7FGbXwesSoYQOR4PtweuKUv3lfwjXfK1VhVQqIOO478v0hNOWA4Ten0QMD--tw?expires=1786536000&signature=4aada1618bb2b32bb4a2b04d22c04639835b7623b50595a27e427e370d2c16c7&req=dSUlEs19mYRXXvMW3nq%2BgYocf5lify6KzqVBLfX1D18s8ExS8ZA1XmLQAKGN%0A0S9hlMAP8KJ6WtsnocJA96t%2Bu8A%3D%0A)

Exemplo de apresentação do mapeamento na seção de configuração de Produtos. No caso da imagem, estão destacados o formato de apresentação dos mapeamentos fixo, de escolha e customizado.

#### Vias de integração dos campos mapeados

Para cada par de campos mapeados existe uma via de integração desses campos que deve ser definida.

As possibilidades são:

- **Sankhya < Ploomes:** valor do campo é apenas enviado do Ploomes para o Sankhya
- **Sankhya > Ploomes:** valor do campo é apenas recebido do Sankhya no Ploomes
- **Sankhya <> Ploomes:** valor do campo é enviado do Ploomes para o Sankhya e também é recebido do Sankhya no Ploomes.

Para a maior parte dos campos mapeados a integração pré-define uma via de integração dos campos - que não é editável, no entanto, para alguns casos é possível alterar as vias de integração.

![Imagem 6: Para a maior parte dos campos mapeados a integração pré-define uma via de integração dos campos - que não é editável,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434600/43fec5d8776210417647866452b7/AD_4nXf2cHas1pS_x1v8XbJLicJzYmqh_MFlpPIUVTF5MLPcXfxL9C9GYvf90BIl-sQIuCKyJYBllazU5yAo08WuWk3AD62k37gWvYe-u7Al9KZbzn6w28L__0SLEYjxhGz_3JIdv6AP?expires=1786536000&signature=8a291cbb3d4c7c16cb121ba16625a80529f83a5be11410e7988b55ee2cc66757&req=dSUlEs19mYdfWfMW3nq%2Bgfgpxp%2Bl12Ie9ud9so9p8WmypntOm9ZAnXu45HNj%0Ag9a3N05rKGCll5dELZHXf%2BqOL1k%3D%0A)

Exemplo de vias de integração de campos na seção de Contato de Cliente. Alguns pares de campos tem sua via pré-definida e outros tem sua via sugerida, podendo alterá-la.

#### Mapeamento de campos de tabelas complementares

A partir da V3 da integração Sankhya é possível realizar o mapeamento de campos de tabelas complementares, conforme descrito no artigo [https://suporte.ploomes.com/pt-BR/articles/14367098](https://sankhya.zendesk.com/hc/pt-br/articles/42427482762391).

#### Compatibilidade por Tipos de Campos

Para o mapeamento de campos é possível selecionar somente os campos compatíveis com base na definição abaixo:

| **Tipo de Campo Sankhya** | **Tipo de Campo Ploomes** |
| --- | --- |
| TEXTO | TEXTO SIMPLES |
| TEXTO | TEXTO MULTILINHA |
| TEXTO LONGO | TEXTO MULTILINHA |
| DECIMAL | MOEDA |
| DECIMAL | NÚMERO DECIMAL DE CASAS ILIMITADAS |
| INTEIRO | NÚMERO INTEIRO |
| DATA | DATA |
| DATA E HORA | DATA |
| HORA | HORA |
| LISTA DE OPÇÕES | OPÇÕES PRÉ-CADASTRADAS**\*** |
| LISTA DE OPÇÕES | NÚMERO INTEIRO**\*\*** |

**\***Apenas os campos abaixo são convertidos automaticamente como opções pré-cadastradas no Ploomes.

- Empresa (TGFCAB)

- TOP (TGFCAB)

- Tipo de Negociação (TGFCAB)

- Natureza (TGFCAB)

- Centro de Resultado (TGFCAB)

- Status da Nota (TGFCAB)

- Transportadoras (TGFCAB)

- Local (TGFITE)

- Controle (TGFITE)

- Unidade de Medida (TGFITE)

- Classificação ICMS (TGFPAR)

**\*\***Outros campos do Sankhya ausentes na lista acima serão importados apenas com sua chave externa (ID) em um campo de número inteiro.

**Observação importante: campos de mapeamentos fixos não podem ter o seu tipo de campo para o campo Ploomes mapeado alterado.**

#### Particularidades do mapeamento de campos de opções pré-cadastradas

Para o mapeamento de campos do tipo opções pré-cadastradas é necessário realizar uma compatibilização das opções existentes no Ploomes.

As opções pré-cadastradas do Ploomes são compatibilizadas apenas na ativação da integração ou na reativação da integração ou na aplicação de edição da integração. Portanto, se forem criadas novas opções pré-cadastradas no Sankhya em algum campo mapeado, existem 3 formas de realizar a importação dessa nova opção:

- Desativando e reativando a integração;
- Ao editar a integração, clicando no botão de Sincronizar da seção, salvando a seção da entidade em questão e aplicando as edições realizadas na integração;
- Importando algum cadastro que possua o campo com a nova opção pré-cadastrada preenchida no Sankhya.

Existe uma premissa básica de que as opções pré-cadastradas no campo do Sankhya irão prevalecer sobre as opções pré-cadastradas no campo do Ploomes. Essa regra segue a seguinte lógica:

- Caso o campo do Ploomes não tenha nenhuma opção cadastrada ainda, ele recebe as opções do Sankhya;
- Caso o campo do Ploomes possua uma ou mais opções cadastradas:

  - As opções que existem no campo Ploomes e não existem no campo Sankhya serão excluídas do campo Ploomes;
  - As opções que existem no campo Ploomes e que tenham exatamente o mesmo “nome da opção” e “chave de identificação da opção” que as opções do campo Sankhya serão mantidas no campo Ploomes;
  - As opções que existem no campo Ploomes e que tenham apenas o mesmo “nome da opção” mas “chave de identificação da opção” diferentes serão excluídas do campo Ploomes.
  - As opções que existem no campo do Sankhya e que não existem no campo Ploomes serão criadas no campo Ploomes.

**Exemplo de aplicação da regra**

Supondo a aplicação da regra considerando a notação de opções assim indicadas ([NOME DA OPÇÃO], [chave da opção]):

- Um campo Sankhya com as opções: (OPÇÃO A,a), (OPÇÃO B,b), (OPÇÃO C, c);
- Mapeado com um campo Ploomes com as opções: (OPÇÃO B, b), (OPÇÃO C#, c), (OPÇÃO D, d);

Então o campo no Ploomes com a compatibilização pela regra acima descrita terá as seguintes ações:

- Ter as opções (OPÇÃO C#, c) e (OPÇÃO D, d) excluídas;
- Ter a opção (OPÇÃO A,a) criada;
- Ter a opção (OPÇÃO C,c) criada;
- Ter a opção (OPÇÃO B, b) mantida.

Resultando nas seguintes opções pré-cadastradas no campo do Ploomes:

- Opções pré-cadastradas no campo no Ploomes:

  - (OPÇÃO A,a)
  - (OPÇÃO B,b)
  - (OPÇÃO C,c)

**# Observações importantes sobre limite de opções pré-cadastradas**

- Existe um limite de criação para a quantidade de opções pré-cadastradas de 10.000 opções.

É importante estar atento a atualizações realizadas em nomes de campos, obrigatoriedades e opções pré-cadastradas em campos mapeados. O usuário administrador do Ploomes e do Sankhya pode alterar o nome de campos, apagar campos, alterar sua obrigatoriedade (apenas para campos dinâmicos) e também alterar - incluindo ou removendo - as opções pré-cadastradas (apenas para campos dinâmicos). Essas alterações podem impactar diretamente a integração.

Se as edições forem realizadas antes de a integração ser ativada, as alterações podem ser consideradas no mapeamento. Caso as alterações sejam realizadas com a integração ativa, pode ser necessário realizar uma nova compatibilização dos cadastros de opções pré-cadastradas ou alterar o mapeamento dos campos.

---

**# Observações importantes sobre mapeamentos**

- Quanto mais campos forem adicionados no mapeamento da integração, mais lenta será a velocidade de processamento de dados (tanto na importação quanto na exportação).
- É necessário observar o limite de campos utilizados na integração que serão utilizados no CPQ, pois a quantidade de campos afeta diretamente a performance e a usabilidade do Ploomes.
- O mapeamento de campos calculados do Sankhya, afeta bruscamente a velocidade de importação dos dados do Sankhya para o Ploomes, pois a consulta no Sankhya se torna mais lenta.

Esse conjunto de padrões de configuração da integração determinam o comportamento da integração na conta Ploomes.

---

### 3.1.6 Configurando os cadastros base

Os cadastros base da integração são as regras de pares de entidades básicas que suportam toda a operação no CRM.

Portanto, configuramos os seguintes pares de entidades Sankhya <> Ploomes:

![Imagem 7: Portanto, configuramos os seguintes pares de entidades Sankhya <> Ploomes:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434586/52aaa62ff3ca2bc7b767d440da92/AD_4nXdapKXmKAniE-rtM8lFHci5j7ZMIuZZpbfXxS1kVKTkDfrnWvMrhCsK1SKqlCAUU5UokfThxZrKih9lpk-e1tiNC8zzBX3C2k7Xmz83Guw5R3Wuehud8m1kH635IwgDhf07_2NKag?expires=1786536000&signature=74389423473f85f9724f7d7a73c352abd08a42ad706d3b5f39755faf17082e28&req=dSUlEs19mYRXX%2FMW3nq%2BgWEYV6ZhadReUhFWVgyVwvp9EmMtTWKw64zg5qaS%0AlGnwICTokZmKMMHRQU3leFbX2Qg%3D%0A)

Em cada seção de pares de entidade para os cadastros base da integração, é necessário configurar os gatilhos, filtros e mapeamento. Conforme exemplo abaixo:

[GIF animado: Imagem 8: Em cada seção de pares de entidade para os cadastros base da integração, é necessário configurar os gatilhos, filtros e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525770281/c6fda0b4148d7f0c2ba1ffc91f91/Configura%C3%A7%C3%A3o_SalvarSecao2.gif?expires=1786536000&signature=76fb104e761c500d15431cd8e5143c20f933ae8807d31cbb105194991e6a6013&req=dSUlE855nYNXWPMW3nq%2BgTqlCvSzeysgX5MKVX6yLZgQt7NTNaWuG57mfHTY%0A5sJeC%2FcGgrzmwmfqpk%2BZQWKY6vY%3D%0A)

Durante a configuração é possível sincronizar metadados do Sankhya. Essa ação é acionável por seção, e permite atualizar os dados de opções pré-cadastradas existentes no Sankhya para criação de filtros de recebimento e também atualiza os campos existentes na entidade do Sankhya integrada.

[GIF animado: Imagem 9: Durante a configuração é possível sincronizar metadados do Sankhya. Essa ação é acionável por seção, e permite…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525772778/0b9a938837db3d7fc132a45d437e/Configura%C3%A7%C3%A3o_SincronizarMetadados.gif?expires=1786536000&signature=85f367c8aac6b4ef19f59eb5aa16b92f45494628add0122bca42affdec19576b&req=dSUlE855n4ZYUfMW3nq%2BgQhELsXfzdUD0VWpey%2BS8X630KeT7f%2BLV%2BJka8s%2B%0Ak4PkloL8vl0jfdDpiZ2yMU6s%2FJo%3D%0A)

Após configurar as seções, o modal informativo existe o texto Configurado nas seções que já foram salvas e Não configurado nas seções ainda não salvas.

![Imagem 10: Após configurar as seções, o modal informativo existe o texto Configurado nas seções que já foram salvas e Não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434602/70ffe05a24a9d905bb82abf47463/AD_4nXe98P3E9Aa2ELhI0Hi4oEQ5tN0Llhk3VhNBnFROWeWXnwnRpCtqF91i0eAqn8vKD_mwzYfJumRm2J7o-AwbxQiJCeyACJSefjraMv8VCoxgcMqWbqHjcEfVEmBN40Y_YtU15hry6w?expires=1786536000&signature=3ce6d8f2ca847818aced1bd52030fa25d6d0af3f20beccc606d7056a08ddda3c&req=dSUlEs19mYdfW%2FMW3nq%2BgTFLwz4UHAKRjXsp55PgUXEB%2BtKdFDNF63noWnnF%0AY0bPEigD6ustMshj1Lv5SdsDe0s%3D%0A)

A seção de cadastros base é extremamente importante, pois impacta diretamente o uso dos cadastros de operação pela integração. Por exemplo: para o sucesso na importação de um Orçamento do Sankhya como Proposta no Ploomes, é necessário que os Produtos, o Parceiro e o Vendedor responsável já estejam integrados no Ploomes.

![Imagem 11: A seção de cadastros base é extremamente importante, pois impacta diretamente o uso dos cadastros de operação pela…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434611/b60ca3f6e3e5d1d79af1eb4a095f/AD_4nXfJHkfYwmrK8KWNbqOvsvM0OzqXJkRmvUPXjxohaM4C_i1CqHaBXKDz-uu5ofdefhNnjGG9R5f3Yp49nm2fa5HzJ04Z85ZjdSEjAiF6IthisHQOLSlm48hCNAbx_07E-MKx4yITqQ?expires=1786536000&signature=5146fc3f688929c2bf0b0850e454a13bc24f9e8082ab55549886334c18e63985&req=dSUlEs19mYdeWPMW3nq%2BgYYUPPQ0QNwtAM5EeFEkhSXZi7A8GHrU%2FYACGzay%0Ae3HKjgPbzsEPiQWtJ%2FgzEBtSx5g%3D%0A)

Após configurar todas as seções de pares de entidades que são a base da integração, é preciso configurar os cadastros de operação.

### 3.1.7 Configurando os cadastros de operação

Os cadastros de operação da integração são as regras de pares de entidades de documentos (Propostas e Vendas no Ploomes) que registram toda a operação comercial no CRM e as TOP’s do Sankhya que serão utilizadas no Ploomes.

Portanto, configuramos os seguintes pares de entidades Sankhya <> Ploomes:

![Imagem 12: Portanto, configuramos os seguintes pares de entidades Sankhya <> Ploomes:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434590/f6d4bc95de1606b1588a2ddded17/AD_4nXf1im-nKPI2RH15VUGen6fHnSr02cB0aNTwVmT5UidV1vjOkcrrAmnvfM4hGtd1snPr4w8A1Dvl3y18uotb0x00H4bEmSPoxQjX83DNKi9dw79J3ghQiVkTUIgI4VugY34H8O383A?expires=1786536000&signature=c3547ac38dfa2af4d86258a1aec571ea12059dae99acdad793b989a7cac2e5bd&req=dSUlEs19mYRWWfMW3nq%2BgVUi%2F5R6fGaJFG0gVbNELYsEt5QU5B5Xg8CYJ85o%0AccI%2FuxEjhX8q9w3yjik%2Fxo%2BQGBc%3D%0A)

#### Configuração de Proposta (Orçamento) e de Venda (Pedido de Venda e Nota de Venda)

Nas seções de Propostas e Vendas, as configurações são as mesmas realizadas para os cadastros base, em que configuramos os gatilhos, filtros e mapeamento dos campos que serão enviados e/ou recebidos entre as entidades.

[GIF animado: Imagem 13: Nas seções de Propostas e Vendas, as configurações são as mesmas realizadas para os cadastros base, em que configuramos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525774481/e346a170409bee1174f4a8fa7220/Configura%C3%A7%C3%A3o_Propostas.gif?expires=1786536000&signature=17c102edb7f7aa3772a5a59de07ea719f00375de8d5f953ff46ddd0d6f07777f&req=dSUlE855mYVXWPMW3nq%2BgZ6ovns%2Bma5Vq5fcqKSnopdUk%2Fekka2zdfi14%2FpT%0A5H9aEpI3zEbAZ6famBjy%2BMr75xo%3D%0A)

Na configuração de Propostas, dado que no Ploomes uma Proposta precisa estar vinculada a um Negócio, é necessário escolher em qual estágio específico e em qual funil que o Negócio gerado automaticamente a partir de Orçamentos do Sankhya sejam salvos. É possível determinar qual funil e estágio do funil em que o Negócio será gerado.

![Imagem 14: Na configuração de Propostas, dado que no Ploomes uma Proposta precisa estar vinculada a um Negócio, é necessário…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434598/177a166f791fe8bb0fb50fa7a318/AD_4nXdgRa_eRqknMKA6Dn5r-GPlXdRdtpg91PdPRcESTLc1nnFouXRchhUxyEYyhgicGfi8W2hm12TMe8y5vYHJWnMpdIIqEKCDWOKYEFo_4o7OJIAH6IzwwBcpAcDrIqIwWZrUmUpV?expires=1786536000&signature=faa50ccde3b728c882002e7a3d4fa56662207145cf7b6bc19e1ad2f9cf1dbaa2&req=dSUlEs19mYRWUfMW3nq%2BgfoRsc1ygZcgE5jP4GVkQXvAF10OoipBC3HJacpV%0AV568IvroxTvWC9AJEHzAQhFLjeA%3D%0A)

Na configuração de Vendas, dado que no Ploomes é opcional o vínculo de uma venda com um Negócio, é possível escolher se os Pedidos de Venda e/ou Notas de Venda recebidos do Sankhya no Ploomes serão vinculados a um Negócio gerado automaticamente ou não. Se sim, é possível determinar qual funil e estágio do funil em que o Negócio será gerado.

![Imagem 15: Na configuração de Vendas, dado que no Ploomes é opcional o vínculo de uma venda com um Negócio, é possível escolher se…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434610/1d1c6843e0af055a065aa11073d4/AD_4nXdUZpQZzsqTKIDmy1lk7gTVdad_OXR5E2ldRsAJKbhhjpNo2-jyNpmlLb6gL-IR86G4TjLn8olBDOdo3C8KkdLg8TEKuKn2JWmk7f05ftbvORs78gLH1vwz2ldIdld2e1gJMu7w?expires=1786536000&signature=45bef30386a52f0ec6f7805d661965589b2c58176d2734e0c1b215b36e00b1d8&req=dSUlEs19mYdeWfMW3nq%2BgVAenbZxz2vZ7oWwaX2jdlRdTn3Ish1skAI83kJW%0AI%2B8wKNmFDVzmOMSADbDVrI3DYbk%3D%0A)

Nos mapeamentos das entidades de Orçamento e Pedido de Venda/Nota de Venda existem regras específicas de mapeamento que influenciam na integração e precisam ser configuradas.

#### Configuração de Tipos de Operação (TOP)

Na seção de configuração de TOP é preciso determinar a relação de TOP’s atribuídas para cada tipo de documento do Sankhya (Proposta, Pedido de Venda e Nota de Venda) que serão utilizadas no Ploomes como opção para seleção e também determinar qual o modelo de documento deve ser utilizado para cada TOP.

![Imagem 16: Na seção de configuração de TOP é preciso determinar a relação de TOP’s atribuídas para cada tipo de documento do…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434635/440fcabdc16007bffecbd25492ab/AD_4nXddgRzVsQOoqkmnXipJfIcHmWGj4s4wH5diEBVq8wCanVlNSuJFTv6aOZNcHkQZ-fNjhGHTyxwp7ukCyILiWtR1seKtLubYT-t3eh10_nka5Rm8EWXV5xmXNkH63wIbSFo8sfvpbA?expires=1786536000&signature=6d7d57e226efd0cfe97f349b8dd79ff3a48270eada2c7e7028de542c148438e6&req=dSUlEs19mYdcXPMW3nq%2BgVLk05b%2Fj%2FKuDWZYgIGHy3XjbRk5XjDG9c6Tt25I%0AtESAxRHhwywf61ZiA9794Bg1Nz4%3D%0A)

Na seção de relacionamento de TOP com o tipo de documento, é possível selecionar mais de uma TOP por tipo de documento.

![Imagem 17: Na seção de relacionamento de TOP com o tipo de documento, é possível selecionar mais de uma TOP por tipo de documento.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434601/0e6c8a528621aea9a336b93f5378/AD_4nXftXTbCdOP7pgsmRTViIaP05sfS0qLgWTpU3brY8iCHbo8o_TPw04ICyJvyA2BipJGQJNd7gz659-W6bUTXjRQ1TpMNkpXi0xC2XR2JDbNzakTxgD0jkQQrkBHezHg3ALiLgbppgQ?expires=1786536000&signature=394251bc5b059e53c90585ccbd13ca5d344e052bc200b98beed343f5b1b5dc1b&req=dSUlEs19mYdfWPMW3nq%2BgYmoG2wC6rvKjAZhQ9g0z%2BUet2N8rlAOAaiJwEW9%0AfXX40tki0J6ZqiNFsIZb4g%2Fd7zo%3D%0A)

Na configuração de TOP’s por entidade são listadas as TOP’s com base no Tipo de Movimento configurado no Sankhya. Para Orçamentos e Pedidos de Venda são listadas todas as TOP’s ativas com exceção das que possuem o Tipo de Movimento (TIPMOV) = “V”. As TOP’s de Tipo de Movimento = “V” só são exibidas como opção para as Notas de Venda.

Somente serão habilitadas para configuração de TOP’s os tipos de documentos configurados em alguma via de ação da integração. Ou seja, caso não estejam ativos gatilhos de Pedido de Venda (exportação ou importação), não será habilitada a configuração de relacionamento de TOP com o tipo de documento Sankhya.

Essa definição do relacionamento da TOP com os tipos de documento, determina que ao importar um documento do Sankhya, se o documento foi gerado com uma TOP relacionada com Proposta do Ploomes, será importada como Proposta, assim como para os demais documentos (Pedido de Venda e Nota de Venda).

Ao gerar um documento no Ploomes, Proposta ou Venda, somente estarão disponíveis para seleção as TOP’s configuradas para aquele tipo de documento do Ploomes. Se estiver gerando uma Proposta, serão listadas as TOP’s de Orçamento, e se estiver gerando uma Venda, serão listadas as TOP’s de Pedido de Venda. Como não é possível exportar Notas de Venda do Ploomes para o Sankhya, não são listadas as TOP’s de Notas de Venda ao gerar uma Venda no Ploomes.

Após determinar os relacionamentos de TOP e tipo de documento Sankhya, é preciso realizar o mapeamento dessas TOP’s selecionadas com os Modelos de Documento do Ploomes a serem utilizados.

![Imagem 18: Após determinar os relacionamentos de TOP e tipo de documento Sankhya, é preciso realizar o mapeamento dessas TOP’s…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434596/b040a89dc5919391822563d01bce/AD_4nXcN2lg4Lh1eOGUlzfTLWaTno6wU5JkNsY95H_Tq2Y0aM43zIjdirQiyPWNump18TE6JwPE6BFbdG2-LU43Qk9opoogXgR4W_dknB86kBZe6bkPLvgLiQxd-C0IMhoIxLRXAYUGKqw?expires=1786536000&signature=ef711558a7a3db55d64e874bf7bc3b15ad5bca5f2ab54efcf3fc28ca84c9d0f4&req=dSUlEs19mYRWX%2FMW3nq%2BgbeNCagZLqTDjrmlP03GyJ0rJBfd11%2FrOgbjPnkC%0Ar50%2BkNhLbPSbVIuhyH90uU0yxio%3D%0A)

Com a conclusão da configuração e salvamento das seções dos pares de entidade de Proposta e Venda e também dos Tipos de Operação para a integração, os cadastros de operação estão prontos.

![Imagem 19: Com a conclusão da configuração e salvamento das seções dos pares de entidade de Proposta e Venda e também dos Tipos de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434617/9518649ecc972a40c13fdfef9fd4/AD_4nXdBJdeby-Ro6c97Rct6g8oVomVkE24QvXv7oZCWzpeBT-Oopjcd-XaylDVCKNa7rOrF7Y4_d4vRYt_-Dj_NH_U3VgQ6277EWxqv6905odYKB8J4E62XjKjqXPl2_9Pb-245BtRbeg?expires=1786536000&signature=0a1f7cd5b4a4197d76e7b8503abf5fba52f89be405ef7f4dd28d33658f586b1a&req=dSUlEs19mYdeXvMW3nq%2BgTElVz%2BBUxqmgsfG2j2iJdmUYCbHUtc%2FJR2wUyls%0Az2aIExH%2FXNp64d0PBJLKYpgPiXo%3D%0A)

### 3.1.8 Configurando as consultas em tempo real

A integração realiza algumas consultas em tempo real ao Sankhya via API e, portanto, é necessária a configuração dessas consultas.

Por padrão, a integração realiza a pré-configuração automaticamente ao habilitar a integração.

Para que as consultas em tempo real funcionem, é necessária a criação de campos do tipo desenvolvedor no Ploomes. Esses campos possuem fórmulas que são criadas automaticamente pela integração. Essas fórmulas indicam quais campos serão enviados no payload de requisição da consulta em tempo real ao Sankhya e quais campos receberão os retornos dessa consulta.

Ao habilitar a integração, os mapeamentos de campos de consulta em tempo real são criados automaticamente com suas respectivas fórmulas. Não é possível desabilitar os mapeamentos de consulta em tempo real. Por padrão, como se trata de um mapeamento de consulta ao Sankhya, a via de integração desses campos é definida por padrão como Sankhya > Ploomes e não pode ser alterada.

A configuração das consultas em tempo real estão dentro das seções de Proposta e Venda, pois as consultas são referentes a essas entidades.

Portanto, são configuradas consultas pertinentes para a geração de Propostas e Vendas no Ploomes. Essas consultas são detalhadas abaixo:

#### Proposta

Para as consultas na tela de geração de Propostas, são configurados os seguintes campos de consulta a dados da Proposta:

- Detalhes financeiros do cliente (Sankhya): este campo retorna os dados de limites de crédito e saldos financeiros do Clientes selecionado na Proposta e integrado a um Parceiro no Sankhya em um campo multilinha.
- Detalhes restrições da TOP (Sankhya): este campo retorna os dados de restrições/exceções da TOP selecionada na configuração da integração em um campo multilinha.

![Imagem 20: Detalhes restrições da TOP (Sankhya): este campo retorna os dados de restrições/exceções da TOP selecionada na…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434591/f8039fb6522865d534a8d7ae4c0f/AD_4nXe7LbgDSF-Yw7s_55pYz4HbumddkzFitxWXsnCngRN0WKHpizIH_8Rvpyrb5Ye43h7n2yvFUw_OA6GMOHE-8E1gWKkZwOlYAqyffiLA3quPkKmvrZY0Nv0eWDdVb25tD3NDO3YpLQ?expires=1786536000&signature=a1ae611b80442b1cd31bb9dfa5e01442f95823434feef04c226ceb514b203fda&req=dSUlEs19mYRWWPMW3nq%2BgT8BaFDdGb%2BbMG7hDBwzIKmWwvDZqBWfuye1ENDj%0AZkZyRw9NrPKRQ9KKt7%2FyyIdytug%3D%0A)

#### Produto da Proposta

Para as consultas na tela de geração de Propostas, são configurados os seguintes campos de consulta a dados de Produto da Proposta:

- Detalhes de estoque (Sankhya): este campo recebe alguns dados de estoque do Produto/Serviço do Sankhya em um campo multilinha que pode ser visualizado como tabela.
- Valor unitário (Sankhya): este campo recebe o valor unitário do respectivo Produto/Serviço integrado do Sankhya conforme a precificação de sua tabela de preço.
- Produto integrado (Sankhya): este campo recebe um valor de True/False para determinar se um Produto da Proposta está integrado a um Produto/Serviço do Sankhya.

![Imagem 21: Produto integrado (Sankhya): este campo recebe um valor de True/False para determinar se um Produto da Proposta está…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434588/432549818a072a4fc585f0518c32/AD_4nXfZMYMfU-V9WFzldZ7RWXRP0FHf8q0mD8zpiLDLRhuIlmiHKeeoudSx1fj_QXz1WPjIgqH7DhBPf6dOevchHPqrr2oCrErlk3mufFQU6vmGIFBsYt228TUO6dDvsFWNkXCnNw0fdw?expires=1786536000&signature=0d9ccc0b1952b439a9eb30c5e8b2a66867c4d5f07054548f19affb4212f34b4d&req=dSUlEs19mYRXUfMW3nq%2BgbYMZ1VklfOKAQ6GwLfmoya9fVyIvqa0R%2FcQd9Kx%0AhNEgizm2P9WGRPCrVs3tDMMuMnI%3D%0A)

E também, especificamente para a consulta de impostos de Produto da Proposta, são configurados os seguintes dados:

- ICMS Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto ICMS.
- ICMS Valor (Sankhya): este campo recebe o valor do imposto ICMS.
- ICMS Base (Sankhya): este campo recebe o valor base do imposto ICMS.
- IPI Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto IPI.
- IPI Valor (Sankhya): este campo recebe o valor do imposto IPI.
- IPI Base (Sankhya): este campo recebe o valor base do imposto IPI.
- ISS Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto ISS.
- ISS Valor (Sankhya): este campo recebe o valor do imposto ISS.
- ISS Base (Sankhya): este campo recebe o valor base do imposto ISS.
- ST Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto ST.
- ST Valor (Sankhya): este campo recebe o valor do imposto ST.
- ST Base (Sankhya): este campo recebe o valor base do imposto ST.
- FCP Valor (Sankhya): este campo recebe o valor do imposto FCP.
- DIFAL Valor UF Remetente (Sankhya): este campo recebe o valor do imposto DIFAL UF Remetente.
- DIFAL Valor UF Destino (Sankhya): este campo recebe o valor do imposto DIFAL UF Destino.

![Imagem 22: DIFAL Valor UF Destino (Sankhya): este campo recebe o valor do imposto DIFAL UF Destino.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434604/59756421acf44d9c3f0e54d3b782/AD_4nXdqtXgu7CxaoHR6bCy7mGAwnKn6D_facRLIrW0G61n-REBXMdktSF5ZdscW-JFjY5WqcE29BOl9amb-vkfgSOE0xxXBhL9T-51CF1lHIZsmyr0hgKuZYR3XS--DkcgE4GOY2ZK4?expires=1786536000&signature=b9215dfd258da8ce4cf61921c9672b5862d0692388df753a09e854f985d08e14&req=dSUlEs19mYdfXfMW3nq%2BgWSGuVpNheS3Y%2FHa%2FSc9EUaGB%2FXh%2FqR6MRqwzu3z%0Ab%2FyGM2Zgwvyi%2B%2FAEPMuj6d0qYWg%3D%0A)

#### Venda

Para as consultas na tela de geração de Vendas, análogo à seção de Propostas, são configurados os seguintes campos de consulta a dados da Proposta:

- Detalhes financeiros do cliente (Sankhya): este campo retorna os dados de limites de crédito e saldos financeiros do Clientes selecionado na Venda e integrado a um Parceiro no Sankhya em um campo multilinha.
- Detalhes restrições da TOP (Sankhya): este campo retorna os dados de restrições/exceções da TOP selecionada na configuração da integração em um campo multilinha.

![Imagem 23: Detalhes restrições da TOP (Sankhya): este campo retorna os dados de restrições/exceções da TOP selecionada na…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434594/1214dd7a869423ebe3ce3062dd22/AD_4nXfyZVF-HGJN_DhAy206M1Ef2fHyLp09Xq3HPP-7khM_3NzPxVwdP2mSASeetYekXw9wLFn1djOtEtZZFjPWSmpiCGRzjgrs4fL7EIXsiS8Er8iPLm30jOS8gt8yyteKbFqjJYyU8w?expires=1786536000&signature=25cf0c3aaef64704aa4873e2314e14fd5e905e9a6c2775f2fb51904fad869d7b&req=dSUlEs19mYRWXfMW3nq%2Bgb8PWJbiXPX%2BWkyoTBl5vunmsalU4gPQBuZIA%2Bmj%0A9JidOcK5Ql3IfS5w%2FZTxi%2FGYjrY%3D%0A)

#### Produto da Venda

Para as consultas na tela de geração de Venda, análogo à seção de Propostas, são configurados os seguintes campos de consulta a dados de Produto da Venda:

- Detalhes de estoque (Sankhya): este campo recebe alguns dados de estoque do Produto/Serviço do Sankhya em um campo multilinha que pode ser visualizado como tabela.
- Valor unitário (Sankhya): este campo recebe o valor unitário do respectivo Produto/Serviço integrado do Sankhya conforme a precificação de sua tabela de preço.
- Produto integrado (Sankhya): este campo recebe um valor de True/False para determinar se um Produto da Venda está integrado a um Produto/Serviço do Sankhya.

![Imagem 24: Produto integrado (Sankhya): este campo recebe um valor de True/False para determinar se um Produto da Venda está…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434597/26d9742ed8c1fc51079c1753a67f/AD_4nXcOTBB5-GmtAh-sH8RHwMK-PIvOhesgN4hAj9HAUwzIfstu6oZBwKANrqy7RS8g-wB3rFcHzRzbI9LRX-KerJOb6stkYpCU4rdTkCsJqF93SGp1GKFrf3VRrKgeWc_jjYL_c5Zq?expires=1786536000&signature=1b6e9263a238f32cca956fb44e7578ca77cb9dd55604d895895d0e38dd7eea3d&req=dSUlEs19mYRWXvMW3nq%2Bgblv9d%2BO4DEGmH3D7TDA6uVNjBfq8DKND9pE5zEL%0Ar%2F2%2Bq7uAeQDRujerKLaqVdZXBG0%3D%0A)

E também, especificamente para a consulta de impostos de Produto da Venda, são configurados os seguintes dados:

- ICMS Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto ICMS.
- ICMS Valor (Sankhya): este campo recebe o valor do imposto ICMS.
- ICMS Base (Sankhya): este campo recebe o valor base do imposto ICMS.
- IPI Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto IPI.
- IPI Valor (Sankhya): este campo recebe o valor do imposto IPI.
- IPI Base (Sankhya): este campo recebe o valor base do imposto IPI.
- ISS Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto ISS.
- ISS Valor (Sankhya): este campo recebe o valor do imposto ISS.
- ISS Base (Sankhya): este campo recebe o valor base do imposto ISS.
- ST Alíquota (Sankhya): este campo recebe o valor da alíquota do imposto ST.
- ST Valor (Sankhya): este campo recebe o valor do imposto ST.
- ST Base (Sankhya): este campo recebe o valor base do imposto ST.
- FCP Valor (Sankhya): este campo recebe o valor do imposto FCP.
- DIFAL Valor UF Remetente (Sankhya): este campo recebe o valor do imposto DIFAL UF Remetente.
- DIFAL Valor UF Destino (Sankhya): este campo recebe o valor do imposto DIFAL UF Destino.

![Imagem 25: DIFAL Valor UF Destino (Sankhya): este campo recebe o valor do imposto DIFAL UF Destino.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434595/322636884148c601c56a6c417676/AD_4nXclFYktrg_a52xMhEIl2lXqIrUg92bm7tX3qsfSRAMTHTKS7VeNI4EAs-nWklkH66SYYk2LqHfxr6RNT4KXYNvaxjpYp5y0fhUSdCyMt-ivXGvhaHmzihvx0Sa_t51BG3nttFKteA?expires=1786536000&signature=b6a55cdb359aa833f7c10bea78d699aa58e6c059ee0424686a10a4ab0d441ccd&req=dSUlEs19mYRWXPMW3nq%2BgRZFpmghmD%2FizS1w9aA28N74cyMXwPAxixyl%2FDm6%0AfQOlQ6JrTwcaGKFlTLITJoUdSgM%3D%0A)

---

**# Observações importantes sobre consultas em tempo real**

- As consultas são pré-configuradas pela integração, preparando o payload de requisição e os valores recebidos nos campos do Ploomes, no entanto, os retornos dependem totalmente das configurações do Sankhya (preço, imposto, estoque, etc), da disponibilidade do Gateway, do servidor Sankhya e dos limites da API do Sankhya.
- As consultas precisam ser engatilhadas com base no preenchimento dos campos mínimos requisitados no Sankhya. Caso algum campo não esteja preenchido, a consulta poderá não ter sucesso. (Exemplo: consultar imposto sem informar o valor total do produto)
- As consultas de impostos dependem diretamente das regras e parâmetros fiscais configurados no Sankhya. Alguns casos de consultas de impostos podem não funcionar na consulta via API, portanto é preciso checar no Sankhya esses parâmetros.

---

## 3.2 Alterações de configuração após a primeira ativação

Com a integração ativa na conta Ploomes, é possível realizar 3 operações de alteração na configuração. Essas alterações afetam diretamente toda a conta e uso da integração, assim como a configuração.

As alterações de configuração possíveis são as seguintes:

### 3.2.1 Editando a integração

Após a ativação da integração na conta, ao abrir a tela de configuração da integração Sankhya no Ploomes, será exibida a tela de configuração com a tela de consulta das seções de configuração cadastradas.

Nesta tela, sem utilizar um dos botões de ação não é possível realizar alterações, apenas consulta das seções configuradas.

No entanto, estarão disponíveis dois botões de ação:

- **Desativar integração:** este botão desativa a integração na conta
- **Editar integração:** este botão inicia uma edição da integração

![Imagem 26: Editar integração: este botão inicia uma edição da integração](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434606/5a17d0f34ae086340e87ff37b424/AD_4nXf5d4fD_1Gjf3KPljJcxLdRkSjKlxeqCsDd_vCYf4msqiydgCr-4bRQhNb_R-Z7x78t1GDrVZeSOLdEcpmNN0iq6N-PxNZF0Dbo9IrVAFbUi7X6c4JLGL0EkyAL-uST2fJHyv0qpQ?expires=1786536000&signature=846292083603b520171dcd57b1105c2bf87f31d555a17615975e7ee9154cdccc&req=dSUlEs19mYdfX%2FMW3nq%2BgTyHQ9K%2FAqOPkX0XWR2ny1rosRjbvaZw7DYB2mgj%0AUX%2Fm68mi0Lngkj20TWYsVCtDUX4%3D%0A)

Para iniciar uma edição da integração, é preciso selecionar o botão “Editar integração”.

![Imagem 27: Para iniciar uma edição da integração, é preciso selecionar o botão “Editar integração”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434619/6495c9caab483c8828467e2980bb/AD_4nXdPPjyFvPJbIKXXXcJrqEX3VeG0VuB0VTZ-mKvLIC5Dg65tAAURY1VuiJAZGzqvpRS913pouxFblAdIIycEtk1a7IR8qpSn9RQlZbloYFnB5d8Y8cmynqegdrxadbcJvf7UrFHNMA?expires=1786536000&signature=5e9ad1195c53ed7cce2518dc79edc6f09efd856d6b126aa98efd1b0f7ffbd70e&req=dSUlEs19mYdeUPMW3nq%2BgS5%2BHa31%2FLpNQPyKDK%2BRbvnsTMjCx8TcCpuOom52%0AhVKriFEMOWaRKXN6vCzs1Rckddc%3D%0A)

Uma vez que o botão seja acionado, será carregada a tela para o modo de edição da integração, então, após o carregamento a tela de configuração será exibida como no exemplo abaixo, contendo os botões de:

- **Desativar integração:** este botão desativa a integração na conta
- **Descartar edições:** este botão descarta as edições realizadas na configuração que não foram aplicadas ainda e encerra a edição da integração
- **Aplicar edições:** este botão aplica as edições realizadas na configuração da integração

![Imagem 28: Aplicar edições: este botão aplica as edições realizadas na configuração da integração](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434648/a3843659bf70718493f4add1c764/AD_4nXeym08UItu2Ia145NJ9Hr2ZD-xfbd6aT5wrcgKxG0xIHku0ST9XBACwxsgJ-b2nNhjwN-DaEZhppXsrHGlKcK2SniRsDtxxF6HTXTJPgnmgt7hhzikaw5PY3DmmGmP2z9w0Sofz?expires=1786536000&signature=6dc52546b3a2267271fc359fdd106f93f7ce43de282f565808474fa99dd4af54&req=dSUlEs19mYdbUfMW3nq%2BgTNLoxTJuIbJNQrIVPig0eA27skAi836ryV6Buge%0AL7uRT9Hcmwax1At2Ydg3WZm3U6o%3D%0A)

Caso a edição tenha sido iniciada equivocadamente, ou sem querer ou simplesmente exista uma desistência da edição, a qualquer momento é possível acionar o botão “Descartar edições”, assim todas as edições serão ignoradas e excluídas e a integração seguirá operando normalmente com as informações da configuração anterior.

![Imagem 29: Caso a edição tenha sido iniciada equivocadamente, ou sem querer ou simplesmente exista uma desistência da edição, a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434620/5d9e1dc033ff6342262073c6688b/AD_4nXcefkbUhHiX-Z922fYkW9h5iLUF3pNBPGxTsHD1LkWARDLKDtRyHwpM2yUOwrKeExZU5QhK3YhxsuQYA1njaVIHD60J-bKVQEYwUQYSWPPdiIQF5F9HPVDsMVuSbufGL729VZyi_g?expires=1786536000&signature=1a3549cb51428fd4123ac76ce0c24450663bae607edb1dd28a07eb46e9f1b299&req=dSUlEs19mYddWfMW3nq%2BgQiidur2XKWkw4K4KN%2FLTYSuu0iC7IZhGHDrKPPG%0AmzrL8lVUrwbfAbOMO5eEY463jb8%3D%0A)

Durante a edição da integração é possível realizar qualquer configuração possível na configuração inicial da integração:

- Ativar ou desativar gatilhos de envio e/ou recebimento para qualquer entidade integrada.
- Incluir ou remover filtros de envio e/ou recebimento para qualquer entidade integrada.
- Incluir ou remover campos no mapeamento para qualquer entidade integrada.

Todas as **alterações de configuração da integração** possíveis de realização **não impactam nos dados retroativos**, isto significa que, por exemplo:

- Caso um gatilho de recebimento para criação de Propostas seja ativo e antes estava desatualizado, apenas as novas Propostas recebidas serão criadas e não serão criadas Propostas do passado.
- Caso um filtro de envio para criação de Cliente seja ativo e antes não existisse, apenas os novos cadastros criados no Ploomes seguirão essa regra do filtro criado.
- Caso um ou mais campos sejam incluídos no mapeamento de uma entidade, os cadastros existentes no Ploomes não serão preenchidos automaticamente. Apenas após as novas importações com o novo mapeamento ativo terão os cadastros recebidos com os dados novos do mapeamento.
- Caso um ou mais campos sejam removidos no mapeamento de uma entidade, os cadastros existentes no Ploomes não perderão seus dados preenchidos anteriormente. Apenas as novas importações com o novo mapeamento ativo terão os cadastros recebidos sem os dados dos campos removidos no novo mapeamento.
- Os cadastros que estiverem na fila de processamento da integração, não sofrem os impactos de edições da integração. Apenas os cadastros importados/exportados após a ativação da edição da integração seguirão os padrões na integração editada.

Ao editar a integração, é importante validar se algum campo mapeado do Ploomes ou do Sankhya, ou algum campo utilizado em algum filtro da integração, ou alguma opção pré-cadastrada utilizada em algum filtro da integração, ou alguma TOP do Sankhya ou Modelo de Documento do Ploomes tenham sido deletados ou editados. Caso ocorra alguma alteração desse tipo, a edição da integração não será aplicada e será necessário corrigir os erros identificados.

Para auxiliar na validação, é possível utilizar o botão de Sincronizar disponível em cada seção da configuração. Assim são trazidas os campos e opções pré-cadastradas existentes do Sankhya no momento da sincronização, evitando algum conflito por informação deletada ou alterada no Sankhya.

![Imagem 30: Para auxiliar na validação, é possível utilizar o botão de Sincronizar disponível em cada seção da configuração. Assim…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434631/4abfc917139454e23730d65d2b2d/AD_4nXcu3Y_YV4DKtjYwMucwPuWEkcSqM9pdxSb7LoAENx2h2RBGNRt9jEUY5Dd2gEHcn2FEltuwl2t-PykdyuRoyrSrlsquRjnqKyQr7xLEI50tLMlhvnRZEuqGIZcRhxfoaVladtKlbQ?expires=1786536000&signature=651b5b23daf354a5d8595ba4d18aa169c1b9e0ad2703cbebcd7cf49b44984221&req=dSUlEs19mYdcWPMW3nq%2Bgaggc2cT95iiQsaeh57Ik1zA0AlUtzKCLnoqRd90%0ASEkccvAtQg5IlSfTY8d0oLfIJQE%3D%0A)

Ao acionar o botão de sincronizar, aparecerá uma mensagem para confirmação.

![Imagem 31: Ao acionar o botão de sincronizar, aparecerá uma mensagem para confirmação.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434599/df9d086a396a2bbd36c1aafb30be/AD_4nXdumtFRR6-Ang35h0g-DPZzcj1Le9Cyc8wf9EP3FJ-NfLaOfICOYpC4dp4MnZydCcPjyyCIhDSOQbVm-PoRArDcRi7fwYdQqKulW0KqV6fZwh_hEIsCMKWd4SbnaoE42qVcVI0j?expires=1786536000&signature=f0f70c3db1a3f7cd86ab7db0a45f063158d99f2d78db305212e22d3c718b1b7c&req=dSUlEs19mYRWUPMW3nq%2BgZYHG4UPZdpOFtKnISnrfIpr21sZKZ6Z5WpXa7QU%0AvB%2BnP%2BnqudvTtHZjJ4T2QAMdm%2BM%3D%0A)

Após a sincronização que leva alguns segundos, será exibido um modal com o resultado da sincronização.

![Imagem 32: Após a sincronização que leva alguns segundos, será exibido um modal com o resultado da sincronização.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434603/834b7a30a7981d689773bd3aff1e/AD_4nXeN2Fm4Cp9bqCEdPs7fCDqp-ccJCVhOjmrm_fp0KRigY-G8lKVNj47SAPoRMZ8jjgiSzFbBxkLu8pwMSF28MZ_8j0Ti2vKJarqLdTwuQdkkpJ-TcwkEDmbjJcebuCGPoUGPL0EROw?expires=1786536000&signature=60496edd7721b2ab2b408d14c3d61f459e28fffd86756c44297ebbe18a1bbfa3&req=dSUlEs19mYdfWvMW3nq%2BgYJl9EUMxo9D%2Fkh5BOLgR%2BJJNksecAmlP6d0XSLH%0A9l5cxUC8%2FcPftOa6sBTTETtzxBY%3D%0A)

Caso todos os cadastros estejam sem erros é necessário salvar as edições realizadas em cada seção através do botão “Salvar edições”.

![Imagem 33: Caso todos os cadastros estejam sem erros é necessário salvar as edições realizadas em cada seção através do botão…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434658/b8069d362b404763f8cc14858bf3/AD_4nXehm-LZjcS74koF5etCl6zh5FL2zIoQmvO9rujf7ijucHbWNLkNwnGU4BwysEWht569YkJWGhEMtsS0DiV0iyTdkMfKY1ZUkhPL9jgJBsQ8m15ZFCrFAJQ6xWixVVWcXGPR2eSO?expires=1786536000&signature=8e18c31d018224b4a632551d19772431d405e365ef5991eebb92182cdf9d2886&req=dSUlEs19mYdaUfMW3nq%2BgQCupx%2F09L%2FXoXEzTf%2FjDnh%2FGKX9E4wh0zOdwnzA%0A3gL%2B5fNoNolTCxQ%2FyZFsbvZja4I%3D%0A)

Após salvar as edições em todas as seções editadas, é possível aplicar as edições da integração. Importante: é necessário salvar as edições em todas as seções editadas, caso contrário não será possível aplicar a edição da configuração da integração.

Ao acionar o botão aplicar edições, será aberta uma nova janela com informações importantes sobre a alteração da integração e seu impacto. Nesta janela é possível cancelar a ação pelo botão “Cancelar” ou confirmar pelo botão “Aplicar edições”.

![Imagem 34: Ao acionar o botão aplicar edições, será aberta uma nova janela com informações importantes sobre a alteração da…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2224013197/e99ca344aff6beadb0390b9d7890/IntegracaoSankhya-ModalParametroKeepFormule.png?expires=1786536000&signature=e1367c41b7f7ed7cb5a6c76e2f358a7ae0a7eae686513280ffd83887f8bfc46b&req=diIlEsl%2FnoBWXvMW3nq%2BgeiXyGybUkLiXriabw3gntCWiAMhymnNj7MIatj6%0ARJGBOKRZb%2BGwEGWeosts%2BP53cs8%3D%0A)

Será exibida uma caixa de seleção para `Não atualizar as fórmulas dos campos ao aplicar edições`.

- **Caso a opção seja marcada**, a integração **não irá resetar as fórmulas** de campos utilizados pela integração para o padrão da integração, preservando assim as eventuais edições e customizações realizadas.
- **Caso a opção NÃO seja marcada**, a integração **irá resetar** as fórmulas de campos utilizados pela integração para o padrão da integração, fazendo com que eventuais edições em fórmulas sejam descartadas.

Após aplicar as edições, então a integração seguirá a etapa de adequação dos cadastros no Ploomes:

- **Compatibilização das opções pré-cadastradas entre campos:** as opções pré-cadastradas existentes em campos do Ploomes são compatibilizadas com as opções pré-cadastradas dos respectivos campos mapeados do Sankhya.
  Isto é:

  - (1) opções pré-cadastradas que foram criadas no Sankhya após a última compatibilização da integração e que não existiam no Ploomes são criadas no Ploomes;
  - (2) opções pré-cadastradas que não existem mais no Sankhya e que ainda existem no Ploomes serão deletadas do Ploomes;
  - (3) opções pré-cadastradas que existem no Ploomes e que existem com o mesmo código e descrição no Sankhya serão mantidas sem alterações.

![Imagem 35: (3) opções pré-cadastradas que existem no Ploomes e que existem com o mesmo código e descrição no Sankhya serão…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434621/bca5242e1e35f838b0c061d4a4a6/AD_4nXdrMRfcwDA6NNjLKATWzIXPwYQOEgNwZfUGF-mkgNpwQg1d8OzEYUUzuB9vJ0IcQS0ucLOifLNi7lfFoZi94PH9mQdwGdCwXQrmS_HTfj4AfV9ttabwuMO_OjyMlbdMCI-NYmHD?expires=1786536000&signature=58ff0f656387a0afd9ee6c3de7db1e5b6930b83b6b3bd82c856e7bd6e559ab21&req=dSUlEs19mYddWPMW3nq%2BgXRPMCGHjvZ7SJFYbfWnpmJ1dENJF8%2FXUOgU0zL5%0AD9VMEaK%2FYxUd%2F0iAHRffwAVGIR0%3D%0A)

Após essas etapas serem processadas pela integração, a edição da integração estará aplicada e passará a valer para as novas edições e criações de cadastros no Ploomes e/ou Sankhya configuradas.

Com a integração ativa na conta após a aplicação de edição da configuração, o processo de configuração está concluído e a conta Ploomes pode ser utilizada integrada ao Sankhya normalmente.

---

**# Observações importantes sobre a edição da integração**

- A edição não realiza carga de dados após a sua aplicação. Apenas impacta no comportamento da integração após a sua ativação de fato na configuração da integração.
- Enquanto uma conta Ploomes estiver com a integração em edição, é possível utilizar a conta normalmente sem impactos, pois o comportamento da integração será o da configuração vigente. Somente após a aplicação de uma edição e após o processamento dos itens que estavam na fila da última versão da integração que a nova versão da configuração da integração passará a estar vigente.
- Quando a edição da integração está em andamento, é importante observar que os gatilhos, campos mapeados e filtros efetivamente ativos na conta não necessariamente serão os gatilhos, campos mapeados e filtros que estão sendo exibidos na tela de configuração.

---

### 3.2.2 Desativando a integração

Na tela de configuração da integração é possível acionar o botão de desativar a integração.

---

**Observação importante sobre a desativação da integração**

- Essa ação é extremamente arriscada e se acionada é irreversível.

---

A desativação da integração significa que uma conta Ploomes não estará mais integrada ao Sankhya e não fará exportações, importações nem consultas em tempo real ao Sankhya. Os cadastros existentes no Ploomes e no Sankhya se manterão normalmente com suas informações, no entanto a vinculação pela integração não existirá mais.

![Imagem 36: A desativação da integração significa que uma conta Ploomes não estará mais integrada ao Sankhya e não fará…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434605/cf839d6c734ce70d89456e832e27/AD_4nXc13RJN1dNyMkz__Uh1vTJOdtzB_5xqiDjw9sxIH_le1EQW3zFDoB6QCUvOi5bBNdu2N5KymMhGrZj4WO48Kg_fMoACOXgvVz8P6cbT95tZhJGA7AzvdBIK_cOau-Uc87p_rtXV?expires=1786536000&signature=2fd10f68ad5c1c2064c913c047fbf62303b5e0e347627e3c186f6eac78eafd9e&req=dSUlEs19mYdfXPMW3nq%2BgeSmxleMAbBsqFNEw1RXiuxEclIn1vqcUzmsTOuC%0A3igX2qCAMq54ha8TYYwyh7gbTc0%3D%0A)

Ao acionar o botão de “Desativar a integração na tela de configuração, será exibida ainda uma nova janela para confirmação da ação.

![Imagem 37: Ao acionar o botão de “Desativar a integração na tela de configuração, será exibida ainda uma nova janela para…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434613/4c28b759d0f599d98a2a1cc50d56/AD_4nXc-_DWzw5J1fj9TRv3vn1L_cFF7McP2e8nYOi8fXX3_d5wUOFEhdqRRg-FbzEkFEPrHW1NqrlnTb8rN1lMmOw_tFGaJpS5nwWgkpEXW6fNtuMghX9Ps5GLWysn-ecIH3B1nx2sR9A?expires=1786536000&signature=f5d696f970a1d59ac20f1fdee8186a791a0eddd10a0556963399d91175415d03&req=dSUlEs19mYdeWvMW3nq%2BgWRTZLZzkvYNHQNnH%2BE%2BRV7rlxxfW3dhsCASBFWS%0A2AAW%2BkQkK3SsRfmzqjhvybCLZfk%3D%0A)

Portanto, uma vez que a desativação é iniciada, são executadas as seguintes ações:

- Os webhooks do Ploomes e rotinas de consulta do Sankhya são desativados e não é possível mais enviar ou receber criações ou edições de cadastros.
- Os cadastros criados no Ploomes continuam existindo e com as informações que possuíam, seja em campos nativos, dinâmicos ou dinâmicos criados pela integração.
- Os campos criados com fórmulas para consultas em tempo real ao Sankhya continuam existindo com as fórmulas, mas as consultas não funcionam mais.
- Os ícones que indicam quais campos foram utilizados no mapeamento da integração deixam de aparecer.
- Os módulos de status da integração deixam de existir.
- Os registros de integração são apagados e as telas para acessá-los deixam de aparecer.

### 3.2.3 Reativando a integração

A reativação é o processo de ativação da integração numa conta Ploomes que já esteve integrada anteriormente.

Após desativar a integração, é possível sim ativar novamente a integração, no entanto, todo o processo de habilitação da integração, configuração da integração e carga inicial de dados será necessário.

Na habilitação da integração, na tela de inserção e validação do Token, é exibida uma opção de flag “Reutilizar última configuração ativa”. Caso essa opção seja marcada, ao habilitar a integração, na tela de configuração serão carregadas as seções configuradas conforme a última versão da integração ativa na conta. Ou seja, os mapeamentos de campos, gatilhos de ação, filtros de recebimento e TOP’s configurados na última versão ativa da integração poderão ser reutilizados.

![Imagem 38: Na habilitação da integração, na tela de inserção e validação do Token, é exibida uma opção de flag “ Reutilizar última…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434625/d2aef70145a60c7657b5f6ce6518/AD_4nXeAUtfZs-bfCJXKi8wl8d4eFKuSgkvxTBbkKtQWTwOpVbWGar7MlLtZEctJl3-CXS4UAPpZPJ1YVouM3sGsya38agP0pIRpmIY57CozFNwUnvCWaA8CXGLH1m7PLHKluDbe_XE76w?expires=1786536000&signature=ae8b09925959a37406a5263c2158d5bb49b479fc3a2ba7d761532248cb1fe2ef&req=dSUlEs19mYddXPMW3nq%2BgQqrQcfPAYD7bSYwup0dru%2FJKTg5lwUcvXdGwGoE%0AiGWz4beryh%2FsPcWVRD6fFzVAvIg%3D%0A)

Se iniciar uma reativação reutilizando a última versão da configuração ativa, será possível reaproveitar os mapeamentos, filtros e gatilhos configurados. No entanto, caso essa opção não seja selecionada, é preciso estar ciente de alguns comportamentos do mapeamento.

#### Comportamentos de mapeamento na reativação sem utilizar a última configuração ativa

- A integração irá sugerir a criação de novos campos com o mesmo nome dos campos dos criados na ativação anterior.
  Por exemplo:

  - Na primeira ativação foi criado o campo “Cód. Parceiro (Sankhya)”.
  - Na segunda ativação será sugerido a criação de um novo campo “Cód. Parceiro (Sankhya)”. Ou seja, um novo campo com o mesmo nome mas que ainda são campos diferentes.

    - Se o campo da segunda ativação for mantido no mapeamento, ele será criado ao ativar a integração e apenas ele estará mapeado. Ou seja, o campo da primeira ativação não será mais utilizado pela integração.
- Para evitar que um novo campo de mesmo nome seja criado, é preciso substituir o campo sugerido pela integração pelo campo já existente no Ploomes.
- Os campos utilizados na primeira ativação (ou ativação anterior) não serão sugeridos automaticamente. O usuário deverá trocar os novos campos sugeridos por campos existentes um a um.
- Se os campos utilizados para pareamento forem substituídos por campos diferentes dos que foram preenchidos na primeira ativação, a reativação poderá duplicar cadastros criados na primeira ativação.
  Por exemplo:

  - Na primeira ativação utilizei o campo “Cód. Parceiro (Sankhya)” para receber o código dos Parceiros do Sankhya.
  - Na segunda ativação troquei esse campo por um campo novo e não preenchido “Código dos Parceiros”.

    - Ao receber um Parceiro Cliente PJ do Sankhya, ele vai tentar ser pareado com Empresa do Ploomes através do campo "Código dos Parceiros", que está vazio.

      - Se ele não tiver CNPJ ou também não encontrar nenhuma Empresa com o mesmo CNPJ, será criada uma nova Empresa no Ploomes, mesmo que alguma Empresa tivesse o respectivo código no campo “Cód. Parceiro (Sankhya)" utilizado no mapeamento da primeira ativação.

Realizando a habilitação da integração, configurando a integração e ativando novamente, após a conclusão da carga inicial o processo de reativação estará concluído.

**Com a integração ativa na conta novamente, o processo de configuração está concluído e a conta Ploomes pode ser utilizada integrada ao Sankhya normalmente.**

---

**Observações importantes sobre a reativação**

- Ao reativar a integração, todo o processo de carga inicial precisa ser feito novamente, mesmo que supostamente já existam no Ploomes. Essa etapa é necessária, pois realiza a adequação dos campos e dados, garantindo a consistência e qualidade dos dados no Ploomes e refaz a vinculação dos itens.
- A carga inicial em uma reativação tende a ser mais demorada do que a primeira carga inicial, pois são feitas as tentativas de pareamento dos cadastros e, portanto, existem muitos cadastros para tentativa de match.
- Como é realizada uma carga inicial, os dados “retroativos” do Sankhya podem ser importados, seguindo as regras de filtro, mapeamentos e gatilhos configuradas.

---

## 4 Ativação

## 4.1 Ativação

Após configurar toda a integração, é possível realizar a Ativação da Integração.

![Imagem 39: Após configurar toda a integração, é possível realizar a Ativação da Integração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434628/9b7044c6adc1c41fa747d16cf6ac/AD_4nXcZGo4S3jdagoO-q3dz7i3u54c6CxR36mp8VirxNBLbQJdyCbBsnONRb1LYB-NzY-1IxN2wsj5-CjkxT4deR2psC5PnUGGSh4SKYFDvdFzLWh8o1EtVGcQrUc2I32bDbA6li99DSQ?expires=1786536000&signature=71916386f7244aad453554313b6e9747cf4c0d985ab16189c4a40a9f1ffe90ea&req=dSUlEs19mYddUfMW3nq%2Bged2amSkK4T%2FLIPWXsjdoG5oIMHeElS9lxC7dRHN%0AG1ddjXerZcbwr85%2Bz4Dw6CpZ%2FFw%3D%0A)

Ao ativar a integração, ocorrem alguns eventos de preparação e então inicia-se a carga inicial de dados para serem integrados.

![Imagem 40: Ao ativar a integração, ocorrem alguns eventos de preparação e então inicia-se a carga inicial de dados para serem…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434623/23beb41a14cb4de0ebff08910464/AD_4nXf-kq0f24E-3vGb-DGutrBwT1Tq35fjx5PSaABHM6zWP4mi3Ynrc7GudKbGNQ83mGzlGb_HEYN8vVS6JLDb552YAzfgFHtzSwUkxofR8QeUrp2aZNAYk2KIZuMkcTCoMaFtYyXeLQ?expires=1786536000&signature=7b9b205375b118072047aef854142fe9a398d1aaec2548cf080abaf305a054cb&req=dSUlEs19mYddWvMW3nq%2BgSo4VFjRin8Txlv0Jc0iMr8mfRruT413fiMl12f5%0Amk3rWoihqEJjbKwLGCa%2FfLDezxo%3D%0A)

Os eventos que ocorrem ao ativar a integração são:

- Os campos dinâmicos sugeridos e utilizados nos mapeamentos são criados.
- A carga inicial de cadastros Sankhya e Ploomes é executada.
- Os ícones que indicam os campos utilizados no mapeamento de cada entidade ficam disponíveis.
- Os modais de status de integração das entidades ficam disponíveis.
- As consultas em tempo real de informações da Sankhya ficam disponíveis.
- Os webhooks de envio de criações e edições do Ploomes são ativados, passando a ser possível enviar cadastros e edições de cadastros para o Sankhya.
- As rotinas periódicas (pooling) de recebimento de criações e edições do Sankhya são ativadas, passando a ser possível receber cadastros e edições de cadastros no Ploomes.
- A tela de Registros da Integração fica disponível.

O progresso de ativação da conta da integração é exibido na tela de configuração.

É exibida uma barra de progresso da evolução das etapas de ativação, sendo a carga inicial de dados a mais custosa em complexidade e tempo de processamento.

![Imagem 41: É exibida uma barra de progresso da evolução das etapas de ativação, sendo a carga inicial de dados a mais custosa em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434632/7133c3c7e39263c6728656a26e2e/AD_4nXfxvV72rSmR0iEpZFRf2BTSqRenaxcgUTvFIdpJStzCH4kmppFsc9vqolB4tDKKyiAfPAhTDhuBHMbUxFqhkRUdz1IyOgc35xoj1l-X8cdeBjxYQGgVdk_hsKiPc8WLVMExZ9HrsA?expires=1786536000&signature=3e4293df6eb2d23008691e7149cc2fc046f463d6de8220e51d6aff704fdb9abf&req=dSUlEs19mYdcW%2FMW3nq%2BgZeEFpENrT%2Bt6iNU9V3RquTRfCL3%2B1iJeJDQV7Og%0Ar1A0XlGQcAYbupkK1mkHg%2B8S7OU%3D%0A)

Em cada etapa, é exibida um breve resumo que é atualizado num intervalo de tempo, detalhando quantos itens do Sankhya já foram salvos na fila ou quantos itens já foram processados.

A barra de progresso exibe um percentual que é simbólico e determina o avanço pelas etapas executadas, no entanto, as últimas etapas de carga de dados podem levar um tempo maior para conclusão, portanto é possível que o percentual pareça estagnado, no entanto os cadastros estão sendo processados para que a etapa seja finalizada.

Para que a integração esteja ativa e liberada para o uso, é necessário que a carga inicial esteja completamente concluída.

## 4.2 Carga inicial de dados

A carga inicial é uma etapa crucial para que a integração seja bem sucedida, portanto, antes de realizar a ativação é extremamente necessário validar toda a configuração da conta, em especial as vias de integração, filtros de recebimento e mapeamento de campos.

A carga inicial é realizada em 4 etapas:

1. Importação do Sankhya para o Ploomes de todos os cadastros do Sankhya que atendam às condições de recebimento configuradas (gatilhos e filtros) e aplicando as regras de pareamento para a importação em cada entidade.
   Nota sobre pareamentos:

   - Os cadastros recebidos que NÃO forem pareados darão origem a novos cadastros no Ploomes.
   - Os cadastros recebidos que forem pareados irão atualizar os cadastros existentes no Ploomes.
2. Exportar do Ploomes para o Sankhya os dados dos campos mapeados dos cadastros pareados do Ploomes que não foram atualizados no recebimento do cadastro do Sankhya.
   Exemplo:

   - Recebe um Parceiro que atualiza a Cidade e Endereço de uma Empresa com a qual foi pareado no Ploomes e, essa mesma Empresa, em seguida, exporta para o Sankhya seu e-mail, que só estava preenchido no Ploomes.
3. Exportar do Ploomes para o Sankhya todos os cadastros do Ploomes que não foram pareados ou criados a partir de cadastros importados do Sankhya e que atendam às condições de envio configuradas (gatilhos e filtros) e aplicando as regras de pareamento para a exportação em cada entidade.
   Nota sobre pareamentos:

   - Os cadastros enviados que NÃO forem pareados darão origem a novos cadastros no Sankhya.
   - Os cadastros enviados que forem pareados irão atualizar os cadastros existentes no Sankhya.
4. Importar do Sankhya para o Ploomes as atualizações de campos mapeados dos cadastros pareados do Sankhya que não foram atualizados no envio do cadastro do Ploomes.
   Exemplo:

   - Envia uma Pessoa que atualiza o telefone e e-mail de um Parceiro com o qual foi pareado no Sankhya e, desse mesmo Parceiro, em seguida, recebe no Ploomes uma atualização de cidade que só estava preenchido pelo Sankhya.

---

**# Observações importantes sobre a carga inicial**

- Durante a carga inicial, são importados somente os CabecalhosNota que possuam `STATUSNOTA = L` no Sankhya.
- A **carga inicial não pode ser cancelada** **pelo usuário** do Ploomes e continua mesmo que o usuário saia da tela de carregamento da carga inicial ou deslogue do Ploomes.
- É **imprescindível que o usuário administrador verifique o volume de dados do Sankhya** que será importado ao Ploomes, pois esse volume impacta diretamente no tempo de ativação da integração na conta. Uma vez que a carga inicial for ativa, não é possível que o administrador modifique os filtros.
- Caso algum campo desejado não esteja mapeado, se sua inclusão no mapeamento for realizada após a carga inicial, os dados desse campo não serão preenchidos automaticamente para os cadastros já integrados, somente valerão para novas importações e/ou exportações. Por isso é **extremamente importante validar os mapeamentos antes de ativar a carga inicial**.
- Caso o servidor Sankhya tenha alguma limitação para realização de consulta de dados via API ou apresente algum erro, essa restrição afetará diretamente a performance da carga inicial.

  - Caso algum campo mapeado (do Ploomes ou do Sankhya) seja deletado (durante a operação normal, mas especialmente durante a carga inicial), a carga inicial falhará e passará a retornar erro.
  - Caso o servidor Sankhya esteja indisponível durante a carga de dados, não será possível realizar a carga inicial por impossibilidade de comunicação com o Sankhya.
  - Caso o servidor Sankhya esteja lento e a consulta de páginas de requisições nas entidades ultrapasse os 2minutos, poderá ocorrer erros de timeout do Gateway Sankhya que paralisarão a carga inicial.
  - Caso o Token gerado para a aplicação seja inativado ou removido durante uma carga inicial ou durante o uso da integração, não será possível realizar carga inicial e nem nenhuma outra operação de integração devido a impossibilidade de comunicação com o Sankhya.
- Em caso de **interrupções da carga inicial por algum erro no Sankhya** ou no Ploomes, a mesma poderá ser reiniciada novamente clicando em “Tentar novamente” caso ocorra algum erro durante seu processamento.

  - Devido às regras de pareamento, caso ocorra alguma falha durante o processo da carga inicial, ao reiniciar o processamento os cadastros já criados durante a carga inicial parcial não serão duplicados e a carga inicial seguirá normalmente.
- A **velocidade da carga inicial depende diretamente** da disponibilidade e velocidade de **resposta do Sankhya e do Ploomes**. Se um ou os dois sistemas apresentarem indisponibilidade ou baixa velocidade de processamento a integração será impactada diretamente.
- Quanto **mais campos forem mapeados** nas entidades integradas, **maior será o tempo de processamento** de dados na exportação e importação, inclusive durante a carga inicial.
- Quanto **melhor definidos os filtros de recebimento** - isto é, adequação dos tipos de cadastros com base em algum campo e com base na data desejada - melhor será a qualidade dos dados importados e menos tempo levará para execução da carga inicial.
- **Não é recomendado executar a carga inicial sem aplicar filtros de recebimento** e principalmente **sem conhecimento do volume de dados existente no Sankhya** para serem importados. Essa etapa de levantamento é importantíssima para o dimensionamento da carga inicial de dados.
- As criações e edições enviadas ou recebidas durante a carga inicial ficam visíveis na tela de Registros da Integração.
- Quanto mais cadastros existirem no Ploomes, maior será o tempo de processamento devido as tentativa de pareamento que são realizadas para a integração. Para cada cadastro, é feita a varredura de todos os itens na tentativa de match para pareamento, e isso aumenta o tempo de processamento.
- A carga de dados durante a importação tem como referência de taxas normais de processamento os seguintes valores:

  - **CabecalhoNota+ItemNota:** 180~300 cadastros/hora (variável em função da quantidade de ItemNota)
  - **Parceiro:** 1500~2000 cadastros/hora
  - **Produto/Serviço:** 1500~2500 cadastros/hora

    **Observação sobre as taxas de processamento:** essas taxas acima são médias esperadas com base no histórico observado da integração Sankhya e da capacidade atual de processamento da API do Ploomes. No entanto, é possível observar performances superiores em alguns casos e também inferiores, à depender de cada caso.

---

Após a conclusão da carga inicial, é possível utilizar a conta Ploomes integrada ao Sankhya normalmente.

A tela de configuração da integração passa a exibir para consulta as informações configuradas em cada seção e passam a estar disponíveis os botões de Desativação e Edição.

## 4.3 Modal de Status da Integração

Após a integração ser ativa na conta, é possível visualizar no menu superior o ícone com a logotipo da Sankhya, indicando que a conta Ploomes tem integração Sankhya ativa.

![Imagem 42: Após a integração ser ativa na conta, é possível visualizar no menu superior o ícone com a logotipo da Sankhya,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434622/b5318fb6565db92cd0bf5ba87228/AD_4nXdZG-cxRxgldZNtBXbSOR41eGoCXn8NsZfoAeFJsU3vIYYenbK_or5XE7UI57Ime0x0D6iq8rLWp0nlTfzOttJBZkic10MChwoqZF4yqQXhom8l3yvabwEtryoO1sCyeYsoov4?expires=1786536000&signature=0a497ec41d3f550b533cf507c0d44e2941a9eef1c577141e227a3392a78885a3&req=dSUlEs19mYddW%2FMW3nq%2BgSuZw4Njn3MkYorzCXh%2BrOJxWyfXTEeWBRrbAqb%2F%0A%2FGgMDAg4BwohDawUCDledQBED28%3D%0A)

Ao clicar sobre o ícone, o usuário é redirecionado para a tela de consulta de Registros da Integração com o filtro pré-selecionado de usuário criador da ação. Dessa forma, será possível visualizar todas as edições realizadas pelo usuário em questão que geraram registros de integração.

![Imagem 43: Ao clicar sobre o ícone, o usuário é redirecionado para a tela de consulta de Registros da Integração com o filtro…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434607/bce06e65c39368fb37602bdb0a17/AD_4nXeazRGLSaWbnhcr8LxbAzTf3ZdWurT-gp0TW9zXKoHy8YdNotKZIYkKUixGJtGeHeBu2USDLVs7tHBYnWRLSr6V8hyjRBkgd5qOH9W5-OSWzOZppx7s59dTVyxV_cA6MpBdObn4dA?expires=1786536000&signature=a4d11b4581b1096e4c58113bfa2d154a65d60559a7dc97b7ddce580742dd0952&req=dSUlEs19mYdfXvMW3nq%2BgX0m0B1A7YiXOPLAWsrI3YXZ7Yv%2BgwVZqB9VM91G%0AJJdPkx%2F%2B%2FcOPH0NV%2FUultxRcIwI%3D%0A)

Todas as entidades integráveis do Ploomes possuem um botão indicador de Status em sua tela de visualização.

![Imagem 44: Todas as entidades integráveis do Ploomes possuem um botão indicador de Status em sua tela de visualização.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434612/272b080ec54799324852cec8c709/AD_4nXe232Ez_D4ISzX8_E-knbLtyGCcY374sQQxKw81pmRljasZjGjC7ZIIc5RyuGeUqO0yzQXvvWQG0UkucTwRBh0zGRDAhyxQPW9ATHRDChSeGEs8f8xReXVgu6zlwsnTWSTiA5bC3A?expires=1786536000&signature=04520015c05bef4b8bbdfbf9d8879bbfc0d4d8f18b754d3c38de77fc4193a4c5&req=dSUlEs19mYdeW%2FMW3nq%2Bgfljw0SbpxePtrJYuRRPX%2F42Ye3F9hegmd%2BNtbcT%0A3RurC6rHMOoUEQBAeDELQIaQX2g%3D%0A)

Esse botão indica se o cadastro específico está integrado ou não. Ao clicar sobre o botão são exibidos detalhes sobre a integração do cadastro.

![Imagem 45: Esse botão indica se o cadastro específico está integrado ou não. Ao clicar sobre o botão são exibidos detalhes sobre a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434661/c7f3b4b8b7633c55bcc043e1e2ea/AD_4nXfa3K2onXhuyu9MjnGuMTQUjwRnmiS5AmqfDAwCfz3upd6RNoCmi1C2LcMHioqFWK6vfSWh0JWW0PmS7CJ2rsO5w-jtTM3fSAbbXdG3AxajmLJAQWmlbFEFTB3Yxy-uYPFlMzG_vw?expires=1786536000&signature=f32063217712f1db2f951a0f7984f650cb532378c65dc7ad6d2fd3172fe7abf9&req=dSUlEs19mYdZWPMW3nq%2BgXzHqNLGvnbaCtLANN7KVMqXiLjnLOZxW8u7LLId%0AnaJ9EJX3C%2BE2UK5084PI%2FnC1VOE%3D%0A)

![Imagem 46: Esse botão indica se o cadastro específico está integrado ou não. Ao clicar sobre o botão são exibidos detalhes sobre a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434616/0f137df042f599dfe13cb8bfb25e/AD_4nXdQ-pyIcIO-ENz3JbrI8n1LvDJqH-lMxIGIttAl8Ly5kIUNU0yF0BxRzzjfiYU7nLUtawzTYrMBtktTbT6jBHPHtf1kZIrTJEYWXzBuaQZr20cKpidy9CF0gthL47NZ_DXTE4Q2?expires=1786536000&signature=39733e2058d07b8303baa10755ba27eabfb743a29669a443aada9b7ae6beed71&req=dSUlEs19mYdeX%2FMW3nq%2BgdsOtNYJBkpCYkDg1IsDxyKiGDTAIb5jxlmEQOYb%0AohRw0wFQgEaJVby6YnrFCRBC%2Bu8%3D%0A)

![Imagem 47: Esse botão indica se o cadastro específico está integrado ou não. Ao clicar sobre o botão são exibidos detalhes sobre a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434615/02302987a344101da987c57b8b5e/AD_4nXfnxQO_HIvEvBCC16V-qKYToDKkndrJRbcJOUqlSQk7oM1VPO5tmTEdwmeVR9VpAhAD1U_ibnUph7dtJY8uZedr5ash6OR_JzroE8eRdwXGcIFyuSYWN4AITF5-GummMUD58wJLVA?expires=1786536000&signature=f9f9dd8fbf1175d85637546bb718e3363494883d0b1e32f0584f3506af93ee46&req=dSUlEs19mYdeXPMW3nq%2BgWlqCkz2p50TeA9DGIyXBXKDKSGY9HNF0yu%2F3Tog%0AOgSNs2A5GM58hAIZGLzD%2FbM0iq8%3D%0A)

Quando o cadastro está integrado o modal de detalhamento exibe as seguintes informações:

- Campos mapeados para a entidade integrada.
- Campos chaves e seus respectivos valores do pareamento do cadastro.
- Gatilhos configurados para envio dos cadastros (se aplicável).
- Gatilhos configurados para recebimento dos cadastros.

![Imagem 48: Gatilhos configurados para recebimento dos cadastros.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434618/36acc9c51f9f678d01b0fd77053c/AD_4nXf9Q63o3RimGXxzx4X39uDldbDBUpSAyC1kH8DqE2wWNclI6nwSk-tGMZQIdk4P9fW9YMJW1Pd673AeXWFQgbJKUp9dakmr6DF7QhmjecWyBByA0yjMs8f899wPnZZcac-gxDIEqg?expires=1786536000&signature=68211597b10c776d6f191b531a03682cdd134dda538d5e887c863adbf34ea585&req=dSUlEs19mYdeUfMW3nq%2BgVW%2F16TJX%2BbBIbqM3y%2FuBnRhY8u2GPYs7ZG8UHPL%0AO9BbPl7kH%2FPyRbVZ7eKRYRsUX2w%3D%0A)

Quando o cadastro NÃO está integrado não são exibidas nenhuma informação no modal de detalhamento.

![Imagem 49: Quando o cadastro NÃO está integrado não são exibidas nenhuma informação no modal de detalhamento.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434614/6389dc5cb53eb2d3ae4ac9cd4e67/AD_4nXfjblyJFzIuSWUTauFH5yzjZHvC_ItcpGB4ydIWdTVx0XQXPan9bSXuKqLI5mpDfAbT2rvXe1k-GmxlczIyL5FrPNduB78nmPgrgJWPlZyc3SM6kPiBvMN84-dxOMQs8J2f-f8XKQ?expires=1786536000&signature=e6e669ce1f147eab424f252256bb98f465313e2064c0f5049b340d637cfa8e95&req=dSUlEs19mYdeXfMW3nq%2BgUDuj%2B2jl3yabXeiFMt%2FbKbrS0rybjdIOsB6%2FrIm%0A2E6PbQ7V3fpRY6R3s5jerZ3WA74%3D%0A)

Em todas as telas de cadastros existe a **identificação com o ícone do Sankhya** ao lado da descrição do campo para **evidenciar um campo que é utilizado no mapeamento da integração** para a entidade integrada.

Os campos que possuírem o ícone Sankhya ao seu lado direito são utilizados no mapeamento da integração e os que não apresentam o ícone Sankhya são campos do Ploomes que não são utilizados no mapeamento da integração.

![Imagem 50: Os campos que possuírem o ícone Sankhya ao seu lado direito são utilizados no mapeamento da integração e os que não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434609/2ae55724f589afb19a1e6af060b8/AD_4nXdjNW06Y1N9-siWh5rrhq7Th1XFkDJKbp-hzj20pIC87RcjVZ_mwxmhD8BmWoZaa8QcQQTX4ZuE4m_oZmN11N_yMxEue9WZZib4paSMBI5GQbthBEXJyqk9o4glRD7-9DvySOwq9w?expires=1786536000&signature=1e024edd59a9280d98a2559b3096098024f71e551f00bd36b418a477f93fa43f&req=dSUlEs19mYdfUPMW3nq%2BgUiyaZc67h03G3%2FCyI09kPCpXqX2V%2BG0GAfjWRzB%0AXlxeEjbXGfXNHN87sd81hnYt0zA%3D%0A)

![Imagem 51: Os campos que possuírem o ícone Sankhya ao seu lado direito são utilizados no mapeamento da integração e os que não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434629/16f66d89d8c58d3b81dc9f7ff0bf/AD_4nXeMgETP4zSPIPCYwWzzXvPDjXx_RajpNX25jkAnkhfecXyBulmfTMue-FF0gvRSxEO2Wmhqf6uw-ZdkC2eW0dKvX-s5W2GGbeIq3w6ylaytw0WGrKlgYgbIgNQXM_eaKW3Dwcy5dw?expires=1786536000&signature=1530d5032370b32fcd329ccf1f0eef54d2f78fa35f1b736ecf8b542d4835ca77&req=dSUlEs19mYddUPMW3nq%2BgYza1L3nW63M71zmdKJ%2FnHbFfdteDBvr5m%2FzTBFN%0AhS0c3cNryxqXFSK3Snik4yuOElw%3D%0A)

![Imagem 52: Os campos que possuírem o ícone Sankhya ao seu lado direito são utilizados no mapeamento da integração e os que não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434630/1e70ac9ceb2864a16d19089fd5b9/AD_4nXc5URrNLztpHcjrGZFjorYie1uZ3PhZUcRJeQBzY-emI4n7Qu8chQ1tERvwjH70fiCQidNpOqQEy9--Zyhq3IVT3U7-Mqz3GPjwlP7uTvneuc4eaWafXUKUUCIJw97_Fpx7VNXI?expires=1786536000&signature=57b6f8f55a54d98bd980e2ece2aef0d1533c8391ea49a6e6463435ddde21c4af&req=dSUlEs19mYdcWfMW3nq%2BgY0eGZoRZj4VvsOCQax3HiLSIuFzlCl0uc4cE8A2%0AGujAySfeBzYg3NiF5NnaKk4%2FC98%3D%0A)

A integração não realiza nenhuma alteração visual no layout do Sankhya para identificação dos registros integrados com o Ploomes. Esses modais de identificação de cadastros integrados existem somente no Ploomes.

---

## 5 Importação

## 5.1 Como funcionam Criação e Edição no Sankhya

### Criação

Ao criar um novo cadastro no Sankhya em uma entidade configurada na integração, é registrado no banco de dados Sankhya a data da última modificação desse cadastro.

A transferência de dados do Sankhya para o Ploomes acontece de forma passiva para o Sankhya. Pois os dados são buscados pelo Ploomes através de um Pooling. O pooling funciona como um processo de varredura no Sankhya, verificando a data da última modificação dos cadastros no Sankhya, trazendo então os dados que foram modificados nos últimos 5 minutos.

O intervalo de 5 minutos do Pooling é o intervalo de verificação no Sankhya e não necessariamente o tempo necessário para uma atualização ser importada após alteração no Sankhya. Não há um tempo mínimo garantido para a integração. Pode ocorrer de os registros serem importados num intervalo menor ou maior do que os 5 minutos, dependendo sempre da disponibilidade do Sankhya e do volume de dados trazidos para a fila.

Esses dados de novas criações buscados, uma vez que atenderam aos filtros de recebimento, são salvos em uma fila de importação, e em seguida são processados e salvos no Ploomes.

### Edição

Ao editar um cadastro no Sankhya em uma entidade configurada na integração, se o cadastro editado estiver integrado (ou seja, já foi processado pela integração anteriormente e está vinculado no Sankhya e no Ploomes), as edições realizadas serão capturadas pelo Pooling da integração, levando esses dados para o Ploomes.

O intervalo de 5 minutos do Pooling é o intervalo de verificação no Sankhya e não necessariamente o tempo necessário para uma atualização ser importada após alteração no Sankhya. Não há um tempo mínimo garantido para a integração. Pode ocorrer de registros serem importados num intervalo menor ou maior do que os 5 minutos, dependendo sempre da disponibilidade do Sankhya e do volume de dados trazidos para a fila.

Esses dados do cadastro editado precisam atender aos filtros de recebimento e via de integração configurados para que sejam de fato capturados pelo Pooling e enviados ao Ploomes.

Esses dados capturados, uma vez que atenderam aos filtros de recebimento, são salvos em uma fila de importação, e em seguida são processados e salvam a edição.

## 5.2 Gatilhos

Os “gatilhos da integração” definem quando um cadastro ou edição de cadastro são enviados/recebidos entre Ploomes e Sankhya para cada par de entidade integrada (ex: Empresa x Parceiro PJ).

Em qualquer um dos casos (Edição ou Criação), o cadastro passará a estar integrado e os gatilhos de envio ou recebimento de edições passarão a ser aplicáveis a esse cadastro.

Comportamento dos gatilhos:

- Só pode ser selecionado um gatilho de recebimento de criação/edição de cadastro por vez;
- São aplicados tanto na carga inicial quanto nas criações após a ativação da integração;
- Funcionam através de pooling - rotina periódica de 5 em 5 minutos que identifica a existência de novos cadastros ou cadastros existentes editados - que captura as informações atualizadas do Sankhya que atendam as condições de recebimento e eventuais filtros criados.

## 5.3 Filtros de recebimento

Os filtros de recebimento (ou importação) da integração são regras configuradas na integração que determinam quais informações devem ser recebidas do Sankhya no Ploomes.

- **Comportamento geral dos filtros**

  - Os filtros de recebimento de cadastros definidos são aplicados tanto na carga inicial da integração quanto durante o uso da integração;
  - Os recebimentos de cadastros que forem barrados pelo filtro não chegarão a ser exibidos na tela de logs, pois nem chegam para a fila da integração, já são barrados na origem;
  - Os filtros de recebimento também afetam os cadastros já integrados, ou seja, afetam o recebimento de edições. Portanto, um cadastro uma vez integrado, também pode ser barrado pelo filtro caso um de seus campos seja alterado de maneira que não atenda a um critério de filtro.
- **Possibilidades de filtro de recebimento de cadastro**

  - Filtro de recebimento de Parceiro Cliente PJ, Parceiro Cliente PF e Contato de Cliente para integração com Empresa ou Pessoa:

    - Filtro customizável através de campos nativos ou dinâmicos de Parceiro e Contato de Cliente, respectivamente;
    - Sem possibilidade de fieldpath (ou uso de campos de entidades relacionadas à empresa) no filtro;
    - Permite a combinação de regras de E e OU.
  - Filtro de recebimento de Produto/Serviço e Grupo de Produto/Serviço para integração com Produto e Grupo de Produto:

    - Filtro customizável através de campos nativos ou dinâmicos de Produto e Serviço;
    - Sem possibilidade de fieldpath (ou uso de campos de entidades relacionadas à produtos - ex.: estoque) no filtro;
    - Permite a combinação dessas duas regras com E e OU.
  - Filtro de recebimento de Vendedor para integração com Usuário:

    - Filtro customizável através de campos nativos ou dinâmicos de Vendedor;
    - Sem possibilidade de fieldpath (ou uso de campos de entidades relacionadas ao usuário) no filtro;
    - Permite a combinação dessas duas regras com E e OU.
  - Filtro de recebimento de Orçamento, Item do Orçamento, Pedido de Venda, Item do Pedido de Venda e Nota de Venda para integração com Proposta, Produto da Proposta, Venda e Produto da Venda e Venda respectivamente:

    - Filtro customizável através de campos nativos ou dinâmicos de Orçamento e Pedido de Venda;
    - Sem possibilidade de fieldpath (ou uso de campos de entidades relacionadas ao Orçamento ou Pedido de Venda) no filtro;
    - Permite a combinação dessas duas regras com E e OU.

## 5.4 Regras de Pareamento

As regras de pareamento são as condições definidas para a vinculação de cadastros do Sankhya com o Ploomes ou não.

Com base nessas regras de pareamento, ao receber um cadastro do Sankhya no Ploomes, é decidido se o cadastro recebido será vinculado a um cadastro existente no Ploomes ou se será criado um novo cadastro no Ploomes.

A tabela abaixo detalha resumidamente por quais campos chave os registros criados ou editados no Sankhya são identificados e pareados com os registros correspondentes no Ploomes durante o processo de importação.

| **Entidade Sankhya** | **Entidade Ploomes** | **Campos Chave de Pareamento** |
| --- | --- | --- |
| **Parceiro PJ (TGFPAR)** | **Empresa** | Cód. Parceiro (`CODPARC`) ou  CNPJ (`CGC_CPF`) |
| **Parceiro PF (TGFPAR)** | **Pessoa** | Cód. Parceiro (`CODPARC`) ou  CPF (`CGC_CPF`) |
| **Contato de Cliente (TGFCTT)** | **Pessoa** | Cód. Parceiro (`CODPARC`) + Cód. Contato (`CODCONTATO`)  ou  Email (`EMAIL`) |
| **Vendedor (TGFVEN)** | **Usuário** | Cód. Vendedor (`CODVEND`)  ou  E-mail (`EMAIL`) |
| **Produto / Serviço (TGFPRO)** | **Produto** | Cód. Produto (`CODPROD`) |
| **Grupo de Produto (TGFGRU)** | **Grupo de Produto** | Cód. Grupo Produto (`CODGRUPOPROD`) |
| **Orçamento (TGFCAB)** | **Proposta e Produto da Proposta** | Nro. Único (`NUNOTA`) |
| **Pedido de Venda (TGFCAB)** | **Venda e Produto da Venda** | Nro. Único (`NUNOTA`) |
| **Nota de Venda (TGFCAB)** | **Venda e Produto da Venda** | Nro. Único (`NUNOTA`) |

## 5.5 Registros da Integração

Todos os eventos de integração (edições e criações de envio e de recebimento), que tenham atendido aos filtros de envio e recebimento, são registrados na tela **Registros do Sankhya.** Disponível na seção de Administração do Ploomes.

![Imagem 53: Todos os eventos de integração (edições e criações de envio e de recebimento), que tenham atendido aos filtros de envio…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434627/9d8968bd4c0d7a2a5c3af0f36b5e/AD_4nXee7ogRmkEJvifV1s7WsYHKAopvzmft5sGO3uoUCA2kCqDHgamWndKlletZo09sqZfQ_zsTBd8GrvwJYn6yf8JNNDpYcV9NmyinpxdId-ajSki_UuWYsCiUFxQxK31AzPq4cSuH8Q?expires=1786536000&signature=c645016c64418b52e13c8502b8a42594fb6b195be497524fde59740fb2d3d665&req=dSUlEs19mYddXvMW3nq%2Bge8E%2F90xwFg7cYCEnxiiDr89GFo8N3mIFPjJV3bh%0ATYrXOiXEoltVNYgN%2B1GbAqehstM%3D%0A)

Ao acessar a tela de registros pelo menu de Administração, é possível consultar todos os eventos de importação da integração realizados na conta do cliente na integração vigente. Ou seja, se a integração for desativada e reativada, a tela de registros “limpa” todos os eventos armazenados, exibindo os eventos para consulta apenas da versão vigente da integração e suas edições.

Detalhes de como filtrar, onde acessar, quais dados estão disponíveis estão [no artigo sobre a tela de registros](https://sankhya.zendesk.com/hc/pt-br/articles/42427450811927).

---

## 6 Exportação

## 6.1 Como funcionam Criação e Edição no Ploomes

### Criação

Ao criar um novo cadastro no Ploomes em uma entidade configurada na integração, é acionado o webhook do Ploomes. Esses webhooks do Ploomes são o gatilho de envio dos dados para o Sankhya.

A transferência de dados do Ploomes para o Sankhya acontece de forma ativa. Uma vez que a exportação depende exclusivamente da ação no Ploomes para que o webhook seja acionado e envie os dados para a integração.

Esses dados enviados, uma vez que atenderam aos filtros de envio, são salvos em uma fila de exportação, e em seguida são processados e salvos no Sankhya.

### Edição

Ao editar um cadastro no Ploomes em uma entidade configurada na integração, é acionado o webhook do Ploomes. Se o cadastro editado estiver integrado (ou seja, já foi processado pela integração anteriormente e está vinculado no Sankhya e no Ploomes) e atender aos filtros de envio configurados, as edições realizadas serão enviadas para a fila da integração.

Uma vez que atenderam aos filtros de envio e foram salvos na fila de exportação, em seguida são processados e salvam a edição no Sankhya.

Ações de edição que não atendam ao filtro de envio serão bloqueados na exportação. Os dados dos webhooks dessas edições serão armazenados em uma tabela de exportações bloqueadas por até 30 dias e, durante esse intervalo, caso uma nova exportação atenda ao filtro de exportação os dados da edição anterior (ou das edições anteriores) serão exportados normalmente.

## 6.2 Gatilhos

Os “gatilhos da integração” definem quando um cadastro ou edição de cadastro são enviados/recebidos entre Ploomes e Sankhya para cada par de entidade integrada (ex: Empresa x Parceiro PJ).

Em qualquer um dos casos (Edição ou Criação), o cadastro passará a estar integrado e os gatilhos de envio ou recebimento de edições passarão a ser aplicáveis a esse cadastro.

Comportamento dos gatilhos:

- Só pode ser selecionado um gatilho de envio de criação/edição por vez;
- São aplicados tanto na carga inicial quanto nas criações após a ativação da integração;
- Funcionam através de webhooks de edição de cadastros, sendo que apenas os campos editados são enviados ao Sankhya e os mesmos precisam estar com a via de integração com sentido de envio para o Sankhya ativa.

## 6.3 Filtros de envio

Os filtros de envio (ou exportação) da integração são regras configuradas na integração que determinam quais informações devem ser enviadas para o Sankhya.

- **Comportamento geral dos filtros**

  - Os filtros de envio de cadastros definidos são aplicados tanto na carga inicial da integração quanto durante o uso da integração.
  - Os envios de cadastros que forem barrados pelo filtro não chegarão a ser exibidos na tela de logs, pois nem chegam para a fila da integração, já são barrados na origem.
  - Os filtros de envio também afetam os cadastros já integrados, ou seja, afetam o envio de edições. Portanto, um cadastro uma vez integrado, também pode ser barrado pelo filtro caso um de seus campos seja alterado de maneira que não atenda a um critério de filtro.
- **Possibilidades de filtro de envio de cadastros**

  - Filtro de envio Empresa ou Pessoa para integração com Parceiro Cliente PJ, Parceiro Cliente PF e Contato de Cliente:

    - Filtro customizável através de campos nativos ou dinâmicos de Empresa e Pessoa, respectivamente;
    - Sem possibilidade de fieldpath (ou uso de campos de entidades relacionadas à empresa) no filtro;
    - Permite a combinação de regras de E e OU.
  - Filtro de envio de Proposta ou Venda para integração com Orçamento e Pedido de Venda:

    - Filtro customizável através de campos nativos ou dinâmicos de proposta e venda, respectivamente;
    - Sem possibilidade de fieldpath (ou uso de campos de entidades relacionadas à empresa) no filtro
    - Sem possibilidade de fazer filtro com campos de produto da proposta ou produto da venda
    - Permite a combinação de regras de E e OU.
  - Filtros de envio de Usuário, Produto/Serviço, Grupo de Produto/Serviço e Nota de Venda **NÃO EXISTEM**, pois a integração não envia dados desses cadastros do Ploomes para o Sankhya.

## 6.4 Regras de Pareamento

As regras de pareamento são as condições definidas para a vinculação de cadastros do Sankhya com o Ploomes ou não.

Com base nessas regras de pareamento, ao enviar algum cadastro do Ploomes para o Sankhya, é decidido se o cadastro enviado será vinculado a um cadastro existente, se será criado um novo cadastro ou se a integração retornará erro.

A tabela abaixo detalha resumidamente por quais campos chave os registros criados ou editados no Ploomes são identificados e pareados com os registros correspondentes no Sankhya durante o processo de exportação.

| **Entidade Ploomes** | **Entidade Sankhya** | **Campos Chave de Pareamento** |
| --- | --- | --- |
| **Empresa** | **Parceiro PJ (TGFPAR)** | Cód. Parceiro (`CODPARC`) ou  CNPJ (`CGC_CPF`) |
| **Pessoa** | **Parceiro PF (TGFPAR)** | Cód. Parceiro (`CODPARC`) ou  CPF (`CGC_CPF`) |
| **Pessoa** | **Contato de Cliente (TGFCTT)** | Cód. Parceiro (`CODPARC`) + Cód. Contato (`CODCONTATO`)  ou  Email (`EMAIL`) |
| **Proposta (Orçamento)** | **Orçamento (TGFCAB)** | Nro. Único (`NUNOTA`) |
| **Venda (Pedido de Venda)** | **Pedido de Venda (TGFCAB)** | Nro. Único (`NUNOTA`) |

## 6.5 Registros da Integração

Todos os eventos de integração (edições e criações de envio e de recebimento), que tenham atendido aos filtros de envio e recebimento, são registrados na tela **Registros do Sankhya.** Disponível na seção de Administração do Ploomes.

![Imagem 54: Todos os eventos de integração (edições e criações de envio e de recebimento), que tenham atendido aos filtros de envio…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434652/e4000ae6fd04c08f3f5cccad1646/AD_4nXf77Wk-YpXB1M05B1db9P0Z0AmklAE9MS9ipVzZ03C0LUlolrgKLdCqQc2qbCrZ9A407Oqc-jpGeQN7xy3qu6xoO41bvAVkOxliUcjHGOUXG2htelRz4ZGNKPVP_8sVBDCWI7aOxA?expires=1786536000&signature=3ae1a54fd4f0165a596814e2cab4a7489623684bc8f6d5002456812cd8637314&req=dSUlEs19mYdaW%2FMW3nq%2BgebmaT52R2QRc3saTp5YtYlxPMAAOH1IP%2FdPYGbf%0AMjVEYzlN4E5eluiaQKZCpga42R8%3D%0A)

Portanto, usuários que não são administradores conseguem consultar apenas eventos de integração com origem no Ploomes (exportação) disparados pelo mesmo. Usuários não administradores não conseguem consultar todos os registros de integração da conta.

Detalhes de como filtrar, onde acessar, quais dados estão disponíveis estão [no artigo sobre a tela de registros](https://sankhya.zendesk.com/hc/pt-br/articles/42427450811927).

---

## 7 Consultas em tempo real

As consultas em tempo real são realizadas com finalidades específicas para entidades específicas. Essas consultas retornam a informação diretamente do Sankhya no momento em que são executadas.

## 7.1 Produto

### 7.1.1 Configuração das consultas

A configuração das consultas em tempo real para a entidade de Produtos é realizada em background pela integração.

É necessário apenas que o recebimento de Produtos / Serviços do Sankhya como Produtos no Ploomes esteja ativo.

### 7.1.2 Consultas realizadas

#### Consulta do estoque disponível

Para os Produtos que foram importados do Sankhya para o Ploomes e estão integrados é possível realizar a consulta de estoque disponível.

Essa consulta é executada na tela de cadastro de cada produto. Ao abrir o cadastro de um produto integrado, é necessário selecionar a unidade de medida e então é exibida uma tabela de estoque:

[GIF animado: Imagem 55: Essa consulta é executada na tela de cadastro de cada produto. Ao abrir o cadastro de um produto integrado, é…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525781228/4a6329fed64a2d725641a510615b/ConsultaRealTime_Estoque_Produtos.gif?expires=1786536000&signature=2e2492a56f1b06a80e929d3d405a26ed3e3c9b705f0dc4d6e2a40b33498bd479&req=dSUlE852nINdUfMW3nq%2BgflTjcsnsJGv1KQWo5qUYF6nIGToQrPQvybGQlyO%0AL6b%2FQQWr9AOf7bOxKR1mvilSoXk%3D%0A)

Nessa tabela, vão ser exibidos em linhas os estoques por:

- **Empresa**
- **Local**
- **Controle**

- E serão exibidos os totais das colunas de:

  - **Estoque:** quantidade total do Produto em estoque
  - **Reservado:** quantidade total reservada o Produto
  - **Disponível:** quantidade total de estoque do Produto que está disponível
- As quantidades exibidas são convertidas em função da unidade de medida selecionada. A conversão é feita pelo Sankhya, com base nos dados das entidades TGFEST (Estoque) e TGFVOA (Volume Alternativo) do Sankhya.

  Não é exibida a coluna de “Poder” na consulta de estoque. No entanto, caso o Sankhya esteja configurado para controlar estoques de em poder Próprio e de Terceiros, serão retornadas na consulta uma linha para cada Poder.

Abaixo estão descritos os comportamentos para:

- Proposta/Venda
- Produto da Proposta/Venda

Esses comportamentos são equivalentes entre as entidades de Proposta+Produto da Proposta e Venda+Produto da Venda, mas ainda assim no Ploomes, são distintas, portanto sua configuração, seus respectivos campos e parametrização no Ploomes são totalmente independentes.

## 7.2 Proposta ou Venda

### 7.2.1 Configuração das consultas

A configuração das consultas em tempo real para a entidade de Proposta/Venda é realizada em background pela integração e precisa ser habilitada na seção de configuração de consultas em tempo real.

![Imagem 56: A configuração das consultas em tempo real para a entidade de Proposta/Venda é realizada em background pela integração…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1598167951/2dc1aff52525bc32be1a3472245f/image.png?expires=1786536000&signature=25f3785fb620301f140f9ffd9d96f9792f3a8ba3314e2351c095eabc28493185&req=dSUuHsh4mohaWPMW3nq%2BgUvq%2FL%2FKqyuQBAQH4H2JH2Q3dbvaU6qDQLQh3AIO%0Aonsik4oJJmSAIh337Oz1kTf0XJU%3D%0A)

Para essa consulta, é criado um campo no Ploomes que recebe esses dados das consultas possíveis para Propostas/Vendas. No entanto, é possível alterar o campo sugerido que receberá esses dados na tela de configuração da integração.

### 7.2.2 Consultas realizadas

#### Consulta de detalhes financeiros do Cliente da Proposta/Venda

Para os Parceiros do Sankhya que estão integrados ao Ploomes como um Cliente, é possível realizar a consulta de detalhes financeiros na tela de Propostas/Vendas.

Na tela de edição de Propostas/Vendas, é possível engatilhar a consulta de detalhes financeiro do Cliente ao selecionar um Cliente e uma TOP.

[GIF animado: Imagem 57: Na tela de edição de Propostas/Vendas, é possível engatilhar a consulta de detalhes financeiro do Cliente ao selecionar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525783468/ec2d967b8ea9390ff0695a85825e/ConsultaRealTime_DetalhesFinanceiros_Proposta.gif?expires=1786536000&signature=617c462459282f38f19defa7e4844464bd06cdc0268d38d31797036f2b374c4e&req=dSUlE852noVZUfMW3nq%2BgeEcwIkuuqkYh%2Ba0pXyVyUhiy3GeUT9aop89V1gF%0A5BZK2%2BwHDIH%2FosM%2Box1USLDHeGw%3D%0A)

Exemplo de consulta aos detalhes financeiros do Cliente da Proposta após selecionar uma TOP.

Essa consulta retorna os dados em uma tabela resumo com os seguintes totais do Parceiro no Sankhya:

- Títulos a vencer
- Títulos em aberto
- Títulos em atraso
- Limite de crédito total
- Limite de crédito mensal

Os dados consultados são os mesmos exibidos na tela “Ficha de Parceiros” e são consultadas nos serviços de API FichaParceiroSP.getIndicadores e FichaParceiroSP.getFatiasPendenciasFInanceiras do módulo /mgecom/.

![Imagem 58: Os dados consultados são os mesmos exibidos na tela “Ficha de Parceiros” e são consultadas nos serviços de API…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434654/8dfed52d7d91f9b8a7a78948cd0d/AD_4nXeshmQXJi8uutguq8YWjZBLF7V-UKQ6QgQfppWe1wX3yepVJsE3d5lXM8xMPXXT6zVA79Qn-plKZT0i8Uam4ocbV6bea62EwXvbxceCi23fuFIRQjQpIRVZp3EdOmSYZoa1whX0Mw?expires=1786536000&signature=1afdb7fc1fdf7c28150be74903af82533e260027d42e7a650a02abaa3b6e54f0&req=dSUlEs19mYdaXfMW3nq%2Bgbcyr15uJyGYuiwZzTX1W2upCUYKxfcEFcIi4yVj%0A%2BiXAGRI30FIDZqd3dKqJBXCpg3c%3D%0A)

Para que essa consulta seja possível na tela de edição de Proposta/Venda, é necessário que o campo “Detalhes Financeiros (Sankhya)” - ou o campo utilizado no seu lugar na configuração - seja inserido no modelo de documento da Proposta/Venda. O campo pode ficar oculto que a consulta ainda irá funcionar.

#### Consulta de restrições de TOP

Para as TOP’s do Sankhya que estão configuradas no Ploomes para utilização nas Propostas/Vendas é possível realizar a consulta das restrições/exceções da TOP na tela de edição da Proposta/Venda.

[GIF animado: Imagem 59: Para as TOP’s do Sankhya que estão configuradas no Ploomes para utilização nas Propostas/Vendas é possível realizar a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525785760/0dbe1a88e3f7775ebb1a56198d12/ConsultaRealTime_DetalhesFinanceiros_Proposta.gif?expires=1786536000&signature=0369536d1e50ab4c7228fade130d7c63adad1ee7b40498ea503cf0c7c9903ade&req=dSUlE852mIZZWfMW3nq%2Bgciik5cMvCkNNLPRPjIr%2BI%2FLe7GIzJ5cREaM3wpQ%0ANhYrhGTngTk3cQG8J8jl4TyzB5I%3D%0A)

Exemplo de consulta às restrições/exceções da TOP na tela de edição da Proposta após selecionar uma TOP.

Essa consulta retorna os dados em uma tabela resumo com os seguintes dados:

- Entidade: entidade que possui a restrição ou exceção com a TOP
- Restrição/Exceção: regra de negócio, se é uma exceção ou uma restrição
- Cadastros: código e descrição do cadastro relacionado a regra de negócio de restrição/exceção da TOP

No Sankhya, as restrições/exceções de TOP são uma regra de negócio importante e podem implicar no bloqueio da exportação de uma Proposta/Venda do Ploomes para o Sankhya caso alguma restrição/exceção não seja atendida.

As restrições podem ser de:

- Empresa
- Parceiro
- Tipo de Negociação
- Centro de Resultado
- Natureza
- TOP de Destino
- Produto/Grupo de Produto
- Usuário/Grupo de Usuário
- Perfil Principal
- Vendedor/Comprador
- Local
- Série

A consulta em tempo real às restrições/exceções de TOP não impede a seleção de opções restringidas pelo Ploomes, mas serve de referência para o preenchimento da Proposta/Venda.

Para que essa consulta seja possível na tela de edição de Proposta/Venda, é necessário que o campo “Detalhes de Restrições da TOP (Sankhya)” - ou o campo utilizado no seu lugar na configuração - seja inserido no modelo de documento da Proposta/Venda. O campo pode ficar oculto que a consulta ainda irá funcionar.

## 7.3 Produto da Proposta ou Produto da Venda

### 7.3.1 Configuração das consultas

A configuração das consultas em tempo real para a entidade de Produto da Proposta/Venda é realizada em background pela integração, com exceção das consultas de preço e imposto.

Para essas consultas configuradas em full background, são criados campos no Ploomes que recebem esses dados das consultas possíveis para Produto da Proposta/Venda. No entanto, é possível alterar o campo sugerido que receberá esses dados na tela de configuração da integração.

A principal configuração é realizada na criação de um campo do tipo desenvolvedor “Consulta única (Sankhya)”. Este campo possui a fórmula orquestradora das consultas de Produto da Proposta/Venda referente à valor unitário e impostos, determinando os gatilhos necessários para cada consulta possível.

A configuração das consultas de preço e impostos estão detalhadas neste artigo: [Consultas em tempo real pela integração Sankhya](https://intercom.help/ploomes_suporte/pt-BR/articles/11157483-consultas-em-tempo-real-pela-integracao-sankhya).

### 7.3.2 Consultas realizadas

#### Consulta de unidades de medida

Para os Produtos da Proposta/Venda que são inseridos no formulário de CPQ é possível realizar uma consulta em tempo real ao Sankhya para exibir as unidades de medida do Produto.

Essa consulta retorna a unidade de medida padrão do produto e também as unidades de medida alternativas vinculadas ao Produto/Serviço do Sankhya que foi integrado ao Ploomes como Produto.

---

**Engatilhamento da consulta**

Para essa consulta ser engatilhada é necessário selecionar um Produto da Proposta/Venda\*.

(\*) Obrigatório

---

[GIF animado: Imagem 60: (\*) Obrigatório](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525792977/e9840fd3ca0ac5f58cd169d10e97/ConsultaRealTime_ProdutoProposta_Unidade.gif?expires=1786536000&signature=eea93bb912b82396b72ba80ecd0710cb5f4d441443df1c93c06929dfb7ae85e4&req=dSUlE853n4hYXvMW3nq%2BgXVmeTXq2vqDCTzozhw73Nq%2BCVwRi3YJKgjKu6e%2B%0AqgnH1ekQW710Qmub2FPRe2q9g0g%3D%0A)

Essa consulta retorna uma lista de opções pré-cadastradas com as unidades de medida vinculadas ao Produto/Serviço no Sankhya.

Para que essa consulta seja possível no formulário de CPQ, é necessário que os campos “Consulta única (Sankhya)”, “Limpa opções (Sankhya)” e “Unidade de Medida (Sankhya)” - ou os campos utilizados no seu lugar na configuração - sejam inseridos no modelo de documento dentro do bloco de Produto da Proposta/Venda.

Os campo “Consulta única (Sankhya)” e “Limpa opções (Sankhya)” podem ficar ocultos que a consulta ainda irá funcionar.

É recomendado inserir o campo “Retorno consulta única (Sankhya)” de forma oculta para conseguir consultar o retorno recebido da consulta tem tempo real no Sankhya.

#### Consulta de controle

Para os Produtos da Proposta/Venda que são inseridos no formulário de CPQ é possível realizar uma consulta em tempo real ao Sankhya para exibir as opções de Controle do Produto.

Essa consulta retorna os Controles cadastrados para o Produto vinculados ao Produto/Serviço do Sankhya que foi integrado ao Ploomes como Produto.

---

**Engatilhamento da consulta**

Para essa consulta ser engatilha é necessário selecionar um Produto da Proposta/Venda\* e opcionalmente uma Unidade de Medida.

(\*) Obrigatório

---

Se a unidade de medida escolhida for a unidade de medida padrão, então serão exibidas as opções pré-cadastradas de todos os Controles possíveis para o Produto. Ou seja, possível também com todas as demais unidades de medida alternativas.

[GIF animado: Imagem 61: Se a unidade de medida escolhida for a unidade de medida padrão, então serão exibidas as opções pré-cadastradas de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525795314/c6990cbb5279db1bf887202c525d/ConsultaRealTime_ProdutoProposta_ControlePadrao.gif?expires=1786536000&signature=59f2a6db1c596adbadb09ec7b154cbf9d53826a3977917e6b7ebda90fde3698c&req=dSUlE853mIJeXfMW3nq%2Bgd1kSUBCOo7qWERlp3EKND%2B2m7OuLjPGRFMejNjR%0AyCcRXJ%2FBNi1f617bPOXC2tl%2FdSo%3D%0A)

Se a unidade de medida escolhida for a unidade de medida alternativa, então serão exibidas as opções pré-cadastradas específicas para os Controles possíveis para o Produto com a unidade de medida selecionada.

[GIF animado: Imagem 62: Se a unidade de medida escolhida for a unidade de medida alternativa, então serão exibidas as opções pré-cadastradas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525796266/700decef66829c4727582dad4513/ConsultaRealTime_ProdutoProposta_ControleAlternativo.gif?expires=1786536000&signature=1d002be2e0b53e34b1eb0d0701fb8039350cfa877c5dea221ed2b5220cdc6b78&req=dSUlE853m4NZX%2FMW3nq%2BgTa1CRyZIlyo0vgsMeKdQPRLcBykWWFkRsIbc%2B7y%0Ax%2BoNgX9U1uvqj2W6okkOMpwuud4%3D%0A)

Para que essa consulta seja possível no formulário de CPQ, é necessário que os campos “Consulta única (Sankhya)”, “Limpa opções (Sankhya)” e “Controle Produto (Sankhya)” - ou os campos utilizados no seu lugar na configuração - sejam inseridos no modelo de documento dentro do bloco de Produto da Proposta/Venda.

Os campos “Consulta única (Sankhya)” e “Limpa opções (Sankhya)” podem ficar ocultos que a consulta ainda irá funcionar.

É recomendado inserir o campo “Retorno consulta única (Sankhya)” de forma oculta para conseguir consultar o retorno recebido da consulta tem tempo real no Sankhya.

#### Consulta de estoque

Para os Produtos da Proposta/Venda que são inseridos no formulário de CPQ é possível realizar uma consulta em tempo real ao Sankhya para exibir uma tabela resumo com as informações de estoque disponível do Produto.

Essa consulta retorna uma tabela resumo com os dados de estoque do Produto/Serviço no Sankhya conforme os campos preenchidos no Ploomes.

---

**Engatilhamento da consulta**

Influenciam nessa consulta o preenchimento dos campos:

- Empresa
- Produto\*
- Unidade de Medida\*
- Controle
- Local
   (\*) Obrigatório

---

[GIF animado: Imagem 63: Local (\*) Obrigatório](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525797661/a61901bbdaeb2cce2472c87ffc67/ConsultaRealTime_ProdutoProposta_Estoque.gif?expires=1786536000&signature=f250427e5c46437aeb386af6dd7d40ee64d0b6f3782c441262960f74f36e9f45&req=dSUlE853modZWPMW3nq%2BgaCHB003I%2FSaQVqDru03yAluXhLwHDmVaijWRv53%0AFZgP%2FcePLDpAKB3V4AkHtIoVEUk%3D%0A)

Nessa tabela, vão ser exibidos em linhas os estoques por:

- **Empresa**
- **Local**
- **Controle**

E serão exibidos os totais das colunas de:

- **Estoque:** quantidade total do Produto em estoque
- **Reservado:** quantidade total reservada o Produto
- **Disponível:** quantidade total de estoque do Produto que está disponível

As quantidades exibidas são convertidas em função da unidade de medida selecionada. A conversão é feita pelo Sankhya, com base nos dados das entidades TGFEST (Estoque) e TGFVOA (Volume Alternativo) do Sankhya.

O campo de consulta ao Sankhya e seu respectivo retorno estão na configuração da integração:

![Imagem 64: O campo de consulta ao Sankhya e seu respectivo retorno estão na configuração da integração:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1524434636/6e95789254f1455b19f266cd5e48/AD_4nXdOEreohqKi9aRMmlWZM0PIZ9oEvywa-TN03KGA7k_ukbA1p1caOUm_j0tWx43MGVtS3PuSTgprCTSuUqx9SGptcnQ_yDJ0YVq5FN_kj38jIBDp02tIrrgF_M-yEZJopW9-1Ouqcg?expires=1786536000&signature=1543acb1a24c03cd478a8df0d28ca99279b549cbcbcfe08a3788eec291e37d66&req=dSUlEs19mYdcX%2FMW3nq%2BgT3iRSjDlyYeatVjQzLpQDuD7TIv7lVbDtRaJ1NJ%0AvCy7gJFz4mDliPN21B9qgKBDVc8%3D%0A)

Para que essa consulta seja possível no formulário de CPQ, é necessário que o campo “Detalhes de Estoque (Sankhya)” - ou o campo utilizado no seu lugar na configuração - seja inserido no modelo de documento dentro do bloco de Produto da Proposta/Venda.

O campo “Detalhes de Estoque (Sankhya)” não pode ficar oculto.

#### Consulta de valor unitário

Para os Produtos da Proposta/Venda que são inseridos no formulário de CPQ é possível realizar uma consulta em tempo real ao Sankhya para obter o valor unitário do Produto.

Essa consulta retorna o valor unitário do Produto/Serviço do Sankhya integrado como Produto no Ploomes com base nos campos informados na Proposta/Venda (como Cliente, TOP, Tipo de Negociação, etc.) e no Produto da Proposta/Venda (Quantidade, Controle e Unidade de Medida) conforme a configuração de consulta de preço realizada.

[GIF animado: Imagem 65: Essa consulta retorna o valor unitário do Produto/Serviço do Sankhya integrado como Produto no Ploomes com base nos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525799299/5db4b27e1056c53fa13c3df22efc/ConsultaRealTime_ProdutoProposta_ValorUnitario.gif?expires=1786536000&signature=7952a1dabae18fc9f0a71fb261c4db007339b17b5113e31d4597405ac46f8360&req=dSUlE853lINWUPMW3nq%2BgeWptFRuj0UkDrnsTenXovgkY1GMlO1etykKqr1h%0AaELl2EkB6h%2Fx%2BDpeYHzvirJt93Q%3D%0A)

Exemplo de consulta de Preço (Valor Unitário) em tempo real ao Sankhya de um Produto integrado na edição de uma Proposta após a alteração dos campos de Produto da Proposta que influenciam no preço.

---

**Engatilhamento da consulta**

Para essa consulta ser engatilhada, portanto, pode ser necessário informar:

- Na Proposta/Venda:

  - Empresa\*
  - Cliente\*
  - Tipo de Negociação\*
  - Natureza\*
  - Centro de Resultado\*
  - Responsável\*
  - TOP\*
  - Outros campos eventualmente configurados.
- No Produto da Proposta/Venda:

  - Produto\*
  - Unidade de medida\*
  - Controle
  - Local\*
  - Quantidade\*
  - Outros campos eventualmente configurados.

(\*) Obrigatório

---

A consulta retorna o valor unitário definido no Sankhya conforme preferência de regra de tabela de preço ou do preço dinâmico da conta Sankhya integrada.

Para que essa consulta seja possível no formulário de CPQ, é necessário que os campos “Consulta única (Sankhya)”, “Limpa opções (Sankhya)”e “Valor Unitário (Sankhya)” (ou o campo configurado para receber o valor unitário consultado) sejam inseridos dentro do bloco de Produto da Proposta/Venda, bem como todos os campos configurados para as consultas.

Os campos “Consulta única (Sankhya)” e “Limpa opções (Sankhya") podem ficar ocultos que a consulta ainda irá funcionar.

#### Consulta de impostos

Para os Produtos da Proposta/Venda que são inseridos no formulário de CPQ é possível realizar uma consulta em tempo real ao Sankhya para obter os dados de impostos do Produto.

Essa consulta retorna os valores de Valor Base, Alíquota e Valor do Imposto do Produto/Serviço do Sankhya integrado como Produto no Ploomes com base nos campos informados na Proposta/Venda e no Produto da Proposta/Venda.

---

\*O NUNOTA Modelo utilizado é sempre o NUNOTA configurado para as consultas em tempo real de impostos.

**Engatilhamento da consulta**

Para essa consulta ser engatilhada, portanto, pode ser necessário informar os valores dos campos abaixo, conforme a configuração realizada:

- Na Proposta/Venda:

  - Nota Modelo\*
  - Empresa\*
  - Cliente\*
  - TOP\*
  - Finalidade da Operação
  - Valor do Frete
  - Valor do Seguro
  - Valor Outros
- No Produto da Proposta/Venda:

  - Produto\*
  - Unidade de medida\*
  - Quantidade\*
  - Valor unitário sem desconto\*
  - Percentual de desconto do Produto

(\*) Obrigatório

---

[GIF animado: Imagem 66: (\*) Obrigatório](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1525800993/8e2437c2e83bd54f78bd5d6a5a2a/ConsultaRealTime_ProdutoProposta_Impostos.gif?expires=1786536000&signature=66136e59644b62f650bc8b850e5dc24d401d1238c55aaac5a1aa015758924b2a&req=dSUlE8F%2BnYhWWvMW3nq%2BgT9XWngrOeBvH%2FDJk%2Bc0WajsKcetRTUPl%2F5N1wxH%0AAGbQkJuvlrEKzDnCHtX6DprPqik%3D%0A)

O Sankhya pode ter diversos impostos configurados, portanto os retornos ou não dos impostos dependem diretamente da configuração dos parâmetros fiscais do Sankhya.

Os campos consultados no Sankhya e retornados no Ploomes são os seguintes:

- PIS (Base, Alíquota e Valor)
- COFINS (Base, Alíquota e Valor)
- ICMS (Base, Alíquota e Valor)
- IPI (Base, Alíquota e Valor)
- ST (Base, Alíquota e Valor)
- ISS (Base, Alíquota e Valor)
- IRPJ (Base, Alíquota e Valor)
- CPP (Base, Alíquota e Valor)
- INSS (Base, Alíquota e Valor)
- IRF (Base, Alíquota e Valor)
- CSSL (Base, Alíquota e Valor)
- Valor Total de Desoneração
- Valor FCP
- Valor DIFAL Remetente
- Valor DIFAL Destinatário

Para que essa consulta seja possível no formulário de CPQ, é necessário que os campos “Consulta única (Sankhya)” e “Limpa opções (Sankhya)” sejam inseridos dentro do bloco de Produto da Proposta/Venda. Também devem ser inseridos os respectivos campos dos impostos que forem configurados.

**Por exemplo:** caso seja necessário utilizar os dados de IPI, devem ser inseridos os campos configurados para receber o retorno da consulta desse imposto.

Os campos “Consulta única (Sankhya)” e “Limpa opções (Sankhya") podem ficar ocultos que a consulta ainda irá funcionar. É recomendado inserir o campo “Retorno consulta única (Sankhya)” de forma oculta para conseguir consultar o retorno recebido da consulta tem tempo real no Sankhya.

---

**Pontos de atenção**

- Os campos que recebem o retorno das consultas de impostos não são campos mapeados, portanto, tem o comportamento de campos não mapeados. Isto é, ao receber edições do Sankhya para o Ploomes, as informações podem ser apagadas.

  - No entanto, é possível mapear esses campos na seção da entidade de Produto da Proposta/Venda, de modo que ao receber importações do Sankhya para o Ploomes os dados venham preenchidos e sejam salvos no Ploomes.
- Preferências e regras configuradas no Sankhya podem impactar no cálculo de impostos via API. Para o cálculo da consulta de impostos retornar os dados de forma coerente com o Frontend Sankhya, o parâmetro das TOP’s para Cálculo de ICMS, IPI e ISS deve estar preenchido com a opção “Calcula e não digita”.

---

## 8 Ações em Tempo Real

É possível configurar e realizar as ações de **Confirmar e/ou Faturar** (apenas faturamento direto) CabecalhosNota do Sankhya através do Ploomes para os documentos que estejam integrados.

Essa funcionalidade está detalhada no artigo: [Ações em tempo real pela integração Sankhya](https://intercom.help/ploomes_suporte/pt-BR/articles/11993949-acoes-em-tempo-real-pela-integracao-sankhya).

---

## 9 Recomendações

Abaixo, listamos recomendações técnicas para o bom funcionamento da integração:

- Configure o tempo mínimo de inatividade da sessão do usuário de integração para **no mínimo 5 minutos**, preferencialmente mais.
- Evite utilizar **campos calculados ou virtuais** no mapeamento.
- Mantenha o ERP Sankhya com **estrutura de dados limpa e padronizada**.
- Faça a ativação e configuração da integração **com acompanhamento técnico da Ploomes**.
- Garanta que o ambiente Sankhya permita conexões externas via API a partir do IP ou rede do Ploomes.
- Configure **certificados SSL** válidos para segurança da comunicação.
- **Evite duplicidades de cadastros**, principalmente Parceiros e Produtos.
- Verifique se o **usuário de integração tem acesso** total às tabelas integradas e as **permissões necessárias** para a integração.
- Recomendamos a utilização Sankhya hospedado em **servidor em nuvem homologada pela Sankhya**, pois será uma infraestrutura adequada e validada pela Sankhya, garantindo estabilidade e conectividade ideal para a comunicação via API.
- **Não recomendamos** a integração com Sankhya hospedado em **servidor local**, pois é mais propício aos problemas de conectividade via API, o que afeta diretamente a experiência e performance da integração. No entanto, **este não é um impeditivo** para realizar a integração.

  - Em caso de servidor local (ou nuvem própria), reforçamos o requisito de infraestrutura mínima recomendada pela Sankhya: [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045373654-Premissas-e-pré-requisitos-para-implantação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045373654-Premissas-e-pr%C3%A9-requisitos-para-implanta%C3%A7%C3%A3o).
  - A infraestrutura mínima não necessariamente é o ideal para todos os Sankhyas, pois existem dependências de performance no acesso aos dados via API como:

    - Quantidade de campos mapeados: quanto mais campos mapeados para a integração, maior será o tempo de processamento na consulta de dados ao Sankhya.
    - Quantidade de campos calculados: os campos calculados no Sankhya tornam o processo de consulta aos dados mais lento (pois requer o cálculo durante a consulta), portanto quanto mais campos calculados maior será o tempo de processamento.
    - Quantidade de ItemNota em CabecalhoNota: quanto mais itens existirem nos Orçamentos/Pedidos de Venda/Notas de Venda, maior será o tempo de processamento para a importação desses dados.
    - Internet disponível: a conectividade em servidores locais dependem muito mais da banda e internet disponível no servidor.

---

## 10 Limitações e observações importantes

## Limitações Gerais

- A API do Sankhya possui uma limitação de 1000 requisições por minuto.
- O acesso ao Sankhya via API Gateway tem a limitação de até 2 minutos no tempo de processamento na infraestrutura do cliente Sankhya. Portanto, caso a infraestrutura do cliente demore mais do que 2 minutos para retornar alguma consulta, ocorrerá timeout - o que pode ser um impeditivo para a utilização da integração, conforme artigo Sankhya: [https://developer.sankhya.com.br/reference/boas-práticas-para-integração](https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o).
- O Pooling (varredura por atualizações no Sankhya) é executado a cada 5 minutos; este é o intervalo de verificação, não o tempo para integrar cada item.
- Não há tempo máximo garantido para um item integrar, pois depende do volume de informações importadas.
- Eventos de integração negados por filtros não aparecem na tela de Registros da Integração.
- Ao desativar e reativar a integração, a tela de Registros da Integração "limpa" os eventos anteriores, exibindo apenas os da versão vigente.
- Usuários sem perfil de administrador só acessam os registros pelo ícone no menu superior direito e só visualizam registros de criações/edições feitas por eles no Ploomes.
- Não é possível importar campos com dados binários que contenham conteúdos como anexos, imagens etc.

## Mapeamento de Campos

- Campos virtuais do Sankhya que não existem na entidade principal integrada não podem ser mapeados.
- Campos de mapeamento fixo não podem ter seu tipo de campo alterado no Ploomes.
- Existe um limite de criação de 40.000 opções pré-cadastradas em campos do Ploomes.
- Quanto mais campos forem adicionados no mapeamento, mais lenta será a velocidade de processamento de dados (importação e exportação). Isso também afeta o tempo da carga inicial.
- O mapeamento de campos calculados do Sankhya afeta bruscamente a velocidade de importação.
- Se um campo desejado não estiver mapeado e for incluído após a carga inicial, os dados desse campo não serão preenchidos automaticamente para os cadastros já integrados, apenas para novas importações/exportações.
- Se um campo mapeado (do Ploomes ou Sankhya) for deletado (especialmente durante a carga inicial), a carga inicial falhará e retornará erro.
- Alterações em nomes de campos, obrigatoriedades ou opções pré-cadastradas em campos mapeados com a integração ativa podem exigir nova compatibilização ou alteração do mapeamento.
- Ao editar a integração, se um campo mapeado, campo de filtro, opção pré-cadastrada em filtro, TOP ou Modelo de Documento for deletado ou editado, a edição da integração não será aplicada e exigirá correção.
- Apenas os campos abaixo são convertidos automaticamente como opções pré-cadastradas no Ploomes. Outros campos do Sankhya ausentes na lista abaixo serão importados apenas com sua chave externa (ID) em um campo de número inteiro.

  - Empresa (TGFCAB)

  - TOP (TGFCAB)

  - Tipo de Negociação (TGFCAB)

  - Natureza (TGFCAB)

  - Centro de Resultado (TGFCAB)

  - Status da Nota (TGFCAB)

  - Transportadoras (TGFCAB)

  - Local (TGFITE)

  - Controle (TGFITE)

  - Unidade de Medida (TGFITE)

  - Classificação ICMS (TGFPAR)

## Habilitação e Carga Inicial

- A carga inicial não pode ser cancelada pelo usuário do Ploomes.
- Não é possível aplicar filtros durante o processo de carga inicial se ela não for interrompida por erro.
- Não é recomendado executar a carga inicial sem aplicar filtros de recebimento e sem conhecimento do volume de dados no Sankhya.
- Limitações no servidor Sankhya, erros na API ou timeout de requisições (acima de 120 segundos) podem paralisar a carga inicial.
- Se o Token de integração for inativado ou removido durante a carga inicial ou uso, nenhuma operação de integração será possível.
- Ao reativar a integração, todo o processo de carga inicial precisa ser feito novamente, mesmo para cadastros já existentes no Ploomes, e tende a ser mais demorado devido às tentativas de pareamento.
- Quanto mais cadastros existirem no Ploomes, maior será o tempo de processamento da carga inicial devido às tentativas de pareamento.
- Para ativar a integração nas entidades de Propostas e Vendas, é necessário contratar o módulo de CPQ.

## Configuração e Edição

- Ações de alteração na configuração da integração podem causar impactos significativos e são irreversíveis.
- Alterações de configuração realizadas após a primeira ativação não impactam nos dados retroativos.
- Os cadastros que estiverem na fila de processamento da integração não sofrem os impactos de edições aplicadas; apenas os processados após a nova configuração estar vigente.
- Não é possível desativar a integração se estiver no modo de edição (Draft). É necessário descartar as edições primeiro.
- É necessário clicar em "Salvar edições" no final de cada seção editada antes de clicar em "Aplicar edições" para que as alterações sejam salvas e aplicadas. Caso contrário, o mapeamento pode não ficar salvo.
- Durante a aplicação de edição, a barra de porcentagem de processamento é simbólica e pode parecer travada; o processamento real deve ser verificado via network. Há uma proteção para não haver filas de processamento concomitantes.

## Limitações por Entidade / Funcionalidade

- Parceiro (Cliente PJ e PF) / Empresa / Pessoa:

  - Se uma Empresa foi importada do Sankhya e o Parceiro PJ for apagado no Sankhya, o pareamento continua valendo.
  - Mesmo que o Parceiro mude seu status para Inativo, se já estiver integrado, continuará podendo enviar e receber atualizações.
  - Se existirem vários Parceiros PJ no Sankhya com o mesmo CNPJ, a Empresa no Ploomes será integrada com o Parceiro que tiver o menor código (CODPARC).
  - Campos de tabelas personalizadas não são integrados, a menos que sejam enviados na tabela TGFPAR.
  - O mapeamento de bairros, endereço e cidade é feito pelo nome, não pelos códigos (CODBAI, CODEND, CODCID). Ao enviar edições de um parceiro integrado, pode-se mudar o CODBAI, CODEND ou CODCID vinculado a ele no Sankhya se houver cadastros duplicados com o mesmo nome no Sankhya.
  - O CNPJ já estar cadastrado no Sankhya como Pessoa Física impede a criação de um novo Parceiro PJ.
  - Problemas com cadastro de endereço (Cidade, Bairro ou Endereço) no Sankhya podem causar falha na criação.
  - Se uma Empresa no Ploomes perder um campo obrigatório no Sankhya (ex: Nome ou Cidade), a edição poderá falhar.
  - Edições em campos não mapeados não geram atualização no Sankhya.
  - Se um cliente Pessoa (Parceiro PF) integrado no Sankhya for alterado para Pessoa Jurídica, criará um novo cliente Empresa no Ploomes com o mesmo código de Parceiro, pois o Ploomes não converte PF para PJ. Os cadastros de Pessoa Física "se tornam órfãos".
  - A edição de telefone do Parceiro no Sankhya tem o comportamento de adicionar mais um telefone no Ploomes em vez de alterar, devido à limitação do Sankhya que integra apenas a primeira posição de um tipo de telefone.

- Contato de Cliente:

  - Somente são integrados Contatos de Cliente de Parceiros Pessoa Jurídica. Eles precisam ter um Parceiro integrado.
  - No Sankhya, se um contato é contato de 2 parceiros, é necessário cadastrá-lo em cada parceiro.
  - A integração preenche somente o Contato da Venda ou da Proposta, não preenche o contato do Negócio.

- Produto / Serviço:

  - Não é possível exportar Produtos/Serviços do Ploomes para o Sankhya. A via de integração é somente Sankhya → Ploomes.
  - Produtos criados manualmente no Ploomes não são enviados ao Sankhya em vendas/propostas porque não estão integrados.
  - No primeiro recebimento, são recebidos somente Produtos/Serviços ativos no Sankhya. Após a integração, edições podem ser recebidas mesmo se o produto ficar inativo.
  - A deleção de um Produto/Serviço no Sankhya ou de um Produto no Ploomes não é refletida no outro sistema .
  - Produtos/Serviços não importados pela via principal (ex: por filtro) ainda podem ser importados se estiverem em um Orçamento, Pedido de Venda ou Nota de Venda importado. O grupo desse produto também é integrado.
  - Produtos/Serviços não possuem campo para informação de valor unitário na entidade; isso é definido na geração de documento.
  - A consulta em tempo real de Controle do Produto somente funciona se o Controle no Sankhya estiver cadastrado como "Lista" (TIPCONTEST = 'S'). A integração só olha informações de Controles de GET Produto ou GET Volume Alternativo, independente da configuração TIPCONTEST.
  - A consulta em tempo real de Estoque exige que o campo "Detalhes de Estoque (Sankhya)" (ou mapeado) não esteja oculto no modelo de documento.
  - Na visualização do estoque, podem aparecer Empresas/Locais repetidos, refletindo dados retornados pela consulta no Sankhya (ex: Poder Terceiros e Poder Próprio), mas não estão realmente duplicados; a coluna "Poder" não é exibida no Ploomes.

- Orçamento / Pedido de Venda / Nota de Venda:

  - Não é possível exportar Notas de Venda do Ploomes para o Sankhya.
  - Os campos mapeados para Pedidos de Venda são reutilizados para a importação de Notas de Venda.
  - As TOPs de Tipo de Movimento = "V" (Notas de Venda) só são exibidas como opção para configuração na seção de Notas de Venda.
  - Os filtros configurados nos modelos de documento do Ploomes (filtros de seção/blocos de produto da proposta) são ignorados na importação de Propostas/Vendas vindas do Sankhya. A integração divide em blocos padrão.
  - Para Propostas/Vendas de Parceiros Pessoa Física, não se deve adicionar o contato no campo "Contato" da proposta; o cliente Pessoa Física deve ser apenas o Cliente do Card.
  - Orçamentos/Pedidos de Venda de Contato de Cliente exigem que o Parceiro Pessoa Jurídica vinculado ao contato seja inserido no Negócio/Venda/Proposta para poder integrar.
  - Quando edições em campos de produto da Proposta/Venda são enviadas ao Sankhya, a API do Sankhya remove todos os produtos e tenta reinseri-los. Se ocorrer um erro durante a reinserção, os produtos podem ser removidos e não adicionados novamente, resultando em um documento sem produtos. Este é um comportamento de limitação da API do Sankhya.
  - As edições no Sankhya são capturadas pelo Pooling somente se o campo DTALTER for alterado. Edições feitas diretamente no banco de dados ou por fórmulas que não atualizem o DTALTER não serão enviadas para o Ploomes.
  - Quando edições vindas do Sankhya são recebidas, o preenchimento de campos de Produto da Proposta (ou Produto da Venda) que não estão mapeados na integração é removido. A integração recria os produtos preenchendo apenas os campos mapeados.
  - Edições feitas no Ploomes só entram na fila de envio se houver alterações em campos mapeados.
  - Se uma edição no Ploomes for barrada inicialmente por um filtro de envio, e o campo do filtro for editado para atender à condição, a edição original nos outros campos mapeados ficará armazenada em uma tabela de itens bloqueados na exportação por até 30 dias e podem ser enviados ao Sankhya normalmente após uma nova edição passar a atender o filtro. Após esse período serão descartados.
  - Vendas/Orçamentos só integram se o Cliente selecionado já estiver integrado ao Sankhya.
  - Duplicar uma proposta integrada no Ploomes sem remover o Nro. Único (Sankhya) impede a exportação do documento para o Sankhya.
  - Vendas e Propostas só vinculam a um Negócio já existente no Ploomes se o campo de Id de Negócio estiver mapeado e preenchido na CRIAÇÃO. O valor preenchido no campo ID do Negócio é considerado apenas na criação de importação; em edições, o valor vindo nesse campo não é usado.
  - Edições/alterações de Parceiros de Propostas/Negócios já existentes no Ploomes são refletidas no Ploomes.
  - Não é realizada confirmação nem faturamento automático de Orçamentos ou Pedidos de Venda no Sankhya pela integração, somente através de ações manuais.

- TOPs:

  - Uma TOP só pode ser utilizada em uma entidade escolhida (Proposta, Venda ou Nota Fiscal); não é possível selecionar a mesma TOP para múltiplos tipos de documento.
  - Na seleção de TOPs para Pedido de Venda e Orçamentos, são exibidas todas as TOPs ativas, exceto as de Tipo de Movimento "V".

## Consultas em Tempo Real

- As informações consultadas em tempo real não estão armazenadas no Ploomes. Portanto, não é possível utilizar esses dados para automações, formulários ou outras ações que requeiram um dado armazenado no banco de dados do Ploomes.
- O campo de consulta ao Controle do Produto só exibe opções se o Controle no Sankhya estiver cadastrado como "Lista" (TIPCONTEST = 'S'), apesar da integração olhar para outros locais na API.
- Os campos de consulta de impostos da integração no Ploomes NÃO NECESSARIAMENTE SÃO CAMPOS MAPEADOS. Eles existem para receber o retorno da consulta feita no Sankhya.
- Os valores dos campos de consulta (Detalhes Financeiros, Restrições de TOP, Detalhes de Estoque, Valor Unitário, Produto Integrado, Impostos) têm seu preenchimento removido em edições recebidas pelo Sankhya. Isso ocorre porque esses campos não existem no Sankhya e não são trazidos na importação; a integração recria os produtos preenchendo apenas os campos mapeados.
- Se a configuração da TOP no Sankhya estiver marcada como "Calcula e Digita” em “Cálculo de ICMS, IPI e ISS”, não retornará corretamente os impostos na integração Sankhya nem por API. Precisa ser trocado para "Calcula e Não Digita”.

---

## 11 FAQ - Perguntas Frequentes

1. **A integração entre o Ploomes e o Sankhya é bidirecional?**

   - **Sim**, a integração é bidirecional, permitindo a importação e exportação de dados entre os sistemas, com exceção dos cadastros de Produtos, Grupos de Produtos e Vendedores, que possuem integração unidirecional (Sankhya > Ploomes).
2. **Quais dados podem ser importados do Sankhya para o Ploomes?**

   - Dados como **parceiros clientes**, **produtos/serviços, grupos de produtos/serviços**, **vendedores**, **orçamentos**, **pedidos de venda**, e **notas de venda** podem ser importados.
3. **Posso exportar Notas de Venda do Ploomes para o Sankhya?**

   - **Não**, a exportação de Notas de Venda do Ploomes para o Sankhya não é suportada.
4. **Como são realizadas as consultas em tempo real durante a criação de documentos?**

   - Durante a criação de propostas ou vendas no Ploomes, o sistema realiza consultas em tempo real ao Sankhya para obter **preço**, **estoque**, e **impostos dos produtos, limites de crédito de Parceiros e restrições de TOP**.
5. **O que acontece se eu cancelar ou excluir um documento no Sankhya?**

   - O **cancelamento** de documentos no Sankhya pode ser sincronizado como uma deleção no Ploomes, desde que o gatilho de importação de cancelamento esteja habilitado. O mesmo comportamento ocorre para deleções de documentos, que dependem de gatilho específico estar ativo.
6. **Posso configurar quais dados serão importados ou exportados?**

   - **Sim**, a configuração de filtros e mapeamentos permite personalizar quais dados serão importados ou exportados entre os sistemas. Campos virtuais do Sankhya não podem ser utilizados no mapeamento.
7. **A integração pode ser utilizada para importar dados históricos de documentos antigos no Sankhya?**

   - **Sim**, a integração importa os dados históricos do Sankhya para o Ploomes durante a carga inicial na ativação da integração somente. Após a ativação, a integração somente trabalha com dados criados ou editados desde então.
8. **Como posso garantir que o estoque no Ploomes esteja sempre atualizado?**

   - A atualização de **estoque** deve ser gerida no **Sankhya**. A integração realiza consultas em tempo real ao ERP para refletir o estoque disponível no Ploomes.
9. **É possível editar documentos no Sankhya após a exportação para o Ploomes?**

   - **Sim**, mas é importante que as edições sejam feitas com cautela, pois a sincronização de alterações pode gerar inconsistências, especialmente se ocorrerem edições simultâneas.
10. **Quais limitações existem para o mapeamento de campos?**

    - **Campos virtuais no Sankhya não podem ser mapeados**. Apenas campos existentes fisicamente nas entidades integradas e em tabelas complementares (com relacionamento 1-1) podem ser sincronizados.
11. **O que devo fazer se os dados não estiverem sendo importados corretamente?**

    - Verifique se os campos obrigatórios estão preenchidos corretamente no **Sankhya** e se os **gatilhos e filtros** da integração estão configurados corretamente.
12. **Há algum limite para o número de opções pré-cadastradas nos campos?**

    - **Sim**, o Ploomes suporta até **40.000 opções** pré-cadastradas em campos do tipo lista. Exceder esse limite pode causar falhas. Não há atualização periódica automática das opções pré-cadastradas importadas do Ploomes para o Sankhya.
13. **A integração oferece suporte a customizações avançadas realizadas no Sankhya?**

    - **Não**, a integração suporta apenas campos e dados que estão presentes nas entidades principais do Sankhya integradas. Customizações profundas podem exigir desenvolvimento adicional.
14. **Quais problemas podem ocorrer se houver falha na sincronização de dados?**

    - A falha pode ocorrer devido a **edições simultâneas** nos documentos, **campo obrigatório não preenchido** ou **problemas de conectividade**. É importante monitorar a API e garantir a integridade dos dados antes da sincronização.
15. **É possível realizar a integração com Views criadas no Sankhya ?**

    - **Não.** Não é possível realizar integração com Views pela integração. Caso seja necessário deverá ser feito um desenvolvimento adicional personalizado.
