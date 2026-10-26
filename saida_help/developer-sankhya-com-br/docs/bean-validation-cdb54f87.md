---
id: "https://developer.sankhya.com.br/docs/bean-validation"
titulo: "🛡️ Validação de Dados com Bean Validation"
url: "https://developer.sankhya.com.br/docs/bean-validation"
atualizado_em: "2026-09-08T19:12:38.000Z"
---

# 🛡️ Validação de Dados com Bean Validation

O **Bean Validation** é um mecanismo que permite definir e validar regras de negócio diretamente nos seus objetos de dados (DTOs e Entidades) usando anotações. O SDK Sankhya integra este padrão (especificação **JSR 303/380**), oferecendo validação automática e declarativa.

## 🤔 Por que usar Bean Validation?

* ✅ **Validação Automática:** Detecte dados inválidos antes que eles cheguem à sua lógica de negócio.
* ✅ **Código Declarativo:** As regras de validação ficam junto aos campos que elas validam, tornando o código mais legível.
* ✅ **Mensagens de Erro Claras:** Forneça feedback específico e customizável para o usuário final.
* ✅ **Padrão de Mercado:** Amplamente utilizado no ecossistema Java, o que facilita a adoção.
* ✅ **Menos Código Boilerplate:** Elimina a necessidade de `if/else` manuais para validações.

***

## 🚀 Como Funciona?

O Bean Validation é ativado com a anotação `@Valid`. Quando um método de um `@Service` recebe um parâmetro anotado com `@Valid`, o SDK intercepta a chamada e executa todas as anotações de validação definidas no objeto.

Se qualquer validação falhar, o SDK lança uma exceção automaticamente, impedindo a execução do método e retornando uma resposta de erro clara.

**Exemplo de Ativação:**

```java
@Service(name = "UsuarioServiceSP")
public class UsuarioService {
    // ...

    @Transactional
    public void cadastrarUsuario(@Valid UsuarioDTO usuario) {
        // O código dentro deste método só será executado
        // se o objeto 'usuario' passar em todas as validações.
        businessService.salvar(usuario);
    }
}
```

***

## Anotações básicas de validação

### 1. Validações de Nulidade e Conteúdo

#### `@NotNull`

Garante que o valor do campo não seja `null`.

```java
@NotNull(message = "O ID do usuário é obrigatório.")
private Long id;
```

#### `@NotBlank`

Para `String`s. Garante que a string não seja `null`, vazia (`""`) ou contenha apenas espaços em branco.

```java
@NotBlank(message = "O nome do usuário é obrigatório.")
private String nome;
```

#### `@NotEmpty`

Para coleções, mapas ou arrays. Garante que não sejam `null` e que tenham pelo menos um elemento.

```java
@NotEmpty(message = "O pedido deve ter pelo menos um item.")
private List<ItemDTO> itens;
```

### 2. Validações de Tamanho

#### `@Size`

Verifica se o tamanho de uma `String`, coleção, mapa ou array está dentro de um intervalo.

```java
@Size(min = 3, max = 50, message = "O nome deve ter entre 3 e 50 caracteres.")
private String nome;

@Size(max = 5, message = "Um produto pode ter no máximo 5 tags.")
private List<String> tags;
```

### 3. Validações Numéricas

#### `@Min` e `@Max`

Garante que um valor numérico seja maior ou igual (`@Min`) ou menor ou igual (`@Max`) a um limite.

```java
@Min(value = 1, message = "A quantidade mínima é 1.")
private int quantidade;

@Max(value = 99, message = "O desconto máximo é 99%.")
private double desconto;
```

#### `@Positive` e `@PositiveOrZero`

Garante que um número seja estritamente positivo (`> 0`) ou positivo ou zero (`>= 0`).

```java
@Positive(message = "O valor do produto deve ser positivo.")
private BigDecimal preco;
```

#### `@Negative` e `@NegativeOrZero`

Garante que um número seja estritamente negativo (`< 0`) ou negativo ou zero (`<= 0`).

### 4. Validações de Formato

#### `@Email`

Verifica se uma `String` tem um formato de e-mail válido.

```java
@Email(message = "Formato de e-mail inválido.")
private String email;
```

#### `@Pattern`

Valida uma `String` contra uma expressão regular (RegEx).

```java
@Pattern(regexp = "[A-Z]{2}[0-9]{4}", message = "A placa deve seguir o formato AA1234.")
private String placa;
```

### 5. Validações de Data e Hora

#### `@Future` e `@FutureOrPresent`

Garante que uma data esteja no futuro ou no futuro/presente.

```java
@Future(message = "A data de entrega deve ser no futuro.")
private LocalDate dataEntrega;
```

#### `@Past` e `@PastOrPresent`

Garante que uma data esteja no passado ou no passado/presente.

```java
@PastOrPresent(message = "A data de nascimento não pode ser no futuro.")
private LocalDate dataNascimento;
```

***

## Validação aninhada (`@Valid`)

Para validar objetos dentro de outros objetos (ex: uma lista de itens dentro de um pedido), use a anotação `@Valid` no campo do objeto aninhado.

```java
// DTO do Pedido
public class PedidoDTO {
    @NotNull
    private Long idCliente;

    @Valid // Ativa a validação para cada ItemDTO na lista
    @NotEmpty
    private List<ItemDTO> itens;
}

// DTO do Item
public class ItemDTO {
    @NotNull
    private Long idProduto;

    @Positive(message = "A quantidade deve ser positiva.")
    private int quantidade;
}
```

Neste exemplo, ao validar um `PedidoDTO`, o SDK irá percorrer a lista de `itens` e aplicar as validações (`@NotNull` e `@Positive`) em cada `ItemDTO`.

## ✨ Boas Práticas

* **Use em DTOs:** A validação deve ocorrer na camada de entrada de dados. Portanto, aplique as anotações principalmente nos seus **Data Transfer Objects (DTOs)**.
* **Mensagens Claras:** Sempre forneça uma `message` clara e útil para o usuário final.
* **Validações Customizadas:** Para regras de negócio complexas, você pode criar suas próprias anotações de validação.
* **Combine Anotações:** É comum e recomendado usar múltiplas anotações em um mesmo campo (ex: `@NotNull` e `@Size`).

### 2. Validações de Tamanho

#### `@Size`

Define tamanho mínimo e/ou máximo para Strings, Collections, Arrays e Maps.

```java
@Data
public class UsuarioDTO {
    @Size(min = 2, max = 50, message = "Nome deve ter entre 2 e 50 caracteres")
    private String nome;
    
    @Size(min = 8, message = "Senha deve ter pelo menos 8 caracteres")
    private String senha;
    
    @Size(max = 5, message = "Máximo 5 endereços permitidos")
    private List<EnderecoDTO> enderecos;
}
```

#### `@Length` (Hibernate Validator)

Similar ao `@Size`, mas específico para Strings.

```java
@Data
public class ProdutoDTO {
    @Length(min = 10, max = 500, message = "Descrição deve ter entre 10 e 500 caracteres")
    private String descricao;
}
```

### 3. Validações Numéricas

#### `@Min` e `@Max`

Definem valores mínimos e máximos para números.

```java
@Data
public class ProdutoDTO {
    @Min(value = 0, message = "Preço não pode ser negativo")
    private BigDecimal preco;
    
    @Max(value = 100, message = "Desconto máximo é 100%")
    private Integer percentualDesconto;
    
    @Min(value = 1, message = "Quantidade mínima é 1")
    @Max(value = 9999, message = "Quantidade máxima é 9999")
    private Integer quantidade;
}
```

#### `@DecimalMin` e `@DecimalMax`

Validação de valores decimais com maior precisão.

```java
@Data
public class FinanceiroDTO {
    @DecimalMin(value = "0.01", message = "Valor mínimo é 0.01")
    private BigDecimal valor;
    
    @DecimalMax(value = "999999.99", inclusive = false, 
                message = "Valor deve ser menor que 999999.99")
    private BigDecimal limite;
}
```

#### `@Positive`, `@PositiveOrZero`, `@Negative`, `@NegativeOrZero`

Validações para números positivos, negativos ou zero.

```java
@Data
public class MovimentacaoDTO {
    @Positive(message = "ID deve ser positivo")
    private Long id;
    
    @PositiveOrZero(message = "Saldo não pode ser negativo")
    private BigDecimal saldo;
    
    @NegativeOrZero(message = "Débito deve ser negativo ou zero")
    private BigDecimal debito;
}
```

#### `@Digits`

Valida o número de dígitos inteiros e fracionários.

```java
@Data
public class MonetarioDTO {
    @Digits(integer = 10, fraction = 2, message = "Formato: máximo 10 dígitos inteiros e 2 decimais")
    private BigDecimal valor;
}
```

### 4. Validações de Data e Tempo

#### `@Past`, `@PastOrPresent`

Validam datas no passado.

```java
@Data
public class PessoaDTO {
    @Past(message = "Data de nascimento deve estar no passado")
    private LocalDate dataNascimento;
    
    @PastOrPresent(message = "Data de cadastro deve ser hoje ou no passado")
    private LocalDateTime dataCadastro;
}
```

#### `@Future`, `@FutureOrPresent`

Validam datas no futuro.

```java
@Data
public class EventoDTO {
    @Future(message = "Data do evento deve estar no futuro")
    private LocalDateTime dataEvento;
    
    @FutureOrPresent(message = "Data de entrega deve ser hoje ou no futuro")
    private LocalDate dataEntrega;
}
```

### 5. Validações de Formato

#### `@Pattern`

Valida contra uma expressão regular.

```java
@Data
public class ContatoDTO {
    @Pattern(regexp = "^[A-Za-z0-9+_.-]+@(.+)$", 
             message = "Formato de email inválido")
    private String email;
    
    @Pattern(regexp = "\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}", 
             message = "CPF deve seguir o formato: 000.000.000-00")
    private String cpf;
    
    @Pattern(regexp = "\\(\\d{2}\\)\\s\\d{4,5}-\\d{4}", 
             message = "Telefone deve seguir o formato: (11) 99999-9999")
    private String telefone;
}
```

#### `@Email`

Validação específica para endereços de email.

```java
@Data
public class UsuarioDTO {
    @Email(message = "Email deve ter um formato válido")
    @NotBlank(message = "Email é obrigatório")
    private String email;
}
```

### 6. Validações Booleanas

#### `@AssertTrue` e `@AssertFalse`

Validam valores booleanos específicos.

```java
@Data
public class TermosDTO {
    @AssertTrue(message = "Deve aceitar os termos de uso")
    private Boolean aceitaTermos;
    
    @AssertFalse(message = "Não deve estar suspenso")
    private Boolean suspenso;
}
```

***

## Tratamento de Erros de Validação

Quando uma validação falha, o sistema lança uma exceção contendo detalhes sobre todos os erros encontrados:

```java
@Service(serviceName = "ProdutoServiceSP")
public class ProdutoController {
    
    @Transactional
    public void cadastrarProduto(@Valid ProdutoDTO produto) {
        try {
            produtoService.salvar(produto);
        } catch (ConstraintViolationException e) {
            // A exceção contém todos os erros de validação
            e.getConstraintViolations().forEach(violation -> {
                String campo = violation.getPropertyPath().toString();
                String mensagem = violation.getMessage();
                Object valorInvalido = violation.getInvalidValue();
                
                System.err.printf("Erro no campo '%s': %s (valor: %s)%n", 
                                campo, mensagem, valorInvalido);
            });
            
            // Re-lançar ou tratar conforme necessário
            throw e;
        }
    }
}
```

***

## Exemplo Completo: Sistema de E-commerce

```java
// DTO principal com validações completas
@Data
public class PedidoCompletoDTO {
    
    @NotBlank(message = "Número do pedido é obrigatório")
    @Pattern(regexp = "PED\\d{6}", message = "Número deve seguir o padrão: PED000000")
    private String numeroPedido;
    
    @Valid
    @NotNull(message = "Dados do cliente são obrigatórios")
    private ClienteDTO cliente;
    
    @Valid
    @NotEmpty(message = "Pedido deve conter pelo menos um item")
    @Size(max = 50, message = "Máximo 50 itens por pedido")
    private List<ItemPedidoDTO> itens;
    
    @Valid
    @NotNull(message = "Dados de entrega são obrigatórios")
    private EnderecoEntregaDTO enderecoEntrega;
    
    @FutureOrPresent(message = "Data de entrega deve ser hoje ou no futuro")
    private LocalDate dataEntregaPrevista;
    
    @DecimalMin(value = "0.00", message = "Valor total não pode ser negativo")
    @Digits(integer = 8, fraction = 2, message = "Valor total deve ter no máximo 8 dígitos inteiros e 2 decimais")
    private BigDecimal valorTotal;
    
    @AssertTrue(message = "Deve aceitar os termos e condições")
    private Boolean aceitaTermos;
}

@Data
public class ClienteDTO {
    @NotBlank(message = "Nome é obrigatório")
    @Size(min = 2, max = 100, message = "Nome deve ter entre 2 e 100 caracteres")
    private String nome;
    
    @Email(message = "Email deve ter formato válido")
    @NotBlank(message = "Email é obrigatório")
    private String email;
    
    @ValidCPF(message = "CPF inválido")
    @NotBlank(message = "CPF é obrigatório")
    private String cpf;
    
    @Pattern(regexp = "\\(\\d{2}\\)\\s\\d{4,5}-\\d{4}", 
             message = "Telefone deve seguir o formato: (11) 99999-9999")
    private String telefone;
}

@Data
public class ItemPedidoDTO {
    @NotBlank(message = "Código do produto é obrigatório")
    @Pattern(regexp = "PROD\\d{4}", message = "Código deve seguir o padrão: PROD0000")
    private String codigoProduto;
    
    @NotBlank(message = "Nome do produto é obrigatório")
    @Size(max = 200, message = "Nome do produto deve ter no máximo 200 caracteres")
    private String nomeProduto;
    
    @Positive(message = "Quantidade deve ser positiva")
    @Max(value = 999, message = "Quantidade máxima por item é 999")
    private Integer quantidade;
    
    @DecimalMin(value = "0.01", message = "Preço unitário deve ser maior que zero")
    @Digits(integer = 6, fraction = 2, message = "Preço deve ter no máximo 6 dígitos inteiros e 2 decimais")
    private BigDecimal precoUnitario;
    
    @DecimalMin(value = "0.00", message = "Subtotal não pode ser negativo")
    private BigDecimal subtotal;
}

@Data
public class EnderecoEntregaDTO {
    @NotBlank(message = "CEP é obrigatório")
    @Pattern(regexp = "\\d{5}-?\\d{3}", message = "CEP deve ter o formato: 00000-000")
    private String cep;
    
    @NotBlank(message = "Logradouro é obrigatório")
    @Size(max = 200, message = "Logradouro deve ter no máximo 200 caracteres")
    private String logradouro;
    
    @NotBlank(message = "Número é obrigatório")
    @Size(max = 20, message = "Número deve ter no máximo 20 caracteres")
    private String numero;
    
    @Size(max = 100, message = "Complemento deve ter no máximo 100 caracteres")
    private String complemento;
    
    @NotBlank(message = "Bairro é obrigatório")
    @Size(max = 100, message = "Bairro deve ter no máximo 100 caracteres")
    private String bairro;
    
    @NotBlank(message = "Cidade é obrigatória")
    @Size(max = 100, message = "Cidade deve ter no máximo 100 caracteres")
    private String cidade;
    
    @NotBlank(message = "UF é obrigatória")
    @Pattern(regexp = "[A-Z]{2}", message = "UF deve ter 2 letras maiúsculas")
    private String uf;
}

// Controller com validação automática
@Service(serviceName = "EcommerceServiceSP")
public class EcommerceController {
    
    private final PedidoService pedidoService;
    
    @Inject
    public EcommerceController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }
    
    @Transactional
    public String criarPedido(@Valid PedidoCompletoDTO pedido) {
        // Todas as validações são executadas automaticamente
        // antes de este método ser executado
        
        return pedidoService.processar(pedido);
    }
}
```

***

## Melhores Práticas

### 1. Combine Múltiplas Validações

```java
@NotBlank(message = "Email é obrigatório")
@Email(message = "Email deve ter formato válido")
@Size(max = 100, message = "Email deve ter no máximo 100 caracteres")
private String email;
```

### 2. Use Mensagens Descritivas

```java
@Min(value = 18, message = "Idade mínima para cadastro é 18 anos")
private Integer idade;
```

### 3. Valide Objetos Aninhados

```java
@Valid
@NotNull(message = "Endereço é obrigatório")
private EnderecoDTO endereco;
```

### 4. Organize por Grupos quando Necessário

```java
@NotNull(groups = UpdateGroup.class)
@Null(groups = CreateGroup.class)
private Long id;
```

O Bean Validation no SDK Sankhya oferece uma solução robusta e padronizada para validação de dados, garantindo a integridade das informações desde o ponto de entrada até a persistência, com feedback claro e automatizado para desenvolvedores e usuários finais.
