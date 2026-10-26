---
id: "https://developer.sankhya.com.br/docs/️mapeamento-de-objetos-com-mapstruct"
titulo: "🗺️ Mapeamento de Objetos com MapStruct"
url: "https://developer.sankhya.com.br/docs/️mapeamento-de-objetos-com-mapstruct"
atualizado_em: "2026-09-08T19:13:40.000Z"
---

# 🗺️ Mapeamento de Objetos com MapStruct

<br />

# 🗺️ Mapeamento de Objetos com MapStruct

O SDK Sankhya oferece integração nativa com o **MapStruct**, uma biblioteca poderosa que simplifica o mapeamento entre diferentes camadas de objetos (como DTOs, Entidades JAPE e outros beans).

Com o MapStruct, você define uma interface de mapeamento e a biblioteca gera a implementação automaticamente em tempo de compilação, eliminando a necessidade de escrever código de conversão manual, repetitivo e propenso a erros.

## 🤔 Por que usar MapStruct?

* ✅ **Produtividade Máxima:** Automatiza a criação de código de mapeamento.
* ✅ **Performance:** O código gerado é tão rápido quanto o mapeamento manual, sem usar reflection.
* ✅ **Segurança de Tipos:** Erros de mapeamento são detectados em tempo de compilação.
* ✅ **Código Limpo:** Suas classes de negócio ficam livres da lógica de conversão.

***

## ⚙️ Como Funciona: Detecção Automática

O processador de anotações do Sankhya Studio é inteligente. Ele **detecta automaticamente** se o MapStruct está presente no classpath do seu projeto.

* **Se o MapStruct for encontrado**, o SDK ativa a integração, processa suas interfaces anotadas com `@Mapper` e as registra no contêiner de injeção de dependências.
* **Se não for encontrado**, a funcionalidade é simplesmente ignorada, sem causar erros.

Durante a compilação, você verá uma das seguintes mensagens no log:

```
✅ MapStruct detectado no classpath. MapperProcessor será ativado.
```

ou

```
ℹ️ MapStruct não detectado no classpath. MapperProcessor será ignorado.
```

***

## 🛠️ Configuração do Projeto

Para usar o MapStruct, você precisa adicionar as dependências ao `build.gradle` do seu addon.

### 1. Dependências para Projetos Java

Se seu projeto é 100% Java, adicione as seguintes dependências:

```groovy
// build.gradle

dependencies {
    // API do MapStruct
    implementation 'org.mapstruct:mapstruct:1.5.5.Final'
    
    // Processador de anotações do MapStruct
    annotationProcessor 'org.mapstruct:mapstruct-processor:1.5.5.Final'
}

// Opcional: configure o compilador para passar opções ao MapStruct
tasks.withType(JavaCompile) {
    options.compilerArgs += [
        '-Amapstruct.defaultComponentModel=cdi',
        '-Amapstruct.unmappedTargetPolicy=IGNORE'
    ]
}
```

### 2. Dependências para Projetos Kotlin (com KSP)

Se seu projeto utiliza Kotlin, atualmente não temos suporte, pois o Mapstruct não possuí compatibilidade com o KSP.

***

## ✨ Exemplo Prático de Uso

Vamos ver como criar, injetar e usar um mapper em um serviço.

### Passo 1: Crie a Interface do Mapper

Defina uma interface e anote-a com `@Mapper`. O SDK recomenda o uso do `componentModel = "cdi"` para melhor integração com o ecossistema de injeção de dependências.

```java
// br/com/fabricante/addon/mapper/UserMapper.java

import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.factory.Mappers;

@Mapper(componentModel = "cdi")
public interface UserMapper {

    // Opcional: permite obter uma instância se a DI não estiver disponível
    UserMapper INSTANCE = Mappers.getMapper(UserMapper.class);

    @Mapping(source = "nomeUsuario", target = "username")
    @Mapping(source = "ativo", target = "enabled")
    UserDTO toDTO(UserJapeEntity entity);

    @Mapping(target = "nomeUsuario", source = "username")
    @Mapping(target = "ativo", source = "enabled")
    UserJapeEntity toEntity(UserDTO dto);
    
    List<UserDTO> toDTOList(List<UserJapeEntity> entities);
}
```

### Passo 2: Injete o Mapper em um Componente

Graças à integração automática, você pode injetar seu mapper diretamente em qualquer classe gerenciada pelo SDK (`@Component`, `@Service`, etc.).

```java
// br/com/fabricante/addon/service/UserService.java

@Component
public class UserService {

    private final UserRepository userRepository;
    private final UserMapper userMapper;

    @Inject
    public UserService(UserRepository userRepository, UserMapper userMapper) {
        this.userRepository = userRepository;
        this.userMapper = userMapper;
    }

    @Transactional
    public UserDTO findUserById(Long userId) {
        UserJapeEntity userEntity = userRepository.findByPK(userId)
            .orElseThrow(() -> new NotFoundException("Usuário não encontrado"));
        
        // Use o mapper para converter a entidade em DTO
        return userMapper.toDTO(userEntity);
    }
    
    public void createUser(UserDTO userDTO) {
        // Use o mapper para converter o DTO em entidade antes de salvar
        UserJapeEntity userEntity = userMapper.toEntity(userDTO);
        userRepository.save(userEntity);
    }
}
```

O código gerado pelo MapStruct será automaticamente registrado no contêiner de DI, e o `UserService` receberá a instância correta sem nenhuma configuração adicional.

***

## 🚨 Troubleshooting (Solução de Problemas)

### Problema: Meu mapper não está sendo injetado (`UnsatisfiedDependencyException`).

**Causas e Soluções:**

1. **Dependências Incorretas:**
   * Verifique se `mapstruct-processor` está na configuração `annotationProcessor` (para Java). A dependência `mapstruct` (API) deve estar em `implementation`.

2. `componentModel`**&#x20;Incorreto:**
   * Certifique-se de que sua anotação `@Mapper` tenha `componentModel = "cdi"` ou `componentModel = "default"`. Isso instrui o MapStruct a gerar um bean que o SDK pode detectar.

3. **Projeto Não Recompilado:**
   * Às vezes, o ambiente de desenvolvimento pode não acionar o processador de anotações. Force uma recompilação limpa:
     ```bash
     ./gradlew clean build
     ```

### Problema: O processador do MapStruct parece não rodar.

**Causas e Soluções:**

1. **Conflito de Processadores:**
   * Em projetos complexos, a ordem dos processadores de anotação pode importar. Verifique se não há configurações conflitantes no seu `build.gradle`.

2. **Cache do Gradle:**
   * Limpe o cache do Gradle para garantir que nenhuma dependência antiga esteja sendo usada:
     ```bash
     ./gradlew clean --refresh-dependencies
     ```

***

## 🔗 Referências

* **Documentação Oficial do MapStruct:** [mapstruct.org](https://mapstruct.org/)
* **Guia de Injeção de Dependências do SDK:** [06\_dependency\_injection.md](./06_dependency_injection.md)
* **Repositório do MapStruct no GitHub:** [github.com/mapstruct/mapstruct](https://github.com/mapstruct/mapstruct)
