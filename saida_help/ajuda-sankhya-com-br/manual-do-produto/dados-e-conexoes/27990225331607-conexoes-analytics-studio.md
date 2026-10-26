---
id: "27990225331607"
titulo: "Conexões - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27990225331607-Conex%C3%B5es-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Dados e conexões"
atualizado_em: "2026-09-23T17:01:43Z"
rotulos: ["Tabelas", "Configuração", "Importação", "Analytics Studio", "Dados"]
---

# Conexões - Analytics Studio

A funcionalidade de Conexões no [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio) possibilita a importação de dados provenientes de um EIP, arquivos CSV ou conexões JDBC, seja para criar novas tabelas ou atualizar tabelas existentes no sistema.

### Usos das Conexões

#### Criando uma nova tabela

É possível criar uma tabela a partir de uma conexão com o EIP, importação via CSV ou banco de dados externo. Isso é feito na área de criação de tabelas, localizada no canto superior esquerdo da tela. Nessa área, é possível optar por criar uma tabela manualmente ou importar dados via arquivo CSV, ou conexão JDBC.

Antes de iniciar o processo de criação, é necessário configurar o tipo de ID que a tabela utilizará. As opções disponíveis são:

- Auto Incremental;
- Numérico;
- Texto.

Essa escolha é essencial para garantir uma estrutura organizada e facilita futuras interações com a tabela, como filtragens e carregamentos de dados externos.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=QbIr2LDEI_I)

#### Atualizando uma tabela existente

Numa tabela, no canto superior direito, é possível acessar a lista de conexões disponíveis e adicionar novas conexões. Ao adicionar uma nova conexão, podem ser incluídas colunas e linhas à tabela já existente.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=c9oTOzunqJE)

### Conexões para tabelas de chave simples

Ao criar uma conexão para uma tabela de chave simples, no lado esquerdo do modal, é exibido um preview dos dados que podem vir de um arquivo CSV ou de uma Query JDBC. Do lado direito, está o resumo, onde é realizada a configuração da conexão.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=KKHtTYOhDw0)

#### Configuração de colunas

**Primeira Coluna (ID) e Segunda Coluna (Descrição):** para tabelas de chave simples em que o ID é do tipo INT ou VARCHAR, a primeira coluna será sempre o ID e a segunda será a descrição. Para tabelas com ID autoincremental, a primeira coluna sempre será a descrição, já que o ID será gerado automaticamente.

**Escolha de Colunas:** para cada coluna do conjunto de dados, é possível optar por:

- **Nova Coluna**: adicionar a coluna como nova na tabela. Ela pode ser configurada como: **"Texto"**, **"Numérico"**, **"Data"** ou uma **"Foreign Key (FK)"**.
- **Ignorar**: não incluir essa coluna na tabela.
- **Descrição de uma FK**: quando há colunas relacionadas a chaves estrangeiras (exemplo: solicitante ID e Solicitante Descrição), é possível definir o Solicitante ID como uma nova coluna do tipo FK, enquanto Solicitante Descrição é configurada como a descrição dessa FK. Dessa forma, as colunas serão associadas corretamente e, para cada nova FK definida, será criada automaticamente uma tabela separada contendo o ID e a descrição configurados. Isso permite que cada chave estrangeira tenha sua própria tabela de referência, facilitando o gerenciamento e a vinculação de dados no sistema.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=dElHf-qLwxQ)

- **Coluna Existente**: associar a coluna a uma já existente na tabela. Essa opção só estará disponível ao editar tabelas existentes, pois ao criar uma nova tabela, não haverá colunas predefinidas.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=J2U86whdA-I)

### Opções adicionais

A fonte de dados pode ser alterada clicando no botão **"Fonte de dados"**, permitindo alternar entre CSV e SQL conforme necessário.

![Imagem 1: A fonte de dados pode ser alterada clicando no botão "Fonte de dados" , permitindo alternar entre CSV e SQL conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/27992247651479)

**Agendamento de conexões**: se escolher importar os dados por um banco de dados externo ou pelo seu EIP, via SQL, é possível agendar a execução da conexão para horários específicos utilizando um código **"CRON"**, permitindo automações como execuções horárias ou diárias.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=gex9JqyHMNQ)

**Critério de Adição de Linhas**: ao configurar a conexão para uma tabela existente, é possível definir se o carregamento de dados deve adicionar apenas novas linhas ou atualizar as linhas já existentes. Essa opção só estará disponível ao atualizar uma tabela existente, pois, ao criar uma nova tabela, todas as linhas serão consideradas novas.

![Imagem 2: Critério de Adição de Linhas : ao configurar a conexão para uma tabela existente, é possível definir se o carregamento…](https://ajuda.sankhya.com.br/hc/article_attachments/27993233481495)

### Conexões com tabelas de chave composta

Ao criar uma conexão para uma tabela de chave composta, o processo de configuração das colunas é diferente das tabelas de chave simples. Em uma tabela de chave composta, onde várias colunas podem atuar como chaves, essas chaves podem estar em qualquer posição no conjunto de dados. 

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=E85qZi6gWE0)

Para cada coluna, é possível escolher uma das seguintes opções:

- **Nova Coluna**: ao definir uma coluna como nova, é possível configurá-la como uma **"Foreign Key (FK)"**. Caso seja uma FK, é permitido criar o cadastro dessa FK durante a configuração ou vinculá-la a uma FK já existente. Toda coluna configurada como FK será parte da chave composta da tabela.

- **Descrição de uma FK**: uma coluna pode ser designada como a descrição de uma FK e vinculada à FK correspondente. Por exemplo:

Considere duas colunas, **"Gerente de Vendas ID"** e **"Gerente de Vendas Descrição"**. A Gerente de Vendas ID pode ser configurado como uma nova coluna do tipo FK, enquanto Gerente de Vendas Descrição é definida como a descrição dessa FK, vinculando-a ao Gerente de Vendas ID.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=U1nZI0t6ZTU)

- **Ignorar**: permite descartar colunas que não serão utilizadas na tabela.
- **Coluna Existente**: usada para mapear uma coluna do conjunto de dados para uma coluna já existente na tabela de destino. Essa opção só estará disponível ao editar uma tabela existente, pois, ao criar uma nova tabela, não haverá colunas predefinidas.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=pt4_8RbtxLQ)

#### Configuração de colunas do tipo tempo

Nas tabelas de chave composta, apenas uma coluna do tipo tempo (que pode representar dia, mês, trimestre ou ano) é permitida. Caso o conjunto de dados contenha mais de uma coluna temporal, é necessário selecionar qual será utilizada. Além disso, é obrigatório definir a granularidade da data e o formato correto para o carregamento dos dados.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=iyE-swYH1rs)

#### Configuração de colunas numéricas

Um dado do tipo número pode ser configurado como um atributo numérico ou uma FK.

- **Atributos Numéricos:** utilizados quando o valor será tratado como somável ou calculável, como valor de vendas ou valor de mensalidade.
- **FK:** representam relacionamentos, como código de cliente ou código de produto. Ao marcar uma coluna como FK, ela é vinculada a um cadastro de destino, criando uma referência entre tabelas. Para colunas configuradas como numéricas, elas serão tratadas como métricas no conjunto de dados.

#### Opções adicionais

- **Fonte de Dados:** a fonte pode ser alterada clicando no botão **"Fonte de dados"**, permitindo alternar entre CSV e SQL.
- **Agendamento de Conexões:** ao utilizar SQL, é possível agendar execuções em horários específicos por meio de códigos CRON, possibilitando automações como execuções horárias ou diárias.

#### Opções adicionais de carregamento

Ao configurar a conexão, tem-se a opção de decidir como os dados serão carregados na tabela de chave composta:

- **Limpar Todos os Dados Antes do Carregamento**: remove todos os dados da tabela antes de importar o novo conjunto de dados.
- **Utilizar uma das FKs como chave de substituição**: permite adicionar novos dados sem reiniciar completamente a tabela, pode-se optar por utilizar uma das FKs como chave de substituição. Nesse caso, deve-se escolher uma FK específica dentro da tabela de chave composta. O sistema irá limpar apenas os registros que correspondem às chaves encontradas no novo conjunto de dados, antes de recarregar os dados para essas chaves específicas.

![Imagem 3: Utilizar uma das FKs como chave de substituição : permite adicionar novos dados sem reiniciar completamente a tabela,…](https://ajuda.sankhya.com.br/hc/article_attachments/28106243290007)

---

![Imagem 4: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157397033111) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
