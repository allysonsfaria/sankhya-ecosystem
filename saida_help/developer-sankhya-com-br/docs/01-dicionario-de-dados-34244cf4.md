---
id: "https://developer.sankhya.com.br/docs/01_dicionario-de-dados"
titulo: "📂 Dicionário de Dados (Data Dictionary)"
url: "https://developer.sankhya.com.br/docs/01_dicionario-de-dados"
atualizado_em: "2026-09-28T16:20:11.000Z"
---

# 📂 Dicionário de Dados (Data Dictionary)

Explica como definir a estrutura de dados (tabelas, campos, entidades) do add-on usando o arquivo `metadados.xml`.

> Conheça o novo mecanismo de Mapeamento de Instâncias/Entidades no Dicionário de Dados.
>
> Leia a documentação de <Anchor target="_blank" href="../11_sdk_sankhya/12_auto_dd.md">AutoDD</Anchor> e de <Anchor target="_blank" href="../11_sdk_sankhya/08_relational_mapping.md">ORM</Anchor>.

<br />

O **Dicionário de Dados** é o coração do seu add-on. É onde você define a estrutura de dados da sua aplicação — tabelas, telas, menus e extensões de entidades nativas — de forma declarativa usando arquivos XML.

Este mecanismo garante que suas personalizações sejam armazenadas e manipuladas de maneira estruturada, segura e padronizada dentro do ecossistema Sankhya.

***

### 🗂️ Estrutura de Arquivos

Todos os arquivos do Dicionário de Dados devem ser criados dentro do diretório `datadictionary`, localizado em `model/src/main/resources/`.

![Estrutura de pastas do Dicionário de Dados](https://files.readme.io/3d313449acc070e930d6eec0b2142e6f13ef8e333e84003729dc96cb28b8c0d6-Screenshot_3.png)

> **💡 Boa Prática:** Crie um arquivo XML separado para cada entidade principal (uma tabela, um menu, etc.). Isso torna a manutenção muito mais simples. Por exemplo, `SGT_MINHATABELA.xml`, `SGT_MEUMENU.xml`.

***

### 📄 Arquivo XML Base e o `metadados.xsd`

Todo arquivo de dicionário de dados deve seguir uma estrutura XML padrão que referencia o `metadados.xsd`. Este XSD (XML Schema Definition) é crucial, pois permite que sua IDE valide o arquivo e ofereça autocompletar, guiando o desenvolvimento.

**Estrutura inicial:**

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
           
    <!-- Suas definições de tabelas, menus, etc., vêm aqui -->

</metadados>
```

<Callout icon="👍" theme="okay">
  ### **IntelliSense na IDE**: Com essa configuração, sua IDE (como o IntelliJ) fornecerá sugestões e documentação ao escrever o XML, bastando passar o mouse sobre as tags e atributos definidos no `metadados.xsd`.
</Callout>

***

### 🏛️ Estruturas de Dados Suportadas

Dentro da tag `<metadados>`, você pode definir diversas estruturas, conforme o `metadados.xsd`.

| Estrutura                 | Tag XML           | Descrição                                                           |
| :------------------------ | :---------------- | :------------------------------------------------------------------ |
| **Tabelas Novas**         | `<table />`       | Define novas tabelas que serão criadas no banco de dados.           |
| **Tabelas Hierárquicas**  | `<treeTable />`   | Define tabelas com estrutura de árvore (pai/filho).                 |
| **Views**                 | `<view />`        | Cria views de banco de dados.                                       |
| **Formulários Dinâmicos** | `<dynamicForm />` | Cria telas de cadastro (formulários) baseadas em suas tabelas.      |
| **Menus**                 | `<menu />`        | Adiciona novas entradas de menu no sistema para acessar suas telas. |
| **Telas (Custom UI)**     | `<ui />`          | Registra telas personalizadas (feitas em XHTML/JSF) no menu.        |
| **Filtros**               | `<filters />`     | Adiciona uma seção de filtros a um formulário dinâmico.             |

<Callout icon="⚠️" theme="warn">
  ### **Deprecated: campos em&#x20;**`<nativeTable />`**.** Não adicione campos em tabelas nativas. Para guardar informações extras de uma entidade nativa, use uma tabela de extensão com [merge-on-root](../11_sdk_sankhya/16_merge_on_root.md).
</Callout>

***

### 🧩 Merge-on-root via XML

O merge-on-root estende uma entidade com os campos de outra tabela, sem criar colunas na tabela estendida. Na instância da entidade raiz, declare um relacionamento 1:1 com a expressão `@ref-param[merge-on-root=true]` para a **tabela de extensão**: uma `<table />` comum com a mesma chave primária da raiz. A plataforma funde as duas, e na tela e no registro é uma entidade só.

<Callout icon="⚠️" theme="warn">
  ### **Tabelas nativas:** não adicione campos customizados em uma tabela nativa. Utilize este mecanismo.
</Callout>

Exemplo: a instância nativa `Parceiro` (`TGFPAR`) estendida pela tabela `CNX_INTEGRACAO_PARCEIRO` (entidade `CNX_IntegracaoParceiro`), ligadas por `CODPARC`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
    <nativeTable name="TGFPAR">
        <instances>
            <nativeInstance name="Parceiro">
                <relationShip>
                    <relation entityName="CNX_IntegracaoParceiro" insert="S" update="S" relation="OneToOne" removeCascade="N">
                        <expression>@ref-param[merge-on-root=true]</expression>
                        <fields>
                            <field localName="CODPARC" targetName="CODPARC"/>
                        </fields>
                    </relation>
                </relationShip>
            </nativeInstance>
        </instances>
    </nativeTable>
</metadados>
```

O mesmo resultado com `@JapeEntity` está em [Merge-on-root](../11_sdk_sankhya/16_merge_on_root.md).

***

### ✨ Boas Práticas

* **Nomenclatura com Prefixo Único**: Use um prefixo exclusivo para suas tabelas e campos (ex: `SGT_` para o add-on "Super Gestão") para evitar conflitos com as tabelas nativas e de outros add-ons.
* **Organização**: Separe as definições em arquivos lógicos. Exemplo: um arquivo para a tabela `SGT_PRODUTOEXTRA`, outro para o menu `menu.xml`.
* **Validação Contínua**: Confie no XSD. Se a IDE apontar um erro no seu XML, corrija-o antes de tentar fazer o deploy.

### 🚫 Anti-Patterns (O que evitar)

* **Uso do Prefixo&#x20;**`AD_`: **Não use o prefixo&#x20;**`AD_`. Ele é utilizado internamente pelo SankhyaOm para campos e tabelas adicionai criados via contrutor de Telas e Dicionário de dados.
* **"Monolito" XML**: Colocar todas as definições (tabelas, menus, telas) em um único arquivo gigante. Isso dificulta a leitura, a manutenção e o trabalho em equipe.
* **Adicionar Campos em Tabelas Nativas**: Não use `<nativeTable />` para criar campos numa tabela nativa (ex: `TGFPAR`). Isso exige migração numa tabela de alta carga, o que pode derrubar o SankhyaOM. Crie uma tabela de extensão (ex: `SGT_INFOPARCEXTRA`) com a mesma chave primária e ligue-a à entidade nativa com [merge-on-root](../11_sdk_sankhya/16_merge_on_root.md).
* **Ignorar o XSD**: Escrever o XML "no bloco de notas" sem a ajuda do `metadados.xsd` é uma receita para erros de sintaxe e estrutura que só serão descobertos em tempo de deploy.
