---
id: "https://developer.sankhya.com.br/docs/04_tabela_hierarquica"
titulo: "🌳 Tabela Hierárquica (`treeTable`)"
url: "https://developer.sankhya.com.br/docs/04_tabela_hierarquica"
atualizado_em: "2025-11-10T23:35:58.000Z"
---

# 🌳 Tabela Hierárquica (`treeTable`)

Como criar tabelas hierárquicas (com estrutura de árvore) em telas customizadas.

Para cadastros que possuem uma estrutura de árvore (pai/filho), como centros de custo, categorias de produtos ou organogramas, o Add-on Studio oferece a tag `<treeTable>`. Ela gera automaticamente uma interface que permite a navegação e o cadastro em níveis hierárquicos.

***

### 🛠️ Como Criar uma Tabela Hierárquica

A definição é semelhante a uma `<table>` padrão, mas com a tag `<treeTable>`.

#### Exemplo Prático

Vamos criar um cadastro hierárquico de "Centros de Custo".

```xml
<!-- arquivo: src/main/resources/datadictionary/SGT_CENTROCUSTO.xml -->
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
           
    <treeTable name="SGT_CENTROCUSTO" defaultMask="##.##.##">
        <description>Centro de Custo</description>
        <primaryKey>
            <field name="CODCENCUS"/>
        </primaryKey>

        <instances>
            <instance name="SGT_CentroCusto">
                <description>Centro de Custo</description>
            </instance>
        </instances>

        <fields>
            <field name="CODCENCUS" dataType="INTEIRO" required="true" />
            <field name="DESCRCENCUS" dataType="TEXTO" size="100" required="true" />
            <field name="ATIVO" dataType="TEXTO" size="1" required="true" />
        </fields>
    </treeTable>
</metadados>
```

Para que esta tela apareça no menu, basta criar um `<dynamicTreeView>` apontando para a instância `SGT_CentroCusto`, de forma semelhante ao que faria com uma tabela comum.

***

### ⚙️ Atributos da Tag `<treeTable>`

| Atributo      | Descrição                                                              | Exemplo            |
| :------------ | :--------------------------------------------------------------------- | :----------------- |
| `name`        | **Obrigatório**. O nome da tabela que será criada no banco de dados.   | `SGT_CENTROCUSTO`  |
| `defaultMask` | (Opcional) Define uma máscara de formatação para o código hierárquico. | `##.##.##`         |
| `maskName`    | (Opcional) Nome da máscara, caso já exista uma definida no sistema.    | `CENTROCUSTO_MASK` |

***

### ⚠️ Campos Obrigatórios (Auto DDL vs. Manual)

O controle da hierarquia (quem é pai de quem) é feito por campos que o sistema espera que existam na tabela.

#### Com Auto DDL Habilitado

Se você usa o [Auto DDL](https://developer.sankhya.com.br/docs/02_autoddl), o Add-on Studio **cria automaticamente** os seguintes campos para você:

* `CODIGOPAI`: Armazena a chave do registro pai.
* `ANALITICO`: Indica se o registro pode receber lançamentos ('S') ou se é apenas um agrupador ('N').
* `GRAU`: Define o nível do registro na hierarquia (0 para raiz, 1 para filhos, etc).

Você não precisa declará-los no seu XML.

#### Com Auto DDL Desabilitado (dbscript manual)

Se você gerencia o banco de dados manualmente com `dbscript`, seu script de `CREATE TABLE` **deve obrigatoriamente** incluir os campos de controle hierárquico, além dos que você declarou no XML.

**Exemplo de`dbscript` para Oracle:**

```sql
CREATE TABLE SGT_CENTROCUSTO (
    -- Campos declarados no XML
    CODCENCUS NUMBER(10) NOT NULL,
    DESCRCENCUS VARCHAR2(100) NOT NULL,
    ATIVO CHAR(1) NOT NULL,
    
    -- Campos de controle hierárquico (obrigatórios)
    CODIGOPAI NUMBER(10),
    ANALITICO CHAR(1) DEFAULT 'S' NOT NULL,
    
    CONSTRAINT PK_SGT_CENTROCUSTO PRIMARY KEY (CODCENCUS)
);
```

> **Atenção**: A falta desses campos em um `dbscript` manual causará erros em tempo de execução, pois a interface do `treeTable` depende deles para funcionar.

***

### ✨ Boas Práticas

* **Use`defaultMask`** : Definir uma máscara ajuda a manter a consistência visual e estrutural dos códigos hierárquicos.
* **Prefira o Auto DDL**: Para `treeTable`, o Auto DDL simplifica muito o processo, pois gerencia os campos de controle para você.

### 🚫 Anti-Patterns (O que evitar)

* **Esquecer os Campos de Controle no`dbscript`** : Este é o erro mais comum ao usar `treeTable` sem Auto DDL e impede o funcionamento da tela.
* **Usar`treeTable` para Dados Não Hierárquicos**: Se os seus dados não têm uma relação de pai e filho, use uma `<table>` normal. Usar `treeTable` desnecessariamente complica o modelo e a interface.
