---
id: "https://developer.sankhya.com.br/docs/11_controller_advice"
titulo: "🛡️ Tratamento Global de Exceções (`@ControllerAdvice`)"
url: "https://developer.sankhya.com.br/docs/11_controller_advice"
atualizado_em: "2026-09-08T19:13:08.000Z"
---

# 🛡️ Tratamento Global de Exceções (`@ControllerAdvice`)

<br />

# 🛡️ Tratamento Global de Exceções (`@ControllerAdvice`)

O `@ControllerAdvice` é uma anotação que permite criar um **ponto centralizado de tratamento de exceções** para todos os seus serviços (`@Service`). Com ela, você pode interceptar exceções lançadas durante a execução de métodos de serviço e retornar respostas personalizadas, registrar logs detalhados e garantir que erros sejam tratados de forma consistente em toda a aplicação.

***

## 🤔 Por que usar `@ControllerAdvice`?

* ✅ **Centralização:** Todo o tratamento de exceções fica em um único lugar, evitando código duplicado.
* ✅ **Respostas Consistentes:** Garante que todas as exceções retornem uma estrutura de resposta padronizada.
* ✅ **Logging Estruturado:** Facilita a implementação de estratégias de log centralizadas e bem organizadas.
* ✅ **Separação de Responsabilidades:** Seus serviços ficam focados na lógica de negócio, enquanto o `@ControllerAdvice` cuida dos erros.
* ✅ **Manutenibilidade:** Mudanças na forma de tratar erros são feitas em um único local.
* ✅ **Rollback Automático:** Quando uma exceção é capturada e tratada, a transação é automaticamente revertida se houver uma ativa.

***

## 📊 Abordagem Antiga vs. Nova

### ❌ Abordagem Tradicional (Try-Catch em Todo Lugar)

No modelo antigo, cada serviço precisava ter seu próprio bloco `try-catch`, resultando em código repetitivo, difícil de manter e propenso a inconsistências.

```java
/**
 * @ejb.bean name="PedidoServiceSP"
 * jndi-name="pacote/da/classe/PedidoServiceSP"
 * type="Stateless" transaction-type="Container" view-type="remote"
 * @ejb.transaction type="Supports"
 * @ejb.util generate="false"
 */
public class PedidoServiceSPBean extends ServiceBean {
    public void criarPedido(ServiceContext sctx) throws Exception {
        try {
            // Lógica de negócio
            processarPedido();
        } catch (ObjectNotFoundException e) {
            // Tratamento manual em cada serviço
            sctx.setJsonResponse(construirErroManualmente(e));
            logger.error("Erro ao criar pedido: " + e.getMessage());
        } catch (ValidationException e) {
            // Outro tratamento manual
            sctx.setJsonResponse(construirOutroErroManualmente(e));
            logger.error("Validação falhou: " + e.getMessage());
        } catch (Exception e) {
            // Tratamento genérico
            logger.error("Erro inesperado", e);
            throw e;
        }
    }

    public void cancelarPedido(ServiceContext sctx) throws Exception {
        try {
            // Mesma lógica de tratamento repetida aqui
            cancelar();
        } catch (ObjectNotFoundException e) {
            sctx.setJsonResponse(construirErroManualmente(e));
            logger.error("Erro ao cancelar pedido: " + e.getMessage());
        } // ... e assim por diante
    }
}
```

**Problemas:**

* ❌ Código duplicado em múltiplos serviços
* ❌ Inconsistência no formato das respostas de erro
* ❌ Difícil manutenção: mudanças precisam ser replicadas em vários lugares
* ❌ Logs desorganizados e difíceis de padronizar
* ❌ Serviços sobrecarregados com lógica de tratamento de erros

### ✅ Nova Abordagem com `@ControllerAdvice`

Com o SDK, você cria uma classe anotada com `@ControllerAdvice` que intercepta as exceções automaticamente. Seus serviços ficam limpos e focados na lógica de negócio.

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = Logger.getLogger(GlobalExceptionHandler.class.getName());

    @ExceptionHandler({ObjectNotFoundException.class})
    public ErrorResponse handleObjectNotFound(ObjectNotFoundException e) {
        logger.log(Level.WARNING, "Recurso não encontrado", e);
        return new ErrorResponse("RESOURCE_NOT_FOUND", "O recurso solicitado não foi encontrado.");
    }

    @ExceptionHandler({ValidationException.class})
    public ErrorResponse handleValidation(ValidationException e) {
        logger.log(Level.WARNING, "Erro de validação", e);
        return new ErrorResponse("VALIDATION_ERROR", e.getMessage());
    }

    @ExceptionHandler({JapeSessionInterruptedError.class})
    public ErrorResponse handleSessionInterruptedError(JapeSessionInterruptedError e) {
        logger.log(Level.SEVERE, "Erro de Interrupção de Sessão JAPE", e);
        return new ErrorResponse("JAPE_ERROR", "Ocorreu um erro de Interrupção de Sessão JAPE.");
    }
}

// Seus serviços ficam limpos:
@Service(serviceName = "PedidoServiceSP")
public class PedidoService {
    private final PedidoBusinessService businessService;

    @Inject
    public PedidoService(PedidoBusinessService businessService) {
        this.businessService = businessService;
    }

    @Transactional
    public void criarPedido(@Valid PedidoDTO pedido) {
        // Sem try-catch! Se houver erro, o GlobalExceptionHandler cuida
        businessService.criar(pedido);
    }

    @Transactional
    public void cancelarPedido(Long pedidoId) {
        // Código limpo e focado
        businessService.cancelar(pedidoId);
    }
}
```

***

## 🚀 Como Funciona?

### Estrutura Básica

Uma classe `@ControllerAdvice` contém métodos anotados com `@ExceptionHandler` que definem quais exceções devem ser interceptadas e como tratá-las.

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler({MinhaException.class})
    public MeuObjetoResposta handleMinhaException(MinhaException e) {
        // Lógica de tratamento
        return new MeuObjetoResposta(...);
    }
}
```

### Características Principais

1. **Anotação&#x20;**`@ControllerAdvice`: Marca a classe como um manipulador global de exceções.

2. **Anotação&#x20;**`@ExceptionHandler`: Define quais exceções o método deve tratar.
   * Aceita um array de classes de exceção: `@ExceptionHandler({ExceptionA.class, ExceptionB.class})`
   * Cada exceção declarada pode ser tratada pelo mesmo método.

3. **Tipo do Parâmetro**: O método recebe como parâmetro a exceção que está sendo tratada.
   * O tipo do parâmetro pode ser **mais genérico** que as exceções declaradas em `@ExceptionHandler`.
   * Exemplo: `@ExceptionHandler({IOException.class, SQLException.class})` pode ter um parâmetro `Exception e`.

4. **Tipo de Retorno**: O método deve retornar um objeto ou tipo primitivo que será serializado para JSON e enviado como resposta.
   * ❌ **Não pode retornar&#x20;**`void` - o método deve sempre retornar um objeto ou tipo primitivo.
   * O objeto retornado será convertido automaticamente para JSON usando Gson.

5. **Rollback Automático**: Se houver uma transação ativa, ela será automaticamente revertida (`setRollbackOnly()`) quando a exceção for capturada.

***

## 📖 Exemplos Práticos

### Exemplo 1: Tratamento de Exceções Específicas

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = Logger.getLogger(GlobalExceptionHandler.class.getName());

    @ExceptionHandler({ObjectNotFoundException.class})
    public ErrorResponse handleObjectNotFound(ObjectNotFoundException e) {
        logger.log(Level.WARNING, "Objeto não encontrado: {0}", e.getMessage());

        return new ErrorResponse(
            "NOT_FOUND",
            "O recurso solicitado não existe.",
            404
        );
    }

    @ExceptionHandler({IllegalArgumentException.class})
    public ErrorResponse handleIllegalArgument(IllegalArgumentException e) {
        logger.log(Level.WARNING, "Argumento inválido fornecido", e);

        return new ErrorResponse(
            "BAD_REQUEST",
            e.getMessage(),
            400
        );
    }
}

// Classe de resposta de erro padronizada
public class ErrorResponse {
    private String code;
    private String message;
    private int status;
    private long timestamp;

    public ErrorResponse(String code, String message, int status) {
        this.code = code;
        this.message = message;
        this.status = status;
        this.timestamp = System.currentTimeMillis();
    }

    // Getters e setters
}
```

### Exemplo 2: Tratamento de Múltiplas Exceções no Mesmo Método

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = Logger.getLogger(GlobalExceptionHandler.class.getName());

    @ExceptionHandler({IOException.class, SQLException.class, TimeoutException.class})
    public ErrorResponse handleInfrastructureErrors(Exception e) {
        // Parâmetro genérico (Exception) pode receber qualquer uma das exceções declaradas
        logger.log(Level.SEVERE, "Erro de infraestrutura detectado", e);

        return new ErrorResponse(
            "INFRASTRUCTURE_ERROR",
            "Erro ao processar a requisição. Por favor, tente novamente.",
            503
        );
    }

    @ExceptionHandler({ArrayIndexOutOfBoundsException.class, NullPointerException.class})
    public ErrorResponse handleProgrammingErrors(RuntimeException e) {
        logger.log(Level.SEVERE, "Erro de programação crítico", e);

        return new ErrorResponse(
            "INTERNAL_ERROR",
            "Ocorreu um erro interno no sistema.",
            500
        );
    }
}
```

### Exemplo 3: Respostas Customizadas por Tipo de Exceção

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = Logger.getLogger(GlobalExceptionHandler.class.getName());

    @ExceptionHandler({ObjectNotFoundException.class})
    public NotFoundResponse handleNotFound(ObjectNotFoundException e) {
        logger.log(Level.INFO, "Recurso não encontrado: {0}", e.getMessage());

        return new NotFoundResponse(
            e.getMessage(),
            "Verifique se o ID informado está correto."
        );
    }

    @ExceptionHandler({ValidationException.class})
    public ValidationErrorResponse handleValidation(ValidationException e) {
        logger.log(Level.WARNING, "Erro de validação", e);

        return new ValidationErrorResponse(
            "VALIDATION_FAILED",
            e.getErrors() // Lista de erros de validação
        );
    }
}

// Diferentes classes de resposta para diferentes cenários
public class NotFoundResponse {
    private String message;
    private String hint;
    // Getters e setters
}

public class ValidationErrorResponse {
    private String code;
    private List<String> errors;
    // Getters e setters
}
```

***

## 🔍 Integração com `@Service`

O `@ControllerAdvice` funciona automaticamente com todos os seus serviços anotados com `@Service`. Qualquer exceção não capturada que sair de um método de serviço será interceptada pelo handler apropriado.

```java
@Service(serviceName = "UsuarioServiceSP")
public class UsuarioService {
    private final UsuarioRepository repository;

    @Inject
    public UsuarioService(UsuarioRepository repository) {
        this.repository = repository;
    }

    @Transactional
    public UsuarioDTO buscarPorId(Long id) {
        // Se o usuário não existir, lança ObjectNotFoundException
        Usuario usuario = repository.findByPK(id)
            .orElseThrow(() -> new ObjectNotFoundException("Usuário não encontrado: " + id));

        return UsuarioMapper.toDTO(usuario);
    }

    @Transactional
    public void salvar(@Valid UsuarioDTO dto) {
        // Se a validação falhar, lança ValidationException
        // Ambas as exceções são automaticamente capturadas pelo GlobalExceptionHandler
        Usuario usuario = UsuarioMapper.toEntity(dto);
        repository.save(usuario);
    }
}
```

***

## ⚠️ Anti-Patterns (Evitar)

### ❌ 1. Não Retornar Objeto (`void`)

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler({JapeSessionInterruptedError.class})
    public void handleError(JapeSessionInterruptedError e) { // ❌ ERRO: não pode retornar void
        // Isso causará erro de compilação
    }
}
```

**✅ Correto:**

```java
@ExceptionHandler({JapeSessionInterruptedError.class})
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    return new ErrorResponse("ERROR", e.getMessage());
}
```

### ❌ 2. Esquecer de Logar a Exceção

```java
@ExceptionHandler({JapeSessionInterruptedError.class})
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    // ❌ Nenhum log! Impossível diagnosticar problemas.
    return new ErrorResponse("ERROR", "Erro");
}
```

**✅ Correto:**

```java
@ExceptionHandler({JapeSessionInterruptedError.class})
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    logger.log(Level.SEVERE, "Erro capturado", e);
    return new ErrorResponse("ERROR", "Erro");
}
```

### ❌ 3. Expor Stack Traces ao Usuário

```java
@ExceptionHandler({JapeSessionInterruptedError.class})
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    // ❌ Stack trace exposto ao cliente
    return new ErrorResponse("ERROR", e.toString() + "\n" + Arrays.toString(e.getStackTrace()));
}
```

**✅ Correto:**

```java
@ExceptionHandler({JapeSessionInterruptedError.class})
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    logger.log(Level.SEVERE, "Erro capturado", e);
    return new ErrorResponse("ERROR", "Erro interno. Contate o suporte.");
}
```

### ❌ 4. Usar `@ExceptionHandler` sem Especificar Exceções

```java
@ExceptionHandler({}) // ❌ Array vazio
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    return new ErrorResponse("ERROR", "Erro");
}
```

**✅ Correto:**

```java
@ExceptionHandler({JapeSessionInterruptedError.class})
public ErrorResponse handleError(JapeSessionInterruptedError e) {
    return new ErrorResponse("ERROR", "Erro");
}
```

### ❌ 5. Duplicar Assinaturas de Handlers

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler({IOException.class})
    public ErrorResponse handleIO1(IOException e) {
        return new ErrorResponse("IO_ERROR", "Erro de I/O");
    }

    @ExceptionHandler({IOException.class}) // ❌ ERRO: IOException já está mapeada
    public ErrorResponse handleIO2(IOException e) {
        return new ErrorResponse("IO_ERROR_2", "Outro erro de I/O");
    }
}
```

**✅ Correto:** Uma exceção deve ser tratada por apenas um handler.

### ❌ 6. Métodos sem `@ExceptionHandler`

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    // ❌ Sem @ExceptionHandler - será ignorado
    public ErrorResponse handleError(JapeSessionInterruptedError e) {
        return new ErrorResponse("ERROR", "Erro");
    }
}
```

**✅ Correto:**

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler({JapeSessionInterruptedError.class})
    public ErrorResponse handleError(JapeSessionInterruptedError e) {
        return new ErrorResponse("ERROR", "Erro");
    }
}
```

***

## ⚠️ Atenção sobre Ordenação de Handlers e uso de Handler com Exception

<Callout icon="❗" theme="error">
  ### **Importante:**
</Callout>

> **Não existe garantia de ordenação ou prioridade entre métodos&#x20;**`@ExceptionHandler`**&#x20;de classes diferentes que tratam a mesma exceção.**
>
> * Se múltiplas classes possuem handlers para a mesma exceção, **não há controle sobre qual será executado**.
> * Para garantir previsibilidade, **evite duplicidade de handlers para a mesma exceção**
>
> **NÃO utilize a classe Exception como tratador genérico**.
>
> * O uso de `@ExceptionHandler({Exception.class})` **NÃO É RECOMENDADO**: esse handler pode capturar exceções filhas e também exceções não mapeadas, impedindo que handlers mais específicos sejam chamados, numa mesma classe ou em classes diferentes.
> * Caso existam handlers para a classe pai Exception, o framework pode escolher qualquer um deles sem ordem definida, podendo afetar o tratamento esperado.

***

**Exemplo a evitar:**

```java
@ExceptionHandler({Exception.class}) // ❌ NÃO RECOMENDADO
public ErrorResponse handleAll(Exception e) {
    // Este método irá capturar todas as exceções, inclusive as filhas
    return new ErrorResponse("GENERIC_ERROR", "Ocorreu um erro inesperado.");
}
```

**Exemplo recomendado:**

```java
@ExceptionHandler({ObjectNotFoundException.class, ValidationException.class})
public ErrorResponse handleSpecific(Exception e) {
    // Trate cada exceção de forma adequada
    // ...
}
```

***

## 🎯 Resumo

* ✅ Use `@ControllerAdvice` para **centralizar** todo o tratamento de exceções.
* ✅ Anote métodos com `@ExceptionHandler` para definir **quais exceções** cada método trata.
* ✅ **Sempre retorne um objeto** (nunca `void`) que será serializado para JSON.
* ❌ **Evite** expor stack traces ou dados sensíveis nas respostas.
* ❌ **Evite** duplicar handlers para a mesma exceção em classes diferentes.
* ❌ **Evite** métodos sem `@ExceptionHandler` em classes `@ControllerAdvice`.
* ❌ **Evite** utilizar `@ExceptionHandler({Exception.class})` para capturar todas as exceções.

***

## 📚 Referências

* [Camada de Serviço (`@Service`)](03_service.md)
* [Bean Validation](05_bean_validation.md)
* [Injeção de Dependências](06_dependency_injection.md)
* [Controle Transacional (`@Transactional`)](07_transactional.md)
