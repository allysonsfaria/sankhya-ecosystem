---
id: "https://developer.sankhya.com.br/docs/conceitos-fundamentais"
titulo: "🎯 Conceitos Fundamentais"
url: "https://developer.sankhya.com.br/docs/conceitos-fundamentais"
atualizado_em: "2026-09-08T19:10:52.000Z"
---

# 🎯 Conceitos Fundamentais

# 🎯 Conceitos Fundamentais do SDK Sankhya

O SDK Sankhya foi criado para modernizar o desenvolvimento na plataforma, tornando-o mais rápido, seguro e alinhado com as melhores práticas do mercado.

Este documento apresenta os conceitos essenciais que transformam a maneira como você cria add-ons.

## 🤔 Por que Mudar? A Diferença na Prática

Vamos comparar a criação de um serviço simples de cadastro nas duas abordagens.

### ❌ Abordagem Tradicional (Legado)

No modelo antigo, o código é verboso, utiliza "strings mágicas" para nomes de campos e exige controle manual de sessões e transações.

```java
// Código verboso, propenso a erros e difícil de testar
public class VeiculoServiceSPBean extends SessionBean {

    public void cadastrarVeiculo(ServiceContext ctx) throws Exception {
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            JapeWrapper dao = JapeFactory.dao("Veiculo");
            FluidCreateVO vo = dao.create();

            // Risco de erros de digitação e sem validação de tipo
            JsonObject jsonRequestBody = ctx.getJsonRequestBody();
            vo.set("PLACA", jsonRequestBody.get("PLACA").getAsString());
            vo.set("MARCA", jsonRequestBody.get("MARCA").getAsString());
            vo.set("ATIVO", "S");

            DynamicVO novoRegistro = vo.save(); // Controle transacional manual

            JsonObject jsonResponse = new JsonObject();
            jsonResponse.addProperty("CODVEICULO", novoRegistro.asBigDecimal("CODVEICULO").toString());
            ctx.setJsonResponse(jsonResponse);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
```

### ✅ Nova Abordagem com o SDK Sankhya

Com o SDK, o código é limpo, declarativo e seguro. As responsabilidades são bem definidas, e o framework cuida da infraestrutura para você.

```java
// Código limpo, seguro, moderno e fácil de testar
@Service(serviceName = "VeiculoServiceSP")
public class VeiculoService {

    private final VeiculoRepository repository;

    @Inject
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }

    @Transactional // O SDK gerencia a transação para você
    public Long cadastrarVeiculo(@Valid VeiculoDTO dto) {
        // Validação automática do DTO
        Veiculo veiculo = new Veiculo();
        veiculo.setPlaca(dto.getPlaca());
        veiculo.setMarca(dto.getMarca());
        veiculo.setAtivo(true);

        // Persistência type-safe
        repository.save(veiculo);

        return veiculo.getCodVeiculo();
    }
}
```

### 📊 Tabela Comparativa

| Aspecto                    | Abordagem Antiga                | ✅ SDK Sankhya                               |
| :------------------------- | :------------------------------ | :------------------------------------------ |
| **Segurança de Tipos**     | ❌ "Strings mágicas"             | **Tipos seguros em compilação**             |
| **Validação**              | ❌ Manual e verbosa              | **Automática com anotações (**`@Valid`**)** |
| **Injeção de Dependência** | ❌ Manual (`JapeFactory`, `new`) | **Automática (**`@Inject`**)**              |
| **Controle de Transação**  | ❌ Manual e complexo             | **Declarativo (**`@Transactional`**)**      |
| **Testabilidade**          | ❌ Difícil de isolar e testar    | **Nativamente testável com mocks**          |
| **Manutenibilidade**       | ❌ Código acoplado e verboso     | **Código limpo, desacoplado e expressivo**  |

***

## ✨ Os 4 Pilares do SDK

A nova abordagem é sustentada por quatro conceitos principais que trabalham juntos.

### 1. Mapeamento Objeto-Relacional (ORM) com POJOs

Em vez de usar `DynamicVO`, você mapeia suas tabelas para **POJOs (Plain Old Java Objects)** com anotações, similar ao padrão JPA.

* `@JapeEntity`: Marca uma classe como uma entidade do banco de dados.
* `@Id` e `@Column`: Mapeiam os campos da classe para as colunas da tabela.

```java
@JapeEntity(entity = "Veiculo", table = "TGFVEI")
public class Veiculo {
    @Id
    @Column(name = "CODVEICULO")
    private Long codVeiculo;

    @Column(name = "PLACA")
    private String placa;
    // ... getters e setters
}
```

### 2. Injeção de Dependências (DI)

O SDK gerencia o ciclo de vida dos seus objetos. Em vez de instanciar manualmente, você simplesmente declara o que precisa no construtor, e o SDK injeta as dependências.

* `@Inject`: Anotação usada no construtor para solicitar a injeção.

```java
public class VeiculoService {
    private final VeiculoRepository repository;

    @Inject // O SDK vai procurar e injetar um VeiculoRepository
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }
}
```

### 3. Padrão Repository

Abstrai completamente a complexidade do Jape. Você define uma interface que estende `JapeRepository`, e o SDK cria a implementação para você.

* `@Repository`: Marca a interface como um repositório.

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
 

    // Para consultas mais complexas
    @Criteria("marca = :marca AND ativo = 'S'")
    List<Veiculo> findAllAtivosPorMarca(@Parameter("marca") String marca);
}
```

### 4. Camada de Serviço e Transações

A lógica de negócio reside na camada de serviço, que orquestra as chamadas aos repositórios.

* `@Service`: Define uma classe como um serviço, tornando-a elegível para injeção.
* `@Transactional`: Garante que todos os métodos dentro dele executem em uma única transação de banco de dados. Se um erro ocorrer, todas as operações são revertidas (rollback).

```java
@Service
public class VeiculoService {
    // ...

    @Transactional
    public void atualizarPlaca(Long codVeiculo, String novaPlaca) {
        Veiculo veiculo = repository.findByPK(codVeiculo)
            .orElseThrow(() -> new NotFoundException("Veículo não encontrado"));

        veiculo.setPlaca(novaPlaca);
        repository.save(veiculo); // Tudo dentro de uma transação segura
    }
}
```

***

## 🏗️ **Os Quatro Pilares Fundamentais**

### 1️⃣ **Mapeamento de Entidades com POJOs**

#### 💡 **Conceito**

O SDK permite o mapeamento de entidades através de **POJOs (Plain Old Java Objects)** anotados, similar ao padrão JPA amplamente utilizado no mercado. Esta abordagem substitui os objetos complexos tradicionais por classes Java simples e modernas.

#### ✨ **Características**

* **Automático:** Mapeamento transparente sem configuração manual
* **Type-safe:** Baseado em tipos, reduzindo erros em tempo de compilação
* **Framework moderno:** Framework leve e eficiente para ORM

#### 🔧 **Exemplo Prático**

```java
@Data
@JapeEntity(entity = "Veiculo", table = "TGFVEI")
public class Veiculo {
    
    @Id
    @Column(name = "CODVEICULO")
    private Long id;
    
    @Column(name = "PLACA")
    @Pattern(regexp = "[A-Z]{3}[0-9]{4}", message = "Formato de placa inválido")
    private String placa;
    
    @Column(name = "ATIVO")
    @NotNull(message = "Status ativo é obrigatório")
    private Boolean ativo;
}
```

#### 🎯 **Benefícios**

* ✅ **Legibilidade:** Código mais limpo e fácil de entender
* ✅ **Manutenibilidade:** Estruturas simples facilitam alterações futuras
* ✅ **Produtividade:** Menos código para escrever e manter
* ✅ **Familiaridade:** Padrão conhecido por desenvolvedores Java/Spring

***

### 2️⃣ **Injeção de Dependências**

#### 💡 **Conceito**

A **Injeção de Dependências (DI)** no SDK Sankhya permite ao sistema fornecer automaticamente as dependências que uma classe precisa, eliminando a necessidade de criação manual de objetos (`new Classe()`).

### Anotações Principais

* `@Component`**:** Marca uma classe como um componente de negócio gerenciável pelo framework
* `@Service`**:** Marca uma classe como um controller/serviço (equivalente aos controllers do Spring)
* `@Inject`**:** Indica que uma dependência deve ser injetada automaticamente

### Exemplo Prático

```java
@Component
public class VeiculoProcessor {
    protected VeiculoProcessor() {}
    
    public void processar(String placa) {
        System.out.println("Processando veículo: " + placa);
    }
}

// @Service como ponto de entrada (Controller)
@Service(serviceName = "VeiculoServiceSP")
public class VeiculoController {
    
    private final VeiculoProcessor processor;
    
    @Inject
    public VeiculoController(VeiculoProcessor processor) {
        this.processor = processor;
    }
    
    public void processarVeiculo(String placa) {
        // Delega para o componente de negócio
        processor.processar(placa);
    }
}
```

### Benefícios

* **Baseado em Guice:** Framework leve e eficiente para DI
* **Desacoplamento:** Classes não dependem de implementações concretas
* **Testabilidade:** Facilita a criação de testes unitários com mocks
* **Separação clara:** `@Service` para pontos de entrada, `@Component` para lógica de negócio

***

## 3. Controle Transacional Declarativo

### Conceito

O **Controle Transacional** garante a integridade e consistência dos dados através de um modelo declarativo. Com uma simples anotação, o desenvolvedor define o comportamento transacional sem código complexo de gerenciamento.

### Funcionamento

A anotação `@Transactional` transforma um método em uma unidade atômica:

* **Início automático:** Transação inicia antes da execução do método
* **Commit automático:** Dados são persistidos se o método executa sem erros
* **Rollback automático:** Todas as alterações são desfeitas em caso de exceção

### Exemplo Prático

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoService {
    
    private final PedidoRepository repository;
    
    @Inject
    public PedidoService(PedidoRepository repository) {
        this.repository = repository;
    }
    
    @Transactional
    public void criarPedidoCompleto(PedidoDTO dados) {
        // 1. Salvar cabeçalho
        Pedido pedido = repository.save(dados.toPedido());
        
        // 2. Salvar itens
        dados.getItens().forEach(item -> 
            repository.saveItem(item.toItemPedido(pedido.getId()))
        );
        
        // Se qualquer operação falhar, TUDO é desfeito automaticamente
    }
}
```

### Benefícios

* **Integridade:** Garante consistência dos dados
* **Simplicidade:** Não requer código manual de transação
* **Segurança:** Rollback automático em caso de erro
* **Performance:** Otimização automática das operações

***

## 4. Bean Validation

### Conceito

O **Bean Validation** oferece um sistema de validação declarativo e automático para objetos (DTOs, entidades, etc.), utilizando anotações padrão da especificação Java Bean Validation.

### Anotações Principais

* `@NotNull`**:** Campo não pode ser nulo
* `@NotBlank`**:** String não pode ser vazia ou só espaços
* `@Size`**:** Define tamanho mínimo/máximo
* `@Pattern`**:** Validação por expressão regular
* `@Valid`**:** Ativa validação em cascata

### Exemplo Prático

```java
@Data
public class VeiculoDTO {
    
    @NotBlank(message = "Placa é obrigatória")
    @Pattern(regexp = "[A-Z]{3}[0-9]{4}", message = "Formato de placa inválido")
    private String placa;
    
    @NotNull(message = "Status ativo é obrigatório")
    private Boolean ativo;
    
    @Size(min = 2, max = 50, message = "Modelo deve ter entre 2 e 50 caracteres")
    private String modelo;
}

@Service(serviceName = "VeiculoServiceSP")
public class VeiculoController {
    
    @Transactional
    public void cadastrarVeiculo(@Valid VeiculoDTO veiculo) {
        // Validações são executadas automaticamente
        // Se alguma validação falhar, uma exceção é lançada
        // antes mesmo de entrar na lógica do método
    }
}
```

### Benefícios

* **Automatização:** Validações executadas automaticamente
* **Declarativo:** Regras definidas através de anotações
* **Reutilização:** Validações aplicáveis em múltiplos contextos
* **Padronização:** Uso de especificação Java padrão
* **Mensagens Customizadas:** Feedback claro para o usuário

***

## Integração dos Conceitos

Estes quatro conceitos trabalham em conjunto para criar uma arquitetura moderna e robusta:

```java
// 1. Entidade POJO
@Data
@JapeEntity(entity = "Veiculo", table = "TGFVEI")
public class Veiculo {
    @Id @Column(name = "CODVEICULO")
    private Long id;
    
    @Column(name = "PLACA")
    private String placa;
}

// 2. DTO com Bean Validation
@Data
public class VeiculoDTO {
    @NotBlank(message = "Placa obrigatória")
    private String placa;
}

// 3. Repositório injetável
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    Optional<Veiculo> findByPlaca(String placa);
}

// 4. Controller com DI e controle transacional
@Service(serviceName = "VeiculoServiceSP")
public class VeiculoController {
    
    private final VeiculoService veiculoService;
    
    @Inject  // Injeção de Dependência
    public VeiculoController(VeiculoService veiculoService) {
        this.veiculoService = veiculoService;
    }
    
    @Transactional  // Controle Transacional
    public void cadastrar(@Valid VeiculoDTO dto) {  // Bean Validation
        // Delega para o componente de negócio
        veiculoService.cadastrar(dto);
    }
}

// 5. Componente de negócio
@Component
public class VeiculoService {
    
    private final VeiculoRepository repository;
    
    @Inject
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }
    
    public void cadastrar(VeiculoDTO dto) {
        Veiculo veiculo = new Veiculo();
        veiculo.setPlaca(dto.getPlaca());
        repository.save(veiculo);  // Entidade POJO
    }
}
```

Esta integração resulta em um código mais limpo, testável, manutenível e alinhado com as melhores práticas do mercado de desenvolvimento Java.
