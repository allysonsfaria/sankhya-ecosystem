---
id: "https://developer.sankhya.com.br/docs/foreign-keys-compostas"
titulo: "🔗 Foreign Keys Compostas"
url: "https://developer.sankhya.com.br/docs/foreign-keys-compostas"
atualizado_em: "2026-09-08T19:12:52.000Z"
---

# 🔗 Foreign Keys Compostas

# 🔗 Foreign Keys Compostas

***

## 📝 O que são Foreign Keys Compostas?

Foreign Keys Compostas são chaves estrangeiras formadas por **múltiplas colunas** que referenciam uma chave primária composta de outra tabela. O SDK Sankhya oferece suporte através das anotações `@JoinColumn` e `@JoinColumns`.

<Callout icon="⚠️" theme="warn">
  ### **IMPORTANTE**: `@JoinColumn` e `@JoinColumns` são **APENAS** para `@ManyToOne` e `@OneToOne`.

  Para `@OneToMany`, use o atributo `relationship` da própria anotação.
</Callout>

| Relacionamento | Mapeamento de Colunas                 |
| -------------- | ------------------------------------- |
| `@ManyToOne`   | `@JoinColumn` ou `@JoinColumns`       |
| `@OneToOne`    | `@JoinColumn` ou `@JoinColumns`       |
| `@OneToMany`   | `relationship = {@Relationship(...)}` |

***

## 🔧 Sintaxe

### @JoinColumn (FK Simples)

```java
@ManyToOne
@JoinColumn(
    name = "CODPARC",                   // Coluna FK na tabela local
    referencedColumnName = "CODPARC",   // Coluna PK na tabela referenciada
    description = "Código do Parceiro"  // Obrigatório com autoDD
)
private Parceiro parceiro;
```

### @JoinColumns (FK Composta)

```java
@ManyToOne
@JoinColumns({
    @JoinColumn(name = "NUNOTA", referencedColumnName = "NUNOTA", description = "Num. Nota"),
    @JoinColumn(name = "SEQUENCIA", referencedColumnName = "SEQUENCIA", description = "Sequencia Item")
})
private ItemNota itemNota;
```

***

## 💡 Exemplos Práticos

### Exemplo 1: PK Simples referenciando PK Composta

```java
@JapeEntity(entity = "ChaveSimples", table = "TB_CHAVE_SIMPLES")
public class ChaveSimples {
    @Id
    @Column(name = "ID")
    private Long id;
    
    @OneToOne
    @JoinColumns({
        @JoinColumn(name = "FK_COL1", referencedColumnName = "COL1", description = "Coluna 1"),
        @JoinColumn(name = "FK_COL2", referencedColumnName = "COL2", description = "Coluna 2")
    })
    private ChaveComposta chaveComposta;
}

@Embeddable
public class ChaveCompostaId implements Serializable {
    @Column(name = "COL1")
    private Long col1;
    
    @Column(name = "COL2")
    private Long col2;
}

@JapeEntity(entity = "ChaveComposta", table = "TB_CHAVE_COMPOSTA")
public class ChaveComposta {
    @Id
    private ChaveCompostaId id;
}
```

### Exemplo 2: PK Composta referenciando PK Composta

```java
@Embeddable
public class ChaveComposta2Id implements Serializable {
    @Column(name = "COL1")
    private Long col1;
    
    @Column(name = "COL2")
    private Long col2;
}

@JapeEntity(entity = "ChaveComposta2", table = "TB_CHAVE_COMPOSTA_2")
public class ChaveComposta2 {
    @Id
    private ChaveComposta2Id id;
    
    @ManyToOne
    @JoinColumns({
        @JoinColumn(name = "FK_TB1_COL1", referencedColumnName = "COL1", description = "FK Col1"),
        @JoinColumn(name = "FK_TB1_COL2", referencedColumnName = "COL2", description = "FK Col2")
    })
    private ChaveComposta1 chaveComposta1;
}
```

### Exemplo 3: @OneToMany com Pai de PK Composta

```java
@Embeddable
public class PaiId implements Serializable {
    @Column(name = "COL1")
    private Long col1;
    
    @Column(name = "COL2")
    private Long col2;
}

@JapeEntity(entity = "Pai", table = "TB_PAI")
public class Pai {
    @Id
    private PaiId id;
    
    @OneToMany(cascade = {Cascade.CREATE, Cascade.MERGE})
    private List<Filha> filhas;
}

@JapeEntity(entity = "Filha", table = "TB_FILHA")
public class Filha {
    @Id
    @Column(name = "ID")
    private Long id;
    
    @ManyToOne
    @JoinColumns({
        @JoinColumn(name = "FK_PAI_COL1", referencedColumnName = "COL1", description = "FK Pai Col1"),
        @JoinColumn(name = "FK_PAI_COL2", referencedColumnName = "COL2", description = "FK Pai Col2")
    })
    private Pai pai;
}
```

***

## ✅ Boas Práticas

* Use nomes descritivos — `CODEMP_CONTRATO` melhor que `EMP`
* Mantenha a mesma ordem em `@JoinColumns` e `@Embeddable`
* Prefira `Cascade.CREATE` e `Cascade.MERGE` ao invés de `Cascade.ALL`
