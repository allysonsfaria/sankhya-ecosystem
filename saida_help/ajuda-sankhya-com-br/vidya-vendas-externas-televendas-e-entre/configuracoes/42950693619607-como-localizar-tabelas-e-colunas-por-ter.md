---
id: "42950693619607"
titulo: "Como localizar tabelas e colunas por termo no banco de dados (Oracle)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950693619607-Como-localizar-tabelas-e-colunas-por-termo-no-banco-de-dados-Oracle"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:10:12Z"
rotulos: ["sync_hc", "vidya", "sync_hash_781e690c26dc", "vidya_599860"]
---

# Como localizar tabelas e colunas por termo no banco de dados (Oracle)

##

### Objetivo

Este artigo descreve uma consulta SQL genérica para localizar, em todo o banco de dados Oracle, quais tabelas possuem colunas cujo nome contenha um determinado **termo de negócio** (por exemplo: `CAMPANHA`, `CLIENTE`, `PEDIDO`, `PAGAMENTO`, `CONTRATO`, `DESCONTO` etc.). É uma consulta base que pode ser reaproveitada sempre que for necessário investigar onde um conceito está representado no modelo de dados.

### A consulta

```
SELECT
    OWNER AS esquema,
    TABLE_NAME AS tabela,
    COLUMN_NAME AS coluna
FROM ALL_TAB_COLUMNS
WHERE UPPER(COLUMN_NAME) LIKE '%TERMO_BUSCADO%'
ORDER BY
    OWNER,
    TABLE_NAME;
```

> Substitua `TERMO_BUSCADO` pela palavra ou trecho que representa o conceito que você está procurando (ex.: `CAMPANHA`, `CLIENTE`, `STATUS`, `DT_`, `COD_`).

### Para que serve

A query consulta a view de dicionário de dados `ALL_TAB_COLUMNS`, que armazena metadados de **todas as colunas de todas as tabelas** acessíveis ao usuário conectado (independentemente do esquema dono da tabela, desde que existam privilégios de leitura). O resultado traz três informações:

- **esquema**: o dono (owner/schema) da tabela;
- **tabela**: o nome da tabela;
- **coluna**: o nome da coluna encontrada.

Ela filtra apenas colunas cujo nome contenha o termo informado, em qualquer posição do nome, sem diferenciar maiúsculas de minúsculas (graças ao `UPPER()`).

### Quando usar

Esta consulta é útil sempre que você precisa:

- **Mapear onde um conceito de negócio está armazenado**, sem saber de antemão os nomes exatos das tabelas (ex.: localizar tudo relacionado a "campanha", "cliente", "contrato", "endereço").
- **Fazer levantamento de impacto** antes de uma alteração, migração ou correção — para saber quais tabelas/colunas serão afetadas por uma mudança relacionada a determinado domínio.
- **Auditar ou documentar** um banco legado ou pouco documentado, ajudando a construir ou complementar um dicionário de dados funcional.
- **Investigar duplicidade ou inconsistência de modelagem**, quando se suspeita que o mesmo conceito foi implementado com nomes de coluna diferentes em várias tabelas (ex.: `DT_CADASTRO`, `DATA_CADASTRO`, `DT_CAD`).
- **Apoiar o desenvolvimento de relatórios, integrações ou APIs**, quando é preciso localizar rapidamente a origem de um dado.
- **Buscar padrões técnicos de nomenclatura**, como prefixos/sufixos (`COD_`, `_ID`, `FLAG_`, `DT_`), e não apenas termos de negócio.

### Como usar

1. Conecte-se ao banco Oracle com um usuário que tenha privilégio de consulta sobre `ALL_TAB_COLUMNS` (normalmente disponível por padrão para qualquer usuário autenticado, pois é uma view pública do dicionário de dados).
2. Defina o termo de busca e substitua `TERMO_BUSCADO` no `LIKE`, mantendo os símbolos `%` como curingas (qualquer sequência de caracteres antes e depois do termo).
3. Execute a consulta em uma ferramenta cliente (SQL Developer, DBeaver, Toad, etc.) ou via script.
4. Analise o resultado: cada linha indica um esquema, tabela e coluna candidatos.
5. Se necessário, refine a busca (veja variações abaixo) para reduzir ruído ou ampliar o escopo.

### Observações importantes

- **`UPPER(COLUMN_NAME)`**: os nomes de colunas no Oracle normalmente já são armazenados em maiúsculas (salvo quando criados com aspas duplas), mas o `UPPER()` garante que a busca funcione mesmo em cenários não convencionais. Digite o termo de busca sempre em maiúsculas, ou aplique `UPPER()` também sobre ele para maior segurança (ex.: `UPPER(COLUMN_NAME) LIKE UPPER('%termo%')`).
- **Escopo da view `ALL_TAB_COLUMNS`**: retorna apenas objetos aos quais o usuário conectado tem acesso (via privilégios diretos ou roles). Existem duas views relacionadas que podem ser mais adequadas dependendo do caso:
  - `USER_TAB_COLUMNS`: mostra apenas colunas de tabelas do **próprio esquema** do usuário conectado.
  - `DBA_TAB_COLUMNS`: mostra colunas de **todos os esquemas do banco**, mas exige privilégio de DBA (ou privilégio `SELECT_CATALOG_ROLE` / `SELECT ANY DICTIONARY`).
- **Desempenho**: como `ALL_TAB_COLUMNS` é uma view baseada em tabelas internas do dicionário de dados, a consulta costuma ser rápida mesmo em bancos grandes, mas pode demorar um pouco mais em ambientes com milhares de esquemas e tabelas.
- **Falsos positivos**: o uso de `LIKE '%TERMO%'` pode trazer colunas que contêm o termo mas não têm relação direta com o conceito de negócio esperado (ex.: buscar `STATUS` também retorna `ID_STATUS_ANTIGO`). Sempre valide o contexto de cada tabela retornada.
- **Termos muito curtos ou genéricos**: buscas com poucos caracteres (ex.: `ID`, `DT`) tendem a gerar muito ruído, pois casam com um grande número de colunas não relacionadas. Prefira termos mais específicos ou combine com outros filtros (ver variações).

### Variações úteis

**Buscar também o tipo de dado e tamanho da coluna:**

```
SELECT
    OWNER AS esquema,
    TABLE_NAME AS tabela,
    COLUMN_NAME AS coluna,
    DATA_TYPE AS tipo,
    DATA_LENGTH AS tamanho
FROM ALL_TAB_COLUMNS
WHERE UPPER(COLUMN_NAME) LIKE '%TERMO_BUSCADO%'
ORDER BY OWNER, TABLE_NAME;
```

**Restringir a um esquema específico:**

```
SELECT
    OWNER AS esquema,
    TABLE_NAME AS tabela,
    COLUMN_NAME AS coluna
FROM ALL_TAB_COLUMNS
WHERE UPPER(COLUMN_NAME) LIKE '%TERMO_BUSCADO%'
  AND OWNER = 'NOME_DO_ESQUEMA'
ORDER BY TABLE_NAME;
```

**Buscar múltiplos termos ao mesmo tempo:**

```
SELECT
    OWNER AS esquema,
    TABLE_NAME AS tabela,
    COLUMN_NAME AS coluna
FROM ALL_TAB_COLUMNS
WHERE UPPER(COLUMN_NAME) LIKE '%TERMO_1%'
   OR UPPER(COLUMN_NAME) LIKE '%TERMO_2%'
   OR UPPER(COLUMN_NAME) LIKE '%TERMO_3%'
ORDER BY OWNER, TABLE_NAME;
```

**Buscar por nome de tabela em vez de coluna** (útil quando o conceito pode estar no nome da tabela, não só da coluna):

```
SELECT
    OWNER AS esquema,
    TABLE_NAME AS tabela
FROM ALL_TABLES
WHERE UPPER(TABLE_NAME) LIKE '%TERMO_BUSCADO%'
ORDER BY OWNER, TABLE_NAME;
```

**Combinar busca por tabela E coluna ao mesmo tempo:**

```
SELECT
    OWNER AS esquema,
    TABLE_NAME AS tabela,
    COLUMN_NAME AS coluna
FROM ALL_TAB_COLUMNS
WHERE UPPER(TABLE_NAME) LIKE '%TERMO_BUSCADO%'
   OR UPPER(COLUMN_NAME) LIKE '%TERMO_BUSCADO%'
ORDER BY OWNER, TABLE_NAME;
```

### Resumo

| Item | Descrição |
| --- | --- |
| **View utilizada** | `ALL_TAB_COLUMNS` (ou `ALL_TABLES` para busca por nome de tabela) |
| **Finalidade** | Localizar tabelas/colunas por padrão de nome em todo o banco |
| **Pré-requisito** | Privilégio de leitura sobre os objetos consultados |
| **Alternativas** | `USER_TAB_COLUMNS` (próprio esquema) / `DBA_TAB_COLUMNS` (visão de DBA) |
| **Cuidado principal** | Validar falsos positivos, privilégios de acesso e evitar termos muito genéricos |

### Exemplos de aplicação

| Termo buscado | Objetivo típico |
| --- | --- |
| `CAMPANHA` | Localizar tabelas de campanhas de marketing/vendas |
| `CLIENTE` | Mapear onde dados de clientes estão armazenados |
| `CONTRATO` | Investigar tabelas relacionadas a contratos |
| `DT_` | Levantar todas as colunas de data do banco |
| `FLAG_` | Levantar colunas booleanas/indicadoras |
| `COD_` | Levantar colunas de código/identificador de negócio |
