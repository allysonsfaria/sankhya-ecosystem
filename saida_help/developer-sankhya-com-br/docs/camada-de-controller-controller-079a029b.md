---
id: "https://developer.sankhya.com.br/docs/camada-de-controller-controller"
titulo: "🎮 Camada de Controller (`@Controller`)"
url: "https://developer.sankhya.com.br/docs/camada-de-controller-controller"
atualizado_em: "2026-09-08T19:11:32.000Z"
---

# 🎮 Camada de Controller (`@Controller`)

<br />

# 🎮 Camada de Controller (`@Controller`)

A anotação `@Controller` é um alias semântico para `@Service`, utilizada para marcar classes que representam pontos de entrada da API interna do seu add-on. Ela facilita a separação entre controllers e serviços de negócio, tornando a arquitetura mais clara em projetos grandes.

***

## 🤔 Por que usar `@Controller`?

* ✅ **Clareza Arquitetural:** Distingue controllers de serviços de negócio, facilitando a manutenção e evolução do sistema.
* ✅ **Orquestração:** Controllers devem apenas orquestrar o fluxo da requisição, delegando toda a lógica para componentes (`@Component`) ou serviços de negócio.
* ✅ **Contratos via DTOs:** Sempre utilize DTOs para entrada e saída dos métodos públicos, nunca exponha entidades do domínio diretamente.

***

## 🏗️ Padrão de Implementação

* Injete dependências via `@Inject` no construtor.
* Use `@Transactional` em métodos que alteram dados.
* Utilize DTOs como contratos de entrada e saída.
* Não exponha entidades do domínio.
* Mantenha a lógica de negócio fora do controller.
* Documente a classe e seus métodos com JavaDoc.
* Teste os controllers isoladamente, utilizando mocks para dependências.
* Siga as boas práticas de design de APIs RESTful.

**Exemplo:**

```java
@Controller
public class EstoqueController {

   private final EstoqueRepository estoqueRepository;
   private final EstoqueBusiness estoqueBusiness;
   private final EstoqueMapper estoqueMapper;

   @Inject
   public EstoqueController(
           EstoqueRepository estoqueRepository,
           EstoqueBusiness estoqueBusiness,
           EstoqueMapper estoqueMapper
   ) {
      this.estoqueRepository = estoqueRepository;
      this.estoqueBusiness = estoqueBusiness;
      this.estoqueMapper = estoqueMapper;
   }

   @Transactional
   public EstoqueDTO atualizarEstoque(@Valid AtualizarEstoqueRequestDTO requestDTO) {
      Estoque estoque = estoqueBusiness.processarAtualizacao(requestDTO);
      Estoque estoqueSalvo = estoqueRepository.save(estoque);
      return estoqueMapper.toDTO(estoqueSalvo);
   }

   public List<EstoqueDTO> listarPorProduto(BigDecimal codProduto) {
      List<Estoque> estoques = estoqueRepository.findByProduto(codProduto);
      return estoques.stream()
              .map(estoqueMapper::toDTO)
              .collect(Collectors.toList());
   }
}
```

***

## Como funciona o `@Controller`

O `@Controller` é utilizado para registrar serviços na plataforma e expor métodos públicos como ações acessíveis externamente.

### Principais características

* **Atributo obrigatório&#x20;**`serviceName`**:** Define o nome do serviço registrado. Por convenção, o nome termina com `SP`.
* **Métodos públicos:** São automaticamente expostos como ações do serviço.
* **Injeção de dependências:** É realizada via construtor.

### URL de acesso

A estrutura para acessar um método do serviço é:

```
<dns>/<contexto-modulo>/service.sbr?serviceName=<nomeDoServico>.<nomeDoMetodo>
```

#### Exemplo de chamada

```
http://localhost:8080/<contexto-do-meu-addon>/service.sbr?serviceName=PedidoControllerSP.criarPedido&mgeSession=<jsession-id-gerado-no-mobile-login>
```

* `contexto-do-meu-addon` corresponde ao valor de `rootProject.name` no arquivo `settings.gradle`.
* Exemplo: para um template `addon-template`, a URL completa seria:

```
http://localhost:8080/addon-template/service.sbr?serviceName=PedidoControllerSP.criarPedido&mgeSession=<jsession-id-gerado-no-mobile-login>
```

### Autenticação

Todas as requisições devem ser autenticadas, utilizando `MobileLogin` para obter o `jsessionId`, que será passado no parâmetro `mgeSession`.

#### Exemplo de login:

```bash
curl --location 'http://localhost:8080/mge/service.sbr?serviceName=MobileLoginSP.login&outputType=json' \
--header 'Content-Type: application/json' \
--data '{
    "requestBody": {
        "NOMUSU": {"$": "USUARIO"},
        "INTERNO": {"$": "SENHA_DO_USUARIO"}
    }
}'
```

O retorno contém o atributo `jsessionId`, que deve ser usado nas requisições aos serviços.

> **Observação**: Em ambientes não gateway, é necessário realizar `MobileLogin`.
> Quando a requisição passa pelo Gateway, a autenticação via `MobileLogin` não é necessária.
> Consulte a [documentação do Gateway](https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya) para mais detalhes.

***

## Controle Transacional (`transactionType`)

A anotação `@Controller` permite configurar o comportamento transacional padrão para todos os métodos da classe através do atributo `transactionType`:

```java
@Controller(
    serviceName = "RelatorioControllerSP",
    transactionType = TransactionType.NotSupported
)
public class RelatorioController {
    // ...
}
```

| `TransactionType` | Descrição                                                                                                    | Quando Usar                                                                        |
| :---------------- | :----------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| `Required`        | Garante que o método sempre execute dentro de uma transação. Se já existir, utiliza-a; senão, cria uma nova. | Ideal para operações de escrita (CRUD).                                            |
| `NotSupported`    | Executa fora de qualquer transação. Se houver uma ativa, ela é suspensa.                                     | Operações de leitura que não precisam de consistência transacional.                |
| `Supported`       | Executa dentro de uma transação se já houver uma ativa; caso contrário, executa sem transação.               | Operações de leitura que podem ou não fazer parte de uma transação maior. (Padrão) |

> **Nota:** A anotação `@Transactional` em um método sempre tem precedência sobre o `transactionType` definido na classe, permitindo controle granular.

### Sobrepondo o padrão com `@Transactional`

```java
@Controller(serviceName = "ConsultaControllerSP", transactionType = TransactionType.NotSupported)
public class ConsultaController {
    
    // Este método usa o padrão da classe (NotSupported)
    public List<ProdutoDTO> listarProdutos() {
        // ... lógica de consulta ...
    }

    @Transactional(type = TransactionType.RequiresNew) // Sobrepõe o padrão
    public void registrarLogDeConsulta() {
        // Executa em sua própria transação
    }
}
```

## Boas Práticas

* Controllers devem apenas orquestrar o fluxo, nunca conter lógica de negócio complexa.
* Sempre use DTOs como contratos.
* Delegue validações e regras para componentes ou serviços de negócio.

***

## 📡 Exemplos de Requisição e Resposta

### 📋 DTOs de Exemplo

Antes de mostrar as requisições HTTP, vamos definir os DTOs que serão utilizados nos exemplos:

#### DTOs de Request

```java PedidoDTO.java
// DTO para criar pedido
public class PedidoDTO {
    private ClienteDTO cliente;
    private List<ItemPedidoDTO> itens;
    private String observacao;
    
    // getters e setters...
}
```

```java ClienteDTO.java
public class ClienteDTO {
    private Integer codigo;
    private String nome;
    
    // getters e setters...
}
```

```java ItemPedidoDTO.java
public class ItemPedidoDTO {
    private Integer produtoId;
    private Integer quantidade;
    private Double valorUnitario;
    
    // getters e setters...
}
```

```java FiltroDTO.java
// DTO para filtros de consulta
public class FiltroDTO {
    private String categoria;
    private Boolean ativo;
    private Integer limite;
    
    // getters e setters...
}
```

```java LoteDTO.java
// DTO para processamento de lote
public class LoteDTO {
    private String identificador;
    private List<RegistroDTO> registros;
    private ConfiguracaoDTO configuracao;
    
    // getters e setters...
}
```

```java RegistroDTO.java
public class RegistroDTO {
    private String tipo;
    private Map<String, Object> dados;
    
    // getters e setters...
}
```

```java ConfiguracaoDTO.java
public class ConfiguracaoDTO {
    private Boolean validacaoRigida;
    private Boolean interromperNoErro;
    
    // getters e setters...
}
```

#### DTOs de Response

```java PedidoCriadoDTO.java
// DTO de resposta para criação de pedido
public class PedidoCriadoDTO {
    private Long numeroPedido;
    private LocalDate dataVencimento;
    private Double valorTotal;
    private String status;
    
    // getters e setters...
}
```

```java ProdutoDTO.java
// DTO para listagem de produtos
public class ProdutoDTO {
    private Long id;
    private String nome;
    private String categoria;
    private Double preco;
    private Boolean ativo;
    
    // getters e setters...
}
```

```java UsuarioDTO.java
// DTO para buscar usuário
public class UsuarioDTO {
    private Long id;
    private String nome;
    private String email;
    private String perfil;
    
    // getters e setters...
}
```

```java ResultadoDTO.java
// DTO de resposta para processamento de lote
public class ResultadoDTO {
    private String loteId;
    private Integer totalProcessados;
    private Integer sucessos;
    private Integer erros;
    private List<DetalheProcessamentoDTO> detalhes;
    
    // getters e setters...
}
```

```java DetalheProcessamentoDTO.java
public class DetalheProcessamentoDTO {
    private Integer registro;
    private String status;
    private Long id;
    private String mensagem;
    
    // getters e setters...
}
```

### 🔄 Exemplo de Requisição HTTP

#### 📋 Formato Padrão da Request

O JSON da request deve seguir o padrão da API legada do Sankhya:

```json
{
  "serviceName": "NomeDoServico.nomeDoMetodo",
  "requestBody": {
    "nomeParametro1": { /* objeto correspondente ao DTO */ },
    "nomeParametro2": { /* objeto correspondente ao DTO */ }
  }
}
```

**Regras importantes:**

* `serviceName`: Nome completo do serviço e método (ex: `PedidoControllerSP.criarPedido`)
* `requestBody`: Contém os argumentos do método como propriedades nomeadas
* **Cada argumento**: É mapeado pelo nome do parâmetro no método Java

**Exemplo de método:**

```java
public PedidoCriadoDTO criarPedido(PedidoDTO pedido) {
    // O parâmetro "pedido" será mapeado para "pedido" no requestBody
}
```

#### 🚀 Exemplo Prático de Requisição

**URL:** `.../<contexto-do-meu-addon>/service.sbr?serviceName=PedidoControllerSP.criarPedido`
**Método:** `POST`

**Content-Type:** `application/json`

**Request Body** (correspondente ao método `criarPedido(PedidoDTO pedido)`):

```json
{
  "serviceName": "PedidoControllerSP.criarPedido",
  "requestBody": {
    "pedido": {
      "cliente": {
        "codigo": 12345,
        "nome": "João Silva"
      },
      "itens": [
        {
          "produtoId": 100,
          "quantidade": 2,
          "valorUnitario": 150.50
        },
        {
          "produtoId": 101,
          "quantidade": 1,
          "valorUnitario": 250.00
        }
      ],
      "observacao": "Entrega urgente"
    }
  }
}
```

### 📤 Exemplo de Resposta

#### 📋 Formato Padrão da Response

A resposta segue o envelope padrão da API legada do Sankhya:

```json
{
  "serviceName": "NomeDoServico.nomeDoMetodo",
  "status": "1",              // "1" = Sucesso, "0" = Erro, "3" = Timeout, "4" = Cancelado
  "pendingPrinting": "false",
  "transactionId": "HASH_DA_TRANSACAO",
  "responseBody": { /* objeto retornado pelo método */ }
}
```

#### ✅ Response de Sucesso

**Response Status:** `200 OK`

**Content-Type:** `application/json`

**Response Body** (correspondente ao `PedidoCriadoDTO` retornado):

```json
{ 
  "serviceName": "PedidoControllerSP.criarPedido",
  "status": "1",
  "pendingPrinting": "false",
  "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
  "responseBody": {
    "numeroPedido": 987654,
    "dataVencimento": "2024-12-31",
    "valorTotal": 551.00,
    "status": "PENDENTE"
  }
}
```

#### ❌ Response de Erro

Quando `status` é diferente de `"1"`, indica erro:

* **"0"** - Erro de execução
* **"3"** - Timeout
* **"4"** - Serviço cancelado por concorrência

```json
{ 
  "serviceName": "PedidoControllerSP.criarPedido",
  "status": "0",
  "pendingPrinting": "false",
  "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
  "statusMessage": "Erro de validação: O campo nome é obrigatório;\n\t- O campo descricao é obrigatório"
}
```

**Observação:** Em caso de erro, o campo `responseBody` não é incluído, e a mensagem de erro fica em `statusMessage`.

## ❌ Anti-Patterns

* Não retornar entidades do domínio.
* Não capturar exceções de negócio sem relançá-las.
* Não misturar lógica de negócio com orquestração.

***

## 📌 Observações

* `@Controller` é tecnicamente equivalente a `@Service`, mas seu uso é recomendado para clareza arquitetural.
* Siga os mesmos padrões de injeção, validação e transação documentados para `@Service`.

***
