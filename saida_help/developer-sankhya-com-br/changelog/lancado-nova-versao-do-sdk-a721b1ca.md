---
id: "https://developer.sankhya.com.br/changelog/lancado-nova-versao-do-sdk"
titulo: "Lançado nova versão do SDK (2.2.0)"
url: "https://developer.sankhya.com.br/changelog/lancado-nova-versao-do-sdk"
---

# Lançado nova versão do SDK (2.2.0)

📋 Visão Geral\
Esta versão traz melhorias significativas na camada de persistência, sistema de injeção de dependências e integração com ferramentas modernas de mapeamento, permitindo arquiteturas mais robustas e produtivas.

***

### ✨ Novidades Principais

🔍 **1. NativeQuery - Consultas SQL Nativas**\
Novo suporte para execução de queries SQL nativas através da anotação @NativeQuery, oferecendo:

✅ Controle Total: Execute SQL complexo com JOINs, subqueries e window functions\
✅ Type-Safe: Mapeamento automático para interfaces (DTOs) e tipos Java\
✅ Segurança: Proteção contra SQL Injection via parâmetros nomeados\
✅ Flexibilidade: Suporte a macros Sankhya e funções SQL específicas do banco\
✅ Integração com JdbcWrapper: Reutilização de conexões existentes em Listeners\
Exemplo:

```java
@NativeQuery("SELECT CAMPO1, CAMPO2 FROM TABELA WHERE STATUS = :status")
List<MeuDTO> buscarPorStatus(String status);

@NativeQuery("SELECT COUNT(1) FROM TGFVEI")
Long contarVeiculos(JdbcWrapper jdbcWrapper);
```

***

**📄 2. API de Paginação no Repository**\
Sistema completo de paginação para consultas @Criteria:

✅ PageRequest: Controle de página, tamanho e ordenação\
✅ `Page<T>`: Objeto de retorno com metadados de paginação\
✅ Ordenação Múltipla: Suporte a múltiplos campos e direções (ASC/DESC)\
✅ Ordenação Padrão: ID incluído automaticamente se não especificado

Exemplo:

```java
@Criteria(clause = "ATIVO = :ativo")
Page<Veiculo> findByAtivoPaginado(Boolean ativo, Pageable pageable);

// Uso no serviço
PageRequest pageRequest = PageRequest.of(0, 10, 
    Sort.by("PLACA", Direction.DESC)
);
Page<Veiculo> resultado = repository.findByAtivoPaginado(true, pageRequest);
```

***

**💉 3. Novas Formas de Injeção de Dependências**
Expansão do sistema de DI com suporte a múltiplas implementações:

Qualificadores Type-Safe com bindWith\
✅ Anotações qualificadoras personalizadas para seleção de implementações\
✅ Verificação em tempo de compilação\
✅ Refatoração segura\
Exemplo:

```java
@Component(bindWith = Primary.class)
public class EmailNotificationService implements NotificationService { }

@Inject
public OrderProcessor(@Primary NotificationService notifier) { }
```

Múltiplas Implementações com Multibinder\
✅ Injeção automática de `Set<Interface>` com todas as implementações\
✅ Ideal para padrões Strategy e Observer\
Exemplo:

```java
@Inject
public EventDispatcher(Set<EventHandler> handlers) {
    // Recebe TODAS as implementações de EventHandler
}
```

Qualificadores por Nome\
✅ Suporte a @Named para casos mais simples\
✅ Flexibilidade com strings identificadoras

***

**🗄️ 4. ORM Mais Poderoso**\
Melhorias significativas no mapeamento objeto-relacional:

Orphan Removal Strategies\
Controle sobre entidades órfãs em relacionamentos:

OrphanRemovalStrategy.NONE: Mantém o relacionamento intacto\
OrphanRemovalStrategy.DETACH: Define FK como NULL sem remover registro\
Exemplo:

```java
@OneToMany(
    cascade = Cascade.ALL, 
    orphanRemovalStrategy = OrphanRemovalStrategy.DETACH
)
private List<EntidadeB> entidadesB;
```

Reverse Column em Relacionamentos\
✅ Propriedade reverseColumn para @OneToOne e @ManyToOne\
✅ Captura explícita de FK em operações CASCADE\
✅ Maior controle sobre mapeamento bidirecional\
Suporte a Chaves Primárias Compostas\
✅ Anotação @Embeddable para PKs compostas\
✅ Repositories funcionam nativamente com @Id composto\
Exemplo:

```java
@Embeddable
public class ItemNotaPK {
    @Column(name="NUNOTA") Long numeroUnico;
    @Column(name="SEQUENCIA") Long sequenciaItem;
}

@Repository
public interface ItemNotaRepository 
    extends JapeRepository<ItemNotaPK, ItemNota> { }
```

***

**🗺️ 5. Integração com MapStruct**\
Framework de mapeamento entre objetos com geração de código em tempo de compilação:

✅ Detecção Automática: SDK detecta MapStruct no classpath\
✅ Injeção Nativa: Mappers disponíveis via @Inject\
✅ Performance: Código gerado sem reflection\
✅ Suporte Java e Kotlin: Configuração com annotationProcessor ou ksp\
✅ Type-Safe: Erros de mapeamento detectados na compilação\
Exemplo:

```java
@Mapper(componentModel = "cdi")
public interface UserMapper {
    @Mapping(source = "nomeUsuario", target = "username")
    UserDTO toDTO(UserJapeEntity entity);
}

@Component
public class UserService {
    @Inject
    public UserService(UserMapper mapper) {
        this.mapper = mapper;
    }
}
```

<br />

**🎯 Benefícios para Desenvolvedores**

|               |                                                       |
| :------------ | :---------------------------------------------------- |
| Recurso       | Benefício                                             |
| NativeQuery   | Consultas complexas com performance otimizada         |
| Paginação     | Aplicações escaláveis com grandes volumes de dados    |
| DI Avançada   | Arquiteturas flexíveis com múltiplas implementações   |
| ORM Melhorado | Controle granular sobre relacionamentos e integridade |
| MapStruct     | Redução drástica de código boilerplate de conversão   |

📚 Documentação Atualizada\
✅ Injeção de Dependências\
✅ Mapeamento Objeto-Relacional\
✅ Camada de Repositório\
✅ Integração MapStruct

> ⚠️ Avisos Importantes
>
> Esta é uma versão em Acesso Antecipado (Beta). As funcionalidades estão sujeitas a modificações.
>
> Para obter acesso, envie um e-mail para <developer@sankhya.com.br> informando a appkey do seu projeto.
