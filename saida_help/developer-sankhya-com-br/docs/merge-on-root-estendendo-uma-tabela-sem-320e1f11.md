---
id: "https://developer.sankhya.com.br/docs/merge-on-root-estendendo-uma-tabela-sem-adicionar-campos-nela"
titulo: "🧩 Merge-on-root: estendendo uma tabela sem adicionar campos nela"
url: "https://developer.sankhya.com.br/docs/merge-on-root-estendendo-uma-tabela-sem-adicionar-campos-nela"
atualizado_em: "2026-09-28T16:17:10.000Z"
---

# 🧩 Merge-on-root: estendendo uma tabela sem adicionar campos nela

O merge-on-root estende uma entidade com os campos de outra tabela, sem criar nenhuma coluna na tabela estendida. Os campos ficam numa tabela de extensão ligada à entidade raiz por um relacionamento 1:1, e a plataforma funde as duas: na tela e no registro, para o usuário, é uma entidade só.  O mecanismo é genérico: funciona para tabelas do seu add-on e para tabelas nativas do SankhyaOM.

***

## 🏛️ Mecanismo oficial para extensão de tabelas nativas

O merge-on-root é o caminho oficial para acrescentar informações a uma entidade nativa (Parceiro, Produto, Nota...). **Não adicione campos em tabelas nativas** — nem por `<nativeTable>` com `<field>`, nem por `ALTER TABLE` em `dbscripts`:

* tabelas nativas têm volume e carga altíssimos, e uma migração em horário de pico pode derrubar o SankhyaOM do seu cliente.
* a alteração pode ser perdida numa atualização da plataforma e invalida o suporte.

Com merge-on-root, a tabela nativa não é alterada: os campos novos vivem na sua tabela de extensão e aparecem na tela nativa como se fossem dela.

***

## ⚙️ Como funciona

1. **Tabela de extensão:** uma tabela sua, com a **mesma chave primária** da entidade raiz, contendo os campos novos.
2. **Relacionamento 1:1:** na entidade raiz, um `@OneToOne` para a tabela de extensão com a expressão `@ref-param[merge-on-root=true]`.
3. **Fusão:** a plataforma exibe e grava os campos da extensão junto com a entidade raiz.

***

## 🚀 Exemplo: estendendo o cadastro de Parceiros (`TGFPAR`)

### 1. A tabela de extensão

Mesma chave primária da raiz (`CODPARC`) e os campos novos:

```java
@JapeEntity(
    entity = "CNX_IntegracaoParceiro",
    table = "CNX_INTEGRACAO_PARCEIRO",
    description = "Integracao de Pedidos por Parceiro"
)
@Data
@NoArgsConstructor
public class IntegracaoParceiro {

    @Id
    @Column(name = "CODPARC", description = "Codigo do Parceiro", dataType = DataType.INTEGER)
    private BigDecimal codigoParceiro;

    @Column(uiTabName = "Integracao", name = "INTEGRACAOATIVA",
            description = "Integracao Ativa", dataType = DataType.CHECKBOX, order = 1)
    private boolean integracaoAtiva;

    @Column(uiTabName = "Integracao", name = "DHULTIMPORT",
            description = "Ultima Importacao", dataType = DataType.DATE_TIME,
            readOnly = true, order = 2)
    private LocalDateTime dataUltimaImportacao;
}
```

### 2. A entidade raiz com o relacionamento 1:1

Aqui a raiz é a instância nativa `Parceiro`. Para estender uma tabela do seu add-on, o relacionamento é o mesmo, sem `isNativeTable`/`isNativeInstance`.

```java
@JapeEntity(
    entity = "Parceiro",
    table = "TGFPAR",
    isNativeTable = true,
    isNativeInstance = true,
    description = "Parceiro"
)
@Data
@NoArgsConstructor
public class Parceiro {

    @Id
    @IgnoreAutoDD
    @Column(name = "CODPARC", dataType = DataType.INTEGER)
    private BigDecimal codigo;

    @IgnoreAutoDD
    @Column(name = "NOMEPARC", dataType = DataType.TEXT)
    private String nome;

    @OneToOne(
        cascade = { Cascade.CREATE, Cascade.UPDATE, Cascade.MERGE },
        expression = @Expression(
            value = "@ref-param[merge-on-root=true]",
            type = Expression.Type.BEAN_SHELL
        )
    )
    @JoinColumn(name = "CODPARC", referencedColumnName = "CODPARC",
                description = "Codigo do Parceiro", dataType = DataType.INTEGER)
    @ToString.Exclude
    private IntegracaoParceiro integracao;
}
```

Os campos de `CNX_INTEGRACAO_PARCEIRO` aparecem dentro da tela de Parceiros, na aba `Integracao`.

***

## ⚠️ Cuidados

* **Mesma chave primária.** A PK da tabela de extensão é a PK da entidade raiz. É isso que torna o 1:1 possível.
* **Não use&#x20;**`Cascade.ALL`**.** Com `DELETE`, a relação passa a ser obrigatória, e uma relação 1:1 obrigatória não é exibida na tela enquanto o registro ainda não tem linha na extensão. Use `CREATE`, `UPDATE` e `MERGE`.
* **Raiz nativa:&#x20;**`@IgnoreAutoDD`**&#x20;em todos os campos, exceto no relacionamento de merge-on-root.** Sem isso, cada `@Column` vira uma coluna nova na tabela nativa. Não coloque `@IgnoreAutoDD` na classe: ele remove a entidade inteira do dicionário, e o merge-on-root some junto.
* **Só 1:1.** Um `@OneToMany` não se funde na entidade raiz: ele aparece como uma aba separada na tela.
