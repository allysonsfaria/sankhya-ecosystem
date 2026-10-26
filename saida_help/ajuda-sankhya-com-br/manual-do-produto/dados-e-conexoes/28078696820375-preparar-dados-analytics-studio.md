---
id: "28078696820375"
titulo: "Preparar Dados - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28078696820375-Preparar-Dados-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Dados e conexões"
atualizado_em: "2026-09-23T16:59:54Z"
rotulos: ["Tabelas", "Queries", "Importação", "Analytics Studio", "Preparar Dados", "Scripts", "Atributos Dinâmicos"]
---

# Preparar Dados - Analytics Studio

A seção Preparar Dados na plataforma [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio) é o local onde é possível gerenciar e manipular os dados. Ele permite criar tabelas, atributos, carregar dados externos e internos (EIP Sankhya), criar scripts, queries e views de banco de dados.

![Imagem 1: A seção Preparar Dados na plataforma Analytics Studio é o local onde é possível gerenciar e manipular os dados. Ele…](https://ajuda.sankhya.com.br/hc/article_attachments/28078696805783)

## Criando novos itens

Na parte superior da lista de dados, o botão **"+ Novo"** oferece diversas opções para adicionar ou criar novos itens na plataforma. Por meio dele, é possível:

- Importar dados do EIP Sankhya;
- Importar arquivos CSV;
- Importar dados de bancos externos;
- Criar tabelas vazias;
- Elaborar queries;
- Desenvolver scripts.

### Tabela

Permite a criação de tabelas diretamente no banco de dados do Analytics AI. Existem dois tipos de tabelas:

#### Tabela de chave simples

Uma única coluna identifica exclusivamente cada registro. Esse tipo de tabela é utilizado para cadastros ou transações. A configuração inclui o campo ID, no qual é possível determinar se ele será definido como Autoincremental, Numérico ou Texto. Outras configurações, como o grupo ao qual a tabela pertence, podem ser ajustadas conforme necessário.

Os atributos padrão, como ID, Descrição, Data de Criação, Usuário de Criação, Data da Última Alteração e Usuário da Última Alteração, são criados automaticamente e não podem ser alterados ou removidos.

Após criar tabelas de chave simples, é permitido realizar as seguintes configurações e carregamentos:

**Configurações:**

- Alterar o grupo ao qual a tabela pertence.
- Definir o tipo do ID: **"Numérico"**, **"Texto"** ou **"Autoincremental"**.
- Ajustar o tipo de exibição: **"Apenas descrição"**, **"Apenas código"** ou **"Ambos"**.
- Definir a ordenação padrão: **"Ordenação por código"** ou por **"Descrição"**.

**Carregamentos:**

Pode-se configurar o carregamento de dados externos para a tabela, É possível importar informações de diferentes fontes, como: dados do EIP, de um arquivo CSV ou de um banco de dados externo conectado. Para mais detalhes, consulte o artigo [Conexões](https://ajuda.sankhya.com.br/hc/pt-br/articles/27990225331607-Conex%C3%B5es-Analytics-AI).

#### Tabela de chave composta

Composta por duas ou mais colunas que, juntas, identificam exclusivamente um registro. Ao criar uma tabela com chave composta, é necessário selecionar os cadastros que irão compor essa chave.

Após criar tabelas de chave composta, é permitido realizar as seguintes configurações e carregamentos:

**Configurações:**

- Alterar o grupo ao qual a tabela pertence.
- Gerenciar as chaves da tabela composta: adicionar ou remover cadastros que compõem a chave composta.

**Carregamentos:**

Assim como nas tabelas de chave simples, é possível configurar carregamentos externos para alimentar a tabela a partir de diferentes fontes de dados, como EIP, CSV ou banco de dados externos. Para mais detalhes, consulte o artigo [Conexões](https://ajuda.sankhya.com.br/hc/pt-br/articles/27990225331607-Conex%C3%B5es-Analytics-AI).

![Imagem 2: Assim como nas tabelas de chave simples, é possível configurar carregamentos externos para alimentar a tabela a partir…](https://ajuda.sankhya.com.br/hc/article_attachments/28078696808215)

#### Importar do EIP

Importa os dados selecionados direto do seu EIP Sankhya. Pode ser utilizado para tabelas com chave simples ou composta. Mais detalhes no artigo Conexões.

#### Importar CSV

Permite carregar dados a partir de arquivos CSV. Pode ser usado para tabelas com chave simples ou composta. Consulte o artigo Conexões para mais detalhes.

#### Importar de banco externo

Conecta e importa dados de bancos de dados externos. Também pode ser utilizado para tabelas com chave simples ou composta. Mais detalhes no artigo Conexões.

#### Query

Crie e execute consultas SQL personalizadas. Utilize o dicionário de dados e variáveis de filtro para construir queries de forma eficiente e integrada aos filtros aplicados nas telas.

![Imagem 3: Crie e execute consultas SQL personalizadas. Utilize o dicionário de dados e variáveis de filtro para construir queries…](https://ajuda.sankhya.com.br/hc/article_attachments/28078690549911)

#### Scripts

Permite escrever operações de DML, como Insert, Delete e Update. O dicionário de dados e variáveis de filtro também estão disponíveis para auxiliar na criação dos scripts.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=y1mcJ0AXask)

## Configurações de tabelas

Nas configurações da tabela, é possível gerenciar como os dados serão exibidos e ordenados nos seletores e visualizações, além de escolher se a tabela será exibida nas operações de Drill ou não.

### Criando um novo atributo

Para adicionar um novo atributo, clique no ícone **"+"** ao lado do último atributo listado. Informe o nome e o tipo do atributo. As opções de tipo incluem:

- Numérico;
- Texto;
- Data;
- Seletor único;
- Foreign Key (FK): cria um relacionamento com outra tabela.

![Imagem 4: Foreign Key (FK): cria um relacionamento com outra tabela.](https://ajuda.sankhya.com.br/hc/article_attachments/28078696813719)

#### Atributo dinâmico

O Analytics AI também permite a criação de atributos dinâmicos, que são uma espécie de view que puxa dados em tempo real com base em uma query. Ele permite que os valores sejam atualizados dinamicamente conforme os dados subjacentes.

Ao configurar um atributo dinâmico, a query deve retornar duas colunas:

- Uma coluna com o ID do cadastro onde o atributo será criado.
- Uma coluna com o resultado do atributo dinâmico.

Essas duas colunas precisam ser mapeadas, ou seja, identificadas e marcadas no sistema para que o Analytics AI reconheça corretamente seus valores e relacionamentos.

**Exemplo prático:**

Para ilustrar a configuração de um atributo dinâmico, considere uma tabela de **"Movimentações Financeiras"**, que possui os campos valor unitário e quantidade para cada transação. O objetivo é criar um atributo dinâmico que calcule automaticamente o valor total de cada transação (quantidade × valor unitário). Assim, sempre que a quantidade ou o valor unitário forem alterados, o valor total será atualizado em tempo real.

**Passo a passo:**

- **Acesse a tabela:** navegue até a tabela onde deseja adicionar o atributo dinâmico. Nesse exemplo, estamos na tabela Movimentações Financeiras.
- **Adicionar novo atributo:** no canto superior da tela da tabela, clique no botão **"+"** para adicionar um novo atributo.
- **Selecione o tipo de atributo:** escolha o tipo de atributo que deseja adicionar. No nosso exemplo, o atributo será numérico (pois estamos calculando um valor).
- **Marcar como dinâmico:** ao selecionar o tipo de atributo, marque a opção **"Dinâmico"**. Isso habilitará um campo para escrever a query que será usada para calcular o valor dinâmico.
- **Escrever a query:** agora, no campo da query, escreva a consulta SQL que retornará os valores desejados. No nosso exemplo, a query utilizada retornará o **"ID"** da transação e o **"Valor Total"** calculado.
- **Mapeamento de colunas:** após executar a query, será necessário configurar a marcação dos resultados para definir qual coluna da query estará associada a qual atributo. A primeira marcação deve ser na coluna ID retornada pela query, adicionando o chip ID da tabela Movimentação Financeira. A segunda marcação deve ser na coluna **"VALOR\_TOTAL"** da query, adicionando o chip Valor Total.
- **Resultado esperado:** após seguir este passo a passo, será configurado um atributo dinâmico para exibir o valor total de cada movimentação financeira na tabela, com base na multiplicação de "quantidade" por "valor unitário". Para auxiliar na configuração, assista ao vídeo de modelo para a configuração desse exemplo.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=iRdyVvvJk30)

### Tabelas nativas do Analytics AI

Ao criar um projeto, o Analytics AI gera automaticamente a tabela nativa **"Calendário"**, contendo os dados de dia, mês, semana, dia da semana, trimestre e ano. Esses dados podem ser utilizados para análises em seu projeto.

---

![Imagem 5: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157214942871) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
