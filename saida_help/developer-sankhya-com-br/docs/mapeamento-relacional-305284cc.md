---
id: "https://developer.sankhya.com.br/docs/mapeamento-relacional"
titulo: "🗄️Mapeamento Objeto-Relacional (ORM)"
url: "https://developer.sankhya.com.br/docs/mapeamento-relacional"
atualizado_em: "2026-09-08T19:13:49.000Z"
---

# 🗄️Mapeamento Objeto-Relacional (ORM)

<br />

# Mapeamento Objeto-Relacional (ORM)

O SDK Sankhya oferece um framework de **Mapeamento Objeto-Relacional (ORM)** inspirado em padrões como JPA/Hibernate. Ele permite que você trabalhe com o banco de dados utilizando objetos Java (POJOs) e anotações, abstraindo a necessidade de escrever SQL ou manipular `DynamicVO` diretamente.

## Mapeando Entidades

A base do ORM é mapear uma classe Java para uma tabela do banco de dados.

### 1. Definição da Entidade

Use a anotação `@JapeEntity` para declarar que uma classe representa uma entidade do sistema e está vinculada a uma tabela.

```java
@JapeEntity(entity = "NomeDaEntidade", table = "NOME_DA_TABELA")
public class MinhaEntidade {
    // ... campos e métodos
}
```

### 2. Chave Primária (`@Id`)

A anotação `@Id` é usada para marcar o campo que corresponde à chave primária da tabela.

```java
@JapeEntity(entity = "EntidadeA", table = "TABELA_ENTIDADE_A")
public class EntidadeA {
    @Id
    @Column(name = "ID_PROJETO")
    private Long id;
    // ...
}
```

#### Chaves Primárias Compostas

Para tabelas com chaves primárias compostas (mais de uma coluna), utilize as anotações `@Id` e `@Embeddable`.

**Passo 1: Crie a classe da chave**
Esta classe deve conter os campos que formam a chave e ser anotada com `@Embeddable`.

```java
@Embeddable // Marca a classe como "embutível"
public class ItemNotaPK implements Serializable {
    @Column(name = "NUNOTA")
    private Long numeroNota;

    @Column(name = "SEQUENCIA")
    private Integer sequencia;

    // Construtores, getters, setters, equals() e hashCode() são obrigatórios.
}
```

**Passo 2: Utilize a chave na entidade principal**
Na sua entidade, use `@Id` para incorporar a classe da chave composta.

```java
@JapeEntity(entity = "ItemNota", table = "TGFITE")
public class ItemNota {
    @Id
    private ItemNotaPK id;

    @Column(name = "CODPROD")
    private Long codigoProduto;
    // ...
}
```

### 3. Mapeamento de Colunas (`@Column`)

A anotação `@Column` vincula um atributo da sua classe a uma coluna específica da tabela.

```java
@Column(name = "NOME_PROJETO")
private String nome;
```

***

## Mapeando Relacionamentos

O SDK suporta os principais tipos de relacionamentos para que você possa navegar entre objetos conectados.

### 1. Um-para-Muitos (`@br.com.sankhya.studio.persistence.OneToMany`)

Representa uma relação onde um registro de uma entidade (Pai) pode estar associado a múltiplos registros de outra entidade (Filha).

**Exemplo:** Um `Pedido` que possui vários `ItemPedido`.

```java
// Entidade Pai: Pedido
@JapeEntity(entity = "CabecalhoNota", table = "TGFCAB")
public class Pedido {
    @Id
    @Column(name = "NUNOTA")
    private Long numeroNota;

    // Relacionamento: Um Pedido tem muitos Itens
    @OneToMany(
        cascade = Cascade.ALL,
        relationship = {
            @Relationship(fromField = "NUNOTA", toField = "NUNOTA")
        }
    )
    private List<ItemPedido> itens;
}

// Entidade Filha: ItemPedido
@JapeEntity(entity = "ItemPedido", table = "TGFITE")
public class ItemPedido {
    @Id
    @Column(name = "ID")
    private Long id;

    // Lado inverso do relacionamento (opcional)
    @ManyToOne
    @ToString.Exclude // Evita StackOverflowError no toString()
    @JoinColumn(
        name = "NUNOTA",
        referencedColumnName = "NUNOTA",
        description = "Número da Nota"
    )
    private Pedido pedido;
}
```

**Regras do&#x20;**`@OneToMany`**:**

* O tipo do atributo deve ser uma `Collection` (como `List` ou `Set`) de outra entidade.
* É **proibido** usar `@Column` em um campo com `@OneToMany`.
* Use o atributo `relationship` para definir o mapeamento de colunas em `@OneToMany`.
* **NÃO** use `@JoinColumn`/`@JoinColumns` em `@OneToMany` (são exclusivos para `@ManyToOne`/`@OneToOne`).

### 2. Muitos-para-Um (`@br.com.sankhya.studio.persistence.ManyToOne`)

Representa o lado "muitos" da relação, onde vários registros de uma entidade apontam para um único registro de outra.

**Exemplo:** Vários `Produto`s que pertencem a uma única `CategoriaProduto`.

```java
// Entidade "Muitos": Produto
@JapeEntity(entity = "Produto", table = "TGFPRO")
public class Produto {
    @Id
    @Column(name = "CODPROD")
    private Long codigo;

    // Relacionamento: Muitos Produtos para uma Categoria
    @ManyToOne
    @ToString.Exclude // Evita StackOverflowError no toString()
    @JoinColumn(
        name = "CODGRUPOPROD",
        referencedColumnName = "CODGRUPOPROD",
        description = "Código do Grupo de Produto"
    )
    private CategoriaProduto categoria;
}

// Entidade "Um": CategoriaProduto
@JapeEntity(entity = "GrupoProduto", table = "TGFGRU")
public class CategoriaProduto {
    @Id
    @Column(name = "CODGRUPOPROD")
    private Long codigo;

    // Lado inverso (opcional)
    @OneToMany(
        relationship = {
            @Relationship(fromField = "CODGRUPOPROD", toField = "CODGRUPOPROD")
        }
    )
    private List<Produto> produtos;
}
```

**Regras do&#x20;**`@ManyToOne`**:**

* É **obrigatório** usar `@JoinColumn` ou `@JoinColumns` para especificar o mapeamento da chave estrangeira.
* **NÃO** use `@Column` em relacionamentos (use apenas em campos simples).

### 3. Um-para-Um (`@br.com.sankhya.studio.persistence.OneToOne`)

Representa uma relação onde um registro de uma entidade está associado a exatamente um registro de outra.

**Exemplo:** Um `Usuario` que tem um único `PerfilUsuario`.

```java
// Entidade Principal: Usuario
@JapeEntity(entity = "Usuario", table = "TSIUSU")
public class Usuario {
    @Id
    @Column(name = "CODUSU")
    private Long codigo;

    // Relacionamento: Um Usuário para um Perfil
    @OneToOne
    @JoinColumn(
        name = "CODIGO_PERFIL",
        referencedColumnName = "CODIGO_PERFIL",
        description = "Código Perfil"
    )
    private PerfilUsuario perfil;
}

// Entidade Dependente: PerfilUsuario
@JapeEntity(entity = "PerfilUsuario", table = "AD_PERFILUSU")
public class PerfilUsuario {
    @Id
    @Column(name = "CODPERFILUSU")
    private Long codigo;

    // Lado inverso (opcional)
    @OneToOne
    @ToString.Exclude // Evita StackOverflowError no toString()
    @JoinColumn(
        name = "CODUSU",
        referencedColumnName = "CODUSU",
        description = "Código Usuário"
    )
    private Usuario usuario;
}
```

**Regras do&#x20;**`@OneToOne`**:**

* É **obrigatório** usar `@JoinColumn` ou `@JoinColumns` no lado que detém a chave estrangeira.
* **NÃO** use `@Column` em relacionamentos (use apenas em campos simples).

***

## Reverse Column: `@OneToOne` e `@ManyToOne`

Existe uma propriedade chamada `reverseColumn` nas anotações `@OneToOne` e `@ManyToOne` que, quando estiver preenchida, é utilizada para capturar o valor
da chave estrangeira em operações de `Cascade.MERGE`, `Cascade.UPDATE` e `Cascade.INSERT`.

Se esta não estiver preenchida, utilizaremos os métodos `default` do Jape para capturar a primeira coluna da chave primária.

***

## Estratégias de Carregamento (`FetchType` vs `@Lazy`)

Atualmente, o SDK suporta apenas o carregamento sob demanda (`Lazy Loading`) entre entidades. O SDK também permite a escolha de campos que devam ter o carregamento sob demanda com a anotação `@Lazy`.

### Lazy Loading - Relacionamento entre entidades (`FetchType.LAZY`)

Com **Lazy Loading**, os dados de uma entidade relacionada **não são carregados na consulta inicial**. O acesso ao banco de dados ocorre **somente quando o relacionamento é acessado pela primeira vez**, por meio do getter.

```java
@ManyToOne(fetchType = FetchType.LAZY)
@JoinColumn(
    name = "CODPARC",
    referencedColumnName = "CODPARC",
    description = "Código Cliente"
)
private Cliente cliente;
```

***

### Lazy Loading com `@Lazy` - Demais campos

Campos simples podem ser anotados com `@Lazy` para que seu valor **só seja recuperado do banco quando o getter for explicitamente chamado**.

**Restrições:**

* ❌ Não se aplica a campos anotados com `@Id`.
* ❌ Não se aplica a campos de relacionamento (`@OneToMany`, `@ManyToOne`, `@OneToOne`).

#### Atenção ao `toString()`

Para garantir que o campo anotado com `@Lazy` permaneça realmente lazy, **é obrigatório removê-lo do&#x20;**`toString()`**&#x20;da entidade**. Caso contrário, operações aparentemente inofensivas — como logs ou `System.out.println` — podem disparar o carregamento do campo, tornando-o **EAGER na prática**.

#### Serialização em Controllers

Em `@Controller` (antigo `@Service`), a serialização de campos `@Lazy` **não ocorre automaticamente**. Isso acontece porque utilizamos **Gson**, que serializa diretamente a partir dos *fields*, e não dos *getters* (como o Jackson).

Dessa forma, para obter uma serialização controlada e previsível, é necessário criar um **Mapper com MapStruct** e converter a entidade `Jape` para um **DTO**.

🔗 Referência: [MapStruct](50_mapstruct.md)

**Exemplo:**

```java
@JapeEntity(entity = "Documento", table = "AD_DOC")
public class Documento {
    @Id
    @Column(name = "ID")
    private Long id;

    @Lazy
    @ToString.Exclude // Obrigatório para evitar carregamento acidental
    @Column(name = "CONTEUDO")
    private Text conteudoGrande;
}
```

***

**Vantagens:**

* **Performance:** Reduz o tempo de carregamento inicial, evitando consultas desnecessárias.
* **Eficiência:** Diminui o consumo de memória ao carregar apenas os dados efetivamente utilizados.

**Ponto de Atenção:**

* O carregamento lazy é disparado **exclusivamente pela chamada do getter**.
* Até que `getCliente()` seja executado, o campo `cliente` permanecerá `null`.
* **Errado:** `if (pedido.cliente == null)`
* **Correto:** `if (pedido.getCliente() == null)`

***

## Tipos de dados para campos `TEXT_BOX` e `FILE`

### `DataType.TEXT_BOX`

* Pode ser mapeado como `char[]` ou `br.com.sankhya.sdk.data.structures.Text`.
* **Recomendação:** Prefira `Text` para campos de texto grande, pois oferece melhor integração, menor consumo de memória e melhor suporte a lazy loading.

É possível criar um `Text` a partir de um `char[]` ou `String`:

```java
// A partir de um char[]
Text fromCharArray = Text.of(new char[]{'t','e','s','t','e'});

// A partir de uma String
Text fromString = Text.of("teste");
```

***

### `DataType.FILE`

* Pode ser mapeado como `byte[]` ou `br.com.sankhya.sdk.data.structures.Binary`.
* **Recomendação:** Prefira `Binary` para manipulação mais eficiente de arquivos binários.

O `Binary` permite trabalhar com arquivos grandes de forma mais segura e eficiente, evitando carga total em memória.

```java
// A partir de um byte[]
Binary fromByteArray = Binary.of(new byte[]{1,2,3});

// A partir de um InputStream
InputStream inputStream = loadFile();
Binary binary = Binary.of(inputStream);
```

***

## Orphan Removal Strategy

Em alguns cenários, uma operação em cascata pode provocar a perda do vínculo entre entidades Pai e Filha, resultando em registros "órfãos".

Atualmente, existem duas estratégias de remoção de objetos órfãos disponíveis:

| Estratégia | Descrição                                                                                                                                                                      |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NONE`     | Nenhuma ação é executada. O relacionamento entre as entidades fica intacto. Muito útil entre relacionamentos de entidades nativas, que não se deseja gerar efeitos colaterais. |
| `DETACH`   | Define o valor da chave estrangeira da entidade Filha como `NULL`, desvinculando-a do Pai sem removê-la do banco de dados.                                                     |

### Exemplo

O desenvolvedor possui as entidades `EntidadeA` e `EntidadeB`:

```java
@JapeEntity(entity = "EntidadeA", table = "TB_ENTIDADE_A")
public class EntidadeA {
    @Id
    @Column(name = "ID")
    private Long id;

    @Column(name = "DESCRICAO")
    private String descricao;
    
    @OneToMany(
        cascade = Cascade.ALL,
        orphanRemovalStrategy = OrphanRemovalStrategy.DETACH,
        relationship = {
            @Relationship(fromField = "ID", toField = "ID_ENTIDADE_A")
        }
    )
    private List<EntidadeB> entidadesB;
}

@JapeEntity(entity = "EntidadeB", table = "TB_ENTIDADE_B")
public class EntidadeB {
    @Id
    @Column(name = "ID")
    private Long id;

    @ManyToOne
    @JoinColumn(
        name = "ID_ENTIDADE_A",
        referencedColumnName = "ID",
        description = "ID da Entidade A"
    )
    private EntidadeA entidadeA;
}
```

#### Tabelas iniciais

`TB_ENTIDADE_A`:

| ID | DESCRICAO |
| :- | :-------- |
| 1  | teste     |

`TB_ENTIDADE_B`:

| ID | ID\_ENTIDADE\_A |
| :- | :-------------- |
| 1  | 1               |
| 2  | 1               |

#### Operação de remoção

O código abaixo remove a referência que a entidade `EntidadeB` com `ID = 2L` possui para `EntidadeA`:

```java
EntidadeA entidadeA = repository.findOne(1L).get();
List<EntidadeB> entidadesB = entidadeA.getEntidadesB();
Iterator<EntidadeB> iterator = entidadesB.iterator();

while (iterator.hasNext()) {
    EntidadeB entidadeB = iterator.next();
    if (entidadeB.getId().equals(2L)) {
        iterator.remove();
        break;
    }
}

repository.save(entidadeA);
```

Após a execução, a entidade `EntidadeB` de ID `2L` permanecerá no banco, mas com o campo `ID_ENTIDADE_A` definido como `NULL`, pois foi aplicada a estratégia `DETACH`.

É importante ressaltar que a operação acima exige ao menos um cascade: `Cascade.MERGE`. Sem este os relacionamentos não são atualizados. No exemplo acima, utilizamos `Cascade.ALL`.

<Callout icon="⚠️" theme="warn">
  ### Observação Importante

  A remoção de órfãos é uma funcionalidade poderosa, que facilita a manutenção da integridade entre entidades relacionadas. No entanto, seu uso incorreto pode causar a perda acidental de vínculos entre entidades que não deveriam ser alteradas.
</Callout>

***

## Operações em Cascata (`Cascade`)

O `cascade` define como as operações (criar, atualizar, excluir) em uma entidade principal são propagadas para suas entidades relacionadas.

> **Importante:** A configuração do `cascade` no SDK Sankhya atualmente é feita através do **dicionário de dados (arquivo XML)**.
> Ainda assim, é uma boa prática documentar o comportamento esperado na anotação `@OneToMany(cascade = ...)` para clareza do código.
> Mapear corretamente agora, permite que seu código já esteja preparado para quando o suporte a `cascade` via anotações for implementado.

| Tipo de Cascade  | Descrição                                                                                                                                                                                          |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Cascade.NONE`   | (Padrão) Nenhuma operação é propagada. Cada entidade deve ser salva individualmente.                                                                                                               |
| `Cascade.CREATE` | Ao salvar a entidade pai, as entidades filhas associadas (que ainda não existem) também são persistidas automaticamente.                                                                           |
| `Cascade.UPDATE` | Ao atualizar a entidade pai, as entidades filhas associadas também têm seus dados sincronizados.                                                                                                   |
| `Cascade.DELETE` | Ao excluir a entidade pai, as entidades filhas associadas também são removidas do banco de dados.                                                                                                  |
| `Cascade.MERGE`  | Sincroniza as entidades relacionadas, vinculando ambas conforme necessário. Exemplo: ao criar/editar a entidade B a partir de A, o relacionamento entre A e B é estabelecido em ambos os sentidos. |
| `Cascade.ALL`    | Propaga todas as operações (`CREATE`, `UPDATE`, `DELETE`, `MERGE`).                                                                                                                                |

#### Exemplo de Configuração no Dicionário de Dados

Para um relacionamento `OneToMany` de `EntidadePai` para `EntidadeFilha`, a configuração de um `Cascade.ALL` seria:

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<metadados>
    <table name="TB_ENTIDADE_PAI">
        <instances>
            <instance name="EntidadePai">
                <relationShip>
                    <relation entityName="EntidadeFilha" 
                              relation="OneToMany" 
                              insert="S" 
                              update="S" 
                              removeCascade="S">
                        <fields>
                            <field localName="ID" targetName="ENTIDADE_PAI_ID"/>
                        </fields>
                    </relation>
                </relationShip>
            </instance>
        </instances>
        </table>
</metadados>
```

***

## Boas Práticas e Considerações

### 1. Evite `StackOverflowError` em Relacionamentos Bidirecionais

Quando duas entidades se referenciam mutuamente, a chamada do método `toString()` pode criar um loop infinito, resultando em um `StackOverflowError`.

**Solução:** Exclua o `toString()` do lado "fraco" da relação (geralmente, o lado `@ManyToOne`). Se estiver usando Lombok, a anotação `@ToString.Exclude` resolve isso facilmente.

```java
// Lado "Fraco": ItemPedido
@Data
@JapeEntity(entity = "ItemNota", table = "TGFITE")
public class ItemPedido {
    // ... outros campos

    @ManyToOne
    @Column(name = "NUNOTA")
    @ToString.Exclude // Exclui este campo do toString() para evitar loop
    private Pedido pedido;
}
```

### 2. Não Inicialize Coleções

Deixe que o framework gerencie a inicialização das coleções de relacionamentos. Inicializá-las manualmente pode interferir no mecanismo de *Lazy Loading*.

```java
// ? BOM: A coleção não é inicializada.
@OneToMany(
    relationship = {@Relationship(fromField = "ID", toField = "ID_CLIENTE")}
)
private List<Pedido> pedidos;

// ❌ RUIM: Não inicialize a coleção.
@OneToMany(
    relationship = {@Relationship(fromField = "ID", toField = "ID_CLIENTE")}
)
private List<Pedido> pedidos = new ArrayList<>();
```

### 3. Utilize Métodos de Conveniência (Helpers)

Para manter a consistência em relacionamentos bidirecionais, crie métodos para adicionar e remover itens que atualizam os dois lados da relação ao mesmo tempo.

```java
// Na classe Pedido
public class Pedido {
    @OneToMany(
        relationship = {@Relationship(fromField = "NUNOTA", toField = "NUNOTA")}
    )
    private List<ItemPedido> itens = new ArrayList<>();

    public void addItem(ItemPedido item) {
        this.itens.add(item);
        item.setPedido(this); // Mantém a consistência
    }

    public void removeItem(ItemPedido item) {
        this.itens.remove(item);
        item.setPedido(null); // Mantém a consistência
    }
}
```
