---
id: "https://developer.sankhya.com.br/docs/guia-de-boas-praticas"
titulo: "Guia de Boas Práticas para Desenvolvimento de Add-ons"
url: "https://developer.sankhya.com.br/docs/guia-de-boas-praticas"
atualizado_em: "2026-04-15T01:55:39.000Z"
---

# Guia de Boas Práticas para Desenvolvimento de Add-ons

<br />

# Boas Práticas para Desenvolvimento de Add-ons Sankhya

## Introdução

Este guia fornece diretrizes essenciais para o desenvolvimento de add-ons de **qualidade profissional** dentro do ecossistema Sankhya Studio.

**Público-alvo**: Desenvolvedores Java que criam extensões para o ERP Sankhya utilizando o framework Sankhya Studio.

**Benefícios de seguir este guia**:

* 💡 Add-ons **eficientes** e com melhor performance
* 💡 Código **seguro** e robusto contra falhas
* 💡 Aplicações **escaláveis** que suportam crescimento
* 💡 **Facilidade de manutenção** e evolução
* 💡 **Compatibilidade** com futuras atualizações do sistema
* 💡 **Melhor experiência** para os usuários finais

## Sumário

1. [Estruturação e Modelagem de Dados](#estruturação-e-modelagem-de-dados)
2. [Desenvolvimento de Código](#desenvolvimento-de-código)
3. [Organização do Código e Arquitetura](#organização-do-código-e-arquitetura)
4. [Logging e Tratamento de Exceções](#logging-e-tratamento-de-exceções)
5. [Transações e Consistência de Dados](#transações-e-consistência-de-dados)
6. [Performance e Otimização](#performance-e-otimização)
7. [Segurança](#segurança)
8. [Testes e Qualidade](#testes-e-qualidade)
9. [Gestão de Recursos e Dependências](#gestão-de-recursos-e-dependências)
10. [Versionamento e Deploy](#versionamento-e-deploy)

## Estruturação e Modelagem de Dados

### Tabelas e Campos

* **Não criar campos com valor default em tabelas nativas**: O sistema possui mecanismos que irão atuar no processo de instalação do Addon, causando falhas e impedindo a atualização correta do addon.

* **Use prefixos únicos**: Sempre utilize um prefixo exclusivo para tabelas e campos customizados
  ```xml
  <!-- ? BOM: Prefixo único -->
  <table name="MKT_CAMPANHA">
      <field name="MKT_CODCAMPANHA" />
      <field name="MKT_DESCRICAO" />
  </table>

  <!-- ? RUIM: Sem prefixo ou prefixo genérico -->
  <table name="CAMPANHA">
      <field name="CODIGO" />
  </table>
  ```

* **NUNCA use o prefixo `AD_`**: Este prefixo é reservado para uso interno do sistema Sankhya

* **Normalize adequadamente**: Evite redundância de dados, mas equilibre com performance
  * **3ª Forma Normal** é geralmente suficiente para a maioria dos casos
  * Desnormalização controlada pode ser aceitável para relatórios complexos

* **Tipos de dados apropriados**:
  * Use `BigDecimal` para valores monetários e numéricos de precisão
  * Use `Long` para chaves primárias numéricas
  * Use `LocalDate` e `LocalDateTime` para datas
  * Evite tipos primitivos em entidades JPA

### Relacionamentos e Integridade

* **Defina chaves estrangeiras**: Garanta integridade referencial no banco de dados
* **Use índices estrategicamente**: Campos frequentemente usados em WHERE e JOINs
* **Considere o impacto em cascata**: Operações de DELETE e UPDATE em relacionamentos

### Extensão de Tabelas Nativas

```xml
<!-- ? BOM: Extensão de tabela nativa -->
<nativeTable name="TGFCAB">
    <field name="MKT_CAMPANHAVINCULADA" type="NUMBER(10)" />
    <field name="MKT_OBSERVACOES" type="VARCHAR2(500)" />
</nativeTable>

<!-- ? RUIM: Criar tabela separada para campos simples -->
<table name="MKT_CAB_EXTRA">
    <field name="NUNOTA" />
    <field name="MKT_CAMPANHAVINCULADA" />
</table>
```

## Desenvolvimento de Código

### Gestão de Estado e Variáveis

* **Não criar variáveis globais (static) em serviços**: Services são singletons gerenciados pelo container EJB. Variáveis de instância podem causar:
  * **Race conditions** em ambientes multi-thread
  * **Memory leaks** se não gerenciadas corretamente
  * **Efeitos colaterais** entre diferentes requisições

```java
// ? PÉSSIMO: Variável de instância em Service
@Service(serviceName = "PedidoService")
public class PedidoService {
    private Long ultimoPedidoProcessado; // NUNCA faça isso!
    
    public void processar(Long numeroPedido) {
        this.ultimoPedidoProcessado = numeroPedido; // Estado compartilhado!
    }
}

// ? BOM: Variáveis locais ou parâmetros
@Service(serviceName = "PedidoService")
public class PedidoService {
    private static final Logger logger = Logger.getLogger(PedidoService.class);
    
    @Inject
    private PedidoRepository repository; // Injeção de dependência OK
    
    public void processar(Long numeroPedido) {
        Long pedidoAtual = numeroPedido; // Variável local - thread-safe
        // ...
    }
}
```

### Nomenclatura e Prefixos

* **Utilizar prefixo em objetos do Add-on** para evitar conflitos:
  * **JNDI Names** (Serviços, Jobs): `com.empresa.addon.MeuService`
  * **Instâncias**: `MeuAddonInstancia`
  * **Campos**: `MAD_CAMPO` (prefixo único de 2-4 letras)
  * **Tabelas**: `MAD_TABELA`

```java
// ? BOM: Nomenclatura com prefixo
@Service(serviceName = "com.minhaempresa.financeiro.CobrancaService")
public class CobrancaService {
    // ...
}

// ? RUIM: Nome genérico sem prefixo
@Service(serviceName = "CobrancaService") // Pode conflitar!
public class CobrancaService {
    // ...
}
```

### Isolamento de Código

* **Não misture componentes de módulo Java e Addon**:
  * Add-ons rodam de forma **isolada** do sistema nas versões mais recentes
  * Personalizações desenvolvidas no ERP **não** funcionam utilizando recursos do Addon
  * Cada Add-on tem seu próprio **ClassLoader**

```java
// ? RUIM: Tentar acessar classes do módulo customizado
import br.com.empresa.custom.MinhaClassePersonalizada; // Não funciona!

// ? BOM: Use apenas APIs públicas do Sankhya ou do seu próprio Add-on
import br.com.sankhya.jape.EntityFacade;
import com.meuaddon.service.MinhaClasseDoAddon;
```

### Null Safety

* **Sempre verifique nulls** antes de acessar métodos ou propriedades
* **Use Optional** quando apropriado (Java 8+)
* **Valide parâmetros** no início dos métodos

```java
// ? BOM: Verificação de null
public void processarPedido(Pedido pedido) {
    if (pedido == null) {
        throw new IllegalArgumentException("Pedido não pode ser nulo");
    }
    
    if (pedido.getItens() == null || pedido.getItens().isEmpty()) {
        throw new ValidationException("Pedido deve conter itens");
    }
    
    // Processamento seguro
}

// ? BOM: Usando Optional
public Optional<Parceiro> buscarParceiroPorCodigo(Long codigo) {
    return repository.findByPK(codigo);
}

// Uso
buscarParceiroPorCodigo(123L)
    .ifPresent(parceiro -> logger.info("Parceiro encontrado: " + parceiro.getNome()));
```

## Organização do Código e Arquitetura

* **Mantenha o Add-on pequeno**:
  * Evitar dependências desnecessárias.
  * Utilizar técnicas para minimizar o tamanho do pacote.
  * Evitar bibliotecas externas pesadas.
* **Assinatura do projeto**:
  * Utilizar a chave da Área do Desenvolvedor para garantir a integridade do projeto.
* **Utilizar boas práticas de engenharia de software**:
  * Clean Code: Código legível, modular e bem estruturado.
  * Padrões de projeto: Aplicar padrões adequados ao contexto.
  * Reaproveitamento de código: Criar bibliotecas reutilizáveis.
  * Alta coesão: Evitar classes monolíticas, que fazem tudo.
  * **MVC**:
    * Projetos já são separados em `-model` e `-vc`.
    * No `-model`, implementar regras de negócio.
    * No `-vc`, implementar a interface de usuário (camada web).

## Logging e Tratamento de Exceções

### Frameworks de Log Suportados

* **Log4j**: Framework recomendado para logging no Sankhya Studio
* **JUL (java.util.logging)**: Suportado como alternativa

### Configuração do Logger

```java
import org.apache.log4j.Logger;

public class MeuServico {
    private static final Logger logger = Logger.getLogger(MeuServico.class);
    
    // Ou usando JUL
    // private static final Logger logger = Logger.getLogger(MeuServico.class.getName());
}
```

### Níveis de Log e Quando Usar

* **TRACE/FINEST**: Informações extremamente detalhadas para diagnóstico profundo
  * Uso: Debugging de fluxos complexos, rastreamento de valores de variáveis
  * **Nunca** usar em produção - apenas em desenvolvimento
* **DEBUG/FINE**: Informações detalhadas para diagnóstico
  * Entrada e saída de métodos importantes
  * Valores de parâmetros relevantes
  * Fluxo de execução em lógicas complexas
  * Exemplo: `logger.debug("Processando pedido: " + numeroPedido);`
* **INFO**: Eventos importantes do ciclo de vida da aplicação
  * Início e fim de operações significativas
  * Mudanças de estado importantes
  * Confirmações de operações bem-sucedidas
  * Exemplo: `logger.info("Pedido " + numeroPedido + " confirmado com sucesso");`
* **WARN/WARNING**: Situações anormais que não impedem o funcionamento
  * Uso de valores default por falta de configuração
  * Recursos não encontrados mas com fallback
  * Operações lentas ou timeouts parciais
  * Exemplo: `logger.warn("Parâmetro não configurado, usando valor default: " + valorDefault);`
* **ERROR/SEVERE**: Erros que impedem uma operação específica
  * Exceções capturadas que afetam o usuário
  * Falhas em operações críticas
  * Sempre incluir a exceção completa
  * Exemplo: `logger.error("Erro ao processar pedido: " + numeroPedido, exception);`

### Quando Capturar Exceções

**? CAPTURE quando:**

* Você pode **tratar** a exceção e a aplicação pode continuar
* Você precisa **adicionar contexto** antes de relançar
* Você precisa **executar cleanup** (fechar recursos, rollback)
* É uma **camada de integração** (API externa, banco de dados)

```java
@Service
public class PedidoService {
    private static final Logger logger = Logger.getLogger(PedidoService.class);
    
    public void confirmarPedido(Long numeroPedido) {
        try {
            // Lógica de confirmação
            pedidoRepository.confirmar(numeroPedido);
            logger.info("Pedido " + numeroPedido + " confirmado");
        } catch (DataIntegrityException e) {
            // Adiciona contexto e relança
            logger.error("Erro de integridade ao confirmar pedido: " + numeroPedido, e);
            throw new BusinessException("Não foi possível confirmar o pedido. Verifique os dados.", e);
        } catch (Exception e) {
            // Tratamento genérico com log
            logger.error("Erro inesperado ao confirmar pedido: " + numeroPedido, e);
            throw new BusinessException("Erro ao confirmar pedido", e);
        }
    }
}
```

**? NÃO CAPTURE quando:**

* Você não sabe como tratar
* Só para logar e relançar (use throws ou deixe propagar)
* Em camadas baixas sem contexto de negócio

### Quando Lançar Exceções

**? LANCE quando:**

* Detectar **violação de regra de negócio**
* Encontrar **estado inconsistente** dos dados
* Receber **parâmetros inválidos** (validação)
* Encontrar **condições que impedem** a continuação

```java
@Component
public class PedidoBusiness {
    private static final Logger logger = Logger.getLogger(PedidoBusiness.class);
    
    public void validarPedido(Pedido pedido) {
        if (pedido.getItens().isEmpty()) {
            logger.warn("Tentativa de criar pedido sem itens: " + pedido.getId());
            throw new ValidationException("Pedido deve ter pelo menos um item");
        }
        
        if (pedido.getValorTotal().compareTo(BigDecimal.ZERO) <= 0) {
            logger.warn("Tentativa de criar pedido com valor inválido: " + pedido.getValorTotal());
            throw new ValidationException("Valor do pedido deve ser maior que zero");
        }
    }
}
```

### Anti-Patterns de Logging

**? Evitar:**

```java
// NÃO: Capturar e não fazer nada (swallow exception)
try {
    operacao();
} catch (Exception e) {
    // Silenciosamente ignora
}

// NÃO: Log sem a exceção completa
catch (Exception e) {
    logger.error("Erro: " + e.getMessage()); // Perde o stack trace!
}

// NÃO: Logar e relançar sem adicionar contexto
catch (Exception e) {
    logger.error("Erro", e);
    throw e; // Duplica logs desnecessariamente
}

// NÃO: Log excessivo em loops
for (Item item : itens) {
    logger.debug("Processando item: " + item.getId()); // Pode gerar milhares de logs
}

// NÃO: Concatenação custosa sem verificação de nível
logger.debug("Processando: " + objetoComplexo.toString()); 
// toString() é executado MESMO se DEBUG estiver desabilitado!

// NÃO: Concatenar objetos grandes implicitamente
logger.debug("Pedido: " + pedidoComMuitosItens); 
// toString() de toda a estrutura é chamado e descartado

// NÃO: Concatenar coleções grandes
logger.debug("Lista de notas: " + listaComMilharesDeNotas);
// Chama toString() de CADA elemento da lista = desperdício MASSIVO

// NÃO: Múltiplas concatenações em uma linha
logger.debug("Dados: " + obj1 + ", " + obj2 + ", " + obj3 + ", " + obj4);
// Cria 4+ objetos String temporários na heap
```

**? Fazer:**

```java
// SIM: Capturar, logar e tratar adequadamente
try {
    operacao();
} catch (RecursoNaoEncontradoException e) {
    logger.warn("Recurso não encontrado, usando fallback: " + e.getMessage());
    return valorPadrao;
}

// SIM: Log com exceção completa
catch (Exception e) {
    logger.error("Erro ao processar operação", e); // Inclui stack trace
}

// SIM: Adicionar contexto antes de relançar
catch (SQLException e) {
    logger.error("Erro ao acessar tabela TGFCAB para nota: " + numeroNota, e);
    throw new DataAccessException("Erro ao buscar nota fiscal", e);
}

// SIM: Verificar nível antes de operações custosas
if (logger.isDebugEnabled()) {
    logger.debug("Processando: " + objetoComplexo.gerarDescricaoCompleta());
}

// SIM: Logar apenas dados essenciais, não o objeto completo
if (logger.isDebugEnabled()) {
    logger.debug("Pedido: " + pedido.getNumero() + ", itens: " + pedido.getItens().size());
    // Ao invés de: logger.debug("Pedido: " + pedido.toString());
}

// SIM: Para coleções, logar tamanho e amostra
if (logger.isDebugEnabled()) {
    logger.debug("Processando " + notas.size() + " notas. Primeira: " + notas.get(0).getNumero());
    // Ao invés de: logger.debug("Notas: " + notas);
}

// SIM: Log resumido para operações em lote
logger.info("Processando lote de " + itens.size() + " itens");
try {
    // processa itens
    logger.info("Lote processado com sucesso: " + itensProcessados + "/" + itens.size());
} catch (Exception e) {
    logger.error("Erro ao processar lote no item " + indiceAtual, e);
}

// SIM: Use StringBuilder para concatenações complexas dentro do if
if (logger.isDebugEnabled()) {
    StringBuilder sb = new StringBuilder("Resumo do pedido: ");
    sb.append("numero=").append(pedido.getNumero());
    sb.append(", parceiro=").append(pedido.getCodigoParceiro());
    sb.append(", valor=").append(pedido.getValorTotal());
    logger.debug(sb.toString());
}
```

### Problema de Concatenação em Logs e Consumo de Memória

**?? ATENÇÃO: Concatenação de strings em logs é executada ANTES da verificação do nível de log!**

Quando você escreve:

```java
logger.debug("Processando pedido: " + pedido.toString());
```

O que acontece:

1. O método `pedido.toString()` é **SEMPRE executado**
2. A concatenação de strings cria **novos objetos String na memória**
3. **DEPOIS** o framework verifica se DEBUG está habilitado
4. Se DEBUG estiver desabilitado, todo esse processamento foi **desperdício**

#### Impacto no Consumo de Memória

```java
// ? PÉSSIMO: Consome memória mesmo com DEBUG desabilitado
logger.debug("Dados: " + objeto1 + ", " + objeto2 + ", " + objeto3);
// Resultado: 4+ objetos String criados na heap, mesmo que o log não seja escrito!

// ? MUITO PIOR: toString() de objeto grande
logger.debug("Pedido completo: " + pedidoComMilharesDeItens.toString());
// toString() gera uma String gigante (ex: 500KB) que será descartada se DEBUG estiver OFF!

// ? CRÍTICO: Loop com concatenação
for (Pedido pedido : listaDe10000Pedidos) {
    logger.debug("Processando: " + pedido.toString()); // 10.000 Strings criadas!
}
// Pode facilmente consumir dezenas de MB de memória e causar Garbage Collection frequente
```

#### Soluções para Evitar Desperdício de Memória

**? Solução 1: Verificar nível de log antes de concatenar**

```java
if (logger.isDebugEnabled()) {
    logger.debug("Processando pedido: " + pedido.toString());
}
// toString() só é chamado se DEBUG estiver habilitado
```

**? Solução 2: Usar formatação com placeholders (recomendado para SLF4J)**

```java
// Se estiver usando SLF4J (mais moderno que Log4j)
logger.debug("Processando pedido: {}, parceiro: {}", pedido, codigoParceiro);
// Objetos só são convertidos para String se o log for realmente escrito
```

**? Solução 3: Criar métodos de log inteligentes**

```java
private void logDebug(String mensagem, Object... args) {
    if (logger.isDebugEnabled()) {
        logger.debug(String.format(mensagem, args));
    }
}

// Uso
logDebug("Processando pedido %s com %d itens", pedido.getNumero(), pedido.getItens().size());
```

#### Exemplos de Consumo de Memória

```java
// Cenário: 1000 iterações com log DEBUG desabilitado

// ? RUIM: ~2MB de lixo criado
for (int i = 0; i < 1000; i++) {
    logger.debug("Iteração: " + i + ", objeto: " + objetoGrande.toString());
}

// ? BOM: ~0 bytes de lixo
for (int i = 0; i < 1000; i++) {
    if (logger.isDebugEnabled()) {
        logger.debug("Iteração: " + i + ", objeto: " + objetoGrande.toString());
    }
}
```

#### Armadilhas com toString() Implícito

```java
// ? toString() é chamado IMPLICITAMENTE na concatenação
logger.debug("Pedido: " + pedido); // Equivale a: pedido.toString()

// ? PIOR: Coleções chamam toString() de CADA elemento
logger.debug("Itens: " + pedido.getItens()); 
// Se tiver 1000 itens, chama 1000x toString() + concatenação da lista!

// ? MELHOR: Logar apenas informações essenciais
if (logger.isDebugEnabled()) {
    logger.debug("Pedido: " + pedido.getNumero() + " com " + pedido.getItens().size() + " itens");
}

// ? IDEAL: Criar toString() lazy só para debug
if (logger.isDebugEnabled()) {
    logger.debug("Pedido: " + pedido.toDebugString()); // Método customizado
}
```

### Boas Práticas de Logging

1. **Use níveis apropriados**: Não abuse de ERROR, use WARN quando apropriado
2. **Inclua contexto**: IDs, nomes de entidades, valores relevantes
3. **Seja consistente**: Mantenha padrão de mensagens similar em todo o código
4. **Evite informações sensíveis**: Nunca logue senhas, tokens, dados pessoais completos
5. **Use mensagens claras**: Prefira "Pedido 12345 não encontrado" ao invés de "Erro no pedido"
6. **Log em português**: Mantenha consistência com o sistema Sankhya
7. **Sempre logue a exceção**: Use `logger.error("mensagem", exception)` ao invés de apenas `e.getMessage()`
8. **Performance e Memória**:
   * **SEMPRE** verifique `isDebugEnabled()` antes de concatenações custosas
   * **NUNCA** concatene objetos grandes diretamente no parâmetro do log
   * **EVITE** concatenação em loops - use log resumido
   * Lembre-se: **concatenação é executada ANTES da verificação do nível de log**

### Exemplo Completo de Boas Práticas

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoService {
    private static final Logger logger = Logger.getLogger(PedidoService.class);
    
    @Inject
    private PedidoRepository repository;
    
    @Inject
    private PedidoBusiness business;
    
    @Transactional
    public PedidoDTO criarPedido(@Valid CriarPedidoRequestDTO request) {
        // ? BOM: Concatenação simples com primitivos/wrappers (baixo custo)
        logger.info("Iniciando criação de pedido para parceiro: " + request.getCodigoParceiro());
        
        try {
            // Validação
            validarRequest(request);
            
            // Lógica de negócio
            Pedido pedido = business.montarPedido(request);
            pedido = repository.save(pedido);
            
            // ? BOM: Log com informação essencial
            logger.info("Pedido criado com sucesso: " + pedido.getNumero());
            
            // ? EXCELENTE: Verificação antes de operação custosa
            if (logger.isDebugEnabled()) {
                // toString() customizado só é executado se DEBUG estiver ON
                logger.debug("Detalhes do pedido: " + pedido.toDebugString());
            }
            
            return mapearParaDTO(pedido);
            
        } catch (ValidationException e) {
            // ? BOM: WARN para erros esperados (validação)
            logger.warn("Validação falhou ao criar pedido: " + e.getMessage());
            throw e; // Relança sem logar como ERROR
        } catch (DataIntegrityException e) {
            // ? BOM: ERROR com contexto + exceção completa
            logger.error("Erro de integridade ao criar pedido para parceiro: " + request.getCodigoParceiro(), e);
            throw new BusinessException("Erro ao salvar pedido. Verifique os dados e tente novamente.", e);
        } catch (Exception e) {
            // ? BOM: ERROR para exceções inesperadas
            logger.error("Erro inesperado ao criar pedido para parceiro: " + request.getCodigoParceiro(), e);
            throw new BusinessException("Erro ao criar pedido", e);
        }
    }
    
    @Transactional
    public void processarLotePedidos(List<Long> numerosPedidos) {
        // ? EXCELENTE: Log resumido para lotes
        logger.info("Iniciando processamento de lote com " + numerosPedidos.size() + " pedidos");
        
        int sucesso = 0;
        int erros = 0;
        
        for (Long numero : numerosPedidos) {
            try {
                business.processarPedido(numero);
                sucesso++;
                
                // ? PÉSSIMO: Não faça isso em loop!
                // logger.debug("Pedido processado: " + numero);
                
                // ? BOM: Log a cada N iterações ou apenas totais
                if (logger.isDebugEnabled() && sucesso % 100 == 0) {
                    logger.debug("Progresso: " + sucesso + " pedidos processados");
                }
                
            } catch (Exception e) {
                erros++;
                // ? BOM: Log de erro com contexto específico
                logger.error("Erro ao processar pedido: " + numero, e);
            }
        }
        
        // ? EXCELENTE: Log resumido ao final
        logger.info("Lote processado. Sucesso: " + sucesso + ", Erros: " + erros);
    }
    
    private void validarRequest(CriarPedidoRequestDTO request) {
        if (request.getItens() == null || request.getItens().isEmpty()) {
            throw new ValidationException("Pedido deve conter pelo menos um item");
        }
        
        // ? BOM: Logar tamanho da coleção, não a coleção inteira
        if (logger.isDebugEnabled()) {
            logger.debug("Validando pedido com " + request.getItens().size() + " itens");
            // ? NUNCA: logger.debug("Validando pedido: " + request);
        }
    }
}

/**
 * Exemplo de entidade com toString() otimizado
 */
@JapeEntity(entity = "Pedido", table = "TGFPED")
public class Pedido {
    private Long numero;
    private Long codigoParceiro;
    private BigDecimal valorTotal;
    private List<ItemPedido> itens; // Pode ter centenas/milhares de itens
    
    // ? PÉSSIMO: toString() padrão que percorre TODOS os itens
    // @Override
    // public String toString() {
    //     return "Pedido{numero=" + numero + ", itens=" + itens + "}";
    // }
    
    // ? BOM: toString() leve para uso geral
    @Override
    public String toString() {
        return "Pedido{numero=" + numero + ", parceiro=" + codigoParceiro + 
               ", itens=" + (itens != null ? itens.size() : 0) + "}";
    }
    
    // ? EXCELENTE: Método específico para debug detalhado
    public String toDebugString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Pedido{numero=").append(numero);
        sb.append(", parceiro=").append(codigoParceiro);
        sb.append(", valor=").append(valorTotal);
        sb.append(", qtdItens=").append(itens != null ? itens.size() : 0);
        
        if (itens != null && !itens.isEmpty()) {
            sb.append(", primeiroItem=").append(itens.get(0).getCodigoProduto());
        }
        sb.append("}");
        
        return sb.toString();
    }
}
```

## Transações e Consistência de Dados

### Gerenciamento de Transações

* **Use @Transactional** para operações que modificam dados
* **Entenda os tipos de transação**:
  * `AUTOMATIC` (padrão): Framework gerencia a transação
  * `REQUIRES_NEW`: Sempre cria uma nova transação (use com cuidado)
  * `NOT_SUPPORTED`: Executa fora de transação

```java
// ? BOM: Transação para operações de escrita
@Service(serviceName = "PedidoService")
public class PedidoService {
    
    @Transactional
    public void confirmarPedido(Long numeroPedido) {
        Pedido pedido = repository.findByPK(numeroPedido)
            .orElseThrow(() -> new NotFoundException("Pedido não encontrado"));
        
        pedido.setStatus("CONFIRMADO");
        repository.save(pedido);
        
        // Se houver exceção, rollback automático
    }
    
    // ? BOM: Leitura pode não precisar de transação
    public PedidoDTO buscarPedido(Long numeroPedido) {
        return repository.findByPK(numeroPedido)
            .map(this::mapearParaDTO)
            .orElse(null);
    }
}
```

### Consistência de Dados

* **Evite transações longas**: Podem causar locks e deadlocks
* **Use locking otimista** quando possível: `@Version` em entidades JPA
* **Validações em múltiplas camadas**:
  * Validação de entrada (DTO com Bean Validation)
  * Validação de regras de negócio (Business layer)
  * Constraints no banco de dados

```java
// ? BOM: Validação em camadas
@Service
public class PedidoService {
    
    @Transactional
    public PedidoDTO criarPedido(@Valid CriarPedidoRequestDTO request) {
        // 1. Validação Bean Validation automática via @Valid
        
        // 2. Validação de regras de negócio
        validarRegrasNegocio(request);
        
        // 3. Persistência (constraints do BD validam integridade)
        Pedido pedido = montarPedido(request);
        return repository.save(pedido);
    }
    
    private void validarRegrasNegocio(CriarPedidoRequestDTO request) {
        if (request.getValorTotal().compareTo(BigDecimal.ZERO) <= 0) {
            throw new BusinessException("Valor total deve ser maior que zero");
        }
    }
}
```

## Performance e Otimização

### Queries e Acesso a Dados

* **Evite N+1 queries**: Use JOINs ou fetch strategies adequadas
* **Use paginação** para grandes volumes de dados
* **Crie índices** em campos usados em WHERE, ORDER BY, e JOINs
* **Evite SELECT** \*: Busque apenas os campos necessários

```java
// ? RUIM: N+1 queries
List<Pedido> pedidos = repository.findAll(); // 1 query
for (Pedido pedido : pedidos) {
    List<Item> itens = pedido.getItens(); // N queries adicionais!
}

// ? BOM: Usar JOIN FETCH
@Repository
public interface PedidoRepository extends JapeRepository<Pedido, Long> {
    
    @Criteria("SELECT p FROM Pedido p JOIN FETCH p.itens WHERE p.status = :status")
    List<Pedido> findByStatusComItens(String status);
}

// ? BOM: Paginação para grandes volumes
@Repository
public interface PedidoRepository extends JapeRepository<Pedido, Long> {
    
    Page<Pedido> findByStatus(String status, Pageable pageable);
}

// Uso
Page<Pedido> pedidos = repository.findByStatus("ATIVO", 
    PageRequest.of(0, 50)); // Página 0, 50 registros
```

### Cache e Reutilização

* **Cache dados estáticos**: Parâmetros, configurações
* **Reutilize conexões**: Não crie conexões desnecessárias
* **Lazy loading** para dados raramente acessados

```java
// ? BOM: Cache de parâmetros
@Component
public class ConfiguracaoService {
    private static final Logger logger = Logger.getLogger(ConfiguracaoService.class);
    
    private final Map<String, String> cacheParametros = new ConcurrentHashMap<>();
    
    public String getParametro(String chave) {
        return cacheParametros.computeIfAbsent(chave, k -> {
            // Busca no banco apenas se não estiver em cache
            return buscarParametroDoBanco(k);
        });
    }
}
```

### Processamento em Lote

* **Agrupe operações** quando possível
* **Use batch processing** para inserções/atualizações em massa
* **Processe assincronamente** tarefas pesadas

```java
// ? BOM: Processamento em lote
@Service
public class PedidoService {
    
    @Transactional
    public void confirmarPedidosEmLote(List<Long> numerosPedidos) {
        // Busca todos de uma vez
        List<Pedido> pedidos = repository.findAllById(numerosPedidos);
        
        // Processa em memória
        pedidos.forEach(pedido -> pedido.setStatus("CONFIRMADO"));
        
        // Salva todos de uma vez (batch)
        repository.saveAll(pedidos);
    }
}
```

## Segurança

### Validação de Entrada

* **SEMPRE valide entrada do usuário**: Nunca confie em dados externos
* **Use Bean Validation**: `@NotNull`, `@NotEmpty`, `@Size`, etc.
* **Sanitize inputs**: Previna SQL Injection e XSS

```java
// ? BOM: DTOs com validação
public class CriarPedidoRequestDTO {
    
    @NotNull(message = "Código do parceiro é obrigatório")
    @Positive(message = "Código do parceiro deve ser positivo")
    private Long codigoParceiro;
    
    @NotEmpty(message = "Pedido deve conter itens")
    @Size(min = 1, max = 1000, message = "Pedido deve ter entre 1 e 1000 itens")
    private List<ItemPedidoDTO> itens;
    
    @NotNull(message = "Valor total é obrigatório")
    @DecimalMin(value = "0.01", message = "Valor total deve ser maior que zero")
    private BigDecimal valorTotal;
}

@Service
public class PedidoService {
    
    public PedidoDTO criar(@Valid CriarPedidoRequestDTO request) {
        // @Valid dispara validações automaticamente
        // Se falhar, lança ConstraintViolationException
    }
}
```

### Controle de Acesso

* **Implemente autorização**: Verifique permissões antes de operações sensíveis
* **Use roles e permissions**: Não hardcode usuários
* **Audit trail**: Registre quem fez o quê e quando

```java
// ? BOM: Verificação de permissão
@Service
public class PedidoService {
    
    @Inject
    private SecurityContext securityContext;
    
    @Transactional
    public void excluirPedido(Long numeroPedido) {
        // Verifica permissão
        if (!securityContext.hasPermission("PEDIDO_EXCLUIR")) {
            throw new SecurityException("Usuário não tem permissão para excluir pedidos");
        }
        
        // Log de auditoria
        logger.info("Pedido " + numeroPedido + " excluído por: " + 
                    securityContext.getCurrentUser());
        
        repository.deleteById(numeroPedido);
    }
}
```

### Proteção de Dados Sensíveis

* **NUNCA logue senhas** ou tokens
* **Criptografe dados sensíveis** em repouso
* **Use HTTPS** para dados em trânsito
* **Mascare dados** em logs e respostas de API

```java
// ? BOM: Mascaramento de dados sensíveis
public class Usuario {
    private String login;
    private String senha; // Nunca logar!
    private String cpf;
    
    public String getCpfMascarado() {
        if (cpf == null || cpf.length() < 11) return "***";
        return cpf.substring(0, 3) + ".***.**" + cpf.substring(9);
    }
    
    @Override
    public String toString() {
        return "Usuario{login='" + login + "', cpf='" + getCpfMascarado() + "'}";
        // Senha NUNCA deve aparecer no toString()!
    }
}
```

## Testes e Qualidade

### Testes Unitários

* **Teste suas regras de negócio**: Alta cobertura em camadas de negócio
* **Use mocks** para dependências externas
* **Nomes descritivos** para testes

```java
// ? BOM: Teste unitário
public class PedidoBusinessTest {
    
    private PedidoBusiness business;
    private PedidoRepository repository;
    
    @Before
    public void setUp() {
        repository = mock(PedidoRepository.class);
        business = new PedidoBusiness(repository);
    }
    
    @Test(expected = ValidationException.class)
    public void deveLancarExcecaoQuandoPedidoSemItens() {
        // Arrange
        Pedido pedido = new Pedido();
        pedido.setItens(new ArrayList<>());
        
        // Act
        business.validarPedido(pedido);
        
        // Assert: exceção esperada
    }
    
    @Test
    public void deveValidarPedidoComItensValidos() {
        // Arrange
        Pedido pedido = new Pedido();
        pedido.setItens(Arrays.asList(new ItemPedido()));
        pedido.setValorTotal(new BigDecimal("100.00"));
        
        // Act & Assert: não deve lançar exceção
        business.validarPedido(pedido);
    }
}
```

### Testes de Integração

* **Teste APIs externas**: Mock ou use ambientes de teste

### Qualidade de Código

* **Code review**: Sempre revise código antes de merge
* **Análise estática**: Use ferramentas como SonarQube, PMD, Checkstyle
* **Formatação consistente**: Use formatadores automáticos
* **Evite code smells**:
  * Métodos muito longos (> 50 linhas)
  * Classes muito grandes (> 500 linhas)
  * Duplicação de código
  * Complexidade ciclomática alta

## Gestão de Recursos e Dependências

### Gerenciamento de Recursos

* **Feche recursos adequadamente**: Use try-with-resources
* **Evite memory leaks**: Limpe referências quando não mais necessário
* **Cuidado com threads**: Use thread pools, não crie threads manualmente

```java
// ? BOM: Try-with-resources
public void processarArquivo(String caminho) {
    try (BufferedReader reader = new BufferedReader(new FileReader(caminho))) {
        String linha;
        while ((linha = reader.readLine()) != null) {
            processar(linha);
        }
    } catch (IOException e) {
        logger.error("Erro ao processar arquivo: " + caminho, e);
        throw new BusinessException("Erro ao processar arquivo", e);
    }
    // Reader é fechado automaticamente
}
```

### Dependências

* **Mantenha Add-on pequeno**: Evite dependências desnecessárias
* **Versione dependências**: Use versões específicas, não ranges
* **Verifique licenças**: Garanta compatibilidade de licenças
* **Evite bibliotecas pesadas**: Prefira alternativas leves

```gradle
// ? BOM: Dependências versionadas e necessárias
dependencies {
    implementation 'br.com.sankhya:jape:4.32'
    implementation 'com.google.code.gson:gson:2.8.9'
    
    // ? EVITE: Dependências muito pesadas
    // implementation 'org.springframework.boot:spring-boot-starter:2.7.0'
}
```

### Configuração e Parâmetros

* **Externalize configurações**: Não hardcode valores
* **Use parâmetros do sistema**: Torne comportamento configurável
* **Documente parâmetros**: Explique o que cada um faz

```java
// ? BOM: Configuração externalizada
@Component
public class ConfiguracaoService {
    
    public int getTimeoutIntegracao() {
        return getParametroInt("ADDON_TIMEOUT_INTEGRACAO", 30000); // Default 30s
    }
    
    public boolean isEnvioEmailHabilitado() {
        return getParametroBoolean("ADDON_ENVIO_EMAIL", true);
    }
    
    private int getParametroInt(String chave, int defaultValue) {
        try {
            return MGEParametro.getParametroInt(chave);
        } catch (Exception e) {
            logger.warn("Parâmetro " + chave + " não configurado, usando default: " + defaultValue);
            return defaultValue;
        }
    }
}
```

## Versionamento e Deploy

### Versionamento Semântico

* **Use Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`
  * **MAJOR**: Mudanças incompatíveis com versões anteriores
  * **MINOR**: Novas funcionalidades compatíveis
  * **PATCH**: Correções de bugs compatíveis

```
Exemplos:
1.0.0 -> Release inicial
1.1.0 -> Nova funcionalidade (compatível)
1.1.1 -> Correção de bug
2.0.0 -> Breaking change (incompatível com 1.x)
```

### Versionamento de Componentes

* **Versionar corretamente**:
  * **Código-fonte**: Git com tags de versão
  * **Scripts de banco**: Versionamento incremental (V1, V2, V3...)
  * **Dicionário de dados**: Sincronizado com versão do código
  * **Documentação**: Atualizada a cada release

```xml
<!-- ? BOM: Scripts versionados -->
dbscripts/
  ??? V1__criar_tabelas_iniciais.xml
  ??? V2__adicionar_campo_observacao.xml
  ??? V3__criar_indice_performance.xml
  ??? V4__corrigir_tipo_campo.xml
```

### Atomicidade de Deploys

* **Manter atomicidade**: Mudanças devem ser consistentes e isoladas
* **Rollback plan**: Sempre tenha um plano de reversão
* **Testes em ambiente de homologação**: Nunca faça deploy direto em produção
* **Deploy incremental**: Divida grandes mudanças em releases menores

### Contexto e AppKey

* **Contexto de add-on é único por `appkey`**:
  * Alterar `appkey` sem mudar o contexto causa erro na instalação
  * Erro comum: "Já existe um add-on de mesmo contexto"
  * Mantenha `appkey` e contexto consistentes durante a vida do add-on

```xml
<!-- ? BOM: Manter appkey e contexto consistentes -->
<addon>
    <appkey>com.minhaempresa.meuaddon</appkey>
    <context>MeuAddon</context>
    <version>1.2.0</version>
</addon>
```

### Changelog e Documentação de Release

* **Mantenha um CHANGELOG.md**: Documente mudanças em cada versão
* **Release notes**: Descreva funcionalidades, correções e breaking changes
* **Migration guide**: Para breaking changes, explique como migrar

```markdown
# Changelog

## [2.0.0] - 2024-01-15
### Breaking Changes
- Removida API deprecated `PedidoService.buscar()`
- Use `PedidoService.buscarPorNumero()` no lugar

### Added
- Nova funcionalidade de aprovação em lote
- Suporte a webhooks para eventos de pedido

### Fixed
- Corrigido cálculo de impostos para regime especial
- Resolvido problema de timeout em integrações

## [1.5.2] - 2024-01-10
### Fixed
- Corrigido null pointer em validação de parceiro
```

### Estratégia de Deploy

* **Blue-Green Deployment**: Mantenha duas versões em paralelo durante transição
* **Canary Release**: Deploy gradual para subset de usuários
* **Feature Flags**: Habilite/desabilite funcionalidades sem redeploy

### Backward Compatibility

* **Mantenha compatibilidade** quando possível
* **Deprecate before remove**: Marque como `@Deprecated` antes de remover
* **Grace period**: Dê tempo para usuários migrarem

```java
// ? BOM: Deprecação adequada
@Deprecated
public void metodoAntigo() {
    logger.warn("metodoAntigo() está deprecated. Use metodoNovo() no lugar.");
    // Delega para novo método para manter funcionamento
    metodoNovo();
}

public void metodoNovo() {
    // Nova implementação
}
```

***

## Conclusão

Seguir estas boas práticas garantirá que seus add-ons sejam:

* **Robustos**: Resistentes a falhas e com tratamento adequado de erros
* **Performáticos**: Otimizados para resposta rápida e uso eficiente de recursos
* **Seguros**: Protegidos contra vulnerabilidades e acesso não autorizado
* **Manuteníveis**: Fáceis de entender, modificar e evoluir
* **Escaláveis**: Preparados para crescimento de dados e usuários

**Lembre-se**: Código é lido muito mais vezes do que é escrito. Invista tempo em qualidade!

### Recursos Adicionais

* [Documentação Oficial Sankhya](https://developer.sankhya.com.br)
* [Área do Desenvolvedor](https://areadev.sankhya.com.br)
* [Comunidade Sankhya Developers](https://community.sankhya.com.br/developers)

### Contribuindo

Este guia é vivo e deve evoluir com o ecossistema. Se você tem sugestões de melhorias ou novos tópicos, contribua através do repositório do projeto.
