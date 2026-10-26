---
id: "https://developer.sankhya.com.br/docs/03_parameter"
titulo: "📦 Parâmetros Embarcados no Add-on"
url: "https://developer.sankhya.com.br/docs/03_parameter"
atualizado_em: "2025-11-10T23:36:18.000Z"
---

# 📦 Parâmetros Embarcados no Add-on

Como criar parâmetros de sistema configuráveis para o add-on.

Os **parâmetros** são uma forma poderosa de tornar seu add-on flexível, permitindo que os usuários ajustem o comportamento do sistema sem precisar de alterações no código-fonte. Com o Add-on Studio, você pode embarcar parâmetros diretamente na sua solução.

Este guia mostra como criar e configurar parâmetros usando o arquivo `parameter.xml`.

***

### 📂 Onde Criar os Parâmetros?

Os parâmetros do seu add-on são definidos no arquivo `parameter.xml`, localizado em:

```
model/src/main/resources/META-INF/parameter.xml
```

***

### ✍️ Como Definir um Parâmetro

Você pode adicionar quantos parâmetros precisar dentro da tag `<parameters>`. Cada parâmetro é definido por uma tag `<parameter>` com seus respectivos atributos.

**Exemplo de`parameter.xml`:**

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE parameters >
<parameters group-name="mge.:name" 
            data-source="br.com.sankhya.modelcore.util.MGECoreParameter" 
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:noNamespaceSchemaLocation="../../../../../.gradle/parameters.xsd">

    <!-- Exemplo de parâmetro para máscara de hierarquia -->
    <parameter 
        name="addon.mascara.MASKHIERARC" 
        key="MASKHIERARC" 
        type="string" 
        default="##\.##\.##" 
        cacheable="true" 
        required="false" 
        module="B" 
        description="Define a máscara para o cadastro de hierarquias."/>
    
</parameters>
```

#### Atributos da Tag `<parameter>`

Cada atributo tem um papel importante na configuração do seu parâmetro.

| Atributo      | Descrição                                                                                               | Exemplo                     |
| :------------ | :------------------------------------------------------------------------------------------------------ | :-------------------------- |
| `name`        | Identificador único do parâmetro no sistema. É usado para referenciá-lo no código.                      | `addon.mascara.MASKHIERARC` |
| `key`         | Chave do parâmetro que aparece na tela de **Preferências** do Sankhya. **Máximo de 15 caracteres**.     | `MASKHIERARC`               |
| `type`        | Tipo de dado do parâmetro. Valores possíveis: `string`, `number`, `date`, `list`, `boolean`, `integer`. | `string`                    |
| `default`     | Valor padrão que será adotado.                                                                          | `##\.##\.##`                |
| `cacheable`   | Define se o valor do parâmetro deve ser armazenado em cache para melhorar a performance.                | `true`                      |
| `required`    | Indica se o parâmetro é obrigatório. Se `true`, um valor `default` deve ser fornecido.                  | `false`                     |
| `module`      | Módulo do Sankhya ao qual o parâmetro está associado (ex: `C` para Contabilidade, `E` para Comercial).  | `B` (Configuração)          |
| `description` | Descrição que será exibida na tela de **Preferências**. **Máximo de 50 caracteres**.                    | `Define a máscara...`       |

> **💡 Dica da IDE**: No IntelliJ, ao passar o mouse sobre um atributo no `parameter.xml`, a IDE exibirá uma documentação útil sobre ele, graças ao `parameters.xsd` referenciado no arquivo.

***

### 🚀 Deploy e Validação

1. **Faça o Deploy**: Após definir seus parâmetros, execute o comando de deploy no terminal da sua IDE:
   ```shell
   ./gradlew clean deployAddon
   ```

2. **Valide no Sankhya**:
   * Acesse seu ambiente Sankhya local.
   * Vá para a tela de **Preferências**.
   * Procure pelo seu parâmetro usando a `key` ou a `description` que você definiu.

![Parâmetro na tela de Preferências](https://files.readme.io/ecc55b8f0f52dd24d9155e68ff95c4622ce9dc0ca36b6d92b465f5e8306e0165-Screenshot_4.png)

> ⚠️ **Importante**: Após o deploy, o parâmetro é criado apenas na interface. Ele só é persistido na tabela `TSIPAR`, caso o usuário decida **alterar e salvar o valor dele manualmente** pelo menos uma vez, caso contrário o valor default é carregado da memória.

***

### ✨ Boas Práticas

* **Nomenclatura Consistente**: Use um prefixo para os seus parâmetros (`name` e `key`) para evitar conflitos com os parâmetros nativos do Sankhya ou de outros add-ons. Ex: `MEUADDON_NOME_PARAM`.
* **Descrições Claras**: Escreva descrições que ajudem o usuário a entender o que o parâmetro faz, sem precisar consultar a documentação.
* **Use`cacheable="true"`** : Para parâmetros que são lidos com frequência e não mudam a todo momento, usar o cache melhora significativamente a performance.
* **Valores Padrão Seguros**: Defina valores padrão que façam sentido e não quebrem o sistema se o usuário não configurar o parâmetro.

### 🚫 Anti-Patterns (O que evitar)

* **Chaves Genéricas**: Usar `key` como `PARAM1` ou `TESTE` é uma má prática. Seja específico.
* **Descrições Vagas**: Uma `description` como "Parâmetro do add-on" não ajuda em nada.
* **Abusar de Parâmetros**: Nem tudo precisa ser um parâmetro. Se uma configuração é muito técnica ou raramente muda, talvez ela deva ser um valor fixo no código.
* **Esquecer de Persistir o Valor**: Não se esqueça de que o parâmetro só é salvo no banco após a primeira alteração manual. Se sua lógica depende dele, instrua o usuário a configurá-lo.
