---
id: "https://developer.sankhya.com.br/docs/iniciando"
titulo: "🚀 Getting Started: Seu Primeiro Serviço com o SDK"
url: "https://developer.sankhya.com.br/docs/iniciando"
atualizado_em: "2026-09-08T19:11:04.000Z"
---

# 🚀 Getting Started: Seu Primeiro Serviço com o SDK

<br />

# 🚀 Getting Started: Seu Primeiro Serviço com o SDK

Este guia prático demonstra como construir um serviço "Hello, World!" utilizando os principais recursos do SDK Sankhya: injeção de dependências, controle transacional, e a definição de entidades e repositórios.

## 🛠️ Pré-requisitos

Garanta que seu projeto esteja configurado para usar a versão `2.0.0` ou superior do plugin do Add-on Studio. Verifique seu arquivo `build.gradle`:

```groovy
// build.gradle
buildscript {
    // ...
    dependencies {
        classpath "br.com.sankhya.studio:gradle-plugin:2.0.+" // Garanta a versão 2.0.0 ou superior
        // ... outras dependências
    }
}
```

## 🧩 Componentes Principais

Vamos construir um serviço para gerenciar uma entidade `Veiculo`.

### 1. A Entidade (`Veiculo.java`)

As entidades agora são **POJOs (Plain Old Java Objects)** anotados, de forma muito similar ao padrão **JPA**. Isso substitui o `DynamicVO` por classes Java modernas e fortemente tipadas.

<Callout icon="📘" theme="info">
  ### **Importante:** Lembre-se que a entidade (`TGFVEI` neste caso) ainda precisa ser definida no **[Dicionário de Dados](https://developer.sankhya.com.br/docs/dicionario-de-dados)** para que a plataforma a reconheça.
</Callout>

```java
// src/main/java/br/com/meuaddon/model/Veiculo.java
package br.com.meuaddon.model;

import br.com.sankhya.studio.persistence.Column;
import br.com.sankhya.studio.persistence.JapeEntity;
import br.com.sankhya.studio.persistence.Id;
import lombok.Data;

@Data
@JapeEntity(entity="Veiculo", table="TGFVEI")
public class Veiculo {

    @Id
    @Column(name = "CODVEICULO")
    private Long id;

    @Column(name = "PLACA")
    private String placa;

    @Column(name = "ATIVO")
    private boolean ativo; // Use tipos primitivos sempre que possível
}
```

**Tipos de Dados Suportados:**
O SDK suporta uma vasta gama de tipos modernos, incluindo:

* Primitivos: `long`, `int`, `boolean`, `float`, `double`
* Wrappers: `Long`, `Integer`, `Boolean`, etc.
* Números de alta precisão: `BigDecimal`, `BigInteger`
* Texto: `String`
* Datas e Horas: `Timestamp`, `LocalDate`, `LocalDateTime`
* Enums

### 2. O Repositório (`VeiculoRepository.java`)

O repositório é a camada de acesso a dados. Crie uma interface que estenda `JapeRepository`, e o SDK cuidará da implementação dos métodos de CRUD (`save`, `findByPK`, `delete`, etc.) e de busca que você definir.

```java
// src/main/java/br/com/meuaddon/repository/VeiculoRepository.java
package br.com.meuaddon.repository;

import br.com.sankhya.studio.persistence.Criteria;
import br.com.sankhya.studio.persistence.Delete;
import br.com.sankhya.studio.persistence.JapeRepository;
import br.com.sankhya.studio.stereotypes.Repository;
import br.com.meuaddon.model.Veiculo;
import java.util.List;
import java.util.Optional;

@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {

    /**
     * O SDK implementa automaticamente buscas por campos da entidade.
     * Retorna um Optional, pois o veículo pode não existir.
     */
    Optional<Veiculo> findByPlaca(String placa);

    /**
     * Use @Criteria para consultas mais complexas com JAPE criteria.
     * O SDK mapeia os parâmetros do método para a criteria.
     */
    @Criteria("this.ATIVO = 'S' AND this.PLACA LIKE :placa")
    List<Veiculo> findAtivosPorPlaca(String placa);

    /**
     * Use @Delete para criar um método de exclusão customizado.
     */
    @Delete("this.PLACA = :placa")
    void deleteByPlaca(String placa);
}
```

* **Retornos Flexíveis:** Métodos podem retornar `Optional<T>`, um único `POJO` ou uma `List<T>`.

### 3. O DTO (`VeiculoDTO.java`)

DTOs (Data Transfer Objects) são usados para transportar dados entre as camadas (ex: da requisição do serviço para a lógica de negócio). O SDK integra o **Bean Validation** para validações automáticas.

```java
// src/main/java/br/com/meuaddon/dto/VeiculoDTO.java
package br.com.meuaddon.dto;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;
import lombok.Data;

@Data
public class VeiculoDTO {

    @NotBlank(message = "A placa não pode ser vazia.")
    @Size(min = 7, max = 8, message = "A placa deve ter entre 7 e 8 caracteres.")
    private String placa;

    private boolean ativo;
}
```

### 4. O Serviço (`VeiculoService.java`)

Esta é a camada que contém a lógica de negócio. Ela usa **injeção de dependências** para obter o repositório e `@Transactional` para garantir a consistência dos dados.

```java
// src/main/java/br/com/meuaddon/service/VeiculoService.java
package br.com.meuaddon.service;

import br.com.meuaddon.dto.VeiculoDTO;
import br.com.meuaddon.model.Veiculo;
import br.com.meuaddon.repository.VeiculoRepository;
import br.com.sankhya.studio.annotations.Service;
import br.com.sankhya.studio.persistence.Transactional;
import com.google.inject.Inject;
import javax.validation.Valid;

@Service // A anotação @Service expõe esta classe como um serviço.
public class VeiculoService {

    private final VeiculoRepository repository;

    @Inject // O SDK injeta a dependência do repositório via construtor.
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }

    /**
     * Cria um novo veículo.
     * A anotação @Transactional garante que a operação seja atômica.
     * A anotação @Valid dispara a validação do DTO.
     */
    @Transactional
    public Long cadastrarNovoVeiculo(@Valid VeiculoDTO dto) {
        if (repository.findByPlaca(dto.getPlaca()).isPresent()) {
            throw new IllegalStateException("Veículo com esta placa já existe.");
        }

        Veiculo novoVeiculo = new Veiculo();
        novoVeiculo.setPlaca(dto.getPlaca());
        novoVeiculo.setAtivo(dto.isAtivo());

        repository.save(novoVeiculo);

        return novoVeiculo.getId();
    }

    /**
     * Atualiza os dados de um veículo existente.
     */
    @Transactional
    public void atualizarVeiculo(Long id, @Valid VeiculoDTO dto) {
        Veiculo veiculo = repository.findByPK(id)
                .orElseThrow(() -> new IllegalStateException("Veículo não encontrado com o ID: " + id));

        veiculo.setPlaca(dto.getPlaca());
        veiculo.setAtivo(dto.isAtivo());

        repository.save(veiculo); // O método save() também atualiza a entidade.
    }

    /**
     * Exclui um veículo pela placa.
     */
    @Transactional
    public void excluirVeiculo(String placa) {
        repository.deleteByPlaca(placa);
    }
}
```

## Resumo do Fluxo

1. **Requisição:** Um cliente chama o serviço `VeiculoService` (ex: método `cadastrarNovoVeiculo`) com um JSON contendo os dados do `VeiculoDTO`.
2. **Controller (SDK Interno):** O SDK recebe a requisição, desserializa o JSON para `VeiculoDTO` e chama o método correspondente no `VeiculoService`.
3. **Validação:** A anotação `@Valid` aciona as validações definidas no `VeiculoDTO`. Se a placa for inválida, uma exceção é lançada e a execução para.
4. **Transação:** A anotação `@Transactional` inicia uma transação no banco de dados.
5. **Lógica de Negócio:** O serviço executa a lógica, como verificar se a placa já existe.
6. **Persistência:** O serviço utiliza o `VeiculoRepository` para salvar, atualizar ou excluir a entidade `Veiculo`.
7. **Commit/Rollback:** Se tudo ocorrer bem, a transação é commitada. Se qualquer exceção for lançada, a transação é revertida (rollback).
8. **Resposta:** O resultado (como o ID do novo veículo) é retornado ao cliente.

## Benefícios e Princípios de Desenvolvimento

Adotar esta arquitetura moderniza o desenvolvimento e traz benefícios significativos de organização, manutenibilidade e testabilidade, alinhando o código a princípios consolidados como **Clean Code** e **SOLID**.

### Injeção de Dependências (ID)

* **O que é?** Em vez de uma classe criar suas próprias dependências (ex: `new VeiculoRepository()`), elas são "injetadas" de fora (pelo construtor, por exemplo).
* **Legibilidade e Clean Code:** O construtor de uma classe declara explicitamente tudo o que ela precisa para funcionar. Isso torna as dependências claras e o código mais fácil de entender.
* **Princípio da Inversão de Dependência (SOLID):** A `VeiculoService` não depende da implementação concreta do `VeiculoRepository`, mas sim de sua interface (abstração). Isso desacopla o código, permitindo que a implementação do repositório seja trocada sem impactar a lógica de negócio.
* **Testabilidade:** Facilita a criação de testes unitários. É possível "mockar" (simular) o `VeiculoRepository` para testar a `VeiculoService` de forma isolada, sem a necessidade de uma conexão real com o banco de dados.

## Definição de Repositórios

* **O que é?** O Padrão de Repositório abstrai a camada de acesso a dados, tratando a fonte de dados como uma coleção de objetos.
* **Legibilidade e Clean Code:** Centraliza toda a lógica de acesso a dados em um único lugar (a interface do repositório). A camada de serviço (`VeiculoService`) apenas utiliza métodos como `findByPlaca`, sem precisar se preocupar com a construção de queries SQL ou com a forma como os dados são persistidos.
* **Princípio da Responsabilidade Única (SOLID):** O repositório tem uma única responsabilidade: gerenciar a persistência da entidade `Veiculo`. A classe de serviço tem outra: orquestrar a lógica de negócio. Essa **separação de preocupações** é a base de uma arquitetura limpa e organizada, tornando o código mais fácil de manter e escalar.
