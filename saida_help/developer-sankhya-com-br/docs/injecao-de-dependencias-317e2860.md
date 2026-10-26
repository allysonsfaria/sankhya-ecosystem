---
id: "https://developer.sankhya.com.br/docs/injecao-de-dependencias"
titulo: "🔧 Injeção de Dependências (DI)"
url: "https://developer.sankhya.com.br/docs/injecao-de-dependencias"
atualizado_em: "2026-09-08T19:13:16.000Z"
---

# 🔧 Injeção de Dependências (DI)

# 🔧 Injeção de Dependências (DI)

A **Injeção de Dependências (DI)** é um dos pilares do SDK Sankhya. É um padrão de projeto que inverte o controle sobre a criação de objetos: em vez de uma classe criar suas próprias dependências, elas são "injetadas" de fora por um contêiner.

No SDK, isso significa que você **nunca mais precisará usar**`new` para instanciar seus serviços, repositórios ou outros componentes.

## 🤔 Por que usar Injeção de Dependências?

* ✅ **Código Desacoplado:** As classes não sabem como criar suas dependências, apenas como usá-las. Isso torna o sistema mais flexível e fácil de manter.
* ✅ **Testabilidade Superior:** A DI, especialmente via construtor, é a chave para testes unitários eficazes. Você pode facilmente "injetar" versões falsas (*mocks*) das dependências para testar uma classe de forma isolada.
* ✅ **Gerenciamento de Ciclo de Vida:** O SDK gerencia o ciclo de vida dos seus objetos (criação, reutilização como singletons, etc.), garantindo eficiência e segurança em ambientes multi-thread.
* ✅ **Configuração Centralizada:** A configuração das dependências é feita através de anotações, tornando o código mais limpo e declarativo.

***

## 📊 Abordagem Antiga vs. Nova

### ❌ Abordagem Tradicional (Criação Manual)

No modelo antigo, cada serviço era responsável por criar suas próprias dependências. Isso gerava um código fortemente acoplado, repetitivo e muito difícil de testar.

```java
// Código legado: acoplado, repetitivo e difícil de testar
/**
 * @ejb.bean name="PedidoServiceSP"
 * jndi-name="mge/placemm/ejb/session/PedidoServiceSP"
 * type="Stateless" transaction-type="Container" view-type="remote"
 * @ejb.transaction type="Supports"
 * @ejb.util generate="false"
 */
public class PedidoServiceSP extends ServiceBean {
    public void processarPedido(ServiceContext ctx) throws Exception {
        // Criação manual de dependências
        PedidoValidator validator = new PedidoValidator();
        CalculadoraTaxas calculadora = new CalculadoraTaxas();
        EstoqueService estoque = new EstoqueService();
        // ... e assim por diante

        // Se a CalculadoraTaxas mudar seu construtor, este código quebra.
        // Como testar PedidoServiceSP sem testar todas as suas dependências junto?
        // ...
    }
}
```

### ✅ Nova Abordagem com Injeção de Dependências

Com o SDK, você simplesmente declara as dependências no construtor da sua classe, e o contêiner de DI do SDK se encarrega de fornecê-las.

```java
@Service(name = "PedidoServiceSP")
public class PedidoService {

    private final PedidoBusinessService businessService;

    @Inject // O SDK injeta a dependência aqui
    public PedidoService(PedidoBusinessService businessService) {
        this.businessService = businessService;
    }

    @Transactional
    public void processarPedido(@Valid PedidoDTO pedido) {
        // A responsabilidade é delegada para a camada de negócio
        businessService.processar(pedido);
    }
}

@Component // Componente de negócio
public class PedidoBusinessService {

    private final PedidoValidator validator;
    private final CalculadoraTaxas calculadora;
    private final EstoqueService estoque;

    @Inject // O SDK injeta TODAS as dependências necessárias
    public PedidoBusinessService(PedidoValidator validator,
                                 CalculadoraTaxas calculadora,
                                 EstoqueService estoque) {
        this.validator = validator;
        this.calculadora = calculadora;
        this.estoque = estoque;
    }

    public void processar(PedidoDTO pedido) {
        // Código limpo, focado e 100% testável
        validator.validar(pedido);
        BigDecimal taxa = calculadora.calcular(pedido.getValor());
        // ...
    }
}
```

***

## ⚙️ Como Funciona: Estereótipos e Injeção

O sistema de DI do SDK é baseado em **estereótipos** (anotações que classificam o papel de uma classe) e na anotação `@Inject`.

<Callout icon="⚠️" theme="warn">
  ### Deve ser utilizado com.google.inject.Inject e NÃO javax.inject.Inject
</Callout>

### 1. Estereótipos: As Anotações que Tornam as Classes Gerenciáveis

Para que uma classe possa ser injetada, ela precisa ser "marcada" com uma das seguintes anotações de estereótipo:

| Anotação      | Propósito                                                                                                                  | Ciclo de Vida |
| :------------ | :------------------------------------------------------------------------------------------------------------------------- | :------------ |
| `@Service`    | Define um ponto de entrada (endpoint) para requisições externas.                                                           | Prototype     |
| `@Job`        | Define uma tarefa agendada.                                                                                                | Prototype     |
| `@Repository` | Define uma interface de acesso a dados (camada de persistência).                                                           | Prototype     |
| `@Component`  | **Anotação genérica** para qualquer outra classe gerenciada pelo SDK, como serviços de negócio, validadores, helpers, etc. | Prototype     |

<Callout icon="💡" theme="default">
  ### **O que é um Singleton?**

  Significa que o SDK cria **apenas uma instância** daquela classe para toda a aplicação. Essa mesma instância é reutilizada em todos os lugares onde for injetada. Isso é eficiente e seguro para classes que não guardam estado.
</Callout>

<Callout icon="💡" theme="default">
  ### **O que é um Prototype?**

  Significa que o SDK cria **uma instância** daquela classe toda vez que ela é injetada.
</Callout>

### 2. `@Inject`: Solicitando uma Dependência

<Callout icon="⚠️" theme="warn">
  ### **Importante:** Utilize a anotação `com.google.inject.Inject`, e **não** `javax.inject.Inject`.
</Callout>

A anotação `@Inject` é usada no **construtor** de uma classe para informar ao SDK quais dependências devem ser fornecidas.

**Regras:**

* Deve haver **apenas um construtor** anotado com `@Inject`.
* Todos os parâmetros do construtor devem ser de tipos que o SDK saiba como criar (ou seja, classes anotadas com um dos estereótipos `@Component` ou `@Repository`).

Se o SDK não conseguir encontrar uma dependência ou se houver um ciclo (ex: `A` depende de `B` e `B` depende de `A`), a aplicação falhará na inicialização com um erro claro, o que é ótimo para detectar problemas de arquitetura rapidamente (*fail-fast*).

## ✨ Boas Práticas

* **Injeção via Construtor:** Sempre prefira a injeção via construtor. Ela torna as dependências explícitas e garante que o objeto seja criado em um estado válido.
* **Use Interfaces:** Programe para interfaces, não para implementações. Em vez de injetar `MeuServicoImpl`, injete a interface `MeuServico` e anote a implementação com o estereótipo. Isso facilita a troca de implementações e os testes.
* **Princípio da Responsabilidade Única (SRP):** Crie classes pequenas e focadas. Se um serviço tem muitas dependências, pode ser um sinal de que ele está fazendo coisas demais e deve ser quebrado em componentes menores.
* **Evite Ciclos de Dependência:** Um ciclo de dependência é um forte indicador de um problema de design na sua aplicação.

### 🎯 **Principais Diferenças**

| Aspecto                | Abordagem Antiga        | SDK Sankhya                  |
| ---------------------- | ----------------------- | ---------------------------- |
| **Criação de Objetos** | ❌ `new` manual          | ✅ `@Inject` automático       |
| **Testabilidade**      | ❌ Dependências fixas    | ✅ Mocks via construtor       |
| **Manutenibilidade**   | ❌ Código espalhado      | ✅ Dependências centralizadas |
| **Detecção de Erros**  | ❌ Runtime               | ✅ Startup (fail-fast)        |
| **Reutilização**       | ❌ Instâncias múltiplas  | ✅ Singletons compartilhados  |
| **Configuração**       | ❌ Manual em cada classe | ✅ Automática via anotações   |

***

Em termos práticos, a adoção da DI resulta em:

* **Menos código repetitivo:** O desenvolvedor foca na lógica de negócio, não na criação e gerenciamento de instâncias.
* **Gerenciamento automático:** O framework controla o ciclo de vida dos objetos (criação, reutilização e destruição).
* **Código mais organizado:** Promove um baixo acoplamento entre as classes e uma clara separação de responsabilidades.
* **Testabilidade superior:** Facilita a criação de mocks e testes unitários isolados.

***

## Anotações de Configuração

O SDK Sankhya utiliza anotações para marcar classes e definir como o framework deve gerenciá-las. Esta abordagem é similar aos padrões modernos de injeção de dependência.

### `@Component`

Marca uma classe como um **componente** genérico gerenciado pelo framework. É o bloco de construção fundamental para lógica de negócio, utilitários, serviços internos e processadores de dados.

**Características:**

* Escopo **Singleton** por padrão
* Instanciação **lazy** (criada quando necessária)
* Disponível para injeção em outras classes

```java
@Component
public class PedidoProcessor {
    
    // Construtor protegido ou público é necessário para o framework
    protected PedidoProcessor() {
    }

    public void processar(Long pedidoId) {
        System.out.println("Processando pedido ID: " + pedidoId);
        // Lógica de processamento do pedido
    }
    
    public boolean validar(PedidoDTO pedido) {
        return pedido != null && pedido.getValor() != null;
    }
}
```

### 2. `@Service` - Pontos de Entrada (Controllers)

No SDK Sankhya, `@Service` é equivalente a um **Controller** do Spring. Representa pontos de entrada externos do Add-on, expondo funcionalidades através de URLs específicas.

**Características:**

* **Ponto de entrada** para requisições externas
* Requer `serviceName` para definir a URL de acesso
* Geralmente delega para `@Component` para lógica de negócio
* **Não recomendado** para lógica complexa interna

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoController {
    
    private final PedidoProcessor pedidoProcessor;
    private final PedidoRepository pedidoRepository;
    
    @Inject
    public PedidoController(PedidoProcessor pedidoProcessor, 
                           PedidoRepository pedidoRepository) {
        this.pedidoProcessor = pedidoProcessor;
        this.pedidoRepository = pedidoRepository;
    }

    // Método público acessível via URL
    public String criarPedido(PedidoDTO pedido) {
        // Delega para o componente de negócio
        pedidoProcessor.processar(pedido.getId());
        return "Pedido criado com sucesso";
    }
}
```

**URL de Acesso:** `<servidor>/<addon>/service.sbr?serviceName=PedidoServiceSP.criarPedido`

### 3. `@Inject` - Injeção via Construtor

A anotação `@Inject` do Guice realiza a injeção de dependências através do construtor. Esta é a forma **recomendada** SDK Sankhya.

**Vantagens da Injeção via Construtor:**

* **Dependências explícitas** e obrigatórias
* **Imutabilidade** (campos `final`)
* **Testabilidade** superior
* **Fail-fast** (falha na criação se dependências não disponíveis)

```java
@Component
public class NotificacaoService {
    
    private final EmailService emailService;
    private final LogService logService;
    
    @Inject
    public NotificacaoService(EmailService emailService, LogService logService) {
        this.emailService = emailService;
        this.logService = logService;
    }
    
    public void notificarPedido(String destinatario, String numeroPedido) {
        try {
            emailService.enviar(destinatario, "Pedido " + numeroPedido + " criado");
            logService.registrar("Email enviado para " + destinatario);
        } catch (Exception e) {
            logService.registrarErro("Falha ao enviar email", e);
        }
    }
}
```

## Lidando com Múltiplas Implementações

Um cenário comum em aplicações complexas é a necessidade de ter várias implementações para a mesma interface. O SDK Sankhya, utilizando o poder do Guice, oferece duas estratégias principais para gerenciar isso: `bindWith` (qualificadores type-safe) e `name` (strings nomeadas).

### 1. Usando `bindWith` com Anotações Qualificadoras (Recomendado)

A abordagem mais robusta e segura é usar anotações qualificadoras personalizadas. Isso garante a verificação em tempo de compilação e melhora a legibilidade do código.

**Passo 1: Crie uma Anotação Qualificadora**

A anotação precisa ter `@Retention(RetentionPolicy.RUNTIME)` e, opcionalmente, `@Qualifier` do JSR-330.

```java
package br.com.fabricante.addon.qualifiers;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import javax.inject.Qualifier;

@Qualifier
@Retention(RetentionPolicy.RUNTIME)
public @interface Primary {
}
```

**Passo 2: Anote a Implementação com**`@Component`**&#x20;e**`bindWith`

Associe a implementação à sua anotação qualificadora.

```java
public interface NotificationService {
    void send(String message);
}

// Implementação primária
@Component(bindWith = Primary.class)
public class EmailNotificationService implements NotificationService {
    @Override
    public void send(String message) {
        // Envia notificação por e-mail
    }
}

// Implementação secundária (padrão)
@Component
public class SmsNotificationService implements NotificationService {
    @Override
    public void send(String message) {
        // Envia notificação por SMS
    }
}
```

**Passo 3: Injete a Implementação Específica**

Use a anotação qualificadora no ponto de injeção para escolher qual implementação você deseja.

```java
@Component
public class OrderProcessor {

    private final NotificationService primaryNotifier;
    private final NotificationService defaultNotifier;

    @Inject
    public OrderProcessor(@Primary NotificationService primaryNotifier,
                          NotificationService defaultNotifier) {
        this.primaryNotifier = primaryNotifier; // Receberá EmailNotificationService
        this.defaultNotifier = defaultNotifier; // Receberá SmsNotificationService
    }

    public void process() {
        primaryNotifier.send("Pedido processado!");
        defaultNotifier.send("Alerta de processamento de pedido.");
    }
}
```

**Vantagens do**`bindWith`**:**

* ✅ **Type-safe:** Erros são detectados em tempo de compilação.
* ✅ **Refatoração segura:** Renomear a anotação atualiza todas as suas usos.
* ✅ **Clareza:** A intenção do código é explícita.

### 2. Usando `name` com Strings

Para casos mais simples ou quando a flexibilidade de strings é desejada, você pode usar o atributo `name`.

**Passo 1: Anote a Implementação com**`@Component`**&#x20;e**`name`

```java
public interface PaymentGateway {
    void processPayment(BigDecimal amount);
}

@Component(name = "creditCard")
public class CreditCardGateway implements PaymentGateway {
    // ...
}

@Component(name = "paypal")
public class PayPalGateway implements PaymentGateway {
    // ...
}
```

**Passo 2: Injete usando**`@Named`

Use a anotação `@Named` do Guice (`com.google.inject.name.Named`) para especificar a implementação.

```java
import com.google.inject.name.Named;

@Component
public class CheckoutService {

    private final PaymentGateway creditCardProcessor;
    private final PaymentGateway paypalProcessor;

    @Inject
    public CheckoutService(@Named("creditCard") PaymentGateway creditCardProcessor,
                           @Named("paypal") PaymentGateway paypalProcessor) {
        this.creditCardProcessor = creditCardProcessor;
        this.paypalProcessor = paypalProcessor;
    }
}
```

**Desvantagens do**`name`**:**

* ❌ **Não é type-safe:** Erros de digitação no nome só são detectados em tempo de execução.
* ❌ **Refatoração manual:** Se o nome mudar, você precisa encontrar e substituir todas as ocorrências da string.

### Comparativo: `bindWith` vs. `name`

| Característica        | `@Component(bindWith = Primary.class)` | `@Component(name = "primary")`        |
| --------------------- | -------------------------------------- | ------------------------------------- |
| **Segurança de Tipo** | ✅ Alta (Compile-time)                  | ❌ Baixa (Runtime)                     |
| **Refatoração**       | ✅ Segura e automatizada (IDE)          | ❌ Manual e propensa a erros           |
| **Clareza**           | ✅ Alta (usa tipos Java)                | ⚠️ Média (depende de "magic strings") |
| **Uso Recomendado**   | **Padrão** para DI qualificada         | Casos simples ou legados              |

### 3. Injetando Todas as Implementações com `Multibinder`

E se você precisar de **todas** as implementações de uma interface? Por exemplo, para notificar um evento em múltiplos canais. O SDK suporta isso automaticamente através do `Multibinder` do Guice.

**Passo 1: Defina as Implementações**

Crie suas implementações normalmente com `@Component`. Você pode até combinar com qualificadores.

```java
public interface EventHandler {
    void onEvent(Event event);
}

@Component
public class LoggingEventHandler implements EventHandler {
    // ...
}

@Component
public class AuditingEventHandler implements EventHandler {
    // ...
}

@Component(name = "special")
public class SpecialEventHandler implements EventHandler {
    // ...
}
```

**Passo 2: Injete um**`Set<Interface>`

Para obter todas as implementações, simplesmente injete um `Set` da sua interface. O SDK irá configurar o `Multibinder` por baixo dos panos e fornecer um conjunto com todas as instâncias registradas.

```java
@Component
public class EventDispatcher {

    private final Set<EventHandler> handlers;

    @Inject
    public EventDispatcher(Set<EventHandler> handlers) {
        this.handlers = handlers; // Contém LoggingEventHandler, AuditingEventHandler e SpecialEventHandler
    }

    public void dispatch(Event event) {
        // Itera e chama todos os handlers
        for (EventHandler handler : handlers) {
            handler.onEvent(event);
        }
    }
}
```

Esta abordagem é extremamente poderosa para padrões de design como **Strategy** ou **Observer**, promovendo um código extensível e desacoplado.

## Exemplo Funcional Completo

Vamos criar um sistema completo de processamento de pedidos demonstrando as melhores práticas:

### 1. **Componentes de Domínio**

```java
// Entidade
@Data
@JapeEntity(entity = "Pedido", table = "TGFCAB")
public class Pedido {
    @Id @Column(name = "NUNOTA")
    private Long numero;
    
    @Column(name = "CODPARC")
    private Long codigoCliente;
    
    @Column(name = "VLRNOTA")
    private BigDecimal valor;
}

// DTO com validação
@Data
public class PedidoDTO {
    @NotNull(message = "Código do cliente é obrigatório")
    private Long codigoCliente;
    
    @DecimalMin(value = "0.01", message = "Valor deve ser maior que zero")
    private BigDecimal valor;
    
    @Valid
    @NotEmpty(message = "Deve conter pelo menos um item")
    private List<ItemPedidoDTO> itens;
}
```

### 2. **Camada de Acesso a Dados**

```java
@Repository
public interface PedidoRepository extends JapeRepository<Long, Pedido> {
    
    @Criteria(clause = "CODPARC = :cliente")
    List<Pedido> findByCliente(Long cliente);
    
    @Criteria(clause = "VLRNOTA >= :valorMinimo")
    List<Pedido> findByValorMinimo(BigDecimal valorMinimo);
}
```

### 3. **Componentes de Negócio**

```java
@Component
public class ValidadorPedido {
    
    public void validarRegrasNegocio(PedidoDTO pedido) {
        if (pedido.getValor().compareTo(new BigDecimal("10000")) > 0) {
            throw new BusinessException("Valor não pode exceder R$ 10.000");
        }
    }
}

@Component
public class CalculadoraTaxas {
    
    public BigDecimal calcularTaxaEntrega(Long codigoCliente, BigDecimal valor) {
        // Lógica de cálculo de taxa baseada no cliente e valor
        return valor.multiply(new BigDecimal("0.05")); // 5%
    }
}

@Component
public class EstoqueService {
    
    public void reservarItens(List<ItemPedidoDTO> itens) {
        for (ItemPedidoDTO item : itens) {
            // Lógica de reserva de estoque
            System.out.println("Reservando item: " + item.getCodigoProduto());
        }
    }
}
```

### 4. **Serviço Principal (Orquestração)**

```java
@Component
public class PedidoService {
    
    private final PedidoRepository pedidoRepository;
    private final ValidadorPedido validador;
    private final CalculadoraTaxas calculadora;
    private final EstoqueService estoqueService;
    
    @Inject
    public PedidoService(PedidoRepository pedidoRepository,
                        ValidadorPedido validador,
                        CalculadoraTaxas calculadora,
                        EstoqueService estoqueService) {
        this.pedidoRepository = pedidoRepository;
        this.validador = validador;
        this.calculadora = calculadora;
        this.estoqueService = estoqueService;
    }
    
    @Transactional
    public Long criarPedido(PedidoDTO pedidoDTO) {
        // 1. Validações de negócio
        validador.validarRegrasNegocio(pedidoDTO);
        
        // 2. Reservar estoque
        estoqueService.reservarItens(pedidoDTO.getItens());
        
        // 3. Calcular taxas
        BigDecimal taxa = calculadora.calcularTaxaEntrega(
            pedidoDTO.getCodigoCliente(), 
            pedidoDTO.getValor()
        );
        
        // 4. Criar e salvar pedido
        Pedido pedido = new Pedido();
        pedido.setCodigoCliente(pedidoDTO.getCodigoCliente());
        pedido.setValor(pedidoDTO.getValor().add(taxa));
        
        Pedido salvo = pedidoRepository.save(pedido);
        return salvo.getNumero();
    }
    
    public List<Pedido> buscarPedidosCliente(Long codigoCliente) {
        return pedidoRepository.findByCliente(codigoCliente);
    }
}
```

### 5. **Controller (Ponto de Entrada)**

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoController {
    
    private final PedidoService pedidoService;
    
    @Inject
    public PedidoController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }
    
    public Long criarNovoPedido(@Valid PedidoDTO pedido) {
        return pedidoService.criarPedido(pedido);
    }
    
    public List<Pedido> consultarPedidosCliente(Long codigoCliente) {
        if (codigoCliente == null) {
            throw new IllegalArgumentException("Código do cliente é obrigatório");
        }
        return pedidoService.buscarPedidosCliente(codigoCliente);
    }
}
```

***

## Boas Práticas

### 1. **Separação de Responsabilidades**

```java
// ✅ BOM: @Service apenas como ponto de entrada
@Service(serviceName = "UsuarioServiceSP")
public class UsuarioController {
    
    private final UsuarioService usuarioService;
    
    @Inject
    public UsuarioController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }
    
    public String criarUsuario(@Valid UsuarioDTO usuario) {
        // Apenas delega para o serviço
        return usuarioService.criar(usuario);
    }
}

// ✅ BOM: @Component para lógica de negócio
@Component
public class UsuarioService {
    // Lógica complexa aqui
}
```

### 2. **Injeção via Construtor**

```java
// ✅ BOM: Dependências explícitas e imutáveis
@Component
public class RelatorioService {
    
    private final PedidoRepository pedidoRepository;
    private final EmailService emailService;
    
    @Inject
    public RelatorioService(PedidoRepository pedidoRepository, 
                           EmailService emailService) {
        this.pedidoRepository = pedidoRepository;
        this.emailService = emailService;
    }
}

// ❌ RUIM: Injeção por campo (não recomendado)
@Component
public class RelatorioService {
    @Inject private PedidoRepository pedidoRepository; // Não recomendado
    @Inject private EmailService emailService; // Não recomendado
}
```

### 3. **Granularidade Adequada**

```java
// ✅ BOM: Componentes focados e coesos
@Component
public class ValidadorCPF {
    public boolean validar(String cpf) { /* ... */ }
}

@Component
public class ValidadorEmail {
    public boolean validar(String email) { /* ... */ }
}

// ❌ RUIM: Componente muito genérico
@Component
public class Validador {
    public boolean validarCPF(String cpf) { /* ... */ }
    public boolean validarEmail(String email) { /* ... */ }
    public boolean validarTelefone(String telefone) { /* ... */ }
    // Muitas responsabilidades
}
```

### 4. **Tratamento de Exceções**

```java
@Component
public class ProcessadorPagamento {
    
    @Inject
    public ProcessadorPagamento(PagamentoGateway gateway) {
        this.gateway = gateway;
    }
    
    public ResultadoPagamento processar(PagamentoDTO pagamento) {
        try {
            return gateway.processar(pagamento);
        } catch (GatewayException e) {
            // Converte exceção específica em exceção de domínio
            throw new ProcessamentoPagamentoException(
                "Falha no processamento do pagamento", e);
        }
    }
}
```

***

## Anti-Patterns

### 1. **Service com Lógica Complexa**

```java
// ❌ RUIM: @Service com muita lógica interna
@Service(serviceName = "PedidoServiceSP")
public class PedidoController {
    
    @Inject
    public PedidoController(PedidoRepository repository) {
        this.repository = repository;
    }
    
    public String criarPedido(PedidoDTO pedido) {
        // PROBLEMA: Lógica complexa no controller
        if (pedido.getValor().compareTo(BigDecimal.ZERO) <= 0) {
            throw new ValidationException("Valor inválido");
        }
        
        // Cálculos complexos
        BigDecimal desconto = pedido.getValor().multiply(new BigDecimal("0.10"));
        BigDecimal valorFinal = pedido.getValor().subtract(desconto);
        
        // Múltiplas validações
        if (valorFinal.compareTo(new BigDecimal("10000")) > 0) {
            throw new BusinessException("Valor muito alto");
        }
        
        // Salvamento
        Pedido entidade = new Pedido();
        entidade.setValor(valorFinal);
        repository.save(entidade);
        
        return "Sucesso";
    }
}

// ✅ BOM: Delegação para componentes especializados
@Service(serviceName = "PedidoServiceSP")
public class PedidoController {
    
    private final PedidoService pedidoService;
    
    @Inject
    public PedidoController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }
    
    public String criarPedido(@Valid PedidoDTO pedido) {
        pedidoService.criar(pedido);
        return "Pedido criado com sucesso";
    }
}
```

### 2. **Dependências Circulares**

```java
// ❌ RUIM: Dependência circular
@Component
public class UsuarioService {
    @Inject
    public UsuarioService(PedidoService pedidoService) { /* ... */ }
}

@Component
public class PedidoService {
    @Inject
    public PedidoService(UsuarioService usuarioService) { /* ... */ }
    // ERRO: Dependência circular!
}

// ✅ BOM: Introduza uma abstração ou reorganize
@Component
public class UsuarioService {
    @Inject
    public UsuarioService(UsuarioRepository usuarioRepository) { /* ... */ }
}

@Component
public class PedidoService {
    @Inject
    public PedidoService(PedidoRepository pedidoRepository,
                        UsuarioRepository usuarioRepository) { /* ... */ }
}
```

### 3. **Componentes com Estado Mutável**

```java
// ❌ RUIM: Componente com estado mutável (não thread-safe)
@Component
public class ContadorService {
    private int contador = 0; // PROBLEMA: Estado mutável
    
    public int incrementar() {
        return ++contador; // Não thread-safe
    }
}

// ✅ BOM: Componente stateless ou thread-safe
@Component
public class ContadorService {
    private final AtomicInteger contador = new AtomicInteger(0);
    
    public int incrementar() {
        return contador.incrementAndGet(); // Thread-safe
    }
}
```

***

## Vantagens da Injeção de Dependência

### **Principais Características:**

* **Mais leve:** Menor overhead e startup mais rápido
* **Compile-time safety:** Erros de configuração detectados em tempo de compilação
* **API fluente:** Configuração mais expressiva e type-safe
* **Menos "mágica":** Comportamento mais previsível e debugável

### **No Contexto Sankhya:**

* **Integração nativa:** Otimizado para o ciclo de vida dos Add-ons
* **Performance:** Adequado para ambiente enterprise Sankhya
* **Simplicidade:** Foco apenas no necessário (DI), sem frameworks pesados

***

## Principais Benefícios

* **Automação:** Elimina código boilerplate de criação e conectividade de objetos
* **Produtividade:** Desenvolvedor foca na lógica de negócio, não na infraestrutura
* **Organização:** Dependências explícitas promovem arquitetura limpa
* **Testabilidade:** Injeção via construtor facilita mocks e testes isolados
* **Manutenibilidade:** Baixo acoplamento facilita alterações e evolução do código

***

## 🚀 **Recursos Implementados**

O sistema de injeção de dependências oferece funcionalidades robustas e testadas:

* ✅ **Constructor Injection**: Injeção via construtor com `@Inject`
* ✅ **Component Scanning**: Descoberta automática de `@Component` e `@Service`
* ✅ **Singleton Management**: Instâncias únicas compartilhadas thread-safe
* ✅ **Lazy Initialization**: Criação sob demanda para melhor performance
* ✅ **Dependency Graph Resolution**: Resolução automática de dependências complexas
* ✅ **Circular Dependency Detection**: Detecção de dependências circulares em tempo de compilação
* ✅ **Type Safety**: Injeção baseada em tipos, sem configuração XML
* ✅ **Qualifiers**: Suporte a `@Named` e anotações qualificadoras com `bindWith` para múltiplas implementações.
* ✅ **Service Name Mapping**: URLs automáticas para `@Service` via `serviceName`
* ✅ **Integration with Transactions**: Funciona nativamente com `@Transactional`
* ✅ **Integration with Validation**: Funciona nativamente com `@Valid`

A injeção de dependências no SDK Sankhya oferece uma base sólida e moderna para desenvolvimento de Add-ons, combinando robustez com simplicidade e familiaridade dos padrões modernos de desenvolvimento.
