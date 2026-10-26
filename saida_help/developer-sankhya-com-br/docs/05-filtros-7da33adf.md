---
id: "https://developer.sankhya.com.br/docs/05_filtros"
titulo: "🔍 Criando Filtros para Formulários"
url: "https://developer.sankhya.com.br/docs/05_filtros"
atualizado_em: "2025-11-10T23:35:59.000Z"
---

# 🔍 Criando Filtros para Formulários

Como adicionar filtros customizados em formulários dinâmicos.

Os filtros permitem que os usuários pesquisem e encontrem dados de forma rápida e eficiente nos formulários dinâmicos. Você pode adicionar uma seção de filtros diretamente na definição da sua tabela no dicionário de dados, e o Add-on Studio se encarregará de renderizá-la na tela.

***

### 🛠️ Como Adicionar Filtros

Para adicionar filtros, utilize a tag `<filters>` dentro da sua definição de `<table>`.

#### Exemplo Prático

Vamos estender a tabela `SGT_TBTESTE` do nosso exemplo anterior para incluir uma seção de filtros.

```xml
<!-- arquivo: src/main/resources/datadictionary/SGT_TBTESTE.xml -->
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
           
    <table name="SGT_TBTESTE">
        <description>Tabela de Atendimentos do Add-on</description>
        <primaryKey>
            <field name="CODIGO"/>
        </primaryKey>
        
        <instances>
            <instance name="SGT_Teste">
                <description>Atendimento</description>
            </instance>
        </instances>
        
        <fields>
            <field name="CODIGO" dataType="INTEIRO" required="true" />
            <field name="DESCRICAO" dataType="TEXTO" size="100" required="true" />
            <field name="CODUSU" dataType="PESQUISA" targetInstance="Usuario" targetField="CODUSU" targetType="INTEIRO" />
            <field name="DATA_CRIACAO" dataType="DATA_HORA" readOnly="true" />
        </fields>

        <!-- Seção de Filtros -->
        <filters>
            <filter field="CODIGO" />
            <filter field="DESCRICAO" useLikeExpression="true" />
            <filter field="CODUSU" label="Usuário Responsável" />
            <filter field="DATA_CRIACAO" type="PERIODO" label="Período de Criação" />
        </filters>
    </table>
</metadados>
```

Após o deploy, o formulário dinâmico "Cadastro de Atendimentos" exibirá automaticamente os campos de filtro acima da grade de resultados.

***

### ⚙️ Atributos da Tag `<filter>`

A tag `<filter>` possui atributos que personalizam o comportamento do campo de filtro.

| Atributo            | Descrição                                                                                        | Exemplo               |
| :------------------ | :----------------------------------------------------------------------------------------------- | :-------------------- |
| `field`             | **Obrigatório**. O nome do campo da tabela que será usado para filtrar.                          | `CODUSU`              |
| `label`             | (Opcional) O texto que aparecerá para o usuário. Se omitido, usa a descrição do campo.           | `Usuário Responsável` |
| `type`              | (Opcional) O tipo de componente de filtro a ser renderizado. O padrão é `PADRAO`.                | `PERIODO`             |
| `useLikeExpression` | (Opcional) Se `true`, a busca em campos de texto usará `LIKE '%valor%'`. Padrão é `false`.       | `true`                |
| `required`          | (Opcional) Se `true`, o filtro deve ser preenchido para executar a busca. Padrão é `false`.      | `true`                |
| `keepLast`          | (Opcional) Se `true`, o sistema memoriza o último valor utilizado neste filtro. Padrão é `true`. | `false`               |

**Tipos de Filtro (`type`):**

* `PADRAO`: Um campo de texto simples ou pesquisa, dependendo do `dataType` do campo.
* `PERIODO`: Renderiza dois campos de data ("De" e "Até") para filtrar um intervalo. Ideal para campos `DATA` ou `DATA_HORA`.
* `MULTI_SELECAO`: Permite selecionar múltiplos valores para o filtro (não aplicável a todos os tipos de campo).

***

### ✨ Boas Práticas

* **Filtros Relevantes**: Adicione filtros para os campos que os usuários mais usarão para encontrar informações, como códigos, descrições e datas.
* **Use`useLikeExpression`** : Para campos de texto livre como "Nome" ou "Descrição", habilitar `useLikeExpression="true"` melhora muito a usabilidade da busca.
* **Use o Tipo`PERIODO`** : Para campos de data, o tipo `PERIODO` é muito mais intuitivo para o usuário do que um campo de data único.
* **Crie Índices para Filtros Críticos**: Para campos frequentemente usados em filtros de tabelas grandes, crie um índice via `dbscript` para otimizar a performance das buscas.

### 🚫 Anti-Patterns (O que evitar)

* **Filtros em Excesso**: Adicionar um filtro para cada campo da tabela polui a interface e pode confundir o usuário. Seja seletivo.
* **Índices em Excesso**: Criar índices para todos os campos filtráveis é um erro. Cada índice consome espaço e degrada a performance de escrita (INSERT, UPDATE, DELETE). Analise e crie índices apenas onde o ganho na consulta justifica o custo.
* **Filtro em Campo Errado**: Criar um filtro para um campo que não faz sentido para busca, como um campo de controle interno ou um booleano raramente usado.
* **Não Usar`label`** : Deixar o filtro com o nome da coluna do banco (ex: `CODUSU`) em vez de um `label` amigável (ex: "Usuário Responsável") prejudica a experiência do usuário.
