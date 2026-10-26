---
id: "5874837664023"
titulo: "Importador de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-23T11:19:59Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "Importação", "Empresas", "br.com.sankhya.importadorDados", "Importador de Dados", "Processo de Importação de Dados", "Implantação"]
---

# Importador de Dados

| ``` ![Imagem 1: Módulo: Configurações > Avançado Versão disponível: A partir da 4.11](https://ajuda.sankhya.com.br/hc/article_attachments/42311144231447) Módulo: Configurações > Avançado            ![Imagem 2: Módulo: Configurações > Avançado Versão disponível: A partir da 4.11](https://ajuda.sankhya.com.br/hc/article_attachments/42311127718935) Versão disponível: A partir da 4.11 ``` |
| --- |

---

**Importante:** os procedimentos e regras apresentados nesse documento, bem como a utilização/execução do Importador de dados são direcionados para a equipe de Implantação da Sankhya.

O Importador de dados disponibiliza os templates dos cadastros e movimentações suportados no processo. Através desses templates, com os dados do cliente provenientes do seu sistema legado, será possível submetê-los na importação, populando a base do Sankhya Om com as informações do cliente que está sendo implantado.

Dessa forma, é eliminada a necessidade de input manual dos cadastros e movimentações que são suportados,  podendo esse tempo ser direcionado às correções de inconsistências dos dados legados, configurações específicas para o cliente, bem como a entrada dos dados que não é possível tratar via importação.

Para utilizar o Importador de dados, você deverá criar e habilitar o parâmetro **"IMPDADOS"** nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834) do sistema. Além disso, é necessário que o Sankhya Om seja acessado com o usuário SUP, ou que a tela seja liberada para o usuário que irá realizar as importações.

O parâmetro deve ser criado de acordo com as seguintes regras:

**Chave:** IMPDADOS

**Descrição:** IMPDADOS

**Módulos do Sistema:** Configurações

**Aba:** Diversas

**Tipo:** Lógico

**Ligado/Desligado:** Ligado

![Imagem 3: Ligado/Desligado: Ligado](https://ajuda.sankhya.com.br/hc/article_attachments/5888623223575)

```
         ![Imagem 4: Ligado/Desligado: Ligado](https://ajuda.sankhya.com.br/hc/article_attachments/42311144235031) A partir da versão 4.12, para utilizar essa tela, é necessário ter sua liberação
                                                 através da tela Acessos - Importador de Dados.
```

Realizado o passo anterior, basta acessar o Sankhya Om no menu **"Configurações > Avançado > Importador de Dados"** ou realizar a busca da tela no campo de pesquisa:

[GIF animado: Imagem 5: Realizado o passo anterior, basta acessar o Sankhya Om no menu "Configurações > Avançado > Importador de Dados" ou…](https://ajuda.sankhya.com.br/hc/article_attachments/5900109495447)

O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos que devem ser realizados após a importação:

| [![Imagem 6: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144237719)](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#baixartemplates) | ![Imagem 7: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144238615) | [![Imagem 8: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144239127)](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento) | ![Imagem 9: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144238615) | [![Imagem 10: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311127723031)](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#importardados) |
| --- | --- | --- | --- | --- |
|  |  |  |  | ![Imagem 11: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144241431) |
| [![Imagem 12: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144243223)](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ap%C3%B3saimporta%C3%A7%C3%A3o) |  | ![Imagem 13: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144243991) |  | [![Imagem 14: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311127726487)](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#historicodeimporta%C3%A7%C3%A3o) |

| ![Imagem 15: O processo de importação contempla 4 etapas. Abaixo, trataremos sobre cada uma delas e também sobre os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42311127727127) |
| --- |

###

### Baixar Templates

A primeira etapa a ser realizada para a importação dos dados de um novo cliente, é o download dos templates, que podem ser acessados na aba **"Baixar Templates"** da tela Importador de dados. Nesta aba é possível visualizar dois padrões para a importação, indicados pela coluna **"Padrão"** :

![Imagem 16: A primeira etapa a ser realizada para a importação dos dados de um novo cliente, é o download dos templates, que podem…](https://ajuda.sankhya.com.br/hc/article_attachments/5889138723607)

Os templates sinalizados com a informação **"Sim"**, são importações com tratativas específicas, que possibilitam realizar o relacionamento de dados entre templates, eliminando a necessidade de importar um template, capturar os códigos do Sankhya-Om que foram gerados para os registros, para posteriormente utilizá-los em outros templates. Além disso, é possível realizar o download do template contendo somente as colunas essenciais, ou do template contendo todas as colunas.

Já os templates sinalizados com a informação **"Não"**, não dispõem das tratativas específicas citadas acima, ou seja, para o relacionamento de dados, é necessário utilizar os códigos do Sankhya-Om para os registros. Com relação ao download do template, ao clicar sobre linha será efetuada a baixa do template com todas as colunas.

| ``` ![Imagem 17: Para mais detalhes sobre os relacionamentos de dados na importação, consulte a seção ID’s externos .](https://ajuda.sankhya.com.br/hc/article_attachments/42311144246551) Para mais detalhes sobre os relacionamentos de dados na importação, consulte a seção ID’s externos. ``` |
| --- |

Ainda na aba Baixar Templates, é possível visualizar dois tipos de templates para download através da coluna **"Tipo"**,  o de **"Tabelas"** e de **"Entidades"**.

![Imagem 18: Ainda na aba Baixar Templates , é possível visualizar dois tipos de templates para download através da coluna "Tipo" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/5889196526359)

Os Templates de Tabelas são arquivos zip, contendo um arquivo csv separado por (**;**), que é o template das tabelas e um arquivo HTML com as descrições e orientações a respeito das colunas presentes no template. Este tipo de template se aplica tanto para os templates que seguem o Padrão, quanto para os que não seguem. Atente-se para as dependências existentes entre as tabelas para que a importação seja possível, pois, caso contrário, ocorrerão falhas no processo.

Já os Templates de Entidades, tratam-se de arquivos zip que contém o conjunto de arquivos csv de Templates de Tabelas que se relacionam para o correto cadastro de uma determinada entidade, como por exemplo, o [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), que depende dos cadastros de [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), [Bairros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599814-Bairro), [Contatos de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113333-Contatos), entre outros. Este tipo de template esta disponível exclusivamente para as importações que seguem o Padrão. Além do conjunto de templates de tabela, o arquivo zip também possui o arquivo HTML contendo as descrições e orientações a respeito das colunas presentes nos templates.

Os templates de entidades disponíveis atualmente são:

| **Empresas** | - Cidades - Bairros - Endereços | - Empresas - Empresas do financeiro | |
| --- | --- | --- | --- |
| **Parceiros** | - Cidades - Bairros - Endereços - Empresas | - Vendedores - Parceiros - Contatos de Parceiros | |
| **Produtos** | - Cidades - Bairros - Endereços - Empresas - Grupo de produtos - Vendedores - Parceiros | - Produtos - Unidades - Unidades alternativas - Descontos promocionais - Descontos por quantidade - Tabela de preços - Preços por produto | |
| **Tipos de Negociação** | - Tipos de negociação - Parcelas dos tipos de negociação - Tipos de títulos | |  |
| **Dados Bancários** | - Bancos - Agências bancárias - Contas bancárias |  |  |

A aba Baixar Templates permite também que você realize a busca dos templates de tabelas e entidades no campo de pesquisa, a partir das suas descrições. Para fazer essa busca, é necessário que seja informado o termo a ser pesquisado e, na sequência, pressionado o **"Enter"** ou um clique sobre o ícone da lupa. Assim, a busca será realizada e os registros encontrados serão exibidos na grade:

[GIF animado: Imagem 19: A aba Baixar Templates permite também que você realize a busca dos templates de tabelas e entidades no campo de…](https://ajuda.sankhya.com.br/hc/article_attachments/5889411192343)

Quando você identificar qual modelo deseja baixar, basta clicar duas vezes sobre ele. Neste momento, poderão ocorrer duas situações:

Caso o template siga o Padrão, será aberto um pop-up com duas opções para seleção, sendo **"Template apenas com as colunas essenciais"**, que possibilita realizar o download do template contendo apenas as colunas que são de preenchimento essencial, e a opção **"Template com todas as colunas"**, que permite baixar o template contendo todas as colunas existentes para a tabela ou entidade em questão. Assim, após selecionar a opção desejada, clique no botão **"Baixar"** para que o download seja realizado. Observe o procedimento abaixo:

[GIF animado: Imagem 20: Caso o template siga o Padrão , será aberto um pop-up com duas opções para seleção, sendo "Template apenas com as…](https://ajuda.sankhya.com.br/hc/article_attachments/5889596453143)

Do contrário, se o template não seguir o Padrão, o download do arquivo .zip já será iniciado, uma vez que templates sem o Padrão possuem apenas a opção de download do arquivo contendo todas as colunas da tabela.

[GIF animado: Imagem 21: Do contrário, se o template não seguir o Padrão , o download do arquivo .zip já será iniciado, uma vez que templates…](https://ajuda.sankhya.com.br/hc/article_attachments/5889694927639)

**Observação:** no caso do download de [Templates de Entidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#templatesdeentidades), o arquivo baixado será um zip  contendo os templates csv das tabelas que compõem a entidade e o HTML **"Leia-me"** com as informações das tabelas:

[GIF animado: Imagem 22: Observação: n o caso do download de Templates de Entidades , o arquivo baixado será um zip contendo os templates csv…](https://ajuda.sankhya.com.br/hc/article_attachments/5889911189527)

**Importante:** o arquivo Leia-me contém as informações necessárias para te orientar e sanar dúvidas sobre o preenchimento dos modelos. As informações disponibilizadas no arquivo são:

- **Tabela:** Trata-se do nome da tabela que o template pertence.
- **Coluna:** Apresenta o nome da coluna na tabela que o template se refere.
- **Tipo:** Representa o tipo de dado que é permitido na coluna.
- **Tamanho:** É o limite de caracteres que é permitido na coluna.
- **Descrição:** Apresenta uma breve descrição da informação que a coluna armazena.
- **Essencial:** Se marcada com um **"X"**, indica que o preenchimento da coluna no csv é essencial.
- **Valor default:** Informa se existe um valor default para a coluna caso não seja informado nenhum dado a ser preenchido. Para as colunas que não possuem um valor padrão a linha da coluna estará vazia.
- **Valores permitidos:** Quando existir uma lista de valores permitidos, o campo só poderá receber um dos valores listados. Esta coluna apresenta os valores seguidos de suas respectivas descrições, separados pelo simbolo **"->"**, por exemplo, N -> Não. Apenas o valor deve ser preenchido no template csv.

O arquivo Leia-me é gerado de acordo com o modelo, ou seja, ele irá conter as informações e regras específicas das colunas do template que foi baixado. No caso dos [Templates de Entidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#templatesdeentidades), é gerado um único arquivo Leia-me, contendo as informações e regras de todos os modelos que compõe a entidade.

Além disso, os arquivos Leia-me que possuem tabelas marcadas como Padrão poderão utilizar o serviço de **"BUSCA CEP"** para importação e preenchimento automático dos dados de Endereço, Cidade e UF. Para isso, o Importador de dados, irá verificar a configuração do parâmetro **"Tipo de consulta automática do CEP - TIPOCONSULTACEP"** na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834), sendo que, caso ele esteja marcado como:

- **Usar informações dos correios:** o Importador de dados irá utilizar do serviço Busca CEP dos Correios, caso não encontre o CEP, irá verificar os dados preenchidos no template.
- **Usar banco de dados local:** o Importador de dados irá manter o comportamento padrão configurado para a base (TSICEP). Caso não encontre, ele tentará utilizar o serviço Busca CEP. Em último caso, se o serviço Busca CEP também falhar, ele irá considerar os dados preenchidos no template.
- **Não usa:** utilizará os dados inseridos manualmente no template.

**Observação:** o parâmetro TIPOCONSULTACEP não será validado para as **"Agências bancárias"** (tabela TSIAGE), **"Contatos de parceiros"** (tabela TGFCTT), **"Empresas"** (tabela TSIEMP) e **"Parceiros"** (TGFPAR).

**Importante:**

- Todos os arquivos csv gerados pelo Importador de dados possuem o padrão de encoding **“UTF-8 (sem BOM)”** e este padrão não deve ser alterado, pois pode acarretar em problemas nos registros de textos com acentuação e caracteres especiais. Além disso, pode acontecer que não sejam gravados na base os valores preenchidos nas colunas **"AD\_IDEXTERNO"**dos templates, que é a chave do Importador de dados para verificar se um registro já foi importado anteriormente, impossibilitando a atualização de registros através da importação.
- As colunas dos templates são geradas a partir das colunas existentes no Dicionário de Dados das respectivas tabelas, exceto pelas colunas **"CLOB"** e **"BLOB"** que não estão disponíveis para serem tratadas via importação.

Realizados os downloads dos templates que serão utilizados na importação genérica, passaremos para a próxima etapa: o preenchimento dos dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#top)

### Realizar Preenchimento

Nessa etapa você deve preencher os dados do cliente que serão importados.

Os templates das tabelas possuem na primeira linha do seu cabeçalho, o nome da coluna da tabela a qual o template pertence, conforme o Dicionário de Dados. A remoção de colunas pode ser realizada somente se a mesma não for de preenchimento essencial (para verificar sobre a obrigatoriedade de colunas, consulte o arquivo [Leia-me](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#leia-me)) ou que ela não seja um pré-requisito para outra coluna que será mantida no arquivo para importação; caso contrário, poderão ocorrer falhas no processo.

Além disso, os nomes das colunas não devem ser alterados, pois também ocorrerão falhas no processo de importação.

Durante o preenchimento dos templates, algumas informações devem ser observadas para que o processamento dos dados aconteça sem falhas, sendo elas:

| [AD\_IDEXTERNO](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#AD_IDEXTERNO) | [ID's externos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#id'sexternos) |
| --- | --- |
| [Tipos de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#tiposdedados) | [Tamanho da coluna](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#tamanhodacoluna) |
| [Dados que não são tratados via importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#dadosquen%C3%A3os%C3%A3otratadosviaimporta%C3%A7%C3%A3o) | [Atualização de registros](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#atualiza%C3%A7%C3%A3oderegistros) |
| [Utilização de registros existentes na base](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#utiliza%C3%A7%C3%A3oderegistrosexistentesnabase) |  |

---

**AD\_IDEXTERNO**

Esta coluna é utilizada para realizar a definição de um ID para os registros que serão importados. E será a chave para a verificação se um registro já existe na tabela que está sendo importada.

Com base nesta verificação, o Importador de dados poderá ignorar o registro já existente na base ou atualizá-lo conforme dados que estão sendo importados no arquivo .csv. 

| ``` ![Imagem 23: Saiba mais sobre a atualização de registros existentes e importação de dados por meio dos links Atualização de…](https://ajuda.sankhya.com.br/hc/article_attachments/42311144246551) Saiba mais sobre a atualização de registros existentes e importação de dados por             meio dos links Atualização de registros e Importar Dados, respectivamente.  ``` |
| --- |

A coluna **"AD\_IDEXTERNO"** já é gerada automaticamente nos templates .csv quando baixados, exceto para os templates no qual ela não é necessária, e funcionam também para relacionar dados entre templates, conforme descrito no item [ID’s Externos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#id'sexternos). 

Quando a coluna **"AD\_IDEXTERNO"** existir no template csv, será necessário criá-la no Dicionário de Dados do Sankhya Om. Assim, clique no vídeo a seguir para conhecer o procedimento de criação da coluna:

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=ZEJWGODXRAw)

**Nota:** caso o template .csv baixado não possua coluna **"AD\_IDEXTERNO"**, a criação da mesma não é necessária, pois o template em questão não fará uso desta informação.

Recomendamos também que seja criado um índice para as colunas **“AD\_IDEXTERNO”**, pois irá contribuir para uma melhor performance da importação, reduzindo o tempo necessário para consulta de dados relacionados aos registros que serão processados.

![Imagem 24: Recomendamos também que seja criado um índice para as colunas “AD_IDEXTERNO” , pois irá contribuir para uma melhor…](https://ajuda.sankhya.com.br/hc/article_attachments/5875992590743)

Para mais informações sobre a criação de colunas, acesse a Central de Ajuda sobre [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#criandoumcampoadicional).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento)

---

**ID's externos**

Alguns templates possuem tratativas específicas para otimizar o relacionamento de dados, exclusivas para os templates que seguem o Padrão, tratam-se das colunas com nomes iniciados com o prefixo **"ID\_EXTERNO\_"**.

Os ID's externos são ID's dos registros do sistema legado e devem ser preenchidos sempre que for necessário realizar vínculos entre cadastros ou movimentações, bem como quando um determinado template tiver nas suas colunas algum ID externo de outro template.

Estes dados são a referência para a realização dos vínculos existentes entre os dados que serão importados e, dessa forma, devem ser preenchidos corretamente, caso contrário, os vínculos não serão realizados e causarão problemas durante a importação ou inconsistências nos dados importados.

Um exemplo de ID externo utilizado é o do template de Cidades, que deve ser informado como referência no template de Empresas, para que seja possível vincular uma Empresa à Cidade que ela pertence.

As colunas iniciadas com o prefixo **"ID\_EXTERNO\_"** são geradas automaticamente nos templates que são baixados, dispensando a criação da coluna no próprio template. Para o seu preenchimento, deve ser utilizado o valor referente ao **“AD\_IDEXTERNO”** do template de tabela no qual deve ser realizado o relacionamento de dados. Além disso, não é necessário criar no Dicionário de Dados as colunas iniciadas com **"ID\_EXTERNO\_"** que existem nos templates baixados.

A seguir, trouxemos alguns exemplos de ID's externos corretamente preenchidos para o relacionamento das tabelas que compõe a entidade **"Empresa"**:

**Template de Endereços**

![Imagem 25: Template de Endereços](https://ajuda.sankhya.com.br/hc/article_attachments/5876010089751)

**Template de Bairros**

![Imagem 26: Template de Bairros](https://ajuda.sankhya.com.br/hc/article_attachments/5876014235671)

**Template de Cidades**

![Imagem 27: Template de Cidades](https://ajuda.sankhya.com.br/hc/article_attachments/15603459152535)

**Template de Empresas com IDs externos de Bairros, Cidades e Endereços preenchidos de acordo dos templates anteriores**

![Imagem 28: Template de Empresas com IDs externos de Bairros, Cidades e Endereços preenchidos de acordo dos templates anteriores](https://ajuda.sankhya.com.br/hc/article_attachments/5876098787607)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento)

---

**Tipos de dados**

Outra regra que deve ser respeitada no preenchimento dos dados nos templates, é o tipo de dado que é aceito por cada uma das colunas. O preenchimento dos campos com um tipo de dado diferente do que é permitido pode gerar problemas durante a importação.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento)

---

**Tamanho da coluna**

O tamanho das colunas deve ser respeitado, caso contrário, ocorrerão erros na importação. Para verificar os tamanhos das colunas, consulte o arquivo [Leia-me](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#leia-me) que foi baixado em conjunto com o template que será preenchido.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento)

---

**Dados que não são tratados via importação**

O Importador de dados possibilita ainda que colunas adicionais sejam inseridas nos templates de colunas essenciais que seguem o Padrão, para que os dados delas sejam submetidos à importação. Para realizar essa ação, devem ser respeitadas as condições abaixo:

- A coluna a ser inserida deve pertencer à tabela na qual o template se refere;
- As informações da coluna devem ser inseridas conforme o cabeçalho do template, ou seja, deve ser preenchido na primeira linha, delimitando através de (**;**) o nome da coluna a ser adicionada;
- O nome da coluna deve ter exatamente o mesmo nome que ela possui no Dicionário de Dados;
- Caso o dado a ser preenchido na coluna adicionada ao template faça referência aos dados de outras tabelas que não são tratadas por importação, eles deverão estar previamente registrados na base para que o relacionamento seja possível, caso contrário, a informação será ignorada na importação e o valor padrão da base será vinculado.

Além dos pontos anteriores, vale ressaltar que as importações de parceiros e tabela de preços inserem registros em duas tabelas. Sendo elas:

- **Parceiros:** Tabelas TGFPAR e TGFCPL;
- **Tabela de preços:** Tabelas TGFTAB e TGFNTA.

Os templates csv destes dois cadastros, possuem, antes do nome da coluna um prefixo que faz referência a qual tabela determinada coluna pertence. Lembrando que, ao adicionar novas colunas a um template, esta regra também deve ser seguida.

No caso do template csv de parceiro, as colunas que pertencerem a tabela TGFCPL terão, o prefixo **"CPL\_"**:

![Imagem 29: Já no caso do template de tabelas de preços, as colunas são iniciadas com os prefixos "TAB_" e "NTA_" , fazendo as…](https://ajuda.sankhya.com.br/hc/article_attachments/5876041439767)
Já no caso do template de tabelas de preços, as colunas são iniciadas com os prefixos **"TAB\_"** e **"NTA\_"**, fazendo as devidas referências as tabelas TGFTAB e TGFNTA respectivamente:

![Imagem 30: Já no caso do template de tabelas de preços, as colunas são iniciadas com os prefixos "TAB_" e "NTA_" , fazendo as…](https://ajuda.sankhya.com.br/hc/article_attachments/5876057276055)

Agora, observe um exemplo do procedimento de adição da coluna não obrigatória **"CODREG"** (Região) da tabela de Bairros no template de colunas essenciais:

1. Primeiramente, identifique o template de Bairros e clique duas vezes sobre ele;
2. Em seguida, no pop-up que será aberto, escolha a opção **"Template com todas as colunas"** e clique em baixar;
3. Abra o arquivo baixado, identifique o campo a ser adicionado que, no nosso exemplo é o CODREG e copie-o.
4. Por fim, cole o campo copiado no passo anterior na coluna de templates obrigatórios.

[GIF animado: Imagem 31: Por fim, cole o campo copiado no passo anterior na coluna de templates obrigatórios.](https://ajuda.sankhya.com.br/hc/article_attachments/5876100883351)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento)

---

**Utilização de registros existentes na base**

Outra funcionalidade que o Importador de dados oferece, é a possibilidade de vincular registros que já existem na base de dados, que fazem referência à tabela que será importada.

Para essa ação, é necessário que você consulte na base como essa informação deve ser preenchida, para que seja possível realizar o vínculo.

Ainda considerando o exemplo de preenchimento da coluna não obrigatória **"CODREG"** (Região), observe abaixo como fazer o procedimento de utilização de registros já existentes na base:

1. Acesse a tela de [Bairros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599814-Bairro) no Sankhya Om e selecione qualquer registro;
2. Clique na lupa do campo **"Região"** para consultar as opções disponíveis para o preenchimento da coluna;
3. Verifique os códigos que serão utilizados e informe-os na coluna do template que corresponde à informação.

[GIF animado: Imagem 32: Verifique os códigos que serão utilizados e informe-os na coluna do template que corresponde à informação.](https://ajuda.sankhya.com.br/hc/article_attachments/5876062620055)

Após preencher as informações não essenciais inseridas no template, o arquivo estará pronto para ser importado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento)

---

**Atualização de registros**

É possível realizar ainda, além da inserção, a atualização de registros já existentes na base, através do Importador de dados, tanto para as importações que seguem o Padrão, quanto para as que não seguem.

O campo **AD\_IDEXTERNO** é obrigatório tanto para inserção quanto para atualização, e caso a tabela já exista na base de dados sem esse campo, será necessário criá-lo e alimentá-lo antes de utilizar um novo arquivo para atualização em massa via Importador de dados, ou seja: a coluna AD\_IDEXTERNO funciona como uma chave primária (PK) para o Importador de dados, determinando se será realizado um INSERT ou um UPDATE. No entanto, isso não substitui a validação do banco de dados, que poderá gerar um erro caso detecte duplicidade de PK na tabela.

Se o campo AD\_IDEXTERNO estiver vazio, o Importador de dados tentará realizar um novo INSERT. Caso o arquivo .csv contenha um registro com uma PK já existente no banco, ocorrerá um erro de PK duplicada.

Por outro lado, se o campo AD\_IDEXTERNO já estiver preenchido no banco de dados, o Importador de dados identificará o registro e realizará um UPDATE.

Com isso, para atualizar os dados da tabela através do Importador de dados, considerando uma tabela já existente no banco de dados, realize os seguintes passos:

1. crie o campo AD\_IDEXTERNO na tabela em questão;
2. realize o UPDATE na tabela de modo a preencher o campo AD\_IDEXTERNO com o valor desejado (a dica é utilizar o mesmo valor da PK da tabela);
3. atualize o arquivo de importação, preenchendo o AD\_IDEXTERNO com o valor utilizado no UPDATE;
4. realize a importação pelo Importador de dados utilizando o arquivo.csv atualizado.

**Nota:** você deve se atentar ao submeter um template com registros para serem atualizadas as colunas que têm seus valores possíveis definidos a partir do dado de outras, como por exemplo, o campo **"SIMPLES"** do template da tabela de Empresas que, caso seja preenchido como **"N"**, deverá ter a coluna **"CODREGTRIB"**, obrigatoriamente, preenchida com o valor **"3"**.

Após preencher os templates de acordo com as regras e orientações passadas, salve o arquivo preenchido, mantendo a extensão no formato csv com delimitação através de (**;**) e padrão de encode **"UTF-8 (sem BOM)"**.

Além disso, mantenha também o nome de cada um dos arquivos csv da mesma forma que foi gerado pelo Importador de dados no momento do download, para que ele possa reconhecer a qual template cada arquivo se refere.

**Observação:** no caso dos templates de entidade, os arquivos csv preenchidos podem ser mantidos dentro do zip que também é gerado pelo sistema para que, dessa forma, seja possível fazer um único upload de arquivo, que conterá todos os templates que devem ser importados.

**Nota:** é possível também, nos casos onde várias entidades serão importadas, reunir todos os arquivos csv em um único arquivo zip e realizar o upload dele para a importação, desde que todos os templates que serão importados sigam o Padrão.

Caso você precise importar alguma coluna com o dado vazio, basta colocar dois delimitadores de (**;**) em sequência na coluna que não terá seu valor preenchido para algum dos registros a serem importados. Exemplo: **";;"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#realizarpreenchimento) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#top)

### Importar Dados

Finalizado o preenchimento do(s) template(s), para dar sequência no processo, você deverá subtmetê-los no Importador de dados para que seja feita a importação dos dados. Para isso, certifique-se, primeiramente, se os templates preenchidos estão de acordo com as regras definidas para eles.

Se as regras forem correspondidas, acesse a aba **"Importar Dados"** da tela e realize o upload do arquivo csv de um template de tabela ou do zip contendo os templates csv das tabelas que compõe as entidades.

Observe abaixo o processo de upload dos arquivos:

[GIF animado: Imagem 33: Observe abaixo o processo de upload dos arquivos:](https://ajuda.sankhya.com.br/hc/article_attachments/6294565502871)

Para fazer o upload de arquivos zip, basta realizar os mesmos passos e, na busca do arquivo, selecionar o arquivo zip que contém os templates a serem importados. Assim, será feito o upload do arquivo e o Importador de dados também o reconhecerá, conforme demonstramos abaixo:

[GIF animado: Imagem 34: Para fazer o upload de arquivos zip , basta realizar os mesmos passos e, na busca do arquivo, selecionar o arquivo zip…](https://ajuda.sankhya.com.br/hc/article_attachments/6294599725463)

**Observação:** o Importador de dados está preparado para reconhecer a ordenação de templates de tabela que seguem o Padrão.

Após o upload do arquivo a ser importado, você deverá responder à três perguntas que interferem diretamente em como o processo será realizado. São elas:

- **Deseja atualizar os registros existentes?**

Essa pergunta está relacionada à atualização de registros existentes na base e se aplica em como a importação deve se comportar para os casos que a coluna **"AD\_IDEXTERNO"** (ou o código Sankhya, caso a importação não tenha essa coluna) de um determinado template coincidir com um registro que já existe na base ou no próprio template.

Aqui, você escolhe se deseja **"Atualizar os registros"**, ou seja, se os registros já existentes na base terão seus dados atualizados de acordo com os dados preenchidos no template importado, conforme verificação dos valores preenchidos na coluna **“AD\_IDEXTERNO”**. Lembrando que, caso um registro do template importado tenha o mesmo valor da coluna **"AD\_IDEXTERNO"** em outra linha, os dados da última linha importada irão prevalecer sobre a anterior.

Ou se deseja **"Nao atualizar"**, fazendo com que os registros que já existem tenham seus dados mantidos e os dados informados no template sejam ignorados para cada registro já existente que for encontrado. O mesmo será aplicado, caso o **"AD\_IDEXTERNO"** se repita em uma mesma linha do arquivo importado.

- **Validar regras de negócio?**

Esta pergunta está relacionada a quais validações os dados que serão importados serão submetidos. Você pode optar por:

1. **Validar regras de negócio** **-** Ao selecionar esta opção, ao iniciar a importação, o Importador de dados irá submeter os dados preenchidos no(s) template(s) à validação das regras de banco de dados, e também, às regras de negócio existentes no sistema. Trata-se de uma validação mais completa.
2. **Não validar regras de negócio** **-** Ao selecionar esta opção, ao iniciar a importação, o Importador de dados irá submeter os dados preenchidos no(s) template(s) à validação somente das regras de banco de dados. Neste cenário, algumas informações que podem ser definidas seguindo as regras de negócio do sistema, podem ter a necessidade de serem informadas manualmente no(s) template(s).

- **Como deseja realizar a importação?**
  Essa pergunta se refere a como o sistema deverá se comportar caso ocorra algum erro durante o processo de importação. Nesse caso, temos as seguintes possibilidades:

1. **Prosseguir com a importação até o fim -** Com essa opção selecionada, ao iniciar a importação, o Importador de dados irá realizar o processamento do template de tabela ou entidade até o fim, e os erros ocorridos durante o processo estarão disponíveis no [Histórico de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#historicodeimporta%C3%A7%C3%A3o) para que sejam verificados e tratados posteriormente.
2. **Interromper caso aconteça algum erro -** Se você selecionar essa opção, fará com que o Importador de dados interrompa o processamento dos dados caso ocorra algum erro. Nesse caso, acesse o Log de Importação, verifique o erro apontado, realize a correção e submeta o(s) template(s) à uma nova importação.

- **Como deseja realizar a importação de Endereço?**

1. **Utilizar correios priorizando a planilha:** Com essa opção selecionada, o Importador de Dados irá utilizar os dados preenchidos na planilha de importação. Caso não encontre e o CEP esteja preenchido, utilizará o serviço de Busca CEP dos Correios.
2. **Utilizar correios priorizando os correios:** Selecionando essa opção, o Importador de Dados utilizará o serviço de Busca CEP dos Correios e sempre que esse serviço retornar alguma informação, a mesma será utilizada.
3. **Utilizar somente Planilha:** Aqui o Importador de Dados não utilizará o serviço Busca CEP dos Correios, realizando a importação conforme os dados da planilha.

   **Observação:** a seção de Como deseja realizar a importação de Endereço? é de preenchimento obrigatório. Pelo menos uma das opções deve estar selecionada, caso contrário, será exibida a mensagem:

   **"Os campos marcados com '\*' são obrigatórios.**
   **Preencha o seguinte campo:**
   **"Como deseja realizar a importação de Endereço?""**

**Nota:** a regra acima é valida para as tabelas TGFPAR, TSIEMP, TSIAGE, TGFCTT.

Finalizando o processo que descrevemos acima, basta clicar sobre o botão **"Prosseguir"** para que a importação seja iniciada.

Ao final do processo, será exibido um pop-up com o resultado do processo de importação.

Observe abaixo como realizar o passo a passo:

[GIF animado: Imagem 35: Observe abaixo como realizar o passo a passo:](https://ajuda.sankhya.com.br/hc/article_attachments/6294724256023)

Ao final do processamento o botão **"Ver Histórico"** é habilitado, clicando sobre ele é possível visualizar as importações realizadas, bem como os respectivos logs.

Você pode também verificar na aba [Histórico de Importações](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#historicodeimporta%C3%A7%C3%A3o) os resultados do processamento dos registros, e os problemas ocorridos através do log da importação, realizar as correções necessárias e submeter o template a uma nova importação até que todos os erros sejam tratados e a importação seja concluída com sucesso.

**Resultado das Importações**

Ao iniciar, ou ao final do processamento dos arquivos submetidos na importação, o Importador de dados poderá exibir uma das mensagens a seguir:

[Importação realizada com sucesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#importa%C3%A7%C3%A3orealizadacomsucesso)                             [Importação interrompida com falhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#importa%C3%A7%C3%A3ointerrompidacomfalhas)

[Importação finalizada com falhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#importa%C3%A7%C3%A3ofinalizadacomfalhas)                                [Colunas Inexistentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#Colunasinexistentes)

[Ausência da coluna “AD\_IDEXTERNO”](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#Aus%C3%AAnciadacolunaad_idexterno)

---

**Importação realizada com sucesso**

Quando as importações ocorrerem sem falhas, será apresentada a seguinte mensagem:

[GIF animado: Imagem 36: Quando as importações ocorrerem sem falhas, será apresentada a seguinte mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/6294788485911)

Em casos como este, os dados foram devidamente importados. Assim, basta validar as informações importadas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ResultadodasImporta%C3%A7%C3%B5es)

---

**Importação interrompida com falhas**

Nos casos em que você submeter um ou mais templates na importação e tiver optado pela interrupção do processo, se ocorrer alguma falha, o Importador de dados exibirá a mensagem a seguir:

[GIF animado: Imagem 37: Nos casos em que você submeter um ou mais templates na importação e tiver optado pela interrupção do processo, se…](https://ajuda.sankhya.com.br/hc/article_attachments/6294790183575)

Para casos como este, o histórico e log de importação devem ser consultados para que seja verificado o problema ocorrido e realizadas as tratativas necessárias para importar os dados corretamente.

**Observação:** se o problema tiver sido corrigido, o Importador de dados dará continuidade na importação ou interromperá o processo novamente, caso seja identificada outra falha.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ResultadodasImporta%C3%A7%C3%B5es)

---

**Importação finalizada com falhas**

A última situação é quando você submete um ou mais templates na importação e decide que o Importador de dados deverá seguir com o processamento dos arquivos até o fim em caso de falhas. Assim, o Log de Importação será gerado contendo todos os registros de falhas que ocorreram durante o processo com as referências para que sejam corrigidas:

[GIF animado: Imagem 38: A última situação é quando você submete um ou mais templates na importação e decide que o Importador de dados deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/6294829253399)

Nessa situação, você deverá realizar as tratativas de todos os erros e efetuar uma nova importação dos templates.

**Importante:** quando você anexar um arquivo vazio ou inválido, o Importador de dados irá notificar que nenhum dado foi importado e que o conteúdo do arquivo deve ser verificado:

[GIF animado: Imagem 39: Importante: quando você anexar um arquivo vazio ou inválido, o Importador de dados irá notificar que nenhum dado foi…](https://ajuda.sankhya.com.br/hc/article_attachments/6294793334935)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ResultadodasImporta%C3%A7%C3%B5es)

---

**Colunas Inexistentes**

Quando você submeter um arquivo que possui uma ou mais colunas que não existem no Dicionário de Dados da tabela, o Importador de dados irá notificar a(s) coluna(s) divergente(s) para que seja realizado as devidas verificações e ajustes.

**Observação:** se for necessário criar novas colunas no Dicionário de Dados, é importante reiniciar a unidade de dados da tabela, para que o Importador de dados reconheça as alterações.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ResultadodasImporta%C3%A7%C3%B5es)

---

**Ausência da coluna AD\_IDEXTERNO**

Caso um arquivo seja submetido cuja importação necessite da coluna **"AD\_IDEXTERNO"**, e a mesma não tiver sido criada no Dicionário de Dados da tabela, o Importador de dados irá notificar a inexistência da coluna para que seja realizado as devidas verificações e ajustes.

**Observação:** após a criação da coluna AD\_IDEXTERNO no Dicionário de Dados, é importante reiniciar a unidade de dados da tabela, para que o Importador de dados a reconheça.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ResultadodasImporta%C3%A7%C3%B5es) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#top)

### Histórico de importações

Nessa etapa, são apresentadas todas as importações que foram realizadas, bem como o log referente a cada uma delas.

Você pode utilizar os filtros de **"Período"** de importação, **"Evento"**, **"Usuário"** ou um filtro personalizado para refinar o histórico de importações.

![Imagem 40: Você pode utilizar os filtros de "Período" de importação, "Evento" , "Usuário" ou um filtro personalizado para refinar…](https://ajuda.sankhya.com.br/hc/article_attachments/5889997926551)

O painel superior se refere ao histórico de importações. Nele, são apresentadas as seguintes informações:

- **Data importação:**Apresenta a data e hora no qual a importação foi submetida.
- **Arquivo processado:**Apresenta o nome do arquivo que foi submetido na importação.
- **Evento:** Informa se a importação foi realizada com sucesso ou se houve algum erro no processo.
- **Total de registros:**Exibe a quantidade total de registros presentes no arquivo importado.
- **Registros processados:** Apresenta a quantidade de registros que foram importados com sucesso.
- **Registros rejeitados:** Exibe a quantidade de registros no qual ocorreu algum erro na importação.
- **Tempo de execução:** Apresenta o tempo total para o processamento do arquivo submetido à importação.
- **Regra de Importação de Endereço:** Informa se a importação de endereço foi realizada utilizando correios priorizando a planilha, correios priorizando os correios ou somente utilizando planilha.
- **Usuário e Nome:** Apresentam respectivamente o código e nome do usuário que realizou a importação.

Já no painel inferior, referente ao log de importação, são exibidas as seguintes informações:

- **Data evento:** Apresenta a data e hora no qual o registro foi processado.
- **Nome template:**Apresenta o template de tabela que foi processado.
- **Evento:** Apresenta se a importação do registro ocorreu com sucesso ou teve alguma falha.
- **Número da linha:** Exibe o número da linha do template importado.
- **ID do sistema de origem:**Apresenta o valor da coluna **”AD\_IDEXTERNO”** preenchido para o registro, caso o template possua a coluna e a mesma tenha sido utilizada.
- **Mensagem:**Apresenta o resultado da importação para o registro em questão.

Além da visualização do histórico e log de importação, é possível realizar o download do log de uma determinada importação. Para isso, selecione o histórico desejado e clique sobre o botão para selecionar o formato do arquivo. 

![Imagem 41: Além da visualização do histórico e log de importação, é possível realizar o download do log de uma determinada…](https://ajuda.sankhya.com.br/hc/article_attachments/5911455356695)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#top)

### Após a Importação

Após o download e preenchimento dos templates, importação, verificação do Log e correções de possíveis problemas, o processo no Importador de dados terá sido concluído.

Dessa forma, é necessário então, que sejam realizadas algumas ações de verificações, conforme descrevemos nos tópicos abaixo, para que a implantação tenha continuidade. Esses passos são de extrema importância para garantir que quaisquer ruídos ou problemas sejam analisados, resolvidos e a implantação seja realizada com sucesso.

Acesse os link's abaixo para verificar sobre essas ações:

[Análise de dados importados](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#an%C3%A1lisededadosimportados)                                                  [Demais inputs e configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#demaisinputseconfigura%C3%A7%C3%B5es)

[Resoluções de problemas](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#resolu%C3%A7%C3%B5esdeproblemas)

---

**Análise de dados importados**

Após as importações, recomendamos que sejam verificadas as informações na base do sistema, para garantir que os dados estejam devidamente preenchidos, vinculados e de acordo com os cadastros e processos do cliente que está sendo implantado.

Ainda nesse passo, possíveis inconsistências que não puderam ser capturadas durante o processo de importação deverão ser analisadas e corrigidas, se necessário.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ap%C3%B3saimporta%C3%A7%C3%A3o)

---

**Demais inputs e configurações**

Outra ação em continuidade à implantação do cliente é a realização, pelo time de serviços, dos inputs de cadastros e movimentos que não puderam ser feitos via importação, bem como a realização de configurações específicas do cliente, como por exemplo, as Preferências, Configurações de Impostos, Informações adicionais, dentre outros.

Esse passo irá garantir que todos os cadastros e movimentações que serão utilizados no Sankhya Om tenham seu funcionamento conforme o esperado e de acordo com os processos do cliente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ap%C3%B3saimporta%C3%A7%C3%A3o)

---

**Resoluções de problemas**

Os possíveis problemas ocorridos e identificados durante o processo de importação que não forem possíveis analisar e tratar por meio do Log de Importação, deverão ser direcionados ao time de Service Desk da Sankhya.

**Observação:** os demais problemas não relacionados aos processos do time de Produto da Sankhya, deverão ser tratados pelo time de Implantação do novo cliente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#ap%C3%B3saimporta%C3%A7%C3%A3o) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5874837664023-Importador-de-Dados#top)

![Imagem 42: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16623338828439) Acesse também:

[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)

[Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados)

[DBExplorer](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603894-DBExplorer)
