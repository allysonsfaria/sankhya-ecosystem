---
id: "https://developer.sankhya.com.br/docs/02_autoddl"
titulo: "📦 Auto DDL: Geração Automática de Tabelas"
url: "https://developer.sankhya.com.br/docs/02_autoddl"
atualizado_em: "2026-09-28T16:20:50.000Z"
---

# 📦 Auto DDL: Geração Automática de Tabelas

Focado na feature `autoddl`, que automatiza a criação e atualização de tabelas no banco de dados com base no `metadados.xml`.

# 📦 Auto DDL: Geração Automática de Tabelas via XML

O recurso **Auto DDL (Data Definition Language)** do Add-on Studio é uma ferramenta poderosa que automatiza a criação e atualização de tabelas no banco de dados. Em vez de escrever scripts SQL manuais, você define suas tabelas em um arquivo XML, e o Add-on Studio cuida do resto.

<Callout icon="📘" theme="info">
  ### **Disponibilidade**: Funcionalidade disponível a partir da versão 2.0 do Add-on Studio.
</Callout>

***

### 🚀 Por que usar o Auto DDL?

* ✅ **Agilidade Extrema**: Crie e modifique seu modelo de dados apenas editando um arquivo XML.
* ✅ **Fonte Única da Verdade**: O XML no seu projeto se torna a definição canônica do seu esquema de banco de dados.
* ✅ **Redução de Erros**: Evita erros manuais e inconsistências entre o dicionário de dados do Sankhya e a estrutura física do banco.
* ✅ **Prototipação Rápida**: Ideal para criar rapidamente a estrutura de banco de dados para novas funcionalidades.
* ✅ **Consistência Garantida**: Mantém o dicionário de dados da plataforma e o banco de dados físico perfeitamente sincronizados.

***

### ⚙️ Como Habilitar

Para ativar o Auto DDL, adicione la propriedade `autoDDL = true` no bloco `addon` do seu arquivo `build.gradle`.

```groovy
// build.gradle
// ...
addon {
    appKey = "SUA_APP_KEY"
    parceiroNome = "SUA_EMPRESA"
    autoDDL = true // Habilita a geração automática de DDL
}
```

<Callout icon="⚠️" theme="warn">
  ### **Atenção**: Ao habilitar o `autoDDL`, você deve remover de seus `dbscripts` todos os comandos `CREATE TABLE` e `ALTER TABLE` que já foram declarados no XML do dicionário de dados. Manter os dois em paralelo pode causar inconsistências e erros durante o deploy.
</Callout>

Com essa configuração, a cada deploy (`./gradlew deployAddon`), o Add-on Studio verificará e aplicará as mudanças do seu XML no banco de dados.

***

### 📄 Estrutura do Dicionário XML

O Auto DDL funciona lendo os arquivo XML definidos no [Dicionario de dados](https://developer.sankhya.com.br/docs/01_dicionario-de-dados) (localizado em `datadictionary/`) que descreve suas tabelas.

**Principais componentes:**

* `<metadados>`: O elemento raiz do documento.
* `<table name="...">`: Define uma nova tabela. O `name` deve seguir o padrão de nomenclatura (ex: `SGT_MINHATABELA`).
* `<primaryKey>`: Define a chave primária da tabela.
* `<fields>`: Agrupa todas as colunas da tabela.
* `<field name="..." dataType="...">`: Define uma coluna.

**Exemplo de&#x20;**`SGT_PROJETOCUSTOM.xml`**:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
           
    <table name="SGT_PROJETOCUSTOM">
        <primaryKey>
            <field>IDPROJ</field>
        </primaryKey>
        <fields>
            <field name="IDPROJ" dataType="INTEIRO" required="true" />
            <field name="NOMEPROJ" dataType="TEXTO" size="100" required="true" />
            <field name="ATIVO" dataType="CHECKBOX" required="true" default="S" />
            <field name="DATA_INICIO" dataType="DATA" />
        </fields>
    </table>
</metadados>
```

#### Tipos de Dados (`dataType`)

O Add-on Studio mapeia os tipos do XML para os tipos de dados SQL apropriados para Oracle e SQL Server.

| Tipo no XML   | Tipo Oracle      | Tipo SQL Server  | Uso Comum                          |
| :------------ | :--------------- | :--------------- | :--------------------------------- |
| `TEXTO`       | `VARCHAR2(size)` | `VARCHAR(size)`  | Nomes, descrições curtas           |
| `INTEIRO`     | `NUMBER`         | `INT`            | Chaves primárias, contadores       |
| `DECIMAL`     | `NUMBER`         | `DECIMAL(p,s)`   | Valores monetários, medidas        |
| `DATA`        | `DATE`           | `DATETIME`       | Datas sem hora                     |
| `DATA_HORA`   | `TIMESTAMP`      | `DATETIME`       | Datas com hora                     |
| `HORA`        | `NUMBER`         | `SMALLINT`       | Somente hora                       |
| `CHECKBOX`    | `CHAR(1)`        | `CHAR(1)`        | Flags (Sim/Não, Ativo/Inativo)     |
| `CAIXA_TEXTO` | `CLOB`           | `TEXT`           | Textos longos, observações         |
| `ARQUIVO`     | `BLOB`           | `VARBINARY(MAX)` | Armazenamento de arquivos binários |

<Callout icon="📘" theme="info">
  ### **Dica**:

  * Campos **TEXTO** com tamanho maior que 100 são convertidos em caixas de texto na interface.
  * Campos **TEXTO** com tamanho maior que 4000 devem ser usados o campo CAIXA_TEXTO, pois o mesmo é convertido para CLOB no banco.
  * Campos **HORA** são armazenados como NUMBER no Oracle e SMALLINT no SQL Server. Durante a leitura, esses valores são automaticamente convertidos para o tipo `java.time.LocalTime` em Java. Por isso, recomendamos utilizar o tipo `LocalTime` em suas entidades para garantir compatibilidade total com o AutoDD e AutoDDL.
</Callout>

***

### ✨ Boas Práticas e Cuidados

O Auto DDL é poderoso, mas deve ser usado com responsabilidade.

* **Ambientes**: É **ideal para desenvolvimento e testes**. Em **produção**, é mais seguro desabilitar o Auto DDL (`autoDDL = false`) e usar scripts de migração controlados por um DBA.
* **Nomenclatura**: **Sempre** use um prefixo único em suas tabelas (ex: `SGT_` ou as iniciais do seu add-on) para evitar conflitos. **Não use o prefixo&#x20;**`AD_`.
* **Controle de Versão**: Seu arquivo XML deve ser versionado no Git. Ele é a "fonte da verdade" do seu esquema.

### 🚫 O que o Auto DDL NÃO Faz (Limitações Importantes)

* **Operações Destrutivas**: O Auto DDL **não executa&#x20;**`DROP TABLE`**&#x20;ou&#x20;**`DROP COLUMN`. Se você remover uma tabela ou campo do XML, terá que removê-lo manualmente do banco de dados. Isso é uma medida de segurança para evitar perda de dados acidental.
* **Renomear Colunas/Tabelas**: Renomear uma coluna no XML resultará na criação de uma **nova coluna**. A antiga permanecerá no banco. Migrações de renomeação devem ser feitas com scripts manuais.
* **Alterar Tipos de Dados com Risco**: Mudar um tipo de dado de `TEXTO` para `INTEIRO`, por exemplo, não é suportado e pode causar erros.
* **Índices e Constraints**: Índices, chaves estrangeiras (`foreign keys`) e outras constraints (além de `PRIMARY KEY` e `NOT NULL`) não são gerenciados pelo Auto DDL. Eles devem ser criados via `dbscript`.

***

### 🔄 Migrando um Projeto Existente para Auto DDL

Se seu projeto já tem tabelas criadas com `dbscript`, siga estes passos para migrar:

1. **Crie o XML**: Defina suas tabelas existentes no arquivo XML do dicionário de dados.
2. **Remova o DDL Antigo**: Exclua os `CREATE TABLE` e `ALTER TABLE` correspondentes dos seus arquivos `dbscript`. Mantenha apenas scripts de `CREATE INDEX`, `constraints`, etc.
3. **Habilite o Auto DDL**: Adicione `autoDDL = true` ao seu `build.gradle`.
4. **Faça o Deploy**: Execute `./gradlew clean deployAddon`.
5. **Verifique e Teste**: Confirme que nenhuma mudança inesperada ocorreu no banco e que sua aplicação continua funcionando perfeitamente.
