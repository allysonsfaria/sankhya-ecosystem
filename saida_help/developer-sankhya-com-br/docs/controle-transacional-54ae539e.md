---
id: "https://developer.sankhya.com.br/docs/controle-transacional"
titulo: "🔗 Controle Transacional"
url: "https://developer.sankhya.com.br/docs/controle-transacional"
atualizado_em: "2026-09-08T19:13:34.000Z"
---

# 🔗 Controle Transacional

# 🔗 Controle Transacional com `@Transactional`

O controle transacional garante a **integridade e a consistência dos dados** durante operações de negócio que envolvem múltiplos passos. Ele assegura que um conjunto de ações no banco de dados seja tratado como uma única unidade atômica: ou **todas** as operações são concluídas com sucesso, ou **nenhuma** delas é permanentemente salva.

No SDK, isso é feito de forma declarativa com a anotação `@Transactional`.

## 🤔 Por que usar `@Transactional`?

* ✅ **Segurança e Integridade:** Evita que dados fiquem em estado inconsistente (ex: um pedido sem itens).
* ✅ **Rollback Automático:** Em caso de erro, o SDK desfaz automaticamente todas as alterações feitas no banco de dados dentro daquele escopo.
* ✅ **Código Limpo:** Elimina a necessidade de blocos `try/catch/finally` para controle manual de transações (`JapeSession.open()`, `JapeSession.close()`).

***

## 🚀 Como Funciona?

Quando um método público em uma classe `@Service` ou `@Component` é anotado com `@Transactional`, o SDK:

1. **Inicia uma transação** antes de o método ser executado.
2. Executa a lógica de negócio do método.
3. **Se o método for concluído sem erros**, a transação é "commitada", e as alterações são salvas permanentemente.
4. **Se qualquer**`Exception`**&#x20;(não checada) for lançada**, a transação sofre "rollback", e todas as alterações são desfeitas.

**Exemplo Prático:**

Imagine um serviço que cria um pedido e seus itens.

```java
@Service(name = "PedidoServiceSP")
public class PedidoService {
    // ... injeção de dependências

    @Transactional
    public void criarNovoPedido(PedidoDTO dto) {
        // 1. Salva o cabeçalho do pedido
        CabecalhoPedido cabecalho = cabecalhoRepository.save(dto.getCabecalho());

        // 2. Simulação de um erro no meio do processo
        if (dto.getItens().isEmpty()) {
            throw new IllegalStateException("Pedido deve ter pelo menos um item.");
        }

        // 3. Salva os itens do pedido
        for (ItemDTO itemDto : dto.getItens()) {
            itemRepository.save(itemDto, cabecalho.getId());
        }
    }
}
```

**Cenários:**

* **Sucesso:** Se o DTO tiver itens, o cabeçalho e todos os itens são salvos no banco de dados.
* **Falha:** Se o DTO não tiver itens, uma `IllegalStateException` é lançada. O `@Transactional` intercepta o erro, e a inserção do cabeçalho (que ocorreu no passo 1) é **desfeita (rollback)**. O banco de dados volta ao estado original, como se nada tivesse acontecido.

***

## ⚙️ Tipos de Propagação Transacional

O atributo `type` na anotação `@Transactional` define como um método transacional se comporta quando é chamado por outro método que já possui uma transação ativa.

```java
import br.com.sankhya.studio.transaction.TransactionType;

@Transactional(type = TransactionType.REQUIRES_NEW)
public void meuMetodo() {
    // ...
}
```

| `TransactionType` | Descrição                                                                                        | Quando Usar                                                                                                                                   |
| :---------------- | :----------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `REQUIRED`        | **(Padrão)** Se uma transação já existir, usa a mesma. Se não, **cria uma nova**.                | A escolha na maioria dos casos. Garante que tudo execute em um contexto transacional.                                                         |
| `REQUIRES_NEW`    | **Sempre cria uma nova transação**, suspendendo a atual se existir.                              | Casos específicos, como registrar um log de auditoria que precisa ser salvo **independentemente** do sucesso ou falha da transação principal. |
| `NOT_SUPPORTED`   | Executa o método **fora de qualquer transação**. Se uma transação estiver ativa, ela é suspensa. | Ideal para **operações de apenas leitura (consultas)**, pois melhora o desempenho ao não criar a sobrecarga de uma transação.                 |
| `SUPPORTS`        | Se uma transação existir, junta-se a ela. Se não, executa sem transação.                         | Raro. Usado quando um método pode ou não precisar de uma transação.                                                                           |
| `MANDATORY`       | Exige que uma transação já exista. Se não existir, lança uma exceção.                            | Usado para garantir que um método só seja chamado dentro de um contexto transacional já estabelecido.                                         |
| `NEVER`           | Lança uma exceção se uma transação estiver ativa.                                                | Usado para garantir que um método nunca seja chamado dentro de um contexto transacional.                                                      |

### Exemplo de `REQUIRES_NEW`

```java
@Service(name = "ProcessamentoServiceSP")
public class ProcessamentoService {

    @Inject private AuditoriaService auditoriaService;

    @Transactional(type = TransactionType.REQUIRED)
    public void processarDados() {
        // Inicia a transação principal (T1)
        try {
            // ... lógica de negócio ...
            throw new RuntimeException("Erro de negócio!");
        } finally {
            // Chama o serviço de auditoria
            auditoriaService.registrarTentativa("processarDados");
        }
    }
}

@Service(name = "AuditoriaServiceSP")
public class AuditoriaService {

    @Transactional(type = TransactionType.REQUIRES_NEW)
    public void registrarTentativa(String operacao) {
        // Suspende T1 e inicia uma nova transação (T2)
        // Salva o log de auditoria
        // Commita T2
    }
}
```

Neste caso, mesmo que `processarDados` falhe e sua transação (T1) sofra rollback, o log de auditoria **será salvo**, pois foi executado em uma transação separada e independente (T2).

## ✨ Boas Práticas

* **Use em Camadas de Serviço:** A anotação `@Transactional` deve ser usada nos métodos da sua camada de serviço (as classes que orquestram a lógica de negócio).
* **Métodos Públicos:** A transação só é aplicada em métodos `public`. Métodos `private` ou `protected` chamados de dentro da mesma classe não herdam o comportamento transacional.
* **Leitura vs. Escrita:** Para métodos que apenas leem dados e não modificam nada, use `@Transactional(type = TransactionType.NOT_SUPPORTED)` ou configure o `@Service` com `transactionType = TransactionType.NotSupported` para melhorar o desempenho.
* **Evite Operações Longas:** Mantenha suas transações curtas e rápidas para evitar prender recursos do banco de dados por muito tempo.

### Tratamento de Erros e Log de Auditoria

```java
@Component
public class AuditoriaService {
    
    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public void registrarErro(String operacao, String erro, String usuario) {
        // Esta operação sempre será salva, mesmo se a transação principal falhar
        System.out.println("Erro registrado: " + operacao + " - " + erro + " - " + usuario);
        // Salvar no banco de auditoria...
    }
    
    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public void registrarOperacao(String operacao, String usuario) {
        // Log de operação independente da transação principal
        System.out.println("Operação registrada: " + operacao + " - " + usuario);
    }
}

@Service(serviceName = "PedidoComAuditoriaServiceSP")
public class PedidoComAuditoriaService {
    
    private final PedidoRepository pedidoRepository;
    private final AuditoriaService auditoriaService;

    @Inject
    public PedidoComAuditoriaService(PedidoRepository pedidoRepository, 
                                     AuditoriaService auditoriaService) {
        this.pedidoRepository = pedidoRepository;
        this.auditoriaService = auditoriaService;
    }

    @Transactional
    public void criarPedidoComAuditoria(String dadosCabecalho, String dadosItens, String usuario) {
        try {
            // Registra o início da operação (sempre será salvo)
            auditoriaService.registrarOperacao("CRIAR_PEDIDO_INICIO", usuario);
            
            // Operações principais
            pedidoRepository.salvarCabecalho(dadosCabecalho);
            pedidoRepository.salvarItens(dadosItens);
            
            // Registra sucesso (sempre será salvo)
            auditoriaService.registrarOperacao("CRIAR_PEDIDO_SUCESSO", usuario);
            
        } catch (Exception e) {
            // Registra o erro (sempre será salvo, mesmo com rollback da transação principal)
            auditoriaService.registrarErro("CRIAR_PEDIDO", e.getMessage(), usuario);
            
            // Re-lança a exceção para causar rollback da transação principal
            throw e;
        }
    }
}
```

### Transações Aninhadas com Diferentes Propagações

```java
@Component
public class NotificacaoService {
    
    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public void enviarEmail(String destinatario, String assunto, String mensagem) {
        try {
            // Simula envio de email
            System.out.println("Email enviado para: " + destinatario);
        } catch (Exception e) {
            // Log do erro, mas como está em transação separada,
            // não afeta a transação principal
            System.err.println("Erro ao enviar email: " + e.getMessage());
        }
    }
}

@Service(serviceName = "PedidoComNotificacaoServiceSP")
public class PedidoComNotificacaoService {
    
    private final PedidoRepository pedidoRepository;
    private final NotificacaoService notificacaoService;

    @Inject
    public PedidoComNotificacaoService(PedidoRepository pedidoRepository,
                                       NotificacaoService notificacaoService) {
        this.pedidoRepository = pedidoRepository;
        this.notificacaoService = notificacaoService;
    }

    @Transactional
    public void criarPedidoComNotificacao(String dadosCabecalho, String dadosItens, String emailCliente) {
        // Salva o pedido (transação principal)
        pedidoRepository.salvarCabecalho(dadosCabecalho);
        pedidoRepository.salvarItens(dadosItens);
        
        try {
            // Envia notificação em transação separada
            // Se falhar, não afeta o salvamento do pedido
            notificacaoService.enviarEmail(emailCliente, 
                                         "Pedido Criado", 
                                         "Seu pedido foi criado com sucesso!");
        } catch (Exception e) {
            // Log do erro, mas não interrompe a operação principal
            System.err.println("Aviso: Não foi possível enviar email de confirmação: " + e.getMessage());
        }
    }
}
```

### Exemplo com Múltiplas Operações e Rollback Seletivo

```java
@Service(serviceName = "ProcessamentoCompletoServiceSP")
public class ProcessamentoCompletoService {
    
    private final PedidoRepository pedidoRepository;
    private final EstoqueService estoqueService;
    private final FinanceiroService financeiroService;

    @Inject
    public ProcessamentoCompletoService(PedidoRepository pedidoRepository,
                                        EstoqueService estoqueService,
                                        FinanceiroService financeiroService) {
        this.pedidoRepository = pedidoRepository;
        this.estoqueService = estoqueService;
        this.financeiroService = financeiroService;
    }

    @Transactional
    public void processarPedidoCompleto(PedidoDTO pedido) 
            throws EstoqueInsuficienteException, CreditoInsuficienteException {
        
        try {
            // 1. Criar o pedido
            pedidoRepository.salvarCabecalho(pedido.getCabecalho());
            pedidoRepository.salvarItens(pedido.getItens());
            
            // 2. Verificar e reservar estoque (pode falhar)
            estoqueService.reservarItens(pedido.getItens());
            
            // 3. Processar pagamento (pode falhar)
            financeiroService.processarPagamento(pedido.getPagamento());
            
            // 4. Confirmar pedido
            pedidoRepository.confirmarPedido(pedido.getId());
            
        } catch (EstoqueInsuficienteException e) {
            // Rollback automático - pedido não será criado
            throw e;
        } catch (CreditoInsuficienteException e) {
            // Rollback automático - pedido não será criado
            throw e;
        } catch (Exception e) {
            // Para outras exceções, também fazer rollback
            throw new RuntimeException("Erro inesperado no processamento do pedido", e);
        }
    }
}
```

***

## Boas Práticas

### 1. **Use Transações no Nível Certo**

```java
// ✅ BOM: Transação na camada de serviço
@Service(serviceName = "UsuarioServiceSP")
public class UsuarioService {
    
    @Transactional
    public void criarUsuario(UsuarioDTO usuario) {
        // Múltiplas operações em uma transação
        usuarioRepository.save(usuario);
        perfilRepository.associarPerfil(usuario.getId(), usuario.getPerfilId());
        auditoriaService.registrar("USUARIO_CRIADO", usuario.getId());
    }
}

// ❌ RUIM: Transação em métodos muito granulares
@Repository
public class UsuarioRepository {
    @Transactional // Muito granular
    public void save(Usuario usuario) { /* ... */ }
}
```

### 2. **Mantenha Transações Curtas**

```java
// ✅ BOM: Transação focada e rápida
@Transactional
public void atualizarStatusPedido(Long pedidoId, StatusPedido novoStatus) {
    Pedido pedido = pedidoRepository.findByPK(pedidoId);
    pedido.setStatus(novoStatus);
    pedidoRepository.update(pedido);
}

// ❌ RUIM: Transação muito longa
@Transactional
public void processarPedidoCompleto(PedidoDTO pedido) {
    // ... múltiplas operações demoradas
    Thread.sleep(5000); // Simula operação lenta
    // ... mais operações
    // PROBLEMA: Mantém locks por muito tempo
}
```

### 3. **Use REQUIRES\_NEW para Operações Independentes**

```java
// ✅ BOM: Log independente da transação principal
@Transactional(Transactional.TxType.REQUIRES_NEW)
public void registrarAuditoria(String operacao, String detalhes) {
    // Sempre salva, mesmo se transação principal falhar
    auditoriaRepository.save(new RegistroAuditoria(operacao, detalhes));
}
```

### 4. **Trate Exceções Apropriadamente**

```java
// ✅ BOM: Tratamento específico de exceções
@Transactional
public void processarDocumento(DocumentoDTO documento) {
    try {
        // Lógica de processamento
        documentoRepository.save(documento);
        validadorService.validar(documento);
    } catch (BusinessException e) {
        // RuntimeException - causa rollback automaticamente
        throw e;
    } catch (ValidationWarningException e) {
        // Se você quiser que esta exceção NÃO cause rollback,
        // capture e trate sem re-lançar
        System.out.println("Aviso de validação: " + e.getMessage());
        // Não re-lança - transação será commitada
    }
}
```

### 5. **Evite Operações de I/O Dentro de Transações**

```java
// ✅ BOM: I/O fora da transação
public void processarPedidoComEmail(PedidoDTO pedido) {
    // 1. Primeiro, salva os dados
    Long pedidoId = salvarPedido(pedido); // Método transacional
    
    // 2. Depois, envia email (fora da transação)
    emailService.enviarConfirmacao(pedido.getEmailCliente(), pedidoId);
}

@Transactional
private Long salvarPedido(PedidoDTO pedido) {
    return pedidoRepository.save(pedido);
}
```

***

## Anti-Patterns e Problemas Comuns

### 1. **Deadlock por Ordem de Acesso a Recursos**

#### ❌ PROBLEMA: Diferentes ordens de acesso

```java
// Transação A
@Transactional
public void transferirSaldo(Long contaOrigemId, Long contaDestinoId, BigDecimal valor) {
    // Acessa conta origem primeiro
    Conta origem = contaRepository.findByPK(contaOrigemId);
    origem.debitar(valor);
    
    // Depois acessa conta destino
    Conta destino = contaRepository.findByPK(contaDestinoId);
    destino.creditar(valor);
}

// Transação B executando simultaneamente com origem/destino invertidos
// DEADLOCK: A espera B liberar conta destino, B espera A liberar conta origem
```

#### ✅ SOLUÇÃO: Ordem consistente de acesso

```java
@Transactional
public void transferirSaldo(Long contaOrigemId, Long contaDestinoId, BigDecimal valor) {
    // Sempre acessa contas na mesma ordem (por ID crescente)
    Long menorId = Math.min(contaOrigemId, contaDestinoId);
    Long maiorId = Math.max(contaOrigemId, contaDestinoId);
    
    Conta conta1 = contaRepository.findByPK(menorId);
    Conta conta2 = contaRepository.findByPK(maiorId);
    
    // Determina qual é origem e qual é destino
    Conta origem = (conta1.getId().equals(contaOrigemId)) ? conta1 : conta2;
    Conta destino = (conta1.getId().equals(contaDestinoId)) ? conta1 : conta2;
    
    origem.debitar(valor);
    destino.creditar(valor);
}
```

### 2. **Lock de Transações Aninhadas com REQUIRES\_NEW**

#### ❌ PROBLEMA: Transação aninhada acessa mesmo registro

```java
@Service(serviceName = "ProblemaLockServiceSP")
public class ProblemaLockService {
    
    @Transactional
    public void atualizarProdutoComLog(Long produtoId, String novoNome) {
        // Transação PRINCIPAL bloqueia o produto
        Produto produto = produtoRepository.findByPK(produtoId);
        produto.setNome(novoNome);
        produtoRepository.update(produto); // LOCK no produto
        
        // Chama método que cria NOVA transação
        registrarAlteracaoProduto(produtoId, novoNome);
        // PROBLEMA: Nova transação tenta acessar o mesmo produto que está bloqueado!
    }
    
    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public void registrarAlteracaoProduto(Long produtoId, String novoNome) {
        // DEADLOCK: Tenta acessar produto já bloqueado pela transação principal
        Produto produto = produtoRepository.findByPK(produtoId); // TRAVA AQUI!
        
        LogAlteracao log = new LogAlteracao();
        log.setProdutoId(produtoId);
        log.setDescricao("Nome alterado para: " + novoNome);
        logRepository.save(log);
    }
}
```

**Por que trava?**

1. A transação principal obtém um **lock exclusivo** no registro do produto
2. A nova transação (`REQUIRES_NEW`) tenta acessar o **mesmo registro**
3. Como são transações **separadas**, a nova transação não consegue acessar o registro bloqueado
4. A transação principal não pode prosseguir até a nova transação terminar
5. A nova transação não pode terminar porque não consegue acessar o registro
6. **DEADLOCK!**

#### ✅ SOLUÇÃO: Evitar acesso ao mesmo registro

```java
@Service(serviceName = "SolucaoLockServiceSP")
public class SolucaoLockService {
    
    @Transactional
    public void atualizarProdutoComLog(Long produtoId, String novoNome) {
        // Obtém dados ANTES de alterar
        Produto produto = produtoRepository.findByPK(produtoId);
        String nomeAntigo = produto.getNome();
        
        // Atualiza o produto
        produto.setNome(novoNome);
        produtoRepository.update(produto);
        
        // Registra log SEM acessar o produto novamente
        registrarAlteracaoProduto(produtoId, nomeAntigo, novoNome);
    }
    
    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public void registrarAlteracaoProduto(Long produtoId, String nomeAntigo, String novoNome) {
        // NÃO acessa o produto - usa apenas os parâmetros
        LogAlteracao log = new LogAlteracao();
        log.setProdutoId(produtoId);
        log.setDescricao("Nome alterado de '" + nomeAntigo + "' para '" + novoNome + "'");
        logRepository.save(log);
    }
}
```

### 3. **Transações Muito Longas**

#### ❌ PROBLEMA: Operações lentas dentro da transação

```java
@Transactional
public void processarRelatorioComBanco(List<Long> pedidoIds) {
    for (Long pedidoId : pedidoIds) {
        Pedido pedido = pedidoRepository.findByPK(pedidoId);
        
        // PROBLEMA: Operação lenta dentro da transação
        RelatorioCompleto relatorio = gerarRelatorioCompleto(pedido); // 30 segundos!
        
        pedido.setRelatorio(relatorio);
        pedidoRepository.update(pedido);
    }
    // Transação mantém locks por muito tempo!
}
```

#### ✅ SOLUÇÃO: Separar operações lentas

```java
public void processarRelatorioComBanco(List<Long> pedidoIds) {
    for (Long pedidoId : pedidoIds) {
        // 1. Busca dados em transação rápida
        Pedido pedido = buscarPedido(pedidoId);
        
        // 2. Gera relatório FORA da transação
        RelatorioCompleto relatorio = gerarRelatorioCompleto(pedido);
        
        // 3. Salva resultado em transação rápida
        salvarRelatorio(pedidoId, relatorio);
    }
}

@Transactional(readOnly = true)
private Pedido buscarPedido(Long pedidoId) {
    return pedidoRepository.findByPK(pedidoId);
}

@Transactional
private void salvarRelatorio(Long pedidoId, RelatorioCompleto relatorio) {
    Pedido pedido = pedidoRepository.findByPK(pedidoId);
    pedido.setRelatorio(relatorio);
    pedidoRepository.update(pedido);
}
```

### 4. **Chamadas a Serviços Externos em Transações**

#### ❌ PROBLEMA: Serviço externo lento

```java
@Transactional
public void processarPagamento(PagamentoDTO pagamento) {
    // Salva dados locais
    pagamentoRepository.save(pagamento);
    
    // PROBLEMA: Chama serviço externo dentro da transação
    ResponseEntity<String> response = restTemplate.postForEntity(
        "https://api-externa.com/pagamento", pagamento, String.class);
    // Se a API demorar 60 segundos, a transação fica aberta por 60 segundos!
    
    if (response.getStatusCode().is2xxSuccessful()) {
        pagamento.setStatus(StatusPagamento.APROVADO);
    } else {
        throw new PagamentoRecusadoException("Pagamento recusado");
    }
}
```

#### ✅ SOLUÇÃO: Padrão Saga ou processamento assíncrono

```java
@Transactional
public void iniciarProcessamentoPagamento(PagamentoDTO pagamento) {
    // Salva com status pendente
    pagamento.setStatus(StatusPagamento.PENDENTE);
    pagamentoRepository.save(pagamento);
    
    // Agenda processamento assíncrono
    pagamentoAsyncService.processarPagamentoAsync(pagamento.getId());
}

@Async
public void processarPagamentoAsync(Long pagamentoId) {
    try {
        // Chama serviço externo FORA da transação principal
        ResponseEntity<String> response = restTemplate.postForEntity(
            "https://api-externa.com/pagamento", pagamento, String.class);
        
        // Atualiza resultado em nova transação rápida
        atualizarStatusPagamento(pagamentoId, 
            response.getStatusCode().is2xxSuccessful() 
                ? StatusPagamento.APROVADO 
                : StatusPagamento.RECUSADO);
                
    } catch (Exception e) {
        atualizarStatusPagamento(pagamentoId, StatusPagamento.ERRO);
    }
}

@Transactional
private void atualizarStatusPagamento(Long pagamentoId, StatusPagamento status) {
    Pagamento pagamento = pagamentoRepository.findByPK(pagamentoId);
    pagamento.setStatus(status);
    pagamentoRepository.update(pagamento);
}
```

***

## Resumo das Melhores Práticas

### ✅ **O que FAZER:**

* Manter transações **curtas e focadas**
* Usar `REQUIRES_NEW` para **operações independentes** (logs, auditoria)
* **Ordenar acesso** a recursos para evitar deadlocks
* Tratar exceções adequadamente (**RuntimeException** causa rollback automaticamente)
* Separar **operações lentas** (I/O, serviços externos) das transações
* Aplicar transações na **camada de serviço**

### ❌ **O que NÃO fazer:**

* **Não** acessar o mesmo registro em transações aninhadas com `REQUIRES_NEW`
* **Não** manter transações abertas por muito tempo
* **Não** chamar serviços externos dentro de transações
* **Não** usar transações para operações de **apenas leitura simples**
* **Não** ignorar o tratamento adequado de exceções

O controle transacional no SDK Sankhya oferece uma base sólida para garantir a integridade dos dados, mas deve ser usado com conhecimento das suas implicações e limitações para evitar problemas de performance e deadlocks.
