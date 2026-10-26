---
id: "https://developer.sankhya.com.br/docs/autodd-geração-automática-do-dicionário-de-dados-data-dictionary"
titulo: "🔄 AutoDD: Geração Automática do Dicionário de Dados (Data Dictionary)"
url: "https://developer.sankhya.com.br/docs/autodd-geração-automática-do-dicionário-de-dados-data-dictionary"
atualizado_em: "2026-09-28T16:24:06.000Z"
---

# 🔄 AutoDD: Geração Automática do Dicionário de Dados (Data Dictionary)

## 📝 O que é o AutoDD?

O **AutoDD** (Auto Data Dictionary) é uma feature do SDK Sankhya que gera automaticamente o **dicionário de dados XML** (data dictionary) a partir das suas entidades Java anotadas com `@JapeEntity`. O dicionário de dados é o coração do ORM Jape da Sankhya: todas as entidades precisam ser mapeadas através dele para que o framework reconheça tabelas, campos, chaves e relacionamentos.

Com o AutoDD, o desenvolvedor **não precisa mais criar manualmente arquivos XML** para mapear suas entidades. Basta anotar corretamente a classe com `@JapeEntity` e as anotações de campo (`@Id`, `@Column`, etc.), e o framework gera o XML de dicionário de dados automaticamente durante o build.

> O AutoDD **não substitui** o mapeamento manual de outras features, como views, menus, dashboards, tree table, filters, etc. Ele é focado exclusivamente no mapeamento de **Table e NativeTable**.

***

## 🔗 Relação entre AutoDD e AutoDDL

* **AutoDD**: Gera o dicionário de dados XML a partir das entidades Java.
* **AutoDDL**: Converte o dicionário de dados XML (gerado pelo AutoDD ou manual) em scripts DDL (CREATE/ALTER) para Oracle/MSSQL.

Essas features são **complementares**: o AutoDD elimina o trabalho manual de criar o XML, e o AutoDDL elimina o trabalho manual de converter o XML em DDL. Para usar o fluxo completo, é necessário habilitar **ambas** as features no `build.gradle` da raiz do projeto:

```groovy
addon {
    autoDD=true
    autoDDL=true
}
```

***

## ✨ Benefícios do AutoDD

* ⚡ **Agilidade**: Não é mais necessário criar XMLs de dicionário de dados manualmente para mapear **entidades**. (views, menus, dashboards e etc... ainda precisam ser mapeados manualmente).
* 🎯 **Menos Erro Humano**: Reduz falhas comuns de digitação e inconsistências de tipos.
* 📏 **Padronização**: Garante que o modelo Java e o dicionário de dados estejam sempre sincronizados.
* 🔄 **Integração Total**: Permite uso imediato do AutoDDL para geração de scripts de banco.

***

## ⚙️ Como Funciona?

1. **Defina sua entidade** usando `@JapeEntity` e anotações de campo (`@Id`, `@Column`, etc.).
2. **Habilite o AutoDD** no `build.gradle` da raiz.
3. **Execute o build** do projeto (ex: `./gradlew clean deployAddon`).
4. O AutoDD processa as entidades e gera automaticamente o XML de dicionário de dados na pasta de build.
5. (Opcional) Se o AutoDDL estiver habilitado, o XML gerado será convertido em scripts SQL DDL para Oracle/MSSQL.

***

## 💡 Exemplo Prático

### 1. Entidade Simples

```java
@Data
@NoArgsConstructor
@JapeEntity(entity = "TST_MinhaClasse", table = "TST_MINHA_CLASSE", description = "Minha Classe Exemplo")
public class MinhaClasse {
    @Id
    @GeneratedValue(strategy = GeneratedValue.GenerationType.AUTO)
    @Column(name = "ID", dataType = DataType.INTEGER, description = "Id")
    private Long id;

    @Column(name = "MSG", dataType = DataType.TEXT, description = "Mensagem")
    private String mensagem;

    @Column(name = "OUTRO_FIELD", dataType = DataType.INTEGER, description = "Outro Campo")
    private Long outroField;

}
```

### 2. Entidades com Relacionamentos

O AutoDD mapeia relacionamentos entre entidades usando `@JoinColumn` (para PK simples) ou `@JoinColumns` (para PK composta).

#### Exemplo: Relacionamento com PK Simples

```java
@Data
@NoArgsConstructor
@JapeEntity(entity = "TST_MinhaClasse", table = "TST_MINHA_CLASSE", description = "Minha Classe Exemplo")
public class MinhaClasse {
    @Id
    @GeneratedValue(strategy = GeneratedValue.GenerationType.AUTO)
    @Column(name = "ID", dataType = DataType.INTEGER, description = "Id")
    private Long id;

    @Column(name = "MSG", dataType = DataType.TEXT, description = "Mensagem")
    private String mensagem;

    @OneToMany(
        cascade = Cascade.ALL,
        orphanRemovalStrategy = OrphanRemovalStrategy.DETACH
    )
    private List<MinhaOutraClasse> itens;
}

@Data
@NoArgsConstructor
@JapeEntity(entity = "TST_MinhaOutraClasse", table = "TST_MINHA_OUTRA_CLASSE", description = "Minha Outra Classe Exemplo")
public class MinhaOutraClasse {
    @Id
    @GeneratedValue(strategy = GeneratedValue.GenerationType.AUTO)
    @Column(name = "ID", dataType = DataType.INTEGER, description = "Id")
    private Long id;

    @Column(name = "STATUS", dataType = DataType.LIST, description = "STATUS",
            options = {
                    @Option(label = "Ativo", value = "ATIVO"),
                    @Option(label = "Inativo", value = "INATIVO")
    })
    private Status status;

    // FK para MinhaClasse
    @ManyToOne(cascade = Cascade.MERGE)
    @JoinColumn(
        name = "MINHA_ENTIDADE_ID",
        referencedColumnName = "ID",
        dataType = DataType.INTEGER,
        description = "Referência para MinhaClasse"
    )
    private MinhaClasse minhaClasse;
}
```

#### Exemplo: Relacionamento com PK Composta

```java
@Embeddable
@Data
@NoArgsConstructor
public class ContratoId implements Serializable {
    @Column(name = "NUMCONTRATO", dataType = DataType.INTEGER, description = "Número do Contrato")
    private Long numContrato;

    @Column(name = "CODEMP", dataType = DataType.INTEGER, description = "Código da Empresa")
    private Long codEmp;
}

@JapeEntity(entity = "TST_Contrato", table = "TST_CONTRATO", description = "Contrato")
@Data
public class Contrato {
    @Id
    private ContratoId id;

    @Column(name = "DESCRICAO", dataType = DataType.TEXT, description = "Descrição")
    private String descricao;
}

@JapeEntity(entity = "TST_Aditivo", table = "TST_ADITIVO", description = "Aditivo de Contrato")
@Data
public class Aditivo {
    @Id
    @Column(name = "NUMADITIVO", dataType = DataType.INTEGER, description = "Número do Aditivo")
    private Long numAditivo;

    // FK composta para Contrato
    @ManyToOne(cascade = Cascade.MERGE)
    @JoinColumns({
        @JoinColumn(
            name = "NUMCONTRATO",
            referencedColumnName = "NUMCONTRATO",
            description = "Número do Contrato"
        ),
        @JoinColumn(
            name = "CODEMP_CONTRATO",
            referencedColumnName = "CODEMP",
            description = "Código da Empresa"
        )
    })
    private Contrato contrato;
}
```

### 3. Tabelas e Instâncias Nativas

É possível mapear uma instância e tabela nativa do Sankhya utilizando os atributos `isNativeTable` e `isNativeInstance` na anotação `@JapeEntity`.

Exemplo:

Podemos criar uma instância customizada na tabela nativa de usuários `TSIUSU`:

```java

@Data
@AllArgsConstructor
@NoArgsConstructor
@JapeEntity(
        entity = "TST_InstanciaCustomizadaUsuarios",
        table = "TSIUSU",
        description = "Instancia Customizada de Usuários",
        isNativeTable = true,
        isNativeInstance = false
)
public class InstanciaCustomizadaUsuarios {

    @Id
    @Column(name = "CODUSU", description = "Cod do Usuario", dataType = DataType.INTEGER)
    private Long codUsuario;

    @Column(name = "NOMUSU", description = "Nome do Usuario", dataType = DataType.TEXT)
    private String nomeUsuario;
}
```

### 4. Campos e relacionamentos com Expressões

É possível também adicionar expressões a campos e relacionamentos.

As expressões são utilizadas para enriquecer ou criar campos calculados.

É possível, por exemplo, utilizar uma expressão para capturar a data-hora atual, o usuário logado e até mesmo executar um script SQL.

Ex:

```java
// Expressão Bean Shell:
@Expression(value = "return $ctx_usuario_logado;", type = Expression.Type.BEAN_SHELL)
@Column(name = "USUARIO_ALTERACAO", description = "Usuario Logado", dataType = DataType.INTEGER)
private Usuario usuarioAlteracao;

// Expressão SQL:
@Expression(value = "SELECT COUNT(1) FROM ALGUMA_TABELA WHERE USUARIO_ALTERACAO_OUTRA_TABELA = USUARIO_ALTERACAO", type = Expression.Type.SQL)
@Column(name = "QTD_ALTERACOES_USUARIO_LOGADO", description = "Qnt Alterações Usuario Logado", calculated = true, dataType = DataType.INTEGER)
private Long qtdAlteracoesUsuario;
```

> É importante ressaltar que não é possível inserir uma instância nativa em uma tabela não nativa, mas o contrário é possível: Uma Tabela Nativa suporta instâncias nativas e não nativas.

<Callout icon="⚠️" theme="warn">
  ### Não adicione CAMPOS em tabelas nativas. Tabelas nativas têm carga elevada, e uma migração durante horário de pico pode derrubar o SankhyaOM. Use uma tabela de extensão com [merge-on-root](16_merge_on_root.md).
</Callout>

***

## Anotações e atributos

### Anotação `@JapeEntity`

Define uma entidade mapeada para o dicionário de dados.

| Atributo         | Descrição                                                    | Obrigatório | Padrão |
| ---------------- | ------------------------------------------------------------ | ----------- | ------ |
| entity           | Nome da entidade no dicionário de dados                      | Sim         | N/A    |
| table            | Nome da tabela no banco de dados                             | Sim         | N/A    |
| isNativeTable    | Se true, gera \<nativeTable> ao invés de \<table>            | Não         | false  |
| isNativeInstance | Indica se é uma instância nativa (requer isNativeTable=true) | Não         | false  |
| description      | Descrição da entidade                                        | Não         | ""     |
| parentInstance   | Instância pai (para herança)                                 | Não         | ""     |
| resourceId       | ID do recurso                                                | Não         | ""     |

### Anotação `@Column`

Define o mapeamento de um campo para uma coluna da tabela.

| Atributo        | Descrição                                | Obrigatório                   | Padrão |
| --------------- | ---------------------------------------- | ----------------------------- | ------ |
| name            | Nome da coluna na tabela                 | Sim                           | N/A    |
| description     | Descrição do campo                       | Obrigatório se autoDDL = true | ""     |
| dataType        | Tipo de dado (DataType enum)             | Obrigatório se autoDDL = true | NONE   |
| documentation   | Documentação adicional do campo          | Não                           | ""     |
| calculated      | Se o campo é calculado                   | Não                           | false  |
| allowSearch     | Permite busca no campo                   | Não                           | false  |
| allowDefault    | Permite valor padrão                     | Não                           | true   |
| visibleOnSearch | Visível na pesquisa                      | Não                           | false  |
| isPresentation  | Se é campo de apresentação               | Não                           | false  |
| nullable        | Se permite valores nulos                 | Não                           | true   |
| visible         | Se o campo é visível                     | Não                           | true   |
| required        | Se o campo é obrigatório                 | Não                           | false  |
| readOnly        | Se o campo é somente leitura             | Não                           | false  |
| order           | Ordem do campo                           | Não                           | 0      |
| size            | Tamanho do campo                         | Não                           | 0      |
| precision       | Precisão (para decimais)                 | Não                           | 0      |
| uiTabName       | Nome da aba na interface                 | Não                           | ""     |
| uiGroupName     | Nome do grupo na interface               | Não                           | ""     |
| targetInstance  | Instância alvo (para relacionamentos)    | Não                           | ""     |
| targetField     | Campo alvo (para relacionamentos)        | Não                           | ""     |
| targetType      | Tipo do alvo (para relacionamentos)      | Não                           | NONE   |
| isNative        | Se é extensão de tabela nativa           | Não                           | false  |
| properties      | Propriedades customizadas (@Property\[]) | Não                           | {}     |
| options         | Opções para campos LISTA (@Option\[])    | Não                           | {}     |

### Anotação `@Expression`

| Atributo | Descrição                       | Obrigatório | Padrão |
| -------- | ------------------------------- | ----------- | ------ |
| value    | A expressão em si.              | Sim         | N/A    |
| type     | Tipos aceitos: Bean Shell e SQL | Sim         | N/A    |

### Anotação `@Id`

Marca um campo como chave primária da entidade. A anotação não possui atributos.

### Anotação `@GeneratedValue`

Define a estratégia de geração da chave primária.

| Atributo | Descrição                                   | Obrigatório | Padrão |
| -------- | ------------------------------------------- | ----------- | ------ |
| strategy | Estratégia de geração (GenerationType enum) | Não         | AUTO   |

**Valores de GenerationType:**

* `AUTO`: Geração automática pelo sistema (sequenceType="A")
* `MANUAL`: Geração manual pela aplicação (sequenceType="M")
* `SEQUENCE`: Geração automática pelo banco de dados. Não pode ser usada em tabelas nativas (sequenceType="M")

**importante:**
`SEQUENCE` Funciona a partir das seguintes versões de banco de dados:

* Funciona para Microsoft SQL Server (MSSQL) a partir da versão 2012 <br />
* Funciona para Oracle a partir da versão 7

### Anotações de Relacionamento

Todas as anotações de relacionamento (`@OneToOne`, `@OneToMany`, `@ManyToOne`) compartilham atributos comuns:

| Atributo   | Descrição                                   | Obrigatório | Padrão |
| ---------- | ------------------------------------------- | ----------- | ------ |
| cascade    | Operações a propagar (Cascade\[] enum)      | Não         | NONE   |
| fetchType  | Estratégia de carregamento (FetchType enum) | Não         | LAZY   |
| expression | Expressão para enriquecer o relacionamento  | Não         | N/A    |

**Atributo exclusivo do&#x20;**`@OneToMany`**:**

| Atributo              | Descrição                       | Obrigatório | Padrão |
| --------------------- | ------------------------------- | ----------- | ------ |
| orphanRemovalStrategy | Estratégia para entidades órfãs | Não         | NONE   |

> **Nota**: Use `@JoinColumn` ou `@JoinColumns` no lado `@ManyToOne`/`@OneToOne` para mapear as colunas FK.

### Anotação `@JoinColumn`

Mapeia uma coluna de chave estrangeira para uma coluna de chave primária.

| Atributo             | Descrição                                | Obrigatório                   | Padrão |
| -------------------- | ---------------------------------------- | ----------------------------- | ------ |
| name                 | Nome da coluna FK na tabela atual        | Sim                           | N/A    |
| referencedColumnName | Nome da coluna PK na tabela referenciada | Sim                           | N/A    |
| description          | Descrição do relacionamento              | Obrigatório se autoDDL = true | ""     |

### Anotação `@JoinColumns`

Agrupa múltiplas `@JoinColumn` para mapear FKs compostas (quando a entidade referenciada tem PK composta).

```java
@JoinColumns({
    @JoinColumn(name = "COL_FK_1", referencedColumnName = "COL_PK_1", description = "..."),
    @JoinColumn(name = "COL_FK_2", referencedColumnName = "COL_PK_2", description = "...")
})
```

### Anotação `@Property`

Define propriedades customizadas para campos.

| Atributo | Descrição  | Obrigatório |
| -------- | ---------- | ----------- |
| name     | Chave/nome | Sim         |
| value    | Valor      | Sim         |

### Anotação `@Option`

Define opções para campos de tipo LIST.

| Atributo | Descrição              | Obrigatório |
| -------- | ---------------------- | ----------- |
| value    | Valor da opção (chave) | Sim         |
| label    | Rótulo exibido         | Sim         |

### Anotação `@IgnoreAutoDD`

Controla seletivamente quais entidades, campos e relacionamentos devem ser ignorados na geração automática do dicionário de dados.

**Aplicação:**

* **Em classes**: Ignora toda a entidade no dicionário de dados
* **Em campos**: Ignora apenas o campo específico
* **Em relacionamentos**: Ignora o campo e o relacionamento

**Principais casos de uso:**

* Mapear entidades que já possuem dicionário de dados em outras soluções (nativas ou de terceiros)
* Evitar duplicação de definições e conflitos durante instalação
* Extender entidades existentes com campos customizados (marcando apenas campos existentes com `@IgnoreAutoDD`)
* Referenciar campos e relacionamentos sem redefinir metadados

**Exemplo - Extendendo entidade existente:**

```java
@JapeEntity(entity = "ParceiroExtendido", table = "TGFPAR")
public class ParceiroExtendido {
    
    // Campo nativo - não incluir no DD
    @Id
    @Column(name = "CODPARC")
    @IgnoreAutoDD
    private BigDecimal codigoParceiro;
    
    // Campo nativo - não incluir no DD
    @Column(name = "NOMEPARC")
    @IgnoreAutoDD
    private String nomeRazaoSocial;
    
    // Campo CUSTOMIZADO - incluir no DD (campo novo do add-on)
    @Column(name = "SGT_SCORING", 
            description = "Score de Crédito do Cliente",
            dataType = DataType.INTEGER)
    private BigDecimal scoringCredito;
}
```

<Callout icon="⚠️" theme="warn">
  ### **Importante:** Sem `@IgnoreAutoDD`, você receberá alertas de conflito durante a instalação ao tentar redefinir estruturas já existentes em outras soluções.
</Callout>

### Enums Importantes

**DataType:**

* `TEXT`, `TEXT_BOX`, `INTEGER`, `DECIMAL`, `DATE`, `DATE_TIME`, `TIME`
* `CHECKBOX`, `LIST`, `SEARCH`, `HTML`, `FILE`, `MULTIPLE_FILES`, `IMAGE`

**Cascade:**

* `ALL`: Permite todas as operações (criar, editar, excluir)
* `NONE`: Não permite nenhuma operação (padrão)
* `CREATE`, `UPDATE`, `DELETE`, `MERGE`: Operações específicas

**FetchType:**

* `LAZY`: Carregamento sob demanda (padrão)

**OrphanRemovalStrategy:**

* `DETACH`: Remove vínculo, mantém registro (seta FK para NULL)
* `NONE`: Não remove órfãos (padrão)

***

## Limitação Conhecida

Atualmente há uma limitação de encoding. O Sankhya trabalha com `ISO-8859-1` para os arquivos de dicionário de dados.
Isso signfica que caracteres especiais (acentos, cedilha, etc.) não são suportados nas descrições e outros campos textuais.

É possível escapar esse caractere especial com o código ASCII correspondente. Exemplo, a palavra `'Código'` poderia ser escrita assim: `'C\u00F3digo'`.

***

## 📋 Boas Práticas

* Use prefixos exclusivos para tabelas e entidades (ex: `SGT_`, `LOG_`).
* Nunca use prefixo `AD_` (reservado do sistema).
* Sempre revise os scripts antes de aplicar em ambientes produtivos.
