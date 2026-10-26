---
id: "https://developer.sankhya.com.br/docs/repositorio-dados"
titulo: "🗃️ A Camada de Repositório (`@Repository`)"
url: "https://developer.sankhya.com.br/docs/repositorio-dados"
atualizado_em: "2026-09-08T19:13:48.000Z"
---

# 🗃️ A Camada de Repositório (`@Repository`)

<br />

# 🗃️ A Camada de Repositório (`@Repository`)

O padrão **Repository** no SDK Sankhya é uma abstração poderosa que simplifica drasticamente o acesso a dados. Ele permite que você defina consultas de forma declarativa, sem escrever uma única linha de implementação, e promove um código limpo, seguro e fácil de manter.

## 🤔 Por que usar Repositórios?

* ✅ **Implementação Automática:** Você define a interface, e o SDK escreve o código de acesso a dados para você em tempo de compilação.
* ✅ **CRUD Gratuito:** Métodos como `save()`, `findByPK()`, `findAll()` e `delete()` já vêm prontos para uso.
* ✅ **Consultas Declarativas:** Escreva consultas complexas com anotações (`@Criteria`), utilizando parametros nomeados.
* ✅ **Segurança de Tipos (Type-Safety):** Chega de "strings mágicas". Parâmetros e retornos são fortemente tipados, e erros são pegos em tempo de compilação, não em execução.
* ✅ **Código Limpo e Testável:** A camada de acesso a dados fica completamente isolada, permitindo que seus serviços sejam testados facilmente com repositórios *mock*.

***

## 📊 Abordagem Antiga vs. Nova

### ❌ Abordagem Tradicional (DAO com Jape)

O padrão DAO (Data Access Object) com Jape manual é verboso, propenso a erros de digitação e vulnerável a SQL Injection.

```java
// Código legado: verboso, inseguro e difícil de manter
public class VeiculoDAO {
    public Optional<Veiculo> buscarPorPlaca(String placa) throws Exception {
        JapeWrapper dao = JapeFactory.dao("Veiculo");
        // Concatenação de strings é perigosa e propensa a erros
        Collection<DynamicVO> vos = dao.find("PLACA = '" + placa + "'");

        if (vos.isEmpty()) {
            return Optional.empty();
        }
        // Conversão manual de DynamicVO para POJO
        DynamicVO vo = vos.iterator().next();
        Veiculo veiculo = new Veiculo();
        veiculo.setId(vo.asLong("CODVEICULO"));
        veiculo.setPlaca(vo.asString("PLACA"));
        return Optional.of(veiculo);
    }
}
```

### ✅ Nova Abordagem com `@Repository`

Com o SDK, você apenas define a interface. O código é limpo, seguro e declarativo.

```java
// Código moderno: seguro, declarativo e sem boilerplate
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    
    @Criteria("ativo = :ativo AND v.marca = :nomeMarca")
    List<Veiculo> findAtivosPorMarca(
        @Parameter("ativo") boolean ativo, 
        @Parameter("nomeMarca") String nomeMarca
    );

    @Criteria(clause = "ATIVO = :ativo")
    Page<Veiculo> findByAtivoPaginado(Boolean ativo, Pageable pageable);
}

// Uso no serviço:
@Service
public class VeiculoService {
    private final VeiculoRepository repository;

    @Inject
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }

    public Optional<Veiculo> buscarPorPlaca(String placa) {
        // Simples, direto e seguro.
        return repository.findByPlaca(placa);
    }
    
    public Page<Veiculo> buscarAtivosPaginados(String nomeMarca) {
        //Objeto de paginação número da página, tamanho da página e argumentos para paginação
        PageRequest pageRequest = PageRequest.of(0, 10, Sort.by("NOME", Direction.DESC), Sort.by("PLACA", Direction.DESC));
        return repository.findByAtivoPaginado(nomeMarca, pageRequest);
    }
}
```

***

## 📝 Como Criar um Repositório

Um repositório no SDK é uma **interface** que estende `JapeRepository<T, ID>`.

* `T`: A classe da sua entidade (ex: `Veiculo`).
* `ID`: O tipo da chave primária da sua entidade (ex: `Long`).

```java
import br.com.sankhya.sdk.data.repository.JapeRepository;
import br.com.sankhya.studio.stereotypes.Repository;

@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    // Seus métodos de consulta customizados virão aqui
}
```

### Métodos CRUD Padrão

Ao estender `JapeRepository`, sua interface herda automaticamente os seguintes métodos:

| Método                       | Descrição                                                          |
| :--------------------------- | :----------------------------------------------------------------- |
| `save(T entity)`             | Salva uma nova entidade ou atualiza uma existente.                 |
| `findByPK(ID id)`            | Busca uma entidade pela sua chave primária. Retorna `Optional<T>`. |
| `findAll()`                  | Retorna todas as instâncias da entidade.                           |
| `findAll(Pageable pageable)` | Retorna uma página de resultados com ordenação. Retorno `Page<T>`  |
| `delete(T entity)`           | Remove uma entidade do banco de dados.                             |

***

## 🔍 Criando Consultas Customizadas

### @Criteria

A anotação `@Criteria` permite definir consultas de busca (SELECT) personalizadas usando condições SQL na cláusula WHERE.

#### Características Principais

* **Declarativa**: Define a consulta através de anotação
* **Parâmetros Nomeados**: Vincula parâmetros do método à query
* **Flexível**: Suporta funções SQL e macros Sankhya
* **Type-Safe**: Retorno tipado (entidade ou lista de entidades)

#### Sintaxe Básica

```java
@Criteria(clause = "CAMPO = :parametro")
ReturnType nomeDoMetodo(TipoParametro parametro);
```

### @NativeQuery

A anotação `@NativeQuery` permite executar consultas SQL nativas diretamente em métodos de repositório, oferecendo controle total sobre o SQL utilizado. Ela é ideal para cenários complexos, de alta performance ou que não podem ser representados facilmente por abstrações como `@Criteria`.

#### Quando Usar

* **Consultas complexas**: JOINs múltiplos, subqueries, window functions e outras operações específicas do banco de dados.
* **Otimização de performance**: Quando é necessário escrever uma consulta altamente otimizada.
* **Relatórios e agregações**: Consultas que realizam cálculos complexos (GROUP BY, HAVING) e retornam DTOs personalizados.

#### Características Principais

* **SQL nativo**: Permite escrever consultas completas e específicas do banco.
* **Segurança**: Suporte a parâmetros nomeados (`:nome`) para evitar SQL Injection.
* **Mapeamento flexível**: Conversão automática para interfaces (DTOs), listas ou tipos Java simples (`String`, `Boolean`, `Long`, etc.).
* **Gerenciamento de transações**: Integração com `JdbcWrapper` para reutilização de conexões existentes.
* **Sankhya Macros**: É possível utilizar Macros Sankhya (ex: `dbDate()`) como em qualquer outro lugar.

#### Sintaxe Básica

```java
@NativeQuery("SELECT CAMPO1, CAMPO2 FROM MINHA_TABELA WHERE CAMPO = :parametro")
List<MeuDTO> nomeDoMetodo(@Parameter("parametro") TipoParametro parametro);
```

#### Tipos de Retorno

A anotação `@NativeQuery` pode retornar tanto interfaces (DTOs) quanto tipos Java simples.

* **Interfaces (DTOs)**

  Interfaces que representam o resultado da consulta devem ser anotadas com `@NativeQuery.Result`. Cada método deve seguir o padrão de getter (`getCampo`) e corresponder exatamente ao nome da coluna ou alias retornado pela query.

  ```java
  // DTO para representar o resultado
  @NativeQuery.Result
  public interface ResumoProdutoDTO {
      Long getCodigo();
      String getDescricao();
      BigDecimal getPreco();
  }

  // Repositório com a consulta
  @Repository
  public interface ProdutoRepository extends JapeRepository<Produto, Long> {
      @NativeQuery("SELECT CODPROD AS Codigo, DESCRPROD AS Descricao, VLRVENDA AS Preco FROM TGFPRO WHERE ATIVO = 'S'")
      List<ResumoProdutoDTO> listarProdutosAtivos();
  }
  ```

  > **Atenção:** O nome dos getters no DTO deve coincidir **exatamente** com os nomes (ou aliases) das colunas na query. Qualquer divergência resultará em `null` no campo correspondente.

* **Tipos Java Simples**

  Também é possível retornar tipos Java diretamente, como `String`, `Long`, `Integer`, `BigDecimal`, etc.

  ```java
  @NativeQuery("SELECT DESCRPROD FROM TGFPRO WHERE CODPROD = :codigo")
  String buscarDescricaoPorCodigo(@Parameter("codigo") Long codigo);

  @NativeQuery("SELECT CODPROD FROM TGFPRO WHERE ATIVO = 'S'")
  List<Long> listarCodigosDeProdutosAtivos();

  @NativeQuery("SELECT COUNT(1) FROM TGFPRO")
  Long contarTotalDeProdutos();
  ```

  <Callout icon="⚠️" theme="warn">
    ### **Importante:** Consultas que retornam tipos Java simples devem garantir que o resultado contenha **exatamente uma (1) coluna**. Caso a consulta retorne mais de uma coluna, será lançada a exceção `ResultHasMoreThanOneColumnException`.

    ✅ **Exemplo válido:** `SELECT NOME FROM TGFPAR`

    ❌ **Exemplo inválido:** `SELECT CODPARC, NOME FROM TGFPAR`
  </Callout>

#### Métodos Ambíguos do ResultSet

Internamente, o `@NativeQuery` utiliza `java.sql.ResultSet` para ler os dados. Em raras situações, pode haver ambiguidade entre métodos com o mesmo tipo de retorno (por exemplo, `getString()` e `getNString()`). Para resolver isso, utilize o atributo `method` da anotação:

```java
@NativeQuery(value = "SELECT CAMPO_NVARCHAR FROM MINHA_TABELA", method = ResultSetMethods.GET_N_STRING)
String buscarComNString();

@NativeQuery(value = "SELECT CAMPO_VARCHAR FROM MINHA_TABELA", method = ResultSetMethods.GET_STRING)
String buscarComString();
```

> **Observação:** A ambiguidade só ocorre em retornos de tipos Java simples. Interfaces (DTOs) são resolvidas automaticamente com base no tipo de cada getter.

#### Recebendo `JdbcWrapper` como Argumento

O `@NativeQuery` permite receber um `JdbcWrapper` como argumento no método do repositório. Isso é essencial ao executar consultas dentro de contextos transacionais já existentes (como em um `@Listener`), pois garante o reaproveitamento da conexão, evitando problemas de performance e vazamento de conexões.

```java
@Repository
public interface PedidoRepository extends JapeRepository<Pedido, Long> {
    @NativeQuery("SELECT COUNT(1) FROM TGFCAB WHERE STATUS = 'P'")
    Long contarPendentes(JdbcWrapper jdbc);
}

// Uso dentro de um listener:
@Listener(instanceNames = {"CabecalhoNota"})
@RequiredArgsConstructor(onConstructor_ = @Inject)
public class MeuListener extends PersistenceEventAdapter {

    private final PedidoRepository repository;

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {
        // Reutiliza a conexão da transação do listener
        JdbcWrapper jdbc = event.getJdbcWrapper();
        Long pendentes = repository.contarPendentes(jdbc);
        // ...
    }
}
```

### Operações de Modificação com @Modifying e @NativeQuery

Para executar operações de modificação de dados (UPDATE, INSERT, DELETE) com SQL nativo, utilize a anotação `@Modifying` em conjunto com `@NativeQuery`. Esta abordagem é ideal para operações em massa que não se encaixam nos métodos padrão do repositório.

#### Quando Usar

* **Atualizações em massa**: Modificar vários registros de uma vez sem precisar carregá-los em memória.
* **Exclusões em massa**: Deletar registros com base em critérios complexos.
* **Operações de alta performance**: Executar uma instrução DML diretamente no banco de dados.

#### Características Principais

* **SQL nativo**: Suporte a `UPDATE`, `INSERT` e `DELETE` através da `@NativeQuery`.
* **Segurança**: Usa parâmetros nomeados (`:nome`) para prevenir SQL Injection.
* **Retorno**: O método deve retornar `int` ou `Integer` para indicar o número de registros afetados. Retornar `void` também é suportado.
* **Transacional**: As operações devem ser executadas dentro de um método anotado com `@Transactional`.

#### Sintaxe Básica

```java
@Modifying
@NativeQuery("UPDATE TGFPRO SET ATIVO = 'N' WHERE CODGRUPOPROD = :grupo")
int desativarProdutosPorGrupo(@Parameter("grupo") Long grupo);
```

#### Exemplos Práticos

* **Atualização em Massa**

  ```java
  @Repository
  public interface ProdutoRepository extends JapeRepository<Produto, Long> {
      @Modifying
      @NativeQuery("UPDATE TGFPRO SET VLRVENDA = VLRVENDA * :fator WHERE CODGRUPOPROD = :grupo")
      int reajustarPrecoPorGrupo(@Parameter("fator") BigDecimal fator, @Parameter("grupo") Long grupo);
  }

  @Component
  public class ProdutoService {
      private final ProdutoRepository repository;
      // ...

      @Transactional
      public void aplicarReajuste(Long grupo, BigDecimal fator) {
          int afetados = repository.reajustarPrecoPorGrupo(fator, grupo);
          // ...
      }
  }
  ```

* **Exclusão em Massa**

  ```java
  @Repository
  public interface LogRepository extends JapeRepository<Log, Long> {
      @Modifying
      @NativeQuery("DELETE FROM AD_LOGS WHERE DTEXPIRACAO < :data")
      int excluirLogsExpirados(@Parameter("data") LocalDate data);
  }
  ```

### Boas Práticas

* **Prefira interfaces (DTOs)** para consultas com múltiplas colunas.
* **Evite&#x20;**`SELECT *`: Mapeie apenas os campos necessários para melhor performance.
* **Verifique os aliases**: Garanta que o nome dos getters no DTO coincida exatamente com os nomes/aliases das colunas retornadas pela query.
* **Use&#x20;**`@Transactional` para todas as operações de escrita (`@Modifying`).
* **Não utilize palavras reservadas como nome de colunas**: Ao mapear uma `@Column`, não utilize palavras reservadas pelo banco de dados como `nome` da coluna. Ex: Não chame uma coluna de `TIMESTAMP`, ou de `DECIMAL` e etc...

***

## 📁 Queries SQL Externas

Para queries SQL complexas (100+ linhas), múltiplos JOINs ou queries que precisam ser reutilizadas em múltiplos repositórios, o SDK permite **externalizar queries em arquivos**. Isso melhora a legibilidade do código, facilita manutenção e permite queries específicas por banco de dados (Oracle vs MSSQL).

### Motivação

**Problemas com SQL inline:**

* Queries complexas poluem o código Java
* Duplicação de queries entre múltiplos repositórios
* Difícil manutenção quando a query tem 300+ linhas
* Sem suporte nativo para queries específicas por banco

**Solução: queries em arquivos externos.**

### Como Funciona

Use o atributo `fromFile = true` na anotação `@NativeQuery`:

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    
    @NativeQuery(value = "queries/listar-veiculos-ativos.sql", fromFile = true)
    List<VeiculoView> listarAtivos(@Parameter("ativo") String ativo);
}
```

### Formato: Arquivo .sql (Single Database)

Para queries compatíveis com Oracle e MSSQL, use arquivos `.sql`:

**Arquivo:** `model/src/main/resources/queries/listar-veiculos-ativos.sql`

```sql
SELECT 
    v.CODVEI,
    v.PLACA,
    v.DESCRICAO,
    v.ATIVO,
    v.DHINC
FROM TGFVEI v
WHERE v.ATIVO = :ativo
  AND v.DHINC >= :dataInicio
ORDER BY v.DESCRICAO
```

**Uso:**

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    @NativeQuery(value = "queries/listar-veiculos-ativos.sql", fromFile = true)
    List<VeiculoView> listarAtivos(
        @Parameter("ativo") String ativo,
        @Parameter("dataInicio") LocalDate dataInicio
    );
}
```

### Formato: Arquivo .xml (Multi-Database)

Para queries que podem ser compartilhadas entre Oracle e MSSQL, utilize arquivos `.xml` com a tag `<both>`:

**Arquivo:** `model/src/main/resources/queries/relatorio-vendas.xml`

```xml
<sql>
    <both>
        SELECT 
            CAB.NUNOTA,
            CAB.DTNEG,
            PAR.NOMEPARC,
            CAB.VLRNOTA
        FROM TGFCAB CAB
        JOIN TGFPAR PAR ON CAB.CODPARC = PAR.CODPARC
        WHERE CAB.DTNEG BETWEEN :dataInicio AND :dataFim
    </both>
</sql>
```

**Uso:**

```java
@NativeQuery(value = "queries/relatorio-vendas.xml", fromFile = true)
List<RelatorioVendasDTO> gerarRelatorio(
    @Parameter("dataInicio") LocalDate inicio,
    @Parameter("dataFim") LocalDate fim
);
```

### Queries Específicas por Banco

Quando a sintaxe SQL diverge entre Oracle e MSSQL, defina queries separadas:

**Arquivo:** `model/src/main/resources/queries/quantidade-vendida.xml`

```xml
<sql>
    <oracle>
        SELECT NVL(SUM(ITE.QTDNEG), 0) AS TOTAL
        FROM TGFITE ITE
        WHERE ITE.CODPROD = :codProd
    </oracle>
    <mssql>
        SELECT ISNULL(SUM(ITE.QTDNEG), 0) AS TOTAL
        FROM TGFITE ITE
        WHERE ITE.CODPROD = :codProd
    </mssql>
</sql>
```

**Em runtime**, o SDK seleciona automaticamente a query correta baseada no tipo de banco de dados do cliente.

### Prioridade de Seleção (XML)

1. **Tag&#x20;**`<both>` (prioridade máxima): Usada para ambos os bancos
2. **Tag&#x20;**`<oracle>`**&#x20;ou&#x20;**`<mssql>`: Usada apenas se `<both>` não estiver preenchida

**Exemplo:**

```xml
<sql>
    <!-- Prioridade 1: Usada sempre que preenchida -->
    <both>SELECT COUNT(*) FROM TABELA</both>
    
    <!-- Prioridade 2: Ignoradas se <both> existe -->
    <oracle>SELECT COUNT(1) FROM TABELA</oracle>
    <mssql>SELECT COUNT(1) FROM TABELA</mssql>
</sql>
```

### Parâmetros Nomeados

Parâmetros funcionam **exatamente igual** com queries inline ou externas:

**Arquivo SQL:**

```sql
SELECT * FROM TGFVEI 
WHERE ATIVO = :ativo 
  AND CODVEI > :codVei
  AND MARCA = :marca
```

**Uso:**

```java
@NativeQuery(value = "queries/buscar-veiculos.sql", fromFile = true)
List<Veiculo> buscar(
    @Parameter("ativo") String ativo, 
    @Parameter("codVei") Long codVei,
    @Parameter("marca") String marca
);
```

### Cache Automático

Queries carregadas de arquivos são **automaticamente cacheadas** em memória. Não há overhead de I/O após a primeira leitura.

### Validações em Compile-Time

O SDK valida queries externas **durante a compilação**:

✅ **Arquivo existe:** Erro se arquivo não for encontrado<br />✅ **Arquivo não vazio:** Erro se arquivo .sql estiver vazio<br />✅ **XML válido:** Erro se XML mal formado<br />✅ **Queries definidas:** Erro se todas as tags (`<both>`, `<oracle>`, `<mssql>`) estiverem vazias<br />⚠️ **Warning:** Se apenas Oracle OU MSSQL estiver definida (pode falhar no cliente)<br />✅ **Parâmetros consistentes:** Erro se Oracle usar `:param1` mas MSSQL usar `:param2`

**Exemplo de erro:**

```
[ERROR] Arquivo SQL não encontrado: queries/listar-veiculos.sql
        Verifique se o arquivo existe em model/src/main/resources/
```

### Tratamento de Erros em Runtime

Se um arquivo desaparecer após o build, exceptions claras são lançadas:

```java
try {
    List<VeiculoView> veiculos = repository.listarAtivos("S");
} catch (InvalidQueryFileException e) {
    // XML mal formado ou query não aplicável ao banco
    logger.error("Query file inválido: " + e.getMessage());
}
```

### Boas Práticas com Queries Externas

1. **Organize por contexto de negócio:**
   ```
   resources/
   ├── queries/
   │   ├── vendas/
   │   │   ├── relatorio-mensal.xml
   │   │   └── top-produtos.sql
   │   ├── estoque/
   │   │   ├── produtos-baixo-estoque.sql
   │   │   └── movimentacao-periodo.xml
   ```

2. **Use&#x20;**`<both>`**&#x20;quando possível:** Simplifique manutenção mantendo uma query única

3. **Documente queries complexas:** Adicione comentários SQL explicando lógica de negócio

4. **Prefira parâmetros nomeados:** Mais legível que `?` posicional

5. **Evite queries dinâmicas:** Para lógica condicional, crie múltiplos métodos ou use `@Criteria`

6. **Teste queries manualmente primeiro:** Execute no banco antes de externalizar

### Troubleshooting

| Problema                    | Causa                                     | Solução                          |
| --------------------------- | ----------------------------------------- | -------------------------------- |
| `InvalidQueryFileException` | XML mal formado                           | Validar estrutura XML com schema |
| Arquivo vazio               | SQL não escrito                           | Adicionar conteúdo ao arquivo    |
| Query errada para banco     | Apenas Oracle/MSSQL definida              | Preencher ambas ou usar `<both>` |
| Parâmetros inconsistentes   | Oracle usa `:param1`, MSSQL usa `:param2` | Alinhar nomes de parâmetros      |

***

### Exemplos Práticos

#### 1. Consulta Simples por Campo

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    
    // Busca por placa específica
    @Criteria(clause = "PLACA = :placa")
    Optional<Veiculo> findByPlaca(String placa);
    
    // Busca por status ativo
    @Criteria(clause = "ATIVO = :ativo")
    List<Veiculo> findByAtivo(Boolean ativo);

    // Busca por status ativo com NativeQuery e DTO
    @NativeQuery("SELECT CODVEICULO, PLACA FROM TGFVEI WHERE MODELO = :modelo")
    List<VeiculoDTO> findByModeloNativo(@Parameter("modelo") String modelo);
}

@NativeQuery.Result
interface VeiculoDTO {
    Long getCodVeiculo();
    String getPlaca();
}
```

#### 2. Consultas com Múltiplos Parâmetros

```java
@Repository
public interface PedidoRepository extends JapeRepository<Long, Pedido> {
    
    // Busca por empresa e status
    @Criteria(clause = "CODEMP = :empresa AND STATUS = :status")
    List<Pedido> findByEmpresaAndStatus(Long empresa, String status);
    
    // Busca com parâmetros nomeados explicitamente
    @Criteria(clause = "CODEMP = :COD_EMP AND DTNEG BETWEEN :dataInicio AND :dataFim")
    List<Pedido> findByPeriodo(
        @Parameter(name = "COD_EMP") Long codigoEmpresa,
        @Parameter(name = "dataInicio") LocalDate inicio,
        @Parameter(name = "dataFim") LocalDate fim
    );

    // Busca com NativeQuery e DTO
    @NativeQuery("SELECT NUNOTA, VLRNOTA FROM TGFCAB WHERE CODEMP = :empresa AND STATUS = :statusPedido")
    List<PedidoDTO> findByEmpresaAndStatusNativo(
        @Parameter("empresa") Long empresa, 
        @Parameter("statusPedido") String status
    );
}

@NativeQuery.Result
interface PedidoDTO {
    Long getNuNota();
    BigDecimal getVlrNota();
}
```

#### 3. Consultas com Operadores SQL

```java
@Repository
public interface ProdutoRepository extends JapeRepository<Long, Produto> {
    
    // Busca com LIKE
    @Criteria(clause = "DESCRPROD LIKE :termo")
    List<Produto> findByDescricaoContaining(String termo);
    
    // Busca com IN
    @Criteria(clause = "CODPROD IN (:codigos)")
    List<Produto> findByCodigos(List<Long> codigos);
    
    // Busca com IN NativeQuery e DTO
    @NativeQuery("SELECT CODPROD, DESCRPROD FROM TGFPRO WHERE CODPROD IN (:codigos)")
    List<ProdutoDTO> findByCodigosNativo(List<Long> codigos);
    
    // Busca com comparação numérica e NativeQuery
    @NativeQuery("SELECT CODPROD, DESCRPROD FROM TGFPRO WHERE VLRVENDA >= :valorMinimo")
    List<ProdutoDTO> findByValorMinimoNativo(@Parameter("valorMinimo") BigDecimal valorMinimo);
}

@NativeQuery.Result
interface ProdutoDTO {
    Long getCodProd();
    String getDescrProd();
}
```

Para cenários onde é necessário filtrar por combinações de valores em múltiplas colunas, use o tipo `ParamMatrix`. A sintaxe SQL difere entre Oracle e MSSQL.

<Callout icon="⚠️" theme="warn">
  ### **Importante:** Devido à diferença de sintaxe entre Oracle e MSSQL para `IN` com múltiplas colunas:

  * Com `@NativeQuery`: **Recomendado** usar arquivos XML com queries específicas por banco.
  * Com `@Criteria`: **não é possível** usar uma única query para ambos os bancos. Crie métodos separados para cada banco de dados.
</Callout>

**Exemplo com&#x20;**`@NativeQuery`**&#x20;e arquivo XML:**

```java
@JapeEntity(entity = "demo", table = "DEMO", description = "Entidade para demostrar consultas com ParamMatrix")
@Data
public class MyCustomEntity {

    @Id
    @Column(name = "ID", description = "id", dataType = DataType.INTEGER, isPresentation = true)
    @GeneratedValue(strategy = GeneratedValue.GenerationType.SEQUENCE)
    private Long id;

    @Column(name = "DESCRIPTION", description = "descri\u00E7\u00E3o", dataType = DataType.TEXT)
    private String description;
}
```

```java
@Repository
public interface MyCustomEntityRepository extends JapeRepository<Long, MyCustomEntity> {

    @NativeQuery(value = "queries/buscar-por-matriz.xml", fromFile = true)
    List<String> buscarDescricaoPorMatriz(@Parameter("matrix") ParamMatrix matrix);
}
```

**Arquivo:** `model/src/main/resources/queries/buscar-por-matriz.xml`

```xml
<sql>
    <oracle>
        SELECT DESCRIPTION FROM DEMO <!-- Onde, DEMO é o nome da tabela -->
        WHERE (ID, DESCRIPTION) IN (:matrix)
    </oracle>
    <mssql>
        SELECT DESCRIPTION
        FROM DEMO <!-- Onde, DEMO é o nome da tabela -->
        WHERE EXISTS (
            SELECT 1
            FROM (VALUES :matrix) valores(id, description)
            WHERE valores.id = DEMO.id <!-- Onde, DEMO é o nome da tabela -->
              AND valores.description = DEMO.description <!-- Onde, DEMO é o nome da tabela -->
        )
    </mssql>
</sql>
```

**Uso no serviço:**

```java
@Component
public class MyCustomEntityService {
    private final MyCustomEntityRepository repository;
    private final ProdutoRepository produtoRepository;

    @Inject
    public MyCustomEntityService(MyCustomEntityRepository repository, ProdutoRepository produtoRepository) {
        this.repository = repository;
        this.produtoRepository = produtoRepository;
    }

    public List<String> buscarPorCombinacoes() {
        
        ParamMatrix matrix = ParamMatrix.of(
            Arrays.asList(1L, "Descrição A"),
            Arrays.asList(2L, "Descrição B"),
            Arrays.asList(3L, "Descrição C")
        );
        return repository.buscarDescricaoPorMatriz(matrix);
    }
}
```

```java
// Operação com Produto
@Component
public class ProdutoService {
    private final ProdutoRepository produtoRepository;

    @Inject
    public ProdutoService(ProdutoRepository produtoRepository) {
        this.produtoRepository = produtoRepository;
    }
    
    public List<ProdutoDTO> buscarPorCombinacoesProduto() {
        // Construindo ParamMatrix a partir de uma lista de produtos
        List<Produto> produtos = produtoRepository.buscarProdutos();

        List<List<Object>> valores = produtos.stream()
                .map(p -> Arrays.asList((Object) p.getCategoriaProduto(), p.getNcm()))
                .collect(Collectors.toList());

        // Onde:
        // valores = [[1L, "Ncm A"], [2L, "Ncm B"], [3L, "Ncm C"]]
        // valores.toArray(new List[0]) retorna List[] = {[1L, "Ncm A"], [2L, "Ncm B"], ...}
        // ParamMatrix.of() recebe varargs List<?>...
        // Resultado: ParamMatrix.of([1L, "Ncm A"], [2L, "Ncm B"], [3L, "Ncm C"])
        ParamMatrix matrix = ParamMatrix.of(valores.toArray(new List[0]));

        return produtoRepository.findByPorMatrizCategoriaENcm(matrix);
    }

    public List<Produto> buscarPorCodigos(List<Long> codigos) {
        if (codigos == null || codigos.isEmpty()) {
            return Collections.emptyList();
        }
        return repository.findByCodigos(codigos);
    }
}
```

**Exemplo com&#x20;**`@Criteria`**&#x20;(métodos separados por banco):**

```java
@Repository
public interface MyCustomEntityRepository extends JapeRepository<Long, MyCustomEntity> {

    // Método para Oracle - sintaxe IN com tuplas
    @Criteria(clause = "(ID, DESCRIPTION) IN (:matrix)")
    List<MyCustomEntity> buscarPorMatrizOracle(@Parameter("matrix") ParamMatrix matrix);

    // Método para MSSQL - sintaxe EXISTS com VALUES
    @Criteria(clause = "EXISTS (SELECT 1 FROM (VALUES :matrix) valores(id, description) WHERE valores.id = DEMO.ID AND valores.description = DEMO.DESCRIPTION)") //Onde, DEMO é o nome da tabela
    List<MyCustomEntity> buscarPorMatrizMssql(@Parameter("matrix") ParamMatrix matrix);
}
```

**Uso no serviço com detecção de banco:**

```java
import br.com.sankhya.sdk.data.repository.helper.SqlHelper;

@Component
public class MyCustomEntityService {
    private final MyCustomEntityRepository repository;

    @Inject
    public SequenciaService(SequenciaRepository repository) {
        this.repository = repository;
    }

    public List<Sequencia> buscarPorCombinacoes() {
        ParamMatrix matrix = ParamMatrix.of(
            Arrays.asList(1L, "Descrição A"),
            Arrays.asList(2L, "Descrição B"),
            Arrays.asList(3L, "Descrição C")
        );

        if (SqlHelper.isOracle()) {
            return repository.buscarPorMatrizOracle(matrix);
        } else {
            return repository.buscarPorMatrizMssql(matrix);
        }
    }
}
```

<Callout icon="💡" theme="default">
  ### **Dica:** Para portabilidade entre bancos sem lógica condicional no serviço, prefira `@NativeQuery` com arquivos XML que definem queries específicas para cada banco automaticamente.
</Callout>

#### 4. Consultas com Funções SQL

```java
@Repository
public interface NotaRepository extends JapeRepository<Long, Nota> {
    
    // Usando função UPPER
    @Criteria(clause = "UPPER(NOMEPARC) = UPPER(:nome)")
    List<Nota> findByNomeParceiroCaseInsensitive(String nome);
    
    // Usando CONCAT com NativeQuery
    @NativeQuery("SELECT NUNOTA, CODTIPOPER FROM TGFCAB WHERE CONCAT(CODPARC, ' - ', NOMEPARC) LIKE :busca")
    List<NotaDTO> findByCodigoOuNomeParcNativo(@Parameter("busca") String busca);
}

@NativeQuery.Result
interface NotaDTO {
    Long getNuNota();
    Long getCodTipoOper();
}
```

#### 5. Consultas com Macros Sankhya

```java
@Repository
public interface MovimentacaoRepository extends JapeRepository<Long, Movimentacao> {
    
    // Usando macro dbDate()
    @Criteria(clause = "DTMOV = dbDate()")
    List<Movimentacao> findByDataAtual();
    
    // Usando macro com NativeQuery
    @NativeQuery("SELECT NUFIN, NUNOTA FROM TGFFIN WHERE DTMOV = dbDate()")
    List<MovimentacaoDTO> findByDataAtualNativo();
}

@NativeQuery.Result
interface MovimentacaoDTO {
    Long getNuFin();
    Long getNuNota();
}
```

#### 6. Consultas com Paginação

> Suportada apenas para `@Criteria`. `@NativeQuery` não suporta paginação.

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    
    // Busca páginada por status ativo
    @Criteria(clause = "ATIVO = :ativo")
    Page<Veiculo> findByAtivoPaginado(Boolean ativo, Pageable pageable);
}
```

```java
@Component
public class VeiculoService {

    private final VeiculoRepository repository;

    @Inject
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }

    public Page<Veiculo> buscarPorAtivoPaginado(Boolean ativo) {
        if (ativo == null) {
            throw new IllegalArgumentException("Ativo não pode ser nulo. Valores aceitos: true ou false");
        }
        // page: número da página (inicia em 0)
        // size: tamanho da página (mínimo 1)
        // sort: se não informado, ordena por ID de forma crescente.
        int page = 0;
        int size = 10;
        PageRequest pageRequest = PageRequest.of(page, size, Sort.by("PLACA", Direction.DESC));
        return repository.findByAtivoPaginado(ativo, pageRequest);
    }
}
```

#### 7. Entidade Com EmbbededID

```java
// Chave primária composta
@Embeddable
public class ItemNotaPK {
    @Column(name="NUNOTA")
    private Long numeroUnico;
    
    @Column(name="SEQUENCIA")
    private Long sequenciaItem;
    // getters e setters
}

// Entidade
@JapeEntity(entity="ItemNota", table="TGFITE")
public class ItemNota {
    @Id
    private ItemNotaPK id;
    
    @Column(name="CODPROD")
    private Long codProduto;
    
    @Column(name="CODVOL")
    private String unidadeMedida;
    // getters e setters
}

// Repositório
@Repository
public interface ItemNotaRepository extends JapeRepository<ItemNota, ItemNotaPK> {
    // Métodos CRUD para chave composta funcionam automaticamente
}
```

***

## Operações de Exclusão com @Delete

A anotação `@Delete` foi descontinuada. Utilize `@Modifying` em conjunto com `@NativeQuery` para todas as operações de `DELETE`.

***

## Limitações e Comportamento Atual

### 1. **Query Methods Não Suportados**

O SDK não suporta a criação de queries a partir do nome do método, como no Spring Data JPA.

```java
// ❌ NÃO SUPORTADO - Query methods do Spring
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    List<Veiculo> findByPlacaStartingWith(String prefix); // Não funciona
}

// ✅ SUPORTADO - Use @Criteria ou @NativeQuery
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    @Criteria(clause = "PLACA LIKE :prefix")
    List<Veiculo> findByPlacaStartingWith(@Parameter("prefix") String prefix);
}
```

### 2. **Controle de Quantidade de Registros**

Por padrão, as consultas são limitadas pela configuração de sessão do Sankhya (geralmente 500 registros).

```java
@Repository
public interface ProdutoRepository extends JapeRepository<Long, Produto> {
    
    // ⚠️ ATENÇÃO: Retorna no máximo 500 registros (configuração padrão da sessão)
    @Criteria(clause = "ATIVO = 'S'")
    List<Produto> findAllAtivos();
}
```

Para contornar essa limitação em consultas que podem retornar muitos dados, use paginação com `@Criteria` e `Pageable`.

***

## Boas Práticas

### 1. **Nomenclatura de Métodos**

```java
// ✅ BOM: Nomes descritivos e consistentes
@Criteria(clause = "PLACA = :placa")
Optional<Veiculo> findByPlaca(String placa);

// ❌ RUIM: Nomes genéricos
@Criteria(clause = "PLACA = :placa")
Optional<Veiculo> buscar(String placa);
```

### 2. **Uso de Optional para Resultados Únicos**

```java
// ✅ BOM: Optional para resultados que podem não existir
@Criteria(clause = "CODPROD = :codigo")
Optional<Produto> findByCodigo(String codigo);

// ❌ RUIM: Pode lançar exceção ou retornar null, exigindo verificação extra
@Criteria(clause = "CODPROD = :codigo")
Produto findByCodigo(String codigo);
```

### 3. **Validação de Parâmetros no Serviço**

```java
@Component
public class VeiculoService {
    private final VeiculoRepository repository;
    // ...
    
    // ✅ BOM: Validação antes da consulta
    public Optional<Veiculo> buscarPorPlaca(String placa) {
        if (placa == null || placa.trim().isEmpty()) {
            throw new IllegalArgumentException("Placa não pode ser vazia");
        }
        return repository.findByPlaca(placa.toUpperCase());
    }
}
```

***

## Anti-Patterns

### 1. **Consultas Muito Genéricas**

```java
// ❌ RUIM: Consulta pode retornar muitos registros e causar problemas de performance
@Criteria(clause = "1 = 1")
List<Produto> findAll();

// ✅ BOM: Consultas específicas com filtros obrigatórios
@Criteria(clause = "ATIVO = 'S' AND CODEMP = :empresa")
List<Produto> findAtivosByEmpresa(Long empresa);
```

### 2. **Uso Incorreto de @Modifying**

```java
// ❌ RUIM: @Modifying sem transação
public class LogService {
    public int limparLogsAntigos(LocalDate data) {
        // Pode falhar e deixar o banco em estado inconsistente
        return logRepository.excluirLogsExpirados(data);
    }
}

// ✅ BOM: @Modifying dentro de uma transação
@Component
public class LogService {
    @Transactional
    public int limparLogsAntigos(LocalDate data) {
        return logRepository.excluirLogsExpirados(data);
    }
}
```

### 3. **Lógica de Negócio no Repositório**

Os repositórios devem se limitar ao acesso a dados. A lógica de negócio pertence à camada de serviço ou componente.

```java
// ❌ RUIM: Lógica de negócio no repositório
@Repository
public interface PedidoRepository extends JapeRepository<Long, Pedido> {
    default void aprovarPedido(Long nunota) {
        // ... lógica para aprovar ...
    }
}

// ✅ BOM: Lógica no serviço
@Component
public class PedidoService {
    private final PedidoRepository repository;
    // ...
    @Transactional
    public void aprovarPedido(Long nunota) {
        Pedido pedido = repository.findByPK(nunota).orElseThrow(...);
        // ... lógica para aprovar ...
        repository.save(pedido);
    }
}
```

***

## Exemplo Completo: Repository de E-commerce

```java
// --- Entidade ---
@JapeEntity(entity = "CabecalhoNota", table = "TGFCAB")
@Data
public class Pedido {
    @Id @Column(name = "NUNOTA")
    private Long numero;
    @Column(name = "CODPARC")
    private Long codigoCliente;
    @Column(name = "VLRNOTA")
    private BigDecimal valor;
    @Column(name = "STATUS")
    private String status; // "R" = Rascunho, "A" = Aprovado
    @Column(name = "DHALTER")
    private LocalDateTime dataAlteracao;
}

// --- DTO ---
@NativeQuery.Result
public interface PedidoResumoDTO {
    Long getNumero();
    BigDecimal getValor();
}

// --- Repositório ---
@Repository
public interface PedidoRepository extends JapeRepository<Pedido, Long> {
    
    @Criteria(clause = "CODPARC = :codigoCliente")
    List<Pedido> findByCliente(@Parameter("codigoCliente") Long codigoCliente);
    
    @NativeQuery("SELECT NUNOTA as numero, VLRNOTA as valor FROM TGFCAB WHERE STATUS = :status AND CODEMP = :empresa")
    List<PedidoResumoDTO> findResumoPorStatus(
        @Parameter("status") String status, 
        @Parameter("empresa") Long empresa
    );
    
    @Modifying
    @NativeQuery("DELETE FROM TGFCAB WHERE STATUS = 'R' AND DHALTER < :dataLimite")
    int deleteRascunhosAntigos(@Parameter("dataLimite") LocalDateTime dataLimite);
}

// --- Serviço ---
@Component
public class PedidoService {
    
    private final PedidoRepository pedidoRepository;
    
    @Inject
    public PedidoService(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }
    
    @Transactional
    public void limparRascunhosAntigos() {
        LocalDateTime dataLimite = LocalDateTime.now().minusDays(30);
        int removidos = pedidoRepository.deleteRascunhosAntigos(dataLimite);
        System.out.println("Removidos " + removidos + " rascunhos antigos.");
    }
    
    public List<Pedido> buscarPedidosDoCliente(Long codigoCliente) {
        if (codigoCliente == null) {
            throw new IllegalArgumentException("Código do cliente é obrigatório.");
        }
        return pedidoRepository.findByCliente(codigoCliente);
    }
}
```

***

## 🚀 **Recursos Implementados**

As seguintes funcionalidades estão disponíveis e testadas:

* ✅ **CRUD Automático**: `save()`, `findByPK()`, `findAll()`, `delete()`
* ✅ **Consultas com Critérios**: `@Criteria` com parâmetros nomeados e múltiplas condições
* ✅ **Consultas Nativas**: `@NativeQuery` para SQL complexo e mapeamento para DTOs
* ✅ **Atualizações Nativas**: `@Modifying` em conjunto com `@NativeQuery` para operações de `UPDATE`, `INSERT` e `DELETE` em massa
* ✅ **Funções SQL e Macros Sankhya**: Suporte completo em `@Criteria` e `@NativeQuery`
* ✅ **Type Safety**: Parâmetros e retornos fortemente tipados
* ✅ **Suporte a&#x20;**`Optional<T>`: Para resultados únicos que podem não existir
* ✅ **Suporte a&#x20;**`List<T>`: Para múltiplos resultados
* ✅ **Paginação**: `Page<T>` para resultados paginados com `@Criteria`

O padrão Repository no SDK Sankhya oferece uma abstração poderosa e flexível para acesso a dados, mantendo a simplicidade e familiaridade com padrões de mercado como Spring Data JPA, enquanto se integra perfeitamente com o ecossistema Sankhya.
