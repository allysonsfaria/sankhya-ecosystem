---
id: "https://developer.sankhya.com.br/docs/injeção-de-valores-value"
titulo: "💉 Injeção de Valores (`@Value`)"
url: "https://developer.sankhya.com.br/docs/injeção-de-valores-value"
atualizado_em: "2026-09-08T19:13:15.000Z"
---

# 💉 Injeção de Valores (`@Value`)

<br />

# 💉 Injeção de Valores (`@Value`)

A anotação `@Value` permite injetar valores de configuração de diferentes fontes (variáveis de ambiente, propriedades do sistema ou parâmetros Sankhya) diretamente em seus componentes, tornando o código mais limpo, testável e desacoplado.

***

## 🤔 Por que usar `@Value`?

* ✅ **Desacoplamento:** Separa configuração do código, facilitando mudanças entre ambientes
* ✅ **Múltiplas Fontes:** Suporte para variáveis de ambiente, propriedades do sistema e parâmetros Sankhya
* ✅ **Injeção Lazy:** Valores resolvidos sob demanda com cache automático para performance
* ✅ **Type-Safe:** Conversão automática para tipos primitivos (Integer, Boolean, etc.)
* ✅ **Valores Padrão:** Fallback quando a propriedade não está disponível
* ✅ **Thread-Safe:** Implementação segura para ambientes multi-thread

***

## 📊 Abordagem Antiga vs. Nova

### ❌ Abordagem Tradicional

```java
// Código legado: acoplado e repetitivo
public class PedidoService extends ServiceBean {
    public void processar(ServiceContext ctx) throws Exception {
        // Busca manual de parâmetros
        String dbUrl = System.getenv("DATABASE_URL");
        if (dbUrl == null) {
            dbUrl = "jdbc:h2:mem:test"; // Valor padrão hardcoded
        }
        
        String portStr = System.getProperty("server.port");
        int port = 8080;
        if (portStr != null) {
            try {
                port = Integer.parseInt(portStr); // Conversão manual
            } catch (NumberFormatException e) {
                // Tratamento de erro manual
            }
        }
        
        // Busca de parâmetros Sankhya
        Object maxConn = MGECoreParameter.getParameter("MAX_CONNECTIONS");
        int maxConnections = 10;
        if (maxConn != null) {
            maxConnections = Integer.parseInt(maxConn.toString());
        }
        
        // ... lógica do serviço
    }
}
```

### ✅ Nova Abordagem com `@Value`

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoService {
    
    // Injeção eager: valor resolvido imediatamente
    @Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
    private Integer serverPort;
    
    // Injeção lazy: valor resolvido sob demanda e cacheado
    @Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "jdbc:h2:mem:test")
    private Provider<String> databaseUrl;
    
    @Value(param = "MAX_CONNECTIONS", type = ValueType.SANKHYA_PARAM, defaultValue = "10")
    private Provider<Integer> maxConnections;
    
    @Transactional
    public void processar(@Valid PedidoDTO pedido) {
        // Valores já disponíveis, convertidos e validados automaticamente
        String url = databaseUrl.get(); // Lazy: resolve e cacheia
        int port = serverPort; // Eager: já está disponível
        
        // ... lógica do serviço
    }
}
```

***

## ⚙️ Tipos de Injeção

### 1. 🚀 Injeção Eager (Direta)

O valor é **resolvido imediatamente** durante a criação do objeto. Use para configurações sempre necessárias.

```java
@Component
public class DatabaseConfig {
    
    @Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
    private Integer serverPort;
    
    @Value(value = "debug.enabled", type = ValueType.SYSTEM_PROPERTY, defaultValue = "false")
    private Boolean debugEnabled;
    
    @Value(value = "app.name", type = ValueType.ENV_VAR, defaultValue = "MyApp")
    private String appName;
    
    public void initialize() {
        // Valores já disponíveis imediatamente
        System.out.println("Servidor na porta: " + serverPort);
        System.out.println("Debug: " + debugEnabled);
    }
}
```

**Quando usar:**

* ✅ Valores necessários imediatamente na inicialização
* ✅ Propriedades sempre utilizadas
* ✅ Configurações críticas do sistema

### 2. ⚡ Injeção Lazy com Cache (Recomendado)

O valor é resolvido **apenas na primeira chamada** de `get()` e então **cacheado** para uso posterior.

```java
@Component
public class ServiceConfig {
    
    @Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "jdbc:h2:mem:test")
    private Provider<String> databaseUrl;
    
    @Value(param = "MAX_CONNECTIONS", type = ValueType.SANKHYA_PARAM, defaultValue = "10")
    private Provider<Integer> maxConnections;
    
    @Value(param = "FEATURE_FLAG", type = ValueType.SANKHYA_PARAM, defaultValue = "false")
    private Provider<Boolean> featureFlag;
    
    public void conectar() {
        if (featureFlag.get()) { // Lazy: resolve apenas se necessário
            String url = databaseUrl.get(); // Primeira chamada: resolve e cacheia
            int max = maxConnections.get(); // Segunda vez que acessar: usa cache
            
            // ... lógica de conexão
        }
        // Se featureFlag for false, databaseUrl e maxConnections nunca são resolvidos
    }
}
```

**Quando usar:**

* ✅ Valores que podem não ser necessários (uso condicional)
* ✅ Propriedades de configuração opcional
* ✅ Otimização de performance (evita resoluções desnecessárias)

**Benefícios do Cache:**

```java
// Primeira chamada: busca o valor e cacheia (pode ser custoso)
String url1 = databaseUrl.get(); // Resolução + Cache

// Chamadas subsequentes: usa o cache (instantâneo)
String url2 = databaseUrl.get(); // Do cache
String url3 = databaseUrl.get(); // Do cache
String url4 = databaseUrl.get(); // Do cache
```

***

## 🎯 Fontes de Propriedades

### 1. Variáveis de Ambiente (`ENV_VAR`)

Busca valores de variáveis de ambiente do sistema operacional.

```java
@Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "jdbc:h2:mem:test")
private Provider<String> databaseUrl;

@Value(value = "API_KEY", type = ValueType.ENV_VAR, defaultValue = "")
private String apiKey;
```

**Como definir:**

```bash
# Linux/Mac
export DATABASE_URL=jdbc:postgresql://localhost:5432/mydb
export API_KEY=my-secret-key

# Windows
set DATABASE_URL=jdbc:postgresql://localhost:5432/mydb
set API_KEY=my-secret-key
```

### 2. Propriedades do Sistema (`SYSTEM_PROPERTY`)

Busca valores de propriedades do sistema Java (definidas com `-D`).

```java
@Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
private Integer serverPort;

@Value(value = "debug.enabled", type = ValueType.SYSTEM_PROPERTY, defaultValue = "false")
private Boolean debugEnabled;
```

**Como definir:**

```bash
# Via linha de comando
java -Dserver.port=9090 -Ddebug.enabled=true -jar myapp.jar

# Programaticamente
System.setProperty("server.port", "9090");
```

### 3. Parâmetros Sankhya (`SANKHYA_PARAM`)

Busca valores dos parâmetros do sistema Sankhya via `MGECoreParameter`.

**Sem grupo:**

```java
@Value(param = "MAX_CONNECTIONS", type = ValueType.SANKHYA_PARAM, defaultValue = "10")
private Provider<Integer> maxConnections;
```

**Com grupo:**

```java
@Value(param = "TIMEOUT", group = "CONNECTION", type = ValueType.SANKHYA_PARAM, defaultValue = "30")
private Provider<Long> connectionTimeout;

@Value(param = "RETRY_COUNT", group = "HTTP", type = ValueType.SANKHYA_PARAM, defaultValue = "3")
private Integer retryCount;
```

### 4. Valor Indefinido (`UNDEFINED`)

Sempre usa o `defaultValue`. Útil para valores fixos ou testes.

```java
@Value(value = "fallback", type = ValueType.UNDEFINED, defaultValue = "default-value")
private String fallbackValue; // Sempre será "default-value"
```

***

## 🔧 Tipos Suportados

A conversão de tipos é automática:

| Tipo Java             | Exemplo                                                                                   |
| :-------------------- | :---------------------------------------------------------------------------------------- |
| `String`              | `@Value(...) private String texto;`                                                       |
| `Integer` / `int`     | `@Value(...) private Integer numero;`                                                     |
| `Boolean` / `boolean` | `@Value(...) private Boolean flag;`                                                       |
| `Long` / `long`       | `@Value(...) private Long id;`                                                            |
| `Double` / `double`   | `@Value(...) private Double preco;`                                                       |
| `Float` / `float`     | `@Value(...) private Float taxa;`                                                         |
| `Provider<T>`         | `@Value(...) private Provider<String> lazy;` (suporta todos os tipos acima como genérico) |

**Conversão Automática:**

```java
// String "8080" → Integer 8080
@Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
private Integer serverPort;

// String "true" → Boolean true
@Value(value = "debug.enabled", type = ValueType.ENV_VAR, defaultValue = "false")
private Boolean debugEnabled;

// String "3.14" → Double 3.14
@Value(value = "taxa", type = ValueType.SANKHYA_PARAM, defaultValue = "0.0")
private Double taxa;
```

***

## 📝 Anatomia da Anotação

```java
@Value(
    value = "PROPERTY_NAME",        // Nome da propriedade (alternativa a param)
    param = "PROPERTY_NAME",         // Nome do parâmetro (alternativa a value)
    group = "GROUP_NAME",            // Grupo (apenas para SANKHYA_PARAM)
    type = ValueType.ENV_VAR,        // Tipo da fonte (obrigatório)
    defaultValue = "default"         // Valor padrão (fallback)
)
```

| Atributo       | Obrigatório | Descrição                                                      |
| :------------- | :---------- | :------------------------------------------------------------- |
| `value`        | ❌           | Nome da propriedade. Alternativa a `param`.                    |
| `param`        | ❌           | Nome do parâmetro. Alternativa a `value`. Tem precedência.     |
| `group`        | ❌           | Grupo do parâmetro (usado apenas com `SANKHYA_PARAM`).         |
| `type`         | ✅           | Tipo da fonte (`ENV_VAR`, `SYSTEM_PROPERTY`, `SANKHYA_PARAM`). |
| `defaultValue` | ✅           | Valor padrão usado quando a propriedade não é encontrada.      |

<Callout icon="⚠️" theme="warn">
  ### **Importante:** Ao menos um entre `value` ou `param` deve ser fornecido. Se ambos forem especificados, `param` tem precedência.
</Callout>

***

## 💡 Exemplos Práticos

### Exemplo 1: Configuração de Banco de Dados

```java
@Component
public class DatabaseConfig {
    
    // Lazy: resolve apenas quando conectar
    @Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, 
           defaultValue = "jdbc:h2:mem:test")
    private Provider<String> databaseUrl;
    
    @Value(value = "DB_USERNAME", type = ValueType.ENV_VAR, 
           defaultValue = "sa")
    private Provider<String> username;
    
    @Value(value = "DB_PASSWORD", type = ValueType.ENV_VAR, 
           defaultValue = "")
    private Provider<String> password;
    
    @Value(param = "MAX_POOL_SIZE", type = ValueType.SANKHYA_PARAM, 
           defaultValue = "20")
    private Provider<Integer> maxPoolSize;
    
    public Connection conectar() {
        // Valores resolvidos apenas quando necessário
        return DriverManager.getConnection(
            databaseUrl.get(),
            username.get(),
            password.get()
        );
    }
}
```

### Exemplo 2: Feature Flags

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoService {
    
    @Value(param = "VALIDACAO_AVANCADA_ATIVA", type = ValueType.SANKHYA_PARAM, 
           defaultValue = "false")
    private Provider<Boolean> validacaoAvancadaAtiva;
    
    @Value(param = "NOVO_CALCULO_IMPOSTO", type = ValueType.SANKHYA_PARAM, 
           defaultValue = "false")
    private Provider<Boolean> novoCalculoImposto;
    
    @Inject
    private ValidadorAvancado validadorAvancado;
    
    @Inject
    private CalculadoraImpostoV2 calculadoraV2;
    
    @Transactional
    public void processar(@Valid PedidoDTO pedido) {
        // Feature flag: só resolve e usa se ativado
        if (validacaoAvancadaAtiva.get()) {
            validadorAvancado.validar(pedido);
        }
        
        if (novoCalculoImposto.get()) {
            calculadoraV2.calcular(pedido);
        } else {
            // Lógica antiga
        }
    }
}
```

### Exemplo 3: Configuração Multi-Ambiente

```java
@Component
public class ApiConfig {
    
    // Eager: sempre necessário
    @Value(value = "ENVIRONMENT", type = ValueType.ENV_VAR, 
           defaultValue = "development")
    private String environment;
    
    // Lazy: pode variar por ambiente
    @Value(value = "API_BASE_URL", type = ValueType.ENV_VAR, 
           defaultValue = "http://localhost:8080")
    private Provider<String> apiBaseUrl;
    
    @Value(value = "API_TIMEOUT", type = ValueType.SYSTEM_PROPERTY, 
           defaultValue = "30000")
    private Provider<Integer> timeout;
    
    @Value(value = "API_KEY", type = ValueType.ENV_VAR, 
           defaultValue = "dev-key")
    private Provider<String> apiKey;
    
    public boolean isProduction() {
        return "production".equalsIgnoreCase(environment);
    }
    
    public HttpClient createClient() {
        return HttpClient.newBuilder()
            .connectTimeout(Duration.ofMillis(timeout.get()))
            .build();
    }
}
```

***

## ✨ Boas Práticas

### 1. ✅ Sempre Forneça `defaultValue`

```java
// ✅ BOM: Tem fallback
@Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "jdbc:h2:mem:test")
private Provider<String> databaseUrl;

// ❌ EVITE: Sem fallback (pode causar erros)
@Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "")
private Provider<String> databaseUrl;
```

### 2. ✅ Use Lazy para Valores Opcionais

```java
// ✅ BOM: Lazy para valores condicionais
@Value(param = "FEATURE_FLAG", type = ValueType.SANKHYA_PARAM, defaultValue = "false")
private Provider<Boolean> featureFlag;

public void executar() {
    if (featureFlag.get()) { // Resolve apenas se necessário
        // ...
    }
}
```

### 3. ✅ Use Eager para Configurações Críticas

```java
// ✅ BOM: Eager para valores sempre necessários
@Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
private Integer serverPort;

public void initialize() {
    // serverPort já está disponível
    System.out.println("Iniciando na porta: " + serverPort);
}
```

### 4. ✅ Prefira Tipos Específicos

```java
// ✅ BOM: Tipo específico (conversão automática)
@Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
private Integer serverPort;

// ❌ EVITE: String quando deveria ser Integer
@Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
private String serverPort; // Teria que fazer Integer.parseInt() manualmente
```

### 5. ✅ Documente os Parâmetros

```java
@Component
public class EmailConfig {
    
    /**
     * URL do servidor SMTP.
     * Variável de ambiente: SMTP_HOST
     * Padrão: smtp.gmail.com
     */
    @Value(value = "SMTP_HOST", type = ValueType.ENV_VAR, defaultValue = "smtp.gmail.com")
    private Provider<String> smtpHost;
    
    /**
     * Porta do servidor SMTP.
     * Propriedade do sistema: smtp.port
     * Padrão: 587
     */
    @Value(value = "smtp.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "587")
    private Integer smtpPort;
}
```

***

## 🚫 Anti-Patterns

### ❌ Não Use `@Value` em Constantes

```java
// ❌ MAL: @Value em campo final/constante
@Value(value = "APP_NAME", type = ValueType.ENV_VAR, defaultValue = "MyApp")
private final String APP_NAME; // Não funciona!

// ✅ BOM: Use campo não-final
@Value(value = "APP_NAME", type = ValueType.ENV_VAR, defaultValue = "MyApp")
private String appName;
```

### ❌ Não Misture Lógica de Negócio com Configuração

```java
// ❌ MAL: Lógica de negócio baseada em configuração hardcoded
@Value(param = "TAXA_PADRAO", type = ValueType.SANKHYA_PARAM, defaultValue = "0.05")
private Double taxaPadrao;

public BigDecimal calcularTotal(BigDecimal valor) {
    // Lógica de negócio acoplada à configuração
    return valor.multiply(BigDecimal.valueOf(1 + taxaPadrao));
}

// ✅ BOM: Separe configuração de lógica
@Component
public class CalculadoraService {
    @Inject
    private TaxaConfig taxaConfig;
    
    public BigDecimal calcularTotal(BigDecimal valor) {
        Double taxa = taxaConfig.getTaxaPadrao().get();
        return valor.multiply(BigDecimal.valueOf(1 + taxa));
    }
}
```

### ❌ Não Abuse de Valores Padrão Complexos

```java
// ❌ MAL: Valor padrão muito complexo
@Value(value = "CONFIG_JSON", type = ValueType.ENV_VAR, 
       defaultValue = "{\"host\":\"localhost\",\"port\":8080,\"ssl\":true}")
private String configJson;

// ✅ BOM: Use múltiplos valores simples
@Value(value = "SERVER_HOST", type = ValueType.ENV_VAR, defaultValue = "localhost")
private String host;

@Value(value = "SERVER_PORT", type = ValueType.ENV_VAR, defaultValue = "8080")
private Integer port;

@Value(value = "SSL_ENABLED", type = ValueType.ENV_VAR, defaultValue = "true")
private Boolean sslEnabled;
```

***

## 🔍 Troubleshooting

### Valor Não Está Sendo Injetado

**Problema:** O campo anotado com `@Value` está `null`.

**Soluções:**

1. Verifique se a classe está anotada com um estereótipo (`@Service`, `@Component`, `@Repository`)
2. Confirme que a classe está sendo gerenciada pelo Guice (não criada com `new`)
3. Verifique se o tipo do campo é suportado

```java
// ❌ Não funciona: classe não gerenciada
public class MinhaClasse {
    @Value(...)
    private String valor; // Será null
}

// ✅ Funciona: classe gerenciada
@Component
public class MinhaClasse {
    @Value(...)
    private String valor; // Injetado corretamente
}
```

### Conversão de Tipo Falhou

**Problema:** Erro ao converter string para tipo numérico.

**Solução:** Use `defaultValue` com formato correto e trate entradas inválidas.

```java
// Se a propriedade contém "abc" em vez de número, usa defaultValue
@Value(value = "TIMEOUT", type = ValueType.SYSTEM_PROPERTY, defaultValue = "30")
private Integer timeout; // Se TIMEOUT="abc", timeout será 30
```

### Cache Não Está Sendo Atualizado

**Problema:** Valores lazy não refletem mudanças em runtime.

**Explicação:** O cache é proposital! Valores são resolvidos uma vez por instância.

**Solução para Testes:**

```java
// Para testes, você pode limpar o cache
ValueProvider<String> provider = (ValueProvider<String>) databaseUrl;
provider.clearCache(); // Força nova resolução
```

***

## 🎯 Resumo

| Aspecto                  | Injeção Eager          | Injeção Lazy                      |
| :----------------------- | :--------------------- | :-------------------------------- |
| **Sintaxe**              | `private String valor` | `private Provider<String> valor`  |
| **Momento da Resolução** | Criação do objeto      | Primeira chamada de `get()`       |
| **Cache**                | N/A (já resolvido)     | ✅ Sim (após primeira resolução)   |
| **Performance**          | Resolve sempre         | Resolve apenas se necessário      |
| **Uso Recomendado**      | Configurações críticas | Valores opcionais ou condicionais |
| **Thread-Safety**        | ✅ Sim                  | ✅ Sim (double-checked locking)    |

**Escolha:**

* Use **Eager** quando o valor for sempre necessário
* Use **Lazy** quando o valor for opcional ou condicional (feature flags, etc.)
* Sempre forneça `defaultValue` para comportamento previsível
* Documente suas configurações para facilitar manutenção

***

## 📚 Veja Também

* [Injeção de Dependências](06_dependency_injection.md)
* [Serviços](03_service.md)
* [Componentes](01_core_concepts.md)
